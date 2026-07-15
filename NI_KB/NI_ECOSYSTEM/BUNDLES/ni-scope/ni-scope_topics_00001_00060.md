# NI DOCUMENT BUNDLE: ni-scope

<!--NI_BUNDLE_CHUNK bundle=ni-scope start=1 end=60 -->
<!--NI_TOPIC bundle=ni-scope path=accessing-the-ni-scope-soft-front-panel.html language=enus -->
## TOPIC 00001: Accessing the NI-SCOPE Soft Front Panel

- bundle_id: `ni-scope`
- source_path: `accessing-the-ni-scope-soft-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/accessing-the-ni-scope-soft-front-panel.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can access the SFP two ways: Launch the SFP by selecting Start»All Programs»National Instruments»NI-SCOPE»SCOPE Soft Front Panel or from NI Launcher in Windows 8. Navigate to <IVIROOTDIR32>\Drivers\niScope\NI-SCOPE Soft Front Panel.exe. <IVIROOTDIR32> is an alias to a specific National Instrumen

### Accessing the NI-SCOPE Soft Front Panel

You can access the SFP two ways:

- Launch the SFP by selecting Start»All Programs»National Instruments»NI-SCOPE»SCOPE Soft Front Panel or from NI Launcher in Windows 8.
- Navigate to <IVIROOTDIR32>\Drivers\niScope\NI-SCOPE Soft Front Panel.exe . <IVIROOTDIR32> is an alias to a specific National Instruments file folder location. Refer to the NI-SCOPE Readme for more information about installed file locations.

Parent topic:

NI-SCOPE 32-Bit Soft Front Panel Help

<!--NI_TOPIC bundle=ni-scope path=accuracy.html language=enus -->
## TOPIC 00002: Accuracy

- bundle_id: `ni-scope`
- source_path: `accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/accuracy.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Accuracy is a measure of the ability of a device to indicate the true value of a measured signal. Accuracy is usually expressed as a percentage of the specified value, for example, 5 V ±1%. Signal Characteristics Knowing the characteristics of the signal under consideration helps you to choose the c

### Accuracy

Accuracy is a measure of the ability of a device to
 indicate the true value of a measured signal. Accuracy is usually expressed as 
 a percentage of the specified value, for example, 
 5 V ±1%.

#### Signal Characteristics

Knowing the characteristics of the signal under consideration helps you to choose the correct 
settings to maximize measurement accuracy. Such characteristics include:

- Peak-to-peak value —This parameter, in units of volts, reflects the maximum change in signal voltage. If V is the 
signal voltage at any given time, then V pk-pk = V max – V min . The peak-to-peak value 
affects the vertical sensitivity or gain of the input amplifier. If you do not know the peak-to-peak value, 
start with the largest input range, and decrease it until the waveform is digitized using the maximum 
dynamic range without clipping the signal. Refer to the specifications for 
your digitizer for the maximum input range. The following figure shows how different ranges affect the 
resolution of a 600 mV pk-pk signal.
 
 
 [IMAGE alt='image' src='GUID-87777A61-A691-481A-AC11-7BB4672FE5BD-a5.svg'] 
 [IMAGE alt='image' src='GUID-B9112FE9-85D9-493A-8937-8F9C0F695710-a5.svg'] 
 [IMAGE alt='image' src='GUID-640EA4D1-09E4-41BD-B0B3-9905D8C5D336-a5.svg']
- Source impedance—Most digitizers have a 1 MΩ input 
resistance in the passband. If the source impedance is large, the signal is attenuated at the amplifier input 
and the measurement is inaccurate. If the source impedance is unknown but suspected to be high, change the 
attenuation ratio on your probe and acquire data. In addition to the input resistance, all digitizers and probes present some input capacitance in parallel with the resistance. This capacitance can interfere with 
your measurement in much the same way as the resistance does.
- Input frequency —If your sample rate is less than twice the highest frequency component at the input, 
the frequency components above half your sample rate will alias in the passband at lower frequencies, 
indistinguishable from other frequencies in the passband. If the highest frequency of the signal is unknown, 
you should start with the digitizer maximum sample rate to prevent aliasing and reduce the digitizer 
sample rate until the display shows either enough cycles of the waveform or the information you need. Refer to the Nyquist Theorem for more information.
- General signal shape —Some signals are easy to capture by ordinary triggering methods. A few iterations 
on the trigger level may finally render a steady display. This method works for sinusoidal, triangular, square, 
and saw tooth waves. Some of the more elusive waveforms, such as irregular pulse trains, runt pulses, and 
transients, may be more difficult to capture. The following figure shows an example of a difficult 
pulse-train trigger. 
 [IMAGE alt='image' src='GUID-B0C786EC-39DC-4991-91CC-EC98A4228AC0-a5.svg'] 
Ideally, the trigger event should occur at condition one, but sometimes the instrument may trigger on 
condition two because the signal crosses the trigger level. You can solve this problem without using 
complicated signal processing techniques by using trigger holdoff, which lets you specify a time from the 
trigger event to ignore additional triggers that fall within that time. With an appropriate holdoff value, 
the waveform shown in the previous figure can be properly captured by discarding conditions two and four.
- Input coupling —On many digitizers, you can configure the input channels to be DC-coupled or AC-coupled. 
DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. 
In contrast, AC coupling removes DC offsets and attenuates low-frequency components of a signal. This feature 
can be exploited to zoom in on AC signals with large DC offsets, such as switching noise on a 12 V power 
supply. Refer to the specifications for your digitizer for input limits 
that you must observe regardless of coupling.

Parent topic:

Fundamentals

Related concepts:

- Resolution
- Impedance and Impedance Matching
- Aliasing
- Nyquist Theorem
- Trigger Holdoff

<!--NI_TOPIC bundle=ni-scope path=acquiring-data-continuously.html language=enus -->
## TOPIC 00003: Acquiring Data Continuously

- bundle_id: `ni-scope`
- source_path: `acquiring-data-continuously.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/acquiring-data-continuously.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Continuous acquisition is the ability to transfer data from the digitizer to the host computer memory while the digitizer is still acquiring data, which can be useful for the following applications:Acquiring records larger than available memory Fetching triggered records while other records are bein

### Acquiring Data Continuously

Continuous acquisition is the ability to transfer data from the digitizer to the host 
computer memory while the digitizer is still acquiring data, which can be useful for the following applications:

- Acquiring records larger than available memory
- Fetching triggered records 
 while other records are being acquired
- Acquiring more records than fit in digitizer memory
- Fetching the most recent data
- Acquiring waveforms at hardware-timed intervals

#### How Continuous Acquisition Works

NI digitizers contain a large amount of onboard memory, generally 8, 16, 32, or 256 MB per channel. This memory is 
divided into individual records when acquiring data. For example, if you are acquiring two records, 
8 MB of memory is divided into two 4 MB records. Each record is treated as a circular buffer.
When the digitizer starts acquiring data, the samples are placed in the beginning of the buffer. 
The digitizer acquires the requested number of pretrigger samples—that is, the actual record length times 
the reference position divided by 100. After the pretrigger samples are complete, the digitizer waits for 
a trigger. While waiting, the digitizer continues to acquire and store data. This data is placed in the 
circular buffer, so after the buffer is filled, the digitizer starts overwriting data at the beginning. If 
a trigger never occurs, the digitizer waits for a trigger forever. After the trigger occurs, the digitizer 
samples the requested number of posttrigger samples, and the record is complete. If another record is 
requested, the digitizer restarts the acquisition, moving to the next record in memory.

Continuous acquisition refers to the digitizer's ability to fetch data from its own circular buffer 
to the host computer's memory while it is acquiring data. When you call 
 Initiate Acquisition, the digitizer starts acquiring data into its circular buffer, as shown in the following figure.

[IMAGE alt='image' src='GUID-7BD28656-54D6-460A-AE00-BCC24DC688D5-a5.svg']

You can 
then use a Fetch function to send the first chunk of data to the host computer while 
the digitizer continues 
to acquire more samples, as shown in the following figure.

[IMAGE alt='image' src='GUID-6E6BA406-2DFD-49AF-88B5-4222795B7D77-a5.svg']

When the circular buffer is filled on the digitizer, it starts to 
overwrite the data at the beginning of the buffer, as shown in the following figure.

[IMAGE alt='image' src='GUID-A29CEE4A-FCA6-42FC-834C-AC3AFF691E6A-a5.svg']

Ideally, you have already copied and saved 
the data that is being overwritten in the host computer.

[IMAGE alt='image' src='GUID-76D4EA72-4A69-4F92-8FD9-967F684F31D8-a5.svg']

If you do not send a trigger, the digitizer continues to acquire data forever or until you call 
 Abort, 
 Reset, or Close.

#### Fetching Continuous Acquisition Data

No special configuration is necessary for continuous acquisition programs. The only 
difference is how the data is fetched. The Fetch functions all work for continuous acquisition, but 
additional attributes are available to specify what data to fetch. In particular, the 
Fetch Relative To attribute supports values of Read Pointer, Now, and Start in addition to 
the standard Trigger and Pretrigger values. These values allow specifying different locations within
 the record 
from which to start fetching. When fetching data continuously, the possibility always exists that 
the data has been overwritten in the onboard memory before you attempt to fetch it. NI-SCOPE returns
 an error in this situation.

When fetching data continuously, the relative initial x value returned in the waveform info structure 
is not valid until the trigger occurs. Often, the trigger never occurs during continuous acquisitions. 
However, the waveform info structure also contains an absolute initial x value, which is a free-running 
timestamp counter on the digitizer. 
Additional status information about your acquisition is available by using the Fetch 
Points Done and Fetch Records Done attributes. The points done is the
 number of samples available in the record specified by the Fetch Record Number
 attribute, starting at the Fetch Offset attribute that is relative to the 
 Fetch Relative To attribute. NI-SCOPE also supports a 
 Fetch Backlog attribute, which is the 
 number of samples that have not been fetched when performing a continuous acquisition.

Parent topic:

Getting Started with NI-SCOPE

Related concepts:

- Acquiring Records Larger than Available Memory
- Fetching Triggered Records while Other Records Are Being Acquired
- Acquiring More Records Than Fit in Digitizer Memory
- Fetching the Most Recent Data
- Acquiring Waveforms at Hardware-Timed Intervals
- Time Stamping

<!--NI_TOPIC bundle=ni-scope path=acquiring-data-with-ni-high-speed-digitizers.html language=enus -->
## TOPIC 00004: Acquiring Data with NI High-Speed Digitizers

- bundle_id: `ni-scope`
- source_path: `acquiring-data-with-ni-high-speed-digitizers.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/acquiring-data-with-ni-high-speed-digitizers.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can acquire data with an NI high-speed digitizer either programmatically or interactively. Programmatically Acquiring Data If you want to integrate a digitizer into your test and measurement application, you can program the device using National Instruments LabVIEW or LabWindows/CVI, Microsoft V

### Acquiring Data with NI High-Speed Digitizers

You can acquire data with an NI high-speed digitizer either programmatically or interactively.

#### Programmatically Acquiring Data

If you want to integrate a digitizer into your test and measurement application, you can program the device using 
National Instruments LabVIEW or LabWindows/CVI, Microsoft Visual C++/C#, Microsoft Visual Basic, and Microsoft Visual Basic .NET.

The following figure illustrates the relationship between your programming environment, NI‑DAQmx, and the digitizer.

[IMAGE alt='image' src='GUID-9283C8B7-84AF-4F86-864A-C47E096EEAC0-a5.svg']

#### Interactively Acquiring Data

If you are using the digitizer as a general-purpose digitizer, you can use the 
NI-SCOPE Soft Front Panel (SFP) to make measurements interactively without writing code.
To launch the NI-SCOPE SFP, select Start»All Programs»National Instruments»NI-SCOPE»NI-SCOPE Soft Front Panel. For more information,
refer to the NI-SCOPE Soft Front Panel Help.

Parent topic:

Getting Started with NI-SCOPE

Related concepts:

- NI-SCOPE Soft Front Panel and InstrumentStudio

<!--NI_TOPIC bundle=ni-scope path=acquiring-records-larger-than-available-memor.html language=enus -->
## TOPIC 00005: Acquiring Records Larger than Available Memory

- bundle_id: `ni-scope`
- source_path: `acquiring-records-larger-than-available-memor.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/acquiring-records-larger-than-available-memor.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: The standard use of continuous acquisition is to fetch a record that is larger than the available memory on the digitizer. Because the data is fetched as it is acquired, the digitizer memory can be overwritten. At slow sampling rates, you can fetch data forever by setting up an acquisition that is n

### Acquiring Records Larger than Available Memory

The standard use of continuous acquisition is to fetch a record that is larger than the 
available memory on the digitizer. Because the data is fetched as it is acquired, the digitizer memory can be 
overwritten. At slow sampling rates, you can fetch data forever by setting up an acquisition that is never 
triggered and is repeatedly fetching. At faster sampling rates, the host computer may not be able to fetch as 
fast as the digitizer samples data. If the data that is being fetched is overwritten, NI-SCOPE returns an 
error message from the Fetch function. Look at the Fetch in Chunks
 example to see how a waveform can be reconstructed with the data from multiple fetch calls. 
 Look at the Fetch Forever example to benchmark how much data you can acquire at a 
 given sampling rate before the data is overwritten.

To fetch a record that is larger than memory, set the Fetch Relative To attribute to Read Pointer. This positions the beginning of the fetch operation at the start of the 
record when you initiate a new acquisition. After every fetch, the read pointer is incremented to be the sample 
after the last sample retrieved. Therefore, you can repeatedly fetch relative to the read pointer, with a retrieval 
offset of zero, to acquire a single, infinite record.

If you specify a positive timeout with a Fetch function, it waits for the 
requested number of samples. Alternatively, specifying a timeout of zero acquires the number of samples 
currently available (up to a maximum of the numSamples parameter). The waveform info 
 structure returns the actual number of samples fetched. Using a timeout of zero achieves slightly better 
 performance because the status of the digitizer is queried less often.

A separate read pointer is stored for each channel, so you can alternate fetching different channels. 
The read pointer is also reset to zero when you fetch from a different record.

Parent topic:

Acquiring Data Continuously

<!--NI_TOPIC bundle=ni-scope path=acquiring-the-data.html language=enus -->
## TOPIC 00006: Acquiring the Data

- bundle_id: `ni-scope`
- source_path: `acquiring-the-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/acquiring-the-data.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SCOPE has two kinds of functions that acquire data—Read and Fetch functions. For simplicity, this example uses a Read function. LabVIEW Example—Acquiring the Data The channels input parameter specifies the channel or channels that NI-SCOPE acquires data from. C Example—Acquiring the Data This exa

### Acquiring the Data

NI-SCOPE has two kinds of functions that acquire data—Read and Fetch functions. 
For simplicity, 
this example uses a Read function.

#### LabVIEW Example—Acquiring the Data

[IMAGE alt='image' src='GUID-B8E09C02-E170-4601-8650-1A1824B41834-a5.gif']

The channels input parameter specifies the channel or channels that NI-SCOPE acquires data from.

#### C Example—Acquiring the Data

This example includes additional functions and parameters not needed in LabVIEW. You need to call 
 niScope_ActualRecordLength to get the actual record length that NI-SCOPE uses 
so you can create enough space for the waveform array. You can then initiate the acquisition and fetch the 
data with niScope_Read. After fetching the data, you need to pass a pointer 
to extract and plot the acquired data. The method you use to do this varies depending on your ADE.

// Get the actual number of samples to be acquired
niScope_ActualRecordLength (vi, &actualRecordLength);

// Get the number of waveforms available for the 
// given channelList
niScope_ActualNumWfms (vi,channelList, &numWfm);

// Allocate space for the waveform information
wfmInfoPtr = malloc (sizeof (struct niScope_wfmInfo) *
numWfm);

// Allocate space for the waveform array
wfmPtr = malloc (sizeof (ViReal64) * actualRecordLength
* numWfm);

// Check if allocations succeeded 
if (!wfmPtr|| !wfmInfoPtr)

return NISCOPE_ERROR_INSUFFICIENT_MEMORY;

// Read the data (Initiates an acquisition and fetches
// the data)
niScope_Read (vi, channelList, timeout,
actualRecordLength, wfmPtr, wfmInfoPtr);

#### About the Parameters

The channelList parameter specifies the channel or channels that NI-SCOPE acquires data from. 
The wfmInfoPtr parameter returns the values needed to display a waveform: relative 
initial x is the time of the first point in the waveform with respect to the trigger 
and is expressed in seconds; absolute initial x is the absolute timestamp of the first point in the waveform; and x increment is the length of time between points in the waveform in seconds.
The wfmPtr parameter is a buffer into which NI-SCOPE stores the waveform it reads. 
The units for the individual array elements are volts.

Parent topic:

NI-SCOPE Tutorial

<!--NI_TOPIC bundle=ni-scope path=acquiring-waveforms-at-hardware-timed-interva.html language=enus -->
## TOPIC 00007: Acquiring Waveforms at Hardware-Timed Intervals

- bundle_id: `ni-scope`
- source_path: `acquiring-waveforms-at-hardware-timed-interva.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/acquiring-waveforms-at-hardware-timed-interva.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Setting the Fetch Relative To attribute to Start sets the starting fetch position to be the first sample acquired by the digitizer. If the trigger happens immediately, the first point sampled by the digitizer would equal the first pretrigger point. However, this is generally not true because the dig

### Acquiring Waveforms at Hardware-Timed Intervals

Setting the Fetch Relative To attribute to Start
sets the starting fetch position to be the first sample acquired by the digitizer. If the trigger 
happens immediately, the first point sampled by the digitizer would equal the first pretrigger point. 
However, this is generally not true because the digitizer usually has to wait for a trigger. 
While the digitizer waits, it continues to sample data, possibly forever. As it samples data into the 
circular, onboard memory, the original data is eventually overwritten. As in other cases, if you attempt 
to fetch data that is overwritten, NI-SCOPE returns an error.
A typical use of fetching relative to start is to acquire nontriggered waveforms at precise intervals. 
You can use the digitizer sample clock to precisely time the duration between waveforms. Suppose you 
want 500 points every millisecond, while sampling at 100 MS/s. You can set the Fetch Relative To 
 attribute to start at the beginning of your program. Then, for every iteration of a loop, call a 
 Fetch function to retrieve 500 samples, and increment the Fetch Offset
 attribute by 100,000 samples. Because 100,000 samples are acquired every millisecond when sampling 
 at 100 MS/s, this program is effectively using the sample clock to 
precisely time the interval between acquired waveforms.

Parent topic:

Acquiring Data Continuously

<!--NI_TOPIC bundle=ni-scope path=bessel-iir-filter.html language=enus -->
## TOPIC 00008: Bessel IIR Filter

- bundle_id: `ni-scope`
- source_path: `bessel-iir-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/bessel-iir-filter.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_BESSEL_FILTER The input waveform is filtered with a Bessel IIR algorithm. The type of the filter is specified by Measurement Filter Type as any of the following values: lowpass highpass bandpass bandstop The order of the filter is specified by the Filter IIR Order prope

### Bessel IIR Filter

C/C++ Equivalent: 
NISCOPE_VAL_BESSEL_FILTER

The input waveform is filtered with a Bessel IIR algorithm. The type of the filter is 
specified by Measurement Filter Type as any of the following 
values:

- lowpass
- highpass
- bandpass
- bandstop

The order of the filter is specified by the Filter IIR Order property or the NISCOPE_ATTR_MEAS_FILTER_ORDER attribute. 
Also, a number of points equal to the Percent Waveform Transient property or the 
NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT attribute 
divided by 100 times the input size are eliminated from the beginning of the filtered waveform
 so that the transient response of the filter does not affect further measurements.

#### Units

Volts

#### X Units

Seconds (nearly linear time delay)

#### Resulting Array Size

inputSize × (1 – Percent Waveform Transient property / 100)

or

inputSize × (1 – NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT attribute / 100)

Parent topic:

Array Measurements in NI-SCOPE

Related concepts:

- Bessel Filters

<!--NI_TOPIC bundle=ni-scope path=burst-triggers.html language=enus -->
## TOPIC 00009: Burst Triggers

- bundle_id: `ni-scope`
- source_path: `burst-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/burst-triggers.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Burst triggering is available only on high-speed digitizers that support onboard signal processing (OSP).To trigger on data bursts, you can configure the digitizer to wait until it detects a quiet period before arming the trigger. Use the Min Quiet Time property or the NISCOPE_ATTR_REF_TRIGGER_MIN

### Burst Triggers

Note

To trigger on data bursts, you can configure the digitizer to wait until it detects a quiet period before arming
 the trigger. Use the Min Quiet Time property or the NISCOPE_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME attribute to set the length of this quiet period.

The following figure shows how burst triggers occur after a configured minimum quiet time of 1.5 seconds.
 The trigger occurs at point A because the minimum quiet time of 1.5 seconds has been exceeded—in this case, 2 seconds have elapsed since a signal above the trigger level was detected. A trigger does not
 occur at point B because only 1 second of quiet time has elapsed.

[IMAGE alt='image' src='GUID-E26F6985-1D8D-4E46-9EEF-3EED6F98F56B-a5.gif']

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-scope path=chebyshev-filters.html language=enus -->
## TOPIC 00010: Chebyshev Filters

- bundle_id: `ni-scope`
- source_path: `chebyshev-filters.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/chebyshev-filters.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SCOPE supports the following attributes for configuring Chebyshev filters:Measurement Filter Type—lowpass, highpass, bandpass, bandstop Measurement Filter Order Measurement Passband Filter Ripple in dB Measurement Transient Waveform Percent These attributes minimize peak error in the passband by

### Chebyshev Filters

NI-SCOPE supports the following attributes for configuring Chebyshev filters:

- Measurement Filter Type—lowpass, highpass, bandpass, bandstop
- Measurement Filter Order
- Measurement Passband Filter Ripple in dB
- Measurement Transient Waveform Percent

These attributes minimize peak error in the passband by setting the maximum allowable absolute value of the difference between the ideal filter and the filter response you want (the maximum tolerable
error in the passband). Chebyshev filters have an equiripple magnitude response in the passband, 
monotonically decreasing magnitude response in the stopband, and a sharper rolloff than Butterworth 
filters. The cutoff frequency for Chebyshev filters is defined as the end of the passband. For 
example, if you specify a lowpass filter with 1 dB ripple, the passband response from 0 Hz to the 
cutoff frequency will have 1 dB ripple. At the cutoff frequency, the response will be 1 dB down, 
and it is monotonically decreasing above the cutoff frequency.

The following figure shows the response of a lowpass Chebyshev filter. Notice that the 
equiripple response in the passband is constrained by the maximum tolerable ripple error and that 
the sharp rolloff appears in the stopband. The advantage of Chebyshev filters over Butterworth 
filters is that Chebyshev filters have a sharper transition between the passband and the stopband 
with a lower order filter, which produces smaller absolute errors and higher execution speeds.

[IMAGE alt='image' src='GUID-3458827E-D7D6-4A57-AA90-A324AF7AEA9F-a5.gif']

Impulse Magnitude and Phase Response Versus Frequency for a Lowpass Chebyshev Filter

Parent topic:

Types of IIR Filters in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=chebyshev-iir-filter.html language=enus -->
## TOPIC 00011: Chebyshev IIR Filter

- bundle_id: `ni-scope`
- source_path: `chebyshev-iir-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/chebyshev-iir-filter.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_CHEBYSHEV_FILTER The input waveform is filtered with a Chebyshev IIR algorithm. The type of the filter is specified by the Filter Type property or the NISCOPE_ATTR_MEAS_FILTER_TYPE attribute as any of the following values: lowpass highpass bandpass bandstop The Chebyshe

### Chebyshev IIR Filter

C/C++ Equivalent: 
NISCOPE_VAL_CHEBYSHEV_FILTER

The input waveform is filtered with a Chebyshev IIR algorithm. The type of the 
filter is specified by the 
Filter Type property or the 
NISCOPE_ATTR_MEAS_FILTER_TYPE attribute as any of the following values:

- lowpass
- highpass
- bandpass
- bandstop

The Chebyshev filter allows you to specify the passband ripple, the Filter Ripple or the 
NISCOPE_ATTR_MEAS_FILTER_RIPPLE,
 in 
decibels. The order of the filter is specified by the Filter Order property or the 
NISCOPE_ATTR_MEAS_FILTER_ORDER attribute. 
Also, a number of points equal to the Percent Waveform Transient property or the NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT attribute divided by 100 times the input size are eliminated from the beginning of the filtered waveform, so the transient response of the filter does not affect further measurements.

#### Units

Volts

#### X Units

Seconds (nonlinear time delay)

#### Resulting Array Size

inputSize × (1 – Percent Waveform Transient property / 100)

or

inputSize × (1 – NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT attribute / 100)

Parent topic:

Array Measurements in NI-SCOPE

Related concepts:

- Chebyshev Filters

<!--NI_TOPIC bundle=ni-scope path=closing-the-session.html language=enus -->
## TOPIC 00012: Closing the Session

- bundle_id: `ni-scope`
- source_path: `closing-the-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/closing-the-session.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: The closing step closes the session and deallocates any resources the session used. Closing the session is important because it releases any temporary buffers that were created to transfer data between the digitizer and the host memory. LabVIEW Example-Closing the Session C Example—Closing the Sessi

### Closing the Session

The closing step closes the session and deallocates any resources the session used. Closing the session is 
important because it releases any temporary buffers that were created to transfer data 
between the digitizer and the host memory.

#### LabVIEW Example-Closing the Session

[IMAGE alt='image' src='GUID-F5DA51D8-600E-4DDD-94F5-9C69807FB409-a5.gif']

#### C Example—Closing the Session

// Close the session
if(vi)
   niScope_close(vi);

Parent topic:

NI-SCOPE Tutorial

<!--NI_TOPIC bundle=ni-scope path=coercions-of-horizontal-parameters.html language=enus -->
## TOPIC 00013: Coercions of Horizontal Parameters

- bundle_id: `ni-scope`
- source_path: `coercions-of-horizontal-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/coercions-of-horizontal-parameters.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: The horizontal timing parameters are all inter-related to comply with the IVI-Scope specification. These parameters all appear in the Configure Horizontal Timing function. The fundamental theory is that your time per record is a constant number during an acquisition. This is accomplished with the fo

### Coercions of Horizontal Parameters

The horizontal timing parameters are all inter-related to comply with the IVI-Scope 
specification. These parameters all appear in the Configure Horizontal Timing
 function. The fundamental theory is that your time per record is a constant number during an acquisition. 
 This is accomplished with the following parameter coercions:

#### Min Sample Rate

The min sample rate parameter is coerced up to the next available sample rate that the 
digitizer supports. The available sample rates change based on the acquisition type (such as normal and 
Flex Res). The actual sampling rate may be retrieved with the Sample Rate function.
 This information is also returned by the Fetch function, with the
 x increment parameter, which is one divided by the actual sampling rate. If the sample 
 rate parameter is set higher than the maximum, NI-SCOPE returns an error.

#### Enforce Realtime

If the enforce realtime parameter is set to FALSE, the digitizer
 enters RIS mode when the sampling rate exceeds the maximum real-time sampling rate of the device. In RIS mode, 
 the sampling rate is coerced up to a multiple of the maximum real-time sampling rate.

#### Min Record Length

The min record length is coerced so that the time per record is constant. The formula is the 
following:

actual rec length = min rec length/min sample rate x actual sample rate

You can find the actual record length by calling the Actual Record Length
 function. You can retrieve this value any time after you call Configure Horizontal Timing.
 Keep in mind that the amount of memory required on the digitizer is generally higher than the actual record 
 length.

#### Reference Position

The reference position is rounded to the nearest sample. You can use
 the relative initial x parameter from a Fetch function to determine the
 actual reference position. If you fetch relative to the pretrigger, and the offset is zero, the
 initial x value is the first pretrigger point to the trigger. Therefore,
 the actual reference position is the following:

The following C code shows how NI-SCOPE accomplishes timing coercions:

```text
// Convert minimum sample rate into its corresponding 
// time-per-record value
timePerRecord = minRecordLength / minSampleRate;
if (minSampleRate <= maxRealTimeSampleRate) 
{
   // For real-time, normal acquisitions, sample rate
   // is an integer divisor of max sample rate
   int divisor = (int) floor (maxRealTimeSampleRate / minSampleRate);
   actualSampleRate = maxRealTimeSampleRate / divisor;
}
else 
{
   //In RIS, sample rate is a multiple of max sample rate
   int overSamplingFactor = (int) ceil (minSampleRate / maxRealTimeSampleRate);
   actualSampleRate = overSamplingFactor × maxRealTimeSampleRate;
}
actualRecordLength = (int) ((timePerRecord × actualSampleRate) + 0.5);
```

Parent topic:

Coercions

<!--NI_TOPIC bundle=ni-scope path=coercions.html language=enus -->
## TOPIC 00014: Coercions

- bundle_id: `ni-scope`
- source_path: `coercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/coercions.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SCOPE allows you to configure the digitizer programmatically. However, the hardware may not support the exact value for some parameters that you specify. Instead of returning an error and forcing your program to be highly device specific, NI-SCOPE may coerce (or round) some input parameters to th

### Coercions

NI-SCOPE allows you to configure the digitizer programmatically. 
However, the hardware may not support the exact value for some parameters that you 
specify. Instead of returning an error and forcing your program to be highly 
device specific, NI-SCOPE may coerce (or round) some input parameters to the next higher 
or lower value that the digitizer supports. Some of these coercions may result in 
incorrect behavior. In most cases, you can query the exact value of the parameter from NI-SCOPE.

Common coercions of NI-SCOPE parameters and attributes include vertical, 
horizontal, and 
trigger parameters.

Parent topic:

Getting Started with NI-SCOPE

Related concepts:

- Coercions of Vertical Parameters
- Coercions of Horizontal Parameters
- Coercions of Trigger Parameters

<!--NI_TOPIC bundle=ni-scope path=complete-ntsc-frame-scan.html language=enus -->
## TOPIC 00015: Complete NTSC Frame Scan

- bundle_id: `ni-scope`
- source_path: `complete-ntsc-frame-scan.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/complete-ntsc-frame-scan.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the result of scanning all 525 lines that compose a complete NTSC frame.

### Complete NTSC Frame Scan

The following figure shows the result of scanning all 525 lines that compose a complete NTSC frame.

[IMAGE alt='image' src='GUID-6D457C6D-9DEE-463C-8C1E-17AF5C226D1E-a5.gif']

Parent topic:

Interlaced Scanning

<!--NI_TOPIC bundle=ni-scope path=composite-and-component-video-signals.html language=enus -->
## TOPIC 00016: Composite and Component Video Signals

- bundle_id: `ni-scope`
- source_path: `composite-and-component-video-signals.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/composite-and-component-video-signals.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Composite Video Signals A composite video signal is a signal in which all the components needed to generate a video signal are embedded in a single signal. The three main components that together form a composite signal are as follows: The luma signal (or luminance)—Contains the intensity (brightnes

### Composite and Component Video Signals

#### Composite Video Signals

A composite video signal is a signal in which all the components needed to generate a video signal are embedded in a single signal. The three main components that together form a composite signal are as follows:

- The luma signal (or luminance) —Contains the intensity (brightness or darkness) information of the video image
- The chroma signal —Contains the color information of the video image
- The synchronization signal —Controls the scanning of the signal on a display such as the TV screen

The monochrome composite signal is built of two components: luma (or luminance) and synchronization. This signal, which is usually called the Y signal, is shown in the following figure.

[IMAGE alt='image' src='GUID-C9DCA584-C402-4DD6-9309-BBCC3AB8E2DE-a5.svg']

#### Monochrome Composite Video Signal (Luma Steps from White to Black)

The chroma signal by itself, which is usually called the C signal, is shown in the following figure.

[IMAGE alt='image' src='GUID-1819F37E-87AB-48AC-A627-94FD073B5670-a5.svg']

#### Color Information Signal for a Color Bar Line (Including the Color Burst)

The composite color video signal, often called the Color Video, Blank, and Sync (CVBS) signal, is the sum of Y and C.

CVBS = Y + C

[IMAGE alt='image' src='GUID-D519A37F-38FC-44E1-A68D-1758A09A1564-a5.svg']

#### Color Composite Video Signal for a Color Bar Line

The two components Y and C can also be distributed separately as two independent signals. These two signals together are called either Y/C or S-video.

Y/C = S-video

#### Component Video Signals

A component video signal is a signal in which all the color components needed to generate a video signal are 
transmitted separately. Most HDTV formats are component (Y-Pb-Pr).

Parent topic:

Video Fundamentals

<!--NI_TOPIC bundle=ni-scope path=configuration-functions.html language=enus -->
## TOPIC 00017: Configuration Functions

- bundle_id: `ni-scope`
- source_path: `configuration-functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/configuration-functions.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configuration functions to set up your acquisition.Using these functions, you can set triggers, input impedance, DC offset, vertical range, sampling rate, and much more. Additionally, NI‑SCOPE can automatically configure your device settings with the Auto Setup function. Once configured, you

### Configuration Functions

Use the Configuration functions to set up your acquisition.

Using these functions, you can set triggers, input impedance, DC offset, vertical range, sampling rate, and much more. Additionally, NI‑SCOPE can automatically configure your device settings with the Auto Setup function. Once configured, you can also export and import device settings between matching models.

#### Configuring Different Parameters

You can use the Configuration functions to configure the following settings and parameters:

- Acquisition type
- Vertical settings
- Horizontal settings
- Configuring triggers

#### Configuration Example

The Configured Acquisition example demonstrates the Configuration functions. 
This example supports most of the functionality of NI-SCOPE, so you can experiment with the digitizer.

Parent topic:

Getting Started with NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=creating-an-application-using-visual-c-or-vis.html language=enus -->
## TOPIC 00018: Creating an Application Using Visual C# or Visual Basic .NET

- bundle_id: `ni-scope`
- source_path: `creating-an-application-using-visual-c-or-vis.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/creating-an-application-using-visual-c-or-vis.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop an NI-SCOPE application with Visual C# or Visual Basic .NET, complete the following steps:Make sure you have installed the following on your computer: Microsoft .NET Framework 2.0NI-SCOPE 3.2 or later Download the NI-SCOPE .NET Libraries. Go to ni.com/downloads. Click Drivers and Updates.

### Creating an Application Using Visual C# or Visual Basic .NET

To develop an NI-SCOPE application with Visual C# or Visual Basic .NET, complete the following steps:

1. Make sure you have installed the following on your computer:
  - Microsoft .NET Framework 2.0
  - NI-SCOPE 3.2 or later
2. Download the NI-SCOPE .NET Libraries.
  1. Go to ni.com/downloads .
  2. Click Drivers and Updates .
  3. Use the Search field to locate the latest version of the NI-SCOPE .NET Libraries.
  4. Click the Readme link for installation instructions and system requirements.

Parent topic:

Creating an Application

<!--NI_TOPIC bundle=ni-scope path=creating-an-application-with-labview.html language=enus -->
## TOPIC 00019: Creating an Application with LabVIEW

- bundle_id: `ni-scope`
- source_path: `creating-an-application-with-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/creating-an-application-with-labview.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: To begin programming in LabVIEW, complete the following steps: Launch LabVIEW. Open an existing LabVIEW VI or create a new VI. Make sure you are on the block diagram screen. Open the NI-SCOPE palette. In LabVIEW 7.1 and later, the path to the palette depends on the current palette view in Tools»Opti

### Creating an Application with LabVIEW

To begin programming in LabVIEW, complete the following steps:

1. Launch LabVIEW.
2. Open an existing LabVIEW VI or create a new VI.
3. Make sure you are on the block diagram screen.
4. Open the NI-SCOPE palette. In LabVIEW 7.1 and later, the path to the palette depends on the current palette view
 in Tools»Options . In the Express palette view (default) the path is Input»Instrument Drivers»NI SCOPE .
5. Build your application using the appropriate programming flow steps.

#### LabVIEW Examples

You can find shortcuts to the LabVIEW examples at Start»All Programs»National Instruments»NI-SCOPE»Examples. 
These examples are also available in the NI-SCOPE portion of the LabVIEW functions palette.

Several forms of help are available for these examples. You 
can find an overall description of the purpose of the example by going to File»VI Properties and 
selecting Documentation
from the Category listbox. For help on individual front-panel controls, activate the LabVIEW help 
window by selecting Help»Show Context Help, and placing the cursor over the control 
you want more information about. The block diagrams of the examples are documented with step-by-step descriptions
of what the example does.

#### NI Example Finder

LabVIEW 7.0 or later users can use the NI Example Finder to search or browse examples. NI-SCOPE examples are classified by keyword, so you can search for a particular device or measurement function.
To browse for NI-SCOPE examples, launch LabVIEW, select Help»Find Examples, then 
navigate to Hardware Input and Output»Modular Instruments»
NI-SCOPE (High-Speed Digitizers).

Parent topic:

Creating an Application

Related concepts:

- NI-SCOPE Programming Flow

<!--NI_TOPIC bundle=ni-scope path=creating-voltage-histograms.html language=enus -->
## TOPIC 00020: Creating Voltage Histograms

- bundle_id: `ni-scope`
- source_path: `creating-voltage-histograms.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/creating-voltage-histograms.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a voltage histogram, you must use attributes and follow these general steps: Set the size of the histogram with the Voltage Histogram Size property or the NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_SIZE attribute. This property defines the number of histogram bins. The larger the number of bins,

### Creating Voltage Histograms

To create a voltage histogram, you must use 
attributes and follow these general steps:

1. Set the size of the histogram with the Voltage Histogram Size property or the 
 
 NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_SIZE attribute. This property defines the number 
of histogram bins. 
The larger the number of bins, the more resolution you have in the histogram. The default size is 256 bins.
2. Set the low limit of the voltage histogram with 
 Voltage Histogram Low Volts property or the 
 NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS attribute. 
 Set the high limit of the voltage histogram with 
 Voltage Histogram High Volts property or the 
 NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS attribute.
3. Call the niScope Clear Waveform Measurement Stats VI or the 
 niScope_ClearWaveformMeasurementStats function 
 to erase the histogram 
 history.

#### Voltage Histogram Example (LabVIEW Only)

Refer to the niScope EX Voltage Histogram.vi example for sample code you can use to create your own 
application.

Parent topic:

Voltage Histograms

Related concepts:

- Voltage Histograms

<!--NI_TOPIC bundle=ni-scope path=cycle-area.html language=enus -->
## TOPIC 00021: Cycle Area

- bundle_id: `ni-scope`
- source_path: `cycle-area.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/cycle-area.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_CYCLE Cycle area = voltage cycle average × pointsPerPeriod × dtwhere pointsPerPeriod is defined in the voltage cycle average description.Units Volts × Seconds

### Cycle Area

C/C++ Equivalent: 
NISCOPE_VAL_CYCLE

Cycle area = voltage cycle average × pointsPerPeriod × dt

where pointsPerPeriod is defined in the voltage cycle average description.

#### Units

Volts × Seconds

Parent topic:

Scalar Measurements in NI-SCOPE

Related concepts:

- Voltage Cycle Average

<!--NI_TOPIC bundle=ni-scope path=dc-estimate.html language=enus -->
## TOPIC 00022: DC Estimate

- bundle_id: `ni-scope`
- source_path: `dc-estimate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/dc-estimate.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_DC_ESTIMATE A Hanning window is applied to give a "processed waveform" and the voltage average is calculated with the following equation:voltage average = (Σ processed waveform[i] ) / (cg × numPoints),where the coherent gain (cg) of the Hanning window is 0.5 – the DC ga

### DC Estimate

C/C++ Equivalent: 
NISCOPE_VAL_DC_ESTIMATE

A Hanning window is applied to give a "processed waveform" and the voltage average is calculated with the following equation:

voltage average = (Σ processed waveform[i] ) / (cg × numPoints),

where the coherent gain (cg) of the Hanning window is 0.5 – the DC gain of the window.

The algorithm minimizes the effect of an uneven number of waveform cycles. For example, performing a simple voltage average on 5.5 cycles of a sine waveform gives a slightly incorrect DC estimate if the extra half cycle is not evenly divided between the positive and negative portions of the sine wave.

#### Units

Volts

Parent topic:

Scalar Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=derivative.html language=enus -->
## TOPIC 00023: Derivative

- bundle_id: `ni-scope`
- source_path: `derivative.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/derivative.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_DERIVATIVE The differences in the waveform are computed using the formula:y[i] = (waveform[i+2] – waveform[i]) / (2 × dt), where dt is the time between two points.Units Volts/second X Units seconds Resulting Array Size inputSize - 2

### Derivative

C/C++ Equivalent: 
NISCOPE_VAL_DERIVATIVE

The differences in the waveform are computed using the formula:

y[i] = (waveform[i+2] – waveform[i]) / (2 × dt), where dt is the time between two points.

#### Units

Volts/second

#### X Units

seconds

#### Resulting Array Size

inputSize - 2

Parent topic:

Array Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=digital-filtering.html language=enus -->
## TOPIC 00024: Digital Filtering

- bundle_id: `ni-scope`
- source_path: `digital-filtering.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/digital-filtering.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Analog filter design is one of the most important areas of electronic design, but it is often reserved for specialists because it requires advanced mathematical knowledge and understanding of the processes involved in the system affecting the filter. With the digital filters in NI-SCOPE, however, yo

### Digital Filtering

Analog filter design is one of the most important areas of electronic design, but it is often 
reserved for specialists because it requires advanced mathematical knowledge and understanding of the processes 
involved in the system affecting the filter. With the digital filters in NI-SCOPE, however, you do not have to 
be a design expert. NI-SCOPE handles all the design issues, computations, memory management, and actual 
filtering internally.

Although digital filters have advantages over analog filters, they have disadvantages such as floating-point 
precision limitations, numerical instability, quantization noise, and frequency warping.

#### Types of Filters

Filters alter or remove unwanted frequencies. Depending on the frequency range that they either pass or 
attenuate, they can be classified into the following types:

- A lowpass filter passes low frequencies, but rejects (or attenuates) high frequencies. 
To specify the cut-off frequency, use the Measurement Filter Cutoff Frequency attribute.
- A highpass filter passes high frequencies, but attenuates low frequencies. To specify the 
cut-off frequency, use the Measurement Filter Cutoff Frequency attribute.
- A bandpass filter passes a certain band of frequencies and attenuates others. To specify the bandpass filter, use the 
Measurement Filter Center Frequency attribute and the Filter Width attribute, where the cut-off frequencies 
are the center frequency plus or minus one-half width.
- A bandstop filter attenuates a certain band of frequencies and passes others. To specify the bandstop filter, use the
 Measurement Filter Center Frequency attribute and the Measurement Filter Width attribute, where the cut-off 
 frequencies are the center frequency plus or minus one-half width.
- An ideal filter has a gain of one (0 dB) in the passband so that the amplitude of the signal 
neither increases nor decreases. The stopband (SB) corresponds to that range of frequencies that do not pass 
through the filter at all and are rejected (attenuated).

[IMAGE alt='image' src='GUID-1EE27C3B-65E7-47AB-BD6C-5818DFD48D93-a5.svg']

#### Infinite Impulse Response (IIR) Versus Finite Impulse Response (FIR) Filters

Another way to classify filters is by impulse response. An impulse response is the response of a 
filter to an input that is an impulse (x[0] = 1 and x[i] = 0 for all i ≠ 0). The FFT of the filtered impulse 
response is known as the frequency response of the filter. The frequency response of a filter tells you what the 
output of the filter is going to be at different frequencies. In other words, it tells you the gain of the filter 
at different frequencies. For an ideal filter, the gain should be 1 in the passband and 0 in the stopband. So, 
all frequencies in the passband are passed as is to the output, but there is no output for frequencies in the 
stopband.

If the impulse response of the filter falls to zero after a finite amount of time, it is known as a FIR filter. 
However, if the impulse response exists indefinitely, it is known as an IIR filter. Whether the impulse response 
is finite (that is, whether the filter is FIR or IIR) depends on how the output is calculated.
The basic difference between FIR and IIR filters is that for FIR filters, the output depends only on the 
current and past input values, whereas for IIR filters, the output depends not only on the current and past 
input values, but also on the past output values. The advantage of digital IIR filters over FIR filters is 
that IIR filters usually require fewer coefficients to perform similar filtering operations. Thus, IIR 
filters execute much faster and do not require extra memory, because they execute in place. The disadvantage of 
IIR filters is that the phase response is nonlinear. If the application does not require phase information, such 
as amplitude spectrum analysis, IIR filters may be appropriate. You should use FIR filters for those applications
 requiring linear phase responses.

Parent topic:

Waveform Measurements

<!--NI_TOPIC bundle=ni-scope path=digital-triggers.html language=enus -->
## TOPIC 00025: Digital Triggers

- bundle_id: `ni-scope`
- source_path: `digital-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/digital-triggers.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital trigger occurs on either a rising edge or falling edge of a digital signal. Digital triggering is possible on the RTSI lines, PFI lines, and the PXI Star Trigger line.

### Digital Triggers

A digital trigger occurs on either a rising edge or falling edge of a digital 
signal. Digital triggering is possible on the RTSI lines,
 PFI lines, and the PXI Star Trigger 
line.

Parent topic:

Trigger Types

Related concepts:

- RTSI Bus
- PFI Lines
- PXI Star Trigger Line

<!--NI_TOPIC bundle=ni-scope path=getting-started-with--ni-scope.html language=enus -->
## TOPIC 00026: Getting Started with NI-SCOPE

- bundle_id: `ni-scope`
- source_path: `getting-started-with--ni-scope.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/getting-started-with--ni-scope.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SCOPE is both the application programming interface (API) and the instrument driver that controls your NI high-speed digitizer. NI-SCOPE is included with all NI high-speed digitizers.Features NI-SCOPE has the following features: Complies with the IVI-Scope driver class specification Handles conti

### Getting Started with NI-SCOPE

NI-SCOPE is both the application programming interface (API) and the instrument driver that 
controls your NI high-speed digitizer. NI-SCOPE is included with all NI high-speed digitizers.

#### Features

NI-SCOPE has the following features:

- Complies with the IVI-Scope driver class specification
- Handles continuous acquisition and multiple device synchronization
- Seamlessly integrates with National Instruments LabVIEW and LabWindows/CVI, as well as conventional programming languages
such as C/C++ and Visual Basic
- Includes more than 50 built-in measurement and analysis functions
- Processes waveform measurements in software rather than in hardware

The NI-SCOPE driver provides flexibility and 
programmability in a standard full-featured instrument driver format.

#### Examples

To help you get started, NI-SCOPE comes with examples you can use or modify. 
You can find shortcuts to the examples for each ADE at Start»All Programs»National Instruments»NI-SCOPE»Examples.

Parent topic:

Programming

Related concepts:

- Instrument Drivers

<!--NI_TOPIC bundle=ni-scope path=getting-started.html language=enus -->
## TOPIC 00027: Getting Started

- bundle_id: `ni-scope`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/getting-started.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: To get started using your NI-SCOPE device and driver software, refer to the getting started guide for your device. The getting started guide explains how to complete the following tasks: Install the software and hardware Configure the hardware in MAX Program the hardware Self-calibrate the hardware

### Getting Started

To get started using your NI-SCOPE device and driver software, refer to the getting started guide for your device. The getting started guide explains how to complete the following tasks:

- Install the software and hardware
- Configure the hardware in MAX
- Program the hardware
- Self-calibrate the hardware
- Make a first measurement
- Troubleshoot

The getting started guide for your device is printed in your hardware kit, installed with the driver software, and available at ni.com/manuals.

Tip

Related concepts:

- Integration and System Considerations
- NI-SCOPE Examples

<!--NI_TOPIC bundle=ni-scope path=hanning-window.html language=enus -->
## TOPIC 00028: Hanning Window

- bundle_id: `ni-scope`
- source_path: `hanning-window.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/hanning-window.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_HANNING_WINDOW The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications. A Hanning window is applied to the waveform using the following equation:y[i] = 0.5 × waveform[i] × [1 – cos(w)]w

### Hanning Window

C/C++ Equivalent: 
NISCOPE_VAL_HANNING_WINDOW

The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications. A Hanning window is applied to the waveform using the following equation:

y[i] = 0.5 × waveform[i] × [1 – cos(w)]

where w = (2[IMAGE alt='image' src='GUID-D51671DC-CC3C-4BD7-8447-2EFF34167458-a5.gif'])i/n and n = waveform size.

[IMAGE alt='image' src='GUID-51FF970C-D52C-4112-AC31-1CD346B10D43-a5.gif']

Note

#### Units

Volts

#### X Units

Seconds

#### Resulting Array Size

inputSize

Parent topic:

Array Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=histogram-measurements.html language=enus -->
## TOPIC 00029: Histogram Measurements

- bundle_id: `ni-scope`
- source_path: `histogram-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/histogram-measurements.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using histograms and histogram statistics with NI high-speed digitizers provides an effective visualization of waveform behavior such as the characterization of jitter in signals. Many applications call for signals with accurate and reliable periodicity and precise amplitude accuracy. Histograms are

### Histogram Measurements

Using histograms and histogram statistics with NI high-speed digitizers provides an 
effective visualization of waveform behavior such as the characterization of jitter in signals. 
Many applications call for signals with accurate and reliable periodicity and precise amplitude accuracy. 
Histograms are very useful in characterizing amplitude and temporal variations of waveforms. 
 
You can make measurements such as cycle-to-cycle and edge-to-edge jitter with time histogram
 measurements; you can make measurements such as pulse height analysis and distortion 
 with voltage histograms.

In some cases the statistical distribution of response values gives richer insights than 
numerical representations such as mean, median, standard deviation, and mode. Histograms are specialized 
plots that capture statistical data about how many times specific values occur. Histograms are 
usually plotted with the dependent variable along the vertical axis and the independent variable 
along the horizontal axis.

#### Histograms from Discrete Data

To create a histogram from discrete response data, a count is taken each time a discrete value occurs.
For example, the following figure is a histogram of 20 students' letter grades on a test.
 The discrete values are the letter grades and the counts represent the number of students who received 
 each grade.

[IMAGE alt='image' src='GUID-03888877-F101-4C45-A50E-FBACD0CC1B03-a5.svg']

#### Histograms from Continuous Data

To create a histogram from continuous response data (as in a frequency-distribution table), the 
response range is divided into ranges called bins. The value of the bin is the mean range the bin covers. 
Using the previous example, imagine the tests were graded with a percentage instead of a letter. 
The histogram in the following figure represents this distribution using bins that represent 10% 
increments.

[IMAGE alt='image' src='GUID-A1B0E0B5-3220-4F27-A915-6BC9262A3343-a5.svg']

Parent topic:

Making Waveform Measurements

Related concepts:

- Time Histograms
- Voltage Histograms

<!--NI_TOPIC bundle=ni-scope path=hysteresis-percent.html language=enus -->
## TOPIC 00030: Hysteresis Percent

- bundle_id: `ni-scope`
- source_path: `hysteresis-percent.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/hysteresis-percent.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: This attribute is used by NI-SCOPE measurements that determine crossing to calculate a measurement. For example, to calculate frequency the algorithm first determines the mid-reference level average for the signal. Next, the algorithm sets up a digital hysteresis around the mid-reference level using

### Hysteresis Percent

This attribute is used by NI-SCOPE measurements that determine crossing to 
calculate a measurement. For example, to calculate frequency the algorithm first 
determines the mid-reference level average for the signal. Next, the algorithm 
sets up a digital hysteresis around the mid-reference level using the attribute 
Hysteresis Percent. The algorithm then finds all crossings by counting the number
 of times the waveform crosses the upper hysteresis level, mid reference level,
 and lower hysteresis level. Note that the hysteresis levels are calculated based 
on the vertical range. The algorithm multiplies the hysteresis percent attribute by 
the vertical range attribute to determine the upper and lower hysteresis levels. 
The default value for the hysteresis percent is configured to 2, which means in a 
2 V vertical range the algorithm does not see signals/noise that are less than 40 mV.

Parent topic:

Reference Levels

<!--NI_TOPIC bundle=ni-scope path=hysteresis-triggers.html language=enus -->
## TOPIC 00031: Hysteresis Triggers

- bundle_id: `ni-scope`
- source_path: `hysteresis-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/hysteresis-triggers.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Hysteresis triggers eliminate incorrect triggers caused by noisy signals. For example, if your signal contains two rising edges of different amplitudes, you can use hysteresis triggering to trigger on one of the edges. Although NI-SCOPE uses a default amount of hysteresis for edge triggering, which

### Hysteresis Triggers

Hysteresis triggers eliminate incorrect triggers caused by noisy signals. For example,
 if your signal contains two rising edges of different amplitudes, you can use hysteresis triggering to 
 trigger on one of the edges. Although NI-SCOPE uses a default amount of hysteresis for edge triggering, 
 which is typically 2.5% of the vertical range, you can override that value by setting your own 
 hysteresis values. The Configure Trigger Hysteresis function or VI allows you to choose 
 the trigger coupling, trigger level, hysteresis value, and trigger slope.

Hysteresis triggering is possible on all analog trigger channels, such as 0, 1, or 
the external trigger input.

A positive slope hysteresis trigger is generated when the signal crosses below the voltage specified by the 
trigger level parameter minus the hysteresis value, and then crosses the trigger level.

[IMAGE alt='image' src='GUID-D82DA1F8-0E32-4C0F-BC9A-4E13961424F9-a5.svg']

A negative slope hysteresis trigger is generated when a signal crosses above the voltage specified by the 
trigger level parameter plus the hysteresis value, and then crosses the trigger level.

[IMAGE alt='image' src='GUID-3D34D69D-8F8C-4FCA-AEA3-E0AAE3A478C0-a5.svg']

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-scope path=iir-filters.html language=enus -->
## TOPIC 00032: IIR Filters

- bundle_id: `ni-scope`
- source_path: `iir-filters.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/iir-filters.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Filters are classified as infinite impulse response (IIR) filters if the impulse response exists indefinitely. For IIR filters, the output depends not only on the current and past input values, but also on the past output values. Truncating Data with IIR Filters Because IIR filters depend on the out

### IIR Filters

Filters are classified as infinite impulse response (IIR) filters if the impulse response 
exists indefinitely. For IIR filters, the output depends not only on the current and past input values, 
but also on the past output values.

#### Truncating Data with IIR Filters

Because IIR filters depend on the output and the input, there is a transient response at the beginning of the 
filtered data that is invalid, due to the assumptions made at the beginning boundary condition. This is due to 
the assumption that negative indices in the general IIR difference equation are zero. NI-SCOPE IIR filters remove the user-defined transient portion by deleting 
the first input size times the Measurement Filter Transient Waveform Percent attribute divided by 100 from the 
beginning of the filtered data array. This feature is useful when using a combination of processing steps, so 
the result of an IIR filter excluding the transient portion may be the input of another measurement. 
The length of the transient response depends on both the filter order and the input waveform, 
and it may require some trial and error to determine the proper setting for the Measurement Filter Transient 
Waveform Percent attribute.

[IMAGE alt='image' src='GUID-100D39D6-D1F0-44E9-A5B4-8629BBBCF9C3-a5.svg']

Parent topic:

Digital Filtering

Related concepts:

- FIR Filters
- Digital Filtering

<!--NI_TOPIC bundle=ni-scope path=immediate-triggers.html language=enus -->
## TOPIC 00033: Immediate Triggers

- bundle_id: `ni-scope`
- source_path: `immediate-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/immediate-triggers.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Immediate triggers occur when the digitizer triggers itself. There is no external signal that triggers the acquisition—the acquisition simply begins immediately after being configured by the driver software. Immediate triggering is the default option on NI high-speed digitizers. Therefore, you can o

### Immediate Triggers

Immediate triggers occur when the digitizer triggers itself. There is no external 
signal that triggers the acquisition—the acquisition simply begins immediately after
being configured by the driver software. Immediate triggering is the default option on NI high-speed digitizers. 
Therefore, you can omit using this function if you never change triggering modes.

Parent topic:

Trigger Types

<!--NI_TOPIC bundle=ni-scope path=initialize.html language=enus -->
## TOPIC 00034: Initialize

- bundle_id: `ni-scope`
- source_path: `initialize.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/initialize.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because you can have multiple digitizers connected to your computer, you must tell NI-SCOPE which digitizer(s) to communicate with by opening a session to the digitizer or digitizers with an Initialize function. What Is a Session? A session establishes a connection between digitizers and your applic

### Initialize

Because you can have multiple digitizers connected to your computer,
 you must tell NI-SCOPE which digitizer(s) to communicate with by opening a session to the digitizer or digitizers with an Initialize function.

#### What Is a Session?

A session establishes a connection between digitizers and your 
application. After this connection is established, the digitizer(s) can transmit data to your 
application. Sessions allow the driver to cache previous settings, which greatly improves performance.

#### How Do You Create a Session?

To create a session, use the Initialize with Options or Initialize functions. 
These functions return a handle that allows you to communicate with the digitizer(s) using other function calls in your 
application.

You can create sessions that include multiple instruments of the same model and in the same chassis. This automatically synchronizes all channels of the included instruments, simplifying your test program development and maintenance. To create a session to multiple digitizers, enter the instrument names as a comma-delimited list of strings in the form PXI1Slot3,PXI1Slot4 for the Resource Name input parameter of an Initialize function.

Note

#### LabVIEW Example—Initializing a Session

[IMAGE alt='image' src='GUID-FA36A94E-E778-4395-8CD3-E3D0470AD505-a5.gif']

#### C Example—Initializing a Session

niScope_init ("PXI1Slot2", VI_TRUE, VI_TRUE, &vi);

Note

- When you run your application, you must use the resource name 
assigned by 
Measurement & Automation Explorer (MAX). 
Find or set the resource name for your digitizers by launching 
MAX and selecting Devices and Interfaces .
- Setting the ID Query parameter to TRUE has no effect with NI-SCOPE.
NI-SCOPE automatically 
 verifies that the digitizer(s) you initialize are supported—therefore, 
 setting this parameter to TRUE is not necessary.
- Setting the Reset Device parameter to TRUE 
 resets digitizers during initialization.

Caution

Parent topic:

NI-SCOPE Tutorial

<!--NI_TOPIC bundle=ni-scope path=input-coupling.html language=enus -->
## TOPIC 00035: Input Coupling

- bundle_id: `ni-scope`
- source_path: `input-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/input-coupling.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: On many digitizers, you can configure the input channels to be DC-coupled, AC-coupled, or GND coupled. DC coupling allows DC and low-frequency components of a signal to pass through without attenuation. In contrast, AC coupling removes DC offsets and attenuates low frequency components of a signal.

### Input Coupling

On many digitizers, you can configure the input channels to be 
DC-coupled, AC-coupled, or GND coupled. DC coupling allows DC and low-frequency components of a 
signal to pass through without attenuation. In contrast, AC coupling removes DC 
offsets and attenuates low frequency components of a signal. This feature can be 
exploited to zoom in on AC signals with large DC offsets, such as switching noise on 
a 12 V power supply. GND coupling disconnects the input and internally connects the channel to
ground to provide a ground, zero-voltage reference.

Refer to the specifications for your specific digitizer for input limits 
that must be observed regardless of coupling.

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=ni-scope path=instrument-drivers.html language=enus -->
## TOPIC 00036: Instrument Drivers

- bundle_id: `ni-scope`
- source_path: `instrument-drivers.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/instrument-drivers.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: An instrument driver is a set of software routines that control programmable instruments. Each routine corresponds to a programmatic operation such as configuring, reading from, writing to, and triggering the instrument. Instrument drivers simplify instrument control and reduce test program developm

### Instrument Drivers

An instrument driver is a set of software routines that control programmable instruments. Each routine corresponds 
to a programmatic operation such as configuring, reading from, writing to, and triggering the instrument. 
Instrument drivers simplify instrument control and reduce test program development time by eliminating the need to 
learn the programming protocol for each instrument. NI-SCOPE, NI-FGEN, NI-DMM, and NI-HSDIO are examples of instrument drivers provided by National Instruments.

#### Instrument Driver Structure

All instrument drivers have the same basic hierarchy. Instrument drivers are written from low-level 
components that are used to program instruments. These component functions fit into 
six categories—Initialize, 
Configuration, Action/Status, Data, Utility, and Close.

#### Initialize

All instrument drivers have an Initialize function. It is the first instrument driver function called and establishes communication with instruments. Optionally, it can also perform instrument identification query and reset operations. Initialization also places instruments in a specific state, usually the default power on state.

#### Configuration

Configuration functions are collections of software routines that configure instruments to perform a desired operation. The number of Configuration functions depends on the complexity of the instruments. After the Configuration functions are called, the instruments are ready to take measurements.

#### Action/Status

The Action/Status category contains two types of functions. Action functions cause instruments to initiate or terminate test and measurement operations such as arming the triggering system or generating a stimulus. Action functions differ from Configuration functions in that they do not change instrument settings; instead, they order the instrument to carry out an action based on its current configuration settings. 
Status functions return the current status of instruments or of pending operations. Specific routines in this category and the actual operations they perform are at the discretion of the instrument driver developer, and are usually created as required by other functions.

#### Data

Data functions include calls to transfer data to or from instruments. Examples of Data function operations include reading a measured value or waveform from a measurement instrument, and downloading waveforms or digital patterns to a source instrument. Specific routines in this category depend on the instrument.

#### Utility

Utility functions perform a variety of operations auxiliary to the most-used instrument driver calls. These functions include the majority of the template instrument driver calls such as reset, 
self-test, revision, and error query, and may include other custom routines such as 
calibration or storing/recalling instrument configurations.

#### Close

All instrument drivers include a Close function. The Close function terminates the software connection to instruments and deallocates system resources used during that instrument session.

Parent topic:

NI-SCOPE Tutorial

<!--NI_TOPIC bundle=ni-scope path=integral.html language=enus -->
## TOPIC 00037: Integral

- bundle_id: `ni-scope`
- source_path: `integral.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/integral.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_INTEGRAL Numerical integration is done using Simpson's rule.Units Volts × seconds

### Integral

C/C++ Equivalent: 
NISCOPE_VAL_INTEGRAL

Numerical integration is done using Simpson's rule.

#### Units

Volts × seconds

Parent topic:

Scalar Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=last-acquisition-histogram-method.html language=enus -->
## TOPIC 00038: Last-Acquisition Histogram Method

- bundle_id: `ni-scope`
- source_path: `last-acquisition-histogram-method.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/last-acquisition-histogram-method.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Last-acquisition histogram method is used by the voltage low and voltage high measurements for computing the extrema of a waveform. This method is useful for ignoring overshoot or preshoot in a square waveform. In this method, a voltage histogram is created from the most recent acquisition. The limi

### Last-Acquisition Histogram Method

Last-acquisition histogram method is used by the voltage low and voltage high measurements for computing the extrema of a waveform. This method is useful for ignoring overshoot or preshoot in a square waveform.
In this method, a voltage histogram is created from the most recent acquisition. The limits of this histogram are set by the minimum and maximum voltages of the acquisition. NI-SCOPE then counts how many samples fall into each bin of the histogram. The resolution is defined by the Last Acquisition Histogram Size attribute, which is 256 bins by default. You can fetch the histogram array using the Fetch Array Measurement function, with Last Acquisition Histogram constant specified as the array measurement function.
The following illustrations show an example of a square wave and its resulting histogram. In the histogram the voltage low and voltage high measurements correspond to the middle value of a bin with the maximum number of hits in the lower 40% or upper 40% respectively.

[IMAGE alt='image' src='GUID-BE513465-9E9F-4295-AF57-E783302F8762-a5.svg']

[IMAGE alt='image' src='GUID-01C92000-32D1-4D80-8D89-BC17C665A6F6-a5.svg']

Parent topic:

Waveform Measurements

<!--NI_TOPIC bundle=ni-scope path=making-waveform-measurements.html language=enus -->
## TOPIC 00039: Making Waveform Measurements

- bundle_id: `ni-scope`
- source_path: `making-waveform-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/making-waveform-measurements.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the different ways to make waveform measurements, which are processed in software by NI-SCOPE. For more information, refer to the following: Fetching Scalar and Array Measurements Making Scalar Measurements Making Array Measurements Processing Time Domain Data Often the time-d

### Making Waveform Measurements

This section describes the different ways to make waveform measurements, which are processed in software 
by NI-SCOPE. For more information, refer to the following:

- Fetching Scalar and Array Measurements
- Making Scalar Measurements
- Making Array Measurements

#### Processing Time Domain Data

Often the time-domain data returned from a digitizer requires processing before measurements are done. 
To do this, register an array measurement as a processing step by using the 
AddWaveformProcessing function. At the time of registering the processing step, the entire set of 
 NISCOPE_ATTR_MEAS parameters are cached. Then when a measurement function is called, the 
processing measurements are completed with this cached set of parameters, and the result is used in the 
measurement. This allows streaming together of measurements. For example, if you register Add Channels
and 
Bessel Filter as processing steps, fetching a frequency measurement actually gives you the frequency of 
the filtered summation of two channels.

Parent topic:

Getting Started with NI-SCOPE

Related concepts:

- Fetching Scalar and Array Measurements
- Making Scalar Measurements
- Making Array Measurements

<!--NI_TOPIC bundle=ni-scope path=measuring-reference-level-crossings.html language=enus -->
## TOPIC 00040: Measuring Reference-Level Crossings

- bundle_id: `ni-scope`
- source_path: `measuring-reference-level-crossings.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/measuring-reference-level-crossings.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: All scalar measurements involving time use the concept of reference-level crossings, which occur when the waveform voltage crosses the reference level. Linear interpolation accurately estimates the crosspoint times, but noise can create a higher number of level crossings. To minimize the impact of n

### Measuring Reference-Level Crossings

All scalar measurements involving time use the concept of reference-level crossings, which occur when the waveform voltage crosses the reference level. 
Linear interpolation accurately estimates the crosspoint times, but noise can create a higher number of level crossings. To minimize the impact of noise, you can create a hysteresis window around crosspoints. To count a crossing, the signal must start outside 
this window and then pass through the window to the crosspoint. 
A crossing is not counted again until the signal passes outside the window and then passes through the window to the crosspoint. The following figure shows an exaggerated example of digital hysteresis, where the dots are the real crosspoints after eliminating the spurious crosspoints caused by noise.

[IMAGE alt='image' src='GUID-9BE752F4-8E53-4AB2-B9E2-8F2F51D0DE9E-a5.svg']

Parent topic:

Waveform Measurements

<!--NI_TOPIC bundle=ni-scope path=mid-ref-volts.html language=enus -->
## TOPIC 00041: Mid Ref Volts

- bundle_id: `ni-scope`
- source_path: `mid-ref-volts.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/mid-ref-volts.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_MID_REF_VOLTS The voltage corresponding to the mid reference level. If the Reference Level Units property or the NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS attribute is set to Voltage, the value of the Channel Based Mid Ref property or the NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL at

### Mid Ref Volts

C/C++ Equivalent: 
NISCOPE_VAL_MID_REF_VOLTS

The voltage corresponding to the mid reference level. If the 
Reference 
Level Units property or the 
NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS attribute 
is set to Voltage, the value of the 
Channel Based Mid Ref property or the 
NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL attribute is returned.

If the 
 Reference 
Level Units property or the 
 NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS attribute 
 is set to Percentage, the voltage is calculated with the method specified by the
Percentage Units Method property or the 
NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD attribute.

#### Units

Volts

Parent topic:

Scalar Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=monitoring-a-device.html language=enus -->
## TOPIC 00042: Monitoring a Device

- bundle_id: `ni-scope`
- source_path: `monitoring-a-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/monitoring-a-device.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can monitor a device with LabVIEW, CVI, TestStand, or your application in the SFP to troubleshoot problems with your device under test or application. View data and device settings by sharing your device between the SFP and your application. Complete the following steps to monitor a device with

### Monitoring a Device

You can monitor a device with LabVIEW, CVI, TestStand, or your application in the SFP to troubleshoot problems with your device under test or application. View data and device settings by sharing your device between the SFP and your application.

Complete the following steps to monitor a device with the SFP:

1. Launch the SFP. Tip 

 You can launch the SFP from the Windows Start menu, the Tools menu in LabVIEW, or from your device listed under Devices and Interfaces in the MAX configuration tree.
2. Select an In Use device that you want to monitor with the SFP. Debug Driver Session (Monitor) is selected from the pull-down menu.
3. When you finish monitoring the device, close the SFP.

Parent topic:

Debugging a Device in the SFP While in Use by Another Application

<!--NI_TOPIC bundle=ni-scope path=multi-acq-average.html language=enus -->
## TOPIC 00043: Multi Acq Average

- bundle_id: `ni-scope`
- source_path: `multi-acq-average.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/multi-acq-average.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_MULTI_ACQ_AVERAGE The first time this measurement is called after it is cleared, an array the same size as the input is initialized to the input waveform, and the initial x and x increment values are set. Every subsequent call updates and returns the running average arr

### Multi Acq Average

C/C++ Equivalent: 
NISCOPE_VAL_MULTI_ACQ_AVERAGE

The first time this measurement is called after it is cleared, an array the same size as 
the input is initialized to the input waveform, and the initial x and 
x increment values are set. Every subsequent call updates and returns the running
 average array without affecting the size of the array. The average array is cleared by calling 
 niScope Clear Waveform Measurement Stats VI or the 
niScope_ClearWaveformMeasurementStats
 with the measurement function parameter set to Multi Acq Average.

#### Units

Volts

#### X Units

Seconds

#### Resulting Array Size

inputSize (during the first call to this measurement after clearing it)

Parent topic:

Array Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=multi-acq-time-histogram.html language=enus -->
## TOPIC 00044: Multi Acq Time Histogram

- bundle_id: `ni-scope`
- source_path: `multi-acq-time-histogram.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/multi-acq-time-histogram.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM The initial x value returned is the bin value for the first bin, corresponding to the midpoint of the range of values in the first bin. The x increment returned is the bin size.Units Count X Units Seconds Resulting Array Size The value of the Me

### Multi Acq Time Histogram

C/C++ Equivalent: 
NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM

The initial x value returned is the bin value for the first bin, corresponding to the midpoint of the range of values in the first bin. The x increment returned is the bin size.

#### Units

Count

#### X Units

Seconds

#### Resulting Array Size

The value of the Measurement Time Histogram Size property or the NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_SIZE attribute during the first time histogram measurement after the histogram is cleared.

Parent topic:

Array Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=multi-acq-voltage-histogram.html language=enus -->
## TOPIC 00045: Multi Acq Voltage Histogram

- bundle_id: `ni-scope`
- source_path: `multi-acq-voltage-histogram.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/multi-acq-voltage-histogram.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM The initial x value returned is the bin value for the first bin, corresponding to the midpoint of the range of values in the first bin. The x increment returned is the bin size.Units Count X Units Volts Resulting Array Size The value of the M

### Multi Acq Voltage Histogram

C/C++ Equivalent: 
NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM

The initial x value returned is the bin value for the first bin, corresponding to the midpoint of the range of values in the first bin. The x increment returned is the bin size.

#### Units

Count

#### X Units

Volts

#### Resulting Array Size

The value of the Measurement Voltage Histogram Size property or the 
NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_SIZE attribute during the first voltage histogram measurement after the histogram is cleared.

Parent topic:

Array Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=multiply-channels.html language=enus -->
## TOPIC 00046: Multiply Channels

- bundle_id: `ni-scope`
- source_path: `multiply-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/multiply-channels.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_MULTIPLY_CHANNELS Multiplies the waveforms from two channels, where one channel is specified by the channel parameter to the niScope Fetch Measurement (poly) VI (Measurement Scalar DBL instance) or the niScope_FetchWaveformMeasurementArray function, and the other channe

### Multiply Channels

C/C++ Equivalent: 
NISCOPE_VAL_MULTIPLY_CHANNELS

Multiplies the waveforms from two channels, where 
one channel is specified by the channel parameter 
to the niScope Fetch Measurement (poly) VI 
(Measurement Scalar DBL instance) or the niScope_FetchWaveformMeasurementArray function, and the other channel is the Other Channel property or the NISCOPE_ATTR_MEAS_OTHER_CHANNEL attribute. Any processing steps registered with the niScope Add Waveform Processing VI or the niScope_AddWaveformProcessing 
function are completed for the "other channel" before this measurement is taken. The
 two channels used in this measurement must be different.

#### Units

Volts<sup>2</sup>

#### X Units

Seconds

#### Resulting Array Size

inputSize (on the channel specified by the measurement VI)

Parent topic:

Array Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=negative-duty-cycle.html language=enus -->
## TOPIC 00047: Negative Duty Cycle

- bundle_id: `ni-scope`
- source_path: `negative-duty-cycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/negative-duty-cycle.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_DUTY_CYCLE_NEG The negative width divided by the period times 100.Units Percentage

### Negative Duty Cycle

C/C++ Equivalent: 
NISCOPE_VAL_DUTY_CYCLE_NEG

The negative width divided by the period times 100.

#### Units

Percentage

Parent topic:

Scalar Measurements in NI-SCOPE

Related concepts:

- Negative Width
- Period

<!--NI_TOPIC bundle=ni-scope path=negative-width.html language=enus -->
## TOPIC 00048: Negative Width

- bundle_id: `ni-scope`
- source_path: `negative-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/negative-width.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_WIDTH_NEG The time difference between the first two mid reference level crossings, where the slopes are negative and positive, respectively. A digital hysteresis is used when finding the crosspoints. Units Seconds

### Negative Width

C/C++ Equivalent: 
NISCOPE_VAL_WIDTH_NEG

The time difference between the first two mid reference level crossings, where the slopes are negative and positive, respectively. A digital hysteresis is used when finding the crosspoints.

#### Units

Seconds

Parent topic:

Scalar Measurements in NI-SCOPE

<!--NI_TOPIC bundle=ni-scope path=ni-scope--programming-flow.html language=enus -->
## TOPIC 00049: NI-SCOPE Programming Flow

- bundle_id: `ni-scope`
- source_path: `ni-scope--programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/ni-scope--programming-flow.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SCOPE provides the same functionality in two formats: In LabVIEW as VIs In traditional programming languages as functions If you are new to NI-SCOPE, read Getting Started with NI-SCOPE (Tutorial) before you read this section. The following diagram illustrates the basic programming flow for usin

### NI-SCOPE Programming Flow

NI-SCOPE provides the same functionality in two formats:

- In LabVIEW as VIs
- In traditional programming languages as functions

Note

The following diagram illustrates the basic programming flow for using NI-SCOPE functions in your own digitizer applications. Click the VIs in the diagram for more detailed programming information.

[IMAGE alt='image' src='GUID-AF91CC0F-3EF5-4D0B-AC9E-D5B893563DEA-a5.png']

For any application you write, you must open a session to establish communication with the digitizer(s) by using niScope Initialize or niScope Initialize With Options. When your program finishes, you must close the session with niScope Close.

Initialize functions set the driver and digitizers to a known state. This function may take a significant amount of time compared to all other NI-SCOPE functions, so you should not include it in a loop when repeatedly acquiring data. Ideally, your program should call an Initialize function one time. If the reset device parameter is set to TRUE, the digitizer resets to the default state, which may include resetting relays and resetting time stamp counters.

Caution

niScope Close is essential for freeing resources, including deallocating memory, destroying threads, and freeing operating system resources. You should close every session that you initialize, even if an error occurs during the program. While debugging your application, it is common to abort execution before you reach Close. Though aborting the execution should not cause problems, NI does not recommend doing so.

#### Examples

All NI-SCOPE examples include niScope Initialize or niScope Initialize With Options, niScope Close, and Error Message (except for LabVIEW). The Getting Started example is a good choice to start with if you are inexperienced with NI-SCOPE because it is the simplest example.

Parent topic:

Getting Started with NI-SCOPE

Related concepts:

- NI-SCOPE Tutorial

<!--NI_TOPIC bundle=ni-scope path=ni-scope-32-bit-soft-front-panel-help.html language=enus -->
## TOPIC 00050: NI-SCOPE 32-Bit Soft Front Panel Help

- bundle_id: `ni-scope`
- source_path: `ni-scope-32-bit-soft-front-panel-help.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/ni-scope-32-bit-soft-front-panel-help.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: This help file contains information about using the 32‑bit NI-SCOPE Soft Front Panel (SFP) to interactively control your NI high-speed digitizer. For information about developing applications, refer to NI High-Speed Digitizers Help»Programming. The information in this help file is relevant only to

### NI-SCOPE 32-Bit Soft Front Panel Help

This help file contains information about using the 32‑bit NI-SCOPE Soft Front Panel (SFP) to interactively control your NI high-speed digitizer. For information about developing applications, refer to NI High-Speed Digitizers Help»Programming.

Note

Similar to stand-alone oscilloscopes, the SFP acquires, controls, analyzes, and presents data. Unlike bench-top instruments, however, you can use the SFP to view and control waveforms directly from your computer. You can also run multiple sessions of the SFP simultaneously.

The SFP provides the following functionality:

- Easily observe and control signal
- Debug a device
- Load/store waveforms
- Load/store device-specific configurations
- Make scalar measurements
- Use NI-SCOPE utilities such as Auto-Setup and Self-Calibration

Note

Help»Show Context Help

Parent topic:

NI-SCOPE Soft Front Panel and InstrumentStudio

Related concepts:

- NI-SCOPE Soft Front Panel and InstrumentStudio

<!--NI_TOPIC bundle=ni-scope path=ni-scope-examples.html language=enus -->
## TOPIC 00051: NI-SCOPE Examples

- bundle_id: `ni-scope`
- source_path: `ni-scope-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/ni-scope-examples.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SCOPE includes several example applications that demonstrate the functionality of your device and can serve as interactive tools, programming models, and building blocks for your own applications. NI Example Finder The NI Example Finder is a utility that organizes examples into categories and all

### NI-SCOPE Examples

NI-SCOPE includes several example applications that demonstrate the functionality of your device and can serve as interactive tools, programming models, and building blocks for your own applications.

#### NI Example Finder

The NI Example Finder is a utility that organizes examples into categories and allows you to browse and search installed examples. For example, search for "SCOPE" to locate all NI Digitizers signal generator examples. You can see descriptions and compatible hardware models for each example or see all the examples compatible with one particular hardware model.

To locate examples using the NI Example Finder within LabVIEW or LabWindows/CVI, select Help»Find Examples and navigate to Hardware Input and Output»Modular Instruments»NI-SCOPE.

#### Installed Example Locations

| Software Application | Installed Example Locations |
| --- | --- |
| LabVIEW | <LabVIEW>\\examples\\instr\\niScope, where <LabVIEW> is the LabVIEW directory for the specific LabVIEW version you installed on your system. |
| LabWindows/CVI | Program Files\\IVI Foundation\\IVI\\Drivers\\niScope\\Examples\\CVI |
| ANSI C or Microsoft Visual C/C++ | <NIDocDir>\\NI-SCOPE\\examples, where <NIDocDir> is one of the following directories: Windows 8/7/Vista—Users\\Public\\Documents\\National Instruments Windows XP—Documents and Settings\\All Users\\Shared Documents\\National Instruments |

#### Common NI-SCOPE Examples

| NI-SCOPE Example | Description |  |
| --- | --- | --- |
|  | niScope EX Getting Started.vi | This example opens a session to the NI-SCOPE driver and uses the Auto Setup VI to optimally configure the session properties and displays the acquired channel data. |
|  | niScope EX Quick Start.vi | This example opens and configures an NI-SCOPE session and allows you to experiment with numerous configurations, including acquisition types and triggering modes, since it supports nearly the entire functionality of NI-SCOPE. It is designed so that if the recommended input signal is used, most configurations will return valid results. |
|  | niScope EX Configured Acquisition.vi | This example configures all the digitizer's vertical, horizontal, and triggering properties before every acquisition. It allows you to experiment with numerous configurations, including acquisition types and triggering modes, since it supports nearly the entire functionality of NI-SCOPE. |
|  | niScope EX Fetch Forever.vi | This example demonstrates using continuous acquisition to fetch an infinite record of data (until you press "Stop"). |
|  | niScope EX Stream to Disk.vi | This example demonstrates streaming a continuous acquisition to disk. |
|  | niScope EX Advanced Measurement Library.vi | This example illustrates using some of the advanced measurement library functions such as waveform processing and filtering. |
|  | niScope EX Multi-Device Configured Acquisition (TClk).vi | This example demonstrates how to easily synchronize an arbitrary number of digitizers with NI-TClk. |

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-scope path=ni-scope-instrument-driver-fpga-extensions.html language=enus -->
## TOPIC 00052: NI-SCOPE Instrument Driver FPGA Extensions

- bundle_id: `ni-scope`
- source_path: `ni-scope-instrument-driver-fpga-extensions.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/ni-scope-instrument-driver-fpga-extensions.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SCOPE instrument driver FPGA extensions for reconfigurable oscilloscopes enable you to use precompiled FPGA bitfiles to customize the behavior of a reconfigurable oscilloscope FPGA while maintaining the functionality of the NI-SCOPE instrument driver.Before you begin using NI-SCOPE instrument dri

### NI-SCOPE Instrument Driver FPGA Extensions

NI-SCOPE instrument driver FPGA extensions for reconfigurable oscilloscopes enable you to use precompiled FPGA bitfiles to customize the behavior of a reconfigurable oscilloscope FPGA while maintaining the functionality of the NI-SCOPE instrument driver.

Before you begin using NI-SCOPE instrument driver FPGA extensions, you must install NI-SCOPE and
 LabVIEW. You must also download a precompiled bitfile to use NI-SCOPE instrument driver
 FPGA extensions. Consult *An Introduction to Instrument Driver FPGA Extensions for
 NI Software-Designed Instruments* for more information and example use
 cases.

Note

Example precompiled bitfiles are included in programs that illustrate how to use the precompiled
 bitfiles. These examples contain three parts: a precompiled bitfile featuring
 application-specific IP, a host-based example that uses NI-SCOPE, and IP dependencies,
 such as source code. You can find examples through VI Package Manager, which installs
 with LabVIEW.

When you install NI-SCOPE, model-specific folders for the supported devices are created in the following location:

- Windows 10/8.1/7: Users\Public\Documents\National Instruments\FPGA Extensions Bitfiles

Note

Parent topic:

Programming

Related concepts:

- Using NI-SCOPE Instrument Driver FPGA Extensions

Related information:

- An Introduction to Instrument Driver FPGA Extensions for NI Software-Designed Instruments
- Download & Manage LabVIEW Add-ons with VI Package Manager
 (VIPM)
- LabVIEW FPGA User Manual

<!--NI_TOPIC bundle=ni-scope path=ni-scope-soft-front-panel-and-instrumentstudi.html language=enus -->
## TOPIC 00053: NI-SCOPE Soft Front Panel and InstrumentStudio

- bundle_id: `ni-scope`
- source_path: `ni-scope-soft-front-panel-and-instrumentstudi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/ni-scope-soft-front-panel-and-instrumentstudi.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: October 2018When you install NI‑SCOPE on a 64‑bit system, you can monitor, control, and record measurements from supported devices using InstrumentStudio. InstrumentStudio is a software-based front panel application that allows you to perform interactive measurements on several different device type

### NI-SCOPE Soft Front Panel and InstrumentStudio

October 2018

When you install NI‑SCOPE on a 64‑bit system, you can monitor, control, and record measurements from supported devices using InstrumentStudio. InstrumentStudio is a software-based front panel application that allows you to perform interactive measurements on several different device types, including oscilloscopes, in a single program.

Note

InstrumentStudio is automatically installed when you install the NI‑SCOPE driver. You can access InstrumentStudio in one of the following ways:

- From the Windows start menu, select National Instruments»NI‑SCOPE Soft Front Panel . This launches InstrumentStudio and runs a soft front panel populated with NI‑SCOPE devices.
- From the Windows start menu, select National Instruments»InstrumentStudio [year] . This launches InstrumentStudio and runs a soft front panel populated with devices detected on your system.
- From Measurement & Automation Explorer (MAX), select a device and then click Test Panels... . This launches InstrumentStudio and runs a soft front panel for the device you selected.

For more information on using InstrumentStudio, refer to the *InstrumentStudio
 Manual*.

Related concepts:

- NI-SCOPE 32-Bit Soft Front Panel Help

Related information:

- InstrumentStudio User Manual

<!--NI_TOPIC bundle=ni-scope path=ni-scope-tutorial.html language=enus -->
## TOPIC 00054: NI-SCOPE Tutorial

- bundle_id: `ni-scope`
- source_path: `ni-scope-tutorial.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/ni-scope-tutorial.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Example Programs NI-SCOPE ships with several examples that demonstrate some basic digitizer applications. You can find these examples at Start»All Programs»National Instruments»NI-SCOPE»Examples. The NI-SCOPE examples assume that you are already familiar with your ADE. If you are unfamiliar with

### NI-SCOPE Tutorial

#### Example Programs

NI-SCOPE ships with several examples that demonstrate some basic digitizer applications. 
You can find these 
 examples at Start»All Programs»National Instruments»NI-SCOPE»Examples.

Note

Getting Started

NI-SCOPE provides the same functionality in two different formats—as virtual instruments (VIs) in LabVIEW and as functions in traditional programming languages.

#### Basic Steps

The tutorial explains how to do the following:

1. Initialize the session.
2. Configure an application.
3. Acquire data.
4. Retrieve error information.
5. Close the session.

After you finish the NI-SCOPE Tutorial, you can find more advanced information in the following sections:

- Acquisition Functions
- Configuration Functions
- Attributes and Attribute Functions

Parent topic:

Getting Started

Related concepts:

- Initialize
- Configure the Application
- Acquiring the Data
- Retrieving Error Information
- Closing the Session
- Acquisition Functions
- Configuration Functions
- Attributes and Attribute Functions

<!--NI_TOPIC bundle=ni-scope path=noise.html language=enus -->
## TOPIC 00055: Noise

- bundle_id: `ni-scope`
- source_path: `noise.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/noise.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise is any unwanted signal that appears in your sampled data. Noise comes from both external sources, such as the AC power line, motors, generators, transformers, fluorescent lights, soldering irons, CRT displays, computers, electrical storms, welders, and radio transmitters, and internal sources,

### Noise

Noise is any unwanted signal that appears in your sampled data. Noise comes from both external sources, such as 
the AC power line, motors, generators, transformers, fluorescent lights, soldering irons, 
CRT displays, computers, electrical storms, welders, and radio transmitters, and internal sources, 
such as digital clocks, microprocessors, and switched mode power supplies.

Noise can be transient in nature, have fixed frequencies such as harmonic or mixer products, 
or be broadband random noise.

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=ni-scope path=nyquist-theorem.html language=enus -->
## TOPIC 00056: Nyquist Theorem

- bundle_id: `ni-scope`
- source_path: `nyquist-theorem.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/nyquist-theorem.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Nyquist theorem states that a signal must be sampled at least twice as fast as the highest frequency component of the signal to accurately reconstruct the waveform. Frequency components higher than half the sample rate are mistakenly interpreted as low-frequency components, a phenomenon known as

### Nyquist Theorem

The Nyquist theorem states that a signal must be sampled at least 
twice as fast as the highest frequency component of the signal to accurately reconstruct the waveform. 
Frequency components higher than half the sample rate are mistakenly interpreted as low-frequency components, a phenomenon known as 
aliasing. The following figure shows a 5 MHz sine wave digitized by a 6 MS/s ADC. The dotted line indicates the aliased signal recorded
by the ADC at that sample rate. The 5 MHz frequency aliases back into the passband, falsely appearing as a 1 MHz sine wave. Inserting a lowpass filter with a cutoff at the Nyquist rate prevents aliasing in the passband.

[IMAGE alt='image' src='GUID-B1BD586E-DD6E-4CA5-B2F9-D48B44499384-a5.svg']

The following figure shows the frequency view of the same example.

[IMAGE alt='image' src='GUID-C962B9FB-E66E-4CE2-9B36-B748B65ABE68-a5.svg']

where

fs = 6 MS/s
fN = 3 MHz (the Nyquist frequency)
fa = 1 MHz (1fs - 5 MHz)

Parent topic:

Sample Rate

Related concepts:

- Aliasing
- Undersampling
- Oversampling

<!--NI_TOPIC bundle=ni-scope path=operating-system-support.html language=enus -->
## TOPIC 00057: Operating System Support

- bundle_id: `ni-scope`
- source_path: `operating-system-support.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/operating-system-support.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: For information about the supported operating system (OS) for your device, refer to the NI-SCOPE Readme at Start»All Programs»National Instruments»NI-SCOPE»Documentation.

### Operating System Support

For information about the supported operating system (OS) for your 
device, refer to the 
 NI-SCOPE Readme at Start»All Programs»National Instruments»NI-SCOPE»Documentation.

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-scope path=oversampling.html language=enus -->
## TOPIC 00058: Oversampling

- bundle_id: `ni-scope`
- source_path: `oversampling.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/oversampling.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: Oversampling is sampling at a rate beyond twice the highest frequency component of interest in the signal. Because real-world signals are not perfectly filtered and often contain frequency components greater than the Nyquist frequency, oversampling can be used to increase the foldover frequency so t

### Oversampling

Oversampling is sampling at a rate beyond twice the highest frequency component of 
interest in the signal. Because real-world signals are not perfectly filtered and often contain frequency components greater than the 
 Nyquist frequency, oversampling can be used to increase the 
foldover 
frequency so that these unwanted components of the signal do not alias into the passband. 
Oversampling is also necessary when trying to capture fast edges, transients, and one-time events.

Parent topic:

Sample Rate

Related concepts:

- Nyquist Theorem

<!--NI_TOPIC bundle=ni-scope path=overshoot.html language=enus -->
## TOPIC 00059: Overshoot

- bundle_id: `ni-scope`
- source_path: `overshoot.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/overshoot.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: C/C++ Equivalent: NISCOPE_VAL_OVERSHOOT The measurement is taken on the first edge of the waveform. If two edges exist, the algorithm finds the time interval from the first edge until one half the time to the second edge. The local maxima and minima are found in this interval. If only one edge is pr

### Overshoot

C/C++ Equivalent: 
NISCOPE_VAL_OVERSHOOT

The measurement is taken on the first edge of the waveform. If two edges exist, the algorithm finds the time interval from the first edge until one half the time to the second edge. The local maxima and minima are found in this interval. If only one edge is present in the waveform, the local maximum and minimum is found between the first edge and the end of the waveform.

If the first edge is positive sloped, overshoot = 100 × (local maximum - voltage high) / voltage amplitude.

If the first edge is negative sloped, overshoot = 100 × (voltage low - local minimum) / voltage amplitude.

The following figure shows an example of an overshoot measurement.

[IMAGE alt='image' src='GUID-7BD8165D-B870-4E9D-84BE-9AB6E6799C44-a5.svg']

#### Units

Percentage

Parent topic:

Scalar Measurements in NI-SCOPE

Related concepts:

- Voltage High
- Voltage Amplitude
- Voltage Low

<!--NI_TOPIC bundle=ni-scope path=pfi-lines.html language=enus -->
## TOPIC 00060: PFI Lines

- bundle_id: `ni-scope`
- source_path: `pfi-lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope/raw/resource/enus/pfi-lines.html
- document_id: `ni-scope`
- page_type: `leaf`
- content_type: `concept`
- source_description: PFI lines are multipurpose programmable function input/outputs. These lines serve as connections to virtually all internal timing signals. Many NI high-speed digitizers have two or more digital lines that can import a trigger, import or export a reference clock, or output various signals.The functio

### PFI Lines

PFI lines are multipurpose programmable function input/outputs. These lines serve as 
connections to virtually all internal timing signals. Many NI high-speed digitizers have two or more digital lines that can import a trigger, import or export a reference clock, or output various signals.

The function of each PFI line is independent. However, only one trigger source can be imported during acquisition.

Notice

Parent topic:

Integration and System Considerations
