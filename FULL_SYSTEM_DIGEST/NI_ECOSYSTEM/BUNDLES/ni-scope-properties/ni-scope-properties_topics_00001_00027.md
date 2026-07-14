# NI DOCUMENT BUNDLE: ni-scope-properties

<!--NI_BUNDLE_CHUNK bundle=ni-scope-properties start=1 end=27 -->
<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/cniscope.html language=enus -->
## TOPIC 00001: niScope Properties

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/cniscope.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/cniscope.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### niScope Properties

May 2020

Use the NI-SCOPE properties to access advanced configuration options for high-speed digitizer applications.

| Property | Description |
| --- | --- |
| Active Channel | Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is Channel Based, you need to first select this property and then pass the name of the specific channel. If the property you specify is not channel based, pass an empty string, or omit setting this property. The default value is " ". Details |
| Vertical:Channel Enabled | Specifies whether the digitizer acquires a waveform for the channel. Details |
| Vertical:Vertical Range | Specifies the absolute value of the input range for a channel. The units are volts. For example, to acquire a sine wave that spans between -5 and +5 V, set this property to 10.0 V. Details |
| Vertical:Vertical Offset | Specifies the location of the center of the range. The value is with respect to ground and is in volts. For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this property to 5.0 V. This property is not supported by all digitizers. Details |
| Vertical:Maximum Input Frequency | Specifies the bandwidth of the channel in hertz. Express this value as the frequency at which the input circuitry attenuates the input signal by 3 dB. Details |
| Vertical:Vertical Coupling | Specifies how the digitizer couples the input signal for the channel. When you change input coupling, the input stage takes a finite amount of time to settle. Details |
| Vertical:Input Impedance | Specifies the input impedance for the channel in ohms. Details |
| Vertical:Probe Attenuation | Specifies the probe attenuation for the input channel. For example, for a 10:1 probe, you would set this property to 10.0. Details |
| Vertical:Channel Terminal Configuration | Specifies how the digitizer configures the channel terminal. Details |
| Vertical:Advanced:Digital Gain | Applies gain to the specified channel in hardware before any onboard signal processing occurs. The default value is 1. The output of the digital gain/offset block is as follows: (ADC value × digital gain) + digital offset Units: Unitless Valid Values: -1.5 to 1.5 Details |
| Vertical:Advanced:Digital Offset | Applies offset to the specified channel in hardware before any onboard signal processing occurs. The default value is 0. Units: Volts Valid Values ±(Vertical Range × 0.4) Details |
| Vertical:Advanced:Bandpass Filter Enabled | Enables the bandpass filter on the specified channel. For the NI PXIe-5622, set the value to TRUE to enable the IF filtered path 50MHz bandpass filter centered at 187MHz. The default value is FALSE. Details |
| Vertical:Advanced:Dither Enabled | Enables or disables the analog dither on the device. Using dither can improve the spectral performance of the device by reducing the effects of quantization. However, adding dither increases the power level to the ADC, so you may need to either decrease the signal level or increase the vertical range. The default value is FALSE. Details |
| Vertical:Advanced:Flex FIR Antialias Filter Type | The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter. Use this property to select from several types of filters to achieve desired filtering characteristics. For most applications, the default value of this property is recommended. The other available filters are useful for optimizing settling time measurements of step responses. The default value is 48 Tap Standard. Details |
| Vertical:Advanced:High Pass Filter Frequency | Specifies the frequency for the highpass filter in Hz. The device uses one of the valid values listed below. If an invalid value is specified, no coercion occurs. The default value is 0. (PXIe-5164) Valid Values: 0 90 450 |
| Vertical:Advanced:Interleaving Offset Correction Enabled | Enables the interleaving offset correction on the specified channel. The default value is TRUE. Details |
| Horizontal:Min Sample Rate | Specifies the sampling rate (in Samples/second) for the acquisition. This attribute is invalid when the device is configured to use an external sample clock timebase. When a DDC is enabled, this attribute specifices the IQ rate. When both the Time Per Record Property and the Min Sample Rate Property are set, the attribute that was set first is ignored. Details |
| Horizontal:Min Number of Points | Specifies the minimum number of points you require in the waveform record for each channel. Details |
| Horizontal:Number of Records | Specify the number of records to acquire. Details |
| Horizontal:Reference Position | Specifies the position of the Reference Event in the waveform record as a percentage of the record. Details |
| Horizontal:Actual Sample Rate | Returns the actual sample rate used for the acquisition. Units: hertz (Samples / Second) Details |
| Horizontal:Actual Record Length | Returns the actual number of points the digitizer acquires for each channel. The value is equal to or greater than the value you specify in the niScope Configure Horizontal Timing VI. Valid Values: 1 to the maximum memory size Details |
| Horizontal:Enable Time Interleaved Sampling | Extends the maximum sample rate on the specified Active Channel for some devices that support Time Interleaved Sampling (TIS). TIS enables the device to use multiple ADCs to sample the same waveform at a higher effective real-time rate. NI 5152/5153/5154 devices fully support Read/Write ability for this property. For other devices that use TIS mode, such as the NI 5185/5186, this property is Read Only. Details |
| Horizontal:Enforce Realtime | Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements. Details |
| Horizontal:Enable Records > Memory | Allows you to acquire more records than fit in onboard memory. TRUE—Enables NI-SCOPE to fetch more records than fit in memory FALSE—Disables NI-SCOPE from fetching more records than fit in memory Details |
| Horizontal:RIS Num Avg | Specifies the number of averages in each RIS bin. Details |
| Horizontal:RIS Method | Specifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the Max Realtime Sample Rate. Details |
| Horizontal:Maximum Real Time Sample Rate | Returns the maximum real-time sample rate in hertz. Details |
| Horizontal:Maximum RIS Rate | Returns the maximum RIS sampling rate in hertz. Details |
| Horizontal:Memory Size | Returns the total combined amount of onboard memory for all channels in bytes. Details |
| Horizontal:Advanced:Enable TDC | Specifies that the digitizer should record the trigger position precisely using time-digital conversion (TDC). Details |
| Horizontal:Advanced:Time Per Record | Specifies the length of time (in seconds) that corresponds to the record length. This attribute is invalid when the device is configured to use an external sample clock timebase. This attribute is also invalid when a DDC is enabled. When both the Time Per Record Property and the Min Sample Rate Property are set, the attribute that was set first is ignored. Details |
| Horizontal:Advanced:Acquisition Start Time | Specifies the length of time (in seconds) from the trigger event to the first point in the waveform record. Details |
| Triggering:Trigger Type | Specifies the type of trigger to use. Details |
| Triggering:Trigger Source | Specifies the source the digitizer monitors for the trigger event. The value must be selected from one of the following valid values. Details |
| Triggering:Trigger Output Terminal | Specifies the destination to export the Reference (Stop) Trigger Refer to the device specifications document for a list of valid destinations. Details |
| Triggering:Terminal Name | Returns the fully qualified name for the Reference Trigger terminal. Details |
| Triggering:Trigger Level | Specifies the voltage threshold for the trigger. The units are volts. Details |
| Triggering:Trigger Modifier | Configures the device to automatically complete an acquisition if a trigger has not been received. Details |
| Triggering:Auto Triggered | Specifies whether the acquisition was triggered automatically. Auto triggering occurs if the Trigger Modifier property is set to Auto Trigger and no trigger has been received for a certain amount of time. Details |
| Triggering:Trigger Hysteresis | Specifies the size of the hysteresis window, in volts, on either side of the trigger level. Details |
| Triggering:Trigger Delay | Specifies the trigger delay time in seconds. Details |
| Triggering:Trigger Holdoff | Specifies the length of time the digitizer waits after detecting a trigger before enabling the trigger subsystem to detect another trigger. The units are seconds. Details |
| Triggering:Trigger Slope | Specifies whether a rising or a falling edge triggers the digitizer. Details |
| Triggering:Trigger Coupling | Specifies how the digitizer couples the trigger source. Details |
| Triggering:Trigger Impedance | Sets the impedance for the external trigger input. Details |
| Triggering:Start To Ref Trigger Holdoff | Pass the length of time (in seconds) you want the digitizer to wait after it starts acquiring data until the digitizer enables the trigger system to detect a reference (stop) trigger. Details |
| Triggering:End of Record to Advance Trigger Holdoff | End of Record to Advance Trigger Holdoff is the length of time (in seconds) that a device waits between the completion of one record and the acquisition of pre-trigger samples for the next record. During this time, the acquisition engine state delays the transition to the Wait for Advance Trigger state, and will not store samples in onboard memory, accept an Advance Trigger, or trigger on the input signal.. Supported Devices: NI 5185/5186 Details |
| Triggering:Trigger Window:Window Mode | Specifies whether to trigger when the signal enters or leaves the window specified by the Trigger Window Low Level property or the Trigger Window High Level property. Details |
| Triggering:Trigger Window:Low Level | Pass the lower voltage threshold you want the digitizer to use for window triggering. Details |
| Triggering:Trigger Window:High Level | Pass the upper voltage threshold you want the digitizer to use for window triggering. Details |
| Triggering:Trigger Video:Signal Format | Specifies the video signal format to use. Details |
| Triggering:Trigger Video:Line Number | Specifies the line number to trigger on. Details |
| Triggering:Trigger Video:Polarity | Specifies whether the video signal is positive or negative. Details |
| Triggering:Trigger Video:Event | Specifies the event to trigger on. Details |
| Triggering:Trigger Video:Enable DC Restore | Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point. The default value is FALSE. Details |
| Triggering:Trigger Glitch:Glitch Condition | Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the specified Glitch Width. Details |
| Triggering:Trigger Glitch:Glitch Width | Specifies the glitch duration, in seconds. Details |
| Triggering:Trigger Glitch:Glitch Polarity | Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering. Details |
| Triggering:Trigger Width:Width Condition | Specifies whether the oscilloscope triggers on pulses within or outside the duration range bounded by the Width Low Threshold and Width High Threshold properties. Details |
| Triggering:Trigger Width:Width Low Threshold | Specifies the low width threshold, in seconds. Details |
| Triggering:Trigger Width:Width High Threshold | Specifies the high width threshold, in seconds. Details |
| Triggering:Trigger Width:Width Polarity | Specifies the polarity of pulses that trigger the oscilloscope for width triggering. Details |
| Triggering:Trigger Runt:Runt Low Threshold | Specifies the lower of two thresholds, in volts, that bound the vertical range to examine for runt pulses. Details |
| Triggering:Trigger Runt:Runt High Threshold | Specifies the higher of two thresholds, in volts, that bound the vertical range to examine for runt pulses. Details |
| Triggering:Trigger Runt:Runt Polarity | Specifies the polarity of pulses that trigger the oscilloscope for runt triggering. Details |
| Triggering:Trigger Runt:Runt Time Condition | Specifies whether runt triggers are time qualified, and if so, how the oscilloscope triggers in relation to the duration range bounded by the Runt Time Low Limit and Runt Time High Limit properties. Details |
| Triggering:Trigger Runt:Runt Time Low Limit | Specifies, in seconds, the low runt threshold time. Details |
| Triggering:Trigger Runt:Runt Time High Limit | Specifies, in seconds, the high runt threshold time. Details |
| Device:CableSense:Voltage | Returns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration. Details |
| Device:CableSense:Mode | Specifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the niScope CableSense Signal Start VI is called. Details |
| Acquisition:Enabled Channels | Returns a comma-separated list of the channels enabled for the session in ascending order. Details |
| Triggering:Onboard Signal Processing:Ref Trigger Detection Location | Specifies which reference trigger detection circuitry to use on the device. Details |
| Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time | Specifies the amount of time (in seconds) the trigger circuit must not detect a signal above the trigger level (or below the trigger level if the trigger slope is negative) before the trigger is armed. This property is useful for triggering at the beginning of signal bursts instead of in the middle of signal bursts. The default value is 0. Details |
| Fetch:Fetch Record Number | Sets the record to fetch. The record is from a channel you specify. The default value is 0. Valid Values: Values greater than or equal to 0 Details |
| Fetch:Fetch Number of Records | Fetches multiple records. If you want to fetch all records from the record you specify in the Fetch Record Number property to the last record configured, use -1. The default value is -1. Details |
| Fetch:Fetch Relative To | Specifies which point in the acquired waveform is the first to be fetched. This property specifies what the 'Fetch Offset' is relative to. Details |
| Fetch:Fetch Offset | Sets the offset in samples; the samples returned also depend on the Fetch Relative To property. The default value is 0. Valid Values: All integers Details |
| Fetch:Data Transfer Block Size | Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system. Details |
| Fetch:Fetch Meas Num Samples | Determines the number of samples to fetch from a digitizer when performing a measurement. -1 means fetch all samples from the Fetch Offset property to the end of the current record. The default value is -1. Details |
| Fetch:Points Done | Actual number of samples acquired relative to the configured value for Fetch Relative To, including Fetch Offset, and for the current configured Fetch Record Number. Details |
| Fetch:Fetch Backlog | Specifies the number of points acquired that have not been fetched yet. Details |
| Fetch:Records Done | Returns the number of records your digitizer has acquired. Details |
| Fetch:Advanced:Maximum Bandwidth | Specifies the maximum bandwidth that the device is allowed to consume. The NI device limits itself to transfer fewer bytes per second on the PCIe bus than the value you specify for this property. Details |
| Fetch:Advanced:Preferred Packet Size | Specifies the preferred size of the data field in the PCI Express packet. In general, the larger the packet size, the more efficiently the device uses the bus. However, some systems, because of their implementation, perform better with smaller packet sizes. The value of this property must be a power of two (64, 128, ... , 512). Details |
| Clocking:Reference (Input) Clock Source | Specifies the input source for the PLL reference clock. Defined Values VAL_NO_SOURCE VAL_PFI_0 VAL_PFI_1 VAL_PFI_2 VAL_PXI_CLOCK VAL_CLK_IN VAL_EXTERNAL VAL_RTSI_CLOCK Details |
| Clocking:Reference Clock Rate | If Reference Clock Source is an external source, specifies the frequency (in hertz) of the input clock (reference clock) to which the internal sample clock timebase is synchronized. Details |
| Clocking:Output Clock Source | Specifies the output source for the 10 MHz clock to which the sample clock of another digitizer can be phase-locked. Details |
| Clocking:Sample Clock Timebase Source | Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling. Details |
| Clocking:Sample Clock Timebase Rate | Specifies, in hertz, the frequency of the external clock used as the timebase source if the Sample Clock Timebase Source is an external source or, if the timebase source is the internal clock for oscilloscopes that support multiple onboard clock rates, of the internal clock. Details |
| Clocking:Sample Clock Timebase Divisor | If Sample Clock Timebase Source is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower. Details |
| Clocking:Sample Clock Timebase Multiplier | If Sample Clock Timebase Source is an external source, this property specifies the ratio between the Sample Clock Timebase Rate and the actual sample rate, which can be higher. This property can be used in conjunction with the Sample Clock Timebase Divisor Property. Details |
| Clocking:Exported Sample Clock Output Terminal | Exports the sample clock to a specified terminal. This property is not supported by all digitizers. Details |
| Clocking:Clock Sync Pulse Source | Specifies the line on which the sample clock or the one-time sync pulse is sent or received. Details |
| Clocking:PLL Lock Status | If TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE, the PLL has become unlocked from the external reference clock since it was last checked. Details |
| Clocking:Advanced:Oscillator Phase DAC Value | Gets or sets the binary phase DAC value that controls the delay added to the phase-locked loop (PLL) of the sample clock. Details |
| Clocking:Advanced:Absolute Sample Clock Offset | Gets or sets the absolute time offset, in seconds, of the sample clock relative to the reference clock. Details |
| Device:FPGA Bitfile Path | Gets the absolute file path to the bitfile loaded on the FPGA. Details |
| Synchronization:Start Trigger (Acq. Arm): Source | Specifies the source the digitizer monitors for an acquisition arm trigger. When an acquisition arm trigger is received, the digitizer begins acquiring pretrigger samples. Details |
| Synchronization:Start Trigger (Acq. Arm): Output Terminal | Specifies the destination to export the Start trigger. When the start trigger is received, the digitizer begins acquiring data. Refer to the device specifications document for a list of valid destinations. Details |
| Synchronization:Start Trigger (Acq. Arm):Terminal Name | Returns the fully qualified name for the Start Trigger terminal. Details |
| Synchronization:Ready for Start:Output Terminal | Specifies the destination to export the Start trigger. When the start trigger is received, the digitizer begins acquiring data. Refer to the device specifications document for a list of valid destinations. Details |
| Synchronization:Ready for Start:Terminal Name | Returns the fully qualified name for the Ready for Start Event terminal. Details |
| Synchronization:Advance Trigger:Source | Specifies the source the digitizer monitors for an advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples for the next record. Details |
| Synchronization:Advance Trigger:Output Terminal | Specifies the destination for the advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples. Details |
| Synchronization:Advance Trigger:Terminal Name | Returns the fully qualified name for the Advance Trigger terminal. Details |
| Synchronization:Ready for Advance:Output Terminal | Specifies the destination for the advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples. Details |
| Synchronization:Ready for Advance:Terminal Name | Returns the fully qualified name for the Ready for Advance Event terminal. Details |
| Synchronization:Arm Reference Trigger:Source | Specifies the source the digitizer monitors for an arm reference trigger. When the arm reference trigger is received, the digitizer begins searching for the reference (stop) trigger from the user-configured trigger source. Details |
| Synchronization:Ready for Reference:Output Terminal | Specifies the destination for the Ready for Reference Event. When this event is asserted, the digitizer is ready to receive a reference trigger. Refer to the device-specific documentation in the NI High-Speed Digitizers Help for a list of valid destinations for your device. Details |
| Synchronization:Ready for Reference:Terminal Name | Returns the fully qualified name for the Ready for Reference Event terminal. Details |
| Synchronization:End of Record:Output Terminal | Specifies the destination for the End of Record event. When this event is asserted, the digitizer has completed sampling a record. Refer to the device specifications document for a list of valid destinations. Details |
| Synchronization:End of Record:Terminal Name | Returns the fully qualified name for the End of Record Event terminal. Details |
| Synchronization:End of Acquisition:Output Terminal | Specifies the destination for the End of Acquisition event. When this event is asserted, the digitizer has completed sampling all records. Refer to the device specifications document for a list of valid destinations. Details |
| Synchronization:End of Acquisition:Terminal Name | Returns the fully qualified name for the End of Acquisition Event terminal. Details |
| Synchronization:5 Volt Power:Output Terminal | Specifies the destination for the 5 Volt power signal. Refer to the device specifications document for a list of valid destinations. Details |
| Synchronization:Master Enable | Specifies whether the device is a master or a slave. Details |
| Acquisition:Binary Sample Width | Indicates the bit width of the binary data in the acquired waveform, which can help you determine which Binary Fetch to use. Details |
| Acquisition:Resolution | Indicates the actual resolution in bits of valid data (as opposed to padding bits) in the acquired waveform. Compare to the Binary Sample Width property. Valid Values: 8 to 32 Details |
| Acquisition:Acquisition Type | Specifies how the oscilloscope acquires data and fills the waveform record. Details |
| Acquisition:Sample Mode | Returns the sample mode the digitizer is currently using. Details |
| Acquisition:Advanced:Enable RIS in Auto Setup | Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup. Details |
| Waveform Measurement:Other Channel | Specifies the second channel for two-channel measurements, such as Add Channels. If processing steps are registered with this channel, the processing happens before the waveform is used in a two-channel measurement. The default value is 0. Details |
| Waveform Measurement:Array Gain | Every element of an array is multiplied by this scalar value during the array gain measurement. The default value is 1.0. Details |
| Waveform Measurement:Array Offset | Every element of an array is added to this scalar value during the array offset measurement. The default value is 0.0. Details |
| Waveform Measurement:Hysteresis Percent | Digital hysteresis that is used in several of the scalar waveform measurements. This property specifies the percentage of the full-scale vertical range for the hysteresis window size. The default value is 2%. Details |
| Waveform Measurement:Last Acq. Histogram Size | Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high. The default value is 256. Details |
| Waveform Measurement:Voltage Histogram:Size | Specifies the number of bins in the running voltage histogram. The default value is 256. Details |
| Waveform Measurement:Voltage Histogram:Low Volts | Specifies the minimum voltage value in the running voltage histogram. The default value is -10.0. Details |
| Waveform Measurement:Voltage Histogram:High Volts | Specifies the maximum voltage value in the running voltage histogram. The default value is 10.0. Details |
| Waveform Measurement:Time Histogram:Size | Determines the multiple acquisition time histogram size. The size is set during the first call to a time histogram measurement after you clear the measurement history with niScope Clear Waveform Measurement Stats. Details |
| Waveform Measurement:Time Histogram:Low Volts | Specifies the low voltage limit for the multi-acquisition time histogram. Only points in the waveform between the low and high voltage limits are included in the histogram. The default value is -10.0. Details |
| Waveform Measurement:Time Histogram:High Volts | Specifies the high voltage limit for the Multi-Acquisition time histogram. Only points in the waveform between the low and high voltage limits are included in the histogram. The default value is 10.0 V. Details |
| Waveform Measurement:Time Histogram:Low Time | Specifies the minimum time limit (in seconds) of the multi-acquisition time histogram, where the time is in seconds relative to the trigger position. Only points in the waveform between the low and high time limits are included in the histogram. The default value is -5.0e-4 . Details |
| Waveform Measurement:Time Histogram:High Time | Specifies the maximum time limit (in seconds) of the Multi-Acquisition time histogram, where the time is in seconds relative to the trigger position. Only points in the waveform between the low and high time limits are included in the histogram. The default value is 5.0e-4 . Details |
| Waveform Measurement:Interpolation:Polynomial Interpolation Order | Specifies the order of the polynomial used during the polynomial interpolation array measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid. The default value is 1 (linear interpolation). Details |
| Waveform Measurement:Interpolation:Sampling Factor | The new number of points for polynomial interpolation is the sampling factor times the input number of points. The default value is 0.0. Details |
| Waveform Measurement:Filter:Type | Specifies the type of digital filter. The default value is lowpass. Details |
| Waveform Measurement:Filter:FIR Taps | Specifies the number of taps for the finite impulse response filter. This value must be odd if the filter type is highpass or bandstop. Otherwise, the magnitude response goes to zero as the frequency goes to half the sampling rate. The default value is 25. Valid Values: >0 Details |
| Waveform Measurement:Filter:FIR Window | Specifies the FIR window type. The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters. The default value is None (0). Details |
| Waveform Measurement:Filter:Width | Specifies the width (in Hz) of a bandpass or bandstop filter. The cutoff frequencies are the (center frequency property ± 0.5 × filter width). The default value is 1.0e3. Details |
| Waveform Measurement:Filter:IIR Order | Specifies the order of the infinite impulse response filter. The default value is 2. Valid Values: >0 Details |
| Waveform Measurement:Filter:Cutoff Frequency | Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter. The default value is 1.0e6 Hz. Details |
| Waveform Measurement:Filter:Center Frequency | The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by Filter Width, where the cutoff frequencies are the center width. The default value is 1.0e6 Hz. Details |
| Waveform Measurement:Filter:Ripple | Specifies the amount of passband ripple (in dB) for Chebyshev filters. More ripple gives a sharper cutoff for a given filter order. The default value is 0.1. Valid Values: >0.0 Details |
| Waveform Measurement:Filter:Percent Waveform Transient | The percentage (0 - 100%) of the infinite impulse response (IIR) filtered waveform to eliminate from the beginning of the waveform. This action allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition. The default value is 20.0%. Valid Range: 0.0 - 100.0% Details |
| Waveform Measurement:Reference Levels:Channel Based Low Ref Level | Specifies the low reference level used in many scalar measurements. The default value is 10.0%. Details |
| Waveform Measurement:Reference Levels:Channel Based Mid Ref Level | Specifies the mid reference level used in many scalar measurements. The default value is 50%. Details |
| Waveform Measurement:Reference Levels:Channel Based High Ref Level | Specifies the high reference level used in many scalar measurements. The default value is 90%. Details |
| Waveform Measurement:Reference Levels:Units | Specifies the units for the waveform measurement reference levels. Details |
| Waveform Measurement:Reference Levels:Percentage Units Method | Specifies the method used to map percentage reference units to voltages. The default value is BaseTop. Details |
| Onboard Signal Processing:DDC:DDC Enabled | Enables/disables the digital downconverter (DDC) block of the digitizer. When the DDC block is disabled, all DDC-related properties are disabled and have no effect on the acquired signal. The default value is FALSE. Details |
| Onboard Signal Processing:DDC:Data Processing Mode | The way in which data is processed by the DDC block. The default value is Complex. Details |
| Onboard Signal Processing:DDC:Frequency Translation Enabled | Enables/disables frequency translating the data around the user-selected center frequency down to baseband. The default value is TRUE. Details |
| Onboard Signal Processing:DDC:Center Frequency | The frequency at which the DDC block frequency translates the input data. The default value is 10 MHz. Details |
| Onboard Signal Processing:DDC:Fetch Interleaved IQ Data | Specifies whether a fetch call retrieves a single waveform with I and Q interleaved, or two separate waveforms. If enabled, the number of elements returned by scalar fetch types (such as 16-bit integer) is twice the requested number of samples. If disabled during DDC acquisitions in Complex mode, two noninterleaved arrays of data are returned per channel, per record. Details |
| Onboard Signal Processing:DDC:Q Source | Specifies the channel that is the input to the Q data stream of the DDC. Details |
| Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase I | The I oscillator phase in degrees at the first point acquired. The default value is 0. Valid Values -360 to 360 Details |
| Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q | The Q oscillator phase in degrees at the first point acquired. Use this property only when the Data Processing Mode property is set to Complex. The default value is 90. Valid Values -360 to 360 Details |
| Onboard Signal Processing:Equalization:Equalization Filter Enabled | Enables the onboard signal processing equalization FIR block, which is connected directly to the input signal. The equalization filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1. The default value is FALSE. Details |
| Onboard Signal Processing:Equalization:Equalization Num Coefficients | Returns the number of coefficients that the equalization FIR filter can accept. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1. Details |
| Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled | Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate. The default value is FALSE. Details |
| Onboard Signal Processing:OSP Overflow Error Reporting | Configures error reporting when the onboard signal processing block detects an overflow in any of its stages. Overflows lead to clipping of the waveform. The default value is Warning. Details |
| Peer-to-Peer:P2P Enabled | Specifies whether the digitizer writes data to the peer-to-peer endpoint. This property is endpoint-based. Details |
| Peer-to-Peer:Channels to Stream | Specifies which channels will be written to a peer-to-peer endpoint. If multiple channels are specified, they will be interleaved by sample. This property is endpoint-based. The default value is 0. Details |
| Peer-to-Peer:Endpoint Size | Returns the size, in samples, of the peer-to-peer endpoint. This property is endpoint-based. Details |
| Peer-to-Peer:Samples Available In Endpoint | Returns the current number of samples available to stream from a peer-to-peer endpoint. This property is endpoint-based. Details |
| Peer-to-Peer:Most Samples Available in Endpoint | Returns the most number of samples available to stream from a peer-to-peer endpoint since the last time this property was read. This property is endpoint-based. Details |
| Peer-to-Peer:Samples Transferred | Returns the number of samples transferred through the peer-to-peer endpoint since the endpoint was last reset. This property is endpoint-based. Details |
| Peer-to-Peer:Endpoint Overflow | Returns TRUE if the peer-to-peer endpoint has overflowed. Reset the endpoint to clear the overflow condition. This property is endpoint-based. Details |
| Peer-to-Peer:FIFO Endpoint Count | Returns the number of FIFO-based peer-to-peer endpoints this device supports. Details |
| Peer-to-Peer:Onboard Memory Enabled | Specifies whether the digitizer writes data to onboard memory when a peer-to-peer endpoint is enabled. Details |
| Peer-to-Peer:Stream Relative To | Determines which trigger peer-to-peer data is streamed relative to. The default value is Start Trigger. Details |
| Peer-to-Peer:Samples Transferred Per Record | Returns the number of samples transferred per record when you set the Stream Relative To property to Reference Trigger or Sync Trigger. Details |
| Peer-to-Peer:Manual:Manual Configuration Enabled | Enables and disables manual configuration of a peer-to-peer endpoint. These attributes cannot be used if an endpoint is being configured by NI-P2P, or a resource reservation error will result. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address | Returns the address of a hardware register used to grant permission for the peer-to-peer endpoint to write data to another peer. The type of this address is determined by the Data Transfer Permission Address Type property. Permission is granted in bytes and the register is additive. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type | Specifies the type of address returned to the user from the Data Transfer Permission Address property. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Configuration:Destination Window Address | Specifies the destination for data written by the peer-to-peer endpoint. The type of this address is specified by the Destination Window Address Type property. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Configuration:Destination Window Address Type | Specifies the type of the Destination Window Address property. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Configuration:Destination Window Size | Specifies the size, in bytes, of the destination window determined by the Destination Window Address and Destination Window Address Type properties. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Notification:Push Message On | Specifies the event to push the Message Push Value property to the Message Push Address property. Specifying Done will push the message when the acquisition has completed. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Notification:Message Push Address | Specifies the address to push the Message Push Value to on the event specified by the Push Message On property. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Notification:Message Push Address Type | Specifies the type of the Message Push Address property. This property is endpoint-based. Details |
| Peer-to-Peer:Manual:Notification:Message Push Value | Specifies the value to be pushed to the Message Push Address property on the event specified in the Push Message On property. This property is endpoint-based. Details |
| Device:Temperature | Returns the temperature of the device in degrees Celsius from the onboard sensor. Details |
| Device:Serial Number | Returns the serial number of the device. Details |
| Device:Accessory:Gain | Returns the calibration gain for the current device configuration. Details |
| Device:Accessory:Offset | Returns the calibration offset for the current device configuration. Details |
| Inherent IVI Attributes:User Options:Range Check | Specifies whether to validate property values and function parameters. If enabled, the instrument driver validates the parameter values that you pass to driver functions. Range checking parameters is very useful for debugging. After you validate your program, you can set this property to FALSE to disable range checking and maximize performance. The default value is TRUE. Use niScope Initialize with Options to override this value. Details |
| Inherent IVI Attributes:User Options:Query Instrument Status | Specifies whether the instrument driver queries the instrument status after each operation. Querying the instrument status is very useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize performance. The instrument driver can choose to ignore status checking for particular properties regardless of the setting of this property. The default value is TRUE. Use niScope Initialize with Options to override this value. Details |
| Inherent IVI Attributes:User Options:Cache | Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, you can significantly increase execution speed. The instrument driver can choose always to cache or never to cache particular properties, regardless of the setting of this property. The default value is TRUE. Use niScope Initialize with Options to override this value. Details |
| Inherent IVI Attributes:User Options:Simulate | Specifies whether to simulate instrument driver I/O operations. The default value is FALSE. Use niScope Initialize with Options to override this value. Details |
| Inherent IVI Attributes:User Options:Record Value Coercions | Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and DBL properties. The default value is FALSE. Use niScope Initialize with Options to override this value. Details |
| Inherent IVI Attributes:User Options:Interchange Check | Specifies whether to perform interchangeability checking and log interchangeability warnings when you call VIs. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Details |
| Inherent IVI Attributes:Driver Identification:Description | A string that contains the description of the instrument. Details |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | A string that contains the prefix for the instrument driver. The name of each user-callable function in this driver starts with this prefix. Details |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | A string that contains the name of the vendor that supplies this driver, for example, "National Instruments". Details |
| Inherent IVI Attributes:Driver Identification:Revision | The string that contains additional version information about this instrument driver. Details |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | The major version number of the class specification with which this driver is compliant. Details |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | The minor version number of the class specification with which this driver is compliant. Details |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | A string that contains a comma-separated list of the instrument model numbers supported by this driver. Details |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | A string that contains a comma-separated list of class-extension groups that this driver implements. Details |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | Indicates the number of channels that the specific instrument driver supports. For channel based properties, the IVI engine maintains a separate cache value for each channel. Details |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | A string that contains the name of the instrument manufacturer, for example, "National Instruments". Details |
| Inherent IVI Attributes:Instrument Identification:Model | A string that contains the model number of the current instrument. Details |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | A string that contains the firmware revision information for the current instrument. Details |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | A string that contains the logical name you specified when opening the current IVI session. Details |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | Indicates the resource descriptor the driver uses to identify the physical device. If you initialize the driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility. If you initialize the instrument driver with the resource descriptor, this property contains that value. Details |
| Device Specific:IF Digitizer:Fetch Interleaved Data | Specifies whether to interleave I and Q data retrieved from the IF digitizer in a single array or to retrieve two separate arrays, one for I data and another for Q data. Details |
| Device Specific:IF Digitizer:Device Number | Returns the device number of the IF digitizer associated with the current session. Details |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_5voltpower.outputterm.html language=enus -->
## TOPIC 00002: Synchronization:5 Volt Power:Output Terminal Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_5voltpower.outputterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_5voltpower.outputterm.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Synchronization:5 Volt Power:Output Terminal Property

**Short Name:**5VoltPower.OutputTerm

Property of [niScope](cniscope.html)

Specifies the destination for the 5 Volt power signal. Refer to the device specifications document for a list of valid destinations.

|  | Note This property is supported only for NI 5152/5153/5154 devices. |
| --- | --- |

**Defined Values**

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PFI_0

VAL_PFI_1

VAL_PFI_2

VAL_PXI_STAR

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Export Signal |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_absolutesampleclockoffset.html language=enus -->
## TOPIC 00003: Clocking:Advanced:Absolute Sample Clock Offset Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_absolutesampleclockoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_absolutesampleclockoffset.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Clocking:Advanced:Absolute Sample Clock Offset Property

**Short Name:**Absolute Sample Clock Offset

Property of [niScope](cniscope.html)

Gets or sets the absolute time offset, in seconds, of the sample clock relative to the reference clock.

**Valid Values**: [-0.5 *Sample Clock Period*, 0.5 *Sample Clock Period*]

**Default Value**: 0

Use this property when performing manual adjustment to correct for skew and jitter between oscilloscopes synchronized with NI-TClk.

Apply offset with this property to reduce skew and jitter, and write the value you set to apply the manual adjustment across sessions and improve synchronization repeatability.

For details on performing manual adjustment, refer to [Improving NI-TClk Synchronization of Oscilloscopes with Manual Adjustment](/csh?topicname=digitizers/ni-tclk-manual-adjustment-oscilloscopes.html).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_centerfrequency.html language=enus -->
## TOPIC 00004: Onboard Signal Processing:DDC:Center Frequency Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_centerfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_centerfrequency.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Onboard Signal Processing:DDC:Center Frequency Property

**Short Name:**Center Frequency

Property of [niScope](cniscope.html)

The frequency at which the [DDC](/csh?topicname=digitizers/glossary.html) block frequency translates the input data. The default value is 10 MHz.

|  | Note This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a device that does not support OSP. |
| --- | --- |

**Valid Values**

0 - (0.5 × Sample Clock Timebase Rate for digitizer)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_firfilterwindow.html language=enus -->
## TOPIC 00005: Waveform Measurement:Filter:FIR Window Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_firfilterwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_firfilterwindow.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Waveform Measurement:Filter:FIR Window Property

**Short Name:**FIR Filter Window

Property of [niScope](cniscope.html)

Specifies the FIR window type. The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters. The default value is None (0).

| None (0) | No window. |
| --- | --- |
| Hanning (409) | Specifies a Hanning window. |
| Hamming (420) | Specifies a Hamming window. |
| Flat Top (410) | Specifies a Flat Top window. |
| Triangle (423) | Specifies a Triangle window. |
| Blackman (424) | Specifies a Blackman window. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_fpgabitfilepath.html language=enus -->
## TOPIC 00006: Device:FPGA Bitfile Path Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_fpgabitfilepath.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_fpgabitfilepath.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Device:FPGA Bitfile Path Property

**Short Name:**FPGA Bitfile Path

Property of [niScope](cniscope.html)

Gets the absolute file path to the bitfile loaded on the FPGA.

|  | Note Gets the absolute file path to the bitfile loaded on the FPGA. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_fractionalresampleenabled.html language=enus -->
## TOPIC 00007: Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_fractionalresampleenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_fractionalresampleenabled.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled Property

**Short Name:**Fractional Resample Enabled

Property of [niScope](cniscope.html)

Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate. The default value is FALSE.

|  | Note This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a device that does not support OSP. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_frequencytranslationenabled.html language=enus -->
## TOPIC 00008: Onboard Signal Processing:DDC:Frequency Translation Enabled Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_frequencytranslationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_frequencytranslationenabled.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Onboard Signal Processing:DDC:Frequency Translation Enabled Property

**Short Name:**Frequency Translation Enabled

Property of [niScope](cniscope.html)

Enables/disables frequency translating the data around the user-selected center frequency down to baseband. The default value is TRUE.

|  | Note This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a device that does not support OSP. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_frequencytranslationphaseq.html language=enus -->
## TOPIC 00009: Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_frequencytranslationphaseq.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_frequencytranslationphaseq.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q Property

**Short Name:**Frequency Translation Phase Q

Property of [niScope](cniscope.html)

The Q oscillator phase in degrees at the first point acquired. Use this property only when the
 [Data Processing Mode](pniscope_dataprocessingmode.html) property is set to Complex. The default value is 90.

**Valid Values**

-360 to 360

|  | Note This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a device that does not support OSP. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_glitchpolarity.html language=enus -->
## TOPIC 00010: Triggering:Trigger Glitch:Glitch Polarity Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_glitchpolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_glitchpolarity.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Glitch:Glitch Polarity Property

**Short Name:**Glitch Polarity

Property of [niScope](cniscope.html)

Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.

Default Value: Positive

| Positive (1) | The oscilloscope triggers on pulses of positive polarity relative to the trigger threshold. |
| --- | --- |
| Negative (2) | The oscilloscope triggers on pulses of negative polarity relative to the trigger threshold. |
| Either (3) | The oscilloscope triggers on pulses of either positive or negative polarity. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Glitch (Glitch Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_glitchwidth.html language=enus -->
## TOPIC 00011: Triggering:Trigger Glitch:Glitch Width Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_glitchwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_glitchwidth.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Glitch:Glitch Width Property

**Short Name:**Glitch Width

Property of [niScope](cniscope.html)

Specifies the glitch duration, in seconds.

The oscilloscope triggers when it detects a pulse of duration either less than or greater than this value depending on the value of the [Glitch Condition](pniscope_glitchcondition.html) property.

Default Value: 0.0

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Glitch (Glitch Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_hysteresispercent.html language=enus -->
## TOPIC 00012: Waveform Measurement:Hysteresis Percent Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_hysteresispercent.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_hysteresispercent.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Waveform Measurement:Hysteresis Percent Property

**Short Name:**Hysteresis Percent

Property of [niScope](cniscope.html)

Digital hysteresis that is used in several of the scalar waveform measurements. This property specifies the percentage of the full-scale vertical range for the hysteresis window size. The default value is 2%.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_manufacturer.html language=enus -->
## TOPIC 00013: Inherent IVI Attributes:Instrument Identification:Manufacturer Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_manufacturer.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Manufacturer Property

**Short Name:**Manufacturer

Property of [niScope](cniscope.html)

A string that contains the name of the instrument manufacturer, for example, "National Instruments".

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_masterenable.html language=enus -->
## TOPIC 00014: Synchronization:Master Enable Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_masterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_masterenable.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Synchronization:Master Enable Property

**Short Name:**Master Enable

Property of [niScope](cniscope.html)

Specifies whether the device is a master or a slave.

The master device is typically the originator of the trigger signal and clock sync pulse. For a stand-alone device, set this property to FALSE.

**Valid Range**

TRUE—Master

FALSE—Slave

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Clock |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_maximumbandwidth.html language=enus -->
## TOPIC 00015: Fetch:Advanced:Maximum Bandwidth Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_maximumbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_maximumbandwidth.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Fetch:Advanced:Maximum Bandwidth Property

**Short Name:**Maximum Bandwidth

Property of [niScope](cniscope.html)

Specifies the maximum bandwidth that the device is allowed to consume. The NI device limits itself to transfer fewer bytes per second on the PCIe bus than the value you specify for this property.

**Related topics:**

- Bandwidth

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_maximumrealtimesamplerate.html language=enus -->
## TOPIC 00016: Horizontal:Maximum Real Time Sample Rate Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_maximumrealtimesamplerate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_maximumrealtimesamplerate.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Horizontal:Maximum Real Time Sample Rate Property

**Short Name:**Maximum Real Time Sample Rate

Property of [niScope](cniscope.html)

Returns the maximum real-time sample rate in hertz.

**Related topics:**

- Sampling Methods
- Real-Time Sampling

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_onboardmemoryenabled.html language=enus -->
## TOPIC 00017: Peer-to-Peer:Onboard Memory Enabled Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_onboardmemoryenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_onboardmemoryenabled.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Peer-to-Peer:Onboard Memory Enabled Property

**Short Name:**Onboard Memory Enabled

Property of [niScope](cniscope.html)

Specifies whether the digitizer writes data to onboard memory when a peer-to-peer endpoint is enabled.

|  | Note This property can be used only with high-speed digitizers that support peer-to-peer streaming. |
| --- | --- |

|  | Note This property is not supported on NI 5160/5162 digitizers. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggerlevel.html language=enus -->
## TOPIC 00018: Triggering:Trigger Level Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggerlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggerlevel.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Level Property

**Short Name:**Trigger Level

Property of [niScope](cniscope.html)

Specifies the voltage threshold for the trigger. The units are volts.

This property affects instrument behavior only when the [Trigger Type](pniscope_triggertype.html) is set to Edge, Hysteresis, or Window.

The values of the **range** and **offset** parameters in [niScope Configure Vertical](/csh?topicname=scopeviref/niscope_configure_vertical.html) determine the valid range for the trigger level on the channel you use as the **trigger source**. The value you pass for this parameter must meet the following conditions:

*Trigger Level <= Vertical Range/2 + Vertical Offset*

*Trigger Level >= (-Vertical Range/2) + Vertical Offset*

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Edge (Analog Edge Ref Trigger), niScope Configure Trigger Glitch (Glitch Trigger), niScope Configure Trigger Hysteresis (Analog Hysteresis Ref Trigger), niScope Configure Trigger Width (Width Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggermodifier.html language=enus -->
## TOPIC 00019: Triggering:Trigger Modifier Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggermodifier.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggermodifier.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Modifier Property

**Short Name:**Trigger Modifier

Property of [niScope](cniscope.html)

Configures the device to automatically complete an acquisition if a trigger has not been received.

|  | Note When Auto Trigger is selected, you may need to modify the timeout on calls to fetch data to ensure that the acquisition does not time out before the auto trigger time elapses. |
| --- | --- |

| None (1) | Normal triggering. |
| --- | --- |
| Auto Trigger (2) | Software will trigger an acquisition automatically if no trigger arrives after a certain amount of time. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggerslope.html language=enus -->
## TOPIC 00020: Triggering:Trigger Slope Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggerslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggerslope.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Slope Property

**Short Name:**Trigger Slope

Property of [niScope](cniscope.html)

Specifies whether a rising or a falling edge triggers the digitizer.

This property affects instrument operation only when the [Trigger Type](pniscope_triggertype.html) property is set to edge, hysteresis, window, or video.

| Positive (1) | Specifies a rising edge (positive slope). |
| --- | --- |
| Negative (0) | Specifies a falling edge (negative slope). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Digital (Digital Edge Ref Trigger), niScope Configure Trigger Edge (Analog Edge Ref Trigger), niScope Configure Trigger Hysteresis (Analog Hysteresis Ref Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggersource.html language=enus -->
## TOPIC 00021: Triggering:Trigger Source Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggersource.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Source Property

**Short Name:**Trigger Source

Property of [niScope](cniscope.html)

Specifies the source the digitizer monitors for the trigger event. The value must be selected from one of the following valid values.

| 0..n | n is the number of channels on the device |
| --- | --- |
| VAL_EXTERNAL | External TRIG input |
| VAL_IMMEDIATE | Triggers immediately |
| VAL_RTSI_0 | RTSI 0 |
| VAL_RTSI_1 | RTSI 1 |
| VAL_RTSI_2 | RTSI 2 |
| VAL_RTSI_3 | RTSI 3 |
| VAL_RTSI_4 | RTSI 4 |
| VAL_RTSI_5 | RTSI 5 |
| VAL_RTSI_6 | RTSI 6 |
| VAL_PFI_0 | PFI 0 |
| VAL_PFI_1 | PFI 1 |
| VAL_PFI_2 | PFI 2 |
| VAL_PFI_3 | PFI 3 |
| VAL_PFI_4 | PFI 4 |
| VAL_PFI_5 | PFI 5 |
| VAL_PFI_6 | PFI 6 |
| VAL_PFI_7 | PFI 7 |
| VAL_PXI_STAR | PXI Star trigger |
| VAL_SW_TRIG_FUNC | Waits for niScope Send Software Trigger Edge |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Digital (Digital Edge Ref Trigger), niScope Configure Trigger Edge (Analog Edge Ref Trigger), niScope Configure Trigger Glitch (Glitch Trigger), niScope Configure Trigger Hysteresis (Analog Hysteresis Ref Trigger), niScope Configure Trigger Runt (Runt Trigger), niScope Configure Trigger Video (Video Ref Trigger), niScope Configure Trigger Width (Width Trigger), niScope Configure Trigger Window (Analog Window Ref Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggertype.html language=enus -->
## TOPIC 00022: Triggering:Trigger Type Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggertype.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Type Property

**Short Name:**Trigger Type

Property of [niScope](cniscope.html)

Specifies the type of trigger to use.

| Edge (1) | Specifies an edge trigger. |
| --- | --- |
| Width (2) | Specifies a width trigger. |
| Runt (3) | Specifies a runt trigger. |
| Glitch (4) | Specifies a glitch trigger. |
| Video (5) | Specifies a video trigger. |
| Immediate (6) | Specifies an immediate trigger. |
| Hysteresis (1001) | Specifies a hysteresis trigger. |
| Digital (1002) | Specifies a digital trigger. |
| Window (1003) | Specifies a window trigger. |
| Software (1004) | Specifies a software trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggerwindowhighlevel.html language=enus -->
## TOPIC 00023: Triggering:Trigger Window:High Level Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggerwindowhighlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggerwindowhighlevel.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Window:High Level Property

**Short Name:**Trigger Window High Level

Property of [niScope](cniscope.html)

Pass the upper voltage threshold you want the digitizer to use for window triggering.

The digitizer triggers when the trigger signal enters or leaves the window you specify with the Trigger Window Low Level property and this property.

The values of the [Vertical Range](pniscope_verticalrange.html) property and the
 [Vertical Offset](pniscope_verticaloffset.html) property determine the valid range for the Trigger Window Low Level property on the channel you specify with the [Trigger Source](pniscope_triggersource.html) property.

The value you pass for this parameter must meet the following conditions:

*High Trigger Level <= Vertical Range/2 + Vertical Offset*

*High Trigger Level >= (-Vertical Range/2) + Vertical Offset*

*High Trigger Level > Low Trigger Level*

**Related topics:**

- Window Triggers

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Window (Analog Window Ref Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggerwindowlowlevel.html language=enus -->
## TOPIC 00024: Triggering:Trigger Window:Low Level Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggerwindowlowlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggerwindowlowlevel.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Window:Low Level Property

**Short Name:**Trigger Window Low Level

Property of [niScope](cniscope.html)

Pass the lower voltage threshold you want the digitizer to use for window triggering.

The digitizer triggers when the trigger signal enters or leaves the window you specify with this property and the
 [Trigger Window High Level](pniscope_triggerwindowhighlevel.html) property.

The values of the [Vertical Range](pniscope_verticalrange.html) property and the [Vertical Offset](pniscope_verticaloffset.html) property determine the valid range for this property on the channel you specify with the
 [Trigger Source](pniscope_triggersource.html) property.

The value you pass for this parameter must meet the following conditions:

*Low Trigger Level <= Vertical Range/2 + Vertical Offset*

*Low Trigger Level >= (-Vertical Range/2) + Vertical Offset*

*Low Trigger Level < High Trigger Level*

**Related topics:**

- Window Triggers

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Window (Analog Window Ref Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_triggerwindowmode.html language=enus -->
## TOPIC 00025: Triggering:Trigger Window:Window Mode Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_triggerwindowmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_triggerwindowmode.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Triggering:Trigger Window:Window Mode Property

**Short Name:**Trigger Window Mode

Property of [niScope](cniscope.html)

Specifies whether to trigger when the signal enters or leaves the window specified by the
 [Trigger Window Low Level](pniscope_triggerwindowlowlevel.html) property or the [Trigger Window High Level](pniscope_triggerwindowhighlevel.html) property.

**Related topics:**

- Window Triggers
- Trigger Parameters

| Entering (0) | Trigger occurs when a signal enters a window. |
| --- | --- |
| Leaving (1) | Trigger occurs when a signal leaves a window. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Window (Analog Window Ref Trigger) |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_verticalcoupling.html language=enus -->
## TOPIC 00026: Vertical:Vertical Coupling Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_verticalcoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_verticalcoupling.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Vertical:Vertical Coupling Property

**Short Name:**Vertical Coupling

Property of [niScope](cniscope.html)

Specifies how the digitizer couples the input signal for the channel. When you change input coupling, the input stage takes a finite amount of time to settle.

**Related topics:**

- Input Coupling

| AC (0) | AC coupled |
| --- | --- |
| DC (1) | DC coupled |
| Ground (2) | Ground coupled |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Vertical |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-scope-properties path=scopepropref/pniscope_verticalrange.html language=enus -->
## TOPIC 00027: Vertical:Vertical Range Property

- bundle_id: `ni-scope-properties`
- source_path: `scopepropref/pniscope_verticalrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-properties/raw/resource/enus/scopepropref/pniscope_verticalrange.html
- document_id: `ni-scope-properties`
- page_type: `leaf`
- content_type: ``

### Vertical:Vertical Range Property

**Short Name:**Vertical Range

Property of [niScope](cniscope.html)

Specifies the absolute value of the input range for a channel. The units are volts. For example, to acquire a sine wave that spans between -5 and +5 V, set this property to 10.0 V.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Vertical |
| Channel-based | Yes |
| Resettable | Yes |
