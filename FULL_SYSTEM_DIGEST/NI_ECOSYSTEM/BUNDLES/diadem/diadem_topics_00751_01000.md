# NI DOCUMENT BUNDLE: diadem

<!--NI_BUNDLE_CHUNK bundle=diadem start=751 end=1000 -->
<!--NI_TOPIC bundle=diadem path=dlgvis/dlgvis/dlgvisxysymbol_dialog.htm language=enus -->
## TOPIC 00751: Display: Signal List » Symbol

- bundle_id: `diadem`
- source_path: `dlgvis/dlgvis/dlgvisxysymbol_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgvis/dlgvis/dlgvisxysymbol_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([DIAdem VISUAL](../dlgvis/dlgvis_general.htm) | [Single Point Processing Dialog Boxes](../../dlgdacsv/dac_dlgssinglevalues_overview.htm)) > [Display Instruments](../dlgvis/dlgvis_signaldisplay_general.htm) > [XY-Display](../dlgvis/dlgvislistxy_dialog.htm) > Display: Signal List » Symbol

Display: Signal List » Symbol

Use this dialog box to specify the symbol for the xy-display.

#### Settings

|  | Symbol | Specifies with which symbol the xy display plots the curve. |
| --- | --- | --- |
|  | Symbol graphic file | Shows the name and the path of the loaded graphics file. Use this setting if you select the symbol Graphic. |
|  | Browse | Opens the dialog box where you select a graphics file. |
|  | Size | Specifies the size of the displayed symbol. |

#### Further Settings

[Signal List](../dlgvis/dlgvislistxy_dialog.htm) | » Symbol | [Parameters](../dlgvis/dlgvisxy_dialog.htm) | [Limit Values](../dlgvis/dlgvislimitdef_dialog.htm) | [Frame](../dlgvis/dlgvisframe_dialog.htm) | [Labels](../dlgvis/dlgvislabellegscale_dialog.htm) | [Position](../dlgvis/dlgvispos_dialog.htm) | [Inputs»Data](../dlgvis/dlgvisdatainpsxy_dialog.htm) | [Inputs»Control](../dlgvis/dlgvisctrlinpstartstopreset_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dmc/dmc.htm language=enus -->
## TOPIC 00752: General Information about the HBM DMC 9012A Device Driver

- bundle_id: `diadem`
- source_path: `dmc/dmc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmc/dmc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

General Information about the HBM DMC 9012A Device Driver

General Information about the HBM DMC 9012A Device Driver

The HBM DMC 9012A device driver operates the measurement amplifier DMC 9012A manufactured by Hottinger Baldwin Messtechnik (HBM).

You need at least one base device and one board to operate the measurement amplifier. You can use up to 12 plug-in boards with the base device. The plug-in boards that you use determine which input-signals are acquired in which measurement ranges.

The IEEE bus connects the device to the computer. You must install an appropriate interface on the computer. The DMC 9012A has a measurement value memory for 24,000 values (optional 120,000).

DIAdem supports the following plug-in boards for the DMC 9012A measurement amplification system:

[DMV10](../dmc/dmv10.htm)

[DMV30](../dmc/dmv30.htm)

[DMV35](../dmc/dmv35.htm)

[DMV50](../dmc/dmv50.htm)

[DMV55](../dmc/dmv55.htm)

If you want to use the measurement amplification system, you must first register the device driver in the device definition.

You only can use the HBM DMC device driver to define inputs (data acquisition). For more information on the required settings, refer to the specific help topics.

[Acquisition Device Definition for HBM DMC 9012A](../dmc/erf_dmc.htm).

#### See Also

[Generating a Device Definition](../dlgdacsv/dac_dlg_general/geraetedefinition.htm)

<!--NI_TOPIC bundle=diadem path=dmc/dmv10.htm language=enus -->
## TOPIC 00753: Supported Functions of the DMV10 Plug-In Board

- bundle_id: `diadem`
- source_path: `dmc/dmv10.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmc/dmv10.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMC 9012A](../dmc/dmc.htm) > Supported Functions of the DMV10 Plug-In Board

Supported Functions of the DMV10 Plug-In Board

The following section lists the device parameter settings and DIAdem-supported functions of the DMV10 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for DMC 9012A

| IEEE address | An IEEE bus address consists of the device address and an offset of 700. Valid entries range from 701 to 730. |
| --- | --- |
| Conv. rate | If you select the standard measurement mode with and without external clock, enter the measurement rate set on the measurement device. The measurement rate must not be greater than the setting for the sampling rate. |
| Sampling rate | Sampling rate that the amplifiers sample and digitize input signals with. The number of activated amplifiers determines with how many sampling rates the amplification system runs. For further details, refer to the manual for the DMC 9012A measurement amplification system. |
|  | The maximum measurement rate is limited by the sampling rate. The measurement rate and the sampling rate ratio must always produce an integer number. You also must configure all measurement amplifiers that you use in a measurement with the same measurement and sampling rate. |
| Trigger slave | You can operate multiple DMC 9012A systems by synchronizing them one under the other with special hardware cables. One device (the trigger master) can control the other devices (the trigger slaves). If you do not want synchronous triggering, select "No". |

#### Features of the DMV10 Plug-In Board

The DMV10 plug-in board functions that DIAdem supports are listed in the following.

| Limit frequency | 800 Hz |
| --- | --- |
| For input signal: | (-1 dB) |

#### Measurement ranges

| DC voltage | ±100 mV, ±10 V |
| --- | --- |
| Thermocouples | J, K, T, S |

#### Comment

Used only in connection with the basic device DMC 9012A.

#### See Also

[Device Parameters for HBM DMC 9012A](../dmc/trb_par_dmc.htm)

[Acquisition Device Definition for HBM DMC 9012A](../dmc/erf_dmc.htm)

[Acquisition Signal Parameters for HBM DMC 9012A](../dmc/erf_par_dmc.htm)

<!--NI_TOPIC bundle=diadem path=dmc/dmv30.htm language=enus -->
## TOPIC 00754: Supported Functions of the DMV30 Plug-In Board

- bundle_id: `diadem`
- source_path: `dmc/dmv30.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmc/dmv30.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMC 9012A](../dmc/dmc.htm) > Supported Functions of the DMV30 Plug-In Board

Supported Functions of the DMV30 Plug-In Board

The following section lists the device parameter settings and DIAdem-supported functions of the DMV30 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for DMC 9012A

| IEEE address | An IEEE bus address consists of the device address and an offset of 700. Valid entries range from 701 to 730. |
| --- | --- |
| Measurement rate | If you select the standard measurement mode with and without external clock, enter the measurement rate set on the measurement device. The measurement rate must not be greater than the setting for the sampling rate. |
| Sampling rate | Sampling rate that the amplifiers sample and digitize input signals with. The number of activated amplifiers determines with how many sampling rates the amplification system runs. For further details, refer to the manual for the DMC 9012A measurement amplification system. |
|  | The maximum measurement rate is limited by the sampling rate. The measurement rate and the sampling rate ratio must always produce an integer number. You also must configure all measurement amplifiers that you use in a measurement with the same measurement and sampling rate. |
| Trigger slave | You can operate multiple DMC 9012A systems by synchronizing them one under the other with special hardware cables. One device (the trigger master) can control the other devices (the trigger slaves). If you do not want synchronous triggering, select "No". |

#### Features of the DMV30 Plug-In Board

The functions of the MC30 plug-in board that DIAdem supports are listed in the following.

| Limit frequency | 120 Hz |
| --- | --- |
| For input signal: | (-1 dB) |

#### Measurement ranges

| DC voltage | ±10 V |
| --- | --- |
| Strain gauge bridges | ± 3 mV/V |

#### Disk Frequency

| For measurement bridges | 600 Hz |
| --- | --- |

#### Bridge supply voltage

| For strain gauge bridges | 5 V, 2 V, 1 V |
| --- | --- |

#### Comment

Used only in connection with the basic device DMC 9012A.

#### See Also

[Device Parameters for HBM DMC 9012A](../dmc/trb_par_dmc.htm)

[Acquisition Device Definition for HBM DMC 9012A](../dmc/erf_dmc.htm)

[Acquisition Signal Parameters for HBM DMC 9012A](../dmc/erf_par_dmc.htm)

<!--NI_TOPIC bundle=diadem path=dmc/trb_par_dmc.htm language=enus -->
## TOPIC 00755: Device Parameters for HBM DMC 9012A

- bundle_id: `diadem`
- source_path: `dmc/trb_par_dmc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmc/trb_par_dmc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMC 9012A](../dmc/dmc.htm) > Device Parameters for HBM DMC 9012A

Device Parameters for HBM DMC 9012A

The following section describes the parameters for the [HBM DMC 9012A](../dmc/dmc.htm) device driver.

You must install an IEEE 488 bus interface board before you can run a measurement. For more information about the device-specific parameters (for example, IEEE 488 bus address, measurement rate, sampling rate), refer to the technical documentation provided by your hardware manufacturer.

The following plug-in boards are available for the DMC measurement amplification system:

[DMV10](../dmc/dmv10.htm)

[DMV30](../dmc/dmv30.htm)

[DMV35](../dmc/dmv35.htm)

[DMV50](../dmc/dmv50.htm)

[DMV55](../dmc/dmv55.htm)

When the measurement starts, DIAdem checks the parameters of the driver.

#### Hardware Requirements

The computer (processor, clock rate, amount of memory, hard drive, configuration ...) you use determines the total sampling rate. Therefore the help only can indicate approximate values.

#### See Also

[General Help for Device Settings](../dlgdacsv/dac_dlg_general/geraetedefinition.htm)

[Acquisition Device Definition for HBM DMC 9012A](../dmc/erf_dmc.htm)

[Acquisition Signal Parameters for HBM DMC 9012A](../dmc/erf_par_dmc.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/dv10.htm language=enus -->
## TOPIC 00756: Supported Features of the DV10 Board

- bundle_id: `diadem`
- source_path: `dmcplus/dv10.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/dv10.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Supported Features of the DV10 Board

Supported Features of the DV10 Board

The following section lists the device parameter settings and DIAdem-supported functions of the DV10 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for the DMCplus

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. The device address determines for the serial interfaces COM1 and COM2 whether the RS-232 interface or the RS-485 interface of the DMCplus communicates with the device. |
| --- | --- |
| Device address | The device address depends on the interface |
|  | IEEE-488 bus |
|  | The device address is the same as the device address set at DMCplus. Valid addresses range from 1 to 30 |
|  | RS-232 |
|  | In this case enter the address 0 |
|  | RS-485 |
|  | Enter the address set at DMCplus Valid entries range from 1 to 30. |
| Integration time | Only set the integration time for the connected amplifiers in the Standard measurement mode. This directly affects the measurement time for individual amplifiers and the maximum attainable sampling rate. |
| Filename | Name of the file in which the measured values are stored. |

#### Features of the DV10 Plug-In Board

The DV10 plug-in board functions that DIAdem supports are listed in the following.

| Sensor | Strain gauge half and full bridges |
| --- | --- |
|  | Potentiometer |

Measurement ranges:

| DC voltage | ±10V |
| --- | --- |
| Strain gauge bridges | ± 1.25 mV/V...± 1280 mV/V |

Disk frequency:

| For measurement bridges: | DC |
| --- | --- |
| Sensor supply: | 0.625 V, 1.25 V, 2.5 V, 5 V |
| Precision class | 0.02 |
| Band width | 4.4 kHz (-3 dB) |

Note:

Used only in connection with the base device DMCplus.

#### See Also

[Device Parameters for HBM DMCplus](../dmcplus/trb_par_dmcplus.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/dv30.htm language=enus -->
## TOPIC 00757: Supported Features of the DV30 Board

- bundle_id: `diadem`
- source_path: `dmcplus/dv30.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/dv30.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Supported Features of the DV30 Board

Supported Features of the DV30 Board

The following section lists the device parameter settings and DIAdem-supported functions of the DV30 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for the DMCplus

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. The device address determines for the serial interfaces COM1 and COM2 whether the RS-232 interface or the RS-485 interface of the DMCplus communicates with the device. |
| --- | --- |
| Device address | The device address depends on the interface |
|  | IEEE-488 bus |
|  | The device address is the same as the device address set at DMCplus. Valid addresses range from 1 to 30 |
|  | RS-232 |
|  | In this case enter the address 0 |
|  | RS-485 |
|  | Enter the address set at DMCplus Valid entries range from 1 to 30. |
| Integration time | Only set the integration time for the connected amplifiers in the Standard measurement mode. This directly affects the measurement time for individual amplifiers and the maximum attainable sampling rate. |
| Filename | For the Disk measurement mode, enter the file for storing the measured values without an extension. |

#### Features of the DV30 Plug-In Board

The DV30 plug-in board functions that DIAdem supports are listed in the following.

| Sensor | Strain gauge half and full bridges |
| --- | --- |
|  | Potentiometer |

Measurement ranges:

| DC voltage | ±10V |
| --- | --- |
| Strain gauge bridges | ± 1.25 mV/V...± 1280 mV/V |

Disk frequency:

| For measurement bridges: | 600 Hz |
| --- | --- |
| Sensor supply: | 0.625 V, 1.25 V, 2.5 V, 5 V |
| Precision class | 0.02 |
| Band width | 250 Hz (-3 dB) |

Note:

Used only in connection with the base device DMCplus.

#### See Also

[Device Parameters for HBM DMCplus](../dmcplus/trb_par_dmcplus.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/dv35.htm language=enus -->
## TOPIC 00758: Supported Functions of the DV35 Plugin Board

- bundle_id: `diadem`
- source_path: `dmcplus/dv35.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/dv35.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Supported Functions of the DV35 Plugin Board

Supported Functions of the DV35 Plugin Board

The following section lists the device parameter settings and DIAdem-supported functions of the DV35 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for the DMCplus

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. The device address determines for the serial interfaces COM1 and COM2 whether the RS-232 interface or the RS-485 interface of the DMCplus communicates with the device. |
| --- | --- |
| Device address | The device address depends on the interface |
|  | IEEE-488 bus |
|  | The device address is the same as the device address set at DMCplus. Valid addresses range from 1 to 30 |
|  | RS-232 |
|  | In this case enter the address 0 |
|  | RS-485 |
|  | Enter the address set at DMCplus Valid entries range from 1 to 30. |
| Integration time | Only set the integration time for the connected amplifiers in the Standard measurement mode. This directly affects the measurement time for individual amplifiers and the maximum attainable sampling rate. |
| Filename | Name of the file in which the measured values are stored. |

#### Capabilities of the DV35 Plugin Board

The DV35 plug-in board functions that DIAdem supports are listed in the following.

| Sensor | Pt100 |
| --- | --- |
|  | Resistances |
|  | Single-DMS |

Measurement ranges:

| DC voltage | ±10V |
| --- | --- |
| Resistances | 50 Ohm, 500 Ohm, 5 kOhm, 50 kOhm |
| Pt100 | Yes |
| Pt1000 | Yes |

Disk frequency:

| For measurement bridges: | 600 Hz |
| --- | --- |
| Sensor supply: | 0.025 mA, 2.5 mA |
| Precision class | 0.02 |
| Band width | 250 Hz (-3 dB) |

Note:

Used only in connection with the base device DMCplus.

#### See Also

[Device Parameters for HBM DMCplus](../dmcplus/trb_par_dmcplus.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/dv55.htm language=enus -->
## TOPIC 00759: Supported Functions of the DV55 Board

- bundle_id: `diadem`
- source_path: `dmcplus/dv55.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/dv55.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Supported Functions of the DV55 Board

Supported Functions of the DV55 Board

The following section lists the device parameter settings and DIAdem-supported functions of the DV55 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for the DMCplus

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. The device address determines for the serial interfaces COM1 and COM2 whether the RS-232 interface or the RS-485 interface of the DMCplus communicates with the device. |
| --- | --- |
| Device address | The device address depends on the interface |
|  | IEEE-488 bus |
|  | The device address is the same as the device address set at DMCplus. Valid addresses range from 1 to 30 |
|  | RS-232 |
|  | In this case enter the address 0 |
|  | RS-485 |
|  | Enter the address set at DMCplus Valid entries range from 1 to 30. |
| Integration time | Only set the integration time for the connected amplifiers in the Standard measurement mode. This directly affects the measurement time for individual amplifiers and the maximum attainable sampling rate. |
| Filename | Name of the file in which the measured values are stored. |

#### Capabilities of the DV55 board

The DV55 plug-in board functions that DIAdem supports are listed in the following.

| Sensor | Pt100 |
| --- | --- |
|  | Resistances |
|  | Single-DMS |

Measurement ranges:

| DC voltage: | ±10 V |
| --- | --- |
| Strain gauge bridges: | ± 1.25 mV/V...± 1280 mV/V |

Disk frequency:

| For measurement bridges: | 4.8 kHz |
| --- | --- |
| Sensor supply: | 0.625V, 1.25V, 2.5V, 5V |
| Precision class | 0.02 |
| Band width | 2.2 kHz (-3 dB) |

Note:

Used only in connection with the base device DMCplus.

#### See Also

[Device Parameters for HBM DMCplus](../dmcplus/trb_par_dmcplus.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/dv60.htm language=enus -->
## TOPIC 00760: Supported Functions of the DV60 Board

- bundle_id: `diadem`
- source_path: `dmcplus/dv60.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/dv60.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Supported Functions of the DV60 Board

Supported Functions of the DV60 Board

The following section lists the device parameter settings and DIAdem-supported functions of the DV60 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for the DMCplus

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. The device address determines for the serial interfaces COM1 and COM2 whether the RS-232 interface or the RS-485 interface of the DMCplus communicates with the device. |
| --- | --- |
| Device address | The device address depends on the interface |
|  | IEEE-488 bus |
|  | The device address is the same as the device address set at DMCplus. Valid addresses range from 1 to 30 |
|  | RS-232 |
|  | In this case enter the address 0 |
|  | RS-485 |
|  | Enter the address set at DMCplus Valid entries range from 1 to 30. |
| Integration time | Only set the integration time for the connected amplifiers in the Standard measurement mode. This directly affects the measurement time for individual amplifiers and the maximum attainable sampling rate. |
| Filename | Name of the file in which the measured values are stored. |

#### Features of the DV60 Plug-In Board

The DV60 plug-in board functions that DIAdem supports are listed in the following.

| Sensor | HBM-torque measurement waves T30FN...T36FN |
| --- | --- |
|  | Measurement transmitter MBL40 |
|  | Frequency provider |

Measurement signal inputs:

| Torque: | 10±5 kHz / 5..20Vss |
| --- | --- |
| Nominal signal range: | 5 kHz |
| RPM | 2 impulse sources offset by p /2 |
| Impulse sequence-Frequency domain | 2 kHz, 20 kHz, 200 kHz |

Note:

Used only in connection with the base device DMCplus.

#### See Also

[Device Parameters for HBM DMCplus](../dmcplus/trb_par_dmcplus.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/dz65.htm language=enus -->
## TOPIC 00761: Supported Functions of the DZ65 Board

- bundle_id: `diadem`
- source_path: `dmcplus/dz65.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/dz65.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Supported Functions of the DZ65 Board

Supported Functions of the DZ65 Board

The following section lists the device parameter settings and DIAdem-supported functions of the DZ65 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for the DMCplus

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. The device address determines for the serial interfaces COM1 and COM2 whether the RS-232 interface or the RS-485 interface of the DMCplus communicates with the device. |
| --- | --- |
| Device address | The device address depends on the interface |
|  | IEEE-488 bus |
|  | The device address is the same as the device address set at DMCplus. Valid addresses range from 1 to 30 |
|  | RS-232 |
|  | In this case enter the address 0 |
|  | RS-485 |
|  | Enter the address set at DMCplus Valid entries range from 1 to 30. |
| Integration time | Only set the integration time for the connected amplifiers in the Standard measurement mode. This directly affects the measurement time for individual amplifiers and the maximum attainable sampling rate. |
| Filename | Name of the file in which the measured values are stored. |

#### Features of the DZ65 Board

The DZ65 plug-in board functions that DIAdem supports are listed in the following.

| Counter inputs | 2 |
| --- | --- |
| Operating modes | Increment/reverse counter |
|  | Incrementer/reverse counter (Modulo counter) |
|  | Period measurement |
|  | Frequency measurement |
| Nominal number range | ± 4 000 000 |

Note:

Used only in connection with the base device DMCplus.

#### See Also

[Device Parameters for HBM DMCplus](../dmcplus/trb_par_dmcplus.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/erf_dmcplus.htm language=enus -->
## TOPIC 00762: Acquisition Device Definition for HBM DMCplus

- bundle_id: `diadem`
- source_path: `dmcplus/erf_dmcplus.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/erf_dmcplus.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Acquisition Device Definition for HBM DMCplus

Acquisition Device Definition for HBM DMCplus

The HBM MGCplus device driver operates the DMCplus measurement amplifier made by Hottinger Baldwin Messtechnik (HBM).

#### Settings

| Name | Name of the device definition |
| --- | --- |
| Driver | Selected device driver HBM DMCplus |
|  | The selected device determines which signal types are available (for example DV 0.625V, DC, TC S, ....). |
| Device parameters | Hardware settings for the HBM DMCplus device driver (for example, interface, device address, integration time). Special help sections for the boards list the device parameters. |

The IEEE 488 bus or the V.24 interface connect the measurement amplification system to the computer. You must install the appropriate interface board to operate the measurement amplifier over the IEEE 488 bus.

When the measurement starts, DIAdem checks the parameters of the driver.

#### See Also

[General Help for Device Settings](../dlgdacsv/dac_dlg_general/geraetedefinition.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/erf_par_dmcplus.htm language=enus -->
## TOPIC 00763: Acquisition Signal Parameters for HBM DMCplus

- bundle_id: `diadem`
- source_path: `dmcplus/erf_par_dmcplus.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/erf_par_dmcplus.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Acquisition Signal Parameters for HBM DMCplus

Acquisition Signal Parameters for HBM DMCplus

The HBM MGCplus device driver operates the DMCplus measurement amplifier made by Hottinger Baldwin Messtechnik (HBM).

The amplification board you use determines which input signals are connected to the measurement amplifier DMCplus. The HBM DMCplus driver supports amplifier plug-ins DV01, DV10, DV30, DV35, DV55, DV60 and DZ65.

Note: 
Not every amplifier board can support all input modes. DIAdem interrupts the measurement if you select an input mode that is incorrect for the particular amplifier.

To run a measurement with this device driver, you must install an interface board. The parameter settings that you need for the signal types are listed in the following.

#### Settings

| Signal type | Name of the signal type |
| --- | --- |
| Device | Name of the device definition |
| Signal type/parameters | Software-controlled parameters for the various plug-in board functions (for example, type of sensor and measurement range of the amplifier board). Possible settings are listed in the following. |
| Device | Opens the dialog box where you set the device parameters. |

#### Signal Types of the DV01 Plug-In Board

| DC | DC voltage |
| --- | --- |
| TC S | Thermovoltages to type S thermocouple. |
| TC T | Thermovoltages to type K thermocouple. |
| TC K | Thermovoltages to type K thermocouple. |
| TC J | Thermovoltages to type J thermocouple. |
| Current | Current (20 mA, 200 mA) |
| default | Contains the parameter settings on the DMCplus, because the ASA command is not sent. |

#### Signal types of the DV10 and DV30 plug-in boards

| DC | DC voltage |
| --- | --- |
| DV 0.625V | Strain gauge full bridges and half bridges |
| DV 1.25V | Strain gauge full bridges and half bridges |
| DV 2.5V | Strain gauge full bridges and half bridges |
| DV 5V | Strain gauge full bridges and half bridges |
| default | Contains the parameter settings on the DMCplus, because the ASA command is not sent. |

#### Signal types of the DV35 plug-in devices

| DC | DC voltage |
| --- | --- |
| Ohm | Resistances |
| default | Contains the parameter settings on the DMCplus, because the ASA command is not sent. |

#### Signal types of the DV55 plug-in device

| DC | DC voltage |
| --- | --- |
| DV 0.625V | Strain gauge full bridges and half bridges |
| DV 1.25V | Strain gauge full bridges and half bridges |
| DV 2.5V | Strain gauge full bridges and half bridges |
| DV 5V | Strain gauge full bridges and half bridges |
| IV 0.625V | Inductive full bridges with 0.625 V bridge supply voltage |
| IV 1.25V | Inductive full bridges with 1.25 V bridge supply voltage |
| IV 2.5V | Inductive full bridges with 2.5 V bridge supply voltage |
| IV 5V | Inductive full bridges with 5 V bridge supply voltage |
| default | Contains the parameter settings on the DMCplus, because the ASA command is not sent. |

#### Signal types of the DV60-Board

n(2 kHz):Measuring the revs at torque measurement waves with impulse frequencies until 2 kHz.

n(20 kHz):Measuring the revs at torque measurement waves with impulse frequencies until 20 kHz.

n(200 kHz):Measuring the revs at torque measurement waves with impulse frequencies until 200 kHz.

#### Signal types of the DZ65-Board

| Counter | Impulse counting |
| --- | --- |

#### Further Settings

The input mode determines whether you must set further parameters for the input type.

| Signal | Signal to be measured |
| --- | --- |
| Zero signal |  |
| Amplifier internal zero signal |  |
| Cal. sig. |  |
|  | Amplifier internal calibration signal |
| Measurement signal (Bu) | Input signal with Butterworth-filter |
| Meas. sig. (Be) | Input signal with Bessel filter |
|  | When you select the input signal, you must connect a signal recorder to the corresponding input on the DMCplus. |
|  | Zero sig. and cal sig. are amplifier-internal zero and calibration signals that you can use for testing a DIAdem DAC configuration. If you select Meas. sig.(Be) or Meas. sig.(Bu), the sensor measurement signal to the measurement amplifier input is interrupted. The (Be) or (Bu) extension specifies which filter type to use for filtering the signal in DMCplus. Specify the filter frequency in the parameter limit frequency. |
| Limit frequency | Specifies a digital filter, which filters the sensor signal online, in the DMCplus. If you select "off", no filtering takes place. |
|  | If you use the standard measurement mode, the integration time determines the filter frequencies. If the integration time and limit frequency are incompatible, DIAdem aborts the measurement preparations. For all other measurement modes this driver supports, the range of filter frequencies depends on the sampling rate. DIAdem checks the corresponding limit frequencies during the measurement preparations and adapts them as necessary. |
| Tara mem. | Calculation of the measured signal in DMCplus with a tare value. Every amplifier input has 2 Tara memories (Tara 0 and Tara 1). If you do not want taring, select "off". |
| Compensation | Every amplifier can be calibrated before the measurement. The following alternatives are available: |
|  | Off |
|  | No calibration |
|  | Tara 0 |
|  | When the measurement preparation starts, DIAdem saves the current measurement value in the zero memory (Tara 0) of DMCplus as the tare value. |
|  | Tara 1 |
|  | When the measurement preparation starts, DIAdem saves the current measurement value in the zero memory (Tara 1) of DMCplus as the tare value. |
|  | Calib. |
|  | Calibration of the specified amplifier |
|  | Calib. + Tara 0 |
|  | Calibration of the amplifier and storage of the measurement signal in the zero memory (tare 0). |
| Generator | Generator for the activation and deactivation of the torque measurement waves. |
| Switch | Specifying the switch type to adapt the connected sensor. Refer to the DMCplus manual for further information. |
| Mode | Operation mode for the counter |
|  | Counter |
|  | Pulse counter |
|  | Mod n |
|  | Impulse counter modulo n |
|  | Mod n scaled |
|  | Impulse counter modulo n with the output value scaled for the area 0..1 |
|  | Carry over |
|  | Count from the transfer from the 1. counter |
|  | 1 s .. 1000 s |
|  | Frequency measurements with gate times between 1 and 1000 seconds |
|  | 10 kHz..1 Mhz |
|  | Pulse width measurement with internal count frequencies between 10 kHz and 1 MHz. |
| Threshold | Sets the threshold value for impulse count. |
| Reset | Sets the function of the C input on the counter board (see DMCplus manual). |
|  | Off |
|  | The C input has no function |
|  | Lock |
|  | The counter function can be disabled at the C-entry |
|  | Delete |
|  | The counter can be reset at the C entry. |
| No. | The counting range for modulo n counts. |

When the measurement starts, DIAdem checks the parameters of the driver.

#### See Also

[General Help for Device Settings](../dlgdacsv/dac_dlg_general/geraetedefinition.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=dmcplus/trb_par_dmcplus.htm language=enus -->
## TOPIC 00764: Device Parameters for HBM DMCplus

- bundle_id: `diadem`
- source_path: `dmcplus/trb_par_dmcplus.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dmcplus/trb_par_dmcplus.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM DMCplus](../dmcplus/dmcplus.htm) > Device Parameters for HBM DMCplus

Device Parameters for HBM DMCplus

The following section describes the parameters for the [HBM DMCplus](../dmcplus/dmcplus.htm) device driver.

You must install the appropriate interface board to operate the measurement amplifier over the IEEE 488 bus. For specific device parameters (for example, interface, device address), refer to the technical documentation provided by your hardware manufacturer.

The following plug-in boards are available for the DMCplus measurement amplification system:

[DV01](../dmcplus/dv01.htm)

[DV10](../dmcplus/dv10.htm)

[DV30](../dmcplus/dv30.htm)

[DV35](../dmcplus/dv35.htm)

[DV55](../dmcplus/dv55.htm)

[DV60](../dmcplus/dv60.htm)

[DZ65](../dmcplus/dz65.htm)

When the measurement starts, DIAdem checks the parameters of the driver.

#### Hardware Requirements

The computer (processor, clock rate, amount of memory, hard drive, configuration ...) you use determines the total sampling rate. Therefore the help only can indicate approximate values.

#### See Also

[General Help for Device Settings](../dlgdacsv/dac_dlg_general/geraetedefinition.htm)

[Acquisition Device Definition for HBM DMCplus](../dmcplus/erf_dmcplus.htm)

[Acquisition Signal Parameters for HBM DMCplus](../dmcplus/erf_par_dmcplus.htm)

<!--NI_TOPIC bundle=diadem path=ecumcdrv/ecumcdrv/ecumcdrv_datainputs_dialog.htm language=enus -->
## TOPIC 00765: Inputs » Data

- bundle_id: `diadem`
- source_path: `ecumcdrv/ecumcdrv/ecumcdrv_datainputs_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ecumcdrv/ecumcdrv/ecumcdrv_datainputs_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[ECU Measurement and Calibration Toolkit](../ecumcdrv/ecumcdrv_general.htm) > Inputs » Data

Inputs » Data

Use this dialog box to specify the incoming data signals.

Refer to [Block Terminals in DIAdem DAC](../../gendacsv/dac_general/block_general.htm) for more information on block terminals. Refer to the page [Buses in DIAdem DAC](../../gendacsv/dac_general/wires.htm) for more information on the buses that you use to connect blocks.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| Signal Name | Specifies the name of the connected signal. |
| Terminal Name | Specifies the terminal name. |

#### Further Settings

[ECU](../ecumcdrv/ecumcdrv_ecu_definition_dialog.htm) | Communication: [CAN](../ecumcdrv/ecumcdrv_ecu_can_dialog.htm) | Communication: [Ethernet](../ecumcdrv/ecumcdrv_ecu_tcpip_dialog.htm) [»DAQ List»](../ecumcdrv/ecumcdrv_ecu_daq_dialog.htm) [Signal List](../ecumcdrv/ecumcdrv_ecu_daq_signals_dialog.htm) | [Signal Filter](../ecumcdrv/ecumcdrv_filter_dialog.htm) | [User dialog](../ecumcdrv/ecumcdrv_userdialog_dialog.htm) | Inputs »Data | [Inputs »System](../ecumcdrv/ecumcdrv_systeminput_dialog.htm) | [Outputs»Data](../ecumcdrv/ecumcdrv_dataoutputs_dialog.htm)

<!--NI_TOPIC bundle=diadem path=ecumcdrv/ecumcdrv/ecumcdrv_dataoutputs_dialog.htm language=enus -->
## TOPIC 00766: Outputs » Data

- bundle_id: `diadem`
- source_path: `ecumcdrv/ecumcdrv/ecumcdrv_dataoutputs_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ecumcdrv/ecumcdrv/ecumcdrv_dataoutputs_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[ECU Measurement and Calibration Toolkit](../ecumcdrv/ecumcdrv_general.htm) > Outputs » Data

Outputs » Data

Use this dialog box to specify the outgoing data signals.

Refer to [Block Terminals in DIAdem DAC](../../gendacsv/dac_general/block_general.htm) for more information on block terminals. Refer to the page [Buses in DIAdem DAC](../../gendacsv/dac_general/wires.htm) for more information on the buses that you use to connect blocks.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| Signal Name | Specifies the name of the connected signal. |

#### Further Settings

[ECU](../ecumcdrv/ecumcdrv_ecu_definition_dialog.htm) | Communication: [CAN](../ecumcdrv/ecumcdrv_ecu_can_dialog.htm) | Communication: [Ethernet](../ecumcdrv/ecumcdrv_ecu_tcpip_dialog.htm) » [DAQ List](../ecumcdrv/ecumcdrv_ecu_daq_dialog.htm) » [Signal List](../ecumcdrv/ecumcdrv_ecu_daq_signals_dialog.htm) | [Signal Filter](../ecumcdrv/ecumcdrv_filter_dialog.htm) | [User Dialog Box](../ecumcdrv/ecumcdrv_userdialog_dialog.htm) | [Inputs»Data](../ecumcdrv/ecumcdrv_datainputs_dialog.htm) | [Inputs»System](../ecumcdrv/ecumcdrv_systeminput_dialog.htm) | Outputs»Data

<!--NI_TOPIC bundle=diadem path=ecumcdrv/ecumcdrv/ecumcdrv_filter_dialog.htm language=enus -->
## TOPIC 00767: ECU Measurement and Calibration Toolkit: Signal Filter

- bundle_id: `diadem`
- source_path: `ecumcdrv/ecumcdrv/ecumcdrv_filter_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ecumcdrv/ecumcdrv/ecumcdrv_filter_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[ECU Measurement and Calibration Toolkit](../ecumcdrv/ecumcdrv_general.htm) > ECU Measurement and Calibration Toolkit: Signal Filter

ECU Measurement and Calibration Toolkit: Signal Filter

Use this dialog box to display only some of the available ECU signals.

Define the filters in a text file. You can connect several filter definitions with an OR operator. Enter a question mark (?) as a wildcard for a character and asterisk (*) for any number of characters. DIAdem displays a signal that meets at least one of the filter definitions for the signal name on the **Signal Browser**.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Enable filter | Enables the filter function. |
|  | Filter file | Specifies the name of the text file including the path. |
|  | Browse | Opens the dialog box where you can select a text file with the filter definitions. |
|  | The file contains more than one filter definition per line. | Specifies that the file contains several filter definitions in one line. Spaces separate the individual filter definitions. |

#### Further Settings

[ECU](../ecumcdrv/ecumcdrv_ecu_definition_dialog.htm) | Communication: [CAN](../ecumcdrv/ecumcdrv_ecu_can_dialog.htm) | Communication: [Ethernet](../ecumcdrv/ecumcdrv_ecu_tcpip_dialog.htm) » [DAQ List](../ecumcdrv/ecumcdrv_ecu_daq_dialog.htm) » [Signal List](../ecumcdrv/ecumcdrv_ecu_daq_signals_dialog.htm) | Signal Filter | [User Dialog Box](../ecumcdrv/ecumcdrv_userdialog_dialog.htm) | [Inputs»Data](../ecumcdrv/ecumcdrv_datainputs_dialog.htm) | [Inputs»System](../ecumcdrv/ecumcdrv_systeminput_dialog.htm) | [Outputs»Data](../ecumcdrv/ecumcdrv_dataoutputs_dialog.htm)

<!--NI_TOPIC bundle=diadem path=ecumcdrv/ecumcdrv/ecumcdrv_general.htm language=enus -->
## TOPIC 00768: ECU Measurement and Calibration Toolkit Driver

- bundle_id: `diadem`
- source_path: `ecumcdrv/ecumcdrv/ecumcdrv_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ecumcdrv/ecumcdrv/ecumcdrv_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

ECU Measurement and Calibration Toolkit Driver

ECU Measurement and Calibration Toolkit Driver

The NI ECU Measurement and Calibration Toolkit is used for acquiring data from Engine Control Units (ECUs).

*The CAN Calibration Protocol (CCP)* or *Universal Measurement and Calibration Protocol (XCP)* is used for executing the measurement data acquisition and calibration of Electronic Control Units (ECU). CCP is a protocol for measuring and calibrating ECU data and is based on CAN. XCP is a generalized version of the CCP. You can use the definitions of an A2L file to access the controller data. The A2L files are based on the ASAM-MCD 2MC standard.

You must first install the NI ECU Measurement and Calibration Toolkit to use the ECU Measurement and Calibration Toolkit driver with DIAdem.

<!--NI_TOPIC bundle=diadem path=emailservice/objects/iemailservice_objects_overview.htm language=enus -->
## TOPIC 00769: Objects

- bundle_id: `diadem`
- source_path: `emailservice/objects/iemailservice_objects_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/objects/iemailservice_objects_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Email](../emailservice_overview.htm) > Objects

[[IMAGE alt='image' src='ms-its:diadem.chm::/plus.png']Display all](#nowhere)  [[IMAGE alt='image' src='ms-its:diadem.chm::/minus2.png']Hide all](#nowhere)

Objects

The following topics describe the object-oriented script interface for sending emails. Use the [CreateEMailService](../../comoff/createemailservice.htm) command to create the [EMailService](../objects/emailservice_objects_iemailservice.htm) object which connects to the mail server and provides the mail server with the necessary properties. You create the [EMail](../objects/emailservice_objects_iemail.htm) object with the [CreateEMail](../methods/emailservice_method_createemail_iemailservice.htm) method. Use the [Send](../methods/emailservice_method_send_iemail.htm) method to send emails.

- EMailService
  - EMail

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_accountemailaddress_iemailservice.htm language=enus -->
## TOPIC 00770: Property: AccountEMailAddress for EMailService

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_accountemailaddress_iemailservice.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_accountemailaddress_iemailservice.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: AccountEMailAddress for EMailService

Property: AccountEMailAddress for EMailService

Specifies the email address of the sender for authentication at the mail server. Most public mail servers require a [password](../properties/emailservice_property_accountpassword_iemailservice.htm) and either an email address or a [user name](../properties/emailservice_property_accountusername_iemailservice.htm) as authentication. This email address does not appear as the sender in the created email. Use the [From](../properties/emailservice_property_from_iemail.htm) property to specify the return address of the email.

```text
Object.AccountEMailAddress
```

| Object | EMailServiceObject with this property |
| --- | --- |
| Object.AccountEMailAddress | String with read and write access |

The following example creates an email and sends it with authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
oMyEMailService.AccountEMailAddress = "john.doe@example.com"
oMyEMailService.AccountUserName = "john.doe@example.com"
oMyEMailService.AccountPassword = "secret_password"
oMyEMailService.SMTPTimeout = 30
oMyEMailService.SMTPServerPort = 465
oMyEMailService.SMTPUseSSL = True
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyEMailService.AccountEMailAddress = "john.doe@example.com" 
oMyEMailService.AccountUserName = "john.doe@example.com" 
oMyEMailService.AccountPassword = "secret_password" 
oMyEMailService.SMTPTimeout = 30 
oMyEMailService.SMTPServerPort = 465 
oMyEMailService.SMTPUseSSL = True 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_accountpassword_iemailservice.htm language=enus -->
## TOPIC 00771: Property: AccountPassword for EMailService

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_accountpassword_iemailservice.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_accountpassword_iemailservice.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: AccountPassword for EMailService

Property: AccountPassword for EMailService

Specifies the password of the sender for authentication at the mail server. Most public mail servers require authentication with a password or an [email address](../properties/emailservice_property_accountemailaddress_iemailservice.htm) or a [user name](../properties/emailservice_property_accountusername_iemailservice.htm).

```text
Object.AccountPassword
```

| Object | EMailServiceObject with this property |
| --- | --- |
| Object.AccountPassword | String with read and write access |

The following example creates an email and sends it with authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
oMyEMailService.AccountEMailAddress = "john.doe@example.com"
oMyEMailService.AccountUserName = "john.doe@example.com"
oMyEMailService.AccountPassword = "secret_password"
oMyEMailService.SMTPTimeout = 30
oMyEMailService.SMTPServerPort = 465
oMyEMailService.SMTPUseSSL = True
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyEMailService.AccountEMailAddress = "john.doe@example.com" 
oMyEMailService.AccountUserName = "john.doe@example.com" 
oMyEMailService.AccountPassword = "secret_password" 
oMyEMailService.SMTPTimeout = 30 
oMyEMailService.SMTPServerPort = 465 
oMyEMailService.SMTPUseSSL = True 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_accountusername_iemailservice.htm language=enus -->
## TOPIC 00772: Property: AccountUserName for EMailService

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_accountusername_iemailservice.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_accountusername_iemailservice.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: AccountUserName for EMailService

Property: AccountUserName for EMailService

Specifies the user name of the sender for authentication at the mail server. Most public mail servers require a [password](../properties/emailservice_property_accountpassword_iemailservice.htm) and either an [Email address](../properties/emailservice_property_accountemailaddress_iemailservice.htm) or a user name as authentication.

```text
Object.AccountUserName
```

| Object | EMailServiceObject with this property |
| --- | --- |
| Object.AccountUserName | String with read and write access |

The following example creates an email and sends it with authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
oMyEMailService.AccountEMailAddress = "john.doe@example.com"
oMyEMailService.AccountUserName = "john.doe@example.com"
oMyEMailService.AccountPassword = "secret_password"
oMyEMailService.SMTPTimeout = 30
oMyEMailService.SMTPServerPort = 465
oMyEMailService.SMTPUseSSL = True
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyEMailService.AccountEMailAddress = "john.doe@example.com" 
oMyEMailService.AccountUserName = "john.doe@example.com" 
oMyEMailService.AccountPassword = "secret_password" 
oMyEMailService.SMTPTimeout = 30 
oMyEMailService.SMTPServerPort = 465 
oMyEMailService.SMTPUseSSL = True 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_bcc_iemail.htm language=enus -->
## TOPIC 00773: Property: BCC for EMail

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_bcc_iemail.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_bcc_iemail.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: BCC for EMail

Property: BCC for EMail

Specifies the email addresses to which DIAdem sends an email as hidden copy. Separate several email addresses with a comma. If you want to include the name in the email address, enter the actual email address between < and > characters.

```text
Object.BCC
```

| Object | EMailObject with this property |
| --- | --- |
| Object.BCC | String with read and write access |

The following example creates an email and sends it without authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
oMyMail.CC       = "to.cc@example.com"
oMyMail.BCC      = "blind.cc@example.com"
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.CC       = "to.cc@example.com" 
oMyMail.BCC      = "blind.cc@example.com" 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_cc_iemail.htm language=enus -->
## TOPIC 00774: Property: CC for EMail

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_cc_iemail.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_cc_iemail.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: CC for EMail

Property: CC for EMail

Specifies the email addresses to which DIAdem sends an email copy. Separate several email addresses with a comma. If you want to include the name in the email address, enter the actual email address between < and > characters.

```text
Object.CC
```

| Object | EMailObject with this property |
| --- | --- |
| Object.CC | String with read and write access |

The following example creates an email and sends it without authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
oMyMail.CC       = "to.cc@example.com"
oMyMail.BCC      = "blind.cc@example.com"
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.CC       = "to.cc@example.com" 
oMyMail.BCC      = "blind.cc@example.com" 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_smtpserver_iemailservice.htm language=enus -->
## TOPIC 00775: Property: SMTPServer for EMailService

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_smtpserver_iemailservice.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_smtpserver_iemailservice.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: SMTPServer for EMailService

Property: SMTPServer for EMailService

Specifies the internet address of the mail server over which DIAdem sends an email. You can specify the internet address as name or IP address. Most public mail servers require a [password](../properties/emailservice_property_accountpassword_iemailservice.htm) and either an [Email address](../properties/emailservice_property_accountemailaddress_iemailservice.htm) or a [user name](../properties/emailservice_property_accountusername_iemailservice.htm) as authentication.

```text
Object.SMTPServer
```

| Object | EMailServiceObject with this property |
| --- | --- |
| Object.SMTPServer | String with read and write access |

The following example creates an email and sends it with authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
oMyEMailService.AccountEMailAddress = "john.doe@example.com"
oMyEMailService.AccountUserName = "john.doe@example.com"
oMyEMailService.AccountPassword = "secret_password"
oMyEMailService.SMTPTimeout = 30
oMyEMailService.SMTPServerPort = 465
oMyEMailService.SMTPUseSSL = True
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyEMailService.AccountEMailAddress = "john.doe@example.com" 
oMyEMailService.AccountUserName = "john.doe@example.com" 
oMyEMailService.AccountPassword = "secret_password" 
oMyEMailService.SMTPTimeout = 30 
oMyEMailService.SMTPServerPort = 465 
oMyEMailService.SMTPUseSSL = True 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_smtpserverport_iemailservice.htm language=enus -->
## TOPIC 00776: Property: SMTPServerPort for EMailService

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_smtpserverport_iemailservice.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_smtpserverport_iemailservice.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: SMTPServerPort for EMailService

Property: SMTPServerPort for EMailService

Specifies the mail server port over which DIAdem sends an email. Most public mail servers require a [password](../properties/emailservice_property_accountpassword_iemailservice.htm) and either an [Email address](../properties/emailservice_property_accountemailaddress_iemailservice.htm) or a [user name](../properties/emailservice_property_accountusername_iemailservice.htm) as authentication.

```text
Object.SMTPServerPort
```

| Object | EMailServiceObject with this property |
| --- | --- |
| Object.SMTPServerPort | LongInteger with read and write access |

The following example creates an email and sends it with authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
oMyEMailService.AccountEMailAddress = "john.doe@example.com"
oMyEMailService.AccountUserName = "john.doe@example.com"
oMyEMailService.AccountPassword = "secret_password"
oMyEMailService.SMTPTimeout = 30
oMyEMailService.SMTPServerPort = 465
oMyEMailService.SMTPUseSSL = True
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyEMailService.AccountEMailAddress = "john.doe@example.com" 
oMyEMailService.AccountUserName = "john.doe@example.com" 
oMyEMailService.AccountPassword = "secret_password" 
oMyEMailService.SMTPTimeout = 30 
oMyEMailService.SMTPServerPort = 465 
oMyEMailService.SMTPUseSSL = True 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_smtptimeout_iemailservice.htm language=enus -->
## TOPIC 00777: Property: SMTPTimeout for EMailService

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_smtptimeout_iemailservice.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_smtptimeout_iemailservice.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: SMTPTimeout for EMailService

Property: SMTPTimeout for EMailService

Specifies the time in seconds that DIAdem needs to connect to the mail server.

```text
Object.SMTPTimeout
```

| Object | EMailServiceObject with this property |
| --- | --- |
| Object.SMTPTimeout | LongInteger with read and write access |

The following example creates an email and sends it with authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
oMyEMailService.AccountEMailAddress = "john.doe@example.com"
oMyEMailService.AccountUserName = "john.doe@example.com"
oMyEMailService.AccountPassword = "secret_password"
oMyEMailService.SMTPTimeout = 30
oMyEMailService.SMTPServerPort = 465
oMyEMailService.SMTPUseSSL = True
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyEMailService.AccountEMailAddress = "john.doe@example.com" 
oMyEMailService.AccountUserName = "john.doe@example.com" 
oMyEMailService.AccountPassword = "secret_password" 
oMyEMailService.SMTPTimeout = 30 
oMyEMailService.SMTPServerPort = 465 
oMyEMailService.SMTPUseSSL = True 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_smtpusessl_iemailservice.htm language=enus -->
## TOPIC 00778: Property: SMTPUseSSL for EMailService

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_smtpusessl_iemailservice.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_smtpusessl_iemailservice.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: SMTPUseSSL for EMailService

Property: SMTPUseSSL for EMailService

Specifies whether the mail server sends an email that is SSL encrypted.

```text
Object.SMTPUseSSL
```

| Object | EMailServiceObject with this property |
| --- | --- |
| Object.SMTPUseSSL | Boolean with read and write access |

The following example creates an email and sends it with authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
oMyEMailService.AccountEMailAddress = "john.doe@example.com"
oMyEMailService.AccountUserName = "john.doe@example.com"
oMyEMailService.AccountPassword = "secret_password"
oMyEMailService.SMTPTimeout = 30
oMyEMailService.SMTPServerPort = 465
oMyEMailService.SMTPUseSSL = True
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text")
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyEMailService.AccountEMailAddress = "john.doe@example.com" 
oMyEMailService.AccountUserName = "john.doe@example.com" 
oMyEMailService.AccountPassword = "secret_password" 
oMyEMailService.SMTPTimeout = 30 
oMyEMailService.SMTPServerPort = 465 
oMyEMailService.SMTPUseSSL = True 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "This is some text") 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_subject_iemail.htm language=enus -->
## TOPIC 00779: Property: Subject for EMail

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_subject_iemail.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_subject_iemail.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Subject for EMail

Property: Subject for EMail

Specifies the subject of an email.

```text
Object.Subject
```

| Object | EMailObject with this property |
| --- | --- |
| Object.Subject | String with read and write access |

The following example creates an email and sends it without authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "", "This is some text")
oMyMail.Subject = "This is the subject"
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "", "This is some text") 
oMyMail.Subject = "This is the subject" 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_textbody_iemail.htm language=enus -->
## TOPIC 00780: Property: TextBody for EMail

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_textbody_iemail.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_textbody_iemail.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: TextBody for EMail

Property: TextBody for EMail

Specifies the text of an email. The text can contain text but not formats.

```text
Object.TextBody
```

| Object | EMailObject with this property |
| --- | --- |
| Object.TextBody | String with read and write access |

The following example creates an email and sends it without authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "")
oMyMail.TextBody = "Hello World" & VBCrLf & "This is my first email!"
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "ToUser <to.example@example.com>", "This is the subject", "") 
oMyMail.TextBody = "Hello World" + "\r\n" + "This is my first email!" 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=emailservice/properties/emailservice_property_to_iemail.htm language=enus -->
## TOPIC 00781: Property: To for EMail

- bundle_id: `diadem`
- source_path: `emailservice/properties/emailservice_property_to_iemail.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/emailservice/properties/emailservice_property_to_iemail.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: To for EMail

Property: To for EMail

Specifies the email addresses to which DIAdem sends the email.

```text
Object.To
```

| Object | EMailObject with this property |
| --- | --- |
| Object.To | String with read and write access |

The following example creates an email and sends it without authentication.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyEMailService, oMyMail
Set oMyEMailService = CreateEMailService("server.example.com")
Set oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "", "This is the subject", "This is some text")
oMyMail.To       = "to@example.com"
oMyMail.BCC      = "blind.cc@example.com"
Call oMyMail.Send
```

[Copy script](javascript:void(0);)

```text
oMyEMailService = dd.CreateEMailService("server.example.com") 
oMyMail = oMyEMailService.CreateEMail("FromUser <from.example@example.com>", "", "This is the subject", "This is some text") 
oMyMail.To       = "to@example.com" 
oMyMail.BCC      = "blind.cc@example.com" 
oMyMail.Send 
```

#### See Also

[Objects Overview](../objects/iemailservice_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/2d_axissynchronization.htm language=enus -->
## TOPIC 00782: 2D Axis Synchronization

- bundle_id: `diadem`
- source_path: `exploff/examples/2d_axissynchronization.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/2d_axissynchronization.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../examples/examples_2daxissystems_overview.htm) | [Version 2020](../examples/examples_new2020_overview.htm)) > 2D Axis Synchronization

| 2D Axis Synchronization |
| --- |

This example shows several 2D axis systems whose x-axes are assigned to a common synchronization group. The y-axes are assigned to two synchronization groups. DIAdem automatically adjusts the scaling of all axes of a synchronization group when you modify the scaling of one of the axes. You can also create synchronization groups and assign axes on the [X-Scaling](../../dlgpresent/graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm) and [Y-Scaling](../../dlgpresent/graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm) tabs of the Axis Parameters tab of the Curve and Axis Definition dialog box for 2D axis systems. Use the [2D-Axis Synchronization](../../dlgpresent/graph_dlg_menu/reportaxessynchronizing_dialog.htm) dialog box to synchronize x- and y-axes of 2D axis systems and manage synchronization groups.

Start example

#### Click a filename to load this file into DIAdem

| 2D_AxisSynchronization.tdr | Layout file |
| --- | --- |
| Example_data.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/2d_tabchanneltransformation.htm language=enus -->
## TOPIC 00783: 2D Table with Channel Transformation

- bundle_id: `diadem`
- source_path: `exploff/examples/2d_tabchanneltransformation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/2d_tabchanneltransformation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Scripts](../examples/examples_scripts_overview.htm) | [Tables](../examples/examples_tables_overview.htm) | [Version 2020](../examples/examples_new2020_overview.htm)) > 2D Table with Channel Transformation

| 2D Table with Channel Transformation |
| --- |

This example shows a 2D table that uses the [channel transformation](../../dlgpresent/graph_dlg_2dtable_tab/d2table_channeltransform_dialog.htm) to convert a temperature channel into different physical units. Use the channel transformation function to edit the displayed channels while DIAdem is plotting. DIAdem does not modify the original data.

Start example

#### Click a filename to load this file into DIAdem.

| 2D_TabChannelTransformation_Main.vbs | Script file |
| --- | --- |
| 2D_TabChannelTransformation_UCMD.vbs | Script file with user commands |
| 2D_TabChannelTransformation.tdr | Layout file |
| Example_data.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/calculationset_example.htm language=enus -->
## TOPIC 00784: Calculating the Sound Pressure Level with Calculation Templates

- bundle_id: `diadem`
- source_path: `exploff/examples/calculationset_example.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/calculationset_example.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Application Examples](../examples/examples_userexamples_overview.htm) | [Mathematics](../examples/examples_maths_overview.htm) | [Scripts](../examples/examples_scripts_overview.htm) | [Version 11.1](../examples/examples_new111_overview.htm)) > Calculating the Sound Pressure Level with Calculation Templates

| Calculating the Sound Pressure Level with Calculation Templates |
| --- |

This example shows the evaluation of various noise data. DIAdem analyzes the sound data through calculations which you can create and edit in the [Calculation Manager](../../dlgmaths/calc_formula_dlg/dlgcm_calculationset_dialog.htm).

The example uses simple formulas, basic mathematical functions, and calculation scripts to analyze the data.

Start example

#### Click a filename to load this file into DIAdem

| CalculationSet_Example.vbs | Script file |
| --- | --- |
| CalculationSet_Example.tdr | Layout file |
| CalculationSet_Example.tca | Calculation template |
| Example_data.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites current data, layouts, and calculations. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/datafinderusedinsud.htm language=enus -->
## TOPIC 00785: Search and Evaluation Functions in User Dialog Boxes

- bundle_id: `diadem`
- source_path: `exploff/examples/datafinderusedinsud.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/datafinderusedinsud.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mining and Loading Data](../examples/examples_loadsearchdata_overview.htm) | [User Dialog Boxes](../examples/examples_userdialogs_overview.htm) | [Version 11.0](../examples/examples_new110_overview.htm)) > Search and Evaluation Functions in User Dialog Boxes

| Search and Evaluation Functions in User Dialog Boxes |
| --- |

This example shows how to use the DIAdem search functions in user-defined dialog boxes.

In the example you can search for various properties in a user dialog box. Then you can select one or more files and execute evaluations.

|  | Note The example uses information from optimized custom properties, so you must optimize the following custom properties of the group before you can start the example: Test_Name, Test_Operator, Test_Procedure, UUT, and Test_Status.To optimize the custom properties, open DIAdem NAVIGATOR and select Settings»My DataFinder»Optimize Custom Properties. Switch to the Group tab and optimize the first five custom properties. |
| --- | --- |

Start example

#### Click a Filename to Load this File into DIAdem

| DataFinderUsedInSUD.vbs | Script file |
| --- | --- |
| DataFinderUsedInSUD.sud | Dialog box file |
| DataFinderUsedInSUD.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/dataplugintimeout.htm language=enus -->
## TOPIC 00786: Checking DataPlugins for Timeout

- bundle_id: `diadem`
- source_path: `exploff/examples/dataplugintimeout.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/dataplugintimeout.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mining and Loading Data](../examples/examples_loadsearchdata_overview.htm) | [Version 11.0](../examples/examples_new110_overview.htm)) > Checking DataPlugins for Timeout

| Checking DataPlugins for Timeout |
| --- |

This example shows in a dialog box a statistic of the files indexed per DataPlugin. The example also shows whether a DataPlugin terminated the indexing process because the time was exceeded. If you double-click the cell, the example returns a detailed list of the files. The example uses the [Navigator Object.](../../scriptnavi/objects/navigator_objects_inavigator.htm)

Start example

#### Click a Filename to Load this File into DIAdem

| DataPluginTimeout.vbs | Script file |
| --- | --- |
| DataPluginTimeout.sud | Dialog box file |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/example_application.htm language=enus -->
## TOPIC 00787: Customized User Interface

- bundle_id: `diadem`
- source_path: `exploff/examples/example_application.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/example_application.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mining and Loading Data](../examples/examples_loadsearchdata_overview.htm) | [Scripts](../examples/examples_scripts_overview.htm) | [User Dialog Boxes](../examples/examples_userdialogs_overview.htm) | [Version 11.1](../examples/examples_new111_overview.htm)) > Customized User Interface

| Customized User Interface |
| --- |

This example shows how you can customize the DIAdem interface completely to your needs.

The example shows a dialog box where you can select various predefined layouts and matching data sets, which you can display as a report. You can display the report as a PDF file or edit the file interactively. You only can use a limited number of functions for editing the report, not the complete DIAdem REPORT functionality. Other DIAdem panels are also hidden.

The example uses user dialog boxes and the [BarManager object](../../tobarmanagerint/objects/tobarmanagerint_objects_overview.htm) to customize the DIAdem interface. The example uses the [CreateQuery](../../scriptnavi/methods/navigator_method_createquery_itdmdatafinder.htm) method to search for data sets.

Start example

#### Click a filename to load this file into DIAdem

| Application.vbs | Script file |
| --- | --- |
| Application_Library.vbs | Script file |
| Application.sud | Dialog box file |
| Application_case_1.tdr | Layout file |
| Application_case_2.tdr | Layout file |
| Application_case_3.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/example_brake_test.htm language=enus -->
## TOPIC 00788: Brake Tests for Trucks

- bundle_id: `diadem`
- source_path: `exploff/examples/example_brake_test.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/example_brake_test.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Application Examples](../examples/examples_userexamples_overview.htm) | [Extending Functionalities with Scripts](../examples/examples_extensions.htm) | [Mathematics](../examples/examples_maths_overview.htm) | [Mining and Loading Data](../examples/examples_loadsearchdata_overview.htm) | [Scripts](../examples/examples_scripts_overview.htm) | [Version 11.1](../examples/examples_new111_overview.htm)) > Brake Tests for Trucks

| Brake Tests for Trucks |
| --- |

This example shows the evaluation of a brake test for trucks. DIAdem evaluates the speed recorded with GPS and the measured brake pressure. You can select different speed ranges for which DIAdem determines the characteristic data. The example uses the DataFinder to find the data to be evaluated. The layout uses a master layout. DIAdem uses the Report.AppendLayout command to add additional worksheets to the report depending on the number of data sets.

The example uses various basic mathematics functions and curve fitting functions to analyze the data.

Start example

#### Click a Filename to Load this File into DIAdem

| Brake_test.vbs | Script file |
| --- | --- |
| Brake_Test.sud | Dialog box file |
| Brake_Test.tdr | Layout file |
| Brake_Test.tdrm | Master layout file |
| Brake_Test_Append.tdr | Layout file |
| Brake_Test_001.tdm | Data file |
| Brake_Test_002.tdm | Data file |
| Brake_Test_003.tdm | Data file |
| Brake_Test_004.tdm | Data file |
| Brake_Test_005.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/example_example_view.htm language=enus -->
## TOPIC 00789: Various Display Modes in DIAdem VIEW

- bundle_id: `diadem`
- source_path: `exploff/examples/example_example_view.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/example_example_view.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Version 11.1](../examples/examples_new111_overview.htm) | [Viewing and Editing Data](../examples/examples_viewworkdata_overview.htm)) > Various Display Modes in DIAdem VIEW

| Various Display Modes in DIAdem VIEW |
| --- |

This example shows various display modes in DIAdem VIEW. The worksheets show various 2D curve displays, a table, a video and a contour display. The video is synchronized with data channels. Click **Play** to run the video. The contour display shows 3D data and horizontal and vertical cross sections of the data. If you move the cursor in the contour display, you move the cross sections vertical to the xy-plane. In the horizontal and vertical cross sections, you also can move the cursor in the z-direction.

The example automatically ends the video. Click the **Pause** symbol to interrupt the video.

Start example

#### Click a filename to load this file into DIAdem.

| Example_data.tdm | Data file |
| --- | --- |
| View_Example.tdv | Layout file |
| DemCar.emf | Graphics file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/example_ole.htm language=enus -->
## TOPIC 00790: Controlling DIAdem as an ActiveX Object

- bundle_id: `diadem`
- source_path: `exploff/examples/example_ole.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/example_ole.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../examples/examples_generatingscripts_overview.htm) > [Using Interfaces](../examples/examples_usinginterfaces_overview.htm) > Controlling DIAdem as an ActiveX Object

| Controlling DIAdem as an ActiveX Object |
| --- |

This example shows how to use DIAdem as an ActiveX object and how to remote control it from a different application.

[javascript:loaddiademdataset();](javascript:loaddiademdataset();) [Load sample data set](javascript:loaddiademdataset();)

Select a layout:

Expl_Report_2DAxis.TDR
 Expl_Report_2DBars.TDR
 Expl_Report_2DGrid.TDR
 Expl_Report_3DAxis.TDR

[javascript:loaddiademlayout();](javascript:loaddiademlayout();) [Open selected layout](javascript:loaddiademlayout();)

|  | Note Depending on which safety settings you have, the operating system warns you that an ActiveX element may be unsafe. You must register the control to run the example. This warning appears if you use the CreateObject command to embed an automation object in an HTML page. |
| --- | --- |
|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |

|  | Note The following script is embedded in the HTML code for this help page. The script registers DIAdem as an ActiveX object and uses the DIAdem command interface to send commands. All other embedded scripts are for evaluating the HTML forms.Copy script Dim oMyDIAdem, ProgramDrv Set oMyDIAdem = new DIAdemAutomation Call oMyDIAdem.LoadDiademDataSet(ProgramDrv & "examples\\data\\report_expl.tdm", True) Call oMyDIAdem.LoadDiademLayout(ProgramDrv & "examples\\documents\\Expl_Report_2DAxis.TDR") Set oMyDIAdem = Nothing Class DIAdemAutomation Dim oDIAdem, DIAdemApp Private Sub Class_Initialize() Set oDIAdem = Nothing Call ConnectToDIAdem Call oDIAdem.VariantVarget("Application",DIAdemApp) Call oDIAdem.VariantVarget("ProgramDrv",ProgramDrv) End Sub '================================================================ Private Sub Class_Terminate() Set oDIAdem = Nothing End Sub '================================================================ Function DIAdem_Exec(DIAdemCommand) DIAdem_exec = False If ConnectToDIAdem Then If oDIAdem.CmdExecuteSync(DIAdemCommand) = 1 Then DIAdem_exec = True End If End Function '================================================================ Sub LoadDiademLayout(LayOut) Call DIAdemApp.Report.LoadLayout(LayOut) Call DIAdem_exec("WndOpen(""Report"")") Call DIAdemApp.Report.Refresh End Sub '================================================================ Sub ExportPDF(PDFName) Call DIAdemApp.Report.Sheets.ExportToPDF(PDFName) End Sub '================================================================ Function LoadDiademDataSet(DataSet, clear) If clear Then Call DIAdemApp.Data.Root.Clear End if Dim MyCommand : MyCommand = "DataFileLoad(""" & DataSet & """)" LoadDiademDataSet = DIAdem_exec(MyCommand) End Function '================================================================ Private Function ConnectToDIAdem Dim nValueT, iWait If NOT oDIAdem Is Nothing Then ConnectToDIAdem = True Exit Function End If ConnectToDIAdem = False On Error Resume Next Set oDIAdem = CreateObject("DIAdem.TOCommand") If Err.Number > 0 then Set oDIAdem = Nothing Err.Clear Else iWait = 0 Do iWait = iWait + 1 If iWait >=1000 Then Exit Function End If Loop Until Not oDIAdem.bInterfaceLocked ' Suppress all messages oDIAdem.bNoMsgDisplay = true oDIAdem.bNoInfoDisplay = true oDIAdem.bNoErrorDisplay = true oDIAdem.bNoWarningDisplay = true oDIAdem.bNoNoDialogDisplay = true ConnectToDIAdem = True End If End Function End Class Copy scriptoMyDIAdem = new DIAdemAutomation oMyDIAdem.LoadDiademDataSet(dd.ProgramDrv + "examples\\\\data\\\\report_expl.tdm", True) oMyDIAdem.LoadDiademLayout(dd.ProgramDrv + "examples\\\\documents\\\\Expl_Report_2DAxis.TDR") oMyDIAdem = None class DIAdemAutomation: def _Class_Initialize(self): oDIAdem = None ConnectToDIAdem oDIAdem.VariantVarget("Application",DIAdemApp) oDIAdem.VariantVarget("ProgramDrv",dd.ProgramDrv) #================================================================ def _Class_Terminate(self): oDIAdem = None #================================================================ def DIAdem_Exec(self, DIAdemCommand): DIAdem_exec = False if ConnectToDIAdem : if oDIAdem.CmdExecuteSync(DIAdemCommand) == 1 : DIAdem_exec = True return DIAdem_Exec #================================================================ def LoadDiademLayout(self, LayOut): DIAdemApp.Report.LoadLayout(LayOut) DIAdem_exec("WndOpen(""Report"")") DIAdemApp.Report.Refresh() #================================================================ def ExportPDF(self, PDFName): DIAdemApp.Report.Sheets.ExportToPDF(PDFName) #================================================================ def LoadDiademDataSet(self, DataSet, clear): if clear : DIAdemApp.Data.Root.Clear() MyCommand = "DataFileLoad(""" + DataSet + """)" LoadDiademData= DIAdem_exec(MyCommand) return LoadDiademDataSet #================================================================ def _ConnectToDIAdem(self): if not oDIAdem is None : ConnectToDIAdem = True Exit Function ConnectToDIAdem = False On Error Resume Next oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") if Err.Number > 0 : oDIAdem = None Err.Clear() else: iWait = 0 while True: iWait = iWait + 1 if iWait >==1000 : Exit Function if not oDIAdem.bInterfaceLocked: break # Suppress all messages oDIAdem.bNoMsgDisplay = True oDIAdem.bNoInfoDisplay = True oDIAdem.bNoErrorDisplay = True oDIAdem.bNoWarningDisplay = True oDIAdem.bNoNoDialogDisplay = True ConnectToDIAdem = True return ConnectToDIAdem |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/example_pycsv_dataplugin.htm language=enus -->
## TOPIC 00791: Creating a Python DataPlugin

- bundle_id: `diadem`
- source_path: `exploff/examples/example_pycsv_dataplugin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/example_pycsv_dataplugin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mining and Loading Data](../examples/examples_loadsearchdata_overview.htm) | [Version 2020](../examples/examples_new2020_overview.htm)) > Creating a Python DataPlugin

| Creating a Python DataPlugin |
| --- |

The following example shows how you can load a simple CSV file with a Python DataPlugin. First register the [DataPlugin](../../procshell/procshell/procshell_register_dataplugins.htm) in DIAdem and load Example.csv from the Examples folder. Open the Python file to see the basic structures of the Python DataPlugin:

- def read_store This is the main function of the Python DataPlugin. This function converts the input file into a Python dictionary and adds the metadata as normal dictionary properties.
- def read_channel_length This method returns the channel length.
- def read_channel_values This method returns the mass data as one value field.

#### Click a filename to load this file into DIAdem.

| PyCSV_DataPlugin.py | Python script file for the DataPlugin |
| --- | --- |
| PyCSV_DataPlugin.uri | DataPlugin for CSV files. You can also register the DataPlugin in DIAdem by double-clicking the URI file in Explorer. |
| Example.csv | ASCII file. After registering the DataPlugin, you can load the file with the DataPlugin. |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

|  | Note To deregister the DataPlugin, use DataPlugin Settings or click here. |
| --- | --- |

#### Procedures

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_2daxissystems_overview.htm language=enus -->
## TOPIC 00792: 2D Axis Systems

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_2daxissystems_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_2daxissystems_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > 2D Axis Systems

| 2D Axis Systems |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show how to use 2D axis systems in a report. The examples show you how to display data as lines, bars, or spikes, for example. You will learn how to define several y-axes, execute logarithmic scaling of axes, and create legends.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_3daxissystems_overview.htm language=enus -->
## TOPIC 00793: 3D Axis Systems

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_3daxissystems_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_3daxissystems_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > 3D Axis Systems

| 3D Axis Systems |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show how to use 3D axis systems in a report. You will learn, for example, how to display 3D data as surfaces, matrices, bars, isolines, curves, or characteristic diagrams.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_extensions.htm language=enus -->
## TOPIC 00794: Extending Functionalities with Scripts

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_extensions.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_extensions.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Examples](../../readme/readme/examples_mainoverview.htm) > Extending Functionalities with Scripts

| Extending Functionalities with Scripts |
| --- |

Use the following examples to add useful functions to DIAdem with scripts. You can start these examples directly from the help. You can use the examples to copy the files to a user folder and to use the files for your own extensions.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new100_overview.htm language=enus -->
## TOPIC 00795: New Examples for Version 10.0

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new100_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new100_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > [Examples before Version 2010](../examples/examples_old_overview.htm) > New Examples for Version 10.0

| New Examples for Version 10.0 |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem Version 10.0.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new101_overview.htm language=enus -->
## TOPIC 00796: New Examples for Version 10.1

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new101_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new101_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > [Examples before Version 2010](../examples/examples_old_overview.htm) > New Examples for Version 10.1

| New Examples for Version 10.1 |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem Version 10.1.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new2010_overview.htm language=enus -->
## TOPIC 00797: New Examples for Version 2010

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new2010_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new2010_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > New Examples for Version 2010

| New Examples for Version 2010 |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem Version 2010.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new2011_overview.htm language=enus -->
## TOPIC 00798: New Examples for Version 2011

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new2011_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new2011_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > New Examples for Version 2011

| New Examples for Version 2011 |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem Version 2011.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new2012_overview.htm language=enus -->
## TOPIC 00799: New Examples for Version 2012

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new2012_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new2012_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > New Examples for Version 2012

| New Examples for Version 2012 |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem Version 2012.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new2014_overview.htm language=enus -->
## TOPIC 00800: New Examples for Version 2014

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new2014_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new2014_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > New Examples for Version 2014

| New Examples for Version 2014 |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem Version 2014.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new2020_overview.htm language=enus -->
## TOPIC 00801: New Examples for Version 2020

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new2020_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new2020_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > New Examples for Version 2020

| New Examples for Version 2020 |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem Version 2020.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_new_overview.htm language=enus -->
## TOPIC 00802: New Examples

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_new_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_new_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

New Examples

| New Examples |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe new features in DIAdem.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_piechart_overview.htm language=enus -->
## TOPIC 00803: Pie Charts

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_piechart_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_piechart_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > Pie Charts

| Pie Charts |
| --- |

The subordinate topics from the tree on the contents tab of the Help show how to use pie charts in a report.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_polaraxissystems_overview.htm language=enus -->
## TOPIC 00804: Polar Axis Systems

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_polaraxissystems_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_polaraxissystems_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > Polar Axis Systems

| Polar Axis Systems |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show how to use polar axis systems in a report. You will learn, for example, how to display measurement data as lines and symbols and in differential form, and how to create polar axis systems with different aperture angles.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_scripts_overview.htm language=enus -->
## TOPIC 00805: Scripts

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_scripts_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_scripts_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../examples/examples_generatingscripts_overview.htm) > Scripts

| Scripts |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show how to use scripts to automate DIAdem. You will learn, for example, how to evaluate a series of files in a script, how to handle errors or work with dynamic enumeration lists.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_spider_overview.htm language=enus -->
## TOPIC 00806: Spider Axis Systems

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_spider_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_spider_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > Spider Axis Systems

| Spider Axis Systems |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show how to use spider axis systems in a report.

<!--NI_TOPIC bundle=diadem path=exploff/examples/examples_tables_overview.htm language=enus -->
## TOPIC 00807: Tables

- bundle_id: `diadem`
- source_path: `exploff/examples/examples_tables_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/examples_tables_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > Tables

| Tables |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe how to use various 2D tables and 3D tables in a report.

<!--NI_TOPIC bundle=diadem path=exploff/examples/exp_interfaces_ab2.htm language=enus -->
## TOPIC 00808: DIAdem Client Operation with Excel as Server

- bundle_id: `diadem`
- source_path: `exploff/examples/exp_interfaces_ab2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/exp_interfaces_ab2.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../examples/examples_generatingscripts_overview.htm) > [Using Interfaces](../examples/examples_usinginterfaces_overview.htm) > DIAdem Client Operation with Excel as Server

| DIAdem Client Operation with Excel as Server |
| --- |

This example shows how DIAdem copies text and data to Microsoft Excel, over the OLE interface.

Start example

#### Click a Filename to Load this File into DIAdem

| Expl_OLE.vbs | Script |
| --- | --- |
| DIAdem.xls | Excel file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

|  | Note To receive CodeCompletion for Excel in the script editor select Microsoft Excel x.x Objects Library in the Registered Type Libraries dialog box. The x.x value depends on your installed Excel version. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/exp_interfaces_ab4.htm language=enus -->
## TOPIC 00809: Communicating with MATLAB

- bundle_id: `diadem`
- source_path: `exploff/examples/exp_interfaces_ab4.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/exp_interfaces_ab4.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Using Interfaces](../examples/examples_usinginterfaces_overview.htm) | [Version 10.0](../examples/examples_new100_overview.htm)) > Communicating with MATLAB

| Communicating with MATLAB |
| --- |

This example shows how DIAdem works with a MATLAB over the OLE interface. First DIAdem generates data, then transfers this data to MATLAB, and finally starts a Mscript in MATLAB. This Mscript calculates a FFT for the transferred values. MATLAB transfers the result data back to DIAdem. DIAdem also calculates a FFT and displays the results of both calculations DIAdem VIEW.

Start example

#### Click a Filename to Load this File into DIAdem

| MatLabTest1.vbs | Script file |
| --- | --- |
| MatLab_FFTTest1.m | Mscript for MATLAB |

|  | Note For this example MATLAB must be installed on your computer. |
| --- | --- |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

|  | Note To receive CodeCompletion for ADO in the script editor, select the MATLAB library in the Registered Type Libraries dialog box. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_ac-dccoupling.htm language=enus -->
## TOPIC 00810: AC/DC Coupling

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_ac-dccoupling.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_ac-dccoupling.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 2014](../examples/examples_new2014_overview.htm)) > AC/DC Coupling

| AC/DC Coupling |
| --- |

This example shows how to remove the DC part (bias) from a signal. The example uses the [AC/DC Coupling](../../dlgmaths/calc_signal_dlg/dlgchnacdccoupling_dialog.htm) function and displays the results in a report.

Start example

#### Click a filename to load this file into DIAdem.

| AC-DC-Coupling.vbs | Script file |
| --- | --- |
| AC-DC-Coupling.py | Python script file |
| FFT_Expl_1.tdm | Data file |
| AC-DC-Coupling.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_analysis_spc.htm language=enus -->
## TOPIC 00811: Calculating Process Capability

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_analysis_spc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_analysis_spc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 10.2](../examples/examples_new102_overview.htm)) > Calculating Process Capability

| Calculating Process Capability |
| --- |

This example executes the calculations for [process capability](../../dlgmaths/calc_statistics_dlg/dlgspcprocesscap_dialog.htm). In DIAdem REPORT two worksheets display the results of the statistical evaluation of the preliminary stage and the final stage of a component. The limits are identified using curve end labels.

Start example

#### Click a filename to load this file into DIAdem.

| Analysis_SPC.vbs | Script file |
| --- | --- |
| Analysis_SPC.py | Python script file |
| Analysis_SPC.tdm | Data file |
| Analysis_SPC.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_analyzehysteresis.htm language=enus -->
## TOPIC 00812: Hysteresis Analysis

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_analyzehysteresis.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_analyzehysteresis.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Application Examples](../examples/examples_userexamples_overview.htm) | [Mathematics](../examples/examples_maths_overview.htm) | [User-Defined Evaluations in DIAdem ANALYSIS](../examples/expl_userdefinedfct.htm) | [Version 2010](../examples/examples_new2010_overview.htm)) > Hysteresis Analysis

| Hysteresis Analysis |
| --- |

This example shows you how to analyze a hysteresis. The function filters the signal and executes several corrections. Find details on the functionality further [down](#functionmode).

The report displays the measured and filtered data in x-direction and in y-direction, the overlapping, and the difference between the up and down curve.

Start example

#### Click a Filename to Load this File into DIAdem

| AnalyzeHysteresis_Automated.vbs | Script file |
| --- | --- |
| AnalyzeHysteresis.tdr | Layout file |
| AnalyzeHysteresis.suc | Dialog box file encrypted |
| AnalyzeHysteresis_Libr.vbc | Script file encrypted |
| AnalyzeHysteresis.ico | Symbol file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Results

The hysteresis analysis determines the following results:

- Difference between the up and down curve
- Hysteresis integral
- Overlapping surfaces between the up and down curve

[IMAGE alt='image' src='../image/hysterese05.gif']

#### Functionality

The hysteresis analysis supports the following schematically displayed curve forms.

[IMAGE alt='image' src='../image/hys_form.gif']

##### Filtering

You can filter the measured x-channel and y-channel with Bessel or a Butterworth lowpass filter to dampen the noise in the data. You can select the filter order and the limit frequency for the filtering.

[IMAGE alt='image' src='../image/hysterese01.gif']

##### Correction

To eliminate errors that occur during the transient oscillation, the analysis function corrects the start values on both sides of the curve. To do so, the DIAdem calculates the mean value for the specified number of values and compares this mean value with a value outside of the mean range. If the value coincides with the mean value within a specified tolerance value, DIAdem deletes all values before this value. The correction impacts all channels involved in the evaluation.

[IMAGE alt='image' src='../image/hysterese02.gif']

##### Start point and end point

To recognize the start and end point of the hysteresis, the analysis function calculates the difference between neighboring points if required. DIAdem saves this difference in an auxiliary channel and smooths the auxiliary channel. The value of the auxiliary channel which is the first to contain a value significantly different from zero, indicates the start point for the valid measurement values. You can calculate the correction for the x-channel or for the x and y-channel. The correction impacts all channels involved.

[IMAGE alt='image' src='../image/hysterese03.gif']

##### Reversal point

The analysis function specifies the reversal point of the hysteresis for the x-channel. The analysis function uses the middle of the plateau as the reversal point for hystereses that contain a plateau. If the hysteresis does not have a plateau, the analysis function uses the peak value as the reversal point. The analysis function splits up the x-channel and the y-channel at the reversal point. The analysis function maps the result data on a joint x-channel and if required, smooths the data.

[IMAGE alt='image' src='../image/hysterese04.gif']

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_analyzewaveformchannels.htm language=enus -->
## TOPIC 00813: Calculating with Waveform Channels

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_analyzewaveformchannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_analyzewaveformchannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Scripts](../examples/examples_scripts_overview.htm) | [Version 10.1](../examples/examples_new101_overview.htm)) > Calculating with Waveform Channels

| Calculating with Waveform Channels |
| --- |

This examples show how to use the property [Value for Property <Data>](../../inavidata/properties/diacmpnt_property_value_idiademproperty.htm) to specify the minimum values and the maximum values of waveform channels. You use the [PNo](../../functions/functions/pno.htm) function to specify the line number of the extreme values and the [ChDWfX](../../varoff/chdwfx.htm) variable to specify the x-value. DIAdem displays the result in a graphic.

Start example

#### Click a filename to load this file into DIAdem.

| AnalyzeWaveformChannels.vbs | Script file |
| --- | --- |
| AnalyzeWaveformChannels.py | Python script file |
| AnalyzeWaveformChannels.tdr | Layout file |
| AnalyzeWaveformChannels.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_datafilter_auto.htm language=enus -->
## TOPIC 00814: Filtering Data without a Dialog Box

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_datafilter_auto.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_datafilter_auto.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > [Version 2014](../examples/examples_new2014_overview.htm) > Filtering Data without a Dialog Box

| Filtering Data without a Dialog Box |
| --- |

This example shows you how to filter data with certain criteria. DIAdem specifies the filter criteria in a script and displays the results in a report.

The example uses the [ChnEventDetectionWindow](../../comoff/chneventdetectionwindow.htm) command to filter numeric channels.

Start example

#### Click a Filename to Load this File into DIAdem

| DataFilter_Auto.vbs | Script file |
| --- | --- |
| DataFilter_Libr.vbs | Script file |
| DataFilter.tdm | Data file |
| DataFilter.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_domesticengineering.htm language=enus -->
## TOPIC 00815: Optimized Heating Control

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_domesticengineering.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_domesticengineering.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Application Examples](../examples/examples_userexamples_overview.htm) | [Version 2011](../examples/examples_new2011_overview.htm)) > Optimized Heating Control

| Optimized Heating Control |
| --- |

This example demonstrates continuous temperature measurement with the aim of lowering operating costs. It shows measurement data before and after optimization.

Before heating optimization, the heat in the house generated by the sun is not taken into consideration. The burner is running even though the radiators are closed. But as solar radiation is also heating the house, heat output can be reduced. DIAdem calculates the solar radiation by measuring the different outside temperatures on the south side and on the north side of the house.

In the case of solar radiation, the radiators remain closed and the burner is running unnecessarily. The difference between the boiler outflow and the heating return flow in this case is relatively big. If the heating is well-adjusted, this difference, in contrast, is only a few Kelvin. After heating optimization, the apartments have an even temperature and the room temperatures show minimal variations.

Start example

#### Click a Filename to Load this File into DIAdem

| Domestic Engineering.tdm | Data file |
| --- | --- |
| Domestic Engineering.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_doublevaluesdelete.htm language=enus -->
## TOPIC 00816: Removing Repeatedly Occurring Values in a Channel

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_doublevaluesdelete.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_doublevaluesdelete.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 2017](../examples/examples_new2017_overview.htm)) > Removing Repeatedly Occurring Values in a Channel

| Removing Repeatedly Occurring Values in a Channel |
| --- |

This example shows how to remove values that occur repeatedly in a channel. The example deletes identical data, or data which only differs within an absolute or relative tolerance. The example shows the raw data and the processed data in a report. The example uses the function [ChnDeleteDuplicateValues](../../comoff/chndeleteduplicatevalues.htm), in order to remove the values that occur repeatedly in a channel.

Start example

#### Click a filename to load this file into DIAdem.

| MultipleValuesDelete.vbs | Script file |
| --- | --- |
| MultipleValuesDelete.py | Python script file |
| MultipleValuesDelete.tdm | Data file |
| MultipleValuesDelete.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_enclosedarea.htm language=enus -->
## TOPIC 00817: Area Calculation between Curves

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_enclosedarea.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_enclosedarea.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 2019](../examples/examples_new2019_overview.htm)) > Area Calculation between Curves

| Area Calculation between Curves |
| --- |

This example shows the result of the [Enclosed Area](../../dlgmaths/calc_basis_dlg/dlgchnenclosedarea_dialog.htm) function. The function calculates the area enclosed by curves. DIAdem calculates the partial areas of the first overlapping to the first intersection point of two curves, from intersection to intersection, and to the last overlapping. In the example, the partial areas are marked by red vertical lines.

Start example

#### Click a filename to load this file into DIAdem.

| EnclosedArea.vbs | Script file |
| --- | --- |
| EnclosedArea.py | Python script file |
| EnclosedArea.tdr | Layout file |
| Report_EXPL.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_2daxis_2.htm language=dede -->
## TOPIC 00818: 2D-Achsensysteme mit kanalabhängige Einfärbung

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_2daxis_2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/exploff/examples/expl_report_2daxis_2.htm
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D-Achsensysteme](../examples/examples_2daxissystems_overview.htm) | [Version 2018](../examples/examples_new2018_overview.htm)) > 2D-Achsensysteme mit kanalabhängige Einfärbung

| 2D-Achsensysteme mit kanalabhängige Einfärbung |
| --- |

Diese Beispiel zeigt Achsensysteme mit verschiedenen Kurven, 
 die DIAdem in Abhängigkeit anderer Kanalwerten einfärbt.

Beispiel starten

Beispieldateien kopieren

#### Klicken Sie auf einen Dateinamen, um diese Datei in DIAdem zu laden

| Expl_Report_2DAxis_2.TDR | Layoutdatei |
| --- | --- |
| Report_Data.tdm | Datendatei |

|  | Hinweis Beim Start dieses Beispiels lädt DIAdem Beispieldateien und überschreibt dabei aktuelle Daten und Layouts. |
| --- | --- |

#### Vorgehensweisen

[Beschriften von Kurvenpunkten mit Texten in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Beschriften von Kurvenpunkten mit x-Werten in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Darstellen eines Kurvenausschnitts in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Darstellen von Konstanten in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Darstellen von Kurven in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Darstellen von Kurvenlegenden in Achsensystemen](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Darstellen zusätzlicher y-Achsen in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Drag&Drop von Kanälen auf Unterachsen in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Eigenschaften von x- und y-Achsen auf andere 2D-Achsensysteme übertragen](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Format übertragen](../../procpresent/report_general/procpres_formatpainter.htm) | [Transformieren von Kurven](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_2dbars_2.htm language=dede -->
## TOPIC 00819: 2D-Achsensysteme mit gestapelten Balken

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_2dbars_2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/exploff/examples/expl_report_2dbars_2.htm
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D-Achsensysteme](../examples/examples_2daxissystems_overview.htm) | [Version 2018](../examples/examples_new2018_overview.htm)) > 2D-Achsensysteme mit gestapelten Balken

| 2D-Achsensysteme mit gestapelten Balken |
| --- |

Diese Beispiel zeigt 2D-Achsensysteme mit verschiedenen 
 gestapelten Balkendarstellungen.

Beispiel starten

Beispieldateien kopieren

#### Klicken Sie auf einen Dateinamen, um diese Datei in DIAdem zu laden

| Expl_Report_2DBars_3.TDR | Layoutdatei |
| --- | --- |
| Report_EXPL.tdm | Datendatei |

|  | Hinweis Beim Start dieses Beispiels lädt DIAdem Beispieldateien und überschreibt dabei aktuelle Daten und Layouts. |
| --- | --- |

#### Vorgehensweisen

[Beschriften von Kurvenpunkten mit Texten in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Beschriften von Kurvenpunkten mit x-Werten in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Darstellen eines Kurvenausschnitts in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Darstellen von Konstanten in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Darstellen von Kurven in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Darstellen von Kurvenlegenden in Achsensystemen](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Darstellen zusätzlicher y-Achsen in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Drag&Drop von Kanälen auf Unterachsen in 2D-Achsensystemen](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Eigenschaften von x- und y-Achsen auf andere 2D-Achsensysteme übertragen](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Format übertragen](../../procpresent/report_general/procpres_formatpainter.htm) | [Transformieren von Kurven](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_ab3.htm language=enus -->
## TOPIC 00820: Diesel Diagram

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_ab3.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_ab3.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [Application Examples](../examples/examples_userexamples_overview.htm) > Diesel Diagram

| Diesel Diagram |
| --- |

This example shows a diesel diagram report. The example shows the measurement values in axis systems that have multiple axes.

Start example

#### Click a Filename to Load this File into DIAdem

| Diesel.tdr | Layout file |
| --- | --- |
| Diesel.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_ab5.htm language=enus -->
## TOPIC 00821: Pump Diagram

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_ab5.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_ab5.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [Application Examples](../examples/examples_userexamples_overview.htm) > Pump Diagram

| Pump Diagram |
| --- |

This example shows a pump diagram report. The example shows 2D axis systems with logarithmic axes.

Start example

#### Click a Filename to Load this File into DIAdem

| Vacuum.tdr | Layout file |
| --- | --- |
| Vacuum.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av13.htm language=enus -->
## TOPIC 00822: 2D Axis System with Linear Scaling of the X-Axis in Date Format

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av13.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av13.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [2D Axis Systems](../examples/examples_2daxissystems_overview.htm) > 2D Axis System with Linear Scaling of the X-Axis in Date Format

| 2D Axis System with Linear Scaling of the X-Axis in Date Format |
| --- |

This example shows 2D axis systems with linear scaling of the x-axis in date format.

Start example

#### Click a Filename to Load this File into DIAdem

| 2D_As_ZD.tdr | Layout file |
| --- | --- |
| Report_Expl.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av14.htm language=enus -->
## TOPIC 00823: 3D Axis System with Bar and Waterfall Display

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av14.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av14.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [3D Axis Systems](../examples/examples_3daxissystems_overview.htm) > 3D Axis System with Bar and Waterfall Display

| 3D Axis System with Bar and Waterfall Display |
| --- |

This example shows 3D axis systems with a bar display and a waterfall display.

Start example

#### Click a Filename to Load this File into DIAdem

| 3D_As_BW.tdr | Layout file |
| --- | --- |
| Report_Expl.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying 3D Curves in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_spacecurves.htm) | [Displaying Surfaces in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_plains.htm) | [Moving Coordinate Planes in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_layers.htm) | [Rotating 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_angle.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av17.htm language=enus -->
## TOPIC 00824: 3D Axis System with Isolines and 3D Curves

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av17.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av17.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [3D Axis Systems](../examples/examples_3daxissystems_overview.htm) > 3D Axis System with Isolines and 3D Curves

| 3D Axis System with Isolines and 3D Curves |
| --- |

This example shows 3D axis systems with isolines and 3D curves.

Start example

#### Click a Filename to Load this File into DIAdem

| 3D_As_IR.tdr | Layout file |
| --- | --- |
| Report_Expl.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying 3D Curves in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_spacecurves.htm) | [Displaying Surfaces in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_plains.htm) | [Moving Coordinate Planes in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_layers.htm) | [Rotating 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_angle.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av25.htm language=enus -->
## TOPIC 00825: Using User Commands for Extended Numeric Display

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av25.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av25.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [User commands](../examples/examples_usercommands_overview.htm) > Using User Commands for Extended Numeric Display

| Using User Commands for Extended Numeric Display |
| --- |

This example shows how you can extend the numeric display on the x-axis and on the y-axis of an axis system with the help of user commands. DIAdem extends the numeric values generated by DIAdem by the unit and by a text.

Start example

#### Click a Filename to Load this File into DIAdem

| 2D As_UserFormat_2.vbs | Script file |
| --- | --- |
| 2D UserFormat.tdm | Data file |
| 2D As_UserFormat_2.tdr | Layout file |
| UserCmdReport.vbs | Script file with user command |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

|  | Note In this example DIAdem registers the user command file UserCmdReport.vbs. If you do not save the program settings when you exit DIAdem, the user commands contained in the program settings are not available in your next DIAdem session until you restart the example. |
| --- | --- |

#### Procedures

[Defining User Commands and Global Variables](../../procauto/procauto/procauto_usercommand.htm) | [Using User Commands](../../procshell/procshell/procshell_user_commands.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av26.htm language=enus -->
## TOPIC 00826: Using User Commands for Trend Displays in Tables

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av26.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av26.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([User commands](../examples/examples_usercommands_overview.htm) | [Version 2014](../examples/examples_new2014_overview.htm)) > Using User Commands for Trend Displays in Tables

| Using User Commands for Trend Displays in Tables |
| --- |

This example shows you how to use user commands in tables. The example displays a monthly trend as symbols, and gates zero values.

Start example

#### Click a Filename to Load this File into DIAdem

| 2D_Tab_UserFormat_1.vbs | Script file |
| --- | --- |
| 2D_UserFormat.tdm | Data file |
| 2D_Tab_UserFormat_1.tdr | Layout file |
| UserCmdReport.vbs | Script file with user command |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

|  | Note In this example DIAdem registers the user command file UserCmdReport.vbs. If you do not save the program settings when you exit DIAdem, the user commands contained in the program settings are not available in your next DIAdem session until you restart the example. |
| --- | --- |

#### Procedures

[Defining User Commands and Global Variables](../../procauto/procauto/procauto_usercommand.htm) | [Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm) | [Using User Commands](../../procshell/procshell/procshell_user_commands.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av30.htm language=enus -->
## TOPIC 00827: 2D Axis Systems with Different Axis Arrangements

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av30.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av30.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [2D Axis Systems](../examples/examples_2daxissystems_overview.htm) > 2D Axis Systems with Different Axis Arrangements

| 2D Axis Systems with Different Axis Arrangements |
| --- |

This example shows axis systems with various axis setups.

Start example

#### Click a Filename to Load this File into DIAdem

| Expl_Report_2DAxis.TDR | Layout file |
| --- | --- |
| Report_EXPL.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av39.htm language=enus -->
## TOPIC 00828: 2D Tables

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av39.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av39.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [Tables](../examples/examples_tables_overview.htm) > 2D Tables

| 2D Tables |
| --- |

This example shows various 2D tables.

Start example

#### Click a Filename to Load this File into DIAdem

| Expl_Report_Table.TDR | Layout file |
| --- | --- |
| Report_EXPL.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av6.htm language=enus -->
## TOPIC 00829: 2D Axis Systems with Bar Display and Differential Display

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av6.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av6.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [2D Axis Systems](../examples/examples_2daxissystems_overview.htm) > 2D Axis Systems with Bar Display and Differential Display

| 2D Axis Systems with Bar Display and Differential Display |
| --- |

This example shows 2D axis systems with bar display and differential display.

Start example

#### Click a Filename to Load this File into DIAdem

| 2D_As_BD.tdr | Layout file |
| --- | --- |
| Report_Expl.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av7.htm language=enus -->
## TOPIC 00830: 2D Axis System with a Legend

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av7.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av7.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [2D Axis Systems](../examples/examples_2daxissystems_overview.htm) > 2D Axis System with a Legend

| 2D Axis System with a Legend |
| --- |

This example shows 2D axis systems with different legends.

Start example

#### Click a Filename to Load this File into DIAdem

| 2D_As_Le.tdr | Layout file |
| --- | --- |
| Report_Expl.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av8.htm language=enus -->
## TOPIC 00831: 2D Axis System with Linear Axis Scaling

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av8.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av8.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [2D Axis Systems](../examples/examples_2daxissystems_overview.htm) > 2D Axis System with Linear Axis Scaling

| 2D Axis System with Linear Axis Scaling |
| --- |

This example shows 2D axis systems with linear scaling.

Start example

#### Click a Filename to Load this File into DIAdem

| 2D_As_Li.tdr | Layout file |
| --- | --- |
| Report_Expl.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_av9.htm language=enus -->
## TOPIC 00832: 2D Axis System with Logarithmic Axis Scaling

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_av9.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_av9.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../examples/examples_generatingreports_overview.htm) > [2D Axis Systems](../examples/examples_2daxissystems_overview.htm) > 2D Axis System with Logarithmic Axis Scaling

| 2D Axis System with Logarithmic Axis Scaling |
| --- |

This example shows 2D axis systems with logarithmic scaling of the x-axes and the y-axes.

Start example

#### Click a Filename to Load this File into DIAdem

| 2D_As_Lo.tdr | Layout file |
| --- | --- |
| Report_Expl.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_layout_to_powerpoint.htm language=enus -->
## TOPIC 00833: Automatically Creating a PowerPoint Presentation

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_layout_to_powerpoint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_layout_to_powerpoint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Application Examples](../examples/examples_userexamples_overview.htm) | [Using Interfaces](../examples/examples_usinginterfaces_overview.htm) | [Version 10.1](../examples/examples_new101_overview.htm)) > Automatically Creating a PowerPoint Presentation

| Automatically Creating a PowerPoint Presentation |
| --- |

This example shows how you automatically create a PowerPoint presentation from the current report. For each worksheet DIAdem creates a slide in the PPTX file. DIAdem uses the PowerPoint export which does not require an installed PowerPoint.

Start example

#### Click a filename to load this file into DIAdem.

| REPORT_Layout_to_PowerPoint.vbs | Script file |
| --- | --- |
| REPORT_Layout_to_PowerPoint.py | Python script file |
| REPORT_Layout_to_PowerPointTemplate.pptx | PowerPoint file |

|  | Note To receive CodeCompletion for PowerPoint in the script editor select Microsoft Powerpoint x.x Objects Library in the Registered Type Libraries dialog box. The x.x value depends on your installed Powerpoint version. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_map_scalablebackgroundimage.htm language=enus -->
## TOPIC 00834: 2D-Axis System with Scalable Background Map

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_map_scalablebackgroundimage.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_map_scalablebackgroundimage.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > [Version 2012](../examples/examples_new2012_overview.htm) > 2D-Axis System with Scalable Background Map

| 2D-Axis System with Scalable Background Map |
| --- |

This example shows two 2D axis systems with the same [Background Graphic](../../dlgpresent/graph_dlg_2d_tab/d2axis_backgroundimage_dialog.htm) in two different scales. The background graphic shows a map of the German Eifel. DIAdem uses the exact map coordinates to scale the background graphic automatically to the value range of the respective axis system.

The example shows the entire route in the left axis system and in the right axis system a part of the route. DIAdem uses the coordinates determined by the longitude and latitude to plot the route as a curve in the map.

Start example

#### Click a Filename to Load this File into DIAdem

| Map_ScalableBackgroundImage.tdr | Layout file |
| --- | --- |
| VIEW_MapDisplay.tdm | Data file |
| Example_Map.png | Background graphic |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_report_marker.htm language=enus -->
## TOPIC 00835: 2D Axis System with Lines and Markers

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_report_marker.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_report_marker.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../examples/examples_2daxissystems_overview.htm) | [Version 2011](../examples/examples_new2011_overview.htm)) > 2D Axis System with Lines and Markers

| 2D Axis System with Lines and Markers |
| --- |

This example shows a 2D axis system with lines and different markers. The layout also has a legend.

Start example

#### Click a Filename to Load this File into DIAdem

| Expl_Report_Marker.tdr | Layout file |
| --- | --- |
| Expl_Legend.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Displaying Additional Y-Axes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_subaxis.htm) | [Displaying Constants in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_constant.htm) | [Displaying Curve Extracts in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_scaling.htm) | [Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm) | [Displaying Curves in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_defining.htm) | [Drag and Drop Channels on Subaxes in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_dragndrop.htm) | [Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm) | [Transfer Format](../../procpresent/report_general/procpres_formatpainter.htm) | [Transferring Properties of the X- and Y-Axes to Other 2D Axis Systems](../../procpresent/axis_systems/procpres_axis_copy_properties.htm) | [Transforming Curves](../../procpresent/axis_systems/procpres_2daxis_transformation.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_reportsegment.htm language=enus -->
## TOPIC 00836: Background Segments in DIAdem REPORT

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_reportsegment.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_reportsegment.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../examples/examples_2daxissystems_overview.htm) | [Version 2010](../examples/examples_new2010_overview.htm)) > Background Segments in DIAdem REPORT

| Background Segments in DIAdem REPORT |
| --- |

This example shows how you can highlight interesting areas, for example, controlling a valve, in a 2D axis system by coloring the background.

Use [background segments](../../dlgpresent/graph_dlg_2d_tab/d2axis_segment_dialog.htm) to display Boolean states. A segment corresponds to a colored area where the state is larger 0 or the Boolean value is unequal False. DIAdem plots the segments in the background of the axis system. Match the transparency of the segments so that the segment at the bottom stays visible when the segments overlap.

DIAdem can display background segments in horizontal or vertical direction. If the display is in vertical direction, the x-channel contains the values and the y-channel contains the corresponding boolean states. If the display is in vertical direction, you must assign the channels in the reverse order. Specify the orientation in the dialog box for background segments under **Type**.

Specify the curve labeling with the event texts in the [Curve Parameters»Markers](../../dlgview/dlgview/view_2dcurveprop_dialog.htm) dialog box. The example uses a text channel to label the curve.

Start example

#### Click a Filename to Load this File into DIAdem

| Segment.tdm | Data file |
| --- | --- |
| Segment.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_script_av10.htm language=enus -->
## TOPIC 00837: User Dialog Box with Tables

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_script_av10.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_script_av10.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../examples/examples_generatingscripts_overview.htm) > [User Dialog Boxes](../examples/examples_userdialogs_overview.htm) > User Dialog Box with Tables

| User Dialog Box with Tables |
| --- |

This example shows the entry of various variable types into a table and the display of this table in DIAdem REPORT.

Start example

#### Click the Files to start the Files in DIAdem

| SudExample_1.sud | Dialog box file |
| --- | --- |
| Sud_Input_4.vbs | Script file |
| Sud_Input_4.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Checking a User Dialog Box Entry](../../procsud/procsud/procsud_input.htm) | [Creating a Dynamic User Dialog Box](../../procsud/procsud/procsud_dynamic.htm) | [Creating a Procedure in the Script of a User Dialog Box](../../procsud/procsud/procsud_declaration.htm) | [Creating a User Dialog Box without Linking Variables](../../procsud/procsud/procsud_withoutvar.htm) | [Creating an Extended Table](../../procsud/procsud/procsud_xtable.htm) | [Displaying Graphics in Selection Lists](../../procsud/procsud/procsud_picture.htm) | [Enabling Controls](../../procsud/procsud/procsud_enable.htm) | [Opening the Dialog Editor](../../procscript/procscript/procscript_generating_userdialog.htm) | [Responding to User Entries in User Dialog Boxes](../../procsud/procsud/procsud_event.htm) | [Saving and Restoring the Last Dialog Box Position](../../procsud/procsud/procsud_savedlgpos.htm) | [Saving Control Groups for User Dialog Boxes](../../procsud/procsud/procsud_catalog.htm) | [Specifying the Default Button](../../procsud/procsud/procsud_defaultbutton.htm) | [Tabulator Order in a User Dialog Box](../../procsud/procsud/procsud_tab.htm) | [Using a Script to Fill a Selection List](../../procsud/procsud/procsud_fill.htm) | [Using Channel Selection Lists](../../procsud/procsud/procsud_chnbox.htm) | [Using Hotkeys in a User Dialog Box](../../procsud/procsud/procsud_accelerator.htm) | [Using the Flex Properties](../../procsud/procsud/procsud_flex.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_script_av11.htm language=enus -->
## TOPIC 00838: Dynamic User Dialog Box

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_script_av11.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_script_av11.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../examples/examples_generatingscripts_overview.htm) > [User Dialog Boxes](../examples/examples_userdialogs_overview.htm) > Dynamic User Dialog Box

| Dynamic User Dialog Box |
| --- |

This example shows how you can control a user dialog box based on the entries of a user.

Start example

#### Click a Filename to Load this File into DIAdem

| SudExample_1.sud | Dialog box file |
| --- | --- |
| Sud_SignalSelect.vbs | Script file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Checking a User Dialog Box Entry](../../procsud/procsud/procsud_input.htm) | [Creating a Dynamic User Dialog Box](../../procsud/procsud/procsud_dynamic.htm) | [Creating a Procedure in the Script of a User Dialog Box](../../procsud/procsud/procsud_declaration.htm) | [Creating a User Dialog Box without Linking Variables](../../procsud/procsud/procsud_withoutvar.htm) | [Creating an Extended Table](../../procsud/procsud/procsud_xtable.htm) | [Displaying Graphics in Selection Lists](../../procsud/procsud/procsud_picture.htm) | [Enabling Controls](../../procsud/procsud/procsud_enable.htm) | [Opening the Dialog Editor](../../procscript/procscript/procscript_generating_userdialog.htm) | [Responding to User Entries in User Dialog Boxes](../../procsud/procsud/procsud_event.htm) | [Saving and Restoring the Last Dialog Box Position](../../procsud/procsud/procsud_savedlgpos.htm) | [Saving Control Groups for User Dialog Boxes](../../procsud/procsud/procsud_catalog.htm) | [Specifying the Default Button](../../procsud/procsud/procsud_defaultbutton.htm) | [Tabulator Order in a User Dialog Box](../../procsud/procsud/procsud_tab.htm) | [Using a Script to Fill a Selection List](../../procsud/procsud/procsud_fill.htm) | [Using Channel Selection Lists](../../procsud/procsud/procsud_chnbox.htm) | [Using Hotkeys in a User Dialog Box](../../procsud/procsud/procsud_accelerator.htm) | [Using the Flex Properties](../../procsud/procsud/procsud_flex.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_script_av27.htm language=enus -->
## TOPIC 00839: Searching for and Evaluating Channels

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_script_av27.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_script_av27.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mining and Loading Data](../examples/examples_loadsearchdata_overview.htm) | [Version 10.0](../examples/examples_new100_overview.htm)) > Searching for and Evaluating Channels

| Searching for and Evaluating Channels |
| --- |

The following example shows how to execute a search, how to evaluate a found data set, and how to evaluate in detail a channel contained in the data set. The search displays all data sets that start with Long_Term_Measurement and contain the text Temperature in the file description. DIAdem displays the search results in a user dialog box where you can select the data set to be evaluated. DIAdem displays all channels of this data set in an overview. You select a channel from the overview. DIAdem zooms the channel and executes a histogram classification for the channel.

Start example

#### Click a Filename to Load this File into DIAdem

| Long_Term_Measurement.vbs | Script file |
| --- | --- |
| Long_Term_Measurement.sud | Dialog box file |
| Long_Term_Measurement.tdr | Layout file |
| Long_Term_Measurement_1.tdm | Data file |
| Long_Term_Measurement_2.tdm | Data file |
|  |  |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_script_av9.htm language=enus -->
## TOPIC 00840: User Dialog Box with Changing Background Color

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_script_av9.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_script_av9.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../examples/examples_generatingscripts_overview.htm) > [User Dialog Boxes](../examples/examples_userdialogs_overview.htm) > User Dialog Box with Changing Background Color

| User Dialog Box with Changing Background Color |
| --- |

This example shows a dynamic user dialog box with a changing background color.

Start example

#### Click a Filename to Load this File into DIAdem

| SudExample_1.sud | Dialog box file |
| --- | --- |
| Sud_ColorSelect.vbs | Script file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Checking a User Dialog Box Entry](../../procsud/procsud/procsud_input.htm) | [Creating a Dynamic User Dialog Box](../../procsud/procsud/procsud_dynamic.htm) | [Creating a Procedure in the Script of a User Dialog Box](../../procsud/procsud/procsud_declaration.htm) | [Creating a User Dialog Box without Linking Variables](../../procsud/procsud/procsud_withoutvar.htm) | [Creating an Extended Table](../../procsud/procsud/procsud_xtable.htm) | [Displaying Graphics in Selection Lists](../../procsud/procsud/procsud_picture.htm) | [Enabling Controls](../../procsud/procsud/procsud_enable.htm) | [Opening the Dialog Editor](../../procscript/procscript/procscript_generating_userdialog.htm) | [Responding to User Entries in User Dialog Boxes](../../procsud/procsud/procsud_event.htm) | [Saving and Restoring the Last Dialog Box Position](../../procsud/procsud/procsud_savedlgpos.htm) | [Saving Control Groups for User Dialog Boxes](../../procsud/procsud/procsud_catalog.htm) | [Specifying the Default Button](../../procsud/procsud/procsud_defaultbutton.htm) | [Tabulator Order in a User Dialog Box](../../procsud/procsud/procsud_tab.htm) | [Using a Script to Fill a Selection List](../../procsud/procsud/procsud_fill.htm) | [Using Channel Selection Lists](../../procsud/procsud/procsud_chnbox.htm) | [Using Hotkeys in a User Dialog Box](../../procsud/procsud/procsud_accelerator.htm) | [Using the Flex Properties](../../procsud/procsud/procsud_flex.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_setupperandlowerlimits_demo.htm language=enus -->
## TOPIC 00841: Set Limit Values

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_setupperandlowerlimits_demo.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_setupperandlowerlimits_demo.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Scripts](../examples/examples_scripts_overview.htm) | [Version 2019](../examples/examples_new2019_overview.htm)) > Set Limit Values

| Set Limit Values |
| --- |

The example checks whether the values of a channel are in a specified window. If the values are outside the window, the example replaces them with the limit values. The example uses the [ChnRangeLimit](../../comoff/chnrangelimit.htm) function to replace out-of-range values with upper or lower limits. The example displays the data in a report.

Start example

#### Click a Filename to Load this File into DIAdem

| SetUpperAndLowerLimits.vbs | Script file |
| --- | --- |
| SetUpperAndLowerLimits.sud | Dialog box file |
| Example_Data.tdm | Data file |
| SetUpperAndLowerLimits.tdr | Dialog box file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_shockresponsespectrum.htm language=enus -->
## TOPIC 00842: Evaluating a Shock Response Spectrum

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_shockresponsespectrum.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_shockresponsespectrum.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 2010](../examples/examples_new2010_overview.htm)) > Evaluating a Shock Response Spectrum

| Evaluating a Shock Response Spectrum |
| --- |

The example uses the shock response spectrum to evaluate data.

The Shock Response Spectrum (SRS) function returns the response of a system to a shock by calculating the acceleration, the velocity, or the displacement of the system over the frequency. The function includes the degree of the damping of the component.

Start example

#### Click a filename to load this file into DIAdem.

| ShockResponseSpectrum_Automated.vbs | Script file |
| --- | --- |
| ShockResponseSpectrum_Automated.py | Python script file |
| ShockResponseSpectrum.tdm | Data file |
| ShockResponseSpectrum.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_signalmapping.htm language=enus -->
## TOPIC 00843: Synchronizing Measurement Data

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_signalmapping.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_signalmapping.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 2015](../examples/examples_new2017_overview.htm)) > Synchronizing Measurement Data

| Synchronizing Measurement Data |
| --- |

This example shows you how to align different measurements of different data sets with each other. To do so, the example loads two files which contain a time channel, the data to align, and a synchronization channel respectively. The synchronization channel contains a trigger signal. First the example displays the raw data and then the synchronized data in a report. The example uses the [ChnResampleFreqBasedXOffsetCalc2](../../comoff/chnresamplefreqbasedxoffsetcalc2.htm) function to execute an offset correction and to resample the data.

Start example

#### Click a filename to load this file into DIAdem.

| SignalMapping.vbs | Script file |
| --- | --- |
| SignalMapping.py | Python script file |
| SignalMapping_01.tdm | Data file |
| SignalMapping_02.tdm | Data file |
| SignalMapping_afterSync.tdr | Layout file |
| SignalMapping_beforeSync.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_smoothing.htm language=enus -->
## TOPIC 00844: Smoothing Signals

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_smoothing.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_smoothing.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 2017](../examples/examples_new2017_overview.htm)) > Smoothing Signals

| Smoothing Signals |
| --- |

This example shows you how to smooth signals by generating the floating arithmetic mean, the floating median, or by using the Savitzky-Golay filter. The example shows the raw data and the processed data in a report. The example uses the functions [ChnSmooth](../../comoff/chnsmooth.htm) and [ChnSavitzkyGolayFilter](../../comoff/chnsavitzkygolayfilter.htm) to smooth signals.

Start example

#### Click a filename to load this file into DIAdem.

| Smoothing.vbs | Script file |
| --- | --- |
| Smoothing.py | Python script file |
| Smoothing.tdm | Data file |
| Smoothing.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_smoothing4253h.htm language=enus -->
## TOPIC 00845: Smoothing Signals with the 4253H Filter

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_smoothing4253h.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_smoothing4253h.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Mathematics](../examples/examples_maths_overview.htm) | [Version 2018](../examples/examples_new2018_overview.htm)) > Smoothing Signals with the 4253H Filter

| Smoothing Signals with the 4253H Filter |
| --- |

This example shows you how to use the 4253H filter to smooth signals. This example shows in a report the original data, the data smoothed with the 4253H filter, the moving arithmetic mean, and the data smoothed with the Savitzky-Golay filter. The example uses the functions [ChnSmooth4253H](../../comoff/chnsmooth4253h.htm), [ChnSmooth](../../comoff/chnsmooth.htm) and [ChnSavitzkyGolayFilter](../../comoff/chnsavitzkygolayfilter.htm) to smooth the signals.

Start example

#### Click a filename to load this file into DIAdem.

| Smoothing4253H.vbs | Script file |
| --- | --- |
| Smoothing4253H.py | Python script file |
| Data1.tdm | Data file |
| Smoothing4253H.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_swiveltest_report.htm language=enus -->
## TOPIC 00846: Swivel Analysis at the Engine

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_swiveltest_report.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_swiveltest_report.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Application Examples](../examples/examples_userexamples_overview.htm) | [Version 2015](../examples/examples_new2017_overview.htm)) > Swivel Analysis at the Engine

| Swivel Analysis at the Engine |
| --- |

This example shows how engine oil behaves when the engine swivels. The engine swivels when braking or accelerating, and when going downhill or steering. In greater swiveling angles, the minimum oil pressure can be undershot, the gas contents might be exceeded, or oil spills might occur. This example evaluates a fixed rpm of 3900 revolutions per minute, and displays the evaluation as a table and as symbols in a 2D axis system. Circles in the 2D axis system show the range limits.

Start example

#### Click a filename to load this file into DIAdem.

| Swiveltest_Report.vbs | Script file |
| --- | --- |
| Swiveltest_Report.py | Python script file |
| Swiveltest_Report.tdm | Data file |
| Swiveltest_Layout.tdr | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_tangentcursor.htm language=enus -->
## TOPIC 00847: Calculating a Tangent to a Curve

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_tangentcursor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_tangentcursor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Version 10.2](../examples/examples_new102_overview.htm) | [Viewing and Editing Data](../examples/examples_viewworkdata_overview.htm)) > Calculating a Tangent to a Curve

| Calculating a Tangent to a Curve |
| --- |

This example calculates a straight line between the corner points of a frame cursor. If you make the frame cursor very narrow, the straight line is the tangent to the curve. In the tooltip, DIAdem shows the gradient as a dy/dx value.

The script file TangentCursor_Init.vbs registers a user command that calculates a diagonal between the corners of the frame cursor, in relation to the current cursor positions. The user command saves the calculated data in a new channel pair and displays this data as a straight line in DIAdem VIEW.

Start example

#### Click a filename to load this file into DIAdem.

| TangentCursor_Init.vbs | Script file |
| --- | --- |
| TangentCursor_Event.vbs | Script file with user command |
| Example_data.tdm | Data file |
| TangentCursor.tdv | Layout file |

|  | Note° When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

|  | Note You only can load the layout file TangentCursor.tdv without errors if you have registered the user command. |
| --- | --- |

|  | Note To reset the event OnCursorChanged click here. DIAdem sets the View.Events.OnCursorChanged property to the default value. |
| --- | --- |

|  | Note In this example DIAdem registers the user command file TangentCursor_Event.vbs. If you do not save the program settings when you exit DIAdem, the user commands contained in the program settings are not available when you start DIAdem again until you restart the example. |
| --- | --- |

#### Procedures

[Defining User Commands and Global Variables](../../procauto/procauto/procauto_usercommand.htm) | [Using User Commands](../../procshell/procshell/procshell_user_commands.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_tolerance.htm language=enus -->
## TOPIC 00848: Wizard for Tolerance Evaluation

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_tolerance.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_tolerance.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([User Dialog Boxes](../examples/examples_userdialogs_overview.htm) | [Version 10.2](../examples/examples_new102_overview.htm)) > Wizard for Tolerance Evaluation

| Wizard for Tolerance Evaluation |
| --- |

This example shows a user dialog box that you use to execute an evaluation. The dialog box is structured like a wizard that requests the necessary information step-by-step. The evaluation compares the charge curves and the discharge curves of a rechargeable flash battery, with a specified set curve. The set curve consists of an upper hull curve and a lower hull curve. You set the tolerance range in the dialog box.

The user dialog box uses the [TabPageCtrl](../../sudref/objects/sud_objects_totabpagectrl.htm) control element to display a different tab for each evaluation step, in the bottom part of the user dialog box.

Start example

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Tolerance.vbs | Script file |
| --- | --- |
| Tolerance.sud | Dialog box file |
| Tolerance.tdr | Layout file |
| Tol_Measure1.tdm | Data file |
| Tol_Measure2.tdm | Data file |
| Tol_Set_Point1.tdm | Data file |
| Tol_Set_Point2.tdm | Data file |

#### Procedures

[Checking a User Dialog Box Entry](../../procsud/procsud/procsud_input.htm) | [Creating a Dynamic User Dialog Box](../../procsud/procsud/procsud_dynamic.htm) | [Creating a Procedure in the Script of a User Dialog Box](../../procsud/procsud/procsud_declaration.htm) | [Creating a User Dialog Box without Linking Variables](../../procsud/procsud/procsud_withoutvar.htm) | [Creating an Extended Table](../../procsud/procsud/procsud_xtable.htm) | [Displaying Graphics in Selection Lists](../../procsud/procsud/procsud_picture.htm) | [Enabling Controls](../../procsud/procsud/procsud_enable.htm) | [Opening the Dialog Editor](../../procscript/procscript/procscript_generating_userdialog.htm) | [Responding to User Entries in User Dialog Boxes](../../procsud/procsud/procsud_event.htm) | [Saving and Restoring the Last Dialog Box Position](../../procsud/procsud/procsud_savedlgpos.htm) | [Saving Control Groups for User Dialog Boxes](../../procsud/procsud/procsud_catalog.htm) | [Specifying the Default Button](../../procsud/procsud/procsud_defaultbutton.htm) | [Tabulator Order in a User Dialog Box](../../procsud/procsud/procsud_tab.htm) | [Using a Script to Fill a Selection List](../../procsud/procsud/procsud_fill.htm) | [Using Channel Selection Lists](../../procsud/procsud/procsud_chnbox.htm) | [Using Hotkeys in a User Dialog Box](../../procsud/procsud/procsud_accelerator.htm) | [Using the Flex Properties](../../procsud/procsud/procsud_flex.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_treecontrol.htm language=enus -->
## TOPIC 00849: User Dialog Box with Tree

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_treecontrol.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_treecontrol.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([User Dialog Boxes](../examples/examples_userdialogs_overview.htm) | [Version 2017](../examples/examples_new2017_overview.htm)) > User Dialog Box with Tree

| User Dialog Box with Tree |
| --- |

This example shows a user dialog box with a tree. Use the [Tree](../../sudref/objects/sud_objects_totreectrl.htm) for input control and configuration. Use a [context menu](../../contextmenu/objects/contextmenu_objects_imenupoints.htm) to open and close the tree. At some places in the tree, the dialog box supports the dragging and dropping into another field of the dialog box.

Start example

#### Click a Filename to Load this File into DIAdem

| TreeControl.sud | Dialog box file |
| --- | --- |
| TreeControl.vbs | Script file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

#### Procedures

[Checking a User Dialog Box Entry](../../procsud/procsud/procsud_input.htm) | [Creating a Dynamic User Dialog Box](../../procsud/procsud/procsud_dynamic.htm) | [Creating a Procedure in the Script of a User Dialog Box](../../procsud/procsud/procsud_declaration.htm) | [Creating a User Dialog Box without Linking Variables](../../procsud/procsud/procsud_withoutvar.htm) | [Creating an Extended Table](../../procsud/procsud/procsud_xtable.htm) | [Displaying Graphics in Selection Lists](../../procsud/procsud/procsud_picture.htm) | [Enabling Controls](../../procsud/procsud/procsud_enable.htm) | [Opening the Dialog Editor](../../procscript/procscript/procscript_generating_userdialog.htm) | [Responding to User Entries in User Dialog Boxes](../../procsud/procsud/procsud_event.htm) | [Saving and Restoring the Last Dialog Box Position](../../procsud/procsud/procsud_savedlgpos.htm) | [Saving Control Groups for User Dialog Boxes](../../procsud/procsud/procsud_catalog.htm) | [Specifying the Default Button](../../procsud/procsud/procsud_defaultbutton.htm) | [Tabulator Order in a User Dialog Box](../../procsud/procsud/procsud_tab.htm) | [Using a Script to Fill a Selection List](../../procsud/procsud/procsud_fill.htm) | [Using Channel Selection Lists](../../procsud/procsud/procsud_chnbox.htm) | [Using Hotkeys in a User Dialog Box](../../procsud/procsud/procsud_accelerator.htm) | [Using the Flex Properties](../../procsud/procsud/procsud_flex.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_userdefinedfct.htm language=enus -->
## TOPIC 00850: User-Defined Evaluations in DIAdem ANALYSIS

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_userdefinedfct.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_userdefinedfct.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Extending Functionalities with Scripts](../examples/examples_extensions.htm) | [Mathematics](../examples/examples_maths_overview.htm) | [Scripts](../examples/examples_scripts_overview.htm) | [User Dialog Boxes](../examples/examples_userdialogs_overview.htm) | [Version 2012](../examples/examples_new2012_overview.htm)) > User-Defined Evaluations in DIAdem ANALYSIS

| User-Defined Evaluations in DIAdem ANALYSIS |
| --- |

This example generates a new function group in DIAdem ANALYSIS to which you can add your own functions.

Start the example to create the new function group. The new function group contains buttons for requesting the configuration dialog box and deleting the function group. DIAdem uses the [BarManager object](../../tobarmanagerint/objects/tobarmanagerint_objects_overview.htm) to create the function group.

Click **Specify Evaluations** to insert functions into this function group. The configuration dialog box offers several functions. Click a checkbox to include the function in the function group. You also can add user-defined functions to the selection. Every function requires a script, an ICO file, and a tooltip. You can arrange the functions in the selection and remove individual functions. When you close the dialog box, DIAdem adds the selected functions to the function group. DIAdem saves the selected functions with the settings.

Start example

#### Click a filename to load this file into DIAdem.

| UserDefinedFCT_Init.vbs | Script file |
| --- | --- |
| UserDefinedFCT_Include.vbs | Script file |
| UserDefinedFCT_Remove.vbs | Script file |
| UserDefinedFCT.sud | Script file |
| REPORT_Library.vbs | Script file |
| UserDefinedFCT*.ico | Symbol file |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_userdeftoolbars.htm language=enus -->
## TOPIC 00851: Custom Toolbars on DIAdem Panels

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_userdeftoolbars.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_userdeftoolbars.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[New Examples](../examples/examples_new_overview.htm) > [Version 2020](../examples/examples_new2020_overview.htm) > Custom Toolbars on DIAdem Panels

| Custom Toolbars on DIAdem Panels |
| --- |

This example generates a new customizable function group on the DIAdem panels you select. You can use this function group to call a configuration dialog box or to delete the function group. DIAdem uses the [BarManager object](../../tobarmanagerint/objects/tobarmanagerint_objects_overview.htm) to create the function group.

Click **Specify Evaluations** in the new function group to create new functions in this function group. Every function requires a script, an ICO file, and a tooltip.

Start example

#### Click a filename to load this file into DIAdem.

| UserDefToolBars_Init.vbs | Script file |
| --- | --- |
| UserDefToolBars_Include.vbs | Script file |
| UserDefToolBars_Remove.vbs | Script file |
| UserDefToolBars.sud | Script file |
| UserDefToolBars*.ico | Symbol file |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_valve_analysis.htm language=enus -->
## TOPIC 00852: Test Rig Analysis

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_valve_analysis.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_valve_analysis.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Application Examples](../examples/examples_userexamples_overview.htm) | [Scripts](../examples/examples_scripts_overview.htm) | [Version 2015](../examples/examples_new2017_overview.htm) | [Viewing and Editing Data](../examples/examples_viewworkdata_overview.htm)) > Test Rig Analysis

| Test Rig Analysis |
| --- |

This examples shows you how to check channels for certain conditions and specify characteristic statistical values in channels. The example uses [Event search](../../dlgmaths/calc_basis_dlg/dlgchneventdetection_dialog.htm) functions, such as [ChnEventDetectionWindow](../../comoff/chneventdetectionwindow.htm), [ChnEventStatMin](../../comoff/chneventstatmin.htm), [ChnEventStatMax](../../comoff/chneventstatmax.htm), and [ChnEventStatArithMean](../../comoff/chneventstatarithmean.htm).

The travel and force of a piston are measured on a test rig. To analyze the force, each travel is divided into sections and their characteristic statistical values calculated.

The example loads a layout into DIAdem VIEW where you analyze the data in graphics.

Start example

#### Click a filename to load this file into DIAdem.

| PistonMovement_Analysis.vbs | Script file |
| --- | --- |
| PistonMovement_Analysis.py | Python script file |
| PistonMovement_Analysis.tdm | Data file |
| PistonMovement_Analysis.tdr | Layout file |
| PistonMovement_Analysis.tdv | Layout file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_view_av1.htm language=enus -->
## TOPIC 00853: Viewing and Automatically Analyzing Data

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_view_av1.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_view_av1.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Scripts](../examples/examples_scripts_overview.htm) | [Viewing and Editing Data](../examples/examples_viewworkdata_overview.htm)) > Viewing and Automatically Analyzing Data

| Viewing and Automatically Analyzing Data |
| --- |

This example shows how you can automatically generate a layout in the DIAdem VIEW panel, and load data into the layout. You can then select a range in the axis system. DIAdem analyzes the range and displays the analysis results in the layout.

Start example

#### Click a filename to load this file into DIAdem.

| VIEW_FFT.vbs | Script file |
| --- | --- |
| VIEW_FFT.py | Python script file |
| FFT_Expl_1.tdm | Data file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_view_av2.htm language=enus -->
## TOPIC 00854: Using a User Command to Calculate the Difference between the Y-Values

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_view_av2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_view_av2.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Viewing and Editing Data](../examples/examples_viewworkdata_overview.htm) > Using a User Command to Calculate the Difference between the Y-Values

| Using a User Command to Calculate the Difference between the Y-Values |
| --- |

This example shows how DIAdem automatically calculates the difference between the y-values of the displayed curve and the y-values of the leading curve, in the DIAdem VIEW panel. 
DIAdem calculates the difference between the y-values in the [user command](../../dlgscript/script_dlg_menu/dlgscriptreg_dialog.htm) CurrentYDiff. The command is in the legend of the VIEW axis system.

Refer to the UserCmdVIEW.vbs user file for the user command CurrentYDiff.

Start example

#### Click a Filename to Load this File into DIAdem

| Expl_VIEW_DiffLeg.vbs | Script file |
| --- | --- |
| Expl_VIEW_DiffLeg.tdv | Layout file |
| Report_EXPL.tdm | Data file |
| UserCmdVIEW.vbs | Script file with user command |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

|  | Note In this example DIAdem registers the user command file UserCmdVIEW.vbs. If you do not save the program settings when you exit DIAdem, the user commands contained in the program settings are not available when you start DIAdem again until you restart the example. |
| --- | --- |

#### Procedures

[Defining User Commands and Global Variables](../../procauto/procauto/procauto_usercommand.htm) | [Using User Commands](../../procshell/procshell/procshell_user_commands.htm)

<!--NI_TOPIC bundle=diadem path=exploff/examples/expl_view_av3.htm language=enus -->
## TOPIC 00855: Creating and Viewing Long Data Channels

- bundle_id: `diadem`
- source_path: `exploff/examples/expl_view_av3.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/exploff/examples/expl_view_av3.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Viewing and Editing Data](../examples/examples_viewworkdata_overview.htm) > Creating and Viewing Long Data Channels

| Creating and Viewing Long Data Channels |
| --- |

This example shows how DIAdem automatically creates long data channels and how you can view the data in the DIAdem VIEW panel. The example creates a layout in the DIAdem VIEW panel and displays the long data channels. DIAdem displays a zoomed extract of the data in an area.

Start example

#### Click a filename to load this file into DIAdem.

| Expl_VIEW_LongChn.vbs | Script file |
| --- | --- |
| Expl_VIEW_LongChn.py | Python script file |

|  | Note When this example starts, DIAdem loads example files and overwrites existing data and layouts. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_autoscaling_offset.htm language=enus -->
## TOPIC 00856: Different Offset Corrections

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_autoscaling_offset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_autoscaling_offset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Scaling and Linearizing](../explonl/explonl_scaling_overview.htm) | [Version 2012](../../exploff/examples/examples_new2012_overview.htm)) > Different Offset Corrections

| Different Offset Corrections |
| --- |

This example shows a block diagram which subtracts an offset from the measurement values. Press <Esc> or click **Stop Measurement** on the toolbar to terminate the measurement.

Start example

#### Scenario

You want to eliminate an offset in the measurement values.

#### Solution

The simulation blocks **Random** and **Generator** generate a signal. Several **Offset Correction** scaling blocks use different methods to specify different offset values from a specified start interval. After the start interval DIAdem subtracts the offset values from this signal. The example uses start intervals of different lengths to specify the first value and the last value, the smallest value and the greatest value, and the mean value as the offset.

The top curve display plots the generated and unchanged signal from the start of the measurement. The the bottom curve display on the other hand does not plot the offset-corrected signal until the specified calculation interval has elapsed. Both y-axes are automatically scaled.

#### Click a Filename to Load this File into DIAdem

| AutoScaling_Offset.DAC | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_ab4.htm language=enus -->
## TOPIC 00857: Generating Signals (2)

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_ab4.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_ab4.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Generating Signals (2)

| Generating Signals (2) |
| --- |

This example shows a block diagram that generates different signals and applies mathematical functions to them. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to modulate manually several generated signals during a measurement.

#### Solution

Two **Function Generator** simulation blocks and one **Formula** processing block generate signals. Slider controls and dials are connected at the remote input of the function generator, to modulate the frequency, the amplitude, and the offset of the generated signal during a measurement. The function generators and the associated manual instruments are in a subblock diagram.

The **Addition** formula block adds all the signals and amplifies the cumulative signal, in order for the signal to be output to the computer speakers.

#### Click a Filename to Load this File into DIAdem

| Fctgene.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_ab5.htm language=enus -->
## TOPIC 00858: Visualizing Measurement Data from a Car Race

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_ab5.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_ab5.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Visualizing Measurement Data from a Car Race

| Visualizing Measurement Data from a Car Race |
| --- |

This example shows a block diagram that simulates a lap of the Vallelunga race track in Italy. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

During a race at the Vallelunga race track, data from a vehicle is saved in a data file. To evaluate the reactions of the driver and the vehicle, you want to simulate one lap of the race.

#### Solution

DIAdem reads out the race data from the Data Portal and visualizes the race with an XY-display below a sketch of the race track. Gauge, bar, binary, and numeric displays illustrate the values measured on the vehicle.

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores and block diagrams. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Course.dac | Block diagram file |
| --- | --- |
| DAC_Expl.tdm | Data file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_ab6.htm language=enus -->
## TOPIC 00859: GPS Visualization

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_ab6.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_ab6.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Version 2014](../../exploff/examples/examples_new2014_overview.htm) | [Visualizing](../explonl/explonl_visualize_overview.htm)) > GPS Visualization

| GPS Visualization |
| --- |

This example displays a block diagram which measures the data of a recorded motorbike test drive through the mountains in the German Eifel. The example displays the entire route in an axis system and the speed and altitude over NN over time. The example also displays the longitude and latitude value pairs as a line in the map display and outputs the towns the test drive passed through in a message. The example uses map data from a cache so that you can use this example offline.

Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to visualize a motorbike test drive through the mountains in the German Eifel. During the trip, a GPS receiver (Global Positioning System) creates a data file with coordinates.

#### Solution

DIAdem reads the coordinates from the Data Portal and visualizes the drive in a map display. It also displays further measured data in curve displays and messages.

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores and block diagrams. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Gps.dac | Block diagram file |
| --- | --- |
| VIEW_MapDisplay.tdm | Data file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_ab7.htm language=enus -->
## TOPIC 00860: Critical Alarms Linked to a Master Alarm

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_ab7.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_ab7.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Critical Alarms Linked to a Master Alarm

| Critical Alarms Linked to a Master Alarm |
| --- |

This example shows a block diagram that displays a master alarm. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

If several critical alarms trigger simultaneously, you want a central master alarm to trigger, which is to be confirmed separately. You want to visualize this master alarm with a light and an alarm message that you format separately.

#### Solution

The alarm generator monitors the signals from three slider controls. If all three signals trigger alarms with the priority **Error**, the subblock diagram **Logic** generates a data signal. This data signal connects a data bus to the alarm generator, which then generates a master alarm with the priority **Danger**.

The **AL FMT2** alarm block forwards a specific warning from the master alarm to the online text display. At the same time, the **Light** subblock diagram activates a status display.

#### Click a Filename to Load this File into DIAdem

| AlDem3.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av10.htm language=enus -->
## TOPIC 00861: Hold Function

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av10.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av10.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Hold Function

| Hold Function |
| --- |

This example shows a block diagram with a hold function. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want a brief control impulse to hold for three seconds.

#### Solution

A **Push button** control block generates a brief control impulse, which a monoflop holds for three seconds. You set the length of the hold time in the **Monoflop** control block.

#### Click a Filename to Load this File into DIAdem

| Hold_Fct.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av11.htm language=enus -->
## TOPIC 00862: Trigger Measurement

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av11.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av11.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Acquiring and Displaying](../explonl/explonl_measure_overview.htm) > Trigger Measurement

| Trigger Measurement |
| --- |

This example shows a block diagram in which a trigger controls the measurement. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want data storage to start at a specific measured value. You also want to save the fifty measured values before the trigger event.

#### Solution

The **Trigger** control block monitors the slider signal. If you move the slider control over the threshold value 5, the **Trigger** control block starts to save values. The pre-trigger setting in the storage block specifies that DIAdem also saves the last fifty values **before** the trigger event.

#### Click a Filename to Load this File into DIAdem

| Triggerm.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av12.htm language=enus -->
## TOPIC 00863: Linear Scaling and Two-Point Scaling

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av12.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av12.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Scaling and Linearizing](../explonl/explonl_scaling_overview.htm) > Linear Scaling and Two-Point Scaling

| Linear Scaling and Two-Point Scaling |
| --- |

This example shows a block diagram with linear scaling and two-point scaling. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to use scaling to adapt and output a generated sine signal with 1 Hz frequency and the amplitude 1:

1. as a voltage signal from -10 to +10 V
2. as a voltage signal from 4 to 6 V
3. as a voltage signal from 0 to 10 V
4. as a current standard signal from 4 to 20 mA

#### Solution

A **Function Generator** simulation block generates a Hz sine signal with the amplitude one. A **Linear Scaling** block uses factor and offset parameters to convert the sine signal into the voltage signals (1) and (2). A **Two-Point Scaling** block uses two value pairs to convert the sine signal into the signals (3) and (4). Scaling in DIAdem enables you to assign units, so the curve display shows the current signal in milliamperes [mA] and the voltage signal in volts [V].

#### Click a Filename to Load this File into DIAdem

| Lin_Scal.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av13.htm language=enus -->
## TOPIC 00864: Free Linearization

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av13.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av13.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Scaling and Linearizing](../explonl/explonl_scaling_overview.htm) > Free Linearization

| Free Linearization |
| --- |

This example shows a block diagram with free linearization. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

A new rpm sensor has been developed. Reference measurements give a sensor-specific characteristic curve. You use the characteristic curve to convert the voltage measured by the sensor into rpm [1/min], and you visualize the data.

#### Solution

The **Free Linearization** type scaling block uses an interpolation table for linearization. The input values are voltages that correspond to the values of the x-channel of the characteristic curve. The scaling block converts the voltages into the corresponding rpm values of the y-channel of the characteristic curve and outputs the scaled values.

#### Click a Filename to Load this File into DIAdem

| M_P_Scal.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av14.htm language=enus -->
## TOPIC 00865: Thermo Linearization

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av14.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av14.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Scaling and Linearizing](../explonl/explonl_scaling_overview.htm) > Thermo Linearization

| Thermo Linearization |
| --- |

This example shows a block diagram with thermo linearizations. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to use thermocouples to measure temperatures.

1. To visualize the temperatures, you use thermo linearization to compensate the non-linear relation between the measured voltage and the temperature.
2. You simulate pre-amplification, which is often executed with external signal conditioning. Your thermo linearization configuration in DIAdem includes these aspects.

#### Solution

A slider control simulates a measured thermo voltage. You set the thermocouple and the reference temperature in the **Thermo scal1** scaling block, which is a **Thermo Linearization** block, and the block converts the voltage signal into the corresponding temperature (1). The **Thermo scal2** scaling block converts the external pre-amplified voltage signal into the corresponding temperature (2). Curve displays visualize all the voltage signals and the resulting temperature signals.

#### Click a Filename to Load this File into DIAdem

| Ther_Sca.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av15.htm language=enus -->
## TOPIC 00866: Message Display

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av15.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av15.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Message Display

| Message Display |
| --- |

This example shows a block diagram that displays messages in relation to a measured value. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to display text messages that relate to measurement values.

#### Solution

In relation to the measured value, DIAdem displays various messages. The message.asc text file contains ten lines with messages. You use the slider control to generate measured values from 0 to 10, which the message block uses as the index for the text lines.

|  | Note The example works only with incrementing message numbers. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Message.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av16.htm language=enus -->
## TOPIC 00867: Remote Control of Manual Instruments

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av16.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av16.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Remote Control of Manual Instruments

| Remote Control of Manual Instruments |
| --- |

This example shows a block diagram with remote-controlled manual instruments. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to be able to control a process manually or to run it automatically.

#### Solution

A generated sine signal automatically controls a slider control and a dial. You use a push button to switch the remote control on and off. When the remote control is off you operate the instruments manually.

#### Click a Filename to Load this File into DIAdem

| Remote.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av17.htm language=enus -->
## TOPIC 00868: Display Instruments

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av17.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av17.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Display Instruments

| Display Instruments |
| --- |

This example shows a block diagram with display instruments. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to display a generated sine signal with various display instruments.

#### Solution

Various display instruments display the sine signal. The polar display and the XY display show an additional sine signal, which is shifted by 90°.

#### Click a Filename to Load this File into DIAdem

| OnlinStr.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av19.htm language=enus -->
## TOPIC 00869: Parallel Runs

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av19.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av19.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Sequence Control](../explonl/explonl_processing_overview.htm) > Parallel Runs

| Parallel Runs |
| --- |

This example shows a block diagram with parallel measurement runs. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to measure two signal sources separately with two measurements that run parallel. You sample the first signal with 10 Hz, and the second signal with 100 Hz.

#### Solution

Two **Noise** simulation blocks generate noise signals. Each noise block is connected to a **System Clock** system block, which specifies the sampling rate.

The top curve display shows a noise signal sampled at 10 Hz. The bottom curve display shows a noise signal sampled at 100 Hz.

#### Click a Filename to Load this File into DIAdem

| Par_Task.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av2.htm language=enus -->
## TOPIC 00870: Data Storage in Files

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av2.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Data Storage](../explonl/explonl_datastorage_overview.htm) > Data Storage in Files

| Data Storage in Files |
| --- |

This example shows a block diagram that saves the measured data directly to a file. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to save measured signals directly to the data file Storedat. You save the file in TDM format to analyze the file later.

#### Solution

Three simulation blocks generate a sine signal, a random signal, and a noise signal, at a sampling rate of 100 Hz. The **File Storage** system block creates the TDM file Storedat.TDM in the user folder and saves the three generated signals as waveform channels. When the number of values to be saved is reached, the storage block finishes the measurement.

|  | Note To specify the properties for data storage, select Settings»Single Point Processing»Data Storage in DIAdem DAC. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| StoreDat.dac | Block diagram file |
| --- | --- |

#### Procedures

[Data Storage in the Data Portal](../../procdacsv/procdacsv/procdacsv_saving_data_portal.htm)

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av20.htm language=enus -->
## TOPIC 00871: Sequential Runs

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av20.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av20.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Sequence Control](../explonl/explonl_processing_overview.htm) > Sequential Runs

| Sequential Runs |
| --- |

This example shows a block diagram with two measurement runs. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to start two measurement runs with different sampling rates, one after the other. You want the second measurement to start after the first measurement finishes.

#### Solution

The first measurement acquires a generated sine signal at a sampling rate of 500 Hz. The second measurement samples a random signal at 100 Hz. Both measurements are limited to five seconds.

A yellow system bus links both measurements via the **Clock Status** control block. The **Clock Status** control block does not start the second measurement until the first measurement is deactivated. Curve displays and numeric displays show the signals.

#### Click a Filename to Load this File into DIAdem

| Seq_Task.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av21.htm language=enus -->
## TOPIC 00872: Dynamic System Clock

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av21.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av21.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Sequence Control](../explonl/explonl_processing_overview.htm) > Dynamic System Clock

| Dynamic System Clock |
| --- |

This example shows a block diagram that sets the clock. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to use a dial to change the sampling rate for the acquisition and visualization of a sine signal during a measurement.

#### Solution

The **Clock** simulation block specifies the sampling rate. The **Timer** control block applies a mathematical formula to the sampling rate and the **Counter** processing block. The clock generator returns a triggered control signal to the **Clock2** system block. The **Clock2** system block converts the control signal into a system signal and forwards the signal to the **Signal Copy** control block. The signal copy generates a new copy of the original sine signal at the new sampling rate and the curve display visualizes the signal copy.

#### Click a Filename to Load this File into DIAdem

| OnlClock.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av22.htm language=enus -->
## TOPIC 00873: Generating Signals (1)

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av22.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av22.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Generating Signals (1)

| Generating Signals (1) |
| --- |

This example shows a block diagram that generates other signals from a sine signal. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to generate other signals from a sine signal.

#### Solution

The **Function Generator** block generates a sine signal from which three **Formula** processing blocks derive three other signals. The **1_Wave_Re** formula block works like a halfwave rectifier and suppresses negative waves. The **2_Wave_Re** formula block works like a fullwave rectifier and turns the negative halfwaves up. The **Phases** formula block executes a phase cut at the positive halfwave and at the negative halfwave.

#### Click a Filename to Load this File into DIAdem

| Sign_Gen.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av23.htm language=enus -->
## TOPIC 00874: Counter

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av23.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av23.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Counter

| Counter |
| --- |

This example shows a block diagram with two counters. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to create two counters:

1. One counter that increments and decrements.
2. One counter that increments and resets.

#### Solution

Counter (1) contains two **Push Button** simulation blocks and one **Formula** processing block on the data level. The formula block performs a mathematical operation on the push button impulses and the **Digits** visualization block displays the result.

Counter (2) contains two **Push Button** control blocks and one **Formula** processing block on the control level. The formula block adds up the push button impulses and the **Digits** visualization block displays the result. The **Reset** button sets the the counter to the value zero.

#### Click a Filename to Load this File into DIAdem

| Counter.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av24.htm language=enus -->
## TOPIC 00875: PID Controller

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av24.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av24.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > PID Controller

| PID Controller |
| --- |

This example shows a block diagram with a PID controller. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to demonstrate how a PID controller functions.

#### Solution

A slider control provides the set point to the **PID Controller** processing block. A **Formula** processing block simulates the controlled system and returns the feedback value to the PID controller. The PID controller is set as a PI controller that controls the feedback value as fast as possible to the set point provided by the slider control.

#### Click a Filename to Load this File into DIAdem

| Control.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av25.htm language=enus -->
## TOPIC 00876: Set Point Generation with Formula Blocks

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av25.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av25.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Set Point Generation with Formula Blocks

| Set Point Generation with Formula Blocks |
| --- |

This example shows a block diagram that calculates measurement cycles from data channels. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

For an engine test stand you want to generate a rpm curve which is divided into several cycles of different duration. You want to monitor the test by visualizing the cycle number, the cycle duration, and the cycle specific rpm.

#### Solution

Two formula blocks read the duration and the rpm of a measurement cycle from the revs channel and the period channel in the Data Portal. The **Cycle End** control block sets the stopwatch to zero at the end of a measurement and counts the cycle numbers up.

The curve display shows the revs over the time. The numeric displays show the current data and the specified data for each measurement cycle.

#### Click a Filename to Load this File into DIAdem

| SetValFx.dac | Block diagram file |
| --- | --- |
| SetValFx.tdm | Data file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av26.htm language=enus -->
## TOPIC 00877: Set Point Generation with Free Linearization

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av26.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av26.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Set Point Generation with Free Linearization

| Set Point Generation with Free Linearization |
| --- |

This example shows a block diagram that uses linearization to generate set points. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to generate a set point curve that contains ramps. You want the set point curve to cover a specific time range.

#### Solution

The **Free Linearization** scaling block uses two data channels from the Data Portal as the x-channel and the y-channel for linearization. The input values are time data that correspond to the values of the x-channel. The scaling block converts the time values into the respective values of the y-channel and outputs the scaled values as set points.

#### Click a Filename to Load this File into DIAdem

| SetValSc.dac | Block diagram file |
| --- | --- |
| SetValSc.tdm | Data file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av27.htm language=enus -->
## TOPIC 00878: Manual Input

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av27.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av27.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Manual Input

| Manual Input |
| --- |

This example shows a block diagram with manual inputs. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to control the measurement manually and to simulate the signals.

#### Solution

You can use the manual inputs switch, push button, slider control, and dial to control applications manually. You also can use the manual inputs to simulate measurement signals.

#### Click a Filename to Load this File into DIAdem

| SimInp.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av28.htm language=enus -->
## TOPIC 00879: Sound Board Acquisition

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av28.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av28.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Acquiring and Displaying](../explonl/explonl_measure_overview.htm) > Sound Board Acquisition

| Sound Board Acquisition |
| --- |

This example shows a block diagram that displays an audio signal, which was acquired with the sound board, three dimensionally online. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to run a measurement using the computer sound board.

#### Solution

The **Analog Input** packet processing block acquires a sound signal, which is received by a microphone. The **Spectral Analysis** block calculates the power spectrum of the sound signal, which two oscilloscopes display as a waterfall diagram and a color/Campbell diagram.

#### Click a Filename to Load this File into DIAdem

| Soundin.dac | Block diagram file |
| --- | --- |

#### Requirements

DIAdem packet processing and as the signal source a microphone or a music player.

|  | NoteIf you do not hear any signals when you start the measurement, check your sound board configuration, your multimedia settings, and microphone connection. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av29.htm language=enus -->
## TOPIC 00880: Extreme Value Calculation

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av29.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av29.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Extreme Value Calculation

| Extreme Value Calculation |
| --- |

This example shows a block diagram that calculates the extreme values for intervals that contain a manually adjustable width. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to check the maximum and minimum extreme values of a measurement signal in a specified interval. You want to recalculate the extreme values for each interval.

#### Solution

A slider control generates measurement values. Two formula blocks determine the minimum and the maximum for an interval of the measurement values. The curve display shows the successive measurement values, minimum values, and maximum values. The **Interval Reset** control block controls the generation of a new interval and the calculation of the maximum values and the minimum values.

#### Click a Filename to Load this File into DIAdem

| Onl_Extr.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av3.htm language=enus -->
## TOPIC 00881: Data Storage in the Data Portal

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av3.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av3.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Data Storage](../explonl/explonl_datastorage_overview.htm) > Data Storage in the Data Portal

| Data Storage in the Data Portal |
| --- |

This example shows a block diagram that saves the measured data directly in the Data Portal. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to save measurement signals in channels in the DIAdem Data Portal. DIAdem panels can directly access the Data Portal to analyze data, to display data, and to archive data.

#### Solution

Three simulation blocks generate a sine signal, a random signal, and a noise signal, at a sampling rate of 100 Hz. The **Channel Storage** system block creates four channels in the default group of the Data Portal. As the reference channel the first channel **Time** contains the relative time in seconds since the start of the measurement. The next three channels contain the acquired signals.

#### Click a Filename to Load this File into DIAdem

| StoreCh.dac | Block diagram file |
| --- | --- |

#### Procedures

[Data Storage in the Data Portal](../../procdacsv/procdacsv/procdacsv_saving_data_portal.htm)

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av30.htm language=enus -->
## TOPIC 00882: Monitoring a Dynamic Set Point Range

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av30.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av30.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Monitoring a Dynamic Set Point Range

| Monitoring a Dynamic Set Point Range |
| --- |

This example shows a block diagram that checks a dynamic set point range. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to check whether a measurement signal is in a changing set point range. Overshooting and undershooting the set point range is to be indicated visually and acoustically.

#### Solution

A **Linear scaling** type scaling block uses a random signal to generate the upper and lower limit value of the set point range that the **Preview** displays. A slider control provides the measurement signal to be monitored. Two formula blocks check whether an offset copy of the set point range stays within the limit in order to enable you to keep the slider control signal within the set point range.

#### Click a Filename to Load this File into DIAdem

| Onl_Setr.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av31.htm language=enus -->
## TOPIC 00883: Sound Board Output

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av31.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av31.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Acquiring and Displaying](../explonl/explonl_measure_overview.htm) > Sound Board Output

| Sound Board Output |
| --- |

This example shows a block diagram that generates an audio signal and outputs this signal via a sound board. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to use the sound board on your computer to output a generated sound signal.

#### Solution

Two connected function generators generate a frequency-modulated sine signal. DIAdem visualizes the original sine signal in one oscilloscope and the frequency-modulated signal in a second oscilloscope. DIAdem outputs the frequency-modulated signal to the sound board.

#### Click a Filename to Load this File into DIAdem

| Soundout.dac | Block diagram file |
| --- | --- |

#### Requirement

DIAdem packet processing, a sound board compatible with Windows and a loudspeaker plugged in at the sound board output

|  | Note If you do not hear any signals when you start the measurement, check your sound board configuration, your multimedia settings, and loudspeaker connection. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av32.htm language=enus -->
## TOPIC 00884: Stopwatch

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av32.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av32.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Acquiring and Displaying](../explonl/explonl_measure_overview.htm) > Stopwatch

| Stopwatch |
| --- |

The following example displays a stopwatch block diagram. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to use the mouse to operate a stopwatch for several time measurements.

#### Solution

The **Stopwatch** block can measure time like a real stopwatch. Use the block control inputs to start, to stop, and to reset the stopwatch. The stopwatch generates a time signal from which three formula blocks calculate the minutes, the seconds, and the tenths of a second. Three gauges display the minutes, the seconds, and the tenths of a second in the graphics of a stopwatch.

#### Click a Filename to Load this File into DIAdem

| StpWatch.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av33.htm language=enus -->
## TOPIC 00885: Impulse Counting

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av33.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av33.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Acquiring and Displaying](../explonl/explonl_measure_overview.htm) > Impulse Counting

| Impulse Counting |
| --- |

The following example shows a block diagram that contains a count block which counts impulses from a control bus. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to count specific events and you want to be able to reverse the counting direction.

#### Solution

The counter counts each impulse of a push button in the range 0 to 5. The switch changes the count direction. The reset button sets the counter to its start value.

#### Click a Filename to Load this File into DIAdem

| Counter2.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av34.htm language=enus -->
## TOPIC 00886: Relay

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av34.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av34.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Packet Processing](../explonl/explonl_packageprocessing_overview.htm) > Relay

| Relay |
| --- |

The following example shows a block diagram that has a packet processing relay that alternately transmits a signal to two oscilloscopes. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to alternately display a signal in two oscilloscopes. You use a switch to select to which oscilloscope to transmit the signal.

#### Solution

The **Signal** packet block generates a triangular signal which the **Relay** packet block transmits to one of the oscilloscopes. To switch the relay manually a **Manual Input** block is connected to the relay control input.

#### Click a Filename to Load this File into DIAdem

| Pac_Rela.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av36.htm language=enus -->
## TOPIC 00887: Creating Data Sections

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av36.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av36.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Packet Processing](../explonl/explonl_packageprocessing_overview.htm) > Creating Data Sections

| Creating Data Sections |
| --- |

The following example shows a block diagram with two packet processing Ignore blocks that extract the positive and negative halfwaves from a sine signal. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to extract and to visualize certain segments from a periodic signal.

#### Solution

The **Sine** function generator generates a sine signal that the **Visual1** oscilloscope displays. The **Segment1** ignore block extracts the top halfwave and the **Segment2** ignore block extracts the bottom halfwave of the sine signal. The **Visual2** oscilloscope displays the top and bottom halfwaves.

#### Click a Filename to Load this File into DIAdem

| Pac_Segm.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av4.htm language=enus -->
## TOPIC 00888: Arithmetic Operations

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av4.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av4.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Arithmetic Operations

| Arithmetic Operations |
| --- |

The following example shows a block diagram that calculates an audible sound signal from the signal of a dial signal. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to generate an audible frequency with a dial and output the sound to the computer loudspeakers.

#### Solution

The dial generates a signal that the **Free Formula** block converts into an audible sound signal. In order to control the signal output on the computer loudspeakers, the formula is multiplied in the **Free Formula** block by the push button signal 0 or 1.

#### Click a Filename to Load this File into DIAdem

| Arith_op.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av40.htm language=enus -->
## TOPIC 00889: Signal Filtering

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av40.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av40.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Packet Processing](../explonl/explonl_packageprocessing_overview.htm) > Signal Filtering

| Signal Filtering |
| --- |

This example shows a packet processing block diagram that uses two lowpass filters to suppress the high-frequency noises of a noisy signal. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to remove the high-frequency noises from a sine signal and visualize the result with the original signal.

#### Solution

A **Generator** packet block generates a noise signal and another generator packet block generates a sine signal that the **Formula Parser** packet block summates. You can modulate the sine signal with the slider control.

To demonstrate the effect of different filters the noisy sine signal is filtered in two **Digital Filter** blocks with different lowpass filters and a limit frequency of 10 Hz. Both blocks use the IIR filter method, one with the Butterworth filter and one with the Chebyshev filter.

The oscilloscope displays the unfiltered signal and the filtered signals. The two filtered signals display different phase offsets to the original signal and behave differently in signal frequencies over the limit frequency.

#### Click a Filename to Load this File into DIAdem

| Pac_Filt.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av41.htm language=enus -->
## TOPIC 00890: Signal Analysis

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av41.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av41.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Packet Processing](../explonl/explonl_packageprocessing_overview.htm) > Signal Analysis

| Signal Analysis |
| --- |

This example shows a packet processing block diagram that calculates and visualizes online a FFT with different digital filters for a signal. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to show the impact of different digital filters on a fast Fourier transform (FFT).

#### Solution

Two signals (sine and triangle) with different changeable frequencies are added and displayed in the time domain and the frequency domain. The cumulative signal is filtered digitally and also displayed in the time domain and the frequency domain.

#### Click a Filename to Load this File into DIAdem

| Pac_Fft.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av43.htm language=enus -->
## TOPIC 00891: Triggered Data Storage

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av43.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av43.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Data Storage](../explonl/explonl_datastorage_overview.htm) > Triggered Data Storage

| Triggered Data Storage |
| --- |

This example shows a block diagram that saves event-related data. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to save an event-related data signal. You want to save only values that change quickly and of which the difference from the previous value is greater than 1. A light is to indicate when the trigger event occurs.

#### Solution

A slider control simulates a measurement signal. The **Signal Alteration** control block monitors the measurement signal. If the difference of the current measurement value to the previous value is greater than 1, the signal change outputs a trigger impulse to the **Storage** system block. The storage block writes the measurement values into a new channel in the Data Portal until the number of values to save is reached. The signal lamp displays the start of the storage. The monoflop block extends the illumination period of the signal lamp to 0.5 seconds.

#### Click a Filename to Load this File into DIAdem

| Deltasa1.dac | Block diagram file |
| --- | --- |

#### Procedures

[Data Storage in the Data Portal](../../procdacsv/procdacsv/procdacsv_saving_data_portal.htm)

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av44.htm language=enus -->
## TOPIC 00892: Displaying Alarms in a Table

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av44.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av44.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Displaying Alarms in a Table

| Displaying Alarms in a Table |
| --- |

This example shows a block diagram that uses the alarm system to monitor whether a data signal exceeds limit values and if so, displays this in an alarm table. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to monitor a measurement signal for the limit values -8, -5, 0, 5, 8. If the signal overshoots or undershoots these limits, an alarm is to be generated as a text message in a table.

#### Solution

The alarm system processes data packets not single values. Therefore the **Pack** packet block combines the values of the slider control to data packets and forwards these data packets to the alarm generator. The alarm generator generates alarm messages if the limit values are overshot or undershot. The **Alarm Table** alarm block formats and displays these messages.

#### Click a Filename to Load this File into DIAdem

| Alarm1.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av45.htm language=enus -->
## TOPIC 00893: Displaying Alarm Status

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av45.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av45.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Displaying Alarm Status

| Displaying Alarm Status |
| --- |

This example shows a block diagram that displays alarms in an alarm table with a status display. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to monitor a measurement signal for the limit values -8, -5, 0, 5, 8. You want to visualize the status of the alarms in an alarm table with a five stage status display.

#### Solution

You add a status display to the example [Displaying Alarms in a Table](../explonl/explonl_dac_av44.htm). The alarm generator outputs the alarm states 0 (OFF, no alarm) or 1 (ON, alarm) as multi-channel data packets at the status output S. To display the five-channel data packet and the status display the **Unpack** packet block separates the five-channel data packet into five buses.

#### Click a Filename to Load this File into DIAdem

| Alarm2.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av46.htm language=enus -->
## TOPIC 00894: Confirming Alarms

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av46.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av46.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Confirming Alarms

| Confirming Alarms |
| --- |

This example shows a block diagram that does not delete alarms in the alarm table until you confirm manually. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to confirm alarms with a push button.

#### Solution

You add a confirmation button to the example [Alarm Status Display](../explonl/explonl_dac_av45.htm). A text bus connects the alarm table to the input T of the alarm generator. This back coupling of the alarm table to the alarm generator enables the user to confirm alarms that occur.

The confirmation adds two alarm status types to the S status output of the alarm generator:

- 0 (OFF confirmed = Alarm no longer exists and was confirmed)
- 1 (OFF = Alarm no longer exists and has not been confirmed yet)
- 2 (ON confirmed = Alarm still exists and has been confirmed)
- 3 (ON = Alarm still exists and has not been confirmed yet)

The four types of alarm status appear in the alarm table with different background colors. The **Push button** control block is connected to the reset control input of the alarm table in order to confirm selected alarms during a measurement.

#### Click a Filename to Load this File into DIAdem

| Alarm3.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av47.htm language=enus -->
## TOPIC 00895: Extended Alarm Status Display

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av47.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av47.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Extended Alarm Status Display

| Extended Alarm Status Display |
| --- |

This example shows a block diagram that displays alarms from different aggregates. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to assign alarms to the aggregate where errors occurred. You want to monitor a pump, a transporter, and a filter.

#### Solution

The example [Confirming Alarms](../explonl/explonl_dac_av46.htm) is extended in order to monitor three aggregates. If the alarms are arranged in alarm groups, the area in which the error occurred can be identified faster. The alarm table also has a column for alarm groups. For better identification the alarm groups display graphic symbols.

#### Click a Filename to Load this File into DIAdem

| Alarm4.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av48.htm language=enus -->
## TOPIC 00896: Displaying Alarms as Text

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av48.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av48.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Displaying Alarms as Text

| Displaying Alarms as Text |
| --- |

This example shows a block diagram that records alarms. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to save all occurring alarms and events in a logfile. You want to view the alarm history during a measurement.

#### Solution

A text display for the alarm history is added to the example [Confirming Alarms](../explonl/explonl_dac_av46.htm). The alarm table reflects the current status of the alarm events and confirms alarm messages. To create an alarm history, the **Alarm => Text** alarm block converts alarm messages into text. You can use filters in order to forward only certain alarm information as text. The **Dynamic Text Display** alarm block displays the alarm messages formatted and in chronological order.

#### Click a Filename to Load this File into DIAdem

| Alarm5.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av49.htm language=enus -->
## TOPIC 00897: Text Input for Commenting Alarms

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av49.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av49.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Text Input for Commenting Alarms

| Text Input for Commenting Alarms |
| --- |

This example shows a block diagram in which you can comment alarms during a measurement. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to comment occurring alarms during a measurement, for example, to identify alarms that occur due to operating errors.

#### Solution

A text entry is added to the example [Displaying Alarms as Text](../explonl/explonl_dac_av48.htm).

The **Text Input** alarm block enables the user to input comments during a measurement. The button connected to the control input at the input transmission controls the transmission of comments and labels the comments with a time stamp. The **Multiplexer** packet block combines comments and alarm messages and transmits them to the alarm block **Dynamic Text Display**.

#### Click a Filename to Load this File into DIAdem

| Alarm6.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av5.htm language=enus -->
## TOPIC 00898: Condition Types

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av5.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av5.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Condition Types

| Condition Types |
| --- |

This example shows a block diagram that uses different condition types. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to check a slider control for three conditions:

1. You want the valid value range to be between 3 and 7 .
2. You want the value 5 to be exceeded with a positive slope.
3. You want the signal change to exceed 0.5 per second in positive or negative direction.

#### Solution

The **Window** control block checks the value range and outputs a control signal when the slider is in the valid range. The **Slope** control block checks the value 5 and outputs a control signal when the slider exceeds the value 5 in ascending direction. The **Signal Alteration** control block monitors the value changes of the slider control and outputs a signal if the value change is greater than 0.5 in one second.

#### Click a Filename to Load this File into DIAdem

| Condit.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av50.htm language=enus -->
## TOPIC 00899: Alarm-Related Visualization

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av50.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av50.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Alarm-Related Visualization

| Alarm-Related Visualization |
| --- |

This example shows a block diagram that displays alarms in relation to the priority. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want the alarm table to appear only for alarms with the highest **Error** priority. You want the alarm table to stay visible until all alarms have the status 0 (non existent and confirmed). You also want to display and to delete error alarms separately from the alarms **Note** and **Warning**.

#### Solution

You add filter criteria to the example [Displaying Alarms as Text](../explonl/explonl_dac_av48.htm), for alarm-related visualization.

The **Error** formula block analyzes the alarm status of the alarm generator and uses control blocks to activate the visualization of the alarm table only if errors alarms are non-confirmed. The two **Alarm => Text** type alarm blocks convert the alarms the alarm generator outputs into formatted text messages and filter the alarm messages so that only certain alarm information is transmitted as text.

The **AL FMT1** alarm block only transfers alarm messages with the priorities **Note** and **Warning**. The **AL FMT2** alarm block only transfers alarms with the priority **error** for text display.

#### Click a Filename to Load this File into DIAdem

| Alarm7.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av51.htm language=enus -->
## TOPIC 00900: Filtering Alarm Messages with Format Blocks

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av51.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av51.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Alarm System](../explonl/explonl_alarmsystem_overview.htm) > Filtering Alarm Messages with Format Blocks

| Filtering Alarm Messages with Format Blocks |
| --- |

This example shows a block diagram that labels alarms with the priority **Error**. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to display only specific alarm events and you want to save the events in a logfile. You also want to count and display **Error** priority alarm events.

#### Solution

In the example [Displaying Alarms as Text](../explonl/explonl_dac_av48.htm), the alarm table is replaced by a text display to display only specific alarms.

Three **Alarm => Text** alarm blocks convert the alarms the alarm generator outputs into formatted text messages and filter the alarm messages so that only certain alarm information is transmitted as text. The **AL FMT1** alarm block forwards the start status, the **AL FMT2** alarm block forwards only the **Warning** priority alarm messages, and the **AL FMT3** alarm block forwards only **Error** priority alarms for text display and storage to a logfile. The **AL FMT3** alarm block simultaneously counts all the alarms that have the priority **Error**.

#### Click a Filename to Load this File into DIAdem

| Alarm8.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av6.htm language=enus -->
## TOPIC 00901: Boolean Operations

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av6.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av6.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Signal Processing](../explonl/explonl_signalprocessing_overview.htm) > Boolean Operations

| Boolean Operations |
| --- |

This example shows a block diagram that executes Boolean operations. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to use control blocks to check several conditions of in various signals. All conditions are met if

1. the slider control AND the dial are in the value range between 6 and 8 AND
2. the switch OR the push button are used.

#### Solution

The **Window** control block monitors the signals of the four input instruments. If the input signals are in the specified value range, the window block outputs a control signal. The formula block connects the input signals with the Boolean operators AND and OR. The formula block and a NOT operator control the display of two graphics to specify whether a condition is true (a) or not true (b).

#### Click a Filename to Load this File into DIAdem

| Bool_op.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av7.htm language=enus -->
## TOPIC 00902: Automatic Dynamic Visualization

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av7.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av7.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Automatic Dynamic Visualization

| Automatic Dynamic Visualization |
| --- |

This example shows a block diagram that switches the visualization automatically after five seconds. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

During the measurement, you want to switch automatically among various types of signal display.

#### Solution

Two control blocks alternately disable and enable the gauge and bars display instruments. The **Time** block generates the toggle impulse that the **Switch** block transmits alternately to the start and stop control inputs of the display instruments.

#### Click a Filename to Load this File into DIAdem

| DynVis_a.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av8.htm language=enus -->
## TOPIC 00903: Manual Dynamic Visualization

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av8.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av8.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Manual Dynamic Visualization

| Manual Dynamic Visualization |
| --- |

This example shows a block diagram in which you can switch the visualization manually. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

During the measurement, you want to switch manually among various signal display types.

#### Solution

Two **Push Button** control blocks control the display instruments Gauge and Bars. If you enable the gauge display, DIAdem disables the bar display and vice versa.

#### Click a Filename to Load this File into DIAdem

| DynVis_M.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_av9.htm language=enus -->
## TOPIC 00904: Signal Acquisition

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_av9.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_av9.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Acquiring and Displaying](../explonl/explonl_measure_overview.htm) > Signal Acquisition

| Signal Acquisition |
| --- |

This example shows a block diagram that simulates and visualizes signals from different sources. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to simulate and to visualize signals from various sources.

#### Solution

To visualize data, the block diagram reads data from the Data Portal. The **Random** simulation block generates a random signal. You can use the dial instrument to generate a visualization signal.

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores and block diagrams. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Acquisit.dac | Block diagram file |
| --- | --- |
| DAC_Expl.tdm | Data file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_dac_video.htm language=enus -->
## TOPIC 00905: Recording Video and Measurement Data

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_dac_video.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_dac_video.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Version 2015](../../exploff/examples/examples_new2017_overview.htm) | [Visualizing](../explonl/explonl_visualize_overview.htm)) > Recording Video and Measurement Data

| Recording Video and Measurement Data |
| --- |

This example shows a block diagram which records measurement data together with a video. The example displays the video signal during the measurement. After the measurement, DIAdem VIEW plays back the recorded video, and displays the measurement data in the 2D display and the channel table in parallel.

If no camera is connected to your computer, DIAdem displays a standard video.

Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

Record several measurement signals with a video.

#### Solution

The **Video** function block allows the storage of video signals. You need to connect a camera to the USB interface. The Video block saves the video signals synchronously with all other measurement signals defined in the block diagram from the start of the measurement. You can find more information on the Video block [here](../../genvis/genvis/video_infos.htm).

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores and block diagrams. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Video_DAC_VIEW.vbs | Script file |
| --- | --- |
| Video_DAC_VIEW.dac | Block diagram file |
| Video_DAC_VIEW.tdv | Layout file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_datastorage_overview.htm language=enus -->
## TOPIC 00906: Storing Data

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_datastorage_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_datastorage_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > Storing Data

| Storing Data |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help describe how you save measurement data in files or in the Data Portal.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_ecu-dialog.htm language=enus -->
## TOPIC 00907: Configuring an ECU with a Dialog Box During a Measurement

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_ecu-dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_ecu-dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Acquiring and Displaying](../explonl/explonl_measure_overview.htm) | [Version 2012](../../exploff/examples/examples_new2012_overview.htm)) > Configuring an ECU with a Dialog Box During a Measurement

| Configuring an ECU with a Dialog Box During a Measurement |
| --- |

This example shows a block diagram which is executing a measurement with the NI ECU Measurement and Calibration Toolkit. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

DIAdem is to display parameters of an Engine Control Unit and allow changes to the characteristics during the measurement.

#### Solution

The ECU driver opens a user dialog box. You can use the controls in this user dialog box during the measurement to make entries and to evaluate different settings for the Engine Control Unit (ECU) driver. The user dialog box connects with the ECU, reads data from several ECU characteristics, and transfers the settings from the dialog box to the ECU.

|  | Note The example requires the installation of the NI ECU Measurement and Calibration Toolkit. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| ECU Dialog.DAC | Block diagram file |
| --- | --- |
| ECU Dialog.SUD | User Dialog Box |
| ECU Dialog.VBS | Script file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_measautomate_overview.htm language=enus -->
## TOPIC 00908: Measuring, Testing, Automating, and Visualizing

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_measautomate_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_measautomate_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Measuring, Testing, Automating, and Visualizing

| Measuring, Testing, Automating, and Visualizing |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show you how to use block diagrams for measurements and for open and closed loop control in the [DIAdem DAC](../../gendacsv/dac_general/dac_allgemein.htm) panel. You see the differences between [Single point processing](../../gendacpp/dac_packet_general/hidx_allgemeines.htm) and [Packet processing](../../gendacpp/dac_packet_general/hidx_allgemeines.htm).

The examples also demonstrate how you use the [DIAdem VISUAL](../../genvis/genvis/visual_general.htm) panel to visualize measured data or data that is calculated online, and how to control block diagrams using manual instruments such as switches or slider controls.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_measure_overview.htm language=enus -->
## TOPIC 00909: Acquiring and Displaying

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_measure_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_measure_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > Acquiring and Displaying

| Acquiring and Displaying |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show you how to use the sound board to measure and to display sound signals. You also see how to measure simulated random signals, how to count the impulses of a signal, and how to execute time measurements.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_packageprocessing_overview.htm language=enus -->
## TOPIC 00910: Packet Processing

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_packageprocessing_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_packageprocessing_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > Packet Processing

| Packet Processing |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show you how to work with [Packet Processing](../../gendacpp/dac_packet_general/hidx_allgemeines.htm) in DIAdem DAC. For example, you learn how to determine statistical values from data blocks, how to filter frequencies, and how to anaylze signals.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_processing_overview.htm language=enus -->
## TOPIC 00911: Sequence Control

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_processing_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_processing_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > Sequence Control

| Sequence Control |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show you how to use block diagrams to control parallel or sequential measurements.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_scaling_overview.htm language=enus -->
## TOPIC 00912: Scaling and Linearizing

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_scaling_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_scaling_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > Scaling and Linearizing

| Scaling and Linearizing |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show you various methods for scaling and linearizing measurement data.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_script_autoscaling1.htm language=enus -->
## TOPIC 00913: Comparing Automatic Scalings

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_script_autoscaling1.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_script_autoscaling1.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Scaling and Linearizing](../explonl/explonl_scaling_overview.htm) | [Version 2012](../../exploff/examples/examples_new2012_overview.htm) | [Visualizing](../explonl/explonl_visualize_overview.htm)) > Comparing Automatic Scalings

| Comparing Automatic Scalings |
| --- |

This example shows the various automatic y-scalings of the curve display, spike display, wiper display, and recorder display. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

The curve displays are to show how the y-axis can adapt to the measurement values. Manual scaling with a fixed value range is the reference.

#### Solution

The simulation blocks **Random** and **Generator** generate a signal. The **Curve Display** blocks display this signal only differently in the y-scaling: **Automatic** (curve 1) scales the y-axis continuously according to the displayed measurement values. **Automatic with peak hold** (Curve 2) scales the y-axis continuously according to the smallest and the largest measurement values of the complete measurement. **Manual** (Curve 3) does not scale and displays a fixed value range. **Automatic with minimum range** (Curve 4) scales the y-axis according to the displayed measurement values without undershooting the predefined range width. **Automatic with Fixed Range** (Curve 5) moves the value range of the y-axis in accordance with the displayed measurement values and keeps the range constant.

#### Click a Filename to Load this File into DIAdem

| AutoScaling_1.DAC | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_script_autoscaling2.htm language=enus -->
## TOPIC 00914: Scaling Several Curves Automatically

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_script_autoscaling2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_script_autoscaling2.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Scaling and Linearizing](../explonl/explonl_scaling_overview.htm) | [Version 2012](../../exploff/examples/examples_new2012_overview.htm) | [Visualizing](../explonl/explonl_visualize_overview.htm)) > Scaling Several Curves Automatically

| Scaling Several Curves Automatically |
| --- |

This example shows the various y-scalings of the curve display, spike display, wiper display, and recorder display for several signals in one axis system. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

Several signals are to be automatically scaled in one curve display.

#### Solution

The simulation blocks **Random** and **Generator** generate several signals which are all displayed in a **Curve display**. If several curves are displayed in one axis system, the automatic scaling aligns each y-axis separately. The top curve display uses the y-scaling **Automatic with peak hold** and scales each y-axis continuously in accordance with the smallest and the greatest measurement value of the associated signal of the entire measurement. The bottom curve display uses the y-scaling **Automatic** and scales every y-axis continuously in accordance with the displayed measurement values of the associated signal.

#### Click a Filename to Load this File into DIAdem

| AutoScaling_2.DAC | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_script_av1.htm language=enus -->
## TOPIC 00915: Test Application: From Configuration to Test Log

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_script_av1.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_script_av1.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Automate](../explonl/explonl_automating_overview.htm) > Test Application: From Configuration to Test Log

| Test Application: From Configuration to Test Log |
| --- |

This example shows how you configure, execute, evaluate, and document a measurement with a script.

Start example

#### Scenario

You want to start, evaluate, and document a measurement automatically. Before the measurement starts enter the name of the tester, the test number, the trigger threshold, and the pre-trigger range, for the test logfile.

#### Solution

A script opens a dialog box where you enter the required details for the measurement. During input, the dialog box checks whether the entries are valid: The trigger threshold must be in the range between -8 and 8 and the pre-trigger range must be between 0 and 200 (integer).

The script loads the block diagram and configures the trigger threshold and the pretrigger range as specified. Then the script starts the measurement and saves the measurement data in the Data Portal. When the number of values to be saved is reached, the storage block finishes the measurement.

The script smooths the measurement values and executes a peak search. After the evaluation the script loads a report layout and displays the measured and analyzed data in a test log.

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores, layouts, block diagrams, and scripts. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| SudExample_2.sud | Dialog box file |
| --- | --- |
| Sud_DACPara | Dialog box |
| Sud_DACPara.vbs | Script file |
| Sud_DACPara.tdr | Layout file |
| Sud_DACPara.dac | Block diagram file |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_script_av2.htm language=enus -->
## TOPIC 00916: Serial Measurements: Automatic Generation of Filenames for Data Storage

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_script_av2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_script_av2.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Automate](../explonl/explonl_automating_overview.htm) > Serial Measurements: Automatic Generation of Filenames for Data Storage

| Serial Measurements: Automatic Generation of Filenames for Data Storage |
| --- |

This example shows how you start and evaluate a serial measurement with a script.

Start example

#### Scenario

You want to execute three successive measurements daily and save the measurement values in separate files. Then you want to document the three measurements in a report.

#### Solution

A script loads a block diagram and starts three measurements in succession. DIAdem saves the measurement values in data files of which the name exists of the date and time of the measurement and a specific prefix.

The script then loads these three data files and creates a report.

|  | Note Specify the user commands that DIAdem executes before and after a measurement under Settings»Block Diagram Parameters. |
| --- | --- |

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores, layouts, block diagrams, and scripts. |
| --- | --- |

|  | Note In this example DIAdem registers the user command UserCmdDAC.vbs. If you do not save the program settings when you exit DIAdem, the user commands contained in the program settings are not available at the restart of DIAdem until you restart the example. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Auto_FileName.vbs | Script file |
| --- | --- |
| Auto_FileName.tdr | Layout file |
| Auto_FileName.dac | Block diagram file |

#### Procedures

[Evaluating a Series of Files](../../procscript/procscript/procscript_serial_evaluation.htm)

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_signalprocessing_overview.htm language=enus -->
## TOPIC 00917: Signal Processing

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_signalprocessing_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_signalprocessing_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > Signal Processing

| Signal Processing |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show you how to process acquired signals mathematically with arithmetic and Boolean operators. You also learn how to use conditions in block diagrams, to generate and monitor set points, and to control signals according to the set points.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/explonl_visualize_overview.htm language=enus -->
## TOPIC 00918: Visualizing

- bundle_id: `diadem`
- source_path: `explonl/explonl/explonl_visualize_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/explonl_visualize_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > Visualizing

| Visualizing |
| --- |

The subordinate topics contained in the tree on the contents tab of the Help show you how to use [DIAdem VISUAL](../../genvis/genvis/visual_general.htm) to visualize measurement data, and how to use manual instruments to control visualization.

<!--NI_TOPIC bundle=diadem path=explonl/explonl/exponl_dacdataportaloldstyle.htm language=enus -->
## TOPIC 00919: Switching the Data Portal Automatically On/Off in DIAdem DAC

- bundle_id: `diadem`
- source_path: `explonl/explonl/exponl_dacdataportaloldstyle.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/exponl_dacdataportaloldstyle.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Automate](../explonl/explonl_automating_overview.htm) > Switching the Data Portal Automatically On/Off in DIAdem DAC

| Switching the Data Portal Automatically On/Off in DIAdem DAC |
| --- |

This example shows how you can switch off the Data Portal in DIAdem DAC, while leaving it unchanged in all other panels. After the example has run, the Data Portal behaves the same as in DIAdem 10.2 or earlier.

When the example starts, DIAdem registers a user command and assigns this command to the [OnPanelChanged](../../varoff/onpanelchanged.htm) variable. Simultaneously the example saves whether the Data Portal is visible in a global variable. The user command checks which panel opens, and hides the Data Portal for DIAdem DAC.

Start example

|  | Note Click here to restore the default behavior of the Data Portal. DIAdem sets the OnPanelChanged variable to the default value. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| DACDataPortalOldStyle_Init.VBS | Script file |
| --- | --- |
| DACDataPortalOldStyle.VBS | Script file as user command |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/exponl_example_dac.htm language=enus -->
## TOPIC 00920: Numeric Display with Scroll Bar and Bar Display

- bundle_id: `diadem`
- source_path: `explonl/explonl/exponl_example_dac.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/exponl_example_dac.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Numeric Display with Scroll Bar and Bar Display

| Numeric Display with Scroll Bar and Bar Display |
| --- |

This example shows a block diagram which displays many measurement channels clearly laid out as bars and digits. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to display a large number of measurement channels as bars and digits.

#### Solution

The bars and digits are displayed with a fixed font size. If the number of channels exceeds the display area, DIAdem displays a slider that you can use to scroll the displays.

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores and block diagrams. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Example_dac.dac | Block diagram file |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/exponl_interfaces_ab1.htm language=enus -->
## TOPIC 00921: Transferring Measurement Reports to Word via OLE

- bundle_id: `diadem`
- source_path: `explonl/explonl/exponl_interfaces_ab1.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/exponl_interfaces_ab1.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Automate](../explonl/explonl_automating_overview.htm) > Transferring Measurement Reports to Word via OLE

| Transferring Measurement Reports to Word via OLE |
| --- |

This example shows how to use a script to transfer a measurement report to Microsoft Word via OLE in order to create a measurement log.

Start example

#### Scenario

You want to start, evaluate, and document a measurement automatically. You also want to create a measurement report with Microsoft Word.

#### Solution

This example contains the following work steps:

1. Input dialog boxes where the user specifies the measurement parameters.
2. Loading a reference characteristic curve.
3. Running a measurement. Move the slider to simulate measurement values.
4. Displaying measurement results in a report.
5. Mathematical evaluation of the measurement.
6. Automatically creating a measurement log in Microsoft Word.

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores, layouts, block diagrams, and scripts. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Wrd_OLE_DAC.vbs | Script file |
| --- | --- |
| Wrd_OLE.sud | Dialog box file |
| Wrd_Demo.tdr | Layout file |
| Wrd_Ref.tdm | Data file |
| Wrd_MeaU.dac | Block diagram file |
| Wrd_MeaI.dac | Block diagram file |
| Wrd_Ole.dot | Word document template for the report |

|  | Note For the example you must install MS Word version 8 or later. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=explonl/explonl/exponl_num_tab_extended.htm language=enus -->
## TOPIC 00922: Numeric and Tabular Display

- bundle_id: `diadem`
- source_path: `explonl/explonl/exponl_num_tab_extended.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/explonl/explonl/exponl_num_tab_extended.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Measuring, Testing, Automating, and Visualizing](../explonl/explonl_measautomate_overview.htm) > [Visualizing](../explonl/explonl_visualize_overview.htm) > Numeric and Tabular Display

| Numeric and Tabular Display |
| --- |

This example shows a block diagram which displays many measurement channels clearly laid out as numerals and tables. DIAdem also calculates in a script driver characteristic statistical values and displays these values in the text field. Press <Esc> or click **Stop Measurement** on the toolbar to cancel the measurement.

Start example

#### Scenario

You want to display a large number of measurement channels as numbers and in tables.

#### Solution

You use numeric and tabular display and a fixed font size. If the number of channels exceeds the display area, DIAdem displays a slider that you can use to scroll the displays.

|  | Note When this example starts, DIAdem loads example files and overwrites current data stores and block diagrams. |
| --- | --- |

#### Click a Filename to Load this File into DIAdem

| Num_Tab_Extended.Dac | Block diagram file |
| --- | --- |
| PeakHold_Max.vbs | Script file for the script driver |
| PeakHold_Min.vbs | Script file for the script driver |

<!--NI_TOPIC bundle=diadem path=filetagging/filetagging_overview.htm language=enus -->
## TOPIC 00923: Document Properties

- bundle_id: `diadem`
- source_path: `filetagging/filetagging_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/filetagging_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Document Properties

Document Properties

The subordinate topics contained in the tree on the contents tab of the Help describe the object-oriented script interface for accessing meta properties of a document. The topics provide information about all objects, collections, methods, properties, and events, and examples that demonstrate how to use the interface.

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_add_idocumentproperties.htm language=enus -->
## TOPIC 00924: Method: Add for DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_add_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_add_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Add for DocumentProperties <Data>

Method: Add for DocumentProperties <Data>

Adds a custom property of a document. Custom properties are user-defined meta properties from the top level of a document. You can read, create, edit, and delete custom properties. You can only read the other meta properties of a document and edit their values. After saving the document with the [Save](../methods/diacmpnt_method_save_idiademdocument.htm) method, you can search for new custom properties.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Set oDocumentProperty = Object.Add(Name, Value, [DataType])
```

| Object | DocumentProperties <Data>Object with this method |  |
| --- | --- | --- |
| Name | StringSpecifies the name of the meta property. |  |
| Value | VariantSpecifies the value of the meta property. |  |
| [DataType] | Enumeration with read access and the following selection terms: 3DataTypeDocumentInt32 32-bit integer values 10DataTypeDocumentFloat64 64-bit real values 23DataTypeDocumentString Text 30DataTypeDocumentDate Time values |  |
| 3 | DataTypeDocumentInt32 | 32-bit integer values |
| 10 | DataTypeDocumentFloat64 | 64-bit real values |
| 23 | DataTypeDocumentString | Text |
| 30 | DataTypeDocumentDate | Time values |
| oDocumentProperty | DocumentProperty <Data>Returned object |  |

The following example checks whether you opened the PDF document in read and write mode. If DIAdem can write in the document, the example adds a new meta property, saves the document, and then displays the names and values of all meta properties of the document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
If Not(oMyDocument.ReadOnly) Then
  Call oMyDocument.Properties.Add("Modified","Yes", DataTypeDocumentString)
  Call oMyDocument.Save()
End If
sOut = "File path: " & oMyDocument.FilePath & VBCrLf
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
if not(oMyDocument.ReadOnly) : 
    oMyDocument.Properties.Add("Modified","Yes", dd.DataTypeDocumentString) 
    oMyDocument.Save() 
sOut = "File path: " + oMyDocument.FilePath + "\r\n" 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_addproperties_idocumentproperties.htm language=enus -->
## TOPIC 00925: Method: AddProperties for DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_addproperties_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_addproperties_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: AddProperties for DocumentProperties <Data>

Method: AddProperties for DocumentProperties <Data>

Adds a copy of the property from the top level of a document. The names of the new meta properties correspond to the names of the copied properties plus a prefix.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.AddProperties(Properties, Prefix)
```

| Object | DocumentProperties <Data>Object with this method |
| --- | --- |
| Properties | PropertiesSpecifies which properties to copy. |
| Prefix | VariantName prefix of the copied properties. |

The following example adds the properties of the first channel group of the loaded data to the meta properties of a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call oMyDocument.Properties.AddProperties(Data.Root.ChannelGroups(1).Channels(1).Properties,"Example~")
sOut = sOut & "==After adding properties==" & VBCrLf
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
oMyDocument.Properties.AddProperties(dd.Data.Root.ChannelGroups(1).Channels(1).Properties,"Example~") 
sOut = sOut + "==After adding properties==" + "\r\n" 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_exists_idocumentnamespaces.htm language=enus -->
## TOPIC 00926: Method: Exists for DocumentNamespaces <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_exists_idocumentnamespaces.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_exists_idocumentnamespaces.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Exists for DocumentNamespaces <Data>

Method: Exists for DocumentNamespaces <Data>

Specifies whether a namespace of a document already exists. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
bExists = Object.Exists(Name)
```

| Object | DocumentNamespaces <Data>Object with this method |
| --- | --- |
| Name | StringSpecifies the name of the namespace. |
| bExists | BooleanSpecifies whether the namespace with the specified name already exists (TRUE) or not (FALSE). |

The following example checks a PDF document for a specific namespace and displays the name of the namespace.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, sNameSpace, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
sNameSpace = "http://ns.adobe.com/xap/1.0/mm/"
If oMyDocument.Namespaces.Exists(sNameSpace) Then 
  sOut = sOut & "Namespace exists: " & oMyDocument.Namespaces(sNameSpace).Name
End If
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
sNameSpace = "http://ns.adobe.com/xap/1.0/mm/" 
if oMyDocument.Namespaces.Exists(sNameSpace) : 
    sOut = sOut + "Namespace exists: " + oMyDocument.Namespaces(sNameSpace).Name 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_exists_idocumentproperties.htm language=enus -->
## TOPIC 00927: Method: Exists for DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_exists_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_exists_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Exists for DocumentProperties <Data>

Method: Exists for DocumentProperties <Data>

Checks whether a property with a specific name already exists in a document. You can read, create, edit, and delete custom properties. You can only read the other meta properties of a document and edit their values.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
bExists = Object.Exists(Name)
```

| Object | DocumentProperties <Data>Object with this method |
| --- | --- |
| Name | StringSpecifies the name of the custom property. |
| bExists | BooleanSpecifies whether the custom property with the specified name already exists (TRUE) or not (FALSE). |

The following example checks a PDF for the custom property copyright and then deletes it.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, oMyProperties, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf",False, eDocumentTypeAuto)
Set oMyProperties = oMyDocument.Properties
For each oMyProperty in oMyProperties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
sOut = sOut & VBCrLf & "==After removing custom property==" & VBCrLf
If oMyProperties.Exists("copyright") Then
  Call oMyDocument.Properties.Remove("copyright")
End If
For each oMyProperty in oMyProperties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf",False, dd.eDocumentTypeAuto) 
oMyProperties = oMyDocument.Properties 
for oMyProperty in oMyProperties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
sOut = sOut + "\r\n" + "==After removing custom property==" + "\r\n" 
if oMyProperties.Exists("copyright") : 
    oMyDocument.Properties.Remove("copyright") 
for oMyProperty in oMyProperties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_exists_idocumentreadonlyproperties.htm language=enus -->
## TOPIC 00928: Method: Exists for DocumentReadOnlyProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_exists_idocumentreadonlyproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_exists_idocumentreadonlyproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Exists for DocumentReadOnlyProperties <Data>

Method: Exists for DocumentReadOnlyProperties <Data>

Checks whether a meta property already exists in a specific namespace of a document. The meta properties in a specific namespace are read-only. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
bExists = Object.Exists(Name)
```

| Object | DocumentReadOnlyProperties <Data>Object with this method |
| --- | --- |
| Name | StringSpecifies the name of the meta property in a specific namespace. |
| bExists | BooleanSpecifies whether the meta property with the specified name already exists in a specific namespace (TRUE) or not (FALSE). |

The following example checks a PDF document for the custom property Copyright in a namespace and displays the name of the namespace and the name and the value of the meta property:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  If oMyNameSpaces.Properties.Exists("Copyright") then
    Set oMyProperty = oMyNameSpaces.Properties("Copyright")
    sOut = sOut & "Namespace: " & oMyNameSpaces.Name & VBCrLf
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  End If
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    if oMyNameSpaces.Properties.Exists("Copyright") : 
        oMyProperty = oMyNameSpaces.Properties("Copyright") 
        sOut = sOut + "Namespace: " + oMyNameSpaces.Name + "\r\n" 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_item_idocumentnamespaces.htm language=enus -->
## TOPIC 00929: Method: Item for DocumentNamespaces <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_item_idocumentnamespaces.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_item_idocumentnamespaces.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Item for DocumentNamespaces <Data>

Method: Item for DocumentNamespaces <Data>

Returns a namespace of a document. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Set oDocumentNamespace = Object.Item(NameOrIndex)
```

| Object | DocumentNamespaces <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the namespace. |
| oDocumentNamespace | DocumentNamespace <Data>Returned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example displays the names of the namespaces for a PDF document.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, iCount
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For iCount = 1 To oMyDocument.Namespaces.Count
  sOut = sOut & "Namespace: " & oMyDocument.Namespaces(iCount).Name & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for iCount in range( 1, oMyDocument.Namespaces.Count + 1): 
    sOut = sOut + "Namespace: " + oMyDocument.Namespaces(iCount).Name + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_item_idocumentproperties.htm language=enus -->
## TOPIC 00930: Method: Item for DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_item_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_item_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Item for DocumentProperties <Data>

Method: Item for DocumentProperties <Data>

Returns a changeable meta property that is not assigned to a namespace, from the top level of a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Set oDocumentProperty = Object.Item(NameOrIndex)
```

| Object | DocumentProperties <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the custom property. |
| oDocumentProperty | DocumentProperty <Data>Returned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example displays the names and values of the meta properties for a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, iCount, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For iCount = 1 to oMyDocument.Properties.Count
  sOut = sOut & "Name: " & oMyDocument.Properties(iCount).Name & ", Value: " & oMyDocument.Properties(iCount).Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for iCount in range( 1, oMyDocument.Properties.Count + 1): 
    sOut = sOut + "Name: " + oMyDocument.Properties(iCount).Name + ", Value: " + oMyDocument.Properties(iCount).Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_item_idocumentreadonlyproperties.htm language=enus -->
## TOPIC 00931: Method: Item for DocumentReadOnlyProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_item_idocumentreadonlyproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_item_idocumentreadonlyproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Item for DocumentReadOnlyProperties <Data>

Method: Item for DocumentReadOnlyProperties <Data>

Returns a meta property in a specific namespace of a document. The meta properties in a specific namespace are read-only. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Set oDocumentProperty = Object.Item(NameOrIndex)
```

| Object | DocumentReadOnlyProperties <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or index of the meta property in a specific namespace. |
| oDocumentProperty | DocumentProperty <Data>Returned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example displays for a PDF document the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, sOut, oMyNameSpaces, iCount
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For Each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For iCount = 1 to oMyNameSpaces.Properties.Count
    sOut = sOut & "Name: " & oMyNameSpaces.Properties(iCount).Name & ", Value: " & oMyNameSpaces.Properties(iCount).Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for iCount in range( 1, oMyNameSpaces.Properties.Count + 1): 
        sOut = sOut + "Name: " + oMyNameSpaces.Properties(iCount).Name + ", Value: " + oMyNameSpaces.Properties(iCount).Value + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_remove_idocumentproperties.htm language=enus -->
## TOPIC 00932: Method: Remove for DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_remove_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_remove_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Remove for DocumentProperties <Data>

Method: Remove for DocumentProperties <Data>

Deletes a custom property of a document. Custom properties are user-defined meta properties from the top level of a document. You can read, create, edit, and delete custom properties. You can only read the other meta properties of a document and edit their values.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Remove(NameOrIndex)
```

| Object | DocumentProperties <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the custom property. |

The following example checks a PDF for the custom property copyright and deletes it.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, oMyProperties, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf",False, eDocumentTypeAuto)
Set oMyProperties = oMyDocument.Properties
For each oMyProperty in oMyProperties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
sOut = sOut & VBCrLf & "==After removing custom property==" & VBCrLf
If oMyProperties.Exists("copyright") Then
  Call oMyDocument.Properties.Remove("copyright")
End If
For each oMyProperty in oMyProperties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf",False, dd.eDocumentTypeAuto) 
oMyProperties = oMyDocument.Properties 
for oMyProperty in oMyProperties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
sOut = sOut + "\r\n" + "==After removing custom property==" + "\r\n" 
if oMyProperties.Exists("copyright") : 
    oMyDocument.Properties.Remove("copyright") 
for oMyProperty in oMyProperties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_removeall_idocumentproperties.htm language=enus -->
## TOPIC 00933: Method: RemoveAll for DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_removeall_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_removeall_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: RemoveAll for DocumentProperties <Data>

Method: RemoveAll for DocumentProperties <Data>

Deletes all custom properties of a document. Custom properties are user-defined meta properties from the top level of a document. You can read, create, edit, and delete custom properties. You can only read the other meta properties of a document and edit their values.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.RemoveAll()
```

| Object | DocumentProperties <Data>Object with this method |
| --- | --- |

The following example deletes all custom properties in a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, oMyProperties, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf",False, eDocumentTypeAuto)
Set oMyProperties = oMyDocument.Properties
For each oMyProperty in oMyProperties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
sOut = sOut & VBCrLf & "==After removing custom properties==" & VBCrLf
Call oMyDocument.Properties.RemoveAll
For each oMyProperty in oMyProperties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf",False, dd.eDocumentTypeAuto) 
oMyProperties = oMyDocument.Properties 
for oMyProperty in oMyProperties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
sOut = sOut + "\r\n" + "==After removing custom properties==" + "\r\n" 
oMyDocument.Properties.RemoveAll() 
for oMyProperty in oMyProperties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/methods/diacmpnt_method_save_idiademdocument.htm language=enus -->
## TOPIC 00934: Method: Save for Document <Data>

- bundle_id: `diadem`
- source_path: `filetagging/methods/diacmpnt_method_save_idiademdocument.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/methods/diacmpnt_method_save_idiademdocument.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Save for Document <Data>

Method: Save for Document <Data>

Saves the document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Save()
```

| Object | Document <Data>Object with this method |
| --- | --- |

The following example checks whether you opened the PDF document in read and write mode. If DIAdem can write into the document, the example adds a new meta property and saves the document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
If Not(oMyDocument.ReadOnly) Then
  Call oMyDocument.Properties.Add("Modified","Yes",DataTypeString)
  Call oMyDocument.Save()
End If
sOut = "File path: " & oMyDocument.FilePath & VBCrLf
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
if not(oMyDocument.ReadOnly) : 
    oMyDocument.Properties.Add("Modified","Yes",dd.DataTypeString) 
    oMyDocument.Save() 
sOut = "File path: " + oMyDocument.FilePath + "\r\n" 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/objects/diacmpnt_objects_idiademdocument.htm language=enus -->
## TOPIC 00935: Object: Document <Data>

- bundle_id: `diadem`
- source_path: `filetagging/objects/diacmpnt_objects_idiademdocument.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/objects/diacmpnt_objects_idiademdocument.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Document Properties](../filetagging_overview.htm) > [Objects](../objects/idiademdocument_objects_overview.htm) > Object: Document <Data>

Object: Document <Data>

The Document <Data> object provides the properties and methods for accessing the meta properties of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

The following example displays the names and values of the meta properties for a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### Properties

[FilePath](../properties/diacmpnt_property_filepath_idiademdocument.htm) | [FileType](../properties/diacmpnt_property_filetype_idiademdocument.htm) | [Namespaces](../properties/diacmpnt_property_namespaces_idiademdocument.htm) | [Properties](../properties/diacmpnt_property_properties_idiademdocument.htm) | [ReadOnly](../properties/diacmpnt_property_readonly_idiademdocument.htm)

#### Methods

[Save](../methods/diacmpnt_method_save_idiademdocument.htm)

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/objects/diacmpnt_objects_idocumentnamespace.htm language=enus -->
## TOPIC 00936: Object: DocumentNamespace <Data>

- bundle_id: `diadem`
- source_path: `filetagging/objects/diacmpnt_objects_idocumentnamespace.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/objects/diacmpnt_objects_idocumentnamespace.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Document Properties](../filetagging_overview.htm) > [Objects](../objects/idiademdocument_objects_overview.htm) > [Document](../objects/diacmpnt_objects_idiademdocument.htm) > [DocumentNamespaces](../objects/diacmpnt_objects_idocumentnamespaces.htm) > Object: DocumentNamespace <Data>

Object: DocumentNamespace <Data>

The DocumentNamespace <Data> object provides the namespace in a document. Use namespaces to identify XML elements clearly in a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

The following example displays for a PDF document the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For each oMyProperty in oMyNameSpaces.Properties
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for oMyProperty in oMyNameSpaces.Properties: 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### Properties

[Name](../properties/diacmpnt_property_name_idocumentnamespace.htm) | [Properties](../properties/diacmpnt_property_properties_idocumentnamespace.htm)

#### Returned From

[DocumentNamespaces <Data>](../objects/diacmpnt_objects_idocumentnamespaces.htm).[Item](../methods/diacmpnt_method_item_idocumentnamespaces.htm)

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/objects/diacmpnt_objects_idocumentnamespaces.htm language=enus -->
## TOPIC 00937: Collection: DocumentNamespaces <Data>

- bundle_id: `diadem`
- source_path: `filetagging/objects/diacmpnt_objects_idocumentnamespaces.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/objects/diacmpnt_objects_idocumentnamespaces.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Document Properties](../filetagging_overview.htm) > [Objects](../objects/idiademdocument_objects_overview.htm) > [Document](../objects/diacmpnt_objects_idiademdocument.htm) > Collection: DocumentNamespaces <Data>

Collection: DocumentNamespaces <Data>

Collection of name spaces in a document. Use namespaces to identify XML elements clearly in a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

The following example displays the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For each oMyProperty in oMyNameSpaces.Properties
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for oMyProperty in oMyNameSpaces.Properties: 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### Properties

[Count](../properties/diacmpnt_property_count_idocumentnamespaces.htm)

#### Methods

[Exists](../methods/diacmpnt_method_exists_idocumentnamespaces.htm) | [Item](../methods/diacmpnt_method_item_idocumentnamespaces.htm)

#### Returned From

[Document <Data>](../objects/diacmpnt_objects_idiademdocument.htm).[Namespaces](../properties/diacmpnt_property_namespaces_idiademdocument.htm)

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/objects/diacmpnt_objects_idocumentproperties.htm language=enus -->
## TOPIC 00938: Collection: DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/objects/diacmpnt_objects_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/objects/diacmpnt_objects_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Document Properties](../filetagging_overview.htm) > [Objects](../objects/idiademdocument_objects_overview.htm) > [Document](../objects/diacmpnt_objects_idiademdocument.htm) > Collection: DocumentProperties <Data>

Collection: DocumentProperties <Data>

Collection of changeable meta properties that are not assigned to a namespace, from the top level of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

The five properties name, description, title,  author, and datetime are the base properties of a document. They are permanent and cannot be deleted.

The following example displays the names and values of the meta properties for a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### Properties

[Count](../properties/diacmpnt_property_count_idocumentproperties.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_idocumentproperties.htm) | [AddProperties](../methods/diacmpnt_method_addproperties_idocumentproperties.htm) | [Exists](../methods/diacmpnt_method_exists_idocumentproperties.htm) | [Item](../methods/diacmpnt_method_item_idocumentproperties.htm) | [Remove](../methods/diacmpnt_method_remove_idocumentproperties.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_idocumentproperties.htm)

#### Returned From

[Document <Data>](../objects/diacmpnt_objects_idiademdocument.htm).[Properties](../properties/diacmpnt_property_properties_idiademdocument.htm)

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/objects/diacmpnt_objects_idocumentproperty.htm language=enus -->
## TOPIC 00939: Object: DocumentProperty <Data>

- bundle_id: `diadem`
- source_path: `filetagging/objects/diacmpnt_objects_idocumentproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/objects/diacmpnt_objects_idocumentproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([DocumentProperties](../objects/diacmpnt_objects_idocumentproperties.htm) | [DocumentReadOnlyProperties](../objects/diacmpnt_objects_idocumentreadonlyproperties.htm)) > Object: DocumentProperty <Data>

Object: DocumentProperty <Data>

The DocumentProperty <Data> object provides the meta properties of the document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

The following example displays the names and values of the meta properties of a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### Properties

[Custom](../properties/diacmpnt_property_custom_idocumentproperty.htm) | [DataType](../properties/diacmpnt_property_datatype_idocumentproperty.htm) | [Name](../properties/diacmpnt_property_name_idocumentproperty.htm) | [Value](../properties/diacmpnt_property_value_idocumentproperty.htm)

#### Returned From

[DocumentProperties <Data>](../objects/diacmpnt_objects_idocumentproperties.htm).[Add](../methods/diacmpnt_method_add_idocumentproperties.htm) | [DocumentProperties <Data>](../objects/diacmpnt_objects_idocumentproperties.htm).[Item](../methods/diacmpnt_method_item_idocumentproperties.htm) | [DocumentReadOnlyProperties <Data>](../objects/diacmpnt_objects_idocumentreadonlyproperties.htm).[Item](../methods/diacmpnt_method_item_idocumentreadonlyproperties.htm)

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/objects/diacmpnt_objects_idocumentreadonlyproperties.htm language=enus -->
## TOPIC 00940: Collection: DocumentReadOnlyProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/objects/diacmpnt_objects_idocumentreadonlyproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/objects/diacmpnt_objects_idocumentreadonlyproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Document Properties](../filetagging_overview.htm) > [Objects](../objects/idiademdocument_objects_overview.htm) > [Document](../objects/diacmpnt_objects_idiademdocument.htm) > [DocumentNamespaces](../objects/diacmpnt_objects_idocumentnamespaces.htm) > [DocumentNamespace](../objects/diacmpnt_objects_idocumentnamespace.htm) > Collection: DocumentReadOnlyProperties <Data>

Collection: DocumentReadOnlyProperties <Data>

Collection of all meta properties in a specific namespace of a document. The meta properties in a specific namespace are read-only. Use namespaces to identify XML elements clearly in a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

The following example displays for a PDF document the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For each oMyProperty in oMyNameSpaces.Properties
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for oMyProperty in oMyNameSpaces.Properties: 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### Properties

[Count](../properties/diacmpnt_property_count_idocumentreadonlyproperties.htm)

#### Methods

[Exists](../methods/diacmpnt_method_exists_idocumentreadonlyproperties.htm) | [Item](../methods/diacmpnt_method_item_idocumentreadonlyproperties.htm)

#### Returned From

[DocumentNamespace <Data>](../objects/diacmpnt_objects_idocumentnamespace.htm).[Properties](../properties/diacmpnt_property_properties_idocumentnamespace.htm)

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/objects/idiademdocument_objects_overview.htm language=enus -->
## TOPIC 00941: Objects

- bundle_id: `diadem`
- source_path: `filetagging/objects/idiademdocument_objects_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/objects/idiademdocument_objects_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Document Properties](../filetagging_overview.htm) > Objects

[[IMAGE alt='image' src='ms-its:diadem.chm::/plus.png']Display all](#nowhere)  [[IMAGE alt='image' src='ms-its:diadem.chm::/minus2.png']Hide all](#nowhere)

Objects

Use the Document <Data> object to access the meta properties of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

The Document object is the global object. Many subobjects have collections of single objects. You can access the single objects and the collection. Use the [Set](../../vbs/general/vbs_set.htm) statement to assign objects to a variable in order to make it easier to access these objects. You use the Add methods to create new objects. You use the Remove methods to delete existing objects. You use properties to change objects.

The following structure of the objects in DIAdem REPORT shows you how to click to the objects:

- Document <Data>
  - DocumentNamespaces <Data>
    - DocumentNamespace <Data>
      - ReadOnlyProperties <Data>
        - DocumentProperty <Data>
  - Properties <Data>
    - DocumentProperty <Data>

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_count_idocumentnamespaces.htm language=enus -->
## TOPIC 00942: Property: Count for DocumentNamespaces <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_count_idocumentnamespaces.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_count_idocumentnamespaces.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Count for DocumentNamespaces <Data>

Property: Count for DocumentNamespaces <Data>

Returns the number of namespaces of a document. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Count
```

| Object | DocumentNamespaces <Data>Object with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays the number of namespaces and their names, for a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
sOut =  "Number of namesspaces:  " & oMyDocument.Namespaces.Count & VBCrLf
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
sOut =  "Number of namesspaces:  " + oMyDocument.Namespaces.Count + "\r\n" 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_count_idocumentproperties.htm language=enus -->
## TOPIC 00943: Property: Count for DocumentProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_count_idocumentproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_count_idocumentproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Count for DocumentProperties <Data>

Property: Count for DocumentProperties <Data>

Returns the number of meta properties of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Count
```

| Object | DocumentProperties <Data>Object with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays the number of, the names, and the values of the meta properties of the PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
sOut = "Number of properties: " & oMyDocument.Properties.Count & VBCrLf
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
sOut = "Number of properties: " + oMyDocument.Properties.Count + "\r\n" 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_count_idocumentreadonlyproperties.htm language=enus -->
## TOPIC 00944: Property: Count for DocumentReadOnlyProperties <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_count_idocumentreadonlyproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_count_idocumentreadonlyproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Count for DocumentReadOnlyProperties <Data>

Property: Count for DocumentReadOnlyProperties <Data>

Returns the number of meta properties in a specific namespace of a document. The meta properties in a specific namespace are read-only. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Count
```

| Object | DocumentReadOnlyProperties <Data>Object with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays for a PDF document the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For each oMyProperty in oMyNameSpaces.Properties
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for oMyProperty in oMyNameSpaces.Properties: 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_custom_idocumentproperty.htm language=enus -->
## TOPIC 00945: Property: Custom for DocumentProperty <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_custom_idocumentproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_custom_idocumentproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Custom for DocumentProperty <Data>

Property: Custom for DocumentProperty <Data>

Specifies whether a meta property of a document is a custom property. Custom properties are user-defined meta properties from the top level of a document. You can read, create, edit, and delete custom properties. You can only read the other meta properties of a document and edit their values.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Custom
```

| Object | DocumentProperty <Data>Object with this property |
| --- | --- |
| Object.Custom | Boolean value with read access |

The following example displays the names and values of all meta properties of the document, for a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
sOut = "File path: " & oMyDocument.FilePath & VBCrLf
For Each oMyProperty in oMyDocument.Properties
  If oMyProperty.Custom Then
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
  End If
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
sOut = "File path: " + oMyDocument.FilePath + "\r\n" 
for oMyProperty in oMyDocument.Properties: 
    if oMyProperty.Custom : 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_datatype_idocumentproperty.htm language=enus -->
## TOPIC 00946: Property: DataType for DocumentProperty <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_datatype_idocumentproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_datatype_idocumentproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: DataType for DocumentProperty <Data>

Property: DataType for DocumentProperty <Data>

Returns the data type of a meta property of a document. Use the method [Add for DocumentProperties <Data>](../methods/diacmpnt_method_add_idocumentproperties.htm) to create new meta properties.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.DataType
```

| Object | DocumentProperty <Data>Object with this property |  |
| --- | --- | --- |
| Object.DataType | Enumeration with read access and the following selection terms: 3DataTypeDocumentInt32 32-bit integer values 10DataTypeDocumentFloat64 64-bit real values 23DataTypeDocumentString Text 30DataTypeDocumentDate Time values |  |
| 3 | DataTypeDocumentInt32 | 32-bit integer values |
| 10 | DataTypeDocumentFloat64 | 64-bit real values |
| 23 | DataTypeDocumentString | Text |
| 30 | DataTypeDocumentDate | Time values |

The following example displays the names and data types of the meta properties of a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Data type: " & PropertyDataTypeAsText(oMyProperty.DataType) & VBCrLf
Next
Call MsgBox(sOut)

' Function to convert data type from integer into text ===
Function PropertyDataTypeAsText(eMyType)
 Select Case eMyType
  Case DataTypeDocumentInt32 
   PropertyDataTypeAsText = "Int32"
  Case DataTypeDocumentFloat64 
   PropertyDataTypeAsText = "Float64"
  Case DataTypeDocumentString 
   PropertyDataTypeAsText = "String"
  Case DataTypeDocumentDate 
   PropertyDataTypeAsText = "Date"
 End Select
End Function
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Data type: " + PropertyDataTypeAsText(oMyProperty.DataType) + "\r\n" 
print(sOut) 
# Function to convert data type from integer into text ===
def PropertyDataTypeAsText(eMyType): 
    select_variable_0 = eMyType 
    if (select_variable_0 == dd.DataTypeDocumentInt32) : 
        PropertyDataTypeAsText = "Int32" 
    elif (select_variable_0 == dd.DataTypeDocumentFloat64) : 
        PropertyDataTypeAsText = "Float64" 
    elif (select_variable_0 == dd.DataTypeDocumentString) : 
        PropertyDataTypeAsText = "String" 
    elif (select_variable_0 == dd.DataTypeDocumentDate) : 
        PropertyDataTypeAsText = "Date" 
    return PropertyDataTypeAsText
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_filepath_idiademdocument.htm language=enus -->
## TOPIC 00947: Property: FilePath for Document <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_filepath_idiademdocument.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_filepath_idiademdocument.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: FilePath for Document <Data>

Property: FilePath for Document <Data>

Returns the absolute path of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.FilePath
```

| Object | Document <Data>Object with this property |
| --- | --- |
| Object.FilePath | String with read access |

The following example displays the absolute path of the open document, for a PDF document.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
sOut = "File path: " & oMyDocument.FilePath
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
sOut = "File path: " + oMyDocument.FilePath 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_filetype_idiademdocument.htm language=enus -->
## TOPIC 00948: Property: FileType for Document <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_filetype_idiademdocument.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_filetype_idiademdocument.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: FileType for Document <Data>

Property: FileType for Document <Data>

Returns the data type of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.FileType
```

| Object | Document <Data>Object with this property |  |
| --- | --- | --- |
| Object.FileType | Enumeration with read access and the following selection terms: 0eDocumentTypeAuto The file type is specified automatically from the filename extension. DIAdem does not return this file type but always one of the following. 1eDocumentTypeXMP XMP file (for example *.pdf; *.jpg; *.jpeg; *.png; *.tif; *.tiff) 2eDocumentTypeWord XML based Word file (for example *.docx; *.docm; *.dotx; *.dotm) 3eDocumentTypeExcel XML based Excel file (for example *.xlsx; *.xltm; *.xltx; *.xltm) 4eDocumentTypePowerPoint XML based PowerPoint file (for example *.pptx; *.pptm; *.potx; *.potm) |  |
| 0 | eDocumentTypeAuto | The file type is specified automatically from the filename extension. DIAdem does not return this file type but always one of the following. |
| 1 | eDocumentTypeXMP | XMP file (for example *.pdf; *.jpg; *.jpeg; *.png; *.tif; *.tiff) |
| 2 | eDocumentTypeWord | XML based Word file (for example *.docx; *.docm; *.dotx; *.dotm) |
| 3 | eDocumentTypeExcel | XML based Excel file (for example *.xlsx; *.xltm; *.xltx; *.xltm) |
| 4 | eDocumentTypePowerPoint | XML based PowerPoint file (for example *.pptx; *.pptm; *.potx; *.potm) |

The following example displays the data type of the open document, for a PDF document.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
sOut = "File type: " & sFileType(oMyDocument.FileType)
Call MsgBox(sOut)

Function sFileType(iFileType)
  Select Case iFileType 
  Case eDocumentTypeXMP 
    sFileType = "XMP"
  Case eDocumentTypeWord
    sFileType = "Word"
  Case eDocumentTypeExcel
    sFileType = "Excel"
  Case eDocumentTypePowerPoint 
    sFileType = "PowerPoint"
  End Select
End Function
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
sOut = "File type: " + sFileType(oMyDocument.FileType) 
print(sOut) 
def sFileType(iFileType): 
    select_variable_0 = iFileType 
    if (select_variable_0 == dd.eDocumentTypeXMP) : 
        sFileType = "XMP" 
    elif (select_variable_0 == dd.eDocumentTypeWord) : 
        sFileType = "Word" 
    elif (select_variable_0 == dd.eDocumentTypeExcel) : 
        sFileType = "Excel" 
    elif (select_variable_0 == dd.eDocumentTypePowerPoint) : 
        sFileType = "PowerPoint" 
    return sFileType
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_name_idocumentnamespace.htm language=enus -->
## TOPIC 00949: Property: Name for DocumentProperty <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_name_idocumentnamespace.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_name_idocumentnamespace.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Name for DocumentProperty <Data>

Property: Name for DocumentProperty <Data>

Returns the name of a namespace in a document. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Name
```

| Object | DocumentNamespace <Data>Object with this property |
| --- | --- |
| Object.Name | String with read access |

The following example displays for a PDF document the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For each oMyProperty in oMyNameSpaces.Properties
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for oMyProperty in oMyNameSpaces.Properties: 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_name_idocumentproperty.htm language=enus -->
## TOPIC 00950: Property: Name for DocumentProperty <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_name_idocumentproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_name_idocumentproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Name for DocumentProperty <Data>

Property: Name for DocumentProperty <Data>

Returns the name of a meta property of a document. Use the method [Add for DocumentProperties <Data>](../methods/diacmpnt_method_add_idocumentproperties.htm) to create meta properties.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Object.Name
```

| Object | DocumentProperty <Data>Object with this property |
| --- | --- |
| Object.Name | String with read accessName of the meta property |

The following example displays the names and values of the meta properties of a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf",False, eDocumentTypeAuto)
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf",False, dd.eDocumentTypeAuto) 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_namespaces_idiademdocument.htm language=enus -->
## TOPIC 00951: Property: Namespaces for Document <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_namespaces_idiademdocument.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_namespaces_idiademdocument.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Namespaces for Document <Data>

Property: Namespaces for Document <Data>

Returns all namespaces of a document. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Set oDocumentNamespaces = Object.Namespaces
```

| Object | Document <Data>Object with this property |
| --- | --- |
| oDocumentNamespaces | DocumentNamespaces <Data>Returned object |

The following example displays for a PDF document the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For each oMyProperty in oMyNameSpaces.Properties
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for oMyProperty in oMyNameSpaces.Properties: 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_properties_idiademdocument.htm language=enus -->
## TOPIC 00952: Property: Properties for Document <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_properties_idiademdocument.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_properties_idiademdocument.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Properties for Document <Data>

Property: Properties for Document <Data>

Returns all meta properties of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Set oDocumentProperties = Object.Properties
```

| Object | Document <Data>Object with this property |
| --- | --- |
| oDocumentProperties | DocumentProperties <Data>Returned object |

The following example displays the names and values of the meta properties for a PDF document:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyProperty in oMyDocument.Properties
  sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value  & VBCrLf
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyProperty in oMyDocument.Properties: 
    sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value  + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=filetagging/properties/diacmpnt_property_properties_idocumentnamespace.htm language=enus -->
## TOPIC 00953: Property: Properties for DocumentNamespace <Data>

- bundle_id: `diadem`
- source_path: `filetagging/properties/diacmpnt_property_properties_idocumentnamespace.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/filetagging/properties/diacmpnt_property_properties_idocumentnamespace.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Properties for DocumentNamespace <Data>

Property: Properties for DocumentNamespace <Data>

Returns all meta properties in a specific namespace of a document. Use namespaces to identify XML elements clearly in a document.

A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP. Use the [OpenDocument](../../comoff/opendocument.htm) command to open a document.

```text
Set oDocumentReadOnlyProperties = Object.Properties
```

| Object | DocumentNamespace <Data>Object with this property |
| --- | --- |
| oDocumentReadOnlyProperties | DocumentReadOnlyProperties <Data>Returned object |

The following example displays for a PDF document the names of the name spaces and the number of properties of the respective name space. The example also displays the names and values of the meta properties of the respective name space:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDocument, oMyProperty, sOut, oMyNameSpaces
Set oMyDocument = OpenDocument(ProgramDrv & "Manuals\DIAdem_GettingStarted.pdf", False, eDocumentTypeAuto)
For each oMyNameSpaces in oMyDocument.Namespaces
  sOut = sOut & "Namespace: " & oMyNameSpaces.Name & ", Number of properties:  " & oMyNameSpaces.Properties.Count & VBCrLf
  For each oMyProperty in oMyNameSpaces.Properties
    sOut = sOut & "Name: " & oMyProperty.Name & ", Value: " & oMyProperty.Value & VBCrLf
  Next
Next
Call MsgBox(sOut)
```

[Copy script](javascript:void(0);)

```text
oMyDocument = dd.OpenDocument(dd.ProgramDrv + "Manuals\\DIAdem_GettingStarted.pdf", False, dd.eDocumentTypeAuto) 
for oMyNameSpaces in oMyDocument.Namespaces: 
    sOut = sOut + "Namespace: " + oMyNameSpaces.Name + ", Number of properties:  " + oMyNameSpaces.Properties.Count + "\r\n" 
    for oMyProperty in oMyNameSpaces.Properties: 
        sOut = sOut + "Name: " + oMyProperty.Name + ", Value: " + oMyProperty.Value + "\r\n" 
print(sOut) 
```

#### See Also

[Objects Overview](../objects/idiademdocument_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=genas/genauto/genauto_autosequences_general.htm language=enus -->
## TOPIC 00954: General Information on Scripts

- bundle_id: `diadem`
- source_path: `genas/genauto/genauto_autosequences_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genas/genauto/genauto_autosequences_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

General Information on Scripts

General Information on Scripts

Use scripts to automate sequences in DIAdem. A script is a sequence of commands that DIAdem saves in a text file and works through sequentially. You generate a script by entering commands in the [script editor](../../genscript/genscript/genscript_editor.htm). Alternatively, use the [recording mode](../../procscript/procscript/procscript_recording_autosequences.htm), where DIAdem records all steps you complete interactively in DIAdem in a script. You can edit scripts by adding control structures or commands.

|  | Note Refer to Structuring Scripts for information on the structure of a script. |
| --- | --- |

When you use scripts, the following files are important:

- VBS files have the filename extension .vbs and contain DIAdem scripts written in Visual Basic Script. If you have encrypted this file, the script files have the extension .vbc.
- Python files have the extension .py and contain DIAdem scripts written in Python.
- List files have the extension .lst and contain the names of files that a script works through.
- Dialog files have the extension .sud and define [user dialog boxes](../../dlgsud/dlgsud/sud_general.htm). If you have encrypted this file, the script files have the extension .suc.
- Text files contain lines that you can read or write in a script.

<!--NI_TOPIC bundle=diadem path=genas/genauto/genauto_channels.htm language=enus -->
## TOPIC 00955: Channel Lists

- bundle_id: `diadem`
- source_path: `genas/genauto/genauto_channels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genas/genauto/genauto_channels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General Information on Scripts](../genauto/genauto_autosequences_general.htm) > Channel Lists

Channel Lists

A channel list is a [Channel](../../inavidata/objects/diacmpnt_objects_idiademchannel.htm) or [Channel list](../../inavidata/objects/diacmpnt_objects_idiademelementlist.htm) object, or a text that refers to one or several channels.

Refer to the Help page on [Channels and Channel References](../../genshell/genshell/genshell_data_channels.htm) for information on how to reference a channel.

Use the [GetChannel](../../inavidata/methods/diacmpnt_method_getchannel_inavidata.htm) method to specify a single channel object, for example: 
Data.GetChannel("[1]/[1]")

Use the [GetChannels](../../inavidata/methods/diacmpnt_method_getchannels_inavidata.htm) method to return a list of channels, for example: 
Data.GetChannels("Example/D*")

You also can specify a channel list as text which refers to one or several channels. If you use channel names to specify a channel area, DIAdem uses the internally assigned channel numbers and specifies the channel section with these numbers.

If you use text to refer to several channels, you must set the individual channel references in single quotation marks and separate them with a comma, for example: 
"'Grp1/Chn1','Grp1/Chn4','Grp1/Chn7','Grp1/Chn20'".

You also can reference several channels if you specify a channel section with the following syntax: *Channel* - *Channel*. For example, if you want to select the channels Grp1/Chn1, Grp1/Chn4 to Grp1/Chn7, and Grp1/Chn20, specify the following channel list: 
"'Grp1/Chn1','Grp1/Chn4'-'Grp1/Chn7','Grp1/Chn20'"

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_3d_organisation.htm language=enus -->
## TOPIC 00956: 3D Data Structure

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_3d_organisation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_3d_organisation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [3D Data Analysis](../genmaths/calc_overview3d.htm) > 3D Data Structure

3D Data Structure

DIAdem can manage, analyze, and display three-dimensional data as value triplets and matrices. The **Convert Matrix** function converts the data structure from triplet to matrix and vice versa.

#### Triplet Structure or Matrix Structure

A triplet consists of three data channels of the same length, which contain the x, y, or z-values. A matrix consists of one numeric x-channel, one numeric y-channel, and several numeric z-channels. The number of z-channels corresponds with the length of the y-channel. The length of the z-channels corresponds with the length of the x-channel. The z-channels must be in consecutive order in a group in the data area. The x-channel and the y-channel can be anywhere in the data area. The following graphic illustrates a matrix structure.

[IMAGE alt='image' src='../image/3d-data.png']

#### Convert Matrix

Matrices of measurement values often develop when tests are repeated with different parameters, for example, if current and voltage curves of a semiconductor are measured repeatedly at different temperatures. Other measurements, for example, the acquisition of the longitude, latitude, and altitude with GPS return measurement values directly as value triplets.

DIAdem supports 3D data in a matrix structure and in a triplet structure. Many calculations and displays in DIAdem such as waterfall displays or bar displays need 3D data in matrix structure. DIAdem supports some displays such as 3D curves only for data in triplet structure. For other displays and calculations such as the characteristic diagram, DIAdem supports triplet data and matrix data.

The **Convert Matrix** function converts the data structure from triplet to matrix and vice versa. For the conversion to matrix structure, DIAdem joins the different x-values to a new x-channel and the different y-values to a new y-channel, and orders the z-values into a z-matrix. The conversion ignores triplets that contain NoValues. X/Y points, which do not occur in the triplet structure, receive the z-value NoValue. If the x-values and the y-values of several triplets are the same, DIAdem saves the arithmetic mean of the z-values in the z-matrix. If the x-values and the y-values are not exactly the same due to measurement inaccuracies or rounding errors in the calculation, the values are saved only once in the matrix if an appropriate tolerance is specified.

If the 3D data is in matrix structure but is required in triplet structure, the **Convert Matrix** function can also convert the 3D data. All points that the x-channel and the y-channel specify are stored with the associated z-value in the three channels x, y, and z. The conversion ignores triplets that contain the NoValue value.

**Example 1**

The following channels specify a 3D data structure.

[IMAGE alt='image' src='../image/f_chnmatconvert1.gif']

The conversion into matrix structure results in the following structure, in which DIAdem saves the z-matrix in two adjoining channels.

[IMAGE alt='image' src='../image/f_chnmatconvert2.gif']

**Example 2**

An x-channel, a y-channel, and three z-channels determine a 3D data structure:

[IMAGE alt='image' src='../image/f_matchnconvert1.gif']

The conversion into a triplet structure produces the following channels:

[IMAGE alt='image' src='../image/f_matchnconvert2.gif']

#### 3D Data Analysis

3D-Data Structure | [3D-Basic Functions](../genmaths/calc_3dbasicfunctions.htm) | [3D-Arithmetic](../genmaths/calc_3darithmetics.htm) | [3D-Basic Mathematics](../genmaths/calc_3dbasicmath.htm) | [3D-Surface Calculations](../genmaths/calc_3dsurfaces.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_3dsurfaces.htm language=enus -->
## TOPIC 00957: 3D Surface Calculation

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_3dsurfaces.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_3dsurfaces.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [3D Data Analysis](../genmaths/calc_overview3d.htm) > 3D Surface Calculation

3D Surface Calculation

DIAdem can interpolate or approximate 3D data through surfaces. The interpolating surface goes exactly through all specified nodes whereas the approximating surface minimizes the distance to the nodes for a specified setup function. On the surfaces DIAdem calculates the curve of equal z-values that are called contour lines or isolines. If the surface or contour lines are not to be calculated for all 3D data, DIAdem limits the evaluation to a specified or calculated hull.

#### Interpolating

The **Interpolate** function calculates surfaces for three-dimensional data which run exactly through the specified nodes. DIAdem has interpolation processes for triplet or matrix input data. First you must specify an x/y matrix for the evaluation points, regardless of the data structure of the 3D data. At these evaluation points DIAdem calculates the z-values for the interpolating surface. Then you can use a hull to limit the interpolation to a partial area, for example, if the data is not defined everywhere. To specify the hull either calculate the convex hull or specify the limiting polygon in two channels.

If the 3D data is in a matrix display, DIAdem uses the surrounding grid points to calculate a bicubic polynomial in each internal grid point and calculates a biquadratic polynomial in each boundary point. If the input data has a triplet structure, DIAdem offers different methods for interpolating the z-values:

- The InverseDistance method is the simplest, fastest, and most robust method. For each evaluation point the weighted sum of the z-values of the neighboring points to be evaluated is calculated. The neighboring points are weighted with the inverse distance in the p-th potency. The larger the distance and the selected exponent p are, the less the neighbor points contribute to the calculation of the z-values. Distance describes the distance between the neighboring point and the evaluation point in the x/y-plane.
- The multiquadric method uses radial basic functions and does not need a manually tuned factor such as the exponent p of the InverseDistance method. Radial basic functions are real value functions whose values depend exclusively on the distance to a center. The multiquadric method combines functions of the sqrt(Distance^2+1) form. DIAdem solves for each evaluation point a linear system of equations of the order n, which is the number of neighboring points to be included.
- The ThinPlate method uses polyharmonic splines which also belong to the radial basic functions. To envisage the method one can imagine a thin plate that is bent so that it runs through all the nodes. In every point of the evaluation grid DIAdem solves several equation systems of the order n+3, in which n is the number of neighboring points to be included.
- The Smart-Interpolating-Spline(SISPL)-Surface method is a spline method which achieves a high degree of optical smoothness regardless of the low calculating time. Although only the evaluation points need to be specified this method delivers good results even if the input data differs considerably.

In addition to the interpolation method you specify which nodes are used for the calculation of a result point. If you set "Use n neighboring points", DIAdem searches for up to 16 of the nearest nodes around the evaluation point. If you set "Use n neighboring points per quadrant", DIAdem divides the x/y-plane for each evaluation point in four quadrants whose separating lines intersect at the current evaluation point. In each quadrant up to four of the nearest neighboring points are searched for. If the number of node points is low, the setting n neighboring points is most suitable. If you set "Use points from within the frame", DIAdem searches for up to 16 of the nearest neighboring points for every evaluation point in a rectangle with the specified edge length around the evaluation point.

The optical smoothness of the interpolating surface increases in the order InverseDistance — Multiquadric — ThinPlate. If you process large quantities of data, use the InverseDistance method and do not select too many neighboring points. You can use the SISPL Surface method as an alternative.

If the interpolation fails because the linear equation systems of the Multiquadric or Thinplate method cannot be solved, check especially all the settings of the selected method. Decrease the number of neighbor points to be included. Use the setting "Use n neighboring points" instead of "Use n neighboring points per quadrant". If the calculation continues to fail, use either the Inverse Distance or the SISPL surface method.

#### Approximating

The **Approximate** function uses the least error squares method to calculate three-dimensional data surfaces which do not run exactly through the specified nodes but minimize the distance to the nodes for the specified setup function. DIAdem approximates triplet or matrix input data. First you must specify an x/y matrix for the evaluation points, regardless of the data structure of the 3D data. At these evaluation points the approximation function calculates the z-values for the approximating surface. Then you can use a hull to limit the approximation to a partial area, for example, if the data is not defined everywhere. To specify the hull either calculate the convex hull or specify the limiting polygon in two channels.

DIAdem has 24 different setup terms such as constant, x-related, y-related, and mixed setup terms. Select up to ten setup terms for the setup function. First, get an overview of the 3D data development before you select a setup term. Then select appropriate setup terms that match the data. The choice of the setup function determines how well the approximation matches the original data. Check the selected setup terms if the coefficients deviate by several quantities from each other.

#### Calculate Contour Lines

Curves of the same height on a 3D surface are called contour lines or isolines. The **Calculate Contour Lines** calculates for each contour value two result channels with the x-values and the y-values of this contour line. You can specify the contour values directly in a channel or calculate them from the extreme values of the 3D surface. If you select automatic calculation, you only specify the number of contour values. If you select manual calculation, you enter the number of contour values and also the lowest and the highest contour value.

The contour line calculation can evaluate 3D surfaces that are in triplet or in matrix structure. Input data in matrix structure is based on a grid of rectangles which DIAdem creates from the x-channel and the y-channel. If the input data is in triplet structure, DIAdem specifies a triangulation for the x, y-points, which is the basis for the contour line calculation.

DIAdem calculates contour lines either for the complete grid or for a partial area. This makes sense, for example, if the surface actually has a bent edge and was only filled for the conversion into matrix structure with NoValues. To calculate the contour lines for a partial area of the surface, specify a closed polygon through an x-channel and a y-channel as the boundary curve. If the input data is a triplet structure, you can calculate the boundary curve directly with the contour lines.

#### Calculate Hull

Hulls are closed polygons that enclose a number of points in the x/y plane. To prevent the hull from intersecting itself, the hull contains each point except the start point only once. The **Calculate Hull** function calculates convex or non-convex hulls for a set of points specified by the x-channel and the y-channel. Convex hulls do not have indentations so that all points on the connection between two points belong to the hull. Non-convex hulls completely enclose the points. However they have indentations which extend into the inside of the point set. This means that there are points on the connecting lines of two hull points which do not belong to the non-convex hull.

To calculate a non-convex hull, DIAdem first determines the convex hull. Then the hull calculation searches for points from the point set near the edges to replace the convex edge with two new edges. The search starts at the longest edge and is controlled by the tolerance setting and the multiplication factor. An edge is only replaced if the length that the tolerance specifies is exceeded, and if at least one of the two edges is shorter than the edge of the convex hull multiplied by the multiplication factor. The hull calculation tries to replace the newly found edges with two new edges.

If you specify the multiplication factor 1, at least one of the two found boundaries is shorter than the convex edge. The multiplication factor should only be larger than 1 if DIAdem cannot otherwise achieve the specified deviance from the convex hull. When DIAdem processes the boundaries, DIAdem starts with the longest and ends with the shortest. This sequence might cause the edges calculated later to exceed the maximum length specified in the HullTol variable, because these edges need points that are already in the hull .

#### 3D Data Analysis

[3D-Data Structure](../genmaths/calc_3d_organisation.htm) | [3D-Basic Functions](../genmaths/calc_3dbasicfunctions.htm) | [3D-Arithmetic](../genmaths/calc_3darithmetics.htm) | [3D-Basic Mathematics](../genmaths/calc_3dbasicmath.htm) | 3D-Surface Calculations

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_approximation.htm language=enus -->
## TOPIC 00958: Approximation

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_approximation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_approximation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Curve Fitting](../genmaths/calc_overviewcurves.htm) > Approximation

Approximation

The approximation fits a curve that an x-channel and a y-channel specify point for point. The calculated approximation function connects x and y with a formula and then enables the calculation of the y-values for any x-values. After a setup function is specified, the approximation calculates first the setup coefficients and then the y-values of the approximation function at the specified evaluation points.

The approximation function setup contains up to 10 setup functions. In order to know which setup functions are best suited, it is necessary to have a graphical display of the curve to be approximated and also to know the principle progression of the available setup function. The approximation provides the following 26 linearly independent setup functions.

| Polynomial functions | Constant, x, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 |
| --- | --- |
| Rational functions | 1/x, 1/x2, 1/x3, 1/x4 |
| Logarithmic functions | ln(x), log(x) |
| Exponential functions | ex, 10x, ex2, 10x2, e-x, e-x2 |
| Radical functions | sqrt(x), x1/3 |

DIAdem uses the least squares method to calculate the setup coefficients. If the dimensions of the calculated setup coefficients differ considerably, for example, 1E+4 and 1E-6, the selected setup function might be inappropriate. The coefficient of determination describes the quality of the approximation and takes values between 0 and 1. For optimal approximation, the determination coefficient is one.

The approximation function does not run through all the specified points so that it does not interpolate. Instead it minimizes the mean distance to the curve. Thus the approximation is suitable, for example, to approximate corrupt measurement values. It makes no sense to select an arbitrary number of setup functions or setup functions with unnecessarily large exponents. If the functional connections are not clear and the curve does not need to be described with a formula, approximating splines might be better suited to calculate a fitting curve.

DIAdem generates the evaluation points through equidistant partition of the whole x-range or of the individual intervals of the x-range, or uses the evaluation points from a specified channel. DIAdem then calculates the y-values of the approximation function for all evaluation points.

The approximation function solves a system of linear equations. If the selected setup functions are not appropriate, the equations system might be ill-conditioned. If the equations system is too ill-conditioned, the approximation displays an error message.

#### Curve Fitting

[Smooth](../genmaths/calc_smoothfunctions.htm) | [Regression](../genmaths/calc_regression.htm) | Approximation | [Non-Linear Curve Fitting](../genmaths/calc_nonlinearcurvefit.htm) | [Gaussian Curve Fitting](../genmaths/calc_gaussianpeakfit.htm) | [General LS-Linear Fitting](../genmaths/calc_genlsfit.htm) | [Splines in DIAdem](../genmaths/calc_splines.htm) | [Non-Parametrical Splines](../genmaths/calc_nonparam_splines.htm) | [Parametrical Splines](../genmaths/calc_param_splines.htm) | [Akima Subsplines](../genmaths/calc_akima_splines.htm) | [Circle Approximation](../genmaths/calc_circles.htm) | [Envelope Curves](../genmaths/calc_envelopecurves.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_basicmathematics.htm language=enus -->
## TOPIC 00959: Basic Mathematics

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_basicmathematics.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_basicmathematics.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > Basic Mathematics

Basic Mathematics

The basic mathematics function group provides functions for fundamental mathematical calculations. The following section describes methods for numeric differentiation and integration, and for the calculation of the floating root mean square.

#### Differentiate

The differentiate function calculates the numerical derivative from the values that are time-discrete in the computer. DIAdem calculates the derivative either over a forward difference quotient or over a central difference quotient.

##### Calculation of the Forward Difference Quotient of The First Order

Up to Version 2011, DIAdem calculated the derivative only over the first order forward difference quotient according to the following formula

[IMAGE alt='image' src='../image/f_derivative.gif']

With this method the result channels are one value shorter than the input channels. The first result channel contains the average of two subsequent values from the x-channel. The second result channel contains the forward difference quotients of two successive value pairs from the input channels. If two subsequent x-values are identical, the y-result value is [NoValue](../genmaths/calc_novalue_description.htm).

##### Calculation over the Second Order Central Difference Quotient

From Version 2012, DIAdem calculates the derivative optionally over the second order central difference quotient according to the following formula

[IMAGE alt='image' src='../image/f_derivative2.gif']

N is the number of values in the channel. This procedure needs equidistant and strictly monotonic increasing x-values.

The necessary number of interpolation points for the calculation of the central difference quotient is not available at the edges. DIAdem calculates the second order forward difference quotient for the first two points of the channel according to the following formula

[IMAGE alt='image' src='../image/f_derivative2a.gif']

DIAdem calculates the second order backward difference quotient for the last two points of the channel according to the following formula

[IMAGE alt='image' src='../image/f_derivative2b.gif']

When the central difference quotient is calculated, the original channel length remains and DIAdem only creates a result channel with the y-values. The x-values remain unchanged. This method is used, for example, for crash evaluations and is described in the regulations SAE J1727 and ECE-R94.

#### Integrate

The integrate function uses either the trapezoidal rule or the Simpson rule to calculate the integral. In each partial interval, DIAdem approximates the surface below the y-values. DIAdem saves the summated sections in the result channel up to the corresponding point on the x-axis. The last value in the result channel receives the integral of the entire x-range.

Up to Version 2012, DIAdem used the trapezoidal rule without an integration constant for calculating the integration. If the integration constant is not enabled, the x-values need not be monotonic increasing. If a negative difference exists between two successive x-values, DIAdem subtracts the partial integral. If one of the input channels contains a [NoValue](../../varoff/novalue.htm), the result for this and the subsequent value is NoValue. The integration is calculated with the following formula

[IMAGE alt='image' src='../image/f_integral.png']

From Version 2014 onwards, DIAdem uses the trapezoidal rule with the integration constant as an option in order to calculate the integration. If the integration constant is enabled, the x-values must be equidistant and monotonic increasing and the y-values must not contain NoValues. This type of integration corresponds to the trapezoidal integration in LabVIEW and uses the following formula. IC stands for integration constant

[IMAGE alt='image' src='../image/f_integral_trapezoid_new.png']

From Version 2014 onwards, DIAdem uses the Simpson rule as an option in order to calculate the integration. The x-values must be equidistant and monotonic increasing and the y-values must not contain NoValues. This type of integration corresponds to the Simpson integration in LabVIEW and uses the following formula. IC stands for integration constant and IE for integration end value

[IMAGE alt='image' src='../image/f_integral_simpson.png']

#### Calculate RMS

The calculate RMS function calculates the floating root mean square (RMS). The RMS values are always positive and provide a measure for the energy of a signal. The following formula calculates the time continuous RMS in the time interval from t1 to t2:

[IMAGE alt='image' src='../image/f_rms_int.gif']

For the time-discrete signal values in the computer, the following formula calculates the RMS:

[IMAGE alt='image' src='../image/f_rms_sum.gif']

DIAdem weights the first and the last signal value with 0.5 and uses the following formula to calculate the RMS:

[IMAGE alt='image' src='../image/f_rms_sum2.gif']

#### Mathematical Functions

Basic Mathematics | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_calculationmanager.htm language=enus -->
## TOPIC 00960: Calculation Manager

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_calculationmanager.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_calculationmanager.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > Calculation Manager

Calculation Manager

Use the Calculation Manager to create calculations, to manage calculations, and to repeat calculations with a minimum of effort. In DIAdem ANALYSIS, select **File»Execute Calculations** to execute calculations and **File»Calculation Manager** to create, edit, and verify these [calculations](../../dlgmaths/calc_formula_dlg/dlgcm_calculationset_dialog.htm).

A calculation can be a simple formula that multiplies the values of a channel, for example. A calculation can be part of an analysis sequence that provides one or more result channels which are used by other calculations. A calculation can be a script, which, depending on the task, executes user-specific formulas, user-defined calculation steps, and analysis functions provided by DIAdem.

A calculation and a calculation script define the calculation rule and the inputs and outputs used by the calculation rule. An input or output can reference a value, a data set property, a channel group property, a channel property, a channel, or a channel list.

When executing a calculation, DIAdem checks whether this calculation requires an output from another calculation as an input, in which case DIAdem executes the other calculation first. DIAdem uses this method to specify the sequence in which calculations are to be executed and can also automatically expand the number of calculations to be executed.

##### Executing Calculations Multiple Times

You can execute calculations and calculation scripts multiple times. If you want to evaluate a series of engine cylinders, you just have to create one calculation that variably uses inputs and outputs, instead of defining a calculation for each cylinder. You can obtain variable inputs and outputs if you insert the expression @@[CCR](../../varoff/ccr.htm)@@ in the input and output references, for example, Cylinder_@@CCR@@ for an input channel. Enter the number of cycles. DIAdem replaces the expression @@CCR@@ with the current cycle number every time a cycle executes. DIAdem evaluates the channels Cylinder_1, Cylinder_2, and Cylinder_3 in three cycles.

##### Validating Calculations

After you have created a calculation, validate whether this calculation can be executed. DIAdem checks the syntax of the calculation rule and whether the input references and the output references of the calculation can be resolved. You can also use the validation script in which you specify further conditions for the executability of the calculation.

DIAdem cannot execute a calculation if the calculation is flagged as an error in the calculation manager. Hover the cursor on the error flag to display a tooltip that describes the cause of the error. Use the functions [Debug Dependent Pre-Calculations](../../dlgmaths/calc_formula_dlg/dlgcm_checkpredependencies_dialog.htm) and [Debug Dependent Post-Calculations](../../dlgmaths/calc_formula_dlg/dlgcm_checkpostdependencies_dialog.htm) to find errors in the interdependent calculations displayed in a tree structure.

##### Managing and Saving Calculations

Create calculation groups to organize calculations and to arrange them in groups. For example, a calculation group Noise can contain all templates for the calculation of noise data.

In the calculation manager, you can save all calculation groups and the associated calculations and also individual calculation groups or calculations as a formula collection in a calculation set. Other users can use these formula collections. If calculations contain specific know-how you do not want to share, save the calculations encrypted. This way other users can execute calculations from the formula collection but cannot view or change them. In the calculation manager you can add existing formula collections to the current calculation set.

Select **Settings»DIAdem Settings** in DIAdem ANALYSIS to specify the calculation set that DIAdem loads when the program launches.

This calculation manager is only available in the versions **DIAdem Advanced** and **DIAdem Professional**. In the **Base Edition**, you can execute but not edit calculation templates that you create and save with the calculation manager.

#### Mathematical Functions

[Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Order Analysis](../genmaths/calc_orderanalysis.htm) | [Statistics](../genmaths/calc_statistics.htm) | [Classifications](../genmaths/calc_classification.htm) | [3D-Data](../genmaths/calc_3d_organisation.htm) | Calculation-Manager

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_channelfunctions.htm language=enus -->
## TOPIC 00961: Channel Functions

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_channelfunctions.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_channelfunctions.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > Channel Functions

Channel Functions

#### Find Peaks

The find peaks function determines a predefined number of minimum or maximum values in a channel. The determined values coincide exactly with channel values. The peak sorting specifies whether the function determines the peaks with the greatest amplitude or the first peaks from the beginning of the channel.

#### Calculate Peaks

The calculate peaks function determines the minimum or maximum values by adjusting a quadratic function sectionwise to the channel values. This makes the function suitable for determining peaks with noisy signals. Because DIAdem interpolates the channel values, the peaks which are found might differ from the channel values.

The interval width specifies the number of values for adjusting the quadratic function. The interval width should not exceed a quarter of the peak width, but if the signals are noise-free, the interval width can be considerably smaller. Select the smallest possible interval width, which is still large enough to preclude incorrect peak values created by noise. If the interval width is very large, the determined amplitude might decrease and the position shift.

The lower limit value specifies the threshold value from which DIAdem evaluates the amplitudes determined by the adjustment of the quadratic function. DIAdem ignores peaks if maximum values are below the limit value or the minimum values exceed the limit value.

#### Event search

Use the Event Search function to check channels for window or slope conditions, which you can connect with Boolean operations such as AND and OR. Use the Event Search function (free formula) to check channels with a free formula for specific events. If you are using the event search in scripts, consider [the results storage in array variables](../genmaths/calc_chneventfindresult.htm).

#### Process NoValues

The process NoValues function deletes NoValues in channels or replaces NoValues with a given value or with a linear interpolation of the neighboring values. [NoValues](../genmaths/calc_novalue_description.htm) are invalid values which DIAdem does not use for calculations and does not display in a report. Use NoValues to eliminate corrupt measurement values from channels.

Use the [CTNV](../../comoff/ctnv.htm) function to replace channel values which overshoot or undershoot limit values with NoValues. Refer to the [Searching for and Interpolating Invalid Values](../../exploff/examples/expl_script_av26.htm) page for an example of how the CTNV function works. Refer to the Help page [Eliminating Outliers Using NoValues](../../procmaths/procmaths/mathsproc_novalue_limit.htm) for a description of how to find outliers that exceed a limit and to replace the outliers with NoValues.

#### Quantize

The quantize functions divides the value range of channels into intervals of equal width in order to map the channel values by rounding on these intervals. The number of steps corresponds to the integer data types 8-bit, 16-bit or 32-bit. After quantifying them, the channels can be saved in a space-saving way.

DIAdem saves the calculated scaling parameters in the variables [ChnStartVal](../../varoff/chnstartval.htm) and [ChnStepWidth](../../varoff/chnstepwidth.htm). If you select **Automatic** in the dialog boxes [DIAdem NAVIGATOR Settings](../../dlgnavigator/dlgnavigator/dlgconfdata_dialog.htm) or [Settings for DIAdem DAT Files](../../dlgnavigator/dlgnavigator/navi_parameters_dat_export_dialog.htm), DIAdem evaluates these scaling parameters when saving TDM files or DAT files.

|  | Note For further information such as mathematical background, input values, directives and rules, refer to the web site RTO-TR-HFM-090 Test Methodology for Protection of Vehicle Occupants against Anti-Vehicular Landmine Effects in paragraph 3.6.2.3 of the third chapter and in paragraph 1.2.2.2 of Appendix I. |
| --- | --- |

#### Resampling

The [Resampling](../genmaths/calc_resample.htm) function converts signals with a high sampling rate to signals with a low sampling rate, or vice versa. Use an interpolation channel or a sampling rate to specify a new time channel.

#### Synchronize Data from Different Files

The [Synchronize Data from Different Files](../genmaths/calc_resample.htm) function removes any offset and, if necessary, maps channels onto a new time channel in order to synchronize channels of different files.

#### Linear Mapping

[Linear Mapping](../genmaths/calc_linearmapping.htm) maps a curve, which is defined point for point by an x-channel and a y-channel, onto a further x-channel, which is the interpolation channel.

#### Channel Functions

[Event Search](../genmaths/calc_chneventfindresult.htm) | [Process NoValues](../genmaths/calc_novalue_description.htm) | [Resampling and Synchronization](../genmaths/calc_resample.htm) | [Linear Mapping](../genmaths/calc_linearmapping.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | Channel Functions | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_compound_classification.htm language=enus -->
## TOPIC 00962: Compound Classification

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_compound_classification.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_compound_classification.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Statistics](../genmaths/calc_overviewstatistics.htm) > Compound Classification

Compound Classification

You use compound classification to classify two interdependent signals. The result of compound classification is a matrix. The matrix has the same number of rows as there are classes in the first signal, and has the same number of columns as the number of classes in the second signal. If you use open boundary classes, DIAdem includes values that are outside all class limits, in the outer classes.

Compound classification offers the following classification methods:

##### Sample

Using the sample count method, DIAdem classifies the related amplitude values of the two signals into the specified classes and increases the value at the corresponding position of the result matrix.

##### Maximum Value Memory

Using the maximum value memory method, DIAdem determines for each signal the maximum value for the number of amplitude values specified by the clock. DIAdem classifies the maximum values of both signals independently of each other, and increases the value by one at the corresponding position in the result matrix. If you enter the value 1 as the clock, DIAdem counts each value. The maximum value memory method is the same as the sample count method.

##### Time at Level1:

Using the time at level1 method, DIAdem determines for each separate signal how long the signal remains in each class and writes the time at the corresponding position in the result matrix. DIAdem assumes that the intervals between the points on the time axis are equidistant. If this is not the case, use the time at level2 method.

##### Time at Level2

Using the time at level2 method, DIAdem determines for each separate signal how long the signal remains in each class and writes the time at the corresponding position in the result matrix. DIAdem does not assume that the intervals on the time axis are equidistant but uses the time values that are stored in the x-channel. If you classify data with an equidistant time axis, time at level1 is faster.

**References**

[1] DIN 45667: Classification Methods for Evaluation of Random Vibrations, 1969.

#### Statistics

[Characteristic Statistical Values](../genmaths/calc_statistics.htm) | [Process Capability](../genmaths/calc_spc.htm) | [Classifications](../genmaths/calc_classification.htm) | [Single Classification](../genmaths/calc_single_classification.htm) | [Reducing Classification](../genmaths/calc_reducing_classification.htm) | Compound Classification | [Rainflow Classification](../genmaths/calc_rainflow.htm) | [Example Rainflow Classification](../genmaths/calc_rainflow_example.htm) | [Algorithm Rainflow Classification](../genmaths/calc_rainflow_algorithm.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_filterfir_iir.htm language=enus -->
## TOPIC 00963: IIR Filters and FIR Filters

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_filterfir_iir.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_filterfir_iir.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) > IIR Filters and FIR Filters

IIR Filters and FIR Filters

The impulse response or the frequency response classify digital filters. An impulse response is the response of a filter to an input impulse: x[0]=1 and x[i]=0 for all i≠0. The Fourier Transform of the impulse response is the frequency response of the filter which illustrates its gain when the frequencies differ.

If the impulse response of the filter falls to zero after a finite period of time, it is an FIR (Finite Impulse Response) filter. However, if the impulse response exists indefinitely, it is an IIR (Infinite Impulse Response) filter. How the output values are calculated determines whether the impulse response of a digital filter falls to zero after a finite period of time. For FIR filters the output values depend on the current and the previous input values, whereas for IIR filters the output values also depend on the previous output values.

#### Advantages and Disadvantages of FIR and IIR Filters

The advantage of IIR filters over FIR filters is that IIR filters usually require fewer coefficients to execute similar filtering operations, that IIR filters work faster, and require less memory space.

The disadvantage of IIR filters is the nonlinear phase response. IIR filters are well suited for applications that require no phase information, for example, for monitoring the signal amplitudes. FIR filters are better suited for applications that require a linear phase response.

#### IIR Filters

The output values of IIR filters are calculated by adding the weighted sum of previous and current input values to the weighted sum of previous output values. If the input values are x<sub>i</sub> and the output values y<sub>i</sub>, the difference equation defines the IIR filter:

[IMAGE alt='image' src='../image/f_iir.gif']

The number of forward coefficients N<sub>x</sub> and the number of reverse coefficients N<sub>y</sub> is usually equal and is the filter order. The higher the filter order, the more the filter resembles an ideal filter. This is illustrated in the following figure of a frequency response of lowpass Butterworth filters with different orders. The steeper the filter gain falls, the higher the filter order is.

[IMAGE alt='image' src='../image/task_butterworth.gif']

##### Butterworth Filters

The frequency response of the Butterworth filter has no ripples in the passband and the stopband. Therefore it is called a maximally flat filter. The advantage of Butterworth filters is the smooth, monotonically decreasing frequency response in the transition region.

##### Chebyshev Filters

If the filter is the same, the frequency response of the Chebyshev filter has a norrower transition range than the frequency response of the Butterworth filter which results in a passband with more ripples. The frequency response characteristics of Chebyshev filters have an equiripple magnitude response in the passband, monotonically decreasing magnitude response in the stopband, and a sharper rolloff in the transition region as compared to Butterworth filters of the same order.

##### Bessel Filters

The frequency response of Bessel filters is similar to the Butterworth filter smooth in the passband and in the stopband. If the filter order is the same, the stopband attenuation of the Bessel filter is much lower than that of the Butterworth filter. Of all filter types the Bessel filter has the widest transition range if the filter order is fixed.

The following figure compares the frequency response with a fixed filter order of the IIR filter types Butterworth, Chebyshev, and Bessel which DIAdem supports.

[IMAGE alt='image' src='../image/task_frequency_overall_filter_response.gif']

#### FIR Filters

FIR filters are also known as non-recursive filters, convolution filters, or moving-average filters because the output values of an FIR filter are described as a finite convolution:

[IMAGE alt='image' src='../image/f_fir.gif']

The output values of a FIR filter depend only on the current and past input values. Because the output values do not depend on past output values, the impulse response decays to zero in a finite period of time. FIR filters have the following properties:

- FIR filters can achieve linear phase response and pass a signal without phase distortion.
- They are easier to implement than IIR filters.

The selection of the window function for a FIR filter is similar to the choice between Chebyshev and Butterworth IIR filters where you have to choose between side lobes near the cutoff frequencies and the width of the transition region.

#### Signal Analysis

[Fourier Transform](../genmaths/calc_fouriertransform.htm) | [FFT Calculations](../genmaths/calc_fft.htm) | [Oscillation Analysis](../genmaths/calc_singletone_sinad.htm) | [Digital Filters](../genmaths/calc_digitalfilter.htm) | IIR and FIR Filters | [Correlation](../genmaths/calc_correlation.htm) | [Frequency-Weighted Acceleration](../genmaths/calc_weightedacceleration.htm) | [Order Analysis](../genmaths/calc_orderanalysis.htm) | [Order Analysis Methods Based on Resampling](../genmaths/calc_oa_resampling.htm) | [Shock Response Spectrum (SRS)](../genmaths/calc_shockresponse.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_fouriertransform.htm language=enus -->
## TOPIC 00964: Fourier Transform (DFT and FFT)

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_fouriertransform.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_fouriertransform.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) > Fourier Transform (DFT and FFT)

Fourier Transform (DFT and FFT)

The sampling required for the digitalization of a signal determines the representation of the signal in the time domain. The time domain representation shows the amplitudes of the signal during the time it was being sampled. For many applications detailed information on the frequency components of the signal is important for a deeper understanding of the signal and the system which generates the signal. The display of the frequency components of a signal is called frequency domain representation.

#### Discrete Fourier Transform (DFT)

The discrete Fourier transform (DFT) algorithm transforms samples of signals from the time domain into the frequency domain. The DFT is widely used in the fields of spectral analysis, applied mechanics, acoustics, medical imaging, numerical analysis, instrumentation, and telecommunications.

The DFT of a time-based signal with N samples produces a frequency range representation with also N values. If the signal is sampled with a sampling rate of f<sub>s</sub>, the time interval between the samples is Δt:

[IMAGE alt='image' src='../image/f_dft1.gif']

If the N samples are x<sub>i</sub> with 0 ≤ i ≤ N–1, the DFT is calculated with the following formula:

[IMAGE alt='image' src='../image/f_dft2.gif']

The result (X<sub>k</sub>, 0 ≤ k ≤ N–1) is the frequency range representation of x<sub>i</sub>. Analogous to the time interval Δt between the samples of x in the time domain, a frequency interval of Δf is produced between the components of X in the frequency domain

[IMAGE alt='image' src='../image/f_dft3.gif']

Δf is also known as the frequency resolution. To increase the frequency resolution and to thus decrease Δf, increase the number of sampling rates N with a constant value f<sub>S</sub> or decrease the sampling rate f<sub>S</sub> with a constant value N.

N samples of the input signal in the time domain equal N values in the frequency domain representation. The DFT equation illustrates that regardless of whether the input signal x<sub>i</sub> is real or complex, X<sub>k</sub> is complex even if the imaginary part is zero. The values amplitude and phase can also define the frequency domain representation.

#### Fast Fourier Transform (FFT)

The DFT calculation for N samples requires approximately N·N complex calculation operations and is a time intensive and a memory intensive calculation. If the length of the sequence is a power of 2,

[IMAGE alt='image' src='../image/f_fft1.gif']

the DFT can be calculated with approximately N·log<sub>2</sub>(N) operations. The algorithms for this special case are called fast Fourier transform (FFT).

The advantages of the FFT include speed and memory efficiency. The DFT can process sequences of any size efficiently but is slower than the FFT and requires more memory, because it saves intermediate results while processing. DIAdem uses the fastest method depending on the number of samples and can process effectively input sequences that do not have a length of the power of 2.

#### Signal Analysis

Fourier Transform | [FFT Calculations](../genmaths/calc_fft.htm) | [Oscillation Analysis](../genmaths/calc_singletone_sinad.htm) | [Digital Filters](../genmaths/calc_digitalfilter.htm) | [IIR and FIR Filters](../genmaths/calc_filterfir_iir.htm) | [Correlation](../genmaths/calc_correlation.htm) | [Frequency-Weighted Acceleration](../genmaths/calc_weightedacceleration.htm) | [Order Analysis](../genmaths/calc_orderanalysis.htm) | [Order Analysis Methods Based on Resampling](../genmaths/calc_oa_resampling.htm) | [Shock Response Spectrum (SRS)](../genmaths/calc_shockresponse.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_gaussianpeakfit.htm language=enus -->
## TOPIC 00965: Gaussian Curve Fitting

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_gaussianpeakfit.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_gaussianpeakfit.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Curve Fitting](../genmaths/calc_overviewcurves.htm) > Gaussian Curve Fitting

Gaussian Curve Fitting

The Gaussian curve fitting approximates a curve which is specified point for point by an x-channel and a y-channel, with a Gaussian curve according to the following formula

[IMAGE alt='image' src='../image/f_gauss1.gif']

The amplitude is a, the center is µ, and the standard deviation of the Gaussian curve is σ. Gaussian curve fitting has three methods for fitting a curve to the input data:

- Least error squares
- Least absolute residual
- Bisquare

The least error squares method minimizes the following quality criterion

[IMAGE alt='image' src='../image/f_gauss2.gif']

and returns good results if the input data is disturbed by noise.

The least absolute residual method minimizes the following quality criterion

[IMAGE alt='image' src='../image/f_gauss3.gif']

and returns better results if the input data has outliers.

The bisquare method calculates the curve fitting iterative according to the following flowchart

[IMAGE alt='image' src='../image/loc_eps_gaussian_peak_fit_flowchart.gif']

and returns the best results for the input data with outliers. The tolerance determines when the iterative curve fitting of the amplitude, center, and standard deviation ends for the bisquare method. If the relative difference of the residual undershoots the tolerance in two successive cycles, the curve fitting stops.

DIAdem generates the evaluation points either through equidistant partition of the whole x-range or of the individual intervals of the x-range, or uses the evaluation points from a specified channel. DIAdem then calculates the y-values of the approximation function for all evaluation points.

#### Curve Fitting

[Smooth Functions](../genmaths/calc_smoothfunctions.htm) | [Regression](../genmaths/calc_regression.htm) | [Approximation](../genmaths/calc_approximation.htm) | [Non-Linear Curve Fitting](../genmaths/calc_nonlinearcurvefit.htm) | Gaussian Curve Fitting | [General LS-Linear Fitting](../genmaths/calc_genlsfit.htm) | [Splines in DIAdem](../genmaths/calc_splines.htm) | [Non-Parametrical Splines](../genmaths/calc_nonparam_splines.htm)| [Parametrical Splines](../genmaths/calc_param_splines.htm) | [Akima Subsplines](../genmaths/calc_akima_splines.htm) | [Circle Approximation](../genmaths/calc_circles.htm) | [Envelope Curves](../genmaths/calc_envelopecurves.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_genlsfit.htm language=enus -->
## TOPIC 00966: General LS Linear Fitting

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_genlsfit.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_genlsfit.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Curve Fitting](../genmaths/calc_overviewcurves.htm) > General LS Linear Fitting

General LS Linear Fitting

The general LS linear fitting specifies the k-dimensional coefficients of a linear fitting which describes a k-dimensional curve. DIAdem uses the least squares method and offers the following methods to solve the occurring system of equations

- SVD
- Givens
- Givens2
- Householder
- LR decomposition ( also called triangular decomposition)
- Cholesky
- SVD for rank deficient matrix H

DIAdem calculates a result channel with the coefficients and optionally the covariance matrix. The weighting channel must be the same length as the y-channel. The number of calculated coefficients is equal the number of columns of the specified matrix. DIAdem saves the mean squared error in the GenLSFitMSE variable.

**Example**

Suppose you want to estimate the total cost of a production of baked products, using the quantity produced, X1, and the price of one pound of flour, X2 in Dollars.

| Cost (Dollars) Y | Quantity X1 | Flour Price X2 |
| --- | --- | --- |
| 150 | 295 | 3.00 |
| 75 | 100 | 3.20 |
| 120 | 200 | 3.10 |
| 300 | 700 | 2.80 |
| 50 | 60 | 2.50 |

You want to fit the coefficients to the equation

**Y** = *b*<sub>0</sub> + *b*<sub>1</sub>**X1** + *b*<sub>2</sub>**X2**

Fill the first column of matrix H with ones because the coefficient *b*<sub>0</sub> is not multiplied by any independent variable.

[IMAGE alt='image' src='../image/f_genlsfit2.gif']

The general LS linear fitting returns the following result to calculate the total cost of the bakery production

**Y** = –20.34 + 0.38**X1** + 19.05**X2**

#### Curve Fitting

[Smooth Functions](../genmaths/calc_smoothfunctions.htm) | [Regression](../genmaths/calc_regression.htm) | [Approximation](../genmaths/calc_approximation.htm) | [Non-Linear Curve Fitting](../genmaths/calc_nonlinearcurvefit.htm) | [Gaussian Curve Fitting](../genmaths/calc_gaussianpeakfit.htm) | General LS-Linear Fitting | [Splines in DIAdem](../genmaths/calc_splines.htm) | [Non-Parametrical Splines](../genmaths/calc_nonparam_splines.htm)| [Parametrical Splines](../genmaths/calc_param_splines.htm) | [Akima Subsplines](../genmaths/calc_akima_splines.htm) | [Circle Approximation](../genmaths/calc_circles.htm) | [Envelope Curves](../genmaths/calc_envelopecurves.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_linearmapping.htm language=enus -->
## TOPIC 00967: Linear Mapping

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_linearmapping.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_linearmapping.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Channel Functions](../genmaths/calc_channelfunctions.htm) > Linear Mapping

Linear Mapping

Linear mapping maps a curve, which is defined point for point by an x-channel and a y-channel, onto a further x-channel, which is the interpolation channel. For example, linear mapping can convert several signals acquired with different sampling rates onto a joint x-channel. This process is also called down-sampling or up-sampling. Linear mapping offers different mapping modes for analog curves, spike curves, stair curves, and stair/analog curves.

Linear mapping maps the new interpolation points in the joint area of the x-channel and the interpolation channel for the different mapping modes according to the following rules, whereby the original x-values are x<sub>i</sub> and original y-values are y<sub>i</sub> = f(x<sub>i</sub>).

- The analog mapping mode creates interim values by interpolating linearly according to the following formula: 
 [IMAGE alt='image' src='../image/f_linmapanalogue.gif']
- The spike mapping mode assigns the spikes to the nearest interpolation points of the new x-channel and sets the other values to zero: 
 [IMAGE alt='image' src='../image/f_linmapspike.gif']
- The stair mapping mode continues the function values for the increasing x-values after every slope on a constant level, so that the level is maintained and the value does not return to zero as is the case in spike curves.
- The stair/analog mapping mode maintains the low level at least up to the original x-value, unlike normal stair curves. 
 [IMAGE alt='image' src='../image/f_linmapstairana.gif']

If the original y-channel contains NoValues, linear mapping can replace these NoValues. For the **Analog** mapping mode, linear mapping executes a linear interpolation. For the **Spike** mapping mode, linear mapping replaces the NoValues with zeros. For the **Stair** mapping mode, linear mapping replaces the NoValues with the last level value. If the Novalues are not to be replaced, linear mapping adopts the NoValues in the new y-channel.

For the digital mapping modes **Spike** and **Stair**, the maximum step width of the new interpolation channel must be smaller than half the minimum step width of the original x-channel because otherwise spikes or level changes might be lost. If the step width of the interpolation channel is too large, DIAdem might assign two values y(x<sub>a</sub>) and y(x<sub>b</sub>) to the same interpolation value x<sub>1</sub>. If this is the case, DIAdem adopts the y-value, whose x-value is closer to the new interpolation point x<sub>1</sub>. If both curve points have the same distance, DIAdem adopts the y-value of the smaller x-value.

If the interpolation channel contains x-values outside the x-range of the existing curve, linear mapping can extrapolate the curve on the extended x-range. If analog curves exceed the original x-area, they are continued either by a freely selected numeric value, by the two y-values of the boundary values, or by a line with the slope at the respective boundary values. Spike functions and stair functions are continued with the value zero or a freely selected numeric value.

#### Channel Functions

[Event Search](../genmaths/calc_chneventfindresult.htm) | [Process NoValues](../genmaths/calc_novalue_description.htm) | [Resampling and Synchronization](../genmaths/calc_resample.htm) | Linear Mapping |

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_nonlinearcurvefit.htm language=enus -->
## TOPIC 00968: Non-Linear Curve Fitting

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_nonlinearcurvefit.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_nonlinearcurvefit.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Curve Fitting](../genmaths/calc_overviewcurves.htm) > Non-Linear Curve Fitting

Non-Linear Curve Fitting

Non-linear curve fitting calculates a non-linear function that fits a curve, which is defined point for point by an x-channel and a y-channel, according to the least error squares approach. The calculated fitting function connects x and y with a formula and enables the calculation of the y-values for any x-values. After the setup function is specified, the non-linear curve fitting calculates first the setup coefficients and then the y-values of the fitting function at the specified evaluation points.

The setup function specifies a functional context with the format y = f(x,a<sub>i</sub>) in VBS syntax. After specifying the independent variable x, DIAdem recognizes the setup coefficients a<sub>i</sub> that need to be specified. The non-linear curve fitting calculates, using the Levenberg-Marquardt algorithm, the setup coefficients that minimize the weighted, mean squared error between the curve and the approximation function. Here, w<sub>i</sub> indicates the weights, y<sub>i</sub> the points of the given curve, and f<sub>i</sub> the values of the approximation function.

[IMAGE alt='image' src='../image/f_nonlinearcurvefit1.gif']

The non-linear curve fitting does not interpolate, which means that the fitting function does not pass through all given points. If the non-linear curve fitting does not find a solution and generates an error message, you must change the initialization of the setup coefficients or adapt the setup function.

DIAdem generates the evaluation points through equidistant partition of the whole x-range or of the individual intervals of the x-range, or uses the evaluation points from a specified channel. DIAdem then calculates the y-values of the approximation function for all evaluation points.

The non-linear curve fitting can calculate the covariance matrix C, where c<sub>jk</sub> determines the covariance between the j-th and the k-th setup coefficient, and stores the results in columns in the Data Portal.

**Example**

The example **Help»Examples»Mathematics»Non-Linear Curve Fitting** shows how various distribution functions are fitted to measured spectral data. Start the example first to familiarize yourself with the task.

Then select **Curve Fitting»Non-Linear Curve Fitting** in DIAdem ANALYSIS. Specify the setup formula A*xh^2/((x-x0)^2+xh^2) to adapt a Lorentz curve to the spectral values given by the Frequency and Intensity channels. The independent variable is x, the setup coefficients that need to be calculated are A, xh, and x0.

With the default initialization value of 1 for all setup coefficients, the non-linear curve fitting results in a mean squared error of 130826. Increasing the number of iterations does not bring an improvement, either. With a start value of 1000 for A and a number of iterations of 100, non-linear curve fitting achieves a much better match that also results in a smaller error of 7194.

#### Curve Fitting

[Smooth Functions](../genmaths/calc_smoothfunctions.htm) | [Regression](../genmaths/calc_regression.htm) | [Approximation](../genmaths/calc_approximation.htm) | Non-Linear Curve Fitting | [Gaussian Curve Fitting](../genmaths/calc_gaussianpeakfit.htm) | [General LS-Linear Fitting](../genmaths/calc_genlsfit.htm) | [Splines in DIAdem](../genmaths/calc_splines.htm) | [Non-Parametrical Splines](../genmaths/calc_nonparam_splines.htm)| [Parametrical Splines](../genmaths/calc_param_splines.htm) | [Akima Subsplines](../genmaths/calc_akima_splines.htm) | [Circle Approximation](../genmaths/calc_circles.htm) | [Envelope Curves](../genmaths/calc_envelopecurves.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_overview.htm language=enus -->
## TOPIC 00969: DIAdem ANALYSIS

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

DIAdem ANALYSIS

DIAdem ANALYSIS

Use DIAdem ANALYSIS to execute mathematical data analyses. DIAdem ANALYSIS offers you the following functions:

|  | Use the Basic Mathematics functions to execute basic mathematical calculations. |
| --- | --- |
|  | Use the Channel Functions to create, to convert, and to analyze channels. |
|  | Use the Curve Fitting functions, for example, to smooth curves, to approximate curves, and to approximate curves using splines. |
|  | Use the Signal Analysis functions, for example, to run fast Fourier transforms (FFT) and order analyses. |
|  | Use the Statistics functions to calculate characteristic statistical values and to run classifications. |
|  | Use the 3D Basic functions to convert, transpose, and sort matrices. |
|  | Use the 3D»Arithmetic functions to calculate matrices, vectors, and scalars; to normalize, relativize, and integrate matrices; and to calculate sums and extreme values of matrices. |
|  | Use the 3D»Surfaces functions to interpolate and to approximate 3D data, or to calculate contours and the envelope. |
|  | Use the Geo functions functions to execute, for example, humidity conversions or altitude profile calculations. |
|  | Use the RDE Analysis functions to execute evaluations of vehicle emissions. |
|  | Use the Crash Analysis functions to run calculations in the vehicle safety area. |
|  | Use the Calculator to enter and calculate a formula. |
|  | Use the Calculation Manager to create calculations, to manage calculations, and to repeat calculations. |
|  | Enable the Calculate Quantity-Based button, to include all units of the Units Catalog in the calculation. |

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_overview3d.htm language=enus -->
## TOPIC 00970: 3D Data Analysis

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_overview3d.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_overview3d.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > 3D Data Analysis

3D Data Analysis

DIAdem can manage, analyze, and display three-dimensional data as value triplets and matrices. The [Convert Matrix](../genmaths/calc_3d_organisation.htm) function converts the data structure from triplet to matrix and vice versa.

The [3D Basic Functions](../genmaths/calc_3dbasicfunctions.htm) in DIAdem include functions for appending and extracting submatrices and for sorting and transposing matrices.

The [3D Arithmetic](../genmaths/calc_3darithmetics.htm) functions can process matrices, vectors, or scalar variables arithmetically. DIAdem calculates the addition, subtraction, and division of matrices componentwise so that one element of matrix A is calculated with one element of matrix B. When DIAdem multiplies a matrix by a second matrix or by a vector, DIAdem can also calculate algebraically so that one row of matrix A is multiplied by one column of matrix B.

The [3D Basic Mathematics](../genmaths/calc_3dbasicmath.htm) functions calculate basic matrix values. DIAdem can normalize and relativize matrices, summate and integrate matrix values, and calculate the extreme values of matrices.

The [3D Surface Calculation](../genmaths/calc_3dsurfaces.htm) functions can interpolate or approximate 3D data through surfaces. The interpolating surface goes exactly through all specified nodes whereas the approximating surface minimizes the distance to the nodes for a specified setup function. DIAdem only evaluates the surface inside the specified or calculated hulls and calculates the contour lines on the surfaces.

#### 3D Data Analysis

[3D-Data Structure](../genmaths/calc_3d_organisation.htm) | [3D-Basic Functions](../genmaths/calc_3dbasicfunctions.htm) | [3D-Arithmetic](../genmaths/calc_3darithmetics.htm) | [3D-Basic Mathematics](../genmaths/calc_3dbasicmath.htm) | [3D-Surface Calculations](../genmaths/calc_3dsurfaces.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | 3D Data Analysis | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_overviewcurves.htm language=enus -->
## TOPIC 00971: Curve Fitting

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_overviewcurves.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_overviewcurves.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > Curve Fitting

Curve Fitting

DIAdem has two functions for smoothing signals. The [Smooth](../genmaths/calc_smoothfunctions.htm) function calculates an unweighted moving average. The [Savitzky-Golay Filter](../genmaths/calc_smoothfunctions.htm) uses a specific weighting of the values for averaging and can thereby better retain the characteristic properties of the original curve.

The [Regression](../genmaths/calc_regression.htm) and the [Approximation](../genmaths/calc_approximation.htm) functions approximate a curve which is specified point for point by an x-channel and a y-channel. The calculated function connects x and y with a formula and then enables the calculation of the y-values for any x-values.

[Non-Linear Curve Fitting](../genmaths/calc_nonlinearcurvefit.htm) calculates a non-linear function that fits a curve, which is defined point for point by an x-channel and a y-channel, according to the least error squares approach. The calculated fitting function connects x and y with a formula and enables the calculation of the y-values for any x-values.

The [Gaussian Curve Fitting](../genmaths/calc_gaussianpeakfit.htm) approximates a curve progression which is specified point for point by an x-channel and a y-channel, with a Gaussian curve. DIAdem uses the least square method, the least absolute residual method, or the bisquare method to calculate the Gaussian curve.

[General LS Linear Fitting](../genmaths/calc_genlsfit.htm) uses k-dimensional linear curve values and k-dimensional coefficients to fit a curve. DIAdem uses the least square method to best fit the k-dimensional curve.

Splines are piecewise polynomial functions. DIAdem offers interpolating splines that pass through the specified points exactly, and approximating splines, which fit a compensation curve to the specified points. DIAdem calculates [three types of splines:](../genmaths/calc_splines.htm) non-parametrical splines, parametrical splines, and Akima subsplines.

[Non-Parametrical Splines](../genmaths/calc_nonparam_splines.htm) calculate curves when the x-values are strictly monotonic. [Parametrical Splines](../genmaths/calc_param_splines.htm) calculate curves also with non-monotonic x-values, for example, for closed curves. [Akima Subsplines](../genmaths/calc_akima_splines.htm) are once continuously differentiable at the interpolation points and suited for curves with jump discontinuities.

The [Circle Approximation](../genmaths/calc_circles.htm) calculates for points that are in a cartesian coordinates system the regression circle, the maximum incircle, the minimum circumcircle, and the concentric incircle and circumcircle.

The minimum values and the maximum values of a curve determine the [Envelope Curves](../genmaths/calc_envelopecurves.htm). The upper hull curve connects the maximum values and the lower hull curve connects the minimum values.

#### Curve Fitting

[Smooth](../genmaths/calc_smoothfunctions.htm) | [Regression](../genmaths/calc_regression.htm) | [Approximation](../genmaths/calc_approximation.htm) | [Non-Linear Curve Fitting](../genmaths/calc_nonlinearcurvefit.htm) | [Gaussian Curve Fitting](../genmaths/calc_gaussianpeakfit.htm) | [General LS-Linear Fitting](../genmaths/calc_genlsfit.htm) | [Splines in DIAdem](../genmaths/calc_splines.htm) | [Non-Parametrical Splines](../genmaths/calc_nonparam_splines.htm)| [Parametrical Splines](../genmaths/calc_param_splines.htm) | [Akima Subsplines](../genmaths/calc_akima_splines.htm) | [Circle Approximation](../genmaths/calc_circles.htm) | [Envelope Curves](../genmaths/calc_envelopecurves.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | Curve Fitting | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_overviewsignalanalysis.htm language=enus -->
## TOPIC 00972: Signal Analysis

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_overviewsignalanalysis.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_overviewsignalanalysis.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > Signal Analysis

Signal Analysis

The [Discrete Fourier Transform (DFT)](../genmaths/calc_fouriertransform.htm) algorithm transforms sampling rates of signals from the time domain into the frequency domain. The DFT is widely used in the fields of spectral analysis, applied mechanics, acoustics, medical imaging, numerical analysis, instrumentation, and telecommunications.

DIAdem has two special functions for analyzing oscillations. The [Characterize Oscillation](../genmaths/calc_singletone_sinad.htm) function specifies in a signal the frequency with the greatest amplitude. The [SINAD Analysis](../genmaths/calc_singletone_sinad.htm) function (signal-to-noise and distortion ratio) calculates the ratio of total signal power to distortion signal power.

[Digital Filters](../genmaths/calc_digitalfilter.htm) change the frequency of a signal and are often used in signal processing. In technical applications filters are used for removing noise or humming sounds and for decimating signals by sending the signals through a lowpass filter and then reducing the sampling rate.

Digital filters are classified [IIR Filters and FIR Filters](../genmaths/calc_filterfir_iir.htm) depending on the impulse response. If the impulse response of the filter falls to zero after a finite period of time, it is an FIR (Finite Impulse Response) filter. However, if the impulse response exists indefinitely, it is an IIR (Infinite Impulse Response) filter.

The [Correlation](../genmaths/calc_correlation.htm) calculates the similarity of signals. The autocorrelation compares the signal with a time-delayed copy of the signal. The cross correlation compares the similarity of two different signals.

The [Frequency-Weighted Acceleration](../genmaths/calc_weightedacceleration.htm) calculates how intensive mechanical vibrations affect the human body at the workplace or in vehicles. The frequency-weighted signals help come to comparable and reliable conclusions for various shock measurements and vibration measurements before a frequency analysis is executed.

The [Order Analysis](../genmaths/calc_orderanalysis.htm) is a technique for analyzing noise and vibration signals in rotating or reciprocating machinery. Some examples of rotating or reciprocating machinery include aircraft and automotive engines, compressors, turbines, and pumps. Order analysis techniques are suitable for analyzing noise and vibration signals when the rotational speed changes over time. Order components take place n times per revolution and are periodic in rotational angle. In order to acquire even-angle samples, you must adjust the sampling rate according to the rotational speed. Typically, you acquire noise and vibration signals with a fixed sampling rate and then use software to [resample](../genmaths/calc_oa_resampling.htm) the signal with the synchronous sampling rate.

[The Shock Response Spectrum (SRS)](../genmaths/calc_shockresponse.htm) describes the answer of multiple single-degree-of-freedom systems with different natural harmonics to a measured acceleration signal. The SRS is calculated in accordance with the ISO norm 18431-4:2007.

#### Signal Analysis

[Fourier Transform](../genmaths/calc_fouriertransform.htm) | [FFT Calculations](../genmaths/calc_fft.htm) | [Oscillation Analysis](../genmaths/calc_singletone_sinad.htm) | [Digital Filters](../genmaths/calc_digitalfilter.htm) | [IIR and FIR Filters](../genmaths/calc_filterfir_iir.htm) | [Correlation](../genmaths/calc_correlation.htm) | [Frequency-Weighted Acceleration](../genmaths/calc_weightedacceleration.htm) | [Order Analysis](../genmaths/calc_orderanalysis.htm) | [Order Analysis Methods Based on Resampling](../genmaths/calc_oa_resampling.htm) | [Shock Response Spectrum (SRS)](../genmaths/calc_shockresponse.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | Signal Analysis | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_overviewstatistics.htm language=enus -->
## TOPIC 00973: Statistics

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_overviewstatistics.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_overviewstatistics.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > Statistics

Statistics

The [characteristic statistical values](../genmaths/calc_statistics.htm) calculated with the statistics functions characterize the properties of data series, for example, of measurement values. You use characteristic statistical values to compress data series, which makes the data series easier to compare to other data series.

The [Process Capability (SPC)](../genmaths/calc_spc.htm) calculation helps to continuously improve the quality and productivity of processes, for example, in manufacturing. Diadem calculates the mean, the standard deviation, and the capability indexes of a process.

[Classifications](../genmaths/calc_classification.htm) are statistical methods for examining the amplitude values of random oscillations. To execute a classification, first break down the amplitude range of the oscillation signal into classes. Then select the classification method, which counts the number of events in each class. The result of the classification is a frequency distribution, which is also called a collective.

Use [Single Classification](../genmaths/calc_single_classification.htm) to determine different single-parameter frequency distributions. In all classification methods you first specify the classes and, depending on the classification method, additional parameters such as the reference line or the hysteresis.

[Reducing Classification](../genmaths/calc_reducing_classification.htm) is a combination of classification and data reduction. DIAdem breaks the x-values down into classes and determines for the associated y-values either the mean, the minimum, the maximum, the sum, or the number of values. Reducing classification can simultaneously classify several y-channels for one x-channel. Reducing classification is therefore suitable for reducing a signal that is defined by x-values and y-values, to a specified number of value pairs.

Use [Compound Classification](../genmaths/calc_compound_classification.htm) to classify two interdependent signals. The result of compound classification is a matrix. The matrix has the same number of rows as there are classes in the first signal, and has the same number of columns as the number of classes in the second signal.

Use [Rainflow Classification](../genmaths/calc_rainflow.htm) to execute fatigue analysis on components. Measured load-time functions such as displacement, expansion, force, or moment, generally oscillate and cannot be subject to a complete mathematical description. However, to estimate the durability of components, the amplitude and the frequency of the cycles generally supply sufficient information. As an example of [Rainflow Classification](../genmaths/calc_rainflow_example.htm), the load-time function has five classes and is classified in a transition matrix and in a rainflow matrix. Finally the [Algorithm of the Rainflow Classification](../genmaths/calc_rainflow_algorithm.htm) is described and illustrated in a flow chart.

#### Statistics

[Characteristic Statistical Values](../genmaths/calc_statistics.htm) | [Process Capability](../genmaths/calc_spc.htm) | [Classifications](../genmaths/calc_classification.htm) | [Single Classification](../genmaths/calc_single_classification.htm) | [Reducing Classification](../genmaths/calc_reducing_classification.htm) | [Compound Classification](../genmaths/calc_compound_classification.htm) | [Rainflow Classification](../genmaths/calc_rainflow.htm) | [Example Rainflow Classification](../genmaths/calc_rainflow_example.htm) | [Algorithm Rainflow Classification](../genmaths/calc_rainflow_algorithm.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | Statistics | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_rainflow_algorithm.htm language=enus -->
## TOPIC 00974: Algorithm of the Rainflow Classification

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_rainflow_algorithm.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_rainflow_algorithm.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Statistics](../genmaths/calc_overviewstatistics.htm) > Algorithm of the Rainflow Classification

Algorithm of the Rainflow Classification

In a rainflow classification, DIAdem first divides the load-time function into n classes. Classes are half-open intervals, which means that a value on the class boundary is included in the next higher class. Rainflow classification includes a value from the load-time function only if the absolute difference between the value and the preceding value in time is greater than a hysteresis Eps and the two values are in different classes (condition A).

If the setting **Use the first and last value as reversal points** is disabled, the first reversal point which crosses a class limit is counted as the first valid value in the load time function (X<sub>1</sub>). The last value of the load-time function is invalid. If the setting is enabled, DIAdem uses the first and the last value as reversal points. DIAdem uses the valid values from the load-time function to construct the residue vector X<sub>i</sub>. The closed load cycles are eliminated from the residue vector and are counted to the rainflow matrix (rain). Additionally all class cycles (from => to) are counted to the transition matrix (trans).

If there are no more valid values in the load-time function (EOF = true), the non-closed load cycles remain in the residue vector. In DIAdem you select whether residues are closed and are counted. If there is an odd number of remaining values in the residue vector, the last value is not included, because there is no target class.

The following graphic shows the flow chart of the rainflow classification in DIAdem.

[IMAGE alt='image' src='../image/rainflow_algorithm.png']

#### Statistics

[Characteristic Statistical Values](../genmaths/calc_statistics.htm) | [Process Capability](../genmaths/calc_spc.htm) | [Classifications](../genmaths/calc_classification.htm) | [Single Classification](../genmaths/calc_single_classification.htm) | [Reducing Classification](../genmaths/calc_reducing_classification.htm) | [Compound Classification](../genmaths/calc_compound_classification.htm) | [Rainflow Classification](../genmaths/calc_rainflow.htm) | [Example Rainflow Classification](../genmaths/calc_rainflow_example.htm) | Algorithm Rainflow Classification

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_rainflow_example.htm language=enus -->
## TOPIC 00975: Example of Rainflow Classification

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_rainflow_example.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_rainflow_example.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Statistics](../genmaths/calc_overviewstatistics.htm) > Example of Rainflow Classification

Example of Rainflow Classification

As an example of a rainflow classification, the load-time function shown in the diagram is classified in a rainflow matrix and in a transition matrix. For clarity, the load-time function is divided into five classes only. For DIAdem the first reversal point of the load-time function with the value 1 is the first valid value and the last but one point of the load-time function with the value 2 is the last valid value (if the setting **Use first and last value as reversal points** is disabled).

[IMAGE alt='image' src='../image/rainflowloadtimefunctionclasses.gif']

#### Transition Matrix

For the transition matrix DIAdem specifies the following 14 positive and negative slopes:

```text
 1 → 4, 4 → 3, 3 → 4, 4 → 2, 2 → 4, 4 → 3, 3 → 5, 5 → 1, 1 → 2, 2 → 1, 1 → 4, 4 → 2, 2 → 3, 3 → 2
```

and counts the start class and the target class of each slope to the transition matrix:

|  |  | Target class |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 1 | 2 | 3 | 4 | 5 |
| Start class | 1 | 0 | 1 | 0 | 2 | 0 |
| 2 | 1 | 0 | 1 | 1 | 0 |  |
| 3 | 0 | 1 | 0 | 1 | 1 |  |
| 4 | 0 | 2 | 2 | 0 | 0 |  |
| 5 | 1 | 0 | 0 | 0 | 0 |  |

#### Rainflow Matrix

For the rainflow matrix DIAdem enters the minimum values and the maximum values of the load-time function into the residue vector and determines the closed load cycles. A load cycle is closed when the second strain load in a strain-stress-strain cycle equals or exceeds the first strain load, or if the second stress load in a stress-strain-stress cycle equals or exceeds the first stress load. In the example the residue vector develops as follows, whereby the load cycle displayed in parentheses is closed and deleted from the following lines:

```text
 1 (4  3) 4
 1       (4  2) 4
 1             (4  3) 5
(1                    5) 1
                        (1  2) 1
                               1  4 (2  3) 2
```

DIAdem counts the following closed load cycles in the rainflow matrix:

```text
4 → 3, 4 → 2, 4 → 3, 1 → 5, 1 → 2, 2 → 3
```

When the closed cycles are deleted, the following values remain in the residue vector:

```text
1, 4, 2
```

If you select **Closing and inclusion of residues** in the rainflow classification dialog box, DIAdem also counts the load cycle 1  → 4 and returns the following rainflow matrix:

|  |  | Target class |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 1 | 2 | 3 | 4 | 5 |
| Start class | 1 | 0 | 1 | 0 | 1 | 1 |
| 2 | 0 | 0 | 1 | 0 | 0 |  |
| 3 | 0 | 0 | 0 | 0 | 0 |  |
| 4 | 0 | 1 | 2 | 0 | 0 |  |
| 5 | 0 | 0 | 0 | 0 | 0 |  |

#### Statistics

[Characteristic Statistical Values](../genmaths/calc_statistics.htm) | [Process Capability](../genmaths/calc_spc.htm) | [Classifications](../genmaths/calc_classification.htm) | [Single Classification](../genmaths/calc_single_classification.htm) | [Reducing Classification](../genmaths/calc_reducing_classification.htm) | [Compound Classification](../genmaths/calc_compound_classification.htm) | [Rainflow Classification](../genmaths/calc_rainflow.htm) | [Example Rainflow Classification](../genmaths/calc_rainflow_example.htm) | [Algorithm Rainflow Classification](../genmaths/calc_rainflow_algorithm.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_smoothfunctions.htm language=enus -->
## TOPIC 00976: Smoothing Functions

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_smoothfunctions.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_smoothfunctions.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Curve Fitting](../genmaths/calc_overviewcurves.htm) > Smoothing Functions

Smoothing Functions

Very often the actual course of the measured signals is distorted due to overlaying noise or humming. The smoothing functions in DIAdem replace each individual channel value by a mean value or the median of the actual value and a specified number of neighbor values. The smoothing functions make the curve more visible and suppress unwanted overlays.

DIAdem has three functions for smoothing signals. The **Smooth** function calculates an unweighted moving average or moving median. The **Savitzky-Golay Filter** uses a specific weighting of the values for averaging and can thereby better retain the characteristic properties of the original curve. The **4253H filter** calculates several moving median values of different widths in succession and thus achieves effective smoothing without losing the special features of the signal.

#### The Smooth Function

The smooth function replaces each individual value of a channel with the unweighted arithmetic mean value or median of a specified number of neighboring values. The channel length remains the same. The smooth function does not execute a data reduction. The one-sided smoothing width N specifies the number of neighboring values which DIAdem uses for smoothing on the left side and the right side of the actual value.

DIAdem calculates the smoothing either with the mean value or the median. If the signal contains strong outliers, they are not totally eliminated by the mean value calculation. In these cases, smoothing with the median is more robust.

- The mean value calculates the smoothing from 2N+1 values according to the following formula. m is the channel length. [IMAGE alt='image' src='../image/f_smoothing.gif']
- For the median the 2N+1 initially sorts the values according to size. The median is the mean of the sorted sequence. At the beginning and at the end of the channel, or with the setting Only previous channel values the number of values is even. In this case, the median is the mean value of the middle values. This means that the sequence {3, 4, 5, 6} has the median 4.5 and the sequence {3, 4, 4, 5, 6} has the median 4.

At the start and at the end of the channel, the distance of the values to the exterior side is smaller than the one-sided smoothing width N, and the smoothing is calculated digressing from the formula with fewer than 2N+1 values. The setting Select the points to be used specifies how many values DIAdem uses to calculate the smoothing of these boundary values. DIAdem uses N values with the Maximum number setting on the interior side even if fewer than N values are available on the outer side. DIAdem uses the same number of values on each side with the Symmetric distribution setting which means that DIAdem uses fewer than N values on the inner side. If you select Only previous channel values, DIAdem uses only the values on the left for the smoothing.

**Example** If the smoothing width is N=5, DIAdem calculates the smoothing from 11 values, which are the value to be replaced and 5 neighboring values on each side, respectively. This does not apply for the first 5 and the last 5 values of the channel. The following table shows how many values DIAdem uses for the smoothing of the second value in the channel.

| Select points | Previous Values | Successive Values | Total |
| --- | --- | --- | --- |
| Maximum number | 1 | 5 | 7 |
| Symmetric distribution | 1 | 1 | 3 |
| Only previous channel values | 1 | 0 | 2 |

#### The 4253H filter

The 4253H filter calculates consecutively several moving median values of different widths. First, the moving median is calculated using 4 values. For the result of the first calculation, the moving median is then calculated using 2 values. In total, the 4253H filter applies the following smoothings one after the other:

1. Calculation of the moving median over 4-values.
2. Calculation of the moving median over 2-values.
3. Calculation of the moving median over 5-values.
4. Calculation of the moving median over 3-values.
5. Calculation of the moving median over 3 values weighted by Hanning (0.25, 0.5, 0.25).

The 4253H Twice filter applies these steps again to the difference between the original values and the transformed values:

1. DIAdem subtracts the transformed values from the original values to calculate the differences.
2. Repetition of steps 1 to 5 for the differences.
3. Addition of the transformed differences to the transformed values.

#### The Savitzky-Golay Filter

The Savitzky-Golay filter replaces each individual channel value with a weighted arithmetic mean from the actual value and a specified number of neighboring values. The channel length remains the same. The Savitzky-Golay filter does not execute a data reduction. The one-sided smoothing width N specifies the number of neighboring values which DIAdem uses for averaging on the left and on the right. DIAdem calculates the mean value from 2N+1 values.

The Savitzky-Golay filter smoothes signals by a piecewise adjustment of a polynomial function. This filtering corresponds to a moving average, where DIAdem weights the values with fixed factors, which is not the case in the smooth function. The factors depend on the order of the polynomial and the window width. The order of the polynomial must be smaller than 2N+1. If the distance at the beginning or the end of the channel is smaller than N, the averaging is also modified in the Savitzky-Golay filter.

DIAdem can use a further weighting for the minimization of the smallest error square with the optional weighting channel. The weighting channel must contain at least 2N+1 values. DIAdem ignores excess weighting values.

The advantage of the Savitzky-Golay filter over the smooth function is that the Savitzky-Golay filter, for example, can better maintain the height and the width of peaks of the original signal, whereas the smooth function tends to iron out such characteristic values.

**Example** If the one-sided smoothing width is N=3 and the polynomial order is 2, DIAdem calculates each smoothed value from altogether 7 values according to the following formula:

[IMAGE alt='image' src='../image/f_savitzky.gif']

#### Curve Fitting

Smooth Functions | [Regression](../genmaths/calc_regression.htm) | [Approximation](../genmaths/calc_approximation.htm) | [Non-Linear Curve Fitting](../genmaths/calc_nonlinearcurvefit.htm) | [Gaussian Curve Fitting](../genmaths/calc_gaussianpeakfit.htm) | [General LS-Linear Fitting](../genmaths/calc_genlsfit.htm) | [Splines in DIAdem](../genmaths/calc_splines.htm) | [Non-Parametrical Splines](../genmaths/calc_nonparam_splines.htm)| [Parametrical Splines](../genmaths/calc_param_splines.htm) | [Akima Subsplines](../genmaths/calc_akima_splines.htm) | [Circle Approximation](../genmaths/calc_circles.htm) | [Envelope Curves](../genmaths/calc_envelopecurves.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_spc.htm language=enus -->
## TOPIC 00977: Process Capability

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_spc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_spc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Statistics](../genmaths/calc_overviewstatistics.htm) > Process Capability

Process Capability

The Process Capability Control (SPC) methods help to continuously improve the quality and productivity of processes, for example, in manufacturing. SPC helps differentiate between random dispersion and so-called assignable causes. Random dispersions are stochastic fluctuations around a mean value, for example, when the thickness of a rolled metal sheet varies slightly around its set point. Dispersions with assignable causes are not stochastic and can occur, for example, due to material or machine errors in the rolling process. If the assignable causes are recognized, process problems can be discovered and corrected early on.

The process capability function in DIAdem calculates the mean value, the standard deviation, and the capability indexes of the process and displays the result data in a dialog box. DIAdem stores the calculated characteristic process values in the appropriate variables and in custom properties of the input channels.

#### Mean Values and Process Limits

##### SPCProcessMean

The mean value of the process is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spcprocessmean.gif']

##### SPCProcessSigma

The standard deviation, which is also called the process sigma, is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spcprocesssigma.gif']

In this case the following formula characters are used

| σ | Mean sample standard deviation |
| --- | --- |
| R | Mean sample range |
| mR | Mean floating range |
| c4 , d2 | Factor dependent on sample range N |

##### SPCUpperNPL

The upper natural process limit is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spcuppernpl.gif']

##### SPCLowerNPL

The lower natural process limit is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spclowernpl.gif']

#### Process Capability Indexes

Capability indexes describe the dispersion of a process or of a machine in relation to the specification.

##### SPCCpU

The one-sided upper process capability index C<sub>pU</sub> is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spccpu.gif']

##### SPCCpL

The one-sided lower process capability index C<sub>pL</sub> is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spccpl.gif']

##### SPCCp

The process capability index C<sub>p</sub> is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spccp.gif']

##### SPCCpk

The process capability index C<sub>pk</sub> is calculated according to the following formula

[IMAGE alt='image' src='../image/f_spccpk.gif']

#### Estimation of Nonconforming Parts

The estimation of nonconforming parts described in the following is based on the assumption of a normal distribution.

##### SPCFracNConf

The estimated nonconforming part is saved in the variable SPCFracNConf.

##### SPCUFracNConf

The estimated nonconforming part above the upper specification limit is saved in the variable SPCUFracNConf.

##### SPCLFracNConf

The estimated nonconforming part below the upper specification limit is saved in the variable SPCLFracNConf.

#### Statistics

[Characteristic Statistical Values](../genmaths/calc_statistics.htm) | Process Capability | [Classifications](../genmaths/calc_classification.htm) | [Single Classification](../genmaths/calc_single_classification.htm) | [Reducing Classification](../genmaths/calc_reducing_classification.htm) | [Compound Classification](../genmaths/calc_compound_classification.htm) | [Rainflow Classification](../genmaths/calc_rainflow.htm) | [Example Rainflow Classification](../genmaths/calc_rainflow_example.htm) | [Algorithm Rainflow Classification](../genmaths/calc_rainflow_algorithm.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=genmaths/genmaths/calc_statistics.htm language=enus -->
## TOPIC 00978: Characteristic Statistical Values in DIAdem

- bundle_id: `diadem`
- source_path: `genmaths/genmaths/calc_statistics.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genmaths/genmaths/calc_statistics.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../genmaths/calc_overview.htm) > [Statistics](../genmaths/calc_overviewstatistics.htm) > Characteristic Statistical Values in DIAdem

Characteristic Statistical Values in DIAdem

The descriptive statistics functions characterize the properties of data series, for example, of measured values. You use characteristic statistical values to compress data series, which makes the data series easier to compare to other data series.

DIAdem calculates the characteristic statistical values either channel or line oriented. You can execute the channel oriented calculation over the entire channel or over a specified line section. DIAdem saves the results as custom properties of the input channels. You can also limit the line oriented calculation over several channels to a specified line area. Because line oriented characteristic values are not saved at the input channels, you should enable the result storage in channels.

For the dispersion measurements and for form measurements you can choose whether the data series displays the population or a sample. The specified formulas have the index P for population or S for sample.

#### Mean values

The mean values are moments of a data series. DIAdem calculates the following mean values:

##### Arithmetic mean

The arithmetic mean is the most commonly used type of mean and is also called the average.

[IMAGE alt='image' src='../image/f_arith_mean.gif']

##### Root mean square

The root mean square, also called the quadratic mean, is used to calculate the RMS level of a signal.

[IMAGE alt='image' src='../image/f_quad_mean.gif']

##### Geometric mean

The geometric mean is useful for the description of data series of which the product is required, for example, for growth rates of bacterial cultures or in the calculation of interest rates. DIAdem calculates the geometric mean when all the measured values are greater than zero.

[IMAGE alt='image' src='../image/f_geom_mean.gif']

##### Harmonic mean

The harmonic mean is used, for example, to calculate the average speed from partial speeds given for partial distances. DIAdem calculates the harmonic mean when all the measured values are greater than zero.

[IMAGE alt='image' src='../image/f_harm_mean.gif']

#### Normal distribution

Many statistical studies are based on the assumption that data series are normal distributions. With the Anderson-Darling test you can check this assumption.

##### Anderson-Darling test

The Anderson-Darling test calculates whether the values of a data series are normally distributed. To do so, DIAdem determines the p-value. If the p-value is greater than 0.05, it is a normal distribution.

#### Quantiles

Quantiles and the mean values are moments. Quantiles are usually less subject to outliers than the mean values. DIAdem requires at least four values to calculate quantiles. DIAdem calculates the following quantiles:

##### 0.25 quantile (lower quartile)

If the measured values are sorted according to size, the 0.25 quantile is the measured value that is undershot by 25% of the measured values. The 0.25 quantile is also called the lower quartile.

##### 0.50 quantile (median)

If the measured values are sorted according to size, the 0.50 quantile is the measured value of which an equal number of values are less than and greater than the value. The 0.50 quantile is also called the median.

##### 0.75 quantile (upper quartile)

If the measured values are sorted according to size, the 0.75 quantile is the measured value that is undershot by 75% of the measured values. The 0.75 quantile is also called the upper quartile.

#### Dispersion

The dispersion values describe the dispersion of data series. For the dispersion measurements, standard deviation, standard error, variance, variation coefficient, and relative variation coefficient you can select whether the data series displays the population or a sample. The specified formulas have the index P for population or S for sample. DIAdem calculates the following dispersion values:

##### Range

The range is the difference between the highest and the lowest measured value.

##### Quartile distance

The quartile distance is the difference between the upper quartile (the 0.75 quantile) and the lower quartile (the 0.25 quantile). This means that 50% of the measured values are inside the quartile distance.

##### Standard deviation

The standard deviation is the square root of the variance of the data series.

[IMAGE alt='image' src='../image/f_standard_deviation_population.gif'], [IMAGE alt='image' src='../image/f_standard_deviation_sample.gif']

##### Standard error

The standard error is the quotient of the standard deviation of the data series and the root of the number of measured values.

[IMAGE alt='image' src='../image/f_standard_error_population.gif'], [IMAGE alt='image' src='../image/f_standard_error_sample.gif']

##### Variance

The variance is the average squared deviation of the data series from its arithmetic mean.

[IMAGE alt='image' src='../image/f_variance_population.gif'], [IMAGE alt='image' src='../image/f_variance_sample.gif']

##### Variation coefficient

The variation coefficient is the quotient from the standard deviation and the arithmetic mean of the data series.

[IMAGE alt='image' src='../image/f_variance_coeff_population.gif'], [IMAGE alt='image' src='../image/f_variance_coeff_sample.gif']

##### Relative variation coefficient

The relative variation coefficient is the quotient from the variation coefficient and its theoretically possible maximum. DIAdem specifies the relative variation coefficient as a percentage.

[IMAGE alt='image' src='../image/f_rel_variance_coeff_population.gif'], [IMAGE alt='image' src='../image/f_rel_variance_coeff_sample.gif']

#### Average Absolute Deviation

Average absolute deviations are especially useful when the variance of a data series is almost infinite. DIAdem calculates the average absolute deviations from the mean and from the median:

##### Average absolute deviation from mean

MAD<sub>μ</sub> specifies the average absolute deviation from the mean value.

[IMAGE alt='image' src='../image/f_maavmw.gif']

##### Average absolute deviation from median

MAD<sub>x˜</sub>specifies the average absolute deviation from the median (the 0.50 quantile).

[IMAGE alt='image' src='../image/f_maavzw.gif']

#### Form

The forms are also called central moments and describe the deviation of the distribution of the measured values from a normal distribution. For the form measurements you can choose whether the data series displays the population or a sample. The specified formulas have the index P for population or S for sample:

##### Skewness

The skewness is the third order central moment and characterizes the degree of asymmetry to the right (positive skewness) or to the left (negative skewness) of a distribution around its mean. Normal distribution has zero skewness.

[IMAGE alt='image' src='../image/f_skewness_population.gif'], [IMAGE alt='image' src='../image/f_skewness_sample.gif']

##### Kurtosis

The kurtosis is the fourth order central moment and describes the peakedness of a distribution of measured values. Normal distribution has kurtosis 3. If the kurtosis is greater than 3, the distribution is more peaked than a normal distribution. If the kurtosis is less than 3, the distribution is flatter.

[IMAGE alt='image' src='../image/f_curtosis_population.gif'], [IMAGE alt='image' src='../image/f_curtosis_sample.gif']

##### Excess

The excess kurtosis describes the difference of the kurtosis of a random value to the kurtosis of the normal distribution. Because the normal distribution has the kurtosis 3, the value 3 is subtracted from the calculated kurtosis.

[IMAGE alt='image' src='../image/f_curtosis_excess_population.gif'], [IMAGE alt='image' src='../image/f_curtosis_excess_sample.gif']

#### Statistics

Characteristic Statistical Values | [Process Capability](../genmaths/calc_spc.htm) | [Classifications](../genmaths/calc_classification.htm) | [Single Classification](../genmaths/calc_single_classification.htm) | [Reducing Classification](../genmaths/calc_reducing_classification.htm) | [Compound Classification](../genmaths/calc_compound_classification.htm) | [Rainflow Classification](../genmaths/calc_rainflow.htm) | [Example Rainflow Classification](../genmaths/calc_rainflow_example.htm) | [Algorithm Rainflow Classification](../genmaths/calc_rainflow_algorithm.htm)

#### Mathematical Functions

[Basic Mathematics](../genmaths/calc_basicmathematics.htm) | [Channel Functions](../genmaths/calc_channelfunctions.htm) | [Curve Fitting](../genmaths/calc_overviewcurves.htm) | [Signal Analysis](../genmaths/calc_overviewsignalanalysis.htm) | [Statistics](../genmaths/calc_overviewstatistics.htm) | [3D Data Analysis](../genmaths/calc_overview3d.htm) | [Calculation Manager](../genmaths/calc_calculationmanager.htm)

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_firewalls.html language=enus -->
## TOPIC 00979: Configuring Firewalls and Network Address Translating Routers for DataFinder Instances

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_firewalls.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_firewalls.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > Configuring Firewalls and Network Address Translating Routers for DataFinder Instances

Configuring Firewalls and Network Address Translating Routers for DataFinder Instances

You must configure firewalls and Network Address Translating (NAT) routers if you want to use them to access a DataFinder instance. If you do not configure the firewall or router correctly, the connection to a DataFinder instance might not work.

DataFinder instances use the UDP port 2343 and a range of UDP ports beginning with port 6000. The number of ports above 6000 that the DataFinder instances use depends on the number of servers running on the computer. Clients of DataFinder instances, such as DIAdem, use a range of UDP ports beginning with port 5000. The number of ports above 5000 that the clients use depends on the number of client applications running on the computer.

Complete the following steps to allow DIAdem or other DataFinder instances outside a firewall to connect to a DataFinder instance inside the firewall. The exact steps for configuring the firewall depend on which specific firewall you use. Refer to the documentation on the firewall for specific instructions about opening ports.

1. Open UDP port 2343 for incoming packets.
2. Open the UDP port range from 6000 to 6010 for incoming packets.

You also can allow clients inside a firewall to connect to a DataFinder instance outside the firewall. Some firewalls automatically transmit incoming packets without any configuration. If the firewall does not open the ports automatically, open the UDP port range from 5000 to 5010 for incoming packets.

Complete the following steps to allow clients outside a NAT router to connect to a server inside the router. The exact steps for configuring the router depend on the specific NAT router you use. Refer to the documentation on the router for further information about forwarding ports. Only one computer inside the router can function as a server.

1. Forward the UDP port 2343 to the computer running the DataFinder instance.
2. Forward the UDP port range 6000 to 6010 to the computer running the DataFinder instance.

You can also allow clients inside a NAT router to connect to a server outside the router. Some routers automatically forward ports without any configuration. If the router does not forward the ports automatically, forward the UDP port range from 5000 to 5010 to the computer running the client (DIAdem).

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_general.htm language=enus -->
## TOPIC 00980: DIAdem NAVIGATOR

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

DIAdem NAVIGATOR

DIAdem NAVIGATOR

Use the DIAdem NAVIGATOR panel to gain an overview of external data, to browse in data, to search for data, and to load and save data.

#### DataFinder

Use the **DataFinder** function group to open a [DataFinder](../gennavigator/navi_search_gui_general.htm). If you run a [Quick Search](../gennavigator/navi_search_specific.htm) with a DataFinder, DIAdem searches for the specified value in the [Properties](../../genshell/genshell/genshell_dd_properties.htm) of the files, groups, and channels of the [Search Areas](../../dlgnavigator/dlgnavigator/navi_search_configure_searchareas_dialog.htm). If you run an [Advanced Search](../gennavigator/navi_search_specific.htm), DIAdem searches for the property values of the files, groups, or channels that you selected. Enter the values to be found in the [Search input area](../../dlgnavigator/dlgnavigator/navi_search_queryform_window.htm). DIAdem lists the [Search Results](../../dlgnavigator/dlgnavigator/navi_search_resultlist_window.htm). Refer to [Searching for Data (DataFinder)](../gennavigator/navi_search_specific.htm) for further information on searching with the DataFinder.

Use the [File Browser](../../dlgnavigator/dlgnavigator/navi_search_tree_window.htm) tab to browse in the search areas of the enabled DataFinder. In all the files for which a DataPlugin exists you can navigate to the channel level, in the file browser.

Use the [Property Display](../../dlgnavigator/dlgnavigator/navi_search_property_window.htm) to view the properties of files, groups, and channels from the search areas and the search results. The Property Display shows, for example, the name, the size, or the storage date of a file.

|  | Note Refer to the Properties in DIAdem - Overview page for an overview of the properties of data sets, groups, and channels. |
| --- | --- |

Select **Find»Save Query As** to save the parameters of the current search in a file with the file extension *.TDQ. Select **Find»Load»Load Only Query** to load a query you saved.

#### Data Stores

Use the **Data Stores** function group to open predefined file-based and server-based [Data stores](../gennavigator/genshell_datastore_definition.htm).

You can [search for data](../../dlgnavigator/dlgnavigator/navi_dssearch_queryform_window.htm) in the ASAM data stores. Enter the search conditions in the [Search Input Area](../../dlgnavigator/dlgnavigator/navi_dssearch_queryform_window.htm). DIAdem lists the [Search Results](../../dlgnavigator/dlgnavigator/navi_datastore_resultlist_window.htm). Use the [Data Browser](../../dlgnavigator/dlgnavigator/navi_datastore_tree.htm) to browse through the ASAM data stores. If you open an ASAM data store, the [Property Display](../../dlgnavigator/dlgnavigator/navi_dssearch_property_window.htm) displays the properties of this ASAM data store. Refer to [Searching for Data (DataFinder)](../gennavigator/navi_dssearch_specific.htm) for further information on how to search in ASAM data stores.

Use the [DataStore object](../../scriptnavi/objects/navigator_objects_itdmdatastore.htm)to access ASAM data stores with a script. You also can[filter](../../dlgnavigator/dlgnavigator/navi_filter_settings_dialog.htm)other data stores, for example, LabVIEW DSC data stores or Lookout data stores. If you open a data store, the[Property Display](../gennavigator/navi_property_window.htm) displays the properties of this data store.

#### Loading and Saving Data

Use DIAdem NAVIGATOR to load data into the [Data Portal](../../genportal/genportal/portal_general.htm). You can load data completely, [selectively](../../dlgnavigator/dlgnavigator/navi_file_load_selective_dialog.htm), or [reduced](../../dlgnavigator/dlgnavigator/reductionloaddlg_dialog.htm). [Drag and drop](../../genshell/genshell/portal_drag_drop.htm) data sets, groups, and channels into the [Data Portal](../../genportal/genportal/portal_general.htm) to load data into DIAdem. You can also [append](../gennavigator/navi_appenddata_general.htm) files and channel groups to channels in the Data Portal.

You also can register data sets. However, DIAdem only generates a reference to registered data but does not load registered data physically into the internal memory. Registered data sets are read only. If you changed a registered data set, you cannot store this data set under the same name. To edit a channel in a registered data set and to save the changes under the same data set name, you must first [expand](../../procportal/procportal/procportal_expanding_channels.htm) all channels of the registered data set.

Use the [Open With](../../dlgnavigator/dlgnavigator/navi_file_load_with_dialog.htm) function in the context menu of a DataFinder or of a data store to specify the loader for loading or registering a selected data set. If the loader you need is not registered in DIAdem you must first register the appropriate [DataPlugin](../../dlgnavigator/dlgnavigator/navi_configdataplugin_dialog.htm) or the appropriate [GPI-DLL](../../dlgshell/dlgshell/dlggpiregister_dialog.htm).

If you drag one or more channels from DIAdem NAVIGATOR to a group in the Data Portal and hover over it for a short time, DIAdem selects this group and inserts the selected channels at the end of this group as soon as you release the mouse button.

Drag and drop data into the file browser of the DataFinder or the data store or select **Save As** from the context menu of the data set to save data from the Data Portal.

Use a [Column-oriented search](../gennavigator/navi_search_columnsoriented.htm) to search for the selected properties of data elements of a DataFinder or of a data store. You can then load the search results with the property values column-wise as channels into the Data Portal.

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_inheritance_datafinder.htm language=enus -->
## TOPIC 00981: Property Inheritance (DataFinder)

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_inheritance_datafinder.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_inheritance_datafinder.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > Property Inheritance (DataFinder)

Property Inheritance (DataFinder)

Before loading data from a DataFinder into the Data Portal, you can specify which properties DIAdem also transfers to the elements in the Data Portal.

#### Parameters

|  | None | Specifies that DIAdem transfers only the properties of the loaded data element into the Data Portal. |
| --- | --- | --- |
|  | Move to loaded level | Specifies that DIAdem transfers the properties of all superordinate levels of the element, which is to be loaded, to the channel group or the channel. The properties are loaded in relation to the level which is to be loaded. If you load channel groups, DIAdem transfers the properties of the root in the Data Portal to the channel group. If you load channels, DIAdem transfers the properties of the channel groups and of the root in the Data Portal to the channel. The Data Portal contains the transferred properties only once. If the Data Portal does not contain data before the loading process, DIAdem names the higher levels in the Data Portal NoName.In the Data Portal the transferred properties of elements, which correspond to the channel group, receive the prefix group~. Transferred properties of elements, which correspond to the root, receive the prefix root~. |
|  | Copy to channel level | Specifies that DIAdem also copies the properties of all superordinate elements also to the channels in the Data Portal.In the Data Portal the transferred properties of elements, which correspond to the channel group, receive the prefix group~. Transferred properties of elements, which correspond to the root, receive the prefix root~. |

|  | Note Properties can only be inherited if DIAdem can index the data to be loaded via a DataPlugin. File properties that DIAdem loads via GPI-DLLs cannot be inherited. |
| --- | --- |

|  | Note The properties which were inherited overwrite the properties of the level to which DIAdem passes on these properties. This behavior is different to the behavior which occurs when ASAM data store properties are inherited. |
| --- | --- |

|  | Note Configure the inheritance of properties for DataFinders in the DIAdem Settings dialog box. Select Settings»DIAdem Settings»NAVIGATOR to open this dialog box.DIAdem uses the tilde character as separator by default for the inheritance of properties. You can change these settings in the DIAdem Settings: Compatibility dialog box. If you disable this setting in the compatibility dialog box, DIAdem also uses the underline as separator in the above-mentioned interface terms. As of DIAdem 2017, DIAdem uses the tilde "~" character as Property Inheritance Separator to group properties in the Properties Display of the Data Portal. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_property_window.htm language=enus -->
## TOPIC 00982: The Property Display of a Data Store

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_property_window.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_property_window.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > The Property Display of a Data Store

[[IMAGE alt='image' src='../image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

The Property Display of a Data Store

Use the DIAdem NAVIGATOR Property Display to view the properties of external data stores. For example, the Property Display shows the name, the size, and the storage date of a file, or the attributes of a folder.

The properties of the most important data types are listed in the following:

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)File system - Root and folder

| Accessed | Specifies the time of the last root or folder access. |
| --- | --- |
| Attributes | Specifies the attributes of the root or folder. If no attribute is set, DIAdem displays a dash. The following attributes are possible:d: Indicates that the selected element is a folder.a: Indicates that the selected element is archived when the data is saved.r: Indicates that the selected element is read only.c: Indicates that the selected element is compressed.s: Indicates that the selected element is a system folder.h: Indicates that the selected element is a hidden folder.t: Indicates that the selected element is a temporary folder.n: Indicates that the selected element has no special attributes. |
| Created | Specifies the time when the root or the folder was created. |
| Fullpath | Specifies the complete path to the root or to the folder. |
| ID | Specifies an internal ID. |
| Modified | Specifies the last time the root or the folder was modified. |
| Name | Specifies the relative name of the root or the folder. If the file system uses links, the name of the link file appears here. DIAdem then displays the target of the link file in the fullpath property. |
| Alias | If you assign an alias, DIAdem displays it. If you do not specify an alias, DIAdem displays the contents of the Name property. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)File system - File

| Accessed | Specifies the last time the file was accessed. |
| --- | --- |
| Attributes | Specifies the file attributes. If no attribute is set, DIAdem displays a dash. The following attributes are possible:d: Indicates that the selected element is a file.a: Indicates that the selected element is archived when the data is saved.r: Indicates that the selected element is read only.c: Indicates that the selected element is compressed.s: Indicates that the selected element is a system file.h: Indicates that the selected element is a hidden file.t: Indicates that the selected element is a temporary file.n: Indicates that the selected element has no special attributes. |
| Created | Specifies when the file was created. |
| Fullpath | Specifies the complete file path. |
| ID | Specifies an internal ID. |
| Modified | Specifies when the file was last changed. |
| Name | Specifies the filename. |
| Size | Specifies the file size. |
| Alias | If you assign an alias, DIAdem displays it. If you do not specify an alias, DIAdem displays the contents of the Name property. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)VILogger - Trace

| ID | Specifies an internal ID. |
| --- | --- |
| Name | Specifies the name of the trace. |
| TraceID | Specifies the ID of the trace. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)VILogger - Measurement

| ID | Specifies an internal ID. |
| --- | --- |
| Measurement_Begin | Specifies the beginning of the measurement. |
| Measurement_End | Specifies the end of the measurement. |
| Name | Specifies the name of the measurement. |
| SubTraceID | Specifies the subID of the trace. |
| TraceID | Specifies the ID of the trace. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)VILogger - Channel

| DataType | Specifies the data type of the channel. |
| --- | --- |
| ID | Specifies an internal ID. |
| Name | Specifies the name of the channel. |
| SubTraceID | Specifies the subID of the channel. |
| Unit_String | Specifies the unit of the channel. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)Lookout - Local host and path

| Description | Specifies the description of a local host or a path. |
| --- | --- |
| ID | Specifies an internal ID. |
| Name | Specifies the name of a local host or a path. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)Lookout - Trace

| Description | Specifies the description of a trace. |
| --- | --- |
| ID | Specifies an internal ID. |
| Name | Specifies the name of the trace. |
| Tracename | Specifies the complete name of the trace including the URL. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)Lookout - Measurement

| Description | Specifies the description of a measurement. |
| --- | --- |
| ID | Specifies an internal ID. |
| Measurement_Begin | Specifies the beginning of the measurement. |
| Measurement_End | Specifies the end of the measurement. |
| Name | Specifies the name of the measurement. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)Lookout - Channel

| DataType | Specifies the data type of the channel. |
| --- | --- |
| ID | Specifies an internal ID. |
| Name | Specifies the name of the channel. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)LabVIEW DSC - Database

| ID | Specifies an internal ID. |
| --- | --- |
| Name | Specifies the name of the database. |
| Path | Specifies the path of the database. |
| URL | Specifies the URL path of the database up to this node. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)LabVIEW DSC - Folder

| ID | Specifies an internal ID. |
| --- | --- |
| Name | Specifies the name of the folder. |
| URL | Specifies the URL path of the folder. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)LabVIEW DSC - Trace

| DataType | Specifies the data type of the trace. |
| --- | --- |
| ID | Specifies an internal ID. |
| Name | Specifies the name of the trace. |
| Start_time | Specifies the trace start time. |
| Stop_time | Specifies the trace stop time. |
| URL | Specifies the URL path of the trace. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)LabVIEW DSC - Measurement

| ID | Specifies an internal ID. |
| --- | --- |
| Measurement_Begin | Specifies the beginning of the measurement. |
| Measurement_End | Specifies the end of the measurement. |
| Name | Specifies the name of the measurement. |

[[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)LabVIEW DSC - Channel

| DataType | Specifies the data type of the channel. |
| --- | --- |
| ID | Specifies an internal ID. |
| Name | Specifies the name of the channel. |
| Unit_string | Specifies the unit of the channel. |

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_remotedatafinder.htm language=enus -->
## TOPIC 00983: DataFinder Instances

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_remotedatafinder.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_remotedatafinder.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > DataFinder Instances

DataFinder Instances

Use a DataFinder instance to run a search with a [DataFinder instance](../gennavigator/navi_search_gui_general.htm) from another computer in the network. The DataFinder instance on the other computer must be shared for [Remote access](../../dlgnavigator/dlgnavigator/navi_search_adv_datafinder_settings_dialog.htm). Once you have connected the two computers, you can browse on the other computer and search for data. If you want to load data from the other computer into your local Data Portal, you must have read access for that data on the other computer. Use your share name, for example, \\MyComputer\MyData to define [search areas](../../dlgnavigator/dlgnavigator/navi_search_configure_searchareas_dialog.htm) on the DataFinder instance. You cannot change the settings for the other computer on your computer. You can create a new connection to a DataFinder instance in the [New DataFinder Server Connections](../../dlgnavigator/dlgnavigator/navi_search_connect_remote_dialog.htm) dialog box.

|  | Note The procedure Searching for Data on a Different Computer in the Network describes how you can create and open a DataFinder instance. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_search_characteristics.htm language=enus -->
## TOPIC 00984: Evaluating Search Conditions (DataFinder)

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_search_characteristics.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_search_characteristics.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > Evaluating Search Conditions (DataFinder)

Evaluating Search Conditions (DataFinder)

By default, the DIAdem DataFinder executes a logical **AND** operation on the search conditions of an [Advanced search](../gennavigator/navi_search_specific.htm). You also can execute **OR** operations on single values of a search condition, or entire search conditions, for example, to search for several filenames.

To link individual values of a search condition with OR enter the values manually in the **Value** column of the search input area and insert OR between these values. Alternatively, click the **...** button repeatedly and select another value with a double-click. DIAdem then automatically connects the selected values with an OR operator. You must select the = sign to connect values with OR.

|  | Note You also can create OR connections in the logical operations line. Refer to the page Executing a Search with OR Operations in the Logical Operations Line for further information. |
| --- | --- |

#### Examples for the Advanced Search

In the following example the DataFinder searches for files, groups, or channels with the filename MyData and the description My Test data:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Filename | = | MyData |
| C2 | File | Description | = | My Test data |
| Logic line: C1 AND C2 |  |  |  |  |

In the following example the DataFinder searches for files, groups, or channels with the filename MyData1 and a group name MyData1:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Filename | = | MyData1 |
| C2 | Group | Name | = | MyData1 |
| Logic line: C1 AND C2 |  |  |  |  |

In the following example the DataFinder searches for files, groups, or channels with a filename MyData1, a group name MyGroup1, and a channel that has the unit m/s.

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Filename | = | MyData1 |
| C2 | Group | Name | = | MyGroup1 |
| C3 | Channel | Unit | = | m/s |
| Logic line: C1 AND C2 AND C3 |  |  |  |  |

The DataFinder displays all files, groups, or channels that meet these search conditions in the search results. Because the DataFinder connects the individual search conditions with an AND operator, the DataFinder only displays results when the channels searched for are in the searched for groups and the searched for groups are in the searched for files.

In the following example the DataFinder searches for files, groups, or channels with the channel name MyChannel:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | Channel | Name | = | MyChannel |
| Logic line: C1 |  |  |  |  |

In the following example the DataFinder searches for files, groups, or channels with the channel name MyChannel1 and MyChannel2:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | Channel | Name | = | MyChannel1 |
| C2 | Channel | Name | = | MyChannel2 |
| Logic line: C1 AND C2 |  |  |  |  |

Because the DataFinder connects the search conditions with **AND** and because no channel can be MyChannel1 and MyChannel2 simultaneously, the DataFinder does not display any results.

In the following example the DataFinder searches for files, groups, or channels with a DataPlugin-Name file property that contains the value TDM or the value TDMS:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | DataPlugin name | = | TDM OR TDMS |
| Logic line: C1 |  |  |  |  |

In the search results the DataFinder displays all files, groups, or channels that meet the first or the second partial condition.

|  | Note You receive the same search result as the above example if you generate two separate search conditions from the TDM OR TDMS search condition and link the two search conditions with an OR operator in the logic line. |
| --- | --- |

In the following example the DataFinder searches for files, groups, or channels with the file property DataPlugin name that contains the value TDM  or with a channel property Name that contains the value MyChannel1.

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | DataPlugin name | = | TDM |
| C2 | Channel | Name | = | MyChannel1 |
| Logic line: C1 OR C2 |  |  |  |  |

In the following example the DataFinder searches for files, groups, or channels that were edited last on 29.10.2007 and that contain a channel named MyChannel1, or that were edited by the author Tom:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Modify date | = | 29.10.2007 |
| C2 | Channel | Name | = | MyChannel1 |
| C3 | File | Author | = | Tom |
| Logic line: C1 AND (C2 OR C3) |  |  |  |  |

In the following example the DataFinder searches for files, groups, or channels that were edited last on 29.10.2007 and that contain a channel named MyChannel1, and searches for files, groups, or channels of the author Tom and that contains a description with the text Test Data:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Modify date | = | 29.10.2007 |
| C2 | Channel | Name | = | MyChannel1 |
| C3 | File | Author | = | Tom |
| C4 | File | Description | = | Test Data |
| Logic line: (C1 AND C2) OR (C3 AND C4) |  |  |  |  |

In the following example the DataFinder searches for files, groups, or channels that were last edited on 29.10.2007 and that contain the filename MyChannel1. The DataFinder also searches for files, groups, or channels that were last edited on 29.10.2007 and that have the author Tom. In the third search condition the DataFinder searches for files, groups, or channels that contain a channel with the name MyChannel1 and that have an author named Tom:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Modify date | = | 29.10.2007 |
| C2 | Channel | Name | = | MyChannel1 |
| C3 | File | Author | = | Tom |
| Logic line: (C1 AND C2) OR (C1 AND C3) OR (C2 AND C3) |  |  |  |  |

#### Advanced Search with Specified Sorting

In the following example the DataFinder searches for files with the filename MyData* and the file description Test* and [sorts](../gennavigator/navi_search_orderby.htm) the search results in ascending order by filename:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 ? | File | Filename | = | MyData* |
| C2 | File | Description | = | Test* |
| Logic line: C1 AND C2 Order By: C1 |  |  |  |  |

In the following example the DataFinder only searches for files with the filename MyData, because the user removed the search condition C2 from the logical operations line. The DataFinder [sorts](../gennavigator/navi_search_orderby.htm) the search results in ascending order according to the description:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Filename | = | MyData |
| C2 ? | File | Description | = | Test* |
| Logic line: C1 Order By: C2 |  |  |  |  |

In the following example the DataFinder searches for files with the filename MyData which also have the custom property Tester. In this case the DataFinder searches only for files that have the custom property Tester even if the search condition C2 is removed from the logical operations line, because the DataFinder can only sort by the existing custom properties. However, unlike the base properties, the custom properties are not always available. The DataFinder [sorts](../gennavigator/navi_search_orderby.htm) the search results in descending order according to the search condition C2:

|  | Level | Property | Operator | Value |
| --- | --- | --- | --- | --- |
| C1 | File | Filename | = | MyData |
| C2 ? | File | Tester | = | * |
| Logic line: C1 Order By: C2 |  |  |  |  |

|  | Note Refer to the help page Searching for Data with the DataFinder for further information about the DataFinder. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_search_columnsoriented.htm language=enus -->
## TOPIC 00985: Column-Oriented Search

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_search_columnsoriented.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_search_columnsoriented.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > Column-Oriented Search

Column-Oriented Search

Use a column-oriented search in DataFinders or datasets to search for specified properties of the data. You can then load the search results with the property values column-wise as channels into the Data Portal.

A column-oriented search returns search results faster than the search for elements because DIAdem only returns the specified properties from the search and does not have to return all the properties of the data elements. Click the **Search Results as Predefined Data Columns** button on the NAVIGATOR toolbar to enable the column-oriented search.

A column-oriented search can return a maximum of 2.5 million search results. The number of search results is the product of the properties defined for the search results list and the returned rows. This means, for example, that the column-oriented search can return a maximum of 2.5 million search results for a defined property, for 10 defined properties a maximum of 250,000 search results, or a maximum of 100,000 search results for 25 properties. The maximum number of properties a column-oriented search returns is 25.

Use the method [SearchProperties for DataFinder](../../scriptnavi/methods/navigator_method_searchproperties_itdmdatafinder.htm) to execute a column-oriented search without the user-interface in a DataFinder. DIAdem saves the results of this search in the property [ResultsProperties (DataFinder)](../../scriptnavi/properties/navigator_property_resultsproperties_itdmdatafinder.htm). Use the method [SearchProperties for DataStore](../../scriptnavi/methods/navigator_method_searchproperties_itdmdatastore.htm) to execute a column-oriented search without the user-interface in a data store. DIAdem saves the results this search in the property [ResultsProperties (DataFinder)](../../scriptnavi/properties/navigator_property_resultsproperties_itdmdatastore.htm).

Use the [Search for QueryForm <DataFinder>](../../scriptnavi/methods/navigator_method_search_inavidatafinderqueryform.htm) method to execute with a script a column-oriented search on the user interface of a DataFinder. The property [ResultsMode for QueryForm <DataFinder>](../../scriptnavi/properties/navigator_property_resultsmode_inavidatafinderqueryform.htm) specify whether you run a column-oriented search or a search for elements. Use the [ResultsProperties (DataFinder)](../../scriptnavi/properties/navigator_property_resultsproperties_inavidatafinderresultdisplay.htm) property to access the results of a column-oriented search on the DIAdem interface.

Use the [Search for QueryForm < DataStore>](../../scriptnavi/methods/navigator_method_search_inavidatastorequeryform.htm) method to execute with a script a column-oriented search on the user interface of a data store. The property [ResultsMode for QueryForm < DataStore>](../../scriptnavi/properties/navigator_property_resultsmode_inavidatastorequeryform.htm) specifies whether you run a column-oriented search or a search for elements. Use the [ResultsProperties (DataStore)](../../scriptnavi/properties/navigator_property_resultsproperties_inavidatastoreresultdisplay.htm) property to access the results of a column-oriented search on the DIAdem interface.

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_search_or.htm language=enus -->
## TOPIC 00986: Notes on Searching with OR (DataFinder)

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_search_or.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_search_or.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > Notes on Searching with OR (DataFinder)

Notes on Searching with OR (DataFinder)

By default, the DIAdem DataFinder executes a logical **AND** operation on the search conditions of an advanced search. You also can execute **OR** operations on single values of a search condition, or entire search conditions, for example, to search for several filenames.

Please note the following items when you use OR operations in the DataFinder:

- You can execute OR operations on single values of a search condition. Enter the values you want in the **Value** column of the search input area and add an OR between the values. Alternatively, click the **...** button multiple times and double-click a value to select this value. DIAdem then automatically connects the selected values with an OR operator.
- You only can execute OR operations in the **value** column if you use the = sign as the operator and if you select text or numeric values as the properties to be searched for.
- To execute OR operations on search conditions, create search conditions in the search input area and then enter OR between each of the search condition names in the logic line.
- In the logic line you can combine AND and OR operations. If you make no entries in the logic line, DIAdem automatically connects the search condition with AND.
- If you delete a search condition, DIAdem automatically updates the logic line. If you change the logical operations line manually and enter a new search condition in the search input area, DIAdem appends a new search condition with an AND operator to the logical operations line. However, if the logical operations line previously only contained one or several OR operators, DIAdem appends the new search condition with an OR operator to the logical operations line.
- If you are connected to a DataFinder that does not support OR operations, DIAdem deactivates the logic line and executes AND operations on all the search conditions.
- If you are connected to a DataFinder that does not support OR operations, and you load a query with a logic expression or if you execute operations on several values of one property, DIAdem displays an error message.
- Use parentheses to specify the order of evaluation. DIAdem replaces the curved brackets { and }, and the square brackets [ and ] automatically with the round brackets ( and ).
- If you select several channels, groups, or properties in the Data Portal and drag and drop them into the search input area, DIAdem generates a search condition with the selected channels, groups, or properties connected with the OR operator. If you select several channels or groups and drag and drop one property from the properties display into the search input area, DIAdem generates a search condition in which the properties of the previously selected channels or groups are connected with the OR operator. If you select several properties in the Data Portal properties display and drag and drop them into the search input area, DIAdem generates several search conditions connected with the AND operator.
- If you search for the text Or, you must enter /Or as the search text, instead of Or.

|  | NoteÂ Â OR operators are only available from DataFinder Version 2.0. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_search_script_general.htm language=enus -->
## TOPIC 00987: Searching for Data with a Script

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_search_script_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_search_script_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > Searching for Data with a Script

Searching for Data with a Script

The object-oriented DIAdem script interface contains methods and properties for accessing Navigator objects and DataFinder objects and for executing a search with a script.

Use the [Display](../../scriptnavi/objects/navigator_objects_idisplay.htm) object type to run a search with the DIAdem NAVIGATOR interface and to allow interaction during the script run. For example, apply the Navigator.Display.[CurrDataFinder](../../scriptnavi/properties/navigator_property_currdatafinder_idisplay.htm) command to use the DataFinder that is open in the Navigator as an object. If the DataFinder you want is not open in the DIAdem NAVIGATOR, open the DataFinder with the Navigator.Display.[OpenDataFinder](../../scriptnavi/methods/navigator_method_opendatafinder_idisplay.htm)(*DataFinderName*) command.

Use the [DataFinder](../../scriptnavi/objects/navigator_objects_itdmdatafinder.htm) object if you do not need to interact in the DIAdem NAVIGATOR interface. For example, use the Navigator.[ConnectDataFinder](../../scriptnavi/methods/navigator_method_connectdatafinder_inavigator.htm)(*DataFinderName*) command to establish a connection to a DataFinder.

Refer to the help pages on [Object-Oriented Interface in DIAdem NAVIGATOR](../../scriptnavi/objects/inavigator_objects_overview.htm) for further information about running a search with a script and about objects, properties, methods, and events.

|  | Note Refer to the Properties in DIAdem - Overview page for an overview of the properties of data sets, groups, and channels.To determine the name of properties that you use in a script, enter the query in the search area of DIAdem NAVIGATOR and press <Ctrl-Shift-C>. Then DIAdem saves a script to the clipboard that also contains the script names of the properties. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=gennavigator/gennavigator/navi_search_specific.htm language=enus -->
## TOPIC 00988: Notes on Searching for Data (DataFinder)

- bundle_id: `diadem`
- source_path: `gennavigator/gennavigator/navi_search_specific.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gennavigator/gennavigator/navi_search_specific.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../gennavigator/navi_general.htm) > Notes on Searching for Data (DataFinder)

Notes on Searching for Data (DataFinder)

#### Quick Search or Advanced Search

Use the quick search if you only have parts of the information you are searching for, or if you do not know whether the information you are searching for is in a file, a group, or a channel. In the quick search DIAdem searches for the specified search term in the file properties, group properties and channel properties of all files in the search areas that are in TDM format or in TDMS format or in a format which can be imported into DIAdem with a registered DataPlugin.

Use the advanced search if you want to search for specific files, groups, or channels. In the advanced search you can specify, for example, that you want to search for channels or files named Time. In the advanced search, you can run more complex search queries if you combine several search conditions. If all search areas are completely indexed, the advanced search returns reproducible results.

The quick search and the advanced search are not case-sensitive.

#### Special Features of the Quick Search

If you work with the quick search, separate the search terms with spaces. After you execute the search, the DataFinder returns all files that contain these search terms regardless of whether the DataFinder found the search term in the property of a file, a group, or a channel. 
The quick search also searches for parts of search terms. The part of the search term must be at the beginning of the search term, for example, exa*.

Note the following characteristics of the quick search:

- The quick search always interprets the search term as text. If you enter, for example, the search term 100, the DataFinder searches for the text 100 and not for the numeric value 100.
- If you enter quotation marks within a search term, DIAdem replaces the quotation marks with a space.
- If the wildcards (* and ?) are at the beginning of a search term, the quick search does not take them into account.
- If a search is too unspecific, for example, a search for te*, the DataFinder might not be able to return any results although many files match this query. In this case you should specify the query more accurately to limit the search results.

#### Special Features of the Advanced Search

The advanced search consists of one or more search conditions. A search condition comprises the file property, the channel group property, or the channel property the DataFinder searches for, and the operator and the value with which the DataFinder compares the property. Before the search starts you can specify whether the DataFinder returns files, channel groups, or channels as the search results.

By default the DataFinder connects all search conditions with an AND operator. However, you can specify a logical operator yourself and connect the search conditions with AND and OR as you like. Use parentheses to specify the order of evaluation.

Please note the following characteristics of the advanced search:

- By default, the DIAdem DataFinder executes a logical **AND** operation on the search conditions of an advanced search. This means that, for example, the search for groups that contain channels with the name Channel1 AND channels that contain the name Channel2, can never return a result.
- You can execute **OR** operations on single values of a search condition, or on entire search conditions, for example, to search for several filenames. Enter the values in the **Value** column of the search input area and insert an OR between these values. Alternatively, click the **...** button multiple times and double-click a value to select this value. DIAdem then automatically connects the selected values with an OR operator. You must select the = sign to connect values with OR.
- You can also create OR operations in the logical operations line. Create a search condition in the search input area, click the operator line, and then enter OR.
- You can only use wildcards (* and ?) when you search for text properties.
- Use the operators =, <>, <, <=, >, and >= to search for numeric properties.
- When you search for text properties, you can use only the operators = and <>.
- In the advanced search for date/time properties, for example, for the file property Creation date, the DataFinder has the following operators: =, >=, <=, and #. If you select the # operator on the DataFinder interface, you can use the following operands: Today , Yesterday , Last 7 Days , Last 14 Days , Last 30 Days. If you execute a search with the operator #, use the following operands: Today, Yesterday, LastSevenDays, LastFourteenDays, and LastThirtyDays. The DataFinder executes the search in relation to the current date. For example, if you use the operator # to search for the creation date Today, and you save the search, the search uses the then current date if you run the search again at a later date. 
To search for [date/time](../../scriptnavi/properties/navigator_property_datatype_itdmindexedproperty.htm) type custom properties, you must [optimize](../../dlgnavigator/dlgnavigator/navi_search_optimized_properties.htm) these custom properties.
- If you use the = operator when you search for date and time properties, you can search for the exact date, otherwise for the exact second.
- In the advanced search for floating point numbers, you cannot use NoValue as the operand, for example, for the channel property Maximum.
- If you search for the text Or, you must enter /Or as the search text, instead of Or.
- If you search for a text property, the property must not be longer than 255 characters.
- The search results are listed in ascending order of the values of the property of the first search condition if the following requirements are met: The property must be a base property of an optimized custom property. DIAdem must be able to clearly evaluate this property for the search result. DIAdem can clearly evaluate only file properties when it searches for files. DIAdem can clearly evaluate only file properties and channel group properties when it searches for channel groups.

|  | NoteÂ Â Refer to Evaluating Search Conditions for further examples of operations with search conditions and the evaluation of search conditions. |
| --- | --- |

#### Combining Search Results

You can combine the search results from various searches. Use the [FreeElementList<DataFinder>](../../scriptnavi/objects/navigator_objects_itdmfreedatafinderelementlist.htm) collection to collect search results in the element lists. Use the [AddElementList for FreeElementList<DataFinder>](../../scriptnavi/methods/navigator_method_addelementlist_itdmfreedatafinderelementlist.htm) method to combine these element lists.

#### Indexing the Search Areas

For the DataFinder to run a search for data from the search area, the indexer must index the data first. Click the [Indexer](../../dlgnavigator/dlgnavigator/navi_search_crawler_dialog.htm) tab of the DataFinder configuration dialog box to specify when and how often DIAdem indexes the search areas of the DataFinder. DIAdem does not start indexing before the time you specified in the dialog box elapses without a mouse movement or a key action.

The indexing process or the indexing update works under the following conditions:

- Indexing and the indexing update run automatically at the times you set on the **Indexer** tab in the **Configure DataFinder** dialog box.
- Indexing or the indexing update run automatically when contents of the search areas change or when you delete a file or create a new file.
- Open the **Configure DataFinder** dialog box, click the **Indexer** tab, and click the **Start Now** button, to start indexing or reindexing.

DIAdem displays an hourglass in the file browser next to files and search areas that the DataFinder has not indexed or has indexed inadequately. How long indexing the search areas takes, depends on the type, the number, and the size of the files to be indexed.

#### Network Drives, CD ROM, and Deleted Folders

If the search areas refer to transient folders, for example, network drives, CD or DVD drives, or memory sticks, the contents of these folders remain in the index although the folders are no longer available. In this case you can search for files, groups, and channels of these folders but you cannot navigate in the folders or load search results from the folders. The file browser identifies folders that are no longer available in a certain search area with a red exclamation mark.

If you delete a search area from the DataFinder, the DataFinder deletes the associated entry from the index. If you delete files or folders from a search area, the DataFinder updates the index. 
If you delete a folder from the search area while the DataFinder is not active, the DataFinder treats the folder like a transient folder. If you restore a deleted folder of a search area or if the transient folder is available again, the DataFinder updates the search area and you can load files from the folder.

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=genpresent/genpresent/genreport_enum.htm language=enus -->
## TOPIC 00989: Enumerations

- bundle_id: `diadem`
- source_path: `genpresent/genpresent/genreport_enum.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genpresent/genpresent/genreport_enum.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../genpresent/genreport_overview.htm) > Enumerations

Enumerations

In DIAdem REPORT and DIAdem VIEW you can use enumerations to label curves. To create an enumeration define a String type custom property named EnumValues for a channel. The enumeration texts must be separated by a delimiter in the EnumValues custom property. DIAdem uses the last character of the custom property as the delimiter. The numeric values of the channel which contains the EnumValues custom property specify how the elements of the collection are ordered. The following example illustrates the connection between the different channels.

[IMAGE alt='image' src='../image/enum_table.png']  [IMAGE alt='image' src='../image/enum_graph.png']

In this example DIAdem displays the Y Values channel over the X Values channel. The Description channel contains the custom property EnumValues with the text "abc,def,ghi,". DIAdem numbers the enumeration text starting at 1. DIAdem assigns the enumeration text to the curve points via the corresponding numeric value of the Description channel. If the Description channel has the value 1, DIAdem uses the first term of the enumeration as the label of the associated points in this case to label the second and the seventh points. The first term here is abc because the comma is the last character of the custom property EnumValues and is therefore interpreted as a delimiter by DIAdem. If the channel has the value 2, DIAdem assigns the text def to the corresponding point of the curve. If the channel has the value 3, DIAdem assigns the text ghi to the corresponding point of the curve. If the channel Description contains the value 0 or if the value is missing, DIAdem does not assign any text to the corresponding point of the curve. The channel value specifies the index of the enumeration which the custom property EnumValues contains and thus the text to which the corresponding point of the curve is assigned.

#### Related Topics

[Enumeration Channels](../../genshell/genshell/genshell_enumchannels.htm)

[Assignment channels](../../genshell/genshell/genshell_assignmentchannels.htm)

<!--NI_TOPIC bundle=diadem path=genpresent/genpresent/genreport_format.htm language=enus -->
## TOPIC 00990: Formatting Text, Numeric Values, and Time Values in Text

- bundle_id: `diadem`
- source_path: `genpresent/genpresent/genreport_format.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genpresent/genpresent/genreport_format.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../genpresent/genreport_overview.htm) > Formatting Text, Numeric Values, and Time Values in Text

Formatting Text, Numeric Values, and Time Values in Text

Use control characters to format text in DIAdem, and to insert variables, formulas, and script results into text. Use [identifiers](../genpresent/genreport_symbol_layout.htm) to format symbols in curves.

#### Displaying and Formatting Variable Contents in Text

Use the @@ character combination to display variable contents in text. You can use the Calculator operands and operations to display text. You can use all the expressions that have a single expression as the result. You must enclose the name of the variable or the Calculator expression in @@ characters. DIAdem evaluates the expression and displays the evaluated expression in the text. You can also connect normal text with expressions. Use the normal VBS syntax for linking text within the @@ expression, for example: @@"CurrDate:"& CurrDate &" CurrTime: "& CurrTime@@

|  | NoteUse three @ characters to display a single @ character in text. For example, if you want to display the e-mail address Info@ni.com in a text, enter the expression Info@@@ni.com. |
| --- | --- |

Use the [Str](../../functions/functions/str.htm) function or the [PU](../../functions/functions/pu.htm) function to format time and date values in text. Enclose the entire expression in @@ characters. Refer to [Using Variables in Text](../../procpresent/text/procpres_text_variables.htm) for more information about formatting variable contents in text. If you do not enter a format, DIAdem automatically selects a format.

#### Formatting Numeric Values in Text

Use numeric format instructions to display a specific number of decimal places, or, for example, to display data as exponents. Use the following format instructions in the Str function and in all dialog boxes where you want to format numeric values.

[[IMAGE alt='image' src='../image/arrowright.gif']Use the following numeric formats:](#nowhere)

|  | If you do not specify a format, DIAdem displays all the numeric values. |
| --- | --- |
| AutoAdj | Automatic numeric format. This format displays the number as compactly as possible, as a decimal or as an exponential. At least 3 numbers and not more than 9 characters display. DIAdem tries to manage without an exponential display. If a display without exponent returns more than 7 characters, DIAdem selects the exponential display.The AutoAdj format displays the number 123.45678 as 123.45, and displays the number 12345.678 as 123E+04. |
| d or D | Displays numbers as decimals or exponents. If you want to display numbers in decimal format, specify each digit to be displayed with d or D. For example, the format specification dd.ddd displays a number with two places before and three places after the decimal point. In numbers that have more places before the decimal point than you specified, DIAdem automatically expands the display. You cannot delete leading blanks with Trim or LTrim if you format the values with D, for example:Call MsgBoxDisp(Trim(Str(1234,"DDDDDDDDD"))) ' => " 1234" You can output leading zeros by formatting values with 0d, for example:Call MsgBoxDisp(Str(2.34,"0dd.dd")) ' =>"02.34" |
| e | Displays numbers as exponents. For example, d.dde displays the format 1.23E+01. |
| h | Displays numbers with powers of ten. For example, d.ddh displays numbers in the format 1.23*10². |
| . or, | Separates the places before and after the decimal point. For example, d.dd displays numbers in the format 1.23. |
| b | Displays numbers in binary format. For example, DIAdem displays the number 43 as 101011. |
| $ | Displays numbers in hexadecimal format.If more characters follow after the first $ character, DIAdem uses this character as the prefix for the result, for example:Call MsgBoxDisp(Str(1234,"$0x")) ' => 0x04D2If further $ characters follow after the prefix, these characters indicate the number of places. DIAdem interprets all characters behind the last $ character as postfix, for example:Call MsgBoxDisp(Str(1234,"$ $$$$$$$$hex")) ' => 000004D2hexIf no further character follows after the first $ character, DIAdem shows the number to be formatted as a hexadecimal value and uses the $ character before the numbers as ID for the hexadecimal display.Call MsgBoxDisp(Str(1234,"$")) ' => $04D2 |
| ! | Suppresses NoValues. |
| abs | Suppressing the sign. You can combine this identifier with the characters listed above, for example, abs d.dd. |
| ENG | Displays numbers in Engineering format. The Engineering format is an exponential format that has a multiple of 3 as the exponent. You specify the number of places after the decimal point with .d. For example, the format ENG.ddd specifies three places after the decimal point. If you specify a d before the decimal point, the point is always the fifth character. For example, the format ENGd.ddd specifies the display " 1.234E+03" or "-123.123E-06". With a non-proportional font, the points can be aligned to each other, for example, in tables in DIAdem VIEW or in DIAdem REPORT. |
| ENGSI | Corresponds to the display of numbers in Engineering format. This format specification adds the decimal prefixes of the International System of Units (SI) to the exponential format.Call MsgBoxDisp(Str(1234,"ENGSI.d")) ' => 1.2k Call MsgBoxDisp(Str(12,"ENGSI.dd")) ' => 1.20da |
| ENGM | Corresponds to the display of numbers in Engineering format. This format specification adds the decimal prefixes of the International System of Units (SI) to the exponential format. The format specification uses these decimal prefixes only for numbers in the thousands range.Call MsgBoxDisp(Str(1234,"ENGM.dd")) ' => 1.23k Call MsgBoxDisp(Str(12,"ENGM.dd")) ' => 12.00 |

#### Formatting Time Values in Text

To interpret data as numeric values, use # as the first character.

[[IMAGE alt='image' src='../image/arrowright.gif']Use the following format instructions for the time formats:](#nowhere)

| m or M | Month |
| --- | --- |
| d or D | Day |
| y or Y | Year |
| k | Calendar week |
| h or H | Hour |
| n or N | Minute |
| s or S | Second |
| f | Fraction of a second |

Example: Call MsgBoxDisp(Str(CurrDateTimeReal,"#MM/DD/YYYY hh:nn")) is 7/27/2005 06:00.

|  | Note If you use the uppercase in the format instructions above, DIAdem deletes leading zeros with leading nulls. The format specification hh:nn:ss displays, for example, 01:01:00, the format specification HH:NN:SS displays 1: 1: 0, and the format specification HH:nn:ss displays 1:01:00. |
| --- | --- |

| hhh or HHH | Display of the consecutive hours. More than 24 hours are possible.Example: Call MsgBox(Str(TTR("0000/01/02 03:04:05","#yyyy/mm/dd hh:nn:ss"),"#hhh:nn:ss")) is 27:04:05. |
| --- | --- |
| ampm | Display in a 12-hour format with a.m. or p.m.Example: Call MsgBoxDisp(Str(CurrDateTimeReal,"#hh:nn ampm")) is 06:00 p.m. |
| AMPM | Display in 12-hour format with AM or PMExample: Call MsgBoxDisp(Str(CurrDateTimeReal,"#hh:nn AMPM")) is 06:00 PM. |
| ap | Display in 12-hour format with a or pExample: Call MsgBoxDisp(Str(CurrDateTimeReal,"#hh:nn ap")) is 06:00 p. |
| AP | Display in 12-hour format with A or PExample: Call MsgBoxDisp(Str(CurrDateTimeReal,"#hh:nn AP")) is 06:00 P. |
| CRLF | Adds a linefeed.Example: Call MsgBoxDisp(Str(CurrDateTimeReal,"#MM/DDCRLFYYYY")) equals: 12/312018 |

Use the following format instructions to display months and days of the week as text:

| #t, #tt, #ttt, ... | Months with 1, 2, 3, ... characters, for example, Nov |
| --- | --- |
| #w, #ww, #www, ... | Days of the week with 1, 2, 3, ... characters, for example, Sun |
| #T | Months written |
| #W | Weekdays written |

|  | Note You can use the format specifications for months and weekdays only for formatted reading out of date/time specifications. |
| --- | --- |

|  | Note Use the TimeFormat variable to specify the time format that DIAdem uses when no other time format is specified. |
| --- | --- |

|  | Note Some variables, for example CurrTime, CurrDate, and CurrDateTime, return dates or time values as text. You must use the TTR function to convert the text into numeric values before you can format the text. |
| --- | --- |

|  | Note Use NRF to label a 2D axis with two lines in the time format. DIAdem repeats the first line at every scale value. DIAdem positions the bottom line in the center of the time unit. For example, if you enter the format # tttNRF yy, DIAdem displays the first three characters of the particular month at each scaled value. DIAdem displays the last two numbers of the particular year in the second line, at the position that shows the middle of the particular year.The CRLF character adds a linefeed in every row. |
| --- | --- |

|  | Note Databases often use #yyyy-mm-dd hh:nn:ss as the time format. |
| --- | --- |

#### Subscript and Superscript

[[IMAGE alt='image' src='../image/arrowright.gif']Use the following control characters for subscript and superscript:](#nowhere)

| ^h | Changes text to superscript. |
| --- | --- |
| ^t | Changes text to subscript. |
| ^n | Undoes one level of the subscript or superscript. |

You can cascade subscript and superscript. DIAdem reduces the size of each level of the subscript or superscript. For example, the Level 2 subscript is smaller than the Level 1 subscript.

#### Formatting Text with User Commands

Use [user commands](../../genshell/genshell/genshell_user_commands.htm) to execute complex formatting. For example, use a script request to label axes with text such as In the border range. You define user commands in a script. If you use user commands for format settings, you must enclose the user commands in two @@ characters, for example, @@MyFunc@@. You must [register](../../dlgscript/script_dlg_menu/dlgscriptreg_dialog.htm) scripts before you can use them.

To transfer the value currently to be formatted, use transfer parameters in functions. Use the [CurrFormatValue](../../varoff/currformatvalue.htm) variable to get the number to be formatted, for example, the current table value or the current value on the axis scaling. Use the [CurrChnNo](../../varoff/currchnno.htm) variable to use the number of the current data channel.

|  | Note The Format Numbers dialog box assists you in formatting time values and numeric values. |
| --- | --- |

#### Procedures

[Displaying Differently Formatted Text](../../procpresent/text/procpres_textobject_insert.htm) | [Inserting Text](../../procpresent/text/procpres_text_insert.htm) | [Rotating Text](../../procpresent/text/procpres_text_rotate.htm) | [Subscript and Superscript](../../procpresent/text/procpres_text_format.htm) | [Using Variables in Text](../../procpresent/text/procpres_text_variables.htm)

<!--NI_TOPIC bundle=diadem path=genpresent/genpresent/genreport_interactivescaling.htm language=enus -->
## TOPIC 00991: Manual Axis Scaling in a Report

- bundle_id: `diadem`
- source_path: `genpresent/genpresent/genreport_interactivescaling.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genpresent/genpresent/genreport_interactivescaling.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../genpresent/genreport_overview.htm) > Manual Axis Scaling in a Report

Manual Axis Scaling in a Report

Use the manual axis scaling functions to modify the value range of an x-axis or a y-axis with the mouse without opening the associated dialog boxes. To manually scale an axis, move the cursor over the scale of the x-axis or the y-axis. DIAdem changes the shape of the cursor depending on its position:

| Cursor | Meaning |
| --- | --- |
|  | This cursor appears when you position the mouse pointer in the upper part of the scale of a y-axis. If you left-click and drag the mouse upwards or turn the mouse wheel forwards, you shrink the value range of the axis. If you left-click and drag the mouse downwards, or turn the mouse wheel backwards, you expand the value range of the axis. The lower limit value of the scale does not change in either case. |
|  | This cursor appears when you position the mouse pointer in the lower part of the scale of a y-axis. If you left-click and drag the mouse upwards or turn the mouse wheel forwards, you expand the value range of the axis. If you left-click and drag the mouse downwards, or turn the mouse wheel backwards, you shrink the value range of the axis. The upper limit value of the scale does not change in either case. |
|  | This cursor appears when you position the mouse pointer in the central part of the scale of a y-axis. If you left-click and drag the mouse upwards or downwards, you move the value range of the axis into the respective direction. If you turn the wheel forwards, you shrink the value range of the axis. If you turn the wheel backwards, you expand the value range of the axis. |
|  | This cursor appears when you position the mouse pointer in the left part of the scale of an x-axis. If you left-click and drag the mouse to the left, or turn the mouse wheel backwards, you shrink the value range of the axis. If you left-click and drag the mouse to the right, or turn the mouse wheel forwards, you expand the value range of the axis. The right limit value of the scaling does not change in either case. |
|  | This cursor appears when you position the mouse pointer in the central part of the scale of an x-axis. If you left-click and drag the mouse to the left or to the right, you move the value range of the axis into the respective direction. If you turn the wheel forwards, you shrink the value range of the axis. If you turn the wheel backwards, you expand the value range of the axis. |
|  | This cursor appears when you position the mouse pointer in the right part of the scale of an x-axis. If you left-click and drag the mouse to the left, or turn the mouse wheel backwards, you expand the value range of the axis. If you left-click and drag the mouse to the right or turn the mouse wheel forwards, you shrink the value range of the axis. The left limit value of the scale does not change in either case. |

|  | Note Press <Ctrl> to accelerate scaling with the mouse wheel. |
| --- | --- |

|  | Note Use Scale Axis Automatically in the context menu of the axis to use automatic axis scaling. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=genpresent/genpresent/genreport_masterlayout.htm language=enus -->
## TOPIC 00992: Master Layouts

- bundle_id: `diadem`
- source_path: `genpresent/genpresent/genreport_masterlayout.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genpresent/genpresent/genreport_masterlayout.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../genpresent/genreport_overview.htm) > Master Layouts

Master Layouts

Use master layouts to save recurring parts of a layout and to add them to different layouts. Link layouts to master layouts, for example, to display logos or other graphics and decorations automatically in layouts. If you change the master layout, you can refresh the layouts that are linked to the master layout manually, or automatically every time you load the layouts.

The master layout contains graphics objects and basic [Layout parameters](../genpresent/genreport_masterlayout.htm). If a layout is linked to a master layout, you specify the **Global page format** the **Frame**, and the **Automatic scaling** in the master layout.

Use the [Use Master Layout](../../dlgpresent/graph_dlg_menu/dlgmasterlayout_dialog.htm) dialog box to link a layout to a master layout, to delete a master layout, or to refresh a master layout. Use the menu **File»Master Layout** to create, to open, or to save master layouts. A master layout always consists of the **Portrait Master** for portrait layouts and the **Landscape Master** for landscape layouts.

Connect the layout that you entered as the **Template** in the [DIAdem REPORT Settings](../../dlgpresent/graph_dlg_menu/dlgconfgraph_dialog.htm) dialog box to a master layout, in order to automatically connect every new layout to a master layout.

|  | Note You can also use other graphics objects such as axis systems and tables in a master layout. If you want to use data-related objects, use the master layout always with the same data type, because you only can change the objects of a master layout in the master layout itself. |
| --- | --- |

#### Procedures

[Creating a Master Layout](../../procpresent/report_general/procpres_masterlayout_connect.htm) | [Using Master Layouts](../../procpresent/report_general/procpres_masterlayout_use.htm)

<!--NI_TOPIC bundle=diadem path=genpresent/genpresent/genreport_mathml.htm language=enus -->
## TOPIC 00993: MathML in Formula Graphics

- bundle_id: `diadem`
- source_path: `genpresent/genpresent/genreport_mathml.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genpresent/genpresent/genreport_mathml.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../genpresent/genreport_overview.htm) > MathML in Formula Graphics

MathML in Formula Graphics

MathML stands for Mathematical Markup Language and is a format for displaying mathematical formulas. DIAdem supports the standard MathML 2.0.

MathML offers various options for describing mathematical expressions:

| Presentation Markup | This description type is suitable for presentations. It specifies the exact order and sequence of the operations and operators within the formula based on the formula display. |
| --- | --- |
| Content Markup | This type of description is suitable for exchanging the formula with mathematical applications. It is based on the formula contents and specifies which operations and operators the formula uses. |
| Mix Markup | This description is a mix of presentation description and content description. |

Visit the website http://www.w3.org/TR/MathML2 for further information on MathML.

If you enter a formula text in a formula graphic in DIAdem REPORT, DIAdem generates a MathML presentation description from this entry.

Enter the text of the formula graphic in the same way that you enter formulas in the DIAdem Calculator. DIAdem generates and displays a presentation description from the entered formula. For example, if you enter sqr, DIAdem displays a square root. In the formula text you not are limited to the variable identifier provided by DIAdem. You also can enter f(x)=sqr(y/2). You can check the entry or the change of the formula text in the preview. DIAdem displays the formula mathematically and marks the missing or non-interpretable operands and operations with a red frame. If the preview displays a square in the specified font color instead of a specific character of the formula text, the selected character set does not contain this character.

If you enclose the variable contents in @@ characters in the text of the formula graphic, DIAdem tries to display these variable contents as a formula.

Use the MathML syntax in the [Formula Graphics](../../dlgpresent/graph_dlg_annotation/fml_tab_text_dialog.htm) dialog box to display complex formulas. For example, enter the following text to display a two-dimensional matrix:

<math xmlns="http://www.w3.org/1998/Math/MathML"> 
  <mrow> 
    <mi>A<‌/mi> 
    <mo>=<‌/mo> 
    <mfenced open="[" close="]"> 
      <mtable> 
        <mtr> 
          <mtd><mi>x<‌/mi><‌/mtd> 
          <mtd><mi>y<‌/mi><‌/mtd> 
        <‌/mtr> 
        <mtr> 
          <mtd><mi>z<‌/mi><‌/mtd> 
          <mtd><mi>b<‌/mi><‌/mtd> 
       <‌/mtr> 
     <‌/mtable> 
    <‌/mfenced> 
  <‌/mrow> 
<‌/math>

DIAdem generates the following graphical formula from this text:

[IMAGE alt='image' src='../image/f_matrix.gif']

<!--NI_TOPIC bundle=diadem path=genpresent/genpresent/genreport_nameoriented_mode.htm language=enus -->
## TOPIC 00994: Name-Oriented Mode

- bundle_id: `diadem`
- source_path: `genpresent/genpresent/genreport_nameoriented_mode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genpresent/genpresent/genreport_nameoriented_mode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../genpresent/genreport_overview.htm) > Name-Oriented Mode

Name-Oriented Mode

In DIAdem REPORT you use the name-oriented mode, which combines the group name or the group index with the channel name or the channel index in channel references. You can use the expanded mode or the non-expanding mode. If you use the non-expanding mode, DIAdem only uses the first data channel that has the specified name, in the graphic display. If you use the expanding mode, DIAdem displays all the data channels that have the specified name.

You can [reference channels](../../genshell/genshell/genshell_data_channels.htm) in various ways in dialog boxes or scripts. To create the channel reference, combine the group name or the group index with the channel name or the channel index. This specifies the channel unambiguously. Refer to the [Channels and Channel References](../../genshell/genshell/genshell_data_channels.htm) help page for more information.

If you load a layout with [Curve Expansion](../../dlgpresent/graph_dlg_menu/dlglayoutdisplay_dialog.htm) in DIAdem REPORT, you can use the same channel names in different groups when expanding the curves or you can use channel names which contain wildcards. If you enable the group reference, DIAdem only displays the channel pairs in the expanding mode that belong to the same channel group.

Use the [Enable for CurveExpansionSettings](../../reportapi/properties/report_property_enable_irepexpansionsettingsint.htm) property to specify whether DIAdem uses the expanding or the non-expanding mode.

As of version 2019, DIAdem no longer supports layouts that use channel numbers. For this reason you can access the property [UseChannelReferenceByName](../../reportapi/properties/report_property_usechannelreferencebyname_irepsettingsint.htm) only in read-only mode. This variable now always has the value TRUE. To convert a number-oriented layout into a name-oriented layout, load the layout to be converted in DIAdem 2018 or earlier, load a suitable data set and execute the [ConvertToChannelReferenceByName](../../reportapi/methods/report_method_converttochannelreferencebyname_irepsettingsint.htm) method.

#### Example

Assumption: In the data area DIAdem contains three channel groups which each contain one data channel called time and one data channel called speed. If you set the display as */speed over */time in the 2D axis definition dialog box, the display in the expanding mode is different to the display in the non-expanding mode.

In the non-expanding mode, DIAdem plots a curve with speed over time. In the expanding mode, DIAdem displays three curve pairs with time over speed.

|  | Note You enable the name-oriented mode in the Layout Parameters dialog box. Select the expanding or the non-expanding mode in the subdialog box Curve expansion. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=genscript/genscript/genscript_vbs_systemlinktdm.htm language=enus -->
## TOPIC 00995: Controlling SystemLink TDM with a VBS script

- bundle_id: `diadem`
- source_path: `genscript/genscript/genscript_vbs_systemlinktdm.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genscript/genscript/genscript_vbs_systemlinktdm.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem SCRIPT](../genscript/genscript_overview.htm) > Controlling SystemLink TDM with a VBS script

Controlling SystemLink TDM with a VBS script

You can control the SystemLink TDM panels in DIAdem with a VBS script. For example, you can use a script to create a DataFinder instance, define search areas for that DataFinder instance and start the instance, and create and configure a Data Preprocessor instance. You can also use a VBS script to create an Analysis Automation instance and perform a data analysis.

The following sample script creates an Analysis Automation instance, prompts you to load an Analysis Automation procedure, creates a manual task, specifies the data source for the analysis, and checks the status of the analysis. The example then deletes the created instances. To use a data source in the script, you must uncomment the corresponding lines in the script. The example script does not create a search area and therefore does not search for data.

[Copy script](javascript:void(0);)

```text
Option Explicit  'Enforces the explicit declaration of all variables in a script.

Dim oRequest, oJsonParser, serverURL, asServerAvailable, asServerName, dataFinderName, manualTaskName, user, password, procName, authString

Set oRequest = CreateObject("MSXML2.ServerXMLHTTP.6.0")
Set oJsonParser = CreateJsonParser()

'Please change the following values according to your requirements 
asServerAvailable = true
serverURL = "http://server:port"
asServerName = "TestAS"
dataFinderName = "TestDataFinder"
manualTaskName = "ManualTestTask"
procName = "TestASProcedure"

if len (T10) = 0 then 
  user = Inputbox("Your user name:", "User","Name.Lastname@ni.com")
  password = Inputbox("Your user password:", "Password","")
  authString = "Basic " & Base64(user & ":" & password)  
  T10 = authString
else
  authString = T10 
end if

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'If not available, create an Analysis Automation instance------------------------------------------------------------------------------------------------------------------
Dim oNewASRequest, newASRequestString, asId, sASResponseString, oASResponseObject, oLinkObject, linkArray, itemArray


If Not asServerAvailable Then 'Check, whether the instance already exists -> if not, a new instance is created; if yes, the old serverID is used

  'Build new AS
  Set oNewASRequest = CreateObject("Scripting.Dictionary")

  Call oNewASRequest.Add("name", asServerName) 

  newASRequestString = oJsonParser.Serialize(oNewASRequest)

  'Create new AS
  sASResponseString = sendRequest("Post", serverURL & "/TDMServer_as/analysisservers", newASRequest)

  Call oJsonParser.Deserialize(sASResponseString, oASResponseObject)
  linkArray = Split(oASResponseObject.Item("link"),"/")
  asId = linkArray(UBound(linkArray))

Else
  
  sASResponseString = sendRequest("Get",serverURL & "/TDMServer_as/analysisservers", null)
  
  Call oJsonParser.Deserialize(sASResponseString, oASResponseObject)
  itemArray = oASResponseObject.Item("items")
  linkArray = Split(itemArray(0).item("link"),"/")
  asId = linkArray(UBound(linkArray))
  
End If

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'ProcId determined from the list of all procedures with "name matching"-----------------------------------------------------------------------------------------------------

MsgBox "Please upload an Analysis Automation procedure with the name assigned in the script header"

Dim procId, sProcedureListGetResponseString, oProcedureListGetResponseObject, tempId, item, tempName

sProcedureListGetResponseString = sendRequest("Get", serverURL&"/TDMServer_as/analysisservers/"&asId&"/analysisprocedures?expand=analysisprocedurename" , null)

Call oJsonParser.Deserialize(sProcedureListGetResponseString, oProcedureListGetResponseObject)
itemArray = oProcedureListGetResponseObject.Item("items")

For each item in itemArray

  tempName = item.Item("analysisprocedurename")
  
  if procName = tempName Then 
  
    linkArray = Split(item.Item("link"),"/")
    procId = linkArray(UBound(linkArray))
    Exit For
    
  End If
  
Next

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'Example for creating and starting a DataFinder and determining the associated DataSourceId in Analysis Automation------------------------------------------------------------
'
'Dim dataFinderId, oDataFinderPostRequest, oDataFinderAdaptorItem, sDataFinderPostString, sDataFinderResponseString, oDataFinderResponseObject
'
'
'Set oDataFinderPostRequest = CreateObject("Scripting.Dictionary")
'Set oDataFinderAdaptorItem = CreateObject("Scripting.Dictionary")
'
'Call oDataFinderAdaptorItem.Add("dbtype", "eAdaptorTypeStandard")
'
'Call oDataFinderPostRequest.Add("name", dataFinderName)
'Call oDataFinderPostRequest.Add("adaptor", oDataFinderAdaptorItem)
'
'sDataFinderPostString = oJsonParser.Serialize(oDataFinderPostRequest)
'
''Send request
'
'sDataFinderResponseString = sendRequest("Post",serverURL&"/TDMServer_dfse/datafinders",sDataFinderPostString)
'
''Specify DataFinderId
'Call oJsonParser.Deserialize(sDataFinderResponseString, oDataFinderResponseObject)
'linkArray = Split(oDataFinderResponseObject.Item("link"),"/")
'dataFinderId = linkArray(UBound(linkArray))
'
''Match DataSource with DataFinder---------------------------------------------------------------------
'
'Dim dataSourceId, sDataSourceGetResponseString, oDataSourceGetResponseObject, running, runningStatus, tempNameArray
'
'sDataSourceGetResponseString = sendRequest("Get",serverURL & "/TDMServer_as/analysisservers/" & asId & "/datasources/datafinder?expand=name",null)
'
'Call oJsonParser.Deserialize(sDataSourceGetResponseString, oDataSourceGetResponseObject)
'itemArray = oDataSourceGetResponseObject.Item("items")
'
'For each item in itemArray
'
'  tempNameArray = Split(item.Item("name"),"@")
'  tempName = tempNameArray(0)
'  
'  if dataFinderName = tempName Then 
'  
'    linkArray = Split(item.Item("link"),"/")
'    dataSourceId = linkArray(UBound(linkArray))
'    Exit For
'    
'  End If
'  
'Next 
'
''Start DataFinder
'
'Call sendRequest("Post",serverURL & "/TDMServer_dfse/datafinders/" & dataFinderId & "/actions/start",null)
'
'running = false
'
'While(NOT running)
'
'  pause(0.5)
'
'  sDataFinderResponseString = sendRequest("Get",serverURL & "/TDMServer_dfse/datafinders/" & dataFinderId,null)
'  
'  Call oJsonParser.Deserialize(sDataFinderResponseString, oDataFinderResponseObject)
'  runningStatus = oDataFinderResponseObject.Item("status")
'  
'  If runningStatus = "eServerStatusStarted" Then
'    running = true
'  End If
'  
'Wend

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'Create Manual Task----------------------------------------------------------------------------------------------------------------------------------------------

Dim oManualTaskPostRequest, sManualTaskPostString, oArrayEntry, oManualTaskResponseObject, sManualTaskResponseString, manualTaskId

Set oManualTaskPostRequest = CreateObject("Scripting.Dictionary")
Set oArrayEntry = CreateObject("Scripting.Dictionary")

Call oArrayEntry.Add("name", "testInt")
Call oArrayEntry.Add("type","Int")
Call oArrayEntry.Add("value","1")
Call oArrayEntry.Add("description","")

Call oManualTaskPostRequest.Add("manualtaskname", manualTaskName)
Call oManualTaskPostRequest.Add("analysisprocedureid", procID) 
Call oManualTaskPostRequest.Add("datasourceid", null ) 'If a DataFinder exists, replace null with the DataSourceId
Call oManualTaskPostRequest.Add("parameters", Array(oArrayEntry))
Call oManualTaskPostRequest.Add("active", true) 
Call oManualTaskPostRequest.Add("usercontext", "eTaskUserContextServerAccount") 

sManualTaskPostString = oJsonParser.Serialize(oManualTaskPostRequest)

'Send request

sManualTaskResponseString = sendRequest("Post",serverURL & "/TDMServer_as/analysisservers/" & asId & "/manualtasks",sManualTaskPostString)

'Evaluate response

Call oJsonParser.Deserialize(sManualTaskResponseString, oManualTaskResponseObject)
linkArray = Split(oManualTaskResponseObject.Item("link"),"/")
manualTaskId = linkArray(UBound(linkArray))

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'Start task-----------------------------------------------------------------------------------------------------------------------------------------------------------

Dim manualTaskExecutionId, oManualTaskStartResponseObject, sManualTaskStartResponseString

sManualTaskStartResponseString = sendRequest("Post",serverURL & "/TDMServer_as/analysisservers/" & asId & "/manualtasks/" & manualTaskId & "/actions/start",null)

Call oJsonParser.Deserialize(sManualTaskStartResponseString, oManualTaskStartResponseObject)
manualTaskExecutionId = oManualTaskStartResponseObject.Item("taskexecutionid")


'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'Check task status-----------------------------------------------------------------------------------------------------------------------------------------------------

Dim oTaskExecutionResultObject, sTaskExecutionResultString, bExecutingFinished, sProcessingStatus, sOutcomeStatus

bExecutingFinished = false

While(NOT bExecutingFinished)

  pause(2)

  sTaskExecutionResultString = sendRequest("Get",serverURL & "/TDMServer_as/analysisservers/" & asId & "/taskexecutions/" & manualTaskExecutionId,null)
  
  Call oJsonParser.Deserialize(sTaskExecutionResultString, oTaskExecutionResultObject)
  sProcessingStatus = oTaskExecutionResultObject.Item("processingstatus")
  
  If sProcessingStatus = "eTaskProcessingStatusFinished" Then
    bExecutingFinished = true
  End If
  
Wend

Call oJsonParser.Deserialize(sTaskExecutionResultString, oTaskExecutionResultObject)
sOutcomeStatus = oTaskExecutionResultObject.Item("outcomestatus")

LogfileWrite "===Result==="

Select Case sOutcomeStatus
    Case "eTaskOutcomeStatusNotExecuted"
      LogfileWrite "> Task was not executed"
    Case "eTaskOutcomeStatusCanceled"
      LogfileWrite "> Task was canceled"
    Case "eTaskOutcomeStatusNoData"
      LogfileWrite "> Task does not provide data"
    Case "eTaskOutcomeStatusSuccess"
      LogfileWrite "> Task processed successfully"
    Case "eTaskOutcomeStatusWarning"
      LogfileWrite "> Warning!"
    Case "eTaskOutcomeStatusTimeout"
      LogfileWrite "> Task timed out"
    Case "eTaskOutcomeStatusError"
      LogfileWrite "ERROR!"
    Case Else
      'Statement
End Select

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'Delete DataFinder, Task and Procedure-----------------------------------------------------------------------------------------------------------------------------------------------------

''Example for stopping and deleting a DataFinder
'
'Call sendRequest("Post",serverURL & "/TDMServer_dfse/datafinders/" & dataFinderId & "/actions/stop",null)
'
'While(running)
'
'  pause(0.5)
'
'  sDataFinderResponseString = sendRequest("Get",serverURL & "/TDMServer_dfse/datafinders/" & dataFinderId,null)
'  
'  Call oJsonParser.Deserialize(sDataFinderResponseString, oDataFinderResponseObject)
'  runningStatus = oDataFinderResponseObject.Item("status")
'  
'  If runningStatus = "eServerStatusStopped" Then
'    running = false
'  End If
'  
'Wend
'
''Delete DataFinder
'Call sendRequest("Delete",serverURL&"/TDMServer_dfse/datafinders/"&dataFinderId,null)

'Delete task
Call sendRequest("Delete",serverURL & "/TDMServer_as/analysisservers/" & asId & "/manualtasks/" & manualTaskId,null)


''Delete procedure (If a procedure is deleted, all tasks dependent on this procedure are also deleted)
'Call sendRequest("Delete",serverURL&"/TDMServer_as/analysisservers/"&asId&"/analysisprocedures/"&procId,null)


'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'Help functions for Base64----------------------------------------------------------------------------------------------------------------------------------------------

Function Base64(ByVal sText)

    With CreateObject("Msxml2.DOMDocument").CreateElement("aux")
        .DataType = "bin.base64"
        .NodeTypedValue = StrToBytes(sText, "utf-8", 3)
        Base64 = .Text
    End With

End Function

Function StrToBytes(ByVal sText, ByVal sTextEncoding, ByVal iBomByteCount)

    With CreateObject("ADODB.Stream")
        .Type = 2  
        .Charset = sTextEncoding
        .Open
        .WriteText sText
        .Position = 0 
        .Type = 1 
        .Position = iBomByteCount 
        StrToBytes = .Read
        .Close
    End With 

End function

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Function sendRequest(ByVal sType, byVal sUrl, byVal sContent) 

  oRequest.open sType, sUrl, false 
  oRequest.setRequestHeader "Content-Type", "application/json" 
  oRequest.setRequestHeader "Accept", "application/json" 
  oRequest.setRequestHeader "User-Agent", "curl/7.50.1" 
  oRequest.setRequestHeader "Authorization", authString 

  If sContent = null Then
    oRequest.send
  Else
    oRequest.send (sContent)
  End If
  
  sendRequest = oRequest.responseText
  
End Function
```

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_basciinformation_overview.htm language=enus -->
## TOPIC 00996: Basic Information

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_basciinformation_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_basciinformation_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > Basic Information

Basic Information

The subordinate topics contained in the tree on the contents tab of the Help provide basic information about working with DIAdem. The topics introduce you to the DIAdem interface and folder structure and describe how to drag and drop items in DIAdem. You will also learn how to work with user commands, events, and objects and how to modify DIAdem behavior after you have launched the program.

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_channels_overview.htm language=enus -->
## TOPIC 00997: Channels

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_channels_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_channels_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > Channels

Channels

The subordinate topics contained in the tree on the contents tab of the Help describe the various DIAdem channel types and show you how to access the channels.

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_channeltypes.htm language=enus -->
## TOPIC 00998: Channel Types

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_channeltypes.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_channeltypes.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > [Channels](../genshell/genshell_channels_overview.htm) > Channel Types

Channel Types

DIAdem organizes data into channels. When you load data, DIAdem recognizes the channel type of the individual channels and marks the channel type in the Data Portal with the respective symbol. You can drag and drop data into the Data Portal or you use the functions [Load](../../dlgnavigator/dlgnavigator/navi_file_load_dialog.htm), [Selective opening, or Register](../../dlgnavigator/dlgnavigator/navi_file_load_selective_dialog.htm) to load or register data from the [DIAdem NAVIGATOR](../../gennavigator/gennavigator/navi_general.htm) into the Data Portal. When you create a new channel in the Data Portal, you can specify whether the channel is a numeric channel, a calculation channel, a text channel, a video channel, or a date/time channel. You can also use the functions [Generate Numeric Channel](../../dlgmaths/calc_basis_dlg/dlgchngen_dialog.htm), [Generate Time Channel](../../dlgmaths/calc_basis_dlg/dlgchngentime_dialog.htm), and [Numeric Channels <-> Waveform Channel](../../dlgmaths/calc_basis_dlg/dlgchntowfchn_dialog.htm) to generate new channels. Use the function [Numeric Channels <-> Assignment Channels](../../dlgmaths/calc_basis_dlg/dlganaassignment_dialog.htm) to connect numeric channels and waveform channels with assignments.

DIAdem supports the following channel types:

| Channel Type | Description |  |
| --- | --- | --- |
|  | Numeric channel | Numeric channels contain the x-part or the y-part of a curve. Numeric values are measured values, calculation results, or entered values.Use numeric channels in calculations and displays as an x-channel and a y-channel. If you use numeric channels as the y-channel in axis systems and do not specify an x-channel, DIAdem displays the numeric channels over the serial index. Index channels do not have a unit. |
|  | Time channel | Time channels contain, for example, the time values of a measurement. DIAdem saves absolute time data in a time channel. Use the DIAdem setting High resolution for absolute time values to increase the accuracy of created time data. You can specify any format for the display of time data. Use the function Generate Time Channel to create time channels.Use time channels as the x-channel in displays and calculations to display the measured values over time. In DIAdem REPORT and DIAdem VIEW you can choose between an absolute and a relative display for time channels. |
|  | Waveform channel | Waveform channels contain the x-part and the y-part of a curve in a channel. The x-part might be the measured time, for example. The Waveform properties specify the x-part that is a linear specification with a start value and a step width. The y-part contains the measurement values. Use the function Numeric Channels <-> Waveform Channels generate waveform channels.Use waveform channels in calculations and curve displays as the y-channel and do not specify an x-channel. Observe the Rules for Calculating with Waveform Channels. In DIAdem REPORT and DIAdem VIEW you can choose between an absolute and a relative display for time channels. |
|  | XY-channel | XY-channels contain the y-part of a curve and the reference to an x-channel. Use the function Numeric Channels <-> XY-Channels to create xy-channels. The x-channel must be in the same channel group as the xy-channels. DIAdem displays the name of the x-channel in the Data Portal in the X-Channel Reference property.In dialog boxes for calculations and curves, you enter xy-channels only for the y-channel. DIAdem automatically adds the x-channel. In curve displays, you do not need to specify the x-channel if the y-channel is a waveform channel or if the y-channel is an xy-channel and you have selected the When plotting xy-channels, automatically determine x-channel if not populated setting in the General DIAdem Settings. |
|  | Text channel | Text channels contain text, for example, observations and comments. DIAdem saves text channels in Unicode.Use text channels in tables in DIAdem VIEW and DIAdem REPORT. You can edit text channels in channel tables in DIAdem VIEW. |
|  | Assignment channel | Assignment channels are numeric, waveform, or xy-channels that connect specific values or value ranges in the Assignments channel property with texts, for example, "Valve open" for the value range 5...10 [bar].Use the mathematical function Numeric Channels <-> Assignment Channels to link numeric, waveform, or time channels with assignments. This function reads the assignment texts from text channels, assignment channels, or Enumeration channels. |
|  | Calculation Channel | Calculation channels are numeric, waveform, text, or xy-channels that are the result of a calculation. Select the Calculation property and click the button with the three dots to open the formula or calculation.In the context menu of the Data Portal, use the New»Formula Channel function to enter and calculate a Formula. |
|  | Video channel | Video channels contain the path to a video file, the frame rate and the start time. The path can be absolute or relative. If you save the data file to another target folder, DIAdem does not automatically copy the video files of the video channels, nor does it change the associated relative paths. |
|  | Complex channel | Complex channels contain the real and imaginary parts of a curve. DIAdem stores the values alternately in the channel, alternating between the real and the imaginary part. Complex channels can also be XY and waveform channels.Complex channels are a preview feature. Preview features are new developments that will be available as a full feature in one of the upcoming DIAdem versions. The user interface, the API, and the scope of functions is subject to change. |

In the Data Portal numeric channels, date/time channels, and calculation channels can be explicit, implicit, and registered channels. Waveform channels and text channels can be explicit or registered channels. Video channels can be registered channels.

#### Registered Channels

Use the **Register** function in the [Open file](../../dlgnavigator/dlgnavigator/navi_file_load_dialog.htm) dialog box or the context menu in DIAdem NAVIGATOR to register large data sets in the Data Portal. DIAdem does not load the data into the internal storage area. DIAdem creates a reference to the data. You can run calculations with channels from registered data sets and display the channels in graphics. Registered data sets are read only. If you changed a registered data set, you cannot store this data set under the same name. To edit a channel in a registered data set and to save the changes under the same data set name, you must first [expand](../../procportal/procportal/procportal_expanding_channels.htm) all channels of the registered data set.

When you register a data set that contains calculation channels, DIAdem always loads all of the calculation channels.

DIAdem flags registered channels in the Data Portal with an additional arrow in the lower left corner of the symbol, for example:

|  | Registered waveform channel |
| --- | --- |

#### Implicit Channels

Use the dialog box [Generate Numeric Channel](../../dlgmaths/calc_basis_dlg/dlgchngen_dialog.htm) and select the **Generate implicit channel** checkbox to generate an implicit channel. An implicit channel contains linear generation specifications, which describes the data, instead of single values. Implicit channels are read only. If you want to edit implicit channels, you must [expand](../../procportal/procportal/procportal_expanding_channels.htm) the channels. The properties of implicit channels are write-protected. You can change the generation rule of an implicit channel in the Data Portal with the properties **Start value** (implicit_start) and **Step width** (implicit_increment).

DIAdem flags implicit channels in the Data Portal with an additional green "i" at the bottom left of the symbol, for example:

|  | Implicit waveform channel |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_diadem_structure.htm language=enus -->
## TOPIC 00999: The DIAdem Interface

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_diadem_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_diadem_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > [Basic Information](../genshell/genshell_basciinformation_overview.htm) > The DIAdem Interface

The DIAdem Interface

DIAdem consists of panels that execute various tasks. For example, use the DIAdem ANALYSIS panel for mathematical calculations or the DIAdem REPORT panel to display data in graphics.

[IMAGE alt='image' src='../image/intro_overview.png']

The following table gives you an overview of the DIAdem interface elements. The numbers refer to the graphic:

| Element | Meaning |
| --- | --- |
| 1. Panel bar | The panel bar is on the left side of the DIAdem interface. Click the respective button to open a panel. |
| 2. Group Bar | In the panels, the group bar is to the right of the panel bar. DIAdem combines panel functions in the buttons of the group bar. |
| 3. Function group | Each symbol of the group bar panel has a function group. When you click a button in the function group, DIAdem executes the respective function or opens a dialog box where you can make settings for the function. |
| 4. Tooltip | If you idle the mouse on a button, a tooltip appears. |
| 5. Toolbar | The toolbar is beneath the menu bar. When you click a button on the toolbar, DIAdem executes the respective action or opens a dialog box where you can specify values for this command. |
| 6. Data Portal | The Data Portal is always on the right side of the DIAdem interface. The Data Portal displays an overview of the loaded data. You can drag and drop data from the Data Portal into a panel, for example, to display data in a report. To load data, you also can drag and drop the data from the DIAdem NAVIGATOR panel into the Data Portal. |
| 7. Workspace | Each panel has its own workspace. For example, use the workspace to create a report in the DIAdem REPORT panel or to create a script in the DIAdem SCRIPT panel. |
| 8. Channel properties | The Data Portal displays the channel properties of the selected channel. You can edit some properties such as the units. |

|  | Note DIAdem supports the notification area of the Windows taskbar. DIAdem, for example, displays a throbber, information icons of a running script, or the status of a message. |
| --- | --- |

|  | Note DIAdem does not support high-contrast Windows themes. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_enumchannels.htm language=enus -->
## TOPIC 01000: Enumeration Channels

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_enumchannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_enumchannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > [Channels](../genshell/genshell_channels_overview.htm) > [Channel Types](../genshell/genshell_channeltypes.htm) > Enumeration Channels

Enumeration Channels

Enumeration channels are numeric or waveform channels with the custom property EnumValues. The custom property contains text with which you can [Label curves](../../genpresent/genpresent/genreport_enum.htm) in DIAdem REPORT and DIAdem VIEW and create [Assignments](../genshell/genshell_assignmentchannels.htm) in DIAdem ANALYSIS.

|  | Note Use the Assignment channels introduced in DIAdem 2014 instead of enumeration channels. Assignment channels offer differentiated possibilities for connecting channel values with text information and for saving these with the channels. |
| --- | --- |

To create an enumeration channel, define for a channel a String type [Custom property](../../dlgportal/dlgportal/portal_additional_properties_dialog.htm) called EnumValues. Enter various texts separated by a separator but without spaces, for example, Low;Medium;High; into this custom property. The closing separator indicates to DIAdem which character to interpret as the separator.

If an enumeration channel only has the custom property EnumValues, the first enumeration Low has the value 0, the second enumeration Medium has the value 1, and the third enumeration High has the value 2. The values of the numeric or waveform channel determine the display order of the enumerations on a curve. DIAdem writes the text Low on the curve at the place where the value 0 is in the channel. The same applies for the value 1 and Medium, and the value 2 and High. The figures on the [Enumeration](../../genpresent/genpresent/genreport_enum.htm) page illustrate the connection between the custom property and the channel values.

If an enumeration channel has the custom property EnumValues and also the CANEnumSubst custom property, the values of the CANEnumSubst custom property are assigned to the enumerations. The order specifies the assignment of the elements of the two custom properties. The first enumeration receives the first value and the number of elements in the two custom properties must be the same. If CANEnumSubst has the values 0;5;7;, DIAdem writes the text High at the curve point where the enumeration channel has the value 7.

#### Related Topics

[Enumerations](../../genpresent/genpresent/genreport_enum.htm)

[Assignment channels](../genshell/genshell_assignmentchannels.htm)
