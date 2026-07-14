# NI DOCUMENT BUNDLE: diadem

<!--NI_BUNDLE_CHUNK bundle=diadem start=251 end=500 -->
<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_replicate.htm language=enus -->
## TOPIC 00251: Replicator

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_replicate.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_replicate.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Replicator

Replicator

Use this packet block to copy data packets and to output data packets repeatedly.

#### Settings

| Continuous | Specifies that DIAdem outputs a data packet to the block diagram continuously until the end of the measurement. Use this setting, for example, for repeated use of a data packet that contains set points or comparative data. |
| --- | --- |
| Number of copies | Specifies that DIAdem outputs a data packet n times to the block diagram. |
| Number of repetitions | Specifies the number of repetitions. |
| Infinite copies of the current packet | Specifies that DIAdem outputs the data packet to the block diagram repeatedly until a new data packet arrives. Use this setting to synchronize data signals of which the data packets arrive irregularly and at long intervals with fast data signals. |
| Delete unused packages | Specifies that DIAdem rejects incoming data packets during a repetition cycle. |
| Hold packages | Specifies that DIAdem saves incoming data packets to the clipboard during a repetition cycle. If you select this setting, DIAdem also stops the packet blocks File-I/O and Generator. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_sammeln.htm language=enus -->
## TOPIC 00252: Merge

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_sammeln.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_sammeln.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Merge

Merge

Use this packet block to merge data packets from several packet buses to one new multi-channel data packet. The data packets from the input signals must have the same packet size and sampling frequency. If the incoming data packets have different units, DIAdem uses the unit of the first data packet. The incoming data packets can be single-channel or multi-channel data packets.

DIAdem arranges the data of the individual channels in multi-channel data packets value-wise. DIAdem first enters all first values, then all second values, and so on, into one data packet. The number of channels a data packet contains is indicated at the beginning of the multi-channel data packet. The packet blocks [Oscilloscope](../dac_packet_osci/hb_oszilloskop.htm), [File-I/O](../dac_packet_dlg_disp_io/hb_datei.htm), [Relay Switch](../dac_packet_dlg_handling/hb_relais.htm), [Copy](../dac_packet_dlg/hb_tstueck.htm), and [Voltmeter](../dac_packet_voltmeter/hb_voltmeter.htm) can process multi-channel data packets.

#### Settings

| Number of input channels to be merged | Specifies the number of signal inputs. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_schieberegister.htm language=enus -->
## TOPIC 00253: Offset Register

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_schieberegister.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_schieberegister.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Offset Register

Offset Register

Use this packet block to output large data packets in smaller overlapping sub packets and to change the packet size.

Settings

| Offset | Specifies the overlapping width with which the offset register outputs the data packets. |
| --- | --- |
| Values | Specifies the size of the offset as the number of values per data channel. |
| Percentage of the packet size | Specifies the size of the offset as a percentage of the packet size of the incoming data packets. |
| New packet size | Specifies whether the offset register changes the packet size. Use this setting, for example, to combine data packets that contain only one value per data channel to larger data packets and to output them overlapping. |
| Values | Specifies the number of values of the data packets to be output. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_stop.htm language=enus -->
## TOPIC 00254: Stop

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_stop.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_stop.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Stop

Stop

Use this packet block to stop the block diagram packet blocks or the complete measurement after a specified number of data packets.

#### Settings

| Number of blocks until STOP | Specifies after how many data packets DIAdem stops the packet blocks. To use data packets from several packet buses use the Merge packet block before the Stop packet block. |
| --- | --- |
| Stop all Timers | Specifies that DIAdem also stops the single point blocks, which stops the entire measurement. If you do not select this setting the single point processing blocks continue to run. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_thermo_lin.htm language=enus -->
## TOPIC 00255: Thermo Linearization

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_thermo_lin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_thermo_lin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Thermo Linearization

Thermo Linearization

Use this packet block to convert the voltages measured with thermocouples and with PT100 resistances into temperatures in ºC or °K.

In a temperature measurement with thermocouples there is a nonlinear relationship between the temperature and the voltage at the element. Thermolinearization compensates this nonlinear behavior.

#### Settings

| Unit | Specifies the unit of the physical value to be output. |
| --- | --- |
| Thermocouple | Specifies the type of linearization function. You can select DIN EN 60584-1 (IEC 584-1) type thermocouples and a thermolinearization for PT100 type resistance elements. |
| Constant reference temperature | Specifies whether DIAdem uses an offset. |
| Reference temperature | Specifies the temperature value to add for the offset. |

#### Examples

[Thermo Linearization](../../explonl/explonl/explonl_dac_av14.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_trigger.htm language=enus -->
## TOPIC 00256: Trigger

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_trigger.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_trigger.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Trigger

Trigger

Use this packet block to output event-related data packets. The trigger block rejects all data before the event.

#### Settings

| Trigger signal included | Specifies that DIAdem checks the data packets from signal input E that the packet block outputs, for trigger events. |
| --- | --- |
| Separated trigger signal | Specifies that DIAdem checks the data packets from the separate trigger input Ex, for trigger events. DIAdem creates the signal input Ex only if you select this setting. The data signal and the trigger signal must have the same sampling rate and packet size. |
| Selected channel | Specifies the channel number of the data channel to be checked if the data packets are multi-channel packets. |
| Pretrigger range | Specifies how many values DIAdem outputs before the trigger event. The pretrigger range must not exceed the block size. |
| Number of packets | Specifies that DIAdem outputs a specific number of data packets after the trigger event. |
| Number | Specifies the number of data packets. |
| Continuous | Specifies that DIAdem outputs all data packets after the trigger event. |
| Type | Specifies the trigger type. |
| Slope type | Specifies the type of slope to be checked. |
| Threshold | Specifies the threshold value of the slope. |
| Window | Specifies whether the trigger event occurs at Window entry or Window exit. |
| Upper | Specifies the top window limit. |
| Lower | Specifies the bottom window limit. |
| Retrigger | Specifies that DIAdem continuously checks the trigger signal for trigger events. If you do not enable this setting, DIAdem only triggers one trigger. |

#### Examples

[Trigger Measurement](../../explonl/explonl/explonl_dac_av11.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm language=enus -->
## TOPIC 00257: Ignore Block

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Ignore Block

Ignore Block

Use this packet block to reduce the amount of incoming data. The Ignore block can reject values, change packet sizes, or only output specified sections of data depending on the control signal.

#### Settings

| Transmit quantity A, ignore quantity B | Specifies that DIAdem periodically outputs a data quantity A and that DIAdem then rejects a second data quantity B. |
| --- | --- |
| Ignore quantity A, transmit quantity B | Specifies that DIAdem periodically rejects a data quantity A and that DIAdem then outputs a second data quantity B. |
| Transmit when control input HIGH | Specifies that a control signal at control input C controls the output of incoming data packets. As long as the control input C receives a control signal (TTL high), the ignore block outputs the incoming data packets. DIAdem creates the control input C only if you select this setting. The data signal and the control signal must have the same sampling rate and packet size. |
| Cut when control input HIGH | Specifies that a control signal at control input C controls the output of incoming data packets. As long as the control input C receives a control signal (TTL high), the ignore block rejects the incoming data packets. DIAdem creates the signal input C only if you select this setting. The data signal and the control signal must have the same sampling rate and packet size.Use this setting to output all data. Regardless of the packet size of the incoming data, the ignore block waits until TTL low changes to TTL high at the control input C, before the block outputs a data packet. Use this setting, for example, for measurements on revolving objects, to create data packets that contain the data of exactly one revolution regardless of the rpm (revolutions per minute). |
| Mode of parameters | Specifies what type of data to create. |
| Number A | Specifies the number of values or of data packets of the first data quantity A. |
| Number B | Specifies the number of values or of data packets of the second data quantity B. |
| Additionally skip first values | Specifies the number of values that DIAdem rejects at the start of a measurement. |
| Create a new packet for values to transmit | Specifies that DIAdem creates a new data packet from data quantity A or B. |
| Minimum packet size | Specifies the minimum number of values that DIAdem needs to create a data packet when a control signal manages the control. DIAdem does not create data packets with smaller packet sizes.The minimum packet size specifies that DIAdem acquires values regardless of the control signal, until the minimum is reached or exceeded. |
| Maximum packet size | Specifies the maximum number of values that DIAdem collects and outputs in a data block when a control signal manages the control. DIAdem does not create data packets with a large packet size.The maximum packet size specifies that DIAdem collects all data from the HIGH cycle in one data packet until the maximum size is reached or until the control signal at control input C changes. |

#### Examples

The following example uses the setting Transmit quantity A, ignore quantity B.

In the following example the ignore block reduces the packet size from 4096 values to 1000 values in order to calculate the mean value for each data packet with 1000 values, after the ignore block. To change the packet size the ignore block has the settings Number of values in channel as the mode of parameters, Number A = 1000 and number B = 0.

In the following example the FFT returns 2048 values from 0 to 25 KHz. To evaluate the frequencies from 4 to 6 KHz the values 328 to 492 must be extracted from a data packet. To reduce data the ignore block provides the settings Number of packets, number A = 165, number B = 1883 and **Additionally skip first value** 327. The first 327 rejected values are like an offset, because the sum of Number A and Number B corresponds to the packet size.

The following example is a measurement with a high sampling rate. The display should only display every tenth data packet. The ignore block has the settings Number of packets, number A = 1 and number B = 9 as the Mode of parameters.

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_xa_dmtplx.htm language=enus -->
## TOPIC 00258: Demultiplexer

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_xa_dmtplx.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_xa_dmtplx.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Demultiplexer

Demultiplexer

Use this packet block to forward data packets to the block diagram via different data outputs. You can specify a fixed data output or change the data output via the control input S, during the measurement.

If you connect a slider control to control input S, you can specify the data output manually during the measurement. Use the demultiplexer, for example, to save data packets in different files or to display various display instruments.

#### Settings

| Number of outputs | Specifies the number of data outputs. |
| --- | --- |
| With control input | Specifies that DIAdem reads the number of the data output from the data blocks of control input S. DIAdem creates the control input S only if you select this setting. |
| Active output | Specifies the number of the data output. You only can select this setting if you disable the setting With control input, else. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_xa_mtplx.htm language=enus -->
## TOPIC 00259: Multiplexer

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_xa_mtplx.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_xa_mtplx.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Multiplexer

Multiplexer

Use this packet block to switch between data packets of several data inputs. You can specify a fixed data input or change the data input via the control input S, during the measurement.

#### Settings

| Number of inputs I1...I | Specifies the number of data inputs. |
| --- | --- |
| Active input/no scan | Specifies that DIAdem reads only one data input. Use this setting to test the individual data inputs. |
| Active input E | Specifies the number of the data input. |
| Value at control input | Specifies that DIAdem reads the number of the active data input from the data blocks of control input S. DIAdem creates the control input S only if you select this setting. If you connect a slider control to control input S, you can specify the active data input manually during the measurement. |
| Continuous scan | Specifies that DIAdem relays the active data input in cycles and that DIAdem starts again at the first data input. If you enable the Asynchronous setting, DIAdem switches to the next data input even if the active data input has not received a data packet.Use the continuous scan setting together with the settings Asynchronous and Hold packages to output all data packets that arrive in irregular intervals and on different packet buses onto one packet bus. |
| One scan | Specifies that DIAdem relays the active data input after each data packet and that DIAdem remains at the last data input. If you enable the Asynchronous setting, DIAdem switches to the next data input only if the active data input receives a data packet.Use this setting to only forward the first data packets from different packet buses. |
| Asynchronous | Specifies that DIAdem forwards each data packet from the data input even if not all data inputs have data packets. DIAdem evaluates data packets at the control input S regardless of the data inputs.If you do not enable this setting the multiplexer operates synchronously. This means that DIAdem only forwards a data packet from the active data input when all data inputs have data packets. Use this setting to display data packets that the Demultiplexer distributed to different packet buses. |
| Hold packages | Specifies that DIAdem saves data packets at inactive data inputs to the clipboard and does not reject the data packets. DIAdem always evaluates data packets at the control input.Use this setting with the Asynchronous setting, for example, to read setpoints from different files at the active data input. |

|  | Note A special feature is the transport of data packets in loops. Use the settings One scan and Asynchronous for the loop. At the first input DIAdem reads an initialization packet from the function generator or from a file. Then the second data input that receives the processed data packets becomes active. DIAdem processes the data packet within the loop continuously, for example, to calculate maximum values and minimum values blockwise or to compare data with data from the last loop. |
| --- | --- |

|  | Note Only the multiplexer block can operate asynchronously. All other packet blocks only operate when they receive data packets. |
| --- | --- |

#### Examples

[Signal Analysis](../../explonl/explonl/explonl_dac_av41.htm) | [Text Input for Commenting Alarms](../../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_math/hb_klassierung.htm language=enus -->
## TOPIC 00260: Online Classification

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_math/hb_klassierung.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_math/hb_klassierung.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Analysis](../dac_packet_dlg_math/dac_dlgspacketvalues_signalanalysis_overview.htm) > Online Classification

Online Classification

Use this packet block to classify data packets during a measurement and to output the related frequencies to the block diagram. Use the oscilloscope to display the frequency in a histogram.

#### Settings

| Classification method | Specifies the classification method. |
| --- | --- |
| Determination mode | Specifies whether DIAdem determines the classes. If you select automatic, you only need to specify the number of classes. If you select manual, you determine the class limits. |
| Number | Specifies the number of classes. |
| Width | Specifies the class width. |
| Begin | Specifies the lower limit of the first class. |
| Range | Specifies the width of all classes. |
| End | Specifies the upper limit of the last class. |
| No | Specifies that DIAdem does not trigger the reset that rejects values and starts a new count. |
| High level in trigger input | Specifies that a control signal (TTL high) at control input T triggers a reset to reject the current values and start a new count. DIAdem creates the control input T only if you select this setting. |
| Repeat after N blocks of data | Specifies that DIAdem rejects the current values and starts a new count after a specific number of data packets. |
| N | Specifies the number of data packets. |
| Relative | Specifies that DIAdem calculates the relative cumulative frequencies. Regardless of the total number of all values, the sum of all classes is always 100. |
| Absolute | Specifies that DIAdem calculates the absolute cumulative frequencies. DIAdem displays the absolute frequencies cumulatively. |
| Hysteresis | Specifies the hysteresis as a percentage of the class width. |
| Reference line | Specifies the zero line for the classification method, to separate oscillations into positive and negative sections. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_manualinput/pk_manualinput_mode.htm language=enus -->
## TOPIC 00261: Input Mode of the Manual Input

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_manualinput/pk_manualinput_mode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_manualinput/pk_manualinput_mode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > [Manual Input](../dac_packet_manualinput/hb_eingabe.htm) > Input Mode of the Manual Input

Input Mode of the Manual Input

Use this dialog box to specify the input instrument. You can specify a slider control, a dial, a switch, a push button, or a bit switch as an input instrument. You can change the input mode during the measurement.

#### Settings

| Channel | Specifies the data channel of the input instrument. |
| --- | --- |
| Mode | Specifies the input instrument. |
| Radio switch | Specifies that the switches of a multi-channel input instrument switch off each other. The switch pressed last is active. Only switches with this setting can switch off each other. |
| Function keys | Specifies which function key you can use to switch the input instrument.When you press the function key, the slider control and the dial jump to the maximum value. The push button, the switch, and the bit switch jump to the other state. You also can assign one function key to several data channels. |
| 1 Bitmap for n switches | Specifies that DIAdem displays a bitmap on all switches of a bit switch. If you do not select this setting, DIAdem distributes the loaded bitmap to the switches. |
| Number of bits | Specifies the number of bits for a bit switch. |
| Number of columns | Specifies the number of columns and the arrangement of the switches in a bit switch. |
| Load bitmap from file | Opens the dialog box where you load a BMP file for the input instrument.If you load a bitmap for a slider control, the bitmap must be the size of the slider on the screen so that DIAdem can display the bitmap on the slider. You cannot insert a bitmap in a dial. If you load a bitmap for a push button, a switch, or a bit switch, DIAdem displays the left half of the bitmap in the switched off mode, on the push button. If the loaded bitmap is larger than twice the size of the display surface, DIAdem does not display the bitmap. |
| Load bitmap from clipboard | Loads the bitmap into the input instrument from the clipboard. If you load the block diagram onto a computer that has a different screen resolution, DIAdem cannot display the bitmap correctly. |
| Delete bitmap | Removes the bitmap from the input instrument of the selected data channel. |

|  | Note Select Input Mode in the context menu of the display window to open this dialog box. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_manualinput/pk_manualinput_range.htm language=enus -->
## TOPIC 00262: Range/Manual Input Range Setting

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_manualinput/pk_manualinput_range.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_manualinput/pk_manualinput_range.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > [Manual Input](../dac_packet_manualinput/hb_eingabe.htm) > Range/Manual Input Range Setting

Range/Manual Input Range Setting

Use this dialog box to specify the slider control scale and the dial scale and to show a digital display.

#### Settings

| Channel | Specifies the data channel of the input instrument. |
| --- | --- |
| Automatic | Specifies that DIAdem displays the scale according to the incoming data packets when input signals are connected. |
| Minimum | Specifies the start value of the slider control scale and the dial scale. |
| Maximum | Specifies the end value of the slider control scale and the dial scale. |
| Units | Specifies the unit of the scale. |
| Display scale | Specifies that DIAdem displays a scale in the input instrument. |
| Change integer only | Specifies that the slider and the dial jump to the integer values. |
| Digital display none/above/below | Specifies how DIAdem displays the output values digitally in the input instrument. |
| Decimal places | Specifies the number of places after the comma for the digital display. |
| Units | Opens the dialog box where you can define up to four user units. |

|  | Note The maximum value should make sense for the subsequent packet blocks. If you connect, for example, a slider control to a D/A block, a buffer overflow can occur when 10 Volt are reached. Enter 9.99 as the maximum instead. |
| --- | --- |

|  | Note Select Range in the context menu of the display window to open this dialog box. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_osci/pk_oscilloscope_3d.htm language=enus -->
## TOPIC 00263: 3D Display

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_osci/pk_oscilloscope_3d.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_osci/pk_oscilloscope_3d.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > [Oscilloscope](../dac_packet_osci/hb_oszilloskop.htm) > [Diagram](../dac_packet_osci/pk_oscilloscope_diagram.htm) > 3D Display

3D Display

Use this dialog box to specify the 3D display of data packets in the oscilloscope. When the signal input of the oscilloscope has multi-channel data packets, the oscilloscope switches from 3D display to curve display. DIAdem cannot display multi-channel data packets three dimensionally in the oscilloscope.

#### Settings

| Waterfall diagram | Specifies that DIAdem plots the curves of the individual packets consecutively and thereby displays the chronological process as a 3D surface. |
| --- | --- |
| Color/Campbell diagram | Specifies that DIAdem displays the values of the incoming data packets in color. The color is the dimension for the signal amplitude. |
| Number of shown curves | Specifies the number of curves to plot in a waterfall diagram or the number of colored values in the Color/Campbell diagram. |
| Delete hidden lines | Specifies that DIAdem does not plot hidden lines. If you select this setting, the time necessary for redrawing the curves increases significantly. |

|  | Note Select Diagram»3D Display in the display window to open this dialog box. |
| --- | --- |

#### Examples

[Creating Data Sections](../../explonl/explonl/explonl_dac_av36.htm) | [Relay](../../explonl/explonl/explonl_dac_av34.htm) | [Signal Analysis](../../explonl/explonl/explonl_dac_av41.htm) | [Signal Filtering](../../explonl/explonl/explonl_dac_av40.htm) | [Sound Board Output](../../explonl/explonl/explonl_dac_av31.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_osci/pk_oscilloscope_cursordisplay.htm language=enus -->
## TOPIC 00264: Cursor Window

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_osci/pk_oscilloscope_cursordisplay.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_osci/pk_oscilloscope_cursordisplay.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > [Oscilloscope](../dac_packet_osci/hb_oszilloskop.htm) > [Options](../dac_packet_osci/pk_oscilloscope_options.htm) > Cursor Window

Cursor Window

Use the cursor window to measure signals with two cursor lines during a measurement. The cursor window displays the point numbers, the x-values and the y-values of the cursor lines, the x-difference and the y-difference, the increase and the integral between the two cursor lines.

Double-click the curve symbol in the top left corner of the cursor window to change the data channel if the display has multiple channels. The color of the curve symbol is the same as the color of the curve of the data channel in the oscilloscope.

During the measurement you can move and resize the cursor window and change the settings in the menus of the oscilloscope display window.

|  | Note Select Options»Cursor in the display window to open this dialog box. |
| --- | --- |

#### Measured Values

| Left N | Receives the point number of the left measurement line. |
| --- | --- |
| Right N | Receives the point number of the right measurement line. |
| Delta N | Receives the distance between the measurement lines. |

#### Examples

[Creating Data Sections](../../explonl/explonl/explonl_dac_av36.htm) | [Relay](../../explonl/explonl/explonl_dac_av34.htm) | [Signal Analysis](../../explonl/explonl/explonl_dac_av41.htm) | [Signal Filtering](../../explonl/explonl/explonl_dac_av40.htm) | [Sound Board Output](../../explonl/explonl/explonl_dac_av31.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_osci/pk_oscilloscope_curves.htm language=enus -->
## TOPIC 00265: Normal Display / Curve Display

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_osci/pk_oscilloscope_curves.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_osci/pk_oscilloscope_curves.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > [Oscilloscope](../dac_packet_osci/hb_oszilloskop.htm) > [Diagram](../dac_packet_osci/pk_oscilloscope_diagram.htm) > Normal Display / Curve Display

Normal Display / Curve Display

Use this dialog box to specify the curve display in the oscilloscope. In the curve display DIAdem deletes the last display and plots a new signal of the incoming data.

#### Settings

| Curve | Specifies that DIAdem plots the incoming data channels as curves. |
| --- | --- |
| Spike | Specifies that DIAdem plots the incoming data channels as vertical spikes. Use spikes, for example, for FFT results. |
| Bars | Specifies that DIAdem plots the incoming data channels as vertical bars. Use bars, for example, for classifications and third analyses. If data packets arrive with only one value, the oscilloscope changes to bar display. |

|  | Note Select Diagram»Normal in the display window to open this dialog box. |
| --- | --- |

#### Examples

[Creating Data Sections](../../explonl/explonl/explonl_dac_av36.htm) | [Relay](../../explonl/explonl/explonl_dac_av34.htm) | [Signal Analysis](../../explonl/explonl/explonl_dac_av41.htm) | [Signal Filtering](../../explonl/explonl/explonl_dac_av40.htm) | [Sound Board Output](../../explonl/explonl/explonl_dac_av31.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_osci/pk_oscilloscope_diagram.htm language=enus -->
## TOPIC 00266: Oscilloscope Diagram

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_osci/pk_oscilloscope_diagram.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_osci/pk_oscilloscope_diagram.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > [Oscilloscope](../dac_packet_osci/hb_oszilloskop.htm) > Oscilloscope Diagram

Oscilloscope Diagram

Use this menu to select the signal display for all data channels or to copy the signal display to the clipboard and print it during a measurement. The display mode of the data channels depends on the specified [packet size](../../dlgdacsv/dac_dlg_menu/dlgpacketcycle_dialog.htm) and on the number of channels in the data packets.

| Normal display | Opens the dialog box where you specify the curve display. Specifies the signal display when you close the dialog box with OK. |
| --- | --- |
| 3D Display | Opens the dialog box where you specify the 3D display of data packets. Specifies the signal display when you close the dialog box with OK. |
| Recorder | Opens the dialog box where you specify the recorder display. Specifies the signal display when you close the dialog box with OK. |
| Copy Bitmap | Copies the display window with the current signal display as a bitmap to the clipboard. |
| Copy Diagram | Copies the current signal display as a Windows metafile to the clipboard. |
| Print Bitmap | Prints the display window with the current signal display as a bitmap. |
| Print Diagram | Prints the current signal display as a vector graphic. |

#### Examples

[Creating Data Sections](../../explonl/explonl/explonl_dac_av36.htm) | [Relay](../../explonl/explonl/explonl_dac_av34.htm) | [Signal Analysis](../../explonl/explonl/explonl_dac_av41.htm) | [Signal Filtering](../../explonl/explonl/explonl_dac_av40.htm) | [Sound Board Output](../../explonl/explonl/explonl_dac_av31.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dac_dlgssinglevalues_control_overview.htm language=enus -->
## TOPIC 00267: Control

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dac_dlgssinglevalues_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dac_dlgssinglevalues_control_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > Control

Control

The subordinate topics contained in the tree on the contents tab of the Help describe the configuration dialog boxes for control blocks.

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgcndabstime_dialog.htm language=enus -->
## TOPIC 00268: Absolute Time: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgcndabstime_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgcndabstime_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > Absolute Time: Parameters

Absolute Time: Parameters

Use absolute time to permanently generate a control signal from a certain time onwards.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| Day | Specifies the day of the date. |
| Month | Specifies the month of the date. |
| Year | Specifies the year of the date. |
| Hour | Specifies the hour of the time. The time is divided into 24 hours. |
| Minute | Specifies the minutes of the time. |
| Second | Specifies the seconds of the time. |

#### Further Settings

Parameters | [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutpinv_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgcndjk_dialog.htm language=enus -->
## TOPIC 00269: JK Flip Flop: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgcndjk_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgcndjk_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > JK Flip Flop: Parameters

JK Flip Flop: Parameters

Use the JK flip flop if you want the output of a control signal to depend on several conditions.

The JK flip flop has five control outputs: a static set input **S** and a dynamic set input**J,** a static reset input **R**, a dynamic reset input **K,** and a clock input. DIAdem processes the state of the dynamic control inputs as soon as the clock is present.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| High level | Specifies that DIAdem evaluates the dynamic set and reset condition when the clock input has the value 1. |
| Positive slope | Specifies that DIAdem evaluates the dynamic set and reset condition when the clock input receives ascending values. |
| Negative slope | Specifies that DIAdem evaluates the dynamic set and reset condition when the clock input receives descending values. |

The JK flip flop works according to the following truth table:

C: clock input, J: dynamic set input, K: dynamic reset input, S: set input, R: reset input, Q: control output,

| C | J | K | S | R | Q |
| --- | --- | --- | --- | --- | --- |
| 0 | x | x | 0 | 0 | Unchanged |
| 0 | x | x | 0 | 1 | 0 |
| 0 | x | x | 1 | 0 | 1 |
| 0 | x | x | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | Unchanged |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | Last value inverted |
| 1 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 0 |

|  | Note The block must not work recursively. Therefore, the Q outputs cannot be coupled back to the R inputs and the S inputs. |
| --- | --- |

#### Further Settings

Parameters | [Inputs»Control](../../dlgvis/dlgvis/dlgvisctrlinpsjckr_dialog.htm) | [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutpinv_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgcndmono_dialog.htm language=enus -->
## TOPIC 00270: Monoflop: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgcndmono_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgcndmono_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > Monoflop: Parameters

Monoflop: Parameters

Use the mono flop to hold the output of a control signal for a specified period of time.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| High level | Specifies that the condition is fulfilled when the control signal at the input S has the value 1. |
| Positive slope | Specifies that the condition is fulfilled when the control signal at the input S receives ascending values. |
| Negative slope | Specifies that the condition is fulfilled when the control signal at the input S receives descending values. |
| Hold time [s] | Specifies how many seconds an impulse is held at the control output. |
| Retrigger | Specifies that the Mono Flop is retriggerable. |

The mono flop works according to the [[IMAGE alt='image' src='../image/arrowright.gif']](#nowhere)[impulse diagrams](#nowhere) shown below:

S: set input, Q: control output,

| Set condition high level without retrigger: |  |
| --- | --- |
| Set condition high level with retrigger: |  |
| Set condition positive slope without retrigger: |  |
| Set condition positive slope with retrigger: |  |
| Set condition negative slope without retrigger: |  |
| Set condition negative slope with retrigger: |  |

#### Further Settings

Parameters | [Inputs»Control](../../dlgvis/dlgvis/dlgvisctrlinp_dialog.htm) | [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutpinv_dialog.htm)

#### Examples

[Hold Function](../../explonl/explonl/explonl_dac_av10.htm) | [Triggered Data Storage](../../explonl/explonl/explonl_dac_av43.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgcndmultirise_dialog.htm language=enus -->
## TOPIC 00271: Signal Alteration: Signal List

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgcndmultirise_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgcndmultirise_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > Signal Alteration: Signal List

Signal Alteration: Signal List

Use this signal alteration to check for rising slopes or falling slopes in measurement values. DIAdem compares the current measured value either with the last measured value or with the measured value for which the condition was last fulfilled. If the condition is fulfilled, DIAdem outputs a control impulse for each monitored data signal.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Copy Names | Copies the signal name into the terminal names. You also can select several signals in the list and copy the signal names. |
|  | Combined Settings | Opens the dialog box where you enter the threshold and the slope type for the selected signals. |
|  | Signal Name | Specifies the name of the signal. |
|  | Terminal Name | Specifies the terminal name. |
|  | Delta | Specifies the difference to be checked between the measurement values. |
|  | Direction | Specifies which signal change DIAdem evaluates. |
|  | Reference | Specifies which value DIAdem compares to the measured value. |

#### Further Settings

Signal List | [Inputs»Data](../../dlgvis/dlgvis/dlgvisdatainps_dialog.htm) | [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutpsinv_dialog.htm)

#### Examples

[Condition Types](../../explonl/explonl/explonl_dac_av5.htm) | [Triggered Data Storage](../../explonl/explonl/explonl_dac_av43.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgcndmultislope_dialog.htm language=enus -->
## TOPIC 00272: Slope: Signal List

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgcndmultislope_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgcndmultislope_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > Slope: Signal List

Slope: Signal List

Use the slope condition to check whether measurement values cross the limit values in the specified slope direction. If the condition is fulfilled, DIAdem outputs a control impulse for each monitored data signal.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Copy Names | Copies the signal name into the terminal names. You also can select several signals in the list and copy the signal names. |
|  | Combined Settings | Opens the dialog box where you enter the threshold and the slope type for the selected signals. |
|  | Signal Name | Specifies the name of the signal. |
|  | Terminal Name | Specifies the terminal name. |
|  | Threshold | Specifies the limit value that must be exceeded or undershot before DIAdem checks the slope direction. |
|  | Slope type | Specifies the slope direction. |

#### Further Settings

Signal List | [Inputs»Data](../../dlgvis/dlgvis/dlgvisdatainps_dialog.htm) | [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutpsinv_dialog.htm)

#### Examples

[Condition Types](../../explonl/explonl/explonl_dac_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgcndnot_dialog.htm language=enus -->
## TOPIC 00273: NOT Operator: Inputs » Control

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgcndnot_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgcndnot_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > NOT Operator: Inputs » Control

NOT Operator: Inputs » Control

Use the NOT operator to invert a control signal.

Refer to [Block Terminals in DIAdem DAC](../../gendacsv/dac_general/block_general.htm) for more information on block terminals. Refer to the page [Buses in DIAdem DAC](../../gendacsv/dac_general/wires.htm) for more information on the buses that you use to connect blocks.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Connect Signal | Connects the signal that is selected in the list to the terminal. |
|  | Disconnect Signal | Disconnects the signal that is selected in the list from the terminal. |
|  | Signal Name | Specifies the name of the connected signal. |
|  | Signal Connected | Shows that a signal is connected at the terminal. |
|  | Signal Disconnected | Shows that a signal is disconnected from the terminal. |
|  | Terminal Name | Specifies the terminal name. |

#### Further Settings

Inputs»Control| [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgmancndcheck_dialog.htm language=enus -->
## TOPIC 00274: Checkbox: Manual Instrument

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgmancndcheck_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgmancndcheck_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > Checkbox: Manual Instrument

Checkbox: Manual Instrument

Use this checkbox to select one or more options. DIAdem outputs control signals for the selected options as long as these options are enabled. For those options that are not enabled, the associated control signals output FALSE.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Label | Specifies the text next to the checkbox. |
|  | Initialization value | Specifies that the checkbox – if enabled – outputs the value 1 as soon as the measurement starts. If you do not enable this setting, the checkbox outputs the value 0, even if it is enabled when the measurement starts. |
|  | Function key | Specifies with which function key you enable the checkbox. |

#### Further Settings

Manual Instrument | [Parameters](../../dlgvis/dlgvis/dlgmanradiocolor_dialog.htm) | [Frame](../../dlgvis/dlgvis/dlgvisframe_dialog.htm) | [Labels](../../dlgvis/dlgvis/dlgvislabel_dialog.htm) | [Position](../../dlgvis/dlgvis/dlgvispos_dialog.htm) | [Inputs»Control](../../dlgvis/dlgvis/dlgvisctrlinpstartstop_dialog.htm) | [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutpsinv_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_control/dlgmancndradio_dialog.htm language=enus -->
## TOPIC 00275: Radio Button: Manual Instrument

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_control/dlgmancndradio_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_control/dlgmancndradio_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Control](../dac_dlg_control/dac_dlgssinglevalues_control_overview.htm) > Radio Button: Manual Instrument

Radio Button: Manual Instrument

Use this dialog box to select one of several options. DIAdem outputs a control signal for the selected option as long as this option is enabled. For all other options the associated control signals output FALSE.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Label | Specifies the text next to the radio button. |
|  | Initialization value | Specifies that the radio button – if enabled – outputs the value 1 as soon as the measurement starts. If you do not enable this setting, the radio button outputs the value 0, even if it is enabled when the measurement starts. |
|  | Function key | Specifies with which function key you enable the radio button. |

#### Further Settings

Manual Instrument | [Parameters](../../dlgvis/dlgvis/dlgmanradiocolor_dialog.htm) | [Frame](../../dlgvis/dlgvis/dlgvisframe_dialog.htm) | [Labels](../../dlgvis/dlgvis/dlgvislabel_dialog.htm) | [Position](../../dlgvis/dlgvis/dlgvispos_dialog.htm) | [Inputs»Control](../../dlgvis/dlgvis/dlgvisctrlinpstartstop_dialog.htm) | [Outputs»Control](../../dlgvis/dlgvis/dlgvisctrloutpsinv_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dac_dlgssinglevalues_general_overview.htm language=enus -->
## TOPIC 00276: General Dialog Boxes

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dac_dlgssinglevalues_general_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dac_dlgssinglevalues_general_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > General Dialog Boxes

General Dialog Boxes

The subordinate topics contained in the tree on the contents tab of the Help describe the general dialog boxes of DIAdem DAC.

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgblinpcable_dialog.htm language=enus -->
## TOPIC 00277: Connect Signals to Terminals

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgblinpcable_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgblinpcable_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [General Dialog Boxes](../dac_dlg_general/dac_dlgssinglevalues_general_overview.htm) > [Bus Signals](../dac_dlg_general/dlgcable_dialog.htm) > [Block Input](../dac_dlg_general/dlgblpininput_dialog.htm) > Connect Signals to Terminals

Connect Signals to Terminals

Use this dialog box for an overview of the signals that DIAdem transports in the bus at the block input, and to connect several signals to the block input simultaneously. Double-click the name of a block output to display the associated signals. Select the signals you want to connect to the associated block input.

#### Settings

| Number of signal terminals | Displays the number of selected terminals. |
| --- | --- |
| Block Output/Signal | Displays the block outputs and the associated signal names. |
| No. of Signals | Displays the number of signals. |

#### Further Settings

[Bus Signals](../dac_dlg_general/dlgcable_dialog.htm) | [Block Input](../dac_dlg_general/dlgblpininput_dialog.htm) » Connect Signals | [Block Output](../dac_dlg_general/dlgblpinoutput_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgblpininput_dialog.htm language=enus -->
## TOPIC 00278: Block Input » Connect Signals

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgblpininput_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgblpininput_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [General Dialog Boxes](../dac_dlg_general/dac_dlgssinglevalues_general_overview.htm) > [Bus Signals](../dac_dlg_general/dlgcable_dialog.htm) > Block Input » Connect Signals

Block Input » Connect Signals

Use this dialog box to specify, to disconnect, or to reconnect incoming signals. Double-click an input to open this dialog box.

#### Settings

|  | Input | Displays the input name. |
| --- | --- | --- |
|  | Connect Signal | Connects the signal that is selected in the list to the terminal. You also can select and connect several signals. |
|  | Disconnect Signal | Disconnects the signal that is selected in the list from the terminal. You also can select and disconnect several signals from the terminal. |
|  | Signal Name | Specifies the name of the signal. |
|  | Signal Connected | Shows that a signal is connected at the terminal. |
|  | Signal Disconnected | Shows that a signal is disconnected from the terminal. |
|  | Terminal Name | Specifies the terminal name. |

#### Further Settings

[Bus Signals](../dac_dlg_general/dlgcable_dialog.htm) | Block Input » [Connect Signals](../dac_dlg_general/dlgblinpcable_dialog.htm) | [Block Output](../dac_dlg_general/dlgblpinoutput_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgblpinoutput_dialog.htm language=enus -->
## TOPIC 00279: Block Output

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgblpinoutput_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgblpinoutput_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [General Dialog Boxes](../dac_dlg_general/dac_dlgssinglevalues_general_overview.htm) > [Bus Signals](../dac_dlg_general/dlgcable_dialog.htm) > Block Output

Block Output

Use this dialog box to specify the outgoing data signals. Double-click an output to open this dialog box.

#### Settings

| Signal Name | Displays the name of the connected signal. |
| --- | --- |

#### Further Settings

[Bus Signals](../dac_dlg_general/dlgcable_dialog.htm) | [Block Input](../dac_dlg_general/dlgblpininput_dialog.htm) » [Connect Signals](../dac_dlg_general/dlgblinpcable_dialog.htm) | Block Output

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgblpinsigcount_dialog.htm language=enus -->
## TOPIC 00280: Number of Terminals

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgblpinsigcount_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgblpinsigcount_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([3D interpolation](../dac_dlg_scaling/dlgscalefxy_dialog.htm) | [Bars](../../dlgvis/dlgvis/dlgvislistbar_dialog.htm) | [Binary](../../dlgvis/dlgvis/dlgvislistbinary_dialog.htm) | [Binary Code -> Gray Code](../dac_dlg_processing/dlgscriptdac_bin2gray_dialog.htm) | [Bit Bundling](../dac_dlg_processing/dlgscriptdac_bundle_dialog.htm) | [Bit Extraction](../dac_dlg_processing/dlgscriptdac_extract_dialog.htm) | [Buffer Monitor](../dac_dlg_input_simulation/dlgsimbufferdrvmonitor_dialog.htm) | [Checkbox](../dac_dlg_control/dlgmancndcheck_dialog.htm) | [Color Matrix](../../dlgvis/dlgvis/dlgvislistmatrix_dialog.htm) | [Constant](../dac_dlg_input_simulation/dlgsimconstant_dialog.htm) | [Container](../../dlgvis/dlgvis/dlgvislistcont_dialog.htm) | [Control Inputs](../../dlgvis/dlgvis/dlgvisctrlinps_dialog.htm) | [Control Signal -> Data Signal](../dac_dlg_processing/dlgsimcondition_dialog.htm) | [Curve](../../dlgvis/dlgvis/dlgvislistcurve_dialog.htm) | [Cylinder Tachometer](../../dlgvis/dlgvis/dlgvislistdrum_dialog.htm) | [Data Inputs](../../dlgvis/dlgvis/dlgvisdatainps_dialog.htm) | [Data Inputs](../../dlgvis/dlgvis/dlgvisdatainpsref_dialog.htm) | [Data Inputs](../../dlgvis/dlgvis/dlgvisdatainpsxy_dialog.htm) | [Data Inputs](../../dlgvis/dlgvis/dlgvisdatainpsmap_dialog.htm) | [Data Inputs](../../dlgvis/dlgvis/dlgvisdatainpspr_dialog.htm) | [Digits](../../dlgvis/dlgvis/dlgvislistnumber_dialog.htm) | [Formula](../dac_dlg_processing/dlgformula_dialog.htm) | [Formula](../dac_dlg_control/dlgcndformula_dialog.htm) | [Free Linearization through Channels](../dac_dlg_scaling/dlgscalefree_dialog.htm) | [Free Linearization through Table](../dac_dlg_scaling/dlgscaletfree_dialog.htm) | [Function Generator](../dac_dlg_input_simulation/dlgsimfktgen_dialog.htm) | [Gauge](../../dlgvis/dlgvis/dlgvislistgauge_dialog.htm) | [GPI Driver](../dac_dlg_input/dlghwinplistdll_dialog.htm) | [GPI Driver](../dac_dlg_output/dlghwoutplistdll_dialog.htm) | [GPI Processing](../dac_dlg_processing/dlggpiprocesslst_dialog.htm) | [Gray Code -> Binary Code](../dac_dlg_processing/dlgscriptdac_gray2bin_dialog.htm) | [Linear Scaling](../dac_dlg_scaling/dlgscalaxb_dialog.htm) | [Map Display](../../dlgvis/dlgvis/dlgvislistmap_dialog.htm) | [Mean of n signals](../dac_dlg_processing/dlgscriptdac_meanvalue_dialog.htm) | [Message](../../dlgvis/dlgvis/dlgvislistmessag_dialog.htm) | [Moving Mean](../dac_dlg_processing/dlgscriptdac_smeanval_dialog.htm) | [Noise](../dac_dlg_input_simulation/dlgsimnoise_dialog.htm) | [Offset Correction](../dac_dlg_scaling/dlgoffsetchn_dialog.htm) | [Pack](../../dlgdacpp/dac_packet_dlg_handling/dlgpacketexport_dialog.htm) | [Polar](../../dlgvis/dlgvis/dlgvislistpolar_dialog.htm) | [Properties](../dac_dlg_system/dlgsystsaveprop_dialog.htm) | [Pt 100 Linearization](../dac_dlg_scaling/dlgscalept100_dialog.htm) | [Radio Button](../dac_dlg_control/dlgmancndradio_dialog.htm) | [Random](../dac_dlg_input_simulation/dlgsimrandom_dialog.htm) | [Read Channel from DAT File](../dac_dlg_input_simulation/dlgsimdatafile_dialog.htm) | [Read Channel from DAT Measurement File](../dac_dlg_input_simulation/dlgsimmeasfile_dialog.htm) | [Read Channel from Data Portal](../dac_dlg_input_simulation/dlgsimchn_dialog.htm) | [Read from Buffer](../dac_dlg_input_simulation/dlgsimbufferdrvout_dialog.htm) | [Recorder](../../dlgvis/dlgvis/dlgvislistscroll_dialog.htm) | [Save in Variables](../dac_dlg_system/dlgvari_dialog.htm) | [Scatter](../../dlgvis/dlgvis/dlgvislistscatterdisp_dialog.htm) | [Script Driver](../dac_dlg_input/dlgscriptdac_input_dialog.htm) | [Script Driver](../dac_dlg_processing/dlgscriptdac_processing_dialog.htm) | [Script Driver](../dac_dlg_output/dlgscriptdac_output_dialog.htm) | [Signal Alteration](../dac_dlg_control/dlgcndmultirise_dialog.htm) | [Signal Copy](../dac_dlg_processing/dlgsignalcopy_dialog.htm) | [Signal Export](../dac_dlg_general/dlgexportpin_dialog.htm) | [Signal Import](../dac_dlg_general/dlgimportpin_dialog.htm) | [Signal Multiplexer](../dac_dlg_processing/dlgvario_dialog.htm) | [Slope](../dac_dlg_control/dlgcndmultislope_dialog.htm) | [Spike](../../dlgvis/dlgvis/dlgvislistspike_dialog.htm) | [Standard Driver](../dac_dlg_input/dlghwinplist_dialog.htm) | [Standard Driver](../dac_dlg_output/dlghwoutplist_dialog.htm) | [Status](../../dlgvis/dlgvis/dlgvisliststate_dialog.htm) | [Table](../../dlgvis/dlgvis/dlgvislisttable_dialog.htm) | [Thermo Linearization](../dac_dlg_scaling/dlgscalethermo_dialog.htm) | [Trigger Sequence](../dac_dlg_system/dlgtrigger_dialog.htm) | [Two-Point Scaling](../dac_dlg_scaling/dlgscal2pt_dialog.htm) | [Unpack](../../dlgdacpp/dac_packet_dlg_handling/dlgpacketimport_dialog.htm) | [Window](../dac_dlg_control/dlgcndmultiwnd_dialog.htm) | [Wiper](../../dlgvis/dlgvis/dlgvislistwiper_dialog.htm) | [Write to Buffer](../dac_dlg_output_simulation/dlgsimbufferdrvinp_dialog.htm) | [XY-Display](../../dlgvis/dlgvis/dlgvislistxy_dialog.htm)) > Number of Terminals

Number of Terminals

Use this dialog box to specify a large number of signals.

#### Settings

| Number of terminals | Specifies the number of signals. |
| --- | --- |
| Automatically increasing | Specifies that DIAdem automatically adjusts the number of signals to the number of connected signals. This setting is only available if the number of data inputs is unlmited. |

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgcable_dialog.htm language=enus -->
## TOPIC 00281: Bus Signals

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgcable_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgcable_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [General Dialog Boxes](../dac_dlg_general/dac_dlgssinglevalues_general_overview.htm) > Bus Signals

Bus Signals

Use this dialog box for an overview of the signals that are transported in the selected bus, or of the signals from the selected bus node. Double-click a bus or a bus node to open the dialog box.

#### Settings

| Block Output/Signal | Displays the name of the block output. Double-click the name of a block output to display the list with the signals. |
| --- | --- |
| No. of Signals | Displays the number of signals. |

#### Further Settings

Bus Signals | [Block Input](../dac_dlg_general/dlgblpininput_dialog.htm) » [Connect Signals](../dac_dlg_general/dlgblinpcable_dialog.htm) | [Block Output](../dac_dlg_general/dlgblpinoutput_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgdacobjrename_dialog.htm language=enus -->
## TOPIC 00282: Rename

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgdacobjrename_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgdacobjrename_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [General Dialog Boxes](../dac_dlg_general/dac_dlgssinglevalues_general_overview.htm) > Rename

Rename

Use this dialog box to change the name of a block.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgexportpin_dialog.htm language=enus -->
## TOPIC 00283: Signal Export

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgexportpin_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgexportpin_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [General Dialog Boxes](../dac_dlg_general/dac_dlgssinglevalues_general_overview.htm) > [Subblock Diagrams](../dac_dlg_menu/sub_general_overview.htm) > [Export Terminals](../dac_dlg_general/dlgplanexport_dialog.htm) > Signal Export

Signal Export

Use this dialog box to specify, to disconnect, or to reconnect the outgoing data signals. To create signal outputs double-click a terminal on the export bar of the subblock diagram.

#### Settings

|  | Export Connection | Specifies the name of the connection. |
| --- | --- | --- |
|  | Terminal text | Specifies the text of the connection label. |
|  | Automatic terminal names | Specifies that DIAdem assigns the signal names to the terminals. |
|  | Connect Signal | Connects the signal that is selected in the list to the terminal. You also can select and connect several signals. |
|  | Disconnect Signal | Disconnects the signal that is selected in the list from the terminal. You also can select and disconnect several signals from the terminal. |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Copy Names | Copies the signal name into the terminal names. You also can select several signals in the list and copy the signal names. |
|  | Signal Name | Specifies the name of the signal. |
|  | Signal Connected | Shows that a signal is connected at the terminal. |
|  | Signal Disconnected | Shows that a signal is disconnected from the terminal. |
|  | Terminal Name | Specifies the terminal name. |

#### Further Settings

[Import Ports](../dac_dlg_general/dlgplanimport_dialog.htm) » [Signal Import](../dac_dlg_general/dlgimportpin_dialog.htm) | Signal Export « [Export Connections](../dac_dlg_general/dlgplanexport_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_general/dlgimportpin_dialog.htm language=enus -->
## TOPIC 00284: Signal Import

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_general/dlgimportpin_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_general/dlgimportpin_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [General Dialog Boxes](../dac_dlg_general/dac_dlgssinglevalues_general_overview.htm) > [Subblock Diagrams](../dac_dlg_menu/sub_general_overview.htm) > [Import Terminals](../dac_dlg_general/dlgplanimport_dialog.htm) > Signal Import

Signal Import

Use this dialog box to specify, to disconnect, or to reconnect the incoming data signals. To create signal inputs double-click a terminal on the import bar of the subblock diagram.

#### Settings

|  | Import Connection | Specifies the name of the connection. |
| --- | --- | --- |
|  | Terminal text | Specifies the text of the connection label. |
|  | Automatic terminal names | Specifies that DIAdem assigns the signal names to the terminals. |
|  | Connect Signal | Connects the signal that is selected in the list to the terminal. You also can select and connect several signals. |
|  | Disconnect Signal | Disconnects the signal that is selected in the list from the terminal. You also can select and disconnect several signals from the terminal. |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Copy Names | Copies the signal name into the terminal names. You also can select several signals in the list and copy the signal names. |
|  | Signal Name | Specifies the name of the signal. |
|  | Signal Connected | Shows that a signal is connected at the terminal. |
|  | Signal Disconnected | Shows that a signal is disconnected from the terminal. |
|  | Terminal Name | Specifies the terminal name. |

#### Further Settings

[Import Ports](../dac_dlg_general/dlgplanimport_dialog.htm) » Signal Import | [Signal Export](../dac_dlg_general/dlgexportpin_dialog.htm) « [Export Connections](../dac_dlg_general/dlgplanexport_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input/dlg_input_gps_parameter.htm language=enus -->
## TOPIC 00285: Read GPS Data: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input/dlg_input_gps_parameter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input/dlg_input_gps_parameter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Driver Inputs](../dac_dlg_input/dac_dlgssinglevalues_inputsdriver_overview.htm) > [GPS Data](../dac_dlg_input/dlg_input_gps_signallist.htm) > Read GPS Data: Parameters

Read GPS Data: Parameters

Use this dialog box to configure the communication between DIAdem and the GPS receiver.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| Communication |  |
| Interface | Specifies the COM interface the GPS receiver is connected to. |
| Baud rate | Specifies the baud rate in Baud. |

#### Further Settings

[Signal List](../dac_dlg_input/dlg_input_gps_signallist.htm) | Parameters | [Inputs »System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input/dlg_input_obd2_overview.htm language=enus -->
## TOPIC 00286: NI OBD-II Driver

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input/dlg_input_obd2_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input/dlg_input_obd2_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Driver Inputs](../dac_dlg_input/dac_dlgssinglevalues_inputsdriver_overview.htm) > NI OBD-II Driver

NI OBD-II Driver

The NI OBD-II driver (On-Board-Diagnostic) is based on the NI Automotive Diagnostic Command Set for reading data from Engine Control Units (ECUs). The OBD-II driver lists all supported signals which you can reduce to the list of signals supported by the vehicle. In order to use this reduction function the diagnostics system must be connected to the vehicle.

The [NI Automotive Diagnostic Command Set (ADCS)](../dac_dlg_input/adcs_overview.htm) is an NI software for creating diagnostic applications for ECUs. ADCS supports diagnostics protocols such as KWP2000 (ISO 14230), and Diagnostics on CAN (ISO 15765, OBD-II). Visit ni.com for further information.

|  | Note In order to be able to use the ODB-II driver with DIAdem, you must first install the NI Automotive Diagnostic Command Set and a CAN interface on your computer. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input/dlghwinpseldll_dialog.htm language=enus -->
## TOPIC 00287: GPI Driver: Parameters » Properties of the Signal Type (Acquisition)

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input/dlghwinpseldll_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input/dlghwinpseldll_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Driver Inputs](../dac_dlg_input/dac_dlgssinglevalues_inputsdriver_overview.htm) > [GPI Driver](../dac_dlg_input/dlghwinplistdll_dialog.htm) > [Parameters](../dac_dlg_input/dlghwinplistdllparam_dialog.htm) > GPI Driver: Parameters » Properties of the Signal Type (Acquisition)

GPI Driver: Parameters » Properties of the Signal Type (Acquisition)

Use this dialog box to specify the properties of the GPI driver and the hardware for the acquisition.

#### Settings

| Signal type | Specifies the name of the signal type. |
| --- | --- |
| Additional driver | Specifies the GPI DAC driver. |
| Device key | Specifies the name of the DAC device.The DAC device transfers all hardware settings to the driver. |
| Signal ID | Specifies the parameter set of the DAC device. |
| Device | Opens the dialog box where you specify the driver parameters.Note The driver determines the device IDs and signal IDs. Refer to the manual and the Help of the driver for further information. |
|  | Note The driver determines the device IDs and signal IDs. Refer to the manual and the Help of the driver for further information. |

|  | Note Since Version 11.1 DIAdem replaces the block names of single point GPI drivers in an existing block diagram, for example, DLL_In1, with the name of the signal type and an appended number. Use a maximum of 13 characters for the signal type name, because the name including the appended number must not exceed 16 characters. If the name is longer than 16 characters, DIAdem automatically uses the original name. In GPI drivers developed externally you might not be able to specify the name of the signal type. |
| --- | --- |

#### Further Settings

[Signal List](../dac_dlg_input/dlghwinplistdll_dialog.htm)| [Parameters](../dac_dlg_input/dlghwinplistdllparam_dialog.htm) » Signal Type | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outtputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input_simulation/dlgsimdatafilechnselect_dialog.htm language=enus -->
## TOPIC 00288: Read Channel from DAT File: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input_simulation/dlgsimdatafilechnselect_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input_simulation/dlgsimdatafilechnselect_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Simulation Inputs](../dac_dlg_input_simulation/dac_dlgssinglevalues_simulationinputs_overview.htm) > [Read Channel from DAT File](../dac_dlg_input_simulation/dlgsimdatafile_dialog.htm) > Read Channel from DAT File: Parameters

Read Channel from DAT File: Parameters

Use this dialog box to load a DAT file, to select the channel in the file, and to transfer these channels into the signal list.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Filename | Shows the name and the path of the loaded DAT file. |
|  | Browse | Opens the dialog box where you select a DAT file. |
|  | Name | Displays the channel name. |
|  | Length | Displays the channel length. |
|  | Comment | Displays the channel comment. |
|  | Create new signal list | Specifies that DIAdem generates a new signal list with the selected file channels. |
|  | Generate | Creates a new signal list with the selected file channels. |
|  | Append to signal list | Specifies that DIAdem appends the selected channels to the existing signal list. |
|  | Append | Adds the selected channels to the end of the current signal list. |

#### Further Settings

[Signal List](../dac_dlg_input_simulation/dlgsimdatafile_dialog.htm) | Parameters | [Inputs »System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input_simulation/dlgsimdate_dialog.htm language=enus -->
## TOPIC 00289: Date: Signal List

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input_simulation/dlgsimdate_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input_simulation/dlgsimdate_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Simulation Inputs](../dac_dlg_input_simulation/dac_dlgssinglevalues_simulationinputs_overview.htm) > Date: Signal List

Date: Signal List

Use this time function to generate separately the day, the month, and the year of the current date. Specify in the signal list the names of the three signals.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| Day | Specifies the signal name for the day. |
| Month | Specifies the signal name for the month. |
| Year | Specifies the signal name for the year. |

#### Further Settings

Signal List | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input_simulation/dlgsimfktgen_dialog.htm language=enus -->
## TOPIC 00290: Function Generator: Signal List

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input_simulation/dlgsimfktgen_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input_simulation/dlgsimfktgen_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Simulation Inputs](../dac_dlg_input_simulation/dac_dlgssinglevalues_simulationinputs_overview.htm) > Function Generator: Signal List

Function Generator: Signal List

Use the Function Generator to generate sine signals, rectangle signals, and triangle signals.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Signal Name | Specifies the name of the signal. |
|  | Enabled | Specifies whether a signal is active. |

#### Further Settings

Signal List | [Parameters](../dac_dlg_input_simulation/dlgsimfktgenparam_dialog.htm) | [Inputs»Data](../../dlgvis/dlgvis/dlgvisdatainpsfktgen_dialog.htm) | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

#### Examples

[Creating Data Sections](../../explonl/explonl/explonl_dac_av36.htm) | [Generating Signals (1)](../../explonl/explonl/explonl_dac_av22.htm) | [Generating Signals (2)](../../explonl/explonl/explonl_dac_ab4.htm) | [Linear Scaling and Two-Point Scaling](../../explonl/explonl/explonl_dac_av12.htm) | [Relay](../../explonl/explonl/explonl_dac_av34.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input_simulation/dlgsimfktgenparam_dialog.htm language=enus -->
## TOPIC 00291: Function Generator: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input_simulation/dlgsimfktgenparam_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input_simulation/dlgsimfktgenparam_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Simulation Inputs](../dac_dlg_input_simulation/dac_dlgssinglevalues_simulationinputs_overview.htm) > [Function Generator](../dac_dlg_input_simulation/dlgsimfktgen_dialog.htm) > Function Generator: Parameters

Function Generator: Parameters

Use this dialog box to specify how to generate sine signals, rectangle signals, and triangle signals.

You can also use the parameters of the function generator as signal inputs. You can use these inputs to remote control the function block with other data signals.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| Signal form | Specifies the form of the signal. |
| Frequency | Specifies the frequency of the signal. The frequency is limited to a tenth of the set sampling rate. |
| Amplitude | Specifies the amplitude of the signal. |
| Offset | Specifies the bias that the function generator adds to the output signal. This enables you, for example, to shift the output signal of the functions generator into the positive range. |
| Phase | Specifies the phasing of the output signal in degrees. |
| Duty cycle | Specifies the symmetry of the output signal. The value range is between 0 and 100%. A symmetrical output signal has a pulse ratio of 50%. |
| Remote control | Specifies that you remote control the function generator through data inputs. If you enable this setting, the dialog box displays Data inputs in the overview. You can only disable this setting if no signal is connected to the remote control input. |
| Interrupt mode | Specifies that DIAdem works in the interrupt mode. Windows interrupts other processes to keep the clock rate as constant as possible. |

#### Further Settings

[Signal List](../dac_dlg_input_simulation/dlgsimfktgen_dialog.htm) | Parameters | [Inputs»Data](../../dlgvis/dlgvis/dlgvisdatainpsfktgen_dialog.htm) | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input_simulation/dlgsimmeasfile_dialog.htm language=enus -->
## TOPIC 00292: Read Channel from DAT Measurement File: Signal List

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input_simulation/dlgsimmeasfile_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input_simulation/dlgsimmeasfile_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Simulation Inputs](../dac_dlg_input_simulation/dac_dlgssinglevalues_simulationinputs_overview.htm) > Read Channel from DAT Measurement File: Signal List

Read Channel from DAT Measurement File: Signal List

Use this read function to read the measurement values of a second measurement instance in DIAdem. The block can access a [DAT file](../dac_dlg_menu/dlgfilemonsave_dialog.htm) which is created as a readable linear file or circle file by a second DIAdem instance connected to the network. Specify in the signal list which channels DIAdem reads from the DAT file.

Use the block [**Read Channel from DAT File**](../dac_dlg_input_simulation/dlgsimdatafile_dialog.htm), to read channels from a DAT file already saved.

The DAT file must be in binary format.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Signal Name | Specifies the name of the signal. |
|  | Channel number | Specifies the channel number in the measurement file. |
|  | Enabled | Specifies whether a signal is active. |

#### Further Settings

Signal List | [Parameters](../dac_dlg_input_simulation/dlgsimmeasfileparam_dialog.htm) » [Channel Selection](../dac_dlg_input_simulation/dlgsimmeasfilechnselect_dialog.htm) | [Inputs»Control](../../dlgvis/dlgvis/dlgvisctrlinp_dialog.htm) | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_input_simulation/dlgsimmeasfilechnselect_dialog.htm language=enus -->
## TOPIC 00293: Read Channel from DAT Measurement File: Parameters » Channel Selection

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_input_simulation/dlgsimmeasfilechnselect_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_input_simulation/dlgsimmeasfilechnselect_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Single Point Processing Dialog Boxes](../dac_dlgssinglevalues_overview.htm) > [Simulation Inputs](../dac_dlg_input_simulation/dac_dlgssinglevalues_simulationinputs_overview.htm) > [Read Channel from DAT Measurement File](../dac_dlg_input_simulation/dlgsimmeasfile_dialog.htm) > [Parameters](../dac_dlg_input_simulation/dlgsimmeasfileparam_dialog.htm) > Read Channel from DAT Measurement File: Parameters » Channel Selection

Read Channel from DAT Measurement File: Parameters » Channel Selection

Use this dialog box to view the channels of the measurement file, to select the channels, and to transfer the channels into the signal list.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |
| Name | Displays the channel name. |
| Length | Displays the channel length. |
| Comment | Displays the channel comment. |
| Create new signal list | Specifies that DIAdem generates a new signal list with the channels selected in the measurement file. |
| Generate | Creates a new signal list with the selected channels from the measurement file. |
| Append to signal list | Specifies that DIAdem appends the selected channels to the existing signal list. |
| Append | Adds the selected channels to the end of the current signal list. |

#### Further Settings

[Signal List](../dac_dlg_input_simulation/dlgsimmeasfile_dialog.htm) | [Parameters](../dac_dlg_input_simulation/dlgsimmeasfileparam_dialog.htm) » Channel Selection | [Inputs»Control](../../dlgvis/dlgvis/dlgvisctrlinp_dialog.htm) | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_menu/dac_dlgspacketvalues_settings_overview.htm language=enus -->
## TOPIC 00294: Packet Processing

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_menu/dac_dlgspacketvalues_settings_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_menu/dac_dlgspacketvalues_settings_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Menu Dialog Boxes](../dac_dlg_menu/dac_dlgssinglevalues_menu_overview.htm) > Packet Processing

Packet Processing

The subordinate topics contained in the tree on the contents tab of the Help describe the mnu items of packet processing.

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_menu/dac_dlgssinglevalues_menu_overview.htm language=enus -->
## TOPIC 00295: Menu Dialog Boxes

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_menu/dac_dlgssinglevalues_menu_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_menu/dac_dlgssinglevalues_menu_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > Menu Dialog Boxes

Menu Dialog Boxes

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes for single point processing you can open from the menu in the DIAdem DAC panel.

<!--NI_TOPIC bundle=diadem path=dlgdacsv/dac_dlg_menu/dlgdaceditparfont_dialog.htm language=enus -->
## TOPIC 00296: Block Diagram » Font

- bundle_id: `diadem`
- source_path: `dlgdacsv/dac_dlg_menu/dlgdaceditparfont_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacsv/dac_dlg_menu/dlgdaceditparfont_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dac_dlgs_overview.htm) > [Menu Dialog Boxes](../dac_dlg_menu/dac_dlgssinglevalues_menu_overview.htm) > [DIAdem DAC Settings](../dac_dlg_menu/dlgconfdac_dialog.htm) > [Block Diagram](../dac_dlg_menu/dlgdaceditpar_dialog.htm) > Block Diagram » Font

Block Diagram » Font

Use this dialog box to specify the fonts in the block diagram.

#### Settings

|  | Standard | Specifies that DIAdem uses the predefined fonts for block diagrams. |
| --- | --- | --- |
|  | User-defined | Specifies that you can specify the fonts for the block diagrams. |
|  | Block name | Displays the font for the block name. |
|  | Select Font | Opens the dialog box where you specify the font attributes for the block names. |
|  | Block terminal small | Displays the font of the block terminals that have more than 99 signals. |
|  | Select Font | Opens the dialog box where you specify the font attributes for block terminals. |
|  | Block terminal large | Displays the font of the block terminals that have fewer than 100 signals. |
|  | Select Font | Opens the dialog box where you specify the font attributes for block terminals. |
|  | Import name/Export name | Specifies the font for the import and export buses. |
|  | Select Font | Opens the dialog box where you specify the font attributes for the import and export buses. |
|  | Number of bus signals | Displays the font of the signal numbers on a bus. |
|  | Select Font | Opens the dialog box where you specify the font attributes for the number of signals. |

#### Further Settings

[Colors](../dac_dlg_menu/dlgdaceditparcolor_dialog.htm) | Fonts

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgd3interp_dialog.htm language=enus -->
## TOPIC 00297: Interpolate (3D)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgd3interp_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgd3interp_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Surfaces](../calc_3d_dlg/calc_3dsurface_overview.htm) > Interpolate (3D)

Interpolate (3D)

Use this dialog box to approximate 3D data with an interpolated surface. The surface goes through the specified points.

#### Settings

|  | X-channel | Specifies the data channel that contains the x-values of the signal. |
| --- | --- | --- |
|  | Y-channel | Specifies the data channel that contains the y-values of the signal. |
|  | Z-channel/Matrix | Specifies the data channel that contains the z-values of the signal or displays the data channels that span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |
|  | Input structure | Specifies whether the input data is in triplets or matrices. |
|  | Result structure | Specifies whether DIAdem displays the result data in triplets or in matrices. |
| Method |  |  |
|  | Interpolation method for triplet structure | Specifies the interpolation method for input data that have a triplet structure. For matrix structures, DIAdem always uses the bicubic spline method. |
|  | Partial load structure | Specifies whether the triplet data is distributed free or in a partial load structure. This setting specifies the interpolation mode of the z-values. If you enable this setting, DIAdem lays y-z-splines with regular interpolation points in y-direction through the points of every partial load. Then DIAdem lays x-z-splines through the interpolation points in x-direction. A partial load is made up of points with x-values that lie in the specified tolerance range. |
|  | Relative tolerance as % / Absolute tolerance | Specifies whether you define the tolerance as a percent of the entire x-area or as the absolute x-area. Points whose x-values lie outside the tolerance are invalid values of the partial load. |
|  | Relative tolerance | Specifies the maximum deviation of the x-value in the partial load as a percentage of the complete x-area. |
|  | Absolute tolerance | Specifies the maximum absolute deviation of the x-value within a partial load. |
|  | Minimum number of measurement points for partial load | Specifies the minimum number of measurement points that must belong to a partial load so that this value is valid. |
|  | Validity area for z-values | Specifies whether DIAdem checks the z-value. If the z-value lies outside the specified limits, the value is invalid. |
|  | Minimum value | Specifies the bottom limit of the z-value to check. |
|  | Maximum value | Specifies the top limit of the z-value to check. |
| Result Points |  |  |
|  | Evaluation points | Specifies whether the subsequent parameters refer to the x-values or to the y-values. |
|  | Take evaluation points from a channel/Calculate evaluation points | Specifies the origin of the points for generating the grid. |
|  | Channel | Specifies the data channel for the grid points. |
|  | Enter/Automatic | Specifies whether to calculate or to enter the start and end values for the grid. |
|  | No. of points | Specifies the number of grid points. |
|  | Start value | Specifies the minimum grid point. |
|  | End value | Specifies the maximum grid point. |
| Analysis |  |  |
|  | Analysis in all points | Specifies whether DIAdem evaluates all points. |
|  | Determination of the limiting polygon through | Specifies how DIAdem defines the polygon. |
|  | X/Y-channel | Specifies the data channels that contain the x-values and y-values of the polygon. |
|  | Check polygon for convexity | Specifies whether to check the boundary curve for convexity. |

#### Result

DIAdem generates the result as a triplet or a matrix.

|  | Refer to the Help page 3D Surface Calculation for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaD3Interp")

[ChnD3Interp](../../comoff/chnd3interp.htm)

[MatD3Interp](../../comoff/matd3interp.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgisolinescalc_dialog.htm language=enus -->
## TOPIC 00298: Calculate Contour Lines (3D)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgisolinescalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgisolinescalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Surfaces](../calc_3d_dlg/calc_3dsurface_overview.htm) > Calculate Contour Lines (3D)

Calculate Contour Lines (3D)

Use this dialog box to calculate curves of the same height on a surface.

For the input data in matrix structure, the contour calculation is based on a grid of rectangles that DIAdem generates using the specified x-channel and y-channel. If the input data is in a triplet structure, a triangulation is specified for the (x,y)-points, which is the basis for the contour line calculation. You can calculate contours for the entire grid or for a subsection.

#### Settings

|  | X-channel | Specifies the data channel that contains the x-values of the signal. |
| --- | --- | --- |
|  | Y-Channel | Specifies the data channel that contains the y-values of the signal. |
|  | Z-channel/Matrix | Specifies the data channel that contains the z-values of the signal or displays the data channels that span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |
|  | Input structure | Specifies whether the input data is in triplets or matrices. |
| Determine Contour Values |  |  |
|  | Take contour values from a channel/Calculate contour values | Specifies how the contour values are selected. |
|  | Channel | Specifies the data channel that contains the contour values. |
|  | Enter/Automatic | Specifies whether the start and end contour values are calculated or entered. |
|  | No. of contour values | Specifies the number of contour values. |
|  | Lowest value | Specifies the minimum contour value. |
|  | Highest value | Specifies the maximum contour value. |
| Boundary Curve (Matrix Structure) |  |  |
|  | Use boundary curve | Specifies whether DIAdem uses the boundary curve to calculate the contour. |
|  | X-channel | Specifies the data channel containing the x-values of the boundary curve. |
|  | Y-Channel | Specifies the data channel containing the y-values of the boundary curve. |
| Boundary Curve (Triplet Structure) |  |  |
|  | X/Y-channel | Specifies the data channels that contain the x and y-values of the boundary curve. |
|  | Convex envelope/Non-convex envelope | Specifies whether DIAdem forms the boundary curve over the convex hull or the non-convex hull. |
|  | Tolerance | Specifies the maximum edge length of the hull. Enter the length of the edge as a percentage of the diameter of the point set in relation to the square unit. |
|  | Multiplication factor | In a non-convex hull calculation, this specifies the factor by which the new edge can be longer than the old edge. |

#### Result

DIAdem generates one or more result channel pairs with the x and y-values of the contour lines.

|  | Refer to the Help page 3D Surface Calculation for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaIsolinesCalc")

[MatIsolinesCalc](../../comoff/matisolinescalc.htm)

[ChnIsolinesCalc](../../comoff/chnisolinescalc.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatappend_dialog.htm language=enus -->
## TOPIC 00299: Append Matrix

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatappend_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatappend_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Basic Functions](../calc_3d_dlg/calc_3dbase_overview.htm) > Append Matrix

Append Matrix

Use this dialog box to append a matrix to an existing matrix.

#### Settings

|  | X1-channel | Specifies the data channel containing the x-values of the existing matrix. |
| --- | --- | --- |
|  | Y1-Channel | Specifies the data channel containing the y-values of the existing matrix. |
|  | Matrix1 | Shows which data channels span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |
|  | X2-channel | Specifies the data channel containing the x-values of the matrix to be added. The data channel must be the same length as the z-channels in the matrix to be appended. |
|  | Matrix2 | Specifies which data channels span the z-matrix that is to be appended. If the channels are not the same length, DIAdem only appends the values from the shortest common channel length to the original matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |

#### Result

DIAdem generates a result matrix. The x-channel and the z-channels of the new matrix are appended to the corresponding channels in the original matrix.

|  | Refer to the Help page 3D Basic Functions for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatAppend")

[MatAppend](../../comoff/matappend.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatchnconvert_dialog.htm language=enus -->
## TOPIC 00300: Convert Matrix

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatchnconvert_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatchnconvert_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Basic Functions](../calc_3d_dlg/calc_3dbase_overview.htm) > Convert Matrix

Convert Matrix

Use this dialog box to convert 3D data from a matrix to a triplet structure and vice versa. If the data is in a matrix structure, DIAdem stores the values in the x-channel and y-channel and the z-channels are stored in three channels, x, y, and z, for the triplet structure.

If the data is in a triplet structure, the x-values and y-values are grouped into new x-channels and y-channels respectively, and the z-values are saved as a matrix. During data acquisition several quasi identical (x,y)-points might have been acquired. Therefore you must specify a tolerance when you convert data so that values which deviate due to measurement inaccuracies are saved only once in the matrix.

#### Settings

|  | X-channel | Specifies the data channel containing the x-values. |
| --- | --- | --- |
|  | Y-Channel | Specifies the data channel containing the y-values. |
|  | Z-channel/Matrix | Specifies the data channel containing the z-values, or displays the data channels that span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |
|  | Matrix to triplet/Triplet to matrix | Specifies the conversion direction. |
|  | Relative tolerance as % / Absolute tolerance | Specifies how to specify the tolerance when converting triplet to matrix. |
|  | Relative tolerance | Specifies the tolerance as a percentage within which DIAdem combines value pairs into single values. |
|  | Absolute tolerance x-direction | Specifies the absolute tolerance within which DIAdem combines x-values into a single value. |
|  | Absolute tolerance y-direction | Specifies the absolute tolerance within which DIAdem combines y-values into a single value. |

#### Result

DIAdem generates a result as a triplet or as a matrix structure.

|  | Refer to the Help page 3D Data Structure for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatChnConvert")

[MatChnConvert](../../comoff/matchnconvert.htm)

[ChnMatConvert](../../comoff/chnmatconvert.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatintegrate_dialog.htm language=enus -->
## TOPIC 00301: Integrate (3D)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatintegrate_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatintegrate_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Arithmetic](../calc_3d_dlg/calc_3darithmethic_overview.htm) > Integrate (3D)

Integrate (3D)

Use this dialog box to calculate the volume of space under a surface that is given by a matrix. DIAdem calculates the integral by adding up the volumes of all the partial rectangles in the xy-grid. Partial rectangles with an x, y, or a z-value that is NoValue are not included in the calculation.

#### Settings

|  | X-channel | Specifies the data channel containing the x-values. |
| --- | --- | --- |
|  | Y-Channel | Specifies the data channel containing the y-values. |
|  | Matrix | Shows which data channels span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |

#### Result

DIAdem generates two result channels. When the integration is calculated rowwise, the first result channel contains the partial integrals that were added up to the respective row. The second result channel contains the respective partial integral for the columnwise calculated integration.

|  | Refer to the Help page 3D Basic Mathematics for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatIntegrate")

[MatIntegrate](../../comoff/matintegrate.htm)

#### Related Topics

[3D Axis System with a Matrix Display](../../exploff/examples/expl_report_av4.htm)

#### Examples

[3D Axis System with a Matrix Display](../../exploff/examples/expl_report_av4.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatmat_dialog.htm language=enus -->
## TOPIC 00302: Matrix-Matrix Operations

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatmat_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatmat_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Arithmetic](../calc_3d_dlg/calc_3darithmethic_overview.htm) > Matrix-Matrix Operations

Matrix-Matrix Operations

Use this dialog box to calculate one matrix with another matrix.

#### Settings

|  | Matrix1 | Specifies which data channels span the first matrix. |
| --- | --- | --- |
|  | Select Channels | Opens the list for selecting the data channels that span the matrix. |
|  | Matrix2 | Specifies which data channels span the second matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the matrix. |
|  | Operation | Specifies the operations such as addition, subtraction, division, or multiplication. |
|  | Algebrac/Componentwise | Specifies whether DIAdem multiplies the matrices algebraically or componentwise. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. This rule applies for each pair of columns, consisting of matrix 1 and matrix 2. You must execute a matrix multiplication componentwise, for the result channels to be waveform channels. |
| --- | --- |

#### Result

DIAdem generates a result matrix. The dimension depends on the operation and the input channels. The calculation uses the maximum possible dimension, which is specified by the number of input channels and the highest common channel length. If there is a NoValue in a matrix element a NoValue appears in the corresponding element of the result matrix. If one of the z-elements in the second matrix is zero when matrices are divided, a NoValue is returned at the corresponding element in the result matrix.

|  | Refer to the Help page 3D Arithmetic for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatMat")

[MatAdd](../../comoff/matadd.htm)

[MatSub](../../comoff/matsub.htm)

[MatDiv](../../comoff/matdiv.htm)

[MatMul](../../comoff/matmul.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatnormalize_dialog.htm language=enus -->
## TOPIC 00303: Normalize (3D)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatnormalize_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatnormalize_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Arithmetic](../calc_3d_dlg/calc_3darithmethic_overview.htm) > Normalize (3D)

Normalize (3D)

Use this dialog box to normalize the elements of a matrix to the range [-1,1] by dividing all matrix values by the absolute highest value.

#### Settings

|  | Matrix | Shows which data channels span the matrix. |
| --- | --- | --- |
|  | Select Channels | Opens the list for selecting the data channels that span the matrix. |
|  | Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. This rule applies to each matrix column. |
| --- | --- |

#### Result

DIAdem generates a result matrix that is the same size as the input matrix.

|  | Refer to the Help page 3D Basic Mathematics for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatNormalize")

[MatNormalize](../../comoff/matnormalize.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatrelativize_dialog.htm language=enus -->
## TOPIC 00304: Relativize (3D)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatrelativize_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatrelativize_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Arithmetic](../calc_3d_dlg/calc_3darithmethic_overview.htm) > Relativize (3D)

Relativize (3D)

Use this dialog box to calculate what part of the total sum of all matrix elements each element in a matrix is, as a percentage.

#### Settings

|  | Matrix | Shows which data channels span the matrix. |
| --- | --- | --- |
|  | Select Channels | Opens the list for selecting the data channels that span the matrix. |
|  | Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | Note The matrix you want to relativize must not contain negative values. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. This rule applies to each matrix column. |
| --- | --- |

#### Result

DIAdem generates a result matrix that is the same size as the input matrix.

|  | Refer to the Help page 3D Basic Mathematics for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatRelativize")

[MatRelativize](../../comoff/matrelativize.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatscalar_dialog.htm language=enus -->
## TOPIC 00305: Matrix-Scalar Operations

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatscalar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatscalar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Arithmetic](../calc_3d_dlg/calc_3darithmethic_overview.htm) > Matrix-Scalar Operations

Matrix-Scalar Operations

Use this dialog box to add a constant to a matrix, or to multiply a constant by a matrix.

#### Settings

|  | Matrix | Shows which data channels span the matrix. |
| --- | --- | --- |
|  | Select Channels | Opens the list for selecting the data channels that span the matrix. |
|  | Scalar | Specifies the value of the scalar. |
|  | Operation | Specifies which operation DIAdem uses. |
|  | Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. This rule applies to each matrix column. |
| --- | --- |

#### Result

DIAdem generates a result matrix that is the same size as the input matrix.

|  | Refer to the Help page 3D Arithmetic for further information. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatScalar")

[MatScalAdd](../../comoff/matscaladd.htm)

[MatScalMul](../../comoff/matscalmul.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatsort_dialog.htm language=enus -->
## TOPIC 00306: Sort Matrix

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatsort_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatsort_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Basic Functions](../calc_3d_dlg/calc_3dbase_overview.htm) > Sort Matrix

Sort Matrix

Use this dialog box to sort the x-channels and the y-channels in a matrix as monotonic increasing. DIAdem moves the related z-values accordingly.

#### Settings

|  | X-channel | Specifies the data channel containing the x-values of the signal. |
| --- | --- | --- |
|  | Y-Channel | Specifies the data channel containing the y-values of the signal. |
|  | Matrix | Shows which data channels span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |
|  | Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | Note Refer to Organizing 3D Data for more information. |
| --- | --- |

#### Result

DIAdem generates an x-channel, a y-channel, and a result matrix of the same size as the input matrix.

|  | Refer to the Help page 3D Basic Functions for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatSort")

[MatSort](../../comoff/matsort.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatsub_dialog.htm language=enus -->
## TOPIC 00307: Create Submatrix

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatsub_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatsub_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Basic Functions](../calc_3d_dlg/calc_3dbase_overview.htm) > Create Submatrix

Create Submatrix

Use this dialog box to extract a submatrix from a matrix.

#### Settings

|  | X-channel | Specifies the data channel containing the x-values of the signal. |
| --- | --- | --- |
|  | Y-Channel | Specifies the data channel containing the y-values of the signal. |
|  | Matrix | Shows which data channels span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |
|  | Matrix rows to be copied | Specifies which rows to copy. |
|  | Matrix columns to be copied | Specifies which columns to copy. |
|  | Save submatrix transposed | Specifies whether DIAdem transposes rows and columns in a submatrix. |

#### Result

DIAdem generates an x-channel, a y-channel, and a result matrix.

|  | Refer to the Help page 3D Basic Functions for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaSubMat")

[SubMat](../../comoff/submat.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatsum_dialog.htm language=enus -->
## TOPIC 00308: Summation (3D)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatsum_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatsum_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Arithmetic](../calc_3d_dlg/calc_3darithmethic_overview.htm) > Summation (3D)

Summation (3D)

Use this dialog box to add up the values in a matrix in rows and columns.

#### Settings

|  | Matrix | Specifies which data channels span the matrix. |
| --- | --- | --- |
|  | Select Channels | Opens the list for selecting the data channels that span the matrix. |

#### Result

DIAdem generates two result channels that contain the subtotal of the matrix values up to the respective row or column.

|  | Refer to the Help page 3D Basic Mathematics for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatSum")

[MatSum](../../comoff/matsum.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Transpose Matrix](../calc_3d_dlg/dlgmattransp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmattransp_dialog.htm language=enus -->
## TOPIC 00309: Transpose Matrix

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmattransp_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmattransp_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Basic Functions](../calc_3d_dlg/calc_3dbase_overview.htm) > Transpose Matrix

Transpose Matrix

Use this dialog box to interchange rows and columns in a matrix.

#### Settings

|  | X-channel | Specifies the data channel containing the x-values of the signal. |
| --- | --- | --- |
|  | Y-Channel | Specifies the data channel containing the y-values of the signal. |
|  | Matrix | Shows which data channels span the z-matrix. |
|  | Select Channels | Opens the list for selecting the data channels that span the z-matrix. |
|  | Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

#### Result

DIAdem generates an x-channel, a y-channel, and a result matrix.

|  | Refer to the Help page 3D Basic Functions for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatTranspose")

[MatTranspose](../../comoff/mattranspose.htm)

#### Related Topics

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm)

#### Examples

[Append Matrix](../calc_3d_dlg/dlgmatappend_dialog.htm) | [Approximate (3D)](../calc_3d_dlg/dlgd3appr_dialog.htm) | [Calculate Contour Lines (3D)](../calc_3d_dlg/dlgisolinescalc_dialog.htm) | [Calculate Convex Hull (3D)](../calc_3d_dlg/dlgchnd3hull_dialog.htm) | [Calculate Extreme Values](../calc_3d_dlg/dlgmatextremeval_dialog.htm) | [Convert Matrix](../calc_3d_dlg/dlgmatchnconvert_dialog.htm) | [Create Submatrix](../calc_3d_dlg/dlgmatsub_dialog.htm) | [Integrate (3D)](../calc_3d_dlg/dlgmatintegrate_dialog.htm) | [Interpolate (3D)](../calc_3d_dlg/dlgd3interp_dialog.htm) | [Matrix-Matrix Operations](../calc_3d_dlg/dlgmatmat_dialog.htm) | [Matrix-Scalar Operations](../calc_3d_dlg/dlgmatscalar_dialog.htm) | [Matrix-Vector Operations](../calc_3d_dlg/dlgmatvector_dialog.htm) | [Normalize (3D)](../calc_3d_dlg/dlgmatnormalize_dialog.htm) | [Relativize (3D)](../calc_3d_dlg/dlgmatrelativize_dialog.htm) | [Sort Matrix](../calc_3d_dlg/dlgmatsort_dialog.htm) | [Summation (3D)](../calc_3d_dlg/dlgmatsum_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_3d_dlg/dlgmatvector_dialog.htm language=enus -->
## TOPIC 00310: Matrix-Vector Operations

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_3d_dlg/dlgmatvector_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_3d_dlg/dlgmatvector_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [3D Arithmetic](../calc_3d_dlg/calc_3darithmethic_overview.htm) > Matrix-Vector Operations

Matrix-Vector Operations

Use this dialog box to multiply a matrix by a vector, either algebraically or componentwise.

#### Settings

|  | Matrix | Shows which data channels span the matrix. |
| --- | --- | --- |
|  | Select Channels | Opens the list for selecting the data channels that span the matrix. |
|  | Vector | Specifies the vector the matrix is multiplied by. |
|  | Operation | Specifies which operation DIAdem uses. |

#### Result

DIAdem generates a result channel for an algebraic multiplication and a result matrix for a componentwise multiplication.

|  | Refer to the Help page 3D Arithmetic for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaMatVector")

[MatVAlgebr](../../comoff/matvalgebr.htm)

[MatVRow](../../comoff/matvrow.htm)

[MatVColumn](../../comoff/matvcolumn.htm)

#### Examples

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/calc_basis_overview.htm language=enus -->
## TOPIC 00311: Basic Mathematics

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/calc_basis_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/calc_basis_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > Basic Mathematics

Basic Mathematics

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes where you execute basic mathematical functions such as addition, subtraction, or integration.

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/calc_channelfunctions_overview.htm language=enus -->
## TOPIC 00312: Channel Functions

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/calc_channelfunctions_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/calc_channelfunctions_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > Channel Functions

Channel Functions

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes where you generate, average, and convert channels, sort channel values, or search for the peak values of a channel.

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlganaassignment_dialog.htm language=enus -->
## TOPIC 00313: Channels <-> Assignment Channels

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlganaassignment_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlganaassignment_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Channels <-> Assignment Channels

Channels <-> Assignment Channels

Use this dialog box to convert numeric channels, waveform channels, and text channels into [assignment channels](../../genshell/genshell/genshell_assignmentchannels.htm) and vice versa. First specify the type of conversion and then the channel and settings.

#### Settings

| Assignment to text channel |  |
| --- | --- |
| Assignments in text channel | Specifies that DIAdem generates a new text channel from assignments of the assignment channel. The values of the assignment channel and the value ranges of the assignments determine the order of the assignment texts in the text channel.DIAdem adds the text channel behind the assignment channel to the Data Portal and uses the channel name of the assignment channel with the extension Text. |
| Assignment channel | Specifies from which original channels to read the assignments. |
| Keep assignment channel | Specifies that the assignment channel remains when DIAdem writes the assignments into a new text channel. |
| Assignment channel to numeric channel |  |
| Assignment channel to numeric channel | Specifies that DIAdem converts the assignment channel into a numeric channel. The channel properties remain, whereas the assignments are lost.DIAdem adds the numeric channel behind the assignment channel to the Data Portal and uses the channel name of the assignment channel with the extension Numeric. |
| Assignment channel | Specifies from which original channels to read the assignments. |
| Set NoValues | Specifies that DIAdem replaces the values in the numeric channel with NoValues, which are connected to assignments in the assignment channel. |
| Store result in original channel | Specifies that DIAdem replaces the assignment channel with the numeric channel. |
| Channel pair to assignment channel |  |
| Channel pair to assignment channel | Specifies that DIAdem generates one assignment channel from two channels. The first channel must be a numeric or a waveform channel. The second channel from which DIAdem takes the assignments, can be a Text channel, an Enumeration channel (Bus Log Converter channel), or an Assignment channel. Both channels must be the same length greater zero.Note An assignment must not have the NoValue value! DIAdem does not convert if the NoValue value is assigned to an assignment. If the first channel is an assignment channel, DIAdem overwrites the existing assignment channel parameter. If the second channel is an Assignment channel, DIAdem transfers the Assignment channel parameters unchanged to the new assignment channel. DIAdem transfers the default value of the input assignment channel to the new assignment channel. The two channels need not be the same length. If the second channel is an Enumeration channel, DIAdem generates the assignment parameters from the channel properties CANEnumSubst and EnumValues. Both properties must have the same number of elements for this. If the enumeration channel only contains the property EnumValues, DIAdem generates the assignments from the values of the enumeration channel and the custom properties. Therefore the enumeration channel must not contain NoValues. If the second channel is a Text channel, DIAdem generates the assignments from the values of the numeric channel and from the texts of the text channel. You can define up to 1000 different assignments. Therefore the numeric channel must not contain NoValues. |
|  | Note An assignment must not have the NoValue value! DIAdem does not convert if the NoValue value is assigned to an assignment. |
| Numeric channel | Specifies which original channel to convert into an assignment channel. |
| Take assignment from | Specifies the channel with the assignments in order to generate an assignment channel from a numeric channel. You can select an Assignment channel, Enumeration channel (Bus Log Converter channel), or a Text channel. |
| Delete the channel to be converted | Specifies that DIAdem replaces the numeric channel with the assignment channel and deletes the channel from which DIAdem takes the texts for the assignments. |
| Default value | Specifies a text which DIAdem uses in assignment channels when no text is assigned to the value.If you do not enter a value, DIAdem transfers the default value of the assignment channel to the new assignment channel. If you do enter a default value, DIAdem transfers this default value to the new assignment channel. |
| Text channel to assignment channel |  |
| Text channel to assignment channel | Specifies that DIAdem generates one assignment channel from one text channel.DIAdem generates an assignment from every text in the text channel and assigns a value to every text. The first text gets the value 1 and the subsequent texts a value incremented by 1. Additionally DIAdem converts the values of the assignments as channel values into the assignment channel. If a text is the same as the default value, DIAdem does not generate an assignment from this text and enters the value 0 for the channel value. You can define up to 1000 different assignments. |
| Text channel | Specifies which original channel to convert into an assignment channel. |
| Delete text channel | Specifies that DIAdem deletes the text channel which contains the texts for the assignments. |
| Default value | Specifies a text which DIAdem uses in assignment channels when no text is assigned to the value. If you leave this entry empty, DIAdem assigns an empty string to the values without an assignment. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates an assignment channel either from a channel pair or from a text channel. If you generate an assignment channel from a channel pair, DIAdem converts the numeric channel or the waveform channel into an assignment channel and reads the assignments from a text channel.

You can either extract the channel values or the assignments from an assignment channel. If you select channel values including channel properties, you receive a numeric or a waveform channel. If you select assignments, you receive a text channel.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnAssignment")

[AssignmentChnToChn](../../comoff/assignmentchntochn.htm)

[AssignmentChnToNumericChn](../../comoff/assignmentchntonumericchn.htm)

[ChnToAssignmentChn](../../comoff/chntoassignmentchn.htm)

[TextChnToAssignmentChn](../../comoff/textchntoassignmentchn.htm)

#### Related Topics

[Channels <-> XY-Channels](../calc_basis_dlg/dlgchntoxychn_dialog.htm) | [Numeric Channels <-> Complex Channels](../calc_basis_dlg/dlgchntocomplexchn_dialog.htm) | [Numeric Channels <-> Time Channels](../calc_basis_dlg/dlgchnnumerictotime_dialog.htm) | [Numeric Channels <-> Waveform Channels](../calc_basis_dlg/dlgchntowfchn_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlganachntransform_dialog.htm language=enus -->
## TOPIC 00314: Transform Channels

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlganachntransform_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlganachntransform_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Transform Channels

Transform Channels

Use this dialog box to transform numeric channels into Cartesian coordinates and vice versa.

#### Settings

| X | Specifies the x-data channel with the Cartesian coordinates for the transformation Cartesian -> Polar. |
| --- | --- |
| Y | Specifies the y-data channel with the Cartesian coordinates for the transformation Cartesian -> Polar. |
| Angle | Specifies the y-data channel with the pases in radian of the polar coordinates for the transformation Polar -> Cartesian. |
| Radius | Specifies the x-data channel with the amplitudes of the polar coordinate for the transformation Polar -> Cartesian. |
| Transformation direction | Specifies whether polar coordinates are the source or the target. |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to continue using the input channels. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels.This function returns waveform channels as a result if the waveform channels have identical properties. |
| --- | --- |

#### Result

DIAdem generates two result channels. DIAdem calculates the phase in radian and the amplitude for polar coordinates, and calculates the x-values and the y-values for Cartesian coordinates.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnTransform")

[ChnPolarToCartesian](../../comoff/chnpolartocartesian.htm)

[ChnCartesianToPolar](../../comoff/chncartesiantopolar.htm)

#### Examples

[Channels <-> Assignment Channels](../calc_basis_dlg/dlganaassignment_dialog.htm) | [Channels <-> XY-Channels](../calc_basis_dlg/dlgchntoxychn_dialog.htm) | [Convert Polar Coordinates to Cartesian Coordinates](../../exploff/examples/expl_polarcartesian.htm) | [Converting Numeric Channels into XY-Channels](../../procmaths/procmaths/mathsproc_xchannelrelationscreate.htm) | [Converting Numerical Channels into Waveform Channels](../../procmaths/procmaths/mathsproc_waveforms_converting.htm) | [Numeric Channels <-> Complex Channels](../calc_basis_dlg/dlgchntocomplexchn_dialog.htm) | [Numeric Channels <-> Time Channels](../calc_basis_dlg/dlgchnnumerictotime_dialog.htm) | [Numeric Channels <-> Waveform Channels](../calc_basis_dlg/dlgchntowfchn_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnadd_dialog.htm language=enus -->
## TOPIC 00315: Add

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnadd_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnadd_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Add

Add

Use this dialog box to add several channels.

#### Settings

|  | 1st channel | Specifies the first channel. |
| --- | --- | --- |
|  | Other channels | Specifies the channels that are to be added. |
|  | Select Channels | Opens the channel selection list. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the result values of the addition.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnAdd")

[ChnAdd](../../comoff/chnadd.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnaverage_dialog.htm language=enus -->
## TOPIC 00316: Averaging Channels

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnaverage_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnaverage_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Averaging Channels

Averaging Channels

Use this dialog box to calculate the arithmetic mean of the values of two or more data channels.

#### Settings

|  | Channels to be averaged | Specifies which data channels DIAdem averages, in rows. |
| --- | --- | --- |
|  | Select Channels | Opens the channel selection list. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates one result channel. Each value in the result channel is the arithmetic mean of the values from the same row in all the input channels.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnAverage")

[ChnAverage](../../comoff/chnaverage.htm)

#### Related Topics

[Add Event](../calc_basis_dlg/dlgchneventdetection_new_dialog.htm) | [Add](../calc_basis_dlg/dlgchnadd_dialog.htm) | [Add](../calc_basis_dlg/dlgchnadd_dialog.htm) | [Calculate Differences](../calc_basis_dlg/dlgchndeltacalc_dialog.htm) | [Calculate Peaks](../calc_basis_dlg/dlgchnpeakdetect_dialog.htm) | [Calculate Reciprocal](../calc_basis_dlg/dlgchnreciproc_dialog.htm) | [Calculate RMS](../calc_basis_dlg/dlgchnrms_dialog.htm) | [Calculating Quantity-Based with Mathematical Functions](../../procmaths/procmaths/mathsproc_calculating_dimension_based.htm) | [Channel Comparison](../calc_basis_dlg/dlgchneventdetection_compare_dialog.htm) | [Channels <-> Assignment Channels](../calc_basis_dlg/dlganaassignment_dialog.htm) | [Channels <-> XY-Channels](../calc_basis_dlg/dlgchntoxychn_dialog.htm) | [Concatenate Channels](../calc_basis_dlg/dlgchnconcatenatechannels_dialog.htm) | [Detrend](../calc_basis_dlg/dlgchndetrendcalc_dialog.htm) | [Difference](../calc_basis_dlg/dlgchneventdetection_difference_dialog.htm) | [Differentiate](../calc_basis_dlg/dlgchndifferent_dialog.htm) | [Divide](../calc_basis_dlg/dlgchndiv_dialog.htm) | [Find Pattern](../calc_basis_dlg/dlgchneventpatternfind_dialog.htm) | [Find Peaks](../calc_basis_dlg/dlgchnpeakfind_dialog.htm) | [Generate Numeric Channel](../calc_basis_dlg/dlgchngen_dialog.htm) | [Generate Time Channel](../calc_basis_dlg/dlgchngentime_dialog.htm) | [Integrate](../calc_basis_dlg/dlgchnintegrate_dialog.htm) | [Limiting Channel Values](../calc_basis_dlg/dlgchnrangelimit_dialog.htm) | [Mirror Channel](../calc_basis_dlg/dlgchnmirror_dialog.htm) | [Multiply](../calc_basis_dlg/dlgchnmul_dialog.htm) | [Normalize](../calc_basis_dlg/dlgchnnormalize_dialog.htm) | [Numeric Channels <-> Complex Channels](../calc_basis_dlg/dlgchntocomplexchn_dialog.htm) | [Numeric Channels <-> Time Channels](../calc_basis_dlg/dlgchnnumerictotime_dialog.htm) | [Numeric Channels <-> Waveform Channels](../calc_basis_dlg/dlgchntowfchn_dialog.htm) | [Offset Correction](../calc_basis_dlg/dlgchnoffset_dialog.htm) | [Optimize Data Type](../calc_basis_dlg/dlgchnoptimizedatatype_dialog.htm) | [Phase Unwrap/Wrap](../calc_basis_dlg/dlgchnwrapunwrap_dialog.htm) | [Process NoValues](../calc_basis_dlg/dlgchnnovhandle_dialog.htm) | [Quantize](../calc_basis_dlg/dlgchnquantize_dialog.htm) | [Relativize](../calc_basis_dlg/dlgchnrelativize_dialog.htm) | [Remove Duplicates](../calc_basis_dlg/dlgchndelduplicates_dialog.htm) | [Resampling](../calc_basis_dlg/dlgchnresample_dialog.htm) | [Rounding](../calc_basis_dlg/dlgchnround_dialog.htm) | [Scale](../calc_basis_dlg/dlgchnlinscale_dialog.htm) | [Slope](../calc_basis_dlg/dlgchneventdetection_slope_dialog.htm) | [Sort Channel Values](../calc_basis_dlg/dlgchnmultisort_dialog.htm) | [Subtract](../calc_basis_dlg/dlgchnsub_dialog.htm) | [Summation](../calc_basis_dlg/dlgchnsum_dialog.htm) | [Synchronize Data from Different Files](../calc_basis_dlg/dlgchnresamplexoffsetcalc_dialog.htm) | [Transform Channels](../calc_basis_dlg/dlganachntransform_dialog.htm) | [Window](../calc_basis_dlg/dlgchneventdetection_window_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnconcatenatechannels_dialog.htm language=enus -->
## TOPIC 00317: Concatenate Channels

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnconcatenatechannels_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnconcatenatechannels_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Concatenate Channels

Concatenate Channels

Use this dialog box to concatenate data channels. You can combine individual data channels to form a new channel. You can concatenate channels with the same channel name or channel index groupwise to each other and add channels. DIAdem only concatenates data channels of the same data type.

#### Settings

| Concatenate mode |  |  |
| --- | --- | --- |
|  | Channelwise | Specifies that DIAdem concatenates the channels. |
|  | Groupwise by channel name | Specifies that DIAdem appends channels with the same name as the groups to be concatenated to the channels of the base group. |
|  | Groupwise by channel index | Specifies that DIAdem appends channels with the same channel index as the groups to be concatenated to the channels of the base group. |
|  | Groupwise with NoValue padding | Specifies that DIAdem adds channels from selected groups to the channels of the base group. DIAdem concatenates channels with the same name. To bring all channels to the same length, DIAdem adds NoValues to the channels that are not contained in all groups. |
| Channelwise |  |  |
|  | Base channel | Specifies the channel to which DIAdem appends further channels. |
|  | Delete Entry | Deletes the selected channel or the selected channels from the list. |
|  | Move Entry Up | Moves the selected channel or channels up.The order of the channels in the list specifies the order in which DIAdem appends these channels to the base channel. |
|  | Move Entry Down | Moves the selected channel or channels down. |
|  | Channels to be concatenated | Specifies the channels which DIAdem appends to the base channel. Drag and drop channels from the Data Portal. |
| Groupwise |  |  |
|  | Base group | Specifies the channel group to which DIAdem adds channels from other groups and appends channels with the same name. |
|  | Complete channel group | Includes all channels of the selected channel group in the base group. |
|  | Delete Entry | Deletes the selected channel or channels from the list of the base group. |
|  | List of base channels | Displays the channels of the base group. You can remove individual channels from the list or restore all channels of the base group. The channels must be equidistant and of equal length. |
|  | Groups to be concatenated | Specifies the channel groups whose channels DIAdem appends or adds to the base channels. Drag and drop channels from the Data Portal.For groupwise concatenation by channel name, the selected channel groups must contain channels that have the same names as the selected base channels. For groupwise concatenation by channel index, the selected channel groups must contain as many channels there are selected base channels. For the groupwise concatenation with adjustment, the channel groups can also contain channels that do not exist in the base group. DIAdem supplements the missing group sections in the channels with NoValues. |
|  | Delete Entry | Deletes the selected channel group or groups. |
|  | Move Entry Up | Moves the selected channel group or channel groups up.The order of the channels in the list specifies the order in which DIAdem appends the channels to the base channel with the same name or the same index. |
|  | Move Entry Down | Moves the selected channel group or channel groups down. |
| Result channels |  |  |
|  | Mark channel boundaries with NoValues | Specifies that DIAdem inserts a separator after each channel to make the original channels visible. For numeric channels DIAdem inserts NoValue and for text channels DIAdem inserts . --- .-.. |
|  | Preserve waveform channels when possible | Specifies that DIAdem saves the result channels like the input channels as waveform channels if possible.This requires the new time axis of each waveform channel to be continually equidistant. For example, if the time axes of the individual waveform channels always begin at 0 s, DIAdem generates two numeric channels: one with the concatenated time data and one with the measurement data. |
|  | Store result in original channel / Store results in original channels | Overwrites the values of the input channel or channels. Do not select this setting if you want to continue using the input channels. |

#### Result

For channelwise concatenation, DIAdem creates a result channel with the new channel. DIAdem creates a new channel group with the same number of result channels as there are channels in the base group or as there are different channels in all channel groups.

If you concatenate waveform channels and the resulting time axis is not continuously equidistant, DIAdem stores the time information and the measurement data in separate numeric channels.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnConcatenate")

[ChnConcatenateChannels](../../comoff/chnconcatenatechannels.htm)

[ChnConcatenateGroups](../../comoff/chnconcatenategroups.htm)

[ChnConcatenateGroupsWithPadding](../../comoff/chnconcatenategroupswithpadding.htm)

#### Examples

[Connect and Mirror Channels](../../exploff/examples/expl_mirrorandappendchannel.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchndelduplicates_dialog.htm language=enus -->
## TOPIC 00318: Remove Duplicates

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchndelduplicates_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchndelduplicates_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Remove Duplicates

Remove Duplicates

Use this dialog box to remove consecutive, identical values from channels. In measurements of slowly changing signals with a high sampling rate, channels containing blocks with identical values are created. The duplicates increase the storage space and the loading time of such channels. Removing duplicates provides a flexible solution for reducing channels to just the meaningful values.

The function can edit numeric values in numeric or waveform channels as well as texts in text channels. If you specify an absolute or a relative tolerance, you remove not only identical numeric values but also numeric values that lie close to each other, as duplicates. The tolerance specifies whether capitalization is considered for text channels.

You can reduce channels specified for reduction and also dependent channels, such as the associated time channel. First, the same points as in the channel to be reduced are deleted in the dependent channels. If the input channels are not the same length, DIAdem shortens all channels starting at the channel end to the length of the shortest channel, so that all result channels are the same length.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Channel to be reduced | Specifies which data channel DIAdem reduces. |
| --- | --- |
| Dependent channels | Specifies whether DIAdem deletes the same points in the dependent channels as in the channel to be reduced. |
| Channels | Specifies the dependent channels. Usually it is wise to specify the time channel as a dependent channel. |
| Tolerance | Specifies whether DIAdem considers numeric values that are very close together in a channel as duplicates. |
| Tolerance value | Specifies the distance at which two numeric values in a channel are still considered duplicates. The percentage value refers to the current channel value of the channel to be reduced. |
| Case-sensitive | Specifies that DIAdem matches the case when comparing texts. |
| Accept data from dependent channels | Specifies which value DIAdem accepts from the dependent channels. If you select First value and the channel you want to cleanse has, for example, the same values from the third to the fifth position, DIAdem deletes the fourth and fifth value of the dependent channels and only retains the third value. If you select Last value, DIAdem in this example deletes the third and fourth value of the dependent channels and only retains the fifth value. For the First valid value and Last valid value settings DIAdem only retains values that are not a NoValue value. |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to continue using the input channels. |

|  | If you want to use waveform channels in this dialog box, follow Rule 1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates one or more result channels without duplicates.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnDelDuplicates")

[ChnDeleteDuplicateValues](../../comoff/chndeleteduplicatevalues.htm) 
[ChnDeleteDuplicateTexts](../../comoff/chndeleteduplicatetexts.htm)

#### Procedures

[Smoothing Signals](../../procmaths/procmaths/mathsproc_smoothing.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchndeltacalc_dialog.htm language=enus -->
## TOPIC 00319: Calculate Differences

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchndeltacalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchndeltacalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Calculate Differences

Calculate Differences

Use this dialog box to specify the difference between two consecutive single values in a numeric channel.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Channel | Specifies from which channel DIAdem calculates the differences of the single values. |
| --- | --- |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the differences of the single values of the original channel. The result channel is one value shorter than the original channel.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnDeltaCalc")

[ChnDeltaCalc](../../comoff/chndeltacalc.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchndetrendcalc_dialog.htm language=enus -->
## TOPIC 00320: Detrend

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchndetrendcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchndetrendcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Detrend

Detrend

Use this dialog box to remove a trend in the channel data. An example is a sensor drift in longterm measurements when the zero point of the sensor drifts away from the calibrated zero point over time and the measured data is falsified with an offset.

#### Settings

| X-channel | Specifies the x-data channel |
| --- | --- |
| Y-channel | Specifies the data channel to be adjusted. If you select a waveform channel, you do not need to specify an x-channel. |
| Store result in original channel | Overwrites the values of the input channel. Do not select this setting if you want to continue using the input channels. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the adjusted values.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnDetrendCalc")

[ChnDetrendCalc](../../comoff/chndetrendcalc.htm)

#### Examples

[Detrending an Oscillation Signal](../../exploff/examples/expl_detrend.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchndifferent_dialog.htm language=enus -->
## TOPIC 00321: Differentiate

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchndifferent_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchndifferent_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Differentiate

Differentiate

Use this dialog box to differentiate signals numerically.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the x-values of the signal. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the y-values of the signal. |
| Maintain original channel length | Specifies how DIAdem calculates the derivation.By default this settings is not selected and DIAdem calculates the Forward difference quotient. The two result channels with the x- and the y-values are one value shorter than the input channels. If you select this setting, DIAdem calculates the 2nd order central difference quotient. The result channel with the y-values is the same length as the input channels and the x-values are unchanged. Note In order to calculate the central difference quotient, the x-values must be equidistant and strictly monotonic increasing. If this condition is not met, DIAdem calculates the forward difference quotient and duplicates the last y-value if the x-values are increasing, and duplicates the first y-value if the x-values are decreasing. This maintains the original channel length. |
|  | Note In order to calculate the central difference quotient, the x-values must be equidistant and strictly monotonic increasing. If this condition is not met, DIAdem calculates the forward difference quotient and duplicates the last y-value if the x-values are increasing, and duplicates the first y-value if the x-values are decreasing. This maintains the original channel length. |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

Depending on which calculation method you select, DIAdem generates one or two result channels.

|  | Note When differentiating noisy signals, variations in the results channel can occur, particularly when using the forward difference quotient. You can use the Savitzky-Golay Filter to smooth the result channel. |
| --- | --- |

|  | Refer to the Help page Basic Mathematics for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnDifferentiate")

[ChnDifferentiate](../../comoff/chndifferentiate.htm)

[ChnDeriveCalc](../../comoff/chnderivecalc.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchndiv_dialog.htm language=enus -->
## TOPIC 00322: Divide

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchndiv_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchndiv_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Divide

Divide

Use this dialog box to divide one numeric channel by a second numeric channel.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Dividend | Specifies the first channel. |
| --- | --- |
| Divisor | Specifies the channel to be divided. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the quotients of the divided channels.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnDiv")

[ChnDiv](../../comoff/chndiv.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnenclosedarea_dialog.htm language=enus -->
## TOPIC 00323: Enclosed Area

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnenclosedarea_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnenclosedarea_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Enclosed Area

Enclosed Area

Use this dialog box to calculate the enclosed area. DIAdem only executes the calculation when each curve overlaps with a second curve over the length of at least two curve points in x-direction.

DIAdem calculates the partial areas of the first overlapping to the first intersection point of two curves, from intersection to intersection, and to the last overlapping. If there are more than two curves, the envelope curves are the boundaries of the partial areas. If you use only one curve, DIAdem calculates the area between curve and x-axis.

#### Settings

|  | Add Entry | Creates a new line to define a further curve. Click in a field and specify the x-channel and the y-channel or a waveform channel from the Data Portal. |
| --- | --- | --- |
|  | Delete Entry | Deletes the selected curve. |
|  | Move Entry Up | Moves the selected curve up. The first curve determines the sign of the partial areas: Partial areas above the first curve have a positive sign and the partial areas below the first curve have a negative sign. |
|  | Move Entry Down | Moves the selected curve down. |
|  | X-channel | Specifies the x-channel of a curve. |
|  | Y-channel | Specifies the y-channel of a curve. If you select only waveform channels, you do not need to specify x-channels. |
|  | Summation | Determines whether the area calculation includes signs when adding the partial areas. If DIAdem does not use signs, DIAdem adds the amounts of the partial areas.If DIAdem uses signs, DIAdem assigns a negative sign to a partial area if the partial area is below the first curve. If you use only one curve to calculate the area between this curve and the x-axis, the partial areas below the x-axis receive negative signs.DIAdem only uses signs for one or for two curves. For more than two curves, DIAdem adds the sums of the partial areas. |
|  | Overlap | Specifies the x value range of the area calculation for more than two curves. In the case of complete overlapping, the joint x-value range refers to all curves. If the overlap is only minimal, the joint x-value range refers to at least two curves. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates three result channels. The first result channel Segments contains the x-values of the curve begin, curve end, and curve intersections. The second result channel Areas receives the partial areas between the curves and the third result channel SumOfAreas receives the summated partial areas.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnEnclosedArea")

[ChnEnclosedArea](../../comoff/chnenclosedarea.htm)

#### Examples

[Area Calculation between Curves](../../exploff/examples/expl_enclosedarea.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventdetection_compare_dialog.htm language=enus -->
## TOPIC 00324: Channel Comparison

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventdetection_compare_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventdetection_compare_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > [Event Search](../calc_basis_dlg/dlgchneventdetection_dialog.htm) > Channel Comparison

Channel Comparison

Use this dialog box to specify the comparison condition.

#### Settings

| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| --- | --- |
| Channel | Specifies the channel which DIAdem compares with the data channel to be inspected. |

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventdetection_dialog.htm language=enus -->
## TOPIC 00325: Event Search

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventdetection_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventdetection_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Event Search

Event Search

Use this dialog box to check channels for window, slope, difference, or comparison conditions. You can connect individual conditions with Boolean operations such as AND and OR, or negate them with NOT.

#### Settings

| Channels to be analyzed |  |  |
| --- | --- | --- |
|  | Add Entry | Adds a new entry to the end of the list. |
|  | Delete Entry | Deletes the last entry from the list. |
|  | Move Entry Up | Moves the selected entry up.If you move the last entry of the list, DIAdem assigns an AND operator to this entry. |
|  | Move Entry Down | Moves the selected entry down.If you move an entry to the end of the list, DIAdem deletes the assigned operator. |
|  | Channel | Specifies which data channel DIAdem checks for an event. |
|  | Event | Specifies for which event DIAdem checks the channel. The event can be the incidence of a window, a slope, a difference, or a comparison condition. |
|  | Settings | Displays the settings of the selected window, slope, difference, or comparison condition. The tooltip contains information on these settings. |
|  | Select SettingsSlope/Window/Difference/Comparison | Opens the dialog box where you make the settings for the window, slope, difference, or comparison condition. |
|  | NOT | Specifies whether DIAdem negates the result of the event. |
|  | Operator | Specifies with which operators DIAdem connects the current check and the check of the following lines. You can only specify the operators if the table contains a subsequent line.Possible operators are AND, OR, GATE and INCLUDED. |

| Result Storage |  |  |
| --- | --- | --- |
|  | Condition fulfilled |  |
|  | Use single value | Specifies the value which DIAdem stores in the result channel when the search condition is fulfilled. The default value is 1. |
|  | Accept value from channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is fulfilled. |
|  | Create new channels per section | Specifies whether DIAdem creates a channel for each section in which the search condition is met. |
|  | Time channel | Specifies the time channel to the generated channel if DIAdem creates a separate channel for each section in which the search condition is fulfilled. |
|  | Channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is fulfilled. |
|  | Condition not fulfilled |  |
|  | Use single value | Specifies the value which DIAdem stores in the result channel when the search condition is not fulfilled. The default value is 0. |
|  | Accept value from channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is not fulfilled. |
|  | Channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is not fulfilled. |

| Characteristic Values |  |  |
| --- | --- | --- |
|  | Calculate characteristic values from the following channel for the events | Specifies from which channel DIAdem calculates the events. |
|  | Minimum value | Specifies whether DIAdem calculates the minimum value. |
|  | Maximum value | Specifies whether DIAdem calculates the maximum value. |
|  | Sum of measured values | Specifies whether DIAdem calculates the sum of the measured values. |
|  | Arithmetic mean | Specifies whether DIAdem calculates the arithmetic mean. |
|  | Standard deviation | Specifies whether DIAdem calculates the standard deviation. |
|  | Number of values | Specifies whether DIAdem calculates the number of values of the event. |

|  | Note The event search assumes that the channels you use are the same length. |
| --- | --- |

#### Result

DIAdem stores the search result in the two-dimensional array variable [ChnEventResultList](../../varoff/chneventresultlist.htm). Refer to [Result of the Event Search](../../genmaths/genmaths/calc_chneventfindresult.htm) for a description of the array. If the event search returns value ranges, which meet the specified calculation instructions, DIAdem converts the contents of the [ChnEventResultList](../../varoff/chneventresultlist.htm) variable automatically into a result channel.

If you want to calculate the characteristic values of a specified channel for the determined events, DIAdem creates an individual result channel for each selected characteristic value. DIAdem saves the calculated characteristic value for each individual event, which means for each determined value range, in this result channel. In addition, DIAdem calculates the characteristic value across all determined events and saves it as a custom property of the result channel. The name of the custom property always starts with the prefix Result~Event~.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnEventDetection")

Use the [ChnEventDetectionSlope](../../comoff/chneventdetectionslope.htm) script command to check a channel for a slope condition. Use the [ChnEventDetectionWindow](../../comoff/chneventdetectionwindow.htm) command to check a channel for a window condition. Use the [ChnEventDetectionDifference](../../comoff/chneventdetectiondifference.htm) command to check whether two consecutive channel values differ by a specific amount. Use the commands [ChnEventOperationAND](../../comoff/chneventoperationand.htm), [ChnEventOperationOR](../../comoff/chneventoperationor.htm), [ChnEventGate](../../comoff/chneventgate.htm), and [ChnEventOperationEventINCLUDED](../../comoff/chneventoperationeventincluded.htm) to connect the results of two searches. Use the [ChnEventOperationNOT](../../comoff/chneventoperationnot.htm) command to negate the result of an event. Use the [ChnEventCreateStatusChn](../../comoff/chneventcreatestatuschn.htm) command to create a result channel from the search result.

|  | Note In the recording mode, press <Ctrl-Shift-C> to automatically record the individual steps of the event search in a script. If the recording mode is not enabled, DIAdem copies the work steps of the event search to the Windows clipboard with <Ctrl-Shift-C>. |
| --- | --- |

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventdetection_difference_dialog.htm language=enus -->
## TOPIC 00326: Difference

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventdetection_difference_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventdetection_difference_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > [Event Search](../calc_basis_dlg/dlgchneventdetection_dialog.htm) > Difference

Difference

Use this dialog box to specify the settings for the difference condition.

Use the difference condition to check whether two consecutive single values of a channel differ by a specific amount.

#### Settings

| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| --- | --- |
| Difference value | Specifies the sum of the difference value on which DIAdem checks a channel. |
| Difference type | Specifies the difference type of the difference value on which DIAdem checks a channel. |

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventdetection_new_dialog.htm language=enus -->
## TOPIC 00327: Add Event

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventdetection_new_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventdetection_new_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > [Event Search](../calc_basis_dlg/dlgchneventdetection_dialog.htm) > Add Event

Add Event

Use this dialog box to add a new event to the event search.

#### Settings

| Channel | Specifies which data channel DIAdem checks for an event. |
| --- | --- |
| Event | Specifies for which event DIAdem checks the channel. The event can be the incidence of a window, a slope, a difference, or a comparison condition. |
| Parameters of the Window Condition |  |
| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| Lower limit | Specifies the lower limit value for which DIAdem checks the channel.If the value is NOVALUE, DIAdem uses a value range without a lower limit. |
| Upper limit | Specifies the top limit value for which DIAdem checks the channel.If the value is NOVALUE, DIAdem uses a value range without an upper limit. |
| Hysteresis - lower limit | Specifies the value of the hysteresis for the bottom limit value of the value range.DIAdem positions a hysteresis window, which is twice as wide as the specified value, centric around the bottom limit value. The default value is 0 and means that DIAdem does not use a hysteresis. |
| Hysteresis - upper limit | Specifies the value of the hysteresis for the top limit value of the value range.DIAdem positions a hysteresis window, which is twice as wide as the specified value, centric around the top limit value. The default value is 0 and means that DIAdem does not use a hysteresis. |
| Use filter | Specifies whether DIAdem checks the search result for short phases. |
| Peak values | Specifies to which events the filter should apply. Select positive peak values if the filter should apply to fulfilled events. Otherwise the filter applies to unfulfilled events. |
| Interval width | Specifies the width of the filter. |
| Interval type | Specifies whether the filter function interprets the specified filter width as an index or as a time value. |

| Parameters of the Slope Condition |  |
| --- | --- |
| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| Threshold | Specifies the value that must be exceeded or undershot before DIAdem checks the slope direction. |
| Slope type | Specifies the slope direction. |
| Hysteresis | Specifies the hysteresis value for the slope value. If the search searches for rising slopes, the hysteresis window is below the slope value. If the search searches for falling slopes, the hysteresis is above the slope value. If the search searches for rising and falling slopes, there are therefore two hysteresis windows. |

| Parameters of the Difference Condition |  |
| --- | --- |
| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| Difference value | Specifies the sum of the difference value on which DIAdem checks a channel. |
| Difference type | Specifies the difference type of the difference value on which DIAdem checks a channel. |

| Parameters of the comparison condition |  |
| --- | --- |
| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| Comparison channel | Specifies the channel which DIAdem compares with the data channel to be inspected. |

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventdetection_slope_dialog.htm language=enus -->
## TOPIC 00328: Slope

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventdetection_slope_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventdetection_slope_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > [Event Search](../calc_basis_dlg/dlgchneventdetection_dialog.htm) > Slope

Slope

Use this dialog box to specify the slope condition.

Use the slope condition to check whether channel values exceed a limit value in a specific slope direction. You can search for rising and falling slopes and specify an optional hysteresis range.

#### Settings

| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| --- | --- |
| Threshold | Specifies the value that must be exceeded or undershot before DIAdem checks the slope direction. |
| Slope type | Specifies the slope direction. |
| Hysteresis | Specifies the hysteresis value for the slope value. If the search searches for rising slopes, the hysteresis window is below the slope value. If the search searches for falling slopes, the hysteresis is above the slope value. If the search searches for rising and falling slopes, there are two hysteresis windows. DIAdem registers the exceeding or undershooting of a limit value only as a new event if the value has also exceeded the hysteresis window when the slopes are falling or when the value exceeds the hysteresis window when the slopes are rising. |

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventdetection_window_dialog.htm language=enus -->
## TOPIC 00329: Window

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventdetection_window_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventdetection_window_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > [Event Search](../calc_basis_dlg/dlgchneventdetection_dialog.htm) > Window

Window

Use this dialog box to specify the window condition.

Use the window condition to check whether the channel values are within a specified window. You can specify an optional hysteresis range for the upper and lower window limit.

#### Settings

| Time channel | Specifies the channel containing the time references of the data channel to be inspected. |
| --- | --- |
| Lower limit | Specifies the lower limit value for which DIAdem checks the channel.If the value is NOVALUE, DIAdem uses a value range without a lower limit. |
| Upper limit | Specifies the top limit value for which DIAdem checks the channel.If the value is NOVALUE, DIAdem uses a value range without an upper limit. |
| Hysteresis - lower limit | Specifies the value of the hysteresis for the bottom limit value of the value range.DIAdem positions a hysteresis window, which is twice as wide as the specified value, centric around the bottom limit value. The default value is 0 and means that DIAdem does not use a hysteresis. DIAdem registers if the limit value is undershot only as a new event if the value of the hysteresis window is also over or undershot. |
| Hysteresis - upper limit | Specifies the value of the hysteresis for the top limit value of the value range.DIAdem positions a hysteresis window, which is twice as wide as the specified value, centric around the top limit value. The default value is 0 and means that DIAdem does not use a hysteresis. DIAdem registers if the limit value is overshot only as a new event if the value of the hysteresis window is also under or overshot. |
| Use filter | Specifies whether DIAdem checks the search result for short phases. |
| Peak values | Specifies to which events the filter should apply. Select positive peak values if the filter should apply to fulfilled events. Otherwise the filter applies to unfulfilled events. |
| Interval width | Specifies the width of the filter. |
| Interval type | Specifies whether the filter function interprets the specified filter width as an index or as a time value. |

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventfind_dialog.htm language=enus -->
## TOPIC 00330: Event Search (Free Formula)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventfind_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventfind_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Event Search (Free Formula)

Event Search (Free Formula)

Use this dialog box to check channels for specific events with a free formula. You can use operators such as < and >,  and Boolean operations such as AND and OR.

#### Settings

|  | Formula | Specifies the calculation instruction of the event. |
| --- | --- | --- |
|  | View | Displays the mathematical formula. |
| Channels to be analyzed |  |  |
|  | Extend List | Adds a new entry to the end of the list. |
|  | Delete Entry | Deletes the selected entry from the list. |
|  | Identifiers | Specifies the designators of the channel. Use the channel designator in the formula. |
|  | Channel | Specifies which channel the designator represents in the formula. |
| Result Storage |  |  |
|  | Condition fulfilled |  |
|  | Use single value | Specifies the value which DIAdem stores in the result channel when the search condition is fulfilled. The default value is 1. |
|  | Accept value from channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is fulfilled. |
|  | Create new channels per section | Specifies whether DIAdem creates a channel for each section in which the search condition is met. |
|  | Time channel | Specifies the time channel to the generated channel if DIAdem creates a separate channel for each section in which the search condition is fulfilled. |
|  | Channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is fulfilled. |
|  | Condition not fulfilled |  |
|  | Use single value | Specifies the value which DIAdem stores in the result channel when the search condition is not fulfilled. The default value is 0. |
|  | Accept value from channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is not fulfilled. |
|  | Channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is not fulfilled. |
| Characteristic Values |  |  |
|  | Calculate characteristic values from the following channel for the events | Specifies from which channel DIAdem calculates the events. |
|  | Minimum value | Specifies whether DIAdem calculates the minimum value. |
|  | Maximum value | Specifies whether DIAdem calculates the maximum value. |
|  | Sum of measured values | Specifies whether DIAdem calculates the sum of the measured values. |
|  | Arithmetic mean | Specifies whether DIAdem calculates the arithmetic mean. |
|  | Standard deviation | Specifies whether DIAdem calculates the standard deviation. |
|  | Number of values | Specifies whether DIAdem calculates the number of values of the event. |

#### Result

DIAdem stores the search result in the two-dimensional array variable [ChnEventResultList](../../varoff/chneventresultlist.htm). Refer to [Result of the Event Search](../../genmaths/genmaths/calc_chneventfindresult.htm) for a description of the array. If the event search returns value ranges, which meet the specified calculation instructions, DIAdem converts the contents of the [ChnEventResultList](../../varoff/chneventresultlist.htm) variable automatically into a result channel.

If you want to calculate the characteristic values of a specified channel for the determined events, DIAdem creates an individual result channel for each selected characteristic value. DIAdem saves the calculated characteristic value for each individual event, which means for each determined value range, in this result channel. In addition, DIAdem calculates the characteristic value across all determined events and saves it as a custom property of the result channel. The name of the custom property always starts with the prefix Result~Event~.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnEventFind")

[ChnEventFind](../../comoff/chneventfind.htm)

Use the [ChnEventCreateStatusChn](../../comoff/chneventcreatestatuschn.htm) command to create a result channel from the search result.

|  | Note In the recording mode, press <Ctrl-Shift-C> to automatically record the individual steps of the event search in a script. If the recording mode is not enabled, DIAdem copies the work steps of the event search to the Windows clipboard with <Ctrl-Shift-C>. |
| --- | --- |

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchneventpatternfind_dialog.htm language=enus -->
## TOPIC 00331: Find Pattern

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchneventpatternfind_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchneventpatternfind_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Find Pattern

Find Pattern

Use this dialog box to find a specific pattern in a signal.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Channels to be analyzed |  |
| --- | --- |
| X-channel | Specifies an x-channel. If the signal channel is a waveform channel, you do not need to specify an x-channel. |
| Signal channel | Specifies the signal channel you want to analyze. |
| Pattern channel | Specifies the channel containing the pattern you want to find. |
| Offset in x-direction | Specifies the maximum number of values by which the signal channel may offset against the pattern channel. |
| Maximum allowed deviation | Specifies the maximum valid deviation of the signal channel to the pattern channel. In an analog signal and pattern channel DIAdem only uses the difference between the y-values of the signal channel and the pattern channel to calculate the deviation. If, however, the signal and pattern channels are digital, DIAdem also includes the value index when calculating the deviation. DIAdem uses a special algorithm for digital channel recognition. If one of the channels contains the custom property NI_display_mode with the value "Analog", DIAdem treats this channel as an analog channel. |
| Remove y-offset | Specifies whether DIAdem removes a y-offset. |
| Generate deviation channel | Specifies whether DIAdem generates a result channel containing the minimal deviations of the signal from the pattern for each point of the signal. |

| Result Storage |  |
| --- | --- |
| Find spot |  |
| Accept single value | Specifies the value which DIAdem stores in the result channel when the search condition is fulfilled. The default value is 1. |
| Accept value from channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is fulfilled. |
| Create new channels per section | Specifies whether DIAdem creates a channel for each section in which the search condition is met. |
| Time channel | Specifies the time channel to the generated channel if DIAdem creates a separate channel for each section in which the search condition is fulfilled. |
| Channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is fulfilled. |
| No occurrence |  |
| Accept single value | Specifies the value which DIAdem stores in the result channel when the search condition is not fulfilled. The default value is 0. |
| Accept value from channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is not fulfilled. |
| Channel | Specifies the channel whose values DIAdem copies into the result channel when the search condition is not fulfilled. |

| Characteristic Values |  |
| --- | --- |
| Calculate characteristic values from the following channel for the occurrences. | Specifies from which channel DIAdem calculates the events. |
| Characteristic values to be calculated |  |
| Minimum value | Specifies whether DIAdem calculates the minimum value. |
| Maximum value | Specifies whether DIAdem calculates the maximum value. |
| Sum of measured values | Specifies whether DIAdem calculates the sum of the measured values. |
| Arithmetic mean | Specifies whether DIAdem calculates the arithmetic mean. |
| Standard deviation | Specifies whether DIAdem calculates the standard deviation. |
| Number of values | Specifies whether DIAdem calculates the number of values of the event. |

#### Result

DIAdem stores the search result in the two-dimensional array variable [ChnEventResultList](../../varoff/chneventresultlist.htm). Refer to [Result of the Event Search](../../genmaths/genmaths/calc_chneventfindresult.htm) for a description of the array. The generated data matrix contains the index 0 to index 7 in the second dimension. The index 0 and index 1 contain the start and end indexes of the wanted event. If you specify a waveform channel as the y-channel or if you specify an x-channel explicitly for the search in the input parameter SourceChn, index 2 and index 3 contain the start and end x-values otherwise the values are Null. Index 4 and index 5 contain the start and end y-values of the inspected signals. Index 6 contains the deviation of the signal channel to the pattern channel.

If the event search returns value ranges, which meet the specified calculation instructions, DIAdem converts the contents of the [ChnEventResultList](../../varoff/chneventresultlist.htm) variable automatically into a result channel.

If you want to calculate the characteristic values of a specified channel for the determined events, DIAdem creates an individual result channel for each selected characteristic value. DIAdem saves the calculated characteristic value for each individual event, which means for each determined value range, in this result channel. In addition, DIAdem calculates the characteristic value across all determined events and saves it as a custom property of the result channel. The name of the custom property always starts with the prefix Result~Event~.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnEventPatternFind")

[ChnEventPatternFind](../../comoff/chneventpatternfind.htm)

#### Examples

[Calculating and Checking a Corridor](../../exploff/examples/expl_corridor.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Find Pattern in Signals](../../exploff/examples/expl_pattern.htm) | [Searching for Events in Channels](../../exploff/examples/expl_eventsearchexample.htm) | [Searching for Outliers with the ChnEvent Function](../../exploff/examples/exp_analysis_av2.htm) | [Set Limit Values](../../exploff/examples/expl_setupperandlowerlimits_demo.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchngen_dialog.htm language=enus -->
## TOPIC 00332: Generate Numeric Channel

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchngen_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchngen_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Generate Numeric Channel

Generate Numeric Channel

Use this dialog box to generate new data channels.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Channel generation mode | Specifies the type of channel generation, such as equidistant or geometric. |
| --- | --- |
| Set the following parameters, depending on the channel generation mode: |  |
| Start value | Specifies the first value in the new data channel. |
| End value | Specifies the last value in the new data channel. |
| Number of values | Specifies the number of values in the new data channel. |
| Channel | Specifies, when selecting Finer than channel, the data channel that DIAdem partitions more finely. Specifies, when selecting Values from the x-share of a waveform channel, the waveform channel whose x-share delivers the values. |
| n | Specifies the number of subdivisions between two subsequent values. |
| Generate implicit channel | Specifies that DIAdem only stores the parameters of the generation specification when saving the channel. The generated channel is read-only. |
| Unit | Specifies the unit in which DIAdem generates the numeric channel. |
| ... | Opens the Unit Symbol Input Help dialog box where you can select a new unit and a new unit symbol. |
| Create numeric channel (relative time reference)/Create time channel (absolute time reference) | Specifies whether DIAdem includes the waveform start time setting. If you consider the start time (absolute time reference), DIAdem generates a time channel, otherwise DIAdem generates a numeric channel (relative time reference). |

|  | Note Use the commands ChnLinGen, ChnGeoGen, ChnDXDivGen, and ChnFromWfXGen, to generate channels in a script. Use the ChnLinGenImp command to generate implicit channels. |
| --- | --- |

#### Result

DIAdem generates one result channel.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnGen")

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchngensignal_dialog.htm language=enus -->
## TOPIC 00333: Generate Signal

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchngensignal_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchngensignal_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Generate Signal

Generate Signal

Use this dialog box to generate a signal and store the data in a new channel.

#### Settings

|  | Signal form | Specifies the signal form of the channel to be generated, like sine or rectangle. |
| --- | --- | --- |
| Depending on the signal form, you can make the following settings: |  |  |
|  | Frequency | Specifies the frequency of the generated channel in Hertz. |
|  | Amplitude | Specifies the amplitude of the generated channel. |
|  | Offset | Specifies the amplitude offset of the generated channel. |
|  | Unit | Specifies the unit of the amplitude values of the generated channel. |
|  | Phase shift | Specifies the phase shift of the generated channels as a percentage of a period. |
|  | Open Input Help for Unit Symbols | Opens the dialog box where you select a new unit symbol. DIAdem searches for the first valid y-channel with a channel and suggests this value to the subdialog box.Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |
|  | Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |  |
|  | Duty cycle | Specifies the symmetry of the generated channel. The value range of the clock ratio is between 0 and 100%. A symmetric signal form has a clock ratio of 50%. |
|  | Number of values | Specifies the number of values in the generated channel. |
|  | Sampling rate | Specifies the sampling rate of the generated channel in Hertz, and thus the number of values to be generated for each period. Use a sampling rate that is at least twice the frequency. |
|  | Time unit | Specifies the unit of the time values of the generated signal. |

#### Result

DIAdem generates a [waveform channel](../../genshell/genshell/genshell_waveforms.htm) as the result.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnGenSignal")

[ChnGenSignal](../../comoff/chngensignal.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchngentime_dialog.htm language=enus -->
## TOPIC 00334: Generate Time Channel

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchngentime_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchngentime_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Generate Time Channel

Generate Time Channel

Use this dialog box to generate a new data channel with equidistant time values.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Start time | Specifies the first value in the new data channel. |
| --- | --- |
| Time unit | Specifies the time unit for the time interval. |
| Time step | Specifies the generation step width. |
| Time domain | Specifies whether the time channel is limited by the last time value or the number of values. |
| End time | Specifies the last time value in the new data channel. |

#### Result

DIAdem generates a time channel.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnGenTime")

[ChnGenTime](../../comoff/chngentime.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnintegrate_dialog.htm language=enus -->
## TOPIC 00335: Integrate

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnintegrate_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnintegrate_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Integrate

Integrate

Use this dialog box to integrate a signal.

#### Settings

| X-channel | Specifies the data channel with the x-values of the signal. |
| --- | --- |
| Y-channel | Specifies the data channel with the y-values of the signal. |
| Integration method | Specifies whether the integration method uses the trapezoidal or the Simpson rule. |
| Specify integration constant | Specifies whether DIAdem uses an integration constant for the trapezoidal rule. Do not enable this option if you want to continue calculating with the method valid up to version 2012. The integration method uses the integration constant as the zeroth value before the first value of the input channel. If you do not specify the integration constant, this value is 0. For the trapezoidal rule the mean value of the integration constant and the first channel value is the first result value.The integration constant is always used with the Simpson rule. If the integration constant is enabled, the x-values must be equidistant and strictly monotonic increasing and the y-values must not contain NoValues. |
| Integration constant | Specifies the value of the integration constant. |
| Integration end value | Specifies the integration end value according to the Simpson rule. |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to continue using the input channels. |

|  | If you want to use waveform channels in this dialog box, follow Rules 2.2 and 2.3 for Calculating with Waveform Channels. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

|  | Note If you are working without an integration constant and with the trapezoidal rule, the x-values do not have to be equidistant and strictly monotonously increasing. If a negative difference exists between two successive x-values, DIAdem subtracts the partial integral. For example, you can also calculate the area of a hysteresis curve. |
| --- | --- |

#### Result

DIAdem generates one result channel. Each value in the result channel contains the integral up to this x-value.

|  | Refer to the Help page Basic Mathematics for further information. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnIntegrate")

[ChnIntegrate](../../comoff/chnintegrate.htm)

#### Procedures

[Calculating the Surface of a Curve](../../procmaths/procmaths/mathsproc_integral.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnlinscale_dialog.htm language=enus -->
## TOPIC 00336: Scale

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnlinscale_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnlinscale_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) | [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm)) > Scale

Scale

Use this dialog box to scale channels.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Channel | Specifies the channel to be scaled. |
| --- | --- |
| Factor | Specifies the factor DIAdem uses to multiply the channel that is to be scaled. |
| Offset | Specifies the offset that DIAdem adds to the channel that is to be scaled. |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the scaled single values of the original channel.

|  | Note Specify the Factor -1 and the Offset 0 to invert the signs of the channel values, for example, to invert the polarity of a signal. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnLinScale")

[ChnLinScale](../../comoff/chnlinscale.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnmaplin_dialog.htm language=enus -->
## TOPIC 00337: Linear Mapping

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnmaplin_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnmaplin_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Linear Mapping

Linear Mapping

Use this dialog box to calculate the mapping of signals to a new x-range. Use linear mapping to convert signals with different x-values to a common x-range.

#### Settings

| X-channel | Specifies the data channel for the x-values of the signals. The data channel must not contain NoValues and the values of the data channel must be monotonic increasing. If all y-channels are waveform channels, you do not need to specify this channel. |
| --- | --- |
| Y-channel | Specifies the data channels for the y-values of the signals. |
| Interpolation channel | Specifies the data channel of the x-range to which DIAdem calculates the values. The data channel must not contain NoValues and the values of the data channel must be monotonic increasing. |
| Mapping mode | Specifies the type of function that is to be mapped. |
| Substitute value | Specifies the value that DIAdem uses in the linear mapping process of spike curves for those values to which DIAdem does not assign an interpolation point. |
| Extrapolation calculation method | Specifies which calculation method DIAdem uses to extend linear mapping for x-values beyond the original x-range, during extrapolation. |
| Constant value | Specifies the constant for extrapolation with a constant value. |
| Interpolate NoValues | Specifies whether DIAdem replaces NoValues in the y-values with interpolated values. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates one or more result channels with the mapped y-values.

|  | Refer to the Help page Linear Mapping for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnMapLinCalc")

[ChnMapLinCalc](../../comoff/chnmaplincalc.htm)

[ChnMapLinCalcExt](../../comoff/chnmaplincalcext.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnmirror_dialog.htm language=enus -->
## TOPIC 00338: Mirror Channel

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnmirror_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnmirror_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Mirror Channel

Mirror Channel

Use this dialog box to mirror the data in a channel so that the last channel value comes first.

#### Settings

| Channel | Specifies which data channel to mirror. |
| --- | --- |
| Store result in original channel | Overwrites the values of the input channel. Do not select this setting if you want to continue using the input channels. |

|  | If you want to use waveform channels in this dialog box, follow Rule 1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates one result channel.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnMirror")

[ChnMirror](../../comoff/chnmirror.htm)

#### Examples

[Connect and Mirror Channels](../../exploff/examples/expl_mirrorandappendchannel.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnmul_dialog.htm language=enus -->
## TOPIC 00339: Multiply

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnmul_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnmul_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Multiply

Multiply

Use this dialog box to multiply several channels.

#### Settings

|  | 1st channel | Specifies the first channel. |
| --- | --- | --- |
|  | Other channels | Specifies the channel or channels to be multiplied. |
|  | Select Channels | Opens the channel selection list. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the products of the multiplied channels.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnMul")

[ChnMul](../../comoff/chnmul.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnmultisort_dialog.htm language=enus -->
## TOPIC 00340: Sort Channel Values

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnmultisort_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnmultisort_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Sort Channel Values

Sort Channel Values

Use this dialog box to sort values or text in a data channel in ascending or descending order and to move the values or text in additional channels with the same index accordingly. The function differentiates between channels in the table to which you assign sorting criteria and further channels you include in the sort.

DIAdem sorts the first channel to be sorted in ascending or descending order. DIAdem also moves the values or text of the other channels to the same positions as their counterparts in the first channel. If several values in the first channel to be sorted are the same, DIAdem includes the sort criteria of the second channel. If several values in the second channel to be sorted are also the same, the third channel is used, and so on. If there are two entries with the same channel in the list of channels to be sorted, DIAdem only includes one.

#### Settings

| Channels to be sorted |  |  |
| --- | --- | --- |
|  | Add Entry | Creates a new row to define a channel to be sorted. Click into this field and select a channel from the Data Portal. |
|  | Delete Entry | Deletes the selected channel. |
|  | Move Entry Up | Moves the selected channel up.The sequence of the channels determines the sorting order. DIAdem sorts the first channel to be sorted and organizes the following channels accordingly. |
|  | Move Entry Down | Moves the selected channel down. |
|  | Channel | Displays the name of the channel to be sorted in the selected row. |
|  | Ignore Upper/Lower Case | Specifies that sorting is not case-sensitive. |
|  | Uppercase First | Specifies that DIAdem sorts text by ordering the uppercase before the lowercase letters. |
|  | Lowercase First | Specifies that DIAdem sorts text by ordering the lowercase before the uppercase letters. |
|  | Ascending | Specifies that DIAdem sorts values or text in ascending order. DIAdem sorts text according to the ASCII table. |
|  | Descending | Specifies that DIAdem sorts values or text in descending order. DIAdem sorts text according to the ASCII table. |
|  | Include the following channels in sort | Specifies that DIAdem moves the values or text of further channels according to the order of the values in the channels to be sorted. If you do not select this setting, the function moves only the channel or channels to be sorted in the order of the specified sorting criteria. |
|  | Channel list | Displays the selected channels included in the sort. |
|  | Select Channels | Opens the channel selection list to specify further channels whose values DIAdem also orders. You can select several nonconsecutive channels. |
|  | Store result in original channel | Overwrites the values of the input channels. If you sort channels with flags and use this setting, DIAdem deletes the flags in the result channels.Do not select this setting if you want to continue using the input channels. |

#### Result

DIAdem generates the same number of result channels as the number of channels and included channels to be sorted. The shortest channel to be sorted determines the length of all result channels. DIAdem does not include channels with a length of 0 when determining the length, but instead fills these channels after the calculation with NoValues up to the length of the result channels. If you select case sensitivity, DIAdem first sorts the letters according to case and then sorts the values in ascending or descending order according to the ASCII table. In descending order, the upper case letters are always sorted at the end of the list.

|  | If you want to use waveform channels in this dialog box, this function converts the channels into numeric channels (Rule 1 for Calculating with Waveform Channels. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnMultipleSort")

[ChnMultipleSortExt](../../comoff/chnmultiplesortext.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnnormalize_dialog.htm language=enus -->
## TOPIC 00341: Normalize

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnnormalize_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnnormalize_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Basic Mathematics](../calc_basis_dlg/calc_basis_overview.htm) > Normalize

Normalize

Use this dialog box to normalize a data channel to the value one. DIAdem divides each value by the highest absolute value in the data channel.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Channel | Specifies which data channel DIAdem normalizes. |
| --- | --- |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Result

DIAdem generates a result channel with values between -1 and 1.

#### Example

The input channel contains the following values:

```text
1, 4, -2, -3, -10
```

The absolute highest value is 10. After normalizing, the result channel contains the following values:

```text
0.1, 0.4, -0.2, -0.3, -1
```

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnNormalize")

[ChnNormalize](../../comoff/chnnormalize.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_basis_dlg/dlgchnnovhandle_dialog.htm language=enus -->
## TOPIC 00342: Process NoValues

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_basis_dlg/dlgchnnovhandle_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_basis_dlg/dlgchnnovhandle_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Channel Functions](../calc_basis_dlg/calc_channelfunctions_overview.htm) > Process NoValues

Process NoValues

Use this dialog box to delete [NoValues](../../genmaths/genmaths/calc_novalue_description.htm) from data channels, or to replace NoValues with a selected value or with interpolated values.

#### Settings

|  | Only process one channel | Specifies whether DIAdem processes one data channel or several. |
| --- | --- | --- |
|  | X-channel | Specifies which data channel DIAdem processes first. |
|  | Y-channels | Specifies the other data channels of which DIAdem processes the data. |
|  | Select Channels | Opens the channel selection list. |
|  | NoValue handling mode | Specifies whether DIAdem interpolates, deletes, or replaces NoValues.Note To interpolate NoValues, the values in the x-channel must be monotonic increasing. |
|  | Note To interpolate NoValues, the values in the x-channel must be monotonic increasing. |  |
|  | Replace | Specifies the value with which DIAdem replaces NoValues. |
|  | Control channel used | Specifies whether DIAdem searches for NoValues only in the x-channel or also in the y-channels. |
|  | Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

|  | Note If you want to process a waveform channel in this dialog box, select Only process one channel and enter the waveform channel as x-channel. If the y-share of the waveform channel is not monotonic increasing, you can only delete or replace but not interpolate NoValues in this channel. If you want to process several waveform channels, you must generate a matching x-channel with the Numeric Channels <-> Waveform Channels function. |
| --- | --- |

|  | Note You can use the CTNV function to replace values that exceed or fall short of the limit values, with NoValues. Refer to the Searching for and Interpolating Invalid Values page for an example of how the CTNV function works. Refer to the Help page Eliminating Outliers Using NoValues for a description of how to find outliers that exceed a limit and to replace the outliers with NoValues. |
| --- | --- |

#### Result

DIAdem generates one or more result channels. If the original channels do not contain NoValues, DIAdem does not generate a result channel. If DIAdem deletes NoValues in a data channel, the succeeding values move up. If the input channels only contain NoValues, DIAdem generates empty result channels.

|  | Refer to the Help page Channel Functions for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnNovHandle")

[ChnNovHandle](../../comoff/chnnovhandle.htm)

#### Related Topics

[Add Event](../calc_basis_dlg/dlgchneventdetection_new_dialog.htm) | [Add](../calc_basis_dlg/dlgchnadd_dialog.htm) | [Add](../calc_basis_dlg/dlgchnadd_dialog.htm) | [Averaging Channels](../calc_basis_dlg/dlgchnaverage_dialog.htm) | [Calculate Differences](../calc_basis_dlg/dlgchndeltacalc_dialog.htm) | [Calculate Peaks](../calc_basis_dlg/dlgchnpeakdetect_dialog.htm) | [Calculate Reciprocal](../calc_basis_dlg/dlgchnreciproc_dialog.htm) | [Calculate RMS](../calc_basis_dlg/dlgchnrms_dialog.htm) | [Calculating Quantity-Based with Mathematical Functions](../../procmaths/procmaths/mathsproc_calculating_dimension_based.htm) | [Channel Comparison](../calc_basis_dlg/dlgchneventdetection_compare_dialog.htm) | [Channels <-> Assignment Channels](../calc_basis_dlg/dlganaassignment_dialog.htm) | [Channels <-> XY-Channels](../calc_basis_dlg/dlgchntoxychn_dialog.htm) | [Concatenate Channels](../calc_basis_dlg/dlgchnconcatenatechannels_dialog.htm) | [Detrend](../calc_basis_dlg/dlgchndetrendcalc_dialog.htm) | [Difference](../calc_basis_dlg/dlgchneventdetection_difference_dialog.htm) | [Differentiate](../calc_basis_dlg/dlgchndifferent_dialog.htm) | [Divide](../calc_basis_dlg/dlgchndiv_dialog.htm) | [Find Pattern](../calc_basis_dlg/dlgchneventpatternfind_dialog.htm) | [Find Peaks](../calc_basis_dlg/dlgchnpeakfind_dialog.htm) | [Generate Numeric Channel](../calc_basis_dlg/dlgchngen_dialog.htm) | [Generate Time Channel](../calc_basis_dlg/dlgchngentime_dialog.htm) | [Integrate](../calc_basis_dlg/dlgchnintegrate_dialog.htm) | [Limiting Channel Values](../calc_basis_dlg/dlgchnrangelimit_dialog.htm) | [Mirror Channel](../calc_basis_dlg/dlgchnmirror_dialog.htm) | [Multiply](../calc_basis_dlg/dlgchnmul_dialog.htm) | [Normalize](../calc_basis_dlg/dlgchnnormalize_dialog.htm) | [Numeric Channels <-> Complex Channels](../calc_basis_dlg/dlgchntocomplexchn_dialog.htm) | [Numeric Channels <-> Time Channels](../calc_basis_dlg/dlgchnnumerictotime_dialog.htm) | [Numeric Channels <-> Waveform Channels](../calc_basis_dlg/dlgchntowfchn_dialog.htm) | [Offset Correction](../calc_basis_dlg/dlgchnoffset_dialog.htm) | [Optimize Data Type](../calc_basis_dlg/dlgchnoptimizedatatype_dialog.htm) | [Phase Unwrap/Wrap](../calc_basis_dlg/dlgchnwrapunwrap_dialog.htm) | [Quantize](../calc_basis_dlg/dlgchnquantize_dialog.htm) | [Relativize](../calc_basis_dlg/dlgchnrelativize_dialog.htm) | [Remove Duplicates](../calc_basis_dlg/dlgchndelduplicates_dialog.htm) | [Resampling](../calc_basis_dlg/dlgchnresample_dialog.htm) | [Rounding](../calc_basis_dlg/dlgchnround_dialog.htm) | [Scale](../calc_basis_dlg/dlgchnlinscale_dialog.htm) | [Slope](../calc_basis_dlg/dlgchneventdetection_slope_dialog.htm) | [Sort Channel Values](../calc_basis_dlg/dlgchnmultisort_dialog.htm) | [Subtract](../calc_basis_dlg/dlgchnsub_dialog.htm) | [Summation](../calc_basis_dlg/dlgchnsum_dialog.htm) | [Synchronize Data from Different Files](../calc_basis_dlg/dlgchnresamplexoffsetcalc_dialog.htm) | [Transform Channels](../calc_basis_dlg/dlganachntransform_dialog.htm) | [Window](../calc_basis_dlg/dlgchneventdetection_window_dialog.htm)

#### Procedures

[Using NoValues to Eliminate Outliers](../../procmaths/procmaths/mathsproc_novalue_limit.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchncfcfilt_dialog.htm language=enus -->
## TOPIC 00343: Crash Analysis (Digital Filters)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchncfcfilt_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchncfcfilt_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Digital Filters)

Crash Analysis (Digital Filters)

Use this dialog box for digital signal filtering without phase shifting.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the amplitude values of the signal. |
| Method | Specifies the filtering characteristic with specific limit frequencies and tolerance widths for the lowpass filters. |
| Data extension mode | Specifies how DIAdem extends the input data at the starting point and the end point of the signal, to eliminate transient response in the filter. DIAdem executes the rotary reflection either at the boundary points of the signal or at the zero amplitude of the boundary points. |
| Free filter class | Specifies the filter class when the CFC filtering is non-standardized. |
| Oversampling back to the original sample rate | Specifies whether DIAdem oversamples the 1600 Hz time channel back to the original sample rate in FIR100 filtering. |
| Remove bias | Specifies whether DIAdem eliminates the bias in FIR100 filtering. DIAdem calculates the bias from the part of the signal before the peak. For DIAdem to calculate the bias correctly, approximately half the signal up to the maximum must contain the bias. |

|  | Refer to the description of the CFC Filter for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels and you set a CFC filter in this dialog box, follow rules 2.2 and 2.3 for calculating with waveform channels. If you use waveform channels and you set an Fir100 filter, follow Rule 2.1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the y-values of the filtered signal.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnCFCFiltCalc")

[ChnCFCFiltCalc](../../comoff/chncfcfiltcalc.htm)

[ChnFir100Calc](../../comoff/chnfir100calc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchncwvcalc_dialog.htm language=enus -->
## TOPIC 00344: Crash Analysis (CWV)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchncwvcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchncwvcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (CWV)

Crash Analysis (CWV)

Use this dialog box to calculate the chest wall velocity that occurs when the chest is crushed by a pressure wave. The chest wall velocity allows statements about injuries to internal organs by overpressure waves which do not affect the ear.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal in seconds. |
| --- | --- |
| Overpressure | Specifies the data channel containing the overpressure in Pascal. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the values of the chest wall velocity in meters per second, in a result channel.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

|  | Note For further information such as mathematical background, input values, directives and rules, refer to the web site RTO-TR-HFM-090 Test Methodology for Protection of Vehicle Occupants against Anti-Vehicular Landmine Effects in paragraph 3.6.2.3 of the third chapter and in paragraph 1.2.2.2 of Appendix I. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnCWVCalc")

[ChnCWVCalc](../../comoff/chncwvcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchndricalc_dialog.htm language=enus -->
## TOPIC 00345: Crash Analysis (DRI)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchndricalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchndricalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (DRI)

Crash Analysis (DRI)

Use this dialog box to calculate the Dynamic Response Index value (DRI). The Dynamic Response Index value is a criterion for axial compression force injuries to the thoracic-lumbar spine. The DRI is a dimensionless value related to the spine deflection.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal in seconds. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the acceleration in m/s^2. |
| Direction of the DRI calculation | Specifies the direction of the DRI calculation. |
| Damping coefficient | Specifies the damping coefficient if the DRI calculation is free. |
| Natural frequency | Specifies the natural frequency of the dynamic system in rad/s if the DRI calculation is free. |

|  | For further information such as mathematical background, input values, directives and rules, refer to the web site RTO-TR-HFM-090 Test Methodology for Protection of Vehicle Occupants against Anti-Vehicular Landmine Effects in paragraph 3.3.2.1 of the third chapter and in paragraph 1.2.2.1 of Appendix I. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a dimensionless result channel. The DRI value is the maximum value of this result channel.

| DRIRes | Receives the result of the DRI calculation. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnDRICalc")

[ChnDRICalc](../../comoff/chndricalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnduration_dialog.htm language=enus -->
## TOPIC 00346: Crash Analysis (Time at Level)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnduration_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnduration_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Time at Level)

Crash Analysis (Time at Level)

Use this dialog box to calculate the time at level and the injury risk. The time at level describes the maximum length of time during which a signal overshoots or undershoots a specific threshold value.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal in seconds. |
| --- | --- |
| Y-channel | Specifies the data channel containing the amplitude values of the signal. |
| Calculate injury | Specifies whether DIAdem calculates the ratio between the times at level, and the limits. If you select this checkbox, you can specify the boundary curves. |
| X1-channel | Specifies the data channel containing the time values of the positive boundary curve, in seconds. |
| Y1-channel | Specifies the data channel containing the amplitude values of the positive limit curve. |
| Include negative limit curve | Specifies whether DIAdem also includes the negative limit curve in the calculation. |
| X2-channel | Specifies the data channel that contains the time values of the negative boundary curve, in seconds. |
| Y2-channel | Specifies the data channel containing the amplitude values of the negative limit curve. |
| Calculation within one peak/Calculation over all peaks/Calculation within one peak (user-defined) | Specifies whether DIAdem calculates the time at level from one section or several sections. |
| No. of steps | Specifies the number of steps for the user-defined time-at-level calculation. |
| Duration | Specifies the duration of the user-defined time-at-level calculation. |

|  | Refer to the description of the Time at Level for further information such as the mathematical background, input values, and directives and laws. |
| --- | --- |

#### Result

DIAdem generates several result channels, which contain the time at level, the amplitudes, and the injury values.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

|  | Note If the data to classify deviates slightly from the class limits, it might be necessary to round the data first. For example, if the data differs in the 12th decimal place, you should round the data mathematically to the 12th decimal place. This prevents DIAdem from classifying the data incorrectly due to minimal variations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnDurCalc")

[ChnDurPosNegCalc](../../comoff/chndurposnegcalc.htm)

[ChnDurInjuryCalc](../../comoff/chndurinjurycalc.htm)

[ChnDurPosCalc](../../comoff/chndurposcalc.htm)

[ChnDurPosInjCalc](../../comoff/chndurposinjcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnffc_dialog.htm language=enus -->
## TOPIC 00347: Crash Analysis (FFC)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnffc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnffc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (FFC)

Crash Analysis (FFC)

Use this dialog box to calculate the Femur Force Criterion (FFC) values.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal in seconds. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Y-Channel | Specifies the CFC600-filtered data channel containing the force in Newton kilo. |

|  | Note The FFC calculation in DIAdem 11.0 and earlier versions is different. DIAdem now uses the cumulative calculation of all peaks according to the EuroNCAP. You can use Time at Level for a continuous calculation within a peak. |
| --- | --- |

|  | Note The FFCVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the description of the FFC criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates five result channels. The first three result channels contain the load duration, the amplitude, and the injury values. The other two result channels contain the x-values and the y-values for the FFC boundary curve.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnFFCBdryCalc")

[ChnFFCBdryCalc](../../comoff/chnffcbdrycalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnhcdcalc_dialog.htm language=enus -->
## TOPIC 00348: Crash Analysis (HCD)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnhcdcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnhcdcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (HCD)

Crash Analysis (HCD)

Use this dialog box to calculate the Head Contact Duration (HCD) values.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Acceleration | Specifies the data channel containing the acceleration values of the signal in gn (acceleration of gravity). |
| Neck force | Specifies the data channel with the resulting contact force in Newton, which is calculated from the neck forces, acceleration values, and the head mass. |
| HCD value | Specifies whether DIAdem calculates the HCD value. |
| HCD 36 value | Specifies whether DIAdem calculates the 36 ms value. |
| HCD 15 value | Specifies whether DIAdem calculates the 15 ms value. |
| HCD XY value | Specifies whether DIAdem calculates the HCD value with adjustable window width. |
| Window width | Specifies the width of the window for calculating the HCD value in milliseconds. |

|  | Refer to the description of the HCD criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

The calculation results are in the 4*4 variable matrix [HCDRes](../../varoff/hcdres.htm) and the channel properties of the input channel. The HCD values are specified in gn (acceleration of gravity) and the time values in ms:

| Result variable | Channel property | Description |
| --- | --- | --- |
| HCDRes(1,1) | Result~HPC~Value | Receives the HCD values for unlimited duration. |
| HCDRes(2.1) | Result~HCD~T1 | Receives the T1 values for an unlimited duration. |
| HCDRes(3.1) | Result~HCD~T2 | Receives the T2 values for an unlimited duration. |
| HCDRes(4.1) | Result~HCD~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for an unlimited duration. |
| HCDRes(1.2) | Result~HCD36~Value | Receives the HCD values for 36 ms. |
| HCDRes(2.2) | Result~HCD36~T1 | Receives the T1 values for 36 ms. |
| HCDRes(3.2) | Result~HCD36~T2 | Receives the T2 values for 36 ms. |
| HCDRes(4.2) | Result~HCD36~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for 36 ms. |
| HCDRes(1.3) | Result~HCD15~Value | Receives the HCD values for 15 ms. |
| HCDRes(2.3) | Result~HCD15~T1 | Receives the T1 values for 15 ms. |
| HCDRes(3.3) | Result~HCD15~T2 | Receives the T2 values for 15 ms. |
| HCDRes(4.3) | Result~HCD15~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for 15 ms. |
| HCDRes(1.4) | Result~HCDd~Value | Receives the HCD values for the value specified in ms. |
| HCDRes(2.4) | Result~HCDd~T1 | Receives the T1 values for the value specified in ms. |
| HCDRes(3.4) | Result~HCDd~T1 | Receives the T2 values for the value specified in ms. |
| HCDRes(4.4) | Result~HCDd~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for the value specified in ms. |
| HCDVersion | Result~HCD~Version | Receives the algorithm version number, which is independent of the DIAdem version number. |
|  | Result~HCDUser~WindowWidth | Receives the width of the window for calculating the HCD value in milliseconds. |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnHCDCalc")

[ChnHCDCalc](../../comoff/chnhcdcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnhiccalc_dialog.htm language=enus -->
## TOPIC 00349: Crash Analysis (HIC)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnhiccalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnhiccalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (HIC)

Crash Analysis (HIC)

Use this dialog box to calculate the Head Injury Criterion (HIC) values.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal in seconds. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Acceleration | Specifies the data channel containing the acceleration values of the signal in gn (acceleration of gravity). |
| HIC value | Specifies whether DIAdem calculates the HIC value. |
| HIC 36 value | Specifies whether DIAdem calculates the 36 ms value. |
| HIC 15 value | Specifies whether DIAdem calculates the 15 ms value. |
| HIC XY value | Specifies whether DIAdem calculates the HIC value with adjustable window width. |
| HIC(d) value | Specifies whether DIAdem calculates the HIC(d) value. |
| Window width | Specifies the width of the window for calculating the HIC value in milliseconds. |

|  | Note The HICVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the description of the HIC criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

The calculation results are in the 4*5 variable matrix [HICRes](../../varoff/hicres.htm) and the channel properties of the input channel. The HIC values are specified in gn (acceleration of gravity) and the time values in ms:

| Result variable | Channel property | Description |
| --- | --- | --- |
| HICRes(1.1) | Result~HIC~Value | Receives the HIC values for unlimited duration. |
| HICRes(2.1) | Result~HIC~T1 | Receives the T1 values for an unlimited duration. |
| HICRes(3.1) | Result~HIC~T2 | Receives the T2 values for an unlimited duration. |
| HICRes(4.1) | Result~HIC~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for an unlimited duration. |
| HICRes(1.2) | Result~HIC36~Value | Receives the HIC values for 36 ms. |
| HICRes(2.2) | Result~HIC36~T1 | Receives the T1 values for 36 ms. |
| HICRes(3.2) | Result~HIC36~T2 | Receives the T2 values for 36 ms. |
| HICRes(4.2) | Result~HIC36~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for 36 ms. |
| HICRes(1.3) | Result~HIC15~Value | Receives the HIC values for 15 ms. |
| HICRes(2.3) | Result~HIC15~T1 | Receives the T1 values for 15 ms. |
| HICRes(3.3) | Result~HIC15~T2 | Receives the T2 values for 15 ms. |
| HICRes(4.3) | Result~HIC15~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for 15 ms. |
| HICRes(1.4) | Result~HICUser~Value | Receives the HIC values for the value specified in ms. |
| HICRes(2.4) | Result~HICUser~T1 | Receives the T1 values for the value specified in ms. |
| HICRes(3,4) | Result~HICUser~T2 | Receives the T2 values for the value specified in ms. |
| HICRes(4.4) | Result~HICUser~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for the value specified in ms. |
| HICRes(1.5) | Result~HICd~Value | Receives the HIC(d) values. |
| HICRes(2.5) | Result~HICd~T1 | Receives the T1 values for the HIC(d) calculation. |
| HICRes(3.5) | Result~HICd~T1 | Receives the T2 values for the HIC(d) calculation. |
| HICRes(4.5) | Result~HICd~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for the HIC(d) calculation. |
| HICVersion | Result~HIC~Version | Receives the algorithm version number, which is independent of the DIAdem version number. |
|  | Result~HICUser~WindowWidth | Receives the width of the window for calculating the HIC value in milliseconds. |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnHICCalc")

[ChnHICCalc](../../comoff/chnhiccalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnhpccalc_dialog.htm language=enus -->
## TOPIC 00350: Crash Analysis (HPC)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnhpccalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnhpccalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (HPC)

Crash Analysis (HPC)

Use this dialog box to calculate the Head Performance Criterion (HPC) values.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal in seconds. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Acceleration | Specifies the data channel containing the acceleration values of the signal in gn (acceleration of gravity). |
| HPC value | Specifies whether DIAdem calculates the HPC value. |
| HPC 36 value | Specifies whether DIAdem calculates the 36 ms value. |
| HPC 15 value | Specifies whether DIAdem calculates the 15 ms value. |
| HPC XY value | Specifies whether DIAdem calculates the HPC value with adjustable window width. |
| Window width | Specifies the width of the window for calculating the HPC value in milliseconds. |

|  | Refer to the description of the HPC criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

The calculation results are in the 4*5 variable matrix [HPCRes](../../varoff/hpcres.htm) and the channel properties of the input channel. The HPC values are specified in gn (acceleration of gravity) and the time values in ms:

| Result variable | Channel property | Description |
| --- | --- | --- |
| HPCRes(1,1) | Result~HPC~Value | Receives the HPC values for unlimited duration. |
| HPCRes(2.1) | Result~HPC~T1 | Receives the T1 values for an unlimited duration. |
| HPCRes(3.1) | Result~HPC~T2 | Receives the T2 values for an unlimited duration. |
| HPCRes(4.1) | Result~HPC~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for an unlimited duration. |
| HPCRes(1.2) | Result~HPC36~Value | Receives the HPC values for 36 ms. |
| HPCRes(2.2) | Result~HPC36~T1 | Receives the T1 values for 36 ms. |
| HPCRes(3.2) | Result~HPC36~T2 | Receives the T2 values for 36 ms. |
| HPCRes(4.2) | Result~HPC36~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for 36 ms. |
| HPCRes(1.3) | Result~HPC15~Value | Receives the HPC values for 15 ms. |
| HPCRes(2.3) | Result~HPC15~T1 | Receives the T1 values for 15 ms. |
| HPCRes(3.3) | Result~HPC15~T2 | Receives the T2 values for 15 ms. |
| HPCRes(4.3) | Result~HPC15~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for 15 ms. |
| HPCRes(1.4) | Result~HPCUser~Value | Receives the HPC values for the value specified in ms. |
| HPCRes(2.4) | Result~HPCUser~T1 | Receives the T1 values for the value specified in ms. |
| HPCRes(3.4) | Result~HPCUser~T2 | Receives the T2 values for the value specified in ms. |
| HPCRes(4.4) | Result~HPCUser~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for the value specified in ms. |
| HPCRes(1.5) | Result~HPCd~Value | Receives the HPC(d) values as an option. |
| HPCRes(2.5) | Result~HPCd~T1 | Receives the T1 values of the HPC(d) calculation as an option. |
| HPCRes(3.5) | Result~HPCd~T1 | Receives the T2 values of the HPC(d) calculation as an option. |
| HPCRes(4.5) | Result~HPCd~MeanAcceleration | Receives the mean value of the head acceleration between T1 and T2 for the HPC(d) calculation as an option. |
| HPCVersion | Result~HPC~Version | Receives the algorithm version number, which is independent of the DIAdem version number. |
|  | Result~HPCUser~WindowWidth | Receives the width of the window for calculating the HPC value in milliseconds. |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnHPCCalc")

[ChnHPCCalc](../../comoff/chnhpccalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnkthcalc_dialog.htm language=enus -->
## TOPIC 00351: Crash Analysis (KTH)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnkthcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnkthcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (KTH)

Crash Analysis (KTH)

Use this dialog box to calculate the Knee Thigh Hip value (KTH) which indicates the injury risk for the hip and thigh.

For the evaluation, the KTH algorithm integrates the forces impacting the hip and thigh from the last zero crossing before the maximum value of the force up to the point at which the force exceeds the value of 4.050 Kilo newton for the first time after the maximum, over time.

#### Settings

| Time channel [ms] | Specifies the data channel containing the time values of the signal in milliseconds. |
| --- | --- |
| Force [kN] | Specifies the data channel containing the forces in Newton. |

|  | Note The KTHVersion variable receives the algorithm version number which differs from the DIAdem version. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the evaluation of the calculation in the variable [KTHRating](../../varoff/kthrating.htm). The variable [KTHFmax](../../varoff/kthfmax.htm) receives the maximum value of the forces inlo Newton and the variable [KTHImpuls](../../varoff/kthimpulse.htm) receives the impulse of t0 after t1 in Newton seconds. The variable [KTHt0](../../varoff/ktht0.htm) receives the time span until the last zero crossing before the maximum value is reached, and the variable [KTHt1](../../varoff/ktht1.htm) receives the time span until the falling slope after the maximum value is reached in milli seconds.

|  | Note DIAdem saves the calculation results and the version number of the algorithm which is not the same as the DIAdem version number in the following custom properties of the result channel: Result~KTH~Rating, Result~KTH~FMax, Result~KTH~t0, Result~KTH~t1, and Result~KTH~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaKTHCalc")

[ChnKTHCalc](../../comoff/chnkthcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnlatardisp_dialog.htm language=enus -->
## TOPIC 00352: Crash Analysis (Lateral Abdominal Rib Displacement)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnlatardisp_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnlatardisp_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Lateral Abdominal Rib Displacement)

Crash Analysis (Lateral Abdominal Rib Displacement)

Use this dialog box to calculate the Lateral Abdominal Rib Displacement.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal. |
| --- | --- |
| Abdominal IR-TRACC length | Specifies the data channel containing the measured length of the rib displacement. |
| Abdominal IR-TRACC rotation | Specifies the data channel containing the measured rotation of the rib displacement. |

|  | Refer to the descriptions in the Crash Analysis Criteria for further information on crash functions such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. In this case, each input channel must be a waveform channel. |
| --- | --- |

#### Result

DIAdem generates one result channel. DIAdem uses the following formula to calculate the Lateral Abdominal Rib Displacement:

[IMAGE alt='image' src='../image/f_lrd_a.gif']

with

[IMAGE alt='image' src='../image/f_lrd_2.gif']

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnLatARDispCalc")

[ChnLateralAbdominalRibDisplacement](../../comoff/chnlateralabdominalribdisplacement.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnlatsrdisp_dialog.htm language=enus -->
## TOPIC 00353: Crash Analysis (Lateral Shoulder Rib Displacement)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnlatsrdisp_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnlatsrdisp_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Lateral Shoulder Rib Displacement)

Crash Analysis (Lateral Shoulder Rib Displacement)

Use this dialog box to calculate the Lateral Shoulder Rib Displacement.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal. |
| --- | --- |
| Shoulder IR-TRACC length | Specifies the data channel containing the measured length of the rib displacement. |
| Shoulder IR-TRACC rotation | Specifies the data channel containing the measured rotation of the rib displacement. |

|  | Refer to the descriptions in the Crash Analysis Criteria for further information on crash functions such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. In this case, each input channel must be a waveform channel. |
| --- | --- |

#### Result

DIAdem generates one result channel. DIAdem uses the following formula to calculate the Lateral Shoulder Rib Displacement:

[IMAGE alt='image' src='../image/f_lrd_s.gif']

with

[IMAGE alt='image' src='../image/f_lrd_2.gif']

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnLatSRDispCalc")

[ChnLateralShoulderRibDisplacement](../../comoff/chnlateralshoulderribdisplacement.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnlattrdisp_dialog.htm language=enus -->
## TOPIC 00354: Crash Analysis (Lateral Thoracic Rib Displacement)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnlattrdisp_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnlattrdisp_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Lateral Thoracic Rib Displacement)

Crash Analysis (Lateral Thoracic Rib Displacement)

Use this dialog box to calculate the Lateral Thoracic Rib Displacement.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal. |
| --- | --- |
| Thoracic IR-TRACC length | Specifies the data channel containing the measured length of the rib displacement. |
| Thoracic IR-TRACC rotation | Specifies the data channel containing the measured rotation of the rib displacement. |

|  | Refer to the descriptions in the Crash Analysis Criteria for further information on crash functions such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. In this case, each input channel must be a waveform channel. |
| --- | --- |

#### Result

DIAdem generates one result channel. DIAdem uses the following formula to calculate the Lateral Thoracic Rib Displacement:

[IMAGE alt='image' src='../image/f_lrd_t.gif']

with

[IMAGE alt='image' src='../image/f_lrd_2.gif']

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnLatTRDispCalc")

[ChnLateralThoracicRibDisplacement](../../comoff/chnlateralthoracicribdisplacement.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnnic_dialog.htm language=enus -->
## TOPIC 00355: Crash Analysis (NIC)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnnic_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnnic_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (NIC)

Crash Analysis (NIC)

Use this dialog box to calculate the Normalized Neck Injury Criterion (NIC) value according to ECE.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal in seconds. |
| --- | --- |
| Y-Channel | Specifies the CFC600-filtered data channel containing the forces in Newton kilo. |
| Data type | Specifies whether the forces are axial tensile forces or shear forces. |

|  | Note The NIC calculation in DIAdem 11.0 and earlier versions is different. DIAdem now uses the cumulative calculation of all peaks according to the EuroNCAP. You can use Time at Level for a continuous calculation within a peak. |
| --- | --- |

|  | Note The NICVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the description of the NIC (front impact ECE) criterion for further information such as the mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates five result channels. The first three result channels contain the load duration, the amplitude, and the injury values. The other two result channels contain the x-values and the y-values for the NIC boundary curve.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnNICBdryCalc")

[ChnNICBdryCalc](../../comoff/chnnicbdrycalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnnicrearcalc_dialog.htm language=enus -->
## TOPIC 00356: Crash Analysis (NIC Rear Impact)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnnicrearcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnnicrearcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (NIC Rear Impact)

Crash Analysis (NIC Rear Impact)

Use this dialog box to execute the Neck Injury Criterion (NIC) Rear Impact calculation.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Head acceleration | Specifies the data channel with the acceleration values of the head in the x-direction, in meters per square second. |
| Spine acceleration | Specifies the data channel containing the acceleration values of the first spinal vertebra in the x-direction, in meters per square second. |

|  | Note According to the legal stipulations, the accelerations must be filtered with CFC180. |
| --- | --- |

|  | Note The NICRearVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the description of the NIC (rear impact ECE) criterion for further information such as the mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rules 2.2 and 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the NIC values.

| NICRearMax | Receives the NIC maximum value, in meters per square second. |
| --- | --- |
| NICRearTime | Receives the time for the NIC maximum value, in seconds. |

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the result channel. Result~NICRear~Max, Result~NICRear~Time, and Result~NICRear~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnNICRearCalc")

[ChnNICRearCalc](../../comoff/chnnicrearcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnnijcalc_dialog.htm language=enus -->
## TOPIC 00357: Crash Analysis (NIJ)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnnijcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnnijcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (NIJ)

Crash Analysis (NIJ)

Use this dialog box to calculate the Normalized Neck Injury Criterion value (NIJ) according to FMVSS.

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal in seconds. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Force Fz | Specifies the data channel containing the values of the axial force in the z-direction at the point where the head intersects with the neck, in Newton. |
| Moment My | Specifies the data channel containing the values of the bending moment (total moment) in the y-direction at the top of the neck, in newton meters. |
| NTF | Specifies whether DIAdem executes the Nij calculation after NTF. |
| Critical compression force Fzc [N] | Specifies the critical compression force in newton for NTF. |
| Critical bending moment Myc [Nm] | Specifies the critical bending moment in newton meters for NTF. |
| NTE | Specifies whether DIAdem executes the Nij calculation after NTE. |
| Critical compression force Fzc [N] | Specifies the critical compression force in newton for NTE. |
| Critical bending moment Myc [Nm] | Specifies the critical bending moment in newton meters for NTE. |
| NCE | Specifies whether DIAdem executes the Nij calculation after NTE. |
| Critical compression force Fzc [N] | Specifies the critical compression force in newton for NCE. |
| Critical bending moment Myc [Nm] | Specifies the critical bending moment in newton meters for NCE. |
| NCF | Specifies whether DIAdem executes the Nij calculation after NCF. |
| Critical compression force Fzc [N] | Specifies the critical compression force in newton for NCF. |
| Critical bending moment Myc [Nm] | Specifies the critical bending moment in newton meters for NCF. |

|  | Note The NijVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |
|  | Refer to the description of the NIJ criterion for further information such as mathematical background, input values, and directives and laws. |

|  | If you want to use waveform channels in this dialog box, follow Rules 2.2 and 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel that contains the values of the NIJ analysis curve.

| NijMax | Receives the maximum value of the NIJ calculation. |
| --- | --- |
| NijTime | Receives the time value for the maximum value. |
| NijType | Receives the calculation type. |

|  | Note DIAdem saves the calculation results and the version number of the algorithm which is not the same as the DIAdem version number in the following custom properties of the result channel: Result~Nij~Max, Result~Nij~Time, Result~Nij~Type, and Result~Nij~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnNijCalc")

[ChnNijCalc](../../comoff/chnnijcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnoivcalc_dialog.htm language=enus -->
## TOPIC 00358: Crash Analysis (OIV)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnoivcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnoivcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (OIV)

Crash Analysis (OIV)

Use this dialog box to specify the Occupant Impact Velocity (OIV).

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal in seconds. |
| --- | --- |
| Acceleration X | Specifies the x-channel containing the CFC180 filtered acceleration values in gn (acceleration of gravity). |
| Acceleration Y | Specifies the y-channel containing the CFC180 filtered acceleration values in gn (acceleration of gravity). |
| Distance head – center of gravity | Specifies the distance between the theoretical head and the vehicle center of gravity in meters. |
| X-distance head – impact surface | Specifies the distance between the theoretical head and the theoretical impact surface in x-direction in meters. |
| Y-distance head - impact surface | Specifies the distance between the theoretical head and the theoretical impact surface in y-direction in meters. |

#### Result

DIAdem saves the results in the following variables:

| OIVTimeFlight | Receives the period of time in seconds during which the impact moves the passengers. |
| --- | --- |
| OIVVelocity | Receives the impact velocity of the passengers in kilometers per hour. |

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the input channel. Result~OIV~TimeFlight, Result~OIV~Velocity, and Result~OIV~Version. |
| --- | --- |

|  | Note The OIVVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Note Refer to the standard EN 1317-1, Road Restraint Systems, Part 1: Terminology and General Criteria for Test Methods, for more information about this crash function. |
| --- | --- |

|  | Note The actual calculation routine does not filter. According to EN 1317-2, Chapter 5.6, the input channels must be filtered with CFC180. |
| --- | --- |

|  | Refer to the descriptions in the Crash Analysis Criteria for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnOIVCalc")

[ChnOIVCalc](../../comoff/chnoivcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnphdcalc_dialog.htm language=enus -->
## TOPIC 00359: Crash Analysis (PHD)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnphdcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnphdcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (PHD)

Crash Analysis (PHD)

Use this dialog box to calculate the Post-Impact Head Deceleration (PHD).

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel that contains the time values of the signal in seconds. |
| --- | --- |
| Acceleration X | Specifies the x-channel containing the CFC180 filtered acceleration values in gn (acceleration of gravity). |
| Acceleration Y | Specifies the y-channel containing the CFC180 filtered acceleration values in gn (acceleration of gravity). |
| Time of collision | Specifies the time of collision of the theoretical head with the theoretical impact surface, in seconds. |

#### Result

DIAdem saves the results in the following variables:

| PHDTime | Receives the time for the maximum head delay, in seconds. |
| --- | --- |
| PHDMax | Receives the maximum head deceleration after the impact in gn (acceleration of gravity). |

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the input channel. Result~PHD~Max, Result~PHD~Time, and Result~PHD~Version. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

|  | Note The PHDVersion variable of the result channel receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Note Refer to the standard EN 1317-1, Road Restraint Systems, Part 1: Terminology and General Criteria for Test Methods, for more information about this crash function. |
| --- | --- |

|  | Note The actual calculation routine does not filter. According to EN 1317-2, Chapter 5.6, the input channels must be filtered with CFC180. |
| --- | --- |

|  | Refer to the descriptions in the Crash Analysis Criteria for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnPHDCalc")

[ChnPHDCalc](../../comoff/chnphdcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnpulselimit_dialog.htm language=enus -->
## TOPIC 00360: Crash Analysis (Pulse Limit)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnpulselimit_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnpulselimit_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Pulse Limit)

Crash Analysis (Pulse Limit)

Use this dialog box to check whether a measured acceleration is within a given corridor.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal in seconds. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the acceleration values in gn (acceleration of gravity). |
| X1-channel | Specifies the data channel containing the x-data points of the upper band. |
| Y1-Channel | Specifies the data channel containing the y-data points of the upper band. |
| X2-channel | Specifies the data channel containing the x-data points of the lower band. |
| Y2-channel | Specifies the data channel containing the y-data points of the lower band. |

|  | Note The time channel of the measured value must be strictly monotonic increasing. The data channels that contain the x-interpolation values must be monotonic increasing. |
| --- | --- |
|  | Note The PulseLimitVer variable receives the algorithm version number, which is independent of the DIAdem version number. |

|  | Refer to the descriptions of the Pulse Test for further information such as the mathematical background, input values, and directives and laws. |
| --- | --- |

#### Result

DIAdem saves the results in the following variables:

| PulseLimit | Specifies whether the measured value is entirely within the specified range. |
| --- | --- |
| PulseLimitTIdx | Receives the number of the first point outside the given range. |

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the input channel. Result~PulseLimit, Result~PulseLimit~TIdx, and Result~PulseLimit~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnPulseLimit")

[ChnPulseLimit](../../comoff/chnpulselimit.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnsplitatvalue_dialog.htm language=enus -->
## TOPIC 00361: Divide Channel at Limit Value

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnsplitatvalue_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnsplitatvalue_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Divide Channel at Limit Value

Divide Channel at Limit Value

Use this dialog box to divide a channel at a specified limit value into two new channels.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Channel | Specifies the data channel containing the values to be divided. |
| --- | --- |
| Limit value | Specifies the limit value at which DIAdem divides a channel. |
| Replace limit values by NoValues | Specifies whether DIAdem replaces the values that correspond to the limit value, with NoValue or with the limit value, in the result channels. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates two result channels that contain the values above and below the limit value.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnSplitAtValue")

[ChnSplitAtValue](../../comoff/chnsplitatvalue.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnthivcalc_dialog.htm language=enus -->
## TOPIC 00362: Crash Analysis (THIV)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnthivcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnthivcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (THIV)

Crash Analysis (THIV)

Use this dialog box to calculate the Theoretical Head Impact Velocity (THIV).

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal in seconds. |
| --- | --- |
| Yaw angle speed | Specifies the data channel containing the rotational velocity in radians per second. |
| Acceleration X | Specifies the x-channel containing the CFC180 filtered acceleration values in gn (acceleration of gravity). |
| Acceleration Y | Specifies the y-channel containing the CFC180 filtered acceleration values in gn (acceleration of gravity). |
| Angle movement direction – vehicle axis | Specifies the angle between the direction of the vehicle and the vehicle axis at the time of impact, in radians. The default value is zero. |
| X-distance head - center of gravity | Specifies the distance between the theoretical head and the center of gravity in x-direction in meters. |
| Y-distance head - center of gravity | Specifies the distance between the theoretical head and the center of gravity in y-direction in meters. |
| X-distance head – impact surface | Specifies the distance between the theoretical head and the theoretical impact surface in x-direction in meters. |
| Y-distance head - impact surface | Specifies the distance between the theoretical head and the theoretical impact surface in y-direction in meters. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the results in the following variables and channels:

| THIVTimeFlight | Receives the time of collision of the theoretical head with the theoretical impact surface, in seconds. |
| --- | --- |
| THIVVelocity | Receives the impact velocity of the theoretical head in kilometers per hour. |
| PHDTime0 | Receives the time of collision of the theoretical head with the theoretical impact surface, in seconds. |
| THIVFlailSpace | Contains the flight distance of the theoretical head. |
| TimeOfFlight | The channel receives the time values up to the collision of the theoretical head with the theoretical impact surface, in seconds. |
| THIV [km/h] | The channel receives the impact velocity of the theoretical head in kilometers per hour associated with the values of the TimeOfFlight channel. |

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the input channel. Result~PHD~Time0, Result~THIV~FlailSpace, Result~THIV~TimeFlight, Result~THIV~Velocity, and Result~THIV~Version. |
| --- | --- |

|  | Note The THIVVersion variable of the result channel receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Note Refer to the standard EN 1317-1, Road Restraint Systems, Part 1: Terminology and General Criteria for Test Methods, for more information about this crash function. |
| --- | --- |

|  | Note The actual calculation routine does not filter. According to EN 1317-2, Chapter 5.6, the input channels must be filtered with CFC180. |
| --- | --- |

|  | Refer to the description of the THIV criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnTHIVCalc")

[ChnTHIVCalc](../../comoff/chnthivcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnticalc_dialog.htm language=enus -->
## TOPIC 00363: Crash Analysis (TI)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnticalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnticalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (TI)

Crash Analysis (TI)

Use this dialog box to calculate the Tibia Index (TI) value.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal. |
| --- | --- |
| Moment Mx | Specifies the CFC600-filtered data channel containing the bending moments around the x-axis, in newton meters. |
| Moment My | Specifies the CFC600-filtered data channel containing the bending moments around the y-axis, in newton meters. |
| Compression force Fz | Specifies the CFC600-filtered data channel containing the axial compression force in the z-direction, in kilonewton. |
| Critical bending moment Mc | Specifies the critical bending moment Mc in newton meters. |
| Critical compression force Fc | Specifies the critical compression force Fc in the z-direction, in kilonewtons. |

|  | Note The TIVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the description of the TI criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the result in the [TIRes](../../varoff/tires.htm) variable. The [TITime](../../varoff/titime.htm) variable receives the point in time in seconds of the calculated Tibia index.

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the input channel. Result~TI~Value, Result~TI~Time, and Result~TI~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnTICalc")

[ChnTICalc](../../comoff/chnticalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchntimeareacopy_dialog.htm language=enus -->
## TOPIC 00364: Crash Analysis (Copy Time Domain)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchntimeareacopy_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchntimeareacopy_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Copy Time Domain)

Crash Analysis (Copy Time Domain)

Use this dialog box to copy a time domain and the associated amplitude values of the measured value channel into two new data channels.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal in seconds. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Measurement channel | Specifies the data channel containing the amplitude values of the signal. |
| Current values - Begin | Displays the starting time for the selected time channel. |
| Current values - End | Displays the finish time for the selected time channel. |
| Selected interval – Begin | Determines the start value of the time domain, in seconds. |
| Selected interval – End | Determines the end value of the time domain, in seconds. |

|  | Note The TimeAreaCopyVer variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |
|  | Refer to the descriptions in the Crash Analysis Criteria for further information such as mathematical background, input values, and directives and laws. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates two result channels. The first result channel contains the time. The second result channel contains the amplitude values.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnTimeAreaCopy")

[ChnTimeAreaCopy](../../comoff/chntimeareacopy.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchntmintmax_dialog.htm language=enus -->
## TOPIC 00365: Crash Analysis (Min/Max)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchntmintmax_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchntmintmax_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Min/Max)

Crash Analysis (Min/Max)

Use this dialog box to determine when the first minimum value and the first maximum value occur in a signal.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal in seconds. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the amplitude values of the signal. |

|  | Note The MinMaxVer variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the descriptions in the Crash Analysis Criteria for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the results in the following variables:

| MinTime | Receives the time of the minimum value. |
| --- | --- |
| MaxTime | Receives the time of the maximum value. |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnTMinTMaxCalc")

[ChnTMinTMaxCalc](../../comoff/chntmintmaxcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchntticalc_dialog.htm language=enus -->
## TOPIC 00366: Crash Analysis (TTI)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchntticalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchntticalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (TTI)

Crash Analysis (TTI)

Use this dialog to calculate the Thorax Trauma Index value (TTI).

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel containing the time values of the signal. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Lower rib | Specifies the data channel containing the unfiltered acceleration values of the fourth rib in gn (acceleration of gravity). |
| Upper rib | Specifies the data channel containing the unfiltered acceleration values of the eighth rib in gn (acceleration of gravity). |
| Spine | Specifies the data channel containing the unfiltered acceleration values of the spine (twelfth vertebra) in gn (acceleration of gravity). |
| Oversampling FIR100 back to original sample rate | Specifies whether DIAdem oversamples the 1600 Hz time channel back to the original sample rate in FIR100 filtering. |

|  | Note The TTIVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the description of the TTI criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the result in the [TTIRes](../../varoff/ttires.htm) variable.

|  | Note DIAdem saves the results and the algorithm version number, which does not depend on the DIAdem version number, in the following custom properties: Result~TTI~Result and Result~TTI~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnTTICalc")

[ChnTTICalc](../../comoff/chntticalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnvccalc_dialog.htm language=enus -->
## TOPIC 00367: Crash Analysis (VC)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnvccalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnvccalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (VC)

Crash Analysis (VC)

Use this dialog box to calculate the Viscous Criterion (VC) values.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal in seconds. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the amplitudes of the unfiltered deformation signal in meters. |
| Deformation constant of the dummy type | Specifies the deformation constant (chest depth) of the dummy in millimeters. |
| Scaling factor | Specifies the scaling factor of the dummy. |
| Directive | Specifies the directive or the law for the VC calculation. |

|  | Refer to the description of the Viscous criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result channel with the calculated VC values.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnVCCalc")

[ChnVCCalc](../../comoff/chnvccalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnxgcalc_dialog.htm language=enus -->
## TOPIC 00368: Crash Analysis (Xg)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnxgcalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnxgcalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Xg)

Crash Analysis (Xg)

Use this dialog box to calculate the Xg value.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the acceleration values of the signal in gn (acceleration of gravity). |
| Acceleration | Specifies the acceleration in gn (gravity acceleration). |
| Calculation within one peak/including all peaks | Specifies whether DIAdem calculates the acceleration, which lasts X ms, from one section or several partial sections. |

|  | Note The XgVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |

|  | Refer to the description of the Xg criterion for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the results in the following variables:

| XgTimeBegin | Receives the time T1 of the calculated Xg acceleration. |
| --- | --- |
| XgTimeEnd | Receives the time T2 of the calculated Xg acceleration. |
| XgMaxPeak | Receives the time interval between T1 and T2 for the Xg calculation. |
| XgDeltaX | Gets the total time when separate sections are calculated. |

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the input channel. Result~Xg~DeltaX, Result~Xg~MaxPeak, Result~Xg~TimeBegin, Result~Xg~TimeEnd, and Result~Xg~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnXgCalc")

[ChnXGCalc](../../comoff/chnxgcalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnxmscalc_dialog.htm language=enus -->
## TOPIC 00369: Crash Analysis (Xms)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnxmscalc_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnxmscalc_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Xms)

Crash Analysis (Xms)

Use this dialog box to calculate the Xms values.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the time values of the signal. The values of the data channel must be monotonic increasing. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the acceleration values of the signal in gn (acceleration of gravity). |
| Time interval | Specifies the time in milliseconds. |
| Calculation within one peak/including all peaks | Specifies whether DIAdem calculates the acceleration from one section or several sections. |
| Include negative signal sections | Specifies whether DIAdem includes the negative signal sections in the Xms calculation. If you select this setting, DIAdem separately calculates the X ms values for the positive signal section, and the Xms values for the absolute value of the negative signal section. DIAdem sets the value for the other signal section to zero. DIAdem saves the X ms values of the higher absolute acceleration in the result variables.If you do not select this setting, DIAdem first calculates the absolute value of the total signal and specifies the Xms value for this signal. |

|  | Note The XmsVersion variable receives the algorithm version number, which is independent of the DIAdem version number. |
| --- | --- |
|  | Refer to the description of the Xms criterion for further information such as mathematical background, input values, and directives and laws. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem saves the results in the following variables:

| XmsAcceleration | Receives the acceleration of the X ms calculation. |
| --- | --- |
| XmsTimeBegin | Receives the time T1 of the calculated Xms acceleration. |
| XmsTimeEnd | Receives the time T2 of the calculated Xms acceleration. |
| XmsDeltaX | Receives the time T in the Xms calculation. |

|  | Note In addition, DIAdem saves the calculated results and the version number, which is independent of the DIAdem version, in the following custom properties of the input channel. Result~Xms~Acceleration, Result~Xms~TimeBegin, Result~Xms~TimeEnd, Result~Xms~DeltaX, and Result~Xms~Version. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnXmsCalc")

[ChnXMSCalc](../../comoff/chnxmscalc.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_crash_dlg/dlgchnxyzabs_dialog.htm language=enus -->
## TOPIC 00370: Crash Analysis (Resultant)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_crash_dlg/dlgchnxyzabs_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_crash_dlg/dlgchnxyzabs_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Crash Analysis](../calc_crash_dlg/calc_crash_overview.htm) > Crash Analysis (Resultant)

Crash Analysis (Resultant)

Use this dialog box to calculate the resultant acceleration from the acceleration values in the spatial directions x, y, and z.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel containing the x-values of the signal. |
| --- | --- |
| Y-Channel | Specifies the data channel containing the y-values of the signal. |
| Z-channel | Specifies the data channel containing the z-values of the signal. |

|  | Refer to the descriptions in the Crash Analysis Criteria for further information such as mathematical background, input values, and directives and laws. |
| --- | --- |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. In this case, each input channel must be a waveform channel. |
| --- | --- |

#### Result

DIAdem generates one result channel. DIAdem uses the following formula to calculate the acceleration values:

[IMAGE alt='image' src='../image/f_res.gif']

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnXYZAbsValue")

[ChnXYZAbsValue](../../comoff/chnxyzabsvalue.htm)

#### Examples

[Crash Analysis](../../exploff/examples/exp_analysis_av1.htm) | [Crash Evaluation Based on the MME Standard](../../exploff/examples/exp_analysis_ab_1.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_formula_dlg/calc_calculationmanager_overview.htm language=enus -->
## TOPIC 00371: Calculations

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_formula_dlg/calc_calculationmanager_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_formula_dlg/calc_calculationmanager_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > Calculations

Calculations

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes with which you create, check, and execute calculations in the [Calculation Manager](../../genmaths/genmaths/calc_calculationmanager.htm).

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_formula_dlg/dlgcm_calculation_dialog.htm language=enus -->
## TOPIC 00372: Calculation Manager - Edit Calculation - Calculation

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_formula_dlg/dlgcm_calculation_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_formula_dlg/dlgcm_calculation_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Calculation Channel](../../dlgportal/dlgportal/portal_new_calculationchannels.htm) | [Edit Calculations](../calc_formula_dlg/dlgcm_calculationset_dialog.htm)) > Calculation Manager - Edit Calculation - Calculation

Calculation Manager - Edit Calculation - Calculation

Use this dialog box to create or to edit a calculation.

You can use calculations to execute mathematical operations on channels and single values with a single-line formula. You can use all calculator functions and all active user commands in the formula.

#### Settings

| Toolbar |  |  |
| --- | --- | --- |
|  | Description | Specifies the calculation description. |
|  | Validation Successful | Checks whether DIAdem can execute the calculation. DIAdem displays the test result as a message. |
|  | Validation Unsuccessful |  |
|  | Run | Executes the calculation. If DIAdem generates result channels, the channels are in the Data Portal. |
|  | Run and Store in Calculation Channel | Runs the calculation and stores the result in a calculation channel. |
| Calculation Definition |  |  |
|  | Name | Specifies the calculation name. |
|  | Formula | Specifies the calculation rule. Define a formula as follows:Output = Input1 Operator Input2Example: Result = Input1 * Input2In a formula you can only use the inputs and outputs that reference values and channels. You must define the formula in one line. To define a multi-line calculation rule, click Script and create a calculation script. |
|  | View | Displays the equation template in mathematical syntax.DIAdem identifies the operands and operators which cannot be interpreted with a red frame. |
|  | Quantity-based | Specifies that DIAdem executes the calculation quantity-based. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
|  | Result unit | Specifies the unit of the result. |
|  | Input Help for Unit Symbols | Opens the dialog box where you can select a new unit and a new unit symbol. |
| Toolbars for Inputs and Outputs |  |  |
|  | Add Input/Output | Creates a new entry in the list of inputs or outputs. |
|  | Delete Input/Output | Deletes the selected input or output. |
|  | Move Input/Output Up | Moves the selected input or output up one position. |
|  | Move Input/Output Down | Moves the selected input or output down one position. |
| Inputs |  |  |
|  | Name | Specifies the name of the input. You use the name of an input as a symbol in the formula. |
|  | Dependency | Contains a message as to whether the input is dependent on an output from another calculation. Click into the table entry to open the dialog box where you define the dependency of an input on an output of another calculation. |
|  | Optional Input | Specifies that DIAdem uses the input when validating the calculation rule. Click into this table entry to flag the input as optional. |
|  | Data type | Specifies the data type of the input. An input can refer to a value, a channel, or a channel list. |
|  | Reference | Contains details on the value, the channel, or the channel list that the input refers to. Click the table entry to open the dialog box where you define the Value reference or the Channel list reference of the input. |
| Outputs |  |  |
|  | Name | Specifies the name of the output. You use the name of an output as a symbol in the formula. |
|  | Optional Output | Specifies that DIAdem uses the output when validating the calculation rule. Click into this table entry to flag the output as optional. |
|  | Data type | Specifies the data type of the output. An output can refer to a value, a channel, or a channel list. |
|  | Reference | Contains details on the value, the channel, or the channel list that the output refers to. Click the table entry to open the dialog box where you define the Value reference or the Channel list reference of the output. |
|  | Message | Indicates whether DIAdem can execute the calculation. |

#### Further Settings

[Calculation Manager](../calc_formula_dlg/dlgcm_calculationset_dialog.htm) | [Run Calculation](../calc_formula_dlg/dlgcm_executecalculations_dialog.htm) | Edit Calculation»Calculation | [Edit Calculation»Script](../calc_formula_dlg/dlgcm_script_dialog.htm) | [Add Calculation Group](../calc_formula_dlg/dlgcm_calculationgroup_dialog.htm) | [Debug Dependent Pre-Calculations](../calc_formula_dlg/dlgcm_checkpredependencies_dialog.htm) | [Debug Dependent Post-Calculations](../calc_formula_dlg/dlgcm_checkpostdependencies_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_geo_dlg/dlgchnabsolutehumidity_dialog.htm language=enus -->
## TOPIC 00373: Absolute Humidity

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_geo_dlg/dlgchnabsolutehumidity_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_geo_dlg/dlgchnabsolutehumidity_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Geo Functions](../calc_geo_dlg/calc_geo_overview.htm) > Absolute Humidity

Absolute Humidity

Use this dialog box to calculate the absolute humidity in g/m³ from the relative humidity and the temperature.

If the relative humidity is 100%, you can no longer draw confident conclusions on the absolute humidity, since the air is then supersaturated. DIAdem then calculates the minimum humidity required to reach 100% humidity.

#### Settings

| Relative Humidity | Specifies the data channel with the relative humidity values in %. |
| --- | --- |
| Temperature | Specifies the data channel containing the temperature values. If you do not calculate in the quantity-based mode, DIAdem assumes that the temperatures are in Kelvin. If you calculate in the quantity-based mode, DIAdem uses the channel unit. |

|  | If you want to use waveform channels in this dialog box, follow Rule 1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem creates a result channel AbsoluteHumidity in the default group with the absolute humidity values.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnAbsoluteHumidity")

[ChnAbsoluteHumidity](../../comoff/chnabsolutehumidity.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_graphs_dlg/calc_graphs_overview.htm language=enus -->
## TOPIC 00374: Curve Fitting

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_graphs_dlg/calc_graphs_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_graphs_dlg/calc_graphs_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > Curve Fitting

Curve Fitting

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes where you, for example, smooth curves, use regression or approximations functions on curves, or map signals onto a new x-value range.

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_graphs_dlg/chngaussfit_dialog.htm language=enus -->
## TOPIC 00375: Gaussian Curve Fitting

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_graphs_dlg/chngaussfit_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_graphs_dlg/chngaussfit_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Curve Fitting](../calc_graphs_dlg/calc_graphs_overview.htm) > Gaussian Curve Fitting

Gaussian Curve Fitting

Use this dialog box to approximate a signal with a Gaussian curve. DIAdem uses the least square method, the least absolute residual method, or the bisquare method to calculate the fitting.

#### Settings

|  | X-channel | Specifies the data channel containing the x-values of the signal. |
| --- | --- | --- |
|  | Y-channel | Specifies the data channel containing the y-values of the signal. |
|  | Weighting channel | Specifies whether DIAdem weights the y-values in a Gaussian curve fitting. |
|  | Setup Coefficients: Amplitude | Receives the amplitude of the Gaussian curve fitting. |
|  | Setup Coefficient: Center | Receives the center of the Gaussian curve fitting. |
|  | Setup Coefficient: Standard deviation | Receives the standard deviation of the Gaussian curve fitting. |
|  | Residue | Specifies the residue or the weighted mean error of a Gaussian curve fitting. |

|  | Note Because Gaussian curve fitting is an iterative method, the quality of the Gaussian curve depends on the initialization of the setup coefficients Amplitude, Center, and Standard deviation. |
| --- | --- |

#### Setup Functions

|  | Tolerance | Specifies the tolerance which determines when the iterative curve fitting of the amplitude, center, and standard deviation ends for the bisquare method. If the relative difference of the residual undershoots the tolerance in two successive cycles, the curve fitting stops. If the tolerance is 0, DIAdem sets the tolerance to 0.0001. |
| --- | --- | --- |
|  | Algorithm for curve fitting | Specifies the algorithm for Gaussian curve fitting. |
|  | Initialization of setup coefficients | Specifies the start values for the amplitude, the center, and the standard deviation of the Gaussian curve fitting. |

#### Evaluation Points

|  | Create evaluation points | Specifies which method DIAdem uses to generate the interpolation point channel. |
| --- | --- | --- |
|  | Partition complete area: Number of partitions | Specifies the number of values in a new data channel. |
|  | Partition intervals: Number of partitions | Specifies the number of equidistant sections in each interval of the x-range. |
|  | Use channel: Channel | Specifies the interpolation channel. |
|  | Store result in original channels | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

#### Result Transfer

|  | Transfer results to clipboard | Specifies whether DIAdem copies the coefficients to the clipboard. If you copy the results to the clipboard, you can then paste the results in a report. |
| --- | --- | --- |
|  | Transfer as values / Transfer as variable reference | Specifies whether DIAdem copies the results to the clipboard as a value or as the vector variable GaussFitInitCoef(). The advantage of a variable reference is that the variables transferred from the clipboard to the report always display the values of the last approximation after a refresh. DIAdem also saves the result in the GaussFitFctStr variable. |
|  | Numeric format | Specifies the format for the coefficients. |
|  | Format Numbers | Opens the dialog box where you select or enter a format specification. |

|  | If you want to use waveform channels in this dialog, note the following: If you use a channel to generate the evaluation points, rule 2.2 on calculating with waveform channels applies. Otherwise, rule 2.1 applies. |
| --- | --- |

#### Result

If an existing data channel specifies the data points, DIAdem generates one result channel. If the data points are generated, DIAdem generates two result channels. These result channels reconstruct a given x/y-channel pair, or recalculate it with a new x-basis.

DIAdem calculates the amplitude, the center, and the standard deviation of the Gaussian curve and saves them in the variables [GaussFitAmplitude](../../varoff/gaussfitamplitude.htm), [GaussFitCenter](../../varoff/gaussfitcenter.htm), and [GaussFitStdDev](../../varoff/gaussfitstddev.htm). DIAdem saves the residual or the weighted mean error of a Gaussian curve fitting in the [GaussFitResidue](../../varoff/gaussfitresidue.htm) variable. If you select the Least Absolute Residual algorithm, the variable receives the absolute error of the weighted mean. If you use other algorithms, the variable does not receive an absolute value.

|  | Refer to the Help page Gaussian Curve Fitting for further information. |
| --- | --- |

|  |  | Note DIAdem stores the calculated coefficients and the residual in the following custom properties of the result channels: Result~GaussFit~Amplitude , Result~GaussFit~Center , Result~GaussFit~StandardDeviation, and Result~GaussFit~Residue. |
| --- | --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv& "AnaChnGaussFit")

[ChnGaussFitXY](../../comoff/chngaussfitxy.htm)

[ChnGaussFitXYWeighted](../../comoff/chngaussfitxyweighted.htm)

[ChnGaussFitY](../../comoff/chngaussfity.htm)

[ChnGaussFitYWeighted](../../comoff/chngaussfityweighted.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_graphs_dlg/chngenlsfit_dialog.htm language=enus -->
## TOPIC 00376: General LS Linear Fitting

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_graphs_dlg/chngenlsfit_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_graphs_dlg/chngenlsfit_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Curve Fitting](../calc_graphs_dlg/calc_graphs_overview.htm) > General LS Linear Fitting

General LS Linear Fitting

In this dialog box you use k-dimensional linear curve values and k-dimensional coefficients for the linear adaptation of a curve. DIAdem uses the least square method to best fit a k-dimensional curve.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Y-Channel | Specifies the data channel containing the y-values of the signal. |
| --- | --- |
| Matrix | Specifies the data channels for the matrix H. This is the matrix that corresponds to the formula and that DIAdem uses to fit the set {X, Y}. |
| Weighting channel | Specifies whether DIAdem weights the y-values of the general LS linear fitting. |
| Algorithm for curve fitting | Specifies the algorithm for the general LS linear fitting. |
| Create matrix of covariances | Specifies whether DIAdem generates the covariance matrix for a general LS linear fitting. |
| Mean squared error | Specifies the mean square error. |

|  | If you want to use waveform channels in this dialog, note the following: If you use a channel to generate the evaluation points, rule 2.2 on calculating with waveform channels applies. Otherwise, rule 2.1 applies. |
| --- | --- |

#### Result

If you select this setting, DIAdem calculates a result channel with the coefficients and a covariance matrix. The number of calculated coefficients is the same as the number of columns of the matrix H. The number of columns is the same as the number of specified channels. DIAdem saves the mean squared error in the [GenLSFitMSE](../../varoff/genlsfitmse.htm) variable.

|  | Note DIAdem saves the mean squared error in the following custom properties of the result channels:Result~GeneralLSLinearFit~MSE. |
| --- | --- |

|  | Refer to the Help page General LS Linear Fitting for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv& "AnaChnGenLSFit")

[ChnGenLSFit](../../comoff/chngenlsfit.htm)

[ChnGenLSFitWeighted](../../comoff/chngenlsfitweighted.htm)

#### Examples

[Evaluating a Shock Response Spectrum](../../exploff/examples/expl_shockresponsespectrum.htm) | [Hysteresis Analysis](../../exploff/examples/expl_analyzehysteresis.htm) | [Linearization via the Values Table](../../exploff/examples/expl_linviatable.htm) | [Non-Linear Curve Fitting](../../exploff/examples/spectralline.htm) | [Optimized Heating Control](../../exploff/examples/expl_domesticengineering.htm) | [Savitzky-Golay Filter](../../exploff/examples/exp_savitzky-golay.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_graphs_dlg/chnnonlinearfit_dialog.htm language=enus -->
## TOPIC 00377: Non-Linear Curve Fitting

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_graphs_dlg/chnnonlinearfit_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_graphs_dlg/chnnonlinearfit_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Curve Fitting](../calc_graphs_dlg/calc_graphs_overview.htm) > Non-Linear Curve Fitting

Non-Linear Curve Fitting

Use this dialog box to approximate a signal with a non-linear y = f(x,a) type function. DIAdem uses the Levenberg-Marquardt algorithm to calculate the coefficients a which minimize the error squares of the input pairs.

#### Settings

|  | X-channel | Specifies the data channel containing the x-values of the signal. |
| --- | --- | --- |
|  | Y-Channel | Specifies the data channel containing the y-values of the signal. |
|  | Weighting channel | Specifies whether DIAdem weights the y-values in a non-linear curve fitting. |
|  | Formula of setup function | Specifies the formula string of the setup function for the non-linear curve fitting in VBS syntax. DIAdem can recognize the coefficients independently. You cannot use the characters e and pi as coefficients because the characters are DIAdem constants for the Eulerian number and the circle number. |
|  | Setup Coefficients | Receives the coefficients of a non-linear curve fitting setup function. |
|  | Mean squared error | Specifies the mean square error of the non-linear curve fitting. |

#### Setup Functions

|  | Maximum number of iterations | Specifies the maximum number of the fitting routine iterations of a non-linear curve fitting. If the number of iterations exceeds this value, the fitting process stops. |
| --- | --- | --- |
|  | Independent variable | Specifies the name of the independent variable in the setup function of a non-linear curve fitting. |
|  | Create matrix of covariances | Specifies whether DIAdem generates the covariance matrix for a non-linear curve fitting. |
|  | Initialization of setup coefficients | Specifies the initially received values for the coefficients of the setup function of a non-linear curve fitting. DIAdem automatically specifies the names of the setup coefficients and assigns the value 1 to the coefficients. You can change this initialization value. |

|  | Note Because the non-linear curve fitting is an iterative method, the initialization of the setup coefficients determines the quality of the fitted curve. |
| --- | --- |

#### Evaluation Points

|  | Create evaluation points | Specifies which method DIAdem uses to generate the interpolation point channel.Depending on which method you choose, specify one of the following parameters: |
| --- | --- | --- |
|  | Partition complete area: Number of partitions | Specifies the number of equidistant sections in the entire x-range. |
|  | Partition intervals: Number of partitions | Specifies the number of equidistant sections in each interval of the x-range. |
|  | Use channel: Channel | Specifies the data channel containing the values that return the interpolation points. |
|  | Store result in original channels | Overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |

#### Result Transfer

|  | Transfer results to clipboard | Specifies whether DIAdem copies the coefficients to the clipboard. If you copy the results to the clipboard, you can then paste the results in a report. |
| --- | --- | --- |
|  | Transfer as values / Transfer as variable reference | Specifies whether DIAdem copies the results to the clipboard as a value or as the vector variable NonLinearFitCoef(). The advantage of a variable reference is that the variables transferred from the clipboard to the report always display the values of the last approximation after a refresh. |
|  | Numeric format | Specifies the format for the coefficients. |
|  | Format Numbers | Opens the dialog box where you select or enter a format specification. |

|  | If you want to use waveform channels in this dialog, note the following: If you use a channel to generate the evaluation points, rule 2.2 on calculating with waveform channels applies. Otherwise, rule 2.1 applies. |
| --- | --- |

#### Result

If an existing data channel specifies the data points, DIAdem generates one result channel. If the data points are generated, DIAdem generates two result channels.

The calculated approximation function consists of a linear combination of single, independent function terms. DIAdem calculates the coefficients of the setup function and stores them in the [NonLinearFitCoef()](../../varoff/nonlinearfitcoef.htm) vector variable. If the specified coefficients have extremely different orders of magnitude, for example 1E+4 and 1E-6, the setup functions were not well selected.

DIAdem calculates the mean squared error of the non-linear curve fitting and saves it in the [NonLinearFitMSE](../../varoff/nonlinearfitmse.htm) variable.

|  | Refer to the Help page Non-Linear Curve Fitting for further information on mathematics. |
| --- | --- |

|  |  | Note DIAdem stores the calculated coefficients and the mean squared error in the following custom properties of the result channels: Result~NonLinearFit~Coefficient, Result~NonLinearFit~CoefficientName, Result~NonLinearFit~ModelFunction, and Result~NonLinearFit~MSE. DIAdem adds to the custom properties Result~NonLinearFit~Coefficient and Result~NonLinearFit~CoefficientName a number corresponding to the number of the coefficient. |
| --- | --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv& "AnaChnNonLinearFit")

[ChnNonLinearFitXY](../../comoff/chnnonlinearfitxy.htm)

[ChnNonLinearFitXYWeighted](../../comoff/chnnonlinearfitxyweighted.htm)

[ChnNonLinearFitY](../../comoff/chnnonlinearfity.htm)

[ChnNonLinearFitYWeighted](../../comoff/chnnonlinearfityweighted.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_graphs_dlg/dlgchnakima_dialog.htm language=enus -->
## TOPIC 00378: Akima Subsplines

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_graphs_dlg/dlgchnakima_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_graphs_dlg/dlgchnakima_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Curve Fitting](../calc_graphs_dlg/calc_graphs_overview.htm) > Akima Subsplines

Akima Subsplines

Use this dialog box to approximate signals with an Akima subspline. Use Akima subsplines to approximate curves that are not smooth, which means that they are not continuously differentiable.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| X-channel | Specifies the data channel that contains the x-values of the signal. |
| --- | --- |
| Y-Channel | Specifies the data channel that contains the y-values of the signal. |
| Type of curve | Specifies whether an interpolating or an approximating curve type is used. |
| Neighboring points included | Specifies the number of neighboring values that DIAdem includes in the approximation of the interpolation points. |
| Weighting factor for the neighboring points | Specifies the influence of the neighboring interpolation points when DIAdem approximates the interpolation points. |
| Compensation range as a %: | Specifies the tolerance (as a percentage) by which the approximated interpolation point may deviate from the original interpolation point. |
| Create evaluation points | Specifies which method DIAdem uses to generate the interpolation point channel.Depending on which method you choose, specify one of the following parameters: |
| Partition complete area: Number of partitions | Specifies the number of equidistant sections in the entire x-range. |
| Partition intervals: Number of partitions | Specifies the number of equidistant sections in each interval of the x-range. |
| Use channel: Channel | Specifies the data channel containing the values that return the interpolation points. |
| Store result in original channel | Overwrites the values of the input channels. Do not select this setting if you want to continue using the input channels. |

|  | Note The values in the x-channel must be strictly monotone increasing. |
| --- | --- |

|  | If you want to use waveform channels in this dialog, note the following: If you use a channel to generate the evaluation points, rule 2.2 on calculating with waveform channels applies. Otherwise, rule 2.1 applies. |
| --- | --- |

#### Result

If an existing data channel specifies the data points, DIAdem generates one result channel. If the interpolation points are regenerated, DIAdem generates two result channels. These result channels reconstruct a given x/y-channel pair, or recalculate it with a new x-basis.

|  | Refer to the Help page Akima Subsplines for mathematical details. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv& "AnaChnAkimaCalc")

[ChnAkimaXYCalc](../../comoff/chnakimaxycalc.htm)

[ChnAkimaYCalc](../../comoff/chnakimaycalc.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_signal_dlg/dlgchnfullspectrumfft_dialog.htm language=enus -->
## TOPIC 00379: Full Spectrum FFT

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_signal_dlg/dlgchnfullspectrumfft_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_signal_dlg/dlgchnfullspectrumfft_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Signal Analysis](../calc_signal_dlg/calc_signalanalysis_overview.htm) > Full Spectrum FFT

Full Spectrum FFT

Use this dialog box to diagnose damage on rotating shafts. Synchronous and equidistant sampling was executed on the signals of two vibration sensors which are positioned perpendicular to each other. First, single spectra are calculated from the two vibration signals and then connected to a full spectrum FFT.

#### Settings

|  | Time channel | Specifies the data channel with the common time values of the input signals. |
| --- | --- | --- |
|  | Input channels 1 | Displays the data channels with the signals of the first sensor. The input channels must not contain NoValues. |
|  | Select Channels | Opens the channel selection list. The number of first input channels must be the same as the number of second input channels. |
|  | Input channels 2 | Displays the data channels with the signals of the second sensor. The input channels must not contain NoValues. |
|  | Select Channels | Opens the channel selection list. The number of first input channels must be the same as the number of second input channels. |
| Window Functions |  |  |
|  | Window type | Specifies the window function for the FFT. You can select: Rectangle, Hanning, Hamming, Blackman, FlatTop. |
|  | Amplitude attenuation correction | Specifies whether DIAdem corrects the damping effect of the window function on the amplitude. You can select either periodic or random correction. |
| Time IntervalsIf you select exactly one input channel, you can split the calculation into intervals. |  |  |
|  | Include all values | Specifies that DIAdem uses all measured values in the calculation. |
|  | Number of intervals | Specifies that DIAdem divides the input channels into a specified number of equidistant intervals and calculates an individual result for each interval. The calculation ignores surplus values. |
|  | Number | Specifies the number of intervals. |
|  | Length of the intervals | Specifies that DIAdem divides the input channels into intervals of a specified number length and calculates an individual result for each interval. The calculation ignores surplus values. |
|  | Length | Specifies the number of values in an interval. |
|  |  |  |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. If you specify a time channel although the input channels are waveform channels, the sampling rate is specified from the time channel. |
| --- | --- |

#### Result

DIAdem generates for every time interval and for every input channel pair one result channel with the calculated amplitudes.

First, the bias is removed from both input channels with AC/DC coupling in a full spectrum FFT calculation. The amplitudes of the power spectrum are calculated from the AC component with the FFT with a time channel. Additionally the phase of the cross spectrum is calculated from both input channels. The full spectrum FFT is established by further connections of both amplitudes and the phase.

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnFullSpectrumFFT")

[ChnFullSpectrum](../../comoff/chnfullspectrum.htm)

#### Procedures

[Examining Measurement Signals in the Frequency Domain](../../procmaths/procmaths/mathsproc_fft.htm)

#### Examples

[AC/DC Coupling](../../exploff/examples/expl_ac-dccoupling.htm) | [Adapted DIAdem Functions](../../exploff/examples/expl_script_av15.htm) | [Calculate Characteristics of an Oscillation](../../exploff/examples/expl_wavecharacteristics.htm) | [Communicating with MATLAB](../../exploff/examples/exp_interfaces_ab4.htm) | [Frequency Weighting (A-, B-, C-Filtering)](../../exploff/examples/expl_abcfiltering.htm) | [Hysteresis Analysis](../../exploff/examples/expl_analyzehysteresis.htm) | [Optimized Heating Control](../../exploff/examples/expl_domesticengineering.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_signal_dlg/dlgchninversefft_dialog.htm language=enus -->
## TOPIC 00380: Inverse FFT

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_signal_dlg/dlgchninversefft_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_signal_dlg/dlgchninversefft_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Signal Analysis](../calc_signal_dlg/calc_signalanalysis_overview.htm) > Inverse FFT

Inverse FFT

Use this dialog box to run an inverse fast Fourier transform (FFT). DIAdem transforms a signal from the frequency domain into the time domain.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Frequency | Specifies the data channel containing the frequencies of the complex signal. The values of the data channel must be strictly monotonic increasing. |
| --- | --- |
| Real part | Specifies the data channel containing the real part of the signal. The data channel must not contain NoValues. |
| Imaginary part | Specifies the data channel containing the imaginary part of the signal. The data channel must not contain NoValues. |
| Phase shift | Specifies the phase offset for the inverse FFT. The setting 90 is the Hilbert transform. The setting -90 is the inverse Hilbert transform. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.1 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates two result channels. The first result channel contains the time. The second result channel contains the amplitude. The length of the result channels of the inverse FFT is twice as long as the length of the frequency channels.

|  | Note If you specify in the compatibility dialog box that DIAdem calculates the FFT to powers with a base of two, DIAdem uses older algorithms. DIAdem does not necessarily use all the measured data. If the length of the input channel is not a power of two, DIAdem uses the next power of two down. |
| --- | --- |

|  | Refer to the Help page Fourier Transform for further information. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnInverseFFT")

[ChnInverseFFT](../../comoff/chninversefft.htm)

#### Procedures

[Examining Measurement Signals in the Frequency Domain](../../procmaths/procmaths/mathsproc_fft.htm)

#### Examples

[AC/DC Coupling](../../exploff/examples/expl_ac-dccoupling.htm) | [Adapted DIAdem Functions](../../exploff/examples/expl_script_av15.htm) | [Calculate Characteristics of an Oscillation](../../exploff/examples/expl_wavecharacteristics.htm) | [Communicating with MATLAB](../../exploff/examples/exp_interfaces_ab4.htm) | [Frequency Weighting (A-, B-, C-Filtering)](../../exploff/examples/expl_abcfiltering.htm) | [Hysteresis Analysis](../../exploff/examples/expl_analyzehysteresis.htm) | [Optimized Heating Control](../../exploff/examples/expl_domesticengineering.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_signal_dlg/dlgchnordanafreq_dialog.htm language=enus -->
## TOPIC 00381: Order Analysis (Frequency Domain)

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_signal_dlg/dlgchnordanafreq_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_signal_dlg/dlgchnordanafreq_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Signal Analysis](../calc_signal_dlg/calc_signalanalysis_overview.htm) > Order Analysis (Frequency Domain)

Order Analysis (Frequency Domain)

Use this dialog box to run an order and frequency analysis in the frequency domain. DIAdem checks rpm-related values in one or more orders. Order analysis in the frequency domain is based on the calculation of rpm-related FFTs.

|  | Open Dialog Box in DIAdem |
| --- | --- |

#### Settings

| Time channel | Specifies the data channel that contains the time values of the signal in seconds. |
| --- | --- |
| Signal channel | Specifies the data channel that contains the amplitude values of the signal. |
| RPM channel | Specifies the data channel with the rpm values of the signal. |

#### Analysis Method

| Analysis method | Specifies whether DIAdem calculates frequencies or orders. |
| --- | --- |
| Maximum order | Specifies the maximum possible order. |
| Recalculate filter when RPM changes by | Specifies the change in the rpm that triggers a recalculation of the filter coefficients. |
| Evaluation type | Specifies how DIAdem evaluates the results. |
| The reference value for 0 dB | Specifies the reference value in the result evaluation. |

#### Parameters

| Start value | Specifies the first rpm value at which DIAdem runs the order/frequency calculation. |
| --- | --- |
| End value | Specifies the last rpm value at which DIAdem runs the order/frequency calculation. |
| Step width | Specifies the step width when generating revs. |
| FFT length | Specifies the number of values for an FFT. |
| Amplitude | Specifies the type of amplitude calculation. |
| Third/octave calculation | Specifies the analysis method. |
| Set Parameters | Sets the dialog box parameters automatically. |

|  | Note The rpm intervals must be equidistant. Sufficient values also have to exist to run an FFT. If not, DIAdem reduces the end value first, until only one step is possible, and then DIAdem reduces the FFT length to make a calculation possible. |
| --- | --- |

#### FFT Window

| Window type | Specifies the window function. |
| --- | --- |
| Parameters of the window function | Specifies the parameters for parameter-related window functions. |
| Channel | Specifies the data channel that contains the values of a user-defined window function. |
| Amplitude attenuation correction | Specifies whether and how DIAdem corrects the damping effect of the window function on the amplitude. |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.2 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates a result matrix. The first result channel contains frequency values or orders, and the second result channel contains the rpm intervals. The other result channels contain the matrix values for the order analysis.

|  | Refer to the Help page Order Analysis for mathematical details. |
| --- | --- |

|  | To calculate quantity-based in DIAdem, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. |
| --- | --- |

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnOrdAFCalc")

[ChnOrdAFCalc](../../comoff/chnordafcalc.htm)

<!--NI_TOPIC bundle=diadem path=dlgmaths/calc_signal_dlg/dlgchnshaftcenterline_dialog.htm language=enus -->
## TOPIC 00382: Shaft Centerline

- bundle_id: `diadem`
- source_path: `dlgmaths/calc_signal_dlg/dlgchnshaftcenterline_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgmaths/calc_signal_dlg/dlgchnshaftcenterline_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem ANALYSIS](../analysisdlgs_overview.htm) > [Signal Analysis](../calc_signal_dlg/calc_signalanalysis_overview.htm) > Shaft Centerline

Shaft Centerline

Use this dialog box to calculate the movement of a rotating shaft in the bearing box. The measurement values of two sensors at the shaft are averaged in order to specify how the position of the shaft center changes over several revolutions. The shaft centerline is the path of the averaged shaft center point.

#### Settings

|  | X-channels | Displays the selected data channels with the x-values of the measured revolutions or orbits. |
| --- | --- | --- |
|  | Select Channels | Opens the channel selection list. |
|  | Y-channels | Displays the selected data channels with the y-values of the measured revolutions or orbits. |
|  | Select Channels | Opens the channel selection list. |
| Reference Point |  |  |
|  | X-value | Specifies the x-margin to the shaft centerline. |
|  | Y-value | Specifies the y-margin to the shaft centerline. |
| Time Intervals |  |  |
|  | Include all values | Specifies that DIAdem uses all measured values for the calculation. |
|  | Number of intervals | Specifies that DIAdem divides the input channel in intervals of the same width in order to calculate these intervals one after the other. |
|  | Number | Specifies the number of intervals. |
|  | Length of the intervals | Specifies that DIAdem uses a certain number of consecutive values for the calculation. |
|  | Length | Specifies the number of values in an interval. |
|  |  |  |

|  | If you want to use waveform channels in this dialog box, follow Rule 2.3 for Calculating with Waveform Channels. |
| --- | --- |

#### Result

DIAdem generates the result channels ShaftCenterlineX and ShaftCenterlineY. The first result channel contains the x-values and the second result channel the y-values of the movement of the shaft center in the bearing.

#### Script Call

Call [SUDDlgShow](../../comoff/suddlgshow.htm)("Main", ResourceDrv & "AnaChnShaftCenterline")

[ChnShaftCenterline](../../comoff/chnshaftcenterline.htm)

#### Procedures

[Examining Measurement Signals in the Frequency Domain](../../procmaths/procmaths/mathsproc_fft.htm)

#### Examples

[AC/DC Coupling](../../exploff/examples/expl_ac-dccoupling.htm) | [Adapted DIAdem Functions](../../exploff/examples/expl_script_av15.htm) | [Calculate Characteristics of an Oscillation](../../exploff/examples/expl_wavecharacteristics.htm) | [Communicating with MATLAB](../../exploff/examples/exp_interfaces_ab4.htm) | [Frequency Weighting (A-, B-, C-Filtering)](../../exploff/examples/expl_abcfiltering.htm) | [Hysteresis Analysis](../../exploff/examples/expl_analyzehysteresis.htm) | [Optimized Heating Control](../../exploff/examples/expl_domesticengineering.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/excelimportwizard_4_dialog.htm language=enus -->
## TOPIC 00383: Import Wizard, Step 4 of 4

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/excelimportwizard_4_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/excelimportwizard_4_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Excel Files](../dlgnavigator/navi_excelfiles_overview.htm) > [Import Wizard for Spreadsheet Files](../dlgnavigator/excelimportwizard_overview.htm) > Import Wizard, Step 4 of 4

Import Wizard, Step 4 of 4

Use this dialog box to specify the channel values. The numbered table rows correspond to the rows that you specified as a Data type in step 1 of the Import Wizard. DIAdem interprets the individual table columns as channels.

You can resize the dialog box in order to enlarge the visible table area of the preview. You can move the separation lines to change the width of the table columns.

#### Settings

| Channel name | Displays, in the first title bar of the table, the text that you assigned the Name property to in step 3 of the Import Wizard. |
| --- | --- |
| Data type | Specifies which data type DIAdem assigns to this channel. Select the data type in the second title bar of the table. DIAdem can read in Numeric, Time, or Text type channels. If you assign the setting Automatic to a column, DIAdem specifies the data type. If you assign the setting Ignore to a column, DIAdem does not use this column. |

|  | Note Click Load and, when prompted, click Yes to generate a DataPlugin from your settings in a next Step, and to register the DataPlugin in DIAdem and in DataFinder. |
| --- | --- |

#### Further Settings

[Introduction](../dlgnavigator/excelimportwizard_overview.htm) | [Import Wizard, Step 1 of 4](../dlgnavigator/excelimportwizard_1_dialog.htm)| [Import Wizard, Step 2 of 4](../dlgnavigator/excelimportwizard_2_dialog.htm) |[Import Wizard, Step 3 of 4](../dlgnavigator/excelimportwizard_3_dialog.htm)| Import Wizard, Step 4 of 4

#### Procedures

[Importing ASCII Files with the DataPlugin Wizard](../../procnavigator/procnavigator/procnavigator_dataplugin.htm) | [Registering DataPlugins](../../procshell/procshell/procshell_register_dataplugins.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/excelimportwizard_overview.htm language=enus -->
## TOPIC 00384: Import Wizard for Spreadsheet Files

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/excelimportwizard_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/excelimportwizard_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Excel Files](../dlgnavigator/navi_excelfiles_overview.htm) > Import Wizard for Spreadsheet Files

Import Wizard for Spreadsheet Files

Use the Import Wizard to interactively read a file into a spreadsheet.

1. In the first step you specify the file structure.
2. In the second step you specify the group properties to be read in.
3. In the third step you specify the channel properties to be read in.
4. In the fourth step you specify the channel values to be read in.

|  | Note To open the Import Wizard in DIAdem NAVIGATOR, click File»Open, and select Import Wizard Excel(*.ods,*.xls,*.xlsx,*.xlsm) as the file type. |
| --- | --- |

|  | Note Use the Excel DataPlugin Wizard to interactively create a new DataPlugin that DIAdem can use to read in or register similar spreadsheet files. Select File»Excel DataPlugin Wizard in DIAdem NAVIGATOR, or select Open With from the context menu of a file to open the Excel DataPlugin Wizard. |
| --- | --- |

#### Further Settings

Introduction | [Import Wizard, Step 1 of 4](../dlgnavigator/excelimportwizard_1_dialog.htm) | [Import Wizard, Step 2 of 4](../dlgnavigator/excelimportwizard_2_dialog.htm) | [Import Wizard, Step 3 of 4](../dlgnavigator/excelimportwizard_3_dialog.htm) | [Import Wizard Step 4 of 4](../dlgnavigator/excelimportwizard_4_dialog.htm)

#### Procedures

[Importing ASCII Files with the DataPlugin Wizard](../../procnavigator/procnavigator/procnavigator_dataplugin.htm) | [Registering DataPlugins](../../procshell/procshell/procshell_register_dataplugins.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/importwizard_4_dialog.htm language=enus -->
## TOPIC 00385: Import Wizard, Step 4 of 4

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/importwizard_4_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/importwizard_4_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Text Files](../dlgnavigator/navi_textfiles_overview.htm) > [Import Wizard for Text Files](../dlgnavigator/importwizard_overview.htm) > Import Wizard, Step 4 of 4

Import Wizard, Step 4 of 4

Use this dialog box to specify the channel values. The numbered table rows correspond to the rows that you specified as a Data type in step 1 of the DataPlugin Wizard. DIAdem interprets the individual table columns as channels.

You can resize the dialog box in order to enlarge the visible table area of the preview. You can use the narrow row above the table header to change the width of table columns. The light gray preview in the right area of the table displays the texts DIAdem will load according to your settings. If you move the cursor over the preview, DIAdem displays, in the tooltip of a cell, the value in the text file.

#### Settings

| Column separators | Specifies the characters that separate the columns in the text file. You can select tabulators, semicolons, commas, blanks, or user-defined characters as delimiters. |
| --- | --- |
| Decimal symbol | Specifies the decimal symbol for numeric values. |
| Thousands symbol | Specifies the thousands symbol for numeric values, which DIAdem ignores when reading. |
| Exponential character | Specifies the exponential character for numeric values. |
| Text qualifier | Specifies the qualifier for texts.DIAdem does not interpret text that these characters enclose. DIAdem accepts the text as an expression. |
| Truncate space | Specifies whether DIAdem truncates blanks and tabulators in texts. |
| NoValue substitute | Specifies the text that DIAdem interprets as NoValue for numeric values. |
| Time | Specifies the format of the time values. You can select a predefined format and customize the format. Use Y for year, M for month, D for day, h for hour, m for minute, s for second, f for a fraction of a second, and pp for AM/PM. |
| Channel name | Displays in the first title bar of the table the text that you assigned the Name property to in step 3 of the DataPlugin Wizard. |
| Data type | Specifies which data type DIAdem assigns to this channel. Select the data type in the second title bar of the table. DIAdem can read in Numeric, Time, or Text type channels. If you assign the setting Ignore to a column, DIAdem does not use this column. |

|  | Note The DataPlugin parameters that you set in this dialog box, apply to the template text file. If a file loaded later with this DataPlugin contains further columns with values, DIAdem loads these columns as numeric channels. |
| --- | --- |

#### Further Settings

[Introduction](../dlgnavigator/importwizard_overview.htm) | [Import Wizard, Step 1 of 4](../dlgnavigator/importwizard_1_dialog.htm)| [Import Wizard, Step 2 of 4](../dlgnavigator/importwizard_2_dialog.htm) |[Import Wizard, Step 3 of 4](../dlgnavigator/importwizard_3_dialog.htm)| Import Wizard, Step 4 of 4

#### Procedures

[Importing ASCII Files with the DataPlugin Wizard](../../procnavigator/procnavigator/procnavigator_dataplugin.htm) | [Registering DataPlugins](../../procshell/procshell/procshell_register_dataplugins.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/importwizard_overview.htm language=enus -->
## TOPIC 00386: Import Wizard for Text Files

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/importwizard_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/importwizard_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Text Files](../dlgnavigator/navi_textfiles_overview.htm) > Import Wizard for Text Files

Import Wizard for Text Files

Use the Import Wizard to interactively read in a text file.

1. In the first step you specify the text file structure.
2. In the second step you specify the group properties to be read in.
3. In the third step you specify the channel properties to be read in.
4. In the fourth step you specify the channel values to be read in.

|  | Note To open the Import Wizard in DIAdem NAVIGATOR, click File»Open, and select Import Wizard Text(*.*) as the file type. |
| --- | --- |

|  | Note Use the Text DataPlugin Wizard to interactively create a new DataPlugin that DIAdem can use to read in or register similar text files. Select File»Text DataPlugin Wizard in DIAdem NAVIGATOR or select Open With from the context menu of a file to open the DataPlugin Wizard. |
| --- | --- |

#### Further Settings

Introduction | [Import Wizard, Step 1 of 4](../dlgnavigator/importwizard_1_dialog.htm) | [Import Wizard, Step 2 of 4](../dlgnavigator/importwizard_2_dialog.htm) | [Import Wizard, Step 3 of 4](../dlgnavigator/importwizard_3_dialog.htm) | [Import Wizard Step 4 of 4](../dlgnavigator/importwizard_4_dialog.htm)

#### Procedures

[Importing ASCII Files with the DataPlugin Wizard](../../procnavigator/procnavigator/procnavigator_dataplugin.htm) | [Registering DataPlugins](../../procshell/procshell/procshell_register_dataplugins.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_browsepath_config_dialog.htm language=enus -->
## TOPIC 00387: Browse Settings

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_browsepath_config_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_browsepath_config_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > [Search: Settings](../dlgnavigator/navi_dssearchdata_dlg_overview.htm) > Browse Settings

Browse Settings

Use this dialog to specify the entities of a data store that DIAdem displays in the [Data Browser](../dlgnavigator/navi_datastore_tree.htm) depending on the given application model.

|  | Note If you use a DataFinder instance which is declared an ASAM ODS Server, you cannot change the browse path of this DataFinder instance. You can change the browse path only on the server itself. However, you can change the display names and the symbols. |
| --- | --- |

#### Settings

|  | New | Deletes the browse settings and opens the dialog box where you select a new start entity. The start entity is the top entity, from which you define the browse path. DIAdem reads the possible start entities from the application model. You can only use as start entities those entities that have a valid path to a measurement value. |
| --- | --- | --- |
|  | Load | Opens the dialog box where you load the browse settings (*.tbs). |
|  | Save As | Opens the dialog box where you save the browse settings (*.tbs). DIAdem embeds the symbols of the entities in the configuration file when saving. If the browse setting you want to save does not lead to an AoMeasurementQuantity type entity, DIAdem displays an error message. |
|  | Reset | Sets the browse settings to the default state. |
|  | Add Entity | Opens the dialog box where you add an entity to the existing browse path. You can only add a new entity if the browse path does not end with a measurement value. |
|  | Complete the Browse Path | Opens the dialog box where DIAdem suggests the possible browse paths from the selected entity to the measurement value. |
|  | Delete Entity | Deletes the selected entity and all entities below this entity from the browse path. You cannot delete the start entity. To create a new browse path, select New. |
|  | Browse path [model view] | Displays the entities of the current browse path. If you have not modified the browse path, DIAdem displays the entities of the standard browse path. Select Show Submatrices from the context menu to enable and disable the display of submatrices and LocalColumns.Note Select Show Parent Reference or Show Child Reference from the context menu of the model view to display the superordinate or subordinate entity. |
|  | Note Select Show Parent Reference or Show Child Reference from the context menu of the model view to display the superordinate or subordinate entity. |  |
|  | Reset Display Names for All Entities | Resets the names of all entities to the standard name if you previously changed the names of entities. |
|  | Reset Symbols for All Entities | Resets the symbols of all entities to the standard symbols if you previously changed the symbols of entities. |
|  | Edit Display Name | Specifies the name of an entity DIAdem uses to display the data elements of that entity in the data browser and in the search results list. For example, as a name you can select the ID of an AoMeasurement type entity or the description of an AoTest type entity. DIAdem does not display changes to the display name in the browse path overview. DIAdem provides the properties of the basic model in the list. Click the ... button to display a list of all available properties in the Edit Display Name dialog box. |
|  | Display name | Opens the dialog box where you change the name of the data elements of the selected entity displayed in the data browser and the search results list. |
|  | Symbol | Opens the dialog box where you specify the symbol with which DIAdem displays the data elements of the selected entity in the data browser and the search results list. |

|  | Note For more information on the effects of a browse setting on the data browser, the search results list, and the load parameters, refer to the Browse Path - General page. |
| --- | --- |

|  | Note The page Varying Browse Settings of a Data Store contains a detailed example on how to use browse settings. |
| --- | --- |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select Settings»Current DataProvider»Browse Settings. You can only open the dialog box when a data store is open. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_browsesettings_suggest_dialog.htm language=enus -->
## TOPIC 00388: Complete the Browse Path

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_browsesettings_suggest_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_browsesettings_suggest_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > [Search: Settings](../dlgnavigator/navi_dssearchdata_dlg_overview.htm) > Complete the Browse Path

Complete the Browse Path

Use this dialog if you want DIAdem to complete an incomplete browse path. A complete browse path begins with the start entity you select and always ends with a measurement value. When the application model enables several browse paths, you can open the different alternatives by clicking the arrow keys.

|  | Note Select Show Parent Reference or Show Child Reference from the context menu of the model view to display the superordinate or subordinate entity. |
| --- | --- |

|  | Note For more information on the effects of a browse setting on the data browser, the search results list, and the load parameters, refer to the Browse Path - General page. |
| --- | --- |

|  | Note To open this dialog in DIAdem NAVIGATOR, select Settings»Current DataProvider»Browse Settings and click the Complete Browse Path button. You can only click the Complete the Browse Path button when the browse path is incomplete. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_changedatastorefiles_dialog.htm language=enus -->
## TOPIC 00389: Open DataFinder

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_changedatastorefiles_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_changedatastorefiles_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [DataFinder](../dlgnavigator/navi_datafinder_overview.htm) > [Search: Settings](../dlgnavigator/navi_searchdata_dlg_overview.htm) > Open DataFinder

Open DataFinder

Use this dialog box to open the local DataFinder or a DataFinder instance.

#### Settings

|  | List of DataFinders | Displays the local DataFinder My DataFinder and all DataFinder instances. |
| --- | --- | --- |
|  | Create DataFinder Instance Connection | Opens the dialog box where you specify or edit access to a DataFinder instance. |
|  | DataFinder Instance Connection Properties | Opens the dialog box where you configure an existing connection. |
|  | Remove DataFinder Instance Connection | Deletes a DataFinder instance. |
|  | Import DataFinder Instance Connection | Imports a connection to a DataFinder instance (*.urf). |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select File»Open DataFinder. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_changedatastoreserver_dialog.htm language=enus -->
## TOPIC 00390: Open Data Store

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_changedatastoreserver_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_changedatastoreserver_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Open Data Store

Open Data Store

Use this dialog box to open a [data store](../../gennavigator/gennavigator/genshell_datastore_definition.htm).

#### Settings

|  | Data stores | Shows an overview of the available data stores. |
| --- | --- | --- |
|  | Create Data Store | Opens the dialog box where you create a new data store. |
|  | Configure Data Store | Opens the dialog box where you configure the data store selected in the overview. |
|  | Remove Data Store | Removes the data store selected in the overview. |
|  | Import Data Store | Opens the dialog box where you import the (.urs) data store. |
|  | Export Data Store | Opens the dialog box where you export a data store. |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select File»Open Data Store. |
| --- | --- |

#### Procedures

[Configuring Data Stores](../../procnavigator/procnavigator/procnavigator_change_data.htm) | [Filtering the Display of Data Stores](../../procnavigator/procnavigator/procnavigator_filter.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_configdataplugin_dialog.htm language=enus -->
## TOPIC 00391: DataPlugin Settings

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_configdataplugin_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_configdataplugin_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [DataPlugins](../dlgnavigator/navi_dataplugin_overview.htm) > DataPlugin Settings

DataPlugin Settings

Use this dialog box to create, to import, to export, to delete, and to configure DataPlugins. Save a DataPlugin in a file with the filename extension .uri. Another user can double-click this file or can use the dialog box **Import DataPlugin** to activate the saved DataPlugin. Visit the DataPlugin Web site for examples and DataPlugins for downloading.

|  | Note You also can create DataPlugins with the DataPlugin Wizard. |
| --- | --- |

#### Settings

|  | Create DataPlugin | Opens the dialog box where you create a new DataPlugin. |
| --- | --- | --- |
|  | Configure DataPlugin | Opens the dialog box where you configure a DataPlugin. |
|  | Remove DataPlugin | Removes a DataPlugin from the list. |
|  | Import DataPlugin | Opens the dialog box where you import a (*.uri) DataPlugin.Note By default the VBS DataPlugins are encrypted. Use the Import DataPlugin button to receive a DataPlugin unencrypted and to then process it. |
|  | Note By default the VBS DataPlugins are encrypted. Use the Import DataPlugin button to receive a DataPlugin unencrypted and to then process it. |  |
|  | Export DataPlugin | Opens the dialog box where you export a DataPlugin. |
|  | Export Encrypted DataPlugin | Opens the dialog box where you export an encrypted DataPlugin. In the list, encrypted DataPlugins have the filename extension uri and are a VBCrypt type.Note DIAdem enables the Export DataPlugins, Remove DataPlugins, and Encrypt DataPlugins buttons only for VBS type DataPlugins. |
|  | Note DIAdem enables the Export DataPlugins, Remove DataPlugins, and Encrypt DataPlugins buttons only for VBS type DataPlugins. |  |
|  | Name | Specifies the name of the DataPlugin. |
|  | Type | Specifies the type of the DataPlugin. |
|  | Filename extensions | Specifies the filename extensions that the DataPlugin can access. |
|  | Display file-based DataPlugins only | Specifies whether the dialog box displays only file-based or also server-based DataPlugins. |
|  | Update | Opens the dialog box where you update the DataPlugins installed on your computer. |

|  | Note You can only develop your own VBS type DataPlugins. If the DataPlugin is a different type, you can use the Configure DataPlugin dialog box to add filename extensions to this DataPlugin. Visit the DataPlugin Web Site for current documentation on how to create and add DataPlugins to DIAdem and to the DIAdem DataPlugin interface.You can load a VBS DataPlugin directly into the DIAdem SCRIPT editor. Select the VBS DataPlugin in the list and select Edit Script from the context menu. |
| --- | --- |

|  | Note Enable the DataPlugin on the DataPlugin tab in the Configure My DataFinder dialog box for a DataFinder to use a DataPlugin. |
| --- | --- |

|  | Note To open this dialog box in the DIAdem NAVIGATOR panel or the DIAdem SCRIPT panel, select Settings»Extensions»DataPlugins. |
| --- | --- |

#### Procedures

[Importing ASCII Files with the DataPlugin Wizard](../../procnavigator/procnavigator/procnavigator_dataplugin.htm) | [Registering DataPlugins](../../procshell/procshell/procshell_register_dataplugins.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_data_browser_options_dialog.htm language=enus -->
## TOPIC 00392: Browser Settings

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_data_browser_options_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_data_browser_options_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Browser Settings

Browser Settings

Use this dialog box to limit the amount of data that DIAdem NAVIGATOR displays. This speeds up the data display.

#### Settings

| Limit number of objects | Specifies that DIAdem only displays a limited amount of data. |
| --- | --- |
| Max. read count | Specifies the maximum amount of data to display. |

|  | Note You can open this dialog box in the context menu of a data store in DIAdem NAVIGATOR. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_datastore_overview.htm language=enus -->
## TOPIC 00393: Data Stores

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_datastore_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_datastore_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > Data Stores

Data Stores

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes where you create, configure, load, and save [Data stores](../../gennavigator/gennavigator/genshell_datastore_definition.htm).

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_dssearch_property_window.htm language=enus -->
## TOPIC 00394: Property Display of the Data Store and of the Search Results

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_dssearch_property_window.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_dssearch_property_window.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > [Search: User Interface](../dlgnavigator/navi_dssearchdata_gui_overview.htm) > Property Display of the Data Store and of the Search Results

Property Display of the Data Store and of the Search Results

Use this window to view the properties of data elements from the data browser and of the search results, and to display the data as a graphic in a preview. In the left area the property display shows, for example, the name or the ID of a measurement quantity. On the right side the channel preview displays a selected measurement quantity in a graphic via its index or as a [Waveform](../../genshell/genshell/genshell_waveforms.htm).

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_dssearch_queryform_window.htm language=enus -->
## TOPIC 00395: Search Input Area (Data Stores)

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_dssearch_queryform_window.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_dssearch_queryform_window.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > [Search: User Interface](../dlgnavigator/navi_dssearchdata_gui_overview.htm) > Search Input Area (Data Stores)

Search Input Area (Data Stores)

Use the search input area to create search conditions and to execute a search in a data store. Select **Find»Save Query As** to save the current search in a file with the file extension *.tdq. Select **Find»Load** to load a stored query. Refer to the Help page [Notes on Searching for Data (Data Stores)](../../gennavigator/gennavigator/navi_dssearch_specific.htm) for further information on searching in data stores.

#### Settings for the Advanced Search

You use four parameters to specify a search condition: the level at which DIAdem executes the search, the property to search, the operator, and the property value to be searched for. You can combine several search conditions into one query. Depending on which **search** button you select, the DataFinder displays tests, measurements, or quantities in the [Search Results](../dlgnavigator/navi_datastore_resultlist_window.htm).

By default DIAdem combines the individual search conditions with an AND operation. You also can execute [OR](../../gennavigator/gennavigator/navi_dssearch_or.htm) operations on single values of a search condition, or entire search conditions, for example, to search for several test names. Refer to the help page on [Evaluating Search Conditions](../../gennavigator/gennavigator/navi_dssearch_characteristics.htm) for information about combining several search conditions.

| Name | Specifies the name of a search condition. Use this name to access search conditions in the logical operations line. |
| --- | --- |
| Level | Specifies the level which contains the specified property. The level depends on the specified browse path. |
| Property | Specifies the property that DIAdem browses for the specified value. The property depends on the specified browse path. |
| Operator | Specifies the operator that DIAdem searches with. |
| Value | Specifies the value of the property DIAdem searches for. |
| ... | Specifies the possible value range of a search. DIAdem opens the Text Display (Data Stores) dialog box if you search for a text in the related search line. DIAdem opens the dialog box Display of Integer Values, Numeric Values, and Date/Time Values (Data Stores) when you search for integer values, numeric values, or date/time values in the associated search line. |
| Search for Tests | Starts the search. DIAdem displays the tests in the search results. |
| Search for Measurements | Starts the search. DIAdem displays the tests in the search results. |
| Search for Measurement Quantities | Starts the search. DIAdem displays the measurement quantities in the search results. |
| Refresh | Refreshes the view of the data browser according to the filter setting. |
| Filtering | Limits the number of elements displayed in the Data Browser. |
| Logical operations line | Contains the logical operator of the individual search condition within a query. DIAdem fills the logical operations line according to the search condition in the search input area. The names C1, C2 and so on refer to the names of individual search conditions. You can change the operators between the individual search conditions in the logical operations line.Note You can connect the search conditions in the logical operations line with AND and OR. Use parentheses to specify the order of evaluation. DIAdem replaces the curved brackets { and }, and the square brackets [ and ] automatically with the round brackets ( and ). |
|  | Note You can connect the search conditions in the logical operations line with AND and OR. Use parentheses to specify the order of evaluation. DIAdem replaces the curved brackets { and }, and the square brackets [ and ] automatically with the round brackets ( and ). |

|  | Note The label on the Search button depends on the browse settings. For more information about how to create a new browse path, refer to the Browse Settings page. For more information on the effects of a browse setting on the data browser, the search results list, and the load parameters, refer to the Browse Path - General page. |
| --- | --- |

Use a [Column-oriented search](../../gennavigator/gennavigator/navi_search_columnsoriented.htm) to search for selected properties of a data store or for selected properties of these data elements. You can then load the search results with the property values column-wise as channels into the Data Portal.

#### Settings for the Quick Search

If you use a DataFinder instance as an ASAM ODS server, you can execute a quick search in the data store the DataFinder instance provides.

| Entry field | Enter the search term in the entry line which DIAdem searches for in the properties of the data store. |
| --- | --- |
| Search | Starts the quick search. The DataFinder displays the found files in the Search results. |

#### Data Store Properties You Can Search for or Not Search For

In data stores you can search for all numeric, text, and date/time type application properties. You cannot search for vector properties, instance properties, and properties with a recursive property path. You also cannot search for properties whose property path contains Test, SubTest, Measurement, or MeasurementQuantity . If the property path, for example, is MyMeasurement.Subtest.Name, select the level Subtest and the property Name to execute a search.

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_dssearch_searchresults_display_dialog.htm language=enus -->
## TOPIC 00396: Configure Search Results List (Data Stores)

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_dssearch_searchresults_display_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_dssearch_searchresults_display_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > [Search: Settings](../dlgnavigator/navi_dssearchdata_dlg_overview.htm) > Configure Search Results List (Data Stores)

Configure Search Results List (Data Stores)

Use this dialog box to specify the columns with properties that DIAdem displays in the search results list.

#### Settings

|  | Test/Measurement/MeaQuantity | Specifies whether DIAdem displays the properties of a test, a measurement, or a measurement quantity in the overview.Note Depending on the Browse Settings, the label on the tabs may vary. For more information on the effects of a browse setting on the data browser, the search results list, and the load parameters, refer to the Browse Path - General page. |
| --- | --- | --- |
|  | Note Depending on the Browse Settings, the label on the tabs may vary. For more information on the effects of a browse setting on the data browser, the search results list, and the load parameters, refer to the Browse Path - General page. |  |
|  | Delete | Deletes the selected property from the list. |
|  | Up | Moves the selected property one line up in the list. |
|  | Down | Moves the selected property one line down in the list. |
|  | Level | Specifies the name of the level to which the property belongs. |
|  | Property | Specifies the name of the property to be displayed.Note In the search results list of data stores you can display all numeric, text, and date/time type application properties, but no vector properties, instance properties, and properties with a recursive property path. If you select a property, of which the property path contains 1:n connections, DIAdem may not be able to interpret the property value precisely and marks the associated line with a blue exclamation mark. |
|  | Note In the search results list of data stores you can display all numeric, text, and date/time type application properties, but no vector properties, instance properties, and properties with a recursive property path. If you select a property, of which the property path contains 1:n connections, DIAdem may not be able to interpret the property value precisely and marks the associated line with a blue exclamation mark. |  |
|  | Automatically determine property column from search | Specifies whether DIAdem automatically displays columns with the properties that you searched for, to the search results. |
|  | Only property names in the column header | Specifies whether DIAdem displays the names of the layers and the associated properties in the column header of the search result list or whether DIAdem hides the layers and only displays the properties. |
|  | Maximum number of displayed search results | Specifies the maximum number of search results that DIAdem determines. DIAdem can determine a maximum of 10,000 values. The default value is 200. |

|  | Note If you select a property, of which the property path contains 1:n connections, DIAdem may not be able to interpret the property value precisely and will mark the associated line with a blue exclamation mark. |
| --- | --- |

|  | Note Select this dialog box from the context menu of the results list of a data store or click the Configure Search Results List button on the toolbar. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_dssearch_valuelimits_dlg.htm language=enus -->
## TOPIC 00397: Display of Integer Values, Numerical Values, and Date/Time Values (Data Stores)

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_dssearch_valuelimits_dlg.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_dssearch_valuelimits_dlg.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > [Search: User Interface](../dlgnavigator/navi_dssearchdata_gui_overview.htm) > Display of Integer Values, Numerical Values, and Date/Time Values (Data Stores)

Display of Integer Values, Numerical Values, and Date/Time Values (Data Stores)

Use this dialog box to display the greatest and the smallest possible value for a property selected in the search results. If you enter a different search condition into the search entry field, DIAdem limits the list according to these search conditions.

|  | Note When you change the operators in the logic line manually, DIAdem no longer limits the list of displayed properties. |
| --- | --- |

#### Settings

| Min | Specifies the minimum value of the selected property. |
| --- | --- |
| Max | Specifies the maximum value of the selected property. |

|  | Note You can open this dialog box in the last column of the search input area of the advanced search in a data store. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_dssearchdata_dlg_overview.htm language=enus -->
## TOPIC 00398: Search: Settings

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_dssearchdata_dlg_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_dssearchdata_dlg_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > Search: Settings

Search: Settings

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes where you configure the search for data in a data store.

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_dssearchdata_gui_overview.htm language=enus -->
## TOPIC 00399: Search: User Interface

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_dssearchdata_gui_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_dssearchdata_gui_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [Data Stores](../dlgnavigator/navi_datastores_overview.htm) > Search: User Interface

Search: User Interface

The subordinate topics contained in the tree on the contents tab of the Help describe the user interfaces of data stores.

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_file_load_dialog.htm language=enus -->
## TOPIC 00400: Open

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_file_load_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_file_load_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Open

Open

Use this dialog box to load data sets.

#### Settings

| Filename | Specifies the name of the data set. |
| --- | --- |
| File type | Specifies the file type of the data set. |

| Loading | Loads the entire data set. |
| --- | --- |
| Register | Registers the channels of the data set. When you register a data set that contains calculation channels, DIAdem always loads all of the calculation channels. |
| Append | Appends the data you want to load to existing channels in the Data Portal instead of storing the data in new channels. You can only append files and channel groups. |
| Selective Opening | Loads the selected channels of the data set. |
| Data reduction | Loads data reduced. A window covers the data channel in steps of a specific interval width and loads one value from each interval. |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select File»Open. |
| --- | --- |

|  | Note The only DataPlugins which you can develop yourself or which you can edit in the Properties dialog box are VBS DataPlugins. If the DataPlugin is a different type you can use the Properties dialog box to add filename extensions to this DataPlugin. Visit the DataPlugin Web Site for current documentation on how to create and add DataPlugins to DIAdem and to the DIAdem DataPlugin interface. |
| --- | --- |

#### Procedures

[Loading TDM Files](../../procnavigator/procnavigator/procnavigator_loading_tdm.htm) | [Reducing Data Loading](../../procnavigator/procnavigator/procnavigator_loaddata_reducing.htm) | [Saving TDM Files](../../procnavigator/procnavigator/procnavigator_saving_tdm.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_file_load_selective_dialog.htm language=enus -->
## TOPIC 00401: Selective Opening

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_file_load_selective_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_file_load_selective_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Selective Opening

Selective Opening

Use this dialog box to load individual channels of a data set.

#### Settings

| External data | Displays the data set and the channels for selective loading. Select the channels to be loaded. |
| --- | --- |
| Loading | Loads the selected channels of the data set. |
| Register | Registers the selected channels of the data set. |
| Append | Appends the data you want to load to existing channels in the Data Portal instead of storing the data in new channels. You can only append files and channel groups. |
| Data reduction | Loads data reduced. A window covers the data channel in steps of a specific interval width and loads one value from each interval. |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select File»Open»Selective Opening. |
| --- | --- |

#### Procedures

[Loading TDM Files](../../procnavigator/procnavigator/procnavigator_loading_tdm.htm) | [Reducing Data Loading](../../procnavigator/procnavigator/procnavigator_loaddata_reducing.htm) | [Saving TDM Files](../../procnavigator/procnavigator/procnavigator_saving_tdm.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_file_load_with_dialog.htm language=enus -->
## TOPIC 00402: Open With...

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_file_load_with_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_file_load_with_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Open With...

Open With...

Use this dialog box to specify the loader and to load or to register a data set. For example, you can load ASCII files with the ASCII import filter.

#### Settings

| Loader | Specifies the loader. |
| --- | --- |
| Filename extensions | Specifies the filename extensions for the loader. |
| Display only Plugins with same extension | Specifies whether DIAdem displays all loaders or only the loaders in which the DataPlugins have the selected file extension. |
| Load | Loads the data set. |
| Register | Registers the data set. |
| Append | Appends the data you want to load to existing channels in the Data Portal instead of storing the data in new channels. You can only append files and channel groups. |
| Selective Opening | Opens the selected channels of the data set or registers the selected channels of the data set. |
| Data reduction | Loads data reduced. A window covers the data channel in steps of a specific interval width and loads one value from each interval. |
| Find | Opens the dialog box where you can install the DataPlugin of a file extension from the NI DataPlugin website. |
| Wizard | Opens the Text DataPlugin Wizard or the Excel DataPlugin Wizardt that you use to create a new DataPlugin. |

|  | Note You open this dialog box in the context menu of a file in DIAdem NAVIGATOR. |
| --- | --- |

#### Procedures

[Loading TDM Files](../../procnavigator/procnavigator/procnavigator_loading_tdm.htm) | [Reducing Data Loading](../../procnavigator/procnavigator/procnavigator_loaddata_reducing.htm) | [Saving TDM Files](../../procnavigator/procnavigator/procnavigator_saving_tdm.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_file_save_dialog.htm language=enus -->
## TOPIC 00403: Save As

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_file_save_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_file_save_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Save As

Save As

Use this dialog box to save data.

#### Settings

| Filename | Specifies the name of the data set. |
| --- | --- |
| File type | Specifies the type of the data set. |
| Save | Saves the entire internal data store. |
| Only elements selected in the Data Portal | Saves the channels selected in the Data Portal. |

|  | Note If you do not save data in the TDM format, the saved data might be incomplete. For example, group information or properties might be lost.If you save data in the CSV format, DIAdem saves only the channels of the first channel group. If you want to save channels from other groups, you must save these channels selectively. If you save data in the CSV format, DIAdem uses a tabulator as the separator.When you save data in Excel format, the group names in the Data Portal must differ within the first 31 characters because Excel does not support more characters in the page names. Similar restrictions may apply to other file formats. |
| --- | --- |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select File»Save As. |
| --- | --- |

#### Procedures

[Loading TDM Files](../../procnavigator/procnavigator/procnavigator_loading_tdm.htm) | [Reducing Data Loading](../../procnavigator/procnavigator/procnavigator_loaddata_reducing.htm) | [Saving TDM Files](../../procnavigator/procnavigator/procnavigator_saving_tdm.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_filter_settings_dialog.htm language=enus -->
## TOPIC 00404: Set Filter Parameters

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_filter_settings_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_filter_settings_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Set Filter Parameters

Set Filter Parameters

Use this dialog box to filter the display of server-based data in the Navigator tree. A grey rectangle with a green point in front of the object type indicates that the filter is enabled.

#### Settings

| Extend List / Reduce List | Extends or reduces the list of object types. |
| --- | --- |
| Object types | Specifies the object types you want to filter. DIAdem only displays the object types that belong to a data store. |
| Extend List / Reduce List | Extends or reduces the list of object properties. |
| Object properties | Specifies the property that DIAdem filters. |
| Operator | Specifies the operator that DIAdem filters with. |
| Operand | Specifies the operand that DIAdem filters with. |
| Combine parameters | Specifies that DIAdem uses the filter settings on all object types. |
| Case-sensitive | Specifies that DIAdem filters case-sensitively. |
| Filter file | Specifies the filter file. |
| Load | Loads filter settings. Filter settings have the filename extension .tsf. |
| Save As | Opens the dialog box where you specify the name of the file in which DIAdem saves the filter settings. |
| Reset | Resets all the filter settings. |

|  | Note If you use the equals sign (=) as the operator you can use a wildcard as the operand for text attributes. Use a question mark (?) as a wildcard for one character, and an asterisk (*) as a wildcard for any number of characters. You cannot use these wildcards for other operators. |
| --- | --- |

|  | Note If you set several filters for one object type, DIAdem filters with all the set filter settings simultaneously. |
| --- | --- |
|  | Note If you change the settings saved in a filter file and click OK to close the dialog box, DIAdem overwrites the filter file with the new settings regardless of the settings you saved previously via Save As in the filter file. |

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_loaddata_dlg_overview.htm language=enus -->
## TOPIC 00405: Loading and Saving Data

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_loaddata_dlg_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_loaddata_dlg_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > Loading and Saving Data

Loading and Saving Data

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes for loading and saving data. The topics provide information about loading and saving [Data stores](../../gennavigator/gennavigator/genshell_datastore_definition.htm), using [DataPlugins](../../dataplugin/examples/general.htm), using wizards to load and save ASCII data and Excel data, and information on many file filters.

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_search_tree_window.htm language=enus -->
## TOPIC 00406: File Browser

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_search_tree_window.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_search_tree_window.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [DataFinder](../dlgnavigator/navi_datafinder_overview.htm) > [Search: User Interface](../dlgnavigator/navi_searchdata_gui_overview.htm) > File Browser

File Browser

Use the file browser to browse in the search areas of the enabled [DataFinder](../../gennavigator/gennavigator/navi_search_gui_general.htm), in the file system, or in [data stores](../../gennavigator/gennavigator/genshell_datastore_definition.htm).

When you open the [DataFinder](../../gennavigator/gennavigator/navi_search_gui_general.htm) My DataFinder, the file browser displays the [Search areas](../dlgnavigator/navi_search_configure_searchareas_dialog.htm) in the top area. When you open a [DataFinder Instance](../../gennavigator/gennavigator/navi_search_gui_general.htm), the file browser displays the search areas of the computer that is shared as the [DataFinder Instance](../dlgnavigator/navi_search_connect_remote_dialog.htm). In the search areas you can click the plus signs in front of the folders, groups, and files to browse down to the channel level. From the file browser, you can load data completely, [selectively](../dlgnavigator/navi_file_load_selective_dialog.htm), or [reduced](../dlgnavigator/reductionloaddlg_dialog.htm). You can also [append](../../gennavigator/gennavigator/navi_appenddata_general.htm) files and channel groups to channels in the Data Portal.

|  | Note The DataFinder must first index the data in the search areas, before you can browse the search areas of a DataFinder. The DataFinder indexes one search area completely before it indexes the next search area. |
| --- | --- |

You can also register data. In this case DIAdem only creates a reference to the data but does not load the data into the internal storage area. When you register a data set that contains calculation channels, DIAdem always loads all of the calculation channels.

Drag and drop data sets, groups, and channels into the [Data Portal](../../genportal/genportal/portal_general.htm) to load data into DIAdem. Use the **File Operations** context menu to copy, delete, move, rename, and protect files, or to open files in the explorer.

When you open the [DataFinder](../../gennavigator/gennavigator/navi_search_gui_general.htm) My DataFinder, the file browser also displays the entire file system in the bottom area. Select **Only Known File Types** from the context menu of the file system for DIAdem to display only the files with a filename extension that is registered in DIAdem. To disable the display of the file system, select **Display Local File System** from the context menu. To add a folder from the file system to the existing search areas, select **Add Search Area** from the context menu.

If you open a [data store](../../gennavigator/gennavigator/genshell_datastore_definition.htm), the file browser displays the folders and files that are associated with the data store. Use a **Load Data with Loading Configuration** to specify the properties of a data store which DIAdem imports into the Data Portal when loading bulk data.

The file browser identifies folders, files, groups, and channels with different symbols. Refer to [Folder Symbols and File Symbols in the File Browser](../../gennavigator/gennavigator/navi_browser_filetypes.htm) for an overview of the symbols.

In the [Property Display](../dlgnavigator/navi_search_property_window.htm), the file browser displays the properties of each of the selected files, groups, and channels. You can drag and drop the properties from the Display to the search area of the quick search or of the advanced search.

|  | Note If you use DIAdem as the client of a DataFinder instance, you can also browse in data in an archiving system. To do so, the DataFinder instance must index the data first. To browse for data, the archiving system does not need to be accessed. When the data is loaded, the data from the archive is automatically restored. |
| --- | --- |

|  | Note You can programmatically access the search results list with the Navigator.Display.CurrDataFinder.ResultsList object. You can add the events OnContextMenuPointSelected and OnShowingContextMenu to the context menu of the search results. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_search_valuelimits_dlg.htm language=enus -->
## TOPIC 00407: Display of Integer Values, Numerical Values, and Date/Time Values (DataFinder)

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_search_valuelimits_dlg.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_search_valuelimits_dlg.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [DataFinder](../dlgnavigator/navi_datafinder_overview.htm) > [Search: User Interface](../dlgnavigator/navi_searchdata_gui_overview.htm) > Display of Integer Values, Numerical Values, and Date/Time Values (DataFinder)

Display of Integer Values, Numerical Values, and Date/Time Values (DataFinder)

Use this dialog box to display the greatest and the smallest indexed value for a property selected in the search results. If you enter a different search condition into the search entry field, DIAdem limits the list according to these search conditions.

|  | Note When you change the operators in the logic line manually, DIAdem no longer limits the list of displayed properties. |
| --- | --- |

#### Settings

| Min | Specifies the minimum value of the selected property. |
| --- | --- |
| Max | Specifies the maximum value of the selected property. |

|  | Note You only can open this dialog box if you search for base properties and optimized custom properties. |
| --- | --- |

|  | Note You can open this dialog box in the last column of the search input area of the advanced search in DIAdem NAVIGATOR. This column is only available in the versions DIAdem Advanced and DIAdem Professional. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_searchdataplugin_dialog.htm language=enus -->
## TOPIC 00408: Find DataPlugin

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_searchdataplugin_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_searchdataplugin_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > [Open With...](../dlgnavigator/navi_file_load_with_dialog.htm) > Find DataPlugin

Find DataPlugin

Use this dialog box to search for a DataPlugin for loading a file with a specific filename extension. You can choose whether to search for the DataPlugin associated with the filename extension on the NI DataPlugin website or on a DataFinder instance. The list only shows the DataPlugins not yet registered on your computer or which the NI website or a DataFinder instance provide in a new version. To load a DataPlugin from the NI DataPlugin website onto your computer, select the DataPlugin in the list, and click **Install**. If you want to download a DataPlugin from a DataFinder instance, DIAdem opens the dialog box [DataFinder Instance](../dlgnavigator/navi_changedatastorefiles_dialog.htm), where you can select a DataFinder instance. Select the DataPlugin in the list and then click **Load**.

|  | Note If you created a DataPlugin on your computer with the same name as a DataPlugin, which the update source is to install, DIAdem overwrites the DataPlugin you created. DIAdem only overwrites the URI file. The VBS file of the DataPlugin you created remains in the local DataPlugin folder. You can restore the DataPlugin you created by generating a new URI file with the VBS file you created. |
| --- | --- |

#### Settings

| DataPlugin Update from NI Web/DataFinder Instance | Specifies whether you search for a DataPlugin on the NI DataPlugin website or on a DataFinder instance. |
| --- | --- |
| DataPlugin | Specifies the name of the DataPlugin. |
| Filename extension | Specifies the filename extensions of the files that the DataPlugin can access. |
| Description | Describes the selected channel. |

#### Procedures

[Importing ASCII Files with the DataPlugin Wizard](../../procnavigator/procnavigator/procnavigator_dataplugin.htm) | [Registering DataPlugins](../../procshell/procshell/procshell_register_dataplugins.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_storage_open_aop4_dialog.htm language=enus -->
## TOPIC 00409: Data Store Properties - [AOP via CORBA]

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_storage_open_aop4_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_storage_open_aop4_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Data Store Properties - [AOP via CORBA]

Data Store Properties - [AOP via CORBA]

Use this dialog box to specify the parameters for connecting an AOP5 server via CORBA.

#### Settings

| Connection type | Specifies the type of connection. |
| --- | --- |
| Server | Specifies the name of the AOP5 server. |
| Port | Specifies the port. |
| URL | Specifies the address of the AOP5 server. |
| User | Specifies the user of the AOP5 server. |
| Password | Specifies the user password. |
| Save password | Specifies that DIAdem saves the password encrypted. If you save the password, you can reopen the data store without entering the password. |
| ... | Opens the dialog box where you search for an address. |
| Extended | Opens the dialog box where you can make additional settings. |

|  | Note You can also open a data store by entering an XML string. For example, press the key combination <Ctrl-Shift-A> in the dialog boxes Data Stores - Settings or New Data Store to generate this XML string for the data store. Then open DIAdem SCRIPT and insert the clipboard contents with <Ctrl-V> into a script in order to get the string. |
| --- | --- |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select Settings»Data Stores»Create Data Store»AOP5. You must download the respective DataPlugin from the NI DataPlugin Website. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_storage_open_citadel_dialog.htm language=enus -->
## TOPIC 00410: Data Store Properties [Citadel 4, Citadel 5, and VI Logger 2]

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_storage_open_citadel_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_storage_open_citadel_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Data Store Properties [Citadel 4, Citadel 5, and VI Logger 2]

Data Store Properties [Citadel 4, Citadel 5, and VI Logger 2]

Use this dialog box to specify the parameters for connecting a Citadel database. Use Citadel data stores to directly access databases that were generated with LabVIEW Datalogging and Supervisory Control or Lookout 6.*x*.

#### Settings

| Computer | Specifies which computer the Citadel database is on. If the Citadel database is on the local computer, you must enter localhost as the computer name. |
| --- | --- |
| ... (Computer) | Opens the dialog box where you search for a computer. |
| Folders | Specifies which folder the Citadel database is in. |
| ... (Folders) | Opens the dialog box where you search for a folder. |
| Database | Specifies the Citadel database. |
| Time interval enable | Specifies that the server only provides data from the specified time interval. |
| Start time | Specifies the start time of the interval. |
| End time | Specifies the end time of the interval. |
| Subintervals | Specifies that DIAdem divides the time interval into subintervals. |
| Interval width (sec) | Specifies the size of the subintervals for the values of the Citadel database in seconds. |
| Calculations enable | Specifies that the Citadel database provides calculated data and not the data from the database. |
| Interval width (sec) | Specifies the size of the subintervals for calculated values in seconds. |
| Interpolation (Citadel 5) | Specifies the type of interpolation |
| Interpolation | Specifies that DIAdem runs linear interpolation on the values in the calculation interval. |
| Minimum | Specifies that DIAdem calculates the minimum in the calculation interval. |
| Maximum | Specifies that DIAdem calculates the maximum value in the calculation interval. |
| Mean value | Specifies that DIAdem calculates the mean value in the calculation interval. |
| Standard deviation | Specifies that DIAdem calculates the standard deviation in the calculation interval. |
| ... (Database) | Opens the dialog box where you search for a database. |

|  | Note The second function group in DIAdem NAVIGATOR offers direct access to data stores that were generated with NI LabVIEW Datalogging and Supervisory Control Module and NI Lookout. If you want to access data stores of earlier product versions, proceed as follows: Delete the default data store you want to replace, in the data store manager, for example, 'Default LabVIEW DSC Module'. Generate a new data store with the same name (for example 'Default LabVIEW DSC Module') for the matching data store type. In the following table you can find information about which data store type supports which product version: Data store type Product version Citadel 4 LabVIEW Datalogging and Supervisory Control Module 6.xx and Lookout 4.xx and 5.xx Citadel 5 LabVIEW Datalogging and Supervisory Control Module 7.x and Lookout 6.x VI Logger 2 VI Logger 2.x |
| --- | --- |
| Data store type | Product version |
| Citadel 4 | LabVIEW Datalogging and Supervisory Control Module 6.xx and Lookout 4.xx and 5.xx |
| Citadel 5 | LabVIEW Datalogging and Supervisory Control Module 7.x and Lookout 6.x |
| VI Logger 2 | VI Logger 2.x |

|  | Note To access data stores from NI VI Logger, NI Lookout, or the NI LabVIEW Datalogging and Supervisory Control modules, you require the appropriate software components which are installed by default with the described NI products. If you want to access Citadel 5 data stores but you do not have any of these NI products installed on your DIAdem computer, you must install the Lookout Webclient in addition to DIAdem. You can download the Lookout Webclient at Citadel5 DataPlugin. |
| --- | --- |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select Settings»Data Stores»Create Data Store»Citadel4/5. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/navi_usersettings_dialog.htm language=enus -->
## TOPIC 00411: Default Settings

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/navi_usersettings_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/navi_usersettings_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Searching for Data](../dlgnavigator/navi_searchdata_overview.htm) > [DataFinder](../dlgnavigator/navi_datafinder_overview.htm) > [Search: Settings](../dlgnavigator/navi_searchdata_dlg_overview.htm) > Default Settings

Default Settings

Use this dialog box to make basic settings for opening a data source. DIAdem manages the settings for each data source separately in this dialog box.

#### Settings

| Restore query when opening the data source | Specifies whether DIAdem loads no query, the last active query, or a query from a file, when opening a data source. |
| --- | --- |
| ... | Opens the dialog box where you select a query. |
| Restore expanded states when opening the data browser | Specifies whether DIAdem restores the last active expansion state in the file browser when opening a data source. |

|  | Note To open this dialog box in DIAdem NAVIGATOR, select Settings»Current Data Provider»Default Settings. |
| --- | --- |

#### Procedures

[Configuring the Search Results](../../procnavigator/procnavigator/procnavigator_datafinder_searchresults_configure.htm) | [Defining Search Areas](../../procnavigator/procnavigator/procnavigator_datafinder_searchareas_define.htm) | [Executing a Search with OR Operations](../../procnavigator/procnavigator/procnavigator_search_or.htm) | [Executing a Text Search](../../procnavigator/procnavigator/procnavigator_search_fast.htm) | [Indexing Search Areas](../../procnavigator/procnavigator/procnavigator_searchengine_config.htm) | [Optimizing Custom Properties](../../procnavigator/procnavigator/procnavigator_optimize_customproperties.htm) | [Saving and Loading a Search Query](../../procnavigator/procnavigator/procnavigator_search_save_load.htm) | [Searching for Data on a Different Computer in the Network](../../procnavigator/procnavigator/procnavigator_search_remotedatafinder.htm) | [Searching for Data with a Script Using the Navigator Interface](../../procauto/procauto/procauto_search_gui.htm) | [Searching for Data with a Script without Using the Navigator Interface](../../procauto/procauto/procauto_search_withoutgui.htm) | [Searching for Multiple Properties](../../procnavigator/procnavigator/procnavigator_search_extended.htm) | [Sorting Search Results before Executing a Search](../../procnavigator/procnavigator/procnavigator_sorted_search.htm)

#### Examples

[Brake Tests for Trucks](../../exploff/examples/example_brake_test.htm) | [Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm) | [Combining DataFinder Search Results](../../exploff/examples/expl_combine_searchresult.htm) | [Context Menu for the Search Results of the DataFinder](../../exploff/examples/expl_script_av24.htm) | [Creating ATFX Files from the Context Menu of an ASAM Data Store](../../exploff/examples/expl_navigator_saveselectiontoatfx.htm) | [Customized User Interface](../../exploff/examples/example_application.htm) | [Evaluation Wizard for the Search Results of the DataFinder](../../exploff/examples/expl_searchresultwizard.htm) | [Filtering Data with a Dialog Box](../../exploff/examples/expl_datafilter_dlg.htm) | [Filtering Data without a Dialog Box](../../exploff/examples/expl_datafilter_auto.htm) | [Search and Evaluation Functions in User Dialog Boxes](../../exploff/examples/datafinderusedinsud.htm) | [Searching for and Evaluating Channels](../../exploff/examples/expl_script_av27.htm) | [Searching for Channels in the NAVIGATOR](../../exploff/examples/expl_script_av25.htm) | [Searching for Data Sets Marked "Failed" in Data Stores](../../exploff/examples/expl_pass_fail_analysis_asam.htm) | [Searching for Data Sets Marked "Failed"](../../exploff/examples/expl_script_av29.htm) | [Searching for Properties and Evaluating the Associated Channels](../../exploff/examples/expl_propertyloadandreport.htm) | [Varying Browse Settings of a Data Store](../../exploff/examples/bs_browsesettings.htm)

<!--NI_TOPIC bundle=diadem path=dlgnavigator/dlgnavigator/reductionloaddlg_dialog.htm language=enus -->
## TOPIC 00412: Reduced Loading of Channels

- bundle_id: `diadem`
- source_path: `dlgnavigator/dlgnavigator/reductionloaddlg_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgnavigator/dlgnavigator/reductionloaddlg_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem NAVIGATOR](../dlgnavigator/navi_dlgs_overview.htm) > [Loading and Saving Data](../dlgnavigator/navi_loaddata_dlg_overview.htm) > [Data Stores](../dlgnavigator/navi_datastore_overview.htm) > Reduced Loading of Channels

Reduced Loading of Channels

Use this dialog box to load only specific values of a channel into the Data Portal.

#### Settings

| Load data section | Specifies that DIAdem only loads a specific part of the channels into the Data Portal. |
| --- | --- |
| Index first value | Specifies the index of the first channel value to be loaded. |
| Index last value | Specifies the index of the last channel value to be loaded. |
| Data reduction | Specifies whether DIAdem divides a channel or a channel section into a specific number of intervals or whether you enter the number of values per interval. |
| Interval width | Specifies the number of values in an interval. |
| No. of intervals | Specifies the number of intervals per channel. |
| Reduction mode per interval | Specifies the data reduction method. You can select several reduction methods simultaneously. DIAdem uses the reduction method for all intervals in the channel. DIAdem creates a new data channel for each reduction process and identifies the selected reduction method with texts at the original channel name:1. Value _Sample Mean value_MeanMinimum_MinMaximum_Max |
| 1. Value | _Sample |
| Mean value | _Mean |
| Minimum | _Min |
| Maximum | _Max |

|  | Note Use the DataFileLoadRed command to load data in reduced mode. Use the DataFileLoadRed command to load channel sections or complete channels. |
| --- | --- |

|  | Note If you want to load text channels in reduced mode, you must select the setting 1. value as Reduction mode per interval. If you select any of the other settings, DIAdem displays an error message and does not load the channels. |
| --- | --- |

#### Procedures

[Loading TDM Files](../../procnavigator/procnavigator/procnavigator_loading_tdm.htm) | [Reducing Data Loading](../../procnavigator/procnavigator/procnavigator_loaddata_reducing.htm) | [Saving TDM Files](../../procnavigator/procnavigator/procnavigator_saving_tdm.htm)

<!--NI_TOPIC bundle=diadem path=dlgportal/dlgportal/dlgassignments_dialog.htm language=enus -->
## TOPIC 00413: Assignment Channel - Parameters

- bundle_id: `diadem`
- source_path: `dlgportal/dlgportal/dlgassignments_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgportal/dlgportal/dlgassignments_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../dlgportal/portal_dlgs_overview.htm) > Assignment Channel - Parameters

Assignment Channel - Parameters

Use this dialog box to view and edit assignments in an [assignment channel](../../genshell/genshell/genshell_assignmentchannels.htm). You can create new assignments, and edit or delete existing assignments. A value or a value range can be assigned to a text.

#### Settings

|  | Selected channel | Displays the name of the assignment channel selected in the Data Portal. |
| --- | --- | --- |
|  | New Entry | Adds a new entry to the end of the list. |
|  | Delete Entry | Deletes the selected entry. |
|  | Value | Specifies the value for an assignment. Click into the field to edit the value.Enable the setting Specify intervals to specify the interval limits instead of a value. Note The NoValue value is not valid! |
|  | Note The NoValue value is not valid! |  |
|  | Minimum | Specifies the bottom limit of the assignment interval. Click into the field to edit the value. |
|  | Maximum | Specifies the top limit of the assignment interval. Click into the field to edit the value. |
|  | Text | Specifies the text assigned to a value or to a value range. Click into the field to edit the text. |
|  | Apply | Transfers the texts according to the specified values or value ranges to the channel values of the assignment channel. |
|  | Specify intervals | Specifies that DIAdem assigns value ranges and not single values to the texts. |
|  | Interval limits | Specifies whether the interval limits are open or closed. |
|  | Default value of the channel | Specifies the text which DIAdem uses in assignment channels when no text is assigned to a value or to a value range. If you leave this entry empty, DIAdem assigns an empty string to the values without an assignment. DIAdem displays the default value in the properties display of the Data Portal. |

|  | Note Select Assignment in the properties window of the Data Portal to open this dialog box. Click the input field of this property and then the button with the three dots. |
| --- | --- |

|  | Note If an assignment channel in the Data Portal is read-only, you can view but not edit the parameters listed here. |
| --- | --- |

|  | Note After you have specified intervals and transferred the new value range with Apply to the channel values, DIAdem dims the setting Specify interval. To make this setting available again, enter the same value for the minimum and maximum of all value ranges. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgportal/dlgportal/dlgdatasetcom_dialog.htm language=enus -->
## TOPIC 00414: Data Set Comments

- bundle_id: `diadem`
- source_path: `dlgportal/dlgportal/dlgdatasetcom_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgportal/dlgportal/dlgdatasetcom_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../dlgportal/portal_dlgs_overview.htm) > Data Set Comments

Data Set Comments

Use this dialog box to edit the comments on a data set.

#### Settings

| No. | Specifies the number of the data set comment. |
| --- | --- |
| Name | Specifies the name of the data set comment. |
| Comment | Specifies the data set comment. |

|  | Note The DataFinder does not index data set comments. Therefore you cannot find data set comments when you search in the NAVIGATOR. Use Custom properties instead of data set properties. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgportal/dlgportal/portal_properties_dialog.htm language=enus -->
## TOPIC 00415: Select Properties

- bundle_id: `diadem`
- source_path: `dlgportal/dlgportal/portal_properties_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgportal/dlgportal/portal_properties_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../dlgportal/portal_dlgs_overview.htm) > Select Properties

Select Properties

Use this dialog box to specify which [properties](../../genshell/genshell/genshell_dd_properties.htm) of the channels, the channel groups, or the data sets DIAdem displays in the list view of the Data Portal.

#### Settings

|  | Properties not for display | Specifies the properties DIAdem does not display. To create a new property in the list, double-click the item <Prepare property>. You can then prepare properties that you later create or load. |
| --- | --- | --- |
|  | Display Custom Properties | Displays the custom properties. Double-click an entry in the Properties not for display list to edit the names of the displayed custom properties. The tilde character is a separator which groups the custom properties in the Property Display of the Data Portal. DIAdem combines custom properties containing the same text before the tilde character. |
|  | > | Moves the selected properties to the properties that are to be displayed. |
|  | < | Moves the selected properties to the properties that are not to be displayed. |
|  | Properties for display | Specifies the properties DIAdem displays. |
|  | Title | Specifies the title for the property to be displayed. |
|  | Numeric format | Specifies the Format for the property to be displayed. You only can specify the format for numeric properties. |
|  | Format Numbers | Opens the dialog box where you select or enter the format specification. |
|  | Up/Down | Moves the selected properties one position up or one position down. |

|  |  | Note Open this dialog box in the Data Portal in the context menu of the list view. |
| --- | --- | --- |

#### Procedures

[Assigning Data Set, Group, and Channel Properties with a Script](../../procauto/procauto/procauto_channel_change_properties.htm) | [Configuring a Text Box Display](../../procview/procview/procview_textfield_parametrize.htm) | [Determining Data Set, Group, and Channel Properties with a Script](../../procauto/procauto/procauto_channel_properties.htm) | [Displaying Properties in the Legend of a Curve](../../procview/procview/procview_legend_properties.htm) | [Generating Custom Properties with a Script](../../procauto/procauto/procauto_set_new_properties_values.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm)

<!--NI_TOPIC bundle=diadem path=dlgportal/dlgportal/portal_properties_rename_dialog.htm language=enus -->
## TOPIC 00416: Rename Properties

- bundle_id: `diadem`
- source_path: `dlgportal/dlgportal/portal_properties_rename_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgportal/dlgportal/portal_properties_rename_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../dlgportal/portal_dlgs_overview.htm) > Rename Properties

Rename Properties

Use this dialog box to rename [Properties](../../genshell/genshell/genshell_dd_properties.htm) of channels, channel groups, or data sets. You can only rename custom properties.

#### Settings

| Previous name | Displays the previous name of the property. |
| --- | --- |
| New name | Specifies the new name of the property. The tilde character is a separator which groups the custom properties in the Properties Display of the Data Portal. DIAdem combines custom properties containing the same text before the tilde character. |
| Group | Displays the name of the group. DIAdem does not display this field if you rename the property of a data set. |
| Channel | Displays the channel name. DIAdem does not display this field if you rename the property of a data set or of a group. |
| New name | Displays the new name of the property. If the text is red, the name does not comply with the Naming Conventions or a property with the same name already exists. |
| Value | Displays the value of the property. |
|  |  |

|  | Note Open this dialog box in the Data Portal with the context menu of the Properties display. |
| --- | --- |

#### Procedures

[Assigning Data Set, Group, and Channel Properties with a Script](../../procauto/procauto/procauto_channel_change_properties.htm) | [Configuring a Text Box Display](../../procview/procview/procview_textfield_parametrize.htm) | [Determining Data Set, Group, and Channel Properties with a Script](../../procauto/procauto/procauto_channel_properties.htm) | [Displaying Properties in the Legend of a Curve](../../procview/procview/procview_legend_properties.htm) | [Generating Custom Properties with a Script](../../procauto/procauto/procauto_set_new_properties_values.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d/d2axis_dlgd2colorpal_dialog.htm language=enus -->
## TOPIC 00417: Colors and Y-Channels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d/d2axis_dlgd2colorpal_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d/d2axis_dlgd2colorpal_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Add Curves](../graph_dlg_2d_tab/d2axis_tab_newcurve_dialog.htm) | [Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Stacked Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm)) > Colors and Y-Channels

Colors and Y-Channels

Use this dialog box to specify the colors in a 2D axis system with grouped or stacked bars and y-channels for the **Palette** line color. DIAdem displays different y-channels in different colors.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DPalette](../../reportapi/objects/report_objects_irepd2paletteint.htm) object.

| Color | Specifies the color of the y-channel. |
| --- | --- |
| Y-channel | Specifies the y-channel of the color. Depending on the display mode, you specify different properties: YChannels for 2DGroupedBars and YChannels for 2DStackedBars. |
| Limit number of colors | Specifies whether the number of palette colors is limited. |
| Number of colors | Specifies the number of palette colors. |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d/dlgcolorcombisettings_dialog.htm language=enus -->
## TOPIC 00418: Combined Settings

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d/dlgcolorcombisettings_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d/dlgcolorcombisettings_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Add Curves](../graph_dlg_2d_tab/d2axis_tab_newcurve_dialog.htm) | [Global Color Palette](../graph_dlg_menu/dlgpicpal_dialog.htm)) > [Color Palette](../graph_dlg_2d/dlgd2colorpal_dialog.htm) > Combined Settings

Combined Settings

Use this dialog box to apply the specified line properties to all palette entries selected in the color palette.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DPalette](../../reportapi/objects/report_objects_irepd2paletteint.htm) object.

| Line color | Specifies the colors of the selected interval sections. |
| --- | --- |
| Line style | Specifies the line style of the selected interval sections. |
| Line width | Specifies the line widths of the selected interval sections. |
| Line interval | Specifies the distance and the length of the line sections for broken line style within the selected interval section. |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d/dlgd2colorpal_dialog.htm language=enus -->
## TOPIC 00419: Color Palette

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d/dlgd2colorpal_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d/dlgd2colorpal_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Add Curves](../graph_dlg_2d_tab/d2axis_tab_newcurve_dialog.htm) | [Global Color Palette](../graph_dlg_menu/dlgpicpal_dialog.htm)) > Color Palette

Color Palette

Use this dialog box to specify the color ranges for the **Palette** line color in a 2D axis system or a polar axis system. DIAdem displays different y-ranges in different colors.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DPalette](../../reportapi/objects/report_objects_irepd2paletteint.htm) object.

| Number of colors | Specifies the number of palette colors. |
| --- | --- |
| Color allocation according to | Specifies how DIAdem assigns the colors to the ranges. For the settings Scaling domain of axis, Distance between axis ticks, and Input interval of the palette the colors correspond with the y-ranges of the curve. For other settings you specify a color channel that DIAdem uses for displaying the curve in the palette colors. |
| Lower interval limit | Specifies the lower limit of the y-range in which DIAdem displays the color palette. DIAdem displays the curve in the first palette color from the beginning of the curve to the lower interval limit. |
| Upper interval limit | Specifies the upper limit of the y-range in which DIAdem displays the color palette. DIAdem displays the curve in the last palette color from the end of the curve to the upper interval limit. |
| Color channel | Specifies the channel with the values that DIAdem uses to display the curve in the colors of the palette. |
| Color | Specifies the color of the interval section. |
| Line style | Specifies the line style of the interval section. |
| Width | Specifies the line width of the interval section. |
| Line interval | Specifies the interval and the length of the line sections for broken line style within the interval section. |
| Color in BordersFrom | Specifies the lowest value of the interval in which DIAdem displays the color, for Color allocation according to»Input values. The values must be ascending. |
| Color in BordersTo | Specifies the highest value of the interval in which DIAdem displays the color, for Color allocation according to»Input values. The values must be ascending. |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_bar_label_text_dialog.htm language=enus -->
## TOPIC 00420: Curve Parameters: Bars » Label » Text

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_bar_label_text_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_bar_label_text_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) | [Stacked Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm)) > [Labels](../graph_dlg_2d_curve/d2axis_labeling_general.htm) > Curve Parameters: Bars » Label » Text

Curve Parameters: Bars » Label » Text

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalLabel](../../reportapi/objects/report_objects_irepd2labeladditionalint.htm) object.

|  | Free text | Specifies whether the curve end labels contain free text. Free text includes symbols or texts that DIAdem displays at the curve points. |
| --- | --- | --- |
|  | Open Dialog Box | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | X-value | Specifies whether DIAdem displays the x-coordinates at the curve points. |
|  | Format | Specifies the format specifications for the x-values of the 2D curve label. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | Y-value | Specifies whether DIAdem displays the y-coordinates at the curve points. |
|  | Format | Specifies the format specifications for the y-values of the 2D curve label. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | Value index | Specifies that DIAdem displays the point numbers at the curve points. |
|  | Format | Specifies the format specifications for the curve label of the point number in the 2D curve. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | From channel | Specifies whether DIAdem labels the 2D curve with texts from a different channel. |
|  | Channel | Specifies the additional channel from which DIAdem takes the label for the 2D curve.You can use the texts from a text channel, the assignments of an Assignment channel, or the EnumValues of an Enumeration channel as a label. |
|  | Format | Specifies the format specifications for the curve label when DIAdem takes the values from an additional channel. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | Index channel | Specifies the channel from which DIAdem takes the positions for the curve labels at the 2D curve.If you use an Assignment channel for the label, DIAdem does not need an index channel for the positioning. The values or the value ranges specify the assignment of the positions at the 2D curve. |
|  | Separator | Specifies the separators that DIAdem uses between the text of the curve label. |
|  | Labels only for first curve | Specifies that DIAdem displays the curve labels only for the first curve, if you select the name-oriented mode and the curve expansion mode. |
|  |  |  |
|  | Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | Label » Text | [Label » Position](../graph_dlg_2d_curve/d2axis_curve_par_bar_label_pos_dialog.htm) | [Label » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_bar_label_textpar_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | Grouped bars | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Procedures

[Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm)

#### Examples

[2D Axis Systems with Different Curve Labels](../../exploff/examples/expl_report_av33.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm language=enus -->
## TOPIC 00421: Curve Parameters: Differential

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > Curve Parameters: Differential

Curve Parameters: Differential

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DDifferentialSettings](../../reportapi/objects/report_objects_irepd2shapeobjdifferentialsettingsint.htm) object.

| Line color | Specifies the color of the differential curve. |
| --- | --- |
| Line style | Specifies the line style. |
| Line width | Specifies the line width. |
| Line interval | Specifies the interval and the length of the line sections for broken lines. |
| Width | Specifies the width of the bars or the width of the upper and lower lines. |
| Offset | Specifies the offset of the upper and lower lines. |
| Filling | Specifies the type of bar filling. |
| Color | Specifies the color of the bar filling. |
| Line width | Specifies the line width for the bar filling. |
| Filling density | Specifies the hatching density of the bar filling. |
| Range/Bars | Specifies whether DIAdem displays ranges or bars. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | Differential | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[2D Axis Systems with Bar Display and Differential Display](../../exploff/examples/expl_report_av6.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm language=enus -->
## TOPIC 00422: Curve Parameters: Filled Area

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > Curve Parameters: Filled Area

Curve Parameters: Filled Area

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DFilledAreaSettings](../../reportapi/objects/report_objects_irepd2shapeobjfilledareasettingsint.htm) object.

| Line color | Specifies the color of the curve. |
| --- | --- |
| Line style | Specifies the line style. |
| Line width | Specifies the line width. |
| Line interval | Specifies the interval and the length of the line sections for broken lines. |
| Filling color | Specifies the type of bar filling. |
| Filling mode | Specifies whether the color shading relates to the curve or to the axis. If the color shading relates to the axis, DIAdem does not use the entire color spectrum of a color shading for shorter curves. In this case, however, it is easier to compare different curves. |
| Transparency | Specifies the transparency of the filling in a 2D axis system. A value of 100 is completely transparent, a value of 0 is opaque. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | Filled area | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

|  | Note For curves with many thousands of points, DIAdem does not draw a filling because the Windows drawing routines used do not support this. Use the resampling feature to, for example, reduce the amount of data. |
| --- | --- |

#### Examples

[2D Axis System with Filled Curve Area and Color Shading in Background](../../exploff/examples/report_filled.htm) | [2D Axis Systems with Bar Display and Differential Display](../../exploff/examples/expl_report_av6.htm) | [2D Axis Systems with Bar Displays](../../exploff/examples/expl_report_av31.htm) | [2D Axis Systems with Grouped Bars](../../exploff/examples/expl_report_2dbars_3.htm) | [2D Axis Systems with Stacked Bars](../../exploff/examples/expl_report_2dbars_2.htm) | [3D Axis System with Bar and Waterfall Display](../../exploff/examples/expl_report_av14.htm) | [Pareto Diagram](../../exploff/examples/expl_pareto.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm language=enus -->
## TOPIC 00423: Curve Parameters: Grouped Bars

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > Curve Parameters: Grouped Bars

Curve Parameters: Grouped Bars

Use this dialog box to specify how DIAdem displays grouped bars in 2D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DBarsSettings](../../reportapi/objects/report_objects_irepd2shapeobjbarssettingsint.htm) object.

| Line color | Specifies the color of the curve. |
| --- | --- |
| Line style | Specifies the line style. |
| Line width | Specifies the line width. |
| Line interval | Specifies the interval and the length of the line sections for broken lines. |
| Width | Specifies the width of the bars or the width of the upper and lower lines. |
| Group distance | Specifies the offset for the bars. |
| Display mode | Specifies whether DIAdem displays 2D bars or 3D bars. |
| Filling color | Specifies the color of the bar filling. |
| Filling | Specifies the type of bar filling. |
| Color | Specifies the color of the bar filling. |
| Line width | Specifies the line width for the bar filling. |
| Filling density | Specifies the hatching density of the bar filling. |
|  |  |
| Color Palette | Opens the dialog box where you specify the y-channel color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting appears only if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

Grouped Bars | [Label » Text](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_label_text_dialog.htm) | [Label » Position](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_label_pos_dialog.htm) | [Label » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_label_textpar_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | Grouped bars | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[2D Axis System with Filled Curve Area and Color Shading in Background](../../exploff/examples/report_filled.htm) | [2D Axis Systems with Bar Display and Differential Display](../../exploff/examples/expl_report_av6.htm) | [2D Axis Systems with Bar Displays](../../exploff/examples/expl_report_av31.htm) | [2D Axis Systems with Grouped Bars](../../exploff/examples/expl_report_2dbars_3.htm) | [2D Axis Systems with Stacked Bars](../../exploff/examples/expl_report_2dbars_2.htm) | [3D Axis System with Bar and Waterfall Display](../../exploff/examples/expl_report_av14.htm) | [Pareto Diagram](../../exploff/examples/expl_pareto.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm language=enus -->
## TOPIC 00424: Curve Parameters: Horizontal Bars

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > Curve Parameters: Horizontal Bars

Curve Parameters: Horizontal Bars

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DBarsHorizontalSettings](../../reportapi/objects/report_objects_irepd2shapeobjbarshorizontalsettingsint.htm) object.

| Line color | Specifies the color of the curve. |
| --- | --- |
| Line style | Specifies the line style. |
| Line width | Specifies the line width. |
| Line interval | Specifies the interval and the length of the line sections for broken lines. |
| Width | Specifies the width of the bars or the width of the upper and lower lines. |
| Offset | Specifies the offset for the bars. |
| Display mode | Specifies whether DIAdem displays 2D bars or 3D bars. |
| Filling | Specifies the type of bar filling. |
| Color | Specifies the color of the bar filling. |
| Line width | Specifies the line width for the bar filling. |
| Filling density | Specifies the hatching density of the bar filling. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | Horizontal bars | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[2D Axis System with Filled Curve Area and Color Shading in Background](../../exploff/examples/report_filled.htm) | [2D Axis Systems with Bar Display and Differential Display](../../exploff/examples/expl_report_av6.htm) | [2D Axis Systems with Bar Displays](../../exploff/examples/expl_report_av31.htm) | [2D Axis Systems with Grouped Bars](../../exploff/examples/expl_report_2dbars_3.htm) | [2D Axis Systems with Stacked Bars](../../exploff/examples/expl_report_2dbars_2.htm) | [3D Axis System with Bar and Waterfall Display](../../exploff/examples/expl_report_av14.htm) | [Pareto Diagram](../../exploff/examples/expl_pareto.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm language=enus -->
## TOPIC 00425: Curve Parameters: Horizontal Spikes

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > Curve Parameters: Horizontal Spikes

Curve Parameters: Horizontal Spikes

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DSpikesSettings](../../reportapi/objects/report_objects_irepd2shapeobjspikessettingsint.htm) object.

| Line color | Specifies the color of the horizontal spikes. |
| --- | --- |
| Line style | Specifies the line style. |
| Line width | Specifies the line width. |
| Line interval | Specifies the interval and the length of the line sections for broken lines. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | Horizontal spikes | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[2D Axis Systems with Spike Displays and Constants](../../exploff/examples/expl_report_av38.htm) | [3D Axis System with Spike Display](../../exploff/examples/expl_report_av19.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbar_curve_dialog.htm language=enus -->
## TOPIC 00426: Curve Parameters: Line » Deviations » Curve Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbar_curve_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbar_curve_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line](../graph_dlg_2d_curve/d2axis_line_general.htm) > [Deviations](../graph_dlg_2d_curve/d2axis_deviation_general.htm) > Curve Parameters: Line » Deviations » Curve Parameters

Curve Parameters: Line » Deviations » Curve Parameters

Use this dialog box to specify how DIAdem displays error bars in 2D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalErrorBars](../../reportapi/objects/report_objects_irepd2errorbarsadditionalint.htm) object.

| Line color | Specifies the color of the error bars. If you select Same Color as Curve, you specify that DIAdem displays the error bars the same color as the curve. |
| --- | --- |
| Line width | Specifies the line width of the error bars. |
| Marker style | Specifies whether DIAdem displays only lines or lines with caps. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_line_marker_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbarx_dialog.htm) | Deviations » Curve Parameters

#### Other Curve Displays

Line | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[Error Bar Display](../../exploff/examples/expl_script_av6.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbarx_dialog.htm language=enus -->
## TOPIC 00427: Curve Parameters: Line » Deviations » X-Error Bars

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbarx_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbarx_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line](../graph_dlg_2d_curve/d2axis_line_general.htm) > [Deviations](../graph_dlg_2d_curve/d2axis_deviation_general.htm) > Curve Parameters: Line » Deviations » X-Error Bars

Curve Parameters: Line » Deviations » X-Error Bars

Use this dialog box to specify how DIAdem displays error bars in 2D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [ErrorBar](../../reportapi/objects/report_objects_ireperrorbarint.htm) object.

| Display | Specifies whether and in which direction DIAdem plots error bars. |
| --- | --- |
| Error amount | Specifies how DIAdem determines the error amount. |
| Fixed value | Specifies which value DIAdem plots as the error amount. |
| Percentage | Specifies which percentage of the current value DIAdem plots as the error amount. |
| Standard deviation | Specifies whether DIAdem plots the Standard deviation of the current value as the error amount. |
| Standard error | Specifies whether DIAdem plots the standard error of the current value as the error amount. The standard error is the quotient of the Standard deviation and the root of the number of values. |
| From channel | Specifies whether DIAdem reads the error amount from a channel. |
| + | Specifies the channel from which DIAdem reads the error amount in positive direction. |
| - | Specifies the channel from which DIAdem reads the error amount in negative direction. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_line_marker_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbary_dialog.htm) | Deviations » X-Error Bars | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbar_curve_dialog.htm)

#### Other Curve Displays

Line | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[Error Bar Display](../../exploff/examples/expl_script_av6.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbary_dialog.htm language=enus -->
## TOPIC 00428: Curve Parameters: Line » Deviations » Y-Error Bars

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbary_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_errorbary_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line](../graph_dlg_2d_curve/d2axis_line_general.htm) > [Deviations](../graph_dlg_2d_curve/d2axis_deviation_general.htm) > Curve Parameters: Line » Deviations » Y-Error Bars

Curve Parameters: Line » Deviations » Y-Error Bars

Use this dialog box to specify how DIAdem displays error bars in 2D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [ErrorBar](../../reportapi/objects/report_objects_ireperrorbarint.htm) object.

| Display | Specifies whether and in which direction DIAdem plots error bars. |
| --- | --- |
| Error amount | Specifies how DIAdem determines the error amount. |
| Fixed value | Specifies which value DIAdem plots as the error amount. |
| Percentage | Specifies which percentage of the current value DIAdem plots as the error amount. |
| Standard deviation | Specifies whether DIAdem plots the Standard deviation of the current value as the error amount. |
| Standard error | Specifies whether DIAdem plots the standard error of the current value as the error amount. The standard error is the quotient of the Standard deviation and the root of the number of values. |
| From channel | Specifies whether DIAdem reads the error amount from a channel. |
| + | Specifies the channel from which DIAdem reads the error amount in positive direction. |
| - | Specifies the channel from which DIAdem reads the error amount in negative direction. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_line_marker_dialog.htm) | Deviations » Y-Error Bars | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbar_curve_dialog.htm)

#### Other Curve Displays

Line | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[Error Bar Display](../../exploff/examples/expl_script_av6.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_marker_dialog.htm language=enus -->
## TOPIC 00429: Curve Parameters: Line » Markers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_marker_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_line_marker_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line](../graph_dlg_2d_curve/d2axis_line_general.htm) > Curve Parameters: Line » Markers

Curve Parameters: Line » Markers

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalMarker](../../reportapi/objects/report_objects_irepd2markeradditionalint.htm) object.

| Marker style | Specifies the symbol for the markers on the curve. |
| --- | --- |
| Line width | Specifies the line width of the markers. |
| Size | Specifies the size of the markers. |
| Size from channel | Specifies the channel whose values DIAdem uses for the size of the markers. |
| Display from [%] | Specifies the minimum size from which DIAdem draws the marker. |
| Marker color | Specifies the color of the markers. If you select Same Color as Curve, DIAdem displays the markers the same color as the curve. |
| Filling color | Specifies the filling color of the markers. If you select Same Color as Curve, you specify that DIAdem displays the marker filling the same color as the curve. |
| Repeat marker | Specifies the frequency of the markers. |
| Every n points | Specifies that DIAdem only displays the markers at every nth point on the curve. |
| Every n percent | Specifies that DIAdem displays the markers at every n percent. First DIAdem specifies the distance that corresponds with the percentage value of the diagonal of the diagram area. DIAdem applies this distance along the curve and plots the labels at the next point. |
| Maximum n points | Specifies that DIAdem displays a maximum of n markers. |
| Also at curve begin | Specifies that DIAdem displays a marker at the beginning of the curve. |
| Also at curve end | Specifies that DIAdem displays a marker at the end of the curve. |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | Markers | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbary_dialog.htm)| [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_line_errorbar_curve_dialog.htm)

#### Other Curve Displays

Line | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_text_dialog.htm language=enus -->
## TOPIC 00430: Curve Parameters: Line and Points » Curve End Labels » Text

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_text_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_text_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) > [Curve End Labels](../graph_dlg_2d_curve/d2axis_curveendlabeling_general.htm) > Curve Parameters: Line and Points » Curve End Labels » Text

Curve Parameters: Line and Points » Curve End Labels » Text

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [AdditionalLineEndLabel](../../reportapi/objects/report_objects_ireplineendlabeladditionalint.htm) object.

|  | Label | Specifies whether DIAdem labels the curve end with user defined text or with default text. |
| --- | --- | --- |
|  | Free text | Specifies text for the curve end labels. The text may also contain @@ expressions, such as @@MyFunc(Par)@@, but not more than one @@ expression. |
|  | Text Input Tool | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | To be labeled | Specifies which curve point DIAdem labels. |
|  | Labels only for first curve | Specifies that DIAdem displays the curve end labels only for the first curve, if you select the name-oriented mode and the curve expansion mode. |
|  | Label each curve section between NoValues | Specifies that DIAdem labels each curve section that is between two NoValues. |
|  | X-coordinate | Specifies whether DIAdem displays the curve end labels at the x-value of the curve point or offset to the x-value. |
|  | Y-coordinate | Specifies whether DIAdem displays the curve end labels at the y-value of the curve point or offset to the y-value. |
|  | X-axis | Specifies the horizontal offset of the curve end labels as a percentage. |
|  | Y-axis | Specifies the vertical offset of the curve end labels as a percentage. |
|  |  |  |
|  | Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_linesym_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_textpar_dialog.htm) | Curve End Label » Text |  [Curve End Labels» Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_textpar_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | Line and points | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box-whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_textpar_dialog.htm language=enus -->
## TOPIC 00431: Curve Parameters: Line and Points » Curve End Labels » Text Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_textpar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_textpar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) > [Curve End Labels](../graph_dlg_2d_curve/d2axis_curveendlabeling_general.htm) > Curve Parameters: Line and Points » Curve End Labels » Text Parameters

Curve Parameters: Line and Points » Curve End Labels » Text Parameters

Use this dialog box to specify whether you label curves with values or with free text. The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAxisSystem](../../reportapi/objects/report_objects_irepd2axisint.htm) object.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [AdditionalLineEndLabel](../../reportapi/objects/report_objects_ireplineendlabeladditionalint.htm) object.

| Font | Specifies the font for the curve end labels. |
| --- | --- |
| Font size | Specifies the font size for the curve end labels. |
| Font color | Specifies the color of the curve end labels. If you select Same Color as Curve, you specify that DIAdem displays the curve end labels the same color as the curve. |
| Highlighting color | Specifies the color with which you highlight the curve end labels. Use the Transparency setting to specify the highlighting intensity. |
| Angle | Specifies the angle of the curve end label. |
| Position | Specifies the position of the curve end label in relation to the curve. |
| Bold | Specifies whether DIAdem uses bold font to display the curve end labels. |
| Italics | Specifies whether DIAdem uses italic font to display the curve end labels. |
| Underline | Specifies whether DIAdem uses underline font to display the curve end labels. |
| Strikethrough | Specifies whether DIAdem uses strikethrough font to display the curve end labels. |
| Frame | Specifies whether DIAdem frames each curve end label. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_linesym_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_textpar_dialog.htm) | [Curve End Label » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_text_dialog.htm) |  Curve End Labels» Text Parameters | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | Line and points | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box-whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Procedures

[Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm)

#### Examples

[2D Axis Systems with Different Curve Labels](../../exploff/examples/expl_report_av33.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbar_curve_dialog.htm language=enus -->
## TOPIC 00432: Curve Parameters: Line and Points » Deviations » Curve Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbar_curve_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbar_curve_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) > [Deviations](../graph_dlg_2d_curve/d2axis_linesymbol_deviation_general.htm) > Curve Parameters: Line and Points » Deviations » Curve Parameters

Curve Parameters: Line and Points » Deviations » Curve Parameters

Use this dialog box to specify how DIAdem displays error bars in 2D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [ErrorBar](../../reportapi/objects/report_objects_ireperrorbarint.htm) object.

| Line color | Specifies the color of the error bars. If you select Same Color as Curve, you specify that DIAdem displays the error bars the same color as the curve. |
| --- | --- |
| Line width | Specifies the line width of the error bars. |
| Marker style | Specifies whether DIAdem displays only lines or lines with caps. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_linesym_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_textpar_dialog.htm) | [Curve End Label » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_text_dialog.htm) |  [Curve End Labels» Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_textpar_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | Deviations » Curve Parameters

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | Line and points | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[Error Bar Display](../../exploff/examples/expl_script_av6.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbary_dialog.htm language=enus -->
## TOPIC 00433: Curve Parameters: Line and Points » Deviations » Y-Error Bars

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbary_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbary_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) > [Deviations](../graph_dlg_2d_curve/d2axis_linesymbol_deviation_general.htm) > Curve Parameters: Line and Points » Deviations » Y-Error Bars

Curve Parameters: Line and Points » Deviations » Y-Error Bars

Use this dialog box to specify how DIAdem displays error bars in 2D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [ErrorBar](../../reportapi/objects/report_objects_ireperrorbarint.htm) object.

| Display | Specifies whether and in which direction DIAdem plots error bars. |
| --- | --- |
| Error amount | Specifies how DIAdem determines the error amount. |
| Fixed value | Specifies which value DIAdem plots as the error amount. |
| Percentage | Specifies which percentage of the current value DIAdem plots as the error amount. |
| Standard deviation | Specifies whether DIAdem plots the Standard deviation of the current value as the error amount. |
| Standard error | Specifies whether DIAdem plots the standard error of the current value as the error amount. The standard error is the quotient of the Standard deviation and the root of the number of values. |
| From channel | Specifies whether DIAdem reads the error amount from a channel. |
| + | Specifies the channel from which DIAdem reads the error amount in positive direction. |
| - | Specifies the channel from which DIAdem reads the error amount in negative direction. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_linesym_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_textpar_dialog.htm) | [Curve End Label » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_text_dialog.htm) | [Curve End Labels» Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_textpar_dialog.htm) | Deviations » Y-Error Bars | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | Line and points | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Examples

[Error Bar Display](../../exploff/examples/expl_script_av6.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_label_pos_dialog.htm language=enus -->
## TOPIC 00434: Curve Parameters: Line and Points » Labels » Position

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_label_pos_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_linesym_label_pos_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) | [Stacked Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm)) > [Labels](../graph_dlg_2d_curve/d2axis_labeling_general.htm) > Curve Parameters: Line and Points » Labels » Position

Curve Parameters: Line and Points » Labels » Position

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DLabelPosition](../../reportapi/objects/report_objects_irepd2labelpositionint.htm) object.

| Position | Specifies how DIAdem positions the curve label in relation to the curve point. |
| --- | --- |
| Offset in x-direction | Specifies the fixed x-position of the curve label in relation to the axis origin. |
| Offset in y-direction | Specifies the fixed y-position of the curve label in relation to the axis origin. |
| Every point / Every nth point / Maximum n points / Every n percent | Specifies how DIAdem repeats the curve labeling. If you set Every n percent, DIAdem first specifies the distance that corresponds with the percent value of the diagonal of the diagram area. DIAdem applies this distance along the curve and plots the labels at the next point. |
| Also at curve begin | Specifies whether DIAdem displays the curve label at the beginning of the curve. |
| Also at curve end | Specifies whether DIAdem also displays the curve label at the end of the curve. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_linesym_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_text_dialog.htm) | Labels » Position | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_label_textpar_dialog.htm) | [Curve End Label » Text](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_text_dialog.htm) |  [Curve End Labels» Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_curveend_textpar_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_linesym_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | Line and points | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm language=enus -->
## TOPIC 00435: Curve Parameters: Special Combination » Curve End Labels » Text

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Special Combination](../graph_dlg_2d_curve/d2axis_speccombination_general.htm) > [Curve End Labels](../graph_dlg_2d_curve/d2axis_speccombination_curveend_general.htm) > Curve Parameters: Special Combination » Curve End Labels » Text

Curve Parameters: Special Combination » Curve End Labels » Text

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [AdditionalLineEndLabel](../../reportapi/objects/report_objects_ireplineendlabeladditionalint.htm) object.

|  | Label | Specifies whether DIAdem labels the curve end with user defined text or with default text. |
| --- | --- | --- |
|  | Free text | Specifies text for the curve end labels. |
|  | Text Input Tool | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | To be labeled | Specifies which curve point DIAdem labels. |
|  | Labels only for first curve | Specifies that DIAdem displays the curve end labels only for the first curve, if you select the name-oriented mode and the curve expansion mode. |
|  | Label each curve section between NoValues | Specifies that DIAdem labels each curve section that is between two NoValues. |
|  | X-coordinate | Specifies whether DIAdem displays the curve end labels at the x-value of the curve point or offset to the x-value. |
|  | Y-coordinate | Specifies whether DIAdem displays the curve end labels at the y-value of the curve point or offset to the y-value. |
|  | X-axis | Specifies the horizontal offset of the curve end labels as a percentage. |
|  | Y-axis | Specifies the vertical offset of the curve end labels as a percentage. |
|  |  |  |
|  | Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm) | Curve End Labels » Text | [Curve End Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm) | [Special Styles](../graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box-whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | Special combination

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm language=enus -->
## TOPIC 00436: Curve Parameters: Special Combination » Curve End Labels » Text Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Special Combination](../graph_dlg_2d_curve/d2axis_speccombination_general.htm) > [Curve End Labels](../graph_dlg_2d_curve/d2axis_speccombination_curveend_general.htm) > Curve Parameters: Special Combination » Curve End Labels » Text Parameters

Curve Parameters: Special Combination » Curve End Labels » Text Parameters

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [AdditionalLineEndLabel](../../reportapi/objects/report_objects_ireplineendlabeladditionalint.htm) object.

| Font | Specifies the font for the curve end labels. |
| --- | --- |
| Font size | Specifies the font size for the curve end labels. |
| Font color | Specifies the color of the curve end labels. If you select Same Color as Curve, you specify that DIAdem displays the curve end labels the same color as the curve. |
| Highlighting color | Specifies the color with which you highlight the curve end labels. Use the Transparency setting to specify the highlighting intensity. |
| Angle | Specifies the angle of the curve end label. |
| Position | Specifies the position of the curve end label in relation to the curve. |
| Bold | Specifies whether DIAdem uses bold font to display the curve end labels. |
| Italics | Specifies whether DIAdem uses italic font to display the curve end labels. |
| Underline | Specifies whether DIAdem uses underline font to display the curve end labels. |
| Strikethrough | Specifies whether DIAdem uses strikethrough font to display the curve end labels. |
| Frame | Specifies whether DIAdem frames each curve end label. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm) | [Curve End Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm) | Curve End Labels » Text Parameters | [Special Styles](../graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box-whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | Special combination

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm language=enus -->
## TOPIC 00437: Curve Parameters: Special Combination » Labels » Text

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Special Combination](../graph_dlg_2d_curve/d2axis_speccombination_general.htm) > [Labels](../graph_dlg_2d_curve/d2axis_speccombination_font_general.htm) > Curve Parameters: Special Combination » Labels » Text

Curve Parameters: Special Combination » Labels » Text

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalLabel](../../reportapi/objects/report_objects_irepd2labeladditionalint.htm) object.

|  | Free text | Specifies whether the curve end labels contain free text. Free text includes symbols or texts that DIAdem displays at the curve points. |
| --- | --- | --- |
|  | Text Input Tool | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | X-value | Specifies whether DIAdem displays the x-coordinates at the curve points. |
|  | Format | Specifies the format specifications for the x-values of the 2D curve label. |
|  | Format Numbers | Opens the dialog box where you select or enter the format specification. |
|  | Y-value | Specifies whether DIAdem displays the y-coordinates at the curve points. |
|  | Format | Specifies the format specifications for the y-values of the 2D curve label. |
|  | Value index | Specifies that DIAdem displays the point numbers at the curve points. |
|  | Format | Specifies the format specifications for the curve label of the point number in the 2D curve. |
|  | From channel | Specifies whether the text of the 2D curve label contains values from a different channel. |
|  | Channel | Specifies the additional channel from which DIAdem takes the label for the 2D curve. |
|  | Format | Specifies the format specifications for the curve label when DIAdem takes the values from an additional channel. |
|  | Index channel | Specifies the index channel for the additional channel from which DIAdem takes the curve label of the 2D curve. |
|  | Separator | Specifies the separators that DIAdem uses between the text of the curve label. |
|  | Labels only for first curve | Specifies that DIAdem displays the curve labels only for the first curve if you select the name-oriented mode and the curve expansion mode. |
|  |  |  |
|  | Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm) | Labels » Text | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_pos_dialog.htm)| [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm) | [Curve End Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm) | [Curve End Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm) | [Special Styles](../graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box-whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | Special combination

#### Examples

[2D Axis Systems with Different Curve Labels](../../exploff/examples/expl_report_av33.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm language=enus -->
## TOPIC 00438: Curve Parameters: Special Combination » Labels » Text Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Special Combination](../graph_dlg_2d_curve/d2axis_speccombination_general.htm) > [Labels](../graph_dlg_2d_curve/d2axis_speccombination_font_general.htm) > Curve Parameters: Special Combination » Labels » Text Parameters

Curve Parameters: Special Combination » Labels » Text Parameters

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalLabel](../../reportapi/objects/report_objects_irepd2labeladditionalint.htm) object.

| Font | Specifies the font for the curve labels. |
| --- | --- |
| Font size | Specifies the font size for the curve labels. |
| Font color | Specifies the color of the curve labels. |
| Highlighting color | Specifies the color with which you highlight the curve labels. Use the Transparency setting to specify the highlighting intensity. |
| Angle | Specifies the angle for the curve labels. |
| Position | Specifies the position of the curve labels in relation to the curve data points. |
| Bold | Specifies whether DIAdem uses bold font to display the curve labels. |
| Italics | Specifies whether DIAdem uses italic font to display the curve labels. |
| Underline | Specifies whether DIAdem uses underline font to display the curve labels. |
| Strikethrough | Specifies whether DIAdem uses strikethrough font to display the curve labels. |
| Frame | Specifies whether DIAdem frames each curve label. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the font color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_pos_dialog.htm) | Labels » Text Parameters | [Curve End Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm) | [Curve End Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm) | [Special Styles](../graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box-whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | Special combination

#### Examples

[2D Axis Systems with Different Curve Labels](../../exploff/examples/expl_report_av33.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm language=enus -->
## TOPIC 00439: Curve Parameters: Special Combination » Line

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Special Combination](../graph_dlg_2d_curve/d2axis_speccombination_general.htm) > Curve Parameters: Special Combination » Line

Curve Parameters: Special Combination » Line

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DSpecialCombinationSettings](../../reportapi/objects/report_objects_irepd2shapeobjspecialcombinationsettingsint.htm) object.

| Line color | Specifies the color of the curve. |
| --- | --- |
| Line style | Specifies the line style of the curve. |
| Line width | Specifies the line width of the curve. This setting does not apply for the Line and Points display mode if Palette is the line color. |
| Line interval | Specifies the interval and the length of the dashes for the broken line styles. This setting is dimmed if you select Palette as the line color with the Line and points display mode. |
| Connect curve points when NoValues occur | Specifies whether DIAdem connects NoValues in curves. |
| Smooth curve | Specifies whether DIAdem smoothes the curve between two data points of a 2D curve. |
| Expand curve | Specifies whether DIAdem expands a curve entry. This setting appears only if you select Settings»Layout Setup»Layout Parameters»Curve Expansion and then select the Expand curves checkbox. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm) | Labels » Text | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_pos_dialog.htm)| [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm) | [Curve End Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm) | [Curve End Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm) | [Special Styles](../graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | Special combination

|  | Note In non-monotonic curves with more than 100.000 points DIAdem does not plot a filling because the calculation takes too long. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm language=enus -->
## TOPIC 00440: Curve Parameters: Special Combination » Markers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Special Combination](../graph_dlg_2d_curve/d2axis_speccombination_general.htm) > Curve Parameters: Special Combination » Markers

Curve Parameters: Special Combination » Markers

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalMarker](../../reportapi/objects/report_objects_irepd2markeradditionalint.htm) object.

| Marker style | Specifies the symbol for the markers on the curve. |
| --- | --- |
| Line width | Specifies the line width of the markers. |
| Size | Specifies the size of the markers. |
| Size from channel | Specifies the channel whose values DIAdem uses for the size of the markers. |
| Display from [%] | Specifies the minimum size from which DIAdem draws the marker. |
| Marker color | Specifies the color of the markers. If you select Same Color as Curve, DIAdem displays the markers the same color as the curve. |
| Filling color | Specifies the filling color of the markers. If you select Same Color as Curve, you specify that DIAdem displays the marker filling the same color as the curve. |
| Repeat marker | Specifies the frequency of the markers. |
| Every n points | Specifies that DIAdem only displays the markers at every nth point on the curve. |
| Every n percent | Specifies that DIAdem displays the markers at every n percent. First DIAdem specifies the distance that corresponds with the percentage value of the diagonal of the diagram area. DIAdem applies this distance along the curve and plots the labels at the next point. |
| Maximum n points | Specifies that DIAdem displays a maximum of n markers. |
| Also at curve begin | Specifies that DIAdem displays a marker at the beginning of the curve. |
| Also at curve end | Specifies that DIAdem displays a marker at the end of the curve. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm) | Markers | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm) | [Curve End Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm) | [Curve End Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm) | [Special Styles](../graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm) | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | Special combination

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm language=enus -->
## TOPIC 00441: Curve Parameters: Special Combination » Special Styles

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_spec_spec_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Special Combination](../graph_dlg_2d_curve/d2axis_speccombination_general.htm) > Curve Parameters: Special Combination » Special Styles

Curve Parameters: Special Combination » Special Styles

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalStyles](../../reportapi/objects/report_objects_irepd2specialcombadditionalstylesint.htm) object.

| Type | Specifies the additional display mode for the curve, such as spikes, stairs, bars, or outline. |
| --- | --- |
| Color | Specifies the curve color for the additional display mode. |
| Line style | Specifies the line style. |
| Line width | Specifies the line width. |
| Line interval | Specifies the interval and the length of the line sections for broken lines. |
| Width | Specifies the width of the bars. |
| Offset | Specifies the offset for the bars. |
| Filling | Specifies the type of bar filling. |
| Filling color | Specifies the color of the bar filling. |
| Line width | Specifies the line width for the bar filling. |
| Filling density | Specifies the hatching density of the bar filling. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Line](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm) | [Markers](../graph_dlg_2d_curve/d2axis_curve_par_spec_marker_dialog.htm) | [Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_text_dialog.htm) | [Labels » Position](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_pos_dialog.htm) | [Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_label_textpar_dialog.htm) | [Curve End Labels » Text](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_text_dialog.htm) | [Curve End Labels » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_curveend_textpar_dialog.htm) | Special Styles | [Deviations » Y-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbary_dialog.htm) | [Deviations » X-Error Bars](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbarx_dialog.htm) | [Deviations » Curve Parameters](../graph_dlg_2d_curve/d2axis_curve_par_spec_errorbar_curve_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | Special combination

|  | Note You can specify only the line properties on the format bar in DIAdem REPORT for the display type Special combination. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_pos_dialog.htm language=enus -->
## TOPIC 00442: Curve Parameters: Stacked Bars » Label » Position

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_pos_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_pos_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) | [Stacked Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm)) > [Labels](../graph_dlg_2d_curve/d2axis_labeling_general.htm) > Curve Parameters: Stacked Bars » Label » Position

Curve Parameters: Stacked Bars » Label » Position

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DLabelPosition](../../reportapi/objects/report_objects_irepd2labelpositionint.htm) object.

| Position | Specifies how DIAdem positions the curve label in relation to the curve point. |
| --- | --- |
| Offset in x-direction | Specifies the fixed x-position of the curve label in relation to the axis origin. |
| Offset in y-direction | Specifies the fixed y-position of the curve label in relation to the axis origin. |
| Every point / Every nth point / Maximum n points / Every n percent | Specifies how DIAdem repeats the curve labeling. If you set Every n percent, DIAdem first specifies the distance that corresponds with the percent value of the diagonal of the diagram area. DIAdem applies this distance along the curve and plots the labels at the next point. |
| Also at curve begin | Specifies whether DIAdem displays the curve label at the beginning of the curve. |
| Also at curve end | Specifies whether DIAdem also displays the curve label at the end of the curve. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Label » Text](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_text_dialog.htm) | Label » Position | [Label » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_textpar_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | Stacked bars | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_text_dialog.htm language=enus -->
## TOPIC 00443: Curve Parameters: Stacked Bars » Label » Text

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_text_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_text_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) | [Stacked Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm)) > [Labels](../graph_dlg_2d_curve/d2axis_labeling_general.htm) > Curve Parameters: Stacked Bars » Label » Text

Curve Parameters: Stacked Bars » Label » Text

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalLabel](../../reportapi/objects/report_objects_irepd2labeladditionalint.htm) object.

|  | Free text | Specifies whether the curve end labels contain free text. Free text includes symbols or texts that DIAdem displays at the curve points. |
| --- | --- | --- |
|  | Open Dialog Box | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | X-value | Specifies whether DIAdem displays the x-coordinates at the curve points. |
|  | Format | Specifies the format specifications for the x-values of the 2D curve label. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | Y-value | Specifies whether DIAdem displays the y-coordinates at the curve points. |
|  | Format | Specifies the format specifications for the y-values of the 2D curve label. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | Value index | Specifies that DIAdem displays the point numbers at the curve points. |
|  | Format | Specifies the format specifications for the curve label of the point number in the 2D curve. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | From channel | Specifies whether DIAdem labels the 2D curve with texts from a different channel. |
|  | Channel | Specifies the additional channel from which DIAdem takes the label for the 2D curve.You can use the texts from a text channel, the assignments of an Assignment channel, or the EnumValues of an Enumeration channel as a label. |
|  | Format | Specifies the format specifications for the curve label when DIAdem takes the values from an additional channel. |
|  | Open Dialog Box | Opens the dialog box where you select or enter the format specification. |
|  | Index channel | Specifies the channel from which DIAdem takes the positions for the curve labels at the 2D curve.If you use an Assignment channel for the label, DIAdem does not need an index channel for the positioning. The values or the value ranges specify the assignment of the positions at the 2D curve. |
|  | Separator | Specifies the separators that DIAdem uses between the text of the curve label. |
|  | Labels only for first curve | Specifies that DIAdem displays the curve labels only for the first curve, if you select the name-oriented mode and the curve expansion mode. |
|  |  |  |
|  | Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | Label » Text | [Label » Position](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_pos_dialog.htm) | [Label » Text Parameters](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_textpar_dialog.htm)

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | Stacked bars | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Procedures

[Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm)

#### Examples

[2D Axis Systems with Different Curve Labels](../../exploff/examples/expl_report_av33.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_textpar_dialog.htm language=enus -->
## TOPIC 00444: Curve Parameters: Stacked Bars » Label » Text Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_textpar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_textpar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) | [Stacked Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm)) > [Labels](../graph_dlg_2d_curve/d2axis_labeling_general.htm) > Curve Parameters: Stacked Bars » Label » Text Parameters

Curve Parameters: Stacked Bars » Label » Text Parameters

Use this dialog box to specify whether you label curves with values or with free text.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAdditionalLabel](../../reportapi/objects/report_objects_irepd2labeladditionalint.htm) object.

| Font | Specifies the font for the curve labels. |
| --- | --- |
| Font size | Specifies the font size for the curve labels. |
| Font color | Specifies the color of the curve labels. |
| Highlighting color | Specifies the color with which you highlight the curve labels. Use the Transparency setting to specify the highlighting intensity. |
| Angle | Specifies the angle for the curve labels. |
| Position | Specifies the position of the curve labels in relation to the curve data points. For stacked bars, the relative position of the curve label does not refer to the curve support point, but to the bar area: At the top, for example, the upper edge of the bar means and centers the center of the bar. |
| Bold | Specifies whether DIAdem uses bold font to display the curve labels. |
| Italics | Specifies whether DIAdem uses italic font to display the curve labels. |
| Underline | Specifies whether DIAdem uses underline font to display the curve labels. |
| Strikethrough | Specifies whether DIAdem uses strikethrough font to display the curve labels. |
| Frame | Specifies whether DIAdem frames each curve label. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the font color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | [Label » Text](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_text_dialog.htm) | [Label » Position](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_label_pos_dialog.htm) | Label » Text Parameters

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | Stacked bars | [Outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm) | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box-whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

#### Procedures

[Labeling Curve Points with Text in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_curvelabel.htm) | [Labeling Curve Points with X-Values in 2D Axis Systems](../../procpresent/axis_systems/procpres_2daxis_symbols.htm)

#### Examples

[2D Axis Systems with Different Curve Labels](../../exploff/examples/expl_report_av33.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm language=enus -->
## TOPIC 00445: Curve Parameters: Outlined Bars

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_curve_par_stair_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > Curve Parameters: Outlined Bars

Curve Parameters: Outlined Bars

Use this dialog box to specify how DIAdem displays curves in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DOutlineBarsSettings](../../reportapi/objects/report_objects_irepd2shapeobjoutlbarssettingsint.htm) object.

| Line color | Specifies the color of the curve. |
| --- | --- |
| Line style | Specifies the line style. |
| Line width | Specifies the line width. |
| Line interval | Specifies the interval and the length of the line sections for broken lines. |
| Filling color | Specifies the color for the filled area under the curve. Use the setting Filling Effects to plot color shading. |
| Filling mode | Specifies whether filling effects relate to the curve or to the axis. If the filling effect relates to the axis, DIAdem does not use the entire color spectrum of a color shading for shorter curves. In this case, however, it is easier to compare different curves. |
| Transparency | Specifies the transparency of the filling in a 2D axis system. A value of 100 is completely transparent, a value of 0 is opaque. |
| Stair/Bars | Specifies whether DIAdem outlines stairs or bars. In stair outlines, the interpolation points of the curve are on the data points. In bar outlines, the interpolation points of the curve are exactly in the middle between two neighboring data points. |
|  |  |
| Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Other Curve Displays

[Line](../graph_dlg_2d_curve/d2axis_curve_par_line_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_curve_par_linesym_line_dialog.htm) | [Spikes](../graph_dlg_2d_curve/d2axis_curve_par_spike_dialog.htm) | [Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Stacked bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm) | Outlined bars | [Differential](../graph_dlg_2d_curve/d2axis_curve_par_diff_dialog.htm) | [Filled area](../graph_dlg_2d_curve/d2axis_curve_par_filled_dialog.htm) | [Constant](../graph_dlg_2d_curve/d2axis_curve_par_const_line_dialog.htm) | [Coordinate](../graph_dlg_2d_curve/d2axis_curve_par_coordinate_marker_dialog.htm) | [Box whisker](../graph_dlg_2d_curve/d2axis_curve_par_boxplot_box_dialog.htm) | [Horizontal spikes](../graph_dlg_2d_curve/d2axis_curve_par_horspike_dialog.htm) | [Horizontal bars](../graph_dlg_2d_curve/d2axis_curve_par_horbar_dialog.htm) | [Horizontal outlined bars](../graph_dlg_2d_curve/d2axis_curve_par_horstair_dialog.htm) | [Special combination](../graph_dlg_2d_curve/d2axis_curve_par_spec_line_dialog.htm)

|  | Note In non-monotonic curves with more than 100.000 points DIAdem does not plot a filling because the calculation takes too long. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_deviation_general.htm language=enus -->
## TOPIC 00446: Deviations

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_deviation_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_deviation_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) > [Curve Parameters](../graph_dlg_2d_curve/d2axis_curveparameters_general.htm) > [Line](../graph_dlg_2d_curve/d2axis_line_general.htm) > Deviations

Deviations

The following topics describe the dialog boxes where you make your settings for the error bars in line display.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_labeling_general.htm language=enus -->
## TOPIC 00447: Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_labeling_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_labeling_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Bars](../graph_dlg_2d_curve/d2axis_curve_par_bar_dialog.htm) | [Grouped Bars](../graph_dlg_2d_curve/d2axis_curve_par_grouped_bar_dialog.htm) | [Line and points](../graph_dlg_2d_curve/d2axis_linesymbol_general.htm) | [Stacked Bars](../graph_dlg_2d_curve/d2axis_curve_par_stacked_bar_dialog.htm)) > Labels

Labels

The following topics describe the dialog boxes in which you configure the curve labels in a 2D axis system.where you make your settings for curves in 2D axis systems.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_curve/d2axis_systems_general.htm language=enus -->
## TOPIC 00448: 2D Axis Systems

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_curve/d2axis_systems_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_curve/d2axis_systems_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > 2D Axis Systems

2D Axis Systems

The following topics describe the dialog boxes where you make your settings for 2D axis systems and curves.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_legend/d2axis_colorlegend_tab_general_dialog.htm language=enus -->
## TOPIC 00449: Color Legend: General

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_legend/d2axis_colorlegend_tab_general_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_legend/d2axis_colorlegend_tab_general_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) > Color Legend: General

Color Legend: General

Use this dialog box to specify the color legend display in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [ColorLegendSettings](../../reportapi/objects/report_objects_irepcolorlegendsettingsint.htm) object.

| Frame entire legend | Specifies whether DIAdem frames the legend. |
| --- | --- |
| Color for all frames | Specifies the color of the frame. |
| Line width | Specifies the line width of the frame. |
| Background color | Specifies the background color for the color legend. Use the setting Filling Effects to plot color shading. |
| Legend symbols | Specifies how DIAdem displays the symbols in the color legend. |
| Frame around symbols | Specifies whether DIAdem frames the color legend symbols. |

#### Further Settings

General | [Color Labels](../graph_dlg_2d_legend/d2axis_colorlegend_tab_label_dialog.htm) | [Text Parameters](../graph_dlg_2d_legend/d2axis_colorlegend_tab_textparameter_dialog.htm) | [Title](../graph_dlg_2d_legend/d2axis_colorlegend_tab_header_dialog.htm) | [Size](../graph_dlg_2d_legend/d2axis_colorlegend_tab_size_dialog.htm) | [Position](../graph_dlg_2d_legend/d2axis_colorlegend_tab_position_dialog.htm)

#### Procedures

[Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm)

#### Examples

[2D Axis System with a Legend](../../exploff/examples/expl_report_av7.htm) | [2D Axis Systems and 3D Axis Systems with Legends](../../exploff/examples/expl_report_av34.htm) | [3D Axis System with Surface Display and a Color Legend](../../exploff/examples/expl_report_av20.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_legend/d2axis_colorlegend_tab_header_dialog.htm language=enus -->
## TOPIC 00450: Color Legend: Title Line

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_legend/d2axis_colorlegend_tab_header_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_legend/d2axis_colorlegend_tab_header_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) > [Color Legend](../graph_dlg_2d_legend/d2axis_colorlegend_tab_general_dialog.htm) > Color Legend: Title Line

Color Legend: Title Line

Use this dialog box to specify the title display for the color legend in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [ColorLegendHeader](../../reportapi/objects/report_objects_irepcolorlegendheaderint.htm) object.

|  | Title text | Specifies the text of the headline in the color legend. |
| --- | --- | --- |
|  | Text Entry Help | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | Text field size as % | Specifies the area for color legend labels as a percentage of the page size. |
|  | Text field boundary | Specifies whether a line separates the text field. |
|  | Text field position | Specifies the relative position of the text field within the color legend. |
|  | Label angle | Specifies the label angle. |
|  | Font | Specifies the font for the title. |
|  | Font size automatic | Specifies whether DIAdem automatically adjusts the font size of the text in the text box to the available space. If you do not select the property, DIAdem specifies the font size automatically. |
|  | Font size | Specifies the font size for the title. |
|  | Font color | Specifies the font color for the title. |
|  | Highlighting color | Specifies the color in which you highlight the title. Use the Transparency setting to specify the highlighting intensity. |
|  | Bold | Specifies whether DIAdem uses bold font to display the title. |
|  | Italics | Specifies whether DIAdem uses italic font to display the title. |
|  | Underline | Specifies whether DIAdem uses underline font to display the title. |
|  | Strikethrough | Specifies whether DIAdem uses strikethrough font to display the title. |
|  |  |  |
|  | Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[General](../graph_dlg_2d_legend/d2axis_colorlegend_tab_general_dialog.htm) | [Color Labels](../graph_dlg_2d_legend/d2axis_colorlegend_tab_label_dialog.htm) | [Text Parameters](../graph_dlg_2d_legend/d2axis_colorlegend_tab_textparameter_dialog.htm) | Title | [Size](../graph_dlg_2d_legend/d2axis_colorlegend_tab_size_dialog.htm) | [Position](../graph_dlg_2d_legend/d2axis_colorlegend_tab_position_dialog.htm)

#### Procedures

[Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm)

#### Examples

[2D Axis System with a Legend](../../exploff/examples/expl_report_av7.htm) | [2D Axis Systems and 3D Axis Systems with Legends](../../exploff/examples/expl_report_av34.htm) | [3D Axis System with Surface Display and a Color Legend](../../exploff/examples/expl_report_av20.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_legend/d2axis_legend_tab_size_dialog.htm language=enus -->
## TOPIC 00451: Legend: Size

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_legend/d2axis_legend_tab_size_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_legend/d2axis_legend_tab_size_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) > [Legend](../graph_dlg_2d_legend/d2axis_legend_tab_general_dialog.htm) > Legend: Size

Legend: Size

Use this dialog box to specify the size of the legend in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [LegendPosition](../../reportapi/objects/report_objects_ireplegendpositionint.htm) object.

| Specify the size of the entire legend / Specify the size of the legend entries | Specifies whether the height and width refer to the entire legend or only to single curve entries. If you select the setting Specify the size of the entire legend, the legend size is unrelated to the number of legend entries. If you select the setting Specify the size of the legend entries, DIAdem adapts the legend size to the number of legend entries. |
| --- | --- |
| Height of entire legend in % | Specifies the height of the entire legend if you select Specify the size of the entire legend. |
| Height of entry in % | Specifies the height of a curve entry in the legend if you select Automatic legend size. |
| Width of entire legend in %. | Specifies the width of the entire legend if you select Specify the size of the entire legend. |
| Width of entry in % | Specifies the width of a curve entry in the legend if you select Automatic legend size. |
| Orientation | Specifies how DIAdem aligns the elements. If the orientation is set to Automatic, DIAdem aligns the legend vertically when the height/width ratio is greater than 0.7, otherwise the alignment is horizontal. |
| Portion of symbol field | Specifies the size of the color field as a percentage of the entire legend size. |
| Angle | Specifies the angle the legend is displayed at. If a legend has several columns, you cannot rotate the legend. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

|  | Note DIAdem ignores the setting Specify the size of the legend entries if Orientation has the value Automatic. |
| --- | --- |

#### Further Settings

[General](../graph_dlg_2d_legend/d2axis_legend_tab_general_dialog.htm) | [Labels](../graph_dlg_2d_legend/d2axis_legend_tab_label_dialog.htm) | [Text Parameters](../graph_dlg_2d_legend/d2axis_legend_tab_textparameter_dialog.htm) | [Title Parameters](../graph_dlg_2d_legend/d2axis_legend_tab_header_dialog.htm) | Size | [Position](../graph_dlg_2d_legend/d2axis_legend_tab_position_dialog.htm)

#### Procedures

[Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm)

#### Examples

[2D Axis System with a Legend](../../exploff/examples/expl_report_av7.htm) | [2D Axis Systems and 3D Axis Systems with Legends](../../exploff/examples/expl_report_av34.htm) | [3D Axis System with Surface Display and a Color Legend](../../exploff/examples/expl_report_av20.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_legend/d2axis_legend_tab_textparameter_dialog.htm language=enus -->
## TOPIC 00452: Legend: Text Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_legend/d2axis_legend_tab_textparameter_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_legend/d2axis_legend_tab_textparameter_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) > [Legend](../graph_dlg_2d_legend/d2axis_legend_tab_general_dialog.htm) > Legend: Text Parameters

Legend: Text Parameters

Use this dialog box to specify the display of the legend labels in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [CurveLegendSettings](../../reportapi/objects/report_objects_irepcurvelegendsettingsint.htm) object.

| Font | Specifies the font for the legend labels. |
| --- | --- |
| Font size automatic | Specifies whether DIAdem automatically adjusts the font size of the legend labels to the space available. If you do not select the property, DIAdem specifies the font size automatically. |
| Font size | Specifies the font size for the legend labels. |
| Font color | Specifies the color of the legend labels. If you select Same Color as Curve, DIAdem adjusts the label colors to the curve colors. If you select Same Color As Curve for stacked bars or grouped bars with the Palette line color, DIAdem adjusts the colors of the label to the first color of the palette. |
| Highlighting color | Specifies the color with which you highlight the legend labels. Use the Transparency setting to specify the highlighting intensity. |
| Text position | Specifies the position of the labels in relation to the symbols. |
| Bold | Specifies whether DIAdem uses bold font to display the legend labels. |
| Italics | Specifies whether DIAdem uses italic font to display the legend labels. |
| Underline | Specifies whether DIAdem uses underline font to display the legend labels. |
| Strikethrough | Specifies whether DIAdem uses strikethrough font to display the legend labels. |
| Text control | Specifies whether DIAdem truncates, or truncates and wraps the legend label at the edge of the legend column. The setting Truncate at cell limit corresponds to the assignment UseTextClipping =True. The setting Wrap and truncate corresponds to the assignments UseTextClipping =True and UseWordWrap =True. No length restrictions corresponds to the assignments UseTextClipping =False and UseWordWrap =False. |
|  |  |
| Curve List | Opens the dialog box where you create or delete the curves or change the display. This setting is only available if you open this dialog box as a main dialog box, not as a subdialog box. |

#### Further Settings

[General](../graph_dlg_2d_legend/d2axis_legend_tab_general_dialog.htm) | [Labels](../graph_dlg_2d_legend/d2axis_legend_tab_label_dialog.htm) | Text Parameters | [Title Parameters](../graph_dlg_2d_legend/d2axis_legend_tab_header_dialog.htm) | [Size](../graph_dlg_2d_legend/d2axis_legend_tab_size_dialog.htm) | [Position](../graph_dlg_2d_legend/d2axis_legend_tab_position_dialog.htm)

#### Procedures

[Displaying Curve Legends in Axis Systems](../../procpresent/axis_systems/procpres_axis_legend.htm)

#### Examples

[2D Axis System with a Legend](../../exploff/examples/expl_report_av7.htm) | [2D Axis Systems and 3D Axis Systems with Legends](../../exploff/examples/expl_report_av34.htm) | [3D Axis System with Surface Display and a Color Legend](../../exploff/examples/expl_report_av20.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_backgroundimage_dialog.htm language=enus -->
## TOPIC 00453: Background Graphic

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_backgroundimage_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_backgroundimage_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > Background Graphic

Background Graphic

Use this dialog box to add background graphics to 2D axis systems and to scale them. The scaling values and units refer to the values of the x-axis and of the first y-axis. Use the background graphics to display geo data on a map or to highlight the numeric values of a color spectrum with appropriate color values.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [D2BackgroundImageScaling](../../reportapi/objects/report_objects_irepd2backgroundimagescalingint.htm) object.

| Filename | Specifies the name of the graphics file. |
| --- | --- |
| ... | Opens the dialog box where you load graphics files. |
| Embed graphic in layout when saving | Specifies whether DIAdem embeds the graphic in the layout file when saving the layout. |
| Scale graphics | Specifies whether the background graphic can be scaled. You can only scale the axis if the axis is scaled linear. |
| X1 | Specifies the first value in x-direction for the scaling of the background graphic. |
| X2 | Specifies the end value in x-direction for the scaling of the background graphic. |
| Y1 | Specifies the start value in y-direction for the scaling of the background graphic. |
| Y2 | Specifies the end value in y-direction for the scaling of the background graphic. |
| X unit | Specifies the unit in x-direction for the background scaling. |
| Y-unit | Specifies the unit in y-direction for the scaling of a background graphic. |

#### See Also

[Transparency](../../genpresent/genpresent/genreport_transparenz.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm language=enus -->
## TOPIC 00454: Curve and Axis Definition: Axis Position

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > Curve and Axis Definition: Axis Position

Curve and Axis Definition: Axis Position

Use this dialog box to modify the display of the x-axis and the y-axis.

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings described in the following are available. |
| --- | --- |

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAxisSettings](../../reportapi/objects/report_objects_irepd2axissettingsint.htm) object.

|  | One system | Specifies that DIAdem displays several data channels in one axis system. |
| --- | --- | --- |
|  | N systems | Specifies that DIAdem displays several data channels in several axis systems. |
|  | Individual axis color and line width | Specifies whether DIAdem displays the x-axis and the y-axis in different colors and line widths. |
|  | New Subaxis Left | Creates a new subaxis to the left of the 2D axis system. |
|  | New Subaxis Right | Creates a new subaxis to the right of the 2D axis system. |
|  | Delete Subaxis | Deletes the selected subaxis. |
|  | No. | Displays the number of the axis. |
|  | Reference | Specifies the reference point of the offset for the axis. Use the tabs Axis Parameters » X Scaling and Axis Parameters » Y Scaling to specify the Axis origin, the Axis begin, and the Axis end. You specify the reference for the x-axis with the OffsetOrigin property, and the reference for the y-axis with the OffsetOrigin property. |
|  | Offset | Specifies the offset for the axis. You specify the offset for the x-axis with the OffsetHorizontal property, and the reference for the y-axis with the OffsetVertical property. |
|  | Height | Specifies the height of the y-axis in relation to the first y-axis. |
|  | Y-offset | Specifies the offset of the y-axis in relation to the first y-axis. |
|  | Axis color | Specifies the color of the axis. Use the properties Color and UseCurveColor for the AxisLine object. |
|  | Line width | Specifies the line width of the axis. |
|  | Invisible | Specifies whether the axis is visible or not. If an axis is not visible, DIAdem does not plot the curve that is assigned to this axis in the curve list. |

#### Further Settings

[Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) | [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) | Axis Position | [Axis Parameters » X-Scaling](../graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm) | [Axis Parameters » X-Numbers](../graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm) |[Axis Parameters » X-Labels](../graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm) | [Axis Parameters » Y-Scaling](../graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm) | [Axis Parameters » Y-Numbers](../graph_dlg_2d_tab/d2axis_tab_yvalue_dialog.htm) | [Axis Parameters » Y-Label](../graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm) | [Position](../graph_dlg_2d_tab/d2axis_position_dialog.htm)

|  | Note You cannot use subaxes and several axis systems simultaneously. |
| --- | --- |

|  | Note If you select several axis systems, you use the Font size on the tab Axis Parameters » Y-Axis Numbers to specify the distance between the axis systems. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm language=enus -->
## TOPIC 00455: Curve and Axis Definition: Curve List

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > Curve and Axis Definition: Curve List

Curve and Axis Definition: Curve List

Use this dialog box to generate or to delete curves in 2D axis systems or to modify the display.

You can enter various [Channel types](../../genshell/genshell/genshell_channeltypes.htm) in the channel list of this axis systems. You always enter [xy-channels](../../genshell/genshell/genshell_channeltypes.htm) as y-channels, since DIAdem automatically completes the associated x-channel. If you enter [Waveform channels](../../genshell/genshell/genshell_waveforms.htm), you do not need to specify an x-channel because waveform channels contain the x-part and the y-part of a curve. If you specify an x-channel, DIAdem plots the y-part of the waveform channel against this x-channel. If the channels are numeric channels and you do not specify an x-channel or a y-channel, DIAdem plots these channels against the index. If a channel is a text channel, DIAdem plots the other channel against the index and uses the texts of the text channel to label the axes. Furthermore, you can use [points and symbols](../../genpresent/genpresent/genreport_symbol_layout.htm) and [enumerations](../../genpresent/genpresent/genreport_enum.htm) in axis systems to label curves. You cannot use text channels for the y-channel and the y1-channel of the differential display.

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings described in the following are available. |
| --- | --- |

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAxisSystem](../../reportapi/objects/report_objects_irepd2axisint.htm) object.

|  | New Entry | Opens the dialog box where you select channels for new curves. |
| --- | --- | --- |
|  | Copy Entry | Copies the selected curve to the end of the list. |
|  | Delete Entry | Deletes the selected curve. |
|  | Move Entry Up | Moves the selected curve one position up. |
|  | Move Entry Down | Moves the selected curve one position down. |
|  | Curve Transformation | Opens the transformation dialog box, if you used Enable Curve Transformation to show this button.DIAdem opens a dialog box where you enter the name of a user command that DIAdem executes when plotting the curve. With the curve transformation function you can edit the displayed channels while they are being plotted. You can use the OnCurveTransformation property to define your own command which DIAdem calls when you click the curve transformation button. |
|  | Configure Curve Transformation | If you do not assign the standard command to the Curve2DTransformationConfiguration for Settings variable and you click Curve Transformation, an additional triangle appears to the right of the Curve Transformation button. Click the triangle to specify the name of the command that DIAdem calls when you click the Curve Transformation button in the 2D curve and axis definition dialog box. |
|  | No. | Displays the number of the curve. Click the number to select a curve. |
|  | Display curve | Specifies whether DIAdem plots the selected curve. |
|  | Type | Opens the dialog box where you specify the curve display mode and the curve parameters.Depending on the curve type the dialog box for Line, Line and points, Spikes, Bars, Outlined bars, Differential, Filled area, Constant, Coordinate, Horizontal spikes, Horizontal bars, Horizontal outlined bars, or Special combination opens. |
|  | Color | Specifies the color of the curve. Use the Type to specify the appearance. |
|  | Y-Axis | Specifies the number of the y-axis, which you specify on the Axis Position tab. |
|  | X-channel | Specifies the channel containing the x-values of the curve. Click the entry field to select another x-channel. You do not need to specify the x-channel if the y-channel is a waveform channel or if the y-channel is an xy-channel and you have selected the When plotting xy-channels, automatically determine x-channel if not populated setting in the General DIAdem Settings. |
|  | Y-Channel | Specifies the channel containing the y-values of the curve. Click the entry to select another y-channel. |
|  | Y1-Channel | Specifies the channel that contains the second y-values of the curve, for the Differential display mode. |
|  | Joint x-channel | Specifies whether DIAdem also uses the x-channel of the first curve as the x-channel for all other curves. You only can select this setting if you select the first curve in the overview. |
|  | Legend | Specifies whether DIAdem displays a legend. |
|  | Legend: Settings | Opens the dialog box where you specify the legend. |
|  | Color legend | Specifies whether DIAdem displays a color legend. |
|  | Color legend: Settings | Opens the dialog box where you specify the color palette for the Palette line color. |

|  | Note For curves with many thousands of points, DIAdem does not draw a filling because the Windows drawing routines used do not support this. Use the resampling feature to, for example, reduce the amount of data. |
| --- | --- |

#### Further Settings

Curve List | [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) | [Axis Position](../graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm) | [Axis Parameters » X-Scaling](../graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm) | [Axis Parameters » X-Numbers](../graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm) |[Axis Parameters » X-Labels](../graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm) | [Axis Parameters » Y-Scaling](../graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm) | [Axis Parameters » Y-Numbers](../graph_dlg_2d_tab/d2axis_tab_yvalue_dialog.htm) | [Axis Parameters » Y-Label](../graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm) | [Position](../graph_dlg_2d_tab/d2axis_position_dialog.htm)

|  | Note If you have subaxes, DIAdem displays the curves of the first subaxis first, then the curves of the subsequent subaxes. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_newcurve_dialog.htm language=enus -->
## TOPIC 00456: Add Curves

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_newcurve_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_newcurve_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) > Add Curves

Add Curves

Use this dialog box to create new curves in a 2D axis system, and to specify the curve display.

You can enter various [channel types](../../genshell/genshell/genshell_channeltypes.htm) as data for the new curve. You always enter [xy-channels](../../genshell/genshell/genshell_channeltypes.htm) as y-channels, since DIAdem automatically completes the associated x-channel. If you enter [Waveform channels](../../genshell/genshell/genshell_waveforms.htm), you do not need to specify an x-channel because waveform channels contain the x-part and the y-part of a curve. If you specify an x-channel, DIAdem plots the y-part of the waveform channel against this x-channel. If the channels are numeric channels and you do not specify an x-channel or a y-channel, DIAdem plots these channels against the index. If a channel is a text channel, DIAdem plots the other channel against the index and uses the texts of the text channel to label the axes. You cannot use text channels for the y-channel and the y1-channel of the differential display.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DCurves](../../reportapi/objects/report_objects_irepd2curvelistint.htm) object. Use the [Add](../../reportapi/methods/report_method_add_irepd2curvelistint.htm) method to create new curves.

|  | X-channel | Specifies the data channel containing the x-values of the curve. |
| --- | --- | --- |
|  | Y-channels | Specifies the data channel that contains the y-values of the curve. Select several data channels to generate several curves simultaneously. |
|  | X-constant | Specifies the x-value that DIAdem displays as a constant line in the Constant display mode. If you assign a unit to the x-scaling, you must also assign a unit to the x-constant. To do so, you use the VU function. |
|  | Y-constant | Specifies the y-value that DIAdem displays as a constant line in the Constant display mode. If you assign a unit to the y-scaling, you must also assign a unit to the y-constant. To do so, you use the VU function. |
|  | X-constant,Y-constant | Specifies for Coordinate display type the x-value and the y-value that DIAdem displays as coordinate. |
|  | Line color/Color | Specifies the color of the curve. Specify the exact appearance in the Curve Parameters dialog box in relation to the curve type. |
|  | Color Palette | Opens the dialog box where you specify the color assignments for the line color Palette. |
|  | Display | Specifies the display mode of the curves. DIAdem also uses the selected display type as the default setting to create new curves in this axis system. |
|  | Curve Parameters | Opens the dialog box where you specify the curve display mode and the curve parameters.Depending on the curve type the dialog box for Line, Line and points, Spikes, Bars, Outlined bars, Differential, Filled area, Constant, Coordinate, Horizontal spikes, Horizontal bars, Horizontal outlined bars, or Special combination opens. |
|  | Assign color automatically | Specifies whether DIAdem automatically uses the next color in the list when you generate several curves simultaneously. Specify in the Settings»DIAdem Settings»Colors dialog box whether DIAdem uses user-defined colors or default colors. |
|  | Assign line style automatically | Specifies whether DIAdem automatically uses the next line style in the list when you generate several curves simultaneously. |

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm language=enus -->
## TOPIC 00457: Curve and Axis Definition: Axis Parameters » X-Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Axis Parameters](../graph_dlg_2d_curve/d2axis_parameters_general.htm) > Curve and Axis Definition: Axis Parameters » X-Labels

Curve and Axis Definition: Axis Parameters » X-Labels

Use this dialog box to specify the axis labeling for a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [AxisLabel](../../reportapi/objects/report_objects_irepaxislabelint.htm) object.

|  | Text | Specifies the axis text. For example, the text @@ChnName(CurrChnNo)@@ [@@chndim(CurrChnNo)@@] returns the channel names and the channel unit of the current channel. |
| --- | --- | --- |
|  | Text Input Tool | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | Font | Specifies the font for the axis text. |
|  | Font size | Specifies the font size of the axis text. |
|  | Font color | Specifies the color of the axis text. If you select Same Color as Curve, you specify that DIAdem displays the font in the same color as the curve. |
|  | Highlighting color | Specifies the color with which you highlight the axis texts. Use the Transparency setting to specify the highlighting intensity. |
|  | X-position | Specifies the distance from the axis text to the x-axis. |
|  | Background color | Specifies the background color of the axis text. |
|  | Angle | Specifies the angle of the axis label. |
|  | Position | Specifies the position of the x-axis labels in relation to the 2D axis. |
|  | Y-position | Specifies the distance from the axis text to the y-axis. |
|  | Bold | Specifies whether DIAdem uses bold font to display the axis text. |
|  | Italics | Specifies whether DIAdem uses italic font to display the axis text. |
|  | Underline | Specifies whether DIAdem uses underline font to display the axis text. |
|  | Strikethrough | Specifies whether DIAdem uses strikethrough font to display the axis labels. |
|  | Frame | Specifies whether DIAdem frames each axis text individually. |

#### Further Settings

[Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) | [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) | [Axis Position](../graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm) | [Axis Parameters » X-Scaling](../graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm) | [Axis Parameters » X-Numbers](../graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm) | Axis Parameters » X-Labels | [Axis Parameters » Y-Scaling](../graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm) | [Axis Parameters » Y-Numbers](../graph_dlg_2d_tab/d2axis_tab_yvalue_dialog.htm) | [Axis Parameters » Y-Label](../graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm) | [Position](../graph_dlg_2d_tab/d2axis_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm language=enus -->
## TOPIC 00458: Curve and Axis Definition: Axis Parameters » X-Scaling

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Axis Parameters](../graph_dlg_2d_curve/d2axis_parameters_general.htm) > Curve and Axis Definition: Axis Parameters » X-Scaling

Curve and Axis Definition: Axis Parameters » X-Scaling

Use this dialog box to specify the x-axis scaling for a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAxisXScaling](../../reportapi/objects/report_objects_irepd2axisxscalingint.htm) object.

|  | Scaling type | Specifies the type of 2D axis scaling. |
| --- | --- | --- |
|  | Time Axis | Specifies how DIAdem displays the time axis when the Scaling type is Date/Time. |
|  | Scaling mode | Specifies whether DIAdem scales the 2D axis automatically. Use the AutoScalingType property to specify the scaling type in the Scaled display. |
|  | Units per cm/inch | Specifies the number of scaling units for scaled display. This setting only applies when you first set the Scaling defined by as Units per unit of length. |
|  | Begin | Specifies the start value for the 2D axis. |
|  | End | Specifies the end value for the 2D axis. |
|  | Range | Specifies the difference between the end value and the start value of the 2D axis. |
|  | Origin | Specifies the value at which the vertical axis intersects the selected axis. |
|  | Tick origin | Specifies the x-value where DIAdem displays the first tick when you scale 2D axes manually. |
|  | Tick interval | Specifies the distance between the ticks that are to be labeled, if you select Tick interval. |
|  | Tick channel | Specifies the channel from which DIAdem takes the tick positions if you select Tick channel. |
|  | Unit | Specifies the unit symbol for the x-axis. If this setting is not empty, DIAdem converts the channels to be displayed into this unit. If DIAdem cannot convert the units, for example, because the unit symbol does not exist in the Units catalog or because the unit symbol is assigned to a different physical quantity, DIAdem does not display the data. Use the VU function to assign a unit to the constant. If the the entered text does not correspond with a unit symbol in the units catalog, DIAdem displays this text in red and indicates the missing symbol unit in the tooltip.Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |
|  | Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |  |
|  | Open Input Help for Unit Symbols | Opens the dialog box where you select a new unit symbol. DIAdem searches for the first valid x-channel with a channel and suggests this value to the subdialog box.Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |
|  | Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |  |
|  | Synchronisation | Specifies the unique name of a synchronization group. If you enter a new name, DIAdem creates the synchronization group. DIAdem automatically adjusts the scaling of all axes that belong to the same synchronization group when you modify an axis scaling. Use the 2D-Axis Synchronization dialog box to synchronize x- and y-axes of 2D axis systems and manage synchronization groups. |
|  | Scaling | Specifies how DIAdem scales the axes for Scaled display. These settings are only available if you enable Scaled in the Layout Parameters dialog box. |
|  | Do not cut curve | Specifies whether DIAdem displays the curve outside the axis range. |
|  | Tick style | Specifies which side of the axis DIAdem displays the ticks on. This setting provides additional options as of DIAdem 2019 SP1 that are not compatible with earlier versions of DIAdem. Refer to the page on Save REPORT Layout As Compatible Version for more information. |
|  | Automatic tick size | Specifies whether DIAdem specifies the length of the ticks automatically. |
|  | Tick size in | Specifies the length of the ticks. |
|  | Number of miniticks | Specifies the number of miniticks between the ticks. |

#### Further Settings

[Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) | [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) | [Axis Position](../graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm) | Axis Parameters » X-Scaling | [Axis Parameters » X-Numbers](../graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm) |[Axis Parameters » X-Labels](../graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm) | [Axis Parameters » Y-Scaling](../graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm) | [Axis Parameters » Y-Numbers](../graph_dlg_2d_tab/d2axis_tab_yvalue_dialog.htm) | [Axis Parameters » Y-Label](../graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm) | [Position](../graph_dlg_2d_tab/d2axis_position_dialog.htm)

|  | Note Select Settings»DIAdem Settings»General to specify the unit for scaled display. |
| --- | --- |

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Examples

[2D Axis System with Linear Axis Scaling](../../exploff/examples/expl_report_av8.htm) | [2D Axis System with Linear Scaling of the X-Axis in Date Format](../../exploff/examples/expl_report_av13.htm) | [2D Axis System with Logarithmic Axis Scaling](../../exploff/examples/expl_report_av9.htm) | [3D Axis System with Logarithmic Scaling](../../exploff/examples/expl_report_av18.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm language=enus -->
## TOPIC 00459: Curve and Axis Definition: Axis Parameters » X-Numbers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Axis Parameters](../graph_dlg_2d_curve/d2axis_parameters_general.htm) > Curve and Axis Definition: Axis Parameters » X-Numbers

Curve and Axis Definition: Axis Parameters » X-Numbers

Use this dialog box to specify the font attributes for the scale of the axis in a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [LabelNumeric](../../reportapi/objects/report_objects_ireplabelnumericint.htm) object.

|  | Font | Specifies the font of the axis scale. |
| --- | --- | --- |
|  | Font size | Specifies the font size of the axis scale. |
|  | Font color | Specifies the color of the axis scale. If you select Same Color as Curve, you specify that DIAdem displays the font in the same color as the curve. |
|  | Highlighting color | Specifies the color in which you highlight the axis numbers. Use the Transparency setting to specify the highlighting intensity. |
|  | Format | Specifies the format for the numbers on the axis scale. |
|  | Format Numbers | Opens the dialog box where you select or enter the format specification. |
|  | Angle | Specifies the angle of the labels on the axis scale. |
|  | Position | Specifies the position of the axis scale in relation to the scale ticks. This setting provides additional options as of DIAdem 2019 SP1 that are not compatible with earlier versions of DIAdem. Refer to the page on Save REPORT Layout As Compatible Version for more information. |
|  | Axis end label | Specifies whether DIAdem labels the beginning and the end of the axes with numbers. To do so, DIAdem uses the same format and the same position as for the axis scaling. However, if the space at the axis beginning or axis end is not sufficient and the text is not rotated, DIAdem tries to shift the axis edge label to the left or to the right in order to not overwrite the axis scale. If you use the axis edge label for the x-axis and for the y-axis, they might overlap. If an axis scale is very near the axis beginning or the axis end, DIAdem hides the labels at the axis ends. |
|  | Bold | Specifies whether DIAdem uses bold font to display the axis scale. |
|  | Italics | Specifies whether DIAdem uses italic font to display the axis scale. |
|  | Underline | Specifies whether DIAdem uses underline font to display the axis scale. |
|  | Strikethrough | Specifies whether DIAdem uses strikethrough font to display the axis scale. |
|  | Frame | Specifies whether DIAdem frames each axis scale. |

|  | Note You can include subscript and superscript in text, format numbers, include variable contents, or use scripts for complex formats. Refer to the page on Formatting Text for more information. |
| --- | --- |

#### Further Settings

[Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) | [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) | [Axis Position](../graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm) | [Axis Parameters » X-Scaling](../graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm) | Axis Parameters » X-Numbers |[Axis Parameters » X-Labels](../graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm) | [Axis Parameters » Y-Scaling](../graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm) | [Axis Parameters » Y-Numbers](../graph_dlg_2d_tab/d2axis_tab_yvalue_dialog.htm) | [Axis Parameters » Y-Label](../graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm) | [Position](../graph_dlg_2d_tab/d2axis_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Examples

[2D Axis System with Linear Axis Scaling](../../exploff/examples/expl_report_av8.htm) | [2D Axis System with Linear Scaling of the X-Axis in Date Format](../../exploff/examples/expl_report_av13.htm) | [2D Axis System with Logarithmic Axis Scaling](../../exploff/examples/expl_report_av9.htm) | [3D Axis System with Logarithmic Scaling](../../exploff/examples/expl_report_av18.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm language=enus -->
## TOPIC 00460: Curve and Axis Definition: Axis Parameters » Y-Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Axis Parameters](../graph_dlg_2d_curve/d2axis_parameters_general.htm) > Curve and Axis Definition: Axis Parameters » Y-Labels

Curve and Axis Definition: Axis Parameters » Y-Labels

Use this dialog box to specify the axis labeling for a 2D axis system.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [AxisLabel](../../reportapi/objects/report_objects_irepaxislabelint.htm) object.

|  | Text | Specifies the axis text. For example, the text @@ChnName(CurrChnNo)@@ [@@chndim(CurrChnNo)@@] returns the channel name and the channel unit of the current channel. |
| --- | --- | --- |
|  | Text Input Tool | Opens the dialog box where you enter text that includes DIAdem variables and formulas. |
|  | Font | Specifies the font for the axis text. |
|  | Font size | Specifies the font size of the axis text. |
|  | Font color | Specifies the color of the axis text. If you select Same Color as Curve, you specify that DIAdem displays the font in the same color as the curve. |
|  | Highlighting color | Specifies the color with which you highlight the axis texts. Use the Transparency setting to specify the highlighting intensity. |
|  | X-position | Specifies the distance from the axis text to the x-axis. |
|  | Background color | Specifies the background color of the axis text. |
|  | Angle | Specifies the angle of the axis labels. |
|  | Position | Specifies the position of the y-axis labels in relation to the 2D axis. |
|  | Y-position | Specifies the distance from the axis text to the y-axis. |
|  | Bold | Specifies whether DIAdem uses bold font to display the axis text. |
|  | Italics | Specifies whether DIAdem uses italic font to display the axis text. |
|  | Underline | Specifies whether DIAdem uses underline font to display the axis text. |
|  | Strikethrough | Specifies whether DIAdem uses strikethrough font to display the axis labels. |
|  | Frame | Specifies whether DIAdem frames each axis text individually. |

#### Further Settings

[Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) | [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) | [Axis Position](../graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm) | [Axis Parameters » X-Scaling](../graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm) | [Axis Parameters » X-Numbers](../graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm) | [Axis Parameters » X-Labels](../graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm) | [Axis Parameters » Y-Scaling](../graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm) | [Axis Parameters » Y-Numbers](../graph_dlg_2d_tab/d2axis_tab_yvalue_dialog.htm) | Axis Parameters » Y-Label | [Position](../graph_dlg_2d_tab/d2axis_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm language=enus -->
## TOPIC 00461: Curve and Axis Definition: Axis Parameters » Y-Scaling

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2d_tab/d2axis_tab_yscale_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis Systems](../graph_dlg_2d_curve/d2axis_systems_general.htm) | [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm)) > [Curve and Axis Definition](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) > [Axis Parameters](../graph_dlg_2d_curve/d2axis_parameters_general.htm) > Curve and Axis Definition: Axis Parameters » Y-Scaling

Curve and Axis Definition: Axis Parameters » Y-Scaling

Use this dialog box to specify the y-axis scaling for a 2D axis system.

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings described in the following are available. |
| --- | --- |

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DAxisYScaling](../../reportapi/objects/report_objects_irepd2axisyscalingint.htm) object.

|  | Scaling type | Specifies the type of 2D axis scaling. If the setting Subaxis ticks aligned to axis grid is selected, DIAdem always uses Linear as the scaling type for the y-scaling. |
| --- | --- | --- |
|  | Time Axis | Specifies how DIAdem displays the time axis when the Scaling type is Date/Time. If you selected Automatic for the time axis, DIAdem displays the time part of the waveform channels with a relative time axis and displays other time channels with an absolute time axis. |
|  | Scaling mode | Specifies whether DIAdem scales the 2D axis automatically. Use the AutoScalingType property to specify the scaling type in the Scaled display. |
|  | Units per cm/inch | Specifies the number of scaling units for scaled display. This setting only applies when you first set the Scaling defined by as Units per unit of length. |
|  | Begin | Specifies the start value for the 2D axis. |
|  | End | Specifies the end value for the 2D axis. |
|  | Range | Specifies the difference between the end value and the start value of the 2D axis. |
|  | Origin | Specifies the value at which the vertical axis intersects the selected axis. |
|  | Tick origin | Specifies the x-value where DIAdem displays the first tick when you scale 2D axes manually. |
|  | Tick interval | Specifies the distance between the ticks that are to be labeled, if you select Tick interval. Some scaling modes like Third, Octave, and Logarithmic ignore the tick interval. In a logarithmic display, DIAdem plots the ticks at the specified distance, but also at the specified distance multiplied by factor 10N. |
|  | Tick channel | Specifies the channel from which DIAdem takes the tick positions if you select Tick channel. |
|  | Unit | Specifies the unit for the y-axis. If this setting is not empty, DIAdem converts the channels to be displayed into this unit. If DIAdem cannot convert the units, for example, because the unit symbol does not exist in the Units catalog or because the unit symbol is assigned to a different physical quantity, DIAdem does not display the data. Use the VU function to assign a unit to the constant. If the the entered text does not correspond with a unit symbol in the units catalog, DIAdem displays this text in red and indicates the missing symbol unit in the tooltip.Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |
|  | Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |  |
|  | Open Input Help for Unit Symbols | Opens the dialog box where you select a new unit symbol. DIAdem searches for the first valid y-channel with a channel and suggests this value to the subdialog box.Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |
|  | Note This setting is only available with the DIAdem Advanced and DIAdem Professional packages. |  |
|  | Synchronisation | Specifies the unique name of a synchronization group. If you enter a new name, DIAdem creates the synchronization group. DIAdem automatically adjusts the scaling of all axes that belong to the same synchronization group when you modify an axis scaling. Use the 2D-Axis Synchronization dialog box to synchronize x- and y-axes of 2D axis systems and manage synchronization groups. |
|  | Scaling | Specifies how DIAdem scales the axes for Scaled display. |
|  | Do not cut curve | Specifies whether DIAdem displays the curve outside the axis range. |
|  | Tick style | Specifies which side of the axis DIAdem displays the ticks on. This setting provides additional options as of DIAdem 2019 SP1 that are not compatible with earlier versions of DIAdem. Refer to the page on Save REPORT Layout As Compatible Version for more information. |
|  | Automatic tick size | Specifies whether DIAdem specifies the length of the ticks automatically. |
|  | Tick size in | Specifies the length of the ticks. |
|  | Number of miniticks | Specifies the number of miniticks between the ticks. If, for example, you want to divide a tick into ten areas, you must enter nine miniticks. |

#### Further Settings

[Curve List](../graph_dlg_2d_tab/d2axis_tab_curve_dialog.htm) | [Axis System](../graph_dlg_2d_tab/d2axis_tab_axis_dialog.htm) | [Axis Position](../graph_dlg_2d_tab/d2axis_tab_axispos_dialog.htm) | [Axis Parameters » X-Scaling](../graph_dlg_2d_tab/d2axis_tab_xscale_dialog.htm) | [Axis Parameters » X-Numbers](../graph_dlg_2d_tab/d2axis_tab_xvalue_dialog.htm) | [Axis Parameters » X-Labels](../graph_dlg_2d_tab/d2axis_tab_xlabel_dialog.htm) | Axis Parameters » Y-Scaling | [Axis Parameters » Y-Numbers](../graph_dlg_2d_tab/d2axis_tab_yvalue_dialog.htm) | [Axis Parameters » Y-Label](../graph_dlg_2d_tab/d2axis_tab_ylabel_dialog.htm) | [Position](../graph_dlg_2d_tab/d2axis_position_dialog.htm)

|  | Note Select Settings»DIAdem Settings»General to specify the unit for scaled display. |
| --- | --- |

|  | Note If you set the Begin and the End manually, and if you also select the Subaxis ticks aligned to main axis grid checkbox on the Axis System tab, DIAdem adjusts the Begin and End values to the Tick interval. |
| --- | --- |

#### Examples

[2D Axis System with Linear Axis Scaling](../../exploff/examples/expl_report_av8.htm) | [2D Axis System with Linear Scaling of the X-Axis in Date Format](../../exploff/examples/expl_report_av13.htm) | [2D Axis System with Logarithmic Axis Scaling](../../exploff/examples/expl_report_av9.htm) | [3D Axis System with Logarithmic Scaling](../../exploff/examples/expl_report_av18.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_channeltransform_conf_dialog.htm language=enus -->
## TOPIC 00462: Configure Channel Transformation

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_channeltransform_conf_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_channeltransform_conf_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > [Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) > Configure Channel Transformation

Configure Channel Transformation

Use this dialog box to specify the name of the command that DIAdem calls when you click the **Curve Transformation** button in the 2D table definition dialog box.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DTableSettings](../../reportapi/objects/report_objects_ireptable2dsettingsint.htm) object.

| Call command for entering curve transformation | Specifies the command that DIAdem calls when you click the Curve Transformation button in the 2D curve and axis definition dialog box. |
| --- | --- |
| Reset | Resets the dialog box to the default settings. |

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_channeltransform_dialog.htm language=enus -->
## TOPIC 00463: Channel Transformation

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_channeltransform_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_channeltransform_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > [Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) > Channel Transformation

Channel Transformation

Use this dialog box to specify the name of a channel transformation function. If you use the channel transformation function, you can edit the displayed channel while DIAdem plots. DIAdem does not modify the original data.

#### Settings

| Name of user command for curve transformation | Specifies the name of the transformation function. |
| --- | --- |

|  | Note Follow the instructions in Working with Events in DIAdem when you use curve transformation functions. |
| --- | --- |

#### See Also

[OnCurveTransformation](../../reportapi/events/report_event_onchanneltransformation_ireptable2dcolumnchannelint.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_general.htm language=enus -->
## TOPIC 00464: 2D Tables

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > 2D Tables

2D Tables

The following topics describe the dialog boxes where you make your settings for 2D tables.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm language=enus -->
## TOPIC 00465: Table Definition: Display

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > Table Definition: Display

Table Definition: Display

Use this dialog box to specify the general display mode for a 2D table.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DTableSettings](../../reportapi/objects/report_objects_ireptable2dsettingsint.htm) object.

| Table |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Alignment | Specifies the alignment of the 2D table. |  |  |  |  |  |
| Frame color | Specifies the frame color of the 2D table. |  |  |  |  |  |
| Background color | Specifies the background color of the 2D table. Use the setting Filling effects to define color shading. |  |  |  |  |  |
| Sort for expanded curves mode | Specifies the order in which DIAdem expands channels in the table. If you choose Same sort as layout, DIAdem sorts the channels according to the Curve expansion setting. If you choose Sort by channels, the first columns now contain all the channels to be displayed in the first expanded group. The next columns contain all channels of the second expanded group to be displayed, and so on. If you choose Sort by groups, the first columns now contain the first channel of the first expanded group to be displayed. The next columns contain the first channel of the second expanded group, and so on. This is followed by the second channel of the first expanded group, then the second channel of the second expanded group, and so on. The following table shows an example of the different settings for three channels in two groups. Sort by channels Group1 / ExpandChn1 Group1 / ExpandChn2 Group1 / ExpandChn3 Group2 / ExpandChn1 Group2 / ExpandChn2 Group2 / ExpandChn3 Sort by groups Group1 / ExpandChn1 Group2 / ExpandChn1 Group1 / ExpandChn2 Group2 / ExpandChn2 Group1 / ExpandChn3 Group2 / ExpandChn3 This setting is only available if you select Settings»Layout Setup»Layout Parameters»Curve Display and then enable the Expand curves checkbox. |  |  |  |  |  |
| Sort by channels | Group1 / ExpandChn1 | Group1 / ExpandChn2 | Group1 / ExpandChn3 | Group2 / ExpandChn1 | Group2 / ExpandChn2 | Group2 / ExpandChn3 |
| Sort by groups | Group1 / ExpandChn1 | Group2 / ExpandChn1 | Group1 / ExpandChn2 | Group2 / ExpandChn2 | Group1 / ExpandChn3 | Group2 / ExpandChn3 |
| Rows |  |  |  |  |  |  |
| Separator between the rows | Specifies whether DIAdem displays lines to separate rows. |  |  |  |  |  |
| Separate headings | Specifies whether DIAdem separates the first row of the 2D table with a thicker line. |  |  |  |  |  |
| Line color | Specifies the color DIAdem uses to display separating lines between the rows in the 2D table. |  |  |  |  |  |
| Line width | Specifies the line width DIAdem uses to display separating lines in the 2D table. |  |  |  |  |  |
| 1st alternating color | Specifies the background color which DIAdem uses for every second row starting at the first row. DIAdem draws this background color over a possible background color of the table. Use the setting Filling effects to define color shading. |  |  |  |  |  |
| 2nd alternating color | Specifies the background color DIAdem uses for every second row starting at the second row. DIAdem draws this background color over possible background colors of the table or rows. Use the setting Filling effects to define color shading. |  |  |  |  |  |
| Columns |  |  |  |  |  |  |
| Separator between the columns | Specifies whether DIAdem displays lines to separate columns. |  |  |  |  |  |
| Separate first column | Specifies whether DIAdem separates the first column of the 2D table with a thicker line. |  |  |  |  |  |
| Line color | Specifies the color DIAdem uses to display separating lines between the columns in the 2D table. |  |  |  |  |  |
| Line width | Specifies the line width DIAdem uses to display separating lines between the columns in the 2D table. |  |  |  |  |  |
| 1st alternating color | Specifies the background color DIAdem uses for every second columnn starting at the first column. DIAdem draws this background color over possible background colors of the table or rows. Use the setting Filling effects to define color shading. |  |  |  |  |  |
| 2nd alternating color | Specifies the background color DIAdem uses for every second column starting at the second column. DIAdem draws this background color over possible background colors of the table, columns, or rows. Use the setting Filling effects to define color shading. |  |  |  |  |  |

|  | Note For the frame, DIAdem uses the wider of the two line widths specified. |
| --- | --- |

#### Further Settings

[Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) | [Scaling](../graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm) | [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm) | [Headers and Footers » Text Parameters Headers](../graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm) | [Headers and Footers » Text Parameters Footers](../graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm) | [Headers and Footers » Display](../graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm) | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | Display | [Position](../graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm language=enus -->
## TOPIC 00466: Table Definition: Headers and Footers » Display

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > [Headers and Footers](../graph_dlg_2dtable_tab/d2table_tableheading_general.htm) > Table Definition: Headers and Footers » Display

Table Definition: Headers and Footers » Display

Use this dialog box to specify the display of the headers and footers for the selected columns in a 2D table. You can only change the header and footer settings if you enable the **Display headers** or **Display footers** setting under [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm).

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DTableColumnHeaderIndividualTitleSettings](../../reportapi/objects/report_objects_ireptable2dcolheaderfooterindititlessettingsint.htm) object.

| Column list | Select a column to make the following settings for that column. |
| --- | --- |

| Headers |  |
| --- | --- |
| Headers in % | Specifies the size of the header cell as a percentage. |
| Separate headers through lines | Specifies whether DIAdem uses lines to separate the individual headers. |
| Background color | Specifies the background color of the header cell. Use the setting Filling effects to define color shading. |
| Individual background color for column | Specifies the background color of the header in the selected column. Use the setting Filling effects to define color shading.This setting is only available if you enabled the Text Parameters for Headers»Use Individual Parameters setting. DIAdem colors over the specified background colors for the table, the rows, and the columns with the individual background color. |
| Footers |  |
| Footers in %: | Specifies the size of the footer cell as a percentage. |
| Separate footers through lines | Specifies whether DIAdem uses lines to separate the individual footers. |
| Background color | Specifies the background color of the footer cell. Use the setting Filling effects to define color shading. |
| Individual background color for column | Specifies the background color of the footer in the selected column. Use the setting Filling effects to define color shading.This setting is only available if you enabled the Text Parameters for Footers»Use Individual Parameters setting. DIAdem colors over the specified background colors for the table, the rows, and the columns with the individual background color. |
| Show footers only at end of table | Specifies whether DIAdem displays the footers only on the last page of the table. This setting is only available if you set Automatically increasing for Table length on the Scaling tab. |

#### Further Settings

[Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) | [Scaling](../graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm) | [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm) | [Headers and Footers » Text Parameters Headers](../graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm) | [Headers and Footers » Text Parameters Footers](../graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm) | Headers and Footers » Display | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | [Display](../graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm) | [Position](../graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm language=enus -->
## TOPIC 00467: Table Definition: Headers and Footers » Text Parameters for Footers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > [Headers and Footers](../graph_dlg_2dtable_tab/d2table_tableheading_general.htm) > Table Definition: Headers and Footers » Text Parameters for Footers

Table Definition: Headers and Footers » Text Parameters for Footers

Use this dialog box to specify the footers of a 2D table.

#### Settings

In the object-oriented script interface for DIAdem REPORT, you can find the following settings in the properties and methods of the [2DTableColumnHeaderFooterIndividualSettings](../../reportapi/objects/report_objects_ireptable2dcolheaderfooterindisettingsint.htm) and [2DTableColumnHeaderFooterIndividualTitleSettings](../../reportapi/objects/report_objects_ireptable2dcolheaderfooterindititlessettingsint.htm) objects.

| Column list | Select a column to make the following settings for that column. |
| --- | --- |
| Automatically set font size for all footers | Specifies whether DIAdem sets the font size of the footers automatically. |
| Use individual parameters | Specifies whether DIAdem configures the table footers with global parameters or with the parameters of the individual columns. If you enable this setting, you can make the following settings for the text and specify an individual background color for the footers. |
| Font | Specifies the character set of the footers. |
| Font size | Specifies the font size of the footers. |
| Font color | Specifies the color of the footers. |
| Highlighting color | Specifies the color in which you highlight the footers. Use the Transparency setting to specify the highlighting intensity. |
| Text control | Specifies whether DIAdem wraps and truncates the footers at the cell boundary or just truncates them.The setting Truncate at cell border corresponds to the assignment UseTextClipping = True. The setting Wrap and truncate corresponds to the assignments UseTextClipping = True and UseWordWrap = True. No length restrictions corresponds to the assignments UseTextClipping = False and UseWordWrap = False.In these assignments you use the UseTextClipping for 2DTableFooterDefaultSettings and UseWordWrap for 2DTableFooterDefaultSettings properties for global parameters. Use the properties UseTextClipping for 2DTableColumnFooterIndividualSettings and UseWordWrap for 2DTableColumnFooterIndividualSettings for individual parameters in these assignments. |
| Text alignment | Specifies the relative position of the footers. You specify the relative position for global parameters with the Alignment for 2DTableHeaderDefaultSettings property and for individual parameters with the Alignment for 2DTableColumnHeaderIndividualSettings property. |
| Angle | Specifies the label angle of the footers. You specify the label angle for global parameters with the Angle for 2DTableFooterDefaultSettings property and for individual parameters with the Angle for 2DTableColumnFooterIndividualSettings property. |
| Bold | Specifies whether DIAdem uses bold font to display the footers. |
| Italics | Specifies whether DIAdem uses italic font to display the footers. |
| Underline | Specifies whether DIAdem uses bold font to underline the footers. |
| Strikethrough | Specifies whether DIAdem uses strikethrough font to display the footers. |
| Frame | Specifies whether DIAdem frames each footer individually. |

#### Further Settings

[Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) | [Scaling](../graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm) | [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm) | [Headers and Footers » Text Parameters Headers](../graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm) | Headers and Footers » Text Parameters Footers | [Headers and Footers » Display](../graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm) | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | [Display](../graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm) | [Position](../graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_general.htm language=enus -->
## TOPIC 00468: Column Properties

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > Column Properties

Column Properties

The following topics describe the dialog boxes where you make your settings for table properties.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm language=enus -->
## TOPIC 00469: Table Definition: Headers and Footers » Text

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > [Headers and Footers](../graph_dlg_2dtable_tab/d2table_tableheading_general.htm) > Table Definition: Headers and Footers » Text

Table Definition: Headers and Footers » Text

Use this dialog box to specify the the headers and footers of a 2D table.

#### Settings

In the object-oriented script interface for DIAdem REPORT, you can find the following settings in the properties and methods of the [2DTableColumnHeaderIndividualTitleSettings](../../reportapi/objects/report_objects_ireptable2dcolheaderfooterindititlessettingsint.htm), [2DTableHeaderDefaultSettings](../../reportapi/objects/report_objects_ireptable2dheaderdefaultsettingsint.htm), [2DTableColumnFooterIndividualTitleSettings](../../reportapi/objects/report_objects_ireptable2dcolheaderfooterindititlessettingsint.htm), and [2DTableFooterDefaultSettings](../../reportapi/objects/report_objects_ireptable2dheaderdefaultsettingsint.htm) objects.

|  | Column list | Select a column to make the following settings for that column. |
| --- | --- | --- |
|  | Display headers | Specifies whether DIAdem displays headers. |
|  | Use individual headers for column | Specifies whether DIAdem labels the selected column with global or individual headers. |
|  | Type | Specifies whether you use predefined or free text in the headers. For global headers you specify the type using the properties TitleDefinition1 for 2DTableHeaderFooterDefaultSettings, TitleDefinition2 for 2DTableHeaderFooterDefaultSettings, and TitleDefinition3 for 2DTableHeaderFooterDefaultSettings. For individual headers you specify the type using the properties TitleDefinition1 for 2DTableColumnHeaderFooterIndividualTitleSettings, TitleDefinition2 for 2DTableColumnHeaderFooterIndividualTitleSettings, and TitleDefinition3 for 2DTableColumnHeaderFooterIndividualTitleSettings. |
|  | Global headers for all columns | Specifies the global headers when you choose the Free Text setting for Type. |
|  | Individual headers for column | Specifies the individual headers for the selected column when you choose the Free Text setting for Type. |
|  | Text Input Tool | Opens the dialog box where you enter and check text that includes DIAdem variables and formulas. |
|  | Display footers | Specifies whether DIAdem displays footers. |
|  | Use individual footers for column | Specifies whether DIAdem labels the selected columns with global or individual footers. |
|  | Type | Specifies whether you use predefined or free text in the footers. For global footers you specify the type using the properties TitleDefinition1 for 2DTableHeaderFooterDefaultSettings, TitleDefinition2 for 2DTableHeaderFooterDefaultSettings, and TitleDefinition3 for 2DTableHeaderFooterDefaultSettings. For individual footers you specify the type using the properties TitleDefinition1 for 2DTableColumnHeaderFooterIndividualTitleSettings, TitleDefinition2 for 2DTableColumnHeaderFooterIndividualTitleSettings, and TitleDefinition3 for 2DTableColumnHeaderFooterIndividualTitleSettings. |
|  | Global footers for all columns | Specifies the global footers when you choose the Free Text setting for Type. |
|  | Individual footers for column | Specifies the individual footers for the selected column when you choose the Free Text setting for Type. |
|  | Text Input Tool | Opens the dialog box where you enter and check text that includes DIAdem variables and formulas. |

|  |  | Note You can also use variables for the headers and footers. For example, the text @@ChnName(CurrChnNo)@@ returns the name of the current channel. Instead of the CurrChnNo variable, you also can use the # character for the current channel in layouts. You can also use the following variables for the statistical values of the column: D2TabChnCountAll, D2TabChnCountVisible, D2TabChnMaxAll, D2TabChnMaxVisible, D2TabChnMeanAll, D2TabChnMeanVisible, D2TabChnMinAll, D2TabChnMinVisible, D2TabChnSumAll, and D2TabChnSumVisible. |
| --- | --- | --- |

#### Further Settings

[Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) | [Scaling](../graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm) | Headers and Footers » Text | [Headers and Footers » Text Parameters Headers](../graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm) | [Headers and Footers » Text Parameters Footers](../graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm) | [Headers and Footers » Display](../graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm) | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | [Display](../graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm) | [Position](../graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm)

|  |  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm language=enus -->
## TOPIC 00470: Table Definition: Headers and Footers » Text Parameters Headers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > [Headers and Footers](../graph_dlg_2dtable_tab/d2table_tableheading_general.htm) > Table Definition: Headers and Footers » Text Parameters Headers

Table Definition: Headers and Footers » Text Parameters Headers

Use this dialog box to specify the headers for a 2D table.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DTableColumnHeaderIndividualTitleSettings](../../reportapi/objects/report_objects_ireptable2dheaderdefaultsettingsint.htm) and [2DTableHeaderDefaultSettings](../../reportapi/objects/report_objects_ireptable2dcolheaderfooterindititlessettingsint.htm) objects.

| Column list | Select a column to make the following settings for that column. |
| --- | --- |
| Automatically set font size for all headers | Specifies whether DIAdem sets the font size of the header text automatically. |
| Use individual parameters | Specifies whether DIAdem uses global parameters or the parameters of the individual columns to parameterize the table headers. If you enable this setting, you can make the following settings for the text and specify an individual background color for the headers. |
| Font | Specifies the character set for the headers. |
| Font size | Specifies the font size for the headers. |
| Font color | Specifies the color for the headers. |
| Highlighting color | Specifies the color in which you highlight the headers. Use the Transparency setting to specify the highlighting intensity. |
| Text control | Specifies whether DIAdem wraps and truncates the headers at the cell boundary or just truncates them. The setting Truncate at cell border corresponds to the assignment UseTextClipping = True. The setting Wrap and truncate corresponds to the assignments UseTextClipping = True and UseWordWrap = True. No length restrictions corresponds to the assignments UseTextClipping = False and UseWordWrap = False.Use the properties UseTextClipping for 2DTableHeaderDefaultSettings and UseWordWrap for 2DTableHeaderDefaultSettings for global parameters in these assignments. Use the properties UseTextClipping for 2DTableColumnHeaderIndividualSettings and UseWordWrap for 2DTableColumnHeaderIndividualSettings for individual parameters in these assignments. |
| Text alignment | Specifies the relative position of the headers. If global parameters are set, the relative position is specified by the Alignment for 2DTableHeaderDefaultSettings property. If individual parameters are set, the relative position is specified by the Alignment for 2DTableColumnHeaderIndividualSettings property. |
| Angle | Specifies the angle of the lable for the headers. If global parameters are set, the label angle is specified by the Angle for 2DTableHeaderDefaultSettings property. If individual parameters are set, the label angle is specified by the Angle for 2DTableColumnHeaderIndividualSettings. |
| Bold | Specifies whether DIAdem displays the headers in bold. |
| Italics | Specifies whether DIAdem displays the headers in italics. |
| Underline | Specifies whether DIAdem underlines the headers. |
| Strikethrough | Specifies whether DIAdem displays the headers in strikethrough. |
| Frame | Specifies whether DIAdem frames each header. |

#### Further Settings

[Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) | [Scaling](../graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm) | [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm) | Headers and Footers » Text Parameters Headers | [Headers and Footers » Text Parameters Footers](../graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm) | [Headers and Footers » Display](../graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm) | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | [Display](../graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm) | [Position](../graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm language=enus -->
## TOPIC 00471: Table Definition: Table Columns

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > Table Definition: Table Columns

Table Definition: Table Columns

Use this dialog box to create or delete columns in 2D tables, or to modify the table display.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DTableColumn](../../reportapi/objects/report_objects_ireptable2dcolumnexpressionint.htm) and [2DTableColumn](../../reportapi/objects/report_objects_ireptable2dcolumnbaseint.htm) objects.

|  | New Entry | Opens the dialog box in which you can select table entries that DIAdem inserts behind the current position. |
| --- | --- | --- |
|  | Copy Entry | Copies the selected entry to the end of the list. |
|  | Delete Entry | Deletes the selected entry. |
|  | Move Entry Up | Moves the selected entry one position up. |
|  | Move Entry Down | Moves the selected entry one position down. |
|  | Sort Data | Specifies whether DIAdem sorts the data in the columns. If you enable this setting, you can select the sorting criteria individually for each column.If you specify a DIAdem expression for Data Type and want to sort the data, you must also specify the Number of Lines. For example, if you want to sort the output of the channel names of the first channel group, specify the DIAdem expression @@Data.Root.ChannelGroups(1).Channels(D2TabRow)@@ as Entry and specify Number of Rows as a numeric value or as DIAdem expression, for example, @@Data.Root.ChannelGroups(1).Channels.Count@@. |
|  | Channel Transformation | Opens the transformation dialog box, if you used Enable Channel Transformation to show this button.DIAdem opens a dialog box where you enter the name of a user command that DIAdem executes when plotting the channel. With the channel transformation function you can edit the displayed channels while they are being plotted. You can use the OnChannelTransformation property to define your own command which DIAdem calls when you click the curve Channel transformation button. |
|  | Configure Channel Transformation | If you do not assign the standard command to the ChannelTransformationConfiguration for Settings variable and you click Channel Transformation, an additional triangle appears to the right of the Channel Transformation button. Click this triangle to specify the name of the command that DIAdem calls when you click the Channel Transformation button in the table definition dialog box. |
|  | No. | Displays the number of the column. Click the number to select a column. |
|  | Data Type | Specifies whether the selected column contains data channels, variables, DIAdem expressions, or text lists. You can use any DIAdem variable as a variable. If you enter a vector variable without an index, DIAdem displays all the vector elements. To define a separate text for each row in text lists, select Column Properties » Text List. |
|  | Entry | Specifies the channel, the variable, or the expression, or the text list, of which DIAdem displays the contents in the table. |
|  | Number of Rows | Specifies the maximum number of table rows for the variable or for DIAdem expressions. |
|  | Relative Width | For vertical tables, specifies the width of a table column in relation to the other columns in the table. |
|  | Relative Height | For horizontal tables, specifies the height of a table row in relation to the other rows in the table. |
|  | Sort | Specifies the sorting criteria of the table column. DIAdem sorts the first channel in ascending or descending order as the selected sorting criteria specifies. DIAdem also moves the values or texts in all other channels if the channels do not have the sorting criteria Do not sort. If two values in the first channel are the same, DIAdem includes the sort criteria of the second channel. If two values are the same in the second channel you want to sort, the third channel to be sorted is the sorting criteria and so on. |

#### Further Settings

Table Columns | [Scaling](../graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm) | [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm) | [Headers and Footers » Text Parameters Headers](../graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm) | [Headers and Footers » Text Parameters Footers](../graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm) | [Headers and Footers » Display](../graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm) | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | [Display](../graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm) | [Position](../graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm language=enus -->
## TOPIC 00472: Table Definition: Position

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > Table Definition: Position

Table Definition: Position

Use this dialog box to specify the position and size of a 2D table.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [ObjectPositionDefinedByBorders](../../reportapi/objects/report_objects_ireppositionbordersint.htm) object.

| Distance from top edge | Specifies the distance from the top edge of the page, as a percentage of the worksheet, in centimeters or inches. |
| --- | --- |
| Distance from left edge | Specifies the distance from the left edge of the worksheet, as a percentage of the worksheet, in centimeters or inches. |
| Distance from right edge | Specifies the distance from the right edge of the page, as a percentage of the worksheet, in centimeters or inches. |
| Distance from bottom edge | Specifies the distance from the bottom edge of the page, as a percentage of the worksheet, in centimeters or inches. |
| Width | Displays the width of the table, as a percentage of the worksheet, in centimeters or inches. |
| Height | Displays the height of the table, as a percentage of the worksheet, in centimeters or inches. |

|  | Note To specify the unit, select Settings»DIAdem Settings»General. |
| --- | --- |

#### Further Settings

[Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) | [Scaling](../graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm) | [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm) | [Headers and Footers » Text Parameters Headers](../graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm) | [Headers and Footers » Text Parameters Footers](../graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm) | [Headers and Footers » Display](../graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm) | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | [Display](../graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm) | Position

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm language=enus -->
## TOPIC 00473: Table Definition: Scaling

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tab_scaling_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > Table Definition: Scaling

Table Definition: Scaling

Use this dialog box to specify the number of table rows to be displayed in a 2D table.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [2DTableIndexSettings](../../reportapi/objects/report_objects_ireptable2dindexsettingsint.htm) object.

| Table length | Specifies how DIAdem determines the table length. |
| --- | --- |
| Start at row | Specifies the first data channel row DIAdem displays in the table. |
| End at row | Specifies the last data channel row DIAdem displays in the table. |
| Step width | Specifies the step width between two values in the data channel. |
| Number of rows | Specifies the number of last rows you want to display in a table. |
| Row height as % of the page | Specifies the height of the row as a percentage of the height of the worksheet, if you set Automatically increasing as the Table length setting. |
| Hide empty lines | Specifies whether DIAdem hides the rows in which the values of all columns contain the value NoValue or an empty string. The setting is only available if you set the Table length to Auto row height. |

|  | If you select Automatically increasing for the Table length setting, you can display the following or the previous table sheet with the table navigation buttons. In order to print out all pages of the automatically expanding tables use the setting Print all pages with expanding tables completely in the DIAdem Settings of REPORT. |
| --- | --- |

#### Further Settings

[Table Columns](../graph_dlg_2dtable_tab/d2table_tab_oview_dialog.htm) | Scaling | [Headers and Footers » Text](../graph_dlg_2dtable_tab/d2table_tab_label_text_dialog.htm) | [Headers and Footers » Text Parameters Headers](../graph_dlg_2dtable_tab/d2table_tab_label_textpara_dialog.htm) | [Headers and Footers » Text Parameters Footers](../graph_dlg_2dtable_tab/d2table_tab_label_footertextpara_dialog.htm) | [Headers and Footers » Display](../graph_dlg_2dtable_tab/d2table_tab_label_display_dialog.htm) | [Column Properties » Text List](../graph_dlg_2dtable_tab/d2table_tab_values_text_dialog.htm) | [Column Properties » Text Parameters](../graph_dlg_2dtable_tab/d2table_tab_values_layout_dialog.htm) | [Column Properties » Display](../graph_dlg_2dtable_tab/d2table_tab_values_display_dialog.htm) | [Display](../graph_dlg_2dtable_tab/d2table_tab_disp_dialog.htm) | [Position](../graph_dlg_2dtable_tab/d2table_tab_position_dialog.htm)

|  | Note If you select Predefine Setting from the context menu of a function group to open this dialog box, not all the settings are available. |
| --- | --- |

#### Procedures

[Displaying Expressions in 2D Tables](../../procpresent/tables/procpres_2dtable_variables.htm) | [Inserting 2D Tables](../../procpresent/tables/procpres_2dtable_defining.htm) | [Scrolling in Multisheet 2D Tables](../../procpresent/tables/procpres_2dtable_continuous.htm)

#### Examples

[2D Table with and without Grid Lines](../../exploff/examples/expl_report_av5.htm) | [2D Table with Channel Transformation](../../exploff/examples/2d_tabchanneltransformation.htm) | [2D Table with Headers and Footers](../../exploff/examples/2d_tabheaderandfooter.htm) | [2D Tables](../../exploff/examples/expl_report_av39.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Table with Automatic Row Height](../../exploff/examples/expl_flextableheight.htm) | [Using User Commands for Trend Displays in Tables](../../exploff/examples/expl_report_av26.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm language=enus -->
## TOPIC 00474: Table Definition

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > Table Definition

Table Definition

The following topics describe the dialog boxes where you make your settings for table columns and table headings.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_2dtable_tab/d2table_tableheading_general.htm language=enus -->
## TOPIC 00475: Headers and Footers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_2dtable_tab/d2table_tableheading_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_2dtable_tab/d2table_tableheading_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [2D Tables](../graph_dlg_2dtable_tab/d2table_general.htm) > [Table Definition](../graph_dlg_2dtable_tab/d2table_tabledefiniton_general.htm) > Headers and Footers

Headers and Footers

The following topics describe the dialog boxes where you make your settings for headers and footers.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_axisdefinition_general.htm language=enus -->
## TOPIC 00476: 3D Axis Definition

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_axisdefinition_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_axisdefinition_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > 3D Axis Definition

3D Axis Definition

The following topics describe the dialog boxes where you make your settings for 3D axis systems and curves.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_axisparameters_general.htm language=enus -->
## TOPIC 00477: Axis Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_axisparameters_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_axisparameters_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [3D Axis Definition](../graph_dlg_3d_curve/d3axis_axisdefinition_general.htm) > Axis Parameters

Axis Parameters

The following topics describe the dialog boxes where you make your settings for scaling the axes of a 3D axis system and for displaying numbers and labels on the axes.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_barssymbols_general.htm language=enus -->
## TOPIC 00478: Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_barssymbols_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_barssymbols_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) > Labels

Labels

The following topics describe the dialog boxes where you make your settings for displaying a 3D curve as bars with symbols.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm language=enus -->
## TOPIC 00479: Points

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > Points

Points

The following topics describe the dialog boxes where you make your settings for the points of a characteristic diagram.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_coordinate_general.htm language=enus -->
## TOPIC 00480: Coordinates

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_coordinate_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_coordinate_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > Coordinates

Coordinates

The following topics describe how you configure the coordinates display.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_curve_par_coordinate_comment_comment_tab_position_dialog.htm language=enus -->
## TOPIC 00481: Curve Parameters: Coordinate » Comment » Position

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_curve_par_coordinate_comment_comment_tab_position_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_curve_par_coordinate_comment_comment_tab_position_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Coordinates](../graph_dlg_3d_curve/d3axis_coordinate_general.htm) > [Text](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_comment_comment_tab_text_dialog.htm) > Curve Parameters: Coordinate » Comment » Position

Curve Parameters: Coordinate » Comment » Position

Use this dialog box to specify the position and size of a comment.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [AdditionalCommentPosition](../../reportapi/objects/report_objects_irepcommentpositionadditionalint.htm) object.

| Size |  |
| --- | --- |
| Width | Specifies the width of the comment, as a percentage of the worksheet, in centimeters or inches. |
| Height | Specifies the height of the comment, as a percentage of the worksheet, in centimeters or inches. |
| Distance to axis system |  |
| Horizontal | Specifies the horizontal distance of the comment to the origin of the axis system, as a percentage of the worksheet, in centimeters or inches. |
| Vertical | Specifies the vertical distance of the comment to the origin of the axis system, as a percentage of the worksheet, in centimeters or inches. |

|  | Note Select Settings»DIAdem Settings»General to specify the unit for scaled display. |
| --- | --- |

#### Further Settings

[Marker](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_marker_dialog.htm) | [Coordinate Labels» Text](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_label_text_dialog.htm) | [Coordinate Labels » Text Parameters](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_label_textpar_dialog.htm) | [Comment » Text](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_comment_comment_tab_text_dialog.htm) | [Coomment » Frame and Arrow](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_comment_tab_line_dialog.htm) | Comment » Position

#### Other Curve Displays

[Surface](../graph_dlg_3d_curve/d3axis_tab_surface_general_dialog.htm) | [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) | [Waterfall](../graph_dlg_3d_curve/d3axis_tab_waterfall_general_dialog.htm) | [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) | [2D-matrix](../graph_dlg_3d_curve/d3axis_tab_matrix_general_dialog.htm) | [Spikes](../graph_dlg_3d_curve/d3axis_tab_spikes_general_dialog.htm) | [3D curve](../graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm) | [Vector](../graph_dlg_3d_curve/d3axis_tab_vector_dialog.htm) | [Points](../graph_dlg_3d_curve/d3axis_tab_symbol_dialog.htm) | [Characteristic diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm) | Coordinate

#### Procedures

[Creating Formula Graphics in a Report](../../procpresent/frames_graphics/procpres_formulas.htm) | [Displaying Arrows and Lines](../../procpresent/frames_graphics/procpres_arrows.htm) | [Displaying Circles](../../procpresent/frames_graphics/procpres_circles.htm) | [Displaying Comments](../../procpresent/frames_graphics/procpres_comments.htm) | [Displaying Rectangles](../../procpresent/frames_graphics/procpres_frames.htm) | [Inserting Graphics into a Report](../../procpresent/frames_graphics/procpres_graphics.htm)

#### Examples

[Decorations](../../exploff/examples/expl_report_av45.htm) | [Text Objects](../../exploff/examples/expl_report_av1.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_general.htm language=enus -->
## TOPIC 00482: Curve Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > Curve Parameters

Curve Parameters

The following topics describe the dialog boxes where you make your settings for the various 3D curve display modes.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_isolines_general.htm language=enus -->
## TOPIC 00483: Isolines

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_isolines_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_isolines_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Surface](../graph_dlg_3d_curve/d3axis_curveparameters_surface_general.htm) > Isolines

Isolines

The following topics describe the dialog boxes where you make your settings for displaying a 3D curve as isolines.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_surface_general.htm language=enus -->
## TOPIC 00484: Surface

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_surface_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_surface_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > Surface

Surface

The following topics describe the dialog boxes where you make your settings for displaying a 3D curve as a surface.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_surfacesymbols_general.htm language=enus -->
## TOPIC 00485: Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_surfacesymbols_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_curveparameters_surfacesymbols_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Surface](../graph_dlg_3d_curve/d3axis_curveparameters_surface_general.htm) > Labels

Labels

The following topics describe the dialog boxes where you make your settings for displaying a 3D curve as a surface with symbols.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_isolinessymbols_general.htm language=enus -->
## TOPIC 00486: Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_isolinessymbols_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_isolinessymbols_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) > Labels

Labels

The following topics describe the dialog boxes where you make your settings for displaying a 3D curve as isolines with symbols.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_parameters_isolines_general.htm language=enus -->
## TOPIC 00487: Isolines

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_parameters_isolines_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_parameters_isolines_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > Isolines

Isolines

The following topics describe the dialog boxes where you make your settings for displaying a characteristic diagram with isolines.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_points_borderpoints_general.htm language=enus -->
## TOPIC 00488: Boundary Points

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_points_borderpoints_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_points_borderpoints_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > Boundary Points

Boundary Points

The following topics describe the dialog boxes where you make your settings for the labels and markers of the boundary points in a characteristic diagram.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_points_invalidpoint_general.htm language=enus -->
## TOPIC 00489: Invalid Values

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_points_invalidpoint_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_points_invalidpoint_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > Invalid Values

Invalid Values

The following topics describe the dialog boxes in which you configure the labels and markers of the invalid values of a characteristic diagram.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_points_maximum_general.htm language=enus -->
## TOPIC 00490: Maximum

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_points_maximum_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_points_maximum_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > Maximum

Maximum

The following topics describe the dialog boxes where you make your settings for the label and markers of the maximum value in a characteristic diagram.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_points_mean_general.htm language=enus -->
## TOPIC 00491: Mean Values

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_points_mean_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_points_mean_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > Mean Values

Mean Values

The following topics describe the dialog boxes where you make your settings for the label and markers of the mean values in a characteristic diagram.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_points_measpoints_general.htm language=enus -->
## TOPIC 00492: Measurement Points

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_points_measpoints_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_points_measpoints_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > Measurement Points

Measurement Points

The following topics describe the dialog boxes where you make your settings for the labels and markers of the measurement points in a characteristic diagram.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_points_minimum_general.htm language=enus -->
## TOPIC 00493: Minimum

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_points_minimum_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_points_minimum_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > Minimum

Minimum

The following topics describe the dialog boxes where you make your settings for the label and markers of the minimum value in a characteristic diagram.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_symbols_general.htm language=enus -->
## TOPIC 00494: Points

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_symbols_general.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_symbols_general.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) | [Points](../graph_dlg_3d_curve/d3axis_symbols_general.htm)) > Points

Points

The following topics describe the dialog boxes where you configure the display of a 3D curve with labels.

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm language=enus -->
## TOPIC 00495: Curve Parameters: 3D Curve » General

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > Curve Parameters: 3D Curve » General

Curve Parameters: 3D Curve » General

Use this dialog box to specify the curve display in a 3D axis system. If you selected the curve color **Palette** or **Glob. Palette, set the line parameters in the dialog boxes to [Color Palette](../graph_dlg_3d_tab/dlgd3colorpal_dialog.htm) or [Global Color Palette](../graph_dlg_menu/dlgpicpal_dialog.htm).**

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [3DLineExtensions](../../reportapi/objects/report_objects_irepd3shapeobjlineextensionsint.htm) object.

| Line style | Specifies the line style of the curve. |
| --- | --- |
| Line width | Specifies the line width of the curve. |
| Line interval | Specifies the interval and the length of the line sections for broken line display. |
| Use color channel | Specifies for the curve color Palette whether the colors are the same as the colors of the y-ranges or whether you must specify a color channel with which DIAdem displays the curve in the palette colors. |
| Color channel | Specifies the color channel with which DIAdem displays the curve in the colors of the palette. |
| Display 3D curve | Specifies whether DIAdem displays the 3D curve. |
| Project to XY plane | Specifies whether to project the 3D curve onto the XY plane. |
| Project to YZ plane | Specifies whether to project the 3D curve onto the YZ plane. |
| Project to XZ plane | Specifies whether to project the 3D curve onto the XZ plane. |

#### Further Settings

General | [Spikes](../graph_dlg_3d_curve/d3axis_tab_3dcurve_spike_dialog.htm) | [Labels » Text](../graph_dlg_3d_curve/d3axis_tab_3dcurve_symbol_dialog.htm) | [Labels » Position](../graph_dlg_3d_curve/d3axis_tab_3dcurve_symbol_position_dialog.htm) | [Labels » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_3dcurve_symbol_textpar_dialog.htm) | [Markers](../graph_dlg_3d_curve/d3axis_tab_3dcurve_marker_dialog.htm)

#### Other Curve Displays

[Surface](../graph_dlg_3d_curve/d3axis_tab_surface_general_dialog.htm) | [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) | [Waterfall](../graph_dlg_3d_curve/d3axis_tab_waterfall_general_dialog.htm) | [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) | [2D-matrix](../graph_dlg_3d_curve/d3axis_tab_matrix_general_dialog.htm) | [Spikes](../graph_dlg_3d_curve/d3axis_tab_spikes_general_dialog.htm) | 3D curve | [Vector](../graph_dlg_3d_curve/d3axis_tab_vector_dialog.htm) | [Points](../graph_dlg_3d_curve/d3axis_tab_symbol_dialog.htm) | [Characteristic diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) | [Coordinate](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_marker_dialog.htm)

#### Procedures

[Changing Layout Templates in DIAdem REPORT](../../procpresent/report_general/procpres_action_bar.htm) | [Changing the Worksheet Parameters](../../procpresent/report_general/procpres_layout_worksheet.htm) | [Creating a Master Layout](../../procpresent/report_general/procpres_masterlayout_connect.htm) | [Displaying 3D Curves in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_spacecurves.htm) | [Displaying Surfaces in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_plains.htm) | [Formatting Numeric Displays](../../procpresent/report_general/procpres_data_format.htm) | [Importing Layout Files](../../procpresent/report_general/procpres_layout_import.htm) | [Inserting Objects into a Report](../../procpresent/report_general/procpres_object_insert.htm) | [Moving Coordinate Planes in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_layers.htm) | [Moving Objects in a Report to the Background or the Foreground](../../procpresent/report_general/procpres_object_infront.htm) | [Processing Global Color Palettes](../../procpresent/report_general/procpres_colorpalettes_changing.htm) | [Rotating 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_angle.htm) | [Scaled Report Display](../../procpresent/report_general/procpres_layout_scaled.htm) | [Transferring REPORT Layouts to DIAdem VIEW](../../procpresent/report_general/procpres_transfer_view.htm) | [Using Master Layouts](../../procpresent/report_general/procpres_masterlayout_use.htm) | [Zooming Objects In and Out in a Report](../../procpresent/report_general/procpres_object_size.htm)

#### Examples

[Displaying 3D Curves in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_spacecurves.htm) | [Displaying Surfaces in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_plains.htm) | [Moving Coordinate Planes in 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_layers.htm) | [Rotating 3D Axis Systems](../../procpresent/axis_systems/procpres_3daxis_angle.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_textpar_dialog.htm language=enus -->
## TOPIC 00496: Curve Parameters: Characteristic Diagram » Isolines » Text Parameters

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_textpar_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_textpar_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Isolines](../graph_dlg_3d_curve/d3axis_parameters_isolines_general.htm) > Curve Parameters: Characteristic Diagram » Isolines » Text Parameters

Curve Parameters: Characteristic Diagram » Isolines » Text Parameters

Use this dialog box to specify how DIAdem displays labels in 3D axis systems. DIAdem displays these settings only for the xy-plane view. The XY-plane can be rotated freely around the z-axis. Select [3D Axis Definition»Axis System](../graph_dlg_3d_tab/d3axis_tab_axis_dialog.htm) to set this view.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [3DAdditionalCharacteristicDiagramIsoline](../../reportapi/objects/report_objects_irepd3characteristicdiagramisolineadditionalint.htm) object.

| Isolines | Specifies whether DIAdem also displays isolines. |
| --- | --- |
| Extended isolines | Specifies whether DIAdem also displays extended isolines. Extended isolines allow you to highlight individual isolines. |
| Font | Specifies the font for the labels. |
| Font size | Specifies the font size for the labels. |
| Font color | Specifies the font color for the labels. |
| Highlighting color | Specifies the font color with which you highlight the labels. Use the Transparency setting to specify the highlighting intensity. |
| Color Palette | Opens the dialog box where you specify the color assignments for the font color Palette. |
| Angle | Specifies the angle of the symbol label. |
| Position | Specifies the position of the labels in relation to the curve data points. |
| Bold | Specifies whether DIAdem uses bold font to display the labels. |
| Italics | Specifies whether DIAdem uses italic font to display the labels. |
| Underline | Specifies whether DIAdem uses underline font to display the labels. |
| Strikethrough | Specifies whether DIAdem uses strikethrough font to display the labels. |
| Frame | Specifies whether DIAdem frames each label. |
| Include isovalues when autoscaling | Specifies whether DIAdem includes the isovalues which DIAdem takes from a data channel, the contour table, or the extended isolines when autoscaling the axes. |

#### Further Settings

[Surface](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) | [Isolines » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_dialog.htm) | [Isolines » Text](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_text_dialog.htm) | Isolines » Text Parameters | [Isolines » Extended](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_advanced_dialog.htm) | [Contour Table](../graph_dlg_3d_curve/d3axis_tab_cdiagram_contour_table_dialog.htm) | [Interpolation](../graph_dlg_3d_curve/d3axis_tab_cdiagram_interpolation_dialog.htm) | [Boundary Curve](../graph_dlg_3d_curve/d3axis_tab_cdiagram_boundarycurve_dialog.htm) | [Points» Measurement Points» Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm) | [Points» Minimum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_label_dialog.htm) | [Points » Maximum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_label_dialog.htm) | [Points » Boundary Points » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_label_dialog.htm) | [Points » Mean Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_label_dialog.htm) | [Points» Invalid Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_label_dialog.htm) | [Points » Measurement Points» Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_marker_dialog.htm) | [Points » Minimum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_marker_dialog.htm) | [Points » Maximum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_marker_dialog.htm) | [Points » Boundary Points » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_marker_dialog.htm) | [Points » Mean Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_marker_dialog.htm) | [Points » Invalid Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_marker_dialog.htm) | [Hyperbola » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_dialog.htm) | [Hyperbola » Lines](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_line_dialog.htm) | [Hyperbola » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_textpar_dialog.htm)

#### Other Curve Displays

[Surface](../graph_dlg_3d_curve/d3axis_tab_surface_general_dialog.htm) | [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) | [Waterfall](../graph_dlg_3d_curve/d3axis_tab_waterfall_general_dialog.htm) | [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) | [2D-matrix](../graph_dlg_3d_curve/d3axis_tab_matrix_general_dialog.htm) | [Spikes](../graph_dlg_3d_curve/d3axis_tab_spikes_general_dialog.htm) | [3D curve](../graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm) | [Vector](../graph_dlg_3d_curve/d3axis_tab_vector_dialog.htm) | [Points](../graph_dlg_3d_curve/d3axis_tab_symbol_dialog.htm) | Characteristic diagram| [Coordinate](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_marker_dialog.htm)

#### Examples

[Diesel Diagram](../../exploff/examples/expl_report_ab3.htm) | [Pump Diagram](../../exploff/examples/expl_report_ab5.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_marker_dialog.htm language=enus -->
## TOPIC 00497: Curve Parameters: Characteristic Diagram » Points » Maximum » Markers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_marker_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_marker_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > [Maximum](../graph_dlg_3d_curve/d3axis_points_maximum_general.htm) > Curve Parameters: Characteristic Diagram » Points » Maximum » Markers

Curve Parameters: Characteristic Diagram » Points » Maximum » Markers

Use this dialog box to specify how DIAdem displays maximum values of a characteristic diagram in 3D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [3DAdditionalMarker](../../reportapi/objects/report_objects_irepd3markeradditionalint.htm) object.

| Maximum | Specifies whether DIAdem also selects the maximum measurement points. DIAdem only displays valid points and peak values without NoValues as x- or y-values. |
| --- | --- |
| Marker style | Specifies the symbol for the markers on the curve. |
| Line width | Specifies the line width of the markers. |
| Size | Specifies the size of the markers. |
| Marker color | Specifies the color of the markers. If you select Same Color as Curve, you specify that DIAdem displays the markers in the same color as the curve. |
| Filling color | Specifies the filling color of the markers. If you select Same Color as Curve, you specify that DIAdem displays the marker filling in the same color as the curve. |

#### Further Settings

[Surface](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) | [Isolines » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_dialog.htm) | [Isolines » Text](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_text_dialog.htm) | [Isolines » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_textpar_dialog.htm) | [Isolines » Extended](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_advanced_dialog.htm) | [Contour Table](../graph_dlg_3d_curve/d3axis_tab_cdiagram_contour_table_dialog.htm) | [Interpolation](../graph_dlg_3d_curve/d3axis_tab_cdiagram_interpolation_dialog.htm) | [Boundary Curve](../graph_dlg_3d_curve/d3axis_tab_cdiagram_boundarycurve_dialog.htm) | [Points» Measurement Points» Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm) | [Points» Minimum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_label_dialog.htm) | [Points » Maximum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_label_dialog.htm) | [Points » Boundary Points » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_label_dialog.htm) | [Points » Mean Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_label_dialog.htm) | [Points» Invalid Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_label_dialog.htm) | [Points » Measurement Points» Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_marker_dialog.htm) | [Points » Minimum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_marker_dialog.htm) | Points » Maximum » Markers | [Points » Boundary Points » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_marker_dialog.htm) | [Points » Mean Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_marker_dialog.htm) | [Points » Invalid Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_marker_dialog.htm) | [Hyperbola » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_dialog.htm) | [Hyperbola » Lines](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_line_dialog.htm) | [Hyperbola » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_textpar_dialog.htm)

#### Other Curve Displays

[Surface](../graph_dlg_3d_curve/d3axis_tab_surface_general_dialog.htm) | [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) | [Waterfall](../graph_dlg_3d_curve/d3axis_tab_waterfall_general_dialog.htm) | [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) | [2D-matrix](../graph_dlg_3d_curve/d3axis_tab_matrix_general_dialog.htm) | [Spikes](../graph_dlg_3d_curve/d3axis_tab_spikes_general_dialog.htm) | [3D curve](../graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm) | [Vector](../graph_dlg_3d_curve/d3axis_tab_vector_dialog.htm) | [Points](../graph_dlg_3d_curve/d3axis_tab_symbol_dialog.htm) | Characteristic diagram| [Coordinate](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_marker_dialog.htm)

#### Examples

[Diesel Diagram](../../exploff/examples/expl_report_ab3.htm) | [Pump Diagram](../../exploff/examples/expl_report_ab5.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_label_dialog.htm language=enus -->
## TOPIC 00498: Curve Parameters: Characteristic Diagram » Points » Mean Values » Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_label_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_label_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > [Mean Values](../graph_dlg_3d_curve/d3axis_points_mean_general.htm) > Curve Parameters: Characteristic Diagram » Points » Mean Values » Labels

Curve Parameters: Characteristic Diagram » Points » Mean Values » Labels

Use this dialog box to specify how DIAdem displays the mean values of the tolerance bands of a characteristic diagram in 3D axis systems. These settings are only available if you select **Partial load structure** in the [Data Check](../graph_dlg_3d_tab/d3axis_cd_partialload_dialog.htm) dialog box.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [3DCharacteristicDiagramPointsLabel](../../reportapi/objects/report_objects_irepd3characteristicdiagrampointslabelint.htm) object.

|  | Mean values of the tolerance bands | Specifies whether DIAdem also selects the mean values of the tolerance bands. |
| --- | --- | --- |
|  | Mean values | Specifies that DIAdem labels the additional mean values of the tolerance bands in characteristic diagrams. |
|  | Font | Specifies the font for the maximum measurement points. |
|  | Font size | Specifies the font size for the maximum measurement points. |
|  | Format | Specifies the format definition for the maximum measurement points. You can include subscript and superscript in text, format numbers, include variable contents, or use scripts for complex formats. Refer to the page on Formatting Text for more information. |
|  | Format Numbers | Opens the dialog box where you select or enter the format specification. |
|  | Angle | Specifies the angle of the label of the maximum measurement points. |
|  | Position | Specifies the position of the maximum measurement points in relation to the curve data points. |
|  | Font color | Specifies the font color for the maximum measurement points. |
|  | Highlighting color | Specifies the font color with which you highlight the labels. Use the Transparency setting to specify the highlighting intensity. |
|  | Color Palette | Opens the dialog box where you specify the color assignments for the font color Palette. |
|  | Bold | Specifies whether DIAdem uses bold font to display the maximum measurement points. |
|  | Italics | Specifies whether DIAdem uses italic font to display the maximum measurement points. |
|  | Underline | Specifies whether DIAdem uses underline font to display the maximum measurement points. |
|  | Strikethrough | Specifies whether DIAdem uses strikethrough font to display the maximum measurement points. |
|  | Frame | Specifies whether DIAdem frames each maximum measurement point. |

#### Further Settings

[Surface](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) | [Isolines » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_dialog.htm) | [Isolines » Text](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_text_dialog.htm) | [Isolines » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_textpar_dialog.htm) | [Isolines » Extended](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_advanced_dialog.htm) | [Contour Table](../graph_dlg_3d_curve/d3axis_tab_cdiagram_contour_table_dialog.htm) | [Interpolation](../graph_dlg_3d_curve/d3axis_tab_cdiagram_interpolation_dialog.htm) | [Boundary Curve](../graph_dlg_3d_curve/d3axis_tab_cdiagram_boundarycurve_dialog.htm) | [Points» Measurement Points» Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm) | [Points» Minimum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_label_dialog.htm) | [Points » Maximum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_label_dialog.htm) | [Points » Boundary Points » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_label_dialog.htm) | Points » Mean Values » Labels | [Points» Invalid Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_label_dialog.htm) | [Points » Measurement Points» Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_marker_dialog.htm) | [Points » Minimum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_marker_dialog.htm) | [Points » Maximum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_marker_dialog.htm) | [Points » Boundary Points » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_marker_dialog.htm) | [Points » Mean Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_marker_dialog.htm) | [Points » Invalid Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_marker_dialog.htm) | [Hyperbola » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_dialog.htm) | [Hyperbola » Lines](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_line_dialog.htm) | [Hyperbola » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_textpar_dialog.htm)

#### Other Curve Displays

[Surface](../graph_dlg_3d_curve/d3axis_tab_surface_general_dialog.htm) | [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) | [Waterfall](../graph_dlg_3d_curve/d3axis_tab_waterfall_general_dialog.htm) | [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) | [2D-matrix](../graph_dlg_3d_curve/d3axis_tab_matrix_general_dialog.htm) | [Spikes](../graph_dlg_3d_curve/d3axis_tab_spikes_general_dialog.htm) | [3D curve](../graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm) | [Vector](../graph_dlg_3d_curve/d3axis_tab_vector_dialog.htm) | [Points](../graph_dlg_3d_curve/d3axis_tab_symbol_dialog.htm) | Characteristic diagram| [Coordinate](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_marker_dialog.htm)

#### Examples

[Diesel Diagram](../../exploff/examples/expl_report_ab3.htm) | [Pump Diagram](../../exploff/examples/expl_report_ab5.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_marker_dialog.htm language=enus -->
## TOPIC 00499: Curve Parameters: Characteristic Diagram » Points » Mean Values » Markers

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_marker_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_marker_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > [Mean Values](../graph_dlg_3d_curve/d3axis_points_mean_general.htm) > Curve Parameters: Characteristic Diagram » Points » Mean Values » Markers

Curve Parameters: Characteristic Diagram » Points » Mean Values » Markers

Use this dialog box to specify how DIAdem displays the mean values of the tolerance bands of a characteristic diagram in 3D axis systems. These settings are only available if you select **Partial load structure** in the [Data Check](../graph_dlg_3d_tab/d3axis_cd_partialload_dialog.htm) dialog box.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [3DAdditionalMarker](../../reportapi/objects/report_objects_irepd3markeradditionalint.htm) object.

| Mean values | Specifies whether DIAdem also selects the mean values of the tolerance bands. |
| --- | --- |
| Marker style | Specifies the symbol for the markers on the curve. |
| Line width | Specifies the line width of the markers. |
| Size | Specifies the size of the markers. |
| Marker color | Specifies the color of the markers. If you select Same Color as Curve, DIAdem displays the markers the same color as the curve. |
| Filling color | Specifies the filling color of the markers. If you select Same Color as Curve, you specify that DIAdem displays the marker filling the same color as the curve. |

#### Further Settings

[Surface](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) | [Isolines » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_dialog.htm) | [Isolines » Text](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_text_dialog.htm) | [Isolines » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_textpar_dialog.htm) | [Isolines » Extended](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_advanced_dialog.htm) | [Contour Table](../graph_dlg_3d_curve/d3axis_tab_cdiagram_contour_table_dialog.htm) | [Interpolation](../graph_dlg_3d_curve/d3axis_tab_cdiagram_interpolation_dialog.htm) | [Boundary Curve](../graph_dlg_3d_curve/d3axis_tab_cdiagram_boundarycurve_dialog.htm) | [Points» Measurement Points» Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm) | [Points» Minimum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_label_dialog.htm) | [Points » Maximum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_label_dialog.htm) | [Points » Boundary Points » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_label_dialog.htm) | [Points » Mean Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_label_dialog.htm) | [Points» Invalid Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_label_dialog.htm) | [Points » Measurement Points» Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_marker_dialog.htm) | [Points » Minimum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_marker_dialog.htm) | [Points » Maximum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_marker_dialog.htm) | [Points » Boundary Points » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_marker_dialog.htm) | Points » Mean Values » Markers | [Points » Invalid Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_marker_dialog.htm) | [Hyperbola » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_dialog.htm) | [Hyperbola » Lines](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_line_dialog.htm) | [Hyperbola » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_textpar_dialog.htm)

#### Other Curve Displays

[Surface](../graph_dlg_3d_curve/d3axis_tab_surface_general_dialog.htm) | [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) | [Waterfall](../graph_dlg_3d_curve/d3axis_tab_waterfall_general_dialog.htm) | [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) | [2D-matrix](../graph_dlg_3d_curve/d3axis_tab_matrix_general_dialog.htm) | [Spikes](../graph_dlg_3d_curve/d3axis_tab_spikes_general_dialog.htm) | [3D curve](../graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm) | [Vector](../graph_dlg_3d_curve/d3axis_tab_vector_dialog.htm) | [Points](../graph_dlg_3d_curve/d3axis_tab_symbol_dialog.htm) | Characteristic diagram| [Coordinate](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_marker_dialog.htm)

#### Examples

[Diesel Diagram](../../exploff/examples/expl_report_ab3.htm) | [Pump Diagram](../../exploff/examples/expl_report_ab5.htm)

<!--NI_TOPIC bundle=diadem path=dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm language=enus -->
## TOPIC 00500: Curve Parameters: Characteristic Diagram » Points » Measurement Points » Labels

- bundle_id: `diadem`
- source_path: `dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgpresent/graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_label_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportdlgs_overview.htm) > [3D Axis Systems](../graph_dlg_3d_curve/3daxissystems_general.htm) > [Curve parameters](../graph_dlg_3d_curve/d3axis_curveparameters_general.htm) > [Characteristic Diagram](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) > [Points](../graph_dlg_3d_curve/d3axis_cdiagrampoints_general.htm) > [Measurement Points](../graph_dlg_3d_curve/d3axis_points_measpoints_general.htm) > Curve Parameters: Characteristic Diagram » Points » Measurement Points » Labels

Curve Parameters: Characteristic Diagram » Points » Measurement Points » Labels

Use this dialog box to specify how DIAdem displays measurement points of a characteristic diagram in 3D axis systems.

#### Settings

The following settings are in the object-oriented script interface for DIAdem REPORT in the properties and methods of the [3DAdditionalCharacteristicDiagramPoints](../../reportapi/objects/report_objects_irepd3characteristicdiagrampointsadditionalint.htm) object.

|  | Measurement points | Specifies whether DIAdem also selects the measurement points. DIAdem only displays valid points and peak values without NoValues as x- or y-values. |
| --- | --- | --- |
|  | Z-value at point | Specifies that DIAdem labels the additional measurement points in characteristic diagrams with the z-value of the measurement points. |
|  | Data reduction value | Specifies whether DIAdem displays the measured values or the values of the data reduction. This setting is only available if the data has a triplet structure and if the display type is not a differential characteristic diagram. |
|  | Font | Specifies the font for the measurement point labels. |
|  | Font size | Specifies the font size of the measurement point labels. |
|  | Format | Specifies the format instructions of the measurement point labels. You can include subscript and superscript in text, format numbers, include variable contents, or use scripts for complex formats. Refer to the page on Formatting Text for more information. |
|  | Format Numbers | Opens the dialog box where you select or enter the format specification. |
|  | Angle | Specifies the angle of the measurement point labels. |
|  | Position | Specifies the position of the measurement point labels in relation to the curve data points. |
|  | Font color | Specifies the font color for the measurement point labels. |
|  | Highlighting color | Specifies the color in which you highlight the labels. Use the Transparency setting to specify the highlighting intensity. |
|  | Color Palette | Opens the dialog box where you specify the color assignments for the font color Palette. |
|  | Bold | Specifies whether DIAdem uses bold font to display the measurement point labels. |
|  | Italics | Specifies whether DIAdem uses italic font to display the measurement point labels. |
|  | Underline | Specifies whether DIAdem uses underline font to display the measurement point labels. |
|  | Strikethrough | Specifies whether DIAdem uses strikethrough font to display the measurement point labels. |
|  | Frame | Specifies whether DIAdem frames each measurement point label. |

#### Further Settings

[Surface](../graph_dlg_3d_curve/d3axis_tab_cdiagram_general_dialog.htm) | [Isolines » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_dialog.htm) | [Isolines » Text](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_text_dialog.htm) | [Isolines » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_textpar_dialog.htm) | [Isolines » Extended](../graph_dlg_3d_curve/d3axis_tab_cdiagram_isolines_advanced_dialog.htm) | [Contour Table](../graph_dlg_3d_curve/d3axis_tab_cdiagram_contour_table_dialog.htm) | [Interpolation](../graph_dlg_3d_curve/d3axis_tab_cdiagram_interpolation_dialog.htm) | [Boundary Curve](../graph_dlg_3d_curve/d3axis_tab_cdiagram_boundarycurve_dialog.htm) | Points» Measurement Points» Labels | [Points» Minimum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_label_dialog.htm) | [Points » Maximum » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_label_dialog.htm) | [Points » Boundary Points » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_label_dialog.htm) | [Points » Mean Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_label_dialog.htm) | [Points» Invalid Values » Labels](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_label_dialog.htm) | [Points » Measurement Points» Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_measpoint_marker_dialog.htm) | [Points » Minimum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_minpoint_marker_dialog.htm) | [Points » Maximum » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_maxpoint_marker_dialog.htm) | [Points » Boundary Points » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_envpoint_marker_dialog.htm) | [Points » Mean Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_meanpoint_marker_dialog.htm) | [Points » Invalid Values » Markers](../graph_dlg_3d_curve/d3axis_tab_cdiagram_point_invalidpoint_marker_dialog.htm) | [Hyperbola » General](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_dialog.htm) | [Hyperbola » Lines](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_line_dialog.htm) | [Hyperbola » Text Parameters](../graph_dlg_3d_curve/d3axis_tab_cdiagram_hyperbola_textpar_dialog.htm)

#### Other Curve Displays

[Surface](../graph_dlg_3d_curve/d3axis_tab_surface_general_dialog.htm) | [Isolines](../graph_dlg_3d_curve/d3axis_tab_isolines_general_dialog.htm) | [Waterfall](../graph_dlg_3d_curve/d3axis_tab_waterfall_general_dialog.htm) | [Bars](../graph_dlg_3d_curve/d3axis_tab_bar_general_dialog.htm) | [2D-matrix](../graph_dlg_3d_curve/d3axis_tab_matrix_general_dialog.htm) | [Spikes](../graph_dlg_3d_curve/d3axis_tab_spikes_general_dialog.htm) | [3D curve](../graph_dlg_3d_curve/d3axis_tab_3dcurve_general_dialog.htm) | [Vector](../graph_dlg_3d_curve/d3axis_tab_vector_dialog.htm) | [Points](../graph_dlg_3d_curve/d3axis_tab_symbol_dialog.htm) | Characteristic diagram| [Coordinate](../graph_dlg_3d_curve/d3axis_curve_par_coordinate_marker_dialog.htm)

#### Examples

[Diesel Diagram](../../exploff/examples/expl_report_ab3.htm) | [Pump Diagram](../../exploff/examples/expl_report_ab5.htm)
