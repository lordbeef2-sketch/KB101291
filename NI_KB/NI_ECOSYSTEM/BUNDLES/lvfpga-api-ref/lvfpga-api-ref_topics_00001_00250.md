# NI DOCUMENT BUNDLE: lvfpga-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvfpga-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/advanced-code-generation-page-fpga-i-o-properties-dialog-box.html language=enus -->
## TOPIC 00001: Advanced Code Generation Page (FPGA I/O Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/advanced-code-generation-page-fpga-i-o-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/advanced-code-generation-page-fpga-i-o-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Advanced Code Generation in the Category list of the FPGA I/O Properties dialog box to display this page. Use this page to select code generation options, such as arbitration and the number of synchronizing registers. You also can specify certain I/O options in the FPGA I/O Node Properties di

### Advanced Code Generation Page (FPGA I/O Properties Dialog Box)

Select **Advanced Code Generation** in the **Category** list of the [FPGA I/O Properties](/csh?context=lvfpga_lvfpgadialog_fpga_io_properties) dialog box to display this page.

Use this page to select code generation options, such as [arbitration](/csh?context=lvfpga_lvfpgaconcepts_fpgaarbintro) and the number of synchronizing registers. You also can specify certain I/O options in the [FPGA I/O Node Properties](/csh?context=lvfpga_lvfpgadialog_fpga_io_node_properties) dialog box. Supported options, values, and defaults vary according to FPGA target and FPGA I/O. This page displays only the options and values supported by the selected FPGA I/O. Some FPGA targets might not allow access to this page at all.

This page can contain the following options:

| Option | Description |  |
| --- | --- | --- |
| ArbitrationForInputData | Specifies the type of arbitration the resource uses for input data. This option typically applies to FPGA I/O items where input requires multiple clock cycles.This option can include Always Arbitrate, Arbitrate if Multiple Requestors Only, and Never Arbitrate. |  |
| ArbitrationForOutputData | Specifies the type of arbitration the resource uses for output data.This option can include Always Arbitrate, Arbitrate if Multiple Requestors Only, and Never Arbitrate. |  |
| ArbitrationForOutputEnable | Specifies the type of arbitration the resource uses for output enable.This option appears for FPGA I/O with output enable, such as bidirectional digital I/O. This option can include Always Arbitrate, Arbitrate if Multiple Requestors Only, and Never Arbitrate. |  |
| NumberOfSyncRegistersForOutputData | Specifies the number of synchronizing registers between the FPGA I/O function executing on the FPGA target and the FPGA target hardware interface. The FPGA target hardware interface might be a physical I/O connector on the device or a connection to a section of the FPGA that contains circuitry designed by NI. Note To ensure consistent timing, use the same number of synchronization registers for output data and output enable. Each synchronization register executes in one clock cycle. Caution Select 0 only if you also use component-level IP (CLIP) and the HDL code contains its own synchronization registers. Supported options typically include the following: 0—Specifies that the FPGA VI uses no synchronization registers. Do not select this option for most FPGA Module applications. Note If you select 0 for digital input and digital output resources in a single-cycle Timed Loop, you create a combinatorial circuit between the two resources. The combinatorial circuit might cause glitches on the output signal. 1—Specifies that the FPGA VI uses one synchronizing register between the FPGA I/O resource and the FPGA target hardware interface. |  |
| NumberOfSyncRegistersForOutputEnable | Specifies the number of synchronizing registers between the FPGA I/O Node executing on the FPGA target and the FPGA target hardware interface. Note To ensure consistent timing, use the same number of synchronization registers for output data and output enable. This option appears for FPGA I/O with the Set Output Enable method available, such as bidirectional digital I/O. Each synchronization register executes in one clock cycle. Caution Select 0 only if you also use component-level IP (CLIP) and the HDL code contains its own synchronization registers. Supported options typically include the following: 0—Specifies that the FPGA VI uses no synchronization registers. Do not select this option for most FPGA Module applications. Note If you select 0 for digital input and digital output resources in a single-cycle Timed Loop, you create a combinatorial circuit between the two resources. The combinatorial circuit might cause glitches on the output signal. 1—Specifies that the FPGA VI uses one synchronizing register between the FPGA I/O resource and the FPGA target hardware interface. |  |
| NumberOfSyncRegistersForRead | Specifies the number of synchronizing registers between the FPGA target hardware interface and the FPGA I/O executing on the FPGA target. The FPGA target hardware interface might be a physical I/O connector on the device or a connection to a section of the FPGA that contains circuitry designed by NI. Each synchronizing register executes in one clock cycle. If you use the FPGA I/O item outside a single-cycle Timed Loop, LabVIEW places one additional synchronizing register, or holding register, that attempts to hold the digital value constant for subsequent operations in the FPGA VI. These synchronizing registers are in addition to enable chain registers that are present outside of the single-cycle Timed Loop. If you use the FPGA I/O item inside a single-cycle Timed Loop, LabVIEW does not add the additional register because logic inside a single-cycle Timed Loop executes every clock cycle. However, you must use caution when synchronizing I/O in single-cycle Timed Loops. Caution Select 0 only if you also use component-level IP (CLIP) and the HDL code contains its own synchronization registers. Otherwise, you might introduce metastable data in the FPGA VI and experience unpredictable behavior. Supported options typically include the following: Auto—Specifies that LabVIEW uses the default number of synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. The following table lists the number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 2 0 Outside an SCTL 1 1 0—Specifies that LabVIEW does not place any synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. Do not select this option for most FPGA Module applications. Note If you select 0 for digital input and digital output resources in a single-cycle Timed Loop, you create a combinatorial circuit between the two resources. The combinatorial circuit might cause glitches on the output signal. The following table lists the total number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 0 0 Outside an SCTL 1 1 1—Specifies that LabVIEW place one synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. Note You might encounter metastable data if the FPGA I/O Node is in a single-cycle Timed Loop and set with this option when the data is not already synchronized to the clock of the single-cycle Timed Loop. The following table lists the total number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 1 0 Outside an SCTL 2 1 2—Specifies that LabVIEW place two synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. Select this option to avoid metastability if the value of the input to the FPGA I/O Node read element might change while the FPGA I/O Node samples the FPGA target hardware interface. If you select this option for an FPGA I/O Node within a single-cycle Timed Loop, you have no metastable data in the FPGA VI. The following table lists the total number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 2 0 Outside an SCTL 3 1 |  |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 2 | 0 |
| Outside an SCTL | 1 | 1 |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 0 | 0 |
| Outside an SCTL | 1 | 1 |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 1 | 0 |
| Outside an SCTL | 2 | 1 |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 2 | 0 |
| Outside an SCTL | 3 | 1 |

Note

Advanced Code Generation FPGA I/O Node Properties

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/compilation-properties-dialog-box.html language=enus -->
## TOPIC 00002: Compilation Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/compilation-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/compilation-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: From the Project Explorer window, right-click Build Specifications and select New»Compilation from the shortcut menu to display this dialog box. You also can right-click a build specification name under Build Specifications and select Properties from the shortcut menu, or double-click the build spec

### Compilation Properties Dialog Box

From the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Build Specifications** and select **New»Compilation** from the shortcut menu to display this dialog box. You also can right-click a build specification name under **Build Specifications** and select **Properties** from the shortcut menu, or double-click the build specification name to display this dialog box.

Use this dialog box to access and configure settings for an FPGA compilation.

This dialog box includes the following pages, which you use to configure the settings for the compilation:

- Information
- Source Files
- Xilinx Options

The bottom of the **Compilation Properties** dialog box includes the following buttons:

| Option | Description |
| --- | --- |
| Build | Updates the LabVIEW project with the build specification settings, closes the dialog box, and builds the build specification with the current settings.Clicking the Build button does not save the settings to disk. You must save the project in order to save these build specification settings. |
| OK | Accepts the current configuration and closes the dialog box. |
| Cancel | Closes the dialog box without accepting the current configuration. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/component-level-ip-properties-dialog-box.html language=enus -->
## TOPIC 00003: Component-Level IP Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/component-level-ip-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/component-level-ip-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target in the Project Explorer window and select New»Component-Level IP to display this dialog box. You also can right-click an existing CLIP item and select Properties from the shortcut menu to display this dialog box. Use this dialog box to create or modify a component-level IP

### Component-Level IP Properties Dialog Box

Right-click an FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **New»Component-Level IP** to display this dialog box. You also can right-click an existing CLIP item and select **Properties** from the shortcut menu to display this dialog box.

Use this dialog box to create or modify a [component-level IP (CLIP)](/csh?context=lvfpga_lvfpgaconcepts_using_component_ip) item under a target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window.

Note

Component-Level IP

This dialog box includes following pages:

- General
- Clock Selections
- Generics
- Terminals

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/configure-3-phase-phase-locked-loop-3-phase-pll.html language=enus -->
## TOPIC 00004: Configure 3-Phase Phase-Locked Loop [3-Phase PLL]

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/configure-3-phase-phase-locked-loop-3-phase-pll.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/configure-3-phase-phase-locked-loop-3-phase-pll.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Control VIs. Tracks the phase and frequency of a 3-Phase signal. The output phase of the 3-Phase Phase-Locked Loop is in pi radians. This operation is useful for FPGA control applications of a 3-phase system. To define the Input mode, double-click this Express VI and use the Input mo

### Configure 3-Phase Phase-Locked Loop [3-Phase PLL]

**Owning Palette:**[Control VIs](../targets/ni/fpga/menus/fpgacategories/programming/control-mnu.html).

Tracks the **phase** and **frequency** of a 3-Phase signal. The output **phase** of the 3-Phase Phase-Locked Loop is in pi radians. This operation is useful for FPGA control applications of a 3-phase system.

To define the **Input mode**, double-click this Express VI and use the **Input mode** control to specify phase value input—**input (phase value)** or line value input—**input (line value)**.

| Option | Description |
| --- | --- |
| PLL Configuration | Contains the following options: Input mode—Specifies whether the input is in phase value mode or line value mode. Reference frequency—Specifies the reference frequency for the loop. The default frequency is 60 Hz. Sampling time (dt)—Specifies the sampling time. The default time is 100 us. PI Controller Configuration—Contains the following options. Proportional gain (Kp)—Specifies the proportional gain of the PI Controller. Increasing the proportional gain increases the proportional change in the output for a given error value. The default gain is 12. Integral gain (Ki)—Specifies the integral gain of the PI controller. The default gain is 200. Anti-windup gain (Ka)—Specifies the anti-windup gain of the PI controller. Place a checkmark in the Anti-windup? checkbox to expose this option. The default gain is 200. Anti-windup?—Specifies whether the PI controller uses anti-windup gain. LabVIEW places a checkmark in the Anti-windup? checkbox by default. Range of Frequency—Contains the following options: High limit—Specifies the high limit of the frequency range. The default value is 85 Hz. Low limit—Specifies the low limit of the frequency range. The default value is 35 Hz. |
| Fixed-Point Configuration | Contains the following options: Input Type—Specifies the Word length and Integer word length of the following: Input Kp—Proportional gain Ki—Integral gain Ka—Anti-windup gain Output Type—Specifies the Word length and Integer word length of the following: f—Frequency type phase—Phase type |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| reset | Forces the internal states of the integrator to reset to zero when the value is TRUE. |
| input (phase value) | Select this input mode to specify that the input of this function is in phase value mode. |
| input (line value) | Select this input mode to specify that the input of this function is in line value mode. |
| PI gains | Specifies the gains of the PI controller: proportional gain (Kp)—Specifies the proportional gain of the PI controller. integral gain (Ki)—Specifies the integral gain of the PI controller. |
| anti-windup gain (Ka) | Specifies the anti-windup gain of the PI controller. If Anti-windup? is unchecked, this input is unavailable. |
| dt | Specifies the time interval between two samples. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| frequency | Returns the frequency of the 3-phase system. |
| phase | Returns the phase of the 3-phase system. phase is in pi radians. |
| sin(phase) | Returns the sine value of phase. |
| cos(phase) | Returns the cosine value of phase. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/configure-compile-worker-dialog-box.html language=enus -->
## TOPIC 00005: Configure Compile Worker Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/configure-compile-worker-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/configure-compile-worker-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Configure in the FPGA Compile Worker window to display this dialog box. Use the Configure Compile Worker dialog box to specify the compile server from which the compile worker accepts compile job requests. This dialog box contains the following components: Option Description Use the local comp

### Configure Compile Worker Dialog Box

Click **Configure** in the [FPGA Compile Worker](/csh?context=lvfpga_lvfpgacompile_fpga_compile_worker) window to display this dialog box.

Use the **Configure Compile Worker** dialog box to specify the compile server from which the compile worker accepts compile job requests.

This dialog box contains the following components:

| Option | Description |
| --- | --- |
| Use the local compile server | Specifies to use the compile server on localhost without logging in with a user name and password. |
| Connect to a compile server | Specifies to connect to the compile server located on the computer specified in Hostname. By default, LabVIEW uses the compile server installed on the local computer, called localhost. If you installed the Xilinx compilation tools, which includes tools for the compile worker, on a remote computer, you can compile an FPGA VI remotely. Hostname—Specifies the computer running the compile server you want to use. Enter the name or IP address of the remote computer running the compile server. If you enter a name of a computer, the computer must be on the same network as the computer running LabVIEW. Enter only the name of the computer, and do not include any additional characters. Username—Specifies the login name to use to connect to the compile server. The default user name is admin. Password—Specifies the password users must enter before they can connect to the compile server. The default password is empty. |
| Number of simultaneous jobs | Specifies the maximum number of compile jobs that the compile worker can take at the same time.If you install the FPGA Compile Farm Server on the computer you want to use as the compile server, you can compile multiple FPGA VIs simultaneously. Otherwise, the compile server will send only one compile job to the compile worker, even if you specify more in this dialog box. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fifo-properties-dialog-box.html language=enus -->
## TOPIC 00006: FIFO Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fifo-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fifo-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target and select New»FIFO from the shortcut menu to display this dialog box. You also can right-click a FIFO item in the Project Explorer window and select Properties from the shortcut menu or right-click a VI-Defined FIFO Configuration node on the block diagram and select Confi

### FIFO Properties Dialog Box

Right-click an FPGA target and select **New»FIFO** from the shortcut menu to display this dialog box. You also can right-click a FIFO item in the **Project Explorer** window and select **Properties** from the shortcut menu or right-click a [VI-Defined FIFO Configuration](../vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-fifo-vi.html) node on the block diagram and select **Configure** from the shortcut menu to display this dialog box.

Use this dialog box to edit properties for [FIFOs](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data).

This dialog box includes the following pages:

- General
- Data Type
- Interfaces

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fpga-clip-clock-properties-dialog-box.html language=enus -->
## TOPIC 00007: FPGA CLIP Clock Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fpga-clip-clock-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fpga-clip-clock-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a CLIP clock in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to rename a CLIP clock in the Project Explorer window and view the configuration of the CLIP clock. The dimmed components in this dialog box display th

### FPGA CLIP Clock Properties Dialog Box

Right-click a CLIP clock in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display this dialog box.

Use this dialog box to rename a CLIP clock in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and view the configuration of the CLIP clock. The dimmed components in this dialog box display the clock values from the CLIP declaration file. You cannot configure the CLIP clock in this dialog box. Instead, you must [update the CLIP declaration file](/csh?context=lvfpga_lvfpgahelp_fpga_using_clip_clock). .

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the clock that appears in the Project Explorer window. |
| Compile for single frequency | Indicates the frequency of the clock if the clock is not variable. |
| Compile for range of frequencies | Indicates that the FPGA VI has a range of clock frequencies. |
| Min Duty Cycle (% High) | Indicates the minimum percentage of time the clock remains high over one period. |
| Max Duty Cycle (% High) | Indicates the maximum percentage of time the clock remains high over one period. |
| Accuracy (ppm) | Indicates the accuracy of the clock in parts per million. |
| Peak Period Jitter (ps) | Indicates the maximum period jitter of the clock in picoseconds. |
| Supports and Requires Runtime Enable/Disable | Indicates whether you use the Start Enabling FPGA Clock and Start Disabling FPGA Clock Vis to enable and disable the clock. CLIP clocks do not support run time enabling and disabling. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fpga-compile-worker-window.html language=enus -->
## TOPIC 00008: FPGA Compile Worker Window

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fpga-compile-worker-window.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fpga-compile-worker-window.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This window appears when you compile an FPGA VI using the compile server on the local computer. You also can display this window manually by navigating to the FPGA\CompileWorker directory. The compile worker does not launch automatically when you run an FPGA VI that is compiled already or that you h

### FPGA Compile Worker Window

This window appears when you compile an FPGA VI using the compile server on the local computer. You also can display this window manually by navigating to the FPGA\CompileWorker directory.

The compile worker does not launch automatically when you run an FPGA VI that is compiled already or that you have not modified since the last compilation.

To free up resources on the local computer, install the Xilinx compilation tools on a remote computer and compile the FPGA VI remotely.

Use the **FPGA Compile Worker** window to view information about a compilation.

Note

This window contains the following components:

| Option | Description |
| --- | --- |
| Status | Displays status information for the current compilation job. |
| Jobs | Displays information about the current compilation jobs. |
| Configure | Displays the Configure Compile Worker dialog box. |

#### Related Information

[Understanding the LabVIEW FPGA Compile System](/csh?context=lvfpga_lvfpgaconcepts_compiling_fpga_vis)

[NI LabVIEW FPGA Compilation Options](https://www.ni.com/r/FPGACompOptions)

[Getting Started with a Compile Farm](/csh?context=lvfpga_lvfpgahelp_fpga_gettingstartedfpgacompilefarm)

[Configure Compile Worker Dialog Box](/csh?context=lvfpga_lvfpgacompile_fpga_config_worker_db)

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fpga-handshake-properties-dialog-box.html language=enus -->
## TOPIC 00009: FPGA Handshake Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fpga-handshake-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fpga-handshake-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target and select New»Handshake from the shortcut menu to display this dialog box. You also can right-click a handshake item in the Project Explorer window and select Properties from the shortcut menu or double-click a VI-Defined Handshake Configuration node on the block diagram

### FPGA Handshake Properties Dialog Box

Right-click an FPGA target and select **New»Handshake** from the shortcut menu to display this dialog box. You also can right-click a [handshake item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) in the **Project Explorer** window and select **Properties** from the shortcut menu or double-click a [VI-Defined Handshake Configuration](../vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-handshake-vi.html) node on the block diagram to display this dialog box.

Use this dialog box to edit properties for [handshake items](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant).

This dialog box includes the following pages:

- General
- Data Type

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fpga-implementation-page-array-constant-properties-dialog-box.html language=enus -->
## TOPIC 00010: FPGA Implementation Page (Array Constant Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fpga-implementation-page-array-constant-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fpga-implementation-page-array-constant-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Array Constant Properties dialog box to edit properties for memory implementation of array constants. This page includes the following components: Option Description Implementation Specifies the type of storage an array constant uses on the FPGA.Contains the following options: •

### FPGA Implementation Page (Array Constant Properties Dialog Box)

Use this page of the Array Constant [Properties](/csh?productcategories=147794&context=lvcore_lvpage_pp_properties_db) dialog box to edit properties for memory implementation of array constants.

This page includes the following components:

| Option | Description |
| --- | --- |
| Implementation | Specifies the type of storage an array constant uses on the FPGA.Contains the following options: • Auto (default)—Specifies that the compiler decides whether to implement an array constant in block memory, look-up tables, or flip-flops. Arrays of size n x m > 2048, where n is the number of elements and m is the number of bits per element, are implemented in block memory. Arrays of size n x m ≤ 2048 are implemented in look-up tables. The compiler also can infer a block memory or look-up table implementation for an array constant based on specific coding patterns. If the compiler cannot infer an implementation, the array constant implements in flip-flops. An array constant created in another context, such as on the development computer, is automatically set to Auto when opened in an FPGA VI. Note To minimize FPGA resource usage, choose a block memory or look-up table implementation for array constants instead of Auto. Ensure that array constants are used in accepted coding patterns. Otherwise, LabVIEW reverts to the flip-flop implementation or returns an error. • Flip-Flops—Stores the array constant in flip-flops and implements logic operations in look-up tables available on the FPGA. This implementation consumes significant FPGA resources as each bit in the array uses a flip-flop on the FPGA. Use flip-flops when working with small arrays, when you need parallel access to more than one element in an array, or when you have strict timing requirements. • Look-Up Tables—Stores the array constant in look-up tables available on the FPGA. Xilinx literature describes this implementation as distributed RAM or LUT RAM. If the compiler cannot infer distributed RAM, LabVIEW returns an error. When used in a single-cycle Timed Loop, read operations execute in the same clock cycle. Data written during a clock cycle is available for read during the next clock cycle. Use Look-up Tables when you have limited remaining block memory, since look-up tables consume FPGA resources because they can function as either FPGA resources or as memory. • Block Memory—Stores the array constant using embedded blocks of memory. Xilinx literature describes this implementation as block RAM or BRAM. If the compiler cannot infer block memory, LabVIEW returns an error. When used in a single-cycle Timed Loop, read operations take one cycle to execute. Data written during a clock cycle is available for read during the next clock cycle. Use block memory first unless you need the advantages of a different type of memory. Block memory does not consume FPGA resources and tends to compile at a high clock rate relative to other types of memory. If a compilation report indicates that an application exceeds block memory availability, review your design for small array constants and implement them in look-up tables. Ensure that array constants are used in accepted coding patterns for a look-up table implementation. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fpga-implementation-page-properties-dialog-box.html language=enus -->
## TOPIC 00011: FPGA Implementation Page (Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fpga-implementation-page-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fpga-implementation-page-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Feedback Node Properties dialog box to configure how LabVIEW implements the Feedback Node on an FPGA target. This page includes the following components: Option Description First call initialization mux location Specifies where the compiler places the multiplexer relative to the

### FPGA Implementation Page (Properties Dialog Box)

Use this page of the Feedback Node [Properties](/csh?productcategories=147794&context=lvcore_lvpage_pp_properties_db) dialog box to configure how LabVIEW implements the Feedback Node on an FPGA target.

This page includes the following components:

| Option | Description |
| --- | --- |
| First call initialization mux location | Specifies where the compiler places the multiplexer relative to the register that represents the Feedback Node on the FPGA. This placement affects the timing of FPGA applications. This section is available only if you wire a value to the initializer terminal. Note Placing the multiplexer after the register can significantly delay the combinatorial path after the Feedback Node, reducing the clock rate at which you can compile the FPGA VI. Use the compilation reports to experiment with the placement that works best for your application. After register—Specifies that the compiler places the multiplexer after the register. Select this option if the FPGA VI has a long combinatorial path leading up to the Feedback Node but a short combinatorial path after the node. Before register—Specifies that the compiler places the multiplexer before the register. Select this option if the FPGA VI has a short combinatorial path leading up to the Feedback Node but a long combinatorial path after the node. Auto—Auto placement (default)—Specifies that the compiler places the multiplexer before the register if you wire a constant value to the initializer terminal. If you do not wire a constant value to this terminal, the compiler places the multiplexer after the register. You must place the constant in the same VI as the Feedback Node. |
| Compile or load initialization option(s) | Compile or load initialization option(s) Ignore reset—Specifies whether this Feedback Node initializes if the FPGA VI resets.Placing a checkmark in this checkbox has the following implications: This node does not initialize if the FPGA VI resets. The node initializes the next time you download the FPGA VI to the FPGA target. Ensure the application does not depend on the value this Feedback Node returns on the first call after resetting the FPGA VI. LabVIEW removes the reset from the underlying register instantiations, which gives the compiler the option to implement the delays by using shift register lookup tables (SRLs) instead of flip-flops. SRLs combine many delays into a single lookup table (LUT), which can reduce FPGA resource usage significantly compared to flip-flops. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fpga-register-properties-dialog-box.html language=enus -->
## TOPIC 00012: FPGA Register Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fpga-register-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fpga-register-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target and select New»Register from the shortcut menu to display this dialog box. You also can right-click a register item in the Project Explorer window and select Properties from the shortcut menu or right-click a VI-Defined Register Configuration node on the block diagram and

### FPGA Register Properties Dialog Box

Right-click an FPGA target and select **New»Register** from the shortcut menu to display this dialog box. You also can right-click a [register item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) in the **Project Explorer** window and select **Properties** from the shortcut menu or right-click a [VI-Defined Register Configuration](../vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-register-vi.html) node on the block diagram and select **Configure** from the shortcut menu to display this dialog box.

Use this dialog box to edit properties for [register items](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant).

This dialog box includes the following pages:

- General
- Data Type
- Interfaces
- Initial Value

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/fpga-target-properties-dialog-box.html language=enus -->
## TOPIC 00013: FPGA Target Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/fpga-target-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/fpga-target-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure FPGA targets. The functionality that you can configure in this dialog box depends on the specific FPGA target. This dialog box can conta

### FPGA Target Properties Dialog Box

Right-click an FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display this dialog box.

Use this dialog box to configure FPGA targets. The functionality that you can configure in this dialog box depends on the specific FPGA target.

This dialog box can contain the following pages in the **Category** list:

- General
- Execution Mode
- Top-Level Clock
- Component-Level IP
- DRAM Properties
- Conditional Disable Symbols

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/information-page-compilation-properties-dialog-box.html language=enus -->
## TOPIC 00014: Information Page (Compilation Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/information-page-compilation-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/information-page-compilation-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Compilation Properties dialog box to name the FPGA application and select the location to build the application. This page includes the following components: Option Description Build specification name Specifies a unique name for the build specification. The name appears under B

### Information Page (Compilation Properties Dialog Box)

Use this page of the [Compilation Properties](/csh?context=lvfpga_lvfpgadialog_fpga_build_spec_db) dialog box to name the FPGA application and select the location to build the application.

This page includes the following components:

| Option | Description |
| --- | --- |
| Build specification name | Specifies a unique name for the build specification. The name appears under Build Specifications in the Project Explorer window. |
| Bitfile name | Specifies the filename for the bitfile.Bitfiles must have a .lvbitx extension. Note If you compile an FPGA VI multiple times without updating the FPGA project, LabVIEW saves the bitfile for the latest compilation only. To track the history of your bitfiles for the same FPGA project, rename the bitfile for each compilation so that all the bitfiles are saved. |
| Destination directory | Specifies the location to save the build on the local computer. You can enter a path or use the Browse button to navigate to and select the location. If the absolute path specified is the project folder or the folder above, the value of Bld_localDestDir in the project file is a relative path and the value of Bld_localDestDirType is relativeToProject or relativeToCommon. |
| Run when loaded | Specifies that FPGA VIs run automatically when you load them to the FPGA target. The availability of this option varies by FPGA target. Note If you download the FPGA VI to the flash memory, the VI automatically loads to the FPGA even if you do not compile it with the Run when loaded to FPGA option. However, the VI does not run automatically. Verify that the FPGA VI is compiled with the Run when loaded to FPGA option if you want the VI to run automatically when it loads to the FPGA. |
| Allow removal of implicit enable signals inside single-cycle Timed Loops | Specifies that the compiler removes implicit enable signals from single-cycle Timed Loops that run independently of other nodes on the block diagram. By default, this checkbox does not contain a checkmark.Note This option is only visible for targets that support removing implicit enable signals. Refer to your target hardware documentation for more information about support for removing implicit enable signals. |
| Version Number | Contains the version number to associate with the build. Major—Specifies the component of the version number that indicates a major revision. Minor—Specifies the component of the version number that indicates a minor revision. Fix—Specifies the component of the version number that indicates a revision to fix problems. Build—Specifies the component of the version number that indicates a specific build. |
| Build specification description | Displays information about the build specification. You can view and edit the description on this page only. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/information-page-project-export-for-vivado-design-suite-properties-dialog-box.html language=enus -->
## TOPIC 00015: Information Page (Project Export for Vivado Design Suite Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/information-page-project-export-for-vivado-design-suite-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/information-page-project-export-for-vivado-design-suite-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Project Export for Vivado Design Suite Properties dialog box to name the exported project and select the location to save the exported project. This page includes the following components: Option Description Build specification name Specifies a unique name for the build specific

### Information Page (Project Export for Vivado Design Suite Properties Dialog Box)

Use this page of the [Project Export for Vivado Design Suite Properties](/csh?context=lvfpga_lvfpgadialog_fpga_vivado_export_db) dialog box to name the exported project and select the location to save the exported project.

This page includes the following components:

| Option | Description |
| --- | --- |
| Build specification name | Specifies a unique name for the build specification. The name appears under Build Specifications in the Project Explorer window. |
| Bitfile name | Specifies the filename for the bitfile.Bitfiles must have a .lvbitx extension. Note If you export an FPGA VI multiple times without updating the FPGA project, LabVIEW saves the bitfile using the name specified in the latest export only. To track the history of your bitfiles for the same FPGA project, rename the bitfile for each export or build so that all the bitfiles are saved. |
| Destination directory | Specifies the location to save the exported project files. You can enter a path or use the Browse button to navigate to and select the location. This directory is the root directory for the Vivado export working directory. NI recommends avoiding extremely long file paths and paths with spaces. |
| Run when loaded | Specifies that compiled bitfiles run automatically when you load them to the FPGA target. The availability of this option varies by FPGA target. Note If you download the compiled bitfile to the flash memory, the bitfile automatically loads to the FPGA even if you do not enable the Run when loaded to FPGA option. However, the bitfile does not run automatically. Verify that the Run when loaded to FPGA option is enabled in the build specification of the exported project if you want the bitfile to run automatically when it loads to the FPGA. |
| Allow removal of implicit enable signals inside single-cycle Timed Loops | Specifies that the compiler removes implicit enable signals from single-cycle Timed Loops that run independently of other nodes on the block diagram. By default, this checkbox does not contain a checkmark.Note This option is only visible for targets that support removing implicit enable signals. Refer to your target hardware documentation for more information about support for removing implicit enable signals. |
| Version Number | Contains the version number to associate with the build. Major—Specifies the component of the version number that indicates a major revision. Minor—Specifies the component of the version number that indicates a minor revision. Fix—Specifies the component of the version number that indicates a revision to fix problems. Build—Specifies the component of the version number that indicates a specific build. |
| Build specification description | Displays information about the build specification. You can view and edit the description on this page only. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/lvfpga-dialog-box-help.html language=enus -->
## TOPIC 00016: LabVIEW FPGA Module Dialog Box Reference

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/lvfpga-dialog-box-help.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/lvfpga-dialog-box-help.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find detailed information about LabVIEW FPGA Module dialog boxes, including the purpose of the dialog box, how to access the dialog box, and detailed information about the controls and indicators in the dialog box. These pages are available by clicking the Help buttons in the dialog boxes.

### LabVIEW FPGA Module Dialog Box Reference

Find detailed information about LabVIEW FPGA Module dialog boxes, including the purpose of the dialog box, how to access the dialog box, and detailed information about the controls and indicators in the dialog box.

These pages are available by clicking the **Help** buttons in the dialog boxes.

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/project-export-for-vivado-design-suite-properties-dialog-box.html language=enus -->
## TOPIC 00017: Project Export for Vivado Design Suite Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/project-export-for-vivado-design-suite-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/project-export-for-vivado-design-suite-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: From the Project Explorer window, right-click Build Specifications and select New»Project Export for Vivado from the shortcut menu to display this dialog box. You also can right-click a build specification name under Build Specifications and select Properties from the shortcut menu, or double-click

### Project Export for Vivado Design Suite Properties Dialog Box

From the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Build Specifications** and select **New»Project Export for Vivado** from the shortcut menu to display this dialog box. You also can right-click a build specification name under **Build Specifications** and select **Properties** from the shortcut menu, or double-click the build specification name to display this dialog box.

Use this dialog box to access and configure settings for exporting FPGA VIs to Vivado Design Suite.

This dialog box includes the following pages, which you use to configure the settings for the compilation:

- Information
- Source Files

The bottom of this dialog box includes the following buttons:

| Option | Description |
| --- | --- |
| Build | Updates the LabVIEW project with the build specification settings, closes the dialog box, and builds the build specification with the current settings.Clicking the Build button does not save the settings to disk. You must save the project in order to save these build specification settings. |
| OK | Accepts the current configuration and closes the dialog box. |
| Cancel | Closes the dialog box without accepting the current configuration. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/simulation-export-properties-dialog-box.html language=enus -->
## TOPIC 00018: Simulation Export Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/simulation-export-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/simulation-export-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: From the Project Explorer window, right-click Build Specifications and select New»Simulation Export from the shortcut menu to display this dialog box. You also can right-click a build specification name under Build Specifications and select Properties from the shortcut menu, or double-click the buil

### Simulation Export Properties Dialog Box

From the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Build Specifications** and select **New»Simulation Export** from the shortcut menu to display this dialog box. You also can right-click a build specification name under **Build Specifications** and select **Properties** from the shortcut menu, or double-click the build specification name to display this dialog box. If you rebuild an existing simulation export, LabVIEW overwrites the existing files from the previous export in the [working directories for simulation](/csh?context=lvfpga_lvfpgaconcepts_fpga_sim_directory).

Use this dialog box to configure and export files for [third-party simulation](/csh?context=lvfpga_lvfpgaconcepts_fpga_simulation_intro).

This dialog box includes the following pages:

- Information
- Source Files
- Model Fidelity

The bottom of this dialog box includes the following buttons:

| Option | Description |
| --- | --- |
| Build | Updates the LabVIEW project with the build specification settings, closes the dialog box, and builds the build specification with the current settings.Clicking the Build button does not save the settings to disk. You must save the project in order to save these build specification settings. |
| OK | Accepts the current configuration and closes the dialog box. |
| Cancel | Closes the dialog box without accepting the current configuration. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/source-files-page-compilation-properties-dialog-box.html language=enus -->
## TOPIC 00019: Source Files Page (Compilation Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/source-files-page-compilation-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/source-files-page-compilation-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Compilation Properties dialog box to specify the top-level FPGA VI to use in the build. This page includes the following components: Option Description Project Files Displays a list of items under the current target in the Project Explorer window. Top-Level VI Specifies which VI

### Source Files Page (Compilation Properties Dialog Box)

Use this page of the [Compilation Properties](/csh?context=lvfpga_lvfpgadialog_fpga_build_spec_info_db) dialog box to specify the top-level FPGA VI to use in the build.

This page includes the following components:

| Option | Description |
| --- | --- |
| Project Files | Displays a list of items under the current target in the Project Explorer window. |
| Top-Level VI | Specifies which VI is the top-level VI. Select a VI from the Project Files list and click the Add Item button to add the VI as the top-level VI. |
| Set as default build specification | Specifies that the current build specification is the build specification that LabVIEW compiles when you click the Run button in the VI. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/source-files-page-project-export-for-vivado-design-suite-properties-dialog-box.html language=enus -->
## TOPIC 00020: Source Files Page (Project Export for Vivado Design Suite Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/source-files-page-project-export-for-vivado-design-suite-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/source-files-page-project-export-for-vivado-design-suite-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Project Export for Vivado Design Suite Properties dialog box to specify the top-level FPGA VI to use in the project export for Vivado. This page includes the following components: Option Description Project Files Displays a list of items under the current target in the Project E

### Source Files Page (Project Export for Vivado Design Suite Properties Dialog Box)

Use this page of the [Project Export for Vivado Design Suite Properties](/csh?context=lvfpga_lvfpgadialog_fpga_vivado_export_db) dialog box to specify the top-level FPGA VI to use in the project export for Vivado.

This page includes the following components:

| Option | Description |
| --- | --- |
| Project Files | Displays a list of items under the current target in the Project Explorer window. |
| Top-Level VI | Specifies which VI is the top-level VI. Select a VI from the Project Files list and click the Add Item button to add the VI as the top-level VI. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=dialog-boxes/timing-violation-analysis-window.html language=enus -->
## TOPIC 00021: Timing Violation Analysis Window

- bundle_id: `lvfpga-api-ref`
- source_path: `dialog-boxes/timing-violation-analysis-window.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/dialog-boxes/timing-violation-analysis-window.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Investigate Timing Violation button in the Compilation Status window to display the Timing Violation Analysis window. The Investigate Timing Violation button appears only if the compile server encounters timing violations while trying to compile an FPGA VI. Use this window to identify comp

### Timing Violation Analysis Window

Click the **Investigate Timing Violation** button in the [Compilation Status](/csh?context=lvfpga_lvfpgadialog_fpga_compile_help) window to display the **Timing Violation Analysis** window. The **Investigate Timing Violation** button appears only if the compile server encounters timing violations while trying to compile an FPGA VI.

Use this window to identify components in the FPGA application that cannot execute within the application clock rate. Double-click an item in the list or click the **Show Element** button to locate the node on the block diagram. You can use different strategies to [fix timing violations](/csh?context=lvfpga_lvfpgaconcepts_fpga_fix_timing_violations).

This window includes the following components:

| Option | Description |
| --- | --- |
| Timing Information | Lists the propagation delay and maximum fanout of components in the FPGA VI that cause the timing violation. The units of Total Delay, Logic Delay, and Routing Delay are in nanoseconds. Paths—Lists sets of VIs and components that exceed the applicable FPGA clock rate. Each path describes the VIs and components between two internal registers. When items in the table correspond to objects on the block diagrams, such as functions, structures, and subVIs, double-clicking the items in the table highlights the corresponding object on the block diagram. . Some items in the table are non-diagram components and do not correspond directly to objects on the block diagrams. Non-diagram components include resources, arbitration circuits, component-level IP (CLIP), and other circuits that depend on the target hardware. You may be able to use the internal name of the non-diagram component to correlate the non-diagram component with a block diagram object or CLIP. For specific FPGA targets, you can double-click a CLIP in the table to see the signal from the top category of the CLIP on the block diagram. Total Delay—Indicates the sum of Logic and Routing. Because of rounding, the value of Total might differ slightly from the sum of the values of Logic and Routing. Logic Delay—Indicates the amount of time in nanoseconds that a logic block takes to execute. Routing Delay—Indicates the amount of time in nanoseconds that a signal takes to traverse between FPGA logic blocks. Max Fanout—Displays the maximum number of logic block inputs from which a single logic block output connects. This maximum fanout can occur anywhere along the path. High signal fanout contributes to greater routing delays. |
| Show Element | Highlights on the block diagram the item you select in the Paths list. You also can double-click an item in the Paths list to highlight the item on the block diagram. |
| Show Path | Highlights on the block diagram all items in the path you select in the Paths list. |

#### Erroneously Listed Single-Cycle Timed Loops

If the FPGA VI uses a large area on the FPGA, the Xilinx compiler optimizations might map different [single-cycle Timed Loops](/csh?context=lvfpga_lvfpga_fpga_timed_loop) to different look-up tables (LUTs) in the same [slice](/csh?context=lvfpga_lvfpgaconcepts_fpga_basic_chip_terms). If two different single-cycle Timed Loops map to the same slice and a timing error occurs in one of them, the **Timing Violation Analysis** window might indicate the wrong single-cycle Timed Loop has the timing violation.

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/clock-error-codes.html language=enus -->
## TOPIC 00022: Clock Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/clock-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/clock-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clocks can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description Code Description −61156 Clock domain crossing is not supported for Occurrences. −61138 Invalid top-level clock for target. The currently configured top-le

### Clock Error Codes (FPGA Module)

Clocks can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| Code | Description |
| −61156 | Clock domain crossing is not supported for Occurrences. |
| −61138 | Invalid top-level clock for target. The currently configured top-level clock, <InvalidTopClockName>, is not supported as a top-level clock for this FPGA target.<TargetSpecificFilteringMessage>Select a supported top-level clock from the FPGA Target Properties dialog box or reconfigure the current top-level clock. Refer to the FPGA target documentation for more information about supported top-level clocks. |
| −61067 | Clock resource limit exceeded. This application uses more clocking resources for derived clocks than are available on the target. <NumberOfMMCMsUsed> Mixed-Mode Clock Managers (MMCMs) are used, however only <NumberOfMMCMsAvailable> are available to generate derived clocks.Reduce the number of derived clocks used in your application. |
| −61060 | Clock domain crossing is not selected for the memory item. The memory Read and Write interfaces are located in different clock domains and the Dual Clock Interface option is not selected. Either place both interfaces in the same clock domain or place a checkmark in the Dual Clock Interface checkbox in the Memory Properties dialog box. |
| −61039 | Clock resource limit exceeded. This application uses more clock resources than are available on the target. <NumberOfBUFGsUsed> clock buffers (BUFGs) are used, however only <NumberOfBUFGsAvailable> are available.Reduce the number of clocks used in your application. |
| −61037 | Clock requested for From-To constraint does not exist. |
| −61033 | Two timing sources in this application have the same clock signal name. |
| −61032 | The available hardware cannot generate a derived clock. |
| −61031 | There are no configured clocks for this application. Please configure a clock in the project tree. |
| −61030 | Clock resource limit exceeded. This application uses more global clock nets than are available on the target. <NumberOfNetsUsed> global clock nets are used however only <NumberOfNetsAvailable> are available.Reduce the number of clocks used in your application. |
| −61029 | VHDL signal names for clocks must contain "Clk" or "Clock". The first letter can be upper or lower case, but subsequent letters must be lower case. |
| −61028 | A plug-in developer for a LV FPGA target did not provide timing constraints for all top level clocks. |
| −61027 | Clock resource limit exceeded. This application uses more clocking resources for derived clocks than are available on the target. <NumberOfDCMsUsed> Digital Clock Managers (DCMs) are used however only <NumberOfDCMsAvailable> are available to generate derived clocks.Reduce the number of derived clocks used in your application. |
| −61026 | A clock name was found that is not configured. |
| 61058 | Invalid clock for single-cycle Timed Loop. The selected single-cycle Timed Loop is configured to use the clock <ActualClockName> as a timing source. This clock either does not exist in the project or is invalid.Select a valid clock by right-clicking the Input Node of the single-cycle Timed Loop and selecting Configure Input Node or create a valid clock in the Project Explorer window with the name <ActualClockName>. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/code-generation-error-codes.html language=enus -->
## TOPIC 00023: Code Generation Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/code-generation-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/code-generation-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Module can return the following code generation error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61507 Peer-to-peer FIFOs are unsupported on the current target. Specify another type for your FIFO, or you can specify another t

### Code Generation Error Codes (FPGA Module)

The FPGA Module can return the following code generation error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61507 | Peer-to-peer FIFOs are unsupported on the current target. Specify another type for your FIFO, or you can specify another target if you want to use peer-to-peer FIFOs. |
| −61505 | Unsupported .xci file. Component-level IP (CLIP) does not support the <FileName> file, because this file is created by an old version of Xilinx Vivado. Specify another .xci file that is created by Xilinx Vivado <ToolVersion>. |
| −61503 | Missing required Xilinx compilation tools. Install the Xilinx <ToolVersion> compilation tools from the appropriate DVD. |
| −61502 | File format mismatch. Component-Level IP (CLIP) does not support certain synthesis files under current targets and the compilation will not include these files. xci, dcp, and xdc file types are supported only by Xilinx Vivado targets. ucf, xco, ngd, vhe, pxml, ngm, and ngd files are supported only by Xilinx ISE targets. |
| −61489 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information:The block diagram or project contains an item that FPGA DFIR cannot handle. |
| −61487 | This channel control or indicator is on the top-level VI. The connector pane of the top-level FPGA VI cannot contain channel controls or indicators when compiling. |
| −61474 | "FFT size" must be greater than or equal to the number of samples per input. |
| −61473 | The "imaginary data" input array size is different from that of the "real data" input. The array sizes of these inputs must be the same. |
| −61472 | The input array size must be 2, 4, 8, or 16. |
| −61471 | You must reload the IO Module declaration file. The IO Module declaration file has been updated on disk since its last association with this LabVIEW project. On the General page of the IO Module Properties dialog box, click Reload. |
| −61470 | You must reload the DRAM declaration file. The Memory Interface DRAM declaration file has been updated on disk since its last association with this LabVIEW project. On the General page of the DRAM Properties dialog box, click Reload. |
| −61469 | Invalid size for Stream or Lossy Stream channel writer. Constants connected to the "size" input of a Stream or Lossy Stream channel writer must have values greater than zero. |
| −61468 | A channel terminal of a non-reentrant subVI is connected to multiple channels. A channel terminal of a non-reentrant subVI can be connected to only one channel on this target. If a non-reentrant subVI is called from multiple locations, the channel wires connected to a given terminal must resolve to the same channel at compile time. To fix this error, either edit the block diagram so that the channel terminal is connected to only one channel or make the subVI reentrant by selecting "File->VI Properties->Execution", and enabling one of the reentrant execution options. |
| −61467 | Stream or Lossy Stream writer endpoints not wired correctly. You must wire a constant to Stream and Lossy Stream writer endpoints. |
| −61466 | LabVIEW encountered an error when trying to run the Vivado Design Suite scripts. LabVIEW encountered an error when trying to run the Vivado Design Suite scripts. For more details about this error, refer to the log file located at <LogPath>. |
| −61465 | LabVIEW failed to delete a file. LabVIEW failed to delete file <FilePath> when building build specification <BuildSpec>. To correct this error, verify that the file is not in use by another application and try again. |
| −61464 | LabVIEW failed to delete a file. LabVIEW failed to delete file <FilePath> when building build specification <BuildSpec>. To correct this error, verify that you have the permission to modify this file and try again. |
| −61463 | LabVIEW failed to export project for the Vivado Design Suite. LabVIEW encountered an error when trying to export project for the Vivado Design Suite. Possible reason: The destination directory path is too long. Solution: Shorten the destination directory path of build specification <BuildSpec> and try again. |
| −61414 | Control or indicator data type is not supported. The data type of the control or indicator is not supported on the FPGA. Note that controls and indicators are not removed from the VI during compilation, even if their block diagram terminals are placed inside of a Diagram Disable Structure. |
| −61355 | An internal software error has occurred. DFIR refnum not found. |
| −61354 | Internal software error(s): Connected node is not constant. A terminal is not connected to a constant. |
| −61353 | Internal software error(s): Output terminal not supported. The current operation is allowed only on input terminals, and the terminal on this block diagram object is an output terminal. |
| −61352 | Internal software error(s): Terminal is not connectable. You are trying to access a connector pane terminal that is not configured as an input or output. |
| −61351 | Internal software error(s): Terminal is unconnected. A block diagram object terminal is unconnected. |
| −61350 | Internal software error(s): Terminal Index Out of Bounds. A terminal with this index does not exist on this block diagram node. |
| −61345 | Unresolved LabVIEW class. LabVIEW cannot determine the static class type of the global variable because the class written to it does not match the type of the global variable's default value. Ensure that all writes to the global variable use the same class type as its default value. |
| −61344 | The array contains arrays of varying sizes. The FPGA Module does not support global variables with default values that contain embedded arrays of varying sizes. |
| −61343 | Unresolved LabVIEW class. The LabVIEW class could not be statically resolved because different classes are wired to separate calls to the non-reentrant VI. Ensure that all calls to the VI use the same classes.Call chain:<CallChain> |
| −61341 | The array contains arrays of varying sizes. The LabVIEW FPGA Module does not support insertion of array elements that result in embedded arrays of varying sizes.Call chain:<CallChain> |
| −61339 | The top-level VI contains a variable-sized array control or indicator. The FPGA Module does not support variable-sized arrays on the front panel of the top-level VI. |
| −61338 | Array does not resolve to a fixed size. LabVIEW cannot determine the size of the array on the local or global variable because arrays of different sizes are written to it. Ensure that all writes to the local or global variable use arrays of the same size. |
| −61337 | Array does not resolve to a fixed size. LabVIEW cannot determine the size of the array on the control or indicator because arrays of different sizes are wired to separate calls to the non-reentrant VI. Ensure that all calls to the VI use array inputs of the same size. |
| −61336 | The While Loop contains an auto-indexed output tunnel. The FPGA Module does not support auto-indexed output tunnels on the While Loop. |
| −61335 | Array does not resolve to a fixed size. LabVIEW cannot determine the size of the array output tunnel because the For Loop does not execute a fixed number of times. This may occur if the N-input is wired to a non-constant value or if the loop contains auto-indexed input tunnels that are wired to variable-sized arrays.Call chain:<CallChain> |
| −61334 | Array does not resolve to a fixed size. LabVIEW cannot determine the size of the array output because a node input is a non-constant value. Ensure that all index and length inputs resolve to constant values.Call chain:<CallChain> |
| −61333 | Array does not resolve to a fixed size. LabVIEW cannot determine the size of the array output because arrays of different sizes are wired to the node. Ensure that all array inputs resolve to the same size.Call chain:<CallChain> |
| −61323 | The current target has no available DCMs for the CLIP. You have included the CLIP <CLIPInstantiationName> that uses <NumberOfUsedDCMs> Digital Clock Managements (DCMs), but the current target does not have any available DCMs.Remove or alter the CLIP, or use the CLIP on a target with available DCMs. |
| −61322 | The current target has no available MMCMs for the CLIP. You have included the CLIP <CLIPInstantiationName> that uses <NumberOfUsedMMCMs> Mixed-Mode Clock Managers (MMCMs), but this target does not have any available MMCMs.Remove or alter the CLIP, or use the CLIP on a target with available MMCMs. |
| −61310 | A clock is not supported on this target. Clock <DerivedExternalClock> is derived from an external clock or a CLIP clock. Virtex 2 and Spartan 3 targets do not support derived clocks from external or CLIP clocks. |
| −61309 | A node requires a synchronous reset but the build spec allows enable removal. One or more nodes requires a synchronous reset signal. When the application is configured to allow the removal of implicit enable signals, LabVIEW does not support placing a node with this requirement inside a single-cycle Timed Loop controlled either by an external clock or by a clock that supports gating. Remove the checkmark from the "Allow removal of implicit enable signals in single-cycle Timed Loops" checkbox in the build specification or change to a timing source that does not support gating. |
| −61308 | A node is not supported when the application allows enable removal. One or more nodes do not specify the required number of cycles during asynchronous reset. When the application is configured to allow the removal of implicit enable signals, LabVIEW does not support placing a node with this requirement inside a single-cycle Timed Loop controlled either by an external clock or by a clock that supports gating. Remove the checkmark from the "Allow removal of implicit enable signals in single-cycle Timed Loops" checkbox in the build specification or configure the required number of cycles for the node. |
| −61307 | A node requiring a running clock during reset is in an application allowing enable removal. The node requires a running clock during asynchronous reset. When the application is configured to allow the removal of implicit enable signals, you cannot place a node with this requirement inside a single-cycle Timed Loop that is controlled either by an external clock or by a clock that supports gating. Reconfigure or remove the node, or remove the checkmark from the "Allow removal of implicit enable signals in single-cycle Timed Loops" checkbox in the build specification. |
| −61306 | This CLIP is not supported for applications that allow enable removal. The CLIP, <ClipName>, does not specify the required number of cycles during asynchronous reset for one or more of its clock inputs and is connected either to an external clock or to a clock that supports gating. You cannot use a CLIP with this requirement inside an application configured to allow the removal of implicit enable signals. Reconfigure or remove the CLIP, or remove the checkmark from the "Allow removal of implicit enable signals in single-cycle Timed Loops" checkbox in the build specification. |
| −61305 | This CLIP is not supported for applications that allow enable removal. The CLIP, <ClipName>, requires a running clock during asynchronous reset and is connected either to an external clock or to a clock that supports gating. You cannot use a CLIP with this requirement in an application configured to allow the removal of implicit enable signals. Reconfigure or remove the CLIP, or remove the checkmark from the "Allow removal of implicit enable signals in single-cycle Timed Loops" checkbox in the build specification. |
| −61299 | A loop requires enable removal but the build spec does not support it. You must enable the required option in the build specification in order to allow the removal of implicit enable signals for this loop. Remove the checkmark from the "Require removal of implicit enable signals" checkbox in the Configure Timed Loop dialog box or place a checkmark in the "Allow removal of implicit enable signals in single-cycle Timed Loops" checkbox in the build specification. Note that allowing the removal of implicit enable signals will restrict the host interface methods that you can use with this bitfile. Refer to the LabVIEW Help for more information about allowing the removal of implicit enable signals. The build specification option is only available on targets that support it. |
| −61298 | This target does not support enable removal. The build specification is configured to allow the removal of implicit enable signals but the target does not support enable removal. Remove the checkmark from the "Allow removal of implicit enable signals in single-cycle Timed Loops" checkbox in the build specification. |
| −61297 | A loop controlled by a clock that does not support gating requires enable removal. LabVIEW does not support the removal of implicit enable signals from loops controlled by clocks that do not support gating. Replace the clock source with one that supports gating or remove the checkmark from the "Require removal of implicit enable signals" checkbox in the Configure Timed Loop dialog box. |
| −61296 | A loop that requires enable removal conditionally stops executing. LabVIEW does not support the removal of implicit enable signals from loops that conditionally stop executing. Valid stop conditions for this loop are unwired Stop if True, Stop if True wired to a FALSE constant, or Continue if True wired to a TRUE constant. Reconfigure the stop condition for the loop or remove the checkmark from the "Require removal of implicit enable signals" checkbox in the Configure Timed Loop dialog box. |
| −61295 | A loop that requires enable removal has dataflow dependencies. LabVIEW requires the enable chain signals to enforce dataflow execution between code inside and outside the loop. Remove the checkmark from the "Require removal of implicit enable signals" checkbox in the Configure Timed Loop dialog box or ensure that code inside the loop does not depend on data computed outside the loop. |
| −61294 | The size of the selected data type is too large for the selected DRAM. The size of the data type for <MemoryName> is too large for <DramBankName>. The size of the data type, which is <Size> bits, must be less than or equal to the DRAM port width, which is <DramPortWidth> bits. |
| −61293 | Insufficient DRAM available for allocation of memories. <DramBankName> is not large enough to allocate the requested memory items. The following memory items have been requested: <MemoryList>Reduce the total amount of memory requested to <DramBankSize> MB. |
| −61292 | Missing Method(s) for DRAM-based memory. The following method(s) are missing for <MemoryName>: <MissingMethodList>. All DRAM-based memory items require Write, Request Data and Retrieve Data methods. |
| −61291 | Request Data and Retrieve Data memory methods must be in the same clock domain. Request Data and Retrieve Data methods for <MemoryName> must be placed in the same clock domain. |
| −61290 | DRAM Memory Method Not Supported Outside SCTL. <MethodName> for <MemoryName> is not supported outside single-cycle Timed Loops (SCTLs). Methods available for DRAM-based memory items are supported only inside SCTLs. |
| −61250 | Corrupt or missing Xilinx installation. Exporting FPGA VIs for simulation requires Xilinx version 11.5 or greater. The Xilinx compilation tools are either not installed or corrupt. Install or repair the Xilinx compilation tools to export FPGA Vis for simulation. |
| −61247 | The VI cannot be compiled for FPGA. The VI belongs to an NI toolkit that is currently in evaluation mode. |
| −61246 | Missing resource definition for FIFO, Memory, or Register method. The node refers to an undefined hardware resource. This can occur if the local FIFO, memory, or register resource is placed in a diagram disable structure. Move the resource definition out of the disable structure or delete the method node. |
| −61245 | The VI cannot be compiled for FPGA. The VI belongs to a toolkit that is currently in evaluation mode. To purchase this product, please contact the vendor of the toolkit. If you have already purchased this product, select Help >> Activate Add-ons to activate this product. |
| −61244 | The VI cannot compile without a block diagram. The LabVIEW FPGA Module does not support VIs saved without block diagrams. |
| −61243 | The array does not meet implementation requirements. The array could not be implemented using the resource type specified. This occurs when either Block Memory or Look-Up Tables is selected and the usage of the array does not meet the limitations of the resource. Restructure the array in order to obtain the desired implementation or change the FPGA Implementation option to Auto. |
| −61242 | The FPGA Module does not support this combination of data types. The top-level FPGA VI cannot include a cluster control or indicator with both name controls and other data types. You must separate name controls and other data types into different clusters. |
| −61241 | Duplicate file error. Two of the files specified though an IP Integration Node or component-level IP object have the same name but different contents. Rename one of the two files and adjust your design as necessary. For example, if your file is a VHDL file with an entity name that matches the filename, you may need to change the entity name and all the references to it.Alternatively, adjust the design to use only one of the files.File path 1: <userFilePath1>File path 2: <userFilePath2> |
| −61240 | Duplicate file error. One of the files specified though an IP Integration Node or component-level IP instance has the same name as a file that LabVIEW creates. Rename the file and adjust your design as necessary. For example, if your file is a VHDL file with an entity name that matches the filename, you may need to change the entity name and all the references to it.File path: <userFilePath> |
| −61237 | Terminal(s) requiring constant input wired to non-constant source(s). One or more terminals on this object must be wired to a constant. For example, if the FPGA I/O Node is in a non-reentrant VI, ensure that you wire a constant to the FPGA I/O In input of the FPGA I/O Node. |
| −61236 | Terminal(s) requiring constant input unwired. One or more terminals on this object must be wired to a constant. Refer to the LabVIEW Help for information about the requirements of this object. |
| −61198 | Handshake methods are not supported outside SCTLs. <MethodName> for <HandshakeName> is not supported outside single-cycle Timed Loops (SCTLs). Handshake methods are only supported inside SCTLs. |
| −61197 | Each handshake cannot support more than one of each type of method. You have used multiple instances of the same <MethodName> method for the <Scope> handshake. Use only one Write method and only one Read or Read Without Acknowledge and Acknowledge method. If you use a Clear method, ensure there is only one. |
| −61196 | The handshake Read Without Acknowledge and Acknowledge methods must be used in the same clock domain. |
| −61195 | The handshake Read Without Acknowledge and Acknowledge methods cannot be used separately. The Read Without Acknowledge and Acknowledge methods must be used together for the <Scope> handshake. Add the missing method in the same clock domain. |
| −61194 | You cannot use a handshake Read method with a Read Without Acknowledge or an Acknowledge method. For the <Scope> handshake, <MethodName> method was used with a Read method. Either use only a Read method or use a Read Without Acknowledge method and an Acknowledge method. |
| −61193 | The handshake is missing a Read or Write method. The <Scope> handshake requires both a Write and a Read or a Read Without Acknowledge method. This <Scope> handshake is missing a <MethodName> method. |
| −61192 | A False constant is wired to a DSP48 node enable terminal. The enable terminal should be wired to a dynamic signal or a True constant. |
| −61191 | The IP Integration node specifies an incompatible .ngc synthesis file. <ngcFileName> was generated with a version of the Xilinx compilation tools that is not supported by this version of LabVIEW. Ensure you have the correct version of the Xilinx compilation tools by installing the tools from the Platform media that accompanies the version of LabVIEW you are using. |
| −61190 | Inconsistent clock settings between CLIP declaration file and CLIP instantiation. The number of CLIP clocks in CLIP instantiation <clipInstanceName> is not the same as that in the CLIP declaration <clipDeclarationName>, or the HDL name, LabVIEW name, and/or port direction is not identical. Navigate to the Clock Selections category of the Component-Level IP Properties dialog box, check the changes, and click OK if you agree to accept them. Alternatively, change the CLIP declaration to make it consistent with the instantiation. |
| −61189 | CLIP refers to an FPGA clock that does not meet requirements. CLIP instance <clipInstanceName> refers to FPGA clock <fpgaClockName> which does not meet the frequency requirements specified in the CLIP declaration <clipDeclarationName> for the clock <clipDeclarationClockName>. Select an FPGA clock that meets the frequency requirements of the CLIP instance or change the CLIP declaration to relax the clock <clipDeclarationClockName> frequency requirements. |
| −61188 | CLIP refers to a missing FPGA clock. CLIP instance <clipInstanceName> refers to FPGA clock <fpgaClockName>, which is missing from the project. Select an FPGA clock already present in the project or add a clock with the name <fpgaClockName> to the project. |
| −61187 | Missing CLIP implementation file. File <implementationFileName> specified in the CLIP declaration <declarationName> is missing. The file may have been deleted, renamed, or moved on the disk. Rescan the CLIP declaration files in the Component-Level IP category of the FPGA Target Properties dialog box for further information about this problem. |
| −61186 | Updated CLIP declaration file. The CLIP declaration file was updated on disk since it was associated with this LabVIEW project. Rescan the CLIP declaration in the Component-Level IP page of the FPGA Target Properties dialog box. File: <filePath> |
| −61185 | Missing CLIP declaration. The specified CLIP declaration file is missing. Update the CLIP declaration file path in the Component-Level IP page of the FPGA Target Properties dialog box or make sure that the file is present in the specified location. File Path: <filePath> |
| −61184 | Incorrectly configured CLIP instance. CLIP instance <name> is configured with a CLIP declaration that is not valid. Change the CLIP instance configuration or add the relevant CLIP declaration to the target. |
| −61179 | Unsupported node on this target. This target does not support the <NodeName> node. Change your algorithm to use blocks supported by the current target or obtain a target that supports the <NodeName> node. |
| −61178 | Internal software error(s): Unable to resolve clock for ports. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information:An object is requesting more than one clock, however it does not specify which ports on the object are synchronous to which clocks. |
| −61177 | Missing Read or Write method for FIFO. Each FIFO requires either a Read or Write method, as applicable. Please add a Read or Write method for <FIFONAME>. |
| −61176 | Invalid clock utilized for FIFO Method. The method connected to <PortName> of'<FifoName> utilizes <CurrentClk>, which is not permitted in this design. This method can exist only within the same clock domain as the Read or Write method of the associated FIFO. Note For Get Stream State only, the default clock domain, <DefaultClk>, is also permitted. Given this design, the permitted clocks are: <ClockList>. |
| −61175 | FPGA FIFO Node is not wired with constant FPGA FIFO Name. |
| −61174 | FPGA Memory Node is not wired with constant FPGA Memory Name. |
| −61173 | Item does not match configuration of the name control. The name control or constant wired to the method node does not match the configuration of the node. |
| −61172 | Project item not found. The name control or constant is configured for an item that does not appear under the current target in the Project Explorer window. Add an appropriate item to the Project Explorer window or select a different item from the control or constant. |
| −61171 | Name control or constant is empty. Empty value is not supported. Select an appropriate item that appears under the current target in the Project Explorer window. |
| −61164 | Local and global variables of this type are not supported. Replace the variable with a control or constant. |
| −61163 | Internal software error(s). <Message> An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61162 | Object must be used inside a single-cycle Timed Loop. An object that must be used inside a single-cycle Timed Loop is being used outside a single-cycle Timed Loop. |
| −61161 | VI Execution Mode not supported outside single-cycle Timed Loop. The Execution Mode of the selected VI is Inside Single-Cycle Timed Loop, but the VI is placed outside any timed loops. Move the VI into a single-cycle Timed Loop or change the Execution Mode in the configuration dialog box. |
| −61160 | VI Execution Mode not supported inside single-cycle Timed Loop. The Execution Mode of the selected VI is Outside Single-Cycle Timed Loop, but the VI is placed inside a timed loop. Move the VI outside any single-cycle Timed Loops or change the Execution Mode in the configuration dialog box. |
| −61158 | Conditional terminal on For Loop not supported. FPGA targets do not support using the conditional terminal on For Loops. Right-click the For Loop border and remove the checkmark next to Conditional Terminal. |
| −61157 | Object(s) not supported in the single-cycle Timed Loop. Look-Up Table 1D with interpolation takes more than one clock cycle to execute.Turn off interpolation mode, remove the VI from the single-cycle Timed Loop, or replace the single-cycle Timed Loop with a While Loop. |
| −61155 | Unsupported Clock For Resource. The <method> <IOType> for <IOResource> is used in a clock domain that it does not support. The supported clock domains include: <SupportedClockList>. |
| −61154 | Access from different clock domains not supported. I/O resource <IOResource> does not support <methodList> accessed from a different clock domain. |
| −61153 | Express VI not configured. The <express_vi> VI has not been configured. Double-click the <express_vi> VI on the block diagram to display the configuration dialog, verify the settings in the dialog, and click the OK button to save the settings. |
| −61152 | Variable clock rate not supported. The Square Wave Generator VI is not supported with a variable clock. Change the top-level clock and reset the FPGA clock rate parameter on the Square Wave Generator VI. |
| −61151 | Function or structure must be wired to a fixed clock name. Reconfigure the block diagram so that the clock name cannot be changed at run time. |
| −61150 | Clock project item not found. The FPGA clock control or constant is configured for a clock that does not appear under the current target in the Project Explorer window. Add the clock to the Project Explorer window or select a different clock from the control or constant. |
| −61149 | Clock control or constant is empty. The FPGA clock control or constant is empty. Select a clock that appears under the current target in the Project Explorer window. |
| −61148 | Clock rate mismatch. The block diagram clock rate does not match the clock rate for which the Square Wave Generator VI was configured. The diagram clock is set to <diagram_clock> and the Square Wave Generator VI clock is set to <square_wave_clock>. Reconfigure the Square Wave Generator VI for the new clock rate. You might also need to modify computed values for the scaled inputs. |
| −61147 | Internal software error(s). The VI <PathToSearchingVI> searched for port <SearchedPort> and did not find it in the port list. |
| −61145 | HDL Interface Node File Not Found. LabVIEW cannot find the file <FilePath>. Reconfigure the HDL Interface Node to point to the current location of this file or remove the reference to this file. Double-click the HDL Interface Node and select the External Files tab to reconfigure the node. |
| −61144 | HDL Interface Node outside single-cycle Timed Loop. Selected HDL Interface Node is only configured for placement inside a single-cycle Timed Loop, but the node is placed outside the loop. Move or reconfigure the node. To reconfigure the node, double-click the node, select the Execution Control category, and reconfigure the Single-Cycle Timed Loop option. |
| −61143 | Front panel control/indicator violates size restrictions. The control/indicator <ObjectName> with total size of <BitSize> bits exceeds the allowed control/indicator size. The maximum size for a control/indicator is <MaxSize> bits. |
| −61142 | VI is broken. This VI has a broken Run button. Click the Run button and resolve the items in the Errors list before trying to compile. |
| −61140 | The VI cannot be compiled because its type is not supported. Only standard VIs can be compiled. |
| −61139 | Top-level clock rate has changed. Top-level clock rate does not match rate for which the Sine Wave Generator VI was configured. Reconfigure the Sine Wave Generator or the top-level clock so that their rates match. You also might need to modify computed values for the frequency (cycles/tick) input. |
| −61137 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information: Directory specified by the FPGASourceFilesDirectoryPath or FPGASimSourceFilesDirPath resource file tag does not exist. Directory path: <Path> |
| −61136 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information: Required constraints (.ucf/.xdc) file not found. FPGA Source Files Directory Path: <Path> |
| −61135 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information: Required top VHDL file not found. File path: <Path> |
| −61134 | HDL Interface Node inside single-cycle Timed Loop. Selected HDL Interface Node is configured only for placement outside a single-cycle Timed Loop, but the node is inside a single-cycle Timed Loop. Move or reconfigure the node. To reconfigure the node, double-click the node, select the Execution Control category, and reconfigure the Single-Cycle Timed Loop option. |
| −61133 | Front panel control/indicator(s) crossing clock domains not supported in subVIs. A subVI is called from clock domain <SubVIsClock> but a control or indicator on the connector pane is accessed from clock domain <FPTerminalClock>. Controls and indicators in subVIs do not support crossing clock domains. Move front panel control or indicator terminals outside the single-cycle Timed Loop. Use a wire to pass data into or out of the loop in the different clock domain. |
| −61132 | Front panel control/indicator(s) crossing clock domains is not supported in subVIs. The read and write interfaces to a control/indicator in a subVI are in different clock domains. Controls/indicators in subVIs do not support crossing clock domains. Change the VI such that all accesses to the control/indicator are in the same clock domain. |
| −61131 | Internal software error(s). A resource component does not exist. An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61130 | Too many resource interface requestors. There are too many objects requesting access to a resource interface. Reduce the number of requestors to <MaxRequestors>. |
| −61129 | Top-level port has more than one driver. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. Top-level port <PortName> has more than one driver. |
| −61128 | Internal software error(s). Internal error while creating a plugin arbiter. An internal software error in LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61127 | Internal software error(s). Resource interface <ResPortName> must be defined before use by selected component. An internal software error in LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61126 | Internal software error(s). Resource <ResName> must be defined before use by selected component. |
| −61125 | The top-level port was requested before the selected component created it. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. The top-level port <PortName> was requested before the selected component created it. |
| −61124 | A resource was requested before the resource database was initialized. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. A resource was requested before the resource database was initialized. |
| −61123 | Internal software error(s). A resource interface was requested with a conflicting configuration. An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61122 | Internal software error(s). Unrequesting resource <ResName> is unsupported. An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61121 | Internal software error(s). A clock <ClockName> was not found when making connections for component. An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61120 | Error attempting to remove register from component. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. Error attempting to remove register from component. |
| −61119 | Arbitration option not supported in the single-cycle Timed Loop. Object(s) are requesting access to a resource through resource interface(s) configured with the Always Arbitrate option, which is not supported inside the single-cycle Timed Loop. Change the arbitration option or replace the single-cycle Timed Loop with a While Loop. Refer to the LabVIEW Help for more information about arbitration options. |
| −61118 | Unsupported function inputs. The selected function does not support arrays and/or clusters as inputs when used in the single-cycle Timed Loop. Unbundle clusters and/or index arrays to reach scalar data types or replace the single-cycle Timed Loop with a While Loop. |
| −61117 | Unsupported function inputs. The selected function has arrays and/or clusters wired to its inputs, which is not supported by the LabVIEW FPGA Module. Index arrays and unbundle clusters to reach scalar data types. |
| −61116 | Unsupported Compound Arithmetic inputs. The selected Compound Arithmetic function has arrays and/or clusters wired to its inputs. The Compound Arithmetic function only supports scalar types in the LabVIEW FPGA Module. Remove any arrays or clusters wired to the Compound Arithmetic function. Index arrays or unbundle clusters to reach scalar data types. |
| −61115 | Non-reentrant subVI(s) used in different clock domains. The selected non-reentrant FPGA subVI is located in more than one clock domain. All instances of a non-reentrant FPGA subVI must be in the same clock domain because LabVIEW generates code for a non-reentrant FPGA subVI only once. First, save a copy of the FPGA subVI with a different name for each clock domain. Next, replace calls to the old FPGA subVI with calls to the new FPGA subVIs based on the clock domain that calls the FPGA subVI. |
| −61114 | Non-reentrant subVI(s) used inside and outside a single-cycle Timed Loop. A non-reentrant FPGA subVI is located both inside and outside a single-cycle Timed Loop. All instances of a non-reentrant FPGA subVI must be either inside or outside a single-cycle Timed Loop but not both, because LabVIEW generates code for a non-reentrant FPGA subVI only once. Save a copy of the FPGA subVI with a different name and replace all calls to the original FPGA subVI inside single-cycle Timed Loops with calls to the new FPGA subVI. |
| −61113 | Constant references not allowed. The selected object is a constant reference. Constant unbound references imply runtime binding. The LabVIEW FPGA Module does not support statically unbound references. Remove the constant reference. |
| −61112 | The method(s) are used in multiple clock domains. Object(s) are requesting access to a resource through method(s) in more than one clock domain. Ensure that all objects requesting access to the corresponding method are in the same clock domain. |
| −61111 | Object(s) only supported in the single-cycle Timed Loop. The selected object is only supported inside the single-cycle Timed Loop. Place a single-cycle Timed Loop around the object. |
| −61110 | Invalid FIFO implementation. An internal software error has occurred. The implementation of FIFO <Fifoname> is invalid. Use the FPGA FIFO Properties dialog box to select a valid implementation. |
| −61109 | Object(s) connected to an initialized shift register. The selected object is connected to an initialized shift register. The selected object contains an embedded uninitialized shift register. Remove the initializer or use a Feedback Node. |
| −61108 | Resource interface(s) requested from both inside and outside the single-cycle Timed Loop. Multiple objects are requesting access to a resource through a resource interface from both inside and outside the single-cycle Timed Loop, which is not supported. Place all objects requesting access to the resource interface either inside or outside the single-cycle Timed Loop. |
| −61107 | Arbitration option not supported inside a single-cycle Timed Loop. Never Arbitrate is the only read port arbitration option supported inside a single-cycle Timed Loop. |
| −61106 | Multiple instances of non-reentrant subVI(s) in the single-cycle Timed Loop. Non-reentrant subVI is called from multiple locations in the single-cycle Timed Loop(s), which is not supported. Change the diagram so that the subVI is called from only one place, use a While Loop instead of a Timed Loop, or change the subVI to be reentrant. Refer to the LabVIEW Help for more information about reentrant VIs. |
| −61105 | Multiple writes to control/indicator and local(s) in single-cycle Timed Loops. Multiple writes to a control/indicator and corresponding local variable(s) are not supported in single-cycle Timed Loops. Create code in the single-cycle Timed Loop such that there is at most one write to a control/indicator or corresponding local variable. You can usually create such code by using a Case structure to select the data to write to a single instance control/indicator or local variable. |
| −61104 | Arbitration option not supported in the single-cycle Timed Loop. Object(s) are requesting access to a resource through resource interface(s) configured with the Never Arbitrate option, which is not supported inside the single-cycle Timed Loop. Use the Arbitrate if Multiple Requestors Only option and make sure there is only a single object requesting access to the resource interface. Refer to the LabVIEW Help for more information about arbitration. |
| −61103 | Arbitration option not supported in the single-cycle Timed Loop. Multiple objects are requesting access to a resource through a resource interface configured with the Arbitrate if Multiple Requestors Only option, which is only supported in the single-cycle Timed Loop if there is only a single requestor per interface. Remove the extra requestor(s), change the arbitration option if possible, or replace the single-cycle Timed Loop with a While Loop. Refer to the LabVIEW Help for more information about arbitration options. |
| −61102 | Arbitration option not supported in the single-cycle Timed Loop. Object(s) are requesting access to a resource through resource interface(s) configured with the Always Arbitrate option, which is not supported inside the single-cycle Timed Loop. Change the arbitration option or replace the single-cycle Timed Loop with a While Loop. Refer to the LabVIEW Help for more information about arbitration options. |
| −61101 | Object(s) not supported in the single-cycle Timed Loop. The selected object takes one or more clock cycles to execute. Remove the object from the single-cycle Timed Loop or replace the single-cycle Timed Loop with a While Loop. |
| −61100 | The Interrupt function cannot wait until its interrupt is cleared in a single-cycle Timed Loop. The Interrupt function must have its Wait Until Cleared input unwired, or have a FALSE constant wired to this input. |
| −61097 | CLIP simulation model not defined. CLIP declaration <clipDeclarationName> either has the top-level simulation behavior defined as "Exclude from simulation model" or does not have simulation behavior defined at all. A simulation model is necessary for simulation. Use the Configure Component-Level IP wizard to define a VHDL simulation model for the IP. |
| −61095 | Object without implicit enable signal is used outside a single-cycle Timed Loop. An object has the implicit enable signal disconnected, but is used outside a single-cycle Timed Loop. If an object is outside a single-cycle Timed Loop, the object requires the implicit enable signal. Move the object inside a single-cycle Timed Loop or open the configuration dialog box for the object and remove the checkmark from the option to disconnect the implicit enable signal. |
| −61094 | Object not supported in simulation. This object is not supported in simulation. Remove the object or disable it using a Conditional Disable structure. |
| −61093 | Object without implicit enable in Case structure. Object has the implicit enable signal disconnected and is used in a Case structure. If an object is in a Case structure, the object requires the implicit enable signal. Move the object outside of all Case structures or open the configuration dialog box for the object and remove the checkmark from the option to disconnect the implicit enable signal. |
| −61092 | Resource does not support single-cycle Timed Loops. The <method> <IOType> for <IOResource> is not allowed inside of a single-cycle Timed Loop. |
| −61091 | Resource requires use inside single-cycle Timed Loop. The <method> <IOType> for <IOResource> must be used inside a single-cycle Timed Loop. |
| −61090 | Resource used in unsupported clock domain. The <method> <IOType> for <IOResource> is used in a clock domain that does not support it. The supported clock domain is <RequiredClockDomain>. <AdditionalCLIPHelp> |
| −61065 | Digital resource access conflict. The digital output resource <resource> cannot be accessed from both a Digital Line Output function and a Digital Port Output function. Use either the Digital Line Output function or Digital Port Output function, but not both. |
| −61064 | HDL Interface Node configured to require clock during reset. HDL Interface Node is configured to require a running clock during reset. The clock domain this node is used in might stop during a reset. If registers inside your HDL are only asynchronously reset or you can guarantee your clock runs during a reset, reconfigure the node by double-clicking the node and removing the checkmark from the Requires Running Clock During Reset checkbox on the Execution Control tab. Otherwise, move the HDL Interface Node into a clock domain that is not external to the device and is not configured to support and require a run-time enable/disable. |
| −61063 | Component requires a running clock during reset. A component is used in a clock domain that might stop. The component requires a running clock during reset to reset properly. Move the component from the clock domain that could stop to a clock domain that cannot stop. |
| −61062 | Internal software error(s). LabVIEW expected to find a port named <portname> in the component clock information but did not find it. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61058 | Loops using external clocks must never exit. FPGA VIs do not support exiting loops that use external clocks. This restriction keeps improper block diagram execution contained within the loop if the clock glitches or setup/hold requirements are otherwise violated on flip-flops in the single-cycle Timed Loop. Unwire the conditional terminal for exiting the loop. |
| −61057 | Internal software error(s). Clock resource <ClockResource> has the resource.xml tag for both ForceBufgInstantiation and ForceBufrInstantiation. FPGA code generation does not support both of these tags set on the same clock resource. Remove one of the tags. |
| −61056 | Top-level clock cannot be enabled/disabled at run time. A clock for the top-level FPGA VI is configured to require run-time enable and disable. This configuration is not allowed because it prevents the FPGA VI from executing. Configure the top-level clock so that it does not support run-time enable and disable. |
| −61055 | Clock requires enable and disable but is not programmed. A clock is configured to require run-time enable and disable, but the FPGA VI does not use the Start Enabling FPGA Clock or Start Disabling FPGA Clock function to program this clock. Use a Start Enabling FPGA Clock and Start Disabling FPGA Clock function with the clock or configure the clock to not support run-time enable and disable. |
| −61054 | Cannot enable or disable a clock in the same clock domain being enabled or disabled. You cannot use the Start Enabling FPGA Clock VI or Start Disabling FPGA Clock VI in the same clock domain as the clock domain you want to enable or disable. Put these VIs in a different clock domain than the clock you want to enable or disable.. |
| −61049 | Enabling and disabling a clock requires the clock support run-time enable and disable. The clock wired to the Start Enabling FPGA Clock VI or Start Disabling FPGA Clock VI is not marked as supporting and requiring run-time enable and disable. Right-click on the clock you want to enable/disable and select Properties. In the Properties dialog, select the option Supports and Requires Runtime Enable and Disable. If this option is not available, the selected clock does not support run-time enable/disable. |
| −61047 | Controls or indicators using Synchronous Display are not supported in single-cycle Timed Loops. Replace the single-cycle Timed Loop with a While Loop or deselect Synchronous Display on the control or indicator. |
| −61038 | Millisecond timing resolution not supported. Timing function is configured to use milliseconds. However, an exact millisecond resolution is not possible within a clock domain with a frequency of <ClockRate> MHz. Change the timing function to use ticks or use a clock domain with a frequency that is a multiple of 1 kHz. |
| −61036 | Microsecond timing resolution not supported. Timing function is configured to use microseconds, however an exact microsecond resolution is not possible within a clock domain with a frequency of <ClockRate> MHz. Change the timing function to use ticks or use a clock domain with a frequency that is a multiple of 1 MHz. |
| −61035 | Microsecond/Millisecond timing resolution not supported. A timing function is configured to use microsecond or millisecond resolution, however the clock domain in which the function was placed uses a clock with a variable frequency. Change the timing function to use ticks or use a clock domain with a frequency that is not variable. |
| −61034 | Invalid top-level clock for target. The currently configured top-level clock, <InvalidTopClockName>, for this FPGA target either does not exist in the project or is invalid. Select a valid top-level clock in the Properties of the FPGA target or add a valid clock with the name <InvalidTopClockName> to the project. |
| −61025 | Enabling/Disabling derived clocks not supported. You have attempted to enable/disable a derived clock. You can enable/disable only base clocks that support and require run-time enable and disable. |
| −61011 | Unsupported FIFO size. The selected FIFO is configured to use block memory implementation but contains less than two elements. Block memory FIFOs must contain at least two elements. Increase the size of the FIFO or use a different implementation for the FIFO. |
| −61009 | Unresolved LabVIEW class. The LabVIEW class could not be statically resolved. Call chain:<CallChain> |
| −61008 | Class control or indicator on top-level VI. The front panel of the top-level FPGA VI cannot contain LabVIEW classes when compiling. |
| −61007 | Conditional Disable Structure contains broken code. The Conditional Disable Structure cannot be compiled while the conditional disable symbol FPGA_EXECUTION_MODE is set to THIRD_PARTY_SIMULATION. |
| −61006 | Syntax error in user supplied HDL. The HDL compiler reported the following error(s): |
| −61005 | Object not supported in simulation. Password protected VIs are not supported in simulation. You can either enter the password for the VI or remove the VI from the design. |
| −61004 | FIFO object not supported in simulation. On this target, built-in control logic and target-optimal control logic for FIFOs are not supported in simulation exports. Use one of the following options to fix this error: remove the object, use the conditional disable structure to disable the object for simulation exports, or change the property of the FIFO control logic implementation to slice fabric. |
| −61003 | You cannot include this function in a For Loop when the For Loop is inside a single-cycle Timed Loop. |
| −61002 | The array size exceeds the limit for the current node when the node is inside a single-cycle Timed Loop. The array size exceeds the limit for the current node when the node is inside a single-cycle Timed Loop. To avoid this error, reduce the array size or move this operation outside of the Timed Loop. |
| 61050 | A parameter to a function is invalid. |
| 61051 | An operation did not complete because requested memory was unavailable. |
| 61052 | HDL code generation error occurred. |
| 61053 | A resource management error occurred. The resources might have conflicting configurations. |
| 61054 | A code generation error occurred while interpreting LabVIEW signals. |
| 61055 | Internal software error(s). An internal software error in the LabVIEW FPGA Module has occurred while generating code. Please contact National Instruments technical support at ni.com/support. |
| 61056 | Timing specified in the diagram cannot be met. |
| 61057 | Internally pipelined object(s) not connected to enough Feedback Nodes. The selected object has an embedded shift register that makes the output on a particular loop iteration correspond to the inputs from the previous iteration. Wire the outputs for the object directly to the minimum number of Feedback Nodes or uninitialized shift registers. You cannot wire the outputs to another object. Refer to the LabVIEW Help for more information about objects with embedded shift registers. |
| 61059 | Invalid initialization option on a Feedback Node that follows a Memory Read method. The FPGA VI contains a Feedback Node, following a Memory Read method, that ignores the FPGA Reset method. This configuration is not supported. Either change the initialization option on the Feedback Node or disconnect the initialization terminal. |
| 61061 | Unsupported delay on Feedback Node following memory read. The delay of the selected Feedback Node following a memory read is greater than 1 cycle.Configure the delay to be 1 cycle. You can place additional delays in a separate Feedback Node after this node. |
| 61062 | Invalid use of the enable terminal on a Feedback Node that follows a Memory Read method. The enable terminal is wired on a Feedback Node that follows a Memory Read method. To fix this error, right-click the Feedback Node and select Show Enable Terminal to remove the checkmark from this option. If you need the enable terminal, place the Memory Read method and Feedback Node inside a Case structure and wire the case selector terminal with the wire you intended to wire to the enable terminal of the Feedback Node. This workaround adds a mux on the output tunnel of the Case Structure, which reduces efficiency. |
| 61063 | Initializer constant is wired through a tunnel. A Feedback Node is configured to ignore the Reset method but has an initializer terminal that is wired to a constant that is wired through a tunnel. If the Feedback Node ignores the Reset method, you must wire the constant directly to the initializer terminal without going through a tunnel. An alternative is to configure the Feedback Node to initialize on the first call to the FPGA VI. |
| 61064 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information: Code Generation quit. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/compilation-error-codes.html language=enus -->
## TOPIC 00024: Compilation Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/compilation-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/compilation-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Module can return the following compilation error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61490 An internal error has occurred. This is normally generated by a user request to cancel an operation. No user visible feedback

### Compilation Error Codes (FPGA Module)

The FPGA Module can return the following compilation error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61490 | An internal error has occurred. This is normally generated by a user request to cancel an operation. No user visible feedback is given for this error. |
| −61462 | The design was unable to meet timing requirements due to a pulse width violation. |
| −61461 | This version of LabVIEW does not support the requested FPGA compilation tools. |
| −61459 | The selected target requires 64-bit Xilinx tools, but the system uses a 32-bit OS. |
| −61458 | Target does not support terminals configured for variable and bounded size arrays. One or more terminals on this wire are configured to accept variable or bounded size arrays, which this target does not support. Place a checkmark in the "Autopreallocate arrays and strings" checkbox in the Execution section of the VI Properties dialog box. |
| −61457 | The compilation status file is missing or corrupt. |
| −61456 | The FPGA design did not meet timing requirements and the source of the timing failure could not be located automatically. |
| −61455 | Some of the compilation steps were not executed. |
| −61454 | Some signals were not properly constrained in the design. |
| −61453 | The constraints file was not used in the compilation. |
| −61452 | The compilation failed due to resource overmapping. |
| −61451 | The compilation failed due to timing violations. |
| −61450 | The compilation failed due to a Xilinx error. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/compile-server-error-codes.html language=enus -->
## TOPIC 00025: Compile Server Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/compile-server-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/compile-server-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The compile server can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61347 The user has reached the maximum number of simultaneous compiles for this compile cloud account. −61346 The version of the compile farm

### Compile Server Error Codes (FPGA Module)

The compile server can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61347 | The user has reached the maximum number of simultaneous compiles for this compile cloud account. |
| −61346 | The version of the compile farm client is newer than the version of the compile farm server. Update the compile farm server and compile again. |
| −61342 | The compile farm server returned an unexpected software error. |
| −61340 | The compilation failed because the system ran out of memory. |
| −61332 | An unexpected error occurred with the compilation tools. Trying to compile the FPGA VI again might resolve the issue. |
| −61331 | The UnitOfWork file sent to the Compile Worker was malformed. |
| −61330 | An internal software error in the compile worker has occurred. |
| −61329 | The LabVIEW FPGA Module fails to download files from the compile farm server. Try recompiling the FPGA VI. |
| −61321 | The compile farm server does not have any compile workers to perform this compilation. |
| −61320 | The compile farm server cancelled the compilation. |
| −61319 | The compile farm server aborted the compilation. |
| −61318 | The compile worker cannot perform the compilation. The compile worker may be configured incorrectly for this compilation or it may be in an error state. |
| −61317 | The Xilinx tools required for this compilation are not installed on this machine. |
| −61316 | The compile worker is not installed on this machine. |
| −61315 | You do not have a license for the compile cloud service or the license has expired. |
| −61314 | The disconnected compilation cannot be retrieved from the compile farm server. |
| −61313 | The compile farm server returned an invalid username and password combination. |
| −61312 | The compile farm server is not installed on this machine. |
| −61311 | LabVIEW cannot contact the compile farm server. If compiling locally, try restarting your machine. If compiling remotely, contact your compile farm administrator. |
| −61304 | The LabVIEW client version is incompatible with the compile server version. |
| −61303 | File operation received an empty path. |
| −61302 | Changing the logging enable requires a restart. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61301 | A reference was accessed that was not allocated. An internal software error has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61300 | User cancelled operation in progress. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/fifo-error-codes.html language=enus -->
## TOPIC 00026: FIFO Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/fifo-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/fifo-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FIFOs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61504 Unsupported FIFO method. The Flush method is not supported on the current target. Specify another target if you want to use the Flush method, or you

### FIFO Error Codes (FPGA Module)

FIFOs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61504 | Unsupported FIFO method. The Flush method is not supported on the current target. Specify another target if you want to use the Flush method, or you can specify another FIFO method. |
| −61413 | FIFO with handshaking interface is outside a single-cycle Timed Loop. FIFOs do not support the handshaking interface outside of single-cycle Timed Loops. Place the FIFO inside a single-cycle Timed Loop, or use the timeout interface. |
| −61412 | Missing feedback node after Ready For Input terminal. You must connect a feedback node after the Ready For Input terminal for FIFO Write methods that use the handshaking interface. |
| −61411 | FIFO invokes methods with incompatible interfaces. FIFOs cannot invoke Write/Read methods that use a combination of the handshaking interface and the timeout interface. Specify the same interface for all Write/Read methods invoked by this FIFO. |
| −61410 | Target does not support the handshaking interface on this FIFO. Your target does not support the handshaking interface on this type of FIFO. To use the handshaking interface, specify another type of FIFO. Tip: All targets support the handshaking interface on target-scoped FIFOs. |
| −61099 | Built-in FIFO used in external clock domain. A FIFO configured with built-in control logic is used in an external clock domain. You can use only slice fabric for FIFO control logic when the FIFO is in a clock domain that might be stopped during reset, including all external clock domains. In the FIFO Properties dialog box, change the control logic to slice fabric. |
| −61088 | Built-in FIFO not supported on current target. The current target does not support built-in control logic for FIFOs. In the FIFO Properties dialog box, change the Control Logic to Slice Fabric or Target Optimal. |
| −61066 | Incompatible clock domains between FIFO count method and FIFO write/read method. The Get Number of Elements to Write method must be in the same clock domain as the Write method. The Get Number of Elements to Read method must be in the same clock domain as the Read method. |
| −61053 | Insufficient DMA channels available. The application is requesting more DMA channels than the target hardware supports. These channels may be requested by different FPGA FIFO items in the project or by other components. |
| −61052 | FIFO missing a function. The <Scope> FIFO needs to have both a Read method and a Write method present on the block diagram. Add a <PortType> function on the block diagram for this FIFO. |
| −61051 | Multiple FIFOs using the same DMA channel. At least one DMA channel is used by several FIFOs, which is not supported. Configure FIFOs to use a unique DMA channel. |
| −61050 | Clock domain crossing is not supported for FIFO implementation. The <Scope> FIFO is configured to use an implementation of <MemoryType> but has read and write interfaces in different clock domains. If you want to read and write in different clock domains, select Block Memory from the Implementation pull-down menu in the FIFO Properties dialog box for the <Scope> FIFO . |
| −61020 | FIFO timeout not supported. The selected FIFO function attempts to block execution with a non-zero timeout. Objects inside the single-cycle Timed Loop cannot block execution. When using an FPGA FIFO function inside a single-cycle Timed Loop, wire a constant of zero to the Timeout input. Otherwise, replace the Timed Loop with a While Loop. |
| −61013 | The FIFO Method Node reached the timeout before being able to access the FIFO. This error is due to another FIFO Method Node accessing the same FIFO and not completing before the current method timed out. |
| −61012 | The FPGA VI reference used to initialize the FIFO is no longer valid. |
| −61010 | You are trying to read from, write to, or close a FIFO that has not been initialized by the InitFIFO method. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/fpga-desktop-execution-node-error-codes.html language=enus -->
## TOPIC 00027: FPGA Desktop Execution Node Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/fpga-desktop-execution-node-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/fpga-desktop-execution-node-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Desktop Execution Node can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61449 The FPGA VI has finished executing. The Desktop Execution Node attempted to update the simulation, but the FPGA VI has alr

### FPGA Desktop Execution Node Error Codes (FPGA Module)

The FPGA Desktop Execution Node can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61449 | The FPGA VI has finished executing. The Desktop Execution Node attempted to update the simulation, but the FPGA VI has already finished executing. Ensure that Desktop Execution Node updates only occur while the FPGA VI is running. Additionally, if you want to simulate your code continuously, you must place your LabVIEW FPGA code inside a While Loop. |
| −61448 | The simulation is not running. The FPGA simulation is not running. This can occur when the Desktop Execution Node tries to write to or read from a resource after the FPGA VI finishes executing. Verify that the FPGA VI is still running when the Desktop Execution Node attempts to interact with it. |
| −61447 | LabVIEW cannot locate the VI. The Desktop Execution Node is configured to execute a VI that LabVIEW cannot locate. You must reconfigure the Desktop Execution Node to point to a valid VI. |
| −61446 | The execution mode is invalid for the Desktop Execution Node. The selected target is set to execute in an execution mode that does not support the Desktop Execution Node. Change the execution mode to Simulation (Simulated I/O) to use the Desktop Execution Node. |
| −61444 | The Desktop Execution Node is misconfigured. The Desktop Execution Node is set to write to or read from a control, indicator, or I/O resource that either does not exist or has changed data types. Reconfigure the Desktop Execution Node and run the simulation again. |
| −61443 | The simulation has exceeded the maximum simulated time. The simulation has exceeded the maximum simulated time of 9223372036854775807 ps. LabVIEW will now abort the simulation. |
| −61442 | The FPGA Desktop Execution Node cannot run the configured VI. The FPGA Desktop Execution Node cannot run the configured VI because it or another VI is already running under the selected FPGA target. Stop all executing VIs under the FPGA target to run the FPGA Desktop Execution Node. |
| −61441 | Another FPGA VI for this target is already executing on the development computer. Stop the other VI before running this VI. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/fpga-interface-error-codes.html language=enus -->
## TOPIC 00028: FPGA Interface Error Codes (FPGA Interface)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/fpga-interface-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/fpga-interface-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Interface can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61506 The FPGA VI configured for running in simulation mode contains controls or indicators with duplicate names. The Read/Write function can

### FPGA Interface Error Codes (FPGA Interface)

The FPGA Interface can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61506 | The FPGA VI configured for running in simulation mode contains controls or indicators with duplicate names. The Read/Write function cannot read from or write to controls or indicators with duplicate names. Rename the controls or indicators. |
| −61460 | Control and indicator names with newline characters are only supported when the VI execution mode is set to Simulation (Simulated I/O) and the FPGA VI reference is configured for Dynamic mode. |
| −61251 | The bitfile is incompatible with the configuration of the FPGA interface reference wire. |
| −61221 | Close and reset is not supported when the FPGA target execution mode is configured to Third-Party Simulation. |
| −61219 | The number of elements requested must be less than or equal to the number of unacquired elements left in the host memory DMA FIFO. There are currently fewer unacquired elements left in the FIFO than are being requested. Use the Delete Data Value Reference function to release some acquired elements before acquiring more elements. |
| −61218 | FIFO.Configure is not supported when configured with greater than 65536 elements and when the FPGA target execution mode is configured to Third-Party Simulation. |
| −61217 | A session cannot be closed or reset and a bitfile cannot be downloaded while DMA FIFO region references are outstanding for the specified session. Use a Delete Data Value Reference function to delete any regions acquired from Acquire Read Region or Acquire Write Region before taking any of these actions. |
| −61216 | A gated clock has violated the handshaking protocol. If you are using external gated clocks, ensure that they follow the required clock gating protocol. If you are generating your clocks internally, please contact National Instruments Technical Support. |
| −61215 | Bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops can run only once. Download the bitfile again before re-running the VI. |
| −61214 | For bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops, LabVIEW FPGA does not support this method prior to running the bitfile. |
| −61213 | LabVIEW FPGA does not support Close and Reset if Last Reference for bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops. Instead, right-click the Close FPGA VI Reference function and select Close. |
| −61212 | LabVIEW FPGA does not support the Abort method for bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops. |
| −61211 | LabVIEW FPGA does not support the Reset method for bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops. |
| −61210 | There was an error initializing the LabVIEW FPGA Simulation. |
| −61209 | This function is not supported when the FPGA target execution mode is configured to Execute VI on Third-Party Simulator. |
| −61208 | This function is supported only when the FPGA VI reference is configured for Dynamic mode and the FPGA target execution mode is configured to Execute VI on Third-Party Simulator. |
| −61206 | The configured item does not exist. |
| −61205 | An item of the selected name is present but is a different data type than that configured in the Open FPGA VI Reference. |
| −61204 | The operation could not be performed because the FPGA is busy operating in Simulation mode. Stop all activities on the FPGA before requesting this operation. |
| −61203 | The operation could not be performed because the FPGA is busy operating in Interactive mode. Stop all activities on the FPGA before requesting this operation. |
| −61202 | LabVIEW could not perform the operation because an FPGA VI reference to another VI is currently open. You must close the currently open FPGA VI reference before attempting to perform this operation. |
| −61201 | The chassis is in Scan Interface programming mode. In order to run FPGA VIs, you must go to the chassis properties page, select FPGA programming mode, and deploy the settings. |
| −61200 | The operation could not be performed because the FPGA is busy operating in FPGA Interface C API mode. Stop all activities on the FPGA before requesting this operation. |
| −61183 | The transfer function order exceeds the maximum order allowed. |
| −61182 | The transfer function is improper. The order of the numerator must be less than or equal to the order of the denominator. |
| −61181 | The notch width or Q factor must be greater than zero. |
| −61180 | All frequencies, f, within the notch region must meet: 0<f< fs/2, where fs is the sample rate. |
| −61170 | The real and imaginary input data arrays must be the same size. |
| −61169 | The input parameter is not achievable on the FPGA at the given clock rate. |
| −61168 | The channel index input is out of the range of the configured number of channels. |
| −61167 | This function is not supported when the FPGA target is configured for Simulation. |
| −61165 | You cannot execute this FPGA VI for Simulation because the FPGA VI is broken. |
| −61159 | This function is not supported when the FPGA target is configured for Simulation with Real I/O. |
| −61141 | The operation could not be performed because the FPGA is busy. Stop all activities on the FPGA before requesting this operation. If the target is in Scan Interface programming mode, put it in FPGA Interface programming mode. If RIO Device Setup or MAX is currently open for downloading a bitfile to flash memory on the device, wait until the download ends. |
| −61078 | The requested memory could not be allocated. |
| −61077 | Terminated DMA FIFO. The FPGA was reconfigured while the DMA FIFO was in use. |
| −61076 | The DMA transfer did not complete within the timeout period. |
| −61075 | The DMA transfer was aborted and did not complete. |
| −61074 | The timeout parameter must be -1, 0, or a positive integer. |
| −61073 | The number of elements to read or write must be less than or equal to the depth of the host memory DMA FIFO. |
| −61072 | The requested FIFO depth is invalid. It is either 0 or an amount not supported by the hardware. |
| −61071 | The selected DMA FIFO was not found in the bitfile or FPGA design or is out of sync with the bitfile. |
| −61059 | The selected control was not found or is out of sync. |
| −61021 | FPGA Interface is out of date with the FPGA VI. Right-click and select Refresh. |
| −61017 | You must recompile the VI for the selected target. |
| −61016 | You must compile the VI for this target. |
| −61015 | No bitfile was found for download. You must compile the VI for this target. |
| 61003 | The FPGA VI specified by the Invoke Method function with the Run method is already running. The interaction of the FPGA VI and the host VI might produce unexpected results. For example, executing this host VI may modify front panel values on the running FPGA VI. User interaction with the front panel of the FPGA VI may affect the execution of the host VI. Terminating either the FPGA VI or the host VI may terminate the other. |
| 61060 | The Wait on IRQ method timed out before the specified interrupt was received. |
| 61211 | Multiple resources with the same name are present in this VI. The Dynamic Mode of the FPGA Interface can only access a single resource of a given name. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/fpga-module-error-codes.html language=enus -->
## TOPIC 00029: FPGA Module Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/fpga-module-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/fpga-module-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page describes error codes specific to the LabVIEW FPGA Module. The error code tables are arranged in ascending order, from negative to positive values. You also can define custom error codes.

### FPGA Module Error Codes (FPGA Module)

This page describes [error codes](/csh?productcategories=147794&context=lvcore_lvhowto_error_code_ranges) specific to the LabVIEW FPGA Module. The error code tables are arranged in ascending order, from negative to positive values. You also can [define custom error codes](/csh?productcategories=147794&context=lvcore_lverror_creating_user_defined_erro).

- [Clock Error Codes (FPGA Module)](../errors/clock-error-codes.html)
- [Code Generation Error Codes (FPGA Module)](../errors/code-generation-error-codes.html)
- [Compilation Error Codes (FPGA Module)](../errors/compilation-error-codes.html)
- [Compile Server Error Codes (FPGA Module)](../errors/compile-server-error-codes.html)
- [FIFO Error Codes (FPGA Module)](../errors/fifo-error-codes.html)
- [FPGA Desktop Execution Node Error Codes (FPGA Module)](../errors/fpga-desktop-execution-node-error-codes.html)
- [FPGA Interface Error Codes (FPGA Interface)](../errors/fpga-interface-error-codes.html)
- [General FPGA Module Error Codes (FPGA Module)](../errors/general-fpga-module-error-codes.html)
- [IP Integration Node Error Codes (FPGA Module)](../errors/ip-integration-node-error-codes.html)
- [Memory Error Codes (FPGA Module)](../errors/memory-error-codes.html)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/general-fpga-module-error-codes.html language=enus -->
## TOPIC 00030: General FPGA Module Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/general-fpga-module-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/general-fpga-module-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Module can return the following general error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61501 Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.c

### General FPGA Module Error Codes (FPGA Module)

The FPGA Module can return the following general error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61501 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information: The XDC constraints file is missing a required macro (e.g. <macro_ClipConstraints>). |
| −61500 | An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with the following information: LabVIEW could not read a CLIP XML file. |
| −61499 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support. |
| −61498 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: Required tag was not found in the resource file. |
| −61497 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: An unsupported register offset was requested. |
| −61496 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: An unexpected case was reached. |
| −61495 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: A path tag specified a value that is not a path. |
| −61494 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: An IP Generator VI did not match the required interface. |
| −61493 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: The specified IP Generator VI could not be found. |
| −61492 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: Error accessing FPGA provider. |
| −61491 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: An IP Generator is missing the required VI Path Tag. |
| −61488 | An internal software error in the LabVIEW FPGA Module has occurred. Please contact National Instruments technical support at ni.com/support with following information: A required XML tag was not found. |
| −61445 | The handshake is outside a single-cycle Timed Loop. Handshake items are supported only inside a single-cycle Timed Loop. |
| −61405 | The operation failed because you do not have a physical target specified for this FPGA target. Right-click the FPGA target in the Project Explorer window, select Properties, and enter an FPGA target resource name in the Resource text box. |
| −61404 | LabVIEW encountered a target-specific error or warning. |
| −61403 | LabVIEW is unable to interact with the current target because a required file is missing or inaccessible. Check that the FPGA target-specific driver software is installed correctly. |
| −61402 | LabVIEW lost communication with the device. The resource for the target was disconnected or removed. If the target is located remotely, the remote system might be turned off or there might be a network problem. |
| −61400 | Operation failed because the type of the hardware specified in the project and/or in the VI does not match the type of the hardware that was physically accessed. |
| −61399 | Execution of the FPGA VI on the development computer is not supported for the given item/node in the custom VI used for FPGA I/O. |
| −61398 | FPGA VI simulation failed because either the path for the specified custom VI for FPGA I/O simulation is missing or incorrect, or the specified custom VI for FPGA I/O simulation uses an incorrect connector pane. Check the custom VI path on the Simulation page of the target settings or check that the VI matches the required interface. |
| −61397 | Execution of the FPGA VI on the development computer failed because the custom VI for FPGA I/O does not conform to the calling requirements of the FPGA VI. |
| −61396 | Execution of the FPGA VI on the development computer failed because the custom VI for FPGA I/O called a VI or a function that returned an error. |
| −61395 | Execution of the FPGA VI on the development computer failed because the custom VI for FPGA I/O is not executable. |
| −61394 | This VI is supported only when the Execution Stage is Running. |
| −61239 | FIFO execution is only supported under FPGA targets. |
| −61238 | Memory execution is only supported under FPGA targets. |
| −61235 | The value wired into the FIFO In input of a FIFO Method Node corresponds to a FIFO item that does not match the configuration of the FIFO Method Node. |
| −61234 | The value wired into the FIFO In input of a FIFO Method Node does not correspond to any FIFO item in the project nor to any VI-defined FIFO. |
| −61233 | The value wired into the FIFO In input of a FIFO Method Node is an empty string. Make sure the wired value corresponds to a FIFO item in the project or to a VI-defined FIFO . |
| −61232 | The value wired into the Memory In input of a Memory Method Node corresponds to a memory item that does not match the configuration of the Memory Method Node. |
| −61231 | The value wired into the Memory In input of a Memory Method Node does not correspond to a memory item in the project or to any VI-defined memory. |
| −61230 | The value wired into the Memory In input of a Memory Method Node is an empty string. Make sure the wired value corresponds to a memory item in the project or a VI-defined memory. |
| −61229 | The value wired into the Register In input of a Register Method Node corresponds to a Register item that does not match the configuration of the Register Method Node. |
| −61228 | The value wired into the Register In input of a Register Method Node does not correspond to a Register item in the project or to any VI-defined Register. |
| −61227 | The value wired into the Register In input of a Register Method Node is an empty string. Make sure the wired value corresponds to a Register item in the project or to a VI-defined Register. |
| −61226 | The value wired into the Handshake In input of a Handshake Method Node corresponds to a Handshake item that does not match the configuration of the Handshake Method Node. |
| −61225 | The value wired into the Handshake In input of a Handshake Method Node does not correspond to a Handshake item in the project or to a VI-defined Handshake. |
| −61224 | The value wired into the Handshake In input of a Handshake Method Node is an empty string. Make sure the wired value corresponds to a Handshake item in the project or to a VI-defined Handshake. |
| −61223 | Register execution is only supported under FPGA targets. |
| −61222 | Handshake execution is only supported under FPGA targets. |
| −61207 | Internal error: DiagramReset did not clear within the timeout period. Please contact National Instruments Technical Support at ni.com/support. |
| −61199 | Execution has terminated because an I/O item that does not support execution on the development computer with real I/O has been encountered. You can execute an FPGA VI on the development computer with real I/O only when all of the I/O items you use in the FPGA VI support this mode of execution. |
| −61166 | HDL Interface Node file conflict. The file at <FilePath> conflicts with another file of that name that has already been created. Reconfigure the HDL Interface Node to point to the correct copy of the file or rename this file. |
| −61083 | A hardware clocking error occurred. A derived clock lost lock with its base clock during the execution of the FPGA VI. If any base clocks with derived clocks are referencing an external source, make sure that the external source is connected and within the supported frequency, jitter, accuracy, duty cycle, and voltage specifications. Also verify that the characteristics of the base clock match the configuration specified in the FPGA Base Clock Properties dialog box. If all base clocks with derived clocks are generated from free-running, on-board sources, please contact National Instruments technical support at ni.com/support. |
| −61082 | The current target does not have sufficient DMA control line sets available. Too many sets of DMA control lines have been requested or some requests are conflicting. The current target has <NUM_CONTROL_SETS> sets of DMA control lines. Review the list of requestors and remove one or more requestors to free up resources. |
| −61081 | Insufficient DMA channels available on the current target. Too many DMA channels have been requested or some requests are conflicting. The current target has <NUM_CHANNELS> DMA channels. Review the list of requested channels and remove one or more requestors to free resources. |
| −61080 | This target does not support FPGA interrupts. Remove the Interrupt node from your FPGA VI or use a target that supports FPGA interrupts. |
| −61079 | Insufficient address space on the FPGA for certain registers. The following components are present in the project: <IPNames>. The registers for each component require <RegisterBlockSizes> bytes of address space respectively. Total available address space on the FPGA for these registers is <AvailableAddressSpace> bytes. To free address space on the FPGA, remove some of the components listed above from the project and/or remove some of the controls and indicators from the top-level FPGA VI. |
| −61070 | The compiled bitfile for the specified VI contains information that is no longer valid or is corrupt. Recompile the VI to correct this error. |
| −61069 | This bitfile was created in a more recent version of LabVIEW and is incompatible with this version. |
| −61061 | Nested libraries are currently not supported in FPGA VIs. |
| −61048 | This target does not support DMA output from the host to the target. |
| −61046 | An error was detected in the communication between the host computer and the FPGA target. If you are using any external clocks, make sure they are connected and within the supported specifications. Also, verify that the rate of any external clocks match the specified clock rates. If you are generating your clocks internally, please contact National Instruments Technical Support. |
| −61045 | Usage of locals is restricted on synchronous controls/indicators. You cannot use a <readwrite> local on the <ctrlind> <Name>. Disable the Synchronous display option on the front panel object to solve the problem. |
| −61044 | The target does not have enough address space to accommodate the number of registers requested. The top-level FPGA VI front panel window contains too many controls and indicators. Group front panel objects into clusters to reduce the number of addresses needed to meet the communication needs of the application. |
| −61043 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information: These required tags in <Path>\\resource.xml file are missing:- <HardwareInterface> <Type> - <MostSignificantAddressLine> |
| −61042 | Internal software error(s). An internal software error has occurred. Please contact National Instruments technical support at ni.com/support with following information: The address requested <Address> for <RegName> is outside of the allowable range specified in <Path>\\resource.xml. Check the following tags: <MostSignificantAddressLine> and <LeastSignificantAddressLine>. |
| −61041 | Register name conflict. The front panel object <RegisterName> is conflicting with another register. Change the name of the front panel object to solve the problem. |
| −61040 | Unsupported access strategy. The selected access strategy is not supported by the selected communication interface. |
| −61024 | The device type that has been configured in this function does not match the actual type of the device. |
| −61023 | The device at the address that was configured in this function is no longer available. |
| −61022 | The FPGA target does not support running the FPGA VI in simulation mode. |
| −61019 | A digital I/O resource cannot be accessed in a single-cycle Timed Loop from both a Digital Output function and a Digital Port Output function. |
| −61018 | An error occurred downloading the VI to the FPGA device. Verify that the target is connected and powered and that the resource of the target is properly configured. |
| −61014 | The device does not exist or is not accepting any connections. Possible Reasons: - The resource for the target is not correct or the target resource specified does not exist. -If the target is located remotely: The remote system might be turned off. The software to use the device on the remote system might not be properly installed. You might not have networking properly configured to access the remote system. You might not have permissions properly set for any servers used to access the target. |
| 61004 | Occurrence traceback failed. The code generator was unable to trace back the use of an occurrence to a single generate occurrence. Occurrence is not statically bound. |
| 61005 | Bad Clock Rate for operation. The Clock Rate is not supported for analog components. |
| 61006 | The alias used by this FPGA Device I/O function, I/O Method Node, or I/O Property Node does not exist. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/ip-integration-node-error-codes.html language=enus -->
## TOPIC 00031: IP Integration Node Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/ip-integration-node-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/ip-integration-node-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The IP Integration Node can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61146 IP Integration Node must have a clock enable port. IP Integration Node does not have an IP Enable Signal selected but is placed in

### IP Integration Node Error Codes (FPGA Module)

The IP Integration Node can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61146 | IP Integration Node must have a clock enable port. IP Integration Node does not have an IP Enable Signal selected but is placed inside a Case structure. If you place an IP Integration Node inside a Case structure, you must specify a clock enable signal for the IP. To specify this signal, right-click the node, select Configure>>Clock and Enable Signals from the shortcut menu, and select the appropriate IP port(s) from the list of possible IP Enable Signal(s). If the IP does not have a port that maps to a clock enable signal, either move the IP Integration Node outside the Case structure or add such a port and specify it using the method described above. |
| −61098 | Derived clock required. You must wire a derived clock to the derived clock input of this IP Integration Node. |
| −61087 | Files changed requiring node reconfiguration. The following files have changed since the IP Integration Node was configured: <ChangedFiles> You must reconfigure the node to ensure the simulation model is up to date and the interface has not changed. |
| −61086 | File(s) do not exist. The following file(s) referenced by the IP Integration Node do not exist on disk: <MissingFiles> Reconfigure the IP Integration Node so it does not depend on these files or add the files on disk in a location the IP Integration Node expects. |
| −61085 | IP not supported on current target. The IP Integration Node is not configured to support the <FpgaDeviceFamily> FPGA device family used on the current FPGA target. |
| −61084 | Relative clock rate mismatch. The configured Relative clock rate of <ConfiguredRelativeClockRate> does not match the actual relative rate of <ActualRelativeClockRate> between the single-cycle Timed Loop clock and the clock specified as the Derived Multiple of Timed Loop Clock in the configuration of the IP Integration Node. Update the configured Relative clock rate or use a different derived clock. |
| −61068 | Unrelated over clock error. The clock wired to the overclock input is not related to the single-cycle Timed Loop clock on which the IP Integration Node or the Xilinx IP Integration Node runs. Select a clock that is related to the single-cycle Timed Loop clock. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=errors/memory-error-codes.html language=enus -->
## TOPIC 00032: Memory Error Codes (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `errors/memory-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/errors/memory-error-codes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Module can return the following memory error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −61408 Feedback Node initialization unsupported. Feedback Node initialization is not supported after the Read (Memory Method) for a memory

### Memory Error Codes (FPGA Module)

The FPGA Module can return the following memory error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −61408 | Feedback Node initialization unsupported. Feedback Node initialization is not supported after the Read (Memory Method) for a memory item with Cycles of read latency greater than 1. |
| −61220 | Invalid memory access. An attempt was made to access an address that is not available for the memory block. |
| −61096 | Memory is read-only with a type defined by a custom control. Memory is read-only and uses a custom control to define the type. Initializing memory with a type defined as a custom control is not supported. Change the data type of the memory. |
| −61089 | Uninitialized read-only memory. Memory is read-only but has no initial values specified. Provide initial values for the memory in the Memory Properties dialog box. |

Parent topic:

FPGA Module Error Codes (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/array-palette-details.html language=enus -->
## TOPIC 00033: Array Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/array-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/array-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Array Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. array constant Single-Cycle Timed Loop Supported. Usage You can view the memory implementation for an array

### Array Palette Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Array Functions](../targets/ni/fpga/menus/fpgacategories/programming/array-mnu.html) palette.

Note

array constant

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You can view the memory implementation for an array constant in the Context Help window when you hover over an array constant. To select a memory implementation, right-click an array and select Properties. Select Auto, Flip Flops, Look-Up Tables, or Block Memory on the FPGA Implementation tab of the Array Constant Properties dialog box. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function alone consumes no FPGA resources. However, when the array constant is wired to a logic operation, the array uses FPGA lookup table resources, except when implemented in block memory. Large arrays can be time and resource intensive if you perform logical operations on each element of the array. Avoid using arrays larger than 32 elements with 16-bit data unless you choose a block memory or look-up table implementation for array constants. |

Array Size

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Array Subset

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. The index and length inputs must be constant so that LabVIEW can determine the size of subarray. You can either wire constant values directly to this function, or rely on value propagation through constant folding. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Array To Cluster

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Build Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. If LabVIEW cannot infer a single size for an array, you may need to manually configure the array to a fixed size. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Cluster To Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. If LabVIEW cannot infer a single size for an array, you may need to manually configure the array to a fixed size. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Decimate 1D Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. You can use constant or non-constant inputs. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Delete From Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. The index and length inputs must be constant so that LabVIEW can determine the size of array w/ subset deleted and deleted portion. You can either wire constant values directly to this function, or rely on value propagation through constant folding. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Index Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function executes in one clock cycle, unless you wire a constant immediately into the index input, in which case the selection occurs at compile time and the function requires no clock cycles. |
| Resources | When the index is not constant, this function consumes FPGA resources in proportion to the size of the array and size of the element. When the index is constant, this function consumes no FPGA resources. |
| Notes | For large arrays, the Index Array function might not be able to execute within a single clock cycle, resulting in a compile-time error. |

Initialize Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. The dimension size input must be constant so that LabVIEW can determine the size of the output array. You can either wire constant values directly to this function, or rely on value propagation through constant folding. If LabVIEW cannot infer a single size for an array, you may need to manually configure the array to a fixed size. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |
| Notes | Although the size of the array you initialize does not affect the timing and resource usage of this function, large arrays can be time and resource intensive when you perform logical operations on the elements of the array. |

Insert Into Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If the index input is beyond the range of the array into which you are inserting elements, this function does not insert anything into the input array. The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. The index input must be constant so that LabVIEW can determine the size of the output array. You can either wire constant values directly to this function, or rely on value propagation through constant folding. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Interleave 1D Arrays

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. You can use constant or non-constant inputs. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Replace Array Subset

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. You can use constant or non-constant inputs. |
| Timing | This function executes in one clock cycle. However, if you wire a constant immediately into the index input, the selection occurs at compile time and the function requires no clock cycles. |
| Resources | When the index is not constant, this function consumes FPGA resources in proportion to the size of the array and size of new element/subarray. When the index is constant, this function consumes no FPGA resources. |
| Notes | For large arrays, the Replace Array Subset function might not be able to execute within a single clock cycle, resulting in a compile-time error. |

Reshape Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. The dimension size input must be constant so that LabVIEW can determine the size of the output array. You can either wire constant values directly to this function, or rely on value propagation through constant folding. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Reverse 1D Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. You can use constant or non-constant inputs. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Rotate 1D Array

| Single-Cycle Timed Loop | Not Supported. |
| --- | --- |
| Usage | If you wire a constant directly to the n input, this function is purely a wiring operation. Otherwise, this function implements an iterative algorithm, rotating the elements by one position each clock cycle. |
| Timing | If n is a constant, this operation requires no clock cycles. Otherwise, this operation takes n clock cycles to execute, plus three clock cycles of overhead. |
| Resources | If you wire a constant directly to the n input, this operation consumes no FPGA resources. Otherwise, this operation consumes FPGA resources in proportion to the size of the array. |

Split 1D Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. The index input must be constant so that LabVIEW can determine the size of the output array. You can either wire constant values directly to this function, or rely on value propagation through constant folding. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/assert-type-palette-details.html language=enus -->
## TOPIC 00034: Assert Type Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/assert-type-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/assert-type-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Assert Type palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. Assert Structural Type Match Single-Cycle Timed Loop Supported. Usage This function does nothing at run time. I

### Assert Type Palette Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Assert Type](../targets/ni/fpga/menus/fpgacategories/programming/compare/typeassert-mnu.html) palette.

Note

Assert Structural Type Match

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | This function does nothing at run time. It breaks the calling VI unless the two input data types are identical. |
| Timing | This function requires no clock cycles to execute because it does nothing at run time. |
| Resources | This function consumes no FPGA resources because it does nothing at run time. |

Assert Structural Type Mismatch

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | This function does nothing at run time. It breaks the calling VI if the input type is the same data type as any of the specified mismatch inputs. |
| Timing | This function requires no clock cycles to execute because it does nothing at run time. |
| Resources | This function consumes no FPGA resources because it does nothing at run time. |

Type Specialization Structure

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | When you use the Type Specialization structure in an FPGA VI, LabVIEW evaluates the compilation results at compile time and compiles only one subdiagram. |
| Timing | Entering and exiting this structure requires no time on the FPGA. |
| Resources | Only one subdiagram of the Type Specialization structure compiles to the FPGA. Inactive subdiagrams consume no FPGA resources. The Type Specialization structure itself also consumes no FPGA resources. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/boolean-palette-details.html language=enus -->
## TOPIC 00035: Boolean Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/boolean-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/boolean-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Boolean Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. The following details apply to all the Boolean functions, except the Compound Arithmetic function, Number

### Boolean Palette Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Boolean Functions](../targets/ni/fpga/menus/fpgacategories/programming/boolfunc-mnu.html) palette.

Note

The following details apply to all the Boolean functions, except the Compound Arithmetic function, Number To Boolean Array function, and True and False constants.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | For maximum time and resource efficiency, use Boolean functions inside a single-cycle Timed Loop. |
| Timing | Inside single-cycle Timed Loop--When you use Boolean functions inside a single-cycle Timed Loop, each Boolean operation adds slightly to the combinatorial logic delay of the single-cycle Timed Loop. Outside single-cycle Timed Loop--When you use Boolean functions outside a single-cycle Timed Loop, each Boolean operation requires one clock cycle. |
| Resources | Boolean functions consume significant FPGA resources only when you wire a large array to the input. Consider limiting arrays to conserve FPGA resources. |

Compound Arithmetic

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. When used in an FPGA VI, the Compound Arithmetic function might return different results for floating-point operations, as this function executes operations in a different order than when used on a host computer. |
| Timing | When placed inside a single-cycle Timed Loop, the combinatorial logic delay is logarithmically proportional to the number of inputs. |
| Resources | This function consumes FPGA resources in proportion to the number of inputs, N. Each operation receives dedicated hardware and the total number of operations is always N - 1. |

Number To Boolean Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. If LabVIEW cannot infer a single size for an array, you may need to manually configure the array to a fixed size. You cannot wire an array or cluster to this function. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

#### True and False Constants

The following details apply to the [True](/csh?productcategories=147794&context=lvcore_glang_true_constant) constant and the [False](/csh?productcategories=147794&context=lvcore_glang_false_constant) constant.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function alone consumes no FPGA resources. However, when you wire a True or False constant to a logical operation, the value is combined with the logical operation. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/channel-wire-endpoints-details.html language=enus -->
## TOPIC 00036: Channel Wire Endpoints Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/channel-wire-endpoints-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/channel-wire-endpoints-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the channel wire endpoints. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. Stream and Lossy Stream: Writer Endpoints The following details apply to the writer endpoints of the Stream and Lossy Strea

### Channel Wire Endpoints Details (FPGA Module)

This topic contains FPGA-specific information about the [channel wire endpoints](/csh?context=lvfpga_lvfpga_channel_wire_endpoint_fpga).

Note

#### Stream and Lossy Stream: Writer Endpoints

The following details apply to the writer endpoints of the [Stream](/csh?context=lvfpga_lvfpga_channel_stream_fpga) and [Lossy Stream](/csh?context=lvfpga_lvfpga_channel_lossy_stream_fpga) channels.

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | When used on FPGA, the size input has no default value and must be connected to a constant with a value greater than zero. For arrays, this endpoint supports only fixed-sized one-dimensional arrays of supported data types. This endpoint does not support variable-sized arrays even if the array resolves to a single size at compile time. This endpoint does not support LabVIEW classes. If you use this endpoint with the single-precision floating-point data type, refer to the following topics for resource use, latency, and single-cycle Timed Loop support implications. Using the Single-Precision Floating-Point Data Type Deciding Which Data Type to Use in FPGA Designs |
| Resources | This endpoint requires FPGA resources proportional to the number you specified in size. |
| Notes | A channel terminal of a non-reentrant subVI can be connected to only one channel. If a non-reentrant subVI is called from multiple locations, the channel wires connected to a given terminal must resolve to the same channel at compile time. |

#### Stream and Lossy Stream: Reader Endpoints

The following details apply to the reader endpoints of the [Stream](/csh?context=lvfpga_lvfpga_channel_stream_fpga) and [Lossy Stream](/csh?context=lvfpga_lvfpga_channel_lossy_stream_fpga) channels.

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | For arrays, this endpoint supports only fixed-sized one-dimensional arrays of supported data types. This endpoint does not support variable-sized arrays even if the array resolves to a single size at compile time. This endpoint does not support LabVIEW classes. If you use this endpoint with the single-precision floating-point data type, refer to the following topics for resource use, latency, and single-cycle Timed Loop support implications. Using the Single-Precision Floating-Point Data Type Deciding Which Data Type to Use in FPGA Designs |
| Resources | This endpoint shares resources with the writer endpoint used together in the channel instance. The writer endpoint requires FPGA resources proportional to the number you specified in size. |
| Notes | A channel terminal of a non-reentrant subVI can be connected to only one channel. If a non-reentrant subVI is called from multiple locations, the channel wires connected to a given terminal must resolve to the same channel at compile time. |

#### One Element Stream, Tag, and Accumulator Tag: All Endpoints

The following details apply to the [One Element Stream](/csh?context=lvfpga_lvfpga_channel_one_element_stream_fpga), [Tag](/csh?context=lvfpga_lvfpga_channel_tag_fpga), and [Accumulator Tag](/csh?context=lvfpga_lvfpga_channel_accumulator_fpga) endpoints.

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | For arrays, this endpoint supports only fixed-sized one-dimensional arrays of supported data types. This endpoint does not support variable-sized arrays even if the array resolves to a single size at compile time. This endpoint does not support LabVIEW classes. If you use this endpoint with the single-precision floating-point data type, refer to the following topics for resource use, latency, and single-cycle Timed Loop support implications. Using the Single-Precision Floating-Point Data Type Deciding Which Data Type to Use in FPGA Designs |
| Notes | A channel terminal of a non-reentrant subVI can be connected to only one channel. If a non-reentrant subVI is called from multiple locations, the channel wires connected to a given terminal must resolve to the same channel at compile time. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/cluster-class-palette-details.html language=enus -->
## TOPIC 00037: Cluster & Class Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/cluster-class-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/cluster-class-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Cluster & Class Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. The following details apply to all the Cluster & Class functions except the To More Specific Clas

### Cluster & Class Palette Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Cluster & Class Functions](../targets/ni/fpga/menus/fpgacategories/programming/cluster-mnu.html) palette.

Note

The following details apply to all the Cluster & Class functions except the To More Specific Class, To More Generic Class, Call Parent Class Method, and Cluster to Array functions.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | The Cluster & Class functions require no clock cycles to execute because they do not include internal registers. |
| Resources | The Cluster & Class functions consume no FPGA resources because they are purely wiring operations. |

The following details apply to the [To More Specific Class](/csh?productcategories=147794&context=lvcore_glang_to_more_specific_class) and [To More Generic Class](/csh?productcategories=147794&context=lvcore_glang_to_more_generic_class) functions.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This Cluster & Class function requires no clock cycles to execute because it does not include internal registers. |
| Resources | This Cluster & Class function consumes no FPGA resources because LabVIEW determines the actual class and creates a static reference before compiling the FPGA VI. |

Cluster to Array

The following details apply to the Cluster to Array function.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only 1-D fixed-size arrays. To make sure this function results in a fixed-size array output, open the VI Properties dialog box, select Execution from the Category pull-down menu, and place a check in the Autopreallocate arrays and strings checkbox. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Call Parent Class Method

The implementation details for the Call Parent Class Method function depend on the class method this function calls.

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/comparison-palette-details.html language=enus -->
## TOPIC 00038: Comparison Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/comparison-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/comparison-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Comparison Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. The following details apply to all the Comparison functions, except for the Fixed Point Overflow?, In

### Comparison Palette Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Comparison Functions](../targets/ni/fpga/menus/fpgacategories/programming/compare-mnu.html) palette.

Note

The following details apply to all the Comparison functions, except for the Fixed Point Overflow?, In Range and Coerce, Max & Min, and Not A Number/Path/Refnum? functions.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use Comparison functions inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the width of the data types you compare. Outside single-cycle Timed Loop--When you use Comparison functions outside a single-cycle Timed Loop, each Comparison function takes one clock cycle. If you use the Comparison functions with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | The Comparison functions use FPGA resources in proportion to the width of the data types you compare. |

Fixed-Point Overflow?

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

In Range and Coerce

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If the value of lower limit is greater than the value of upper limit, LabVIEW does not swap the values of lower limit and upper limit. You must change the values of lower limit and upper limit manually if you do not want the value of lower limit to be greater than the value of upper limit. You cannot wire an array or cluster to this function in a single-cycle Timed Loop. If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use Comparison functions inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the width of the data types you compare. Outside single-cycle Timed Loop--When you use Comparison functions outside a single-cycle Timed Loop, each Comparison function takes one clock cycle. If you use the Comparison functions with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | The Comparison functions use FPGA resources in proportion to the width of the data types you compare. |

Max & Min

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | This function does not support Compare Aggregates mode. If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use Comparison functions inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the width of the data types you compare. Outside single-cycle Timed Loop--When you use Comparison functions outside a single-cycle Timed Loop, each Comparison function takes one clock cycle. |
| Resources | The Comparison functions use FPGA resources in proportion to the width of the data types you compare. |

Not A Number/Path/Refnum?

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The FPGA Module supports only the Not A Number functionality. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes FPGA resources only when the input is single-precision floating-point (SGL). When the input is anything other than a SGL, the function returns a FALSE constant and is optimized out if not connected to other logic. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/conversion-palette-details.html language=enus -->
## TOPIC 00039: Conversion Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/conversion-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/conversion-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Conversion Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. The following details apply to all the Conversion functions, except the Boolean Array to Number, Numbe

### Conversion Palette Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Conversion Functions](../targets/ni/fpga/menus/fpgacategories/programming/numeric/convert-mnu.html) palette.

Note

The following details apply to all the Conversion functions, except the Boolean Array to Number, Number To Boolean Array, To Fixed-Point, and To Single Precision Float functions.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | The Conversion functions require no clock cycles to execute because they do not include internal registers. If you use the Conversion functions with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | The Conversion functions consume no FPGA resources because they are purely wiring operations. If you use the Conversion functions with the fixed-point data type, the overflow and rounding modes might impact resources. |

Boolean Array To Number

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. The Boolean Array To Number function converts fixed-size arrays by default to use the smallest unsigned integer representation that will fit the array size. |
| Timing | This function requires no clock cycles to execute because it does not include internal registers. |
| Properties Dialog Box | The data type of number changes based on the size of the array when the Adapt to source checkbox in the Output Configuration page contains a checkmark. The following list describes the relationship between the array size and the data type of number: If the array size is between 0 and 8, inclusive, number has a data type of U8. If the array size is between 9 and 16, inclusive, number has data type of U16. If the array is any other size, number has a data type of U32. For example, if Boolean array is a fixed-size array of size 9, number has a data type of U16. If the number of elements in your array is between 33 and 64, inclusive, and you want all of them to be represented in the number, you must uncheck the Adapt to source checkbox. If the number of elements in your array exceeds 64, some of the elements from the array will not be represented in the number. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Number To Boolean Array

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. If LabVIEW cannot infer a single size for an array, you may need to manually configure the array to a fixed size. You cannot wire an array or cluster to this function. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

To Fixed-Point

| Single-Cycle Timed Loop | Supported for fixed-point and integer inputs only. |
| --- | --- |
| Usage | This function does not support array inputs. However, you can pass array data to this function element-by-element if you meet the following criteria: You place the function inside a For Loop within a single-cycle Timed Loop You enable auto-indexing on the For Loop tunnels You use the function with other supported functions You do not include shift registers or Feedback Nodes |
| Timing | This function requires no clock cycles for fixed-point and integer inputs if you select the Wrap overflow mode and Truncate rounding mode. Other overflow and rounding modes might impact timing. This function requires multiple cycles to execute for single-precision floating-point inputs. |
| Resources | This function consumes no FPGA resources for fixed-point and integer inputs if you select the Wrap overflow mode and Truncate rounding mode. Other overflow and rounding modes might impact resources. This function consumes significant FPGA resources when the input type is single-precision floating-point in order to scale the significand to the appropriate output type. |
| Notes | You also can use the High Throughput To Fixed-Point function to perform fixed-point math and analysis on an FPGA target. |

To Single Precision Float

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires multiple cycles to execute for all input types. |
| Resources | This function consumes significant FPGA resources in order to normalize fixed-point or integer values and compute their exponents. Resource usage is roughly proportional to the width of the input fixed-point or integer value. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/data-manipulation-palette-details.html language=enus -->
## TOPIC 00040: Data Manipulation Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/data-manipulation-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/data-manipulation-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains detailed information about the objects on the Data Manipulation Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. Join Numbers Single-Cycle Timed Loop Supported. Usage N/A Timing This function requires no clock cyc

### Data Manipulation Palette Details (FPGA Module)

This topic contains detailed information about the objects on the [Data Manipulation Functions](../targets/ni/fpga/menus/fpgacategories/programming/advdata-mnu.html) palette.

Note

Join Numbers

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Logical Shift

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The logical shift operation shifts all bits including the sign bit of a signed integer. To preserve the sign of a signed integer, use the Scale By Power Of 2 function. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. |

Rotate

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. |

Rotate Left With Carry

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You cannot wire an array or cluster input to this function in a single-cycle Timed Loop. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Rotate Right With Carry

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You cannot wire an array or cluster input to this function in a single-cycle Timed Loop. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Split Number

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | This function supports array and cluster inputs of all data types except fixed-point. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Swap Bytes

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You cannot wire a fixed-point data type to this function. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Swap Words

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You cannot wire a fixed-point data type to this function. |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function consumes no FPGA resources because it is purely a wiring operation. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/dynamic-fpga-interface-cast.html language=enus -->
## TOPIC 00041: Dynamic FPGA Interface Cast Function

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/dynamic-fpga-interface-cast.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/dynamic-fpga-interface-cast.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Casts Session In to the data type of Type. This function only changes the type of elements that FPGA VI reference contains. This function does not convert data. Use this function with the FPGA Interface Dynamic Refnum constant to create a dynamic host interface. Some FPGA targets might not support t

### Dynamic FPGA Interface Cast Function

Casts **Session In** to the data type of **Type**. This function only changes the type of elements that FPGA VI reference contains. This function does not convert data. Use this function with the FPGA Interface Dynamic Refnum constant to create a dynamic host interface. Some FPGA targets might not support this function.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='icon' src='dynamic-fpga-interface-cast.png']

#### Inputs/Outputs

| Type — Session In is the FPGA VI reference you want to convert to Type. Session In — Type is the reference data type to which you want to convert the FPGA VI reference. Wire any constant or control to Type to set the reference data type to which you want to convert the FPGA VI reference. Session Out — Session Out is the FPGA VI reference Session In converted to the same reference data type as Type. |
| --- |

Use this function with an [FPGA Interface Dynamic Refnum](../vi-lib/rvi/interface/nifpgainterfacerefnumconstant-vi.html) wired to **Type** to specify the interface for the FPGA VI reference. The interface can contain elements such as controls, indicators, DMA channels, and target-specific methods.

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/fixed-point-palette-details.html language=enus -->
## TOPIC 00042: Fixed-Point Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/fixed-point-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/fixed-point-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Fixed-Point Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. The following details apply to all the Fixed-Point functions except the Reinterpret Number function.

### Fixed-Point Palette Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Fixed-Point Functions](../targets/ni/fpga/menus/fpgacategories/programming/numeric/fxp-mnu.html) palette.

Note

The following details apply to all the Fixed-Point functions except the Reinterpret Number function.

The Fixed-Point functions do not support array inputs. However, you can pass array data to these functions element-by-element if you meet the following criteria:

- You place the function inside a For Loop within a single-cycle Timed Loop
- You enable auto-indexing on the For Loop tunnels
- You use the function with other supported functions
- You do not include shift registers or Feedback Nodes

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/fpga-vi-and-function-details.html language=enus -->
## TOPIC 00043: FPGA VI and Function Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/fpga-vi-and-function-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/fpga-vi-and-function-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Because FPGAs operate differently than standard PC processors, you need to keep in mind different considerations when you create a VI to run on an FPGA target versus when you create a VI to run on a PC. The following palettes contain objects with FPGA-specific considerations. Array Assert Type Boole

### FPGA VI and Function Details (FPGA Module)

Because FPGAs operate differently than standard PC processors, you need to keep in mind different considerations when you create a VI to run on an FPGA target versus when you create a VI to run on a PC. The following palettes contain objects with FPGA-specific considerations.

- Array
- Assert Type
- Boolean
- Cluster & Class
- Comparison
- Conversion
- Fixed-Point
- Data Manipulation
- Math & Scientific Constants
- Numeric
- Structures

The [channel wire endpoints](/csh?context=lvfpga_lvfpga_channel_wire_details) also have FPGA-specific considerations.

The details for each object include a table with the following FPGA-specific considerations.

- Single-Cycle Timed Loop —Specifies whether you can use the VI or function inside a single-cycle Timed Loop.
- Usage —Contains information about the behavior of the VI or function when used in an FPGA VI.
- Timing —Contains information about the amount of time the VI or function takes to execute. Inside the single-cycle Timed Loop, this information refers to the combinatorial path length of the VI or function. Outside the single-cycle Timed Loop, this information refers to the number of clock cycles a VI or function takes to execute.
- Properties Dialog Box —Contains information about the behavior of the VI or function when you enable the Adapt to source checkbox in the Properties dialog box.
- Resources —Contains information about the FPGA resource usage of the VI or function.
- Notes —Contains additional useful information that you can refer to when using the VI or function.

- [Array Palette Details (FPGA Module)](../functions/array-palette-details.html)
- [Assert Type Palette Details (FPGA Module)](../functions/assert-type-palette-details.html)
- [Boolean Palette Details (FPGA Module)](../functions/boolean-palette-details.html)
- [Channel Wire Endpoints Details (FPGA Module)](../functions/channel-wire-endpoints-details.html)
- [Cluster & Class Palette Details (FPGA Module)](../functions/cluster-class-palette-details.html)
- [Comparison Palette Details (FPGA Module)](../functions/comparison-palette-details.html)
- [Conversion Palette Details (FPGA Module)](../functions/conversion-palette-details.html)
- [Data Manipulation Palette Details (FPGA Module)](../functions/data-manipulation-palette-details.html)
- [Fixed-Point Palette Details (FPGA Module)](../functions/fixed-point-palette-details.html)
- [Math & Scientific Constant Details (FPGA Module)](../functions/math-scientific-constant-details.html)
- [Numeric Palette Details (FPGA Module)](../functions/numeric-palette-details.html)
- [Structures Palette Details (FPGA Module)](../functions/structures-palette-details.html)

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/math-scientific-constant-details.html language=enus -->
## TOPIC 00044: Math & Scientific Constant Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/math-scientific-constant-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/math-scientific-constant-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains FPGA-specific information about the objects on the Math & Scientific Constants palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. The following details apply when you use these constants in an FPGA VI. Single-Cycle Timed Loop

### Math & Scientific Constant Details (FPGA Module)

This topic contains FPGA-specific information about the objects on the [Math & Scientific Constants](/csh?context=lvfpga_lvfpga_fpga_mathandscientific_palette) palette.

Note

The following details apply when you use these constants in an FPGA VI.

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The default data type for these constants is single-precision floating-point (SGL). |
| Timing | These constants require no clock cycles to execute because they do not include internal registers. |
| Resources | These constants alone consume no FPGA resources. However, if you wire a constant to a logical operation, FPGA lookup table resources store the constant value. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/numeric-palette-details.html language=enus -->
## TOPIC 00045: Numeric Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/numeric-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/numeric-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains detailed information about the objects on the Numeric Functions palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. Absolute Value Single-Cycle Timed Loop Supported. Usage If you use this function with the single-precision flo

### Numeric Palette Details (FPGA Module)

This topic contains detailed information about the objects on the [Numeric Functions](../targets/ni/fpga/menus/fpgacategories/programming/numeric-mnu.html) palette.

Note

Absolute Value

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

Add

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x or y, whichever data type is larger. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x or y, whichever data type is larger. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

Compound Arithmetic

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. When used in an FPGA VI, the Compound Arithmetic function might return different results for floating-point operations, as this function executes operations in a different order than when used on a host computer. |
| Timing | When placed inside a single-cycle Timed Loop, the combinatorial logic delay is logarithmically proportional to the number of inputs. |
| Resources | This function consumes FPGA resources in proportion to the number of inputs, N. Each operation receives dedicated hardware and the total number of operations is always N - 1. |

Decrement

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

Divide

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | This function usually requires clock cycles in proportion to the number of bits in x/y. If you use this function with the fixed-point data type and select the Round-Half-Up rounding mode, the function requires one more clock cycle than the other two rounding modes. |
| Resources | Division is an expensive operation on the FPGA. In general, the function requires FPGA resources proportional to the number of bits in x, y, and x/y. If you use this function with the fixed-point data type, the rounding mode might impact resources. |
| Notes | You also can use the High Throughput Divide function to perform fixed-point math and analysis on an FPGA target. |

Enum Constant

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute and never includes an internal register. |
| Resources | This function alone consumes no FPGA resources. However, when you wire the constant to a logical operation, the constant uses FPGA lookup table resources. |

Increment

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

#### Machine Epsilon, Negative Infinity, and Positive Infinity

The following details apply to [Machine Epsilon](/csh?productcategories=147794&context=lvcore_glang_machine_epsilon), [Negative Infinity](/csh?productcategories=147794&context=lvcore_glang_numeric_constants), and [Positive Infinity](/csh?productcategories=147794&context=lvcore_glang_numeric_constants)

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | The default data type for these constants is single-precision floating-point (SGL). |
| Timing | These constants require no clock cycles to execute because they do not include internal registers. |
| Resources | These constants alone consume no FPGA resources. However, if you wire one of these constants to a logical operation, FPGA lookup table resources store the constant value. |

Multiply

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | Most FPGA targets contain a limited number of embedded multipliers. The FPGA Module compiler uses embedded multipliers to implement multiply operations until it occupies all the embedded multipliers. If the FPGA target runs out of embedded multipliers, the compiler uses generic logic gates instead, and the Multiply function becomes expensive in terms of FPGA resource usage. If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x or y, whichever data type is larger. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x or y, whichever data type is larger. Consider using the smallest data type possible to optimize FPGA VIs. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |
| Notes | You also can use the High Throughput Multiply function to perform fixed-point math and analysis on an FPGA target. |

Negate

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

numeric constant

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function alone consumes no FPGA resources. However, if you wire a Numeric constant to a logical operation, FPGA lookup table resources store the constant value. |

Quotient & Remainder

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | Division is a relatively expensive operation on the FPGA in terms of both resource usage and time. Use the Scale By Power of 2 function with n wired as a negative constant to increase efficiency when dividing by a power of two. This function does not support the single-precision floating-point data type. |
| Timing | This function requires clock cycles and registers in proportion to the number of bits in x or y, whichever data type is larger. Each clock cycle corresponds to one register. |
| Resources | This function requires FPGA resources proportional to the number of bits in x or y, whichever data type is larger. |

Reciprocal

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | This function normally requires clock cycles in proportion to the number of bits in 1/x. If you use this function with the fixed-point data type and select the Round-Half-Up rounding mode, the function requires one more clock cycle than the other two rounding modes. |
| Resources | Division is an expensive operation on the FPGA. In general, the function requires FPGA resources proportional to the number of bits in x and 1/x. If you use this function with the fixed-point data type, the rounding mode might impact resources. |
| Notes | You also can use the High Throughput Reciprocal function to perform fixed-point math and analysis on an FPGA target. |

Ring Constant

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This function alone consumes no FPGA resources because it is purely a wiring operation. |

Round Toward -Infinity

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | This function does not support the single-precision floating-point data type. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. The overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. The overflow and rounding modes might impact resources. |

Round Toward +Infinity

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | This function does not support the single-precision floating-point data type. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. The overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. The overflow and rounding modes might impact resources. |

Round To Nearest

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | This function does not support the single-precision floating-point data type. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in number. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. The overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in number. |

Scale By Power Of 2

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you wire a constant directly to the n input, this function uses no space on the FPGA and requires no clock cycles. If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--If n is not a constant and you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--If n is not a constant and you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. |
| Resources | If n is not a constant, this function requires FPGA resources in proportion to the number of bits in x. |

Sign

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in number. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in number. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

Square

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | Most FPGA targets contain a limited number of embedded multipliers. The FPGA Module compiler uses embedded multipliers to implement multiply operations until it occupies all the embedded multipliers. If the FPGA target runs out of embedded multipliers, the compiler uses generic logic gates instead, and the Square function becomes expensive in terms of FPGA resource usage. If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x. Consider using the smallest data type possible to optimize FPGA VIs. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

Square Root

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | If the fractional word length of sqrt(x) is larger than half of the fractional word length of x, the function requires clock cycles in proportion to the number of bits in sqrt(x). Otherwise, the required clock cycles are proportional to the number of bits in x. |
| Resources | In general, the function requires FPGA resources proportional to the number of bits in x and sqrt(x). If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |
| Notes | You also can use the High Throughput Square Root function to perform fixed-point math and analysis on an FPGA target. |

Subtract

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | If you use this function with the single-precision floating-point data type, refer to the Using the Single-Precision Floating-Point Data Type and Deciding Which Data Type to Use in FPGA Designs topics for resource use, latency, and single-cycle Timed Loop support implications. |
| Timing | Inside single-cycle Timed Loop--When you use this function inside a single-cycle Timed Loop, the combinatorial logic delay is proportional to the number of bits in x or y, whichever data type is larger. Outside single-cycle Timed Loop--When you use this function outside a single-cycle Timed Loop, it takes one clock cycle and uses one register. If you use this function with the fixed-point data type, the overflow and rounding modes might impact timing. |
| Resources | This function requires FPGA resources proportional to the number of bits in x or y, whichever data type is larger. If you use this function with the fixed-point data type, the overflow and rounding modes might impact resources. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/open-dynamic-bitfile-reference.html language=enus -->
## TOPIC 00046: Open Dynamic Bitfile Reference Function

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/open-dynamic-bitfile-reference.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/open-dynamic-bitfile-reference.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to an FPGA bitfile at run time and returns a dynamic FPGA interface. Use this function in place of the Open FPGA VI Reference function when you want to open a bitfile by path at run time. You must open a reference to the FPGA target before the host VI can communicate with the FPGA

### Open Dynamic Bitfile Reference Function

Opens a reference to an FPGA bitfile at run time and returns a dynamic FPGA interface. Use this function in place of the Open FPGA VI Reference function when you want to open a bitfile by path at run time.

You must open a reference to the FPGA target before the host VI can communicate with the FPGA VI. Only targets that use NI-RIO driver software support the Open Dynamic Bitfile Reference function.

Note

interface with an FPGA bitfile even if you do not have the FPGA Module installed

[IMAGE alt='icon' src='open-dynamic-bitfile-reference.png']

#### Inputs/Outputs

| Type — Type specifies the reference data type to which you want to convert the dynamic interface reference. Wire any constant or control to Type to set the reference data type to which you want to convert the dynamic FPGA interface. Right-click the control or constant and select Configure FPGA VI Reference to configure the interface. The reference this function returns is cast to the data type you wire to Type. If you do not specify a data type, this function returns an empty dynamic interface reference. Device address — Device address specifies the address of the FPGA target. Bitfile path — Bitfile path specifies the path to the bitfile. Bitfiles must have a .lvbitx extension. Run When Loaded — Run When Loaded specifies whether the bitfile runs automatically after downloading. The availability of this option varies by FPGA target. The default is TRUE. If you set the value to FALSE, the FPGA VI waits to execute until you set the value to TRUE. Error In — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Bitfile reference out — Bitfile reference out returns a reference to a bitfile. Error Out — error out contains error information. This output provides standard error out functionality. |
| --- |

You can download and run only one FPGA VI at a time on a single FPGA target. If you attempt to download a second VI to the FPGA target while the first FPGA VI is still in use, LabVIEW reports an error and the download fails.

Place and wire a [Close FPGA VI Reference](/csh?context=lvfpgahost_close_vi_reference) function for every Open Dynamic Bitfile Reference function in a host VI. When the Open Dynamic Bitfile Reference function first executes, the function checks whether the compiled FPGA VI already exists on the FPGA target. If the compiled FPGA VI is not on the FPGA target, the Open Dynamic Bitfile Reference function downloads the compiled FPGA VI to the FPGA target.

Use this function with an [FPGA Interface Dynamic Refnum](/csh?context=lvfpgahost_fpga_dyn_refnum_constant) wired to **Type** to specify the interface for the FPGA VI reference. The interface can contain elements such as controls, indicators, DMA channels, and target-specific methods.

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=functions/structures-palette-details.html language=enus -->
## TOPIC 00047: Structures Palette Details (FPGA Module)

- bundle_id: `lvfpga-api-ref`
- source_path: `functions/structures-palette-details.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/functions/structures-palette-details.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This topic contains detailed information about the objects on the Structures palette. The information in this topic is subject to change with each version of the LabVIEW FPGA Module. Case Structure Single-Cycle Timed Loop Supported. Usage N/A Timing Inside single-cycle Timed Loop--When you use a Cas

### Structures Palette Details (FPGA Module)

This topic contains detailed information about the objects on the [Structures](../targets/ni/fpga/menus/fpgacategories/programming/structs-mnu.html) palette.

Note

Case Structure

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | N/A |
| Timing | Inside single-cycle Timed Loop--When you use a Case structure inside a single-cycle Timed Loop, the combinatorial logic delay required to evaluate the case selector is proportional to the width of the selector input data type and the number of cases. The combinatorial logic delay introduced by output tunnels is proportional to the number of cases. Outside single-cycle Timed Loop--When you use a Case structure outside a single-cycle Timed Loop, it takes one clock cycle to evaluate the case selector. Output tunnels require no clock cycles to execute and never include a register. |
| Resources | The case selector requires FPGA resources proportional to the width of the input data type and the number of cases. Output tunnels require FPGA resources proportional to the width of the output data type and the number of cases. |
| Notes | Complex Case structures can lead to long combinatorial paths and limit the maximum clock rate of a clock domain. |

Conditional Disable Structure

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | When you use the Conditional Disable structure in an FPGA VI, LabVIEW evaluates the conditions at compile time and compiles only one subdiagram. |
| Timing | Entering and exiting this structure requires no time on the FPGA. |
| Resources | Only one subdiagram of the Diagram Disable structure compiles to the FPGA. Inactive subdiagrams consume no FPGA resources. The Diagram Disable structure itself also consumes no FPGA resources. |

Diagram Disable Structure

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | When you use the Diagram Disable structure in an FPGA VI, front panel objects inside the structure do compile. |
| Timing | Because the objects inside the Diagram Disable structure do not compile on the FPGA, this structure takes no time to execute. |
| Resources | Each front panel object in a Diagram Disable structure consumes FPGA resources. Arrays controls appearing as top-level front panel objects consume significant space on the FPGA because each bit in the array uses a flip-flop on the FPGA. Consider replacing array controls with FIFOs or memory items to transfer data. |

Feedback Node

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You can use the Feedback Node to implement a pipeline and reduce long combinatorial paths. You also can use the Feedback Node for feedback in a subVI within a single-cycle Timed Loop. When you use the Feedback Node inside a Case structure, the Feedback Node updates data only on clock cycles when the owning subdiagram executes. Right-click the Feedback Node and select Properties from the shortcut menu to open the Properties dialog box. On the Configuration page, you can specify more options for the Feedback Node. |
| Timing | Inside single-cycle Timed Loop--When you initialize a Feedback Node inside a single-cycle Timed Loop, initialization requires no clock cycles. However, if the initialized data comes from a different clock domain, initialization can take multiple clock cycles. Outside single-cycle Timed Loop--Initialization of all Feedback Nodes outside the single-cycle Timed Loop requires one clock cycle. |
| Resources | The Feedback Node is implemented as a register and requires FPGA resources in proportion to the width of the data type. Using the initialization terminal slightly increases FPGA resource usage. |
| Notes | Consider using the Discrete Delay function instead of the Feedback Node. |

Flat Sequence Structure

| Single-Cycle Timed Loop | Using a sequence structure inside a single-cycle Timed Loop has no sequencing effect. |
| --- | --- |
| Usage | N/A |
| Timing | This structure requires no clock cycles to execute because it does not include an internal register. |
| Resources | This structure consumes minimal FPGA resources. |

For Loop

| Single-Cycle Timed Loop | Limited support. You can place a For Loop in a single-cycle Timed Loop if the For Loop contains only Array, Numeric, Boolean, or Comparison operations and uses only auto-indexed tunnels. Objects that generate or contain state, such as shift registers, Feedback Nodes, or VI calls, are not allowed in For Loops within a single-cycle Timed Loop. |
| --- | --- |
| Usage | The iteration (i) terminal is a 32-bit signed integer that saturates on reaching its maximum value, 2^31 - 1. The conditional terminal is not supported. Parallel loop iteration is not supported. |
| Timing | The For Loop incurs two clock cycles of overhead between iterations. If the For Loop contains initialized shift registers, it takes one clock cycle before the first iteration to initialize shift register values. |
| Resources | The For Loop consists of a small state machine. Shift registers require FPGA resources in proportion to the width of the data type. Loop auto-indexers consist of a hidden shift register for each array element. |
| Notes | The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. If LabVIEW cannot infer a single size for an array, you may need to manually configure the array to a fixed size. |

Global Variable

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | Global variables use less space on the FPGA than local variables, which makes them a better choice for data you do not need to transfer to a host VI. |
| Timing | A global variable takes at least one clock cycle, whereas a wire takes no clock cycles. For maximum efficiency, avoid using a variable when a wire would suffice. |
| Resources | A global variable consumes FPGA resources in proportion to the width of the data type. |

Local Variable

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | Global variables use less space on the FPGA than local variables, which makes them a better choice for data you do not need to transfer to a host VI. |
| Timing | A local variable takes at least one clock cycle, whereas a wire takes no clock cycles. For maximum efficiency, avoid using a variable when a wire would suffice. |
| Resources | A local variable consumes FPGA resources in proportion to the width of the data type, plus additional overhead to facilitate communication with a host VI. Consider limiting front panel objects, including those used as local variables, to optimize the FPGA VI. |

Stacked Sequence Structure

| Single-Cycle Timed Loop | Using a sequence structure inside a single-cycle Timed Loop has no sequencing effect. |
| --- | --- |
| Usage | N/A |
| Timing | This function requires no clock cycles to execute because it does not include an internal register. |
| Resources | This structure consumes minimal FPGA resources. |

Timed Loop

Refer to the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) topic for more information about using and configuring the Timed Loop in an FPGA VI.

Type Specialization Structure

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | When you use the Type Specialization structure in an FPGA VI, LabVIEW evaluates the compilation results at compile time and compiles only one subdiagram. |
| Timing | Entering and exiting this structure requires no time on the FPGA. |
| Resources | Only one subdiagram of the Type Specialization structure compiles to the FPGA. Inactive subdiagrams consume no FPGA resources. The Type Specialization structure itself also consumes no FPGA resources. |

While Loop

| Single-Cycle Timed Loop | Not supported. |
| --- | --- |
| Usage | The iteration (i) terminal is a 32-bit signed integer that saturates on reaching its maximum value, 2^31 - 1. |
| Timing | The While Loop incurs two clock cycles of overhead between iterations. If the While Loop contains initialized shift registers, it takes one clock cycle before the first iteration to initialize shift register values. Code placed in a While Loop generally takes longer to execute than the same code placed in a single-cycle Timed Loop. |
| Resources | The While Loop consists of a small state machine. Shift registers require FPGA resources in proportion to the width of the data type. Loop auto-indexers consist of a hidden shift register for each array element. |

Parent topic:

FPGA VI and Function Details (FPGA Module)

<!--NI_TOPIC bundle=lvfpga-api-ref path=lvfpga_intro.html language=enus -->
## TOPIC 00048: LabVIEW FPGA Module Programming Reference Manual

- bundle_id: `lvfpga-api-ref`
- source_path: `lvfpga_intro.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/lvfpga_intro.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: With the LabVIEW FPGA Module and LabVIEW, you can create VIs that run on NI FPGA targets, such as Reconfigurable I/O (RIO) devices. FPGA targets contain a reconfigurable FPGA (Field-Programmable Gate Array) surrounded by fixed I/O resources. Depending on the specific FPGA target, fixed I/O resources

### LabVIEW FPGA Module Programming Reference Manual

With the LabVIEW FPGA Module and LabVIEW, you can create VIs that run on NI FPGA targets, such as Reconfigurable I/O (RIO) devices. FPGA targets contain a reconfigurable FPGA (Field-Programmable Gate Array) surrounded by fixed I/O resources. Depending on the specific FPGA target, fixed I/O resources can include analog and digital resources, such as analog-to-digital converters (ADCs) and digital-to-analog converters (DACs), that you can control from the FPGA.

#### Other Resources

[LabVIEW FPGA Module Release Notes](https://www.ni.com/en-us/support/documentation/release-notes/product.labview-fpga-module.html) 
Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW FPGA Module release.

[NI License Manager Documentation](https://www.ni.com/docs/en-us/bundle/license-manager/page/manual-overview.html) 
Find documentation about activating, deactivating, and transferring software products using license activation codes or license files. For license administrators, this manual includes information for automating product activation and adding volume license servers.

Note

switch to English content

<!--NI_TOPIC bundle=lvfpga-api-ref path=menus/categories/fpga/advanced-mnu.html language=enus -->
## TOPIC 00049: Advanced

- bundle_id: `lvfpga-api-ref`
- source_path: `menus/categories/fpga/advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/menus/categories/fpga/advanced-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This palette includes the Up Cast function. The function on this palette can return general LabVIEW error codes, specific FPGA Interface error codes, or error codes specific to the FPGA target. icon

### Advanced

This palette includes the Up Cast function.

The function on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&&context=lvcore_lverror_misc_lv_error_codes), specific [FPGA Interface error codes](/csh?context=lvfpga_lvfpgahelp_fpga_error_codes_fpgainterface), or error codes specific to the FPGA target.

[IMAGE alt='icon' src='advanced-mnu.png']

- [Up Cast](../../../vi-lib/rvi/interface/nirviupcast/nirviupcast-xnode.html) Converts an FPGA VI-specific reference to a more generic reference. You then can use common code to interact with different FPGA VIs. The FPGA targets must be of the same class. You may want to use this function if you want to evaluate different algorithms in a host VI without rewriting the host VI. Some FPGA targets might not support this function.

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=menus/categories/fpga/dir-mnu.html language=enus -->
## TOPIC 00050: FPGA Interface

- bundle_id: `lvfpga-api-ref`
- source_path: `menus/categories/fpga/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/menus/categories/fpga/dir-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA Interface VIs and functions to communicate with an FPGA VI from a host VI. The VI that runs on an FPGA target is called the FPGA VI. A host VI is a VI that communicates with the FPGA VI to control the FPGA target. A host VI can run on a computer running Windows or on an RT target. You c

### FPGA Interface

Use the FPGA Interface VIs and functions to communicate with an FPGA VI from a host VI. The VI that runs on an FPGA target is called the FPGA VI. A host VI is a VI that communicates with the FPGA VI to control the FPGA target. A host VI can run on a computer running Windows or on an RT target.

You can use the FPGA Interface functions to programmatically control and communicate with an FPGA VI. Use the FPGA Interface functions to perform the following operations in host VIs:

- Establish and terminate communication with the FPGA VI or bitfile.
- Download, abort, reset, and run the FPGA VI on the FPGA target.
- Read and write data to the FPGA VI.
- Wait for and acknowledge FPGA VI interrupts.
- Read DMA FIFOs.
- Verify your FPGA design.

Note

My Computer

Project Explorer

The functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes), specific [FPGA Interface error codes](/csh?context=lvfpga_lvfpgahelp_fpga_error_codes_fpgainterface), or error codes specific to the FPGA target.

[IMAGE alt='icon' src='dir-mnu.png']

- [Open FPGA VI Reference](../../../vi-lib/rvi/interface/nirviopenfpga/nirviopenfpga-xnode.html) Opens a reference to the FPGA VI or bitfile and FPGA target you specify. Right-click the Open FPGA VI Reference function and select Configure Open FPGA VI Reference from the shortcut menu to display the Configure Open FPGA VI Reference dialog box. You must open a reference to the FPGA target before you can communicate between the host VI and the FPGA VI. You can download and run only one FPGA VI at a time on a single FPGA target. If you attempt to download a second VI to the FPGA target while the first FPGA VI is still in use, LabVIEW reports an error and the download fails.
- [Read/Write Control](../../../vi-lib/rvi/interface/nirvireadwritecontrol/nirvireadwritecontrol-xnode.html) Reads a value from or writes a value to a control or indicator in the FPGA VI on the FPGA target.
- [Invoke Method](../../../vi-lib/rvi/interface/nirvimethod/nirvimethod-xnode.html) Invokes an FPGA Interface method or action from a host VI on an FPGA VI. Use methods to do the following: download, abort, reset, and run the FPGA VI on the FPGA target, wait for and acknowledge FPGA VI interrupts, read DMA FIFOs, and write to DMA FIFOs. The methods you can choose from depend on the target hardware and the FPGA VI. You must wire the FPGA VI Reference In input to view the available methods in the shortcut menu.
- [Close FPGA VI Reference](../../../vi-lib/rvi/interface/nirviclosefpga/nirviclosefpga-xnode.html) Closes the reference to the FPGA VI and, optionally, resets execution of the VI. By default, the Close FPGA VI Reference function closes the reference to the FPGA VI and resets the FPGA VI. To configure this function only to close the reference, right-click the function and select Close from the shortcut menu.
- [Dynamic FPGA Interface Cast Function](../../../functions/dynamic-fpga-interface-cast.html) Casts Session In to the data type of Type . This function only changes the type of elements that FPGA VI reference contains. This function does not convert data. Use this function with the FPGA Interface Dynamic Refnum constant to create a dynamic host interface. Some FPGA targets might not support this function.
- [FPGA Interface Dynamic Refnum](../../../vi-lib/rvi/interface/nifpgainterfacerefnumconstant-vi.html) Use the FPGA Interface Dynamic Refnum constant to specify an FPGA interface. Specify the configuration of the interface by right-clicking the constant and selecting Configure FPGA VI Reference from the shortcut menu.
- [Open Dynamic Bitfile Reference Function](../../../functions/open-dynamic-bitfile-reference.html) Opens a reference to an FPGA bitfile at run time and returns a dynamic FPGA interface. Use this function in place of the Open FPGA VI Reference function when you want to open a bitfile by path at run time.
- [FPGA Desktop Execution Node](../../../vi-lib/rvi/desktopexecutionnode/desktopexecutionnode-xnode.html) Runs an FPGA VI on a development computer with simulated I/O for the specified number of clock ticks. This node writes all inputs, passes the amount of simulated time you specify, then reads all outputs. The FPGA VI pauses execution until the FPGA Desktop Execution Node is called again, at which point the FPGA VI resumes for the specified number of clock ticks.
- [Scaling](../../../menus/categories/fpga/scaling-mnu.html) Use the Scaling VIs to convert the clock and sample rate for the Loop Timer Express VI and to reconfigure input settings and post-process data from the FPGA Math & Analysis VIs.
- [Advanced](../../../menus/categories/fpga/advanced-mnu.html) This palette includes the Up Cast function.

<!--NI_TOPIC bundle=lvfpga-api-ref path=menus/categories/fpga/scaling-mnu.html language=enus -->
## TOPIC 00051: Scaling

- bundle_id: `lvfpga-api-ref`
- source_path: `menus/categories/fpga/scaling-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/menus/categories/fpga/scaling-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Scaling VIs to convert the clock and sample rate for the Loop Timer Express VI and to reconfigure input settings and post-process data from the FPGA Math & Analysis VIs. icon

### Scaling

Use the Scaling VIs to convert the clock and sample rate for the [Loop Timer](/csh?context=lvfpga_lvfpga_loop_timer) Express VI and to reconfigure input settings and post-process data from the [FPGA Math & Analysis](/csh?context=lvfpga_lvfpga_fpga_math_analysis_palette) VIs.

[IMAGE alt='icon' src='scaling-mnu.png']

- [Sample Rate To Loop Time](../../../vi-lib/rvi/analysis/host/public/sample-rate-to-loop-time-vi.html) Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.
- [Normalize Signal Generation Parameters](../../../vi-lib/rvi/analysis/host/public/normalize-signal-generation-parameters-vi.html) Converts frequency, phase, and duty cycle parameters into fixed-point units normalized to the clock rate. Use the Normalize Signal Generation Parameters VI in a host VI to convert values for the following FPGA VIs: Sine Wave Generator and Square Wave Generator.
- [Butterworth Coefficients](../../../vi-lib/rvi/analysis/host/butterworth/xnode/butterworthcoefficients-xnode.html) Generates filter coefficients for the Butterworth Filter Express VI. Use this VI in a host VI.
- [Notch Coefficients](../../../vi-lib/rvi/analysis/host/notch/xnode/notchcoefficients-xnode.html) Generates filter coefficients for the Notch Filter Express VI.
- [Scale Period](../../../vi-lib/rvi/analysis/host/public/scale-period-vi.html) Converts the period output, expressed in samples, from the Analog Period Measurement Express VI to a period in units of seconds using the sample rate you specify. This VI also returns the frequency of the measurement in hertz using the sample rate you specify. Use the Scale Period VI in a host VI.
- [FFT to Spectrum](../../../vi-lib/rvi/analysis/host/public/fft-to-spectrum-vi.html) Converts the output of the Fast Fourier Transform ( FFT ) Express VI to a power or amplitude spectrum. The spectrum is single-sided and scaled.
- [Discrete FP Transfer Function to FXP](../../../vi-lib/rvi/analysis/host/public/discrete-fp-transfer-function-to-fxp-vi.html) Converts a transfer function system model from floating-point to fixed-point representation. Obtain this model by entering values into the FP Transfer Function Model control or by using the VIs included with the LabVIEW Control Design & Simulation Module.
- [Convert PID Gains](../../../vi-lib/rvi/analysis/host/public/convert-pid-gains-vi.html) Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects.

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=menus/fpgacategories/programming/xilinx-ip-functions.html language=enus -->
## TOPIC 00052: Xilinx IP Functions

- bundle_id: `lvfpga-api-ref`
- source_path: `menus/fpgacategories/programming/xilinx-ip-functions.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/menus/fpgacategories/programming/xilinx-ip-functions.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Xilinx IP functions to implement different Xilinx IP in an FPGA VI. LabVIEW implements these functions using the IP Integration Node. The names and descriptions for these functions come from Xilinx IP data sheets, available on the Xilinx website at www.xilinx.com. The Xilinx IP palette varie

### Xilinx IP Functions

Use the Xilinx IP functions to implement different Xilinx IP in an FPGA VI. LabVIEW implements these functions using the IP Integration Node. The names and descriptions for these functions come from Xilinx IP data sheets, available on the Xilinx website at [www.xilinx.com](http://www.xilinx.com/products/intellectual-property/index.htm).

The Xilinx IP palette varies by target and displays only Xilinx IP functions that your FPGA device supports. Not all FPGA device families support all Xilinx IP. Refer to the Xilinx IP data sheets for information about FPGA device family support.

Some of the Xilinx IP requires licensing from Xilinx. You can find the licensing information in the **Context Help** window for a specific Xilinx IP. To import a license, place the .lic file in one of the following default directories, depending on your specific FPGA target:

- (Xilinx ISE) C:\NIFPGA\programs\*XilinxY_Z*\ISE\coregen\core_licenses , where *XilinxY_Z* is the current version of the Xilinx compilation tool for ISE for your FPGA target.
- (Xilinx Vivado) C:\NIFPGA\programs\*VivadoA_B*\data\ip\core_licenses , where *VivadoA_B* is the current version of the Xilinx compilation tool for Vivado for your FPGA target.

To compile VIs containing licensed IP, ensure that the license exists on the computer.

Note

- You must have the Xilinx compilation tools installed on the local computer to configure these functions. Refer to the Xilinx Compilation Tools Readme for instructions on installing Xilinx compilation tools for LabVIEW.
- If you move Xilinx IP generated on a given FPGA target to another FPGA target, you may need to regenerate the Xilinx IP.

| Subpalette | Description |
| --- | --- |
| AXI Infrastructure | Use the AXI Infrastructure functions to build AXI-based applications or systems. This palette is available only on Xilinx Vivado targets. |
| BaseIP | Use the BaseIP functions to implement IP for basic FPGA arithmetic operations such as multiply-add and multiply-accumulate. |
| Basic Elements | Use the Basic Elements functions to implement IP such as accumulators, counters, memory elements, and shift registers. |
| Communication & Networking | Use the Communication & Networking functions to implement IP related to telecommunication and wireless applications. |
| Digital Signal Processing | Use the Digital Signal Processing functions to implement IP such as filters, transforms, and modulation. |
| Math Functions | Use the Math Functions functions to implement IP for various mathematical and floating-point operations. |
| Memories & Storage Elements | Use the Memories & Storage Elements functions to implement IP related to FIFOs, RAMs, and ROMs. |
| Video & Image Processing | Use the functions on this palette to implement IP such as color correction, video timing, and color space conversion. |

#### Related Information

[Integrating Xilinx IP into FPGA VIs](/csh?context=lvfpga_lvfpgahelp_fpga_xilinxip_using)

[Interfacing AXI IP in FPGA VIs](/csh?context=lvfpga_lvfpgaconcepts_xilinxip_using)

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/channels/accumulator-tag.html language=enus -->
## TOPIC 00053: Accumulator Tag

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/channels/accumulator-tag.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/channels/accumulator-tag.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module Use the Accumulator Tag channel to share a single value among multiple writers and readers. Sharing the value is similar to sharing a global or network shared variable. Each time a writer endpoint writes a value to the channel, the channel adds the value to the existing value.

### Accumulator Tag

**Requires:** FPGA Module

Use the Accumulator Tag channel to share a single value among multiple writers and readers. Sharing the value is similar to sharing a global or network shared variable. Each time a writer endpoint writes a value to the channel, the channel adds the value to the existing value. Reader endpoints can optionally clear the value when they retrieve the current sum.

Note

Refer to the [Channel Wire Endpoints Details](/csh?context=lvfpga_lvfpga_channel_wire_details) topic for information about Timed Loop compatibility, usage, and resource considerations related to the Accumulator Tag endpoints.

| Endpoint | Description |
| --- | --- |
| Read | Reads the sum of values from an Accumulator Tag channel and optionally clears the value after the endpoint retrieves the current sum. |
| Read With Abort | Reads the value from an Accumulator Tag channel, optionally clears the accumulator, and optionally signals the channel to abort. This endpoint is the same as the Read endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Accumulator Tag channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Write With Abort endpoint. |
| Write | Adds a value to an Accumulator Tag channel. |
| Write With Abort | Adds a value to an Accumulator Tag channel or signals the channel to abort. This endpoint is the same as the Write endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Accumulator Tag channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Read With Abort endpoint. |

Parent topic:

Channel Wire Endpoints

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/channels/channel-wire-endpoint-fpga.html language=enus -->
## TOPIC 00054: Channel Wire Endpoints

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/channels/channel-wire-endpoint-fpga.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/channels/channel-wire-endpoint-fpga.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module Channel wire endpoints are nodes where a channel wire terminates. By connecting a channel writer endpoint to a reader endpoint using a channel wire, you build a channel. The channel wire endpoints operate on the channel in the following way: the writer endpoints write data to t

### Channel Wire Endpoints

**Requires:** FPGA Module

[Channel wire](/csh?productcategories=147794&context=lvcore_lvconcepts_channel_wires_intro) endpoints are nodes where a channel wire terminates. By connecting a channel writer endpoint to a reader endpoint using a channel wire, you build a channel. The channel wire endpoints operate on the channel in the following way: the writer endpoints write data to the channel, and reader endpoints read data from the channel. You can use the channel wire endpoints to write or read data between parallel sections of code. LabVIEW provides several channel templates. Each template expresses a different communications protocol to use between the writers and readers. Choose which channel template to use based on your communications needs.

Create a channel endpoint by right-clicking a terminal or a wire and selecting **Create»Channel Writer** or **Create»Channel Reader**. When you create an endpoint from a terminal, you instantiate the channel template with that data type as its transmission type.

Refer to the [Channel Wire Endpoints Details](/csh?context=lvfpga_lvfpga_channel_wire_details) topic for information about Timed Loop compatibility, usage, and resource considerations related to the channel wire endpoints.

| Template | Description |
| --- | --- |
| Stream | Use the Stream channel to communicate homogeneous data from a single writer to a single reader. The data elements are buffered and transferred with no data loss in a first-in-first-out (FIFO) order. |
| Tag | Use the Tag channel to share a single value among multiple readers and/or writers. Sharing the value is similar to sharing a global or network shared variable. Each time a writer endpoint writes a value to the channel, the value overwrites the existing value in the channel to ensure that the reader endpoints always read the latest value. |
| Accumulator Tag | Use the Accumulator Tag channel to share a single value among multiple writers and readers. Sharing the value is similar to sharing a global or network shared variable. Each time a writer endpoint writes a value to the channel, the channel adds the value to the existing value. Reader endpoints can optionally clear the value when they retrieve the current sum. |
| Lossy Stream | Use the Lossy Stream channel to communicate homogeneous data from a single writer to a single reader. If the channel is already full when the writer attempts to write a new data, the writer does not wait for space to be available. Instead, the channel optionally either drops the oldest data element in the channel to make room for this new data or discards this new data. You can use the Lossy Stream readers to identify data gaps. |
| One Element Stream | Use the One Element Stream channel exactly the way you use a Stream channel with size equal to one. Allowing only one element in the buffer makes One Element Stream channels more optimized. They execute faster and save resources compared with Stream channels. |

Depending on the driver you installed, refer to the following VIs for examples of using channel wires on FPGA targets:

- (R Series) examples\R Series\FPGA Fundamentals\Data Storage and Transfer\Channel Wire\R Series FPGA Channel Wire Basic\R-Series FPGA Channel Wire Basic.lvproj
- (CompactRIO) examples\CompactRIO\FPGA Fundamentals\Data Transfer and Storage\Channel Wire\cRIO FPGA Channel Wire Basic\cRIO FPGA Channel Wire Basic.lvproj

- [Stream](../../resource/channels/stream.html)
- [Tag](../../resource/channels/tag.html)
- [Accumulator Tag](../../resource/channels/accumulator-tag.html)
- [Lossy Stream](../../resource/channels/lossy-stream.html)
- [One Element Stream](../../resource/channels/one-element-stream.html)

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/channels/lossy-stream.html language=enus -->
## TOPIC 00055: Lossy Stream

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/channels/lossy-stream.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/channels/lossy-stream.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module Use the Lossy Stream channel to communicate homogeneous data from a single writer to a single reader. If the channel is already full when the writer attempts to write a new data, the writer does not wait for space to be available. Instead, the channel optionally either drops th

### Lossy Stream

**Requires:** FPGA Module

Use the Lossy Stream channel to communicate homogeneous data from a single writer to a single reader. If the channel is already full when the writer attempts to write a new data, the writer does not wait for space to be available. Instead, the channel optionally either drops the oldest data element in the channel to make room for this new data or discards this new data. You can use the Lossy Stream readers to identify data gaps.

Refer to the [Channel Wire Endpoints Details](/csh?context=lvfpga_lvfpga_channel_wire_details) topic for information about Timed Loop compatibility, usage, and resource considerations related to the Lossy Stream endpoints.

| Endpoint | Description |
| --- | --- |
| Read | Reads an element from a Lossy Stream channel. |
| Read With Abort | Reads an element from a Lossy Stream channel or signals the channel to abort. This endpoint is the same as the Read endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Lossy Stream channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Write With Abort endpoint. |
| Write | Writes an element to a Lossy Stream channel. If the channel is full, this endpoint either drops the oldest element in the channel to make room for this new element or discards this new element. |
| Write With Abort | Writes an element to a Lossy Stream channel or signals the channel to abort. The endpoint waits if the channel is full. This endpoint is the same as the Write endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Lossy Stream channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Read With Abort endpoint. |

Parent topic:

Channel Wire Endpoints

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/channels/one-element-stream.html language=enus -->
## TOPIC 00056: One Element Stream

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/channels/one-element-stream.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/channels/one-element-stream.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module Use the One Element Stream channel exactly the way you use a Stream channel with size equal to one. Allowing only one element in the buffer makes One Element Stream channels more optimized. They execute faster and save resources compared with Stream channels. Refer to the Chann

### One Element Stream

**Requires:** FPGA Module

Use the One Element Stream channel exactly the way you use a Stream channel with size equal to one. Allowing only one element in the buffer makes One Element Stream channels more optimized. They execute faster and save resources compared with Stream channels.

Refer to the [Channel Wire Endpoints Details](/csh?context=lvfpga_lvfpga_channel_wire_details) topic for information about Timed Loop compatibility, usage, and resource considerations related to the One Element Stream endpoints.

| Endpoint | Description |
| --- | --- |
| Read | Waits to read data from a One Element Stream channel. |
| Read With Abort | Waits to read an element from a One Element Stream channel or signals the channel to abort. This endpoint is the same as the Read endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the One Element Stream channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Write With Abort endpoint. |
| Write | Writes an element to a One Element Stream channel. The endpoint waits if the channel is full. |
| Write With Abort | Writes an element to a One Element Stream channel or signals the channel to abort. The endpoint waits if the channel is full. This endpoint is the same as the Write endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the One Element Stream channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Read With Abort endpoint. |

Parent topic:

Channel Wire Endpoints

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/channels/stream.html language=enus -->
## TOPIC 00057: Stream

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/channels/stream.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/channels/stream.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module Use the Stream channel to communicate homogeneous data from a single writer to a single reader. The data elements are buffered and transferred with no data loss in a first-in-first-out (FIFO) order. Refer to the Channel Wire Endpoints Details topic for information about Timed L

### Stream

**Requires:** FPGA Module

Use the Stream channel to communicate homogeneous data from a single writer to a single reader. The data elements are buffered and transferred with no data loss in a first-in-first-out (FIFO) order.

Refer to the [Channel Wire Endpoints Details](/csh?context=lvfpga_lvfpga_channel_wire_details) topic for information about Timed Loop compatibility, usage, and resource considerations related to the Stream endpoints.

| Endpoint | Description |
| --- | --- |
| Read | Reads an element from a Stream channel. The endpoint waits if the channel is empty. |
| Read With Abort | Reads an element from a Stream channel or signals the channel to abort. This endpoint is the same as the Read endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Stream channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Write With Abort endpoint. |
| Write | Writes an element to a Stream channel. The endpoint waits if the channel is full. |
| Write With Abort | Writes an element to a Stream channel or signals the channel to abort. The endpoint waits if the channel is full. This endpoint is the same as the Write endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Stream channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Read With Abort endpoint. |

Parent topic:

Channel Wire Endpoints

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/channels/tag.html language=enus -->
## TOPIC 00058: Tag

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/channels/tag.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/channels/tag.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module Use the Tag channel to share a single value among multiple readers and/or writers. Sharing the value is similar to sharing a global or network shared variable. Each time a writer endpoint writes a value to the channel, the value overwrites the existing value in the channel to e

### Tag

**Requires:** FPGA Module

Use the Tag channel to share a single value among multiple readers and/or writers. Sharing the value is similar to sharing a global or network shared variable. Each time a writer endpoint writes a value to the channel, the value overwrites the existing value in the channel to ensure that the reader endpoints always read the latest value.

Refer to the [Channel Wire Endpoints Details](/csh?context=lvfpga_lvfpga_channel_wire_details) topic for information about Timed Loop compatibility, usage, and resource considerations related to the Tag endpoints.

| Endpoint | Description |
| --- | --- |
| Read | Reads a value from a Tag channel. |
| Read With Abort | Reads a value from a Tag channel or signals the channel to abort. This endpoint is the same as the Read endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Tag channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Write With Abort endpoint. |
| Write | Writes a value to a Tag channel. |
| Write With Abort | Writes a value to a Tag channel or signals the channel to abort. This endpoint is the same as the Write endpoint except that it has an abort input and an aborted? output. You can use the abort capability of the Tag channel to close a channel abruptly, ignoring any data left in the channel buffer. You must use this endpoint together with the Read With Abort endpoint. |

Parent topic:

Channel Wire Endpoints

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/dialog/preferencesdialog/preferencepages/fpga/fpga-module-options-dialog-box.html language=enus -->
## TOPIC 00059: FPGA Module Options Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/dialog/preferencesdialog/preferencepages/fpga/fpga-module-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/dialog/preferencesdialog/preferencepages/fpga/fpga-module-options-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Tools»Options to display the Options dialog box and select FPGA Module from the Category list to display this dialog box. Use this dialog box to specify the location of the FPGA compile server and simulation options. This dialog box includes the following components: Option Description Compil

### FPGA Module Options Dialog Box

Select **Tools»Options** to display the [Options](/csh?context=lvfpga_lvfpgadialog_fpga_module_options) dialog box and select **FPGA Module** from the **Category** list to display this dialog box.

Use this dialog box to specify the location of the FPGA [compile server](/csh?context=lvfpga_lvfpgaconcepts_compiling_fpga_vis) and simulation options.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Compile Server | Sets options for the compile server. Use the local compile server—Specifies that LabVIEW use the compilation tools installed on the local computer, called localhost. Connect to server—Specifies that LabVIEW use the compilation tools installed on another computer or that LabVIEW use localhost when authentication is required. Compile server name—Displays the name or IP address of the computer running the compile server. User name—Displays the name of the account that you use to log into the compile server. Configure remote server—Displays the Configure Remote Compile Server dialog box. Connect to LabVIEW FPGA Compile Cloud Service—Specifies that LabVIEW use the compilation tools available through the LabVIEW FPGA Compile Cloud Service. User name—Displays the name of the account that you use to log into the LabVIEW FPGA Compile Cloud Service. Configure cloud server—Displays the Configure Cloud Service dialog box. Prompt to select a compile server for each compilation—Specifies whether LabVIEW prompts you to select a compile server for each compilation. |
| Notification of Completed Compilation | Sets options for how LabVIEW notifies you of completed compilations. Display a message in the system tray—Specifies whether LabVIEW displays a message in the system tray upon completing a compilation. LabVIEW places a checkmark in the Display a message in the system tray checkbox by default. Play a sound—Specifies whether LabVIEW plays a sound upon completing a compilation. Click the Browse button to specify the notification audio file that LabVIEW plays. Display a popup message—Specifies whether LabVIEW displays a popup message upon completing a compilation. |
| Simulation | Sets the simulator you want to use. Simulator—Specifies the simulator you want to use. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/builds/fpga/ui/information-page-simulation-export-properties-dialog-box.html language=enus -->
## TOPIC 00060: Information Page (Simulation Export Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/builds/fpga/ui/information-page-simulation-export-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/builds/fpga/ui/information-page-simulation-export-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Simulation Export Properties dialog box to name the FPGA simulation export and select the location to save the export. This page includes the following components: Option Description Build specification name Specifies a unique name for the build specification. The name appears u

### Information Page (Simulation Export Properties Dialog Box)

Use this page of the [Simulation Export Properties](/csh?context=lvfpga_lvfpgadialog_fpga_sim_export_db) dialog box to name the FPGA simulation export and select the location to save the export.

This page includes the following components:

| Option | Description |
| --- | --- |
| Build specification name | Specifies a unique name for the build specification. The name appears under Build Specifications in the Project Explorer window. |
| Top-level sim model name | Specifies the name of the simulation model. The name must follow VHDL entity naming conventions. |
| Destination directory | Specifies the location to save the FPGA simulation files. You can enter a path or use the Browse button to navigate to and select the location.This directory is the root directory for the simulation export working directory. NI recommends avoiding extremely long file paths and paths with spaces. |
| Build specification description | Displays information about the build specification. You can view and edit the description on this page only. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/builds/fpga/ui/model-fidelity-page-simulation-export-properties-dialog-box.html language=enus -->
## TOPIC 00061: Model Fidelity Page (Simulation Export Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/builds/fpga/ui/model-fidelity-page-simulation-export-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/builds/fpga/ui/model-fidelity-page-simulation-export-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Simulation Export Properties dialog box to learn about the fidelity of the simulation model. This page includes the following components: Option Description Simulation Model Lists the simulation models within the main FPGA model that correspond to the bus interface, top-level fr

### Model Fidelity Page (Simulation Export Properties Dialog Box)

Use this page of the [Simulation Export Properties](/csh?context=lvfpga_lvfpgadialog_fpga_sim_export_db) dialog box to learn about the fidelity of the simulation model.

This page includes the following components:

| Option | Description |
| --- | --- |
| Simulation Model | Lists the simulation models within the main FPGA model that correspond to the bus interface, top-level framework, and I/O. |
| ModelFidelity | Displays the type of fidelity.The model fidelity is target-specific and can be one of the following types: Hardware Implementation—The timing is exactly the same as the hardware timing, and the VHDL code is the same as the code that the driver software implements on the target. Cycle Accurate—The timing is exactly the same as the hardware timing, but the VHDL code is different than the code that the driver software implements on the target. Simplified Model—The timing is not necessarily the same as the hardware timing, and the VHDL code is different than the code that the driver software implements on the target. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/builds/fpga/ui/source-files-page-simulation-export-properties-dialog-box.html language=enus -->
## TOPIC 00062: Source Files Page (Simulation Export Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/builds/fpga/ui/source-files-page-simulation-export-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/builds/fpga/ui/source-files-page-simulation-export-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Simulation Export Properties dialog box to specify the top-level FPGA VI and the signals to export to the waveform viewer. This page includes the following components: Option Description Project Files Displays a list of items under the current target in the Project Explorer wind

### Source Files Page (Simulation Export Properties Dialog Box)

Use this page of the [Simulation Export Properties](/csh?context=lvfpga_lvfpgadialog_fpga_sim_export_db) dialog box to specify the top-level FPGA VI and the signals to export to the waveform viewer.

This page includes the following components:

| Option | Description |
| --- | --- |
| Project Files | Displays a list of items under the current target in the Project Explorer window. |
| Top-Level VI | Specifies which VI is the top-level VI. Select a VI from the Project Files list and click the Add Item button to add the VI as the top-level VI. |
| Signals to Populate in Waveform | Specifies the types of signals you want to export for easier reference in the waveform viewer. clip—Specifies to export CLIP signals.You must set the simulation behavior of CLIP before you can simulate CLIP signals. nipi—Specifies to export signals from IP Integration Nodes.You must set the simulation behavior of the node before you can simulate the signals. eio—Specifies to export signals from FPGA I/O Nodes. topLvlCtrlsInds—Specifies to export signals from the controls and indicators in the top-level VI. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/builds/fpga/ui/xilinx-options-page-for-ise-compilation-properties-dialog-box.html language=enus -->
## TOPIC 00063: Xilinx Options Page for ISE (Compilation Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/builds/fpga/ui/xilinx-options-page-for-ise-compilation-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/builds/fpga/ui/xilinx-options-page-for-ise-compilation-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can display this page in the following two ways: If an FPGA build specification does not exist, right-click Build Specifications under an FPGA target in the Project Explorer window and select New»Compilation to display the Compilation Properties dialog box. Select Xilinx Options from the Categor

### Xilinx Options Page for ISE (Compilation Properties Dialog Box)

You can display this page in the following two ways:

- If an FPGA build specification does not exist, right-click Build Specifications under an FPGA target in the Project Explorer window and select New»Compilation to display the Compilation Properties dialog box. Select Xilinx Options from the Category list to display this page.
- If an FPGA build specification exists, right-click the build specification and select Properties from the shortcut menu to display the Compilation Properties dialog box. Select Xilinx Options from the Category list to display this page.

Note

Xilinx Options

Category

Xilinx Options Page for Vivado (Compilation Properties Dialog Box)

Use this page to define the Xilinx ISE options to use when you compile an FPGA VI. The options you can specify depend on your specific FPGA target. Refer to the [support document](https://www.ni.com/r/XilinxCompileTools) at ni.com for more information about NI hardware supported by each Xilinx compilation tool.

In general, you do not need to adjust the options on this page unless the FPGA VI fails to compile. Use the information from the [Compilation Status](/csh?context=lvfpga_lvfpgadialog_fpga_compile_help) window to determine which options on this page might help the FPGA VI compile successfully. Refer to the Xilinx website at [www.xilinx.com](http://www.xilinx.com/support.html) for information about different design strategies and optimization options.

This page contains the following components:

| Option | Description |
| --- | --- |
| Use recommended settings | Specifies that the Xilinx compiler uses the options that the target provides. By default, this checkbox contains a checkmark. Remove the checkmark to customize Xilinx options on this page. |
| Design Strategy | Specifies a set of Xilinx options for the application. You can select from preset configurations to minimize the compilation time, maximize timing performance, or optimize the design area. You can override any of the options of a design strategy to create a custom configuration. Balanced—Selects options that balance the compilation time with the amount of effort the Xilinx compiler uses to meet the timing and design objectives of the FPGA application. Minimum Compilation Time—Selects options that minimize the compilation time by reducing the mapping effort of the Xilinx compiler. Timing Performance—Selects options that maximize the timing performance of the FPGA application. Area—Selects options that optimize the area usage on the FPGA. Custom—Indicates that options might not match any of the preset configurations. |
| Synthesis Optimization Goal | Specifies the synthesis optimization goal of the Xilinx compiler. Synthesis is the component of the Xilinx compilation process that creates logic gates from the design of the FPGA VI. Speed—Configures the Xilinx compiler to reduce the logic levels in the design implementation. Area—Configures the Xilinx compiler to minimize the total amount of logic in the design implementation. |
| Synthesis Optimization Effort Level | Specifies the effort level the Xilinx compiler uses during synthesis. The effort levels are relative to each other and not absolute levels. Normal—Configures the Xilinx compiler to optimize the design using minimization and algebraic factoring algorithms. High—Configures the Xilinx compiler to perform additional optimizations for the specific FPGA architecture. Specifying the High synthesis optimization effort level increases the compilation time because the Xilinx compiler attempts multiple optimization algorithms to determine the best result for the target architecture. |
| Map Overall Effort Level | Specifies the effort level the Xilinx compiler uses to map the FPGA VI to the FPGA. The effort levels are relative to each other and not absolute levels. Default Xilinx setting—Configures the Xilinx compiler to use the Xilinx default effort level for mapping. Standard—Configures the Xilinx compiler to use the standard level of effort. High—Configures the Xilinx compiler to use the highest level of effort when compiling the FPGA VI. The High effort level takes more time to compile than other effort levels. |
| Place and Route Overall Effort Level | Specifies the effort level of the Xilinx compiler uses to place the logic blocks and route the combinatorial paths on the FPGA. The effort levels are relative to each other and not absolute levels. Standard—Configures the Xilinx compiler to use the standard level of effort. High—Configures the Xilinx compiler to use the highest level of effort when compiling the FPGA VI. The High effort level takes more time to compile than other effort levels. |
| Use random value for starting placer cost table | Specifies a random value for the Starting Placer Cost Table property of the Place and Route process in the Xilinx tools. Enabling this checkbox will not initiate code generation, but could impact performance and device utilization results. Refer to the Xilinx website at www.xilinx.com for more information about place and route properties. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/builds/fpga/ui/xilinx-options-page-for-vivado-compilation-properties-dialog-box.html language=enus -->
## TOPIC 00064: Xilinx Options Page for Vivado (Compilation Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/builds/fpga/ui/xilinx-options-page-for-vivado-compilation-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/builds/fpga/ui/xilinx-options-page-for-vivado-compilation-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can display this page in the following two ways: If an FPGA build specification does not exist, right-click Build Specifications under an FPGA target in the Project Explorer window and select New»Compilation to display the Compilation Properties dialog box. Select Xilinx Options from the Categor

### Xilinx Options Page for Vivado (Compilation Properties Dialog Box)

You can display this page in the following two ways:

- If an FPGA build specification does not exist, right-click Build Specifications under an FPGA target in the Project Explorer window and select New»Compilation to display the Compilation Properties dialog box. Select Xilinx Options from the Category list to display this page.
- If an FPGA build specification exists, right-click the build specification and select Properties from the shortcut menu to display the Compilation Properties dialog box. Select Xilinx Options from the Category list to display this page.

Note

Xilinx Options

Category

Xilinx Options Page for ISE (Compilation Properties Dialog Box)

Use this page to define the Xilinx Vivado options to use when you compile an FPGA VI. The options you can specify depend on your specific FPGA target. Refer to the [support document](https://www.ni.com/r/XilinxCompileTools) at ni.com for more information about NI hardware supported by each Xilinx compilation tool.

In general, you do not need to adjust the options on this page unless the FPGA VI fails to compile. Use the information from the [Compilation Status](/csh?context=lvfpga_lvfpgadialog_fpga_compile_help) window to determine which options on this page might help the FPGA VI compile successfully. Refer to the Xilinx website at [www.xilinx.com](http://www.xilinx.com/support/documentation/sw_manuals/xilinx2013_2/ug904-vivado-implementation.pdf) for information about different Vivado design strategies and directive options.

This page contains the following components:

| Option | Description |
| --- | --- |
| Implementation strategy | Specifies a set of Xilinx options for the application. You can select from preset configurations to optimize performance, optimize the design area, optimize power, optimize design congestion on the chip, or reduce compilation time. You also can override any of the options of a design strategy to create a custom configuration. Default—Configures the Xilinx compiler to use the Xilinx default implementation strategy. Optimize performance—Selects the options that maximize the timing performance of the FPGA application. Optimize area—Selects options that reduces LUT count on the FPGA chip. Optimize power—Selects options that optimize the power usage on the FPGA chip. Optimize congestion—Selects options that minimize design congestion on the FPGA chip. Reduce compilation time—Selects options that minimize the compilation time by reducing the mapping effort of the Xilinx compiler. Custom—Indicates that options might not match any of the preset configurations. |
| Design optimization directive | Specifies how the Xilinx compiler optimizes the FPGA design. This option is available only when you select the Custom option in Implementation strategy. You can choose Default, Explore, Explore area, Explore sequential area, Add re-map, Run-time optimized, or Disable BRAM power optimization. Refer to the Xilinx website at www.xilinx.com for more information about Vivado directive options. |
| Placement directive | Specifies how the Xilinx compiler places the FPGA design on the chip. This option is available only when you select the Custom option in Implementation strategy. You can choose Default, Explore, Wire-length-driven block placement, Late block placement, Extra net delay (high), Extra net delay (medium), Extra net delay (low), Spread logic (high), Spread logic (medium), Spread logic (low), Extra post-placement optimization, Extra timing optimization (SSI), Spread SSLs (SSI), Balance SSLs (SSI), Balance SLRs (SSI), High utilization SLRs (SSI), Run-time optimized, Quick, or Alternate wire-length-driven placement. Refer to the Xilinx website at www.xilinx.com for more information about Vivado directive options. |
| Physical design optimization directive | Specifies how the Xilinx compiler optimizes the FPGA design on the chip. This option is available only when you select the Custom option in Implementation strategy. You can choose Default, Explore, Explore with hold violation fixing, Aggressively explore, Alternate replication, Aggressive fan-out optimization, Alternate delay modeling, Add register re-timing, Alternate flow with re-timing, or Not enabled. Refer to the Xilinx website at www.xilinx.com for more information about Vivado directive options. |
| Routing directive | Specifies how the Xilinx compiler routes the FPGA design on the chip. This option is available only when you select the Custom option in Implementation strategy. You can choose Default, Explore, No timing relaxation, More global iterations, Higher delay cost, Advanced skew modeling, or Run-time optimized. Refer to the Xilinx website at www.xilinx.com for more information about Vivado directive options. |
| Run power optimization? | Specifies that the Xilinx compiler adds power optimization to reduce power consumption. By default this checkbox contains a checkmark only if you select the Optimize power option in Implementation strategy. |
| Build using multiple threads, if available | Specifies that the Xilinx compiler uses multithreading, if multiple threads are available. By default, this checkbox contains a checkmark. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lveio/private/configure-fpga-i-o-name-control-type-dialog-box.html language=enus -->
## TOPIC 00065: Configure FPGA I/O Name Control Type Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lveio/private/configure-fpga-i-o-name-control-type-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lveio/private/configure-fpga-i-o-name-control-type-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA I/O control or constant and select Configure I/O Type from the shortcut menu to display this dialog box. Use this dialog box to configure the specific data type of an FPGA I/O control or constant, including the supported methods and properties. This dialog box contains the follow

### Configure FPGA I/O Name Control Type Dialog Box

Right-click an FPGA I/O control or constant and select **Configure I/O Type** from the shortcut menu to display this dialog box.

Use this dialog box to [configure the specific data type](/csh?context=lvfpga_lvfpgahelp_fpga_io_name_control_config) of an FPGA I/O control or constant, including the supported methods and properties.

This dialog box contains the following components:

| Option | Description |
| --- | --- |
| I/O Items | Lists all the FPGA I/O items that you previously added to the project. Select one of these I/O items as a model for the specific data type of the FPGA I/O control. |
| I/O Item Type | Lists the methods and properties that the I/O item you select from the I/O Items list supports. |
| Replace All | Copies all methods or properties from the I/O Item Type list to the I/O Name Control Type list. |
| I/O Item Type Details | Provides information about the method or property you select in the I/O Item Type list. |
| I/O Name Control Type | Lists the methods and properties that the I/O control supports. |
| Remove | Removes unwanted methods or properties you select from the I/O Name Control Type list. |
| I/O Name Control Type Details | Provides information about the method or property you select in the I/O Name Control Type list. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lveio/private/fpga-i-o-properties-dialog-box.html language=enus -->
## TOPIC 00066: FPGA I/O Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lveio/private/fpga-i-o-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lveio/private/fpga-i-o-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA I/O item in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure an FPGA I/O item. The options that appear vary by FPGA target and FPGA I/O. The configuration options you specify in the Project Explo

### FPGA I/O Properties Dialog Box

Right-click an FPGA I/O item in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display this dialog box.

Use this dialog box to configure an FPGA I/O item. The options that appear vary by FPGA target and FPGA I/O.

Note

Project Explorer

This dialog box might contain the following pages in the **Category** list:

- General
- Advanced Code Generation

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lveio/private/general-page-fpga-i-o-properties-dialog-box.html language=enus -->
## TOPIC 00067: General Page (FPGA I/O Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lveio/private/general-page-fpga-i-o-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lveio/private/general-page-fpga-i-o-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA I/O item in the Project Explorer window and select Properties from the shortcut menu to display the FPGA I/O Properties dialog box. Select General in the Category list to display this page. Use this page to configure general characteristics of the FPGA I/O item. This page contain

### General Page (FPGA I/O Properties Dialog Box)

Right-click an FPGA I/O item in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display the **FPGA I/O Properties** dialog box. Select **General** in the **Category** list to display this page.

Use this page to configure general characteristics of the FPGA I/O item.

This page contains the following components:

| Option | Description |
| --- | --- |
| Name | Displays the name of the I/O item that appears in the Project Explorer window.You can change the name of the I/O item by typing in the Name column in the New FPGA I/O table, by typing in the Name string control in the FPGA I/O Properties dialog box, or by right-clicking the FPGA I/O item in the Project Explorer window and selecting Rename from the shortcut menu. |
| Resource | Displays the I/O resource on the target.The I/O resource is the resource that you selected from the Available Resources tree in the New FPGA I/O table. The Resource corresponds to an I/O resource on the FPGA target. You can change the resource by right-clicking the FPGA item in the Project Explorer window and selecting Select Resource from the shortcut menu. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lveio/private/new-fpga-i-o-dialog-box.html language=enus -->
## TOPIC 00068: New FPGA I/O Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lveio/private/new-fpga-i-o-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lveio/private/new-fpga-i-o-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The New FPGA I/O dialog box appears when you create new FPGA I/O items in the Project Explorer window. You also can right-click an FPGA I/O Node and select Add New FPGA I/O from the shortcut menu to display this dialog box. Use this dialog box to specify the I/O resources you want to use in the Proj

### New FPGA I/O Dialog Box

The **New FPGA I/O** dialog box appears when you create new FPGA I/O items in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window. You also can right-click an [FPGA I/O Node](../../../../../vi-lib/eio/eionode/eionode-xnode.html) and select **Add New FPGA I/O** from the shortcut menu to display this dialog box.

Use this dialog box to specify the I/O resources you want to use in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and to edit the names of the I/O items you select.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Available Resources | Displays the I/O resources available for the FPGA target for which you create the FPGA I/O items. The FPGA target you right-click in the Project Explorer window determines the I/O resources that appear in the Available Resources tree. |
| Add | Adds the I/O resources you select in the Available Resources tree to the list of FPGA I/O items in the New FPGA I/O table. |
| Remove | Removes the FPGA I/O items you select in the New FPGA I/O table from the table. The FPGA I/O item returns to the Available Resources tree. |
| New FPGA I/O | Displays the I/O resources you add to the table from the Available Resources tree. Each I/O item that appears in this table appears in the Project Explorer window when you click the OK button.Contains the following options: Name—Displays the name of the I/O item that appears in the Project Explorer window.You can change the name of the I/O item by typing in the Name column in the New FPGA I/O table, by typing in the Name string control in the FPGA I/O Properties dialog box, or by right-clicking the FPGA I/O item in the Project Explorer window and selecting Rename from the shortcut menu. Resource—Displays the I/O resource on the target.The I/O resource is the resource that you selected from the Available Resources tree in the New FPGA I/O table. The Resource corresponds to an I/O resource on the FPGA target. You can change the resource by right-clicking the FPGA item in the Project Explorer window and selecting Select Resource from the shortcut menu. |
| Place new I/O in folders | Organizes the I/O items in folders according to the I/O type in the Project Explorer window. |

Tip

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lveio/private/select-resource-dialog-box.html language=enus -->
## TOPIC 00069: Select Resource Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lveio/private/select-resource-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lveio/private/select-resource-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA I/O item in the Project Explorer window and select Select Resource from the shortcut menu to display this dialog box. Use this dialog box to view the I/O resources available for the FPGA target under which the FPGA I/O item appears in the Project Explorer window. Select an I/O re

### Select Resource Dialog Box

Right-click an FPGA I/O item in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Select Resource** from the shortcut menu to display this dialog box.

Use this dialog box to view the I/O resources available for the FPGA target under which the FPGA I/O item appears in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window. Select an I/O resource in the tree to change the I/O resource to which the FPGA I/O item is assigned. You might need to select a new FPGA I/O resource if you [copy](/csh?context=lvfpga_lvfpgaconcepts_reusing_fpga_objects) the FPGA I/O item from another FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window.

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/component-level-ip-page-fpga-target-properties-dialog-box.html language=enus -->
## TOPIC 00070: Component-Level IP Page (FPGA Target Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/component-level-ip-page-fpga-target-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/component-level-ip-page-fpga-target-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target in the Project Explorer window and select Properties from the shortcut menu to display the FPGA Target Properties dialog box. Select Component-Level IP from the Category list to display this page. Use this page to create and/or modify component-level IP (CLIP) declaration

### Component-Level IP Page (FPGA Target Properties Dialog Box)

Right-click an FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display the [FPGA Target Properties](/csh?context=lvfpga_lvfpgadialog_fpga_target_properties) dialog box. Select **Component-Level IP** from the **Category** list to display this page.

Use this page to create and/or modify component-level IP (CLIP) [declaration XML files](/csh?context=lvfpga_lvfpgaconcepts_defining_clip) using the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard. You also can add, remove, or rescan declaration XML files on this page.

This page contains the following components:

| Option | Description |
| --- | --- |
| Declaration List MCL | Lists the name of declaration XML files you added. |
| DragDrop Path Ctrl | Lists the path to the declaration XML files you added. |
| Create File | Launches the Configure Component-Level IP wizard to generate a new CLIP interface. |
| Modify File | Launches the Configure Component-Level IP wizard to modify an existing CLIP interface. Select a declaration file from the table and click this button to modify it. |
| Add File | Displays the Select a Component-Level IP Declaration File dialog box, which you use to select a declaration XML file.You also can drag a file from the file system to the Component-Level IP Path field to add the file. |
| Remove File | Removes the declaration XML file you select. |
| Rescan All Files | Reloads all declaration XML files listed in the table. Use the Rescan button if you modify a declaration XML file on disk after you add the file to the target. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/configure-fifo-name-control-type-dialog-box.html language=enus -->
## TOPIC 00071: Configure FIFO Name Control Type Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/configure-fifo-name-control-type-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/configure-fifo-name-control-type-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a FIFO control or constant and select Configure FIFO Type from the shortcut menu to display this dialog box. Use this dialog box to configure the FIFO control or constant. You can specify the data type of the FIFO and the supported methods. When you use a FIFO control as an input on a su

### Configure FIFO Name Control Type Dialog Box

Right-click a FIFO [control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) or [constant](../../../../vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-fifonameconstant-vi.html) and select **Configure FIFO Type** from the shortcut menu to display this dialog box.

Use this dialog box to configure the FIFO control or constant. You can specify the data type of the FIFO and the supported methods. When you use a FIFO control as an input on a [subVI](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls), the input accepts only FIFO items that support the data type and methods you enabled for the FIFO control.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| FIFO Data Type | Specifies the data type of the data in the FIFO. You can select a fixed-point (FXP) data type; a Boolean data type; an 8-, 16-, 32-, or 64-bit signed or unsigned integer data type; or a single-precision floating-point (SGL) data type. You also can select a custom control as the data type. If you select FXP, configure the data type in the Fixed-Point Configuration section. Note DMA and peer-to-peer FIFOs do not support custom data types. Fixed-Point Configuration—Sets the configuration settings for fixed-point data. Set Data Type to FXP to enable the fixed-point settings.LabVIEW automatically configures the Range based on the Encoding settings you specify. Note Fixed-point data type FIFOs do not include an overflow bit when transferring data. To transfer the overflow bit, use a separate FIFO. You also can specify a wider data type for the FIFO so that you can manipulate the data to add the overflow bit when writing to the FIFO and subtract the overflow bit when reading from the FIFO. Encoding—Sets the binary encoding settings for a fixed-point value. Signed—Sets the fixed-point data to represent a signed number. Unsigned—Sets the fixed-point data to represent an unsigned number. Word length—Sets the number of bits that LabVIEW uses to represent the possible fixed-point values. Integer word length—Sets the number of integer bits, or the number of bits to shift the binary point to reach the most significant bit, for all the possible fixed-point values. Integer word length can be positive or negative. Range—Indicates the range for a fixed-point value. Note The fields you use to specify these values display the values in double-precision floating-point representation, so the precision of Maximum, Minimum, and Delta might not be exact in terms of fixed-point representation. However, the deviation is very small. Minimum—Indicates the minimum value for the fixed-point data range. Maximum—Indicates the maximum value for the fixed-point data range. Delta—Indicates the maximum distance between any two sequential numbers in the fixed-point data range. Custom Control—Opens a dialog box in which you can navigate to the custom control you want to use. This button appears only when you select Custom Control in the Data Type pull-down menu. |
| Supported Methods | Use this section to set the methods you can use with the FIFO Method Node. Write—Enables support for the Write and Get Number of Elements to Write methods. Number of Elements per Write—Specifies the number of elements that the FPGA VI can write to the DMA FIFO each clock cycle. The default is 1. Note Support for configurable numbers of elements in FIFOs varies by target. Refer to your target hardware documentation for more information. Read—Enables support for the Read and Get Number of Elements to Read methods. Number of Elements per Read—Specifies the number of elements that the FPGA VI can read from the DMA FIFO each clock cycle. The default is 1. Note Support for configurable numbers of elements in FIFOs varies by target. Refer to your target hardware documentation for more information. Clear—Enables support for the Clear method for a target-scoped or VI-defined FIFO. Peer-to-Peer Streaming Methods—Enables support for peer-to-peer FIFOs.Methods for peer-to-peer FIFOs are not compatible with the Clear method. Individual peer-to-peer FIFOs do not support both the Read and Write methods. The following methods are supported when you place a checkmark in the Peer-to-Peer Streaming Methods checkbox. Disable Enable Get Stream State The following additional methods of the FIFO Method Node are supported when you place a checkmark in the Peer-to-Peer Streaming Methods and Write checkboxes. Flush Flush and Disable Get Number of Elements to Write Write The following additional methods of the FIFO Method Node are supported when you place a checkmark in the Peer-to-Peer Streaming Methods and Read checkboxes. Get Number of Elements to Read Read Flush—Enables support for the Flush method for a DMA target-to-host FIFO or a peer-to-peer writer FIFO. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/configure-memory-name-control-type-dialog-box.html language=enus -->
## TOPIC 00072: Configure Memory Name Control Type Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/configure-memory-name-control-type-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/configure-memory-name-control-type-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a Memory control or constant and select Configure Memory Type from the shortcut menu to display this dialog box. Use this dialog box to configure the Memory control or constant. You can specify the data type of the memory and the supported methods. When you use a Memory control as an inp

### Configure Memory Name Control Type Dialog Box

Right-click a Memory [control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) or [constant](../../../../vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevimemorynameconstant-vi.html) and select **Configure Memory Type** from the shortcut menu to display this dialog box.

Use this dialog box to configure the Memory control or constant. You can specify the data type of the memory and the supported methods. When you use a Memory control as an input on a subVI, the input accepts only memory items that support the data type and methods you enabled for the Memory control.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Memory Data Type | Specifies the data type of the data in the memory. You can select a fixed-point (FXP) data type; a Boolean data type; an 8-, 16-, 32-, or 64-bit signed or unsigned integer data type; or a single-precision floating-point (SGL) data type. You also can select a custom control as the data type.If you select FXP, configure the data type in the Fixed-Point Configuration section. Fixed-Point Configuration—Sets the configuration settings for fixed-point data. Set Data Type to FXP to enable the fixed-point settings.LabVIEW automatically determines the Range based on the Encoding settings you specify. Note Memory items do not support overflow for the fixed-point data type. Encoding—Sets the binary encoding settings for a fixed-point value. Signed—Sets the fixed-point data to represent a signed number. Unsigned—Sets the fixed-point data to represent an unsigned number. Word length—Sets the number of bits that LabVIEW uses to represent the possible fixed-point values. Integer word length—Sets the number of integer bits, or the number of bits to shift the binary point to reach the most significant bit, for all the possible fixed-point values. Integer word length can be positive or negative. Range—Indicates the range for a fixed-point value. Note LabVIEW displays these values in double-precision floating-point representation, so the precision of Maximum, Minimum, and Delta might not be exact in terms of fixed-point representation. However, the deviation is very small. Minimum—Indicates the minimum value for the fixed-point data range. Maximum—Indicates the maximum value for the fixed-point data range. Delta—Indicates the maximum distance between any two sequential numbers in the fixed-point data range. Custom Control—Opens a dialog box in which you can navigate to the custom control you want to use. This button appears only when you select Custom Control in the Data Type pull-down menu. |
| Supported Methods | Use this section to set the methods you can use with the Memory Method Node. Read A—Enables support for the Read method on the A interface of the memory. Read B—Enables support for the Read method on the B interface of the memory. Read support for the B interface supports only memory configured with LUTs and block memory. Write B—Enables support for the Write method on the B interface of the block memory. DRAM Methods—Enables support for methods specific to accessing DRAM. DRAM methods are not compatible with other methods. Maximum Cycles of Read Latency—Specifies the maximum number of cycles of read latency for memory items used with this name control. The default value is 2 cycles of latency. An increase in the number of cycles of latency results in an increase in internal pipelining, which also can increase the maximum frequency of your compiled design. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/configure-register-and-handshake-name-control-type-dialog-box.html language=enus -->
## TOPIC 00073: Configure Register and Handshake Name Control Type Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/configure-register-and-handshake-name-control-type-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/configure-register-and-handshake-name-control-type-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a Register or Handshake control or constant and select Configure Register Type or Configure Handshake Type from the shortcut menu to display this dialog box. Use this dialog box to configure the Register or Handshake control or constant. You can specify the data type of the register item

### Configure Register and Handshake Name Control Type Dialog Box

Right-click a Register or Handshake [control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) or [constant](../../../../vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettenameconstantmergevi-vi.html) and select **Configure Register Type** or **Configure Handshake Type** from the shortcut menu to display this dialog box.

Use this dialog box to configure the Register or Handshake control or constant. You can specify the data type of the [register item or handshake item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant).

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Data Type | Specifies the data type of the data in the register item. Click the arrow to see the list of supported types. If you select FXP, configure the data type in the Fixed-Point Configuration section. Fixed-Point Configuration—Sets the configuration settings for fixed-point data. Set Data Type to FXP to enable the fixed-point settings. LabVIEW automatically determines the Range based on the Encoding settings you specify. Note Register items do not support overflow for the fixed-point data type. Encoding—Sets the binary encoding settings for a fixed-point value. Signed—Sets the fixed-point data to represent a signed number. Unsigned—Sets the fixed-point data to represent an unsigned number. Word length—Sets the number of bits that LabVIEW uses to represent the possible fixed-point values. Integer word length—Sets the number of integer bits, or the number of bits to shift the binary point to reach the most significant bit, for all the possible fixed-point values. Integer word length can be positive or negative. Range—Indicates the range for a fixed-point value. Note LabVIEW displays these values in double-precision floating-point representation, so the precision of Maximum, Minimum, and Delta might not be exact in terms of fixed-point representation. However, the deviation is very small. Minimum—Indicates the minimum value for the fixed-point data range. Maximum—Indicates the maximum value for the fixed-point data range. Delta—Indicates the maximum distance between any two sequential numbers in the fixed-point data range. Custom Control—Opens a dialog box in which you can navigate to the custom control you want to use. This button appears only when you select Custom Control in the Data Type pull-down menu. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/dram-properties-page-fpga-target-properties-dialog-box.html language=enus -->
## TOPIC 00074: DRAM Properties Page (FPGA Target Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/dram-properties-page-fpga-target-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/dram-properties-page-fpga-target-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target in the Project Explorer window and select Properties from the shortcut menu to display the FPGA Target Properties dialog box. Select DRAM Properties from the Category list to display this page. Use this page to configure how LabVIEW implements the DRAM in the project and h

### DRAM Properties Page (FPGA Target Properties Dialog Box)

Right-click an FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display the [FPGA Target Properties](/csh?context=lvfpga_lvfpgadialog_fpga_target_properties) dialog box. Select **DRAM Properties** from the **Category** list to display this page.

Use this page to configure how LabVIEW implements the [DRAM](/csh?context=lvfpga_lvfpgaconcepts_fpga_memory_items) in the project and how LabVIEW [arbitrates between DRAM memory items using the same bank](/csh?context=lvfpga_lvfpgaconcepts_fpga_dram_intro).

Note

target hardware documentation

This page includes the following components:

| Option | Description |
| --- | --- |
| DRAM Bank | Specifies which DRAM bank to configure. Mode—Specifies how to represent the DRAM memory in the project.You can select from the following options: LabVIEW FPGA Memories—(Default) LabVIEW creates a DRAM memory item in the project. Socketed CLIP—LabVIEW uses a socketed-CLIP interface to read and write DRAM memory. Memory Items—Lists the DRAM memory items you created with the Memory Properties dialog box. Grant Time (cycles)—Specifies the amount of time in cycles that LabVIEW grants access to each partition of DRAM memory. LabVIEW grants access to each partition using round robin scheduling. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/execution-mode-fpga-target-properties-dialog-box.html language=enus -->
## TOPIC 00075: Execution Mode (FPGA Target Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/execution-mode-fpga-target-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/execution-mode-fpga-target-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target in the Project Explorer window and select Properties from the shortcut menu to display the FPGA Target Properties dialog box. Select Execution Mode from the Category list to display this page. Use this page to select the execution mode of the FPGA VI. The Simulation and Si

### Execution Mode (FPGA Target Properties Dialog Box)

Right-click an FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display the [FPGA Target Properties](/csh?context=lvfpga_lvfpgadialog_fpga_target_properties) dialog box. Select **Execution Mode** from the **Category** list to display this page.

Use this page to select the execution mode of the FPGA VI. The **Simulation** and **Simulation with Real I/O** options are useful for debugging an FPGA VI because you can test the logic of an FPGA VI before compiling the FPGA VI.

This page includes the following components:

| Option | Description |
| --- | --- |
| FPGA Target | Executes the FPGA VI on the FPGA target. |
| Simulation | Specifies whether to Use Simulated I/O or Use Custom VI for FPGA I/O when executing the FPGA VI on a development computer. VI Path—Specifies the path to the custom VI for FPGA I/O.This option is available only if you select Use Custom VI for FPGA I/O. New—Creates a new custom VI. LabVIEW calls the custom VI whenever FPGA I/O Nodes, FPGA I/O Property Nodes, or FPGA I/O Method Nodes execute on the block diagram of the FPGA VI.You can use the custom VI as part of a test bench. Open VI—Opens the custom VI you specify in the VI Path. |
| Simulation with Real I/O | Executes the FPGA VI on the development computer using I/O from the FPGA target. Some FPGA targets do not support this option. Some FPGA targets that support this option do not support all I/O resources. |
| Third-Party Simulation | Executes the FPGA VI in an installed third-party simulator. Select this execution mode to enable cycle-accurate simulation. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/general-page-fpga-target-properties-dialog-box.html language=enus -->
## TOPIC 00076: General Page (FPGA Target Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/general-page-fpga-target-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/general-page-fpga-target-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target in the Project Explorer window and select Properties from the shortcut menu to display the FPGA Target Properties dialog box. The General page appears by default. Use this page to set general characteristics of the FPGA target. This page contains the following components:

### General Page (FPGA Target Properties Dialog Box)

Right-click an FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display the [FPGA Target Properties](/csh?context=lvfpga_lvfpgadialog_fpga_target_properties) dialog box. The **General** page appears by default.

Use this page to set general characteristics of the FPGA target.

This page contains the following components:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the FPGA target that appears in the Project Explorer window. |
| Resource | Specifies the FPGA target hardware. For FPGA targets that appear in NI Measurement & Automation Explorer (MAX), this is the resource or device name. |
| Target Information | Displays the FPGA target class of the FPGA target you configured in the Project Explorer window as well as other target-specific information. For example, the NI PXI-7831R FPGA target class is PXI-7831R and the FPGA device family is Virtex-II. The functionality and options that you can configure on an FPGA target depend on the FPGA target class and what the FPGA target class supports. You cannot change the Target Class after you add the FPGA target to the Project Explorer window. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/networked-computer-device-properties-dialog-box.html language=enus -->
## TOPIC 00077: Networked Computer/Device Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/networked-computer-device-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/networked-computer-device-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click Networked Computer/Device in the Project Explorer window and select Properties from the shortcut men to display this dialog box. Networked Computer/Device appears in the project if you add an FPGA target from a remote system. Use this dialog box to enter t

### Networked Computer/Device Properties Dialog Box

In the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Networked Computer/Device** in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut men to display this dialog box. **Networked Computer/Device** appears in the project if you [add an FPGA target from a remote system](/csh?context=lvfpga_lvfpgahelp_adding_an_fpga_target).

Use this dialog box to enter the name and IP address for a specific remote FPGA system. [Verify communication with a remote FPGA target](/csh?context=lvfpga_lvfpgahosthelp_fpga_using_rpc) before you enter the name and IP address.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Name | Specifies the name of an existing networked computer or device, which is known as a remote FPGA system. Name appears in the Project Explorer window. |
| Address | Specifies the IP address of an existing networked computer or device, which is known as a remote FPGA system. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/framework/providers/lvfpga-llb/top-level-clock-page-fpga-target-properties-dialog-box.html language=enus -->
## TOPIC 00078: Top-Level Clock Page (FPGA Target Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/framework/providers/lvfpga-llb/top-level-clock-page-fpga-target-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/framework/providers/lvfpga-llb/top-level-clock-page-fpga-target-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target in the Project Explorer window and select Properties from the shortcut menu to display the FPGA Target Properties dialog box. Select Top-Level Clock from the Category list to display this page. Use this page to set the top-level clock of the FPGA target. Supported top-leve

### Top-Level Clock Page (FPGA Target Properties Dialog Box)

Right-click an FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display the [FPGA Target Properties](/csh?context=lvfpga_lvfpgadialog_fpga_target_properties) dialog box. Select **Top-Level Clock** from the **Category** list to display this page.

Use this page to set the top-level [clock](/csh?context=lvfpga_lvfpgahelp_applying_fpga_clocks_and_timing_title) of the FPGA target. Supported top-level clocks vary according to FPGA target.

This page includes the following components:

| Option | Description |
| --- | --- |
| Use Target Default | Specifies that the top-level clock of the FPGA target is the default target base clock. |
| Select Clock | Allows you to select a clock other than the default FPGA target clock as the top-level clock. Select from existing clocks included with the target or derived clocks you create. |
| Configured Clocks | Displays the list of available clocks you can set as the top-level FPGA target clock. You can select a clock in this list if you click the Select Configured Clock option. Note You cannot select a clock that can be disabled as a top-level clock because the clock might prevent execution of the FPGA VI. Therefore, you cannot select an external clock as a top-level clock. You also cannot select a clock that must be enabled and disabled at run time. |
| Selection | Displays information about the top-level clock and if the FPGA target supports the clock you want to use. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/rvi/startipgenerators/start-ip-generator-dialog-box.html language=enus -->
## TOPIC 00079: Start IP Generator Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/rvi/startipgenerators/start-ip-generator-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/rvi/startipgenerators/start-ip-generator-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA target and select Start IP Generator from the shortcut menu to display this dialog box. You must have one or more IP generators installed and licensed to access this dialog box. Use this dialog box to display available IP generators and start the IP generation wizard for a specif

### Start IP Generator Dialog Box

Right-click an FPGA target and select **Start IP Generator** from the shortcut menu to display this dialog box. You must have one or more IP generators installed and licensed to access this dialog box.

Use this dialog box to display available IP generators and start the IP generation wizard for a specific generator.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Select IP Generator | Lists all installed IP generators for FPGA targets. Adaptive Filters—Generates LabVIEW FPGA code for a fixed-point adaptive filter that you create with the LabVIEW Digital Filter Design Toolkit. LMS Adaptive Filter Digital Filters—Generates LabVIEW FPGA code for a fixed-point digital filter that you create with the LabVIEW Digital Filter Design Toolkit. Single-Rate Filter Multirate Filter Multistage Multirate Filter Moving Average Filter |
| Description | Displays a description of the IP generator you select from the Select IP Generator list. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/rvi/startupprojectwizard/fpga-project-wizard.html language=enus -->
## TOPIC 00080: FPGA Project Wizard

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/rvi/startupprojectwizard/fpga-project-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/rvi/startupprojectwizard/fpga-project-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can display this wizard in the following ways: In the Create Project dialog box: Select LabVIEW FPGA Project from the Project List.Select Templates from the Filters list at left and then select LabVIEW FPGA Project. In the New dialog box, select FPGA Project from the Create New list. Use the FPG

### FPGA Project Wizard

You can display this wizard in the following ways:

- In the Create Project dialog box:
  - Select LabVIEW FPGA Project from the Project List .
  - Select Templates from the Filters list at left and then select LabVIEW FPGA Project .
- In the New dialog box, select FPGA Project from the Create New list.

Use the FPGA Project Wizard to create a LabVIEW project for a specific FPGA target. The wizard lists any installed target wizards. Select a target and click the **Next** button to display the wizard for the target.

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=resource/rvi/stockio/private/advanced-code-generation-page-fpga-i-o-node-properties-dialog-box.html language=enus -->
## TOPIC 00081: Advanced Code Generation Page (FPGA I/O Node Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `resource/rvi/stockio/private/advanced-code-generation-page-fpga-i-o-node-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/resource/rvi/stockio/private/advanced-code-generation-page-fpga-i-o-node-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Advanced Code Generation in the Category list of the FPGA I/O Node Properties dialog box to display this page. Use this page to select code generation options, such as the number of synchronizing registers. Supported options, values, and defaults depend on the FPGA target and FPGA I/O you use

### Advanced Code Generation Page (FPGA I/O Node Properties Dialog Box)

Select **Advanced Code Generation** in the **Category** list of the [FPGA I/O Node Properties](/csh?context=lvfpga_lvfpgadialog_fpga_io_node_properties) dialog box to display this page.

Use this page to select code generation options, such as the number of synchronizing registers. Supported options, values, and defaults depend on the FPGA target and FPGA I/O you use. This page displays only the options and values supported for the selected FPGA I/O. Some FPGA targets and FPGA I/O nodes might not allow access to this page at all.

This page can contain the following option:

| Option | Description |  |
| --- | --- | --- |
| NumberOfSyncRegistersForRead | Specifies the number of synchronizing registers between the FPGA target hardware interface and the FPGA I/O Node executing on the FPGA target. The FPGA target hardware interface might be a physical I/O connector on the device or a connection to a section of the FPGA that contains circuitry designed by NI. Each synchronizing register executes in one clock cycle. If you use the FPGA I/O Node outside a single-cycle Timed Loop, LabVIEW places one additional synchronizing register, or holding register, that attempts to hold the digital value constant for subsequent operations in the FPGA VI. These synchronizing registers are in addition to enable chain registers that are present outside of the single-cycle Timed Loop. If you use the FPGA I/O Node inside a single-cycle Timed Loop, LabVIEW does not add the additional register because logic inside a single-cycle Timed Loop executes every clock cycle. However, you must use caution when synchronizing I/O in single-cycle Timed Loops. Caution Select 0 only if you also use component-level IP (CLIP) and the HDL code contains its own synchronization registers. Otherwise, you might introduce metastable data in the FPGA VI and experience unpredictable behavior. Supported options typically include the following: Inherit from the Project Item—Specifies to use the number of synchronizing registers configured in the Advanced Code Generation page of the FPGA I/O Properties dialog box. Auto—Specifies that LabVIEW uses the default number of synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. The following table lists the number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 2 0 Outside an SCTL 1 1 0—Specifies that LabVIEW does not place any synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. Do not select this option for most FPGA Module applications. Note If you select 0 for digital input and digital output resources in a single-cycle Timed Loop, you create a combinatorial circuit between the two resources. The combinatorial circuit might cause glitches on the output signal. The following table lists the total number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 0 0 Outside an SCTL 1 1 1—Specifies that LabVIEW place one synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. Note You might encounter metastable data if the FPGA I/O Node is in a single-cycle Timed Loop and set with this option when the data is not already synchronized to the clock of the single-cycle Timed Loop. The following table lists the total number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 1 0 Outside an SCTL 2 1 2—Specifies that LabVIEW place two synchronizing registers between the FPGA hardware I/O interface and the FPGA I/O Node implemented on the FPGA. Select this option to avoid metastability if the value of the input to the FPGA I/O Node read element might change while the FPGA I/O Node samples the FPGA target hardware interface. If you select this option for an FPGA I/O Node within a single-cycle Timed Loop, you have no metastable data in the FPGA VI. The following table lists the total number of registers LabVIEW uses depending on the location of the FPGA I/O Node on the block diagram. Location Synchronizing Registers Enable Chain Register Inside an SCTL 2 0 Outside an SCTL 3 1 |  |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 2 | 0 |
| Outside an SCTL | 1 | 1 |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 0 | 0 |
| Outside an SCTL | 1 | 1 |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 1 | 0 |
| Outside an SCTL | 2 | 1 |
| Location | Synchronizing Registers | Enable Chain Register |
| Inside an SCTL | 2 | 0 |
| Outside an SCTL | 3 | 1 |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/clock-selections-page-component-level-ip-properties-dialog-box.html language=enus -->
## TOPIC 00082: Clock Selections Page (Component-Level IP Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/clock-selections-page-component-level-ip-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/clock-selections-page-component-level-ip-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Component Level IP Properties dialog box, select Clock Selections from the Category list to display this page. Use this page to link each ToCLIP clock port defined by the CLIP to a clock on the FPGA target. You can link ToCLIP clock ports to FPGA target clocks in the following ways: Add the F

### Clock Selections Page (Component-Level IP Properties Dialog Box)

In the [Component Level IP Properties](/csh?context=lvfpga_lvfpgadialog_clip_properties) dialog box, select **Clock Selections** from the **Category** list to display this page.

Use this page to link each ToCLIP clock port defined by the CLIP to a clock on the FPGA target. You can link ToCLIP clock ports to FPGA target clocks in the following ways:

- Add the FPGA target clock manually to the LabVIEW project before linking from this page.
- Click Create Necessary Clocks to add the appropriate FPGA target clock and link to it automatically.

This page includes the following components:

| Option | Description |
| --- | --- |
| CLIP Clock MCL | Lists clock(s) you defined in the CLIP declaration XML file. Clock Name—Lists the names of the defined clocks. Clock Requirement—Displays the requirement for the FPGA target clock as the CLIP declaration XML defines it. The CLIP declaration XML can specify three types of clock requirements: A single clock frequency A clock within a frequency range A specific clock under the FPGA targetNote In order to specify this type of clock requirement, you must add the SpecifyTargetClock tag to the CLIP declaration XML file manually. Connection—Displays the current FPGA target clock associated with the defined CLIP clock. If no available FPGA target clock meets the Frequency requirement, this field displays the following message: No Appropriate Clock Frequency—Displays the frequency at which the CLIP clock runs for the current instantiation of the CLIP. |
| Frequency | Specifies an override frequency for a CLIP clock that you select in the Clock Name column if that clock has a Clock Requirement of a frequency range. The override frequency must fall within the required range. If the clock has any other type of Clock Requirement, this field displays the required clock frequency and cannot be edited. |
| Connection | Lists clocks available on the FPGA target. |
| Create Necessary Clocks | Creates FPGA target clocks that meet the Clock Requirement for any defined ToCLIP clocks without associated FPGA target clocks in the Connection column and links these clocks to appropriate CLIP clocks automatically. If you have defined CLIP clocks with a frequency range clock requirement, you must specify single clock frequencies for these clocks before clicking Create Necessary Clocks. Note Clocks you create by clicking Create Necessary Clocks remain available even if you close the Clock Selections Page by clicking Cancel. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/configure-timed-loop-dialog-box.html language=enus -->
## TOPIC 00083: Configure Timed Loop Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/configure-timed-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/configure-timed-loop-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In an FPGA VI, double-click the Input Node of a Timed Loop or right-click the node and select Configure Input Node from the shortcut menu to display this dialog box. Use this dialog box to configure options on a single-cycle Timed Loop in an FPGA VI. To specify the clock that controls a single-cycle

### Configure Timed Loop Dialog Box

In an FPGA VI, double-click the Input Node of a [Timed Loop](/csh?productcategories=147794&context=lvcore_glang_timed_loop) or right-click the node and select **Configure Input Node** from the shortcut menu to display this dialog box.

Use this dialog box to configure options on a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) in an FPGA VI.

Note

Source Name

subVIs with configurable clocks

You can specify that a single-cycle Timed Loop uses any [clock](/csh?context=lvfpga_lvfpgahelp_applying_fpga_clocks_and_timing_title) under the FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window. You can have multiple single-cycle Timed Loops on a block diagram, each executing at different clock rates. Double-click the **Input Node** of a Timed Loop to display this dialog box.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Loop Name | Specifies the name of the single-cycle Timed Loop in the FPGA VI. You can use this name to identify the single-cycle Timed Loop in the Timing Violation Analysis window. |
| Require removal of implicit enable signals | Requires the compiler to remove the implicit enable signal from the single-cycle Timed Loop. When it is not possible for the compiler to remove the implicit enable signal, the compiler returns a code generation error. By default, this checkbox does not contain a checkmark. Note This option is only visible for targets that support the removal of implicit enable signals. Refer to your target hardware documentation for more information about support for removing implicit enable signals. |
| Use Parent Diagram | Specifies that the single-cycle Timed Loop uses the top-level FPGA target clock. |
| Select Timing Source | Allows you to select a clock other than the top-level FPGA target clock. You can select the FPGA target base clock or any FPGA target clock you derive. |
| Available Timing Sources | Displays a list of the available timing sources that appear under the FPGA target in the Project Explorer window. |
| Selection | Displays details about the clock you select as the single-cycle Timed Loop clock. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/data-type-page-fpga-register-properties-memory-properties-fifo-properties-and-fpga-handshake-properties-dialog-boxes.html language=enus -->
## TOPIC 00084: Data Type Page (FPGA Register Properties, Memory Properties, FIFO Properties, and FPGA Handshake Properties Dialog Boxes)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/data-type-page-fpga-register-properties-memory-properties-fifo-properties-and-fpga-handshake-properties-dialog-boxes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/data-type-page-fpga-register-properties-memory-properties-fifo-properties-and-fpga-handshake-properties-dialog-boxes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the FPGA Register Properties dialog box, the Memory Properties dialog box, the FIFO Properties dialog box, or the FPGA Handshake Properties dialog box, select Data Type from the Category list to display this page. Use this page to specify the data type for a FIFO, memory, register item, or a hand

### Data Type Page (FPGA Register Properties, Memory Properties, FIFO Properties, and FPGA Handshake Properties Dialog Boxes)

In the [FPGA Register Properties](/csh?context=lvfpga_lvfpgadialog_fpga_register_prop_db) dialog box, the [Memory Properties](/csh?context=lvfpga_lvfpgadialog_fpga_memory_prop_db) dialog box, the [FIFO Properties](/csh?context=lvfpga_lvfpgadialog_edit_fifo) dialog box, or the [FPGA Handshake Properties](/csh?context=lvfpga_lvfpgadialog_fpga_handshake_prop_db) dialog box, select **Data Type** from the **Category** list to display this page.

Use this page to specify the data type for a [FIFO](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data), [memory](/csh?context=lvfpga_lvfpgaconcepts_fpga_memory_items), [register item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant), or a [handshake item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant).

This page includes the following components:

| Option | Description |
| --- | --- |
| Data Type | Specifies the data type of the data in the item you are configuring. Click the arrow to see the list of supported types. If you select FXP, configure the data type in the Fixed-Point Configuration section. Note DMA and peer-to-peer FIFOs do not support custom data types. Fixed-Point Configuration—Sets the configuration settings for fixed-point data. Set Data Type to FXP to enable the fixed-point settings.LabVIEW automatically determines the Range based on the Encoding settings you specify. Note Fixed-point data type FIFOs do not include an overflow bit when transferring data. If you need to transfer the overflow bit, use a separate FIFO, or specify a wider data type for the current FIFO and manipulate the data to add the overflow bit when writing to the FIFO and separate the overflow bit when reading from the FIFO. Encoding—Sets the binary encoding settings for a fixed-point value. Signed—Sets the fixed-point data to represent a signed number. Unsigned—Sets the fixed-point data to represent an unsigned number. Word length—Sets the number of bits that LabVIEW uses to represent the possible fixed-point values. Integer word length—Sets the number of integer bits, or the number of bits to shift the binary point to reach the most significant bit, for all the possible fixed-point values. Integer word length can be positive or negative. Range—Indicates the range for a fixed-point value. Note LabVIEW displays these values in double-precision floating-point representation, so the precision of Maximum, Minimum, and Delta might not be exact in terms of fixed-point representation. However, the deviation is very small. Minimum—Indicates the minimum value for the fixed-point data range. Maximum—Indicates the maximum value for the fixed-point data range. Delta—Indicates the maximum distance between any two sequential numbers in the fixed-point data range. Custom Control—Opens a dialog box in which you can navigate to the custom control you want to use. This button appears only when you select Custom Control in the Data Type pull-down menu. |
| Maximum Data Width for DRAM | Indicates the physical port width of the DRAM. The data type you select for the DRAM memory cannot be wider than the data width. This option is available only for memory items implemented using DRAM. Make sure the sum of the data widths of all items in a custom control is not greater than the Maximum Data Width for DRAM. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/fpga-base-clock-properties-dialog-box.html language=enus -->
## TOPIC 00085: FPGA Base Clock Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/fpga-base-clock-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/fpga-base-clock-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click the base clock in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use the FPGA Base Clock Properties dialog box to configure an FPGA base clock associated with an FPGA target. The options available in this dialog box vary according to

### FPGA Base Clock Properties Dialog Box

Right-click the base clock in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** from the shortcut menu to display this dialog box.

Use the **FPGA Base Clock Properties** dialog box to [configure an FPGA base clock](/csh?context=lvfpga_lvfpgahelp_config_fpga_base_clk) associated with an FPGA target.

The options available in this dialog box vary according to FPGA target and clock.

This dialog box might include the following components:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the clock that appears in the Project Explorer window. |
| Resource | Specifies the resource the FPGA target uses as the base clock. |
| Compile for single frequency | Specifies the frequency of the base clock if the clock is not variable.You can select MHz, kHz, or Hz as the unit of frequency. |
| Compile for range of frequencies | Specifies to compile an FPGA VI for a range of clock frequencies. You must specify the Minimum and the Maximum frequencies of the base clock to specify the range. |
| Minimum | Specifies the minimum frequency of the base clock.You can select MHz, kHz, or Hz as the unit of frequency. |
| Maximum | Specifies the maximum frequency of the base clock.You can select MHz, kHz, or Hz as the unit of frequency. |
| Min Duty Cycle (% High) | Specifies the minimum percentage of time the base clock remains high over one period. |
| Max Duty Cycle (% High) | Specifies the maximum percentage of time the base clock remains high over one period. |
| Accuracy (ppm) | Specifies the accuracy of the base clock in parts per million. |
| Peak Period Jitter (ps) | Specifies the maximum period jitter of the base clock in picoseconds. |
| Supports and Requires Runtime Enable and Disable | Specifies whether you must use the Start Enabling FPGA Clock and Start Disabling FPGA Clock Vis to enable and disable the base clock.This option is available only for clocks that support enabling and disabling at run time. Select this option if the clock might glitch, causing setup or hold violations on flip-flops in the clock domain using the clock. You might also select this option if the I/O that is assumed to be synchronous to the clock becomes unsynchronized for a period of time. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/fpga-derived-clock-properties-dialog-box.html language=enus -->
## TOPIC 00086: FPGA Derived Clock Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/fpga-derived-clock-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/fpga-derived-clock-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA base, external, or CLIP clock in the Project Explorer window and select New FPGA Derived Clock from the shortcut menu to display this dialog box. You also can right-click an existing derived clock in the Project Explorer window and select Properties to display this dialog box. Us

### FPGA Derived Clock Properties Dialog Box

Right-click an FPGA base, external, or CLIP clock in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **New FPGA Derived Clock** from the shortcut menu to display this dialog box. You also can right-click an existing derived clock in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Properties** to display this dialog box.

Use the **FPGA Derived Clock Properties** dialog box to [create and configure](/csh?context=lvfpga_lvfpgahelp_creating_fpga_derived_clk) FPGA-derived clocks. You can scale the frequency of an FPGA target base, external, or CLIP clock by using a derived clock. If you do not know if the FPGA target supports the frequency you want to use, enter a value in the **Desired Derived Frequency** and read the resulting **Message** text. LabVIEW selects a supported clock using the equation in the **Actual Derived Configuration** and determines a **Derived Frequency** as close as possible to the **Desired Derived Frequency**.

Support for FPGA-derived clocks varies according to FPGA target.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the derived clock that appears in the Project Explorer window below the parent clock. |
| Parent Clock Name | Displays the name of the parent clock from which the derived clock was created. |
| Desired Derived Frequency | Specifies the frequency you want the FPGA-derived clock to use. |
| Actual Derived Configuration | Displays the equation LabVIEW uses to determine the frequency of the derived clock. LabVIEW optimizes the derived configuration to use the least amount of resources on the FPGA. Parent Frequency—Displays the frequency of the parent clock from which you derive the new clock. Multiplier—Displays the numerator of the number by which LabVIEW multiplies the Parent Frequency to determine the derived frequency of the FPGA-derived clock. Divisor—Displays the denominator of the number by which LabVIEW multiplies the Parent Frequency to determine the derived frequency of the FPGA-derived clock. Derived Frequency—Displays the frequency of the resulting derived clock. Parent Period—Displays the period of the parent FPGA clock. Derived Period—Displays the period of the FPGA-derived clock. |
| Message | Displays information about the FPGA-derived clock. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/general-page-component-level-ip-properties-dialog-box.html language=enus -->
## TOPIC 00087: General Page (Component-Level IP Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/general-page-component-level-ip-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/general-page-component-level-ip-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Component-Level IP Properties dialog box, select General from the Category list to display this page. Use this page to name the component-level IP (CLIP) item in the project and select the CLIP declaration to use. Before you can add the CLIP item to the project, you must add the CLIP to the t

### General Page (Component-Level IP Properties Dialog Box)

In the [Component-Level IP Properties](/csh?context=lvfpga_lvfpgadialog_clip_properties) dialog box, select **General** from the **Category** list to display this page.

Use this page to name the [component-level IP (CLIP)](/csh?context=lvfpga_lvfpgaconcepts_using_component_ip) item in the project and select the CLIP declaration to use.

Note

Component-Level IP

This page includes the following options:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the CLIP instance in the Project Explorer window. The name must only contain English letters and numbers, spaces, periods, dashes, and underscores. |
| CLIP Declaration | Specifies the declaration to use for the CLIP item. You must add the declaration to the Component-Level IP FPGA Target Properties page before you can use the declaration.You can select the same CLIP declaration for multiple CLIP items. However, each CLIP item must have a unique name. Do not prefix CLIP constant names with k. |
| CLIP Description | Displays the description of the CLIP from the declaration XML file. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/general-page-fifo-properties-dialog-box.html language=enus -->
## TOPIC 00088: General Page (FIFO Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/general-page-fifo-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/general-page-fifo-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the FIFO Properties dialog box, select General from the Category list to display this page. Use this page to edit properties for FIFOs. This page includes the following components: Option Description Name Specifies the name of the FIFO that appears in the Project Explorer window or in the VI-Defi

### General Page (FIFO Properties Dialog Box)

In the [FIFO Properties](/csh?context=lvfpga_lvfpgadialog_edit_fifo) dialog box, select **General** from the **Category** list to display this page.

Use this page to edit properties for [FIFOs](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data).

This page includes the following components:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the FIFO that appears in the Project Explorer window or in the VI-Defined FIFO Configuration node. The name also appears in the FIFO Method Node on the block diagram, and you can use it in FIFO name controls and constants to access target-scoped FIFOs. |
| Type | Specifies the type of FIFO to use. This option is not available for VI-defined FIFOs. Target-Scoped—FIFOs can transfer data within the FPGA VI as well as between FPGA VIs under the same target in the Project Explorer window. Host to Target - DMA or Target to Host - DMA—DMA FIFOs can transfer data between the host VI and target. Peer to Peer Writer or Peer to Peer Reader—FIFOs can transfer data using a peer-to-peer stream. |
| Disable on Overflow | Specifies to disable the peer-to-peer stream when the writer FIFO attempts to write to the stream and fails. This option is only available for peer-to-peer writer FIFOs. |
| Disable on Underflow | Specifies to disable the peer-to-peer stream when the reader FIFO does not receive data from the stream. This option is only available for peer-to-peer reader FIFOs. |
| Requested Number of Elements | Specifies the desired number of elements the FIFO can hold. The maximum number of elements the FIFO can hold depends on the Implementation you select and the amount of resources available on the FPGA for the Implementation. If the FIFO uses built-in control logic, the maximum number of elements also depends on the data type. The width of the built-in FIFO must be less than or equal to 1024. If the FPGA does not have enough resources for the Requested Number of Elements you enter, the FPGA VI fails to compile. If you select Host to Target - DMA or Target to Host - DMA in the Type pull-down menu, Requested Number of Elements specifies the size of the FPGA FIFO of the DMA channel. Maximum DMA FIFO size varies by target. Refer to the specific FPGA target hardware documentation for more information about DMA FIFO size limitations. If you select Block Memory in the Implementation control, restrictions apply to the number of elements the FIFO can hold. Actual Number of Elements indicates the number of elements in the FIFO, which may not be the same as Requested Number of Elements. Note If you experience timeout during DMA transfers from the FPGA to a host, use the FIFO.Configure method of the Invoke Method function and increase the Depth parameter rather than increasing the Requested Number of Elements. Increasing the Depth parameter increases the size of the host-side buffer, which is more likely to resolve the timeout and does not increase FPGA device utilization. |
| Implementation | Specifies the type of storage the FIFO implements on the FPGA. You can specify the implementation only for target-scoped and VI-defined FIFOs.Contains the following options: Flip-Flops—Stores the data in flip-flops available on the FPGA and provides the fastest performance. NI recommends using this option for small FIFOs, up to 100 bytes. You cannot use FIFOs with an Implementation of Flip-Flops across multiple clock domains. Look-Up Table—Stores the data in look-up tables available on the FPGA. Xilinx literature describes this implementation as distributed RAM or LUT RAM. NI recommends using this option for FIFOs that are 100–300 bytes. You cannot use FIFOs with an Implementation of Look-Up Table across multiple clock domains. Block Memory—Stores the data using embedded blocks of memory. Xilinx literature describes this implementation as block RAM or BRAM. NI recommends using this option for FIFOs larger than 300 bytes.Note If you select the Block Memory option, you might not be able to read data in a target-scoped FIFO or VI-defined FIFO until up to six clock cycles after you write the data to the FIFO. If you select the timeout interface, use the Timed Out? output of the FIFO Method Node that invokes the Read method to determine when the upstream data is ready. If you select the handshaking interface, use the Output Valid output of the FIFO Method Node that invokes the Read method to determine whether the upstream data is ready. UltraRAM—Stores the data in UltraRAM resources available on most Xilinx UltraScale+ targets. Xilinx literature describes this implementation as URAM. This option is available only when you select Target-Scoped in Type. You cannot use FIFOs with an Implementation of UltraRAM across multiple clock domains.Note The Get Number of Elements to Read and Get Number of Elements to Write methods do not support FIFOs implemented using UltraRAM. All of the above implementation options contain the following components: Actual Number of Elements—Returns the configured number of elements. Sometimes the requested number of elements is not compatible with the FIFO configuration. In this case, LabVIEW coerces the requested number of elements to a compatible number and Actual Number of Elements returns this number. If you select the built-in or target-optimal control logic, Actual Number of Elements might return multiple numbers. Interpret these numbers in the following ways: Built-In—Actual Number of Elements returns two numbers, which LabVIEW uses when the handshaking interface is disabled or enabled, respectively. Note (Xilinx Vivado)The actual number of elements in the FIFO is unknown at configuration time. Actual Number of Elements returns only one number, which is the closest power of two, greater than Requested Number of Elements. This number is a minimum guaranteed number, which might be smaller than the actual number of elements in the FIFO. Target-Optimal—LabVIEW implements the FIFO using either slice fabric or built-in control logic, depending on the clock domain and target type. Actual Number of Elements returns two or three numbers: the first one for the slice fabric control logic and the other(s) for the built-in control logic. Control Logic—Specifies how the FPGA implements the FIFO. Slice Fabric—Specifies that the FPGA uses flip-flops, LUTs, and block memory to implement the control logic for the FIFO. Target Optimal—Specifies that the FPGA uses built-in FIFO control logic or slice fabric control logic, depending on the target and application. Built-In—Specifies that the FPGA uses built-in FIFO control logic. Not all FPGAs support built-in FIFO control logic and restrictions apply. Note (Xilinx Vivado)If you select the built-in control logic, you cannot use this FIFO with the Get Number of Elements to Read or Get Number of Elements to Write method because the actual number of elements in the FIFO is unknown at configuration time. In simulation mode, the Timed Out? output value of the Read or Write method might not reflect the actual behavior on hardware because these methods use the conservative number in Actual Number of Elements as the FIFO depth, which might be smaller than the actual number of elements in the FIFO. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/general-page-fpga-register-properties-and-fpga-handshake-properties-dialog-boxes.html language=enus -->
## TOPIC 00089: General Page (FPGA Register Properties and FPGA Handshake Properties Dialog Boxes)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/general-page-fpga-register-properties-and-fpga-handshake-properties-dialog-boxes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/general-page-fpga-register-properties-and-fpga-handshake-properties-dialog-boxes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the FPGA Register Properties dialog box or the FPGA Handshake Properties dialog box, select General from the Category list to display this page. Use this page to edit the Name property for a register item or a handshake item. This page includes the following component: Option Description Name Spe

### General Page (FPGA Register Properties and FPGA Handshake Properties Dialog Boxes)

In the [FPGA Register Properties](/csh?context=lvfpga_lvfpgadialog_fpga_register_prop_db) dialog box or the [FPGA Handshake Properties](/csh?context=lvfpga_lvfpgadialog_fpga_handshake_prop_db) dialog box, select **General** from the **Category** list to display this page.

Use this page to edit the **Name** property for a [register item or a handshake item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant).

This page includes the following component:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the register item or handshake item that appears in the Project Explorer window, the VI-Defined Register Configuration node, or the VI-Defined Handshake Configuration. The name also appears in the Register Method Node or Handshake Method Nodeon the block diagram. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/general-page-memory-properties-dialog-box.html language=enus -->
## TOPIC 00090: General Page (Memory Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/general-page-memory-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/general-page-memory-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Memory Properties dialog box, select General from the Category list to display this page. Use this page to edit properties for memory items. This page includes the following components: Option Description Name Specifies the name of the memory item that appears in the Project Explorer window o

### General Page (Memory Properties Dialog Box)

In the [Memory Properties](/csh?context=lvfpga_lvfpgadialog_fpga_memory_prop_db) dialog box, select **General** from the **Category** list to display this page.

Use this page to edit properties for [memory items](/csh?context=lvfpga_lvfpgaconcepts_fpga_memory_items).

This page includes the following components:

| Option | Description |
| --- | --- |
| Name | Specifies the name of the memory item that appears in the Project Explorer window or in the VI-Defined Memory Configuration node. The name also appears in the Memory Method Node on the block diagram. |
| Requested Number of Elements | Specifies the number of elements you want to hold in the memory item.The actual memory usage, in bytes, depends on the number of elements and the data type you specify. |
| Implementation | Specifies how the FPGA stores this memory item.Contains the following options: Block Memory—Stores the data using embedded blocks of memory.Xilinx describes this implementation as block RAM or BRAM. Memory items using embedded block memory take at least one clock cycle to execute. Use block memory in the following situations. • In a single-cycle Timed Loop, when you do not need to access this memory during the same cycle as the one in which you provide the address. • When the amount of memory you need is large. • When you do not have enough free resources available on the FPGA. This option contains the following components: Actual Number of Elements—Returns the configured number of elements. Sometimes the requested number of elements is not compatible with the memory configuration. In this case, LabVIEW coerces the Actual number of elements to a compatible number. Cycles of read latency—Specifies the number of cycles of latency for the Read (Memory Method) of memory items implemented using block memory. The default value is 2 cycles of latency. An increase in cycles of read latency results in an increase in internal pipelining, which also can increase the maximum frequency of your compiled design.The number of cycles required for the Read (Memory Method) to produce valid data is equal to the number of Cycles of read latency. Note When you use the Read (Memory Method) within the single-cycle Timed Loop for a memory item implemented using block memory, the number of Feedback Nodes or uninitialized shift registers wired to the data output must be greater than or equal to the number of Cycles of read latency. If you do not wire enough Feedback Nodes or uninitialized shift registers after the Read (Memory Method), the FPGA VI fails to compile and LabVIEW returns an error. —Look-Up Table—Stores the memory item in look-up tables available on the FPGA. This storage consumes FPGA resources that the FPGA uses for other logical operations, such as addition and subtraction. Xilinx describes this implementation as distributed RAM or LUT RAM.Use look-up tables in the following situations. • You are accessing this memory in a single-cycle Timed Loop and need to read data from the memory item during the same cycle as the one in which you provide the address. • The amount of memory you need is smaller than the minimum amount of embedded block memory on the FPGA. • You do not have enough free embedded block memory on the FPGA. This option contains the following component: Actual Number of Elements—Returns the configured number of elements. Sometimes the requested number of elements is not compatible with the memory configuration. In this case, LabVIEW coerces the Actual number of elements to a compatible number. —DRAM—Stores the memory item in DRAM available on the FPGA.Not all hardware supports using DRAM for memory. See the DRAM Properties page of the FPGA Target Properties dialog box to configure how LabVIEW implements DRAM in the project.This option contains the following components: Actual Number of Elements—Returns the configured number of elements. Sometimes the requested number of elements is not compatible with the memory configuration. In this case, LabVIEW coerces the Actual number of elements to a compatible number. Maximum outstanding requests for data—Specifies the number of maximum requests for data that the application allows to be outstanding. DRAM bank—Specifies which DRAM bank to use. Allocated for this Memory—Indicates the amount of memory allocated in this memory item. Allocated Elsewhere—Indicates how much memory is allocated in other items. Available—Indicates how much memory is still available in the bank. Total Physical Size—Indicates the total size of the bank. |
| Persist memory values between VI executions while executing on the development computer | If you do not place a checkmark in this checkbox, the values in this memory item reset to the initial values as specified on the Initial Values page of the Memory Properties dialog box between VI executions while executing on the development computer.If you place a checkmark in this checkbox, LabVIEW retains values in this memory item between VI executions while executing on the development computer but may result in higher memory consumption and slower execution for large memories. By default, this checkbox does not contain a checkmark for new LabVIEW projects. Note The checkbox contains a checkmark for previous versions of LabVIEW projects in order to maintain the behavior of previous versions of FPGA applications. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/generics-and-syntax-check-page-component-level-ip-properties-dialog-box.html language=enus -->
## TOPIC 00091: Generics and Syntax Check Page (Component-Level IP Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/generics-and-syntax-check-page-component-level-ip-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/generics-and-syntax-check-page-component-level-ip-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Component-Level IP Properties dialog box, select Generics from the Category list to display this page. Use this page to view and override the default generic values defined in the CLIP declaration file for the IP. If you override the default generic values, you must check the syntax of the fi

### Generics and Syntax Check Page (Component-Level IP Properties Dialog Box)

In the [Component-Level IP Properties](/csh?context=lvfpga_lvfpgadialog_clip_properties) dialog box, select **Generics** from the **Category** list to display this page.

Use this page to view and override the default generic values defined in the CLIP declaration file for the IP. If you override the default generic values, you must check the syntax of the file .

This page includes the following components:

| Option | Description |
| --- | --- |
| generic settings | Lists the names of all the generics in the VHDL. |
| Type | Displays the type for the generic listed in the Generic Name column. |
| Default Value | Displays the default value of the generic as the CLIP declaration XML defines it. |
| Value | Displays the value of the generic for this instantiation of the CLIP. |
| Value | Specifies an override value for the generic you select in the Generic Name column. |
| Check Syntax | Checks the current generic values to ensure that they are valid. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/initial-value-page-fpga-register-properties-dialog-box.html language=enus -->
## TOPIC 00092: Initial Value Page (FPGA Register Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/initial-value-page-fpga-register-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/initial-value-page-fpga-register-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the FPGA Register Properties dialog box, select Initial Value from the Category list to display this page. Use this page to initialize a register item. You can enter an initial value or call an initialization VI that you create. This page includes the following components: Option Description Use

### Initial Value Page (FPGA Register Properties Dialog Box)

In the [FPGA Register Properties](/csh?context=lvfpga_lvfpgadialog_fpga_register_prop_db) dialog box, select **Initial Value** from the **Category** list to display this page.

Use this page to initialize a [register item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant). You can enter an initial value or call an initialization VI that you create.

This page includes the following components:

| Option | Description |
| --- | --- |
| Use Initialization VI | Specifies whether LabVIEW uses an initialization VI that you create. The default is unchecked. Note You must use an initialization VI if you have specified Custom control as the data type for the register item. |
| VI Path | Specifies the path to the initialization VI. |
| New | Creates an instance of a template VI, saves the VI to the location you specify in the Name the New Initialization VI dialog box, and opens the VI. You must close the FPGA Register Properties dialog box to edit the VI. |
| Open VI | Opens the VI you specify in the VI Path field. You must close the FPGA Register Properties dialog box to edit the VI. |
| Run | Runs the VI you specify in the VI Path field. LabVIEW then imports the output value into the register item and displays the corresponding value in the Initial Value field. |
| Initial Value | Indicates the initial value of the register item. If you do not select an initialization VI, use this control to specify an initial value. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/initial-values-page-memory-properties-dialog-box.html language=enus -->
## TOPIC 00093: Initial Values Page (Memory Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/initial-values-page-memory-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/initial-values-page-memory-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Memory Properties dialog box, select Initial Values from the Category list to display this page. Use this page to initialize the memory item you create in the Memory Properties dialog box. You can edit data elements individually, define linear segments, use predefined functions, or call an in

### Initial Values Page (Memory Properties Dialog Box)

In the [Memory Properties](/csh?context=lvfpga_lvfpgadialog_fpga_memory_prop_db) dialog box, select **Initial Values** from the **Category** list to display this page.

Use this page to initialize the memory item you create in the **Memory Properties** dialog box. You can edit data elements individually, define linear segments, use predefined functions, or call an initialization VI you create.

This page includes the following components:

| Option | Description |
| --- | --- |
| Initialization Method | Specifies the method you want to use to initialize the memory item. Select Standard Function to populate the memory item with constants, straight lines, sine waves, or cosine waves. Select Initialization VI to populate the memory item with an array that an initialization VI creates. Standard Function—Contains the following options: Mode—Specifies the contents with which LabVIEW populates the address interval you select.You can select from the following values: Constant—Populates using the constant you specify in Value. Linear—Populates using a linear segment computed from the values you specify in Starting value and Slope. Sine—Populates using a full-scale sine wave that you specify in Number of Cycles.This option is available only for signed integers and signed fixed-point numbers. Cosine—Populates using a full-scale cosine wave that you specify in Number of Cycles.This option is available only for signed integers and signed fixed-point numbers. Start Address—Specifies the low end of the memory item interval you want to populate. End Address—Specifies the high end of the memory item interval you want to populate. Value—Specifies a value.This value is the constant LabVIEW enters in the memory item if you select Constant from the Mode pull-down menu. Starting Value—Specifies the first value LabVIEW enters in the memory item if you select Linear from the Mode pull-down menu. Parameter—Specifies the slope of the line LabVIEW enters in the memory item if you select Linear from the Mode pull-down menu. Number of Cycles—Specifies the number of cycles LabVIEW enters in the memory item if you select Sine or Cosine from the Mode pull-down menu. Apply—Displays the initial values in the Graph Preview and Data Values tabs. Clicking the Apply button does not save the initialization data. You must click the Apply button and the OK button to save the initialization data. Initialization VI—Contains the following options: VI Path—Specifies the path to the initialization VI. New—Creates an instance of a template VI, saves the VI to the location you specify in the Name the New Initialization VI dialog box, and opens the VI. You must close the Memory Properties dialog box to edit the VI. Open—Opens the VI you specify in the VI Path field. You must close the Memory Properties dialog box to edit the VI. Run—Runs the VI you specify in the VI Path field. LabVIEW then imports the output array into the memory item and displays the corresponding values in the Graph Preview and Data Values tabs. |
| Graph Preview | Displays the current contents of the memory item in a waveform graph. |
| Data Values | Displays the current contents of the memory item. |
| Reset to Default Values | Resets the contents of the memory item to the default value.For the Boolean data type, the default is 0 (FALSE). For integer data types, the default is 0. For fixed-point data types, the default is 0 if Maximum is greater than or equal to 0 and Minimum is less than or equal to 0 on the General Memory Properties page. If Maximum is less than 0, the default is equal to Maximum. If Minimum is greater than 0, the default is equal to Minimum. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/interfaces-page-fifo-properties-dialog-box.html language=enus -->
## TOPIC 00094: Interfaces Page (FIFO Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/interfaces-page-fifo-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/interfaces-page-fifo-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the FIFO Properties dialog box, select Interfaces from the Category list to display this page. Use this page to configure the arbitration options and the number of elements that the FPGA VI can read or write to the DMA FIFO in each clock cycle. This page includes the following components: Option

### Interfaces Page (FIFO Properties Dialog Box)

In the [FIFO Properties](/csh?context=lvfpga_lvfpgadialog_edit_fifo) dialog box, select **Interfaces** from the **Category** list to display this page.

Use this page to configure the arbitration options and the number of elements that the FPGA VI can read or write to the DMA FIFO in each clock cycle.

This page includes the following components:

| Option | Description |
| --- | --- |
| Arbitration for Read | Sets the type of arbitration for reading from the FIFO item. Select Arbitrate if Multiple Requestors Only or Never Arbitrate if you use the FIFO Method Node in a single-cycle Timed Loop. |
| Number of Elements per Read | Specifies the number of elements that the FPGA VI can read from the DMA FIFO each clock cycle. The default is 1. Note Support for configurable numbers of elements in FIFOs varies by target. Refer to your target hardware documentation for more information. |
| Arbitration for Write | Sets the type of arbitration for writing to the FIFO item. Select Arbitrate if Multiple Requestors Only or Never Arbitrate if you use the FIFO Method Node in a single-cycle Timed Loop. |
| Number of Elements per Write | Specifies the number of elements that the FPGA VI can write to the DMA FIFO each clock cycle. The default is 1. Note Support for configurable numbers of elements in FIFOs varies by target. Refer to your target hardware documentation for more information. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/interfaces-page-fpga-register-properties-dialog-box.html language=enus -->
## TOPIC 00095: Interfaces Page (FPGA Register Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/interfaces-page-fpga-register-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/interfaces-page-fpga-register-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the FPGA Register Properties dialog box, select Interfaces from the Category list to display this page. Use this page to configure the arbitration options for the register item. This page includes the following component: Option Description Arbitration for Write Specifies the type of arbitration

### Interfaces Page (FPGA Register Properties Dialog Box)

In the [FPGA Register Properties](/csh?context=lvfpga_lvfpgadialog_fpga_register_prop_db) dialog box, select **Interfaces** from the **Category** list to display this page.

Use this page to configure the arbitration options for the [register item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant).

This page includes the following component:

| Option | Description |
| --- | --- |
| Arbitration for Write | Specifies the type of arbitration for the Write interface of the register item. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/interfaces-page-memory-properties-dialog-box.html language=enus -->
## TOPIC 00096: Interfaces Page (Memory Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/interfaces-page-memory-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/interfaces-page-memory-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Memory Properties dialog box, select Interfaces from the Category list to display this page. Use this page to configure the arbitration options and to specify read and/or write ports for the memory item. This page includes the following components: Option Description Dual Clock Interface Spec

### Interfaces Page (Memory Properties Dialog Box)

In the [Memory Properties](/csh?context=lvfpga_lvfpgadialog_fpga_memory_prop_db) dialog box, select **Interfaces** from the **Category** list to display this page.

Use this page to configure the arbitration options and to specify read and/or write ports for the memory item.

This page includes the following components:

| Option | Description |
| --- | --- |
| Dual Clock Interface | Specifies that you can write data to the memory item in one clock domain and read from the memory item in a different clock domain. This option is available only for memory items implemented using block memory. The default is unchecked. Caution When you use memory items implemented using block memory in multiple clock domains, it is possible to read and write from the same address simultaneously. Doing so can result in reading incorrect data. |
| Interface A | Specifies the type of arbitration for reading from Interface A. Method A—Indicates the type of memory access for the interface.Interface A is always read-only. Arbitration A—Sets the type of arbitration for the memory interface. Select Arbitrate if Multiple Requestors Only or Never Arbitrate if you use the Memory Method Node configured for Interface A in a single-cycle Timed Loop. |
| Interface B | Specifies the method and type of arbitration for Interface B. Method B—Specifies the type of memory access for the interface.Interface B has write access by default. The read method for interface B is not compatible with custom data types. If you select a custom data type in the Data Type page, the Method for interface B is dim. Arbitration B—Sets the type of arbitration for the memory interface. Select Arbitrate if Multiple Requestors Only or Never Arbitrate if you use the Memory Method Node configured for Interface B in a single-cycle Timed Loop. |
| MemorySchematicDiagram | Reflects the configuration of the memory block. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/advdata-mnu.html language=enus -->
## TOPIC 00097: Data Manipulation

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/advdata-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/advdata-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Data Manipulation functions to modify data values used in LabVIEW. This palette is specific to FPGA targets and contains a subset of the VIs and functions that are on this palette when you edit a host VI. Refer to the Data Manipulation Palette Details topic for information about Timed Loop c

### Data Manipulation

Use the Data Manipulation functions to modify data values used in LabVIEW.

Note

Refer to the [Data Manipulation Palette Details](/csh?context=lvfpga_lvfpga_data_manip_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

Parent topic:

Numeric

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/analysis-mnu.html language=enus -->
## TOPIC 00098: FPGA Math & Analysis

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/analysis-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/analysis-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA Math & Analysis VIs and Functions to perform math, analysis, and control operations in FPGA VIs. This palette is specific to FPGA targets. icon

### FPGA Math & Analysis

Use the FPGA Math & Analysis VIs and Functions to perform math, analysis, and control operations in FPGA VIs.

Note

[IMAGE alt='icon' src='analysis-mnu.png']

- [Generation](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/siggen-mnu.html) Use the Generation VIs in FPGA VIs to generate signals.
- [Control](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/control-mnu.html) Use the Control VIs in FPGA VIs to create control applications for FPGA targets.
- [Utilities](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/math-utility-mnu.html) Use the Utilities VIs in FPGA VIs to perform various tasks such as detecting state changes of Boolean inputs, detecting zero crossings, delaying the input value, limiting the valid range of a signal, and performing linear interpolation.
- [High Throughput Math](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/highthroughputmath-mnu.html) Use the High Throughput Math functions to achieve high throughput rates when performing fixed-point math and analysis on FPGA targets.
- [DC and RMS Measurements](../../../../../../vi-lib/rvi/analysis/measure/dc-rms/xnode/nifpgadc-rms-xnode.html) Calculates the DC (mean) and/or RMS values of an input signal. You also can use this Express VI to calculate the intermediate sum, mean square, or square sum values in order to save FPGA resources. This Express VI accepts frames of data, performs measurement on the input data, and returns a valid single result for each frame.
- [Mean, Variance, and Standard Deviation](../../../../../../vi-lib/rvi/analysis/measure/mean-var-std/xnode/nifpgamean-var-std-xnode.html) Calculates the mean, variance, and/or standard deviation of an input signal. This Express VI analyzes discrete frames of data rather than analyzing data continuously. This Express VI waits for N cycles to collect a frame of data before returning one valid output, where N is the number of samples in each frame. It then waits for another N cycles to return another valid output.
- [Analog Period Measurement](../../../../../../vi-lib/rvi/analysis/measure/period/xnode/nifpgaanalogperiod-xnode.html) Calculates the period of an evenly sampled periodic signal using threshold crossing detection. This Express VI accepts frames of data, performs measurement on the input data, and returns a valid single result for each frame.
- [Linear Algebra](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/linearalgebra-mnu.html) Use the Linear Algebra functions to perform vector and matrix calculations in high speed and high throughput FPGA applications, such as RF applications.
- [Butterworth Filter](../../../../../../vi-lib/rvi/analysis/measure/butterworth/xnode/nifpgabutterworthfilter-xnode.html) Filters one or more input signals using a lowpass or highpass IIR Butterworth filter.
- [Notch Filter](../../../../../../vi-lib/rvi/analysis/measure/notch/xnode/nifpganotchfilter-xnode.html) Attenuates a specific frequency band in one or more input signals using a second order IIR notch filter.
- [Rational Resampler](../../../../../../vi-lib/rvi/analysis/measure/lmrsmpl/xnode/nifpga-rational-resampler-xnode.html) Provides a rational resampling filter, which updates the input sample rate by an L / M factor where L is an interpolation factor and M is a decimation factor.
- [Scaled Window](../../../../../../vi-lib/rvi/analysis/measure/window/xnode/nifpga-scaled-window-xnode.html) Minimizes spectral leakage associated with truncated waveforms. This Express VI scales the windowed time-domain signal so that when a LabVIEW object computes the power or amplitude spectrum of the windowed waveform, all windows provide the same level within the accuracy constraints of the output wavelength.
- [FFT](../../../../../../vi-lib/rvi/analysis/measure/fft/xnode/nifpgafft-xnode.html) Computes the Fast Fourier Transform (FFT). The Single Channel, Single Sample input format computes the FFT point by point. The Single Channel, Multiple Samples input format allows you to perform FFT analysis on a data stream with multiple samples/cycle.
- [NI Floating-Point Library](../../../../../../vi-lib/rvi/analysis/flplib-xnode/nifpgaflplib-xnode.html) Redirects to the LabVIEW Tools Network on ni.com where you can download a library of floating-point math operation functions. You can use these functions in your FPGA application to minimize resource usage outside single-cycle Timed Loops or to optimize timing performance inside 40 MHz single-cycle Timed Loops.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/array-mnu.html language=enus -->
## TOPIC 00099: Array

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/array-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/array-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Array functions to create and manipulate arrays. The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time. This palette is specific to FPGA targets and contains a subset of the VIs and functions that are on this palette when you edit a host V

### Array

Use the Array functions to create and manipulate arrays. The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time.

Note

Refer to the [Array Palette Details](/csh?context=lvfpga_lvfpga_array_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='array-mnu.png']

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/basicelements-mnu.html language=enus -->
## TOPIC 00100: Basic Elements

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/basicelements-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/basicelements-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Basic Elements functions to perform low-level FPGA operations such as accumulating totals, delaying signals, performing binary arithmetic, or accessing a DSP48E slice. You typically use these functions to create higher-level IP. icon

### Basic Elements

Use the Basic Elements functions to perform low-level FPGA operations such as accumulating totals, delaying signals, performing binary arithmetic, or accessing a DSP48E slice. You typically use these functions to create higher-level IP.

[IMAGE alt='icon' src='basicelements-mnu.png']

- [Discrete Delay](../../../../../../vi-lib/rvi/fxpmathlib/basic-elements/fxpdiscretedelay/xnode/nifxpmath-discretedelay-xnode.html) Delays input value for a number of loop iterations. This VI is analogous to a z^-n block where n can be constant or variable.
- [AddSub](../../../../../../vi-lib/rvi/fxpmathlib/basic-elements/fxpaddsub/xnode/nifxpmath-addsub-xnode.html) Implements an adder-subtractor that operates on bit patterns. You can cascade AddSub functions and pipeline them to achieve higher throughput rates.
- [Accumulator](../../../../../../vi-lib/rvi/fxpmathlib/basic-elements/fxpintaccumulator/xnode/nifxpmath-intaccumulator-xnode.html) Accumulates or decrements x . This function supports multi-channel operations and feedback scaling.
- [DSP48E](../../../../../../vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48emerge-vi.html) Represents a DSP48E slice on a supported FPGA target. You can use this function on the following FPGA targets: Virtex-5, Virtex-6, Kintex-7, and Zynq.
- [DSP48E1](../../../../../../vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48e1merge-vi.html) Represents a DSP48E1 slice on a supported FPGA target. You can use this function on the following FPGA targets: Virtex-6, Kintex-7, and Zynq.

Parent topic:

High Throughput Math

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/boolfunc-mnu.html language=enus -->
## TOPIC 00101: Boolean

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/boolfunc-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/boolfunc-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Boolean functions to perform logical operations on single Boolean values or arrays of Boolean values. When you use the Boolean to Array function in an FPGA VI, the function converts fixed-size arrays to use the smallest unsigned representation that will fit the array size. When you use the B

### Boolean

Use the Boolean functions to perform logical operations on single Boolean values or arrays of Boolean values.

When you use the Boolean to Array function in an FPGA VI, the function converts fixed-size arrays to use the smallest unsigned representation that will fit the array size. When you use the Boolean to Array function in a host VI, the function converts a Boolean array to a 32-bit unsigned integer.

Note

Refer to the [Boolean Palette Details](/csh?context=lvfpga_lvfpga_boolean_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='boolfunc-mnu.png']

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/cluster-mnu.html language=enus -->
## TOPIC 00102: Cluster & Class

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/cluster-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/cluster-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Cluster & Class functions to create and manipulate clusters. This palette is specific to FPGA targets and contains a subset of the VIs and functions that are on this palette when you edit a host VI. Refer to the Cluster & Class Palette Details topic for information about Timed Loop compatibi

### Cluster & Class

Use the Cluster & Class functions to create and manipulate clusters.

Note

Refer to the [Cluster & Class Palette Details](/csh?context=lvfpga_lvfpga_cluster_variant) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='cluster-mnu.png']

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/communicationprotocols-mnu.html language=enus -->
## TOPIC 00103: Communication Protocols

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/communicationprotocols-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/communicationprotocols-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at ni.com/labview-tools-network. Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communica

### Communication Protocols

Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at [ni.com/labview-tools-network](https://www.ni.com/r/exqsb9). Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communication protocols, such as Inter-Integrated Circuit (I2C) and Serial Peripheral Interface (SPI).

To access IP using the Communication Protocols functions, you must have the JKI VI Package Manager (VIPM) software installed. When you click a Communication Protocols function, LabVIEW automatically detects whether the VIPM software is installed and proceeds with the following operations:

- If the VIPM software is installed, LabVIEW launches a VIPM software dialog box that displays detailed information about the corresponding IP. You can use this dialog box to install and uninstall the IP.
- If the VIPM software is not installed, LabVIEW launches the NI LabVIEW VIPM Helper dialog box that prompts you to install the VIPM software. After the installation is complete, LabVIEW launches the VIPM software dialog box that you can use to install and uninstall the IP.

[IMAGE alt='icon' src='communicationprotocols-mnu.png']

#### Related Information

[Accessing LabVIEW Add-ons with the VI Package Manager (VIPM) Software (Windows)](/csh?productcategories=147794&context=lvcore_lvhelp_vipm)

- [Communication Protocols Functions](../../../../../../vi-lib/rvi/communicationprotocols/spi-xnode/nifpgaspi-xnode.html) Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at ni.com/labview-tools-network . Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communication protocols, such as Inter-Integrated Circuit (I2C) and Serial Peripheral Interface (SPI).
- [Communication Protocols Functions](../../../../../../vi-lib/rvi/communicationprotocols/i2c-xnode/nifpgai2c-xnode.html) Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at ni.com/labview-tools-network . Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communication protocols, such as Inter-Integrated Circuit (I2C) and Serial Peripheral Interface (SPI).

Parent topic:

FPGA I/O

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/compare-mnu.html language=enus -->
## TOPIC 00104: Comparison

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/compare-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/compare-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Comparison functions to compare Boolean values, numeric values, arrays, and clusters. This palette is specific to FPGA targets and contains a subset of the VIs and functions that are on this palette when you edit a host VI. The Comparison functions treat Boolean, numeric, array, and cluster

### Comparison

Use the Comparison functions to compare Boolean values, numeric values, arrays, and clusters.

Note

The Comparison functions treat [Boolean](/csh?productcategories=147794&context=lvcore_lvhowto_boolean_comparison), [numeric](/csh?productcategories=147794&context=lvcore_lvhowto_numeric_comparison), [array](/csh?productcategories=147794&context=lvcore_lvhowto_array_comparison), and [cluster](/csh?productcategories=147794&context=lvcore_lvhowto_cluster_comparison) values differently. You can [change the comparison mode](/csh?productcategories=147794&context=lvcore_lvhowto_setting_compare_functions) of some Comparison functions.

Refer to the [Comparison Palette Details](/csh?context=lvfpga_lvfpga_comparison_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='compare-mnu.png']

- [Assert Type](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/compare/typeassert-mnu.html) Use the Assert Type nodes for the following purposes:

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/compare/typeassert-mnu.html language=enus -->
## TOPIC 00105: Assert Type

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/compare/typeassert-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/compare/typeassert-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Assert Type nodes for the following purposes: Customizing sections of code in a malleable VI (.vim) for specific data typesForcing a malleable VI to accept only data types that meet certain requirementsForcing a malleable VI to decline specific data types This palette is specific to FPGA tar

### Assert Type

Use the Assert Type nodes for the following purposes:

- Customizing sections of code in a malleable VI ( .vim ) for specific data types
- Forcing a malleable VI to accept only data types that meet certain requirements
- Forcing a malleable VI to decline specific data types

Note

Refer to the [Assert Type Palette Details](/csh?context=lvfpga_lvfpga_assert_type_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='typeassert-mnu.png']

Parent topic:

Comparison

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/control-mnu.html language=enus -->
## TOPIC 00106: Control

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/control-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Control VIs in FPGA VIs to create control applications for FPGA targets. This palette is specific to FPGA targets. icon

### Control

Use the Control VIs in FPGA VIs to create control applications for FPGA targets.

Note

[IMAGE alt='icon' src='control-mnu.png']

- [PID](../../../../../../vi-lib/rvi/analysis/control/pid/nifpgapid-wrapper-vi.html) Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.
- [Matrix*Vector](../../../../../../vi-lib/rvi/analysis/control/matrixvector/nifpga-matrix-vector-product-vi.html) Multiplies Matrix A by an input Vector b . This operation is useful for FPGA control applications, such as state-feedback control. You can use more than one multiplier to reduce the latency of this operation.
- [3-Phase PLL](../../../../../../vi-lib/rvi/analysis/control/3phasepll/nifpga-3phasepll-vi.html) Tracks the phase and frequency of a three-phase signal. This operation is useful for FPGA control applications of a three-phase system. The output phase of the 3-Phase Phase-Locked Loop is in pi radians.
- [Discrete Nonlinear Systems](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/nonlinear-mnu.html) Use the Discrete Nonlinear Systems VIs to model nonlinear systems on FPGA targets.
- [Discrete Linear Systems](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/discretelinear-mnu.html) Use the Discrete Linear Systems VIs to control or model discrete linear systems on FPGA targets.

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/dir-mnu.html language=enus -->
## TOPIC 00107: Programming

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/dir-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the LabVIEW FPGA Module VIs and functions to build VIs that run on FPGA targets, such as NI Reconfigurable I/O (RIO) devices, and VIs to communicate with FPGA targets. You must add an FPGA target to a LabVIEW project to access the FPGA Module palettes, VIs, functions, and development tools. When

### Programming

Use the LabVIEW FPGA Module VIs and functions to build VIs that run on FPGA targets, such as NI Reconfigurable I/O (RIO) devices, and VIs to communicate with FPGA targets.

You must [add an FPGA target](/csh?context=lvfpga_lvfpgahelp_adding_an_fpga_target) to a [LabVIEW project](/csh?productcategories=147794&context=lvcore_lvconcepts_using_labview_projects) to access the FPGA Module palettes, VIs, functions, and development tools. When you develop an FPGA VI, you have access only to the LabVIEW VIs and functions that are compatible with the FPGA target. In addition to the subset of the standard LabVIEW VIs and functions, the FPGA Module provides FPGA target-specific VIs and functions.

When you build [host VIs](/csh?context=lvfpga_lvfpgaconcepts_pfi_comm), you can access the [FPGA Interface](../../../../../../menus/categories/fpga/dir-mnu.html) functions.

The VIs and functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes), specific [FPGA Module error codes](/csh?context=lvfpga_lvfpgahelp_fpga_error_codes), or error codes specific to the FPGA target.

[IMAGE alt='icon' src='dir-mnu.png']

- [Structures](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/structs-mnu.html) Use the structures to control data flow.
- [Array](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/array-mnu.html) Use the Array functions to create and manipulate arrays. The LabVIEW FPGA Module supports only one-dimensional arrays that resolve to a single size at compile time.
- [Cluster & Class](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/cluster-mnu.html) Use the Cluster & Class functions to create and manipulate clusters.
- [Numeric](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/numeric-mnu.html) Use the Numeric functions to create and perform arithmetic operations on numbers and to convert numbers from one numeric data type to another.
- [Boolean](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/boolfunc-mnu.html) Use the Boolean functions to perform logical operations on single Boolean values or arrays of Boolean values.
- [Comparison](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/compare-mnu.html) Use the Comparison functions to compare Boolean values, numeric values, arrays, and clusters.
- [Timing](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/timing-mnu.html) Use the Timing VIs to control the execution timing of FPGA operations.
- [FPGA I/O](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/fpgaio-mnu.html) Use the FPGA I/O functions to perform operations on FPGA targets.
- [Data Storage & Transfer](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/memory-mnu.html) Use the functions on this palette to access memory or transfer data.
- [Synchronization](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/synch-mnu.html) Use the Synchronization functions to synchronize tasks executing in parallel and pass data between parallel tasks.
- [Channel Wire Endpoints](../../../../../../resource/channels/channel-wire-endpoint-fpga.html)
- [FPGA Math & Analysis](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/analysis-mnu.html) Use the FPGA Math & Analysis VIs and Functions to perform math, analysis, and control operations in FPGA VIs.
- [FPGA VI and Function Details (FPGA Module)](../../../../../../functions/fpga-vi-and-function-details.html)
- [FPGA Target Methods & Properties Nodes](../../../../../../vi-lib/rvi/eio/fpganode/fpga-target-methods-properties-nodes.html)
- [IP Integration Node](../../../../../../vi-lib/rvi/ipintegrationnode/ipinode-xnode/nifpgaipinode-xnode.html) Integrates third-party IP into a LabVIEW FPGA VI. Before you add this node to a block diagram, ensure the necessary Xilinx compilation tools are installed on the development computer. You can place this node only inside a single-cycle Timed Loop .
- [Xilinx IP Functions](../../../../../../menus/fpgacategories/programming/xilinx-ip-functions.html)

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/discretelinear-mnu.html language=enus -->
## TOPIC 00108: Discrete Linear Systems

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/discretelinear-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/discretelinear-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Discrete Linear Systems VIs to control or model discrete linear systems on FPGA targets. This palette is specific to FPGA targets. icon

### Discrete Linear Systems

Use the Discrete Linear Systems VIs to control or model discrete linear systems on FPGA targets.

Note

[IMAGE alt='icon' src='discretelinear-mnu.png']

- [Discrete Normalized Integrator](../../../../../../vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-normalized-integrator-m-vi.html) Integrates a discrete input signal using forward Euler integration. The VI assumes that the integration interval (dt) is normalized to 1. The data type you wire to input determines output data type, where output word length is equal to input word length + 16 bits.
- [Unit Delay](../../../../../../vi-lib/rvi/analysis/basicops/templates/nifpga-unit-delay-m-vi.html) Delays the input value for one cycle. The data type you wire to input determines the output data type.
- [Basic Discrete Delay](../../../../../../vi-lib/express/rvi/analysis/control/discrete-linear/nifpga-discrete-delay-vi.html) Delays the input value for the number of loop iterations you specify in the Configure Basic Discrete Delay dialog box.
- [Zero-Order Hold](../../../../../../vi-lib/rvi/analysis/control/linear/templates/nifpga-zero-order-hold-m-vi.html) Samples an input signal and holds it for a specified number of calls to the VI. The data type you wire to input determines the output data type.
- [Initial Condition](../../../../../../vi-lib/rvi/analysis/control/linear/templates/nifpga-initial-condition-m-vi.html) Produces a predefined initial condition immediately after the first time you call or initialize the VI. The data type you wire to input determines the output data type.
- [Discrete Transfer Function Direct](../../../../../../vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-transfer-function-direct-vi.html) Implements a fixed-point transfer function system model on an FPGA. Obtain this model by using the Discrete FP Transfer Function to FXP VI.
- [Discrete Control Filter](../../../../../../vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-control-filter-m-vi.html) Applies a fifth-order low-pass integer FIR filter to the input data. The filter cut-off frequency is 1/10 of the sample frequency of the input . Use the Discrete Control Filter VI to filter measured values, such as the process variable, in control applications. The data type you wire to input determines the output data type.

Parent topic:

Control

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/fpgafifo-mnu.html language=enus -->
## TOPIC 00109: FIFO

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/fpgafifo-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/fpgafifo-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FIFO Method Node with the Read and Write methods to transfer data from one loop to another using FIFOs in an FPGA VI, such as among single-cycle Timed Loops. You also can use the Write method to transfer data to host VIs using a DMA FIFO. This palette is specific to FPGA targets and contains

### FIFO

Use the FIFO Method Node with the Read and Write methods to transfer data from one loop to another using [FIFOs](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data) in an FPGA VI, such as among [single-cycle Timed Loops](/csh?context=lvfpga_lvfpga_fpga_timed_loop). You also can use the Write method to transfer data to host VIs using a [DMA FIFO](/csh?context=lvfpga_lvfpgaconcepts_fpga_dma_communication).

Note

The VIs and functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes), specific [FPGA Module error codes](/csh?context=lvfpga_lvfpgahelp_fpga_error_codes), or error codes specific to the FPGA target.

[IMAGE alt='icon' src='fpgafifo-mnu.png']

- [VI-Defined FIFO Configuration](../../../../../../vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-fifo-vi.html) Represents a VI-defined FIFO. Right-click the node and select Configure to configure the VI-defined FIFO.
- [FIFO Method Node](../../../../../../vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-vi.html) Invokes a FIFO method on an FPGA VI. You must specify a FIFO before specifying a method. The available methods vary depending on the FPGA target and the type of FIFO.
- [FIFO Constant](../../../../../../vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-fifonameconstant-vi.html) Use the FIFO constant to specify a FIFO item on the block diagram.

Parent topic:

Synchronization

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/fpgahsio-mnu.html language=enus -->
## TOPIC 00110: User-Controlled I/O Sampling

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/fpgahsio-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/fpgahsio-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the User-Controlled I/O Sampling functions to perform I/O with more specific control over the I/O hardware than you have with the FPGA I/O functions. Not all targets support the User-Controlled I/O Sampling functions. Refer to the specific FPGA target hardware documentation for information about

### User-Controlled I/O Sampling

Use the User-Controlled I/O Sampling functions to perform I/O with more specific control over the I/O hardware than you have with the FPGA I/O functions.

Note

hardware documentation

Unlike the [FPGA I/O](fpgaio-mnu.html) functions, you can use the User-Controlled I/O Sampling functions to create [pipeline operations](/csh?context=lvfpga_lvfpgaconcepts_fpga_pipelining). Pipelining allows you to achieve higher-speed I/O than generally possible using FPGA I/O functions.

To use these nodes you must create several loops. One loop controls the timing of the acquisition. A second loop reads and/or writes the data. A third loop checks the status of the acquisition or generation.

[IMAGE alt='icon' src='fpgahsio-mnu.png']

- [Read I/O](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/readiomerge-vi.html) Reads the I/O data from the I/O items. This function waits for new I/O data to become available through the Generate I/O Sample Pulse Method function.
- [Configure I/O](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/configureiomerge-vi.html) Writes channel configuration data to the I/O items. Use this node with multiplexed analog input devices where the configuration for a channel transfers from the FPGA to the target I/O on each clock pulse. If the channel configuration does not update with each sample pulse, the previously written configuration transfers again, and the device will continue to acquire from the same channel with the same configuration.
- [Write I/O](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/writeiomerge-vi.html) Writes new output data to the I/O items as soon as the target is ready to receive new data. This function does not overwrite previously written data.
- [Generate I/O Sample Pulse](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/generateiosamplepulsemerge-vi.html) Initiates a pulse on the sample clock terminal of the I/O items.
- [Get I/O Read Status](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioreadstatusmerge-vi.html) Reports the status of reading I/O data from the I/O items.
- [Get I/O Configuration Status](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioconfigurationstatusmerge-vi.html) Reports the status of writing channel configuration data to I/O items.
- [Get I/O Write Status](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/getiowritestatusmerge-vi.html) Reports the status of written output from the I/O items.
- [Reset I/O](../../../../../../vi-lib/eio/eiogrowablemethodnode/fixedmethods/resetiomerge-vi.html) Resets the state, clears the data path, and clears any error conditions for the I/O items. This node also resets any pipeline stages and counters for the I/O item.

Parent topic:

FPGA I/O

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/fpgaio-mnu.html language=enus -->
## TOPIC 00111: FPGA I/O

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/fpgaio-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/fpgaio-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA I/O functions to perform operations on FPGA targets. This palette is specific to FPGA targets. The VIs and functions on this palette can return general LabVIEW error codes, specific FPGA Module error codes, or error codes specific to the FPGA target. icon

### FPGA I/O

Use the FPGA I/O functions to perform operations on FPGA targets.

Note

The VIs and functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes), specific [FPGA Module error codes](/csh?context=lvfpga_lvfpgahelp_fpga_error_codes), or error codes specific to the FPGA target.

[IMAGE alt='icon' src='fpgaio-mnu.png']

- [FPGA I/O Node](../../../../../../vi-lib/eio/eionode/eionode-xnode.html) Performs specific FPGA I/O operations on FPGA targets. You can configure the FPGA I/O Node with one or more FPGA I/O items.
- [FPGA I/O Constant](../../../../../../vi-lib/rvi/eio/api/nifpga-palettemergevi-ionameconstant-vi.html) Use the FPGA I/O constant to specify an FPGA I/O item on the block diagram.
- [Communication Protocols](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/communicationprotocols-mnu.html) Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at ni.com/labview-tools-network . Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communication protocols, such as Inter-Integrated Circuit (I2C) and Serial Peripheral Interface (SPI).
- [FPGA I/O Method Node](../../../../../../vi-lib/eio/eiomethodnode/eiomethodnode-xnode.html) Invokes a method on an I/O item or hardware under an FPGA target in the Project Explorer window, such as a C Series module. In some cases, you also can invoke methods on the FPGA target itself. The methods available depend on the FPGA target and the FPGA I/O item or C Series module you select.
- [FPGA I/O Property Node](../../../../../../vi-lib/eio/eiopropertynode/eiopropertynode-xnode.html) Gets or sets one or more properties on an I/O item or hardware under an FPGA target in the Project Explorer window, such as a C Series module. In some cases, you also can set and retrieve properties on the FPGA target itself. The properties available vary by the FPGA target or the C Series module and the I/O resource.
- [User-Controlled I/O Sampling](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/fpgahsio-mnu.html) Use the User-Controlled I/O Sampling functions to perform I/O with more specific control over the I/O hardware than you have with the FPGA I/O functions.
- [cRIO I/O Device](../../../../../../targets/ni/fpga/rio/compactrio/vi-lib/criorefnumtag-vi.html) Use the cRIO I/O Device to specify a cRIO I/O item on the block diagram.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/highthroughputmath-mnu.html language=enus -->
## TOPIC 00112: High Throughput Math

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/highthroughputmath-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/highthroughputmath-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the High Throughput Math functions to achieve high throughput rates when performing fixed-point math and analysis on FPGA targets. The High Throughput Math functions do not support real-time (RT) targets. To perform fixed-point math and analysis on RT targets, use the Numeric functions. icon

### High Throughput Math

Use the High Throughput Math functions to achieve high throughput rates when performing fixed-point math and analysis on FPGA targets.

Note

Numeric

[IMAGE alt='icon' src='highthroughputmath-mnu.png']

- [High Throughput Add](../../../../../../vi-lib/rvi/fxpmathlib/fxpadd/xnode/nifxpmath-add-xnode.html) Computes the sum of x and y .
- [High Throughput Subtract](../../../../../../vi-lib/rvi/fxpmathlib/fxpsub/xnode/nifxpmath-sub-xnode.html) Computes the difference between x and y .
- [High Throughput Multiply](../../../../../../vi-lib/rvi/fxpmathlib/fxpmul/xnode/nifxpmath-multiplier-xnode.html) Computes the product of x and y .
- [High Throughput Complex Multiply](../../../../../../vi-lib/rvi/fxpmathlib/fxpmultcomplex/xnode/nifpgamultcomplex-xnode.html) Computes the product of two complex numbers.
- [High Throughput Divide](../../../../../../vi-lib/rvi/fxpmathlib/fxpdiv/xnode/nifxpmath-div-xnode.html) Computes the quotient of x and y . This function rounds the result by truncating the value of the x/y output terminal towards 0.
- [High Throughput Reciprocal](../../../../../../vi-lib/rvi/fxpmathlib/fxpreciprocal/xnode/nifxpmath-reciprocal-xnode.html) Computes 1/ x . This function rounds the result by truncating the value of the 1/x output terminal towards 0.
- [High Throughput Square Root](../../../../../../vi-lib/rvi/fxpmathlib/fxpsqrt/xnode/nifxpmath-sqrt-xnode.html) Computes the square root of x . The encoding of x must be unsigned.
- [High Throughput To Fixed-Point](../../../../../../vi-lib/rvi/fxpmathlib/fxpconvert/xnode/nifxpmath-convert-xnode.html) Modifies the fixed-point configuration of x .
- [High Throughput Rectangular To Polar](../../../../../../vi-lib/rvi/fxpmathlib/fxprecttopolar/xnode/nifxpmath-recttopolar-xnode.html) Converts rectangular coordinates to polar coordinates.
- [High Throughput Polar To Rectangular](../../../../../../vi-lib/rvi/fxpmathlib/fxppolartorect/xnode/nifxpmath-polartorect-xnode.html) Converts polar coordinates to rectangular coordinates.
- [High Throughput Sine & Cosine](../../../../../../vi-lib/rvi/fxpmathlib/fxpsinandcos/xnode/nifxpmath-sinandcos-xnode.html) Computes the sine and cosine of x . This function assumes that x is in pi radians.
- [High Throughput Inverse Tangent (2 Input)](../../../../../../vi-lib/rvi/fxpmathlib/fxpatan2/xnode/nifxpmath-atan2-xnode.html) Computes the arctangent of y / x in pi radians.
- [High Throughput Exponential](../../../../../../vi-lib/rvi/fxpmathlib/fxpexp/xnode/nifxpmath-exp-xnode.html) Computes e raised to the power of x . The value of x must be in the range [–1, 1).
- [High Throughput Natural Logarithm](../../../../../../vi-lib/rvi/fxpmathlib/fxpln/xnode/nifxpmath-naturallogarithm-xnode.html) Computes the natural logarithm of x . The value of x must be in the range [1/e, 1), the encoding must be unsigned, and the integer word length must be 0 bits.
- [High Throughput Hyperbolic Sine & Cosine](../../../../../../vi-lib/rvi/fxpmathlib/fxpsinhandcosh/xnode/nifxpmath-sinhandcosh-xnode.html) Computes the hyperbolic sine and cosine of x . The value of x must be in the range [–1, 1).
- [Basic Elements](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/basicelements-mnu.html) Use the Basic Elements functions to perform low-level FPGA operations such as accumulating totals, delaying signals, performing binary arithmetic, or accessing a DSP48E slice. You typically use these functions to create higher-level IP.

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/linearalgebra-mnu.html language=enus -->
## TOPIC 00113: Linear Algebra

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/linearalgebra-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/linearalgebra-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Linear Algebra functions to perform vector and matrix calculations in high speed and high throughput FPGA applications, such as RF applications. The Linear Algebra functions do not support NI real-time (RT) targets. icon

### Linear Algebra

Use the Linear Algebra functions to perform vector and matrix calculations in high speed and high throughput FPGA applications, such as RF applications.

Note

[IMAGE alt='icon' src='linearalgebra-mnu.png']

- [Matrix Transpose](../../../../../../vi-lib/rvi/linearalgebra/matrixtranspose/xnode/nifxpla-matrixtranspose-xnode.html) Transposes a complex matrix.
- [Dot Product](../../../../../../vi-lib/rvi/linearalgebra/dotproduct/xnode/nifxpla-dotproduct-xnode.html) Computes the dot product of two complex vectors.
- [Norm Square](../../../../../../vi-lib/rvi/linearalgebra/normsquare/xnode/nifxpla-normsquare-xnode.html) Computes the norm square of a complex vector.
- [Matrix Multiply](../../../../../../vi-lib/rvi/linearalgebra/matrixmultiply/xnode/nifxpla-matrixmultiply-xnode.html) Computes the multiplication of two complex matrices.

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/math-utility-mnu.html language=enus -->
## TOPIC 00114: Utilities

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/math-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/math-utility-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Utilities VIs in FPGA VIs to perform various tasks such as detecting state changes of Boolean inputs, detecting zero crossings, delaying the input value, limiting the valid range of a signal, and performing linear interpolation. This palette is specific to FPGA targets. icon

### Utilities

Use the Utilities VIs in FPGA VIs to perform various tasks such as detecting state changes of Boolean inputs, detecting zero crossings, delaying the input value, limiting the valid range of a signal, and performing linear interpolation.

Note

[IMAGE alt='icon' src='math-utility-mnu.png']

- [Look-Up Table 1D](../../../../../../vi-lib/express/rvi/analysis/signal-generation/look-up-table-1d/nifpga-look-up-table-1d-vi.html) Provides a general-purpose block of initialized memory. Use look-up tables to store waveforms for signal generation, to model nonlinear systems, and for arithmetic computations. If you use the Look-Up Table 1D Express VI in a single-cycle Timed Loop , wire the outputs directly to Feedback Nodes . The Look-Up Table 1D Express VI takes an entire clock cycle to execute in a single-cycle Timed Loop.
- [Linear Interpolation](../../../../../../vi-lib/rvi/analysis/basicops/templates/nifpga-linear-interpolation-m-vi.html) Performs linear interpolation to approximate a function evaluation at an arbitrary location in an interval between two known points. The data type you wire to y0 determines the output y data type.
- [Zero Crossing](../../../../../../vi-lib/rvi/analysis/basicops/templates/nifpga-zero-crossing-m-vi.html) Detects zero crossings of an input signal. The data type you wire to input determines the output data type.
- [Boolean Crossing](../../../../../../vi-lib/express/rvi/analysis/control/nonlinear/nifpga-boolean-crossing-vi.html) Detects state changes of Boolean input points. You can choose from three detectors: either, false-true, or true-false.

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/memory-mnu.html language=enus -->
## TOPIC 00115: Data Storage & Transfer

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/memory-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/memory-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the functions on this palette to access memory or transfer data. This palette is specific to FPGA targets. The VIs and functions on this palette can return general LabVIEW error codes, specific FPGA Module error codes, or error codes specific to the FPGA target. icon

### Data Storage & Transfer

Use the functions on this palette to access memory or transfer data.

Note

The VIs and functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes), specific [FPGA Module error codes](/csh?context=lvfpga_lvfpgahelp_fpga_error_codes), or error codes specific to the FPGA target.

[IMAGE alt='icon' src='memory-mnu.png']

- [VI-Defined Register Configuration](../../../../../../vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-register-vi.html) Represents a VI-defined register item . Right-click the node and select Configure to configure the VI-defined register item.
- [Register Method Node](../../../../../../vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettemethodnodemergevi-vi.html) Invokes a method on a register item on the FPGA.
- [Register Constant](../../../../../../vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettenameconstantmergevi-vi.html) Use the Register constant to specify a register item on the block diagram.
- [VI-Defined Memory Configuration](../../../../../../vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-memory-vi.html) Represents a VI-defined memory item. Right-click the node and select Configure to configure the VI-defined memory item.
- [Memory Method Node](../../../../../../vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevi-vi.html) Invokes a method on a memory block on the FPGA. The methods available depend on the type of memory you configure.
- [Memory Constant](../../../../../../vi-lib/rvi/memory/memory-common/nirvimemorypalettemergevimemorynameconstant-vi.html) Use the Memory constant to specify a memory item on the block diagram.
- [VI-Defined FIFO Configuration](../../../../../../vi-lib/rvi/localresourcemanager/lrm-api/nirvilrmpalette-mergevi-fifo-vi.html) Represents a VI-defined FIFO. Right-click the node and select Configure to configure the VI-defined FIFO.
- [FIFO Method Node](../../../../../../vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-vi.html) Invokes a FIFO method on an FPGA VI. You must specify a FIFO before specifying a method. The available methods vary depending on the FPGA target and the type of FIFO.
- [FIFO Constant](../../../../../../vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-fifonameconstant-vi.html) Use the FIFO constant to specify a FIFO item on the block diagram.
- [VI-Defined Handshake Configuration](../../../../../../vi-lib/rvi/localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-handshake-vi.html) Represents a VI-defined handshake item . Right-click the node and select Configure to configure the VI-defined handshake item. Use VI-defined handshake items to create reentrant subVIs and avoid resource conflicts.
- [Handshake Method Node](../../../../../../vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettemethodnodemergevi-vi.html) Invokes a handshake method on an FPGA VI.
- [Handshake Constant](../../../../../../vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettenameconstantmergevi-vi.html) Use the Handshake constant to specify a handshake item on the block diagram.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/nonlinear-mnu.html language=enus -->
## TOPIC 00116: Discrete Nonlinear Systems

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/nonlinear-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/nonlinear-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Discrete Nonlinear Systems VIs to model nonlinear systems on FPGA targets. This palette is specific to FPGA targets. icon

### Discrete Nonlinear Systems

Use the Discrete Nonlinear Systems VIs to model nonlinear systems on FPGA targets.

Note

[IMAGE alt='icon' src='nonlinear-mnu.png']

- [Backlash](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-backlash-m-vi.html) Implements a backlash or deadband function. output does not change until input differs from the previous output by at least half of deadband . The data type you wire to input determines the output data type.
- [Friction](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-friction-m-vi.html) Implements a discontinuity at zero with linear behavior elsewhere. The data type you wire to input determines the output data type.
- [Quantizer](../../../../../../vi-lib/express/rvi/analysis/control/nonlinear/nifpga-quantizer-vi.html) Quantizes an integer input signal using fixed-point rounding.
- [Dead Zone](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-dead-zone-m-vi.html) Provides a region of zero output, or a dead zone. output is zero if start of dead zone <= input <= end of dead zone . The data type you wire to input determines the output data type.
- [Rate Limiter](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-rate-limiter-m-vi.html) Specifies a maximum rate of change of a signal. The data type you wire to input determines the output data type.
- [Relay](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-relay-m-vi.html) Switches between the output when on and output when off inputs. When the relay is on, it remains on until input is less than switch off point . When the relay is off, it remains off until input is greater than switch on point . The relay is off by default. The data type you wire to input determines the output data type.
- [Saturation](../../../../../../vi-lib/express/rvi/analysis/control/nonlinear/nifpga-saturate-vi.html) Limits the valid range of a signal to that specified by Upper limit and Lower limit . You can configure the VI to specify the integer or bit limits and signed or unsigned inputs.
- [Switch](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-switch-m-vi.html) Switches between two input values based on the value of control input . The data type you wire to input 1 or input 2 determines the output data type.
- [Boolean Crossing](../../../../../../vi-lib/express/rvi/analysis/control/nonlinear/nifpga-boolean-crossing-vi.html) Detects state changes of Boolean input points. You can choose from three detectors: either, false-true, or true-false.
- [Zero Crossing](../../../../../../vi-lib/rvi/analysis/basicops/templates/nifpga-zero-crossing-m-vi.html) Detects zero crossings of an input signal. The data type you wire to input determines the output data type.
- [Memory Element](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-memory-element-m-vi.html) Stores the input value and returns it on the next call. The data type you wire to input determines the output data type.
- [Trigger](../../../../../../vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-trigger-m-vi.html) Detects changes of the input signal during a control or simulation process. The data type you wire to trigger signal determines the triggered data type.

Parent topic:

Control

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/numeric-mnu.html language=enus -->
## TOPIC 00117: Numeric

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/numeric-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/numeric-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Numeric functions to create and perform arithmetic operations on numbers and to convert numbers from one numeric data type to another. You also can access the following constants from this palette: positive infinity negative infinity This palette is specific to FPGA targets and contains a su

### Numeric

Use the Numeric functions to create and perform arithmetic operations on numbers and to convert numbers from one numeric data type to another.

You also can access the following constants from this palette:

- positive infinity
- negative infinity

Note

Refer to the [Numeric Palette Details](/csh?context=lvfpga_lvfpga_numeric_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='numeric-mnu.png']

- [Conversion](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/numeric/convert-mnu.html) Use the Conversion functions to convert data types. The FPGA Module does not support double- or extended-precision floating-point conversions.
- [Data Manipulation](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/advdata-mnu.html) Use the Data Manipulation functions to modify data values used in LabVIEW.
- [Fixed-Point](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/numeric/fxp-mnu.html) Use the Fixed-Point functions to manipulate the overflow status and shift the bit pattern of a fixed-point number.
- [SGL Numeric Constant VI](../../../../../../vi-lib/dlg-ctls-llb/sgl-numeric-constant.html)
- [Math & Scientific Constants](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/numeric/constant-mnu.html) Use the Math & Scientific Constants to create LabVIEW applications.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/numeric/constant-mnu.html language=enus -->
## TOPIC 00118: Math & Scientific Constants

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/numeric/constant-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/numeric/constant-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Math & Scientific Constants to create LabVIEW applications. icon

### Math & Scientific Constants

Use the Math & Scientific Constants to create LabVIEW applications.

[IMAGE alt='icon' src='constant-mnu.png']

Parent topic:

Numeric

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/numeric/convert-mnu.html language=enus -->
## TOPIC 00119: Conversion

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/numeric/convert-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/numeric/convert-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Conversion functions to convert data types. The FPGA Module does not support double- or extended-precision floating-point conversions. This palette is specific to FPGA targets and contains a subset of the VIs and functions that are on this palette when you edit a host VI. When these function

### Conversion

Use the Conversion functions to convert data types. The FPGA Module does not support double- or extended-precision floating-point conversions.

Note

When these functions convert an integer to a smaller integer, they copy the least-significant bits without checking for overflow. When they convert an integer to a larger integer, they extend the sign of a signed integer and pad an unsigned integer with zeros.

Use caution when converting numbers to smaller representations, particularly when converting integers, because the LabVIEW conversion routines do not check for overflow.

Refer to the [Conversion Palette Details](/csh?context=lvfpga_lvfpga_conversion_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='convert-mnu.png']

Parent topic:

Numeric

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/numeric/fxp-mnu.html language=enus -->
## TOPIC 00120: Fixed-Point

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/numeric/fxp-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/numeric/fxp-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Fixed-Point functions to manipulate the overflow status and shift the bit pattern of a fixed-point number. This palette is specific to FPGA targets and contains functions that are on this palette when you edit an FPGA VI. The functions on this palette can return general LabVIEW error codes.

### Fixed-Point

Use the Fixed-Point functions to manipulate the overflow status and shift the bit pattern of a fixed-point number.

Note

The functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes).

Refer to the [Fixed-Point Palette Details](/csh?context=lvfpga_lvfpga_fixed_point_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='fxp-mnu.png']

- [Reinterpret Number](../../../../../../../vi-lib/rvi/fxpmathlib/fxpinterpret/xnode/nifxpmath-interpret-xnode.html) Shifts the decimal point of the bit pattern of x and returns y , where y has the same bit pattern as x but a different fixed-point configuration and value. This shift represents a hardware-efficient way to multiply or divide x by 2^ n .

Parent topic:

Numeric

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/occur-mnu.html language=enus -->
## TOPIC 00121: Occurrences

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/occur-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/occur-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Occurrences functions to control separate, synchronous activities. In particular, use these functions when you want one part of a block diagram to wait until another part of a block diagram finishes a task without forcing LabVIEW to poll. This palette is specific to FPGA targets and includes

### Occurrences

Use the Occurrences functions to control separate, synchronous activities. In particular, use these functions when you want one part of a block diagram to wait until another part of a block diagram finishes a task without forcing LabVIEW to poll.

Note

You can perform functionality similar to the occurrences functions using global variables, with one loop polling the global variable until its value changes. However, global variables consume more system resources and can introduce jitter because of the polling loop.

[IMAGE alt='icon' src='occur-mnu.png']

- [Wait on Occurrence with Timeout in Ticks](../../../../../../vi-lib/rvi/occurrence/nirviwaitonoccurrence-vi.html) Waits for the Set Occurrence function to set or trigger the given occurrence .

Parent topic:

Synchronization

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/siggen-mnu.html language=enus -->
## TOPIC 00122: Generation

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/siggen-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/siggen-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Generation VIs in FPGA VIs to generate signals. This palette is specific to FPGA targets. icon

### Generation

Use the Generation VIs in FPGA VIs to generate signals.

Note

[IMAGE alt='icon' src='siggen-mnu.png']

- [Sine Wave Generator](../../../../../../vi-lib/rvi/analysis/siggen/sinewave/nifpga-sine-wave-generator-vi.html) Generates a point-by-point sine wave using direct digital synthesis. The synthesis runs continuously from the top-level FPGA target clock to produce an accurate real-time frequency. Each execution of this VI returns the most recent sample produced by the underlying synthesis engine.
- [Square Wave Generator](../../../../../../vi-lib/rvi/analysis/siggen/squarewave/nifpga-square-wave-generator-vi.html) Generates a point-by-point square wave using direct digital synthesis (DDS). The synthesis runs continuously using the block diagram clock rate to produce a real-time frequency. The block diagram clock rate is the top-level clock rate , unless the Square Wave Generator Express VI is inside a single-cycle Timed Loop configured with a different clock rate.
- [White Noise Generator](../../../../../../vi-lib/rvi/analysis/siggen/whitenoise/nifpga-white-noise-generator-vi.html) Generates a white noise signal with uniform or Gaussian distribution.

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/structs-mnu.html language=enus -->
## TOPIC 00123: Structures

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/structs-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/structs-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the structures to control data flow. If you use a global variable in an FPGA VI, the global variable maps directly to a register on the FPGA target. Use global variables to transfer data between loops efficiently. This palette is specific to FPGA targets and contains a subset of the VIs and func

### Structures

Use the structures to control data flow.

If you use a global variable in an FPGA VI, the global variable maps directly to a register on the FPGA target. Use global variables to transfer data between loops efficiently.

Note

Refer to the [Structures Palette Details](/csh?context=lvfpga_lvfpga_structures_details) topic for information about Timed Loop compatibility, usage, timing, and resource considerations related to the objects on this palette.

[IMAGE alt='icon' src='structs-mnu.png']

- [Timed Structures](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/structures/timedloop-mnu.html) Use the Timed Loop structure to control the rate at which a subdiagram executes.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/structures/timedloop-mnu.html language=enus -->
## TOPIC 00124: Timed Structures

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/structures/timedloop-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/structures/timedloop-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Timed Loop structure to control the rate at which a subdiagram executes. icon

### Timed Structures

Use the Timed Loop structure to control the rate at which a subdiagram executes.

[IMAGE alt='icon' src='timedloop-mnu.png']

- [FPGA Clock Constant](../../../../../../../vi-lib/rvi/timedloop/nifpga-palettemergevi-clocknameconstant-vi.html) Use the FPGA clock constant to specify an FPGA clock on the block diagram.
- [Start Enabling FPGA Clock](../../../../../../../vi-lib/fpga/timing/nifpgastartenableclock-vi.html) Starts enabling an FPGA clock . To ensure data integrity, the clock you want to enable must be glitch free and free running. When you reenable the clock using this VI, the state of all registers and memory using the disabled clock is the same as the last cycle before the clock was disabled.
- [Start Disabling FPGA Clock](../../../../../../../vi-lib/fpga/timing/nifpgastartdisableclock-vi.html) Starts disabling an FPGA clock to protect circuitry dependent on a periodic clock. Use this VI to disable the clock prior to glitches or before the clock signal becomes unavailable. Clocks that support and require enabling and disabling at run time begin disabled after you download or reset the FPGA VI. When you reenable the clock using the Start Enabling FPGA Clock VI, the state of all registers and memory using the disabled clock is the same as the last cycle before the clock was disabled.
- [Timed Loop](../../../../../../../vi-lib/rvi/timedloop/timed-loop.html)

Parent topic:

Structures

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/synch-mnu.html language=enus -->
## TOPIC 00125: Synchronization

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/synch-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/synch-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Synchronization functions to synchronize tasks executing in parallel and pass data between parallel tasks. This palette is specific to FPGA targets and contains a subset of the VIs and functions that are on this palette when you edit a host VI. icon

### Synchronization

Use the Synchronization functions to synchronize tasks executing in parallel and pass data between parallel tasks.

Note

[IMAGE alt='icon' src='synch-mnu.png']

- [FIFO](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/fpgafifo-mnu.html) Use the FIFO Method Node with the Read and Write methods to transfer data from one loop to another using FIFOs in an FPGA VI, such as among single-cycle Timed Loops . You also can use the Write method to transfer data to host VIs using a DMA FIFO .
- [Occurrences](../../../../../../targets/ni/fpga/menus/fpgacategories/programming/occur-mnu.html) Use the Occurrences functions to control separate, synchronous activities. In particular, use these functions when you want one part of a block diagram to wait until another part of a block diagram finishes a task without forcing LabVIEW to poll.
- [Interrupt](../../../../../../vi-lib/rvi/interrupt/nifpga-interrupt-vi.html) Asserts an interrupt on the interrupt line of the FPGA target.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/menus/fpgacategories/programming/timing-mnu.html language=enus -->
## TOPIC 00126: Timing

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/menus/fpgacategories/programming/timing-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/menus/fpgacategories/programming/timing-mnu.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Timing VIs to control the execution timing of FPGA operations. This palette is specific to FPGA targets and contains a subset of the VIs and functions that are on this palette when you edit a host VI. icon

### Timing

Use the Timing VIs to control the execution timing of FPGA operations.

Note

[IMAGE alt='icon' src='timing-mnu.png']

- [Loop Timer](../../../../../../vi-lib/express/rvi/timing/nirvilooptimer-vi.html) Waits the value you specify in Count between loop iterations. You can call this function in a loop to control the loop execution rate. If an execution instance is missed, such as when the logic in the loop takes longer to execute than the specified interval, the Loop Timer Express VI returns immediately and establishes a new reference time stamp for subsequent calls. To manage execution rates with the Loop Timer Express VI, place the Loop Timer Express VI in the first frame of a Flat Sequence structure or a Stacked Sequence structure and put the rest of the code in subsequent frames.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/rio/compactrio/vi-lib/criorefnumtag-vi.html language=enus -->
## TOPIC 00127: cRIO I/O Device

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/rio/compactrio/vi-lib/criorefnumtag-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/rio/compactrio/vi-lib/criorefnumtag-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the cRIO I/O Device to specify a cRIO I/O item on the block diagram. icon

### cRIO I/O Device

Use the cRIO I/O Device to specify a cRIO I/O item on the block diagram.

[IMAGE alt='icon' src='criorefnumtag-vi.png']

Parent topic:

FPGA I/O

<!--NI_TOPIC bundle=lvfpga-api-ref path=targets/ni/fpga/terminals-page-component-level-ip-properties-dialog-box.html language=enus -->
## TOPIC 00128: Terminals Page (Component-Level IP Properties Dialog Box)

- bundle_id: `lvfpga-api-ref`
- source_path: `targets/ni/fpga/terminals-page-component-level-ip-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/targets/ni/fpga/terminals-page-component-level-ip-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Component-Level IP Properties dialog box, select General from the Category list to display this page. Use this page to specify the names and data types of block diagram terminals that correspond to VHDL ports in the component-level IP (CLIP). This page includes the following options: Option D

### Terminals Page (Component-Level IP Properties Dialog Box)

In the [Component-Level IP Properties](/csh?context=lvfpga_lvfpgadialog_clip_properties) dialog box, select **General** from the **Category** list to display this page.

Use this page to specify the names and data types of block diagram terminals that correspond to VHDL ports in the [component-level IP (CLIP)](/csh?context=lvfpga_lvfpgaconcepts_using_component_ip).

This page includes the following options:

| Option | Description |
| --- | --- |
| terminal settings | Lists the terminals in the CLIP by their LabVIEW names. |
| Default Data Type | Displays the default terminal type as the CLIP declaration XML defines it. |
| LabVIEW Data Type | Displays the data type of the terminal for this instantiation of the CLIP. |
| terminal type selector | Specifies an override data type for the terminal you select in the LabVIEW Name column. Fixed-point encoding—Specifies whether the selected terminal is Signed or Unsigned. This option is valid for fixed-point terminals only. Integer word length—Specifies the integer word length of the selected terminal between [–2048, 2047]. This option is valid for fixed-point terminals only. LabVIEW sets the word length of the terminal to the width of the corresponding port as specified in the IP. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/dlg-ctls-llb/sgl-numeric-constant.html language=enus -->
## TOPIC 00129: SGL Numeric Constant VI

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/dlg-ctls-llb/sgl-numeric-constant.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/dlg-ctls-llb/sgl-numeric-constant.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: icon

### SGL Numeric Constant VI

[IMAGE alt='icon' src='sgl-numeric-constant.png']

Parent topic:

Numeric

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/configureiomerge-vi.html language=enus -->
## TOPIC 00130: Configure I/O

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/configureiomerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/configureiomerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes channel configuration data to the I/O items. Use this node with multiplexed analog input devices where the configuration for a channel transfers from the FPGA to the target I/O on each clock pulse. If the channel configuration does not update with each sample pulse, the previously written con

### Configure I/O

Writes channel configuration data to the I/O items. Use this node with multiplexed analog input devices where the configuration for a channel transfers from the FPGA to the target I/O on each clock pulse. If the channel configuration does not update with each sample pulse, the previously written configuration transfers again, and the device will continue to acquire from the same channel with the same configuration.

[IMAGE alt='icon' src='configureiomerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. I/O Item — I/O Item is the configuration data written to the selected I/O item. The data type and the function of I/O Item vary depending on the hardware. Timeout — specifies the maximum time, in number of clock ticks, that the function will wait to write channel configuration data. A value of –1 prevents the function from timing out, so the function completes execution only when it writes all data. If Timeout is 0 and this function cannot write data immediately, a timeout occurs. If a timeout occurs, the previous configuration does not change. Input Valid — Input Valid specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. error out — error out contains error information. This output provides standard error out functionality. Timed Out — returns TRUE if this function times out. If Timed Out is TRUE, this function did not write data to any I/O items. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. Ready for Input — Ready for Input returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the Input Valid terminal is TRUE during the following cycle. To display this terminal, right-click the function and select Inside single-cycle Timed Loop from the shortcut menu. |
| --- |

The following connector pane displays the parameters that appear when this function is outside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Note

This function does not wait for the data to transfer to the I/O items, but only posts the data. This posted data transfers immediately to the I/O item until the I/O item is primed. Once the I/O item is primed, posted data transfers from the FPGA to the I/O item only on each sample pulse the Generate I/O Sample Pulse Method function generates. You must prime the I/O item with data before the Generate I/O Sample Pulse Method function runs or the sample pulse is gated.

All references to the same I/O item use the same buffer, even if different Configure I/O Method functions reference the I/O item. Functions that write data always wait for the existing data in the buffer to be read and will not overwrite buffer data. When the Generate I/O Sample Pulse Method function executes, the oldest data in the buffer is read. If the buffer is empty when the Generate I/O Sample Pulse Method function executes, the buffer regenerates using stale data. If multiple I/O items are present in the same node, the write occurs only if each I/O item has space available. Otherwise, this function reports a timeout.

#### Single-Cycle Timed Loop Details

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it. Right-click the function and select **Execution Mode»Outside single-cycle Timed Loop** or **Inside single-cycle Timed Loop** to specify where the function executes.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/generateiosamplepulsemerge-vi.html language=enus -->
## TOPIC 00131: Generate I/O Sample Pulse

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/generateiosamplepulsemerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/generateiosamplepulsemerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a pulse on the sample clock terminal of the I/O items. icon Inputs/Outputs cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In FPGA I/O In is an optional input that allows you to sp

### Generate I/O Sample Pulse

Initiates a pulse on the sample clock terminal of the I/O items.

[IMAGE alt='icon' src='generateiosamplepulsemerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. error out — error out contains error information. This output provides standard error out functionality. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. |
| --- |

To select a method, first configure the node with an I/O item.

Note

The action that occurs when a sample pulse is generated is hardware-specific and may vary from target to target. For instance, the sample pulse for a multiplexed hardware module will cause a single conversion on a single channel. The same sample pulse on a simultaneous sampling hardware module may cause a conversion to occur on all channels of the module.

If the node contains multiple I/O items, a sample pulse occurs only if each I/O item is ready to receive the sample pulse. Otherwise, the sample pulse is gated, and the node immediately returns control. Use the [Get I/O Read Status Method](getioreadstatusmerge-vi.html) function, [Get I/O Write Status Method](getiowritestatusmerge-vi.html) function, or the [Get I/O Configuration Status Method](getioconfigurationstatusmerge-vi.html) function to determine whether the sample pulse was gated or generated successfully.

#### Single-Cycle Timed Loop Details

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioconfigurationstatusmerge-vi.html language=enus -->
## TOPIC 00132: Get I/O Configuration Status

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioconfigurationstatusmerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioconfigurationstatusmerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports the status of writing channel configuration data to I/O items. icon Inputs/Outputs cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In FPGA I/O In is an optional input that allows you

### Get I/O Configuration Status

Reports the status of writing channel configuration data to I/O items.

[IMAGE alt='icon' src='getioconfigurationstatusmerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. error out — error out contains error information. This output provides standard error out functionality. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. Data Regenerated — Data Regenerated returns TRUE if the Configure I/O Method function regenerates data. A value of TRUE also indicates that the Generate I/O Sample Pulse Method function providing timing for the I/O item executed at least two times since the last execution of the Configure I/O Method function. This function does not report the number of data points regenerated, only that some data was regenerated. The value of Data Regen does not reset until read through this function or the Reset I/O Method function executes. Primed — Primed returns TRUE when the configuration data path for the I/O item is primed. You must write one or more data values using the Configure I/O Method function to prime the data path before executing the Generate I/O Sample Pulse Method function. Otherwise, the sample pulse is gated. The value of Primed remains TRUE until the Reset I/O Method function executes. |
| --- |

To select a method, first configure the node with an I/O item.

Note

#### Single-Cycle Timed Loop Details

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioreadstatusmerge-vi.html language=enus -->
## TOPIC 00133: Get I/O Read Status

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioreadstatusmerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/getioreadstatusmerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports the status of reading I/O data from the I/O items. icon Inputs/Outputs cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In FPGA I/O In is an optional input that allows you to specify

### Get I/O Read Status

Reports the status of reading I/O data from the I/O items.

[IMAGE alt='icon' src='getioreadstatusmerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. error out — error out contains error information. This output provides standard error out functionality. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. Overwrite — Overwrite returns TRUE if the Generate I/O Sample Pulse Method function wrote over data for any I/O item before the Read I/O Method function could read it. A value of TRUE indicates that the Generate I/O Sample Pulse Method function providing the timing for the I/O item executed at least two times since the last execution of the Read I/O Method function. The Get I/O Read Status Method function does not report the number of data points overwritten, only that some data was overwritten. The value of Overwrite does not reset until this function reads it or the Reset I/O Method function executes. Sample Gated — Sample Gated returns TRUE when the Generate I/O Sample Pulse Method function generates a sample pulse that is gated. This function does not report the number of sample pulses gated, only that at least one pulse has been gated since the last time this function executed. The value of Clock Gated does not reset until this function reads it or the Reset I/O Method function executes. A sample pulse can be gated for the following reasons: The Generate I/O Sample Pulse Method function tries to execute more quickly than the maximum specified rate of the I/O item. Arbitration for the resource is occurring. The target is conducting an operation such that it cannot issue a clock pulse. |
| --- |

To select a method, first configure the node with an I/O item.

Note

#### Single-Cycle Timed Loop Details

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/getiowritestatusmerge-vi.html language=enus -->
## TOPIC 00134: Get I/O Write Status

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/getiowritestatusmerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/getiowritestatusmerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports the status of written output from the I/O items. icon Inputs/Outputs cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In FPGA I/O In is an optional input that allows you to specify th

### Get I/O Write Status

Reports the status of written output from the I/O items.

[IMAGE alt='icon' src='getiowritestatusmerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. error out — error out contains error information. This output provides standard error out functionality. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. Data Regenerated — returns TRUE if the Generate I/O Sample Pulse Method function causes data to be regenerated. A value of TRUE indicates that the Generate I/O Sample Pulse Method function providing timing for the I/O item executed at least two times since the last execution of the Write I/O Method function. This function does not report the number of data points regenerated, only that some data regenerated. The value of Data Regen does not reset until this function reads it or the Reset I/O Method function executes. Sample Gated — returns TRUE when the Generate I/O Sample Pulse Method function generates a sample pulse that is gated. This function does not report the number of sample pulses gated, only that at least one pulse has been gated since the last time this function executed. The value of Clock Gated does not reset until this function reads it or the Reset I/O Method function executes. A sample pulse can be gated for the following reasons: The Generate I/O Sample Pulse Method function tries to execute more quickly than the maximum specified rate of the I/O item. Arbitration for the resource is occurring. The target is conducting an operation such that it cannot issue a clock pulse. Write Completed — returns TRUE each time data transfers from the write buffer to the I/O item. Use this status to determine when the data that the Write I/O Method function writes is ready for the Generate I/O Sample Pulse Method function to output. The value of Write Completed does not reset until this function reads it or the Reset I/O Method function executes. |
| --- |

To select a method, first configure the node with an I/O item.

Note

#### Single-Cycle Timed Loop Details

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/readiomerge-vi.html language=enus -->
## TOPIC 00135: Read I/O

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/readiomerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/readiomerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the I/O data from the I/O items. This function waits for new I/O data to become available through the Generate I/O Sample Pulse Method function. The following connector pane displays the parameters that appear when this function is outside a single-cycle Timed Loop. icon Inputs/Outputs cerrcod

### Read I/O

Reads the I/O data from the I/O items. This function waits for new I/O data to become available through the [Generate I/O Sample Pulse Method](/csh?context=lvfpga_lvfpga_fpga_uc_generate_io_pulse) function.

The following connector pane displays the parameters that appear when this function is outside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

[IMAGE alt='icon' src='readiomerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. Timeout — specifies the maximum time, in number of clock ticks, that the function waits until it can write to an I/O item without overwriting data. A value of -1 prevents the function from timing out, so the function completes execution only when it writes all data. If Timeout is 0 and this function cannot write data immediately, a timeout occurs. If a timeout occurs, previously written data remains intact. Ready for Output — Ready for Output specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the Ready for Input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To display this terminal, right-click the function and select Inside single-cycle Timed Loop from the shortcut menu. error out — error out contains error information. This output provides standard error out functionality. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. I/O Item — I/O Item is the data read from the FPGA I/O item. Timed Out — returns TRUE if this function times out. If Timed Out is TRUE, this function did not write data to any I/O items. Output Valid — Output Valid returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the Input Valid input of a downstream node to transfer data from the node to the downstream node. To display this terminal, right-click this function and select Inside single-cycle Timed Loop from the shortcut menu. |
| --- |

#### Read I/O Details

To select a method, first configure the node with an I/O item.

Note

If multiple Read I/O Method functions contain the same I/O item, all functions reference the same data buffer. A read from any function will return the oldest unread data, and data that the Generate I/O Sample Pulse Method function acquires will overwrite the oldest element in the buffer. If the node contains multiple I/O items, this node reads data only if each I/O item has unread data available for reading.

#### Single-Cycle Timed Loop Support

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it. Right-click the function and select **Execution Mode»Outside single-cycle Timed Loop** or **Inside single-cycle Timed Loop** to specify where the function executes.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/resetiomerge-vi.html language=enus -->
## TOPIC 00136: Reset I/O

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/resetiomerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/resetiomerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the state, clears the data path, and clears any error conditions for the I/O items. This node also resets any pipeline stages and counters for the I/O item. icon Inputs/Outputs cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides

### Reset I/O

Resets the state, clears the data path, and clears any error conditions for the I/O items. This node also resets any pipeline stages and counters for the I/O item.

[IMAGE alt='icon' src='resetiomerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. error out — error out contains error information. This output provides standard error out functionality. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. |
| --- |

#### Reset I/O Details

To select a method, first configure the node with an I/O item.

Note

#### Single-Cycle Timed Loop Details

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. If **error in** indicates an error, this function executes normally and passes the value of **error in** to **error out**. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiogrowablemethodnode/fixedmethods/writeiomerge-vi.html language=enus -->
## TOPIC 00137: Write I/O

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiogrowablemethodnode/fixedmethods/writeiomerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiogrowablemethodnode/fixedmethods/writeiomerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes new output data to the I/O items as soon as the target is ready to receive new data. This function does not overwrite previously written data. The following connector pane displays the parameters that appear when this function is outside a single-cycle Timed Loop. icon Inputs/Outputs cerrcode

### Write I/O

Writes new output data to the I/O items as soon as the target is ready to receive new data. This function does not overwrite previously written data.

The following connector pane displays the parameters that appear when this function is outside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

[IMAGE alt='icon' src='writeiomerge-vi.png']

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. I/O Item — is the data to write to the FPGA I/O item. When you select an element on the node without wiring a value to FPGA I/O In, the name of this parameter changes to match the name of the FPGA I/O item you specify. Timeout — specifies the maximum time, in number of clock ticks, that the function waits until it can write to an I/O item without overwriting data. A value of -1 prevents the function from timing out, so the function completes execution only when it writes all data. If Timeout is 0 and this function cannot write data immediately, a timeout occurs. If a timeout occurs, previously written data remains intact. Input Valid — Input Valid specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshakingterminal, right-click the function and select Inside single-cycle Timed Loop from the shortcut menu. error out — error out contains error information. This output provides standard error out functionality. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O In. Timed Out — returns TRUE if this function times out. If Timed Out is TRUE, this function did not write data to any I/O items. Ready for Input — Ready for Input returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the Input Valid terminal is TRUE during the following cycle. To display this terminal, right-click the function and select Inside single-cycle Timed Loop from the shortcut menu. |
| --- |

Note

To select a method, first configure the node with an I/O item.

This function writes data to a buffer on the FPGA. Once this function writes data to the buffer, the data transfers from the buffer to the I/O item. Once the Generate I/O Sample Method executes, the I/O item can output the data. Data transfers to the I/O item either immediately if the item has space available or after the Generate I/O Sample Pulse Method executes if no space is available. Use the Get I/O Write Status Method function to determine when the data has transferred to the I/O item.

If multiple Write I/O Method functions contain the same I/O item, all functions reference the same data buffer. If the buffer is empty when the Generate I/O Sample Pulse Method function executes, the buffer regenerates and the previously written data is transferred again. 
 If multiple I/O Items in the same node are present, the write will occur only if each I/O Item has space available. Otherwise, a timeout will be reported.

#### Single-Cycle Timed Loop Support

This node is supported inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) if the target supports it. Right-click the function and select **Execution Mode»Outside single-cycle Timed Loop** or **Inside single-cycle Timed Loop** to specify where the function executes.

#### Error Handling Details

You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

User-Controlled I/O Sampling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiomethodnode/eiomethodnode-xnode.html language=enus -->
## TOPIC 00138: FPGA I/O Method Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiomethodnode/eiomethodnode-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiomethodnode/eiomethodnode-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes a method on an I/O item or hardware under an FPGA target in the Project Explorer window, such as a C Series module. In some cases, you also can invoke methods on the FPGA target itself. The methods available depend on the FPGA target and the FPGA I/O item or C Series module you select. To se

### FPGA I/O Method Node

Invokes a method on an I/O item or hardware under an FPGA target in the Project Explorer window, such as a C Series module. In some cases, you also can invoke methods on the FPGA target itself. The methods available depend on the FPGA target and the FPGA I/O item or C Series module you select.

To select a method, first [configure](/csh?context=lvfpga_lvfpgahelp_creating_fpgaio_method) the FPGA I/O Method Node with an item.

| Parameter | Description |
| --- | --- |
| FPGA I/O In | FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant.To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. |
| FPGA I/O Out | FPGA I/O Out returns the FPGA I/O item on which you configure the node to operate. |

[IMAGE alt='icon' src='eiomethodnode-xnode.png']

Support for certain methods inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_fpga_timed_loop) varies by target and I/O item. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for more information.

Tip

Find Item in Project

Project Explorer

Additional parameters vary depending on the related method. Method support varies by FPGA target and I/O resource. Some FPGA targets do not support any methods. A method can have zero or more parameters.

FPGA targets with [bidirectional digital I/O lines and ports](/csh?context=lvfpgaconcepts_performing_basic_i_o) typically support the following methods for bidirectional I/O items.

- Set Output Data Method —Writes data to the digital line or port without enabling the line or port. You can use the Set Output Data method to optimize performance when performing successive writes to a DIO resource. The data type of the Data input depends on the I/O item. For example, if the I/O item is a digital line, Data requires a Boolean data type.
- Set Output Enable Method —Determines whether the digital input and output resource reads external input or writes output. Wiring TRUE to Set Output Enable for a digital line allows the resource to write data. Wiring FALSE to Set Output Enable allows the resource to read external data. The data type of the Enable input depends on the I/O item. For example, if the I/O item is a digital line, Enable requires a Boolean data type, and if the I/O item is an 8-bit digital port, Enable requires a U8 data type. The binary values of the U8 input correspond to the individual lines of the digital port. Zeros correspond to false inputs and ones correspond to true inputs.
- Get Timed Input Data Method —Reads data from the external digital line. Valid returns TRUE when you configure the DIO resource to read external input by using the Set Timed Output Enable method or after you reset the block diagram. You can use this method to perform successive read operations from a DIO resource on FPGA targets. Data supports the Boolean data type only.
- Set Timed Output Data Method —Writes data to the digital line without enabling the line. Ready returns TRUE when you configure the DIO resource to write output. You can use this method to perform successive write operations to a DIO resource on FPGA targets. Data supports the Boolean data type only.
- Set Timed Output Enable Method —Determines whether the DIO resource reads external input or writes output. Settled returns TRUE when the line I/O direction changes. When you use this method in a single-cycle Timed Loop, the number of clock cycles between the time when you change the Enable value and the time when the Settled value changes to TRUE varies depending on the FPGA target. Set Enable to TRUE for a digital line allows the resource to write data. Set Enable to FALSE allows the resource to read external data. NI recommends that you use this method to configure a DIO resource on FPGA targets when possible. Enable supports the Boolean data type only. When you use this method outside a single-cycle Timed Loop, Settled always returns TRUE.

**Error Handling Details**

You can right-click the FPGA I/O Method Node on the block diagram and select **Show Error Terminals** from the shortcut menu to add standard LabVIEW **error in** and **error out** parameters to the function. You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Note

error in

error out

error in

error out

Parent topic:

FPGA I/O

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eionode/eionode-xnode.html language=enus -->
## TOPIC 00139: FPGA I/O Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eionode/eionode-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eionode/eionode-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs specific FPGA I/O operations on FPGA targets. You can configure the FPGA I/O Node with one or more FPGA I/O items. To add additional FPGA I/O items to an FPGA I/O Node, right-click the I/O Item section and select Add Element from the shortcut menu. You also can expand or contract the FPGA I

### FPGA I/O Node

Performs specific FPGA I/O operations on FPGA targets. You can configure the FPGA I/O Node with one or more FPGA I/O items.

To add additional FPGA I/O items to an FPGA I/O Node, right-click the **I/O Item** section and select **Add Element** from the shortcut menu. You also can expand or contract the FPGA I/O Node by clicking the upper or lower edge of the node with the Positioning tool and dragging the edge up or down.

[IMAGE alt='icon' src='eionode-xnode.png']

#### Inputs/Outputs

| I/O Item — I/O Item is the data read from or written to the FPGA I/O item you specify. For FPGA I/O items that support the read operation, this parameter is an indicator by default. For I/O items that do not support the read operation, this parameter is a control by default. For FPGA I/O items that support reading and writing, this parameter can be either a control or an indicator. This parameter changes to a control or indicator when you right-click an element in the node and select Change to Write or Change to Read, respectively. When you select an element on the node without wiring a value to FPGA I/O In, the name of this parameter changes to match the name of the FPGA I/O item you specify. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O item on which you configure the node to operate. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. |
| --- |

When you right-click the element section of the FPGA I/O Node and select **Select FPGA I/O** from the shortcut menu, LabVIEW displays the FPGA I/O items that appear in the [Project Explorer](/csh?context=lvcore_lvdialog_project_explorer_window) window below the same FPGA target as the FPGA VI you are currently editing. You also can right-click the element selection and select **Add New FPGA I/O** to add new FPGA I/O items under the FPGA target.

[Digital input and output](/csh?context=lvfpgaconcepts_performing_basic_i_o) (DIO) resources can perform both read and write operations. To change the operation of an FPGA I/O item, right-click the element and select **Change to Read** or **Change to Write** from the shortcut menu. Use the [FPGA I/O Method Node](../eiomethodnode/eiomethodnode-xnode.html) configured with the Set Output Enable method to change the direction of a Digital Input and Output I/O resource.

When you configure an I/O Node with multiple I/O items, LabVIEW displays **FPGA I/O In**, **FPGA I/O Out**, and **I/O Item** parameters for each I/O item. When you configure an I/O Node with multiple I/O items, the execution timing of the I/O items depends on the specific hardware devices and I/O items you use. Some FPGA I/O operations execute in parallel, while others execute sequentially.

Tip

Find Item in Project

Project Explorer

**Error Handling Details**

You can right-click the FPGA I/O Node on the block diagram and select **Show Error Terminals** from the shortcut menu to add standard LabVIEW **error in** and **error out** parameters to the function. If an error occurs, you might receive incorrect data. Add error terminals to be sure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Note

error in

error out

error in

error out

Parent topic:

FPGA I/O

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eionode/fpga-i-o-node-properties-dialog-box.html language=enus -->
## TOPIC 00140: FPGA I/O Node Properties Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eionode/fpga-i-o-node-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eionode/fpga-i-o-node-properties-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an FPGA I/O Node on the block diagram and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure the FPGA I/O Node. The options that appear in this dialog box vary by the FPGA target and FPGA I/O you use. The options you configure in the FPG

### FPGA I/O Node Properties Dialog Box

Right-click an [FPGA I/O Node](eionode-xnode.html) on the block diagram and select **Properties** from the shortcut menu to display this dialog box.

Use this dialog box to configure the FPGA I/O Node. The options that appear in this dialog box vary by the FPGA target and FPGA I/O you use.

Note

Project Explorer

This dialog box might include the [Advanced Code Generation](../../../resource/rvi/stockio/private/stockfpga-eiodialogcontexthelpholder-vi.html) page in the **Category** list.

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/eio/eiopropertynode/eiopropertynode-xnode.html language=enus -->
## TOPIC 00141: FPGA I/O Property Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/eio/eiopropertynode/eiopropertynode-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/eio/eiopropertynode/eiopropertynode-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets one or more properties on an I/O item or hardware under an FPGA target in the Project Explorer window, such as a C Series module. In some cases, you also can set and retrieve properties on the FPGA target itself. The properties available vary by the FPGA target or the C Series module an

### FPGA I/O Property Node

Gets or sets one or more properties on an I/O item or hardware under an FPGA target in the Project Explorer window, such as a C Series module. In some cases, you also can set and retrieve properties on the FPGA target itself. The properties available vary by the FPGA target or the C Series module and the I/O resource.

To select a property, first [configure](/csh?context=lvfpga_lvfpgahelp_creating_fpgaio_property_nodes) the FPGA I/O Property Node with an item. Then, click the **Property** section of the FPGA I/O Property Node and select a property from the shortcut menu. To add additional properties to an FPGA I/O Property Node, right-click the **Property** section and select **Add Element** from the shortcut menu. You also can expand or contract the FPGA I/O Property Node by dragging the upper or lower edge of the node with the Positioning tool.

[IMAGE alt='icon' src='eiopropertynode-xnode.png']

#### Inputs/Outputs

| Property — Property is the value of the I/O Property you specify. To specify whether this parameter is a control or an indicator, right-click an element in the Property section of the FPGA Property Node and select Change to Read or Change to Write from the shortcut menu. FPGA I/O Out — FPGA I/O Out returns the FPGA I/O item on which you configure the node to operate. FPGA I/O In — FPGA I/O In is an optional input that allows you to specify the FPGA I/O item to read or write using an FPGA I/O control or constant. To use an FPGA I/O control as a connector pane input, the FPGA VI must be configured for reentrant execution. |
| --- |

Support for use of the FPGA I/O Property Node and specific properties inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_fpga_timed_loop) varies by target, I/O item, and property. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for more information.

When you expand the FPGA I/O Property Node, LabVIEW displays a **Property** parameter for each element of the Node. However, the FPGA I/O Property Node contains only one set of FPGA I/O In and FPGA I/O Out parameters. Each FPGA I/O Property Node operates on a single FPGA I/O item.

Tip

Find Item in Project

Project Explorer

**Error Handling Details**

You can right-click the FPGA I/O Property Node on the block diagram and select **Show Error Terminals** from the shortcut menu to add standard LabVIEW **error in** and **error out** parameters to the function. If an error occurs, you might receive incorrect data. Add error terminals to be sure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Note

error in

error out

error in

error out

Parent topic:

FPGA I/O

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/analysis/control/discrete-linear/nifpga-discrete-delay-vi.html language=enus -->
## TOPIC 00142: Basic Discrete Delay

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/analysis/control/discrete-linear/nifpga-discrete-delay-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/analysis/control/discrete-linear/nifpga-discrete-delay-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delays the input value for the number of loop iterations you specify in the Configure Basic Discrete Delay dialog box. icon Dialog Box Options Inputs/Outputs ci32.png input Inputs the data point the VI processes. cbool.png initialize Causes LabVIEW to return initial condition as the output. The VI i

### Basic Discrete Delay

Delays the input value for the number of loop iterations you specify in the **Configure Basic Discrete Delay** dialog box.

[IMAGE alt='icon' src='nifpga-discrete-delay-vi.png']

#### Dialog Box Options

#### Inputs/Outputs

| input — Inputs the data point the VI processes. initialize — Causes LabVIEW to return initial condition as the output. The VI initializes automatically when it first runs. initial condition — Inputs the data point the VI returns when first called or when initialize is TRUE. The VI returns initial condition every call after initialization until the loop iterations meet the specified delay. output — Returns the delayed input value. |
| --- |

Parent topic:

Discrete Linear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/analysis/control/nonlinear/nifpga-boolean-crossing-vi.html language=enus -->
## TOPIC 00143: Boolean Crossing

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/analysis/control/nonlinear/nifpga-boolean-crossing-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/analysis/control/nonlinear/nifpga-boolean-crossing-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects state changes of Boolean input points. You can choose from three detectors: either, false-true, or true-false. icon Inputs/Outputs cbool.png initialize initialize, when TRUE, stores input and sets crossing to FALSE. The VI initializes automatically when you first call it in a VI. cbool.png i

### Boolean Crossing

Detects state changes of Boolean input points. You can choose from three detectors: either, false-true, or true-false.

[IMAGE alt='icon' src='nifpga-boolean-crossing-vi.png']

#### Inputs/Outputs

| initialize — initialize, when TRUE, stores input and sets crossing to FALSE. The VI initializes automatically when you first call it in a VI. input — input is the Boolean data the VI compares with the previous value of input. direction — direction is the kind of Boolean crossing. 0either 1false-true 2true-false crossing — crossing is TRUE if a Boolean crossing occurred. |  |
| --- | --- |
| 0 | either |
| 1 | false-true |
| 2 | true-false |

Parent topic:

Discrete Nonlinear Systems

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/analysis/control/nonlinear/nifpga-quantizer-vi.html language=enus -->
## TOPIC 00144: Quantizer

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/analysis/control/nonlinear/nifpga-quantizer-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/analysis/control/nonlinear/nifpga-quantizer-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Quantizes an integer input signal using fixed-point rounding. icon Dialog Box Options Dialog Box Options Parameter Description Quantization Contains the following option: Interval (bits)—Specifies the desired integer quantization interval, such that 2^(Interval (bits)) is the width of each quantizat

### Quantizer

Quantizes an integer input signal using fixed-point rounding.

[IMAGE alt='icon' src='nifpga-quantizer-vi.png']

#### Dialog Box Options

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Quantization | Contains the following option: Interval (bits)—Specifies the desired integer quantization interval, such that 2^(Interval (bits)) is the width of each quantization bin. |
| Rounding Mode | Contains the following options: Round to nearest—The default rounding mode. LabVIEW rounds to the value nearest the original input while setting the lowest bits, specified by Interval (bits), to zero. If input is at the exact midpoint of a quantization bin, LabVIEW rounds the result to an even number. Use this option to return the most accurate result.Rounding up in the upper-most quantization bin results in overflow. This function uses the wrap overflow mode, which produces a negative output if the upper-most quantization bin overflows. Truncate—Equivalent to rounding to negative infinity. LabVIEW sets the lowest bits, specified by Interval (bits), to zero and leaves the rest of inputunaffected. Use this option to optimize the size of the VI. |
| Result Preview | Previews the behavior of the function for the selected Interval (bits). The options in this section do not affect the behavior of the quantizer but allow you to see how the quantizer affects any integer input. Input—Specifies the value the VI quantizes. Quantized output—Displays how the quantizer affects input. |

#### Inputs/Outputs

| input — The value you want to quantize. input is a 32-bit signed integer. output — The quantized input. output = [input / 2n] * 2n where n is equal to the configured interval (bits) and the [] operator indicates a fixed-point quantization operation that discards the lowest n bits using the specified Rounding Mode. |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/analysis/control/nonlinear/nifpga-saturate-vi.html language=enus -->
## TOPIC 00145: Saturation

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/analysis/control/nonlinear/nifpga-saturate-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/analysis/control/nonlinear/nifpga-saturate-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limits the valid range of a signal to that specified by Upper limit and Lower limit. You can configure the VI to specify the integer or bit limits and signed or unsigned inputs. icon Dialog Box Options Parameter Description Saturation Limits Contains the following options: By width—Allows you to spe

### Saturation

Limits the valid range of a signal to that specified by **Upper limit** and **Lower limit**. You can configure the VI to specify the integer or bit limits and signed or unsigned inputs.

[IMAGE alt='icon' src='nifpga-saturate-vi.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Saturation Limits | Contains the following options: By width—Allows you to specify the limits in terms of signed or unsigned word size. Bits (1 to 32)—Specifies the word size in bits of the range you want. Unsigned range—Produces nonnegative limits. The minimum and maximum limits are 0 to 2bits–1, respectively. If the checkbox does not contain a checkmark, the minimum and maximum limits are –2bits–1 to 2bits–1–1, respectively. By value—Allows you to specify limits as integers. Upper limit—Specifies the upper limit of the range. Lower limit—Specifies the lower limit of the range. |
| Input Type | Contains the following options: Signed—Specifies signed integers for the inputs. Unsigned—Specifies unsigned integers for the inputs. |
| Bits (1 to 32) | Specifies the word size in bits of the range you want. |

#### Inputs/Outputs

| upper limit — Specifies the upper saturation limit for input. You configure the default value in the Saturation Limits section of the Configure Saturation dialog box. The value you wire to this input overrides the selection you make in the Configure Saturation dialog box. input — Any signed or unsigned integer. If input is unsigned, select the Unsigned option in the Configure Saturation dialog box. lower limit — Specifies the lower saturation limit for input. You configure the default value in the Saturation Limits section of the Configure Saturation dialog box. The value you wire to this input overrides the value in the Configure Saturation dialog box. output — The saturated input. Input is saturated if input > upper limit or input < lower limit. output = upper limit if input > upper limit output = lower limit if input < lower limit Otherwise output equals input. |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/analysis/signal-gen/lut-1d/configure/define-table-dialog-box.html language=enus -->
## TOPIC 00146: Define Table Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/analysis/signal-gen/lut-1d/configure/define-table-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/analysis/signal-gen/lut-1d/configure/define-table-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Define Table button in the Configure Look-Up Table 1D dialog box to display this dialog box. Use this dialog box to initialize the look-up table you create in the Configure Look-Up Table 1D dialog box. You can edit data elements individually, define linear segments, use predefined function

### Define Table Dialog Box

Click the **Define Table** button in the [Configure Look-Up Table 1D](../../../signal-generation/look-up-table-1d/nifpga-look-up-table-1d-vi.html) dialog box to display this dialog box.

Use this dialog box to initialize the look-up table you create in the **Configure Look-Up Table 1D** dialog box. You can edit data elements individually, define linear segments, use predefined functions, or call an initialization VI you create.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Data Points | Displays the current contents of the look-up table. The values in the Element column correspond to the indexes of the look-up table array. |
| Define Segments | Opens the Configure Segment dialog box. You can specify endpoints of intervals you want to populate with a constant value, a line, a sine wave, or a cosine wave. |
| Call VI | Opens the Call Initialization VI dialog box.You can create, edit, or run an initialization VI to produce an array of elements to import into the Look-Up Table 1D Express VI. |
| Defined Signal | Displays the current contents of the look-up table in a waveform graph. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/analysis/signal-generation/look-up-table-1d/nifpga-look-up-table-1d-vi.html language=enus -->
## TOPIC 00147: Look-Up Table 1D

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/analysis/signal-generation/look-up-table-1d/nifpga-look-up-table-1d-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/analysis/signal-generation/look-up-table-1d/nifpga-look-up-table-1d-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a general-purpose block of initialized memory. Use look-up tables to store waveforms for signal generation, to model nonlinear systems, and for arithmetic computations. If you use the Look-Up Table 1D Express VI in a single-cycle Timed Loop, wire the outputs directly to Feedback Nodes. The

### Look-Up Table 1D

Provides a general-purpose block of initialized memory. Use look-up tables to store waveforms for signal generation, to model nonlinear systems, and for arithmetic computations. If you use the Look-Up Table 1D Express VI in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop), wire the outputs directly to [Feedback Nodes](/csh?context=lvcore_glang_feedback_node). The Look-Up Table 1D Express VI takes an entire clock cycle to execute in a single-cycle Timed Loop.

The main FPGA resources used for implementation of the Look-Up Table 1D are block memories, which Xilinx literature describes as block RAMs or BRAMs.

[IMAGE alt='icon' src='nifpga-look-up-table-1d-vi.png']

#### Dialog Box Options

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Look-Up Table Specifications | Contains the following options: Number of elements—Specifies the number of available elements in the look-up table. Data type—Specifies the data type of the output data from the look-up table. Choose among signed and unsigned integers. If you select an unsigned integer, you cannot select the Sine Wave or Cosine Wave modes in the Configure Segment dialog box. Interpolate data—interpolate-data If you place a checkmark in this checkbox, the Look-Up Table 1D Express VI takes at least two clock cycles to execute. Do not place a checkmark in the Interpolate data checkbox if the Look-Up Table 1D Express VI is in a single-cycle Timed Loop. Memory size—Displays the amount of memory the FPGA uses for the look-up table. Define Table—Opens the Define Table dialog box. You can initialize the memory block by editing points individually, defining linear segments, using predefined functions, or calling an initialization VI you create. |
| Function Name | Specifies a name for the look-up table to identify functionality of different instances of the Look-Up Table 1D Express VI on the block diagram. |
| Table Preview | Displays a preview of the data in the look-up table. |

#### Inputs/Outputs

| fractional index (x 2^16) — Specifies the 16-bit integer the VI interprets as a positive fractional number in the range 0 <= fractional index (x 2^16) < 1 to compute the linearly interpolated output between adjacent look-up table elements. Multiply the fractional index you want to use by 2^16 (65536) to convert it to a U16 integer data type for use on FPGA targets. For example, if you want a fractional index of .5, enter .5 x 2^16 = 32768 for the fractional index (x 2^16) input. The VI uses this input only if you place a checkmark in the Interpolate data checkbox in the Configure Look-Up Table 1D dialog box. address — Specifies an element of the look-up table. If address exceeds the Number of elements range you specify in the Configure Look-Up Table 1D dialog box, LabVIEW attempts to wrap the value into the valid range by using the lowest log2(Number of elements) bits of address. If Number of elements is an exact power of 2, any address input results in valid data out from the look-up table. For other sizes, the resulting wrapped address still exceeds the range. The VI returns 0 for data out. data out — The result of the table look-up operation. Specify the data type of this parameter in the Configure Look-Up Table 1D dialog box with the Data type selection. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Utilities\Look-Up Table\Look-Up Table.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Utilities\Look-Up Table\Look-Up Table.lvproj

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/shared/call-initialization-vi-dialog-box.html language=enus -->
## TOPIC 00148: Call Initialization VI Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/shared/call-initialization-vi-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/shared/call-initialization-vi-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Call Initialization VI button in the Define Table dialog box to display the Call Initialization VI dialog box. Use this dialog box to run, edit, or create an initialization VI to create an array that initializes a look-up table. This dialog box includes the following components: Option Des

### Call Initialization VI Dialog Box

Click the **Call Initialization VI** button in the [Define Table](/csh?context=lvfpga_lvfpgadialog_define_table) dialog box to display the **Call Initialization VI** dialog box.

Use this dialog box to run, edit, or create an initialization VI to create an array that initializes a look-up table.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Mode | Specifies the operation LabVIEW performs.Mode contains the following options: Run/Load Existing Initialization VI—Runs the VI you specify in Existing initialization VI path.LabVIEW then imports the output array into the look-up table. Edit Existing Initialization VI—Opens the VI you specify in Existing initialization VI path.LabVIEW then returns to the Define Table dialog box. You must close the dialog box to edit the initialization VI. Create New Initialization VI From Template—Opens an instance of a template VI and saves it to the location you specify in New initialization VI path.You must create all new initialization VIs using the Create New Initialization VI From Template option in this dialog box. You must close the dialog box to edit the initialization VI. |
| Initialization VI path | Specifies the path to an initialization VI.You must enter the Existing initialization VI path before you can run, edit, or create initialization VIs with the Call Initialization VI dialog box. |
| New initialization VI path | Specifies the path to save a new initialization VI when you select Create New Initialization VI From Template from the Mode pull-down menu. You must enter the New initialization VI path before you can run, edit, or create initialization VIs with the Call Initialization VI dialog box. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/shared/configure-segment-dialog-box.html language=enus -->
## TOPIC 00149: Configure Segment Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/shared/configure-segment-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/shared/configure-segment-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Define Segment button in the Define Table dialog box to display this dialog box. Use this dialog box to initialize the look-up table. You can populate specific look-up table segments with constants, straight lines, or sinusoidal waves. This dialog box includes the following components: Opt

### Configure Segment Dialog Box

Click the **Define Segment** button in the [Define Table](/csh?context=lvfpga_lvfpgadialog_define_table) dialog box to display this dialog box.

Use this dialog box to initialize the look-up table. You can populate specific look-up table segments with constants, straight lines, or sinusoidal waves.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| Starting address | Specifies the low end of the look-up table interval you want to populate. |
| Ending address | Specifies the high end of the look-up table interval you want to populate. |
| Mode | Specifies the contents with which LabVIEW populates the address interval you select.Mode contains the following values: Constant—Populates using the constant you specify in Value. Linear—Populates using a linear segment computed from the values you specify in Starting value and Slope. Sine Wave—Populates using a full-scale sine wave that you specify in Number of cycles. Cosine Wave—Populates using a full-scale cosine wave that you specify in Number of cycles. |
| Value | Specifies the constant LabVIEW enters in the look-up table if you select Constant from the Mode pull-down menu. |
| Starting value | Specifies the first value LabVIEW enters in the look-up table if you select Linear from the Mode pull-down menu. |
| Slope | Specifies the slope of the line LabVIEW enters in the look-up table if you select Linear from the Mode pull-down menu. |
| Number of cycles | Specifies the number of cycles LabVIEW enters in the look-up table if you select Sine Wave or Cosine Wave from the Mode pull-down menu. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/express/rvi/timing/nirvilooptimer-vi.html language=enus -->
## TOPIC 00150: Loop Timer

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/express/rvi/timing/nirvilooptimer-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/express/rvi/timing/nirvilooptimer-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits the value you specify in Count between loop iterations. You can call this function in a loop to control the loop execution rate. If an execution instance is missed, such as when the logic in the loop takes longer to execute than the specified interval, the Loop Timer Express VI returns immedia

### Loop Timer

Waits the value you specify in **Count** between loop iterations. You can call this function in a loop to control the loop execution rate. If an execution instance is missed, such as when the logic in the loop takes longer to execute than the specified interval, the Loop Timer Express VI returns immediately and establishes a new reference time stamp for subsequent calls. To [manage execution rates](/csh?context=lvfpga_lvfpgaconcepts_using_timing_functions) with the Loop Timer Express VI, place the Loop Timer Express VI in the first frame of a [Flat Sequence](/csh?context=lvcore_glang_flat_sequence) structure or a [Stacked Sequence](/csh?context=lvcore_glang_flat_sequence) structure and put the rest of the code in subsequent frames.

The Loop Timer Express VI differs from the [Wait Until Next ms Multiple](/csh?context=lvcore_glang_wait_till_next_ms_multiple) function, which wakes on a multiple of the wired in **millisecond multiple**.

During run time, you can use the [Sample Rate To Loop Time](../../../rvi/analysis/host/public/sample-rate-to-loop-time-vi.html) VI to convert the clock rate and sample rate to the appropriate count for the Loop Timer Express VI.

[IMAGE alt='icon' src='nirvilooptimer-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Counter Units | Unit of time the VI uses for the counter. Ticks—Sets the counter units to a single clock cycle, the length of which is determined by the clock rate for which the VI is compiled. uSec—Sets the counter units to microseconds. mSec—Sets the counter units to milliseconds. |
| Size of Internal Counter | Specifies the maximum time a timer can track. To save space on the FPGA, use the smallest Size of Internal Counter possible for the FPGA VI. |

#### Inputs/Outputs

| Count(Ticks) — Specifies the time between loop iterations. Tick Count(Ticks) — Returns the value of a free running counter at the time the VI wakes up. A free running counter rolls over when the counter reaches the maximum of Size of Internal Counter specified in the configuration dialog box. |
| --- |

The first time the Loop Timer Express VI executes in a loop, it records the current time. The next time the Loop Timer Express VI executes, it adds **Count** to the initial time and waits until **Count** has elapsed from the initial recorded time. The Loop Timer Express VI determines whether**Count** has elapsed only on whole integer value updates of its internal clock. Therefore, this function might increase loop execution time. To address this issue, set the**Counter Units** to **Ticks**. This change might help to reduce execution time by increasing the frequency of the internal clock updates.

The Loop Timer Express VI does not wait the first time you call it in an FPGA VI. If you place the Loop Timer Express VI in a loop so that it can execute immediately when the loop starts, all the code parallel with the Loop Timer Express VI in the loop executes twice before **Count** elapses after the initial time. To prevent the code from executing twice before **Count** elapses, use a [Flat Sequence](/csh?context=lvcore_glang_flat_sequence) structure or a [Stacked Sequence](/csh?context=lvcore_glang_flat_sequence) structure with the Loop Timer Express VI in the first frame and the rest of the code in subsequent frames to ensure that the code for the first and subsequent iterations is properly timed.

When called repeatedly using nested structures or continuous run mode, the Loop Timer Express VI timing does not reset each time. The Loop Timer Express VI continues to increment the time record it initiated upon the first call.

Tip

single-cycle Timed Loop

Parent topic:

Timing

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/fpga/timing/nifpgastartdisableclock-vi.html language=enus -->
## TOPIC 00151: Start Disabling FPGA Clock

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/fpga/timing/nifpgastartdisableclock-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/fpga/timing/nifpgastartdisableclock-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts disabling an FPGA clock to protect circuitry dependent on a periodic clock. Use this VI to disable the clock prior to glitches or before the clock signal becomes unavailable. Clocks that support and require enabling and disabling at run time begin disabled after you download or reset the FPGA

### Start Disabling FPGA Clock

Starts disabling an [FPGA clock](/csh?context=lvfpga_lvfpgahelp_applying_fpga_clocks_and_timing_title) to protect circuitry dependent on a periodic clock. Use this VI to disable the clock prior to glitches or before the clock signal becomes unavailable. Clocks that support and require enabling and disabling at run time begin disabled after you download or reset the FPGA VI. When you reenable the clock using the [Start Enabling FPGA Clock](/csh?context=lvfpga_lvfpga_start_enable_clk) VI, the state of all registers and memory using the disabled clock is the same as the last cycle before the clock was disabled.

You must include the Start Disabling FPGA Clock VI outside of the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) that is using the clock you are disabling.

Note

CLIP clocks

[IMAGE alt='icon' src='nifpgastartdisableclock-vi.png']

#### Inputs/Outputs

| FPGA Clock To Disable — FPGA Clock to Disable specifies the clock to disable. The clock you specify must support disabling at run time. To configure a clock to support disabling, place a checkmark in the Supports and Requires Runtime Enable/Disable checkbox in the FPGA Base Clock Properties dialog box. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. FPGA VIs do not support the Simple Error Handler VI, General Error Handler VI, or exception control. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You must configure the FPGA VI to execute the Start Disabling FPGA Clock and Start Enabling FPGA Clock VIs at different times. The Start Disabling FPGA Clock VI has no effect when you run an FPGA VI on a development computer or use the VI on a non-FPGA target. |
| Timing | A short delay exists before the clock is actually disabled because the disable must go through one register in the clock domain where the Start Disabling FPGA Clock VI is running and two registers in the clock domain you want to disable. |
| Resources | This VI consumes minimal FPGA resources. |

Parent topic:

Timed Structures

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/fpga/timing/nifpgastartenableclock-vi.html language=enus -->
## TOPIC 00152: Start Enabling FPGA Clock

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/fpga/timing/nifpgastartenableclock-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/fpga/timing/nifpgastartenableclock-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts enabling an FPGA clock. To ensure data integrity, the clock you want to enable must be glitch free and free running. When you reenable the clock using this VI, the state of all registers and memory using the disabled clock is the same as the last cycle before the clock was disabled. You must

### Start Enabling FPGA Clock

Starts enabling an [FPGA clock](/csh?context=lvfpga_lvfpgahelp_applying_fpga_clocks_and_timing_title). To ensure data integrity, the clock you want to enable must be glitch free and free running. When you reenable the clock using this VI, the state of all registers and memory using the disabled clock is the same as the last cycle before the clock was disabled.

You must include the Start Enabling FPGA Clock VI outside of the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) that is using the clock you are enabling.

Note

CLIP clocks

[IMAGE alt='icon' src='nifpgastartenableclock-vi.png']

#### Inputs/Outputs

| FPGA Clock To Enable — FPGA Clock to Enable specifies the clock to enable. The clock you specify must support enabling at run time. To configure a clock to support enabling, place a checkmark in the Supports and Requires Runtime Enable/Disable checkbox in the FPGA Base Clock Properties dialog box. If you place a checkmark in this checkbox, the FPGA Module disables the clock when you download or reset the FPGA VI. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. FPGA VIs do not support the Simple Error Handler VI, General Error Handler VI, or exception control. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

| Single-Cycle Timed Loop | Supported. |
| --- | --- |
| Usage | You must configure the FPGA VI to execute the Start Enabling FPGA Clock and Start Disabling FPGA Clock VIs at different times. The Start Enabling FPGA Clock VI has no effect when you run an FPGA VI on a development computer or use the VI on a non-FPGA target. |
| Timing | A short delay exists before the clock is actually enabled because the enable must go through one register in the clock domain where the Start Enabling FPGA Clock VI is running and two registers in the clock domain you want to enable. |
| Resources | This VI consumes minimal FPGA resources. |

Parent topic:

Timed Structures

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/basicops/templates/nifpga-linear-interpolation-m-vi.html language=enus -->
## TOPIC 00153: Linear Interpolation

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/basicops/templates/nifpga-linear-interpolation-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/basicops/templates/nifpga-linear-interpolation-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs linear interpolation to approximate a function evaluation at an arbitrary location in an interval between two known points. The data type you wire to y0 determines the output y data type. The maximum input word length is 16 bits. icon Inputs/Outputs cunkn.png y0 y0 is the value of the funct

### Linear Interpolation

Performs linear interpolation to approximate a function evaluation at an arbitrary location in an interval between two known points. The data type you wire to **y0** determines the output **y** data type.

The maximum **input** word length is 16 bits.

[IMAGE alt='icon' src='nifpga-linear-interpolation-m-vi.png']

#### Inputs/Outputs

| y0 — y0 is the value of the function at the interval endpoint corresponding to x equals zero. y1 — y1 is the value of the function at the interval endpoint corresponding to x equals one. y0 to y1 forms an interval over which to interpolate. x — x specifies the evaluation point relative to the interval y0 <= y < y1). x is a fixed-point number in the range 0 <= x < 1. The data type for x is limited to <±,16,0>. Extra fractional bits are coerced to 16 fractional bits at the VI boundary using round-to-nearest-even mode. y — y is the interpolated function evaluation. y = (y1 – y0)x + y0 |
| --- |

The VI uses truncation as the output rounding mode.

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/basicops/templates/nifpga-unit-delay-m-vi.html language=enus -->
## TOPIC 00154: Unit Delay

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/basicops/templates/nifpga-unit-delay-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/basicops/templates/nifpga-unit-delay-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delays the input value for one cycle. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRUE, returns initial condition as the output. The VI initializes automatically when it first runs in a VI.

### Unit Delay

Delays the input value for one cycle. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-unit-delay-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, returns initial condition as the output. The VI initializes automatically when it first runs in a VI. input — input is the data point the VI processes. initial condition — initial condition is the data point the VI returns the first time you call it or when reset is TRUE. output — output returns the delayed input value. output[n] = input[n – 1] where output[n] is the value of output on the nth call to the VI after initialization and output[0] = initial condition. |
| --- |

Parent topic:

Discrete Linear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/basicops/templates/nifpga-zero-crossing-m-vi.html language=enus -->
## TOPIC 00155: Zero Crossing

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/basicops/templates/nifpga-zero-crossing-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/basicops/templates/nifpga-zero-crossing-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects zero crossings of an input signal. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRUE, stores input and sets crossing to FALSE. The VI initializes automatically when you first call it

### Zero Crossing

Detects zero crossings of an input signal. The data type you wire to **input** determines the **output** data type.

input

[IMAGE alt='icon' src='nifpga-zero-crossing-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, stores input and sets crossing to FALSE. The VI initializes automatically when you first call it in a VI. input — input is the data point the VI processes. direction — direction is the kind of zero crossing. 0either 1minus-plus 2plus-minus crossing — crossing is TRUE if a zero crossing occurred. |  |
| --- | --- |
| 0 | either |
| 1 | minus-plus |
| 2 | plus-minus |

Parent topic:

Discrete Nonlinear Systems

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/3phasepll/nifpga-3phasepll-vi.html language=enus -->
## TOPIC 00156: 3-Phase PLL

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/3phasepll/nifpga-3phasepll-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/3phasepll/nifpga-3phasepll-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Tracks the phase and frequency of a three-phase signal. This operation is useful for FPGA control applications of a three-phase system. The output phase of the 3-Phase Phase-Locked Loop is in pi radians. To define the Input mode, double-click this Express VI and use the Input mode control to specify

### 3-Phase PLL

Tracks the **phase** and **frequency** of a three-phase signal. This operation is useful for FPGA control applications of a three-phase system. The output **phase** of the 3-Phase Phase-Locked Loop is in pi radians.

To define the **Input mode**, double-click this Express VI and use the **Input mode** control to specify phase value input—**input (phase value)** or line value input—**input (line value)**.

Use this VI in a While Loop.

Note

[IMAGE alt='icon' src='nifpga-3phasepll-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| PLL Configuration | Contains the following options: Input mode— Specifies whether the input is a phase value (a, b, c) or a line value (ab, bc). Reference frequency— Specifies the reference frequency for the loop. The default frequency is 60 Hz. Sampling time (dt)— Specifies the sampling time, or the time interval between two samples. The default time is 100 µs. PI Controller Configuration—Contains the following options: Proportional gain (Kp)— Specifies the proportional gain of the PI controller. Increasing the proportional gain increases the proportional change in the output for a given error value. The default gain is 12. Integral gain (Ki)— Specifies the integral gain of the PI controller. The default gain is 200. Anti-windup gain (Ka)— Specifies the anti-windup gain of the PI controller. Place a checkmark in the Anti-windup? checkbox to enable this option. The default gain is 200. Anti-windup?— Specifies whether the PI controller uses anti-windup gain. This option is enabled by default. Range of Frequency— Contains the following options: High limit— Specifies the high limit of the frequency range. The default is 85 Hz. Low limit— Specifies the low limit of the frequency range. The default is 35 Hz. |
| Fixed-Point Configuration | Contains the following options: Input Type— Specifies the Word length and Integer word length of the input. Output Type— Specifies the Word length and Integer word length of the output. |

#### Inputs/Outputs

| input (phase value) — Specifies that the input of this function is a phase voltage or phase current. Select this input type for a system using a Y connection. a — b — c — reset — Forces the internal states of the integrator to reset to zero when the value is TRUE. anti-windup gain (Ka) — Specifies the anti-windup gain of the PI controller. You must select Anti-windup? in the configuration dialog box to display this input. dt — Specifies the sampling time, or the time interval between two samples. PI gains — Specifies the gains of the PI controller: proportional gain (Kp) — Specifies the proportional gain. integral gain (Ki) — Specifies the integral gain. phase (pi) — Returns the phase of the 3-phase system. phase is in pi radians. cos(phase) — Returns the cosine value of phase. sin(phase) — Returns the sine value of phase. frequency — Returns the frequency of the 3-phase system. |
| --- |
| a — b — c — |
| proportional gain (Kp) — Specifies the proportional gain. integral gain (Ki) — Specifies the integral gain. |

#### Tuning Information

The default values of this Express VI assume a three-phase signal with an amplitude of 1: (Kp, Ki, Ka)=(x, y, z)

For a three-phase signal with an amplitude A, tune the values as follows: (Kp, Ki, Ka)=(x/A, y/A, z/A)

Parent topic:

Control

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-control-filter-m-vi.html language=enus -->
## TOPIC 00157: Discrete Control Filter

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-control-filter-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-control-filter-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a fifth-order low-pass integer FIR filter to the input data. The filter cut-off frequency is 1/10 of the sample frequency of the input. Use the Discrete Control Filter VI to filter measured values, such as the process variable, in control applications. The data type you wire to input determi

### Discrete Control Filter

Applies a fifth-order low-pass integer FIR filter to the input data. The filter cut-off frequency is 1/10 of the sample frequency of the **input**. Use the Discrete Control Filter VI to filter measured values, such as the process variable, in control applications. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 16 bits.

[IMAGE alt='icon' src='nifpga-discrete-control-filter-m-vi.png']

#### Inputs/Outputs

| reset — reset causes LabVIEW to reset the internal filter states to the value of the current input and to pass that value to the output. The VI initializes automatically when it first runs. input — input is a data point from the signal you want to filter. output — output is the filtered result. |
| --- |

The Discrete Control Filter VI uses integer filter coefficients obtained by scaling the coefficients of a floating-point lowpass filter design by a factor of 2<sup>16</sup> and rounding to ensure the filter has a unity gain. The intermediate results are 32 bits wide and do not overflow.

Parent topic:

Discrete Linear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-normalized-integrator-m-vi.html language=enus -->
## TOPIC 00158: Discrete Normalized Integrator

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-normalized-integrator-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-normalized-integrator-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Integrates a discrete input signal using forward Euler integration. The VI assumes that the integration interval (dt) is normalized to 1. The data type you wire to input determines output data type, where output word length is equal to input word length + 16 bits. The maximum input word length is 32

### Discrete Normalized Integrator

Integrates a discrete input signal using forward Euler integration. The VI assumes that the integration interval (dt) is normalized to 1. The data type you wire to **input** determines **output** data type, where output word length is equal to input word length + 16 bits.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-discrete-normalized-integrator-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, returns initial condition as the output. The VI initializes automatically when it first runs in a VI. input — input is the data point the VI processes. initial condition — initial condition is the data point the VI returns the first time you call it or when reset is TRUE. output — output returns the forward integration result. output[n] = input[n – 1] + output[n – 1] where output[n] is the value of output on the nth call to the VI and output[0] = initial condition. |
| --- |

If the **output** exceeds the range of the **output** data type, the result saturates, returning the maximum numeric value representable by the **output** and its data type with the same sign as the actual result.

The Discrete Normalized Integrator VI assumes a sampling interval (dt) of 1 and implements a discrete accumulator. To use the VI as a stand-alone integrator, multiply the **input** or **output** by dt externally or in a host VI. To implement a transfer function from several integrators, you must take the sampling interval into account during the transfer function design phase.

Parent topic:

Discrete Linear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-transfer-function-direct-vi.html language=enus -->
## TOPIC 00159: Discrete Transfer Function Direct

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-transfer-function-direct-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/linear/templates/nifpga-discrete-transfer-function-direct-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a fixed-point transfer function system model on an FPGA. Obtain this model by using the Discrete FP Transfer Function to FXP VI. icon Inputs/Outputs cbool.png reset reset returns the model to its initial conditions. cunkn.png input u(k) input u(k) specifies the input to the model at time

### Discrete Transfer Function Direct

Implements a fixed-point transfer function system model on an FPGA. Obtain this model by using the [Discrete FP Transfer Function to FXP](/csh?context=lvfpga_lvfpgahost_discrete_tf_fp_fxp) VI.

[IMAGE alt='icon' src='nifpga-discrete-transfer-function-direct-vi.png']

#### Inputs/Outputs

| reset — reset returns the model to its initial conditions. input u(k) — input u(k) specifies the input to the model at time k. In a feedback system, u(k) is the difference between the reference input and measurements that a sensor makes on a plant. FXP Transfer Function Model — FXP Transfer Function Model specifies the model this VI implements. Obtain this model by using the Discrete FP Transfer Function to FXP VI. Numerator — Numerator contains the constant coefficients, in ascending order, of a polynomial that represents the numerator of a SISO transfer function. Denominator — Denominator contains the constant coefficients, in ascending order, of a polynomial that represents the denominator of a SISO transfer function. Order — output y(k) — output y(k) returns the output of the model at time k. This output is the value you send to the actuator. |
| --- |
| Numerator — Numerator contains the constant coefficients, in ascending order, of a polynomial that represents the numerator of a SISO transfer function. Denominator — Denominator contains the constant coefficients, in ascending order, of a polynomial that represents the denominator of a SISO transfer function. Order — |

Parent topic:

Discrete Linear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/linear/templates/nifpga-initial-condition-m-vi.html language=enus -->
## TOPIC 00160: Initial Condition

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/linear/templates/nifpga-initial-condition-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/linear/templates/nifpga-initial-condition-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Produces a predefined initial condition immediately after the first time you call or initialize the VI. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRUE, returns initial condition as the ou

### Initial Condition

Produces a predefined initial condition immediately after the first time you call or initialize the VI. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-initial-condition-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, returns initial condition as the output. The VI initializes automatically when it first runs in a VI. input — input is the data point the VI processes. initial condition — initial condition is the data point the VI returns the first time you call it or when reset is TRUE. output — output returns the value of input except the first time you call the VI or when reset is TRUE. output returns the value of initial condition when reset is TRUE. |
| --- |

Parent topic:

Discrete Linear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/linear/templates/nifpga-zero-order-hold-m-vi.html language=enus -->
## TOPIC 00161: Zero-Order Hold

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/linear/templates/nifpga-zero-order-hold-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/linear/templates/nifpga-zero-order-hold-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Samples an input signal and holds it for a specified number of calls to the VI. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRUE, returns initial condition as the output. The VI initializes

### Zero-Order Hold

Samples an input signal and holds it for a specified number of calls to the VI. The data type you wire to **input** determines the **output** data type.

input

[IMAGE alt='icon' src='nifpga-zero-order-hold-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, returns initial condition as the output. The VI initializes automatically when it first runs in a VI. input — input is the data point the VI processes.During the hold time, the VI ignores new input values. hold time in cycles — hold time in cycles determines the number of calls to the VI between updates to output. output — output returns the zero-order hold signal. output is a sampled version of input with a sample interval of hold time in cycles. |
| --- |

Parent topic:

Discrete Linear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/matrixvector/nifpga-matrix-vector-product-vi.html language=enus -->
## TOPIC 00162: Matrix*Vector

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/matrixvector/nifpga-matrix-vector-product-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/matrixvector/nifpga-matrix-vector-product-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Multiplies Matrix A by an input Vector b. This operation is useful for FPGA control applications, such as state-feedback control. You can use more than one multiplier to reduce the latency of this operation. To define Matrix A, double-click this Express VI and use the Matrix Data Initialization page

### Matrix*Vector

Multiplies **Matrix A** by an input **Vector b**. This operation is useful for FPGA control applications, such as state-feedback control. You can use more than one multiplier to reduce the latency of this operation.

To define **Matrix A**, double-click this Express VI and use the **Matrix Data Initialization** page to specify a VI, TXT, or CSV file that contains the matrix data. If you do not define **Matrix A**, this Express VI uses a matrix of zeroes instead.

[IMAGE alt='icon' src='nifpga-matrix-vector-product-vi.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| General | Contains general information about this Express VI. Matrix A Dimensions—Specifies the dimensions of Matrix A. Matrix A rows—Specifies the number of rows in Matrix A. The maximum value is 50 rows. Matrix A columns—Specifies the number of columns in Matrix A. The maximum value is 50 columns. Multiplier Configuration—Specifies information about the multipliers this Express VI uses. Number of multipliers—Specifies the number of multipliers this Express VI uses. Increasing the number of multipliers reduces the latency of this Express VI but increases the amount of FPGA resources this Express VI requires. The default value is one multiplier. The maximum number of multipliers either is the number of Matrix A rows or 25, whichever is smaller. Number of multiplier pipeline stages—Specifies the number of pipelining stages for the multiplier(s). Increasing the number of stages increases the clock rate at which this Express VI can compile but also increases the amount of FPGA resources this Express VI requires. The default is 0 stages, which specifies no pipelining. The maximum is 1 stage. Fixed-Point Configuration—Specifies word lengths and integer word lengths of the elements of Matrix A, Vector b, and Vector c. The configurations you specify determine the value range of these elements. Matrix A Type—Specifies the fixed-point configuration of all elements of Matrix A. Word length—Specifies the word length of each element. Integer word length—Specifies the integer word length of each element. Vector b Type—Specifies the fixed-point configuration of all elements of the input Vector b. Word length—Specifies the word length of each element. Integer word length—Specifies the integer word length of each element. Vector c Type—Specifies the fixed-point configuration of all elements of the output Vector c. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow and rounding errors. By default, this checkbox contains a checkmark and LabVIEW dims the Word length and Integer word length controls. Word length—Specifies the word length of each element. Integer word length—Specifies the integer word length of each element. Overflow mode—Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturate option requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode—Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose might affect the amount of resources this function requires. |
| Matrix Data Initialization | Contains options for specifying the source of data for Matrix A. Initialization method—Specifies the source of data for Matrix A. If you load a matrix that is larger than the Matrix A Dimensions, this Express VI deletes rows and columns that exceed the dimensions. If you load a matrix that is smaller than the Matrix A Dimensions, this Express VI pads the empty cells with zeroes. Choose from the following options: Initialization VI (default)—Populates Matrix A with a 2D array that an initialization VI creates. To create an initialization VI from a template, click the New VI from Template button. Read from TXT file—Populates Matrix A with values from a text (.txt) file. The elements must be separated by tabs, commas, semicolons, or spaces. Read from CSV file—Populates Matrix A with values from a comma-separated values (.csv) file. You can create .csv files by using Microsoft Excel. File path—Specifies a path to the .vi, .txt, or .csv file depending on the Initialization method you specify. New VI from Template—Creates an instance of a template VI, saves the VI to a location you specify, and opens the VI. You can use this template to create an initialization VI. You must close this configuration dialog box to edit the VI. Load—Loads data into Matrix A from the File path you specify and populates the Matrix A table with this data. Matrix Data Preview—Displays Matrix A. Matrix A—Displays the data of Matrix A after you click the Load button. You also can enter data into this table directly. |
| Configuration Feedback | Displays information about how this Express VI executes and other helpful information, such as warnings and errors. |

#### Inputs/Outputs

| Vector b — Specifies the vector this Express VI multiplies by Matrix A. Vector c — Returns Matrix A * Vector b. |
| --- |

Parent topic:

Control

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-backlash-m-vi.html language=enus -->
## TOPIC 00163: Backlash

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-backlash-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-backlash-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a backlash or deadband function. output does not change until input differs from the previous output by at least half of deadband. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRU

### Backlash

Implements a backlash or deadband function. **output** does not change until **input** differs from the previous **output** by at least half of **deadband**. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-backlash-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, uses initial output instead of the previous output to perform the deadband computation. The VI initializes automatically when it first runs in an FPGA VI. input — input is the data point the VI processes. deadband — deadband is an unsigned fixed-point number representing an interval around the previous output. output does not change unless input is outside the deadband interval. initial output — initial output is the value LabVIEW compares to input the first time you call the VI or when reset is TRUE. output — output is the processed data point. If the magnitude of the difference between input and the previous output is greater than half of deadband, output = input – deadband / 2 for input > previous output and output = input + deadband / 2 for input <= previous output Otherwise, output remains unchanged. |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-dead-zone-m-vi.html language=enus -->
## TOPIC 00164: Dead Zone

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-dead-zone-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-dead-zone-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a region of zero output, or a dead zone. output is zero if start of dead zone <= input <= end of dead zone. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cunkn.png input input is the data point the VI processes

### Dead Zone

Provides a region of zero output, or a dead zone. **output** is zero if **start of dead zone** <= **input** <= **end of dead zone**. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-dead-zone-m-vi.png']

#### Inputs/Outputs

| input — input is the data point the VI processes. start of dead zone — start of dead zone specifies the low end of the dead zone. end of dead zone — end of dead zone specifies the high end of the dead zone. output — output is the processed data. output = input – start of dead zone for input < start of dead zone output = input – end of dead zone for input > end of dead zone output = 0 for start of dead zone <= input <= end of dead zone |
| --- |

If the result exceeds the range of the **output** data type, the result saturates, returning the maximum value representable by the data type with the same sign as the actual result.

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-friction-m-vi.html language=enus -->
## TOPIC 00165: Friction

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-friction-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-friction-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a discontinuity at zero with linear behavior elsewhere. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cunkn.png input input is the data point the VI processes. cunkn.png gain gain is the gain to apply to inpu

### Friction

Implements a discontinuity at zero with linear behavior elsewhere. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-friction-m-vi.png']

#### Inputs/Outputs

| input — input is the data point the VI processes. gain — gain is the gain to apply to input. The gain input must not exceed that of a fixed-point <±,16,8> type. Extra fractional bits are coerced to 8 fractional bits at the VI boundary using round-to-nearest-even mode. offset — offset is an integer added to input * gain to determine the value of output. The VI only applies offset when input does not equal zero. output — output is the processed data. output = input * gain + offset for input > 0 output = input * gain – offset for input < 0 output = 0 for input = 0 |
| --- |

If the result exceeds the **output** data type, the result saturates, returning the maximum value representable by the data type with the same sign as the actual result.

The VI truncates the multiplication result before adding the offset.

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-memory-element-m-vi.html language=enus -->
## TOPIC 00166: Memory Element

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-memory-element-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-memory-element-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the input value and returns it on the next call. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRUE, returns initial condition as the output. The VI initializes automatically when it f

### Memory Element

Stores the input value and returns it on the next call. The data type you wire to **input** determines the **output** data type.

input

[IMAGE alt='icon' src='nifpga-memory-element-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, returns initial condition as the output. The VI initializes automatically when it first runs in a VI. input — input is the data point the VI processes. initial condition — initial condition is the data point the VI returns the first time you call it or when reset is TRUE. output — output returns the stored memory element. output[n] = input[n – 1] where output[n] is the value of output on the nth call to the VI after reset, and output[0] = initial condition. |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-rate-limiter-m-vi.html language=enus -->
## TOPIC 00167: Rate Limiter

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-rate-limiter-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-rate-limiter-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a maximum rate of change of a signal. The data type you wire to input determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRUE, passes the current input directly to the output. The VI initializes automatically the first

### Rate Limiter

Specifies a maximum rate of change of a signal. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-rate-limiter-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, passes the current input directly to the output. The VI initializes automatically the first time you call it in a VI. input — input is the data point the VI processes. pos slew rate * dt — pos slew rate * dt is a positive fixed-point number or integer representing the allowable positive change in output between successive calls to the VI. You must precalculate this parameter by multiplying the positive slew rate you want in units/time by dt, which represents the time interval between successive calls to the VI. neg slew rate * dt — neg slew rate * dt is a negative fixed-point number or integer representing the allowable negative change in output between successive calls to the VI. You must precalculate this parameter by multiplying the negative slew rate you want in units/time by dt, which represents the time interval between successive calls to the VI. output — output is the processed data. output equals input if the resulting positive or negative change in output is less than the value of pos slew rate * dt or neg slew rate * dt, respectively. Otherwise, LabVIEW sets output to the previous output plus the positive or negative rate limit. |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-relay-m-vi.html language=enus -->
## TOPIC 00168: Relay

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-relay-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-relay-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Switches between the output when on and output when off inputs. When the relay is on, it remains on until input is less than switch off point. When the relay is off, it remains off until input is greater than switch on point. The relay is off by default. The data type you wire to input determines th

### Relay

Switches between the **output when on** and **output when off** inputs. When the relay is on, it remains on until **input** is less than **switch off point**. When the relay is off, it remains off until **input** is greater than **switch on point**. The relay is off by default. The data type you wire to **input** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-relay-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, turns the relay off unless input is greater than switch on point, in which case output equals output when on. Otherwise, output equals output when off. input — input is the data point the VI processes. switch on point — switch on point is the input threshold above which the relay is on. switch off point — switch off point is the input threshold below which the relay is off. output when on — output when on is the value of output when the relay is on. output when off — output when off is the value of output when the relay is off. output — output is the processed data. output = output when on for input > switch on point and output = output when off for input < switch off point For input values such that switch off point <= input <= switch on point, output is the same as the previous call to the VI. |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-switch-m-vi.html language=enus -->
## TOPIC 00169: Switch

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-switch-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-switch-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Switches between two input values based on the value of control input. The data type you wire to input 1 or input 2 determines the output data type. The maximum input word length is 32 bits. icon Inputs/Outputs cunkn.png input 1 input 1 is the result if control input is greater than threshold. cunkn

### Switch

Switches between two input values based on the value of **control input**. The data type you wire to **input 1** or **input 2** determines the **output** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-switch-m-vi.png']

#### Inputs/Outputs

| input 1 — input 1 is the result if control input is greater than threshold. control input — control input allows you to select between input 1 and input 2. input 2 — input 2 is the result if control input is less than or equal to threshold. threshold — threshold is the setpoint to which LabVIEW compares control input. output — output is the switched result. output = input 1 for control input > threshold output = input 2 for control input <= threshold |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-trigger-m-vi.html language=enus -->
## TOPIC 00170: Trigger

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-trigger-m-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/nonlinear/templates/nifpga-trigger-m-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects changes of the input signal during a control or simulation process. The data type you wire to trigger signal determines the triggered data type. The maximum input word length is 32 bits. icon Inputs/Outputs cbool.png reset reset, when TRUE, sets triggered to FALSE and stores the current trig

### Trigger

Detects changes of the input signal during a control or simulation process. The data type you wire to **trigger signal** determines the **triggered** data type.

The maximum **input** word length is 32 bits.

[IMAGE alt='icon' src='nifpga-trigger-m-vi.png']

#### Inputs/Outputs

| reset — reset, when TRUE, sets triggered to FALSE and stores the current trigger signal. trigger signal — trigger signal is the input signal the VI monitors. trigger type — trigger type determines which changes to trigger signal set triggered to TRUE. You can choose one of the following settings: rising, falling, or either. triggered — triggered is TRUE when the last two trigger signal points meet the conditions described by trigger type. |
| --- |

Parent topic:

Discrete Nonlinear Systems

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/pid/nifpgapid-wrapper-vi.html language=enus -->
## TOPIC 00171: PID

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/pid/nifpgapid-wrapper-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/pid/nifpgapid-wrapper-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications. The PID algorithm features control action range and u

### PID

Implements a [single-precision floating-point](/csh?context=lvfpga_lvfpgaconcepts_fpgasingleprecisfloat) PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.

The PID algorithm features control action range and uses an integrator anti-windup calculation to limit the effect of the integral action during transients. The PID algorithm also features bumpless controller output for PID gain changes.

[IMAGE alt='icon' src='nifpgapid-wrapper-vi.png']

The PID VI calculates the **output**, *u*(*k*), according to the following equations:

[IMAGE alt='image' src='loc_eq_control_output.gif']

[IMAGE alt='image' src='loc_eq_proportional_action.gif']

[IMAGE alt='image' src='loc_eq_integral_action.gif']

[IMAGE alt='image' src='loc_eq_derivative_action.gif']

[IMAGE alt='image' src='loc_eq_error_with_beta.gif']

[IMAGE alt='image' src='loc_eq_error_with_gamma.gif']

where

p

proportional gain

i

integral gain

d

derivative gain

a

filter coefficient

SP

setpoint

beta

proportional weighting

PV

process variable

gamma

derivative weighting

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

- [PID (PID)](../../../../../vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pidwrapper-vi.html) Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.
- [PID](../../../../../vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-piwrapper-vi.html) Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.
- [PID](../../../../../vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pdwrapper-vi.html) Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.

Parent topic:

Control

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pdwrapper-vi.html language=enus -->
## TOPIC 00172: PID

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pdwrapper-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pdwrapper-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications. The PID algorithm features control action range and u

### PID

Implements a [single-precision floating-point](/csh?context=lvfpga_lvfpgaconcepts_fpgasingleprecisfloat) PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.

The PID algorithm features control action range and uses an integrator anti-windup calculation to limit the effect of the integral action during transients. The PID algorithm also features bumpless controller output for PID gain changes.

[IMAGE alt='icon' src='nifpgapid-pdwrapper-vi.png']

#### Inputs/Outputs

| channel (0) — channel specifies the channel that this VI processes. The valid value range is [0, 255]. The default is 0. reset? (F) — reset? specifies whether to reset the internal state of the channel that you specify. The default is FALSE. setpoint — setpoint specifies the value that you want process variable to attain. In equations that define the PID controller, SP represents setpoint. process variable — process variable specifies the value of the variable that you want to control. In equations that define the PID controller, PV represents process variable. manual control — manual control specifies the control mode and the control output value for the manual control mode. manual? (F) — manual? specifies whether to use the automatic or manual control mode. The default is FALSE, which specifies to use the automatic control mode. manual input (0) — manual input specifies the control output value for the manual control mode. The default is 0. gains — gains specifies the PD gain parameters. The gains are without units. proportional gain — proportional gain specifies the normalized proportional gain of the controller. In equations that define the PID controller, Kp represents proportional gain. derivative gain — derivative gain specifies the normalized derivative gain of the controller. In equations that define the PID controller, Kd represents derivative gain. filter coefficient — filter coefficient specifies the derivative lowpass filter coefficient of the controller. The valid value range is [0, 1]. Increasing the value of filter coefficient increases damping of the derivative action. In equations that define the PID controller, a represents filter coefficient. output range — output range specifies the range for the control output value. If the control output value is outside output range, this VI coerces the value to fall within the range and returns the coerced value as the control output value. This VI implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value. output high (Inf) — output high specifies the maximum control output value. The default is Inf. output low (-Inf) — output low specifies the minimum control output value. The default is -Inf. setpoint weighting — setpoint weighting specifies a set of weighting that adjust the error applied to the proportional action and the derivative action. proportional weighting (1) — proportional weighting specifies the relative emphasis of setpoint tracking to disturbance rejection. The valid value range is [0, 1]. The default is 1, which is appropriate for most applications. In equations that define the PID controller, beta represents proportional weighting. derivative weighting (0) — derivative weighting specifies an amount by which to weight the error applied to the derivative action. The default value is 0, which avoids the derivative kick. The valid value range is [0, 1]. In equations that define the PID controller, gamma represents derivative weighting. output — output returns the control output value of the PID algorithm. error — error returns the difference between setpoint and process variable. actions — actions returns the values of the proportional action and the derivative action in the PD algorithm. proportional action — proportional action returns the value of the proportional action. derivative action — derivative action returns the value of the derivative action. |
| --- |
| manual? (F) — manual? specifies whether to use the automatic or manual control mode. The default is FALSE, which specifies to use the automatic control mode. manual input (0) — manual input specifies the control output value for the manual control mode. The default is 0. |
| proportional gain — proportional gain specifies the normalized proportional gain of the controller. In equations that define the PID controller, Kp represents proportional gain. derivative gain — derivative gain specifies the normalized derivative gain of the controller. In equations that define the PID controller, Kd represents derivative gain. filter coefficient — filter coefficient specifies the derivative lowpass filter coefficient of the controller. The valid value range is [0, 1]. Increasing the value of filter coefficient increases damping of the derivative action. In equations that define the PID controller, a represents filter coefficient. |
| output high (Inf) — output high specifies the maximum control output value. The default is Inf. output low (-Inf) — output low specifies the minimum control output value. The default is -Inf. |
| proportional weighting (1) — proportional weighting specifies the relative emphasis of setpoint tracking to disturbance rejection. The valid value range is [0, 1]. The default is 1, which is appropriate for most applications. In equations that define the PID controller, beta represents proportional weighting. derivative weighting (0) — derivative weighting specifies an amount by which to weight the error applied to the derivative action. The default value is 0, which avoids the derivative kick. The valid value range is [0, 1]. In equations that define the PID controller, gamma represents derivative weighting. |
| proportional action — proportional action returns the value of the proportional action. derivative action — derivative action returns the value of the derivative action. |

The PID VI calculates the **output**, *u*(*k*), according to the following equations:

[IMAGE alt='image' src='loc_eq_control_output.gif']

[IMAGE alt='image' src='loc_eq_proportional_action.gif']

[IMAGE alt='image' src='loc_eq_integral_action.gif']

[IMAGE alt='image' src='loc_eq_derivative_action.gif']

[IMAGE alt='image' src='loc_eq_error_with_beta.gif']

[IMAGE alt='image' src='loc_eq_error_with_gamma.gif']

where

p

proportional gain

i

integral gain

d

derivative gain

a

filter coefficient

SP

setpoint

beta

proportional weighting

PV

process variable

gamma

derivative weighting

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

Parent topic:

PID

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pidwrapper-vi.html language=enus -->
## TOPIC 00173: PID (PID)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pidwrapper-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-pidwrapper-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications. The PID algorithm features control action range and u

### PID (PID)

Implements a [single-precision floating-point](/csh?context=lvfpga_lvfpgaconcepts_fpgasingleprecisfloat) PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.

The PID algorithm features control action range and uses an integrator anti-windup calculation to limit the effect of the integral action during transients. The PID algorithm also features bumpless controller output for PID gain changes.

[IMAGE alt='icon' src='nifpgapid-pidwrapper-vi.png']

#### Inputs/Outputs

| channel (0) — channel specifies the channel that this VI processes. The valid value range is [0, 255]. The default is 0. reset? (F) — reset? specifies whether to reset the internal state of the channel that you specify. The default is FALSE. setpoint — setpoint specifies the value that you want process variable to attain. In equations that define the PID controller, SP represents setpoint. process variable — process variable specifies the value of the variable that you want to control. In equations that define the PID controller, PV represents process variable. manual control — manual control specifies the control mode and the control output value for the manual control mode. manual? (F) — manual? specifies whether to use the automatic or manual control mode. The default is FALSE, which specifies to use the automatic control mode. manual input (0) — manual input specifies the control output value for the manual control mode. The default is 0. gains — gains specifies the proportional gain, integral gain, derivative gain, and filter coefficient parameters of the controller. The proportional gain, integral gain, and derivative gain are normalized. Use the Convert PID Gains VI to convert PID gains into the form that gains requires. proportional gain — proportional gain specifies the normalized proportional gain of the controller. In equations that define the PID controller, Kp represents proportional gain. integral gain — integral gain specifies the normalized integral gain of the controller. In equations that define the PID controller, Ki represents integral gain. derivative gain — derivative gain specifies the normalized derivative gain of the controller. In equations that define the PID controller, Kd represents derivative gain. filter coefficient — filter coefficient specifies the derivative lowpass filter coefficient of the controller. The valid value range is [0, 1]. Increasing the value of filter coefficient increases damping of the derivative action. In equations that define the PID controller, a represents filter coefficient. output range — output range specifies the range for the control output value. If the control output value is outside output range, this VI coerces the value to fall within the range and returns the coerced value as the control output value. This VI implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value. output high (Inf) — output high specifies the maximum control output value. The default is Inf. output low (-Inf) — output low specifies the minimum control output value. The default is -Inf. setpoint weighting — setpoint weighting specifies corrections to apply to the error values of the controller. setpoint weighting tunes the proportional action and the derivative action. proportional weighting (1) — proportional weighting specifies the relative emphasis of setpoint tracking to disturbance rejection. The valid value range is [0, 1]. The default is 1, which is appropriate for most applications. In equations that define the PID controller, beta represents proportional weighting. derivative weighting (0) — derivative weighting specifies an amount by which to weight the error applied to the derivative action. The default value is 0, which avoids the derivative kick. The valid value range is [0, 1]. In equations that define the PID controller, gamma represents derivative weighting. output — output returns the control output value of the PID algorithm. error — error returns the difference between setpoint and process variable. actions — actions returns the values of the proportional action, the integral action, and the derivative action in the PID algorithm. proportional action — proportional action returns the value of the proportional action. integral action — integral action returns the value of the integral action. derivative action — derivative action returns the value of the derivative action. |
| --- |
| manual? (F) — manual? specifies whether to use the automatic or manual control mode. The default is FALSE, which specifies to use the automatic control mode. manual input (0) — manual input specifies the control output value for the manual control mode. The default is 0. |
| proportional gain — proportional gain specifies the normalized proportional gain of the controller. In equations that define the PID controller, Kp represents proportional gain. integral gain — integral gain specifies the normalized integral gain of the controller. In equations that define the PID controller, Ki represents integral gain. derivative gain — derivative gain specifies the normalized derivative gain of the controller. In equations that define the PID controller, Kd represents derivative gain. filter coefficient — filter coefficient specifies the derivative lowpass filter coefficient of the controller. The valid value range is [0, 1]. Increasing the value of filter coefficient increases damping of the derivative action. In equations that define the PID controller, a represents filter coefficient. |
| output high (Inf) — output high specifies the maximum control output value. The default is Inf. output low (-Inf) — output low specifies the minimum control output value. The default is -Inf. |
| proportional weighting (1) — proportional weighting specifies the relative emphasis of setpoint tracking to disturbance rejection. The valid value range is [0, 1]. The default is 1, which is appropriate for most applications. In equations that define the PID controller, beta represents proportional weighting. derivative weighting (0) — derivative weighting specifies an amount by which to weight the error applied to the derivative action. The default value is 0, which avoids the derivative kick. The valid value range is [0, 1]. In equations that define the PID controller, gamma represents derivative weighting. |
| proportional action — proportional action returns the value of the proportional action. integral action — integral action returns the value of the integral action. derivative action — derivative action returns the value of the derivative action. |

The PID VI calculates the **output**, *u*(*k*), according to the following equations:

[IMAGE alt='image' src='loc_eq_control_output.gif']

[IMAGE alt='image' src='loc_eq_proportional_action.gif']

[IMAGE alt='image' src='loc_eq_integral_action.gif']

[IMAGE alt='image' src='loc_eq_derivative_action.gif']

[IMAGE alt='image' src='loc_eq_error_with_beta.gif']

[IMAGE alt='image' src='loc_eq_error_with_gamma.gif']

where

p

proportional gain

i

integral gain

d

derivative gain

a

filter coefficient

SP

setpoint

beta

proportional weighting

PV

process variable

gamma

derivative weighting

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

Parent topic:

PID

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-piwrapper-vi.html language=enus -->
## TOPIC 00174: PID

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-piwrapper-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/control/pid/subvis/nifpgapid-piwrapper-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a single-precision floating-point PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications. The PID algorithm features control action range and u

### PID

Implements a [single-precision floating-point](/csh?context=lvfpga_lvfpgaconcepts_fpgasingleprecisfloat) PID algorithm for PID applications with high-speed control and/or high channel count on an FPGA target. You can use this VI to create single-channel, multi-channel, and multi-rate control applications.

The PID algorithm features control action range and uses an integrator anti-windup calculation to limit the effect of the integral action during transients. The PID algorithm also features bumpless controller output for PID gain changes.

[IMAGE alt='icon' src='nifpgapid-piwrapper-vi.png']

#### Inputs/Outputs

| channel (0) — channel specifies the channel that this VI processes. The valid value range is [0, 255]. The default is 0. reset? (F) — reset? specifies whether to reset the internal state of the channel that you specify. The default is FALSE. setpoint — setpoint specifies the value that you want process variable to attain. In equations that define the PID controller, SP represents setpoint. process variable — process variable specifies the value of the variable that you want to control. In equations that define the PID controller, PV represents process variable. manual control — manual control specifies the control mode and the control output value for the manual control mode. manual? (F) — manual? specifies whether to use the automatic or manual control mode. The default is FALSE, which specifies to use the automatic control mode. manual input (0) — manual input specifies the control output value for the manual control mode. The default is 0. gains — gains specifies the PI gain parameters. The gains are without units. proportional gain — proportional gain specifies the normalized proportional gain of the controller. In equations that define the PID controller, Kp represents proportional gain. integral gain — integral gain specifies the normalized integral gain of the controller. In equations that define the PID controller, Ki represents integral gain. output range — output range specifies the range for the control output value. If the control output value is outside output range, this VI coerces the value to fall within the range and returns the coerced value as the control output value. This VI implements integrator anti-windup when the control output is saturated at the specified minimum or maximum value. output high (Inf) — output high specifies the maximum control output value. The default is Inf. output low (-Inf) — output low specifies the minimum control output value. The default is -Inf. proportional weighting (1) — proportional weighting specifies the relative emphasis of setpoint tracking to disturbance rejection. The valid value range is [0, 1]. The default is 1, which is appropriate for most applications. In equations that define the PID controller, beta represents proportional weighting. output — output returns the control output value of the PID algorithm. error — error returns the difference between setpoint and process variable. actions — actions returns the values of the proportional action and the integral action in the PI algorithm. proportional action — proportional action returns the value of the proportional action. integral action — integral action returns the value of the integral action. |
| --- |
| manual? (F) — manual? specifies whether to use the automatic or manual control mode. The default is FALSE, which specifies to use the automatic control mode. manual input (0) — manual input specifies the control output value for the manual control mode. The default is 0. |
| proportional gain — proportional gain specifies the normalized proportional gain of the controller. In equations that define the PID controller, Kp represents proportional gain. integral gain — integral gain specifies the normalized integral gain of the controller. In equations that define the PID controller, Ki represents integral gain. |
| output high (Inf) — output high specifies the maximum control output value. The default is Inf. output low (-Inf) — output low specifies the minimum control output value. The default is -Inf. |
| proportional action — proportional action returns the value of the proportional action. integral action — integral action returns the value of the integral action. |

The PID VI calculates the **output**, *u*(*k*), according to the following equations:

[IMAGE alt='image' src='loc_eq_control_output.gif']

[IMAGE alt='image' src='loc_eq_proportional_action.gif']

[IMAGE alt='image' src='loc_eq_integral_action.gif']

[IMAGE alt='image' src='loc_eq_derivative_action.gif']

[IMAGE alt='image' src='loc_eq_error_with_beta.gif']

[IMAGE alt='image' src='loc_eq_error_with_gamma.gif']

where

p

proportional gain

i

integral gain

d

derivative gain

a

filter coefficient

SP

setpoint

beta

proportional weighting

PV

process variable

gamma

derivative weighting

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

Parent topic:

PID

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/flplib-xnode/nifpgaflplib-xnode.html language=enus -->
## TOPIC 00175: NI Floating-Point Library

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/flplib-xnode/nifpgaflplib-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/flplib-xnode/nifpgaflplib-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Redirects to the LabVIEW Tools Network on ni.com where you can download a library of floating-point math operation functions. You can use these functions in your FPGA application to minimize resource usage outside single-cycle Timed Loops or to optimize timing performance inside 40 MHz single-cycle

### NI Floating-Point Library

Redirects to the LabVIEW Tools Network on ni.com where you can download a library of floating-point math operation functions. You can use these functions in your FPGA application to minimize resource usage outside single-cycle Timed Loops or to optimize timing performance inside 40 MHz single-cycle Timed Loops.

**Accessing the NI Floating-Point Library**

To access the NI Floating-Point library, you must have the [JKI VI Package Manager (VIPM)](/csh?productcategories=147794&context=lvcore_lvhelp_vipm) software installed. When you click **NI Floating-Point Library** on the palette, LabVIEW automatically detects whether the VIPM software is installed and proceeds with the following operations:

- If the VIPM software is installed, LabVIEW launches a VIPM software dialog box that displays detailed information about this library. Click Install or Uninstall to install or uninstall the library.
- If the VIPM software is not installed, LabVIEW launches the NI LabVIEW VIPM Helper dialog box that prompts you to install the VIPM software. After the installation is complete, LabVIEW launches the VIPM software dialog box that displays detailed information about this library. Click Install or Uninstall to install or uninstall the library.

After you install the NI Floating-Point library in the VIPM software, you can access the functions on the [User Libraries](/csh?productcategories=147794&context=lvcore_glang_user_libraries) palette. Refer to the Getting Started with the NI LabVIEW FPGA Floating-Point Library document (Getting_Started_with_the_NI_LabVIEW_FPGA_Floating_Point_Library.pdf), located in the labview\user.lib\_NI FLP Library\documentation folder, for more information about using the functions in this library.

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/butterworth/xnode/butterworthcoefficients-xnode.html language=enus -->
## TOPIC 00176: Butterworth Coefficients

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/butterworth/xnode/butterworthcoefficients-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/butterworth/xnode/butterworthcoefficients-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates filter coefficients for the Butterworth Filter Express VI. Use this VI in a host VI. Large changes to inputs during run time cause invalid states and instability in the Butterworth Filter Express VI. Change the inputs gradually or reset the filter after changing the inputs. icon Dialog Box

### Butterworth Coefficients

Generates filter coefficients for the Butterworth Filter Express VI. Use this VI in a host VI.

Note

[IMAGE alt='icon' src='butterworthcoefficients-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Filter Specifications | Contains the following options: Type—Specifies whether the filter type is Lowpass or Highpass. Cutoff frequency (Hz)—Specifies the cutoff frequency of the filter. The allowable frequency range depends on the Expected sample rate you specify. The normalized cutoff frequency (Cutoff frequency/Expected sample rate) must be less than 0.5, which corresponds to the Nyquist frequency. Expected sample rate (S/s)—Specifies the sample rate, in samples per second, of the input signal. This Express VI uses the rate you specify to calculate the normalized cutoff frequency, which is Cutoff frequency/Expected sample rate. Caution The actual sample rate is specified elsewhere in the FPGA application. If the sample rate changes, you must change the Expected sample rate in this VI. Otherwise, this VI might not behave as expected. Order—Specifies the filter order. You can select 1 (first-order), 2 (second-order), or 4 (fourth-order). |
| Implementation | Contains the following options: Number of channels—Specifies the number of channels to process. The number of channels must match the number of channels specified in the configuration dialog box for corresponding filter Express VI. FPGA clock rate (MHz)—Specifies the clock rate at which the compilation tools compile the FPGA VI. |
| Filter Response | Displays the actual magnitude response of the filter. |

#### Inputs/Outputs

| cutoff frequency (Hz) — Specifies the cutoff frequency of the filter in hertz. The default is 1000 Hz. sample rate (S/s) — Specifies the sampling rate of the signal in samples per second. The default is 50000 S/s. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. channel index — Specifies the index of the channel for the scaled coefficients configuration. This parameter is available only if the Number of channels option is greater than 1. error out — error out contains error information. This output provides standard error out functionality. scaled coefficients — Returns single-channel filter coefficients to load at run time. Scaled coefficients is a fixed-size array of 32-bit signed integers. The size of the array depends on the order you specify. You can select 1 (the array contains two elements), 2 (the array contains three elements), or 4 (the array contains six elements). The filter coefficients must correspond to the filter type and order you specify using the Type and Order options in the Butterworth Filter Express VI. You cannot change the order or type of the filter at run time. configuration — Returns the scaled coefficients to load at run time for the channel index you specify using the channel index element of this cluster. This parameter is available only when you configure the VI such that Number of channels is greater than one. |
| --- |

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/notch/xnode/notchcoefficients-xnode.html language=enus -->
## TOPIC 00177: Notch Coefficients

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/notch/xnode/notchcoefficients-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/notch/xnode/notchcoefficients-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates filter coefficients for the Notch Filter Express VI. Large changes to inputs during run time cause invalid states and instability in the Notch Filter Express VI. Change the inputs gradually or reset the filter after changing the inputs. icon Dialog Box Options Option Description Filter Spe

### Notch Coefficients

Generates filter coefficients for the Notch Filter Express VI.

Note

[IMAGE alt='icon' src='notchcoefficients-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Filter Specifications | Contains the following options: Notch frequency (Hz)—Specifies the center frequency for the notch filter to attenuate. Expected sample rate (S/s)—Specifies the sample rate of the input signal. This Express VI uses the rate you specify to calculate the normalized notch frequency, which is Notch frequency/Expected sample rate. Caution The actual sample rate is specified elsewhere in the FPGA application. If the sample rate changes, you must change the Expected sample rate in this VI. Otherwise, this VI might not behave as expected. Specify quality—Allows you to configure the Q factor of the notch filter. Q factor—Specifies the quality factor of the notch filter. This option is available only when you select Specify quality. Specify bandwidth—Allows you to configure the Notch width (Hz) of the notch filter. Notch width (Hz)—Specifies the 3-dB bandwidth of the filter, which is the frequency range for which the filter attenuates the signal energy by a factor of two or more. This option is available only when you select Specify bandwidth. |
| Implementation | Contains the following options: Number of channels—Specifies the number of channels to process. The number of channels must match the number of channels specified in the configuration dialog box for corresponding filter Express VI. FPGA clock rate (MHz)—Specifies the clock rate at which the compilation tools compile the FPGA VI. |
| Filter Response | Displays the actual magnitude response of the filter. |

#### Inputs/Outputs

| notch frequency (Hz) — Specifies the center frequency for the notch filter to attenuate. The default is 1000 hertz. notch width (Hz) — Specifies the 3-dB bandwidth of the filter, which is the frequency range for which the filter attenuates the signal energy by a factor of two or more. The default is 200 Hz. This option is available only when you select the Specify bandwidth option. Q factor — Specifies the quality factor of the notch filter. The default is 5. This option is available only when you select the Specify quality option. sample rate (S/s) — Specifies the sampling rate of the signal in samples per second. The default is 50000 S/s. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. channel index — Specifies the index of the channel for the scaled coefficients configuration. This parameter is available only if the Number of channels option is greater than 1. scaled coefficients — Returns single-channel filter coefficients to load at run time. Scaled coefficients is a fixed-size array of 32-bit signed integers. The size of the array depends on the order you specify. If the filter order is one, the array contains two elements. If the filter order is two, the array contains three elements. If the filter order is four, the array contains six elements. The filter coefficients must correspond to the filter type and order you specify using the Type and Order options in the Notch Filter Express VI. You cannot alter the order or type of the filter at run time. configuration — Returns the scaled coefficients to load at run time for the channel index you specify using the channel index element of this cluster. This parameter is available only when you configure the VI such that Number of channels is greater than one. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/private/convert-pid-gains-pd-vi.html language=enus -->
## TOPIC 00178: Convert PID Gains

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/private/convert-pid-gains-pd-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/private/convert-pid-gains-pd-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects. icon Inputs/Outputs cu8.png filter coefficient unit (Alpha) filter coefficient unit specifies the unit that distinguishes the type of the derivative lowpass filter coefficients. 0Alp

### Convert PID Gains

Converts PID gains in the [Academic, Parallel, or Series form](/csh?context=lvcore_lvpidmain_pid_topo) to the normalized Parallel form that the [PID](/csh?context=lvfpga_lvfpga_fpga_floating_point_pid) VI expects.

[IMAGE alt='icon' src='convert-pid-gains-pd-vi.png']

#### Inputs/Outputs

| filter coefficient unit (Alpha) — filter coefficient unit specifies the unit that distinguishes the type of the derivative lowpass filter coefficients. 0Alpha (default)—Specifies that the filter coefficients are expressed in Alpha. 1N—Specifies that the filter coefficients are expressed in N. 2Cutoff Frequency—Specifies that the filter coefficients are expressed in hertz. 3Time Constant—Specifies that the filter coefficients are expressed in seconds. filter coefficient (NaN) — filter coefficient specifies the derivative lowpass filter coefficient. If you specify a value for filter coefficient unit, you must also specify a value for filter coefficient. When filter coefficient unit is Alpha, the valid value range of filter coefficient is [0, 1]. When filter coefficient unit is N, the valid value range of filter coefficient is [1, 1000]. The following equations explain the relationships among the available units: N = 1 / Alpha Time Constant = 1 / (2 * Pi * Cutoff Frequency) When you leave both filter coefficient unit and filter coefficient unwired, this VI uses 0.1 for filter coefficient. gains pattern (Parallel) — gains pattern specifies the form of the PD gains. 0Academic—Specifies that the gains are in the Academic form. 1Parallel (default)—Specifies that the gains are in the Parallel form. 2Series—Specifies that the gains are in the Series form. proportional — proportional specifies the value of the proportional gain. derivative — derivative specifies the value of the derivative gain. sampling time — sampling time specifies the loop time, in seconds, at which the PID loop on the FPGA target runs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. proportional unit (Gain (K)) — proportional unit specifies the unit of the proportional gain. The relationship between the available units is K = 100 / PB. 0Gain (K) (default)—Specifies that the proportional gain is expressed in terms of proportional gain (K). 1Band (PB)—Specifies that the proportional gain is expressed in terms of proportional band (PB). derivative unit (s) — derivative unit specifies the units of the derivative gain. 0Hz—Specifies that the derivative gain is expressed in hertz. 1s (default)—Specifies that the derivative gain is expressed in seconds. 2min—Specifies that the derivative gain is expressed in minutes. gains — gains returns the normalized PD gain parameters. proportional gain — proportional gain returns the normalized proportional gain. In equations that define the PID gains conversion, Kp represents proportional gain. derivative gain — derivative gain returns the normalized derivative gain. In equations that define the PID gains conversion, Kd represents derivative gain. filter coefficient — filter coefficient returns the derivative lowpass filter coefficient. In equations that define the PID controller, a represents filter coefficient. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Alpha (default)—Specifies that the filter coefficients are expressed in Alpha. |
| 1 | N—Specifies that the filter coefficients are expressed in N. |
| 2 | Cutoff Frequency—Specifies that the filter coefficients are expressed in hertz. |
| 3 | Time Constant—Specifies that the filter coefficients are expressed in seconds. |
| 0 | Academic—Specifies that the gains are in the Academic form. |
| 1 | Parallel (default)—Specifies that the gains are in the Parallel form. |
| 2 | Series—Specifies that the gains are in the Series form. |
| 0 | Gain (K) (default)—Specifies that the proportional gain is expressed in terms of proportional gain (K). |
| 1 | Band (PB)—Specifies that the proportional gain is expressed in terms of proportional band (PB). |
| 0 | Hz—Specifies that the derivative gain is expressed in hertz. |
| 1 | s (default)—Specifies that the derivative gain is expressed in seconds. |
| 2 | min—Specifies that the derivative gain is expressed in minutes. |
| proportional gain — proportional gain returns the normalized proportional gain. In equations that define the PID gains conversion, Kp represents proportional gain. derivative gain — derivative gain returns the normalized derivative gain. In equations that define the PID gains conversion, Kd represents derivative gain. filter coefficient — filter coefficient returns the derivative lowpass filter coefficient. In equations that define the PID controller, a represents filter coefficient. |  |

Use the following table to understand the details about the equations that the Convert PID Gains VI uses when converting the PID gains. The converted PID gains are *K<sub>p</sub>*, *K<sub>i</sub>*, and *K<sub>d</sub>*, respectively.

| Original PID Form | Original Gains: Units | Conversion Equations |
| --- | --- | --- |
| Academic | Kc: Gain (K) |  |
| Ti: s |  |  |
| Td: s |  |  |
| Parallel | Kp': Gain (K) |  |
| Ki': Hz |  |  |
| Kd': s |  |  |
| Series | KC': Gain (K) |  |
| TI': s |  |  |
| TD': s |  |  |

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

Parent topic:

Convert PID Gains

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/private/convert-pid-gains-pi-vi.html language=enus -->
## TOPIC 00179: Convert PID Gains

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/private/convert-pid-gains-pi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/private/convert-pid-gains-pi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects. icon Inputs/Outputs cu8.png gains pattern (Parallel) gains pattern specifies the form of the PI gains. 0Academic—Specifies that the gains are in the Academic form. 1Parallel (default

### Convert PID Gains

Converts PID gains in the [Academic, Parallel, or Series form](/csh?context=lvcore_lvpidmain_pid_topo) to the normalized Parallel form that the [PID](/csh?context=lvfpga_lvfpga_fpga_floating_point_pid) VI expects.

[IMAGE alt='icon' src='convert-pid-gains-pi-vi.png']

#### Inputs/Outputs

| gains pattern (Parallel) — gains pattern specifies the form of the PI gains. 0Academic—Specifies that the gains are in the Academic form. 1Parallel (default)—Specifies that the gains are in the Parallel form. 2Series—Specifies that the gains are in the Series form. proportional — proportional specifies the value of the proportional gain. integral — integral specifies the value of the integral gain. sampling time — sampling time specifies the loop time, in seconds, at which the PID loop on the FPGA target runs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. proportional unit (Gain (K)) — proportional unit specifies the unit of the proportional gain. The relationship between the available units is K = 100 / PB. 0Gain (K) (default)—Specifies that the proportional gain is expressed in terms of proportional gain (K). 1Band (PB)—Specifies that the proportional gain is expressed in terms of proportional band (PB). integral unit (Hz) — integral unit specifies the units of the integral gain. 0Hz (default)—Specifies that the integral gain is expressed in hertz. 1s—Specifies that the integral gain is expressed in seconds. 2min—Specifies that the integral gain is expressed in minutes. gains — gains returns the normalized PI gain parameters. proportional gain — proportional gain returns the normalized proportional gain. In equations that define the PID gains conversion, Kp represents proportional gain. integral gain — integral gain returns the normalized integral gain. In equations that define the PID gains conversion, Ki represents integral gain. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Academic—Specifies that the gains are in the Academic form. |
| 1 | Parallel (default)—Specifies that the gains are in the Parallel form. |
| 2 | Series—Specifies that the gains are in the Series form. |
| 0 | Gain (K) (default)—Specifies that the proportional gain is expressed in terms of proportional gain (K). |
| 1 | Band (PB)—Specifies that the proportional gain is expressed in terms of proportional band (PB). |
| 0 | Hz (default)—Specifies that the integral gain is expressed in hertz. |
| 1 | s—Specifies that the integral gain is expressed in seconds. |
| 2 | min—Specifies that the integral gain is expressed in minutes. |
| proportional gain — proportional gain returns the normalized proportional gain. In equations that define the PID gains conversion, Kp represents proportional gain. integral gain — integral gain returns the normalized integral gain. In equations that define the PID gains conversion, Ki represents integral gain. |  |

Use the following table to understand the details about the equations that the Convert PID Gains VI uses when converting the PID gains. The converted PID gains are *K<sub>p</sub>*, *K<sub>i</sub>*, and *K<sub>d</sub>*, respectively.

| Original PID Form | Original Gains: Units | Conversion Equations |
| --- | --- | --- |
| Academic | Kc: Gain (K) |  |
| Ti: s |  |  |
| Td: s |  |  |
| Parallel | Kp': Gain (K) |  |
| Ki': Hz |  |  |
| Kd': s |  |  |
| Series | KC': Gain (K) |  |
| TI': s |  |  |
| TD': s |  |  |

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

Parent topic:

Convert PID Gains

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/private/convert-pid-gains-pid-vi.html language=enus -->
## TOPIC 00180: Convert PID Gains (PID)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/private/convert-pid-gains-pid-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/private/convert-pid-gains-pid-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects. icon Inputs/Outputs cu8.png filter coefficient unit (Alpha) filter coefficient unit specifies the unit that distinguishes the type of the derivative lowpass filter coefficients. 0Alp

### Convert PID Gains (PID)

Converts PID gains in the [Academic, Parallel, or Series form](/csh?context=lvcore_lvpidmain_pid_topo) to the normalized Parallel form that the [PID](/csh?context=lvfpga_lvfpga_fpga_floating_point_pid) VI expects.

[IMAGE alt='icon' src='convert-pid-gains-pid-vi.png']

#### Inputs/Outputs

| filter coefficient unit (Alpha) — filter coefficient unit specifies the unit that distinguishes the type of the derivative lowpass filter coefficients. 0Alpha (default)—Specifies that the filter coefficients are expressed in Alpha. 1N—Specifies that the filter coefficients are expressed in N. 2Cutoff Frequency—Specifies that the filter coefficients are expressed in hertz. 3Time Constant—Specifies that the filter coefficients are expressed in seconds. filter coefficient (NaN) — filter coefficient specifies the derivative lowpass filter coefficient. If you specify a value for filter coefficient unit, you must also specify a value for filter coefficient. When filter coefficient unit is Alpha, the valid value range of filter coefficient is [0, 1]. When filter coefficient unit is N, the valid value range of filter coefficient is [1, 1000]. The following equations explain the relationships among the available units: N = 1 / Alpha Time Constant = 1 / (2 * Pi * Cutoff Frequency) When you leave both filter coefficient unit and filter coefficient unwired, this VI uses 0.1 for filter coefficient. gains pattern (Parallel) — gains pattern specifies the form of the PID gains. 0Academic—Specifies that the gains are in the Academic form. 1Parallel (default)—Specifies that the gains are in the Parallel form. 2Series—Specifies that the gains are in the Series form. proportional — proportional specifies the value of the proportional gain. integral — integral specifies the value of the integral gain. derivative — derivative specifies the value of the derivative gain. sampling time — sampling time specifies the loop time, in seconds, at which the PID loop on the FPGA target runs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. proportional unit (Gain (K)) — proportional unit specifies the unit of the proportional gain. The relationship between the available units is K = 100 / PB. 0Gain (K) (default)—Specifies that the proportional gain is expressed in terms of proportional gain (K). 1Band (PB)—Specifies that the proportional gain is expressed in terms of proportional band (PB). integral unit (Hz) — integral unit specifies the units of the integral gain. 0Hz (default)—Specifies that the integral gain is expressed in hertz. 1s—Specifies that the integral gain is expressed in seconds. 2min—Specifies that the integral gain is expressed in minutes. derivative unit (s) — derivative unit specifies the units of the derivative gain. 0Hz—Specifies that the derivative gain is expressed in hertz. 1s (default)—Specifies that the derivative gain is expressed in seconds. 2min—Specifies that the derivative gain is expressed in minutes. gains — gains returns the normalized PID gain parameters. proportional gain — proportional gain returns the normalized proportional gain. In equations that define the PID gains conversion, Kp represents proportional gain. integral gain — integral gain returns the normalized integral gain. In equations that define the PID gains conversion, Ki represents integral gain. derivative gain — derivative gain returns the normalized derivative gain. In equations that define the PID gains conversion, Kd represents derivative gain. filter coefficient — filter coefficient returns the derivative lowpass filter coefficient. In equations that define the PID controller, a represents filter coefficient. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Alpha (default)—Specifies that the filter coefficients are expressed in Alpha. |
| 1 | N—Specifies that the filter coefficients are expressed in N. |
| 2 | Cutoff Frequency—Specifies that the filter coefficients are expressed in hertz. |
| 3 | Time Constant—Specifies that the filter coefficients are expressed in seconds. |
| 0 | Academic—Specifies that the gains are in the Academic form. |
| 1 | Parallel (default)—Specifies that the gains are in the Parallel form. |
| 2 | Series—Specifies that the gains are in the Series form. |
| 0 | Gain (K) (default)—Specifies that the proportional gain is expressed in terms of proportional gain (K). |
| 1 | Band (PB)—Specifies that the proportional gain is expressed in terms of proportional band (PB). |
| 0 | Hz (default)—Specifies that the integral gain is expressed in hertz. |
| 1 | s—Specifies that the integral gain is expressed in seconds. |
| 2 | min—Specifies that the integral gain is expressed in minutes. |
| 0 | Hz—Specifies that the derivative gain is expressed in hertz. |
| 1 | s (default)—Specifies that the derivative gain is expressed in seconds. |
| 2 | min—Specifies that the derivative gain is expressed in minutes. |
| proportional gain — proportional gain returns the normalized proportional gain. In equations that define the PID gains conversion, Kp represents proportional gain. integral gain — integral gain returns the normalized integral gain. In equations that define the PID gains conversion, Ki represents integral gain. derivative gain — derivative gain returns the normalized derivative gain. In equations that define the PID gains conversion, Kd represents derivative gain. filter coefficient — filter coefficient returns the derivative lowpass filter coefficient. In equations that define the PID controller, a represents filter coefficient. |  |

Use the following table to understand the details about the equations that the Convert PID Gains VI uses when converting the PID gains. The converted PID gains are *K<sub>p</sub>*, *K<sub>i</sub>*, and *K<sub>d</sub>*, respectively.

| Original PID Form | Original Gains: Units | Conversion Equations |
| --- | --- | --- |
| Academic | Kc: Gain (K) |  |
| Ti: s |  |  |
| Td: s |  |  |
| Parallel | Kp': Gain (K) |  |
| Ki': Hz |  |  |
| Kd': s |  |  |
| Series | KC': Gain (K) |  |
| TI': s |  |  |
| TD': s |  |  |

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

Parent topic:

Convert PID Gains

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ms-vi.html language=enus -->
## TOPIC 00181: Sample Rate To Loop Time (ms)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ms-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ms-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs. icon Inputs/Outputs cdbl.png FPGA clock rate (Hz) FPGA clock rate (Hz) specifies the clock rate at which the compilation tools compile the F

### Sample Rate To Loop Time (ms)

Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.

[IMAGE alt='icon' src='sample-rate-to-loop-time-ms-vi.png']

#### Inputs/Outputs

| FPGA clock rate (Hz) — FPGA clock rate (Hz) specifies the clock rate at which the compilation tools compile the FPGA VI. sample rate (S/s) — sample rate (S/s) specifies the sampling rate for the signal in samples per second. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. count (ms/S) — count (ms/S) returns the time between loop iterations in milliseconds. actual sample rate (S/s) — actual sample rate (S/s) returns the achievable sampling rate based on FPGA clock rate (Hz). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sample Rate To Loop Time

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ticks-vi.html language=enus -->
## TOPIC 00182: Sample Rate To Loop Time (ticks)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ticks-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ticks-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs. icon Inputs/Outputs cdbl.png FPGA clock rate (Hz) FPGA clock rate (Hz) specifies the clock rate at which the compilation tools compile the F

### Sample Rate To Loop Time (ticks)

Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.

[IMAGE alt='icon' src='sample-rate-to-loop-time-ticks-vi.png']

#### Inputs/Outputs

| FPGA clock rate (Hz) — FPGA clock rate (Hz) specifies the clock rate at which the compilation tools compile the FPGA VI. sample rate (S/s) — sample rate (S/s) specifies the sampling rate for the signal in samples per second. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. count (ticks/S) — count (ticks/S) returns the time between loop iterations in units of clock cycles. The clock rate for the FPGA VI determines the length of time between iterations. actual sample rate (S/s) — actual sample rate (S/s) returns the achievable sampling rate based on FPGA clock rate (Hz). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sample Rate To Loop Time

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-us-vi.html language=enus -->
## TOPIC 00183: Sample Rate To Loop Time (us)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-us-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-us-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs. icon Inputs/Outputs cdbl.png FPGA clock rate (Hz) FPGA clock rate (Hz) specifies the clock rate at which the compilation tools compile the F

### Sample Rate To Loop Time (us)

Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.

[IMAGE alt='icon' src='sample-rate-to-loop-time-us-vi.png']

#### Inputs/Outputs

| FPGA clock rate (Hz) — FPGA clock rate (Hz) specifies the clock rate at which the compilation tools compile the FPGA VI. sample rate (S/s) — sample rate (S/s) specifies the sampling rate for the signal in samples per second. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. count (us/S) — count (us/S) returns the time between loop iterations in microseconds. actual sample rate (S/s) — actual sample rate (S/s) returns the achievable sampling rate based on FPGA clock rate (Hz). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sample Rate To Loop Time

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/public/convert-pid-gains-vi.html language=enus -->
## TOPIC 00184: Convert PID Gains

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/public/convert-pid-gains-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/public/convert-pid-gains-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects. icon Use the following table to understand the details about the equations that the Convert PID Gains VI uses when converting the PID gains. The converted PID gains are K[p], K[i], a

### Convert PID Gains

Converts PID gains in the [Academic, Parallel, or Series form](/csh?context=lvcore_lvpidmain_pid_topo) to the normalized Parallel form that the [PID](/csh?context=lvfpga_lvfpga_fpga_floating_point_pid) VI expects.

[IMAGE alt='icon' src='convert-pid-gains-vi.png']

Use the following table to understand the details about the equations that the Convert PID Gains VI uses when converting the PID gains. The converted PID gains are *K<sub>p</sub>*, *K<sub>i</sub>*, and *K<sub>d</sub>*, respectively.

| Original PID Form | Original Gains: Units | Conversion Equations |
| --- | --- | --- |
| Academic | Kc: Gain (K) |  |
| Ti: s |  |  |
| Td: s |  |  |
| Parallel | Kp': Gain (K) |  |
| Ki': Hz |  |  |
| Kd': s |  |  |
| Series | KC': Gain (K) |  |
| TI': s |  |  |
| TD': s |  |  |

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Channel PID\Multi-Channel PID.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Floating-point PID\Multi-Rate PID\Multi-Rate PID.lvproj

- [Convert PID Gains (PID)](../../../../../vi-lib/rvi/analysis/host/private/convert-pid-gains-pid-vi.html) Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects.
- [Convert PID Gains](../../../../../vi-lib/rvi/analysis/host/private/convert-pid-gains-pi-vi.html) Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects.
- [Convert PID Gains](../../../../../vi-lib/rvi/analysis/host/private/convert-pid-gains-pd-vi.html) Converts PID gains in the Academic, Parallel, or Series form to the normalized Parallel form that the PID VI expects.

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/public/discrete-fp-transfer-function-to-fxp-vi.html language=enus -->
## TOPIC 00185: Discrete FP Transfer Function to FXP

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/public/discrete-fp-transfer-function-to-fxp-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/public/discrete-fp-transfer-function-to-fxp-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a transfer function system model from floating-point to fixed-point representation. Obtain this model by entering values into the FP Transfer Function Model control or by using the VIs included with the LabVIEW Control Design & Simulation Module. You then can implement this model on an FPGA

### Discrete FP Transfer Function to FXP

Converts a transfer function system model from floating-point to fixed-point representation. Obtain this model by entering values into the **FP Transfer Function Model** control or by using the VIs included with the LabVIEW Control Design & Simulation Module.

You then can implement this model on an FPGA by using the [Discrete Transfer Function Direct](../../control/linear/templates/nifpga-discrete-transfer-function-direct-vi.html) VI.

[IMAGE alt='icon' src='discrete-fp-transfer-function-to-fxp-vi.png']

#### Inputs/Outputs

| FP Transfer Function Model — FP Transfer Function Model specifies the floating-point transfer function controller model this VI converts to fixed-point representation. The model you wire to this terminal must meet the following requirements: The model must be in transfer function form. If the model is in zero-pole-gain or state-space form, use the Model Conversion VIs to convert the model to transfer function form. These VIs are available with the LabVIEW Control Design & Simulation Module. The order of the denominator must be less than or equal to eight. The transfer function must be proper; that is, the order of the denominator must be greater than or equal to the order of the numerator. The model must be in the simulation data type. If you created the model with the LabVIEW Control Design & Simulation Module, you must use the CD Convert Control Design to Simulation VI to convert the model to the simulation data type. The model must be discrete. If the model is continuous, use the CD Convert Continuous to Discrete VI, available with the Control & Simulation Module, to discretize the model. The sampling time of the discrete model must match the execution rate of the FPGA. To calculate the proper sampling time and FPGA execution rate, take the following factors into account: The rate at which the controller accepts input u(k) from a sensor The rate at which the actuator accepts input y(k) from the controller Ideally, these rates will be equal. In this situation, set the sampling time of the model and the FPGA execution rate to this rate. For example, if the controller accepts input at 1 kHz and the actuator accepts the controller output at 1 kHz, set the sampling time of the model to 1/1,000 or 0.001 s. Set the FPGA execution rate to 1 kHz. If these two rates are different, set the sampling time and FPGA execution rate to the faster of these two rates. For example, if the controller accepts input at 1 kHz but the actuator accepts the controller output at 2 kHz, set the sampling time to 1/2,000 or 0.0005 s. Set the FPGA execution rate to 2 kHz. Numerator — Numerator is a one-dimensional array representing the coefficients of the numerator polynomial. Denominator — Denominator is a one-dimensional array representing the coefficients of the denominator polynomial. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. FXP Transfer Function Model — FXP Transfer Function Model returns the FP Transfer Function Model in fixed-point representation. Wire this output to the FXP Transfer Function Model input of the Discrete Transfer Function Direct VI. Each element of FXP Transfer Function Model has a data type of <+/–, 32, 12>. You can change this data type, but before doing so you must right-click this indicator and select Disconnect from Type Def. from the shortcut menu. Numerator — Numerator contains the constant coefficients, in ascending order, of a polynomial that represents the numerator of a SISO transfer function. Denominator — Denominator contains the constant coefficients, in ascending order, of a polynomial that represents the denominator of a SISO transfer function. Order — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Numerator — Numerator is a one-dimensional array representing the coefficients of the numerator polynomial. Denominator — Denominator is a one-dimensional array representing the coefficients of the denominator polynomial. |
| Numerator — Numerator contains the constant coefficients, in ascending order, of a polynomial that represents the numerator of a SISO transfer function. Denominator — Denominator contains the constant coefficients, in ascending order, of a polynomial that represents the denominator of a SISO transfer function. Order — |

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/public/fft-to-spectrum-vi.html language=enus -->
## TOPIC 00186: FFT to Spectrum

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/public/fft-to-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/public/fft-to-spectrum-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the output of the Fast Fourier Transform (FFT) Express VI to a power or amplitude spectrum. The spectrum is single-sided and scaled. icon Inputs/Outputs c1ddbl.png real FFT data real FFT data specifies the real data to convert to the spectrum. c1ddbl.png imaginary FFT data imaginary FFT dat

### FFT to Spectrum

Converts the output of the Fast Fourier Transform ([FFT](/csh?context=lvfpga_lvfpga_fpga_fft)) Express VI to a power or amplitude spectrum. The spectrum is single-sided and scaled.

[IMAGE alt='icon' src='fft-to-spectrum-vi.png']

#### Inputs/Outputs

| real FFT data — real FFT data specifies the real data to convert to the spectrum. imaginary FFT data — imaginary FFT data specifies the imaginary data to convert to the spectrum. spectrum type — spectrum type specifies whether the output spectrum is an amplitude or power spectrum. The default is Power (Vrms^2). 0Power (Vrms^2) 1Amplitude (Vrms) sample rate (S/s) — sample rate (S/s) specifies the sampling rate, in samples per second, for the FFT. Use the actual sample rate (S/s) output from the Sample Rate To Loop Time VI to obtain the sampling rate. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. spectrum out — spectrum out contains the power or amplitude spectrum corresponding to spectrum type. spectrum out is single-sided and scaled. df (Hz) — df (Hz) returns the frequency resolution of the spectrum in hertz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Power (Vrms^2) |
| 1 | Amplitude (Vrms) |

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/public/normalize-signal-generation-parameters-vi.html language=enus -->
## TOPIC 00187: Normalize Signal Generation Parameters

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/public/normalize-signal-generation-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/public/normalize-signal-generation-parameters-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts frequency, phase, and duty cycle parameters into fixed-point units normalized to the clock rate. Use the Normalize Signal Generation Parameters VI in a host VI to convert values for the following FPGA VIs: Sine Wave Generator and Square Wave Generator. icon Inputs/Outputs cdbl.png FPGA cloc

### Normalize Signal Generation Parameters

Converts frequency, phase, and duty cycle parameters into fixed-point units normalized to the clock rate. Use the Normalize Signal Generation Parameters VI in a host VI to convert values for the following FPGA VIs: Sine Wave Generator and Square Wave Generator.

[IMAGE alt='icon' src='normalize-signal-generation-parameters-vi.png']

#### Inputs/Outputs

| FPGA clock rate (Hz) — FPGA clock rate (Hz) specifies the clock rate at which the compilation tools compile the FPGA VI. frequency (Hz) — frequency (Hz) specifies the frequency of the generated signal in hertz. phase offset (deg) — phase offset (deg) specifies the phase in degrees. duty cycle (%) — duty cycle (%) specifies the percentage of time the square wave remains high over one period. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. frequency (periods/tick) — frequency (periods/tick) returns the scaled frequency, in number of periods per clock cycle, of the FPGA clock. This value is an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. phase offset (periods) — phase offset (periods) returns the scaled phase offset in number of periods. This value is an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. duty cycle (periods) — duty cycle (periods) returns the scaled duty cycle in number of periods. This value is an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. actual frequency (Hz) — actual phase offset (deg) — |
| --- |

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/public/sample-rate-to-loop-time-vi.html language=enus -->
## TOPIC 00188: Sample Rate To Loop Time

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/public/sample-rate-to-loop-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/public/sample-rate-to-loop-time-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs. icon

### Sample Rate To Loop Time

Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.

[IMAGE alt='icon' src='sample-rate-to-loop-time-vi.png']

- [Sample Rate To Loop Time (ticks)](../../../../../vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ticks-vi.html) Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.
- [Sample Rate To Loop Time (us)](../../../../../vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-us-vi.html) Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.
- [Sample Rate To Loop Time (ms)](../../../../../vi-lib/rvi/analysis/host/private/sample-rate-to-loop-time-ms-vi.html) Converts the desired sample rate to the appropriate count for the Loop Timer Express VI and computes the achievable sample rate for use with other Scaling VIs.

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/host/public/scale-period-vi.html language=enus -->
## TOPIC 00189: Scale Period

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/host/public/scale-period-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/host/public/scale-period-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the period output, expressed in samples, from the Analog Period Measurement Express VI to a period in units of seconds using the sample rate you specify. This VI also returns the frequency of the measurement in hertz using the sample rate you specify. Use the Scale Period VI in a host VI. i

### Scale Period

Converts the period output, expressed in samples, from the [Analog Period Measurement](/csh?context=lvfpga_lvfpga_fpga_period_measurement) Express VI to a period in units of seconds using the sample rate you specify. This VI also returns the frequency of the measurement in hertz using the sample rate you specify. Use the Scale Period VI in a host VI.

[IMAGE alt='icon' src='scale-period-vi.png']

#### Inputs/Outputs

| period (S) — period (S) specifies the measured period in units of samples. period (S) is an unsigned fixed-point number with a word length of 32 bits and an integer word length of 16 bits. period (S) does not include an overflow status. sample rate (S/s) — sample rate (S/s) specifies the sampling rate for the analog period measurement. Use the actual sample rate (S/s) output from the Sample Rate To Loop Time VI to obtain the sampling rate. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. period (s) — period (s) returns the period in units of seconds. frequency (Hz) — frequency (Hz) returns the frequency in units of hertz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scaling

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/butterworth/xnode/nifpgabutterworthfilter-xnode.html language=enus -->
## TOPIC 00190: Butterworth Filter

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/butterworth/xnode/nifpgabutterworthfilter-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/butterworth/xnode/nifpgabutterworthfilter-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters one or more input signals using a lowpass or highpass IIR Butterworth filter. The filter can be of order 1, 2, or 4. You can use the Butterworth Coefficients Express VI to generate the set of filter coefficients during run time. icon Dialog Box Options Parameter Description Filter Specificat

### Butterworth Filter

Filters one or more input signals using a lowpass or highpass IIR Butterworth filter.

You can use the [Butterworth Coefficients](../../../host/butterworth/xnode/butterworthcoefficients-xnode.html) Express VI to generate the set of filter coefficients during run time.

[IMAGE alt='icon' src='nifpgabutterworthfilter-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Filter Specifications | Contains the following options: Type—Specifies whether the filter type is Lowpass or Highpass. Order—Specifies the filter order. You can select 1 (first-order), 2 (second-order), or 4 (fourth-order). Expected sample rate (S/s)—Specifies the sample rate, in samples per second, of the input signal. This Express VI uses the rate you specify to calculate the normalized cutoff frequency, which is Cutoff frequency/Expected sample rate. Caution The actual sample rate is specified elsewhere in the FPGA application. If the sample rate changes, you must change the Expected sample rate in this VI. Otherwise, this VI might not behave as expected. Cutoff frequency (Hz)—Specifies the cutoff frequency of the filter. The allowable frequency range depends on the Expected sample rate you specify. The normalized cutoff frequency (Cutoff frequency/Expected sample rate) must be less than 0.5, which corresponds to the Nyquist frequency. |
| Output Data Type | Contains the following options: Avoid overflow—Specifies that the word length and integer word length of the output data type are large enough to ensure that the filter output does not overflow. Same as input—Specifies that the output data type is the same as the input data type. The output will saturate if the output range is exceeded during signal transients. Overflow will not occur with a steady-state sinusoidal input. |
| Implementation | Contains the following options: Number of channels—Specifies the number of channels of input data to process.The calling VI must supply a sequential channel scan to input data on successive calls to this Express VI. The channel order must be fixed. FPGA clock rate (MHz)—Specifies the clock rate at which LabVIEW compiles the FPGA VI. If the FPGA clock rate parameter does not match the top-level clock rate, the Code Generation Errors window returns an error when you compile the FPGA VI. Use the Top-Level Clock FPGA Target Properties page to change the top-level clock rate. |
| Filter Response | Displays the actual magnitude response of the filter. |

#### Inputs/Outputs

| input data — Specifies the input signal to filter.input data is a fixed-point number or integer with a maximum word length of 32 bits. reset — Resets the filter state of the input data channel to zero if TRUE. Resetting the filter state does not reset the filter coefficients. This Express VI resets automatically the first time you call it. scaled coefficients — Specifies single-channel filter coefficients to load at run time.Scaled coefficients is a fixed-size array of 32-bit signed integers. The size of the array depends on the order you specify. If the filter order is one, the array contains two elements. If the filter order is two, the array contains three elements. If the filter order is four, the array contains six elements. The filter coefficients must correspond to the filter type and order you specify using the Type and Order options. You cannot alter the order or type of the filter at run time. This parameter is available only when you configure the VI for single-channel input in the configuration dialog box. configuration — Specifies the scaled coefficients to load at run time for the channel index you specify using the channel index element of this cluster. This Express VI continues to use either the default coefficients or the last coefficients you specified for the channel until you specify new coefficients. This parameter is available only when you configure the VI for multi-channel input in the configuration dialog box. output data — Returns the filtered signal corresponding to the input data channel. |
| --- |

Refer to the [support document](https://www.ni.com/r/exbpmj) at ni.com for more information about the accuracy of the FPGA Math and Analysis VIs.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Butterworth Filter\Butterworth Filter.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Butterworth Filter\Butterworth Filter.lvproj

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/dc-rms/xnode/nifpgadc-rms-xnode.html language=enus -->
## TOPIC 00191: DC and RMS Measurements

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/dc-rms/xnode/nifpgadc-rms-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/dc-rms/xnode/nifpgadc-rms-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the DC (mean) and/or RMS values of an input signal. You also can use this Express VI to calculate the intermediate sum, mean square, or square sum values in order to save FPGA resources. This Express VI accepts frames of data, performs measurement on the input data, and returns a valid si

### DC and RMS Measurements

Calculates the DC (mean) and/or RMS values of an input signal. You also can use this Express VI to calculate the intermediate sum, mean square, or square sum values in order to save FPGA resources. This Express VI accepts frames of data, performs measurement on the input data, and returns a valid single result for each frame.

[IMAGE alt='icon' src='nifpgadc-rms-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Measurement Time Setup | Contains the following options: Measurement time (s)—Specifies the measurement time (averaging time) in seconds for the Measurements you select. This Express VI always coerces the Measurement time (s) so it corresponds to an integer Actual number of measurement samples. Actual number of measurement samples—Specifies the number of samples used to calculate the Measurements you select.If you want to save resources on the FPGA, enter a value that is a power of two for the Actual number of measurement samples. Expected sample rate (S/s)— Specifies the sample rate of the input signal. Caution The actual sample rate is specified elsewhere in the FPGA application. If the sample rate changes, you must change the Expected sample rate in this Express VI. Otherwise, this Express VI might not behave as expected. |
| Windowing | Contains the following options: Apply Hanning window—Specifies whether to apply a Hanning window to the input signal before calculating the measurement results. Selecting this option can reduce spectral leakage and achieve more accurate and stable results if the input signal contains periodic components. If you select this option, you cannot select the Square Sum measurement. |
| Execution Mode | Contains the following options: Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Latency—Displays the number of cycles between the last point in the input frame and the valid output, which is a single point. Latency is available only when you select Inside single-cycle Timed Loop. |
| Measurements | Contains the following options: DC (Mean)—Specifies whether to return the DC value of the input signal. Sum—Specifies whether to return the sum of the input signals. RMS—Specifies whether to return the RMS (Root Mean Square) value of the input signal. Mean Square—Specifies whether to return the mean value of the squares of the input signals. Square Sum—Specifies whether to return the sum of the squares of the input samples. You cannot select this option if you place a checkmark in the Apply Hanning window checkbox. |

#### Inputs/Outputs

| input data — Specifies the input signal to measure. input data is a fixed-point number or integer with a maximum word length of either 32 bits if signed or 31 bits if unsigned. reset — Clears all internal states when this signal is TRUE. Outside the single-cycle Timed Loop, this Express VI clears all internal states on the same call that reset is TRUE. Inside the single-cycle Timed Loop, this Express VI clears all internal states on the first cycle that reset is FALSE after reset is TRUE. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. DC — Returns the DC value of the input signal. sum — Returns the sum of the input signals. square sum — Returns the sum of the squares of the input signals. RMS — Returns the root mean square value of the input signal. mean square — Returns the mean value of the squares of the input signals. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. After returning TRUE for the previous output frame, output valid returns FALSE and waits for the next frame to complete. Wire output valid to input valid of a downstream node to transfer data from this Express VI to a downstream node. To display output valid, select the Inside single-cycle Timed Loop option in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

Refer to the [support document](https://www.ni.com/r/exbpmj) at ni.com for more information about the accuracy of the DC and RMS Measurements VI.

DC and RMS measurements contain common [error sources](/csh?context=lvfpga_lvanlsconcepts_dc_rms_error_sources).

#### Conserving FPGA Resources

The DC and RMS Express VI can calculate the [DC](/csh?context=lvfpga_lvanlsconcepts_what_is_dc_level) and [RMS](/csh?context=lvfpga_lvanlsconcepts_what_is_rms_level) values of an input signal. However, some of the operations for the calculation require significant FPGA resources. You can save FPGA resources by splitting the operations into two groups that run on the FPGA VI and the host VI, respectively. In the following calculations, you can perform the operations in blue on the host.

DC = Sum/Actual number of measurement samples

RMS = sqrt(Mean square)

RMS = sqrt(Square Sum/Actual number of measurement samples)

You also can save FPGA resources if **Actual number of measurement samples** is a power of two.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\DC and RMS Measurement\DC and RMS Measurement.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\DC and RMS Measurement\DC and RMS Measurement.lvproj

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/fft/xnode/nifpgafft-xnode.html language=enus -->
## TOPIC 00192: FFT

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/fft/xnode/nifpgafft-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/fft/xnode/nifpgafft-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the Fast Fourier Transform (FFT). The Single Channel, Single Sample input format computes the FFT point by point. The Single Channel, Multiple Samples input format allows you to perform FFT analysis on a data stream with multiple samples/cycle. You can use the Single Channel, Single Sample

### FFT

Computes the Fast Fourier Transform (FFT). The **Single Channel, Single Sample** input format computes the FFT point by point. The **Single Channel, Multiple Samples** input format allows you to perform FFT analysis on a data stream with multiple samples/cycle.

You can use the **Single Channel, Single Sample** input format of this Express VI after you use the [Scaled Window Express VI](../../window/xnode/nifpga-scaled-window-xnode.html) to minimize spectral leakage associated with truncated waveforms. You can also use the [FFT to Spectrum](../../../host/public/fft-to-spectrum-vi.html) VI to convert the output of this Express VI to an amplitude or power spectrum if you use the **Single Channel, Single Sample** input format.

[IMAGE alt='icon' src='nifpgafft-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Input Format | Contains the following options: Single Channel, Single Sample—Select this option when each input is one sample from one channel. Single Channel, Multiple Samples—Select this option when you want to process multiple samples from one channel during each clock cycle. When you select this option, real data in, imaginary data in, real data out, and imaginary data out are arrays, with each element representing one sample. These inputs support array sizes of 2, 4, 8, and 16.If you use hardware that sends multiple samples per data clock cycle, the Single Channel, Multiple Samples input format allows you to process the data directly from the FPGA I/O node. If you do not use the I/O module, you can use this option to achieve much higher data throughput compared with the Single Channel, Single Sample input format. Note Selecting the Single Channel, Multiple Samples input format consumes significantly more FPGA resources compared with the Single Channel, Single Sample input format. If your compilation fails because of insufficient resources on the FPGA target, consider using an FPGA target with greater resources. |
| Transform Parameters | Contains the following options: FFT size—Specifies the length of the transform that this Express VI calculates. When you select Single Channel, Single Sample in the Input Format section, valid options are powers of two between 8 and 8,192. When you select Single Channel, Multiple Samples in the Input Format section, valid options are powers of two between 8 and 65,536. The default is 64. Direction—Specifies whether to calculate a forward FFT or inverse FFT. |
| Output Data Type | Contains the following options: Adapt to source— Specifies whether this Express VI decides the output data type. Disable the Adapt to source checkbox if you want to use Word length to determine the output data type. Word length—Specifies any output word length in the range of [8, 32]. Word length is available only if you deselect the Adapt to source checkbox. Word length must be between the input word length and 32 if the input is signed. Word length must be between the input word length + 1 and 32 if the input is unsigned. The data you wire to real data in determines the input word length. Tip Decreasing the value of Word length conserves FPGA resources but reduces precision. NI recommends that you simulate a given configuration to ensure that the precision you achieve meets your FPGA resource and timing needs. Integer word length—Indicates the output integer word length that this Express VI calculates. |
| Execution Mode | Contains the following options: Outside single-cycle Timed Loop— Select this option when you use this Express VI outside of a single-cycle Timed Loop. This option is available only when you select Single Channel, Single Sample in the Input Format section. Using this Express VI outside the single-cycle Timed Loop produces a latency of two times the Length, meaning that it takes two times Length calls to this Express VI before this Express VI returns a valid output. After the initial latency, this Express VI returns a valid output every time LabVIEW calls this Express VI. Inside single-cycle Timed Loop—Select this option when you use this Express VI inside a single-cycle Timed Loop. Selecting Inside single-cycle Timed Loop enables the Throughput option. When you execute this Express VI inside the single-cycle Timed Loop, you can use handshaking signals to schedule the timing of data. Throughput—Specifies the minimum number of cycles between two successive input data. This option is available only if you select Single Channel, Single Sample and select Inside single-cycle Timed Loop. If you select Single Channel, Single Sample and select Outside single-cycle Timed Loop, LabVIEW sets the throughput to 1 call / input, which means this Express VI can accept data every time it is called. If you select Single Channel, Multiple Samples, LabVIEW sets the throughput to 1 cycle / input, which means this Express VI can accept new data every cycle. Tip Increasing the throughput consumes many more FPGA resources. Select 1 cycle / input only if you need higher throughput. Latency—Displays the number of cycles between the first point in the input frame and the first point in the valid output frame. Clock rate—Specifies the level of pipelining stages this Express VI uses internally. Increasing the number of stages increases the clock rate at which this Express VI can compile for both Inside the single-cycle Timed Loop and Outside the single-cycle Timed Loop. This option does not set the clock rate explicitly. Note Adjusting the value of Clock rate increases the FPGA resource usage and latency of this Express VI. An increased latency indicates that this Express VI takes longer to return a valid result. The value for Clock rate is High if you select Single Channel, Multiple Samples in the Input Format section. |
| Implementation Goal | Specifies whether this Express VI optimizes the accuracy of the FFT results or the resource usage on the FPGA target. This option is available only when you select Single Channel, Multiple Samples in the Input Format section and select Adapt to Source in the Output Data Type section. When you deselect Adapt to Source, you may select only Accuracy and the output word length you configure determines the accuracy and FPGA resource usage. Contains the following options: Accuracy—Select this option when you want the last bits of output data to be more accurate at the cost of increased FPGA resource usage. The default is Accuracy. Resource usage—Select this option when you want to reduce FPGA resource use at the cost of less accurate results. Note NI recommends that you select Resource usage when the input contains 16 samples per cycle and the FFT length is 16384, 32768, or 65536. Selecting Accuracy when the input contains 16 samples per cycle and the FFT length is 16384, 32768, or 65536 results in large FPGA resource requirements. |
| Input/Output Index Pattern | Specifies the intervals of the indexes in the FFT frame for the input and output data. The image below Input/Output Index Pattern represents the configuration you selected. Contains the following options: Continuous input indexes / continuous output indexes—Select this option when you want the indexes in the FFT frame to be continuous for both the input data and the output data. This option is available only when you select Single Channel, Single Sample in the Input Format section. Continuous input indexes / M-interval output indexes—Select this option when you want the indexes in the FFT frame to be continuous for the input data and the indexes in the FFT frame to have intervals of M for the output data, where M=FFT size/Number of samples per input. This option is available only when you select Single Channel, Multiple Samples in the Input Format section. Note If the data source of an FFT Express VI originates from another FFT Express VI, such as when performing inverse FFT on FFT results, ensure that the input pattern of the second FFT Express VI is the same as the output pattern of the first FFT Express VI. Otherwise, the FFT results will be inaccurate. M-interval input indexes / continuous output indexes—Select this option when you want the indexes in the FFT frame to have intervals of M for the input data, where M=FFT size/Number of samples per input, and the indexes in the FFT frame to be continuous for the output data. This option is available only when you select Single Channel, Multiple Samples in the Input Format section. Note If the data source of an FFT Express VI originates from another FFT Express VI, such as when performing inverse FFT on FFT results, ensure that the input pattern of the second FFT Express VI is the same as the output pattern of the first FFT Express VI. Otherwise, the FFT results will be inaccurate. |
| Configuration Feedback | Displays information about how this Express VI executes and other helpful information, such as warnings and error. |

#### Inputs/Outputs

| real data in — Specifies the real part of the input signal. Input data is a fixed-point number with a maximum word length of 24 bits or a 1D array of fixed-point numbers with maximum word lengths of 24 bits. imaginary data in — Specifies the imaginary part of the input signal. Input data is a fixed-point number with a maximum word length of 24 bits or a 1D array of fixed-point numbers with maximum word lengths of 24 bits. Leave imaginary data in unwired to read only real data. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. reset — Clears all internal states on the cycle or call for which this signal is TRUE. For the Outside the single-cycle Timed Loop execution mode, the Express VI restarts on the same call that reset is TRUE. For the Outside the single-cycle Timed Loop execution mode, the Express VI restarts on the same call that reset is TRUE. For the Inside the single-cycle Timed Loop execution mode, the Express VI restarts on the first call that reset is deasserted after reset is TRUE. Additionally, the handshaking signals behave as follows during the cycles where reset is asserted: input valid is ignored. ready for output is ignored. output valid is FALSE. ready for input is FALSE, which handles cases where reset is held TRUE for a long time. The Express VI is not ready for inputs when reset is asserted. real data out — Returns the real part of the FFT result. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Wire output valid to input valid of a downstream node to transfer data from this Express VI to a downstream node. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. data index — Indicates which FFT bin the VI returns. To display data index, select Single Channel, Single Sample in the Input Format section of the configuration dialog box. data out indexes — Indicates which FFT bins the VI returns. To display data out indexes, select Single Channel, Multiple Samples in the configuration dialog box. imaginary data out — Returns the imaginary part of the FFT result. |
| --- |

#### Timing Diagram Outside the Single-Cycle Timed Loop (Single Channel, Single Sample Input Format)

The following diagram demonstrates timing when you use this Express VI outside of a single-cycle Timed Loop.

[IMAGE alt='image' src='loc_eps_streaming-1.gif']

#### Timing Diagram Inside the Single-Cycle Timed Loop When Throughput is Equal to 1 cycle / input

The following diagram demonstrates timing when you use this Express VI inside a single-cycle Timed Loop with **Throughput** equal to 1 cycle / input.

[IMAGE alt='image' src='loc_eps_streaming-2.gif']

#### Timing Diagram Inside the Single-Cycle Timed Loop When Throughput is Not Equal to 1 cycle / input

The following diagram demonstrates timing when you use this Express VI inside a single-cycle Timed Loop with **Throughput** not equal to 1 cycle / input.

[IMAGE alt='image' src='loc_eps_streaming-3.gif']

#### Avoiding Data Loss During FFT Calculation

In a single-cycle Timed Loop, this Express VI does not accept or return values while computing the FFT. During this time, if the system or another node sends data to this Express VI, LabVIEW discards the data. This might happen if this Express VI receives data as part of a complicated or non-uniform pattern.

To ensure no data is lost, [create a FIFO](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data) to hold data until this Express VI accepts values again. Ensure that the FIFO you create is large enough to hold all data points that collect during the FFT calculation time. To roughly estimate the size of the FIFO you need to create, divide the latency of this Express VI by the average system throughput.

#### Selecting the Appropriate Input/Output Index Pattern (Single Channel, Multiple Samples Input Format)

When using the **Single Channel, Multiple Samples** input format, you must select the appropriate **Input/Output Index Pattern**. If the data source of an FFT Express VI is the FPGA I/O node, select **Continuous input indexes / M-interval output indexes**. If the data source is the output of another FFT Express VI, such as when performing inverse FFT on FFT results, ensure that the input pattern of the second FFT Express VI is the same as the output pattern of the first FFT Express VI. Otherwise, the FFT results will be inaccurate.

For a 4096-point FFT with 4 samples per input using the **Continuous input indexes / M-interval output indexes** **Input/Output Index Pattern** (where *M* equals 1024), the indexes of the input samples are 0, 1, 2, 3 in the first valid input cycle, 4, 5, 6, 7 in the second cycle, and so on. The indexes of the output samples are 0, 1024, 2048, 3072 in the first valid output cycle, 1, 1025, 2049, 3073 in the second cycle, and so on. The following figure shows a graphical representation of such a **Continuous input indexes / M-interval output indexes** **Input/Output Index Pattern**:

[IMAGE alt='image' src='noloc_eps_input_pattern_1.gif']

Conversely, if you select the **M-interval input indexes / Continuous output indexes** **Input/Output Index Pattern**, the output will be in the continuous pattern. Compared with the previous example, the patterns of input and output are reversed. The following figure shows a graphical representation of such an **M-interval input indexes / Continuous output indexes** **Input/Output Index Pattern**:

[IMAGE alt='image' src='noloc_eps_input_pattern_2.gif']

#### Implementation Goal Considerations (Single Channel, Multiple Samples Input Format)

Theoretically, performing an *N*-point FFT on fixed-point input data results in output data with word lengths increased by *log<sub>2</sub>(N)+1* bits compared to the input data. When you select **Accuracy** in the **Implementation Goal** section of the configuration dialog box, the FFT Express VI extends the word length of the input data to the output word length by padding zeros, and all internal complex multiply operations use this word length. Conversely, when you select **Resource usage**, the FFT Express VI increases the word length stage-by-stage from input to output. Therefore, the bit width of complex multipliers also increases stage-by-stage.

When you select **Resource usage**, the complex multipliers retain fewer bits than when you select **Accuracy**, so the increased *log<sub>2</sub>(N)+1* bits in the output data are not as accurate compared to when you select **Accuracy**. Selecting **Resource usage** saves FPGA resources because the bit widths of the complex multipliers and internal registers are smaller than the bit widths that result when you select **Accuracy**. You potentially can achieve a higher FPGA clock rate at compilation when you select **Resource usage** because of the resulting shorter word lengths used for complex multipliers.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\FFT\FFT.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\FFT (1 Channel, N Samples)\FFT (1 Channel, N Samples).lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Cross-correlation Using FFT (1 Channel, N Samples)\Cross-correlation Using FFT (1 Channel, N Samples).lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\FFT\FFT.lvproj

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/lmrsmpl/xnode/nifpga-rational-resampler-xnode.html language=enus -->
## TOPIC 00193: Rational Resampler

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/lmrsmpl/xnode/nifpga-rational-resampler-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/lmrsmpl/xnode/nifpga-rational-resampler-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a rational resampling filter, which updates the input sample rate by an L/M factor where L is an interpolation factor and M is a decimation factor. Rational resampling is the process of converting the sample rate of a signal to another sample rate that differs from the original sample rate

### Rational Resampler

Provides a rational resampling filter, which updates the input sample rate by an **L**/**M** factor where **L** is an interpolation factor and **M** is a decimation factor.

Rational resampling is the process of converting the sample rate of a signal to another sample rate that differs from the original sample rate by a rational factor of **L**/**M**, where both **L** and **M** are integer values. When **L**=1 and **M**>1, the resampling is an integer decimation, and when **L**>1 and **M**=1, the resampling is an integer interpolation.

Rational resampling is useful for interfacing with digital signal processing (DSP) systems that operate at different sample rates. By choosing **L** and **M** properly, you can approximate any desired sample rate change ratio.

[IMAGE alt='icon' src='nifpga-rational-resampler-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Filter Parameters | Contains the following options: L— Specifies the interpolation factor. M— Specifies the decimation factor. Note L and M must never be equal. Stopband attenuation— Specifies the attenuation above where the gain versus frequency has finished its rapid falloff. The default is 80 dB. Input sample rate— Specifies the sample rate of each input channel. The Input sample rate, combined with L and M, determines the Output sample rate. Output sample rate— Indicates the calculated average rate at which the Express VI returns valid output data for each channel. |
| Implementation | Contains the following options: Show reset terminal— Specifies whether this Express VI includes a reset input on the block diagram to reset this Express VI at run time. Number of channels— Specifies the number of source channels that this Express VI handles. Adapt to source— Specifies whether this Express VI decides the output data type. Disable the Adapt to source checkbox if you want to use Word length to determine the output data type. Word length— Specifies any output word length in the range of [1, 32]. Word length is available only if you disable the Adapt to source checkbox. Integer word length— Indicates the output integer word length that this Express VI calculates. |
| Filter Response | Displays the actual magnitude response of the filter. |
| Execution Mode | Contains the following options: Outside single-cycle Timed Loop— Select this option to use this Express VI outside of a single-cycle Timed Loop. Outside single-cycle Timed Loop is disabled when L/M is greater than 1. Inside single-cycle Timed Loop— Select this option to use this Express VI inside a single-cycle Timed Loop. Selecting Inside single-cycle Timed Loop enables Throughput. When you execute this Express VI inside the single-cycle Timed Loop, the Express VI provides four handshaking signals you can use to schedule the timing of data. This option is useful if you want to achieve higher throughput using a rational resampling filter. Throughput— Displays the minimum number of cycles between two successive frames of valid input data. LabVIEW sets the value of Throughput according to the options you specify in the configuration dialog box. Throughput is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, LabVIEW sets the throughput to 1 call / sample, which means that this Express VI can accept data every time it is called. Clock rate— Specifies the level of pipelining stages this Express VI uses internally. Increasing the number of stages increases the clock rate at which this Express VI can compile for both Inside the single-cycle Timed Loop and Outside the single-cycle Timed Loop. This option does not set the clock rate explicitly. <note>Note Adjusting the value of Clock rate increases the FPGA resource usage and latency of this Express VI. An increased latency indicates that this Express VI takes longer to return a valid result.</note> |
| Configuration Feedback | Displays information about how this Express VI executes. This information is based on the configuration options you specify. LabVIEW displays this information only if you select Outside single-cycle Timed Loop. |

#### Inputs/Outputs

| input data — Specifies the data you want to filter. reset — Resets the state of the internal resampling filter.Outside the single-cycle Timed Loop, the Express VI restarts on the same call that reset is TRUE. Inside the single-cycle Timed Loop, the Express VI restarts on the first call that reset is deasserted after reset is TRUE. Additionally, the handshaking signals behave as follows during the cycles where reset is asserted: input valid is ignored. ready for output is ignored. output valid is FALSE. ready for input is FALSE, which handles cases where reset is held TRUE for a long time. The Express VI is not ready for inputs when reset is asserted. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. output data — Returns the filtered data. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node.To display output valid, select Inside single-cycle Timed Loop in the configuration box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input is FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. channel index — Indicates the index of the channel corresponding to the last valid output data. |
| --- |

handshaking with multiple channels

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/mean-var-std/xnode/nifpgamean-var-std-xnode.html language=enus -->
## TOPIC 00194: Mean, Variance, and Standard Deviation

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/mean-var-std/xnode/nifpgamean-var-std-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/mean-var-std/xnode/nifpgamean-var-std-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the mean, variance, and/or standard deviation of an input signal. This Express VI analyzes discrete frames of data rather than analyzing data continuously. This Express VI waits for N cycles to collect a frame of data before returning one valid output, where N is the number of samples in

### Mean, Variance, and Standard Deviation

Calculates the mean, variance, and/or standard deviation of an input signal. This Express VI analyzes discrete frames of data rather than analyzing data continuously. This Express VI waits for N cycles to collect a frame of data before returning one valid output, where N is the number of samples in each frame. It then waits for another N cycles to return another valid output.

[IMAGE alt='icon' src='nifpgamean-var-std-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Number of Samples | Specifies the number of samples in each frame on which this Express VI performs statistical measurements. |
| Statistics | Contains the following options: Mean—Specifies whether to calculate and return the mean value of the input signal. Standard deviation—Specifies whether to calculate and return the standard deviation of the current input signal. Variance—Specifies whether to calculate and return the variance of the current input signal. |
| Execution Mode | Contains the following options: Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Latency—Displays the number of cycles between the last point in the input frame and the valid output, which is a single point. Latency is available only when you select Inside single-cycle Timed Loop. |

#### Inputs/Outputs

| input data — Specifies the input signal to measure.input data is a fixed-point number or integer with a maximum word length of either 32 bits if signed or 31 bits if unsigned. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI.To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. reset — Clears all internal states when this signal is TRUE.Outside the single-cycle Timed Loop, this Express VI clears all internal states on the same call that reset is TRUE. Inside the single-cycle Timed Loop, this Express VI clears all internal states on the first cycle that reset is FALSE after reset is TRUE. mean — Returns the mean value of the input signal. standard deviation — Returns the standard deviation of the input signal. variance — Returns the variance of the input signal. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. After returning TRUE for the previous output frame, output valid returns FALSE and waits for the next frame to complete. Wire output valid to input valid of a downstream node to transfer data from this Express VI to a downstream node. To display output valid, select the Inside single-cycle Timed Loop option in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. |
| --- |

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/notch/xnode/nifpganotchfilter-xnode.html language=enus -->
## TOPIC 00195: Notch Filter

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/notch/xnode/nifpganotchfilter-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/notch/xnode/nifpganotchfilter-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attenuates a specific frequency band in one or more input signals using a second order IIR notch filter. You can use the Notch Coefficients Express VI to generate the set of filter coefficients during run time. icon Dialog Box Options Option Description Filter Specifications Contains the following o

### Notch Filter

Attenuates a specific frequency band in one or more input signals using a second order IIR notch filter.

You can use the [Notch Coefficients](../../../host/notch/xnode/notchcoefficients-xnode.html) Express VI to generate the set of filter coefficients during run time.

[IMAGE alt='icon' src='nifpganotchfilter-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Filter Specifications | Contains the following options: Notch frequency (Hz)—Specifies the center frequency for the notch filter to attenuate. Expected sample rate (S/s)—Specifies the sample rate of the input signal. This Express VI uses the rate you specify to calculate the normalized notch frequency, which is Notch frequency/Expected sample rate. Caution The actual sample rate is specified elsewhere in the FPGA application. If the sample rate changes, you must change the Expected sample rate in this VI. Otherwise, this VI might not behave as expected. Specify quality—Allows you to configure the Q factor of the notch filter. Q factor—Specifies the quality factor of the notch filter. This option is available only when you select Specify quality.This option is available only when you select Specify quality. Specify bandwidth—specify-bandwidth Notch width (Hz)—Specifies the 3-dB bandwidth of the filter, which is the frequency range for which the filter attenuates the signal energy by a factor of two or more. This option is available only when you select Specify bandwidth.This option is available only when you select Specify bandwidth. |
| Output Data Type | Contains the following options: Avoid overflow—Specifies that the word length and integer word length of the output data type are large enough to ensure that the filter output does not overflow. Same as input—Specifies that the output data type is the same as the input data type. The output will saturate if the output range is exceeded during signal transients. Overflow will not occur with a steady-state sinusoidal input. |
| Implementation | Contains the following options: Number of channels—Specifies the number of channels of input data to process.The calling VI must supply a sequential channel scan to input data on successive calls to this Express VI. The channel order must be fixed. FPGA clock rate (MHz)—Specifies the clock rate at which LabVIEW compiles the FPGA VI. If the FPGA clock rate parameter does not match the top-level clock rate, the Code Generation Errors window returns an error when you compile the FPGA VI.Use the Top-Level Clock FPGA Target Properties page to change the top-level clock rate. |
| Filter Response | Displays the actual magnitude response of the filter. |

#### Inputs/Outputs

| input data — Specifies the input signal to filter.input data is a fixed-point number or integer with a maximum word length of 32 bits. reset — Resets the filter state of the input data channel to zero if TRUE. Resetting the filter state does not reset the filter coefficients. This Express VI resets automatically the first time you call it. scaled coefficients — Specifies single-channel filter coefficients to load at run time.Scaled coefficients is a fixed-size array of three 32-bit signed integers. This parameter is available only when you configure the VI for single-channel input in the configuration dialog box. configuration — Specifies the scaled coefficients to load at run time for the channel index you specify using the channel index element of this cluster. This Express VI continues to use either the default coefficients or the last coefficients you specified for the channel until you specify new coefficients. This parameter is available only when you configure the VI for multi-channel input in the configuration dialog box. output data — Returns the filtered signal corresponding to the input data channel. |
| --- |

You can configure the sharpness of the notch by specifying either the **Notch width** or the **Q factor** of the filter. To use **Notch width**, select **Specify bandwidth** in the **Filter Specifications** section of the configuration dialog box. To use **Q factor**, select **Specify quality** in the **Filter Specifications** section of the configuration dialog box.

**Q factor** and **Notch width** are related by the following equation:

**Q factor** = **Notch frequency**/**Notch width**.

**Notch frequency** and **Notch width** or **Q factor** are constrained such that the upper end of the attenuated frequency band is less than half of the **Expected sample rate (S/s)** (Nyquist frequency) and the lower end of the attenuated frequency range is greater than zero (DC).

Refer to the [support document](https://www.ni.com/r/exbpmj) at ni.com for more information about the accuracy of the FPGA Math and Analysis VIs.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Notch Filter\Notch Filter.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Notch Filter\Notch Filter.lvproj

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/period/xnode/nifpgaanalogperiod-xnode.html language=enus -->
## TOPIC 00196: Analog Period Measurement

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/period/xnode/nifpgaanalogperiod-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/period/xnode/nifpgaanalogperiod-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the period of an evenly sampled periodic signal using threshold crossing detection. This Express VI accepts frames of data, performs measurement on the input data, and returns a valid single result for each frame. During run time, you can use the Scale Period VI to convert the period outp

### Analog Period Measurement

Calculates the period of an evenly sampled periodic signal using threshold crossing detection. This Express VI accepts frames of data, performs measurement on the input data, and returns a valid single result for each frame.

During run time, you can use the [Scale Period](../../../host/public/scale-period-vi.html) VI to convert the period output to units of seconds using the sample rate you specify.

[IMAGE alt='icon' src='nifpgaanalogperiod-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Threshold Crossing Detection | Contains the following option: Level—Specifies the level that, when crossed by input data in the direction you specify, defines a crossing. The value you enter in this option sets the default value of the threshold level input on the block diagram. Hysteresis—Specifies a band around the threshold level that input data must leave before this Express VI can detect another crossing. The Hysteresis option sets the default value of the hysteresis input on the block diagram.The input data meets the hysteresis condition following a rising crossing only after meeting the following conditions in order: input data ≥ threshold level + hysteresis, followed by input data ≤ threshold level – hysteresis. For a falling crossing, input data must meet the above conditions in reverse order. To improve noise suppression, set Hysteresis to the maximum value appropriate for the input signal. Direction—Specifies whether to measure the period between rising or falling threshold crossings. This option sets the default value of the direction input on the block diagram. Interpolate crossings—Specifies whether LabVIEW applies linear interpolation to the input data points immediately before and after the threshold crossing in order to get a more accurate estimate of the actual crossing time instance. |
| Measurement Time | Contains the following option: Number of periods—Specifies the number of periods over which to average the measurement. Increasing the value of this option results in a more accurate measurement by amortizing the fixed errors at the two crossing endpoints. Increasing the value does not require any additional logic, but this Express VI takes longer to return a result. Increase the value of this option only if you need additional accuracy and if the signal period is stable over the number of periods you select. |

#### Inputs/Outputs

| input data — Specifies the periodic signal to measure.input data is a fixed-point number or integer with a maximum word length of 32 bits. threshold level — Specifies the level that, when crossed by input data in the direction you specify, defines a crossing. The value you wire to this input overrides the value you specify in the configuration dialog box. direction — Specifies whether to measure the period between rising or falling threshold crossings. The value you wire to this input overrides the value you specify in the configuration dialog box. reset — Restarts the measurement at the next crossing after input data leaves the hysteresis band. This Express VI initializes automatically the first time you call it. hysteresis — Specifies a band around the threshold level that input data must leave before this Express VI can detect another crossing. The value you wire to this input overrides the value you specify in the configuration dialog box. crossing — Returns TRUE when the current input data sample completes a threshold level crossing in the direction you specify. timeout — Indicates that the Express VI failed to detect enough transitions to complete a measurement in time to avoid overflow in period (Samples). The Express VI resets the measurement after each timeout. period (samples) — Returns the measured period in units of input data samples. period (samples) is a fixed-point number with a word length of 32 and an integer word length of 16. output valid — Returns TRUE on the same call as the crossing that completes the number of periods of the measurement. After returning TRUE for the previous output frame, this indicator returns FALSE, waiting for the next frame to complete. The period output is only valid when output valid is TRUE. |
| --- |

#### Analog Period Measurement Details

The actual period in floating-point units of time is given by:

Period (sec) = **period (samples)** * *loop rate*,

where *loop rate* (in samples per second) is the time between calls to the Analog Period Measurement Express VI and must be constant for the duration of the measurement.

If you do not place a checkmark in the **Interpolate crossings** checkbox, the worst-case error for a given input signal frequency is determined by rounding the measurement duration to an integer number of samples. The number of samples per period is given by

samples = sample rate (S/s) * period (s).

The maximum error (in samples) is given by

maximum error = max (samples – floor(samples), ceiling(samples)-samples).

The **Interpolate crossings** setting computes the linear interpolation of the crossing instant to 8-bit accuracy. The effect on measurement accuracy is dependent on the input signal. In the worst case (a perfect square wave), it has no effect, but for other signals it can provide a significant increase in accuracy.

For example, a 3600 Hz input signal sampled at 50 kS/sec consists of 50,000/3600 = 13.9 samples per period, where one period is 1/3600 = 278 µs. If you do not place a checkmark in **Interpolate crossings** checkbox, the maximum error for a single-period measurement is 0.889 samples/50,000 samples/sec = 17.8 µs, or (17.8/278) * 100 = 6.4% relative error. If the input is a sine wave and you place a checkmark in the **Interpolate crossings** checkbox, you can reduce the error to 0.121 µs, or (0.121/278) * 100 = 0.044% relative error.

Refer to the [support document](https://www.ni.com/r/exbpmj) at ni.com for more information about the accuracy of the Analog Period Measurement Express VI.

#### Detecting a Rising Crossing

The following illustration shows when the Analog Period Measurement Express VI detects a rising crossing.

[IMAGE alt='image' src='loc_eps_threshold_hysteresis.gif']

(A) The Express VI resets the measurement.

(B) The Express VI does not detect a rising crossing because the input signal did not meet the low hysteresis condition since the reset.

(C) The Express VI detects a rising crossing and begins the period measurement.

(D) The Express VI does not detect a rising crossing because the input signal did not meet the high hysteresis condition.

(E) The Express VI does not detect a rising crossing because the input signal must first meet the high hysteresis condition and then the low hysteresis condition before the VI can detect the next rising crossing.

(F) The Express VI detects the second rising crossing, completes the first period measurement, sets **output valid** to TRUE for one sample, and begins the next measurement from the same crossing.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Analog Period Measurement\Analog Period Measurement.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Analog Period Measurement\Analog Period Measurement.lvproj

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/measure/window/xnode/nifpga-scaled-window-xnode.html language=enus -->
## TOPIC 00197: Scaled Window

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/measure/window/xnode/nifpga-scaled-window-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/measure/window/xnode/nifpga-scaled-window-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Full or Professional EditionMinimizes spectral leakage associated with truncated waveforms. This Express VI scales the windowed time-domain signal so that when a LabVIEW object computes the power or amplitude spectrum of the windowed waveform, all windows provide the same level within the

### Scaled Window

Requires: Full or Professional Edition

Minimizes spectral leakage associated with truncated waveforms. This Express VI scales the windowed time-domain signal so that when a LabVIEW object computes the power or amplitude spectrum of the windowed waveform, all windows provide the same level within the accuracy constraints of the output wavelength.

Use this Express VI before you use the [FFT](../../fft/xnode/nifpgafft-xnode.html) Express VI.

[IMAGE alt='icon' src='nifpga-scaled-window-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Window Configuration | Contains the following options: Type— Specifies the type of window. You can select from the following options: Hanning Hamming Blackman-Harris Exact Blackman Blackman Flat Top 4 Term B-Harris 7 Term B-Harris Low Sidelobe Length— Specifies the length of the window. The range of Length is [2, 8192]. |
| Output Data Type | Contains the following options: Adapt to source— Specifies whether this Express VI decides the output data type. Disable the Adapt to source checkbox if you want to use Word length to determine the output data type. Word length— Specifies any output word length in the range of [1, 32]. Word length is available only if you disable the Adapt to source checkbox. Integer word length— Indicates the output integer word length that this Express VI calculates. |
| Implementation | Contains the following options: Show reset terminal— Specifies whether this Express VI includes a reset input on the block diagram to reset this Express VI at run time. You can save resources on the FPGA if you do not enable the Show reset terminal checkbox. Show coefficient index terminal— Specifies whether you specify the indices of the window coefficients in coefficient index. If you do not enable this checkbox, this Express VI automatically indexes the window coefficients. |
| Window Coefficients | Displays the values of the window coefficients. |
| Execution Mode | Contains the following options: Outside single-cycle Timed Loop— Specifies that this Express VI runs outside the single-cycle Timed Loop. Inside single-cycle Timed Loop— Specifies that this Express VI runs inside the single-cycle Timed Loop. Selecting Inside single-cycle Timed Loop makes the handshaking signals available for use. Refer to the Scheduling Timing Using Handshaking Signals topic for information about using the handshaking signals available for this Express VI. Throughput— Displays the number of cycles between two successive values of valid input data. This number always is one cycle. Therefore, LabVIEW sets the value according to where you place this Express VI. If you select Inside single-cycle Timed Loop, LabVIEW sets the throughput to 1 cycle / sample. If you select Outside single-cycle Timed Loop, LabVIEW sets the throughput to 1 call / sample. Latency— Displays the number of clock cycles this Express VI needs to return a valid result inside a single-cycle Timed Loop. This option is available only if you select Inside single-cycle Timed Loop. If you select Outside single-cycle Timed Loop, this Express VI returns valid output data on every call to the Express VI. The Configuration Feedback section displays the number of clock cycles each call takes to execute. Clock rate— Specifies the level of pipelining stages this Express VI uses internally. Increasing the number of stages increases the clock rate at which this Express VI can compile for both Inside the single-cycle Timed Loop and Outside the single-cycle Timed Loop. This option does not set the clock rate explicitly. |
| Configuration Feedback | Displays information about how this Express VI executes. This information is based on the configuration options you specify. LabVIEW displays this information only if you select Outside single-cycle Timed Loop. |

#### Inputs/Outputs

| real data in — Specifies the real part of the input signal. reset — Specifies whether to reset the auto-indexing process. Inside the single-cycle Timed Loop, reset ignores the incoming data point during the reset cycle. reset is available only if you enable the Show reset terminal checkbox in the configuration dialog box. imaginary data in — Specifies the imaginary part of the input signal. Leave imaginary data in unwired to read only real data. coefficient index — Specifies the window coefficient index. coefficient index is available only if you enable the Show coefficient index checkbox in the configuration dialog box. input valid — Specifies whether the next data point has arrived for processing. Wire output valid of an upstream node to input valid to transfer data from the upstream node to this Express VI. To display this handshaking terminal, select Inside single-cycle Timed Loop in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this Express VI to return a new value. The default is TRUE. Use a Feedback Node to wire ready for input of a downstream node to ready for output of the current node. Note If ready for output is FALSE during a given cycle, output valid returns FALSE during that cycle. To display ready for output, select Inside single-cycle Timed Loop in the configuration dialog box. data index — Indicates the current window coefficient index corresponding to the current output. When running this Express VI inside the single-cycle Timed Loop, LabVIEW ignores this value if output valid is FALSE. You can use data index for debugging. imaginary data out — Returns the imaginary part of the windowed signal. output valid — Returns TRUE if this Express VI has computed a result that downstream nodes can use. Use output valid for handshaking with other FPGA VIs and functions. To display output valid, select Inside single-cycle Timed Loop in the configuration dialog box. ready for input — Returns TRUE if this Express VI is ready to accept new input data. Use a Feedback Node to wire ready for input to ready for output of an upstream node. Note If ready for input returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this Express VI during the following cycle. LabVIEW discards this data even if input valid is TRUE during the following cycle. To display ready for input, select Inside single-cycle Timed Loop in the configuration dialog box. real data out — Returns the real part of the windowed signal. |
| --- |

Parent topic:

FPGA Math & Analysis

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/siggen/sinewave/nifpga-sine-wave-generator-vi.html language=enus -->
## TOPIC 00198: Sine Wave Generator

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/siggen/sinewave/nifpga-sine-wave-generator-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/siggen/sinewave/nifpga-sine-wave-generator-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a point-by-point sine wave using direct digital synthesis. The synthesis runs continuously from the top-level FPGA target clock to produce an accurate real-time frequency. Each execution of this VI returns the most recent sample produced by the underlying synthesis engine. During run time,

### Sine Wave Generator

Generates a point-by-point sine wave using direct digital synthesis. The synthesis runs continuously from the [top-level FPGA target clock](/csh?context=lvfpga_lvfpgahelp_selecting_toplevel_fpga_clk) to produce an accurate real-time frequency. Each execution of this VI returns the most recent sample produced by the underlying synthesis engine.

During run time, you can use the [Normalize Signal Generation Parameters](../../host/public/normalize-signal-generation-parameters-vi.html) VI to convert frequency, phase, and duty cycle parameters to fixed-point units normalized to the clock rate.

[IMAGE alt='icon' src='nifpga-sine-wave-generator-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Sine Parameters | Contains the following options: Frequency (Hz)— Specifies the output frequency in Hz. The generation process runs continuously from the FPGA clock. Each call to the Sine Wave Generator Express VI samples the current output of the look-up table. If the Show frequency terminal checkbox does not contain a checkmark, Frequency (Hz) determines the frequency of the sine output. If the Show frequency terminal checkbox does contain a checkmark, Frequency (Hz) determines the default value of the frequency (periods/tick) input. Amplitude— Determines the zero-to-peak amplitude of the output sine wave. The default is the full signed range of the Amplitude resolution you select. Full scale— Selects the largest possible amplitude for the Amplitude resolution you select. If Full scale does not contain a checkmark, Amplitude resolution accommodates the Amplitude you select. Phase offset (deg)— Specifies the phase in degrees of the signal the Sine Wave Generator Express VI returns relative to its initialization. If the Show offset terminal checkbox does not contain a checkmark, Phase offset (deg) determines the phase offset of the sine output. If the Show offset terminal checkbox does contain a checkmark, Phase offset (deg) determines the default value of the phase offset (periods) input. |
| Implementation | Contains the following options: Look-up table size— Specifies the number of sine wave points LabVIEW stores in block memory on the FPGA target. Use the Power Spectrum Preview waveform graph to choose a Look-up table size that provides sufficient spurious free dynamic range for the application you create. LabVIEW coerces the Look-up table size you select to the nearest size supported by the FPGA target for the Amplitude resolution you select. For example, if you select an Amplitude resolution of 16 bits, the smallest Look-up table size you can use is 1024. Use linear interpolation— Provides a more accurate sine output by using remaining phase accumulator bits as a fractional index into the look-up table. However, if you place a checkmark in the Use linear interpolation checkbox, you increase latency and FPGA usage. The result of the VI calculation is a 32-bit number. The VI truncates the lower 16 bits to return Sine out. Amplitude resolution— Specifies the output data type of the sine wave. You can choose 8-, 16-, or 32-bit signed integers. Frequency (periods/tick)— Displays the frequency, in number of periods per tick of the FPGA clock, that corresponds to the Frequency (Hz) you specify. If you place a checkmark in the Show frequency terminal checkbox, you can use Frequency (periods/tick) to verify the programmatic frequency (periods/tick) input is correct. Phase offset (periods)— Displays the number of periods by which the phase is offset. This number corresponds to the Phase offset (deg) you specify. If you place a checkmark in the Show offset terminal checkbox, you can use Phase offset (periods) to verify the programmatic phase offset (periods) input is correct. Show frequency terminal— Creates a frequency (periods/tick) input on the Sine Wave Generator Express VI. If the Show frequency terminal checkbox does not contain a checkmark, Frequency (Hz) determines the frequency of the sine output. If the Show frequency terminal checkbox does contain a checkmark, Frequency (Hz) determines the default value of the frequency (periods/tick) input. Show offset terminal— Creates a phase offset (periods) input on the Sine Wave Generator Express VI. If the Show offset terminal checkbox does not contain a checkmark, Phase offset (deg) determines the phase offset of the sine output. If the Show offset terminal checkbox does contain a checkmark, Phase offset (deg) determines the default value of the phase offset (periods) input. Output sine and cosine— Creates a cosine out output on the Sine Wave Generator Express VI, offset by 90 degrees from the sine out output. You cannot use linear interpolation if you place a checkmark in the Output sine and cosine checkbox. FPGA clock rate (MHz)— Specifies the clock rate at which LabVIEW builds the Sine Wave Generator Express VI. If the FPGA clock rate parameter does not match the top-level clock rate, the Code Generation Errors window returns an error when you compile. Use the Top-Level Clock FPGA Target Properties page to change the top-level clock rate. Use top-level clock— Populates FPGA clock rate (MHz) with the frequency of the currently configured top-level FPGA target clock. If you do not use the Sine Wave Generator Express VI in an FPGA VI under an FPGA target in the Project Explorer window, LabVIEW uses the default value of 40 MHz for the FPGA clock rate (MHz). |
| Power Spectrum Preview | Displays a preview of the configured signal power spectrum. The peak corresponding to the configured frequency is normalized to 0 dB. The next highest peak in the spectrum gives an estimate of the spurious free dynamic range resulting from the configured implementation parameters. Refer to the support document at ni.com for information about the spurious free dynamic range. |

#### Inputs/Outputs

| reset — Sets the VI to the initial state determined by phase offset (periods). The VI resets automatically when it first runs. frequency (periods/tick) — (Optional) Specifies the frequency, in number of periods per tick of the FPGA clock, of the sine wave. The output frequency depends on the top-level FPGA target clock rate. Verify the top-level FPGA target clock rate is set in the Top-Level Clock FPGA Target Properties page before you configure the Sine Wave Generator Express VI. The default corresponds to the value of Frequency (Hz) you enter in the Configure Sine Wave Generator dialog box. The step size through a 32-bit accumulator determines the frequency. The upper n bits specify the address of the sine point in a 2n element look-up table. Place a checkmark in the Show frequency terminal checkbox in the Configure Sine Wave Generator dialog box to add this parameter to the VI connector pane on the block diagram. The value you wire to this terminal must be an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. If you wire a data type with a different configuration to this terminal, LabVIEW coerces the configuration to be <+,32,0>. phase offset (periods) — (Optional) Specifies the initial phase, in number of periods, of the sine wave according to the following formula. phase offset (periods) = Phase offset (deg) / 360 The default corresponds to the value of Phase offset (deg) that you enter in the Configure Sine Wave Generator dialog box. Place a checkmark in the Show offset terminal checkbox in the Configure Sine Wave Generator dialog box to add this parameter to the VI connector pane on the block diagram. The value you wire to this terminal must be an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. If you wire a data type with a different configuration to this terminal, LabVIEW coerces the configuration to be <+,32,0>. sine out — Returns a signed 8-, 16-, or 32-bit integer containing the sine output point. cosine out — (Optional) Returns a signed 8-, 16-, or 32-bit integer containing the sine output point offset by 90 degrees. |
| --- |

If you [run the FPGA VI on a development computer](/csh?context=lvfpga_lvfpgahelp_running_fpga_vi_on_emulator), the Sine Wave Generator Express VI outputs every point of the generated sine wave, regardless of the rate at which LabVIEW calls the VI. To produce the same data when you run the FPGA VI on a development computer as when you run the FPGA VI on an FPGA target, change **frequency (periods/tick)** to take into account the rate at which the FPGA VI calls the Sine Wave Generator VI. The following equation determines the correction for running the FPGA VI on a development computer.

frequency (periods/tick)

frequency (periods/tick)

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Generation\Sine Wave\Sine Wave.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Generation\Sine Wave\Sine Wave.lvproj

Parent topic:

Generation

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/siggen/squarewave/nifpga-square-wave-generator-vi.html language=enus -->
## TOPIC 00199: Square Wave Generator

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/siggen/squarewave/nifpga-square-wave-generator-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/siggen/squarewave/nifpga-square-wave-generator-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a point-by-point square wave using direct digital synthesis (DDS). The synthesis runs continuously using the block diagram clock rate to produce a real-time frequency. The block diagram clock rate is the top-level clock rate, unless the Square Wave Generator Express VI is inside a single-c

### Square Wave Generator

Generates a point-by-point square wave using direct digital synthesis (DDS). The synthesis runs continuously using the block diagram clock rate to produce a real-time frequency. The block diagram clock rate is the [top-level clock rate](/csh?context=lvfpga_lvfpgahelp_selecting_toplevel_fpga_clk), unless the Square Wave Generator Express VI is inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpgahelp_setting_timed_loop_fpga_clk) configured with a different clock rate.

During run time, you can use the [Normalize Signal Generation Parameters](../../host/public/normalize-signal-generation-parameters-vi.html) VI to convert frequency, phase, and duty cycle parameters to fixed-point units normalized to the clock rate.

[IMAGE alt='icon' src='nifpga-square-wave-generator-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Square Wave Parameters | Contains the following options: Frequency— Specifies the desired output frequency in Hz. Phase offset— Specifies the phase in degrees of the signal the Square Wave Generator Express VI returns relative to its initialization. Duty cycle— Specifies the desired percentage of time the square wave remains high over one period. The default is 50%. Frequency (periods/tick)— Returns the scaled output frequency in number of periods per tick of the FPGA clock. The VI calculates this value using the following formula: Frequency (periods/tick) = Frequency / Clock rate Each call to the VI samples the current value. Phase offset (periods)— Returns the scaled phase offset in number of periods. The VI calculates this value using the following formula: Phase offset (periods) = Phase offset / 360 Duty cycle (periods)— Returns the scaled percentage of time, in number of periods, the square wave remains high over one period. The VI calculates this value using the following formula: Duty cycle (periods) = Duty cycle / 100 Clock rate— Indicates the value you specify in the FPGA clock rate parameter in the Clock section of the configuration dialog box. |
| Output | Contains the following options: Data type— Specifies the data type of the square wave. If you select Boolean, the Amplitude and Offset options are not available. Offset— Specifies the DC offset of the square wave. The default is 0. Refer to the Details section for more information. Amplitude— Specifies the amplitude of the square wave. The default is 32767, so square wave out is either –32767 or 32767. Refer to the Details section for more information. |
| Execution Mode | Contains the following options: Inside single-cycle Timed Loop— Guarantees that the VI executes in one cycle. If you select the Inside single-cycle Timed Loop option and place the VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error. Outside single-cycle Timed Loop— Waits until the VI detects an edge before returning output. You can call this function in a While Loop to control the loop execution rate because the time between edges depends on the frequency. If you select the Outside single-cycle Timed Loop option and place the VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error. |
| Signal Output Preview | Displays a preview of the configured square wave. |
| Clock | Contains the following options: FPGA clock rate— Specifies the clock rate at which LabVIEW builds the Square Wave Generator Express VI. If the FPGA clock rate parameter does not match the block diagram clock rate when you compile, the Code Generation Errors window reports an error. Use the Top-Level Clock FPGA Target Properties page to change the block diagram clock rate. If the Square Wave Generator VI is inside a single-cycle Timed Loop, use the Configure Timed Loop dialog box or Source Name input on the Timed Loop to change the block diagram clock rate. Set to top-level clock rate— Sets the FPGA clock rate to the top-level clock rate that is currently configured. |

#### Inputs/Outputs

| reset — Sets the VI to the initial state determined by phase offset (periods). The VI resets automatically when it first runs. duty cycle (periods) — Specifies the scaled duty cycle, in number of periods, according to the following formula. duty cycle (periods) = duty cycle (%) / 100 To save FPGA resources, leave the duty cycle (periods) input unwired and use the configuration dialog box to specify the duty cycle. If you change the value of the duty cycle (periods) input at run time, the square wave updates on the next period edge. The value you wire to this terminal must be an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. If you wire a data type with a different configuration to this terminal, LabVIEW coerces the configuration to be <+,32,0>. amplitude — Specifies the amplitude of the square wave. The default is 32767, so square wave out is either –32767 or 32767. offset — Specifies the DC offset of the square wave. The default is 0. frequency (periods/tick) — Specifies the scaled output frequency, in number of periods per tick of the FPGA clock, according to the following formula. frequency (periods/tick) = frequency (Hz) / FPGA clock rate To save FPGA resources, leave the frequency (periods/tick) input unwired and use the configuration dialog box to specify the frequency. If you change the value of the frequency (periods/tick) input at run time, the square wave updates on the next call. If you change the frequency, the DDS preserves the position in the period so only the rate changes on the next call. The value you wire to this terminal must be an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. If you wire a data type with a different configuration to this terminal, LabVIEW coerces the configuration to be <+,32,0>. phase offset (periods) — Specifies the scaled phase offset, in number of periods, according to the following formula. phase offset (periods) = phase offset (deg) / 360 To save FPGA resources, leave the phase offset (periods) input unwired and use the configuration dialog box to specify the phase offset. If you change the value of the phase offset (periods) input at run time, the square wave updates on the next call. To avoid glitch conditions, do not change the value of the phase offset (periods) input by more than the value of the frequency (periods/tick) input for each call to the VI. The value you wire to this terminal must be an unsigned fixed-point data type with a 32-bit word length and a 0-bit integer word length. If you wire a data type with a different configuration to this terminal, LabVIEW coerces the configuration to be <+,32,0>. square wave out — Returns a Boolean or an 8-, 16-, or 32-bit integer containing the square wave output. If the Square Wave Generator Express VI is inside a single-cycle Timed Loop, square wave out is a single sample point. If the Square Wave Generator Express VI is outside a single-cycle Timed Loop, square wave out updates after each edge of the square wave. |
| --- |

Amplitude is the distance between the offset and peak. In the following example, the offset is 5 and the amplitude is 10.

[IMAGE alt='image' src='loc_eps_offset_amplitude.gif']

To pass the square wave to an output line, you can wire **square wave out** to an I/O resource using the [FPGA I/O Node](../../../../eio/eionode/eionode-xnode.html).

Over time, the Express VI returns the expected period length and frequency. However, some jitter might occur. For example, suppose you want to create a 6.25 MHz square wave using a 40 MHz top-level clock. In this case, a clock cycle is 25 ns and a square wave period is 160 ns, so the average square wave period should be 6.4 clock cycles long. Each square wave period is an integer number of cycles, but the Express VI returns period lengths of 6, 6, 6, 7, and 7. As a result, the average period length is 6.4 clock cycles, and the average frequency is 6.25 MHz.

If you place the Express VI outside a single-cycle Timed Loop and [run the FPGA VI on a development computer](/csh?context=lvfpga_lvfpgahelp_running_fpga_vi_on_emulator), the timing is not precise. So, the Express VI returns a square wave that alternates between the high and low value.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\Generation\Square Wave\Square Wave.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\Generation\Square Wave\Square Wave.lvproj

Parent topic:

Generation

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/analysis/siggen/whitenoise/nifpga-white-noise-generator-vi.html language=enus -->
## TOPIC 00200: White Noise Generator

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/analysis/siggen/whitenoise/nifpga-white-noise-generator-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/analysis/siggen/whitenoise/nifpga-white-noise-generator-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a white noise signal with uniform or Gaussian distribution. icon Dialog Box Options Parameter Description White Noise Type Contains the following options: Uniform— Generates a uniformly distributed, pseudorandom pattern whose values are in the range [–a:a–1], where a is the value of Amplit

### White Noise Generator

Generates a [white noise](/csh?context=lvfpga_lvanlsconcepts_noise_generation) signal with uniform or Gaussian distribution.

[IMAGE alt='icon' src='nifpga-white-noise-generator-vi.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| White Noise Type | Contains the following options: Uniform— Generates a uniformly distributed, pseudorandom pattern whose values are in the range [–a:a–1], where a is the value of Amplitude. Gaussian— Generates a Gaussian-distributed, pseudorandom pattern. |
| Execution Mode | Contains the following options: Inside single-cycle Timed Loop— For uniform signals, select this option to guarantee that the VI executes in one cycle. For Gaussian signals, select this option to provide a new output value every nth call to the VI. For the n–1 cycles between valid outputs, the data ready? output returns FALSE. If you select this option and place the VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error. Outside single-cycle Timed Loop— For Gaussian signals, select this option to return an output after every call to the White Noise Generator Express VI. If you select this option and place the VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error. |
| Scaling | Contains the following options: Show amplitude terminal— Creates an amplitude input on the White Noise Generator Express VI. This option only appears if you select Uniform as the White Noise Type. You can save resources on the FPGA if you do not place a checkmark in the Show amplitude terminal checkbox. Show RMS terminal— Creates an RMS input on the White Noise Generator Express VI. This option only appears if you select Gaussian as the White Noise Type. You can save resources on the FPGA if you do not place a checkmark in the Show RMS terminal checkbox. RMS— Specifies the root mean square (RMS) value of white noise out. The default is 4096. You can set RMS to any value from 0–6000. This option only appears if you select Gaussian as the White Noise Type. Amplitude— Specifies the amplitude of the uniform white noise. The default is 32768, so the white noise out output is uniformly distributed between –32768 and 32767. You can set Amplitude to any value from 0–32768. This option only appears if you select Uniform as the White Noise Type. Expected peak value— Returns the theoretical peak value based on the RMS value. The peak value is six times the RMS value or 32767, whichever is smaller. Set to original value— Sets Amplitude to the default value of 32768 or RMS to the default value of 4096. |

#### Inputs/Outputs

| seed — Specifies the starting point in the internal pseudorandom pattern. amplitude — Specifies the amplitude of the uniform white noise. The default is 32768, so the white noise out output is uniformly distributed between -32768 and 32767. If you wire a value greater than 32768 to the amplitude input, the VI coerces the value to 32768.The value you wire to this input overrides the value in the configuration dialog box. RMS — Specifies the root mean square (RMS) value of white noise out. The default is 4096. You can set RMS to any value from 0–6000. If you wire a value greater than 6000, the VI coerces the value to 6000. The value you wire to this input overrides the value in the configuration dialog box. reset — Sets the VI to the initial state determined by the seed input. white noise out — Returns the uniformly distributed or Gaussian-distributed, pseudorandom pattern as a 16-bit integer. |
| --- |

For Gaussian signals, the White Noise Generator Express VI calculates the sum of *n* samples of uniform white noise and scales the result to fit the range. If **RMS** is 4096, the theoretical peak value is 24576 and the crest factor is 6. Therefore, the maximum possible output value is 6 standard deviations above 0. Output values saturate if the peak value is greater than 32767. If **RMS** is 6000, the peak value is 32767 and the crest factor is 5.46. The following graph shows a comparison between an ideal Gaussian curve and the curve the White Noise Generator Express VI returns.

[IMAGE alt='image' src='loc_fp_FPGA_gaussian.gif']

The White Noise Generator Express VI cannot guarantee that the mean is zero.

Parent topic:

Generation

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/cdr/code-generation-errors-window.html language=enus -->
## TOPIC 00201: Code Generation Errors Window

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/cdr/code-generation-errors-window.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/cdr/code-generation-errors-window.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This window appears if errors occur while LabVIEW is generating intermediate files. Use this window to view errors that occurred during code generation. This window does not update after you correct an error. You must recompile the FPGA VI to see the latest errors. This window includes the following

### Code Generation Errors Window

This window appears if errors occur while LabVIEW is generating intermediate files.

Use this window to view errors that occurred during code generation. This window does not update after you correct an error. You must recompile the FPGA VI to see the latest errors.

This window includes the following components:

| Option | Description |
| --- | --- |
| Items with errors | Lists all LabVIEW items affected by errors and warnings in the current VI. |
| Errors | Lists all objects with errors in the FPGA VI. |
| Details | Includes specific details about the error you select from the Errors list.This component also provides suggestions for correcting the error. However, you might be able to correct the error using techniques other than the suggestions. |
| Show Error | Highlights the location of the error in the VI or Project Explorer window. You also can double-click an error in the Errors list to highlight the location of the error.Clicking the Show Error button does not close the Code Generation Errors window. LabVIEW disables the Show Error button if no object in the VI or Project Explorer window corresponds to the error you select. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/cdr/compilation-status-window.html language=enus -->
## TOPIC 00202: Compilation Status Window

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/cdr/compilation-status-window.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/cdr/compilation-status-window.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Compilation Status window appears when you compile an FPGA VI. If you have compiled a build specification already, you can right-click the build specification and select Display Compilation Results from the shortcut menu to display this window. Use this window to view status and compilation info

### Compilation Status Window

The **Compilation Status** window appears when you [compile an FPGA VI](/csh?context=lvfpga_lvfpgahelp_compiling_fpga_vis_howto). If you have compiled a build specification already, you can right-click the build specification and select **Display Compilation Results** from the shortcut menu to display this window.

Use this window to view status and compilation information for the FPGA build specification. You also can use this window to [disconnect](/csh?context=lvfpga_lvfpgahelp_disconnecting_from_compile_server) from the compile server or cancel the compilation.

This window can include the following components, depending on your specific FPGA target:

| Option | Description |
| --- | --- |
| Build Specifications | Lists the build specifications that are compiling or have compiled during this session of the Compilation Status window.To remove a build specification from this list, right-click the build specification and select Remove from List from the shortcut menu. |
| Status | Displays the progress of the FPGA VI compilation. |
| Last Update Time | Displays the last time the compile server updated the information. |
| Reports | Specifies the type of compiler information you want to view. Not all reports are available at the beginning of the compilation. A message appears in the Compilation Status window when reports become available to view.You can select from the following reports, depending on your specific FPGA target: Summary Configuration Estimated device utilization (pre-synthesis) Estimated device utilization (synthesis)/Estimated device utilization (placement) Final device utilization (map)/Final device utilization (placement) Estimated timing (map)/Estimated timing (placement) Final timing (place and route)/Final timing (routing) Xilinx log |
| Save | Saves the final compilation status report to a file. The Save button is available only for the Xilinx log report and only when the compilation is complete. |
| Timing Violation | Displays the Timing Violation Analysis window. This button is available only if a timing violation occurs. |
| Compilation Error | Opens the support document on ni.com about interpreting common Xilinx compilation errors in the FPGA Module. This button is available only if a compilation error occurs. |
| Cancel Compilation | Cancels the compilation of the build specification you select in the Build Specifications list. |
| Close | Closes the Compilation Status window. Use the pull-down menu on this button to close the window with the following options: Close Window (default)—Closes the window and continues communicating with the compile server. Disconnect All—Disconnects LabVIEW from the compile server. Any compile jobs running will continue, but LabVIEW will not receive any updates. Disconnect from the compile server when you want to shutdown LabVIEW. You do not need to disconnect from the compile server to perform other operations in LabVIEW while the FPGA VI is compiling. Stop Compilation—Cancels the current compile jobs. |
| Switch to mini view | Shrinks the Compilation Status window to show only the Build Specifications list. |
| Switch to full view | Expands the Compilation Status window to its full size. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/cdr/configure-cloud-service-dialog-box.html language=enus -->
## TOPIC 00203: Configure Cloud Service Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/cdr/configure-cloud-service-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/cdr/configure-cloud-service-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to configure LabVIEW to connect to the LabVIEW FPGA Compile Cloud Service. The LabVIEW FPGA Module includes the ability to offload compiles to dedicated computers. To offload compiles to a high-performance server and compile multiple VIs in parallel, you can purchase the LabVIEW

### Configure Cloud Service Dialog Box

Use this dialog box to configure LabVIEW to connect to the LabVIEW FPGA Compile Cloud Service.

Note

NI website

ni.com

To access this dialog box, select **Tools»Options** to display the [Options](/csh?productcategories=147794&context=lvcore_lvdialog_options_dialog_box) dialog box and select **FPGA Module** from the **Category** list, then select **Connect to LabVIEW FPGA Compile Cloud Service**.

| Option | Description |
| --- | --- |
| User name | Displays the name of the account that you use to log into the LabVIEW FPGA Compile Cloud Service. |
| Password | Specifies the password that you must enter before you can connect to the LabVIEW FPGA Compile Cloud Service. |
| Remember password | Specifies whether LabVIEW stores the password for this User name on this server. |
| Test Connection | Attempts to connect to the LabVIEW FPGA Cloud Service and returns the connection status. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/cdr/configure-remote-compile-server-dialog-box.html language=enus -->
## TOPIC 00204: Configure Remote Compile Server Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/cdr/configure-remote-compile-server-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/cdr/configure-remote-compile-server-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to configure LabVIEW to connect to a remote compile server. The LabVIEW FPGA Module includes the ability to offload compile jobs to dedicated computers. To create an on-site compile farm that has one or more compile workers that multiple developers can target, you can install the

### Configure Remote Compile Server Dialog Box

Use this dialog box to configure LabVIEW to connect to a remote compile server.

Note

FPGA Compile Farm Server

FPGA Module Readme

To access this dialog box, select **Tools»Options** to display the [Options](/csh?productcategories=147794&context=lvcore_lvdialog_options_dialog_box) dialog box. Next, select **FPGA Module** from the **Category** list. Finally, select **Connect to a network compile server**.

| Option | Description |
| --- | --- |
| Compile servers | Displays a list of configured compile servers. Select a compile server from this list to specify which compile server LabVIEW uses. Click the Add/Remove buttons to add and remove compile servers. |
| User name | Specifies the name of the account that you use to log into the remote compile server. The default is admin. If you cannot connect to the remote compile server using the default user name, contact the owner and request a valid user account. Before you can configure the remote compile server, you must add the User name and Password to the list of user names with permission to compile FPGA VIs on the compile server. If you use the FPGA Compile Farm Server, any user that you add to the Users tab can compile VIs on the compile server. Select a compile server to enable this option. |
| Password | Specifies the password for the User name The default is blank. If you cannot connect to the remote compile server using the default password, contact the owner and request a valid user account. |
| Remember password | Specifies whether LabVIEW stores the password for this User name on this compile server. |
| Test Connection | Attempts to connect to the compile server and returns connection status. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/cdr/select-compile-server-dialog-box.html language=enus -->
## TOPIC 00205: Select Compile Server Dialog Box

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/cdr/select-compile-server-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/cdr/select-compile-server-dialog-box.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to specify a compile server for the current build specification. To access this dialog box, select Build from the build specification shortcut menu. LabVIEW displays this dialog box by default. To disable the Select Compile Server prompt, select Tools»Options to display the Optio

### Select Compile Server Dialog Box

Use this dialog box to specify a compile server for the current build specification.

To access this dialog box, select **Build** from the [build specification shortcut menu](/csh?context=lvfpga_lvfpgahelp_fpga_build_spec_working_with). LabVIEW displays this dialog box by default.

To disable the **Select Compile Server** prompt, select **Tools»Options** to display the **Options** dialog box and select **FPGA Module** from the **Category** list, then remove the checkmark from the **Prompt to select a compile server for each compilation** checkbox.

| Option | Description |
| --- | --- |
| Use the local compile server | Specifies that LabVIEW use the compilation tools installed on the local computer, called localhost. |
| Connect to server | Specifies that LabVIEW use the compilation tools installed on another computer or that LabVIEW use localhost when authentication is required. Compile server name—Displays the name or IP address of the computer running the compile server. User name—Displays the name of the account that you use to log into the compile server. Configure remote server—Displays the Configure Remote Compile Server dialog box. |
| Connect to LabVIEW FPGA Compile Cloud Service | Specifies that LabVIEW use the compilation tools available through the LabVIEW FPGA Compile Cloud Service. User name—Displays the name of the account that you use to log into the LabVIEW FPGA Compile Cloud Service. Configure cloud server—Displays the Configure Cloud Service dialog box. |
| Prompt to select a compile server for each compilation | Specifies whether LabVIEW prompts you to select a compile server for each compilation. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/additional-clock-signal-settings-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00206: Additional Clock Signal Settings Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/additional-clock-signal-settings-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/additional-clock-signal-settings-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to specify the ports in the IP that behave as a clock or clock enable signal. Click the Create File or Modify File button in the Component-Level IP page of the FPGA Target Properties dialog box to display the Configure Component-Level IP wizar

### Additional Clock Signal Settings Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to specify the ports in the IP that behave as a clock or clock enable signal.

Click the **Create File** or **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the **FPGA Target Properties** dialog box to display the Configure Component-Level IP wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| LabVIEW Name | Displays the name you enter in the LabVIEW name text box of the Basic Signal Settings page. |
| Direction | Indicates whether the signal receives data from the CLIP or sends data to the CLIP. |
| Frequency | Indicates the frequency, in hertz, of the signal. |
| Duty Cycle | Indicates the duty cycle of the signal. |
| Accuracy | Indicates the accuracy of the clock in parts per million. |
| Jitter | Indicates the variation in the clock period. |
| Number of DCMs needed | Specifies how many digital clock managers (DCM) to reserve on the FPGA. LabVIEW uses this number when compiling to determine if the code instantiates too many DCMs. |
| Number of MMCMs needed | Specifies how many mixed mode clock managers (MMCM) to reserve on the FPGA. LabVIEW uses this number when compiling to determine if the code instantiates too many MMCMs. |
| Number of BUFGs needed | Specifies how many BUFGs to reserve on the FPGA. LabVIEW uses this number when compiling to determine if the code instantiates too many global clock nets. |
| Minimum frequency | Specifies the minimum supported frequency in hertz. |
| Maximum frequency | Specifies the maximum supported frequency in hertz. |
| Minimum duty cycle | Specifies the minimum time by percentage that the clock signal stays high. The default value is 50 percent. |
| Maximum duty cycle | Specifies the maximum time by percentage that the clock signal stays high. The default value is 50 percent. |
| Accuracy | Specifies the accuracy of the clock in parts per million. |
| Jitter | Specifies the variation in the clock period. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/additional-clock-status-signal-settings-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00207: Additional Clock Status Signal Settings Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/additional-clock-status-signal-settings-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/additional-clock-status-signal-settings-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to view and change information about clock status signals in the IP. Click the Create file or the Modify File button in the Component-Level IP page of the FPGA Target Properties dialog box to display the Configure Component-Level IP wizard. Th

### Additional Clock Status Signal Settings Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to view and change information about clock status signals in the IP.

Click the **Create file** or the **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the [FPGA Target Properties](/csh?context=lvfpga_lvfpgadialog_fpga_target_properties) dialog box to display the Configure Component-Level IP wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| HDL Name | Displays the name of the clock status signal in the VHDL file. |
| Clock Status Type | Indicates the type of clock status signal. LabVIEW determines the type based on the direction of the signal. Available status types are Derived Clocks Valid and Source Clock Ready. |
| Associated Clock | Displays the LabVIEW name of the clock associated with the clock status signal. |
| Available Clock | Displays a list of available clocks. Use this list to specify the clock associated with the clock status signal. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/additional-data-signal-settings-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00208: Additional Data Signal Settings Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/additional-data-signal-settings-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/additional-data-signal-settings-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to specify any required clock domains for a signal. Click the Create File or Modify File button in the Component-Level IP page of the FPGA Target Properties dialog box to display the Configure Component-Level IP wizard. This page includes the

### Additional Data Signal Settings Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to specify any required clock domains for a signal.

Click the **Create File** or **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the **FPGA Target Properties** dialog box to display the Configure Component-Level IP wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| LabVIEW Name | Displays the name you enter in the LabVIEW name text box of the Basic Signal Settings page. |
| Required Clock Domain | Displays the clock domain you select in the Required clock domain pull-down menu. |
| Single-Cycle Timed Loop | Displays the configuration of the signal in regards to single-cycle Timed Loops.Specify the configuration in the Single-Cycle Timed Loop pull-down menu. |
| Required clock domain | Specifies whether the signal is valid only in a specific clock domain. If you do not specify a required clock domain, you can use the I/O in any clock domain.The required clock domain must match a clock signal name defined in another location of the CLIP XML file. If you require a clock domain, any I/O Node on the block diagram that uses this CLIP I/O must be in the clock domain you specify. If the I/O Node is in the wrong clock domain, LabVIEW returns an error during compilation of the FPGA VI. |
| Single-Cycle Timed Loop | Specifies the configuration of the signal in regards to single-cycle Timed Loop structures.In a single-cycle Timed Loop, you can ensure that data latches on every clock edge. If the IP in the CLIP expects to receive values on every clock edge, then setting this value to Required makes LabVIEW enforce this requirement. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/basic-signal-settings-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00209: Basic Signal Settings Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/basic-signal-settings-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/basic-signal-settings-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to specify the names and data types of block diagram terminals that correspond to VHDL ports in the component-level IP (CLIP). Click the Create File or Modify File button in the Component-Level IP page of the FPGA Target Properties dialog box

### Basic Signal Settings Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to specify the names and data types of block diagram terminals that correspond to VHDL ports in the [component-level IP (CLIP)](/csh?context=lvfpga_lvfpgaconcepts_using_component_ip).

Click the **Create File** or **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the **FPGA Target Properties** dialog box to display the Configure Component-Level IP wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| HDL Name | Displays the name of the signal in the VHDL file. |
| LabVIEW Name | Displays the name that LabVIEW uses to identify the signal. By default, the LabVIEW name matches the HDL name. You can enter a new name in the LabVIEW name text box. |
| Direction | Indicates whether the signal receives data from the CLIP or sends data to the CLIP. |
| Signal Type | Displays the type of signal. You can change the signal type by selecting a new type in the Signal type pull-down menu. |
| Default LabVIEW Data Type | Displays the default LabVIEW data type. You can change the data type in the Default LabVIEW Data Type section of this dialog box. |
| LabVIEW name | Specifies a name corresponding to the HDL signal. |
| Signal type | Specifies the type of signal for the signal you select in the table.You can select from the following values: data—Use if the signal is a standard I/O data signal. If you do not specify a value for the SignalType tag, the default is data. clock—Use if the signal is a clock. If you use clock, you must use the <Boolean/> tag within the DataType tag. reset—Use if the signal is a reset signal that connects to the global asynchronous reset signal of the FPGA VI. The global asynchronous reset signal for FPGA VIs is active-high. You can use reset only if the InterfaceType tag is set to Fabric. A reset signal must be a ToCLIP signal. clock status—There are two types of clock status signals: SourceClockReady and DerivedClocksValid. Both signals are required for each FromCLIP clock with the SupportDerivedClocks tag. These signals together implement the handshaking interface with the LabVIEW FPGA clocking circuitry that produces derived clocks. |
| terminal type selector | Defines the data type of the signal. If the signal is for a LabVIEW interface, the data type also defines how LabVIEW represents this signal. Fixed-point encoding—Specifies whether the selected terminal is Signed or Unsigned. This option is valid for fixed-point terminals only. Integer word length—Specifies the integer word length of the selected terminal between [–2048, 2047]. This option is valid for fixed-point terminals only. LabVIEW sets the word length of the terminal to the width of the corresponding port as specified in the IP. |
| Signal description | Specifies the description of the signal. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/entity-architecture-fpga-family-and-ip-type-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00210: Entity, Architecture, FPGA Family and IP Type Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/entity-architecture-fpga-family-and-ip-type-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/entity-architecture-fpga-family-and-ip-type-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to define the top-level entity and architecture you want to synthesize and simulate. You also use this page to specify the FPGA families on which this CLIP can compile. Click the Create File or Modify File button in the Component-Level IP page

### Entity, Architecture, FPGA Family and IP Type Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to define the top-level entity and architecture you want to synthesize and simulate. You also use this page to specify the FPGA families on which this CLIP can compile.

Click the **Create File** or **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the **FPGA Target Properties** dialog box to display the Configure Component-Level IP wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| Top-Level Entity and Architecture | Specifies the entity/architecture pairs you want to use for IP synthesis and simulation. Synthesis Module—Specifies the top-level entity/architecture pair to use for IP synthesis. syn entity—Specifies the top-level entity to use for IP synthesis. syn arc—Specifies the top-level architecture to use for IP synthesis. Simulation Model—Specifies the top-level entity/architecture pair to use for IP simulation. This section is available only if you selected the User-defined option in the Set Simulation Behavior dialog box for the top-level synthesis file. sim entity—Specifies the top-level entity to use for IP simulation. sim arc—Specifies the top-level architecture to use for IP simulation. |
| FPGA Family Support | Specifies the families of FPGAs on which this IP can execute. You can determine the FPGA device family of the current FPGA target on the General page of the FPGA Target Properties dialog box. unlimited—Specifies that this IP can run on all FPGA families, including but not limited to the ones listed on this page. Select this option if the IP does not contain any family-specific code and the IP does not contain any Xilinx compilation tool-specific file types. limited—Specifies that this IP can run only on FPGAs that belong to the families you specify. Select this option if the IP contains code that can execute only on a particular FPGA family. |
| Component Level IP Type | Specifies the type of CLIP. User-defined IP—Specifies that the HDL code communicates directly with an FPGA VI. Socketed IP—Specifies that LabVIEW treats the IP as socketed CLIP. Some FPGA targets define a fixed CLIP socket in the FPGA where you can insert socketed CLIP. Select socket type—Specifies the target-defined socket type. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/generics-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00211: Generics Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/generics-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/generics-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to view and change information about generics in the IP. Click the Create File or the Modify File button in the Component-Level IP page of the FPGA Target Properties dialog box to display the Configure Component-Level IP wizard. This page incl

### Generics Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to view and change information about generics in the IP.

Click the **Create File** or the **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the **FPGA Target Properties** dialog box to display the Configure Component-Level IP wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| Generics | Displays information about generics that correspond to the entity and architecture you specified on the previous page of the configuration wizard. Generic Name—Displays the name of the generic. Type—Displays the generic type. Default Value—Displays the default generic value from the top-level synthesis file. You can override this value in the CLIP declaration by entering a new value in the Default value text box. In LabVIEW, you can override the default value from the CLIP declaration by entering a new value in the Generics page of the Component-Level IP Properties dialog box. |
| Default value | Specifies a new value for the selected generic. |
| Check syntax | Checks the syntax of the VHDL code. You must verify the syntax of the synthesis files before continuing in the wizard. |
| Generic description | Specifies a description for the generic. The description appears in the message box of the Generics page of the Component-Level IP Properties dialog box. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/name-and-source-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00212: Name and Source Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/name-and-source-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/name-and-source-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to specify the CLIP declaration name and define the synthesis and simulation files the CLIP can use. Click the Create File or Modify File button in the Component-Level IP page of the FPGA Target Properties dialog box to display this wizard. Th

### Name and Source Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to specify the CLIP declaration name and define the synthesis and simulation files the CLIP can use.

Click the **Create File** or **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the **FPGA Target Properties** dialog box to display this wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| Declaration name | Specifies the name of the CLIP declaration. This name is not the same as the name of the declaration XML file itself, which you will specify later in the wizard. |
| Component-level IP description | Specifies a description to associate with the CLIP. You can view and edit the description on this page only. |
| Source Files | Displays the synthesis files that compose the IP. |
| Simulation Behavior | Displays the simulation behavior that corresponds to each synthesis file. |
| Add Syn File | Prompts you for a synthesis file to add to the CLIP declaration.The files you add appear in the table under the Synthesis File column. |
| Set Sim Behavior | Launches the Set Simulation Behavior dialog box, which you use to change the simulation behavior of the selected synthesis file or exclude this synthesis file from simulation. |
| Set Top | Sets the selected synthesis file as the top-level file. Note CLIP does not support using a netlist file as the top-level synthesis file. |
| Remove | Removes the selected synthesis file from the table. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/set-simulation-behavior-dialog-box-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00213: Set Simulation Behavior Dialog Box (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/set-simulation-behavior-dialog-box-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/set-simulation-behavior-dialog-box-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to set the simulation behavior for a particular synthesis file in the CLIP. To access this dialog box, select a synthesis file in the table on the Name and Sources page of the Configure Component-Level IP wizard. Then click the Set Simulation Behavior button. This dialog box incl

### Set Simulation Behavior Dialog Box (Configure Component-Level IP Wizard)

Use this dialog box to set the simulation behavior for a particular synthesis file in the CLIP.

To access this dialog box, select a synthesis file in the table on the [Name and Sources](/csh?context=lvfpga_lvfpgadialog_fpga_clip_wiz_name) page of the Configure Component-Level IP wizard. Then click the **Set Simulation Behavior** button.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| User-defined | Specifies that you will define one or more files, such as .vhd or .mif, as the simulation model for the synthesis file. Use the buttons to the right of this list in the following ways: Add File—Prompts you to add a file to the list. Remove File—Prompts you to remove a file from the list. Select the file and then click the Remove File button. Set as Top—Prompts you to set a file as the top-level simulation file. Select a file and then click the Set as Top button. By default, the first file you add is the top-level simulation file. |
| Same as synthesis | Specifies that LabVIEW uses the synthesis file itself for simulation. This option is available only if the synthesis file is not a netlist file. |
| Exclude from simulation model | Specifies that LabVIEW does not export this file for simulation. Select this option if you do not need to simulate the synthesis file.If you select this option for the top-level synthesis file, then LabVIEW will not simulate any of the IP, regardless of the simulation behavior you specify for the other synthesis files. |

#### Batch Setting Simulation Behaviors

If you select multiple synthesis files before launching this dialog box, LabVIEW dims certain behaviors according to the following rules:

- LabVIEW always dims the User-defined behavior.
- LabVIEW dims the Same as synthesis behavior if you selected at least one netlist file
- LabVIEW dims the Exclude from simulation model behavior if you selected the top-level synthesis file

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/clip/clip-generator/xml-export-page-configure-component-level-ip-wizard.html language=enus -->
## TOPIC 00214: XML Export Page (Configure Component-Level IP Wizard)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/clip/clip-generator/xml-export-page-configure-component-level-ip-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/clip/clip-generator/xml-export-page-configure-component-level-ip-wizard.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Configure Component-Level IP wizard to review the finished CLIP declaration XML file. Click the Create File or Modify File button in the Component-Level IP page of the FPGA Target Properties dialog box to display the Configure Component-Level IP wizard. This page includes the fo

### XML Export Page (Configure Component-Level IP Wizard)

Use this page of the [Configure Component-Level IP](/csh?context=lvfpga_lvfpgaconcepts_fpga_clip_using_wizard) wizard to review the finished CLIP declaration XML file.

Click the **Create File** or **Modify File** button in the [Component-Level IP](../../../../resource/framework/providers/lvfpga-llb/prefpage-fpga-clipdeclarations-vi.html) page of the **FPGA Target Properties** dialog box to display the Configure Component-Level IP wizard.

This page includes the following components:

| Option | Description |
| --- | --- |
| XML file content | Displays the finished CLIP declaration XML file content. If you need to change anything in the file, click the Back button in the wizard and make the change on the appropriate page. |
| XML file path | Specifies the name and path to the CLIP declaration XML file. |

Parent topic:

LabVIEW FPGA Module Dialog Box Reference

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/communicationprotocols/i2c-xnode/nifpgai2c-xnode.html language=enus -->
## TOPIC 00215: Communication Protocols Functions

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/communicationprotocols/i2c-xnode/nifpgai2c-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/communicationprotocols/i2c-xnode/nifpgai2c-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at ni.com/labview-tools-network. Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communica

### Communication Protocols Functions

Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at [ni.com/labview-tools-network](https://www.ni.com/r/exqsb9). Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communication protocols, such as Inter-Integrated Circuit (I2C) and Serial Peripheral Interface (SPI).

Parent topic:

Communication Protocols

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/communicationprotocols/spi-xnode/nifpgaspi-xnode.html language=enus -->
## TOPIC 00216: Communication Protocols Functions

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/communicationprotocols/spi-xnode/nifpgaspi-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/communicationprotocols/spi-xnode/nifpgaspi-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at ni.com/labview-tools-network. Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communica

### Communication Protocols Functions

Use the Communication Protocols functions to access communication protocols IP available on the LabVIEW Tools Network at [ni.com/labview-tools-network](https://www.ni.com/r/exqsb9). Each Communication Protocols function corresponds to IP. Use the IP to establish communication between masters and slaves through different communication protocols, such as Inter-Integrated Circuit (I2C) and Serial Peripheral Interface (SPI).

Parent topic:

Communication Protocols

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/handshake/common/acknowledge-handshake-method.html language=enus -->
## TOPIC 00217: Acknowledge (Handshake Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/handshake/common/acknowledge-handshake-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/handshake/common/acknowledge-handshake-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acknowledges receipt of an element of data from an upstream writer node, meaning that it clears the data to enable another write operation. Use the Handshake Method Node to implement this method. You must use this method inside a single-cycle Timed Loop. Inputs/Outputs Option Description Handshake I

### Acknowledge (Handshake Method)

Acknowledges receipt of an element of data from an upstream writer node, meaning that it clears the data to enable another write operation.

Use the [Handshake Method Node](nifpgahandshakepalettemethodnodemergevi-vi.html) to implement this method. You must use this method inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Handshake In | Handshake In specifies the handshake item.You can wire a handshake control, handshake constant, VI-Defined Handshake Configuration node, or the Handshake Out terminal of another Handshake Method Node to Handshake In. |
| Enable | Enable Specifies whether to acknowledge the transfer for a single clock cycle. If Enable is FALSE, this method does not execute. |
| Handshake Out | Handshake Out returns Handshake In if Handshake In is wired. Otherwise, Handshake Out returns the handshake item that you specify in the Handshake Method Node. |

Use this method in addition to the [Read Without Acknowledge](/csh?context=lvfpga_lvfpga_fpgahandshake_read_woack) method as an alternative to the [Read](/csh?context=lvfpga_lvfpga_fpgahandshake_read) method to [read one element of data](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) if you need to control when the node acknowledges the data transfer. After a reader node has read the data, this method clears the current data in the handshake item to enable another write. If data is received before a reader node has read the current data in the handshake item, this method ignores the acknowledgment. This method clears the data in one clock cycle. However, if you cross clock domains, the handshake item is not ready for a new write operation for several clock cycles.

Parent topic:

Handshake Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/handshake/common/clear-handshake-method.html language=enus -->
## TOPIC 00218: Clear (Handshake Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/handshake/common/clear-handshake-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/handshake/common/clear-handshake-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears and resets a handshake item. Aborting and restarting the VI does not reset a handshake item. Use this method to clear any data in the handshake item and reset the Output Valid and Ready for Input terminals of connected nodes to their default values. This method may take more than one clock cy

### Clear (Handshake Method)

Clears and resets a handshake item. Aborting and restarting the VI does not reset a handshake item. Use this method to clear any data in the handshake item and reset the Output Valid and Ready for Input terminals of connected nodes to their default values.

Note

Use the [Handshake Method Node](nifpgahandshakepalettemethodnodemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Handshake In | Handshake In specifies the handshake item.You can wire a handshake control, handshake constant, VI-Defined Handshake Configuration node, or the Handshake Out terminal of another Handshake Method Node to Handshake In. |
| Start | Start specifies that the node begin to clear and reset the handshake. |
| Handshake Out | Handshake Out returns Handshake In if Handshake In is wired. Otherwise, Handshake Out returns the handshake item that you specify in the Handshake Method Node. |
| Done | Done indicates that the node has finished clearing and resetting the handshake and that no clear is in progress. |

You can invoke **Clear** before or after a reader node reads the data. This method terminates any transfer in progress and acknowledges any transfer that a node has read but not acknowledged by removing the data.

You can invoke the **Clear** method in a different clock domain than the reader or the writer clock domains.

You must use this method inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Parent topic:

Handshake Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettemethodnodemergevi-vi.html language=enus -->
## TOPIC 00219: Handshake Method Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettemethodnodemergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettemethodnodemergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes a handshake method on an FPGA VI. You must specify a handshake item before you specify a method. You must specify a handshake item before you specify a method. You can invoke the following methods on FPGA handshake items: Write, Read, Clear, Read Without Acknowledge, Acknowledge icon Inputs/

### Handshake Method Node

Invokes a handshake method on an FPGA VI.

You must specify a handshake item before you specify a method.

You must specify a handshake item before you specify a method.

You can invoke the following methods on FPGA handshake items:

[Write](/csh?context=lvfpga_lvfpga_fpgahandshake_write), [Read](/csh?context=lvfpga_lvfpga_fpgahandshake_read), [Clear](/csh?context=lvfpga_lvfpga_fpgahandshake_clear), [Read Without Acknowledge](/csh?context=lvfpga_lvfpga_fpgahandshake_read_woack), [Acknowledge](/csh?context=lvfpga_lvfpga_fpgahandshake_ack)

[IMAGE alt='icon' src='nifpgahandshakepalettemethodnodemergevi-vi.png']

#### Inputs/Outputs

| Handshake In — specifies the handshake item. You can wire a handshake control, handshake constant, VI-Defined Handshake Configuration node, or the Handshake Out terminal of another Handshake Method Node to Handshake In Handshake Out — returns Handshake In if Handshake In is wired. Otherwise, Handshake Out returns the handshake item that you specify in the Handshake Method Node. |
| --- |

To use the Handshake Method Node, you first must [create a handshake item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant). You can create a handshake item in the Project Explorer window or using the [VI-Defined Handshake Configuration](../../../localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-handshake-vi.html) node. You then can right-click the Handshake Method Node and select the handshake item from the **Select Handshake** shortcut menu.

When you wire a handshake item to **Handshake In**, LabVIEW renames this node to Handshake Item to indicate that the node is now associated with a handshake item in the project.

Tip

Project Explorer

Add New Handshake

Tip

Handshake In

Find Item in Project

You must use the Handshake Method Node inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Refer to the [Scheduling Timing Using Handshaking Signals](/csh?context=lvfpga_lvfpgaconcepts_fpga_handshaking) topic for more information about handshaking.

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettenameconstantmergevi-vi.html language=enus -->
## TOPIC 00220: Handshake Constant

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettenameconstantmergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/handshake/common/nifpgahandshakepalettenameconstantmergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Handshake constant to specify a handshake item on the block diagram. Use the Configure Handshake Name Control Type dialog box to configure a Handshake constant. The pull-down menu that appears when you click the arrow on the Handshake constant lists only the handshake items that appear in th

### Handshake Constant

Use the Handshake constant to specify a [handshake item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) on the block diagram.

Use the [Configure Handshake Name Control Type](/csh?context=lvfpga_lvfpgadialog_fpga_reg_control_db) dialog box to configure a Handshake constant.

The pull-down menu that appears when you click the arrow on the Handshake constant lists only the handshake items that appear in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window under the same FPGA target as the active VI and that match the configuration of the constant. When you select an item from the pull-down menu, the configuration of the constant matches the configuration of the item you select from the pull-down menu.

You also can use the [Handshake control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) to specify a handshake item on the block diagram.

Note

FPGA I/O constant

FPGA clock constant

Register constant

Memory constant

FIFO constant

[IMAGE alt='icon' src='nifpgahandshakepalettenameconstantmergevi-vi.png']

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/handshake/common/read-handshake-method.html language=enus -->
## TOPIC 00221: Read (Handshake Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/handshake/common/read-handshake-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/handshake/common/read-handshake-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one element of data from a handshake item and automatically removes the data to prepare for the next transfer. If Ready for Output is FALSE during a given clock cycle, Output Valid returns FALSE during that clock cycle.Use the Handshake Method Node to implement this method. Inputs/Outputs Opti

### Read (Handshake Method)

Reads one element of data from a handshake item and automatically removes the data to prepare for the next transfer.

Note

Ready for Output

Output Valid

Use the [Handshake Method Node](nifpgahandshakepalettemethodnodemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Handshake In | Handshake In specifies the handshake item.You can wire a handshake control, handshake constant, VI-Defined Handshake Configuration node, or the Handshake Out terminal of another Handshake Method Node to Handshake In. |
| Ready for Output | Ready for Output specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the Ready for Input output of a downstream node to this input. |
| Handshake Out | Handshake Out returns Handshake In if Handshake In is wired. Otherwise, Handshake Out returns the handshake item that you specify in the Handshake Method Node. |
| Data | Data is the data retrieved from the handshake item.The Data data type is the data type you configure in the FPGA Handshake Properties dialog box when you create the handshake item. |
| Output Valid | Output Valid returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the Input Valid input of a downstream node to transfer data from the node to the downstream node. |

You must use this method inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Parent topic:

Handshake Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/handshake/common/read-without-acknowledge-handshake-method.html language=enus -->
## TOPIC 00222: Read Without Acknowledge (Handshake Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/handshake/common/read-without-acknowledge-handshake-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/handshake/common/read-without-acknowledge-handshake-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the data element from a handshake item without acknowledging the transfer, meaning that the data remains in the handshake item. Use this method in addition to the Acknowledge method as an alternative to the Read method to read one element of data if you need to control when the node acknowledg

### Read Without Acknowledge (Handshake Method)

Reads the data element from a handshake item without acknowledging the transfer, meaning that the data remains in the handshake item. Use this method in addition to the [Acknowledge](/csh?context=lvfpga_lvfpga_fpgahandshake_ack) method as an alternative to the [Read](/csh?context=lvfpga_lvfpga_fpgahandshake_read) method to [read one element of data](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) if you need to control when the node acknowledges the data transfer.

Use the [Handshake Method Node](nifpgahandshakepalettemethodnodemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Handshake In | Handshake In specifies the handshake item.You can wire a handshake control, handshake constant, VI-Defined Handshake Configuration node, or the Handshake Out terminal of another Handshake Method Node to Handshake In. |
| Ready for Output | Ready for Output specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the Ready for Input output of a downstream node to this input. |
| Handshake Out | Handshake Out returns Handshake In if Handshake In is wired. Otherwise, Handshake Out returns the handshake item that you specify in the Handshake Method Node. |
| Data | Data returns the data transferred using the handshake item. |
| Output Valid | Output Valid returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the Input Valid input of a downstream node to transfer data from the node to the downstream node. |

You can continue to read the same data element by holding **Ready for Output** TRUE until you invoke the **Acknowledge** method.

You must use this method inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Parent topic:

Handshake Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/handshake/common/write-handshake-method.html language=enus -->
## TOPIC 00223: Write (Handshake Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/handshake/common/write-handshake-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/handshake/common/write-handshake-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an element of data to a handshake item. If the Ready for Input terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the Input Valid terminal is TRUE during the following cycle.

### Write (Handshake Method)

Writes an element of data to a handshake item.

Note

Ready for Input

Input Valid

Use the [Handshake Method Node](nifpgahandshakepalettemethodnodemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Handshake In | Handshake In specifies the handshake item.You can wire a handshake control, handshake constant, VI-Defined Handshake Configuration node, or the Handshake Out terminal of another Handshake Method Node to Handshake In. |
| Data | Data is the data to transfer using the handshake item.The Data data type is the data type you configure in the FPGA Handshake Properties dialog box when you create the handshake item. |
| Input Valid | Input Valid specifies whether the next data point has arrived for processing. Wire the Output Valid output of an upstream node to this input to transfer data from the upstream node to this node. |
| Handshake Out | Handshake Out returns Handshake In if Handshake In is wired. Otherwise, Handshake Out returns the handshake item that you specify in the Handshake Method Node. |
| Ready for Input | Ready for Input returns TRUE if the previous write operation is complete and the node is ready to accept new input data. Use a Feedback Node to wire this output to the Ready for Output input of an upstream node. |

You can use this method to transfer [one element of data](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) when you need to synchronize the reader and writer nodes. A new write operation cannot begin until the reader node has read and acknowledged, or removed, the previous data element.

You must use this method inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop).

Parent topic:

Handshake Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettemethodnodemergevi-vi.html language=enus -->
## TOPIC 00224: Register Method Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettemethodnodemergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettemethodnodemergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes a method on a register item on the FPGA. You must specify a register item before you specify a method. The methods are Write and Read. You must specify a register item before you specify a method. The methods are Write and Read. icon Inputs/Outputs cgenclassrntag.png Register In specifies th

### Register Method Node

Invokes a method on a [register item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) on the FPGA.

You must specify a register item before you specify a method. The methods are Write and Read.

You must specify a register item before you specify a method. The methods are Write and Read.

[IMAGE alt='icon' src='nifpgaregisterpalettemethodnodemergevi-vi.png']

#### Inputs/Outputs

| Register In — specifies the FPGA register item. You can wire a Register control, Register constant, VI-Defined Register Configuration node, or another Register Method Node to Register In Register Out — eturns Register In if Register In is wired. Otherwise, Register Out returns the register item that you specify in the Register Method Node. |
| --- |

To use the Register Method Node, you first must create register items. You can create a register item in the **Project Explorer** window or using a [VI-Defined Register Configuration](../../../localresourcemanager/lrm-api/nifpgalrmpalette-mergevi-register-vi.html) node. You then can right-click the Register Method Node and select the register item from the **Select Register** shortcut menu.

When you wire a register item to **Register In**, LabVIEW renames this node to Register Item to indicate that the node is now associated with a register item in the project.

Tip

Right-click the Register Method Node and select **Add New Register** from the shortcut menu to create a new register item in the Project Explorer window.

Tip

Register In

Find Item in Project

You can invoke the following register methods:

- Write
- Read

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettenameconstantmergevi-vi.html language=enus -->
## TOPIC 00225: Register Constant

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettenameconstantmergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/register/common/nifpgaregisterpalettenameconstantmergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Register constant to specify a register item on the block diagram. Use the Configure Register Name Control Type dialog box to configure a Register constant. The pull-down menu that appears when you click the arrow on the Register constant lists only the register items that appear in the Proj

### Register Constant

Use the Register constant to specify a [register item](/csh?context=lvfpga_lvfpgaconcepts_fpga_storing_reentrant) on the block diagram.

Use the [Configure Register Name Control Type](/csh?context=lvfpga_lvfpgadialog_fpga_reg_control_db) dialog box to configure a Register constant.

The pull-down menu that appears when you click the arrow on the Register constant lists only the register items that appear in the Project Explorer window under the same FPGA target as the active VI and that match the configuration of the constant. When you select an item from the pull-down menu, the configuration of the constant matches the configuration of the item you select from the pull-down menu.

You also can use a [Register control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) to specify a register item on the block diagram.

Note

FPGA clock constant

FPGA I/O constant

FIFO constant

Memory constant

[IMAGE alt='icon' src='nifpgaregisterpalettenameconstantmergevi-vi.png']

Parent topic:

Data Storage & Transfer

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/register/common/read-register-method.html language=enus -->
## TOPIC 00226: Read (Register Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/register/common/read-register-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/register/common/read-register-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single value from a register on the FPGA target. Use this method in conjunction with the Write method. Use the Register Method Node to implement this method. Inputs/Outputs Option Description Register In Specifies the FPGA register item. You can wire a Register control, Register constant, VI

### Read (Register Method)

Reads a single value from a register on the FPGA target. Use this method in conjunction with the [Write](/csh?context=lvfpga_lvfpga_register_write) method.

Use the [Register Method Node](nifpgaregisterpalettemethodnodemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Register In | Specifies the FPGA register item. You can wire a Register control, Register constant, VI-Defined Register Configuration node, or another Register Method Node to Register In. |
| Register Out | Returns Register In if Register In is wired. Otherwise, Register Out returns the register item that you specify in the Register Method Node. |
| Data | Is the data read from memory on the FPGA target. Data is directly accessible only from within the FPGA VI. You cannot directly access the data in the memory of the FPGA target from the host VI. You must use controls, indicators, or DMA FIFOs to access data from the host VI. The Data data type is the data type you configure in the FPGA Register Properties dialog box when you create the register item. If you do not initialize the register item, the data is undefined. |

Parent topic:

Register Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/datatransferandstorage/register/common/write-register-method.html language=enus -->
## TOPIC 00227: Write (Register Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/datatransferandstorage/register/common/write-register-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/datatransferandstorage/register/common/write-register-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single value to a register available on the FPGA target. Use this method in conjunction with the Read method. Use the Register Method Node to implement this method. Inputs/Outputs Option Description Register In Specifies the FPGA register item. You can wire a Register control, Register cons

### Write (Register Method)

Writes a single value to a register available on the FPGA target. Use this method in conjunction with the [Read](/csh?context=lvfpga_lvfpga_register_read) method.

Use the [Register Method Node](nifpgaregisterpalettemethodnodemergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| Register In | Specifies the FPGA register item. You can wire a Register control, Register constant, VI-Defined Register Configuration node, or another Register Method Node to Register In. |
| Data | Is the data to write to the register on the FPGA target. You can directly write to Data only from the FPGA VI. You cannot directly write to the data in the memory of the FPGA target from the host VI. You must use controls, indicators, or DMA FIFOs to access data from the host VI.The Data data type is the data type you configure in the FPGA Register Properties dialog box when you create the register item. If you do not initialize the register item, the data is undefined. |
| Register Out | Returns Register In if Register In is wired. Otherwise, Register Out returns the register item that you specify in the Register Method Node. |

#### Considerations for Single-Cycle Timed Loops

If you use the **Write** method in a single-cycle Timed Loop and there are multiple instances of this method in the FPGA VI, be aware of the following considerations:

- You must set the Write option on the Interfaces page of the FPGA Register Properties dialog box to Never Arbitrate .
- All instances of this method must be in the same clock domain.

Parent topic:

Register Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/desktopexecutionnode/desktopexecutionnode-xnode.html language=enus -->
## TOPIC 00228: FPGA Desktop Execution Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/desktopexecutionnode/desktopexecutionnode-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/desktopexecutionnode/desktopexecutionnode-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs an FPGA VI on a development computer with simulated I/O for the specified number of clock ticks. This node writes all inputs, passes the amount of simulated time you specify, then reads all outputs. The FPGA VI pauses execution until the FPGA Desktop Execution Node is called again, at which poi

### FPGA Desktop Execution Node

Runs an FPGA VI on a development computer with simulated I/O for the specified number of clock ticks. This node writes all inputs, passes the amount of simulated time you specify, then reads all outputs. The FPGA VI pauses execution until the FPGA Desktop Execution Node is called again, at which point the FPGA VI resumes for the specified number of clock ticks.

[IMAGE alt='icon' src='desktopexecutionnode-xnode.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Simulation Configuration | Contains the following options: VI—Specifies the FPGA VI to run. Browse VI—Displays the Select VI dialog box. Click this button to select the VI you want to reference. Reference Clock—Specifies an available FPGA clock to use as the timing source for simulated time. Clock Ticks—Specifies the number of clock ticks to run the FPGA VI for each call to the node. You must specify a non-zero integer. |
| Terminal Configuration | Contains the following options: Available Resources—Displays the I/O resources and front panel controls and indicators available for simulating with the FPGA Desktop Execution Node. The FPGA target you specify in the VI selection box determines the resources that appear in the Available Resources tree. Click the Add/Remove buttons to the right of the Available Resources list to add and remove resources. Selected Resources—Displays the list of resources you select from the Available Resources tree. Change Terminal Direction—Contains the following options: In—Specifies that the selected resource has an input terminal on the block diagram. Out—Specifies that the selected resource has an output terminal on the block diagram. In/Out—Specifies that the selected resource has both input and output terminals on the block diagram. |

#### Inputs/Outputs

| Parameter | Description |
| --- | --- |
| Error In | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| Error Out | error out contains error information. This output provides standard error out functionality. |

You must set the execution mode of the target to [Simulation (Simulated I/O)](/csh?context=lvfpga_lvfpgahelp_fpga_host_running). You cannot use this node with a [custom VI](/csh?context=lvfpgaconcepts_creating_test_benches) for FPGA I/O. You cannot use this node with Component-Level IP I/O. You cannot use this node with the [User-Controlled I/O Sampling](../../../targets/ni/fpga/menus/fpgacategories/programming/fpgahsio-mnu.html) functions.

If you want to simulate your code continuously, you must place your LabVIEW FPGA code inside a [While Loop.](/csh?context=lvcore_glang_while_loop)

#### Related Information

[Debugging with the FPGA Desktop Execution Node](/csh?context=lvfpga_lvfpgahelp_using_desktop_execution_node)

[Testing and Debugging LabVIEW FPGA Code](https://www.ni.com/r/FPGADENdebug)

[Using the LabVIEW FPGA Desktop Execution Node](https://www.ni.com/r/FPGADENUsing)

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\Simulation\Simulating Analog Signals with the DEN\Simulating Analog Signals with the DEN.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\Simulation\Simulating Digital Signals with the DEN\Simulating Digital Signals with the DEN.lvproj
- labview\examples\R Series\FPGA Fundamentals\Simulation\Simulating Analog Signals with the DEN\Simulating Analog Signals with the DEN.lvproj
- labview\examples\R Series\FPGA Fundamentals\Simulation\Simulating Digital Signals with the DEN\Simulating Digital Signals with the DEN.lvproj

Parent topic:

FPGA Interface

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/eio/api/nifpga-palettemergevi-ionameconstant-vi.html language=enus -->
## TOPIC 00229: FPGA I/O Constant

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/eio/api/nifpga-palettemergevi-ionameconstant-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/eio/api/nifpga-palettemergevi-ionameconstant-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA I/O constant to specify an FPGA I/O item on the block diagram. Use the Configure FPGA I/O Name Control Type dialog box to configure an FPGA I/O constant and determine which methods and properties an FPGA I/O constant supports. The shortcut menu that appears when you click inside the FPG

### FPGA I/O Constant

Use the FPGA I/O constant to specify an FPGA I/O item on the block diagram.

Use the [Configure FPGA I/O Name Control Type](/csh?context=lvfpga_lvfpgadialog_io_category) dialog box to configure an FPGA I/O constant and determine which methods and properties an FPGA I/O constant supports.

The shortcut menu that appears when you click inside the FPGA I/O constant lists only the FPGA I/O items that appear in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window under the same FPGA target as the active VI. If the FPGA I/O constant is already configured, the list displays only I/O items that support the configuration.

You also can specify an I/O item by clicking inside the FPGA I/O constant and typing the name of the I/O item.

To reference an FPGA I/O resource using the FPGA I/O constant, you must [add the I/O resource](/csh?context=lvfpga_lvfpgahelp_creating_fpgaio) under the FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window.

When creating a reusable subVI, use the [FPGA I/O control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) to specify an FPGA I/O item on the block diagram.

Note

FPGA clock constant

[IMAGE alt='icon' src='nifpga-palettemergevi-ionameconstant-vi.png']

Parent topic:

FPGA I/O

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/eio/fpganode/fpga-target-methods-properties-nodes.html language=enus -->
## TOPIC 00230: FPGA Target Methods & Properties Nodes

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/eio/fpganode/fpga-target-methods-properties-nodes.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/eio/fpganode/fpga-target-methods-properties-nodes.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA Target Methods & Properties Nodes to perform operations on FPGA targets programmatically. This palette is specific to FPGA targets, but not all FPGA targets support these functions. The functions on this palette can return general LabVIEW error codes, specific FPGA Module error codes, o

### FPGA Target Methods & Properties Nodes

Use the FPGA Target Methods & Properties Nodes to perform operations on FPGA targets programmatically.

Note

The functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes), specific [FPGA Module error codes](/csh?context=lvfpga_lvfpgahelp_fpga_error_codes), or error codes specific to the FPGA target.

- [FPGA Target Method Node](../../../../vi-lib/rvi/eio/fpganode/nifpgatargetmethod-mergevi-vi.html) Invokes a method on an FPGA target in the Project Explorer window. The available methods depend on the FPGA target and some FPGA targets do not support any methods.
- [FPGA Target Property Node](../../../../vi-lib/rvi/eio/fpganode/nifpgatargetproperty-mergevi-vi.html) Gets or sets properties on an FPGA target in the Project Explorer window. The available properties depend on the FPGA target and some FPGA targets do not support any properties.

Parent topic:

Programming

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/eio/fpganode/nifpgatargetmethod-mergevi-vi.html language=enus -->
## TOPIC 00231: FPGA Target Method Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/eio/fpganode/nifpgatargetmethod-mergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/eio/fpganode/nifpgatargetmethod-mergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes a method on an FPGA target in the Project Explorer window. The available methods depend on the FPGA target and some FPGA targets do not support any methods. To select a method, click the Method section of the FPGA Target Method Node and select a method from the shortcut menu. icon The FPGA T

### FPGA Target Method Node

Invokes a method on an FPGA target in the [Project Explorer](/csh?context=lvcore_lvdialog_project_explorer_window) window. The available methods depend on the FPGA target and some FPGA targets do not support any methods.

To select a method, click the **Method** section of the FPGA Target Method Node and select a method from the shortcut menu.

[IMAGE alt='icon' src='nifpgatargetmethod-mergevi-vi.png']

The FPGA Target Method Node is an [FPGA I/O Method Node](../../../eio/eiomethodnode/eiomethodnode-xnode.html) configured for the FPGA target in the project. You can only configure the node for the FPGA target that contains the VI in which this node is placed.

Support for certain methods inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) varies by target. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for more information.

Additional parameters vary depending on the related method. A method can have zero or more parameters.

**Error Handling Details**

You can right-click the FPGA Target Method Node on the block diagram and select **Show Error Terminals** from the shortcut menu to add standard LabVIEW **error in** and **error out** parameters to the function. You can use the error terminals to place this node in the data flow of the VI as well as to ensure the data you receive is valid. FPGA targets might report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Parent topic:

FPGA Target Methods & Properties Nodes

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/eio/fpganode/nifpgatargetproperty-mergevi-vi.html language=enus -->
## TOPIC 00232: FPGA Target Property Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/eio/fpganode/nifpgatargetproperty-mergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/eio/fpganode/nifpgatargetproperty-mergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets properties on an FPGA target in the Project Explorer window. The available properties depend on the FPGA target and some FPGA targets do not support any properties. To select a property, click the Property section and select a property from the shortcut menu. To add additional propertie

### FPGA Target Property Node

Gets or sets properties on an FPGA target in the [Project Explorer](/csh?context=lvcore_lvdialog_project_explorer_window) window. The available properties depend on the FPGA target and some FPGA targets do not support any properties.

To select a property, click the **Property** section and select a property from the shortcut menu. To add additional properties, right-click the **Property** section and select **Add Element** from the shortcut menu. You also can expand or contract the node by dragging the upper or lower edge of the node with the Positioning tool. To specify whether this node sets or returns a property, right-click an element in the **Property** section of the node and select **Change to Write** or **Change to Read** from the shortcut menu.

[IMAGE alt='icon' src='nifpgatargetproperty-mergevi-vi.png']

The FPGA Target Method Node is an [FPGA I/O Method Node](../../../eio/eiomethodnode/eiomethodnode-xnode.html) configured for the FPGA target in the project. You can configure this node for only the FPGA target that contains the VI on which the node is placed.

Support for use of the FPGA Target Property Node and specific properties inside and outside the [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop) varies by target. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for more information.

**Error Handling Details**

You can right-click the FPGA Target Property Node on the block diagram and select **Show Error Terminals** from the shortcut menu to add standard LabVIEW **error in** and **error out** parameters to the function. If an error occurs, you may receive incorrect data. Add error terminals to be sure the data you receive is valid. FPGA targets may report errors differently. Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about how specific FPGA targets report errors.

Note

error in

error out

error in

error out

Parent topic:

FPGA Target Methods & Properties Nodes

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/clear-fifo-method.html language=enus -->
## TOPIC 00233: Clear (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/clear-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/clear-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a target-scoped or VI-defined FIFO on the FPGA. You cannot use this method with DMA FIFOs or peer-to-peer FIFOs. To clear DMA FIFOs from the host VI, use the Stop method on the Invoke Method function. To clear peer-to-peer FIFOs, use the Peer-to-peer streaming VIs and functions. Use the FIFO

### Clear (FIFO Method)

[Clears](/csh?context=lvfpga_lvfpgahelp_clearing_fpga_fifos) a target-scoped or VI-defined FIFO on the FPGA.

You cannot use this method with DMA FIFOs or peer-to-peer FIFOs. To clear DMA FIFOs from the host VI, use the Stop method on the [Invoke Method](../../interface/nirvimethod/nirvimethod-xnode.html) function. To clear peer-to-peer FIFOs, use the [Peer-to-peer streaming](/csh?context=lvcore_p2pstream_p2pstream) VIs and functions.

Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |

The following [types of FIFOs](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data) support this method:

- Target-scoped
- VI-defined

#### Considerations for Single-Cycle Timed Loops

You cannot use the Clear method inside a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop). However, when FIFOs are configured as **Block Memory**, you can use the Clear method in the top-level clock domain, even if the top-level clock domain is different than the clock domain(s) specified by the single-cycle Timed Loop(s) in which the FIFO [Write](/csh?context=lvfpga_lvfpga_fifo_write) and [Read](/csh?context=lvfpga_lvfpga_fifo_read) methods are used.

#### Considerations When Using the Clear Method with Built-in FIFOs

If the FIFO uses built-in controller logic, the Clear method takes multiple clock cycles because it clears elements one by one instead of simultaneously. The Clear method also increases resource usage and may reduce the maximum frequency of the clock domain that contains the FIFO.

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/disable-fifo-method.html language=enus -->
## TOPIC 00234: Disable (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/disable-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/disable-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the peer-to-peer writer and reader FIFOs in a peer-to-peer streaming session. Wiring either a writer or reader FIFO to this node disables both the writer and reader in the streaming session. Data in the writer FIFO that has not transferred to the reader FIFO is lost. To send all data in the

### Disable (FIFO Method)

Disables the peer-to-peer writer and reader FIFOs in a [peer-to-peer streaming session](/csh?context=lvfpga_lvfpgahelp_fpga_p2p_intro). Wiring either a writer or reader FIFO to this node disables both the writer and reader in the streaming session.

Data in the writer FIFO that has not transferred to the reader FIFO is lost. To send all data in the writer FIFO to the reader FIFO before disabling the FIFOs, use the [Flush and Disable](/csh?context=lvfpga_lvfpga_fpga_fifo_flushdisable) method. The Disable method does not clear data in the reader FIFO. Therefore, you can read any data left in the reader FIFO after this node runs and the peer-to-peer stream is disabled.

This node waits until both the writer and reader FIFOs are disabled. If the peer-to-peer stream is in a disabled or unlinked state already, this node does nothing.

This method is only available with peer-to-peer FIFOs. Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |

#### Considerations for Single-Cycle Timed Loops

Because this node waits until the peer-to-peer writer and reader FIFOs are disabled, you cannot use this node in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop). If you use this node in a single-cycle Timed Loop, LabVIEW reports a code generation error when you try to compile the FPGA VI.

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/enable-fifo-method.html language=enus -->
## TOPIC 00235: Enable (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/enable-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/enable-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears and enables the peer-to-peer writer and reader FIFOs in a peer-to-peer streaming session. Wiring either a writer or reader FIFO to this node enables both the writer and reader in the streaming session. This node waits until both the writer and reader FIFOs are enabled. If the peer-to-peer str

### Enable (FIFO Method)

Clears and enables the peer-to-peer writer and reader FIFOs in a [peer-to-peer streaming session](/csh?context=lvfpga_lvfpgahelp_fpga_p2p_intro). Wiring either a writer or reader FIFO to this node enables both the writer and reader in the streaming session.

This node waits until both the writer and reader FIFOs are enabled. If the peer-to-peer stream is already in an enabled state, this node does nothing.

This method is only available with peer-to-peer FIFOs. Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |

#### Considerations for Single-Cycle Timed Loops

Because this node waits until the peer-to-peer reader and writer FIFOs are enabled, you cannot use this node in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop). If you use this node in a single-cycle Timed Loop, LabVIEW reports a code generation error when you try to compile the FPGA VI.

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/flush-and-disable-fifo-method.html language=enus -->
## TOPIC 00236: Flush and Disable (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/flush-and-disable-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/flush-and-disable-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Flushes a peer-to-peer writer FIFO and then disables the peer-to-peer writer and reader FIFOs in a peer-to-peer streaming session. Wiring either a writer or reader FIFO to this node disables both the writer and reader in the streaming session. This method writes all data from the writer FIFO to the

### Flush and Disable (FIFO Method)

Flushes a peer-to-peer writer FIFO and then disables the peer-to-peer writer and reader FIFOs in a [peer-to-peer streaming session](/csh?context=lvfpga_lvfpgahelp_fpga_p2p_intro). Wiring either a writer or reader FIFO to this node disables both the writer and reader in the streaming session. This method writes all data from the writer FIFO to the reader FIFO before disabling the FIFOs. To flush a peer-to-peer writer FIFO without disabling the writer and reader FIFOs, use the [Flush](/csh?context=lvfpga_lvfpga_fpga_fifo_flush) method. To disable the FIFOs without flushing the writer, use the [Disable](/csh?context=lvfpga_lvfpga_fpga_fifo_disable) method.

This node waits until both the writer and reader FIFOs are disabled. If the peer-to-peer stream is already in a disabled or unlinked state, this node does nothing. The Flush and Disable method does not clear data in the reader FIFO. Therefore, you can read any data left in the reader FIFO after this node runs and the peer-to-peer stream is disabled.

This method is only available with peer-to-peer FIFOs. Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| Timeout | Timeout specifies the time, in number of clock ticks, that the method waits to flush all data from the writer FIFO and write the data to the reader FIFO.A Timeout value of –1 waits indefinitely for the flush to complete. A value of 0 specifies that this node does not wait. A value greater or equal to 1 specifies the number of clock cycles to wait for the flush to complete. If the flush does not finish before the Timeout value, Timed out? returns TRUE. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |
| Timed Out? | Timed Out? returns TRUE if the flush did not complete before the time limit. Otherwise, Timed Out? is FALSE. If Timed Out? is TRUE, data remaining in the writer FIFO is lost. |

#### Considerations for Single-Cycle Timed Loops

Because this node waits until the peer-to-peer writer and reader FIFOs are disabled, you cannot use this node in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop). If you use this node in a single-cycle Timed Loop, LabVIEW reports a code generation error when you try to compile the FPGA VI.

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/flush-fifo-method.html language=enus -->
## TOPIC 00237: Flush (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/flush-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/flush-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Flushes data from a DMA target-to-host FIFO to the host or from a peer-to-peer writer FIFO to the peer-to-peer reader FIFO. You must enable the peer-to-peer stream when flushing a peer-to-peer writer FIFO. Otherwise, the Flush method does nothing. To flush a peer-to-peer writer FIFO and then disable

### Flush (FIFO Method)

Flushes data from a DMA target-to-host FIFO to the host or from a peer-to-peer writer FIFO to the peer-to-peer reader FIFO. You must enable the peer-to-peer stream when flushing a peer-to-peer writer FIFO. Otherwise, the Flush method does nothing. To flush a peer-to-peer writer FIFO and then disable the peer-to-peer writer and reader FIFOs, use the [Flush and Disable](/csh?context=lvfpga_lvfpga_fpga_fifo_flushdisable) method.

Note

Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |

You can use the Flush method to flush FIFOs with the handshaking interface and the timeout interface. The Flush method functions regardless of the status of the [Write](/csh?context=lvfpga_lvfpga_fifo_write) method. For example, the flush still works in the following situations:

- The Timed Out? output of the Write method returns TRUE when you use the Flush method.
- The Ready for Input output of the Write method returns FALSE when you use the Flush method.

If you use the Flush method when another FIFO flush is in progress, LabVIEW merges both flushes.

#### Considerations for Single-Cycle Timed Loops

If you use the Flush method in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop), the Flush method must be in the same clock domain as the Write method. Otherwise, LabVIEW returns a code generation error when you try to compile the FPGA VI.

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/get-number-of-elements-to-read-fifo-method.html language=enus -->
## TOPIC 00238: Get Number of Elements to Read (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/get-number-of-elements-to-read-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/get-number-of-elements-to-read-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of elements remaining to be read in the FPGA FIFO. You must use this node in the same clock domain as the clock domain containing the FIFO Method Node configured with the Read method. Use the FIFO Method Node to invoke this method. Inputs/Outputs Option Description FIFO In FIFO In

### Get Number of Elements to Read (FIFO Method)

Returns the number of elements remaining to be read in the FPGA FIFO. You must use this node in the same clock domain as the clock domain containing the FIFO Method Node configured with the [Read](/csh?context=lvfpga_lvfpga_fifo_read) method.

Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to invoke this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |
| Number of Elements to Read | Number of Elements to Read—Returns the number of remaining elements for the application to read from the FIFO.The number of elements that this method returns is less than or equal to the actual number of elements remaining in the FIFO. |

You can use the following [types of FIFOs](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data) in this method:

- Target-scoped
- VI-defined
- DMA
- Peer-to-peer

(Xilinx Vivado) This method does not support FIFOs with the built-in control logic or implemented using UltraRAM.

The sum of the values returned from this method and [Get Number of Elements to Write](/csh?context=lvfpga_lvfpga_fpga_fifo_num_elem_write) method is less than or equal to the total number of elements in the FIFO. You can use this method to ensure that the FIFO can handle bursts of elements before the Read method times out.

Note

Get Number of Elements to Write

Get Number of Elements to Read

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/get-number-of-elements-to-write-fifo-method.html language=enus -->
## TOPIC 00239: Get Number of Elements to Write (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/get-number-of-elements-to-write-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/get-number-of-elements-to-write-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of empty element slots available to be written to in the FPGA FIFO. You must use this node in the same clock domain as the clock domain containing the FIFO Method Node configured with the Write method. Use the FIFO Method Node to implement this method. Inputs/Outputs Option Descri

### Get Number of Elements to Write (FIFO Method)

Returns the number of empty element slots available to be written to in the FPGA FIFO. You must use this node in the same clock domain as the clock domain containing the FIFO Method Node configured with the [Write](/csh?context=lvfpga_lvfpga_fifo_write) method.

Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |
| Number Of Elements to Write | Number Of Elements to Write—Returns the number of empty element slots available to be written to in the FPGA FIFO.The number of elements that this method returns is less than or equal to the actual number of elements available to write to the FIFO. Note This method may generate different output values when executed in simulation mode versus on hardware. In simulation mode, the output value of this method is the actual number. On hardware, block memory FIFOs implemented using slice fabric control logic include an additional buffer. This additional buffer contains five elements when the FIFO reader and writer are in the same clock domain, or six elements when they are in different clock domains. On hardware, this method does not report the number of elements available in the additional buffer. If the FIFO contains less elements than the depth of the additional buffer, the output value of this method is less than the actual number of elements available to write. Otherwise, the output value of this method is the actual number. |

You can use the following [types of FIFOs](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data) in this method:

- Target-scoped
- VI-defined
- DMA
- Peer-to-peer

(Xilinx Vivado) This method does not support FIFOs with the built-in control logic or implemented using UltraRAM.

The sum of the values returned from this method and the [Get Number of Elements to Read](/csh?context=lvfpga_lvfpga_fpga_fifo_num_elem_read) method is less than or equal to the total number of elements in the FIFO. You can use this method to ensure that the FIFO can handle bursts of elements before the Write method times out.

Note

Get Number of Elements to Write

Get Number of Elements to Read

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/get-stream-state-fifo-method.html language=enus -->
## TOPIC 00240: Get Stream State (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/get-stream-state-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/get-stream-state-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the state of the peer-to-peer streaming session. This method is only available with peer-to-peer FIFOs. Use the FIFO Method Node to implement this method. Inputs/Outputs Option Description FIFO In FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configur

### Get Stream State (FIFO Method)

Returns the state of the [peer-to-peer streaming session](/csh?context=lvfpga_lvfpgahelp_fpga_p2p_intro).

This method is only available with peer-to-peer FIFOs. Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |
| State | State returns the state of the peer-to-peer stream. The state models for peer-to-peer streaming coordinate the writer, reader, and host. 0Unlinked 1Disabled 2Enabled 3Flushing |
| 0 | Unlinked |
| 1 | Disabled |
| 2 | Enabled |
| 3 | Flushing |

#### Considerations for Single-Cycle Timed Loops

If you use this node in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop), the Get Stream State method must be in the same [clock domain](/csh?context=lvfpga_lvfpgaconcepts_implementing_domains) as the [Read](/csh?context=lvfpga_lvfpga_fifo_read) or [Write](/csh?context=lvfpga_lvfpga_fifo_write) method or the [Enable](/csh?context=lvfpga_lvfpga_fpga_fifo_enable) or [Disable](/csh?context=lvfpga_lvfpga_fpga_fifo_disable) method for the peer-to-peer writer or reader FIFO.

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-fifonameconstant-vi.html language=enus -->
## TOPIC 00241: FIFO Constant

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-fifonameconstant-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-fifonameconstant-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FIFO constant to specify a FIFO item on the block diagram. Use the Configure FIFO Name Control Type dialog box to configure the FIFO constant. To reference a FIFO resource using the FIFO constant, you must add a target-scoped, DMA, or peer-to-peer FIFO under the FPGA target in the Project Ex

### FIFO Constant

Use the FIFO constant to specify a FIFO item on the block diagram.

Use the [Configure FIFO Name Control Type](/csh?context=lvfpga_lvfpgadialog_fpga_fifo_name_control_db) dialog box to configure the FIFO constant.

To reference a FIFO resource using the FIFO constant, you must [add a target-scoped, DMA, or peer-to-peer FIFO](/csh?context=lvfpga_lvfpgaconcepts_fpga_transfer_data) under the FPGA target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window.

The pull-down menu that appears when you click the arrow on the FIFO constant lists only the FIFO items that appear in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window under the same FPGA target as the active VI and that match the configuration of the constant. When you select an item from the pull-down menu, the configuration of the constant matches the configuration of the item you select from the pull-down menu.

You also can use the [FIFO control](/csh?context=lvfpga_lvfpgaconcepts_fpga_name_controls) to specify a FIFO item on the block diagram.

Note

FPGA clock constant

FPGA I/O constant

Memory constant

[IMAGE alt='icon' src='nirvififopalette-mergevi-fifonameconstant-vi.png']

Parent topic:

Data Storage & Transfer

Parent topic:

FIFO

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-vi.html language=enus -->
## TOPIC 00242: FIFO Method Node

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/nirvififopalette-mergevi-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invokes a FIFO method on an FPGA VI. You must specify a FIFO before specifying a method. The available methods vary depending on the FPGA target and the type of FIFO. Refer to the specific FPGA target hardware documentation for information about the FIFO methods you can use. icon Inputs/Outputs cgen

### FIFO Method Node

Invokes a FIFO method on an FPGA VI. You must specify a FIFO before specifying a method. The available methods vary depending on the FPGA target and the type of FIFO.

Refer to the specific FPGA target [hardware documentation](/csh?context=lvfpga_lvfpgahelp_fpga_target_docs) for information about the FIFO methods you can use.

[IMAGE alt='icon' src='nirvififopalette-mergevi-vi.png']

#### Inputs/Outputs

| FIFO In — specifies the FIFO. You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. FIFO Out — returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |
| --- |

To use the FIFO Method Node, you first must [create a FIFO](/csh?context=lvfpga_lvfpgahelp_fpga_creating_fifos). After creating a FIFO, add a FIFO Method Node to the block diagram, right-click the node, and select the FIFO from the **Select FIFO** shortcut menu. Unless the FIFO is a VI-defined FIFO, you can also drag the FIFO from the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window to the block diagram to place the configured FIFO Method Node on the block diagram.

When you wire a FIFO to **FIFO In**, LabVIEW renames the FIFO Method Node to FIFO Item to indicate that the node is now associated with a FIFO in the project. If **FIFO In** is unwired, you can right-click the FIFO Method Node and select **Find Item in Project** from the shortcut menu to highlight the FIFO in the **Project Explorer** window.

#### Selecting an Interface

You can [select between the timeout and handshaking](/csh?context=lvfpga_lvfpgaconcepts_fpga_interface_options) interfaces by right-clicking a FIFO Method Node that invokes a Read or Write method and selecting **Interface»Timeout** or **Interface»Handshaking** from the shortcut menu.

By default, FIFO methods use the timeout interface, which allows you to specify a time, in number of clock ticks, that the method waits to complete an operation before it returns a timeout. The timeout interface helps you handle unresponsive devices or sections of code. However, if you use a Read or Write method within a single-cycle Timed Loop, you can enable the handshaking interface to facilitate communication between upstream and downstream nodes in high throughput applications. The handshaking interface reduces the amount of logic needed to implement a [handshaking protocol](/csh?context=lvfpga_lvfpgaconcepts_fpga_handshaking).

Note

#### Displaying Error-Handling Terminals

If an error occurs, you might receive incorrect data. Add error terminals to ensure the data you receive is valid. You also can add error terminals to place the FIFO Method Node in the data flow. Right-click the FIFO Method Node and select **Show Error Terminals** from the shortcut menu to add standard LabVIEW **error in** and **error out** parameters to the function.

Note

error in

error out

error in

error out

To use the FIFO Method Node in the data flow without using error terminals, include the node in a [Flat Sequence](/csh?productcategories=147794&context=lvcore_glang_flat_sequence) or [Stacked Sequence](/csh?productcategories=147794&context=lvcore_glang_flat_sequence) structure.

Parent topic:

Data Storage & Transfer

Parent topic:

FIFO

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/read-fifo-method.html language=enus -->
## TOPIC 00243: Read (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/read-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/read-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads and removes the oldest element(s) from the FPGA FIFO. Configure the number of elements per read from the Interfaces page of the FIFO Properties dialog box. Use the FIFO Method Node to implement this method. The input and outputs available for this method depend on if you select the timeout or

### Read (FIFO Method)

Reads and removes the oldest element(s) from the FPGA FIFO. Configure the number of elements per read from the [Interfaces](/csh?context=lvfpga_lvfpgadialog_fifo_adv_code_gen) page of the [FIFO Properties](/csh?context=lvfpga_lvfpgadialog_edit_fifo) dialog box.

Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

The input and outputs available for this method depend on if you [select the timeout or handshaking](/csh?context=lvfpga_lvfpgaconcepts_fpga_interface_options) interface.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| Timeout | Timeout specifies the time, in number of clock ticks, that the method waits for available data in the FIFO if the FIFO is empty. A value of –1 prevents the function from timing out, so the function completes execution only when data is available for reading. A value of 0 indicates that the function does not wait. Wire a constant of 0 to Timeout if you use the FIFO Method Node in a single-cycle Timed Loop.This input is the default for the Read method. To display this input, right-click the Read method and select Interface»Timeout from the shortcut menu. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |
| Element | Element returns the oldest data element or elements in the FIFO.The Element data type is the data type you configure in the FIFO Properties dialog box when you create the FIFO. If the FIFO is empty, Element is undefined and no read occurs. |
| Timed Out? | Timed Out? returns TRUE if an element is not available in the FIFO before the function completes execution. If Timed Out? is TRUE, Element is undefined and no read occurs. Note (Xilinx Vivado) In simulation mode, if the FIFO is implemented with the built-in control logic, the Timed Out? value might not reflect the actual behavior on hardware because this method uses Actual Number of Elements in the General Page of the FIFO Properties dialog box as the FIFO depth, which might be smaller than the actual number of elements in the FIFO. This output is the default for the Read method. To display this output, right-click the Read method and select Interface»Timeout from the shortcut menu. |
| Ready for Output | Ready for Output specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the Ready for Input output of a downstream node to this input of the current node. Note If Ready for Output is FALSE during a given cycle, the Output Valid terminal returns FALSE during the given cycle. To display this handshaking terminal, right-click the Read method within a single-cycle Timed Loop and select Interface»Handshaking from the shortcut menu. |
| Output Valid | Output Valid returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the Input Valid input of a downstream node to transfer data from this node to the downstream node. To display this handshaking terminal, right-click the Read method within a single-cycle Timed Loop and select Interface»Handshaking from the shortcut menu. |

If you use this method in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop), you must set the **Read** option on the [Interfaces](/csh?context=lvfpga_lvfpgadialog_fifo_adv_code_gen) page of the **FIFO Properties** dialog box to **Arbitrate if Multiple Requestors Only** or **Never Arbitrate** for the FIFO item you read. When you set the **Read** option to **Arbitrate if Multiple Requestors Only**, you cannot use multiple FIFO Method Nodes configured with the Read method to access the same FIFO in the FPGA VI.

If you enable the timeout interface for this method within a single-cycle Timed Loop, you also must wire a constant of 0 to **Timeout**. If the FIFO is empty, the method executes and returns a timeout instead of valid data. The method continues to return a timeout until data is available to read.

You can use the handshaking interface only within a single-cycle Timed Loop. Additionally, some targets do not support the handshaking interface for peer-to-peer and DMA FIFOs. LabVIEW returns a compile time error for FIFOs that do not support the handshaking interface.

You can use FIFOs to [transfer data among multiple clock domains](/csh?context=lvfpga_lvfpgaconcepts_implementing_domains).

#### Related Information

[Understanding Arbitration Options](/csh?context=lvfpga_lvfpgaconcepts_arbitration_options)

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fifo/fifo-common/write-fifo-method.html language=enus -->
## TOPIC 00244: Write (FIFO Method)

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fifo/fifo-common/write-fifo-method.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fifo/fifo-common/write-fifo-method.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an element or elements to an FPGA FIFO. Configure the number of elements per write from the Interfaces page of the FIFO Properties dialog box. Use the FIFO Method Node to implement this method. The inputs and outputs available for this method depend on if you select the timeout or handshaking

### Write (FIFO Method)

Writes an element or elements to an FPGA FIFO. Configure the number of elements per write from the [Interfaces](/csh?context=lvfpga_lvfpgadialog_fifo_adv_code_gen) page of the [FIFO Properties](/csh?context=lvfpga_lvfpgadialog_edit_fifo) dialog box.

Use the [FIFO Method Node](nirvififopalette-mergevi-vi.html) to implement this method.

The inputs and outputs available for this method depend on if you [select the timeout or handshaking](/csh?context=lvfpga_lvfpgaconcepts_fpga_interface_options) interface.

#### Inputs/Outputs

| Option | Description |
| --- | --- |
| FIFO In | FIFO In specifies the FIFO.You can wire a FIFO control, FIFO constant, VI-Defined FIFO Configuration node, or the FIFO Out terminal of another FIFO Method Node to FIFO In. |
| Element | Element specifies the data element or elements you want to store in the FIFO. The Element data type is the data type you configure in the FIFO Properties dialog box when you create the FIFO. |
| Timeout | Timeout specifies the time, in number of clock ticks, that the method waits for available space in the FIFO if the FIFO is full. A value of –1 prevents the function from timing out. A value of 0 indicates no wait. Wire a constant of 0 to Timeout if you use the FIFO Method Node in a single-cycle Timed Loop.This input is the default for the Write method. To display this input, right-click the Write method and select Interface»Timeout from the shortcut menu. |
| FIFO Out | FIFO Out returns FIFO In if FIFO In is wired. Otherwise, FIFO Out returns the FIFO that you specify in the FIFO Method Node. |
| Timed Out? | Timed Out? returns TRUE if space in the FIFO is not available before the function completes execution. If Timed Out? is TRUE, the function does not write Element to the FIFO. Note (Xilinx Vivado) In simulation mode, if the FIFO is implemented with the built-in control logic, the Timed Out? value might not reflect the actual behavior on hardware because this method uses Actual Number of Elements in the General Page of the FIFO Properties dialog box as the FIFO depth, which might be smaller than the actual number of elements in the FIFO. This output is the default for the Write method. To display this output, right-click the Write method and select Interface»Timeout from the shortcut menu. |
| Input Valid | Input Valid specifies whether the next data point has arrived for processing. Wire the Output Valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshaking terminal, right-click the Write method within a single-cycle Timed Loop and select Interface»Handshaking from the shortcut menu. |
| Ready for Input | Ready for Input returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the Ready for Output input of an upstream node. To display this handshaking terminal, right-click the Write method within a single-cycle Timed Loop and select Interface»Handshaking from the shortcut menu. |

If you use this method in a [single-cycle Timed Loop](/csh?context=lvfpga_lvfpga_fpga_timed_loop), you must set the **Write** option on the [Interfaces](/csh?context=lvfpga_lvfpgadialog_fifo_adv_code_gen) page of the **FIFO Properties** dialog box to **Arbitrate if Multiple Requestors Only** or **Never Arbitrate**. When you set the **Write** option to **Arbitrate if Multiple Requestors Only**, you cannot use multiple FIFO Method Nodes configured with the Write method to access the same FIFO in the FPGA VI.

If you enable the timeout interface for this method within a single-cycle Timed Loop, you also must wire a constant of 0 to **Timeout**. If there is no data to write, the method executes and returns a timeout instead of valid data. The method continues to return a timeout until data is available to write.

You can use the handshaking interface only within a single-cycle Timed Loop. Additionally, some targets do not support the handshaking interface for peer-to-peer and DMA FIFOs. LabVIEW returns a compile time error for FIFOs that do not support the handshaking interface.

You can use FIFOs to [transfer data among multiple clock domains](/csh?context=lvfpga_lvfpgaconcepts_implementing_domains).

#### Related Information

[Understanding Arbitration Options](/csh?context=lvfpga_lvfpgaconcepts_arbitration_options)

Parent topic:

FIFO Method Node

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48e1merge-vi.html language=enus -->
## TOPIC 00245: DSP48E1

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48e1merge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48e1merge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DSP48E1 slice on a supported FPGA target. You can use this function on the following FPGA targets: Virtex-6, Kintex-7, and Zynq. This help file is not intended to be a comprehensive discussion of DSP48E or DSP48E1 slices. Before using these functions, NI recommends you become familiar w

### DSP48E1

Represents a [DSP48E1 slice](/csh?context=lvfpga_lvfpgaconcepts_dsp48e_top) on a supported FPGA target. You can use this function on the following FPGA targets: Virtex-6, Kintex-7, and Zynq.

Note

Virtex-6 FPGA DSP48E1 Slice User Guide

www.xilinx.com

[IMAGE alt='icon' src='dsp48e1merge-vi.png']

#### Inputs/Outputs

| a — b — c — p — |
| --- |

Parent topic:

Basic Elements

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48emerge-vi.html language=enus -->
## TOPIC 00246: DSP48E

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48emerge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/basic-elements/dsp48e/wrap/dsp48emerge-vi.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DSP48E slice on a supported FPGA target. You can use this function on the following FPGA targets: Virtex-5, Virtex-6, Kintex-7, and Zynq. This help file is not intended to be a comprehensive discussion of DSP48E slices. Before using this function, NI recommends you become familiar with

### DSP48E

Represents a [DSP48E slice](/csh?context=lvfpga_lvfpgaconcepts_dsp48e_top) on a supported FPGA target. You can use this function on the following FPGA targets: Virtex-5, Virtex-6, Kintex-7, and Zynq.

Note

Virtex-5 FPGA XtremeDSP Design Considerations User Guide

www.xilinx.com

[IMAGE alt='icon' src='dsp48emerge-vi.png']

#### Inputs/Outputs

| a — b — c — p — |
| --- |

Parent topic:

Basic Elements

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/basic-elements/fxpaddsub/xnode/nifxpmath-addsub-xnode.html language=enus -->
## TOPIC 00247: AddSub

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/basic-elements/fxpaddsub/xnode/nifxpmath-addsub-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/basic-elements/fxpaddsub/xnode/nifxpmath-addsub-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements an adder-subtractor that operates on bit patterns. You can cascade AddSub functions and pipeline them to achieve higher throughput rates. This function supports scalar Boolean values, arrays of Boolean values, and scalar values of integer and fixed-point data types. icon Dialog Box Option

### AddSub

Implements an adder-subtractor that operates on bit patterns. You can cascade AddSub functions and pipeline them to achieve higher throughput rates.

This function supports scalar Boolean values, arrays of Boolean values, and scalar values of integer and fixed-point data types.

[IMAGE alt='icon' src='nifxpmath-addsub-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Data Type | Specifies the data type of the input and output terminals. LabVIEW enables different options depending on the data types you wire to the x and y input terminals. Signed— (default)Specifies that the terminals are signed. Unsigned—Specifies that the terminals are unsigned. Word length—Specifies the word length between 1 and 65535 bits. The default value is 16 bits. |
| Operation | Specifies the operation this function performs on x and y. Add—Specifies that this function computes x + y. Subtract—Specifies that this function computes x – y. Add/Subtract—(default) Displays the is sub? input terminal. Use this terminal to specify programmatically whether this function computes x + y or x – y. |
| Optional Terminals | Specifies whether LabVIEW displays several optional block diagram terminals. The options in this section change based on the Operation you specify. By default, all checkboxes contain checkmarks. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| use zero instead of x — Specifies whether this function ignores the value you wire to the x input terminal. If use zero instead of x is TRUE, the function uses a value of 0 instead of the value you wire to x. If use zero instead of x is FALSE, the function uses the value you wire to x input terminal. Use this terminal to remove x from the expression this function calculates. For example, use this terminal to return –y instead of x – y.LabVIEW displays this terminal only if you place a checkmark in the Use zero instead of x checkbox in the Optional Terminals section. x — Specifies an input to this function. If x is a fixed-size Boolean array, the first array element represents the least-significant bit (LSB) and the last element represents the most-significant bit (MSB). y — Specifies an input to this function. If y is a fixed-size Boolean array, the first array element represents the LSB and the last element represents the MSB. is sub? — Specifies whether this function performs subtraction or addition. If is sub? is TRUE, this function calculates x – y. If is sub? is FALSE, this function calculates x + y. Use this terminal to change the operation of this function programmatically. LabVIEW displays this terminal only if the Operation is Add/Subtract. carry-in/inverted borrow-in — Specifies whether this function accounts for an additional LSB. For example, the LSB could come from the bit pattern of the carry-out/inverted borrow-out terminal of an upstream AddSub function. If is sub? is FALSE and carry-in/inverted borrow-in is TRUE, this function adds one extra LSB to x + y. If is sub? is TRUE and carry-in/inverted borrow-in is FALSE, this function subtracts one extra LSB from x – y. LabVIEW displays this terminal only if the Operation is Add/Subtract and you place a checkmark in the Carry-in/inverted borrow-in checkbox in the Optional Terminals section. carry-in — Specifies whether this function accounts for an additional LSB. For example, the LSB could come from the bit pattern of the carry-out terminal of an upstream AddSub function. If carry-in is TRUE, this function adds one extra LSB to x + y. If carry-in is FALSE, this function just computes x + y. LabVIEW displays this terminal only if the Operation is Add and you place a checkmark in the Carry-in checkbox in the Optional Terminals section. borrow-in — Specifies whether this function accounts for an additional LSB. For example, the LSB could come from the bit pattern of the borrow-out terminal of an upstream AddSub function. If borrow-in is TRUE, this function subtracts one extra LSB from x – y. If borrow-in is FALSE, this function just computes x – y. LabVIEW displays this terminal only if the Operation is Subtract and you place a checkmark in the Borrow-in checkbox in the Optional Terminals section. overflow — Returns TRUE if the encoding is Signed and the theoretical computed value of s exceeds the valid range of the data type of s. In this situation, this function wraps the value of s. Note If you cascade functions, you must use unsigned functions in the intermediate operations. Then set the encoding of the final function to the encoding you want for the entire cascaded operation. carry-out/inverted borrow-out — Returns TRUE if the data type of s cannot represent the result of an unsigned addition operation. This terminal returns FALSE if the data type of s cannot represent the result of an unsigned subtraction operation. In this situation, this function wraps the value of s. If you cascade this function, you can use this terminal to specify whether a downstream function carries or borrows a value. To specify that a downstream function uses this value, wire the carry-out/inverted borrow-out output terminal to the carry-in/inverted borrow-in input terminal of the downstream function. LabVIEW displays this terminal only if the Data Type is Unsigned and the Operation is Add/Subtract. carry-out — Returns TRUE if the data type of s cannot represent the result of an unsigned addition operation. In this situation, the bit pattern of carry-out stores the most significant bit of the addition operation. To build a cascaded adder, you can carry this value forward to a downstream AddSub function by wiring this terminal to the carry-in input terminal of the downstream function. carry-out returns FALSE if the function does not need to carry a value forward. LabVIEW displays this terminal only if the Data Type is Unsigned and the Operation is Add. borrow-out — Returns TRUE if the data type of s cannot represent the result of an unsigned subtraction operation. In this situation, the bit pattern of borrow-out stores the most significant bit of the subtraction operation. To build a cascaded subtractor, you can borrow this value forward to a downstream AddSub function by wiring this terminal to the borrow-in input terminal of the downstream function. borrow-out returns FALSE if the function does not need to borrow a value forward. LabVIEW displays this terminal only if the Data Type is Unsigned and the Operation is Subtract. s — Returns the result this function computes. The result depends on not only the values of x and y, but also the values of any Boolean input terminals this function displays. Note This function applies the Wrap overflow mode to s in the following situations: carry-out, borrow-out, or overflow returns TRUE is sub? is TRUE and carry-out/inverted borrow out returns FALSE is sub? is FALSE and carry-out/inverted borrow out returns TRUE |
| --- |

This function makes full use of lookup tables ([LUTs](/csh?productcategories=147794&context=lvcore_lvfpgaconcepts_fpga_basic_chip_terms)) to reduce FPGA resource usage. This function also uses dedicated carry logic on the FPGA to improve execution speed.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Efficient Adders\Efficient Adders.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Efficient Adders\Efficient Adders.lvproj

Parent topic:

Basic Elements

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/basic-elements/fxpdiscretedelay/xnode/nifxpmath-discretedelay-xnode.html language=enus -->
## TOPIC 00248: Discrete Delay

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/basic-elements/fxpdiscretedelay/xnode/nifxpmath-discretedelay-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/basic-elements/fxpdiscretedelay/xnode/nifxpmath-discretedelay-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delays input value for a number of loop iterations. This VI is analogous to a z^-n block where n can be constant or variable. This function supports scalar and array values of integer, fixed-point, and Boolean data types, clusters, and arrays of clusters. icon Dialog Box Options Parameter Descriptio

### Discrete Delay

Delays input value for a number of loop iterations. This VI is analogous to a z^-n block where n can be constant or variable.

This function supports scalar and array values of integer, fixed-point, and Boolean data types, clusters, and arrays of clusters.

[IMAGE alt='icon' src='nifxpmath-discretedelay-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| General | Specifies general information about this function. Data Type—Contains information about the data type of the D input terminal. Width—Specifies the number of bits of D, which affects the number of internal registers this function creates. If you wire an integer or a fixed-point data type to D, LabVIEW dims this option and sets it to the word length of the data type you wire. If you wire a Boolean, cluster, or fixed-size array, LabVIEW dims this option and sets D to the combined word length of all elements in the data type. Note The data type of D does not adapt to source. Optional Terminal—Contains information about an optional input terminal. Enable—Specifies whether LabVIEW displays the enable input terminal. By default, this checkbox does not contain a checkmark and LabVIEW sets the value of this terminal to TRUE. Delay Settings—Contains options relating to the delay. Constant delay—Specifies that this function applies a constant delay Delay—Specifies the number of clock cycles by which this function delays D. Delay must be less than or equal to 512 cycles. The default value is 1 cycle. Dynamic delay—Specifies that this function applies a variable delay. Maximum delay—Specifies the maximum number of clock cycles by which this function can delay D, which in turn specifies the number of internal registers this function uses. The value must be between 16 and 512 cycles, inclusive. Use the n–1 input terminal to specify which register reaches the output terminal Q. Resulting schematic—Displays the FPGA logic of this function. The schematic changes based on the configuration options you select. |
| Initial Values | Contains settings for the initial values of the internal registers this function uses. Initialization—Specifies when and how the internal registers reset or initialize. Reset to zeros on first call—Specifies that when you first call this function or invoke the Reset method, all internal registers reset to 0. Initialize on compile or load—Specifies that when you compile or load the VI that contains this function, internal registers initialize to the values you define in the Initial Values table. This function does nothing if the FPGA is reset using the Reset method. Initialization VI—Contains options about the initialization VI LabVIEW uses to initialize the internal registers of this function. These options are available only if you select the Initialize on compile or load option in the Initialization section. VI Path—Specifies the path to the VI that provides initial values to this function. New VI from Template—Creates an instance of a template VI and opens the VI. You can use this template to create an initialization VI. You must close this configuration dialog box to edit the VI. Open VI—Opens the VI you specify in the VI Path field. You must close this dialog box to edit the VI. Run VI—Runs the VI you specify in the VI Path field and populates the Initial Values table with the values the VI returns. If the output data type of the initialization VI is different from the data type of the Discrete Delay function, LabVIEW attempts to coerce the output values to the data type of the function. If this coercion does not succeed, LabVIEW displays an error message. Initial Values—Specifies the initial values of this function in hexadecimal, decimal, or binary format. This table is available only if you select the Initialize on compile or load option in the Initialization section. If you wire a cluster or a non-Boolean fixed-size array to the D input terminal, you cannot use this table to specify initial values. Instead, you must either select the Reset to zeros on first call option or use the Initialization VI section to define custom initial values. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| D — Specifies the data to delay. Note The data type of D does not adapt to source. n-1 — Specifies the index of the internal register whose value reaches the Q output terminal. The value of n–1 can be between 0 and n–1, where n is the value of the Maximum delay control in the configuration dialog box. LabVIEW displays this terminal only if you select the Dynamic delay option in the configuration dialog box. enable — Specifies whether this function ignores the input terminal D. The default value is TRUE, which means this function shifts all values to the next internal register and takes in a value of D to the first internal register. If enable is FALSE, this function ignores D and does not shift existing values, which means the internal registers retain the value they had during the previous clock cycle. Use this terminal to operate on only valid values of D. For example, you can wire the output valid output terminal of a High Throughput Math function to this input terminal. In this situation, the Discrete Delay function takes in a value of D only if the incoming value is valid. LabVIEW displays enable only if you place a checkmark in the Enable checkbox in the configuration dialog box. If you do not display this terminal, LabVIEW sets it to TRUE internally. Q — Returns the delayed value of D. If this function is set to Constant delay, Q returns the value of the last internal register. If this function is set to Dynamic delay, Q returns the value of the register you specify with the n–1 input terminal. |
| --- |

This function implements delays by using shift register lookup tables (SRLs) instead of flip-flops. SRLs combine many delays into a single lookup table (LUT), which can reduce FPGA resource usage significantly compared to flip-flops.

#### Differences between the Discrete Delay Function and the Feedback Node

The [Feedback Node](/csh?productcategories=147794&context=lvcore_glang_feedback_node) and the Discrete Delay function are similar but have some key differences. The following table provides information about the differences between these objects.

|  | Feedback Node | Discrete Delay Function | Recommendation |
| --- | --- | --- | --- |
| Design and Features | Designed for feeding back output signals to an input.Designed for delaying an input signal by a constant number of clock cycles. | Designed for delaying an input signal by a constant or variable number of clock cycles. | Use the function that represents the use case you are programming. |
| Initialization options | Initialize internal registers to custom values on first call to the FPGA VI or when the FPGA VI resets Initialize internal registers to custom values when the FPGA VI compiles or loads or when the FPGA VI resets Initialize internal registers to custom values when the FPGA VI compiles or loads, ignoring an FPGA VI resets | Reset internal registers to zeroes on the first call to the FPGA VI or when the FPGA VI resets Initialize internal registers to custom values when the FPGA VI compiles or loads, ignoring an FPGA VI resets | The Discrete Delay implements delays by using SRLs instead of flip-flops. SRLs combine many delays into a single lookup table (LUT), which can reduce FPGA resource usage significantly compared to flip-flops. |
| Ways of defining initial values | You define initial values by wiring a value to the initializer terminal on the diagram. | You define initial values by using the Initial Values table or by using a custom initialization VI. | Use the Discrete Delay function if you have an initialization VI or if you need to delay a fixed-size array. |
| Support for dynamic delay |  |  | Use the Discrete Delay function if you need a dynamic delay. |
| Support for representing feedback on a block diagram |  |  | Use the Feedback Node if you need to represent feedback on a block diagram. |

#### Constant Delay vs. Dynamic Delay

The following example illustrates the differences between a **Constant delay** and a **Dynamic delay**.

If you set **Constant delay** to 20 clock cycles, this function creates 20 internal registers, numbered 0 through 19, to store values you wire to **D**. A value you send to **D** on the first clock cycle will be stored until the 20th clock cycle, assuming the value of the **enable** terminal is TRUE.

As you send new values to **D**, the function shifts values from one register to another. The original value you enter moves from register 0, to register 1, to register 2, and so on, until the value reaches register 19 on the 20th clock cycle. On the 21st clock cycle, the output terminal **Q** returns the value you entered during the first clock cycle. The value has been delayed for 20 clock cycles.

The function behaves similarly for a **Dynamic delay**. If you set **Maximum delay** to 20 clock cycles, the function also creates 20 registers for storing values. A value you wire to **D** moves from register 0 to register 19 with each successive clock cycle.

However, the function also displays the **n–1** input terminal, which you use to specify the number of an internal register. **Q** returns the value of this register instead of always returning the value of the last register.

For example, if 17 clock cycles have elapsed, the value of **D** you sent during the first clock cycle is in register 16. If you wire a value of 16 to **n–1** during the 18th clock cycle, the function returns this value. The value has been delayed for 17 clock cycles, not 20.

#### Simulation Export Details

This node can increase simulation run time significantly when used in conjunction with downloading, stopping, or running the FPGA VI.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Multi-Channel Averaging\Multi-Channel Averaging.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Multi-Channel Averaging\Multi-Channel Averaging.lvproj

Parent topic:

Basic Elements

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/basic-elements/fxpintaccumulator/xnode/nifxpmath-intaccumulator-xnode.html language=enus -->
## TOPIC 00249: Accumulator

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/basic-elements/fxpintaccumulator/xnode/nifxpmath-intaccumulator-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/basic-elements/fxpintaccumulator/xnode/nifxpmath-intaccumulator-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accumulates or decrements x. This function supports multi-channel operations and feedback scaling. This function supports only Boolean arrays and scalar values of integer and fixed-point data types. icon Dialog Box Options Parameter Description Fixed-Point Configuration Specifies the encodings and w

### Accumulator

Accumulates or decrements **x**. This function supports multi-channel operations and feedback scaling.

This function supports only Boolean arrays and scalar values of integer and [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data types.

[IMAGE alt='icon' src='nifxpmath-intaccumulator-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings and word lengths of the input x and the output s. The fractional word length of the output s always is equal to that of the input x. x Type—Specifies the fixed-point configuration of the x input terminal. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. s Type—Specifies the fixed-point configuration of the s output terminal. Signed—Specifies that s is signed. LabVIEW dims this option and matches the encoding of x. Unsigned—Specifies that s is unsigned. LabVIEW dims this option and matches the encoding of x. Word length—Specifies the word length of s. The value must be greater than or equal to the Word length of x. This function sets the integer word length of s internally to keep the fractional word length of s the same as the fractional word length of x. For example, if the data type of x is <+, 8, 3>, the fractional word length is 5 bits. If you set the Word length of s to 11 bits, this function sets the integer word length of s to 6 bits internally. This setting maintains a fractional word length of 5 bits in both x and s. |
| Accumulator settings | Contains settings for the accumulator. Feedback down scaling—Specifies the number of bits by which this function right-shifts the bit pattern of s before accumulating/decrementing s by x. This binary shift is an efficient way to divide s by 2^n automatically, where n is the value of this control.The value of Feedback down scaling must be less than the Word length of s or 64 bits, whichever value is smaller. The default value is 0 bits, which specifies no shift. For example, a value of 3 bits is equivalent to dividing s by 2^3, or 8, before accumulating/decrementing s by x. Number of channels—Specifies the number of channels of data on which this function operates. This function stores data from separate channels in separate internal registers. If you specify more than 1 channel, you must interleave values that you send to the x input terminal. The default value is 1 channel. Refer to the Details section for an example of using this function in a multi-channel application. Register overflow—Specifies whether this function adds an internal register before the overflow output terminal. By default, this checkbox does not contain a checkmark, which means this function returns the overflow result one clock cycle before the value of s. To return the value of overflow during the same clock cycle as the value of s, place a checkmark in this checkbox. LabVIEW displays this option only if x and s are Signed. Register carry-out/inverted borrow-out—Specifies whether this function adds an internal register before the carry-out/inverted borrow-out output terminal. By default, this checkbox does not contain a checkmark, which means this function returns the carry-out/inverted borrow-out result one clock cycle before the value of s. This situation is helpful if you are cascading Accumulator functions and do not want any delay between the carry-out/inverted borrow-out terminal of this function and the carry-in/inverted borrow-in terminal of the downstream function. To return the value of carry-out/inverted borrow-out during the same clock cycle as the value of s, place a checkmark in this checkbox. LabVIEW displays this option only if x and s are Unsigned. |
| Reset | Contains options for resetting the internal registers of this function to 0. First call—Specifies that this function resets on the first call of the FPGA VI during an execution. This option uses a few more FPGA resources than the Compile or load option does. Compile or load—Specifies that this function resets when the FPGA VI compiles or when the FPGA VI loads onto the FPGA. This function does not reset if you invoke the Reset method. This option uses fewer FPGA resources than the First call option does. Use this option to maintain an accumulated value of s between runs of the FPGA VI. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies the data to add to or subtract from the value of s. If x is a fixed-size Boolean array, the first array element represents the least-significant bit (LSB) and the last element represents the most-significant bit (MSB). A value of x applies to one channel only.Refer to the Details Details section for an example of using this function in a multi-channel application. is sub? (F) — Specifies whether this function performs subtraction or addition. If is sub? is TRUE, this function calculates s – x. If is sub? is FALSE, this function calculates s + x. Use this terminal to change the operation of this function programmatically. The default value is FALSE. load (F) — Specifies whether to start a new accumulation from 0. The default value is FALSE, which means this function adds x to, or subtracts x from, the previous value of s. If load is TRUE, this function ignores any previous value of s and begins a new accumulation by loading the value of x. Use this terminal to start a new accumulation by setting load to TRUE. Then, set load to FALSE for as long as you want a single value of s to accumulate. To restart accumulation, set load to TRUE again. In multi-channel applications, this parameter affects the channel whose data is coming into the input terminal x on the clock cycle you change the value of load. For example, if you are accumulating two channels for eight clock cycles, you could restart accumulation on channel 1 during the third clock cycle, when you receive the second value of channel 1. This change does not affect the accumulation of channel 2. enable (T) — Specifies whether this function operates on the value of the x input terminal. The default value is TRUE, which means this function reads the current value of x and uses it in accumulation. If enable is FALSE, this function ignores x and does nothing. Use this terminal to operate on only valid values of x. For example, you can wire the output valid output terminal of a High Throughput Math function to this input terminal. In this situation, the accumulator operates only if the High Throughput Math function produces a value result. In multi-channel applications, this parameter affects the channel whose data is coming into the input terminal x on the clock cycle you change the value of enable. For example, if you are accumulating two channels for eight clock cycles, x receives data from channel 1 during the first, third, fifth, and seventh clock cycles. You could skip the second value of channel 1 by setting enable to FALSE during the third clock cycle and setting it back to TRUE during the fifth clock cycle. This change does not affect channel 2. carry-in/inverted borrow-in (F) — Specifies whether this function accounts for an extra least-significant bit (LSB). For example, the LSB could come from the bit pattern of the carry-out/inverted borrow-out terminal of an upstream Accumulator function. The default value of carry-in/inverted borrow-in is FALSE, which means this function computes s – x – 1(LSB) if is sub? is TRUE or s + x if is sub? is FALSE. If carry-in/inverted borrow-in is TRUE, this function computes s – x if is sub? is TRUE or s + x + 1(LSB) if is sub? is FALSE. carry-out/inverted borrow-out — Returns TRUE if the data type of s cannot represent the result of an unsigned addition operation. This terminal returns FALSE if the data type of s cannot represent the result of an unsigned subtraction operation. In this situation, this function wraps the value of s. LabVIEW displays this terminal only if the encoding is Unsigned. If you cascade this function, you can use this terminal to specify whether a downstream function carries or borrows a value. To specify that a downstream function uses this value, wire the carry-out/inverted borrow-out output terminal to the carry-in/inverted borrow-in input terminal of the downstream function. overflow — Returns TRUE if the encoding is Signed and the theoretical computed value of s exceeds the valid range of the data type of s. In this situation, this function wraps the value of s. Note If you cascade functions, you must use unsigned functions in the intermediate operations. Then set the encoding of the final function to the encoding you want for the entire cascaded operation. s — Returns the result this function computes. This result depends on not only the value of x, but also the values of any Boolean input terminals LabVIEW displays. For example, s accumulates only while load is FALSE and enable is TRUE. A value of s applies to one channel only. In multi-channel applications, s accumulates separately for each channel. Refer to the Details section for an example of using this function in a multi-channel application. This function applies the Wrap overflow mode to s in any of the following situations: overflow returns TRUE is sub? is TRUE and carry-out/inverted borrow out returns FALSE is sub? is FALSE and carry-out/inverted borrow out returns TRUE |
| --- |

#### Multi-channel Operation

This function always takes one cycle to compute a value of **s**. This function maintains separate internal values of **s** for each channel. This behavior has implications for multi-channel applications. For example, consider the following six data samples from a two-channel data acquisition operation:

| Data Sample Number | Channel 1 | Channel 2 |
| --- | --- | --- |
| 1 | 6 | 8 |
| 2 | 44 | 5 |
| 3 | 2 | 3 |

To interleave this data, create a one-dimensional array with the following values: [6 8 44 5 2 3]. Then wire one element per clock cycle to the **x** input of the Accumulator function, as the following figure shows:

[IMAGE alt='image' src='loc_bd_accumulator.gif']

The previous figure executes the Accumulator function for seven clock cycles. the accumulator function takes in **x** values from channel 1 during clock cycles 1, 3, and 5. Because of the one-cycle latency, the function returns accumulated **s** values for channel 1 during clock cycles 2, 4, and 6.

For channel 2, the function takes in **x** values during clock cycles 2, 4, and 6. The function returns accumulated **s** values for channel 2 during clock cycles 3, 5, and 7. This behavior means that for each cycle the function takes in an **x** value from channel 1, the function returns an **s** value for channel 2.

Note

s

s

s

If the function computes **s** + **x**, the following table shows the operation of this VI in detail.

| Clock cycle | Input x | Explanation of x | Output s | Explanation of s |
| --- | --- | --- | --- | --- |
| 1 | 6 | Channel 1, data sample number 1 | – | The function does not return a result during the first clock cycle because the function takes one clock cycle to execute. |
| 2 | 8 | Channel 2, data sample number 1 | 6 (the accumulation of channel 1) | Although this clock cycle takes input data from channel 2, the function returns data it received during the previous clock cycle. This data was from channel 1, when s was 0 and x was 6, so this function returns 6 in s. |
| 3 | 44 | Channel 1, data sample number 2 | 8 (the accumulation of channel 2) | Although this clock cycle takes input data from channel 1, the function returns data it received during the previous clock cycle. This data was from channel 2, when s was 0 and x was 8, so this function returns 8 in s. |
| 4 | 5 | Channel 2, data sample number 2 | 50 (the accumulation of channel 1) | s = 6 from clock cycle 2, x = 44 from clock cycle 3 |
| 5 | 2 | Channel 1, data sample number 3 | 13 (the accumulation of channel 2) | s = 8 from clock cycle 3, x = 5 from clock cycle 4 |
| 6 | 3 | Channel 2, data sample number 3 | 52 (the accumulation of channel 1) | s = 50 from clock cycle 4, x = 2 from clock cycle 5 |
| 7 | – | There is no more data from channel 1 | 16 (the accumulation of channel 2) | s = 13 from clock cycle 5, x = 3 from clock cycle 6 |

#### Simulation Export Details

This node can increase simulation run time significantly when used in conjunction with downloading, stopping, or running the FPGA VI.

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Multi-Channel Averaging\Multi-Channel Averaging.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Multi-Channel Averaging\Multi-Channel Averaging.lvproj
- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Long Width Calculation\Long Width Calculation.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Long Width Calculation\Long Width Calculation.lvproj

Parent topic:

Basic Elements

<!--NI_TOPIC bundle=lvfpga-api-ref path=vi-lib/rvi/fxpmathlib/fxpadd/xnode/nifxpmath-add-xnode.html language=enus -->
## TOPIC 00250: High Throughput Add

- bundle_id: `lvfpga-api-ref`
- source_path: `vi-lib/rvi/fxpmathlib/fxpadd/xnode/nifxpmath-add-xnode.html`
- source_url: https://docs-be.ni.com/bundle/lvfpga-api-ref/raw/resource/enus/vi-lib/rvi/fxpmathlib/fxpadd/xnode/nifxpmath-add-xnode.html
- document_id: `lvfpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the sum of x and y. This function supports only scalar and array values of the fixed-point data type. icon Dialog Box Options Parameter Description Fixed-Point Configuration Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. T

### High Throughput Add

Computes the sum of **x** and **y**.

This function supports only scalar and array values of the [fixed-point](/csh?productcategories=147794&context=lvcore_lvhowto_fixed_point_numbers) data type.

[IMAGE alt='icon' src='nifxpmath-add-xnode.png']

#### Dialog Box Options

| Parameter | Description |
| --- | --- |
| Fixed-Point Configuration | Specifies the encodings, word lengths, and integer word lengths of the input and output terminals of this function. The configurations you specify determine the value range of the terminals. x Type—Specifies the fixed-point configuration of the x input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. y Type—Specifies the fixed-point configuration of the y input terminal. If you wire a fixed-point data type to this terminal, LabVIEW dims this section and uses information from the wire. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. x+y Type—Specifies the fixed-point configuration of the x+y output terminal. Adapt to source—Specifies whether LabVIEW automatically adjusts the fixed-point configuration of the output data type to avoid overflow and rounding errors. By default, this checkbox contains a checkmark and LabVIEW dims the following options. Note LabVIEW supports a maximum word length of 64 bits and a maximum integer word length of 2047 bits. If you place a checkmark in this checkbox and the output data type requires a word length that exceeds these maximum values, overflow and/or rounding errors might occur. Signed—Specifies that this terminal is signed. Unsigned—Specifies that this terminal is unsigned. Word length—Specifies the word length of this terminal. Integer word length—Specifies the integer word length of this terminal. Include overflow status—Specifies whether the output terminal includes the overflow status. LabVIEW propagates this status to downstream nodes. Including this status requires additional FPGA resources. By default, this checkbox does not contain a checkmark. If you place a checkmark in this checkbox, the overflow status becomes TRUE in either of the following situations: The overflow status of an input terminal is TRUE. Overflow occurs during the operation of this function. If you place a checkmark in the Adapt to source checkbox, LabVIEW sets Include overflow status depending on whether an input terminal includes this status. Overflow mode—Specifies how this function handles overflow. You can choose either Wrap (default) or Saturate. Note The Saturateoption requires more FPGA resources and a longer combinatorial path than the Wrap option does. In this situation, choosing Saturate might decrease the maximum clock rate at which this function can compile. Rounding mode—Specifies how this function rounds the output data if rounding is necessary. You can choose Truncate (default), Round Half-Up, or Round Half-Even. If rounding occurs, the option you choose mightaffect the amount of resources this function requires. |
| Execution Mode | Specifies how this function executes. Outside single-cycle Timed Loop—Configures this Express VI to execute outside a single-cycle Timed Loop. If you select this option and place this Express VI inside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Inside single-cycle Timed Loop—Configures this Express VI to execute inside a single-cycle Timed Loop. If you select this option and place this Express VI outside a single-cycle Timed Loop, the Code Generation Errors window reports an error when you compile the FPGA VI. Throughput—Displays the number of cycles between two successive values of valid input data. This number always is one cycle. Therefore, LabVIEW sets the value according to where you place this Express VI. If you select Inside single-cycle Timed Loop,LabVIEW sets the throughput to 1 cycle / sample. If you select Outside single-cycle Timed Loop, LabVIEW sets the throughput to 1 call / sample. |
| Registers | Specifies whether to add internal registers for function output terminal. This section is available only if you select Inside single-cycle Timed Loop. Note Adding registers can reduce the length of the combinatorial path, which can prevent compilation errors that result from a long combinatorial path. However, adding registers also increases the latency of this function, which means this function takes additional clock cycles to return a valid result. Register outputs—Adds internal registers before the outputs of this function. Selecting this option increases the latency of the function by one cycle. |
| Optional Terminal | Specifies a setting for displaying an optional block diagram terminal. Operation overflow—Specifies that this function displays the operation overflow output terminal on the block diagram. This terminal indicates whether overflow occurred during the operation of this function. |
| Configuration Feedback | Displays information about how this function executes. This information is based on the configuration options you specify. |

#### Inputs/Outputs

| x — Specifies an addend. y — Specifies an addend. input valid — Specifies whether the next data point has arrived for processing. Wire the output valid output of an upstream node to this input to transfer data from the upstream node to this node. To display this handshaking terminal, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. ready for output — Specifies whether downstream nodes are ready for this node to return a new value. The default is TRUE. Use a Feedback Node to wire the ready for input output of a downstream node to this input of the current node. Note If this terminal is FALSE during a given cycle, the output valid terminal returns FALSE during that cycle. To display this terminal, select Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. x+y — Returns the sum of x and y. operation overflow — Returns TRUE if the theoretical computed value exceeds the valid range of the output data type. If operation overflow returns TRUE, the Overflow mode option determines the value this function returns. LabVIEW displays the operation overflow terminal only if you place a checkmark in the Operation overflow checkbox. This checkbox is located in the Optional Terminal section of the configuration dialog box. output valid — Returns TRUE if this node has computed a result that downstream nodes can use. Wire this output to the input valid input of a downstream node to transfer data from the node to the downstream node. To display this terminal, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. ready for input — Returns TRUE if this node is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output input of an upstream node. Note If this terminal returns FALSE during a given cycle, LabVIEW discards any data that other nodes send to this node during the following cycle. LabVIEW discards this data even if the input valid terminal is TRUE during the following cycle. To display this terminal, select the Inside single-cycle Timed Loop option and place a checkmark in the Register outputs checkbox. These options are located in the configuration dialog box. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW FPGA Module.

- labview\examples\CompactRIO\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj
- labview\examples\R Series\FPGA Fundamentals\FPGA Math and Analysis\High-Throughput Math\Vector Normalization\Vector Normalization.lvproj

Parent topic:

High Throughput Math
