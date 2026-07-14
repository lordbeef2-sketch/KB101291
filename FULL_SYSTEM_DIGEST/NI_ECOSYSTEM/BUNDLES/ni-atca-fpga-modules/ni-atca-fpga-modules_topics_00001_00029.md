# NI DOCUMENT BUNDLE: ni-atca-fpga-modules

<!--NI_BUNDLE_CHUNK bundle=ni-atca-fpga-modules start=1 end=29 -->
<!--NI_TOPIC bundle=ni-atca-fpga-modules path=aio-3681-digitizer-module-for-fmc.html language=enus -->
## TOPIC 00001: AIO-3681 Digitizer Module for FMC

- bundle_id: `ni-atca-fpga-modules`
- source_path: `aio-3681-digitizer-module-for-fmc.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/aio-3681-digitizer-module-for-fmc.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The AIO-3681 is an expansion module that provides single- or dual-channel 12-bit analog-to-digital conversion at RF sampling rates up to 4 GS/s, depending on hardware configuration. The AIO-3681 features a TI ADC12D2000RF analog-to-digital converter (ADC) component and is shipped with software suppo

### AIO-3681 Digitizer Module for FMC

The AIO-3681 is an expansion module that provides single- or dual-channel 12-bit
 analog-to-digital conversion at RF sampling rates up to 4 GS/s, depending on
 hardware configuration.

Note

For the ADC, 8 samples per channel are provided in the user
 diagram per data clock cycle. Therefore, the data clock
 always runs at one-eighth the frequency of the sampling
 clock. For example, at a sampling clock rate of 2.5 GHz, the
 data clock will run at 312.5 MHz.

CLIP Reset

Note

The self-calibration algorithm between the CLIP and ADC takes
 approximately 20 seconds to complete.

CLIP Ready

Note

Rerun calibration after significantly altering the settings or
 conditions of the AIO-3681. To preform calibration, use the
 3681 Generic Config VI to set the CAL bit (Addr: 0h; Bit 15)
 to low for a minimum of 1,280 sample clock cycles and then
 high for a minimum of 1,280 sample clock cycles. Visit
 ni.com/info and enter the
 Info Code exsq59 to access the
 specifications for the ADC12D2000RF and navigate to section
 17.3.3 of the document for more information about the
 calibration feature.

Note

You can change gain range and configuration registers using
 *3681 Gain Config* and *3681 Generic
 Config*.

Figure 8.

[IMAGE alt='image' src='GUID-B917C370-58ED-4492-A971-730509974C78-a5.png']

Figure 9.

[IMAGE alt='image' src='GUID-ABE155E8-E381-4A5F-93D8-C624EE1671F7-a5.png']

Parent topic:

NI-ATCA FPGA Modules Devices

Related information:

- Using an Info Code

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=aio-3681-socketed-clip-interface.html language=enus -->
## TOPIC 00002: AIO-3681 Socketed CLIP Interface

- bundle_id: `ni-atca-fpga-modules`
- source_path: `aio-3681-socketed-clip-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/aio-3681-socketed-clip-interface.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW support for the AIO-3681 includes two versions of the Socketed CLIP interface. One version is for dual-channel I/Q sampling. One version is for single-channel dual-edge sampling (DES).Because the hardware assembly uses different components based on the desired sampling mode, always choose th

### AIO-3681 Socketed CLIP Interface

LabVIEW support for the AIO-3681 includes two versions of the Socketed CLIP
 interface. One version is for dual-channel I/Q sampling. One version is for single-channel
 dual-edge sampling (DES).

Because the hardware assembly uses different components based on the desired sampling mode,
 always choose the appropriate Socketed CLIP to match the hardware configuration present
 in the system.

In dual-channel sampling mode, the same clock edge is used to sample both signals at the same time. In DES mode, opposite edges of the clock are used to sample each channel in an alternating fashion, effectively doubling the sample rate of the ADC.

For more information on the sampling modes supported by the ADC, refer to the TI ADC12D2000RF
 device data sheet on the Texas Instruments website at
 www.ti.com.

Figure 10.

[IMAGE alt='image' src='GUID-654812F7-8B2F-45F0-9258-66BD39696F27-a5.gif']

Parent topic:

AIO-3681 Digitizer Module for FMC

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=aio-3682-signal-generator-module-for-fmc.html language=enus -->
## TOPIC 00003: AIO-3682 Signal Generator Module for FMC

- bundle_id: `ni-atca-fpga-modules`
- source_path: `aio-3682-signal-generator-module-for-fmc.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/aio-3682-signal-generator-module-for-fmc.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The AIO-3682 is an expansion module that provides dual-channel 14-bit digital-to-analog conversion at RF sampling rates up to 5.6 GS/s. The module features two Analog Devices AD9129 digital-to-analog (DAC) components. Software support requires that both DACs be driven by the same external clock at a

### AIO-3682 Signal Generator Module for FMC

The AIO-3682 is an expansion module that provides dual-channel 14-bit
 digital-to-analog conversion at RF sampling rates up to 5.6 GS/s.

The module features two Analog Devices AD9129 digital-to-analog (DAC) components.
 Software support requires that both DACs be driven by the same external clock at all
 times, although the DACs can operate on separate sampling clock domains.

Refer to the specifications document for your hardware at
 ni.com/docs for complete specifications.

Figure 11.

[IMAGE alt='image' src='GUID-3F43B023-98DD-4239-8C66-73DF6C13E4CF-a5.png']

Parent topic:

NI-ATCA FPGA Modules Devices

Related information:

- AIO-3682 Specifications

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=aio-3682-socketed-clip-interface.html language=enus -->
## TOPIC 00004: AIO-3682 Socketed CLIP Interface

- bundle_id: `ni-atca-fpga-modules`
- source_path: `aio-3682-socketed-clip-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/aio-3682-socketed-clip-interface.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-ATCA FPGA Modules includes a Socketed CLIP interface for using both DACs simultaneously with the same external sampling clock.The primary DAC (signal AO 0) must always be used in a LabVIEW design, and must be driven by a stable external sampling clock at all times. The secondary DAC (signal AO 1)

### AIO-3682 Socketed CLIP Interface

NI-ATCA FPGA Modules includes a Socketed CLIP interface for using both DACs
 simultaneously with the same external sampling clock.

The primary DAC (signal AO 0) must always be used in a LabVIEW design, and must be driven by a
 stable external sampling clock at all times. The secondary DAC (signal AO 1) is
 optional. It may be left out of a design, and its external clock input can be left
 disconnected when not in use. The logic clock generated by the CLIP for the diagram is
 derived purely from the output of the primary DAC (AO 0).

For each DAC, 8 samples are provided in the user diagram per data clock cycle. Therefore, the data clock always runs at one eighth the frequency of the sampling clock. For example, at a sampling clock rate of 2.5 GHz, the data clock will run at 312.5 MHz.

Note

Note

To help manage this initialization time, a CLIP Ready signal is also provided which can be
 monitored to determine when the DAC is ready to accept output data. Any interruptions to
 the external clock or software events, such as resetting the diagram or downloading a
 new bitstream, should always be followed by a reset to the CLIP.

Figure 12.

[IMAGE alt='image' src='GUID-8CC61E08-7496-4F0B-9791-596D8D53983D-a5.gif']

Parent topic:

AIO-3682 Signal Generator Module for FMC

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=aio-3691-high-speed-serial-adapter-module.html language=enus -->
## TOPIC 00005: AIO-3691 High-Speed Serial Adapter Module

- bundle_id: `ni-atca-fpga-modules`
- source_path: `aio-3691-high-speed-serial-adapter-module.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/aio-3691-high-speed-serial-adapter-module.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The AIO-3691 is an expansion module that provides 16 lanes of high-speed serial connectivity between each FPGA and the front panel of the ATCA-3671. It features four SFF-8644 (miniSAS-HD) connectors, which allow for quad x4 data interfaces to be implemented for communicating between ATCA-3671 FPGA m

### AIO-3691 High-Speed Serial Adapter Module

The AIO-3691 is an expansion module that provides 16 lanes of high-speed serial
 connectivity between each FPGA and the front panel of the ATCA-3671.

It features four SFF-8644 (miniSAS-HD) connectors, which allow for quad x4 data
 interfaces to be implemented for communicating between ATCA-3671 FPGA modules or to
 other external high-speed serial equipment, such as the PXIe-6591 High-Speed Serial
 Instrument.

Refer to the specifications document for your hardware at
 ni.com/docs for complete specifications.

Figure 13.

[IMAGE alt='image' src='GUID-0E631580-2096-45C1-92FB-57D93EC2CA2F-a5.png']

Parent topic:

NI-ATCA FPGA Modules Devices

Related information:

- AIO-3691 Specifications

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=aio-3691-socketed-clip-interface.html language=enus -->
## TOPIC 00006: AIO-3691 Socketed CLIP Interface

- bundle_id: `ni-atca-fpga-modules`
- source_path: `aio-3691-socketed-clip-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/aio-3691-socketed-clip-interface.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-ATCA FPGA Modules includes a Socketed CLIP example for the AIO-3691, which features an optimally hardware-efficient implementation of the Aurora protocol across all lanes running at 10.4167 GHz.Each SFF-8644 port has its own x4 Aurora IP instance and data ports to the LabVIEW diagram, but all fou

### AIO-3691 Socketed CLIP Interface

NI-ATCA FPGA Modules includes a Socketed CLIP example for the AIO-3691, which
 features an optimally hardware-efficient implementation of the Aurora protocol across all
 lanes running at 10.4167 GHz.

Note

Note

Figure 14.

[IMAGE alt='image' src='GUID-E216DE49-8D40-4EE2-B7CC-E62084A5F6FA-a5.gif']

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| fmc_dp_c2m_p(15:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| fmc_dp_c2m_n(15:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| fmc_dp_m2c_p(15:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| fmc_dp_m2c_n(15:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| fmc_gtbclk0_m2c_p | In (pad) | N/A | Reference clock input pins from the FMC connector. These ports are directly connected to the top-level ports of the FPGA and are unbuffered. Therefore, IBUFDS_GTE2 instances are required in the CLIP. |
| fmc_gtbclk0_m2c_n | In (pad) | N/A | Reference clock input pins from the FMC connector. These ports are directly connected to the top-level ports of the FPGA and are unbuffered. Therefore, IBUFDS_GTE2 instances are required in the CLIP. |
| fmc_gtbclk1_m2c_p | In (pad) | N/A | Reference clock input pins from the FMC connector. These ports are directly connected to the top-level ports of the FPGA and are unbuffered. Therefore, IBUFDS_GTE2 instances are required in the CLIP. |
| fmc_gtbclk1_m2c_n | In (pad) | N/A | Reference clock input pins from the FMC connector. These ports are directly connected to the top-level ports of the FPGA and are unbuffered. Therefore, IBUFDS_GTE2 instances are required in the CLIP. |
| fmc_312p5_refclk(3:0) | In | N/A | Reference clock inputs for the shared 312.5 MHz oscillator. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| fmc_jc_refclk(3:0) | In | N/A | Reference clock inputs for the GTH reference clock generated by the jitter cleaner. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| fmc_sma_refclk(3:0) | In | N/A | Reference clock inputs for the shared front panel SMA connector. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| fmc_fpga_ready | In | Async | Signal driven by fixed logic to indicate that all clocks and power supplies required by the FPGA are active and stable. |
| fmc_jc_srcclk | Out | N/A | Optional output signal which can be driven out from the CLIP to be used as the source clock for the jitter cleaner (useful for recovered-clock applications where the interface IP produces a clock that must be externally filtered for reuse as a reference clock). The source clock to be driven out to the jitter cleaner is selected through the External Clock Configuration properties window. |

Parent topic:

AIO-3691 High-Speed Serial Adapter Module

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=atca-3671-clocking-features.html language=enus -->
## TOPIC 00007: ATCA-3671 Clocking Features

- bundle_id: `ni-atca-fpga-modules`
- source_path: `atca-3671-clocking-features.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/atca-3671-clocking-features.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the onboard and external clocks on the ATCA-3671.The clocking resources available on the system are summarized in the table below. If the software programming environment provides support for runtime configuration of clocking resources, refer to specific software product documentation for

### ATCA-3671 Clocking Features

Configure the onboard and external clocks on the ATCA-3671.

The clocking resources available on the system are summarized in the table below. If the software
 programming environment provides support for runtime configuration of clocking resources,
 refer to specific software product documentation for more information.

| Name | Direction | Description |
| --- | --- | --- |
| Fixed 100 MHz | N/A | A single 100 Fixed MHz reference clock is distributed to all four FPGAs on the ATCA-3671. This clock is free-running and may be used to derive any other clock frequencies desired inside the FPGA. |
| DDR3 Clock | N/A | A single 400 Hz reference clock is distributed to all four FPGAs on the ATCA-3671 for explicit use by the soft double data rate type three (DDR3) memory controller logic in the FPGA. The actual frequency of the logic clock available on the user interface side of the memory controller may vary based on the software platform, but is typically 167 MHz for the maximum DDR3 dynamic random access memory (DRAM) speed of 1,333 MHz. |
| SYNC A SYNC B | Input | Each of these two independent signals can be used to drive a clock to all four FPGAs on the ATCA-3671. By default, the SMA input on the front panel of the system is enabled as the signal source. However, in environments where a full ATCA backplane is present, this setting can be overridden in firmware to select the corresponding ATCA backplane signals to use the source instead. When added to a LabVIEW project, these clock sources are defined as free-running base clocks which support derived clocks. Therefore, the external clock source must be connected and stable at the correct frequency before running the FPGA application, even if they are not explicitly used in the diagram. Otherwise, errors are reported. In addition, the SYNC A and SYNC B signals must not be used as clocks in the same application (and vice versa) if they are used as FPGA I/O. |
| CLK IN/OUT A CLK IN/OUT B CLK IN/OUT C CLK IN/OUT D | Input/output | Each of these connectors on the front panel are coupled to one FPGA on the ATCA-3671 (denoted by A, B, C, or D) as either an input or output. The direction of the signal is configured in software, and can be changed dynamically at runtime. In LabVIEW, this clock source for each FPGA is defined as an external clock. This implies that it may not always be stable or connected and therefore cannot be used as the default top level clock or to generate derived clocks. |
| JC OUT A JC OUT B JC OUT C JC OUT D | Output | Each FPGA on the ATCA-3671 can drive out an ultra-low phase noise clock through a designated onboard jitter cleaning phase-locked loop (PLL). The exact frequency configuration of this PLL is controlled by software. See Configuring the Jitter Cleaner for Use as a Clock Source for more information. |
| MGT REF | Input | An input on the front panel used to distribute a single multi-gigabit transceiver (MGT) reference clock to every user-accessible high-speed transceiver on all four FPGAs on the ATCA-3671. |
| AIO CLK | Input | An input on the front panel used to drive an auxiliary external clock into all four of the AIO slots on the front panel of the ATCA-3671. This clock is not driven directly into the FPGA. Therefore, its usage and availability are dependent on the ATCA I/O module present in the system. |

Parent topic:

ATCA-3671 FPGA Module for ATCA

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=atca-3671-fpga-module-for-atca.html language=enus -->
## TOPIC 00008: ATCA-3671 FPGA Module for ATCA

- bundle_id: `ni-atca-fpga-modules`
- source_path: `atca-3671-fpga-module-for-atca.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/atca-3671-fpga-module-for-atca.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the ATCA-3671 module, including the clocking features and user-accessible multi-gigabit transceivers (MGTs).Refer to ATCA-3671 Specifications for complete specifications.

### ATCA-3671 FPGA Module for ATCA

Learn about the ATCA-3671 module, including the clocking features and user-accessible
 multi-gigabit transceivers (MGTs).

Refer to *ATCA-3671 Specifications* for complete specifications.

Parent topic:

NI-ATCA FPGA Modules Devices

Related information:

- ATCA-3671 Specifications

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=atca-3671-front-panel-diagram.html language=enus -->
## TOPIC 00009: ATCA-3671 Front Panel

- bundle_id: `ni-atca-fpga-modules`
- source_path: `atca-3671-front-panel-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/atca-3671-front-panel-diagram.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: View the ATCA-3671 front panel, including the location of the LED lights.1 ATCA-3671 Front Panel Red LED Green LED Blue LED

### ATCA-3671 Front Panel

View the ATCA-3671 front panel, including the location of the LED lights.

Figure 1.

[IMAGE alt='image' src='GUID-A98F307F-90B2-49BA-858F-6AE028D01D79-a5.gif']

1. Red LED
2. Green LED
3. Blue LED

Parent topic:

ATCA-3671 FPGA Module for ATCA

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=atca-3671-jitter-cleaning-phase-locked-loop-p.html language=enus -->
## TOPIC 00010: ATCA-3671 Jitter Cleaning Phase-Locked Loop (PLL)

- bundle_id: `ni-atca-fpga-modules`
- source_path: `atca-3671-jitter-cleaning-phase-locked-loop-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/atca-3671-jitter-cleaning-phase-locked-loop-p.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each FPGA has a designated TI LMK04808 jitter-cleaning dual-PLL device, which is used when an ultra-low phase noise clock must be generated from a clock source inside the FPGA.The primary input to the jitter cleaner is driven by a differential pair on the FPGA. The jitter cleaner then outputs two di

### ATCA-3671 Jitter Cleaning Phase-Locked Loop (PLL)

Each FPGA has a designated TI LMK04808 jitter-cleaning dual-PLL device, which is used
 when an ultra-low phase noise clock must be generated from a clock source inside the
 FPGA.

The primary input to the jitter cleaner is driven by a differential pair on the FPGA. The jitter
 cleaner then outputs two different clocks back to the FPGA: one MGT reference clock,
 which is duplicated so that it can reach every MGT quad on the FPGA, and one SMA output
 clock.

Note

For more information on the configuration and performance of the jitter cleaner, refer to the
 LMK0480X datasheet on the Texas Instruments website at
 www.ti.com.

Software features are provided to fully configure the jitter cleaner based on a user-defined set
 of input and output frequencies.

Parent topic:

ATCA-3671 Clocking Features

Related information:

- LMK0480x Low-Noise Clock Jitter Cleaner with Dual Loop
 PLLs

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=atca-3671-som-commands.html language=enus -->
## TOPIC 00011: ATCA-3671 SOM Commands

- bundle_id: `ni-atca-fpga-modules`
- source_path: `atca-3671-som-commands.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/atca-3671-som-commands.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use System-on-Module (SOM) commands to control the ATCA-3671. The ATCA-3671 SOM hosts an SSH server that can be connected to using standard SSH tools. After connecting the Ethernet port on the ATCA-3671 to a computer, enter the following default credentials: IP address: 192.168.0.75 User: ro

### ATCA-3671 SOM Commands

You can use System-on-Module (SOM) commands to control the ATCA-3671.

The ATCA-3671 SOM hosts an SSH server that can be connected to using standard SSH tools. After
 connecting the Ethernet port on the ATCA-3671 to a computer, enter the
 following default credentials:

- IP address: 192.168.0.75
- User: root
- Leave the password field empty

Update the default credentials in accordance with your IT policies.

You can use boardctl commands and minicom commands with the ATCA-3671. Use
 minicom commands to communicate with the microblaze of an individual FPGA.
 Use boardctl commands to communicate with the ATCA-3671 as a whole.

If your software programming environment provides support for runtime
 configuration of clocking resources, refer to specific software product
 documentation.

- [Boardctl Commands](boardctl-commands.html) Use boardctl commands to communicate with ATCA-3671 as a whole.
- [Minicom Commands](minicom-commands.html) Use minicom commands to interact with the ATCA fixed logic microblaze directly.

Parent topic:

ATCA-3671 FPGA Module for ATCA

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=atca-3671-user-accessible-multi-gigabit-trans.html language=enus -->
## TOPIC 00012: ATCA-3671 User-Accessible Multi-Gigabit Transceivers

- bundle_id: `ni-atca-fpga-modules`
- source_path: `atca-3671-user-accessible-multi-gigabit-trans.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/atca-3671-user-accessible-multi-gigabit-trans.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATCA-3671 hardware has 76 user-accessible multi-gigabit transceivers (MGTs) available to the user for high-speed, low-latency data communication between devices.The FPGAs on the ATCA-3671 feature a Xilinx GTH transceiver, which allows for supported line rates up to 12.5 Gbps on most interfaces.T

### ATCA-3671 User-Accessible Multi-Gigabit
 Transceivers

The ATCA-3671 hardware has 76 user-accessible multi-gigabit transceivers (MGTs)
 available to the user for high-speed, low-latency data communication between
 devices.

The FPGAs on the ATCA-3671 feature a Xilinx GTH transceiver, which allows for supported line
 rates up to 12.5 Gbps on most interfaces.

The ATCA-3671 user-accessible MGTs are organized into five different groups:

- Three MGT groups connect the four FPGAs in a full mesh pattern
- One MGT group connects the FPGAs to the ATCA I/O (AIO)
slot
- One MGT group connects the FPGAs to the Rear Transition Module (RTM) slot

The following figure shows the logical structure of the five transceiver groups.

Figure 3.

[IMAGE alt='image' src='GUID-FEDE295E-E977-413D-A0A5-38B2567191A4-a5.png']

1. AIO
2. RTM
3. FPGA Ring Up
4. FPGA Ring Down
5. FPGA Diagonal

Each transceiver group is defined in the following table.

| Name | Number of MGTs | Connection | Configuration |
| --- | --- | --- | --- |
| AIO | 16 | Each FPGA to a designated AIO module connector | Depends on which AIO module is populated in each slot |
| RTM | 16 | Each FPGA to the RTM | Depends on which RTM is populated in the system |
| FPGA Ring Up | 16 | Upstream, between FPGAs | Ring (A to D, B to A, C to B, and D to C) |
| FPGA Ring Down | 16 | Downstream, between FPGAs | Ring (A to B, B to C, C to D, and D to A) |
| FPGA Diagonal | 12 | Diagonal, between FPGAs | Diagonal (A to C, B to D, C to A, D to B) |

Parent topic:

ATCA-3671 FPGA Module for ATCA

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=boardctl-commands.html language=enus -->
## TOPIC 00013: Boardctl Commands

- bundle_id: `ni-atca-fpga-modules`
- source_path: `boardctl-commands.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/boardctl-commands.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use boardctl commands to communicate with ATCA-3671 as a whole.Once you have accessed the System-on-Module (SOM) according to the instructions in SOM Commands, enter any of the boardctl commands listed in the following table. 2 Boardctl Commands Command Direction boardctl power - 0 boardctl power -

### Boardctl Commands

Use boardctl commands to communicate with ATCA-3671 as a whole.

Once you have accessed the System-on-Module (SOM) according to the instructions in *SOM
 Commands*, enter any of the boardctl commands listed in the following table.

| Command | Direction |
| --- | --- |
| boardctl power - 0 boardctl power - 1 | Powers on or powers off the ATCA-3671 module.-0, turn blade off -1, turn blade on |
| boardctl program <fpga> <BIN file> | Programs the specified FPGA with the specified binary file.<fpga>: A B C D<BIN file>: File to be programmed |
| boardctl reset <device> <duration> | Resets the specified component with a reset pulse equivalent to the <duration> in ms. <device>: A B C D S PA B C D: FPGA IDsS: GbE switchP: GbE PHY<duration>: Duration of reset pulse in ms (default is 10 ms) |
| boardctl sensors <option>... | -p, --power: Read power usage -t, --temperature: Read temperatures -v, --voltage <source>: Read voltages for <source>; either the global rails (G), a given FPGA (A B C D), or the power sequencer (P). |
| boardctl fault - c boardctl fault - f | -c: clear any temperature faults -f: log fault info to a given file |
| boardctl gclk <fpga> <output> <input> | Routes GCLK output (0-3) on specified FPGA to be controlled by input FPGA. <fpga>: Target FPGA (A B C D)<output>: Target GCLK net (0 1 2 3)<input>: Source clock (A B C D) |
| boardctl info | Prints out ATCA-3671 module information. |
| boardctl rtminfo | Prints out RTM board information. |

Parent topic:

ATCA-3671 SOM Commands

Related concepts:

- ATCA-3671 SOM Commands

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=configure-new-atca-3671-fpga-target.html language=enus -->
## TOPIC 00014: Configuring a New ATCA-3671 FPGA Target

- bundle_id: `ni-atca-fpga-modules`
- source_path: `configure-new-atca-3671-fpga-target.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/configure-new-atca-3671-fpga-target.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: After creating an FPGA target for the ATCA-3671, additional project configuration options are available. Adding and Assigning Custom CLIP Files Assign a new CLIP file to any of the five available sockets. Each socket is assigned an idle CLIP by default. The following sockets are available for config

### Configuring a New ATCA-3671 FPGA
 Target

After creating an FPGA target for the ATCA-3671, additional project configuration options
 are available.

#### Adding and Assigning Custom CLIP Files

Assign a new CLIP file to any of the five available sockets. Each socket is assigned
 an idle CLIP by default.

- AIO
- FPGA Diagonal
- FPGA Ring Down
- FPGA Ring Up
- RTM

1. Right-click the FPGA target and select Properties from
 the shortcut menu. 
 The FPGA Target Properties dialog box displays.
2. Select Component-Level IP from the
 Category list. 
 The Component-Level IP Properties page displays.
3. Select Add File.
4. Select all the CLIP XML files that you need for your design and click
 OK. 
 These files are your CLIP declaration files.Note The default CLIP files are installed in the LabVIEW folder at
 Targets\NI\FPGA\ATCA\CLIP. If you are not using a
 specific socket in your design, add the corresponding Idle MGT CLIP XML file
 located in the Idle subdirectory.
5. Click OK to close the FPGA Target Properties
 Window. 
 Note If you select multiple CLIPs, it may
 take longer to scan and populate all of the CLIPs.
6. Right-click a socket on the FPGA target and select
 Properties from the shortcut menu. 
 The Component-Level IP Properties dialog box displays.
7. Select the corresponding CLIP declaration that you added in step 4 from the
 Socketed Component-Level IP Declaration pull-down
 menu.
8. Click the Clock Selections tab. 
 Ensure that a valid connection appears for each clock. If a valid connection
 does not appear, add a derived clock to the target which matches the desired
 frequency or select Create Necessary Clocks.Note Idle CLIPs do not require that a clock be specified in
 the Clock Selections tab.
9. Click OK. 
 The FPGA Target Properties window closes.

The Project Explorer window includes the I/O defined in the
 declaration XML file.

#### Configuring the Clock Routing on the
 FPGA

You can configure the clock routing on the FPGA.

1. Right-click the External Clock Configuration item in the
 target and select Properties from the shortcut
 menu. 
 The External Clock Properties dialog box displays.
2. Select the appropriate values for your design and use according to the
 following table. 
 You can choose to leave all settings at the default values.Table 1.Jitter Cleaner and
 FPGA In/Out SMADesign
 Use
 ActionJitter cleaner
 In use
 Select the clock source and output frequencies.
 Jitter cleaner
 Not in use
 Leave the settings at the default values.
 FPGA In/Out SMA
 Using as output
 Select the Enable FPGA In/Out SMA clock as
 output checkbox and select a clock source
 from the FPGA In/Out SMA Clock Source
 pull-down menu.
 FPGA In/Out SMA
 Using as input
 Leave the settings at the default values.
 FPGA In/Out SMA
 Not in use
 Leave the settings at the default values.
3. Click OK.

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=configuring-dram-with-fpga-memory-items.html language=enus -->
## TOPIC 00015: Configuring DRAM with FPGA Memory Items

- bundle_id: `ni-atca-fpga-modules`
- source_path: `configuring-dram-with-fpga-memory-items.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/configuring-dram-with-fpga-memory-items.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATCA-3671 Getting Started DRAM example demonstrates multiple methods to access the external DRAM memory from the FPGA.Complete the following steps to configure DRAM with FPGA memory items using the ATCA-3671 Getting Started DRAM VI: Within LabVIEW, select Help Find Examples . Search for ATCA. Op

### Configuring DRAM with FPGA Memory Items

The *ATCA-3671 Getting Started DRAM* example demonstrates multiple methods
 to access the external DRAM memory from the FPGA.

Complete the following steps to configure DRAM with FPGA memory items using the ATCA-3671 Getting
 Started DRAM VI:

1. Within LabVIEW, select Help»Find Examples .
2. Search for ATCA .
3. Open ATCA 3671 - Getting Started DRAM.lvproj .
4. Open the ATCA 3671 - Getting Started DRAM (FPGA).vi from the
 project. This VI demonstrates the various methods for accessing the DRAM from
 the FPGA on the ATCA-3671.
5. Examine the front panel input controls.
6. Open the ATCA 3671 - Getting Started DRAM (Host).vi from the
 project. This Host VI controls the data that flows into and out of the
 different external memory access methods on the FPGA.
7. Examine the front panel input controls and follow the in-software instructions. Note To create new Memory
 or FIFO resources on your target, right-click on the target. Select
 New... and follow the prompts.
8. Click Run to run the ATCA 3671 - Getting Started
 DRAM (Host).vi . Experiment with this example to determine your
 preferred method of accessing the DRAM. Note You can copy segments of the
 code included in these examples into your application.

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=configuring-jitter-cleaner-as-clock-source.html language=enus -->
## TOPIC 00016: Configuring the Jitter Cleaner for Use as a Clock Source

- bundle_id: `ni-atca-fpga-modules`
- source_path: `configuring-jitter-cleaner-as-clock-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/configuring-jitter-cleaner-as-clock-source.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure the ATCA-3671 Jitter Cleaner as a clock source by selecting a clock and setting input, VCO, and output frequencies. In your LabVIEW project window, navigate to the External Clock Configuration page of the ATCA-3671 FPGA target. In the Jitter Cleaner Clock Source drop-down menu, select one

### Configuring the Jitter Cleaner for Use as a
 Clock Source

Configure the ATCA-3671 Jitter Cleaner as a clock source by selecting a clock and
 setting input, VCO, and output frequencies.

1. In your LabVIEW project window, navigate to the External Clock Configuration
 page of the ATCA-3671 FPGA target.
2. In the Jitter Cleaner Clock Source drop-down menu,
 select one of the following clock sources. 
 OptionDescriptionCLK100
 Default setting that requires no external wiring.
 CLK100 allows you to use the Jitter Cleaner
 to derive a new clock rate.SYNC_A or SYNC_B
 Drive the Jitter Cleaner from an external source on the Sync A or
 Sync B clock net.FMC_CLIP or RTM_CLIP
 Drive the Jitter Cleaner from Socketed CLIP. This setting is useful
 for recovering a clock source. 
 Note Driving the Jitter Cleaner from the CLIP can
 recover an existing clock source for protocols such as Common Public Radio
 Interface (CPRI) or Synchronous Ethernet.
3. Wire external input/output connections. 
 If you are using Sync A or Sync B clock nets as a source, connect an
 external clock source to the front or back panel Sync port for the sync
 net you want to use.
 If you are using Jitter Cleaner SMA output, connect the Jitter Cleaner
 output to what you want to drive (including FPGAs).
4. Use one of the following to specify the input frequency to match the known
 frequency of the input clock source.
  - ATCA-3671 Configure Jitter Cleaner VI
  - minicom jc_set_input_freq command
5. Use one of the following to set the VCO frequency so that the frequency is
 between 2,750 MHz and 3,072 MHz and a multiple of your desired output frequency. 
 
 Note The VCO frequency must also share a
 factor with the VCXO frequency, which should always be 122.88 MHz. Because the VCXO is external to
 the JC, its frequency cannot be changed. Whenever calling the
 jc_set_vco_freq command, ensure that the VCXO frequency
 argument is always 122,880 kHz.
  - ATCA-3671 Configure Jitter Cleaner VI
  - minicom jc_set_vco_freq command
6. Use one of the following to set the output frequency for the type of connection
 you are using. 
 
 Valid values are factors of the VCO frequency, which can be obtained by
 dividing with an integer number between 1 and 1,045.Note Because the SMA and GTH outputs are separate, the
 output frequency can be different for each.
  - ATCA-3671 Configure Jitter Cleaner VI
  - minicom jc_set_output_freq command
7. Use the output from one of the following to determine if the Jitter Cleaner is
 locked. 
 
 If the Jitter Cleaner is not locked, refer to *ATCA-3671 Jitter Cleaner
 Operation* for troubleshooting information.
  - ATCA-3671 Configure Jitter Cleaner VI
  - minicom jc_get_status command

Parent topic:

ATCA-3671 Clocking Features

Related concepts:

- ATCA-3671 Jitter Cleaner Operation

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=deploying-bitfile.html language=enus -->
## TOPIC 00017: Deploying a Bitfile to the ATCA-3671

- bundle_id: `ni-atca-fpga-modules`
- source_path: `deploying-bitfile.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/deploying-bitfile.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are programming with LabVIEW, use the ATCA-3671 Transfer Bitstream VI and refer to the corresponding example implementation to transfer a bitstream. If you are not programming with LabVIEW, complete the following steps to transfer a bitstream remotely. Transferring a Bitstream Remotely Transf

### Deploying a Bitfile to the ATCA-3671

If you are programming with LabVIEW, use the ATCA-3671 Transfer Bitstream VI and refer to
 the corresponding example implementation to transfer a bitstream.

If you are not programming with LabVIEW, complete the following steps to transfer
 a bitstream remotely.

Parent topic:

ATCA-3671 FPGA Module for ATCA

#### Transferring a Bitstream Remotely

Transfer a LabVIEW FPGA bitstream from an .lvbitx file to the
 ATCA-3671 over TCP.

1. Connect the ATCA-3671 to the host machine using an Ethernet network
 connection.
2. Retrieve the raw bitstream contents of the desired LabVIEW bitfile
 (.lvbitx) using an XML parsing library or similar
 tool. 
 The bitstream is tagged with the <Bitstream> XML tag
 within the .lvbitx file.
3. Complete the following steps to format the bitstream:
  1. Remove all white space characters, including line feed, from the raw
 bitstream string.
  2. Remove all = characters from the end of the string if they are
 present.
4. Open a TCP connection with the ATCA-3671 System-on-Module (SOM) port 48871
 (0xBEE7). 
 The default IP address of the ATCA-3671 is 192.168.0.75.
5. Over the TCP connection, write a header packet made up of three 4-byte words
 (12 bytes total) of the following format: 
 word0 OPCODE
 word1 FPGA ID
 word20x1
 FPGA A = 0x1,
 FPGA B = 0x2,
 FPGA C = 0x3,
 FPGA D = 0x4,
 length of bitstream in bytes
6. Over the same TCP connection, send a message containing the bitstream formatted
 as described in step 2.
7. Read 4 bytes from the TCP connection following your write. 
 These bytes indicate the U32 return status of your download operation. A
 return status of zero indicates a successful transfer.
8. Send the following message, consisting of three 4-byte words, to terminate the
 session: 
 word0 OPCODE
 word1
 word20xFFFF
 0x0
 0x0
9. Close the TCP connection with the ATCA SOM.

#### Downloading a Bitstream to the FPGA

Download a bitstream to the FPGA over a TCP connection.

1. Open a TCP connection to the ATCA SOM on port 48871 (0xBEE7).
2. Over the open TCP connection, write a packet made up of three 4-byte words (12
 bytes total) of the following format: 
 word0 OPCODE
 word1 FPGA ID
 word20x2
 FPGA A = 0x1,
 FPGA B = 0x2,
 FPGA C = 0x3,
 FPGA D = 0x4,
 0x0
3. Read 4 bytes from the TCP connection following your write. 
 These bytes indicate the U32 return status of your download operation. A
 return status of zero indicates a successful transfer.
4. Send the following message, consisting of three 4-byte words, to terminate the
 session: 
 word0 OPCODE
 word1
 word20xFFFF
 0x0
 0x0
5. Close the TCP connection with the ATCA SOM.

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=getting-started.html language=enus -->
## TOPIC 00018: Getting Started

- bundle_id: `ni-atca-fpga-modules`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/getting-started.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: To get started using your NI-ATCA system and software, refer to the ATCA-3671 Getting Started Guide.The getting started guide provides information about the following tasks: Installing the software and driver Installing the adapter modules Configuring the hardware in MAX Programming the hardware Com

### Getting Started

To get started using your NI-ATCA system and software, refer to the *ATCA-3671
 Getting Started Guide*.

The getting started guide provides information about the following tasks:

- Installing the software and driver
- Installing the adapter modules
- Configuring the hardware in MAX
- Programming the hardware

Tip

Related information:

- ATCA-3671 Getting Started

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=installed-examples.html language=enus -->
## TOPIC 00019: Installed Examples

- bundle_id: `ni-atca-fpga-modules`
- source_path: `installed-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/installed-examples.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-ATCA FPGA Modules includes several example applications for LabVIEW. These examples serve as interactive tools and programming models. Additionally, you can use the examples as building blocks in your own applications.LabVIEW users can use the Example Finder to search or browse examples. NI-ATCA

### Installed Examples

NI-ATCA FPGA Modules includes several example applications for LabVIEW. These
 examples serve as interactive tools and programming models. Additionally, you can use the
 examples as building blocks in your own applications.

LabVIEW users can use the Example Finder to search or browse examples. NI-ATCA examples are
 classified by keyword, so you can search for a particular device or measurements
 function. With LabVIEW running, select Help»Find Examples to launch the NI Example Finder. The NI Example Finder offers two ways to
 access all installed LabVIEW example VIs and their descriptions.

- Click the Browse tab to locate NI-ATCA examples by task at Hardware Input and Output»ATCA .
- Click the Search tab to search all installed examples by keyword. For
 example, search ATCA to locate all NI-ATCA examples.

Examples also are available online that demonstrate NI-ATCA basics, such as using DRAM, acquiring
 data from adapter modules, and performing high throughput streaming. Refer to
 ni.com/examples to find these examples.

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=inter-fpga-socketed-clip-interfaces.html language=enus -->
## TOPIC 00020: Inter-FPGA Socketed CLIP Interfaces

- bundle_id: `ni-atca-fpga-modules`
- source_path: `inter-fpga-socketed-clip-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/inter-fpga-socketed-clip-interfaces.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-ATCA FPGA Modules includes Socketed CLIP examples for the inter-FPGA MGT groups.The ATCA-3671 - Aurora Pattern example project includes an optimally hardware-efficient implementation of the Aurora protocol across all inter-FPGA lanes running at 12.5 Gbps. For the Ring Up and Ring Down groups, the

### Inter-FPGA Socketed CLIP Interfaces

NI-ATCA FPGA Modules includes Socketed CLIP examples for the inter-FPGA MGT
 groups.

Note

Figure 4.

[IMAGE alt='image' src='GUID-2FA3B0C1-50B7-4CE5-9EA5-938ADD16640D-a5.gif']

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| diag_txp(14:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| diag_txn(14:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| diag_rxp(14:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| diag_rxn(14:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| diag_312p5_refclk(3:0) | In | N/A | Reference clock inputs for the shared 312.5 MHz oscillator. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| diag_jc_refclk(3:0) | In | N/A | Reference clock inputs for the GTH reference clock generated by the jitter cleaner. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| diag_sma_refclk(3:0) | In | N/A | Reference clock inputs for the shared front panel SMA connector. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| diag_fpga_ready | In | Async | Signal driven by fixed logic to indicate that all clocks and power supplies required by the FPGA are active and stable. |

Figure 5.

[IMAGE alt='image' src='GUID-82DAA115-2F80-4681-8FF5-03C13EF8813B-a5.gif']

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| ring_up_txp(15:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| ring_up_txn(15:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| ring_up_rxp(15:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| ring_up_rxn(15:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| ring_up_312p5_refclk(3:0) | In | N/A | Reference clock inputs for the shared 312.5 MHz oscillator. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| ring_up_jc_refclk(3:0) | In | N/A | Reference clock inputs for the GTH reference clock generated by the jitter cleaner. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| ring_up_sma_refclk(3:0) | In | N/A | Reference clock inputs for the shared front panel SMA connector. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| ring_up_fpga_ready | In | Async | Signal driven by fixed logic to indicate that all clocks and power supplies required by the FPGA are active and stable. |

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| ring_down_txp(15:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| ring_down_txn(15:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| ring_down_rxp(15:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| ring_down_rxn(15:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| ring_down_312p5_refclk(3:0) | In | N/A | Reference clock inputs for the shared 312.5 MHz oscillator. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| ring_down_jc_refclk(3:0) | In | N/A | Reference clock inputs for the GTH reference clock generated by the jitter cleaner. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| ring_down_sma_refclk(3:0) | In | N/A | Reference clock inputs for the shared front panel SMA connector. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| ring_down_fpga_ready | In | Async | Signal driven by fixed logic to indicate that all clocks and power supplies required by the FPGA are active and stable. |

Parent topic:

ATCA-3671 User-Accessible Multi-Gigabit Transceivers

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=jitter-cleaner-operation.html language=enus -->
## TOPIC 00021: ATCA-3671 Jitter Cleaner Operation

- bundle_id: `ni-atca-fpga-modules`
- source_path: `jitter-cleaner-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/jitter-cleaner-operation.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the ATCA-3671 Jitter Cleaner operation in default mode, including CLKinX input selection, fixed 122.88 MHz VCXO, and lock behavior. Default ModeBy default, the Jitter Cleaner operates in dual PLL with internal VCO mode, as shown in the following diagram. In this mode, the Jitter Cleaner

### ATCA-3671 Jitter Cleaner Operation

Learn about the ATCA-3671 Jitter Cleaner operation in default mode, including
 CLKinX input selection, fixed 122.88 MHz VCXO, and lock behavior.

#### Default Mode

By default, the
 Jitter Cleaner operates in dual PLL with internal VCO mode, as shown
 in the following diagram. In this mode, the Jitter Cleaner
 propagates a clock signal through two phase locked loops (PLLs) to
 generate a specific clock rate or clean an existing clock
 signal.

Figure 2.

[IMAGE alt='image' src='GUID-4491CC32-C14E-4E71-8754-3407DB40FD26-a5.png']

#### CLKinX

The
 CLKinX terminal provides input to the Jitter Cleaner. By default,
 the clock source of the Jitter Cleaner is set to the 100 MHz onboard
 reference clock.

To modify the signal used by the CLKinX,
 follow the instructions in *Configuring the Jitter Cleaner for
 Use as a Clock Source*. The input frequency must be
 specified to the Jitter Cleaner using the ATCA-3671
 Configure Jitter Cleaner VI or the
 minicom jc_set_input_freq command. These
 commands change the PLL1 R and N dividers accordingly.

#### VCXO

The VCXO is an external
 oscillator set at 122.88 MHz. The
 frequency of this oscillator is constant and cannot be
 configured.

#### Locking

If
 the Jitter Cleaner does not lock with your current settings, ensure
 that the jc_set_input command was provided with the
 actual CLKinX frequency and that the jc_set_vco
 command was called with 122.88 MHz as the VCXO frequency. If either
 of these commands is called with a frequency other than the actual
 signal, the dividers will be set incorrectly and the feedback and
 reference paths will not match.

If the input frequency and
 VCXO frequency are set correctly, the clock propagation and feedback
 paths will be the same frequency at each PLL. You can verify this by
 reading the R and N divider values from the register of the JC and
 plotting out the frequency along each path.

Refer to
 *ATCA-3671 Jitter Cleaning Phase Locked Loop
 (PLL)* or Section 9.1.5 of the *LMK0480X
 Datasheet* on www.ti.com to
 learn more about PLL locking.

Parent topic:

ATCA-3671 Clocking Features

Related concepts:

- ATCA-3671 Jitter Cleaning Phase-Locked Loop (PLL)

Related tasks:

- Configuring the Jitter Cleaner for Use as a Clock Source

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=mgt-lane-and-quad-mappings.html language=enus -->
## TOPIC 00022: MGT Lane and Quad Mappings

- bundle_id: `ni-atca-fpga-modules`
- source_path: `mgt-lane-and-quad-mappings.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/mgt-lane-and-quad-mappings.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn the lane and quad mappings for all MGTs on each ATCA-3671 FPGA.7 MGT Lane and Quad Mappings GTH Usage GTH Channel Quad Quad GTH Channel GTH Usage Reserved Reserved Reserved Reserved X0Y39 X0Y38 X0Y37 X0Y36 219 119 X1Y39 X1Y38 X1Y37 X1Y36 RingDown[15] RingDown[14] RingDown[13] RingDown[12]

### MGT Lane and Quad Mappings

Learn the lane and quad mappings for all MGTs on each ATCA-3671 FPGA.

| GTH Usage | GTH Channel | Quad |  | Quad | GTH Channel | GTH Usage |
| --- | --- | --- | --- | --- | --- | --- |
| Reserved Reserved Reserved Reserved | X0Y39 X0Y38 X0Y37 X0Y36 | 219 |  | 119 | X1Y39 X1Y38 X1Y37 X1Y36 | RingDown[15] RingDown[14] RingDown[13] RingDown[12] |
| Diag[11] Diag[10] Diag[9] Diag[8] | X0Y35 X0Y34 X0Y33 X0Y32 | 218 |  | 118 | X1Y35 X1Y34 X1Y33 X1Y32 | RingDown[11] RingDown[10] RingDown[9] RingDown[8] |
| Aio[15] Aio[14] Aio[13] Aio[12] | X0Y31 X0Y30 X0Y29 X0Y28 | 217 |  | 117 | X1Y31 X1Y30 X1Y29 X1Y28 | RingDown[7] RingDown[6] RingDown[5] RingDown[4] |
| Aio[11] Aio[10] Aio[9] Aio[8] | X0Y27 X0Y26 X0Y25 X0Y24 | 216 |  | 116 | X1Y27 X1Y26 X1Y25 X1Y24 | RingDown[3] RingDown[2] RingDown[1] RingDown[0] |
| Aio[7] Aio[6] Aio[5] Aio[4] | X0Y23 X0Y22 X0Y21 X0Y20 | 215 |  | 115 | X1Y23 X1Y22 X1Y21 X1Y20 | Rtm[15] Rtm[14] Rtm[13] Rtm[12] |
| Aio[3] Aio[2] Aio[1] Aio[0] | X0Y19 X0Y18 X0Y17 X0Y16 | 214 |  | 114 | X1Y19 X1Y18 X1Y17 X1Y16 | Rtm[11] Rtm[10] Rtm[9] Rtm[8] |
| RingUp[15] RingUp[14] RingUp[13] RingUp[12] | X0Y15 X0Y14 X0Y13 X0Y12 | 213 |  | 113 | X1Y15 X1Y14 X1Y13 X1Y12 | Rtm[7] Rtm[6] Rtm[5] Rtm[4] |
| RingUp[11] RingUp[10] RingUp[9] RingUp[8] | X0Y11 X0Y10 X0Y9 X0Y8 | 212 |  | 112 | X1Y11 X1Y10 X1Y9 X1Y8 | Rtm[3] Rtm[2] Rtm[1] Rtm[0] |
| RingUp[7] RingUp[6] RingUp[5] RingUp[4] | X0Y7 X0Y6 X0Y5 X0Y4 | 211 |  | 111 | X1Y7 X1Y6 X1Y5 X1Y4 | Diag[7] Diag[6] Diag[5] Diag[4] |
| RingUp[3] RingUp[2] RingUp[1] RingUp[0] | X0Y3 X0Y2 X0Y1 X0Y0 | 210 |  | 110 | X1Y3 X1Y2 X1Y1 X1Y0 | Diag[3] Diag[2] Diag[1] Diag[0] |

Parent topic:

ATCA-3671 User-Accessible Multi-Gigabit Transceivers

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=mgt-reference-clocks.html language=enus -->
## TOPIC 00023: MGT Reference Clocks

- bundle_id: `ni-atca-fpga-modules`
- source_path: `mgt-reference-clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/mgt-reference-clocks.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATCA-3671 family of devices provides a wide range of options for delivering reference clocks to each of the MGT interfaces in the system.Three MGT reference clocks are distributed to reach every MGT bank (Quad) in every FPGA on the ATCA-3671, as shown in the following table. 6 MGT Reference Cloc

### MGT Reference Clocks

The ATCA-3671 family of devices provides a wide range of options for delivering
 reference clocks to each of the MGT interfaces in the system.

Three MGT reference clocks are distributed to reach every MGT bank (Quad) in every FPGA on the ATCA-3671, as shown in the following table.

| MGT Reference Clock | Description |
| --- | --- |
| Fixed oscillator | A pair of fixed 312.5 MHz oscillators are used on the ATCA-3671 to deliver this common reference clock frequency to the entire board. One oscillator drives all reference clocks on FPGAs A and B, and the other drives all reference clocks on FPGAs C and D. |
| External SMA | An SMA connector on the front panel may be used to distribute an external reference clock to every transceiver on the entire board. |
| Jitter cleaner | Each FPGA has its own jitter-attenuating, dual-PLL device (LMK04808) that is capable of creating an ultra-low phase noise output that can be used as an MGT reference clock to all transceivers on the same FPGA. |

Additional reference clock options are available on the AIO and RTM interfaces.

Parent topic:

ATCA-3671 User-Accessible Multi-Gigabit Transceivers

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=minicom-commands.html language=enus -->
## TOPIC 00024: Minicom Commands

- bundle_id: `ni-atca-fpga-modules`
- source_path: `minicom-commands.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/minicom-commands.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use minicom commands to interact with the ATCA fixed logic microblaze directly.Once you have accessed the System-on-Module (SOM) according to the instructions in SOM Commands, start a minicom session by entering minicom <fpga> (where <fpga> is the letter of the desired FPGA—A B C D) in an SSH connec

### Minicom Commands

Use minicom commands to interact with the ATCA fixed logic
 microblaze directly.

Once you have accessed the System-on-Module (SOM) according to the instructions in *SOM
 Commands*, start a minicom session by entering minicom
 <fpga> (where
 <fpga> is the letter of the
 desired FPGA—A B C D) in an SSH connection.

The following table lists available minicom commands. You can enter numeric input in base ten (0) or hexadecimal (x0).

| Command | Usage |
| --- | --- |
| jc_spi_write <data> | Writes four bytes to the jitter cleaner. The last 5 bits of data specify the register's address. |
| jc_spi_read <address> | Reads four bytes from the jitter cleaner at given address. |
| jc_show_reg_vals | Prints out the register contents of the jitter cleaner. |
| jc_set_input_freq <input freq (khz)> <pdf_val [min\|max\|freq in hz] (optional)> <cp_current [100\|200\|400\|1600] (optional)> | Specifies the input frequency to the JC. You can also specify the PLL1 PDF and cp current. PLL1 R and N dividers are set accordingly. |
| jc_set_output_freq <gth/sma> <output freq (khz> | Sets output frequency for the GTH or SMA by modifying output dividers. Valid values must be factors of the VCO frequency. |
| jc_set_vco_freq <vcxo freq (khz)> <vco_freq (khz)> | Sets VCO/VCOX parameters for PLL2. The VCOX frequency specifies the external VCOX frequency and should always be set to 122.88 MHz. The VCO frequency may be set within the range of 2,750 MHz TO 3,072 MHz. PLL2 R and N dividers ARE automatically set to compatible values. |
| jc_enable_sma <true/false> | Enables/disables the jitter cleaner SMA output. |
| jc_get_status | Checks if the jitter cleaner reports locked. |
| jc_disable_lmk | Disables jitter cleaner. LMK can be re-enabled by setting the output frequency. |
| version | Displays code version. |

Parent topic:

ATCA-3671 SOM Commands

Related concepts:

- ATCA-3671 SOM Commands

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=ni-atca-fpga-modules-devices.html language=enus -->
## TOPIC 00025: NI-ATCA FPGA Modules Devices

- bundle_id: `ni-atca-fpga-modules`
- source_path: `ni-atca-fpga-modules-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/ni-atca-fpga-modules-devices.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the following NI-ATCA FPGA module devices.

### NI-ATCA FPGA Modules Devices

Learn about the following NI-ATCA FPGA module devices.

- [ATCA-3671 FPGA Module for ATCA](atca-3671-fpga-module-for-atca.html) Learn about the ATCA-3671 module, including the clocking features and user-accessible multi-gigabit transceivers (MGTs).
- [RTM-3661 PCI Express Rear Transition Module for ATCA](rtm-3661-pci-express-rear-transition-module-f.html) The RTM-3661 rear transition module provides PCI Express Gen3 x8 host connectivity and x4 Quad Small Form-factor Pluggable (QSFP) ports for every FPGA on the ATCA-3671.
- [AIO-3681 Digitizer Module for FMC](aio-3681-digitizer-module-for-fmc.html) The AIO-3681 is an expansion module that provides single- or dual-channel 12-bit analog-to-digital conversion at RF sampling rates up to 4 GS/s, depending on hardware configuration.
- [AIO-3682 Signal Generator Module for FMC](aio-3682-signal-generator-module-for-fmc.html) The AIO-3682 is an expansion module that provides dual-channel 14-bit digital-to-analog conversion at RF sampling rates up to 5.6 GS/s.
- [AIO-3691 High-Speed Serial Adapter Module](aio-3691-high-speed-serial-adapter-module.html) The AIO-3691 is an expansion module that provides 16 lanes of high-speed serial connectivity between each FPGA and the front panel of the ATCA-3671.

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=rtm-3661-front-panel-diagram.html language=enus -->
## TOPIC 00026: RTM-3661 Front Panel

- bundle_id: `ni-atca-fpga-modules`
- source_path: `rtm-3661-front-panel-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/rtm-3661-front-panel-diagram.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: View the RTM-3661 front panel.6 RTM-3661 Front Panel

### RTM-3661 Front Panel

View the RTM-3661 front panel.

Figure 6.

[IMAGE alt='image' src='GUID-05646B82-18FC-4C79-B9BC-E8C51A7AC70F-a5.png']

Parent topic:

RTM-3661 PCI Express Rear Transition Module for ATCA

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=rtm-3661-pci-express-rear-transition-module-f.html language=enus -->
## TOPIC 00027: RTM-3661 PCI Express Rear Transition Module for ATCA

- bundle_id: `ni-atca-fpga-modules`
- source_path: `rtm-3661-pci-express-rear-transition-module-f.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/rtm-3661-pci-express-rear-transition-module-f.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RTM-3661 rear transition module provides PCI Express Gen3 x8 host connectivity and x4 Quad Small Form-factor Pluggable (QSFP) ports for every FPGA on the ATCA-3671.The PCI Express ports support the latest Gen3 external cabling standard, and feature pass-through repeater devices on all transmit a

### RTM-3661 PCI Express Rear Transition Module for ATCA

The RTM-3661 rear transition module provides PCI Express Gen3 x8 host connectivity
 and x4 Quad Small Form-factor Pluggable (QSFP) ports for every FPGA on the
 ATCA-3671.

The PCI Express ports support the latest Gen3 external cabling standard, and feature pass-through repeater devices on all transmit and receive lanes to support 8.0 Gbps line rates over copper cables up to 3 m in length. The QSFP ports feature active retimer devices in the transmit direction only and support up to 10.4167 Gbps line rates over a variety of cables.

Refer to the specifications document for your hardware at ni.com/docs for
 complete specifications.

Parent topic:

NI-ATCA FPGA Modules Devices

Related information:

- RTM-3661 Specifications

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=rtm-3661-socketed-clip-interface.html language=enus -->
## TOPIC 00028: RTM-3661 Socketed CLIP Interface

- bundle_id: `ni-atca-fpga-modules`
- source_path: `rtm-3661-socketed-clip-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/rtm-3661-socketed-clip-interface.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-ATCA FPGA Modules include a Socketed CLIP example for the RTM-3661.The x8 PCI Express host interface is critical to operation of the ATCA-3671 FPGA module in LabVIEW and is contained in the fixed logic of the FPGA. Therefore, those MGT lanes are not included in the Socketed CLIP definition. Eight

### RTM-3661 Socketed CLIP Interface

NI-ATCA FPGA Modules include a Socketed CLIP example for the RTM-3661.

Note

Note

Figure 7.

[IMAGE alt='image' src='GUID-AB63F9F5-C518-4C78-9C73-98F7B1D170A6-a5.gif']

| Port | Direction | Clock Domain | Description |
| --- | --- | --- | --- |
| rtm_txp(7:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| rtm_txn(7:0) | Out (pad) | N/A | Dedicated high-speed serial transmit pins for GTH transceivers. |
| rtm_rxp(7:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| rtm_rxn(7:0) | In (pad) | N/A | Dedicated high-speed serial receive pins for GTH transceivers. |
| rtm_312p5_refclk(1:0) | In | N/A | Reference clock inputs for the shared 312.5 MHz oscillator. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| rtm_jc_refclk(1:0) | In | N/A | Reference clock inputs for the GTH reference clock generated by the jitter cleaner. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| rtm_sma_refclk(1:0) | In | N/A | Reference clock inputs for the shared front panel SMA connector. IBUFDS_GTE2 instances are already present in fixed logic, so these input ports are already buffered and may be used directly in the CLIP. Each clock signal in the vector is mapped to a GTH Quad in the same order as the TX/RX pairs. For example, refclk(0) should be used for the Quad containing txp/txn/rxp/rxn(3:0), and so on. |
| rtm_jc_srcclk | Out | N/A | Optional output signal which can be driven out from the CLIP to be used as the source clock for the jitter cleaner (useful for recovered-clock applications where the interface IP produces a clock that must be externally filtered for reuse as a reference clock). The source clock to be driven out to the jitter cleaner is selected using the External Clock Configuration properties window. |
| rtm_fpga_ready | In | Async | Signal driven by fixed logic to indicate that all clocks and power supplies required by the FPGA are active and stable. |

Parent topic:

RTM-3661 PCI Express Rear Transition Module for ATCA

<!--NI_TOPIC bundle=ni-atca-fpga-modules path=user-manual-welcome.html language=enus -->
## TOPIC 00029: NI-ATCA FPGA Modules User Manual

- bundle_id: `ni-atca-fpga-modules`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-atca-fpga-modules/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-atca-fpga-modules`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-ATCA FPGA Modules User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-ATCA FPGA Modules
 User Manual

The NI-ATCA FPGA Modules User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- ATCA-3671 Getting Started
- ATCA-3671 Specifications
- RTM-3661 Specifications
- AIO-3682 Specifications
- AIO-3691 Specifications
- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Dimensional Drawings
- Product Certifications
- Letter of Volatility
- Discussion Forums
- NI Learning Center
