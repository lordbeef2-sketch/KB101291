# NI DOCUMENT BUNDLE: rfmxspecan-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxspecan-labview-api-ref start=251 end=304 -->
<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-configure-fft-vi.html language=enus -->
## TOPIC 00251: RFmxSpecAn OBW Configure FFT VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-configure-fft-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-configure-fft-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures window and FFT to obtain a spectrum for the occupied bandwidth (OBW) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default

### RFmxSpecAn OBW Configure FFT VI

Configures window and FFT to obtain a spectrum for the occupied bandwidth (OBW) measurement.

[IMAGE alt='icon' src='rfmxspecan-obw-configure-fft-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. FFT Window — FFT Window specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectral Measurements topic for more information about FFT window types. The default value is Flat Top. None (0) Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. Flat Top (1) Measures single-tone amplitudes accurately. Hanning (2) Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. Hamming (3) Analyzes closely-spaced sine waves. Gaussian (4) Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. Blackman (5) Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. Blackman-Harris (6) Useful as a general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. Kaiser-Bessel (7) Separates two tones with frequencies close to each other but with widely-differing amplitudes. FFT Padding — FFT Padding specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth. The default value is -1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| Flat Top (1) | Measures single-tone amplitudes accurately. |
| Hanning (2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| Hamming (3) | Analyzes closely-spaced sine waves. |
| Gaussian (4) | Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. |
| Blackman (5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| Blackman-Harris (6) | Useful as a general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| Kaiser-Bessel (7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-configure-span-vi.html language=enus -->
## TOPIC 00252: RFmxSpecAn OBW Configure Span VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-configure-span-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-configure-span-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range, in Hz, around the center frequency, to acquire for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The

### RFmxSpecAn OBW Configure Span VI

Configures the frequency range, in Hz, around the center frequency, to acquire for the measurement.

[IMAGE alt='icon' src='rfmxspecan-obw-configure-span-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Span (Hz) — Span specifies the frequency range, in Hz, around the center frequency, to acquire for the measurement. The default value is 1 MHz. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-fetch-vi.html language=enus -->
## TOPIC 00253: RFmxSpecAn OBW Fetch VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-fetch-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches occupied bandwidth (OBW) measurement results. icon

### RFmxSpecAn OBW Fetch VI

Fetches occupied bandwidth (OBW) measurement results.

[IMAGE alt='icon' src='rfmxspecan-obw-fetch-vi.png']

- [RFmxSpecAn OBW Fetch Measurement VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-fetch-measurement-vi.html) Returns the occupied bandwidth (OBW) measurement.
- [RFmxSpecAn OBW Fetch Spectrum Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-fetch-spectrum-trace-vi.html) Fetches the spectrum trace used for the OBW measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-interval-mode-vi.html language=enus -->
## TOPIC 00254: RFmxSpecAn PAVT Configure Measurement Interval Mode VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-interval-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-interval-mode-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement interval mode. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::s

### RFmxSpecAn PAVT Configure Measurement Interval Mode VI

Configures the measurement interval mode.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-measurement-interval-mode-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Interval Mode — Measurement Interval Mode specifies the mode of configuring the measurement interval. The default value is Uniform. Uniform (0) The time offset from the start of segment and the duration over which the measurement is performed is uniform for all segments and is given by the PAVT Meas Offset property and the PAVT Meas Length property respectively. Variable (1) The time offset from the start of segment and the duration over which the measurement is performed is configured separately for each segment and is given by the PAVT Segment Meas Offset property and the PAVT Segment Meas Length property respectively. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Uniform (0) | The time offset from the start of segment and the duration over which the measurement is performed is uniform for all segments and is given by the PAVT Meas Offset property and the PAVT Meas Length property respectively. |
| Variable (1) | The time offset from the start of segment and the duration over which the measurement is performed is configured separately for each segment and is given by the PAVT Segment Meas Offset property and the PAVT Segment Meas Length property respectively. |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-interval-vi.html language=enus -->
## TOPIC 00255: RFmxSpecAn PAVT Configure Measurement Interval VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-interval-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement offset and measurement length for the segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empt

### RFmxSpecAn PAVT Configure Measurement Interval VI

Configures the measurement offset and measurement length for the segments.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-measurement-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Offset (s) — Measurement Offset specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the PAVT Meas Interval Mode property to Uniform. The default value is 0. Measurement Length (s) — Measurement Length specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid when you set the PAVT Meas Interval Mode property to Uniform. The default value is 1 millisecond. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-location-type-vi.html language=enus -->
## TOPIC 00256: RFmxSpecAn PAVT Configure Measurement Location Type VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-location-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-measurement-location-type-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement location type for the segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examp

### RFmxSpecAn PAVT Configure Measurement Location Type VI

Configures the measurement location type for the segments.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-measurement-location-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Location Type — Measurement Location Type specifies whether the location at which the segment is measured is indicated by time or trigger. The default value is Time. Time (0) The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the PAVT Segment Start Time property. The number of segments is equal to the number of segment start times. Trigger (1) The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Time (0) | The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the PAVT Segment Start Time property. The number of segments is equal to the number of segment start times. |
| Trigger (1) | The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-number-of-segments-vi.html language=enus -->
## TOPIC 00257: RFmxSpecAn PAVT Configure Number of Segments VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-number-of-segments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-number-of-segments-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" Yo

### RFmxSpecAn PAVT Configure Number of Segments VI

Configures the number of segments.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-number-of-segments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Segments — Number of Segments specifies the number of segments to be measured. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-measurement-interval-array-vi.html language=enus -->
## TOPIC 00258: RFmxSpecAn PAVT Configure Segment Measurement Interval (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-measurement-interval-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-measurement-interval-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of segment measurement offsets and lengths for the segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is ""

### RFmxSpecAn PAVT Configure Segment Measurement Interval (Array) VI

Configures an array of segment measurement offsets and lengths for the segments.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-segment-measurement-interval-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Segment Measurement Offset (s) — Segment Measurement Offset specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the PAVT Meas Interval Mode property to Variable. The default value is 0. Segment Measurement Length (s) — Segment Measurement Length specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid when you set the PAVT Meas Interval Mode property to Variable. The default value is 1 millisecond. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PAVT Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-measurement-interval-vi.html language=enus -->
## TOPIC 00259: RFmxSpecAn PAVT Configure Segment Measurement Interval VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-measurement-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-measurement-interval-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the segment measurement offset and length for the segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and segment number. If you do not specify the signal name, the default signal instance is used. The default va

### RFmxSpecAn PAVT Configure Segment Measurement Interval VI

Configures the segment measurement offset and length for the segments.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-segment-measurement-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" You can use the RFmxSpecAn Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Segment Measurement Offset (s) — Segment Measurement Offset specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid only when you set the PAVT Meas Interval Mode property to Variable. The default value is 0. Segment Measurement Length (s) — Segment Measurement Length specifies the duration within each segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This property is valid when you set the PAVT Meas Interval Mode property to Variable. The default value is 1 millisecond. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-type-array-vi.html language=enus -->
## TOPIC 00260: RFmxSpecAn PAVT Configure Segment Type (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-type-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-type-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of segment types. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1"

### RFmxSpecAn PAVT Configure Segment Type (Array) VI

Configures an array of segment types.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-segment-type-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Segment Type — Segment Type specifies the type of segment. The default value is Phase and Amplitude. Phase and Amplitude (0) Phase and amplitude is measured in this segment. Amplitude (1) Amplitude is measured in this segment. Frequency Error Measurement (2) Frequency error is measured in this segment. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Phase and Amplitude (0) | Phase and amplitude is measured in this segment. |
| Amplitude (1) | Amplitude is measured in this segment. |
| Frequency Error Measurement (2) | Frequency error is measured in this segment. |

Parent topic:

PAVT Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-type-vi.html language=enus -->
## TOPIC 00261: RFmxSpecAn PAVT Configure Segment Type VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-configure-segment-type-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the segment type. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "si

### RFmxSpecAn PAVT Configure Segment Type VI

Configures the segment type.

[IMAGE alt='icon' src='rfmxspecan-pavt-configure-segment-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" You can use the RFmxSpecAn Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Segment Type — Segment Type specifies the type of segment. The default value is Phase and Amplitude. Phase and Amplitude (0) Phase and amplitude is measured in this segment. Amplitude (1) Amplitude is measured in this segment. Frequency Error Measurement (2) Frequency error is measured in this segment. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Phase and Amplitude (0) | Phase and amplitude is measured in this segment. |
| Amplitude (1) | Amplitude is measured in this segment. |
| Frequency Error Measurement (2) | Frequency error is measured in this segment. |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-amplitude-trace-vi.html language=enus -->
## TOPIC 00262: RFmxSpecAn PAVT Fetch Amplitude Trace VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-amplitude-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-amplitude-trace-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the amplitude trace for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name,

### RFmxSpecAn PAVT Fetch Amplitude Trace VI

Fetches the amplitude trace for the measurement.

[IMAGE alt='icon' src='rfmxspecan-pavt-fetch-amplitude-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Amplitude (dBm) — Amplitude returns the amplitude trace for the measurement. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the amplitude values of the complex baseband samples, in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the amplitude values of the complex baseband samples, in dBm. |

Parent topic:

RFmxSpecAn PAVT Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-array-vi.html language=enus -->
## TOPIC 00263: RFmxSpecAn PAVT Fetch Phase and Amplitude (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of mean values of phase and amplitude of the segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not sp

### RFmxSpecAn PAVT Fetch Phase and Amplitude (Array) VI

Fetches an array of mean values of phase and amplitude of the segments.

[IMAGE alt='icon' src='rfmxspecan-pavt-fetch-phase-and-amplitude-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Absolute Amplitude (dBm) — Mean Absolute Amplitude returns an array of the mean absolute amplitude of the segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Mean Relative Phase (deg) — Mean Relative Phase returns an array of the mean phase of the segment relative to the first segment of the measurement. This value is expressed in degrees. Mean Relative Amplitude (dB) — Mean Relative Amplitude returns an array of the mean amplitude of the segment relative to the first segment of the measurement. This value is expressed in dB. Mean Absolute Phase (deg) — Mean Absolute Phase returns an array of the mean absolute phase of the segment. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn PAVT Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-vi.html language=enus -->
## TOPIC 00264: RFmxSpecAn PAVT Fetch Phase and Amplitude VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean values of phase and amplitude of the segment. Use "segment<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not

### RFmxSpecAn PAVT Fetch Phase and Amplitude VI

Fetches the mean values of phase and amplitude of the segment.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxspecan-pavt-fetch-phase-and-amplitude-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxSpecAn Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Absolute Amplitude (dBm) — Mean Absolute Amplitude returns the mean absolute amplitude of the segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Mean Relative Phase (deg) — Mean Relative Phase returns the mean phase of the segment, relative to the phase of the reference segment. This value is expressed in degrees. Mean Relative Amplitude (dB) — Mean Relative Amplitude returns the mean amplitude of the segment, relative to the amplitude of the reference segment. This value is expressed in dB. Mean Absolute Phase (deg) — Mean Absolute Phase returns the mean absolute phase of the segment. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn PAVT Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-trace-vi.html language=enus -->
## TOPIC 00265: RFmxSpecAn PAVT Fetch Phase Trace VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-trace-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase trace for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the

### RFmxSpecAn PAVT Fetch Phase Trace VI

Fetches the phase trace for the measurement.

[IMAGE alt='icon' src='rfmxspecan-pavt-fetch-phase-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Phase (deg) — Phase returns the phase trace for the measurement. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the phase values of the complex baseband samples, in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the phase values of the complex baseband samples, in degrees. |

Parent topic:

RFmxSpecAn PAVT Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-vi.html language=enus -->
## TOPIC 00266: RFmxSpecAn PAVT Fetch VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase amplitude versus time (PAVT) measurement. icon

### RFmxSpecAn PAVT Fetch VI

Fetches the phase amplitude versus time (PAVT) measurement.

[IMAGE alt='icon' src='rfmxspecan-pavt-fetch-vi.png']

- [RFmxSpecAn PAVT Fetch Phase and Amplitude VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-vi.html) Fetches the mean values of phase and amplitude of the segment.
- [RFmxSpecAn PAVT Fetch Phase and Amplitude (Array) VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-and-amplitude-array-vi.html) Fetches an array of mean values of phase and amplitude of the segments.
- [RFmxSpecAn PAVT Fetch Phase Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-phase-trace-vi.html) Fetches the phase trace for the measurement.
- [RFmxSpecAn PAVT Fetch Amplitude Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-pavt-fetch-amplitude-trace-vi.html) Fetches the amplitude trace for the measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-configure-auto-range-vi.html language=enus -->
## TOPIC 00267: RFmxSpecAn PhaseNoise Configure Auto Range VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-configure-auto-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-configure-auto-range-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset range and the RBW percentage when you set the PhaseNoise Range Definition property to Auto. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxSpecAn PhaseNoise Configure Auto Range VI

Configures the offset range and the RBW percentage when you set the [PhaseNoise Range Definition](/csh?context=rfmxspecan_rfmxspecanprop_attr130002) property to **Auto**.

[IMAGE alt='icon' src='rfmxspecan-phasenoise-configure-auto-range-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Start Frequency (Hz) — Start Frequency specifies the start frequency of the offset frequency range when you set the PhaseNoise Range Definition property to Auto. This value is expressed in Hz. The default value is 1000. Stop Frequency (Hz) — Stop Frequency specifies the stop frequency of the offset frequency range when you set the PhaseNoise Range Definition property to Auto. This value is expressed in Hz. The default value is 1000000. RBW Percentage (%) — RBW Percentage specifies the RBW as a percentage of the start frequency of each subrange when you set the PhaseNoise Range Definition property to Manual. This value is expressed as a percentage. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-configure-averaging-multiplier-vi.html language=enus -->
## TOPIC 00268: RFmxSpecAn PhaseNoise Configure Averaging Multiplier VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-configure-averaging-multiplier-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-configure-averaging-multiplier-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the averaging multiplier. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1"

### RFmxSpecAn PhaseNoise Configure Averaging Multiplier VI

Configures the averaging multiplier.

[IMAGE alt='icon' src='rfmxspecan-phasenoise-configure-averaging-multiplier-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Multiplier — Averaging Multiplier specifies the factor by which you increase the averaging count for each range. This setting applies to both Auto and Manual range definitions. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-measured-log-plot-trace-vi.html language=enus -->
## TOPIC 00269: RFmxSpecAn PhaseNoise Fetch Measured Log Plot Trace VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-measured-log-plot-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-measured-log-plot-trace-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the log plot trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result in

### RFmxSpecAn PhaseNoise Fetch Measured Log Plot Trace VI

Fetches the log plot trace.

[IMAGE alt='icon' src='rfmxspecan-phasenoise-fetch-measured-log-plot-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Frequency (Hz) — Frequency returns an array of the frequency offsets where phase noise has been measured. Measured Phase Noise (dBc/Hz) — Measured Phase Noise returns an array of measured phase noise at the frequency offset. This value is expressed in dBc/Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn PhaseNoise Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-smoothed-log-plot-trace-vi.html language=enus -->
## TOPIC 00270: RFmxSpecAn PhaseNoise Fetch Smoothed Log Plot Trace VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-smoothed-log-plot-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-smoothed-log-plot-trace-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the smoothened log plot trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defaul

### RFmxSpecAn PhaseNoise Fetch Smoothed Log Plot Trace VI

Fetches the smoothened log plot trace.

[IMAGE alt='icon' src='rfmxspecan-phasenoise-fetch-smoothed-log-plot-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Frequency (Hz) — Frequency returns an array of the frequency offsets where phase noise has been measured. Smoothed Phase Noise (dBc/Hz) — Smoothed Phase Noise returns an array of smoothed phase noise at the frequency offset. This value is expressed in dBc/Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn PhaseNoise Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-spot-noise-vi.html language=enus -->
## TOPIC 00271: RFmxSpecAn PhaseNoise Fetch Spot Noise VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-spot-noise-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-spot-noise-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spot noise. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instan

### RFmxSpecAn PhaseNoise Fetch Spot Noise VI

Fetches the spot noise.

[IMAGE alt='icon' src='rfmxspecan-phasenoise-fetch-spot-noise-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Spot Phase Noise (dBc/Hz) — Spot Phase Noise returns the phase noise corresponding to the value of the PhaseNoise Spot Noise Freq List property, by using the smoothed log plot trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn PhaseNoise Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-vi.html language=enus -->
## TOPIC 00272: RFmxSpecAn PhaseNoise Fetch VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase noise measurements. icon

### RFmxSpecAn PhaseNoise Fetch VI

Fetches the phase noise measurements.

[IMAGE alt='icon' src='rfmxspecan-phasenoise-fetch-vi.png']

- [RFmxSpecAn PhaseNoise Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-carrier-measurement-vi.html) Fetches the carrier measurement.
- [RFmxSpecAn PhaseNoise Fetch Spot Noise VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-spot-noise-vi.html) Fetches the spot noise.
- [RFmxSpecAn PhaseNoise Fetch Integrated Noise VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-integrated-noise-vi.html) Fetches the integrated noise measurement.
- [RFmxSpecAn PhaseNoise Fetch Measured Log Plot Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-measured-log-plot-trace-vi.html) Fetches the log plot trace.
- [RFmxSpecAn PhaseNoise Fetch Smoothed Log Plot Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-phasenoise-fetch-smoothed-log-plot-trace-vi.html) Fetches the smoothened log plot trace.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-powerlist-fetch-maximum-power-array-vi.html language=enus -->
## TOPIC 00273: RFmxSpecAn PowerList Fetch Maximum Power (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-powerlist-fetch-maximum-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-powerlist-fetch-maximum-power-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum power of all segments measured using the PowerList measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If y

### RFmxSpecAn PowerList Fetch Maximum Power (Array) VI

Returns the maximum power of all segments measured using the PowerList measurement.

[IMAGE alt='icon' src='rfmxspecan-powerlist-fetch-maximum-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Maximum Power (dBm) — Maximum Power returns an array of maximum power in dBm for each segment. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn PowerList Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-powerlist-fetch-mean-absolute-power-array-vi.html language=enus -->
## TOPIC 00274: RFmxSpecAn PowerList Fetch Mean Absolute Power (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-powerlist-fetch-mean-absolute-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-powerlist-fetch-mean-absolute-power-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean absolute power of all segments measured using the PowerList measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used

### RFmxSpecAn PowerList Fetch Mean Absolute Power (Array) VI

Returns the mean absolute power of all segments measured using the PowerList measurement.

[IMAGE alt='icon' src='rfmxspecan-powerlist-fetch-mean-absolute-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Mean Absolute Power (dBm) — Mean Absolute Power returns an array of mean absolute power, in dBm for each segment. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn PowerList Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-read-vi.html language=enus -->
## TOPIC 00275: RFmxSpecAn Read VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-read-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns measurement results. icon

### RFmxSpecAn Read VI

Configures hardware for acquisition, performs measurement on acquired data, and returns measurement results.

[IMAGE alt='icon' src='rfmxspecan-read-vi.png']

- [RFmxSpecAn ACP Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-acp-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns the adjacent channel power (ACP) measurement results.
- [RFmxSpecAn CCDF Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-ccdf-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns complementary cumulative distribution function (CCDF) measurement results.
- [RFmxSpecAn CHP Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-chp-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns the channel power (CHP) measurement results.
- [RFmxSpecAn FCnt Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-fcnt-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns the frequency count (FCnt) measurement results.
- [RFmxSpecAn Harm Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-harm-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns Harmonics measurement results.
- [RFmxSpecAn OBW Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-obw-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns occupied bandwidth (OBW) measurement results.
- [RFmxSpecAn Spectrum Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spectrum-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns Spectrum measurement results.
- [RFmxSpecAn TXP Read VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-read-vi.html) Configures hardware for acquisition, performs measurement on acquired data, and returns the transmit power (TXP) measurement results.

Parent topic:

SpecAn

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-absolute-limit-array-vi.html language=enus -->
## TOPIC 00276: RFmxSpecAn Spur Configure Range Absolute Limit (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-absolute-limit-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-absolute-limit-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the absolute power limits corresponding to the beginning and end of the frequency range and specifies whether the absolute limit threshold is a flat line or a line with a slope. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies

### RFmxSpecAn Spur Configure Range Absolute Limit (Array) VI

Configures the absolute power limits corresponding to the beginning and end of the frequency range and specifies whether the absolute limit threshold is a flat line or a line with a slope.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-absolute-limit-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Absolute Limit Mode — Absolute Limit Mode specifies whether the absolute limit threshold is a flat line or a line with a slope. The default value is Couple. Manual (0) The line specified by the Spur Range Abs Limit Start and Spur Range Abs Limit Stop property values as the two ends is considered as the mask. Couple (1) The two ends of the line are coupled to the value of the Spur Range Abs Limit Start property. Absolute Limit Start (dBm) — Absolute Limit Start specifies the array of absolute power limits, in dBm, corresponding to the beginning of the frequency range. The value of this parameter is also set as the absolute power limit for the range when you set the Absolute Limit Mode parameter to Couple. The default value is -10. Absolute Limit Stop (dBm) — Absolute Limit Stop specifies the array of absolute power limits, in dBm, corresponding to the end of the frequency range. This parameter is ignored when you set the Absolute Limit Mode parameter to Couple. The default value is -10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Manual (0) | The line specified by the Spur Range Abs Limit Start and Spur Range Abs Limit Stop property values as the two ends is considered as the mask. |
| Couple (1) | The two ends of the line are coupled to the value of the Spur Range Abs Limit Start property. |

Parent topic:

Spur Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-absolute-limit-vi.html language=enus -->
## TOPIC 00277: RFmxSpecAn Spur Configure Range Absolute Limit VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-absolute-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-absolute-limit-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the absolute power limits corresponding to the beginning and end of the frequency range. Use "range<n>" as the selector string to configure this VI. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising

### RFmxSpecAn Spur Configure Range Absolute Limit VI

Configures the absolute power limits corresponding to the beginning and end of the frequency range.

Use "range<*n*>" as the selector string to configure this VI.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-absolute-limit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0". Example: "range0" "signal::sig1/range0" You can use the RFmxSpecAn Build Range String2 VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Absolute Limit Mode — Absolute Limit Mode specifies whether the absolute limit threshold is a flat line or a line with a slope. The default value is Couple. Manual (0) The line specified by the Spur Range Abs Limit Start and Spur Range Abs Limit Stop property values as the two ends is considered as the mask. Couple (1) The two ends of the line are coupled to the value of the Spur Range Abs Limit Start property. Absolute Limit Start (dBm) — Absolute Limit Start specifies the absolute power limit, in dBm, corresponding to the beginning of the frequency range. The value of this parameter is also set as the absolute power limit for the range when you set the Absolute Limit Mode parameter to Couple. The default value is -10. Absolute Limit Stop (dBm) — Absolute Limit Stop specifies the absolute power limit, in dBm, corresponding to the end of the frequency range. This parameter is ignored when you set the Absolute Limit Mode parameter to Couple. The default value is -10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Manual (0) | The line specified by the Spur Range Abs Limit Start and Spur Range Abs Limit Stop property values as the two ends is considered as the mask. |
| Couple (1) | The two ends of the line are coupled to the value of the Spur Range Abs Limit Start property. |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-detector-array-vi.html language=enus -->
## TOPIC 00278: RFmxSpecAn Spur Configure Range Detector (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-detector-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-detector-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the detector settings including detector type and the number of points to be detected. Refer to Spectral Measurements topic for more information on detector types. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal

### RFmxSpecAn Spur Configure Range Detector (Array) VI

Configures an array of the detector settings including detector type and the number of points to be detected.

Refer to [Spectral Measurements](/csh?context=rfmxspecan_rfmxspecan_spectral_measurements_concepts) topic for more information on detector types.

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-detector-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Detector Type — Detector Type specifies the type of detector to be used. The default value is None. Refer to Spectral Measurements topic for more information on detectors. None (0) The detector is disabled. Sample (1) The middle sample in the bucket is detected. Normal (2) The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. Peak (3) The maximum value of the samples in the bucket is detected. Negative Peak (4) The minimum value of the samples in the bucket is detected. Average RMS (5) The average RMS of all the samples in the bucket is detected. Average Voltage (6) The average voltage of all the samples in the bucket is detected. Average Log (7) The average log of all the samples in the bucket is detected. Detector Points — Detector Points specifies an array of the number of points after the detector is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | The detector is disabled. |
| Sample (1) | The middle sample in the bucket is detected. |
| Normal (2) | The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. |
| Peak (3) | The maximum value of the samples in the bucket is detected. |
| Negative Peak (4) | The minimum value of the samples in the bucket is detected. |
| Average RMS (5) | The average RMS of all the samples in the bucket is detected. |
| Average Voltage (6) | The average voltage of all the samples in the bucket is detected. |
| Average Log (7) | The average log of all the samples in the bucket is detected. |

Parent topic:

Spur Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-detector-vi.html language=enus -->
## TOPIC 00279: RFmxSpecAn Spur Configure Range Detector VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-detector-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-detector-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the detector settings including detector type and the number of points to be detected. Use "range<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and range number. If yo

### RFmxSpecAn Spur Configure Range Detector VI

Configures the detector settings including detector type and the number of points to be detected.

Use "range<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-detector-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0". Example: "range0" "signal::sig1/range0" You can use the RFmxSpecAn Build Range String2 VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Detector Type — Detector Type specifies the type of detector to be used. The default value is None. Refer to Spectral Measurements topic for more information on detectors. None (0) The detector is disabled. Sample (1) The middle sample in the bucket is detected. Normal (2) The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. Peak (3) The maximum value of the samples in the bucket is detected. Negative Peak (4) The minimum value of the samples in the bucket is detected. Average RMS (5) The average RMS of all the samples in the bucket is detected. Average Voltage (6) The average voltage of all the samples in the bucket is detected. Average Log (7) The average log of all the samples in the bucket is detected. Detector Points — Detector Points specifies the number of points after the detector is applied. The default value is 1001. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | The detector is disabled. |
| Sample (1) | The middle sample in the bucket is detected. |
| Normal (2) | The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. |
| Peak (3) | The maximum value of the samples in the bucket is detected. |
| Negative Peak (4) | The minimum value of the samples in the bucket is detected. |
| Average RMS (5) | The average RMS of all the samples in the bucket is detected. |
| Average Voltage (6) | The average voltage of all the samples in the bucket is detected. |
| Average Log (7) | The average log of all the samples in the bucket is detected. |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-frequency-array-vi.html language=enus -->
## TOPIC 00280: RFmxSpecAn Spur Configure Range Frequency (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-frequency-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-frequency-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency start and stop values and specifies whether to enable measurement of the spurious emissions (Spur) in the frequency range. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signa

### RFmxSpecAn Spur Configure Range Frequency (Array) VI

Configures the frequency start and stop values and specifies whether to enable measurement of the spurious emissions (Spur) in the frequency range.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-frequency-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Start Frequency (Hz) — Start Frequency specifies the array of start frequencies of the frequency range, in Hz, for the measurement. The default value is 500 MHz. Stop Frequency (Hz) — Stop Frequency specifies the array of stop frequencies of the frequency range, in Hz, for the measurement. The default value is 1.5 GHz. Range Enabled — Range Enabled specifies whether to measure the Spur in the frequency range. The default value is True. False (0) Disables the acquisition of the frequency range. True (1) Enables measurement of Spurs in the frequency range. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables the acquisition of the frequency range. |
| True (1) | Enables measurement of Spurs in the frequency range. |

Parent topic:

Spur Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-frequency-vi.html language=enus -->
## TOPIC 00281: RFmxSpecAn Spur Configure Range Frequency VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-frequency-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency start and stop values of the range. Use "range<n>" as the selector string to configure this VI. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and range number. If

### RFmxSpecAn Spur Configure Range Frequency VI

Configures the frequency start and stop values of the range.

Use "range<*n*>" as the selector string to configure this VI.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0". Example: "range0" "signal::sig1/range0" You can use the RFmxSpecAn Build Range String2 VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Start Frequency (Hz) — Start Frequency specifies the start of the frequency range, in Hz, for the measurement. The default value is 500 MHz. Stop Frequency (Hz) — Stop Frequency specifies the stop of the frequency range, in Hz, for the measurement. The default value is 1.5 GHz. Range Enabled — Range Enabled specifies whether to measure the Spurs in the frequency range. The default value is True. False (0) Disables the acquisition of the frequency range. True (1) Enables measurement of Spurs in the frequency range. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables the acquisition of the frequency range. |
| True (1) | Enables measurement of Spurs in the frequency range. |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-number-of-spurs-to-report-array-vi.html language=enus -->
## TOPIC 00282: RFmxSpecAn Spur Configure Range Number of Spurs to Report (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-number-of-spurs-to-report-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-number-of-spurs-to-report-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of Spurs that the measurement should report in the frequency range. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default

### RFmxSpecAn Spur Configure Range Number of Spurs to Report (Array) VI

Specifies the number of Spurs that the measurement should report in the frequency range.

**Supported devices:**
 PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-number-of-spurs-to-report-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Spurs to Report — Number of Spurs to Report specifies the array of number of Spurs that the measurement should report in the frequency range. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Spur Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-number-of-spurs-to-report-vi.html language=enus -->
## TOPIC 00283: RFmxSpecAn Spur Configure Range Number of Spurs to Report VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-number-of-spurs-to-report-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-number-of-spurs-to-report-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of Spurs that the measurement should report in the frequency range. Use "range< n >" as the selector string to configure this VI. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the si

### RFmxSpecAn Spur Configure Range Number of Spurs to Report VI

Specifies the number of Spurs that the measurement should report in the frequency range.

Use "range<
 *n*
 >" as the selector string to configure this VI.

**Supported devices:**
 PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-number-of-spurs-to-report-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0". Example: "range0" "signal::sig1/range0" You can use the RFmxSpecAn Build Range String2 VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Spurs to Report — Number of Spurs to Report specifies the number of Spurs that the measurement should report in the frequency range. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-peak-criteria-array-vi.html language=enus -->
## TOPIC 00284: RFmxSpecAn Spur Configure Range Peak Criteria (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-peak-criteria-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-peak-criteria-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures arrays of peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur). icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the

### RFmxSpecAn Spur Configure Range Peak Criteria (Array) VI

Configures arrays of peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur).

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-peak-criteria-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Threshold (dBm) — Threshold specifies the array of threshold levels, in dBm, above which the measurement detects spurs in the range. The default value is -200. Excursion (dB) — Excursion specifies the array of peak excursion values, in dB, used to find the spurs in the spectrum. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered as a spur. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Spur Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-rbw-array-vi.html language=enus -->
## TOPIC 00285: RFmxSpecAn Spur Configure Range RBW (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-rbw-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-rbw-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default va

### RFmxSpecAn Spur Configure Range RBW (Array) VI

Configures the resolution bandwidth (RBW) filter.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-rbw-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement computes the RBW. Refer to the Spectrum topic for details on RBW and sweep time. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. RBW (Hz) — RBW specifies the array of bandwidths, in Hz, of the RBW filter used to sweep the acquired range, when you set the RBW Auto parameter to False. The default value is 10 kHz. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

Spur Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-relative-attenuation-vi.html language=enus -->
## TOPIC 00286: RFmxSpecAn Spur Configure Range Relative Attenuation VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-relative-attenuation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-relative-attenuation-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation, in dB, relative to the external attenuation. Use "range<n>" as the selector string to configure this VI. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and range

### RFmxSpecAn Spur Configure Range Relative Attenuation VI

Specifies the attenuation, in dB, relative to the external attenuation.

Use "range<*n*>" as the selector string to configure this VI.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-relative-attenuation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0". Example: "range0" "signal::sig1/range0" You can use the RFmxSpecAn Build Range String2 VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Relative Attenuation (dB) — Relative Attenuation specifies the attenuation, in dB, relative to the external attenuation. Use this parameter to compensate for variations in external attenuation when the offset channels are spread wide in frequency. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-sweep-time-array-vi.html language=enus -->
## TOPIC 00287: RFmxSpecAn Spur Configure Range Sweep Time (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-sweep-time-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-configure-range-sweep-time-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Supported devices: PXIe-5665, PXIe-5668 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string

### RFmxSpecAn Spur Configure Range Sweep Time (Array) VI

Configures the sweep time.

**Supported devices:** PXIe-5665, PXIe-5668

[IMAGE alt='icon' src='rfmxspecan-spur-configure-range-sweep-time-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Spur Range Sweep Time property. True (1) The measurement calculates the sweep time based on the value of the Spur Range RBW property. Sweep Time Interval (s) — Sweep Time Interval specifies the array of sweep times, in seconds, when you set the Sweep Time Auto parameter to False. The default value is 1 ms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify in the Spur Range Sweep Time property. |
| True (1) | The measurement calculates the sweep time based on the value of the Spur Range RBW property. |

Parent topic:

Spur Array VIs

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-range-status-array-vi.html language=enus -->
## TOPIC 00288: RFmxSpecAn Spur Fetch Range Status (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-range-status-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-range-status-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the range status for Spur measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, t

### RFmxSpecAn Spur Fetch Range Status (Array) VI

Fetches the range status for Spur measurements.

[IMAGE alt='icon' src='rfmxspecan-spur-fetch-range-status-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Range Status — Range Status indicates the array of measurement statuses for each frequency range. Number of Detected Spurs — Number of Detected Spurs returns the array of number of detected spurious emissions (Spur) in each frequency range. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn Spur Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-array-vi.html language=enus -->
## TOPIC 00289: RFmxSpecAn Spur Fetch Spur Measurement (Array) VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-array-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the information of Spurs in the range. Use "range<n>" as the active channel string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and range number. If you do not specify the si

### RFmxSpecAn Spur Fetch Spur Measurement (Array) VI

Fetches the information of Spurs in the range.

Use "range<n>" as the active channel string to read results from this VI.

[IMAGE alt='icon' src='rfmxspecan-spur-fetch-spur-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and range number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "range0" "signal::sig1/range0" "signal::sig1/result::r1/range0" "result::r1/range0" You can use the RFmxSpecAn Build Range String2 VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Spur Margin (dB) — Spur Margin returns the array of differences between the spur amplitude and the absolute limit at the spur frequency. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spur Frequency (Hz) — Spur Frequency returns the array of frequencies, in Hz, of the detected spurs. Spur Amplitude (dBm) — Spur Amplitude returns the array of powers, in dBm, of the detected spurs. Spur Absolute Limit (dBm) — Spur Absolute Limit returns the array of thresholds, in dBm, used to calculate the margin of the detected spurs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn Spur Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-vi.html language=enus -->
## TOPIC 00290: RFmxSpecAn Spur Fetch Spur Measurement VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the information of Spurs in the range. Use "range<n>/spur<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, range number, and spur number. If you do not

### RFmxSpecAn Spur Fetch Spur Measurement VI

Fetches the information of Spurs in the range.

Use "range<n>/spur<k>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxspecan-spur-fetch-spur-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, range number, and spur number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "range0/spur0" "signal::sig1/range0/spur0" "signal::sig1/result::r1/range0/spur0" "result::r1/range0/spur0" You can use the RFmxSpecAn Build Spur String2 VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Spur Absolute Limit (dBm) — Spur Absolute Limit returns the threshold, in dBm, used to calculate the margin of the detected spur. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spur Frequency (Hz) — Spur Frequency returns the frequency, in Hz, of the detected spur. Spur Amplitude (dBm) — Spur Amplitude returns the power, in dBm, of the detected spur. Spur Margin (dB) — Spur Margin returns the difference between the spur amplitude and the absolute limit at the spur frequency. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn Spur Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-vi.html language=enus -->
## TOPIC 00291: RFmxSpecAn Spur Fetch VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches spurious emission (spur) measurement results. icon

### RFmxSpecAn Spur Fetch VI

Fetches spurious emission (spur) measurement results.

[IMAGE alt='icon' src='rfmxspecan-spur-fetch-vi.png']

- [RFmxSpecAn Spur Fetch All Spurs VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-all-spurs-vi.html) Fetches all the spurs across all ranges.
- [RFmxSpecAn Spur Fetch Measurement Status VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-measurement-status-vi.html) Indicates the overall Spur measurement status.
- [RFmxSpecAn Spur Fetch Spur Measurement VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-vi.html) Fetches the information of Spurs in the range.
- [RFmxSpecAn Spur Fetch Range Status VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-range-status-vi.html) Fetches the range status for Spur measurements.
- [RFmxSpecAn Spur Fetch Spur Measurement (Array) VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-spur-measurement-array-vi.html) Fetches the information of Spurs in the range.
- [RFmxSpecAn Spur Fetch Range Status (Array) VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-range-status-array-vi.html) Fetches the range status for Spur measurements.
- [RFmxSpecAn Spur Fetch Range Absolute Limit Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-range-absolute-limit-trace-vi.html) Fetches the absolute limit line used in the range.
- [RFmxSpecAn Spur Fetch Range Spectrum Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-spur-fetch-range-spectrum-trace-vi.html) Fetches the measured range spectrum trace. You can fetch traces only for the range index specified by the Spur Trace Range Index property.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-averaging-vi.html language=enus -->
## TOPIC 00292: RFmxSpecAn TXP Configure Averaging VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-averaging-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the transmit power (TXP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). E

### RFmxSpecAn TXP Configure Averaging VI

Configures averaging for the transmit power (TXP) measurement.

[IMAGE alt='icon' src='rfmxspecan-txp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power trace is averaged in a logarithmic scale. Scalar (2) The square root of the power trace is averaged. Max (3) The peak power in the power trace at each sample instance is retained from one acquisition to the next. Min (4) The least power in the power trace at each sample instance is retained from one acquisition to the next. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter to calculate the number of acquisitions over which the measurement is averaged. |
| RMS (0) | The power trace is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power trace is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power trace is averaged. |
| Max (3) | The peak power in the power trace at each sample instance is retained from one acquisition to the next. |
| Min (4) | The least power in the power trace at each sample instance is retained from one acquisition to the next. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-measurement-interval-vi.html language=enus -->
## TOPIC 00293: RFmxSpecAn TXP Configure Measurement Interval VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-measurement-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-measurement-interval-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition time, in seconds, for the transmit power (TXP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value

### RFmxSpecAn TXP Configure Measurement Interval VI

Specifies the acquisition time, in seconds, for the transmit power (TXP) measurement.

[IMAGE alt='icon' src='rfmxspecan-txp-configure-measurement-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Interval (s) — Measurement Interval specifies the acquisition time, in seconds, for the measurement. The default value is 1 ms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00294: RFmxSpecAn TXP Configure RBW Filter VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-rbw-filter-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxSpecAn TXP Configure RBW Filter VI

Configures the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter.

[IMAGE alt='icon' src='rfmxspecan-txp-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW (Hz) — RBW specifies the bandwidth, in Hz, of the resolution bandwidth (RBW) filter used to measure the signal. The default value is 100 kHz. — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. None (1) The measurement does not use any RBW filtering. Gaussian (2) The RBW filter has a Gaussian response. Flat (3) The RBW filter has a flat response. RRC (4) The RRC filter with the roll-off specified by RRC Alpha parameter is used as the RBW filter. RRC Alpha — RRC Alpha specifies the roll-off factor for the root-raised-cosine (RRC) filter. The default value is 0.1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (1) | The measurement does not use any RBW filtering. |
| Gaussian (2) | The RBW filter has a Gaussian response. |
| Flat (3) | The RBW filter has a flat response. |
| RRC (4) | The RRC filter with the roll-off specified by RRC Alpha parameter is used as the RBW filter. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-threshold-vi.html language=enus -->
## TOPIC 00295: RFmxSpecAn TXP Configure Threshold VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-threshold-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-threshold-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the threshold level for the samples that need to be considered for the transmit power (TXP) measurement. Enable the threshold when analyzing burst signals or signals with dead time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the

### RFmxSpecAn TXP Configure Threshold VI

Configures the threshold level for the samples that need to be considered for the transmit power (TXP) measurement. Enable the threshold when analyzing burst signals or signals with dead time.

[IMAGE alt='icon' src='rfmxspecan-txp-configure-threshold-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Threshold Enabled — Threshold Enabled specifies whether to enable thresholding of the acquired samples to be used for the measurement. The default value is False. False (0) All samples are considered for the measurement. True (1) The samples above the threshold level specified in the Threshold Level parameter are considered for the measurement. Threshold Level (dB or dBm) — Threshold Level specifies either the relative or absolute threshold power level based on the value of the Threshold Type parameter. The default value is -20 dB. Threshold Type — Threshold Type specifies the reference for the power level used for thresholding. The default value is Relative. Relative (0) The threshold is relative to the peak power, in dB, of the acquired samples. Absolute (1) The threshold is the absolute power, in dBm. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | All samples are considered for the measurement. |
| True (1) | The samples above the threshold level specified in the Threshold Level parameter are considered for the measurement. |
| Relative (0) | The threshold is relative to the peak power, in dB, of the acquired samples. |
| Absolute (1) | The threshold is the absolute power, in dBm. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-vbw-filter-vi.html language=enus -->
## TOPIC 00296: RFmxSpecAn TXP Configure VBW Filter VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-vbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-configure-vbw-filter-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures VBW settings including the VBW mode, video bandwidth (VBW), and the VBW to RBW ratio. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The def

### RFmxSpecAn TXP Configure VBW Filter VI

Configures VBW settings including the VBW mode, video bandwidth (VBW), and the VBW to RBW ratio.

[IMAGE alt='icon' src='rfmxspecan-txp-configure-vbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. VBW Auto — VBW Auto specifies whether the VBW is expressed directly or computed based on VBW to RBW ratio. The default value is True. False (0) Specify the video bandwidth in the VBW parameter. The VBW to RBW Ratio parameter is disregarded in this mode. True (1) Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the TXP VBW to RBW Ratio property and the TXP RBW property. The value of the VBW parameter is disregarded in this mode. VBW (Hz) — VBW specifies the video bandwidth when you set the VBW Auto parameter to False. This value is expressed in Hz. The default value is 30KHz. VBW to RBW Ratio — VBW to RBW Ratio specifies the VBW to RBW Ratio when you set the VBW Auto parameter to True. The default value is 3. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Specify the video bandwidth in the VBW parameter. The VBW to RBW Ratio parameter is disregarded in this mode. |
| True (1) | Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the TXP VBW to RBW Ratio property and the TXP RBW property. The value of the VBW parameter is disregarded in this mode. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-measurement-vi.html language=enus -->
## TOPIC 00297: RFmxSpecAn TXP Fetch Measurement VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-measurement-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the powers measured using the TXP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result

### RFmxSpecAn TXP Fetch Measurement VI

Returns the powers measured using the TXP measurement.

[IMAGE alt='icon' src='rfmxspecan-txp-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Minimum Power (dBm) — Minimum Power returns the minimum power, in dBm, of the averaged power trace. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Average Mean Power (dBm) — Average Mean Power returns the mean power, in dBm, of the signal. Only the samples above the threshold are used by the measurement when you set the TXP Threshold Enabled property to True. When you set the TXP Averaging Enabled property to True, the mean power is measured on the power trace averaged over multiple acquisitions. Peak to Average Ratio (dB) — Peak to Average Ratio returns the ratio of the peak power of the signal to the mean power. Only the samples above the threshold are used by the measurement when you set the TXP Threshold Enabled property to True. When you set the TXP Averaging Enabled property to True, the peak and mean powers are measured using the power trace averaged over multiple acquisitions. Maximum Power (dBm) — Maximum Power returns the maximum power, in dBm, of the averaged power trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn TXP Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-power-trace-vi.html language=enus -->
## TOPIC 00298: RFmxSpecAn TXP Fetch Power Trace VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-power-trace-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power trace used for the transmit power (TxP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not spe

### RFmxSpecAn TXP Fetch Power Trace VI

Fetches the power trace used for the transmit power (TxP) measurement.

[IMAGE alt='icon' src='rfmxspecan-txp-fetch-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Power (dBm) — Power returns the power versus time trace. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the measured average power, in units specified by Spectrum Power Units property, at each time instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns the measured average power, in units specified by Spectrum Power Units property, at each time instance. |

Parent topic:

RFmxSpecAn TXP Fetch VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-vi.html language=enus -->
## TOPIC 00299: RFmxSpecAn TXP Fetch VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches transmit power (TXP) measurement results. icon

### RFmxSpecAn TXP Fetch VI

Fetches transmit power (TXP) measurement results.

[IMAGE alt='icon' src='rfmxspecan-txp-fetch-vi.png']

- [RFmxSpecAn TXP Fetch Measurement VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-measurement-vi.html) Returns the powers measured using the TXP measurement.
- [RFmxSpecAn TXP Fetch Power Trace VI](../../../../../vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-fetch-power-trace-vi.html) Fetches the power trace used for the transmit power (TxP) measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-read-vi.html language=enus -->
## TOPIC 00300: RFmxSpecAn TXP Read VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-txp-read-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the transmit power (TXP) measurement results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the def

### RFmxSpecAn TXP Read VI

Configures hardware for acquisition, performs measurement on acquired data, and returns the transmit power (TXP) measurement results.

[IMAGE alt='icon' src='rfmxspecan-txp-read-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Minimum Power (dBm) — Minimum Power returns the minimum power, in dBm, of the averaged power trace. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Average Mean Power (dBm) — Average Mean Power returns the mean power, in dBm, of the signal. Only the samples above the threshold are used by the measurement when you set the TXP Threshold Enabled property to True. When you set the TXP Averaging Enabled property to True, the mean power is measured on the power trace averaged over multiple acquisitions. Peak to Average Ratio (dB) — Peak to Average Ratio returns the ratio of the peak power of the signal to the mean power. Only the samples above the threshold are used by the measurement when you set the TXP Threshold Enabled property to True. When you set the TXP Averaging Enabled property to True, the peak and mean powers are measured using the power trace averaged over multiple acquisitions. Maximum Power (dBm) — Maximum Power returns the maximum power, in dBm, of the averaged power trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxSpecAn Read VI

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-vi-tree-vi.html language=enus -->
## TOPIC 00301: RFmxSpecAn VI Tree VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-vi-tree-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-vi-tree-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays all the VIs available in RFmxSpecAn for measurement configuration and fetching results. The VIs are organized in the order they must be used in the program you create. icon

### RFmxSpecAn VI Tree VI

Displays all the VIs available in RFmxSpecAn for measurement configuration and fetching results. The VIs are organized in the order they must be used in the program you create.

[IMAGE alt='icon' src='rfmxspecan-vi-tree-vi.png']

Parent topic:

SpecAn

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00302: RFmxSpecAn Wait for Measurement Complete VI

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/rfmxspecan-wait-for-measurement-complete-vi.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you

### RFmxSpecAn Wait for Measurement Complete VI

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxspecan-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxSpecAn Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time, in seconds, for which the VI waits for the measurement to complete. A value of -1 specifies that the VI waits until the measurement is complete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00303: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=rfmxspecan-labview-api-ref path=vi-lib/rfmx/specan/mx/rfmxspecan-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00304: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxspecan-labview-api-ref`
- source_path: `vi-lib/rfmx/specan/mx/rfmxspecan-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/specan/mx/rfmxspecan-llb/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxspecan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
