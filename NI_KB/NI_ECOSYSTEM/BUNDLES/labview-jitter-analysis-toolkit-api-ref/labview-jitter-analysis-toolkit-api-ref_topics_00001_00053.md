# NI DOCUMENT BUNDLE: labview-jitter-analysis-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-jitter-analysis-toolkit-api-ref start=1 end=53 -->
<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/area_jittertk.html language=enus -->
## TOPIC 00001: Area VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/area_jittertk.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/area_jittertk.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Area VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the areas and mean voltages of unit intervals in a waveform. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Area (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='area.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | area sequence returns an array of the areas that cycles in the waveform occupy. |
|  | Vavg sequence returns an array of the mean values of the voltages in each cycle. In other words, these values are the sums of the voltage values divided by the measurement time in samples. Each element of Vavg sequence corresponds to an element of area sequence. |
|  | sequence timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Area (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='area.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | area sequence returns an array of the areas that cycles in the waveform occupy. |
|  | Vavg sequence returns an array of the mean values of the voltages in each cycle. In other words, these values are the sums of the voltage values divided by the measurement time in samples. Each element of Vavg sequence corresponds to an element of area sequence. |
|  | sequence timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/bathtub_plot_sup.html language=enus -->
## TOPIC 00002: Bathtub Plot Support VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/bathtub_plot_sup.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/bathtub_plot_sup.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Bathtub Plot Support VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the bit error rate at positions along the unit interval and returns a bathtub plot that represents the eye opening as a function of the bit error rate (BER). Bathtub plots are useful for showing the relationship of the sampling time in the waveform to BER.

|  | Note This VI appears on the block diagram when you add a bathtub plot to the front panel. On the Controls palette, select Addons»Jitter Analysis to navigate to the bathtub plot indicator. |
| --- | --- |

[Details](#details)

[IMAGE alt='image' src='bathtub_plot_support.gif']

|  | TB specifies the length in time of the unit interval on the x-axis of the bathtub plot. |
| --- | --- |
|  | random jitter specifies the amount of random jitter in the signal. |
|  | deterministic jitter specifies the amount of deterministic jitter in the signal. |
|  | BER limit specifies the minimum bit error rate (BER) you want to display in the bathtub plot. The default is 1E–25. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Bathtub plot returns the data you can wire to a bathtub plot indicator. |
|  | BER eye closure returns the level at which the eye becomes completely closed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Bathtub Plot Support Details

The following front panel shows how a bathtub plot illustrates the probability of a bit error occurring given the sampling time along the unit interval.

[IMAGE alt='image' src='loc_fp_bathtub.gif']

Near the level crossings, the BER is 0.5, which means there is an equal probability of an error occurring in a bit transmission. The curve is mainly flat near the level crossings because deterministic jitter, colored yellow, primarily affects signals at those positions. The BER, represented by the curve, drops sharply as the sampling point moves away from the level crossings on either end of the unit interval. These areas, colored blue, contain random jitter mechanisms. The sigma of the Gaussian processes that produce random jitter determines the BER.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/bitcount_to_bitstream.html language=enus -->
## TOPIC 00003: Bit Count to Bitstream Conversion VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/bitcount_to_bitstream.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/bitcount_to_bitstream.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Bit Count to Bitstream Conversion VI

**Owning Palette:** [Clock Recovery VIs](../lvjitterphtk/clock_recovery_pal.html)

**Requires:** Jitter Analysis Toolkit

Converts information about the number of bits between transitions in a data signal to a sequence of bits that represents the data value at each unit interval.

[IMAGE alt='image' src='bit_count_to_bitstream_conversion.gif']

|  | data contains information about the data bit sequence between transitions in a waveform. You can use the Clock Recovery (Mean Clock) VI to generate this cluster. bit count specifies the number of bits between successive transitions in the waveform. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| --- | --- |
|  | bit count specifies the number of bits between successive transitions in the waveform. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | bitstream is an array of zeros and ones that represent whether the signal is at its low or high state, respectively, during each unit interval. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/burst_width.html language=enus -->
## TOPIC 00004: Burst Width VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/burst_width.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/burst_width.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Burst Width VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the duration of each burst in a waveform, beginning when an edge in the waveform crosses a threshold level and ending when a subsequent edge crosses another threshold, with a minimum idle region on both sides of the burst. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

This VI identifies a burst as occurring when the waveform is contained within the lower or upper thresholds for at least the minimum idle time you specify, both before and after the burst.

#### Burst Width (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. To [reduce the size of the data and the memory usage](jat_overview.html#memory), Use the I8 instance of this VI with integer data.

[IMAGE alt='image' src='burst_width.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | upper threshold defines the upper level used to identify the beginnings and ends of bursts. The default is 2. |
|  | lower threshold defines the lower level used to identify the beginnings and ends of bursts. The default is –2.If the lower threshold is greater than the upper threshold value, this VI does not return an error, but LabVIEW does not identify bursts, even if they exist. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | idle time min defines the amount of time the waveform must remain between the upper threshold and lower threshold before and after part of the waveform. When that idle time occurs, this VI identifies that part of the waveform as a burst. |
|  | burst widths sequence is an array of the durations, in seconds, that bursts last. |
|  | time axis contains the time, relative to the start of the waveform, at which the waveform falls on the upper threshold or lower threshold and marks the beginning of a burst. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Burst Width (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='burst_width.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | upper threshold defines the upper level used to identify the beginnings and ends of bursts. The default is 2. |
|  | lower threshold defines the lower level used to identify the beginnings and ends of bursts. The default is –2.If the lower threshold is greater than the upper threshold value, this VI does not return an error, but LabVIEW does not identify bursts, even if they exist. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | idle time min defines the amount of time the waveform must remain between the upper threshold and lower threshold before and after part of the waveform. When that idle time occurs, this VI identifies that part of the waveform as a burst. |
|  | burst widths sequence is an array of the durations, in seconds, that bursts last. |
|  | time axis contains the time, relative to the start of the waveform, at which the waveform falls on the upper threshold or lower threshold and marks the beginning of a burst. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/chan_to_chan_skew.html language=enus -->
## TOPIC 00005: Channel-to-Channel Skew VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/chan_to_chan_skew.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/chan_to_chan_skew.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Channel-to-Channel Skew VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the time differences between corresponding level crossings in two waveforms. The difference in times is also known as delay time, or [skew](/csh?topicname=mxcncpts/skew.html).

You can use this VI to measure the response of a signal to a particular stimulus. For example, **level crossings A** might be the original signal, and **level crossings B** might be the response signal following a stimulus. You also can use this VI to compare waveforms from two different channels.

[Details](#details)

[IMAGE alt='image' src='channel_channel_skew.gif']

|  | level crossings A contains information about the locations of level crossings in a waveform. You can use the Level Crossing VI to generate this cluster from a waveform. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | level crossings B (ref) contains information about the locations of level crossings in a waveform. level crossings B (ref) serves as the reference against which this VI compares level crossings A. You can use the Level Crossing VI to generate this cluster from a waveform. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | offset specifies an amount of time, in seconds, by which to offset the locations of level crossings in level crossings B (ref). Specifying an offset allows you to more accurately match corresponding transitions in level crossings A and level crossings B (ref) when the initial times in the two waveforms are not equal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | slope specifies the direction of the transitions for which you want to return measurements. -1Falling Edge—Returns information about falling edges, or those with negative slopes.0Both—Returns information about both rising and falling edges.1Rising Edge (default)—Returns information about rising edges, or those with positive slopes. |
| -1 | Falling Edge—Returns information about falling edges, or those with negative slopes. |
| 0 | Both—Returns information about both rising and falling edges. |
| 1 | Rising Edge (default)—Returns information about rising edges, or those with positive slopes. |
|  | delay time sequence is an array of the differences, in seconds, between the times at which level crossings occur in level crossings A and the times the corresponding level crossings occur in level crossings B (ref). |
|  | delay time timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of all waveform samples that fall on the crossing level in transitions of the direction you specify in slope. This VI returns the index numbers from level crossings A. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of all waveform samples that fall on the crossing level in transitions of the direction you specify in slope. This VI returns the index numbers from level crossings A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Channel-to-Channel Skew Details

This VI uses **level crossings B (ref)** as the reference against which to measure the skew in **level crossings A**. Thus, when **level crossings A** occurs after **level crossings B (ref)**, the **delay time sequence** value is positive. When the opposite is true, the **delay time sequence** value is negative.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/clock_recovery.html language=enus -->
## TOPIC 00006: Clock Recovery (Mean Clock) VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/clock_recovery.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/clock_recovery.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Clock Recovery (Mean Clock) VI

**Owning Palette:** [Clock Recovery VIs](../lvjitterphtk/clock_recovery_pal.html)

**Requires:** Jitter Analysis Toolkit

Constructs reference level crossings from a measured waveform. The reference level crossings are synchronized to a recovered internal clock using a method that finds a best fit of the reference to the waveform level crossings. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Examples](#examples)

#### Clock Recovery (Mean Clock) (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='clock_recovery_mean_clock.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | expected unit interval specifies the time interval you expect one bit period to last. The default is –1, which means this VI calculates an estimate of the clock period to use as the unit interval. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | data returns information about the data bit sequence between transitions in the waveform. bit count returns the number of bits between successive transitions. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | bit count returns the number of bits between successive transitions. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | waveform dup returns waveform unchanged. |
|  | level crossings dup returns the level crossings unchanged. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | ref level crossings returns information about the locations of level crossings in the reference clock waveform. t0 returns the time at which the first sample occurred in the clock signal. dt returns the time interval in seconds between the individual samples in the clock signal. indexes returns the index numbers of samples in the clock signal that fall on the crossing level. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the clock signal. |
|  | dt returns the time interval in seconds between the individual samples in the clock signal. |
|  | indexes returns the index numbers of samples in the clock signal that fall on the crossing level. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | unit interval returns the best fit duration of a single bit in the waveform. |

#### Clock Recovery (Mean Clock) (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='clock_recovery_mean_clock.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | expected unit interval specifies the time interval you expect one bit period to last. The default is –1, which means this VI calculates an estimate of the clock period to use as the unit interval. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | data returns information about the data bit sequence between transitions in the waveform. bit count returns the number of bits between successive transitions. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | bit count returns the number of bits between successive transitions. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | waveform dup returns waveform unchanged. |
|  | level crossings dup returns the level crossings unchanged. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | ref level crossings returns information about the locations of level crossings in the reference clock waveform. t0 returns the time at which the first sample occurred in the clock signal. dt returns the time interval in seconds between the individual samples in the clock signal. indexes returns the index numbers of samples in the clock signal that fall on the crossing level. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the clock signal. |
|  | dt returns the time interval in seconds between the individual samples in the clock signal. |
|  | indexes returns the index numbers of samples in the clock signal that fall on the crossing level. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | unit interval returns the best fit duration of a single bit in the waveform. |

#### Examples

Refer to the following VIs for examples of using the Clock Recovery (Mean Clock) VI:

- ISI Jitter Measurement VI: labview\examples\Jitter Analysis\Jitter Measurements
- Simulated Signal with Jitter VI: labview\examples\Jitter Analysis\Jitter Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/clock_recovery_2nd_pll.html language=enus -->
## TOPIC 00007: Clock Recovery by 2nd Order PLL VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/clock_recovery_2nd_pll.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/clock_recovery_2nd_pll.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Clock Recovery by 2nd Order PLL VI

**Owning Palette:** [Clock Recovery VIs](../lvjitterphtk/clock_recovery_pal.html)

**Requires:** Jitter Analysis Toolkit

Constructs a reference clock that is synchronous with the data in a signal by using a second-order phase-locked loop (PLL) to lock the phase of an oscillator to the phase of the data edges. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Clock Recovery by 2nd Order PLL (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='clock_recovery_by_2nd_order_pll.gif']

|  | reset? specifies whether to clear the internal state of the PLL prior to starting operation. When reset? is TRUE, LabVIEW clears all state information and initializes the PLL with an initial phase of 0. When reset? is FALSE, as in a continuous operation, this VI uses the state information at the end of the previous iteration to initialize the PLL at the beginning of the current iteration. |
| --- | --- |
|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | gain specifies the loop gain. The default is 1. |
|  | damping specifies the damping factor. The default is 0.707. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VCO carrier freq (Hz) specifies the reference carrier frequency used by the voltage-controlled oscillator (VCO) to track the carrier phase of the input signal. The default is 0 Hz. |
|  | PLL waveform returns the waveform representation of the clock signal. t0 returns the start time of the waveform. dt returns the time interval in seconds between data points in the waveform. Y returns the data values of the waveform. |
|  | t0 returns the start time of the waveform. |
|  | dt returns the time interval in seconds between data points in the waveform. |
|  | Y returns the data values of the waveform. |
|  | ref level crossings returns information about the locations of level crossings in the reference clock waveform. t0 returns the time at which the first sample occurred in the clock signal. dt returns the time interval in seconds between the individual samples in the clock signal. indexes returns the index numbers of samples in the clock signal that fall on the crossing level. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the clock signal. |
|  | dt returns the time interval in seconds between the individual samples in the clock signal. |
|  | indexes returns the index numbers of samples in the clock signal that fall on the crossing level. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Clock Recovery by 2nd Order PLL (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='clock_recovery_by_2nd_order_pll.gif']

|  | reset? specifies whether to clear the internal state of the PLL prior to starting operation. When reset? is TRUE, LabVIEW clears all state information and initializes the PLL with an initial phase of 0. When reset? is FALSE, as in a continuous operation, this VI uses the state information at the end of the previous iteration to initialize the PLL at the beginning of the current iteration. |
| --- | --- |
|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | gain specifies the loop gain. The default is 1. |
|  | damping specifies the damping factor. The default is 0.707. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VCO carrier freq (Hz) specifies the reference carrier frequency used by the voltage-controlled oscillator (VCO) to track the carrier phase of the input signal. The default is 0 Hz. |
|  | PLL waveform returns the waveform representation of the clock signal. t0 returns the start time of the waveform. dt returns the time interval in seconds between data points in the waveform. Y returns the data values of the waveform. |
|  | t0 returns the start time of the waveform. |
|  | dt returns the time interval in seconds between data points in the waveform. |
|  | Y returns the data values of the waveform. |
|  | ref level crossings returns information about the locations of level crossings in the reference clock waveform. t0 returns the time at which the first sample occurred in the clock signal. dt returns the time interval in seconds between the individual samples in the clock signal. indexes returns the index numbers of samples in the clock signal that fall on the crossing level. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the clock signal. |
|  | dt returns the time interval in seconds between the individual samples in the clock signal. |
|  | indexes returns the index numbers of samples in the clock signal that fall on the crossing level. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/clock_recovery_pal.html language=enus -->
## TOPIC 00008: Clock Recovery VIs

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/clock_recovery_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/clock_recovery_pal.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Clock Recovery VIs

**Owning Palette:** [Jitter Analysis VIs](../lvjitterphtk/lvjitterphtk_pal.html)

**Requires:** Jitter Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Clock Recovery VIs to establish the timing of the reference clock from data within a signal. After you generate a reference clock signal, you can use the [Jitter](../lvjitterphtk/jitter_pal.html) VIs to compare a measured signal with the clock signal to measure jitter.

| Palette Object | Description |
| --- | --- |
| Bit Count to Bitstream Conversion | Converts information about the number of bits between transitions in a data signal to a sequence of bits that represents the data value at each unit interval. |
| Clock Recovery (Mean Clock) | Constructs reference level crossings from a measured waveform. The reference level crossings are synchronized to a recovered internal clock using a method that finds a best fit of the reference to the waveform level crossings. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Clock Recovery by 2nd Order PLL | Constructs a reference clock that is synchronous with the data in a signal by using a second-order phase-locked loop (PLL) to lock the phase of an oscillator to the phase of the data edges. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Clock Recovery by PLL Filter | Constructs a reference clock that is synchronous with the data in a signal by using a phase-locked loop (PLL) to lock the phase of an oscillator to the phase of the data edges. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Reference Bit Waveform Creation | Creates an ideal reference data waveform that is synchronized to the source waveform by using the reference crossing times to locate when the data bit changes state. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/clock_recovery_pll.html language=enus -->
## TOPIC 00009: Clock Recovery by PLL Filter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/clock_recovery_pll.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/clock_recovery_pll.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Clock Recovery by PLL Filter VI

**Owning Palette:** [Clock Recovery VIs](../lvjitterphtk/clock_recovery_pal.html)

**Requires:** Jitter Analysis Toolkit

Constructs a reference clock that is synchronous with the data in a signal by using a phase-locked loop (PLL) to lock the phase of an oscillator to the phase of the data edges. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Clock Recovery by PLL Filter (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='clock_recovery_by_pll_filter.gif']

|  | reset? specifies whether to clear the internal state of the PLL prior to starting operation. When reset? is TRUE, LabVIEW clears all state information and initializes the PLL with an initial phase of 0. When reset? is FALSE, as in a continuous operation, this VI uses the state information at the end of the previous iteration to initialize the PLL at the beginning of the current iteration. |
| --- | --- |
|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | loop filter (forward) specifies the forward coefficients of the IIR loop filter. The default is (1.05, –0.95). |
|  | loop filter (reverse) specifies the reverse coefficients of the IIR loop filter. The default is (1, –1). |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VCO carrier freq (Hz) specifies the reference carrier frequency used by the voltage-controlled oscillator (VCO) to track the carrier phase of the input signal. The default is 0 Hz. |
|  | PLL waveform returns the waveform representation of the clock signal. t0 returns the start time of the waveform. dt returns the time interval in seconds between data points in the waveform. Y returns the data values of the waveform. |
|  | t0 returns the start time of the waveform. |
|  | dt returns the time interval in seconds between data points in the waveform. |
|  | Y returns the data values of the waveform. |
|  | ref level crossings returns information about the locations of level crossings in the reference clock waveform. t0 returns the time at which the first sample occurred in the clock signal. dt returns the time interval in seconds between the individual samples in the clock signal. indexes returns the index numbers of samples in the clock signal that fall on the crossing level. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the clock signal. |
|  | dt returns the time interval in seconds between the individual samples in the clock signal. |
|  | indexes returns the index numbers of samples in the clock signal that fall on the crossing level. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Clock Recovery by PLL Filter (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='clock_recovery_by_pll_filter.gif']

|  | reset? specifies whether to clear the internal state of the PLL prior to starting operation. When reset? is TRUE, LabVIEW clears all state information and initializes the PLL with an initial phase of 0. When reset? is FALSE, as in a continuous operation, this VI uses the state information at the end of the previous iteration to initialize the PLL at the beginning of the current iteration. |
| --- | --- |
|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | loop filter (forward) specifies the forward coefficients of the IIR loop filter. The default is (1.05, –0.95). |
|  | loop filter (reverse) specifies the reverse coefficients of the IIR loop filter. The default is (1, –1). |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VCO carrier freq (Hz) specifies the reference carrier frequency used by the voltage-controlled oscillator (VCO) to track the carrier phase of the input signal. The default is 0 Hz. |
|  | PLL waveform returns the waveform representation of the clock signal. t0 returns the start time of the waveform. dt returns the time interval in seconds between data points in the waveform. Y returns the data values of the waveform. |
|  | t0 returns the start time of the waveform. |
|  | dt returns the time interval in seconds between data points in the waveform. |
|  | Y returns the data values of the waveform. |
|  | ref level crossings returns information about the locations of level crossings in the reference clock waveform. t0 returns the time at which the first sample occurred in the clock signal. dt returns the time interval in seconds between the individual samples in the clock signal. indexes returns the index numbers of samples in the clock signal that fall on the crossing level. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the clock signal. |
|  | dt returns the time interval in seconds between the individual samples in the clock signal. |
|  | indexes returns the index numbers of samples in the clock signal that fall on the crossing level. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the crossing level value at which the clock signal falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/cycle_to_cycle_jitter.html language=enus -->
## TOPIC 00010: Cycle-to-Cycle Jitter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/cycle_to_cycle_jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/cycle_to_cycle_jitter.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cycle-to-Cycle Jitter VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the differences between the amounts of [period jitter](../lvjitterphtk/period_jitter.html) in successive cycles of a waveform to show the change in period jitter from cycle to cycle.

This VI is similar to the [N Cycle Jitter](../lvjitterphtk/n_cycle_to_cycle_jitter.html) VI, except this VI always computes the differences between period jitter in adjacent cycles of the waveform.

[IMAGE alt='image' src='cycle_cycle_jitter.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | cycle-to-cycle jitter sequence returns the differences in period jitter between successive cycles in the waveform. |
|  | cycle-to-cycle jitter timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/cycle_to_cycle_meas.html language=enus -->
## TOPIC 00011: Cycle-to-Cycle Measurement VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/cycle_to_cycle_meas.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/cycle_to_cycle_meas.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cycle-to-Cycle Measurement VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the differences between consecutive elements of an array of measurements.

[Details](#details)

[IMAGE alt='image' src='cycle_to_cycle_measurement.gif']

|  | sequence contains measurements whose differences you want to compute. |
| --- | --- |
|  | timestamps describes the waveform in which the measurements occur. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of samples in the waveform from which the measurements were taken. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of samples in the waveform from which the measurements were taken. |
|  | cycle-to-cycle sequence returns the differences between the elements of the input sequence. |
|  | cycle-to-cycle timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes returns the index numbers of the measurements in the waveform. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes returns the index numbers of the measurements in the waveform. |

#### Cycle-to-Cycle Measurement Details

You can use this VI to measure cycle-to-cycle differences in the output sequences that many Jitter Analysis Toolkit VIs return. For example, you can wire the **+ width sequence** output from the [Positive Width](../lvjitterphtk/positive_width.html) VI to this VI to see how the positive widths of cycles change between successive cycles, as shown in the following block diagram.

[IMAGE alt='image' src='loc_bd_c2cmeas.gif']

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/data_dependent_jitter.html language=enus -->
## TOPIC 00012: Data Dependent Jitter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/data_dependent_jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/data_dependent_jitter.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Data Dependent Jitter VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the worst-case amounts of different types of data-dependent jitter (DDJ) from time interval error values measured in a waveform. Data-dependent jitter is a form of deterministic jitter caused by level crossing time deviations correlated to the sequence of bits. You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance to use.

[Details](#details)  [Example](#examples)

#### Data Dependent Jitter (Periodic)

Use this polymorphic instance when the **TIE sequence** was computed from a waveform that contains a sequence of bits whose period is known, or periodic. When you know the length and pattern of the bit sequence, this polymorphic instance requires less processor resources to measure the data-dependent jitter than the Arbitrary instance.

This VI divides the **TIE sequence** into segments that are **# bits** long and then averages the segments to remove the uncorrelated jitter components.

[IMAGE alt='image' src='data_dependent_jitter_periodic.gif']

|  | TIE sequence specifies the time interval error measurements from which to calculate data-dependent jitter values. You can use the Time Interval Error VI to generate these measurements. |
| --- | --- |
|  | # bits specifies the length, in bits, of the repeating sequence of time interval error values in TIE sequence. |
|  | data contains information about the data bit sequence between transitions in a waveform. You can use the Clock Recovery (Mean Clock) VI to generate this cluster. bit count specifies the number of bits between successive transitions in the waveform. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | bit count specifies the number of bits between successive transitions in the waveform. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TIE (less DDJ) sequence returns the time interval error measurements with all forms of data-dependent jitter removed. Any remaining jitter in the sequence is uncorrelated deterministic jitter or random jitter. |
|  | data dependent jitter (s p-p) returns the peak-to-peak value of the averaged time interval error values in the TIE sequence. |
|  | inter-symbol interference (s p-p) returns the peak-to-peak value of inter-symbol interference values. This output returns the greater of the peak-to-peak value of averaged time interval error in rising edges and the corresponding value for falling edges. |
|  | duty cycle distortion (s p-p) returns the peak-to-peak value of duty cycle distortion values. This VI subtracts the mean time interval error average for falling edges from the mean time interval error average for rising edges to measure the duty cycle distortion. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Data Dependent Jitter (Arbitrary)

Use this polymorphic instance when the **TIE sequence** was computed from a waveform that contains a sequence of bits that does not repeat and whose period is unknown, or arbitrary.

[IMAGE alt='image' src='data_dependent_jitter_arbitrary.gif']

|  | TIE sequence specifies the time interval error measurements from which to calculate data-dependent jitter values. You can use the Time Interval Error VI to generate these measurements. |
| --- | --- |
|  | # bits specifies the length, in bits, of the repeating sequence of time interval error values in TIE sequence. |
|  | data contains information about the data bit sequence between transitions in a waveform. You can use the Clock Recovery (Mean Clock) VI to generate this cluster. bit count specifies the number of bits between successive transitions in the waveform. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | bit count specifies the number of bits between successive transitions in the waveform. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | minimum population specifies a threshold for the number of instances a particular bit pattern must repeat for this VI to include jitter at those bits in measurements of data-dependent jitter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | data dependent jitter (s p-p) returns the peak-to-peak value of the averaged time interval error values in the TIE sequence. |
|  | inter-symbol interference (s p-p) returns the peak-to-peak value of inter-symbol interference values. This output returns the greater of the peak-to-peak value of averaged time interval error in rising edges and the corresponding value for falling edges. |
|  | duty cycle distortion (s p-p) returns the peak-to-peak value of duty cycle distortion values. This VI subtracts the mean time interval error average for falling edges from the mean time interval error average for rising edges to measure the duty cycle distortion. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | DDJ collector is an array of clusters that describe repeated bit patterns in the TIE sequence. count returns the number of times the bit pattern occurs. TIE avg returns the average time interval error value of bits in the pattern. TIE index is an array of indexes of elements in TIE sequence that exist in this bit pattern. |
|  | count returns the number of times the bit pattern occurs. |
|  | TIE avg returns the average time interval error value of bits in the pattern. |
|  | TIE index is an array of indexes of elements in TIE sequence that exist in this bit pattern. |

#### Data Dependent Jitter Details

The following pseudocode illustrates the algorithm this VI uses.

TIE<sub>avg</sub> = ensemble average TIE[k, k+1, .. K + Nb –1], yielding M waveforms M = floor(N / Nb)

TIE<sub>+avg</sub> = average of rising edges

TIE<sub>–avg</sub> = average of falling edges

data dependent jitter = P-P of TIE<sub>avg</sub>

inter-symbol interference = max [ (P-P(TIE<sub>+avg</sub>), P-P(TIE<sub>–avg</sub>) ]

duty cycle distortion = mean(TIE<sub>+avg</sub>) – mean(TIE<sub>–avg</sub>)

#### Example

Refer to the ISI Jitter Measurement VI in the labview\examples\Jitter Analysis\Jitter Measurements directory for an example of using the Data Dependent Jitter VI.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/duty_cycle_distortion.html language=enus -->
## TOPIC 00013: Duty Cycle Distortion VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/duty_cycle_distortion.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/duty_cycle_distortion.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Duty Cycle Distortion VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the duty cycle distortion in a waveform, or the amount by which the mean positive width of cycles differs from the mean negative width.

Duty cycle distortion is a type of deterministic jitter in which the clock generates positive pulses that are not equal to negative pulses.

[IMAGE alt='image' src='duty_cycle_distortion.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | slope specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | DCD (s) returns the amount by which the mean pulse duration of positive pulses differs from the mean pulse duration of negative pulses. |
|  | DCD (%) is the duty cycle distortion as a percentage of the mean cycle period. This VI computes the DCD (%) as (1/mean period × DCD (s) × 100). |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/duty_cycle_jitterphtk.html language=enus -->
## TOPIC 00014: Duty Cycle VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/duty_cycle_jitterphtk.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/duty_cycle_jitterphtk.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Duty Cycle VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the percentages of the times that cycles in a waveform occur above and below the level at which a crossing occurs. This measurement is known as the [duty cycle](/csh?topicname=measfunds/dutycycle.html), or duty factor, of the waveform.

[IMAGE alt='image' src='duty_cycle.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | + duty cycle sequence returns an array of the percentages of the time the cycles remain above the crossing level. LabVIEW calculates the value using the following equation: |
|  | - duty cycle sequence returns an array of the percentages of the time the cycles remain below the crossing level. LabVIEW calculates the value using the following equation: |
|  | sequence timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level and mark the transition of a cycle from the direction specified by rising/falling to the opposite direction. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level and mark the transition of a cycle from the direction specified by rising/falling to the opposite direction. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/eye_color_scale.html language=enus -->
## TOPIC 00015: Eye Color and Scale Generation VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/eye_color_scale.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/eye_color_scale.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eye Color and Scale Generation VI

**Owning Palette:** [Eye Diagram Measurements VIs](../lvjitterphtk/eye_diagram_pal.html)

**Requires:** Jitter Analysis Toolkit

Configures the colors you want to map to particular values in an eye diagram.

|  | Note This VI appears on the block diagram when you add an eye diagram to the front panel. On the Controls palette, select Addons»Jitter Analysis to navigate to the eye diagram indicator. |
| --- | --- |

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='eye_color_and_scale_generation.gif']

|  | eye diagram is the array of values between 0 and 1 that represent the intensity of the plot at locations in the eye diagram. Use the Eye Diagram Support VI to generate this array. |
| --- | --- |
|  | z-axis mapping specifies the scale to use to assign specific values in the eye diagram to colors. 0linear—Specifies to generate values on a logarithmic scale.1logarithmic (default)—Specifies to generate values on a linear scale. |
| 0 | linear—Specifies to generate values on a logarithmic scale. |
| 1 | logarithmic (default)—Specifies to generate values on a linear scale. |
|  | color settings is a cluster whose elements define the color scheme to use in the eye diagram. Colormap type specifies the method to use to generate colors for the eye diagram. 0single hue - dark to light (default)—Specifies to color the waveform with the hue you specify and to scale the lightness from dark at lower values to light at higher values.1rainbow hues—Specifies to color the waveform with a different hue at each value. hue is the color in which you want waveform segments to display. You can use a color box constant to supply this value. background color is the color in which you want empty areas of the eye diagram to display. You can use a color box constant to supply this value. |
|  | Colormap type specifies the method to use to generate colors for the eye diagram. 0single hue - dark to light (default)—Specifies to color the waveform with the hue you specify and to scale the lightness from dark at lower values to light at higher values.1rainbow hues—Specifies to color the waveform with a different hue at each value. |
| 0 | single hue - dark to light (default)—Specifies to color the waveform with the hue you specify and to scale the lightness from dark at lower values to light at higher values. |
| 1 | rainbow hues—Specifies to color the waveform with a different hue at each value. |
|  | hue is the color in which you want waveform segments to display. You can use a color box constant to supply this value. |
|  | background color is the color in which you want empty areas of the eye diagram to display. You can use a color box constant to supply this value. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | eye diagram dup returns the eye diagram unchanged. |
|  | MarkerVals is an array whose elements are (value, color) pairs that specify a value and the color to assign to that value when it appears in the eye diagram. Wire this cluster to the Marker Values[] property to assign colors to waveform segments in the eye diagram. value is a value to be matched with a color in the eye diagram. Color is the RGB color value to assign to locations in the eye diagram. |
|  | value is a value to be matched with a color in the eye diagram. |
|  | Color is the RGB color value to assign to locations in the eye diagram. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eye Color and Scale Generation Details

Use this VI with the [Eye Diagram Support](../lvjitterphtk/eye_diagram_support.html) VI to graph the eye diagram. The following block diagram illustrates a common workflow for the Eye Diagram Measurements VIs, including how to assign colors to values in the eye diagram:

[IMAGE alt='image' src='loc_bd_eye_support.gif']

#### Examples

Refer to the following VIs for examples of using the Eye Color and Scale Generation VI:

- Basic Eye Diagram VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Mask and Limit Test VI: labview\examples\Jitter Analysis\Eye Diagram Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/eye_diagram_pal.html language=enus -->
## TOPIC 00016: Eye Diagram Measurements VIs

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/eye_diagram_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/eye_diagram_pal.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eye Diagram Measurements VIs

**Owning Palette:** [Jitter Analysis VIs](../lvjitterphtk/lvjitterphtk_pal.html)

**Requires:** Jitter Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Eye Diagram Measurements VIs to construct an eye diagram that displays information about jitter in a waveform signal. In eye diagrams, corresponding segments of a waveform are superimposed upon each other to illustrate variations in the time at which features in the waveform occur.

[Examples](#examples)

| Palette Object | Description |
| --- | --- |
| Eye Color and Scale Generation | Configures the colors you want to map to particular values in an eye diagram. |
| Eye Data Generation | Divides a waveform into segments and returns data you can use to create an eye diagram. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Eye Diagram Support | Formats data about waveform segments and optionally, a mask and eye height and width lines, into an array of values you can plot on an eye diagram. |
| Eye Height and Width | Computes the height and width of the eye opening and adds data to the eye diagram information that allows you to plot those values in an eye diagram. You must manually select the polymorphic instance to use. |
| Eye Pattern Limit Test | Applies a mask to an eye diagram to perform limit testing on unit intervals in the diagram. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Eye Pattern Mask Definition | Defines a region, or mask, with which you want to compare unit intervals in an eye diagram to determine whether values fall within the mask you specify. Masks typically represent an area in the eye opening that you want to ensure unit intervals do not fall within. |
| Quality Factor | Measures the quality of a waveform based on the histograms at the base and top of an eye diagram formed from the waveform. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |

#### Examples

Refer to the following VIs for examples of using the Eye Diagram Measurements VIs:

- Basic Eye Diagram VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Mask and Limit Test VI: labview\examples\Jitter Analysis\Eye Diagram Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/eye_diagram_support.html language=enus -->
## TOPIC 00017: Eye Diagram Support VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/eye_diagram_support.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/eye_diagram_support.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eye Diagram Support VI

**Owning Palette:** [Eye Diagram Measurements VIs](../lvjitterphtk/eye_diagram_pal.html)

**Requires:** Jitter Analysis Toolkit

Formats data about waveform segments and optionally, a **mask** and eye height and width lines, into an array of values you can plot on an eye diagram.

|  | Note This VI appears on the block diagram when you add an eye diagram to the front panel. On the Controls palette, select Addons»Jitter Analysis to navigate to the eye diagram indicator. |
| --- | --- |

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='eye_diagram_support.gif']

|  | eye diagram data is a cluster of data that defines the eye diagram you want to plot. Note Height- and width-related cluster elements contain default data unless you use the Eye Height and Width VI before this VI to calculate those values. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
| --- | --- |
|  | Note Height- and width-related cluster elements contain default data unless you use the Eye Height and Width VI before this VI to calculate those values. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | mask defines a region in the eye diagram you want to compare with waveform segments. Use the Eye Pattern Mask Definition VI to generate this cluster. time is an array of time values at which mask boundaries intersect on the x-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. voltage is an array of voltage values at which mask boundaries intersect on the y-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. upper limit specifies the upper boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. lower limit specifies the lower boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | time is an array of time values at which mask boundaries intersect on the x-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
|  | voltage is an array of voltage values at which mask boundaries intersect on the y-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
|  | upper limit specifies the upper boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | lower limit specifies the lower boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | plot height/width, if TRUE, specifies you want to plot lines that represent the minimum height and width of the eye opening in the eye diagram. If plot height/width is TRUE but the values of height or width in the eye diagram data cluster are FALSE, this VI runs normally but does not plot height or width lines. |
|  | eye diagram returns an array of values you can wire to an eye diagram to plot the waveform segments. This array corresponds to the 2D histogram array, but the values in eye diagram are scaled to fall between 0 and 1. The numbers in the array represent the intensity of the plot in locations within the eye diagram. The indexes of the elements in the 2D array set the plot locations for the values. |
|  | x scale returns offset and multiplier values you can use to scale the eye diagram. You can use this cluster with the Offset and Multiplier property to set the offset and multiplier of the x-axis in the eye diagram. Offset is the amount by which to offset the origin of the chart or graph on the x-axis. This VI returns the value of t min as the Offset. Multiplier returns the multiplier, or interval, for scaling data using (deltaX)*X + X0. |
|  | Offset is the amount by which to offset the origin of the chart or graph on the x-axis. This VI returns the value of t min as the Offset. |
|  | Multiplier returns the multiplier, or interval, for scaling data using (deltaX)*X + X0. |
|  | y scale returns offset and multiplier values you can use to scale the eye diagram. You can use this cluster with the Offset and Multiplier property to set the offset and multiplier of the y-axis in the eye diagram. Offset is the amount by which to offset the origin of the chart or graph on the y-axis. This VI returns the value of v min as the Offset. Multiplier returns the multiplier, or interval, for scaling data using (deltaY)*Y + Y0. |
|  | Offset is the amount by which to offset the origin of the chart or graph on the y-axis. This VI returns the value of v min as the Offset. |
|  | Multiplier returns the multiplier, or interval, for scaling data using (deltaY)*Y + Y0. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eye Diagram Support Details

Before you use the Eye Diagram Support VI, use the [Eye Data Generation](../lvjitterphtk/generate_eye_data.html) VI and other Eye Diagram Measurements VIs to construct the **eye diagram data**. The following block diagram illustrates a common workflow for the Eye Diagram Measurements VIs, including how to set the scale offset and multiplier of the eye diagram.

[IMAGE alt='image' src='loc_bd_eye_support.gif']

#### Examples

Refer to the following VIs for examples of using the Eye Diagram Support VI:

- Basic Eye Diagram VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Mask and Limit Test VI: labview\examples\Jitter Analysis\Eye Diagram Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/eye_height_width.html language=enus -->
## TOPIC 00018: Eye Height and Width VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/eye_height_width.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/eye_height_width.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eye Height and Width VI

**Owning Palette:** [Eye Diagram Measurements VIs](../lvjitterphtk/eye_diagram_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the height and width of the eye opening and adds data to the eye diagram information that allows you to plot those values in an eye diagram. You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) to use.

[Details](#details)  [Examples](#examples)

#### Eye Height and Width (Statistics at Center, DBL)

Refer to the [Details](#details) section of this topic for information about how this polymorphic instance measures the eye height and width.

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='eye_height_and_width_stats.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram data in is a cluster of data that defines the eye diagram you want to plot. Use the Eye Data Generation VI to generate this cluster. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | level specifies the voltage at which to measure the eye width. |
|  | time specifies the location along the unit interval at which to measure the eye height. The default is 0.5, which means this VI measures the height halfway along the unit interval. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | eye diagram data out is a cluster of data that defines the eye diagram with height and width measurements added. segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval returns the unit interval unchanged. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level returns the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index number within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index number within the original waveform of the last sample in the waveform segment. |
|  | ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval returns the unit interval unchanged. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level returns the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | height returns the height of the eye opening. Refer to the Details section for more information about how this VI calculates the height value. |
|  | width returns the width of the eye opening. Refer to the Details section for more information about how this VI calculates the width value. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | crossing percent measures the amplitude of the level crossings as a fraction of the mean values above and below the crossing level. |

#### Eye Height and Width (Statistics at Center, I8)

Refer to the [Details](#details) section of this topic for information about how this polymorphic instance measures the eye height and width.

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='eye_height_and_width_stats.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram data in is a cluster of data that defines the eye diagram you want to plot. Use the Eye Data Generation VI to generate this cluster. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | level specifies the voltage at which to measure the eye width. |
|  | time specifies the location along the unit interval at which to measure the eye height. The default is 0.5, which means this VI measures the height halfway along the unit interval. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | eye diagram data out is a cluster of data that defines the eye diagram with height and width measurements added. segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval returns the unit interval unchanged. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level returns the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index number within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index number within the original waveform of the last sample in the waveform segment. |
|  | ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval returns the unit interval unchanged. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level returns the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | height returns the height of the eye opening. Refer to the Details section for more information about how this VI calculates the height value. |
|  | width returns the width of the eye opening. Refer to the Details section for more information about how this VI calculates the width value. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | crossing percent measures the amplitude of the level crossings as a fraction of the mean values above and below the crossing level. |

#### Eye Height and Width (Max at Center, DBL)

Refer to the [Details](#details) section of this topic for information about how this polymorphic instance measures the eye height and width.

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='eye_height_and_width_center.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram data in is a cluster of data that defines the eye diagram you want to plot. Use the Eye Data Generation VI to generate this cluster. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | level specifies the voltage at which to measure the eye width. |
|  | time specifies the location along the unit interval at which to measure the eye height. The default is 0.5, which means this VI measures the height halfway along the unit interval. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | eye diagram data out is a cluster of data that defines the eye diagram with height and width measurements added. segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval returns the unit interval unchanged. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level returns the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index number within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index number within the original waveform of the last sample in the waveform segment. |
|  | ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval returns the unit interval unchanged. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level returns the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | height returns the height of the eye opening. Refer to the Details section for more information about how this VI calculates the height value. |
|  | width returns the width of the eye opening. Refer to the Details section for more information about how this VI calculates the width value. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | crossing percent measures the amplitude of the level crossings as a fraction of the mean values above and below the crossing level. |

#### Eye Height and Width (Max at Center, I8)

Refer to the [Details](#details) section of this topic for information about how this polymorphic instance measures the eye height and width.

[IMAGE alt='image' src='eye_height_and_width_center.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram data in is a cluster of data that defines the eye diagram you want to plot. Use the Eye Data Generation VI to generate this cluster. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | level specifies the voltage at which to measure the eye width. |
|  | time specifies the location along the unit interval at which to measure the eye height. The default is 0.5, which means this VI measures the height halfway along the unit interval. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | eye diagram data out is a cluster of data that defines the eye diagram with height and width measurements added. segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval returns the unit interval unchanged. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level returns the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index number within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index number within the original waveform of the last sample in the waveform segment. |
|  | ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval returns the unit interval unchanged. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level returns the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | height returns the height of the eye opening. Refer to the Details section for more information about how this VI calculates the height value. |
|  | width returns the width of the eye opening. Refer to the Details section for more information about how this VI calculates the width value. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | crossing percent measures the amplitude of the level crossings as a fraction of the mean values above and below the crossing level. |

#### Eye Height and Width (Search for Max)

Refer to the [Details](#details) section of this topic for information about how this polymorphic instance measures the eye height and width.

[IMAGE alt='image' src='eye_height_and_width_search.gif']

|  | eye diagram data in is a cluster of data that defines the eye diagram you want to plot. Use the Eye Data Generation VI to generate this cluster. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
| --- | --- |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | eye diagram data out is a cluster of data that defines the eye diagram with height and width measurements added. segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval returns the unit interval unchanged. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level returns the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. end idx is the index number within the original waveform of the last sample in the waveform segment. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index number within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index number within the original waveform of the last sample in the waveform segment. |
|  | ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval returns the unit interval unchanged. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurement occurs. This VI calculates the height time as the product of (unit interval × time). |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level returns the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | height returns the height of the eye opening. Refer to the Details section for more information about how this VI calculates the height value. |
|  | width returns the width of the eye opening. Refer to the Details section for more information about how this VI calculates the width value. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | crossing percent measures the amplitude of the level crossings as a fraction of the mean values above and below the crossing level. |

#### Eye Height and Width Details

Before you use the Eye Diagram Height and Width VI, use the [Eye Data Generation](../lvjitterphtk/generate_eye_data.html) VI to construct the **eye diagram data in** cluster. The following block diagram illustrates a common workflow for the Eye Diagram Measurements VIs.

[IMAGE alt='image' src='loc_bd_eye_support.gif']

#### Statistics at Center Polymorphic Instance

The Statistics at Center polymorphic instance does not calculate the eye height and width from the maximum eye opening. This VI measures the eye **height** as the difference between the inner 3[IMAGE alt='image' src='sigma.gif'] points on the inside of histograms of the voltage values on the y-axis. The **top** and **base** elements in **eye diagram data out** correspond to those inner 3[IMAGE alt='image' src='sigma.gif'] points. Similarly, this VI measures the eye **width** as the difference between the inner 3[IMAGE alt='image' src='sigma.gif'] points on the inside of histograms of level crossings times placed on the x-axis. In the case of width, the **left** and **right** cluster elements correspond to those inner 3[IMAGE alt='image' src='sigma.gif'] points.

The following front panel shows an eye diagram with the height and width this polymorphic instance calculates plotted.

[IMAGE alt='image' src='loc_fp_eye_hw.gif']

#### Max at Center Polymorphic Instance

The Max at Center polymorphic instance measures the eye height as the difference of the lowest voltage at the top of the eye opening and the highest voltage at the base of the opening at the x-axis **time** you specify. This instance measures eye width as the difference of the lowest time value at the right of the eye opening and the highest time value at the left of the opening at the y-axis **level** you specify.

#### Search for Max Polymorphic Instance

The Search for Max polymorphic instance searches for the maximum eye opening and from its center, measures the eye height as the difference of the lowest voltage at the top of the opening and the highest voltage at the base of the opening. This instance measures the eye width as the difference of the lowest time value at the right of the opening and the highest time value at the left of the opening as measured from the center of the eye.

#### Examples

Refer to the following VIs for examples of using the Eye Height and Width VI:

- Basic Eye Diagram VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Basic Eye Diagram with Colormap Explorer VI: labview\examples\Jitter Analysis\Eye Diagram Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/eye_pattern_limit_test.html language=enus -->
## TOPIC 00019: Eye Pattern Limit Test VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/eye_pattern_limit_test.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/eye_pattern_limit_test.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eye Pattern Limit Test VI

**Owning Palette:** [Eye Diagram Measurements VIs](../lvjitterphtk/eye_diagram_pal.html)

**Requires:** Jitter Analysis Toolkit

Applies a mask to an eye diagram to perform limit testing on unit intervals in the diagram. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

Use the [Eye Data Generation](../lvjitterphtk/generate_eye_data.html) VI to generate the **eye diagram data** to which you want to apply the mask. Use the [Eye Pattern Mask Definition](../lvjitterphtk/eye_pattern_mask_def.html) VI to define the **mask** you want to apply to the eye diagram. Refer to the [Details](#details) section of this topic for more information about using this VI with the rest of the Eye Diagram Measurements VIs.

[Details](#details)  [Example](#examples)

#### Eye Pattern Limit Test (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='eye_pattern_limit_test.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram data is a cluster of data that defines the eye diagram you want to plot. Note Height- and width-related cluster elements contain default data unless you use the Eye Height and Width VI before this VI to calculate those values. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | Note Height- and width-related cluster elements contain default data unless you use the Eye Height and Width VI before this VI to calculate those values. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | mask defines a region in the eye diagram you want to compare with waveform segments. Use the Eye Pattern Mask Definition VI to generate this cluster. time is an array of time values at which mask boundaries intersect on the x-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. voltage is an array of voltage values at which mask boundaries intersect on the y-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. upper limit specifies the upper boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. lower limit specifies the lower boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | time is an array of time values at which mask boundaries intersect on the x-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
|  | voltage is an array of voltage values at which mask boundaries intersect on the y-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
|  | upper limit specifies the upper boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | lower limit specifies the lower boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | failed returns the number of samples in the waveform that fall inside the mask region or that violate the upper limit or lower limit you specify. |
|  | total number returns the total number of samples in the waveform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eye Pattern Limit Test (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='eye_pattern_limit_test.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram data is a cluster of data that defines the eye diagram you want to plot. Note Height- and width-related cluster elements contain default data unless you use the Eye Height and Width VI before this VI to calculate those values. segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval is the time between level crossings in the eye diagram. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurements occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level specifies the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | Note Height- and width-related cluster elements contain default data unless you use the Eye Height and Width VI before this VI to calculate those values. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. start idx is the index within the original waveform of the first sample in the waveform segment. end idx is the index within the original waveform of the last sample in the waveform segment. ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index within the original waveform of the first sample in the waveform segment. |
|  | end idx is the index within the original waveform of the last sample in the waveform segment. |
|  | ref crossing specifies the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval is the time between level crossings in the eye diagram. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurements occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level specifies the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations within the eye diagram. |
|  | mask defines a region in the eye diagram you want to compare with waveform segments. Use the Eye Pattern Mask Definition VI to generate this cluster. time is an array of time values at which mask boundaries intersect on the x-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. voltage is an array of voltage values at which mask boundaries intersect on the y-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. upper limit specifies the upper boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. lower limit specifies the lower boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | time is an array of time values at which mask boundaries intersect on the x-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
|  | voltage is an array of voltage values at which mask boundaries intersect on the y-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
|  | upper limit specifies the upper boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | lower limit specifies the lower boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | failed returns the number of samples in the waveform that fall inside the mask region or that violate the upper limit or lower limit you specify. |
|  | total number returns the total number of samples in the waveform. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eye Pattern Limit Test Details

The following block diagram illustrates a common workflow for using this VI to perform limit testing.

[IMAGE alt='image' src='loc_bd_eye_limit_test.gif']

#### Example

Refer to the Mask and Limit Test VI in the labview\examples\Jitter Analysis\Eye Diagram Measurements directory for an example of using the Eye Pattern Limit Test VI.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/eye_pattern_mask_def.html language=enus -->
## TOPIC 00020: Eye Pattern Mask Definition VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/eye_pattern_mask_def.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/eye_pattern_mask_def.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eye Pattern Mask Definition VI

**Owning Palette:** [Eye Diagram Measurements VIs](../lvjitterphtk/eye_diagram_pal.html)

**Requires:** Jitter Analysis Toolkit

Defines a region, or mask, with which you want to compare unit intervals in an eye diagram to determine whether values fall within the mask you specify. Masks typically represent an area in the eye opening that you want to ensure unit intervals do not fall within.

Use the [Eye Pattern Limit Test](../lvjitterphtk/eye_pattern_limit_test.html) VI to compare a signal in an eye diagram to the **mask** this VI generates and perform limit testing. Refer to the [Details](#details) section of this topic for more information about using this VI with the rest of the Eye Diagram Measurements VIs.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='eye_pattern_mask_definition.gif']

|  | time is an array of time values at which mask boundaries intersect on the x-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
| --- | --- |
|  | voltage is an array of voltage values at which mask boundaries intersect on the y-axis. (time, voltage) values at the same indexes define the mask-boundary intersections. |
|  | upper limit specifies the upper boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | lower limit specifies the lower boundary of the mask you want to apply to voltage values to determine whether the signal falls in the mask. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | mask out returns the input values as a cluster that defines the mask against which you want to test the waveform. Pass this cluster to the Eye Pattern Limit Test VI to perform limit testing, or to the Eye Diagram Support VI to plot the mask in the eye diagram. This VI draws lines between (time, voltage) pairs to define the mask boundaries and reorders the pairs to reflect the order in which the VI draws lines between start and end points. This VI also duplicates the (time, voltage) point at the origin of the mask because the VI must draw a line between the final point and the origin to close the mask. time is an array of time values at which mask boundaries intersect on the x-axis. voltage is an array of time values that define the positions where mask boundaries intersect. Each y-axis value in voltage corresponds to the x-axis value at the same index in the time output. upper limit returns upper limit unchanged. lower limit returns lower limit unchanged. |
|  | time is an array of time values at which mask boundaries intersect on the x-axis. |
|  | voltage is an array of time values that define the positions where mask boundaries intersect. Each y-axis value in voltage corresponds to the x-axis value at the same index in the time output. |
|  | upper limit returns upper limit unchanged. |
|  | lower limit returns lower limit unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eye Pattern Mask Definition Details

The following block diagram illustrates a common workflow for using this VI to define a mask for use in limit testing.

[IMAGE alt='image' src='loc_bd_eye_limit_test.gif']

#### Example

Refer to the Mask and Limit Test VI in the labview\examples\Jitter Analysis\Eye Diagram Measurements directory for an example of using the Eye Pattern Mask Definition VI.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/fall_time.html language=enus -->
## TOPIC 00021: Fall Time VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/fall_time.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/fall_time.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Fall Time VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the transition duration of falling transitions in a waveform. The duration of a falling transition, or fall time, is the difference in time between its **start index** and **end index**. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Fall Time (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='fall_time.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | fall time sequence is an array of the durations, in seconds, between the beginning and end of each falling transition. |
|  | fall time timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Fall Time (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='fall_time.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | fall time sequence is an array of the durations, in seconds, between the beginning and end of each falling transition. |
|  | fall time timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Fall Time Details

A rising transition duration is known as rise time, and a falling transition duration is known as fall time, as shown in the following example:

[IMAGE alt='image' src='loc_eps_rftimex.gif']

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/find_transitions.html language=enus -->
## TOPIC 00022: Find Transitions VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/find_transitions.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/find_transitions.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Find Transitions VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the boundaries and directions of each transition in a waveform given the reference levels you specify. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

Refer to the [Details](#details) section of this topic for more information about how this VI identifies transitions.

You can use the transition information this VI generates to perform measurements such as the [overshoot](../lvjitterphtk/overshoot_and_undershoot.html), [rise time](../lvjitterphtk/rise_time.html), and [fall time](../lvjitterphtk/fall_time.html) of waveform transitions.

[Details](#details)  [Examples](#examples)

#### Find Transitions (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='find_transitions.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. You can use the State Levels or Reference Levels VIs to generate this cluster. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | reference levels specifies the high, middle, and low reference levels of a waveform. You can use the Reference Levels VI to generate this cluster. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | transitions returns information about the transitions in the waveform. transition is an array of clusters that describe the boundaries and direction of each transition in waveform. start index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition begins. If the slope of the transition is Rising Edge, the start index is where the signal crosses the low ref level. If the slope is Falling Edge, the start index is where the signal crosses the high ref level. end index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition ends. If the slope of the transition is Rising Edge, the end index is where the signal crosses the high ref level. If the slope is Falling Edge, the end index is where the signal crosses the low ref level. slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state ref levels returns the three reference levels of the waveform in absolute units. LabVIEW uses the reference levels to define the interval of one cycle measurement. high ref level returns the high reference level. mid ref level returns the middle reference level. low ref level returns the low reference level. |
|  | transition is an array of clusters that describe the boundaries and direction of each transition in waveform. start index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition begins. If the slope of the transition is Rising Edge, the start index is where the signal crosses the low ref level. If the slope is Falling Edge, the start index is where the signal crosses the high ref level. end index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition ends. If the slope of the transition is Rising Edge, the end index is where the signal crosses the high ref level. If the slope is Falling Edge, the end index is where the signal crosses the low ref level. slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
|  | start index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition begins. If the slope of the transition is Rising Edge, the start index is where the signal crosses the low ref level. If the slope is Falling Edge, the start index is where the signal crosses the high ref level. |
|  | end index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition ends. If the slope of the transition is Rising Edge, the end index is where the signal crosses the high ref level. If the slope is Falling Edge, the end index is where the signal crosses the low ref level. |
|  | slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
|  | state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels returns the three reference levels of the waveform in absolute units. LabVIEW uses the reference levels to define the interval of one cycle measurement. high ref level returns the high reference level. mid ref level returns the middle reference level. low ref level returns the low reference level. |
|  | high ref level returns the high reference level. |
|  | mid ref level returns the middle reference level. |
|  | low ref level returns the low reference level. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Find Transitions (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='find_transitions.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. You can use the State Levels or Reference Levels VIs to generate this cluster. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | reference levels specifies the high, middle, and low reference levels of a waveform. You can use the Reference Levels VI to generate this cluster. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | transitions returns information about the transitions in the waveform. transition is an array of clusters that describe the boundaries and direction of each transition in waveform. start index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition begins. If the slope of the transition is Rising Edge, the start index is where the signal crosses the low ref level. If the slope is Falling Edge, the start index is where the signal crosses the high ref level. end index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition ends. If the slope of the transition is Rising Edge, the end index is where the signal crosses the high ref level. If the slope is Falling Edge, the end index is where the signal crosses the low ref level. slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state ref levels returns the three reference levels of the waveform in absolute units. LabVIEW uses the reference levels to define the interval of one cycle measurement. high ref level returns the high reference level. mid ref level returns the middle reference level. low ref level returns the low reference level. |
|  | transition is an array of clusters that describe the boundaries and direction of each transition in waveform. start index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition begins. If the slope of the transition is Rising Edge, the start index is where the signal crosses the low ref level. If the slope is Falling Edge, the start index is where the signal crosses the high ref level. end index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition ends. If the slope of the transition is Rising Edge, the end index is where the signal crosses the high ref level. If the slope is Falling Edge, the end index is where the signal crosses the low ref level. slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
|  | start index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition begins. If the slope of the transition is Rising Edge, the start index is where the signal crosses the low ref level. If the slope is Falling Edge, the start index is where the signal crosses the high ref level. |
|  | end index is the index of the sample at which the signal crosses the high ref level or low ref level and the transition ends. If the slope of the transition is Rising Edge, the end index is where the signal crosses the high ref level. If the slope is Falling Edge, the end index is where the signal crosses the low ref level. |
|  | slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
|  | state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels returns the three reference levels of the waveform in absolute units. LabVIEW uses the reference levels to define the interval of one cycle measurement. high ref level returns the high reference level. mid ref level returns the middle reference level. low ref level returns the low reference level. |
|  | high ref level returns the high reference level. |
|  | mid ref level returns the middle reference level. |
|  | low ref level returns the low reference level. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Find Transitions Details

This VI identifies transition boundaries by locating a level crossing in the waveform, and then finding the nearest reference level crossing on each side of the crossing. In other words, this VI identifies transitions as in the following descriptions:

- This VI identifies falling transitions by finding all portions of the waveform that cross the high reference level and then cross the low reference level from above with no other high or low reference crossings in between.
- This VI identifies rising transitions by finding all portions of the waveform that cross the low reference level and then cross the high reference level from below with no other high or low reference crossings in between.

#### Examples

Refer to the following VIs for examples of using the Find Transitions VI:

- Mask and Limit Test VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Overshoot Demo VI: labview\examples\Jitter Analysis\Level Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/generate_eye_data.html language=enus -->
## TOPIC 00023: Eye Data Generation VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/generate_eye_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/generate_eye_data.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eye Data Generation VI

**Owning Palette:** [Eye Diagram Measurements VIs](../lvjitterphtk/eye_diagram_pal.html)

**Requires:** Jitter Analysis Toolkit

Divides a waveform into segments and returns data you can use to create an eye diagram. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

Refer to the [Details](#details) section of this topic for information about using this VI to plot a waveform in an eye diagram.

[Details](#details)  [Examples](#examples)

#### Eye Data Generation (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='eye_data_generation.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram resolution contains controls you can use to set the resolution of the eye diagram data. bins on time specifies the number of intervals into which you want to group time values on the x-axis. bins on voltage specifies the number of intervals into which you want to group voltage values on the y-axis. |
|  | bins on time specifies the number of intervals into which you want to group time values on the x-axis. |
|  | bins on voltage specifies the number of intervals into which you want to group voltage values on the y-axis. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | unit interval is the best fit duration of a single bit in the waveform. You can use the Clock Recovery (Mean Clock) VI to generate this value. |
|  | percent overlap specifies the amount of previous and subsequent unit intervals to include in each segment to be plotted. The default is 50 percent. |
|  | waveform dup returns waveform unchanged. |
|  | eye diagram data is a cluster of data that defines the eye diagram you want to plot. Note Height- and width-related cluster elements contain default data because this VI does not measure those values. Use this cluster with the Eye Height and Width VI to calculates those values. segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. The start idx of the segment that contains a particular unit interval is the sample in the previous unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the start idx as the sample halfway into the previous unit interval. end idx is the index number within the original waveform of the last sample in the waveform segment. The end idx of the segment that contains a particular unit interval is the sample in the following unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the end idx as the sample halfway into the next unit interval. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval returns the unit interval unchanged. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurement occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level returns the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | Note Height- and width-related cluster elements contain default data because this VI does not measure those values. Use this cluster with the Eye Height and Width VI to calculates those values. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. The start idx of the segment that contains a particular unit interval is the sample in the previous unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the start idx as the sample halfway into the previous unit interval. end idx is the index number within the original waveform of the last sample in the waveform segment. The end idx of the segment that contains a particular unit interval is the sample in the following unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the end idx as the sample halfway into the next unit interval. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index number within the original waveform of the first sample in the waveform segment. The start idx of the segment that contains a particular unit interval is the sample in the previous unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the start idx as the sample halfway into the previous unit interval. |
|  | end idx is the index number within the original waveform of the last sample in the waveform segment. The end idx of the segment that contains a particular unit interval is the sample in the following unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the end idx as the sample halfway into the next unit interval. |
|  | ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval returns the unit interval unchanged. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurement occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level returns the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eye Data Generation (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='eye_data_generation.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | eye diagram resolution contains controls you can use to set the resolution of the eye diagram data. bins on time specifies the number of intervals into which you want to group time values on the x-axis. bins on voltage specifies the number of intervals into which you want to group voltage values on the y-axis. |
|  | bins on time specifies the number of intervals into which you want to group time values on the x-axis. |
|  | bins on voltage specifies the number of intervals into which you want to group voltage values on the y-axis. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | unit interval is the best fit duration of a single bit in the waveform. You can use the Clock Recovery (Mean Clock) VI to generate this value. |
|  | percent overlap specifies the amount of previous and subsequent unit intervals to include in each segment to be plotted. The default is 50 percent. |
|  | waveform dup returns waveform unchanged. |
|  | eye diagram data is a cluster of data that defines the eye diagram you want to plot. Note Height- and width-related cluster elements contain default data because this VI does not measure those values. Use this cluster with the Eye Height and Width VI to calculates those values. segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. The start idx of the segment that contains a particular unit interval is the sample in the previous unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the start idx as the sample halfway into the previous unit interval. end idx is the index number within the original waveform of the last sample in the waveform segment. The end idx of the segment that contains a particular unit interval is the sample in the following unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the end idx as the sample halfway into the next unit interval. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. t min is the initial time in the eye diagram. t max is the final time in the eye diagram. v min is the minimum voltage value in the eye diagram. v max is the maximum voltage value in the eye diagram. unit interval returns the unit interval unchanged. height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. height time is the time at which the height measurement occurs. top is the upper voltage level of the eye opening. base is the lower voltage level of the eye opening. width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. crossing level returns the voltage at which the eye width measurement occurs. left is the lower time value of the eye opening. right is the upper time value of the eye opening. 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | Note Height- and width-related cluster elements contain default data because this VI does not measure those values. Use this cluster with the Eye Height and Width VI to calculates those values. |
|  | segments is an array of values that define portions of the waveform to plot in the eye diagram. Each segment contains one unit interval that is preceded and followed by portions of adjacent unit intervals. start idx is the index number within the original waveform of the first sample in the waveform segment. The start idx of the segment that contains a particular unit interval is the sample in the previous unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the start idx as the sample halfway into the previous unit interval. end idx is the index number within the original waveform of the last sample in the waveform segment. The end idx of the segment that contains a particular unit interval is the sample in the following unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the end idx as the sample halfway into the next unit interval. ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | start idx is the index number within the original waveform of the first sample in the waveform segment. The start idx of the segment that contains a particular unit interval is the sample in the previous unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the start idx as the sample halfway into the previous unit interval. |
|  | end idx is the index number within the original waveform of the last sample in the waveform segment. The end idx of the segment that contains a particular unit interval is the sample in the following unit interval that corresponds to the percent overlap you specify. For example, if percent overlap is 50, this VI sets the end idx as the sample halfway into the next unit interval. |
|  | ref crossing returns the index number of the sample between start index and end index whose value falls at the crossing level. |
|  | t min is the initial time in the eye diagram. |
|  | t max is the final time in the eye diagram. |
|  | v min is the minimum voltage value in the eye diagram. |
|  | v max is the maximum voltage value in the eye diagram. |
|  | unit interval returns the unit interval unchanged. |
|  | height is TRUE if this cluster contains values that define the height of the eye opening. If height is FALSE, height time, top, and base contain default data. |
|  | height time is the time at which the height measurement occurs. |
|  | top is the upper voltage level of the eye opening. |
|  | base is the lower voltage level of the eye opening. |
|  | width is TRUE if this cluster contains values that define the width of the eye opening. If width is FALSE, crossing level, left, and right contain default data. |
|  | crossing level returns the voltage at which the eye width measurement occurs. |
|  | left is the lower time value of the eye opening. |
|  | right is the upper time value of the eye opening. |
|  | 2D histogram is a 2D array of values that represent the magnitude at locations in the eye diagram. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eye Data Generation Details

Use this VI with the [Eye Diagram Support](../lvjitterphtk/eye_diagram_support.html) VI to graph the eye diagram. The following block diagram illustrates a common workflow for the Eye Diagram Measurements VIs.

[IMAGE alt='image' src='loc_bd_eye_support.gif']

#### Examples

Refer to the following VIs for examples of using the Eye Data Generation VI:

- Basic Eye Diagram VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Mask and Limit Test VI: labview\examples\Jitter Analysis\Eye Diagram Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/jat_overview.html language=enus -->
## TOPIC 00024: Measuring Jitter in Signals (Jitter Analysis Toolkit)

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/jat_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/jat_overview.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Measuring Jitter in Signals (Jitter Analysis Toolkit)

When you measure jitter in signals, you typically perform a common set of tasks to acquire and analyze the signal data. The sections that follow describe steps in a basic jitter-measurement application and the VIs the [Jitter Analysis Toolkit](../lvjitterphtk/lvjitterphtk_pal.html) provides to perform the steps.

The following block diagram shows a common workflow for using the Jitter Analysis Toolkit to analyze jitter in a waveform.

[IMAGE alt='image' src='loc_bd_jat_overview.gif']

#### Acquiring Waveform Data

If you want to perform automated testing of signals, stream data from hardware using drivers appropriate for your device. If you want to perform measurements on signal data saved to disk, you can read the data from file using functions appropriate for the file format you are using. For example, you can use the [TDM Streaming](/csh?topicname=glang/tdm_streaming_functions.html) VIs and functions to read waveform data from a .tdms file. You can use the [Storage/DataPlugin](/csh?topicname=glang/storage_vis.html) VIs to read measurement data from a variety of file formats.

##### Managing Memory and Performance

Depending on how you acquire waveform data, the **Y** data values that are part of the [waveform data type](/csh?topicname=lvconcepts/types_of_graphs_and_charts.html) might be double-precision, floating-point numeric values or 8-bit signed integers. Analyzing waveforms represented by integers reduces the size of the data you must analyze, which requires less memory. Many VIs in the Jitter Analysis Toolkit can operate on the waveform data type when it contains double-precision floating-point data *or* 8-bit signed integers.

#### Measuring State and Reference Levels

After reading in waveform data, establish [state and reference levels](/csh?topicname=lvwave/state_and_reference_levels.html) that allow you to identify repeating waveform features. For example, after you set a low reference level, you can identify each waveform sample that falls at that voltage level and the time at which it occurs in the waveform. High and low state levels define the voltages at which the signal is at its highest and lowest states. Reference levels fall within the state levels, often as percentages of the state-level amplitude, and allow you to identify features of waveform transitions. The high, mid, and low reference levels are typically 90%, 50%, and 10%, respectively, of the state-level amplitude.

You can use the [State Levels](../lvjitterphtk/state_levels.html) VI with the [Reference Levels](../lvjitterphtk/reference_levels.html) VI to measure these levels for a waveform, or you can use only the Reference Levels (waveform in) polymorphic instance to measure all levels.

#### Identifying Transitions and Level Crossings

As mentioned previously, high and low reference levels identify transitions in a waveform between its high and low states. Transitions are also the waveform features in which jitter, deviation from the clock signal, is typically measured. When you identify transitions, you also reduce the total data you must analyze, which requires less processor resources.

After isolating the transitions in a waveform, it is useful to further reduce the data with which you are working to a single, common voltage value within each transition so you can measure time differences at that one point. This common voltage value is referred to as a crossing level. Applications typically use the 50% mid reference level as the value at which to identify level crossings.

Use the [Level Crossing](../lvjitterphtk/level_crossing.html) VI to measure transitions in a waveform and return the locations at which level crossings within the transitions occur.

#### Recovering the Clock Signal

With level crossings identified in each transition, you must compare their locations in time to the times at which the corresponding crossings occur in the reference clock waveform. The reference clock triggers the transitions in the measured waveform, so you can consider the clock signal to represent the ideal state of the waveform. Use the [Clock Recovery](../lvjitterphtk/clock_recovery_pal.html) VIs to recover the level crossings in the reference clock waveform from a measured waveform.

#### Measuring and Analyzing Jitter

After you identify level crossings in both a waveform and the corresponding reference clock waveform, you can use [Jitter](../lvjitterphtk/jitter_pal.html) VIs to measure the following types of jitter:

- Time interval error —Time differences of level crossings in a waveform and the level crossings from the reference clock.
- Period jitter —Differences between cycle durations in a waveform and the corresponding cycle durations from the reference clock.
- Cycle-to-cycle jitter —Differences between the amounts of period jitter in successive cycles of a waveform.

The previous VIs return jitter sequence arrays, where each element is a jitter value at a level crossing. You can use the [Probability & Statistics](/csh?topicname=gmath/prob_and_statistics_vis.html) VIs with the jitter sequences that many of the VIs on this palette return to perform probability, descriptive statistics, analysis of variance, and interpolation functions.

##### Separating Jitter Components

With jitter sequences, you then can calculate the amounts of random jitter, deterministic jitter, and total jitter in the signal as a whole, rather than jitter at each level crossing. You also can separate deterministic jitter into periodic jitter and data-dependent jitter. The [Jitter](../lvjitterphtk/jitter_pal.html) palette contains VIs that separate components of jitter.

##### Creating Eye Diagrams

Use the [Eye Diagram Measurements](../lvjitterphtk/eye_diagram_pal.html) VIs to construct an eye diagram that displays information about jitter in a waveform signal. In eye diagrams, corresponding segments of a waveform are superimposed upon each other to illustrate variations in the time at which features in the waveform occur.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/jitter_pal.html language=enus -->
## TOPIC 00025: Jitter VIs

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/jitter_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/jitter_pal.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Jitter VIs

**Owning Palette:** [Jitter Analysis VIs](../lvjitterphtk/lvjitterphtk_pal.html)

**Requires:** Jitter Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Jitter VIs to measure the jitter in a waveform and separate, or decompose, it into components, such as random jitter, deterministic jitter, and so on. When separated, the individual components of jitter can indicate causes of excessive jitter in the system.

[Example](#examples)

You can use the [Probability & Statistics](/csh?topicname=gmath/prob_and_statistics_vis.html) VIs with the jitter sequences that many of the VIs on this palette return to perform probability, descriptive statistics, analysis of variance, and interpolation functions.

| Palette Object | Description |
| --- | --- |
| Bathtub Plot Support | Computes the bit error rate at positions along the unit interval and returns a bathtub plot that represents the eye opening as a function of the bit error rate (BER). Bathtub plots are useful for showing the relationship of the sampling time in the waveform to BER. |
| Cycle-to-Cycle Jitter | Computes the differences between the amounts of period jitter in successive cycles of a waveform to show the change in period jitter from cycle to cycle. |
| Cycle-to-Cycle Measurement | Computes the differences between consecutive elements of an array of measurements. |
| Data Dependent Jitter | Computes the worst-case amounts of different types of data-dependent jitter (DDJ) from time interval error values measured in a waveform. Data-dependent jitter is a form of deterministic jitter caused by level crossing time deviations correlated to the sequence of bits. You must manually select the polymorphic instance to use. |
| Duty Cycle Distortion | Measures the duty cycle distortion in a waveform, or the amount by which the mean positive width of cycles differs from the mean negative width. |
| N Cycle Jitter | Computes the differences in the amounts of jitter between cycles of a waveform, which indicates the change in jitter at different locations in the waveform. |
| N Cycle Measurement | Computes the differences between elements in an array of measurements at the interval you specify. |
| N Period Jitter | Measures the differences between period times from a waveform and the corresponding ideal periods from the reference clock. |
| Period Jitter | Measures the differences between cycle durations in a waveform and the corresponding cycle durations from the reference clock. |
| Phase Noise | Converts a jitter sequence into the frequency domain and measures the RMS value integrated between two frequencies. |
| RJ PJ Separation | Separates the random and periodic components of jitter in a jitter sequence and returns their RMS and peak-to-peak values. |
| Time Interval Error | Measures the differences between the positions in time of waveform level crossings and the times at which the corresponding level crossings occur in the reference clock. |
| Total Jitter | Computes the total jitter for the random and deterministic jitter levels you specify. The total jitter value is the amount of jitter that has a probability of being exceeded equal to the BER limit you specify. |

#### Example

Refer to the Rj Dj Delta Delta Separation VI in the labview\examples\Jitter Analysis\Jitter Measurements directory for an example of using the Jitter VIs.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/level_crossing.html language=enus -->
## TOPIC 00026: Level Crossing VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/level_crossing.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/level_crossing.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Level Crossing VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the times and locations a waveform crosses a particular voltage level. The Jitter Analysis VIs use **level crossings** to identify a common position in all transitions that you can use for comparison. Wire data to the **transitions** input and the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

This VI uses linear interpolation of the waveform points in transition regions to locate the precise crossing times. If the signal crosses the level more than once in a transition region, this VI returns only the first crossing.

[Examples](#examples)

#### Level Crossing (Transitions in, DBL)

Use this polymorphic instance to identify the level crossings in a waveform from information about its **transitions**.

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='level_crossing_transitions_in.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | crossing level specifies the value at which this VI identifies level crossings in the waveform. If you do not wire a crossing level value, LabVIEW uses the mid reference level of the waveform. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | level crossings returns information about the locations of level crossings in the waveform. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Level Crossing (Transitions in, I8)

Use this polymorphic instance to identify the level crossings in a waveform from information about its **transitions**.

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='level_crossing_transitions_in.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | crossing level specifies the value at which this VI identifies level crossings in the waveform. If you do not wire a crossing level value, LabVIEW uses the mid reference level of the waveform. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | level crossings returns information about the locations of level crossings in the waveform. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Level Crossing (Levels in, DBL)

Use this polymorphic instance to identify the level crossings in a waveform from its **state levels** and **reference levels**. This instance uses the **mid ref level** as the crossing level.

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='level_crossing_levels_in.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. You can use the State Levels or Reference Levels VIs to generate this cluster. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | reference levels specifies the high, middle, and low reference levels of a waveform. You can use the Reference Levels VI to generate this cluster. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | level crossings returns information about the locations of level crossings in the waveform. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Level Crossing (Levels in, I8)

Use this polymorphic instance to identify the level crossings in a waveform from its **state levels** and **reference levels**. This instance uses the **mid ref level** as the crossing level.

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='level_crossing_levels_in.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | crossing level specifies the value at which this VI identifies level crossings in the waveform. If you do not wire a crossing level value, LabVIEW uses the mid reference level of the waveform. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | level crossings returns information about the locations of level crossings in the waveform. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level and whose transition crosses both the high and low reference levels. |
|  | slope returns whether the direction of the first transition in the waveform is rising or falling -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge—The transition is a rising edge, or one with a positive slope. |
|  | crossing level returns the input crossing level value at which the waveform falls at each sample in indexes. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Level Crossing VI:

- Basic Eye Diagram VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Rj Dj Separation VI: labview\examples\Jitter Analysis\Jitter Measurements
- Simulated Signal with Jitter VI: labview\examples\Jitter Analysis\Jitter Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/level_pal.html language=enus -->
## TOPIC 00027: Level VIs

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/level_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/level_pal.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Level VIs

**Owning Palette:** [Jitter Analysis VIs](../lvjitterphtk/lvjitterphtk_pal.html)

**Requires:** Jitter Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Level VIs to perform amplitude and level measurements on a signal and to identify positions in time of waveform features.

[Example](#examples)

The Level VIs are useful both before and after you perform jitter measurements. For example, before you can measure jitter, you use the Reference Levels and Find Transitions VIs to identify positions in time of waveform features, such as edges. After you identify jitter in a waveform, you can use other Level VIs to measure additional aspects of signal integrity.

| Palette Object | Description |
| --- | --- |
| Area | Measures the areas and mean voltages of unit intervals in a waveform. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Find Transitions | Measures the boundaries and directions of each transition in a waveform given the reference levels you specify. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Max and Min Voltage | Measures the maximum and minimum voltages in the portions of a waveform between transitions. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Overshoot and Undershoot | Measures the times, locations, and amounts by which a waveform rises above and falls below a state level before or after a transition. The rise above a state level is known as overshoot, and the drop below a state level is known as undershoot. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Peak-to-Peak Voltage | Measures the differences between the peaks, or highest and lowest values, in waveform cycles. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Reference Levels | Computes reference levels based on an input waveform or on state levels computed before this VI runs. LabVIEW uses the reference levels to define the boundaries of edges in waveforms. Wire data to the state levels settings input and the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Root Mean Square Voltage | Measures the RMS values of unit intervals in a waveform. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| State Levels | Computes the high and low state levels of a waveform and the corresponding amplitude. You can use state levels to identify the position in time of a waveform feature to be measured. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |

#### Example

Refer to the Overshoot Demo VI in the labview\examples\Jitter Analysis\Level Measurements directory for an example of using the Level VIs.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/lvjitterphtk_pal.html language=enus -->
## TOPIC 00028: Jitter Analysis VIs

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/lvjitterphtk_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/lvjitterphtk_pal.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Jitter Analysis VIs

June 2012, 373270B-01

**Requires:** Jitter Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Jitter Analysis VIs to perform automated [jitter, eye diagram, and phase-noise measurements](../lvjitterphtk/jat_overview.html). You can use these VIs to measure and analyze signal data, and then graph the data in an eye diagram or bathtub plot.

| Subpalette | Description |
| --- | --- |
| Clock Recovery VIs | Use the Clock Recovery VIs to establish the timing of the reference clock from data within a signal. After you generate a reference clock signal, you can use the Jitter VIs to compare a measured signal with the clock signal to measure jitter. |
| Eye Diagram Measurements VIs | Use the Eye Diagram Measurements VIs to construct an eye diagram that displays information about jitter in a waveform signal. In eye diagrams, corresponding segments of a waveform are superimposed upon each other to illustrate variations in the time at which features in the waveform occur. |
| Jitter VIs | Use the Jitter VIs to measure the jitter in a waveform and separate, or decompose, it into components, such as random jitter, deterministic jitter, and so on. When separated, the individual components of jitter can indicate causes of excessive jitter in the system. |
| Level VIs | Use the Level VIs to perform amplitude and level measurements on a signal and to identify positions in time of waveform features. |
| Signal Generation VI | Use the Signal with Jitter VI to generate signals you can use to test and debug jitter analysis applications. |
| Timing VIs | Use the Timing VIs to return information about the times and locations at which events in a signal occur. |

© 2010–2012 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/max_and_min_voltage.html language=enus -->
## TOPIC 00029: Max and Min Voltage VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/max_and_min_voltage.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/max_and_min_voltage.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Max and Min Voltage VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the maximum and minimum voltages in the portions of a waveform between transitions. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Max and Min Voltage (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='max_min_voltage.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | max sequence returns an array of the maximum values in the areas between the end index of one transition and the start index of the next transition. |
|  | max timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occurred. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples this VI measures as maximum voltage values. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples this VI measures as maximum voltage values. |
|  | min sequence returns an array of the minimum values in areas between the end index in one transition and the start index of the next transition. |
|  | min timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples this VI measures as minimum voltage values. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples this VI measures as minimum voltage values. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Max and Min Voltage (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='max_min_voltage.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | max sequence returns an array of the maximum values in the areas between the end index of one transition and the start index of the next transition. |
|  | max timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occurred. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples this VI measures as maximum voltage values. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples this VI measures as maximum voltage values. |
|  | min sequence returns an array of the minimum values in areas between the end index in one transition and the start index of the next transition. |
|  | min timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples this VI measures as minimum voltage values. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples this VI measures as minimum voltage values. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/n_cycle_to_cycle_jitter.html language=enus -->
## TOPIC 00030: N Cycle Jitter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/n_cycle_to_cycle_jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/n_cycle_to_cycle_jitter.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### N Cycle Jitter VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the differences in the amounts of jitter between cycles of a waveform, which indicates the change in jitter at different locations in the waveform.

This VI is similar to the [Cycle-to-Cycle Jitter](../lvjitterphtk/cycle_to_cycle_jitter.html) VI, except this VI can compute differences in jitter between cycles at a specific interval.

[IMAGE alt='image' src='n_cycle_jitter.gif']

|  | Nc specifies the cycle interval at which to compute differences in period jitter. For example, if Nc is 2, this VI subtracts the period jitter value for the first cycle from the value for the third cycle, the period jitter value for the second cycle from the value for the fourth cycle, and so on to compute the N cycle jitter sequence. |
| --- | --- |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | N cycle jitter sequence returns the differences in period jitter between cycles at the interval you specify. |
|  | N cycle jitter timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/n_cycle_to_cycle_meas.html language=enus -->
## TOPIC 00031: N Cycle Measurement VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/n_cycle_to_cycle_meas.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/n_cycle_to_cycle_meas.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### N Cycle Measurement VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the differences between elements in an array of measurements at the interval you specify.

Cycle-to-Cycle Measurement

[IMAGE alt='image' src='n_cycle_measurement.gif']

|  | sequence contains measurements whose differences you want to compute. |
| --- | --- |
|  | timestamps describes the waveform in which the measurements occur. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of samples in the waveform from which the measurements were taken. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of samples in the waveform from which the measurements were taken. |
|  | N specifies the interval at which to compute differences in the input sequence. For example, if N is 2, this VI subtracts the value of the first element from the value of the third element, the value for the second element from the value for the fourth element, and so on. |
|  | N cycle sequence returns the differences between the elements in the input sequence at the interval you specify. |
|  | N cycle timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes returns the index numbers of the measurements in the waveform. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes returns the index numbers of the measurements in the waveform. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/n_period_jitter.html language=enus -->
## TOPIC 00032: N Period Jitter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/n_period_jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/n_period_jitter.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### N Period Jitter VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the differences between period times from a waveform and the corresponding ideal periods from the reference clock.

This VI is similar to the [Period Jitter](../lvjitterphtk/period_jitter.html) VI, except this VI can compute the period jitter between edges at a specific interval, rather than between adjacent edges.

[IMAGE alt='image' src='n_period_jitter.gif']

|  | Np specifies the edge interval at which to compute period jitter. For example, if Np is 2, this VI subtracts the jitter value at the first edge in the waveform from the jitter value at the third edge, the jitter at the second edge from the jitter at the fourth edge, and so on to compute the N period jitter sequence. |
| --- | --- |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | N period jitter sequence is an array of durations of cycles in the waveform, in seconds. In other words, the values represent the differences between the times that transitions at the interval you specify fall on the crossing level. |
|  | N period jitter timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/negative_width.html language=enus -->
## TOPIC 00033: Negative Width VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/negative_width.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/negative_width.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Negative Width VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the pulse duration that follows the level crossing in each falling transition.

[IMAGE alt='image' src='negative_width.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | - width sequence returns an array of the time differences in seconds between the time the signal falls below the crossing level and the time at which the signal next rises above that level. |
|  | - width timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occurred. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level in falling edges of cycles that later rise above the crossing level. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level in falling edges of cycles that later rise above the crossing level. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/overshoot_and_undershoot.html language=enus -->
## TOPIC 00034: Overshoot and Undershoot VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/overshoot_and_undershoot.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/overshoot_and_undershoot.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Overshoot and Undershoot VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the times, locations, and amounts by which a waveform rises above and falls below a state level before or after a transition. The rise above a state level is known as overshoot, and the drop below a state level is known as undershoot. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

|  | Note The terminology and measurement definitions for this VI comply with IEEE Standard 181-2003, IEEE Standard on Transitions, Pulses, and Related Waveforms. |
| --- | --- |

[Details](#details)  [Example](#examples)

#### Overshoot and Undershoot (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='overshoot_and_undershoot.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition select sets whether to identify overshoot and undershoot in the regions before or after each transition. 0pre-transition—Specifies to return measurements from the regions that precede transitions.1post-transition (default)—Specifies to return measurements from the regions that follow transitions. |
| 0 | pre-transition—Specifies to return measurements from the regions that precede transitions. |
| 1 | post-transition (default)—Specifies to return measurements from the regions that follow transitions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | slope specifies the direction of the transitions for which you want to return measurements. -1Falling Edge—Returns information about falling edges, or those with negative slopes.0Both—Returns information about both rising and falling edges.1Rising Edge (default)—Returns information about rising edges, or those with positive slopes. |
| -1 | Falling Edge—Returns information about falling edges, or those with negative slopes. |
| 0 | Both—Returns information about both rising and falling edges. |
| 1 | Rising Edge (default)—Returns information about rising edges, or those with positive slopes. |
|  | overshoot sequence returns an array of the overshoot values for local maximums associated with the types of transitions you specify using slope and transition select. Overshoot measures the height as a fraction of the amplitude of the signal. Refer to the Details section of this topic for more information about how this VI calculates overshoot. |
|  | overshoot timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform measured as overshoot. Each element of indexes corresponds to an element of overshoot sequence. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform measured as overshoot. Each element of indexes corresponds to an element of overshoot sequence. |
|  | undershoot sequence returns an array of the undershoot values for local minimums associated with the types of transitions you specify using slope and transition select. Undershoot measures the height as a fraction of the amplitude of the signal. Refer to the Details section of this topic for more information about how this VI calculates undershoot. |
|  | undershoot timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform measured as undershoot. Each element of indexes corresponds to an element of undershoot sequence. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform measured as undershoot. Each element of indexes corresponds to an element of undershoot sequence. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Overshoot and Undershoot (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='overshoot_and_undershoot.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition select sets whether to identify overshoot and undershoot in the regions before or after each transition. 0pre-transition—Specifies to return measurements from the regions that precede transitions.1post-transition (default)—Specifies to return measurements from the regions that follow transitions. |
| 0 | pre-transition—Specifies to return measurements from the regions that precede transitions. |
| 1 | post-transition (default)—Specifies to return measurements from the regions that follow transitions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | slope specifies the direction of the transitions for which you want to return measurements. -1Falling Edge—Returns information about falling edges, or those with negative slopes.0Both—Returns information about both rising and falling edges.1Rising Edge (default)—Returns information about rising edges, or those with positive slopes. |
| -1 | Falling Edge—Returns information about falling edges, or those with negative slopes. |
| 0 | Both—Returns information about both rising and falling edges. |
| 1 | Rising Edge (default)—Returns information about rising edges, or those with positive slopes. |
|  | overshoot sequence returns an array of the overshoot values for local maximums associated with the types of transitions you specify using slope and transition select. Overshoot measures the height as a fraction of the amplitude of the signal. Refer to the Details section of this topic for more information about how this VI calculates overshoot. |
|  | overshoot timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform measured as overshoot. Each element of indexes corresponds to an element of overshoot sequence. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform measured as overshoot. Each element of indexes corresponds to an element of overshoot sequence. |
|  | undershoot sequence returns an array of the undershoot values for local minimums associated with the types of transitions you specify using slope and transition select. Undershoot measures the height as a fraction of the amplitude of the signal. Refer to the Details section of this topic for more information about how this VI calculates undershoot. |
|  | undershoot timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform measured as undershoot. Each element of indexes corresponds to an element of undershoot sequence. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform measured as undershoot. Each element of indexes corresponds to an element of undershoot sequence. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Overshoot and Undershoot Details

The following illustration shows the overshoot and undershoot in a single negative transition.

[IMAGE alt='image' src='loc_eps_ovun_nst.gif']

The following illustration shows the overshoot and undershoot in a single positive transition.

[IMAGE alt='image' src='loc_eps_ovun_pst.gif']

#### Pre-transition Measurements

To calculate pre-transition overshoot and undershoot for each transition, LabVIEW searches for a local minimum and maximum in the pre-transition aberration region immediately preceding the beginning of the transition. The pre-transition aberration region is defined as the minimum of 3*(end time – start time) and (current transition start time – previous transition end time) / 2. If the transition to measure is the first in the waveform, the interval is defined as the minimum of 3*(end time – start time) and (start time – beginning of the waveform).

If **slope** is falling, LabVIEW calculates the pre-transition undershoot using the following equation:

[IMAGE alt='image' src='loc_eq_fallpolun_jit.gif']

If **slope** is rising, LabVIEW calculates the pre-transition undershoot using the following equation:

[IMAGE alt='image' src='loc_eq_risepolp_jit.gif']

If **slope** is falling, LabVIEW calculates the pre-transition overshoot using the following equation:

[IMAGE alt='image' src='loc_eq_fallpolp_jit.gif']

If **slope** is rising, LabVIEW calculates the pre-transition overshoot using the following equation:

[IMAGE alt='image' src='loc_eq_riseprto_jit.gif']

where the state levels and amplitude are defined in the **transitions** input.

#### Post-transition Measurements

To calculate post-transition undershoot and overshoot for each transition, LabVIEW searches for a local minimum and maximum in the post-transition aberration region immediately following the end of the transition. The post-transition aberration region is defined as the minimum of 3*(end time – start time) and (next transition start time – current transition end time) / 2. If the transition to measure is the last in the waveform, the interval is defined as the minimum of 3*(end time – start time) and (end of the waveform – end time).

If **slope** is falling, LabVIEW calculates the post-transition undershoot using the following equation:

[IMAGE alt='image' src='loc_eq_risepolp_jit.gif']

If **slope** is rising, LabVIEW calculates the post-transition undershoot using the following equation:

[IMAGE alt='image' src='loc_eq_fallpolun_jit.gif']

If **slope** is falling, LabVIEW calculates the post-transition overshoot using the following equation:

[IMAGE alt='image' src='loc_eq_riseprto_jit.gif']

If **slope** is rising, LabVIEW calculates the post-transition overshoot using the following equation:

[IMAGE alt='image' src='loc_eq_fallpolp_jit.gif']

where the state levels and amplitude are defined in the **transitions** input.

#### Example

Refer to the Overshoot Demo VI in the labview\examples\Jitter Analysis\Level Measurements directory for an example of using the Overshoot and Undershoot VI.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/peak_to_peak_voltage.html language=enus -->
## TOPIC 00035: Peak-to-Peak Voltage VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/peak_to_peak_voltage.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/peak_to_peak_voltage.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Peak-to-Peak Voltage VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the differences between the peaks, or highest and lowest values, in waveform cycles. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Peak-to-Peak Voltage (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='peak_to_peak_voltage.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | peak-to-peak voltage sequence is an array of the differences between the maximum and minimum peaks in cycles. Each element of the array corresponds to a cycle in the waveform. If the waveform does not contain at least two pairs of rising and falling transitions, LabVIEW returns an empty array. |
|  | peak-to-peak voltage timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Peak-to-Peak Voltage (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='peak_to_peak_voltage.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | peak-to-peak voltage sequence is an array of the differences between the maximum and minimum peaks in cycles. Each element of the array corresponds to a cycle in the waveform. If the waveform does not contain at least two pairs of rising and falling transitions, LabVIEW returns an empty array. |
|  | peak-to-peak voltage timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/period_jitter.html language=enus -->
## TOPIC 00036: Period Jitter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/period_jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/period_jitter.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Period Jitter VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the differences between cycle durations in a waveform and the corresponding cycle durations from the reference clock.

This VI is similar to the [N Period Jitter](../lvjitterphtk/n_period_jitter.html) VI, except this VI always computes the period jitter between adjacent edges in the waveform.

[Example](#examples)

[IMAGE alt='image' src='period_jitter.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | period jitter sequence returns the differences between each cycle period in the measured waveform and the corresponding periods in the ideal waveform. |
|  | period jitter timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Simulated Signal with Jitter VI in the labview\examples\Jitter Analysis\Jitter Measurements directory for an example of using the Period Jitter VI.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/period_jittertk.html language=enus -->
## TOPIC 00037: Period VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/period_jittertk.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/period_jittertk.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Period VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the durations of portions of a waveform. Wire data to the **rising/falling** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Example](#examples)

#### Period (clock)

Use this polymorphic instance to measure the periods of cycles in waveforms with evenly spaced rising and falling transitions.

[IMAGE alt='image' src='period_clock.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | period sequence is an array of durations of cycles in the waveform, in seconds. In other words, the values represent the differences between the time that successive transitions of the same direction fall on the crossing level. |
|  | frequency sequence is an array of the frequencies of cycles in the waveform. The elements in frequency sequence are the reciprocals of the period sequence values. |
|  | sequence timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Period (data)

Use this polymorphic instance to measure the unit intervals in waveforms with unevenly spaced rising and falling transitions. When transitions are unevenly spaced, unit intervals provide a more useful measure of time than cycle periods.

[IMAGE alt='image' src='period_data.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | bit count specifies the number of bits between pairs of transitions of the opposite direction in the waveform. Each element of bit count corresponds to an element of unit-interval sequence. |
|  | unit-interval sequence is an array of unit intervals in the waveform, in seconds. To calculate these values, LabVIEW divides the time between successive level crossings by the number of bits between those locations, as specified by bit count. |
|  | unit-interval timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a half-cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a half-cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Simulated Signal with Jitter VI in the labview\examples\Jitter Analysis\Jitter Measurements directory for an example of using the Period VI.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/phase_jitterphtk.html language=enus -->
## TOPIC 00038: Phase VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/phase_jitterphtk.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/phase_jitterphtk.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Phase VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the differences in phase between corresponding cycles in two waveforms.

You can use this VI to measure the response of a signal to a particular stimulus. For example, **level crossings A** might be the original signal, and **level crossings B** might be the response signal following a stimulus. You also can use this VI to compare waveforms from two different channels.

[Details](#details)

[IMAGE alt='image' src='phase.gif']

|  | level crossings A contains information about the locations of level crossings in a waveform. You can use the Level Crossing VI to generate this cluster from a waveform. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | level crossings B (ref) contains information about the locations of level crossings in a waveform. level crossings B (ref) serves as the reference against which this VI compares level crossings A. You can use the Level Crossing VI to generate this cluster from a waveform. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | phase unit specifies the units in which to express the phase measurements. 0degrees (default)1radians |
| 0 | degrees (default) |
| 1 | radians |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | phase sequence returns the differences between the times that cycles begin, in units specified by phase unit. The time difference relative to the period of level crossings A (Tdiff/T) is the phase ratio. |
|  | phase timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occurred. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of all waveform samples that fall on the crossing level in transitions of the direction you specify in slope. This VI returns the index numbers from level crossings A. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of all waveform samples that fall on the crossing level in transitions of the direction you specify in slope. This VI returns the index numbers from level crossings A. |
|  | mean phase is the average of the phase offset measurements returned in phase sequence. This VI uses the Mean VI to compute the mean of the values in phase sequence. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Phase Details

This VI uses **level crossings B (ref)** as the reference against which to measure the phase difference in **level crossings A**. Thus, when **level crossings A** occurs after **level crossings B (ref)**, the phase measurement is positive. When the opposite is true, the phase measurement is negative.

To identify the first pair of cycles to measure, this VI finds the edge in **level crossings B** nearest to the first edge in **level crossings A** of the direction specified by **slope**. The next edges of the same direction in each input also become pairs, and so on.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/phase_noise.html language=enus -->
## TOPIC 00039: Phase Noise VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/phase_noise.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/phase_noise.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Phase Noise VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Converts a jitter sequence into the frequency domain and measures the RMS value integrated between two frequencies.

[IMAGE alt='image' src='phase_noise.gif']

|  | jitter sequence is an array of jitter measurements. |
| --- | --- |
|  | jitter timestamps describes the waveform and the times at which measurements in the corresponding sequence occur. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | band defines the frequency of the signal at which you want to measure phase noise. start frequency (Hz) is the frequency at which to begin the frequency spectrum. stop frequency (Hz) is the frequency at which to end the frequency spectrum. |
|  | start frequency (Hz) is the frequency at which to begin the frequency spectrum. |
|  | stop frequency (Hz) is the frequency at which to end the frequency spectrum. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | phase noise in band (s rms) returns the phase noise, expressed in seconds as an RMS value. |
|  | phase jitter spectrum (dBc/Hz) returns a graph of the phase-noise spectrum. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/positive_width.html language=enus -->
## TOPIC 00040: Positive Width VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/positive_width.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/positive_width.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Positive Width VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the pulse duration that follows the level crossing in each rising transition.

[IMAGE alt='image' src='positive_width.gif']

|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | + width sequence returns an array of the time differences in seconds between the time the signal rises above the crossing level and the time at which the signal next falls below that level. |
|  | + width timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of waveform samples that fall on the crossing level in rising edges of cycles that later fall below the crossing level. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of waveform samples that fall on the crossing level in rising edges of cycles that later fall below the crossing level. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/quality_factor.html language=enus -->
## TOPIC 00041: Quality Factor VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/quality_factor.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/quality_factor.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Quality Factor VI

**Owning Palette:** [Eye Diagram Measurements VIs](../lvjitterphtk/eye_diagram_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the quality of a waveform based on the histograms at the base and top of an eye diagram formed from the waveform. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Quality Factor (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='quality_factor.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | quality factor returns the quality measure for the waveform using the mean and standard deviation values of the histograms formed at the base and top of an eye diagram. LabVIEW uses the following equation to calculate the quality factor. When random jitter causes the standard deviations of the histograms at the base and top to increase, the quality factor decreases and indicates a lower quality signal. |
|  | decision voltage returns the computed best decision voltage, or the lowest bit error rate. |
|  | estimated BER returns an estimate of the bit error rate, given the quality factor. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Quality Factor (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='quality_factor.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | quality factor returns the quality measure for the waveform using the mean and standard deviation values of the histograms formed at the base and top of an eye diagram. LabVIEW uses the following equation to calculate the quality factor. When random jitter causes the standard deviations of the histograms at the base and top to increase, the quality factor decreases and indicates a lower quality signal. |
|  | decision voltage returns the computed best decision voltage, or the lowest bit error rate. |
|  | estimated BER returns an estimate of the bit error rate, given the quality factor. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/ref_bit_waveform.html language=enus -->
## TOPIC 00042: Reference Bit Waveform Creation VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/ref_bit_waveform.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/ref_bit_waveform.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Reference Bit Waveform Creation VI

**Owning Palette:** [Clock Recovery VIs](../lvjitterphtk/clock_recovery_pal.html)

**Requires:** Jitter Analysis Toolkit

Creates an ideal reference data waveform that is synchronized to the source waveform by using the reference crossing times to locate when the data bit changes state.

[Example](#examples)

#### Reference Bit Waveform Creation (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='reference_bit_waveform_creation.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | ideal bit waveform returns a representation of the waveform that has voltage values replaced with bits that indicate whether the waveform is in its high or low state at unit intervals. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. Y is a sequence of zeros and ones that represent whether the waveform is at its low or high state, respectively, at each unit interval. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | Y is a sequence of zeros and ones that represent whether the waveform is at its low or high state, respectively, at each unit interval. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reference Bit Waveform Creation (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='reference_bit_waveform_creation.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | ideal bit waveform returns a representation of the waveform that has voltage values replaced with bits that indicate whether the waveform is in its high or low state at unit intervals. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. Y is a sequence of zeros and ones that represent whether the waveform is at its low or high state, respectively, at each unit interval. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | Y is a sequence of zeros and ones that represent whether the waveform is at its low or high state, respectively, at each unit interval. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the ISI Jitter Measurement VI in the labview\examples\Jitter Analysis\Jitter Measurements directory for an example of using the Reference Bit Waveform Creation VI.

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/reference_levels.html language=enus -->
## TOPIC 00043: Reference Levels VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/reference_levels.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/reference_levels.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Reference Levels VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes reference levels based on an input waveform or on state levels computed before this VI runs. LabVIEW uses the [reference levels](/csh?topicname=lvwave/state_and_reference_levels.html) to define the boundaries of edges in waveforms. Wire data to the **state levels settings** input and the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Examples](#examples)

#### Reference Levels (waveform in, DBL)

Use this polymorphic instance to calculate the **reference levels** of a waveform when you do not know its high and low state levels.

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='reference_levels_waveform_in.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | state levels settings sets the method this VI uses to determine the high and low state levels of a waveform. Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. |
|  | method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
| 0 | histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. |
| 1 | peak—Searches the entire waveform for its maximum and minimum levels. |
| 2 | auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails). |
| 3 | auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
|  | histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. |
|  | histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode |
| 0 | mode |
|  | search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | reference levels settings defines how this VI measures the reference levels of the waveform. high ref level specifies the high reference level of the waveform as a percentage (default) or in absolute units. The default is 90.00. mid ref level specifies the middle reference level as a percentage (default) or in absolute units. The default is 50.00. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. ref units specifies how this VI uses the high ref level, mid ref level, and low ref level inputs to compute the actual reference levels of the waveform. 0absolute—Specifies to return the input reference level values unchanged in the reference levels output.1percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
|  | high ref level specifies the high reference level of the waveform as a percentage (default) or in absolute units. The default is 90.00. |
|  | mid ref level specifies the middle reference level as a percentage (default) or in absolute units. The default is 50.00. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | ref units specifies how this VI uses the high ref level, mid ref level, and low ref level inputs to compute the actual reference levels of the waveform. 0absolute—Specifies to return the input reference level values unchanged in the reference levels output.1percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
| 0 | absolute—Specifies to return the input reference level values unchanged in the reference levels output. |
| 1 | percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | reference levels contains the high, middle, and low reference levels of a waveform in absolute units. high ref level returns the high reference level. mid ref level returns the middle reference level. low ref level returns the low reference level. |
|  | high ref level returns the high reference level. |
|  | mid ref level returns the middle reference level. |
|  | low ref level returns the low reference level. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reference Levels (waveform in, I8)

Use this polymorphic instance to calculate the **reference levels** of a waveform when you do not know its high and low state levels.

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='reference_levels_waveform_in.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | state levels settings sets the method this VI uses to determine the high and low state levels of a waveform. Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. |
|  | method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
| 0 | histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. |
| 1 | peak—Searches the entire waveform for its maximum and minimum levels. |
| 2 | auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails). |
| 3 | auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
|  | histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. |
|  | histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode |
| 0 | mode |
|  | search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | reference levels settings defines how this VI measures the reference levels of the waveform. high ref level specifies the high reference level of the waveform as a percentage (default) or in absolute units. The default is 90.00. mid ref level specifies the middle reference level as a percentage (default) or in absolute units. The default is 50.00. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. ref units specifies how this VI uses the high ref level, mid ref level, and low ref level inputs to compute the actual reference levels of the waveform. 0absolute—Specifies to return the input reference level values unchanged in the reference levels output.1percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
|  | high ref level specifies the high reference level of the waveform as a percentage (default) or in absolute units. The default is 90.00. |
|  | mid ref level specifies the middle reference level as a percentage (default) or in absolute units. The default is 50.00. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | ref units specifies how this VI uses the high ref level, mid ref level, and low ref level inputs to compute the actual reference levels of the waveform. 0absolute—Specifies to return the input reference level values unchanged in the reference levels output.1percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
| 0 | absolute—Specifies to return the input reference level values unchanged in the reference levels output. |
| 1 | percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | reference levels contains the high, middle, and low reference levels of a waveform in absolute units. high ref level returns the high reference level. mid ref level returns the middle reference level. low ref level returns the low reference level. |
|  | high ref level returns the high reference level. |
|  | mid ref level returns the middle reference level. |
|  | low ref level returns the low reference level. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reference Levels (states in)

Use this polymorphic instance to calculate the **reference levels** of a waveform from high and low state levels computed before this VI runs.

[IMAGE alt='image' src='reference_levels_states_in.gif']

|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. You can use the State Levels VI to generate this cluster. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
| --- | --- |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | reference levels settings defines how this VI measures the reference levels of the waveform. high ref level specifies the high reference level of the waveform as a percentage (default) or in absolute units. The default is 90.00. mid ref level specifies the middle reference level as a percentage (default) or in absolute units. The default is 50.00. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. ref units specifies how this VI uses the high ref level, mid ref level, and low ref level inputs to compute the actual reference levels of the waveform. 0absolute—Specifies to return the input reference level values unchanged in the reference levels output.1percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
|  | high ref level specifies the high reference level of the waveform as a percentage (default) or in absolute units. The default is 90.00. |
|  | mid ref level specifies the middle reference level as a percentage (default) or in absolute units. The default is 50.00. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | ref units specifies how this VI uses the high ref level, mid ref level, and low ref level inputs to compute the actual reference levels of the waveform. 0absolute—Specifies to return the input reference level values unchanged in the reference levels output.1percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
| 0 | absolute—Specifies to return the input reference level values unchanged in the reference levels output. |
| 1 | percent (default)—Specifies to calculate the reference levels using the input reference level settings as percentages of the amplitude of the high and low state levels. For more information about how this VI calculates reference levels, refer to the Details section of this topic. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | state levels dup returns the state levels unchanged. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | reference levels contains the high, middle, and low reference levels of a waveform in absolute units. high ref level returns the high reference level. mid ref level returns the middle reference level. low ref level returns the low reference level. |
|  | high ref level returns the high reference level. |
|  | mid ref level returns the middle reference level. |
|  | low ref level returns the low reference level. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reference Levels Details

When **ref units** is **percent**, this VI uses the following equation to compute the reference levels:

[IMAGE alt='image' src='loc_eq_ref_levels.gif']

where    *y<sub>x%</sub>* is the value of a particular reference level

*level(s<sub>1</sub>)* is the **low state level**

*A* is the difference of the high and low state levels, or **amplitude**

*x* represents the percentage for that reference level that you specify in **reference levels settings**.

#### Examples

Refer to the following VIs for examples of using the Reference Levels VI:

- Basic Eye Diagram VI: labview\examples\Jitter Analysis\Eye Diagram Measurements
- Simulated Signal with Jitter VI: labview\examples\Jitter Analysis\Jitter Measurements
- Overshoot Demo VI: labview\examples\Jitter Analysis\Level Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/rise_time.html language=enus -->
## TOPIC 00044: Rise Time VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/rise_time.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/rise_time.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Rise Time VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the transition duration of rising transitions in a waveform. The duration of a rising transition, or rise time, is the difference in time between its **start index** and **end index**. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Rise Time (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='rise_time.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rise time sequence is an array of the durations, in seconds, between the beginning and end of each rising transition. |
|  | rise time timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Rise Time (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='rise_time.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | transitions contains information about the transitions in the waveform. Use the Find Transitions VI to generate this cluster. transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | transition is an array of clusters that describe each transition in waveform. start index specifies the sample of waveform at which the transition begins. end index specifies the sample of waveform at which the transition ends. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | start index specifies the sample of waveform at which the transition begins. |
|  | end index specifies the sample of waveform at which the transition ends. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | state levels specifies the high and low state values in the waveform and the corresponding amplitude. amplitude is the difference between high state level and low state level. high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level specifies the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level specifies the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | ref levels specifies the high, middle, and low reference levels of a waveform. high ref level specifies the high reference level of the waveform in absolute units. mid ref level specifies the middle reference level of the waveform in absolute units. low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | high ref level specifies the high reference level of the waveform in absolute units. |
|  | mid ref level specifies the middle reference level of the waveform in absolute units. |
|  | low ref level specifies the low reference level as a percentage (default) or in absolute units. The default is 10.00. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rise time sequence is an array of the durations, in seconds, between the beginning and end of each rising transition. |
|  | rise time timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that represent the beginnings of edges. Each element of indexes corresponds to an element of the sequence array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Rise Time Details

A rising polarity transition duration is known as rise time, and a falling polarity transition duration is known as fall time, as shown in the following example:

[IMAGE alt='image' src='loc_eps_rftimex.gif']

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/rj_dj_separation.html language=enus -->
## TOPIC 00045: RJ PJ Separation VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/rj_dj_separation.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/rj_dj_separation.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### RJ PJ Separation VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Separates the random and periodic components of jitter in a jitter sequence and returns their RMS and peak-to-peak values.

Refer to the [Details](#jitter_types) section of this topic for more information about random and periodic jitter.

[Details](#details)  [Examples](#examples)

#### nTone

After this instance resamples the jitter sequence, as described in the [Details](#details) section, it computes periodic jitter by modeling spectrum peaks as sinusoids and returning the sum of the identified sinusoids. This instance searches for peaks above a **threshold** within the amplitude spectrum of the **jitter sequence**.

[IMAGE alt='image' src='rj_pj_separation_-_ntone.gif']

|  | mode specifies how this VI identifies periodic jitter. 0search for fit (default)—Searches for the minimum number of periodic components that are above the threshold and that yield the best fit of the data. This mode is useful because it provides an effective method that typically avoids over-fitting the data.1manual—Uses all tones whose amplitude is greater than the threshold to fit the data, up to a maximum number of tones you specify in the periodic fit settings input. |
| --- | --- |
| 0 | search for fit (default)—Searches for the minimum number of periodic components that are above the threshold and that yield the best fit of the data. This mode is useful because it provides an effective method that typically avoids over-fitting the data. |
| 1 | manual—Uses all tones whose amplitude is greater than the threshold to fit the data, up to a maximum number of tones you specify in the periodic fit settings input. |
|  | jitter sequence is an array of jitter measurements. |
|  | jitter timestamps describes the waveform and the times at which measurements in the corresponding sequence occur. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | periodic fit settings contains the following elements that determine how this VI identifies periodic jitter. threshold specifies the minimum amplitude that peaks in the input sequence must exceed to be measured as periodic jitter. Setting a threshold allows you to ignore peaks that result from noise rather than periodic jitter mechanisms. max num tones specifies the maximum number of tones that this VI extracts. If you set max num tones to –1, this VI extracts all tones whose amplitude exceeds threshold. |
|  | threshold specifies the minimum amplitude that peaks in the input sequence must exceed to be measured as periodic jitter. Setting a threshold allows you to ignore peaks that result from noise rather than periodic jitter mechanisms. |
|  | max num tones specifies the maximum number of tones that this VI extracts. If you set max num tones to –1, this VI extracts all tones whose amplitude exceeds threshold. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | periodic search info returns the following elements that describe the periodic jitter in the jitter sequence. actual num tones returns the number of tones whose amplitude exceeds the threshold value that defines periodic jitter. min amplitude returns the amplitude of the smallest tone that exceeds the threshold. |
|  | actual num tones returns the number of tones whose amplitude exceeds the threshold value that defines periodic jitter. |
|  | min amplitude returns the amplitude of the smallest tone that exceeds the threshold. |
|  | periodic jitter (s p-p) returns the periodic jitter measured as a peak-to-peak value. |
|  | periodic jitter (s rms) returns the standard deviation of the periodic jitter in the jitter sequence. |
|  | random jitter (s rms) returns the RMS value of the original jitter sequence minus the periodic jitter. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | jitter spectrum is a graph that displays the spectrum of the original jitter sequence and the periodic jitter in the signal. |

#### Spectral Trend

After this instance resamples the jitter sequence, as described in the [Details](#details) section, it removes the DC level and then computes the power spectrum. This instance approximates and removes the spectrum trend and peaks, leaving the random portion of the spectrum.

[IMAGE alt='image' src='rj_pj_separation_-_spectral_trend.gif']

|  | jitter sequence is an array of jitter measurements. |
| --- | --- |
|  | jitter timestamps describes the waveform and the times at which measurements in the corresponding sequence occur. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | periodic jitter (s p-p) returns the periodic jitter measured as a peak-to-peak value. |
|  | periodic jitter (s rms) returns the standard deviation of the periodic jitter in the jitter sequence. |
|  | random jitter (s rms) returns the RMS value of the original jitter sequence minus the periodic jitter. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | jitter spectrum is a graph that displays the spectrum of the original jitter sequence and the periodic jitter in the signal. |

#### RJ PJ Separation Details

If you wire waveform data to the **jitter timestamps** input, this VI resamples the input **jitter sequence** so it is evenly sampled. Otherwise, this VI assumes the measurements in the **jitter sequence** are already evenly sampled. Jitter sequences are not evenly sampled in time because the jitter is measured when the last value required to measure the jitter occurs. For example, time interval error values have corresponding timestamps at the level crossing of the data signal, while period jitter values have corresponding timestamps at the time of the second level crossing of the data signal. Thus, the resampling allows the jitter sequence to be evenly spaced for the FFT.

##### Random Jitter vs. Periodic Jitter

Random jitter is unbounded and does not achieve a maximum or minimum phase deviation within any time interval. By contrast, deterministic jitter is bounded and reaches maximum and minimum phase deviation values within an identifiable time interval. Periodic jitter is a type of systematic deterministic jitter that is not data dependent, or correlated with a specific sequence of bits in a waveform.

#### Examples

Refer to the following VIs for examples of using the RJ PJ Separation VI:

- Rj Dj Separation VI: labview\examples\Jitter Analysis\Jitter Measurements
- Rj Dj Delta Delta Separation VI: labview\examples\Jitter Analysis\Jitter Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/rms_voltage.html language=enus -->
## TOPIC 00046: Root Mean Square Voltage VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/rms_voltage.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/rms_voltage.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Root Mean Square Voltage VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the [RMS values](/csh?topicname=lvanlsconcepts/what_is_rms_level.html) of unit intervals in a waveform. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

#### Root Mean Square Voltage (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='root_mean_square_voltage.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | Vrms sequence is an array of the RMS values for each unit interval in the waveform. |
|  | Vrms timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Root Mean Square Voltage (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='root_mean_square_voltage.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rising/falling specifies the direction of the transition at which to begin the measurement. This VI begins measuring at the first transition of that direction in the waveform. –1Falling Edge—Specifies to begin measuring at the first falling edge in the waveform.1Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
| –1 | Falling Edge—Specifies to begin measuring at the first falling edge in the waveform. |
| 1 | Rising Edge (default)—Specifies to begin measuring at the first rising edge in the waveform. |
|  | Vrms sequence is an array of the RMS values for each unit interval in the waveform. |
|  | Vrms timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the waveform samples that fall on the crossing level in the direction specified by rising/falling and that mark the beginning of a complete cycle. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/setup_time.html language=enus -->
## TOPIC 00047: Setup and Hold Time VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/setup_time.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/setup_time.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Setup and Hold Time VI

**Owning Palette:** [Timing VIs](../lvjitterphtk/timing_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the setup and hold times in a waveform. Setup time is the time difference between when a waveform falls on the **crossing level** and when a level crossing in a reference clock occurs. Hold time is the time difference between when a level crossing in a reference clock occurs and when a transition in a waveform falls on the **crossing level**.

[IMAGE alt='image' src='setup_and_hold_time.gif']

|  | level crossings A contains information about the locations of level crossings in a waveform. You can use the Level Crossing VI to generate this cluster from a waveform. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
| --- | --- |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | level crossings B (ref) contains information about the locations of level crossings in a waveform. level crossings B (ref) serves as the reference against which this VI compares level crossings A. You can use the Level Crossing VI to generate this cluster from a waveform. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | offset specifies an amount of time, in seconds, by which to offset the locations of level crossings in level crossings B (ref). Specifying an offset allows you to more accurately match corresponding transitions in level crossings A and level crossings B (ref) when the initial times in the two waveforms are not equal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | setup time sequence is an array of the durations that the original waveform is stable before clock transitions. |
|  | hold time sequence is an array of the durations that the original waveform is stable following clock transitions. |
|  | sequence timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of all waveform samples that fall on the crossing level. This VI returns the indexes from the reference waveform, level crossings A. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of all waveform samples that fall on the crossing level. This VI returns the indexes from the reference waveform, level crossings A. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/signal_with_jitter.html language=enus -->
## TOPIC 00048: Signal with Jitter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/signal_with_jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/signal_with_jitter.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Signal with Jitter VI

**Owning Palette:** [Signal Generation VI](../lvjitterphtk/utility_pal.html)

**Requires:** Jitter Analysis Toolkit

Creates a clock or data stream signal waveform and injects jitter into the signal. You can use this VI to create a waveform with which to test applications that measure jitter.

[Examples](#examples)

[IMAGE alt='image' src='signal_with_jitter.gif']

|  | reset specifies the initialization of the internal states. The first time this VI runs, or when reset is TRUE, the internal states initialize to zero. If reset is FALSE, this VI sets the internal states to the final states from the previous call to the VI. The default is FALSE. |
| --- | --- |
|  | amp noise, if TRUE, specifies to add amplitude noise to the signal in the form of Gaussian-distributed, pseudorandom pattern. This VI uses the Gaussian White Noise VI to add amplitude noise. |
|  | amplitude levels sets the mapping of low and high logic levels to amplitude values. high value is the amplitude for a high logic value. The default is 1. low value is the amplitude for a low logic value. The default is 1. |
|  | high value is the amplitude for a high logic value. The default is 1. |
|  | low value is the amplitude for a low logic value. The default is 1. |
|  | sample settings controls the duration, frequency, and sample rate of the waveform you want to generate. duration (s) specifies the duration of the waveform you want to generate. This VI returns the actual duration and number of samples of the waveform in signal info. fc (Hz) specifies the clock frequency in Hz. sample rate (S/s) specifies the sampling rate for the signal in samples per second. |
|  | duration (s) specifies the duration of the waveform you want to generate. This VI returns the actual duration and number of samples of the waveform in signal info. |
|  | fc (Hz) specifies the clock frequency in Hz. |
|  | sample rate (S/s) specifies the sampling rate for the signal in samples per second. |
|  | signal type specifies the type of signal you want to this VI to generate. 0clock - square (default)—Create a clock signal whose cycles are square.1clock - sine—Creates a clock signal whose cycles are sinusoidal.2clock - wavetable—Creates a clock signal in which each cycle shape is determined by the wavetable input you specify.3data signal—Create a signal that streams the repeated sequence of bits in data stream. |
| 0 | clock - square (default)—Create a clock signal whose cycles are square. |
| 1 | clock - sine—Creates a clock signal whose cycles are sinusoidal. |
| 2 | clock - wavetable—Creates a clock signal in which each cycle shape is determined by the wavetable input you specify. |
| 3 | data signal—Create a signal that streams the repeated sequence of bits in data stream. |
|  | random jitter controls the Gaussian random components of the period jitter you want to inject. random jitter specifies the mean and standard deviation of a Gaussian noise component. When random jitter contains multiple elements, this VI applies the period jitter you specify to cycles in a repeating pattern. mean (s) is the mean of the Gaussian noise component. std rms (s) is the standard deviation of the Gaussian noise component. random seed controls the seeding of the random components. When random seed is greater than 0, LabVIEW reseeds the noise sample generator. The default is –1. |
|  | random jitter specifies the mean and standard deviation of a Gaussian noise component. When random jitter contains multiple elements, this VI applies the period jitter you specify to cycles in a repeating pattern. mean (s) is the mean of the Gaussian noise component. std rms (s) is the standard deviation of the Gaussian noise component. |
|  | mean (s) is the mean of the Gaussian noise component. |
|  | std rms (s) is the standard deviation of the Gaussian noise component. |
|  | random seed controls the seeding of the random components. When random seed is greater than 0, LabVIEW reseeds the noise sample generator. The default is –1. |
|  | deterministic jitter is an array of clusters whose elements are the parameters for each sine tone that is added to form the deterministic jitter to inject. frequency specifies the frequency of the sine tone in hertz. amplitude specifies the amplitude of the sine tone. phase specifies the initial phase of the sine tone in degrees. The default is 0. |
|  | frequency specifies the frequency of the sine tone in hertz. |
|  | amplitude specifies the amplitude of the sine tone. |
|  | phase specifies the initial phase of the sine tone in degrees. The default is 0. |
|  | ISI and DCD controls the simulated channel and duty cycle distortion. channel filter introduces inter-symbol interference into the waveform. bandwidth is the bandwidth of the channel lowpass filter, in normalized units of cycles/sample. The default is 0.5, which disables the simulated channel. type selects the type of filter to use in simulating a channel response. 0IIR (default)—Specifies to introduce nonlinear phase delays.1FIR—Specifies to generate linear phase with pure time delay. DCD (s) introduces duty-cycle distortion (DCD) into the waveform. A positive value compresses the amplitude of the low range of the signal, thus introducing positive DCD. A negative value compresses the high amplitude portion of the signal, thus introducing negative DCD. The default is 0. |
|  | channel filter introduces inter-symbol interference into the waveform. bandwidth is the bandwidth of the channel lowpass filter, in normalized units of cycles/sample. The default is 0.5, which disables the simulated channel. type selects the type of filter to use in simulating a channel response. 0IIR (default)—Specifies to introduce nonlinear phase delays.1FIR—Specifies to generate linear phase with pure time delay. |
|  | bandwidth is the bandwidth of the channel lowpass filter, in normalized units of cycles/sample. The default is 0.5, which disables the simulated channel. |
|  | type selects the type of filter to use in simulating a channel response. 0IIR (default)—Specifies to introduce nonlinear phase delays.1FIR—Specifies to generate linear phase with pure time delay. |
| 0 | IIR (default)—Specifies to introduce nonlinear phase delays. |
| 1 | FIR—Specifies to generate linear phase with pure time delay. |
|  | DCD (s) introduces duty-cycle distortion (DCD) into the waveform. A positive value compresses the amplitude of the low range of the signal, thus introducing positive DCD. A negative value compresses the high amplitude portion of the signal, thus introducing negative DCD. The default is 0. |
|  | wavetable contains one cycle of a custom clock waveform when signal type is clock - wavetable. The simulated clock signal linearly interpolates through cycles of this wavetable, where a range of [–1, +1] is mapped to the [low value, high value] settings specified by amplitude levels. |
|  | data stream contains the sequence of bits that LabVIEW repeats to construct the waveform when signal type is data signal. Zeros represent low logic values in the signal and ones represent high logic values. |
|  | waveform is the resulting waveform. t0 returns the trigger time of the waveform. dt returns the time interval in seconds between data points in the waveform. Y returns the data values of the waveform. |
|  | t0 returns the trigger time of the waveform. |
|  | dt returns the time interval in seconds between data points in the waveform. |
|  | Y returns the data values of the waveform. |
|  | signal info returns the duration and size of the resulting waveform. duration (s) returns the actual duration, in seconds, of the waveform. samples returns the actual number of samples in the waveform. |
|  | duration (s) returns the actual duration, in seconds, of the waveform. |
|  | samples returns the actual number of samples in the waveform. |
|  | PJ metrics returns characteristics of the periodic jitter in the waveform this VI generates. PJmin returns the amplitude of the tone with the smallest amplitude from periodic jitter. PJmax returns the amplitude of the tone with the greatest amplitude from periodic jitter. PJmean returns the average amplitude of tones from periodic jitter. PJrms returns the root mean square of tones from periodic jitter. |
|  | PJmin returns the amplitude of the tone with the smallest amplitude from periodic jitter. |
|  | PJmax returns the amplitude of the tone with the greatest amplitude from periodic jitter. |
|  | PJmean returns the average amplitude of tones from periodic jitter. |
|  | PJrms returns the root mean square of tones from periodic jitter. |

#### Examples

Refer to the following VIs for examples of using the Signal with Jitter VI:

- Simulated Signal with Jitter VI: labview\examples\Jitter Analysis\Jitter Measurements
- Rj Dj Separation VI: labview\examples\Jitter Analysis\Jitter Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/state_levels.html language=enus -->
## TOPIC 00049: State Levels VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/state_levels.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/state_levels.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### State Levels VI

**Owning Palette:** [Level VIs](../lvjitterphtk/level_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the high and low [state levels](/csh?topicname=lvwave/state_and_reference_levels.html) of a waveform and the corresponding amplitude. You can use state levels to identify the position in time of a waveform feature to be measured. Wire data to the **waveform** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

You also can use the Reference Levels (waveform in) instances of the [Reference Levels](../lvjitterphtk/reference_levels.html) VI to measure the state levels of a waveform.

|  | The terminology and measurement definitions for this VI comply with IEEE Standard 181-2003, IEEE Standard on Transitions, Pulses, and Related Waveforms. |
| --- | --- |

#### State Levels (DBL)

This instance operates on the waveform data type when the **Y** data values are double-precision, floating-point numeric values. Use the I8 instance of this VI with integer data to [reduce the size of the data and the memory usage](jat_overview.html#memory).

[IMAGE alt='image' src='state_levels.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | state levels settings sets the method this VI uses to determine the high and low state levels of a waveform. Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. |
|  | method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
| 0 | histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. |
| 1 | peak—Searches the entire waveform for its maximum and minimum levels. |
| 2 | auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails). |
| 3 | auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
|  | histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. |
|  | histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode |
| 0 | mode |
|  | search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | error out contains error information. This output provides standard error out functionality. |

#### State Levels (I8)

This instance operates on the waveform data type when the [Y data values are 8-bit signed integers](../lvjitterphtk/jat_overview.html#memory).

[IMAGE alt='image' src='state_levels.gif']

|  | waveform is the waveform to measure. t0 specifies the start time of the waveform. dt specifies the time interval in seconds between data points in the waveform. Y specifies the data values of the waveform. |
| --- | --- |
|  | t0 specifies the start time of the waveform. |
|  | dt specifies the time interval in seconds between data points in the waveform. |
|  | Y specifies the data values of the waveform. |
|  | state levels settings sets the method this VI uses to determine the high and low state levels of a waveform. Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | Note With any method you use to calculate state levels, very irregular waveforms might result in inaccurate state level measurements. In this case, manually specify state levels that are appropriate for the specific waveform. |
|  | method specifies how LabVIEW computes the high and low state levels of the waveform. 0histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform.1peak—Searches the entire waveform for its maximum and minimum levels.2auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails).3auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
| 0 | histogram (default)—Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. |
| 1 | peak—Searches the entire waveform for its maximum and minimum levels. |
| 2 | auto select—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails). |
| 3 | auto select independent—Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the hits within their respective regions. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the peak method. This ensures a reasonable answer when positive pulses in the waveform are much longer than negative pulses, and vice versa, such as when the waveform contains duty cycle distortion. |
|  | histogram size specifies the number of bins in the histogram LabVIEW uses to determine the high and low state levels of the waveform. If you select the peak method, LabVIEW ignores this input. |
|  | histogram method specifies how LabVIEW computes the high and low state levels of the waveform. Currently, mode is the only available histogram method. 0mode |
| 0 | mode |
|  | search width/total bins specifies the percent level of the waveform at which to set the upper boundary of the region that corresponds to the low state of the waveform and the lower boundary of the region that corresponds to the high state. LabVIEW uses the lesser of this value and 0.5. The default is 0.45.If you select the peak method, LabVIEW ignores this input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | waveform dup returns waveform unchanged. |
|  | state levels returns the state level information from the waveform. amplitude is the difference between high state level and low state level. high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | amplitude is the difference between high state level and low state level. |
|  | high state level returns the level at which a pulse or transition waveform is defined to be in its highest state. |
|  | low state level returns the level at which a pulse or transition waveform is defined to be in its lowest state |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/time_interval_error.html language=enus -->
## TOPIC 00050: Time Interval Error VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/time_interval_error.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/time_interval_error.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Time Interval Error VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Measures the differences between the positions in time of waveform level crossings and the times at which the corresponding level crossings occur in the reference clock.

[Examples](#examples)

[IMAGE alt='image' src='time_interval_error.gif']

|  | data in contains information about the data bit sequence between transitions in a waveform. You can use the Clock Recovery (Mean Clock) VI to generate this cluster. bit count specifies the number of bits between successive transitions in the waveform. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| --- | --- |
|  | bit count specifies the number of bits between successive transitions in the waveform. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | level crossings contains information about the locations of level crossings in the original waveform. You can use the Level Crossing VI to generate this cluster. t0 specifies the time at which the first sample occurs in the original waveform. dt specifies the time interval in seconds between the individual samples in the original waveform. indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the original waveform. |
|  | dt specifies the time interval in seconds between the individual samples in the original waveform. |
|  | indexes contains the index numbers of the samples in the waveform with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the waveform at each of the samples in indexes. |
|  | ref level crossings specifies information about the locations of level crossings in the reference clock waveform. You can use the Clock Recovery VIs to generate this cluster from a measured waveform. t0 specifies the time at which the first sample occurs in the clock signal. dt specifies the time interval in seconds between the individual samples in the clock signal. indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | t0 specifies the time at which the first sample occurs in the clock signal. |
|  | dt specifies the time interval in seconds between the individual samples in the clock signal. |
|  | indexes contains the index numbers of the samples in the clock signal with values that fall at the crossing level. |
|  | slope identifies the direction of the first transition in the waveform. -1Falling Edge—Specifies the transition is a falling edge, or one with a negative slope.1Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—Specifies the transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—Specifies the transition is a rising edge, or one with a positive slope. |
|  | crossing level specifies the value of the clock signal at each of the samples in indexes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | data out returns information about the data bit sequence between transitions in the waveform. bit count returns the number of bits between successive transitions. slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
|  | bit count returns the number of bits between successive transitions. |
|  | slope returns whether the direction of the transition is rising or falling. -1Falling Edge—The transition is a falling edge, or one with a negative slope.1Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
| -1 | Falling Edge—The transition is a falling edge, or one with a negative slope. |
| 1 | Rising Edge (default)—The transition is a rising edge, or one with a positive slope. |
|  | TIE sequence returns the time interval error measurements. |
|  | TIE timestamps returns timing information about the waveform that allows you to identify the times at which measurements in the corresponding sequence occur. t0 returns the time at which the first sample occurred in the original waveform. dt returns the time interval in seconds between the individual samples in the original waveform. indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | t0 returns the time at which the first sample occurred in the original waveform. |
|  | dt returns the time interval in seconds between the individual samples in the original waveform. |
|  | indexes returns the index numbers of samples in the measured waveform that fall on the crossing level. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Time Interval Error VI:

- Rj Dj Separation VI: labview\examples\Jitter Analysis\Jitter Measurements
- Rj Dj Delta Delta Separation VI: labview\examples\Jitter Analysis\Jitter Measurements

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/timing_pal.html language=enus -->
## TOPIC 00051: Timing VIs

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/timing_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/timing_pal.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Timing VIs

**Owning Palette:** [Jitter Analysis VIs](../lvjitterphtk/lvjitterphtk_pal.html)

**Requires:** Jitter Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Timing VIs to return information about the times and locations at which events in a signal occur.

The Timing VIs are useful both before and after you perform jitter measurements. For example, before you can measure jitter, you use the Level Crossing VI to identify a common position in transitions with which to measure jitter. After you identify jitter in a waveform, you can use other Timing VIs to measure additional aspects of signal integrity.

| Palette Object | Description |
| --- | --- |
| Burst Width | Measures the duration of each burst in a waveform, beginning when an edge in the waveform crosses a threshold level and ending when a subsequent edge crosses another threshold, with a minimum idle region on both sides of the burst. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Channel-to-Channel Skew | Measures the time differences between corresponding level crossings in two waveforms. The difference in times is also known as delay time, or skew. |
| Duty Cycle | Measures the percentages of the times that cycles in a waveform occur above and below the level at which a crossing occurs. This measurement is known as the duty cycle, or duty factor, of the waveform. |
| Fall Time | Measures the transition duration of falling transitions in a waveform. The duration of a falling transition, or fall time, is the difference in time between its start index and end index. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Level Crossing | Measures the times and locations a waveform crosses a particular voltage level. The Jitter Analysis VIs use level crossings to identify a common position in all transitions that you can use for comparison. Wire data to the transitions input and the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Negative Width | Measures the pulse duration that follows the level crossing in each falling transition. |
| Period | Measures the durations of portions of a waveform. Wire data to the rising/falling input to determine the polymorphic instance to use or manually select the instance. |
| Phase | Measures the differences in phase between corresponding cycles in two waveforms. |
| Positive Width | Measures the pulse duration that follows the level crossing in each rising transition. |
| Rise Time | Measures the transition duration of rising transitions in a waveform. The duration of a rising transition, or rise time, is the difference in time between its start index and end index. Wire data to the waveform input to determine the polymorphic instance to use or manually select the instance. |
| Setup and Hold Time | Measures the setup and hold times in a waveform. Setup time is the time difference between when a waveform falls on the crossing level and when a level crossing in a reference clock occurs. Hold time is the time difference between when a level crossing in a reference clock occurs and when a transition in a waveform falls on the crossing level. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/total_jitter.html language=enus -->
## TOPIC 00052: Total Jitter VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/total_jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/total_jitter.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Total Jitter VI

**Owning Palette:** [Jitter VIs](../lvjitterphtk/jitter_pal.html)

**Requires:** Jitter Analysis Toolkit

Computes the total jitter for the random and deterministic jitter levels you specify. The total jitter value is the amount of jitter that has a probability of being exceeded equal to the **BER limit** you specify.

[IMAGE alt='image' src='total_jitter.gif']

|  | random jitter specifies the amount of random jitter in the signal. |
| --- | --- |
|  | deterministic jitter specifies the amount of deterministic jitter in the signal. |
|  | BER limit specifies the minimum bit error rate (BER) for which you want to know the total jitter. The default is 1E–25. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | total jitter is the most jitter that results from the random and deterministic jitter at the BER limit. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-jitter-analysis-toolkit-api-ref path=lvjitterphtk/utility_pal.html language=enus -->
## TOPIC 00053: Signal Generation VI

- bundle_id: `labview-jitter-analysis-toolkit-api-ref`
- source_path: `lvjitterphtk/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-jitter-analysis-toolkit-api-ref/raw/resource/enus/lvjitterphtk/utility_pal.html
- document_id: `labview-jitter-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Signal Generation VI

**Owning Palette:** [Jitter Analysis VIs](../lvjitterphtk/lvjitterphtk_pal.html)

**Requires:** Jitter Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Signal with Jitter VI to generate signals you can use to test and debug jitter analysis applications.

| Palette Object | Description |
| --- | --- |
| Signal with Jitter | Creates a clock or data stream signal waveform and injects jitter into the signal. You can use this VI to create a waveform with which to test applications that measure jitter. |
