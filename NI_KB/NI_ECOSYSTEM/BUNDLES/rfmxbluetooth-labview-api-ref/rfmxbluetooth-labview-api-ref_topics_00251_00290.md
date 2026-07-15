# NI DOCUMENT BUNDLE: rfmxbluetooth-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxbluetooth-labview-api-ref start=251 end=290 -->
<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-phase-error-vi.html language=enus -->
## TOPIC 00251: RFmxBT ModAcc Fetch DEVM Phase Error VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-phase-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-phase-error-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default si

### RFmxBT ModAcc Fetch DEVM Phase Error VI

Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-devm-phase-error-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Average RMS Phase Error Mean (deg) — Average RMS Phase Error Mean returns the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. Peak RMS Phase Error Maximum (deg) — Peak RMS Phase Error Maximum returns the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-vi.html language=enus -->
## TOPIC 00252: RFmxBT ModAcc Fetch DEVM VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches ModAcc differential EVM (DEVM) measurement results. These results are valid only for enhanced data rate (EDR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal

### RFmxBT ModAcc Fetch DEVM VI

Fetches ModAcc differential EVM (DEVM) measurement results. These results are valid only for enhanced data rate (EDR) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-devm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Peak RMS DEVM Maximum (%) — Peak RMS DEVM Maximum returns the peak of the RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. When you set ModAcc Averaging Enabled property to True, it returns the maximum of the peak RMS DEVM values computed for each averaging count. This value is expressed in percentage. Peak DEVM Maximum (%) — Peak DEVM Maximum returns the peak of the DEVM values computed on symbols in the EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the maximum of the peak symbol DEVM values computed for each averaging count. This value is expressed in percentage. 99% DEVM (%) — 99% DEVM returns the 99th percentile of the DEVM values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed in percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1-vi.html language=enus -->
## TOPIC 00253: RFmxBT ModAcc Fetch df1 VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name,

### RFmxBT ModAcc Fetch df1 VI

Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-df1-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. df1avg Maximum (Hz) — df1avg Maximum returns the df1avg value computed on the signal. This value is expressed in Hz. When you set the ModAcc Averaging Enabled property to True, it returns the maximum of the df1avg results computed for each averaging count. df1avg Minimum (Hz) — df1avg Minimum returns the df1avg value computed on the signal. This value is expressed in Hz. When you set the ModAcc Averaging Enabled property to True, it returns the minimum of the df1avg results computed for each averaging count. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1max-trace-vi.html language=enus -->
## TOPIC 00254: RFmxBT ModAcc Fetch df1max Trace VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1max-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1max-trace-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the df1max versus the time trace. This VI is applicable only for basic rate (BR) and low energy (LE) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the

### RFmxBT ModAcc Fetch df1max Trace VI

Fetches the df1max versus the time trace. This VI is applicable only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-df1max-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Time (s) — Time returns the array of time instances at which the df1max values are computed. This value is expressed in seconds. df1max (Hz) — df1max returns the array of df1max values computed over the packet at each time instance. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2-vi.html language=enus -->
## TOPIC 00255: RFmxBT ModAcc Fetch df2 VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc df2 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name,

### RFmxBT ModAcc Fetch df2 VI

Fetches the ModAcc df2 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-df2-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. df2avg Minimum (Hz) — df2avg Minimum returns the df2avg value computed on the signal. When you set the ModAcc Averaging Enabled property to True, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz. Percentage of Symbols above df2max Threshold (%) — Percentage of Symbols above df2max Threshold returns the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the ModAcc Averaging Enabled property to True, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2max-trace-vi.html language=enus -->
## TOPIC 00256: RFmxBT ModAcc Fetch df2max Trace VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2max-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2max-trace-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the df2max versus the time trace. This VI is valid only for basic rate (BR) and low energy (LE) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the defa

### RFmxBT ModAcc Fetch df2max Trace VI

Fetches the df2max versus the time trace. This VI is valid only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-df2max-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Time (s) — Time returns the array of time instances at which the df2max values are computed. This value is expressed in seconds. df2max (Hz) — df2max returns the array of df2max values computed over the packet at each time instance. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df4avg-trace-vi.html language=enus -->
## TOPIC 00257: RFmxBT ModAcc Fetch df4avg Trace VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df4avg-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df4avg-trace-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the df4avg versus the time trace. This VI is valid only for LE-CS Packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. I

### RFmxBT ModAcc Fetch df4avg Trace VI

Fetches the df4avg versus the time trace. This VI is valid only for LE-CS Packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-df4avg-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Time (s) — Time returns the array of time instances at which the df4avg values are computed. This value is expressed in seconds. df4avg (Hz) — df4avg (Hz)returns the array of df4avg values computed over the packet at each time instance. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-evm-per-symbol-trace-vi.html language=enus -->
## TOPIC 00258: RFmxBT ModAcc Fetch EVM Per Symbol Trace VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-evm-per-symbol-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-evm-per-symbol-trace-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM values for symbols from the payload portion including the payload header of the LE-HDT packet. This VI is valid only for LE-HDT packet. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you d

### RFmxBT ModAcc Fetch EVM Per Symbol Trace VI

Fetches the EVM values for symbols from the payload portion including the payload header of the LE-HDT packet. This VI is valid only for LE-HDT packet.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-evm-per-symbol-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. EVM Per Symbol (dB) — EVM Per Symbol (dB) returns the EVM values for symbols from the payload portion including the payload header of the LE-HDT packet. The values are expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-br-vi.html language=enus -->
## TOPIC 00259: RFmxBT ModAcc Fetch Frequency Error (BR) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-br-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-br-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc frequency error trace for basic rate (BR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not

### RFmxBT ModAcc Fetch Frequency Error (BR) VI

Fetches the ModAcc frequency error trace for basic rate (BR) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-frequency-error-br-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Initial Frequency Error Maximum (Hz) — Initial Frequency Error Maximum returns the initial frequency error value computed on the preamble of the BR packet. When you set the ModAcc Averaging Enabled property to True, it returns a value corresponding to the maximum of absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. Peak Frequency Drift Maximum (Hz) — Peak Frequency Drift Maximum returns the peak frequency drift value computed on the BR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. Peak Frequency Drift Rate Maximum (Hz) — Peak Frequency Drift Rate Maximum returns the peak frequency drift rate value computed on the BR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-edr-vi.html language=enus -->
## TOPIC 00260: RFmxBT ModAcc Fetch Frequency Error (EDR) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-edr-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-edr-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is u

### RFmxBT ModAcc Fetch Frequency Error (EDR) VI

Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-frequency-error-edr-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Header Frequency Error wi Maximum (Hz) — Header Frequency Error wi Maximum returns the frequency error value computed on the header of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute header frequency error values computed for each averaging count. This value is expressed in Hz. Peak Frequency Error wi+w0 Maximum (Hz) — Peak Frequency Error wi+w0 Maximum returns the peak frequency error value computed on the EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. Peak Frequency Error w0 Maximum (Hz) — Peak Frequency Error w0 Maximum returns the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-le-vi.html language=enus -->
## TOPIC 00261: RFmxBT ModAcc Fetch Frequency Error (LE) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-le-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-le-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches ModAcc frequency error measurement results for low energy (LE) or low energy - channel sounding (LE-CS) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name,

### RFmxBT ModAcc Fetch Frequency Error (LE) VI

Fetches ModAcc frequency error measurement results for low energy (LE) or low energy - channel sounding (LE-CS) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-frequency-error-le-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Frequency Drift Rate Maximum (Hz) — Peak Frequency Drift Rate Maximum returns the peak frequency drift rate value computed on the LE packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Peak Frequency Error Maximum (Hz) — Peak Frequency Error Maximum when you set the Direction Finding Mode property to Disabled, it returns the peak frequency error value computed on the preamble and payload portion of the LE packet. When you set the Direction Finding Mode property to Angle of Arrival, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the ModAcc Averaging Enabled property to True, , it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. Initial Frequency Drift Maximum (Hz) — Initial Frequency Drift Maximum returns the initial frequency drift value computed on the LE packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz. Peak Frequency Drift Maximum (Hz) — Peak Frequency Drift Maximum returns the peak frequency drift value computed on the LE packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-br-vi.html language=enus -->
## TOPIC 00262: RFmxBT ModAcc Fetch Frequency Error Trace (BR) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-br-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-br-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc frequency error trace for basic rate (BR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not

### RFmxBT ModAcc Fetch Frequency Error Trace (BR) VI

Fetches the ModAcc frequency error trace for basic rate (BR) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-frequency-error-trace-br-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Time (s) — Time returns an array of time instances corresponding to the start of the bit blocks at which the frequency error values are computed. This value is expressed in seconds. Frequency Error (Hz) — Frequency Error (Hz) returns an array of frequency errors computed over the packet. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-le-vi.html language=enus -->
## TOPIC 00263: RFmxBT ModAcc Fetch Frequency Error Trace (LE) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-le-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-le-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the defaul

### RFmxBT ModAcc Fetch Frequency Error Trace (LE) VI

Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-frequency-error-trace-le-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Time (s) — Time returns an array of time instances corresponding to the start of the bit blocks at which the frequency error values are computed. This value is expressed in seconds. Frequency Error (Hz) — Frequency Error (Hz) returns the array of frequency errors computed over the packet. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-wi-w0-trace-edr-vi.html language=enus -->
## TOPIC 00264: RFmxBT ModAcc Fetch Frequency Error wi+w0 Trace (EDR) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-wi-w0-trace-edr-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-wi-w0-trace-edr-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If yo

### RFmxBT ModAcc Fetch Frequency Error wi+w0 Trace (EDR) VI

Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-frequency-error-wi-w0-trace-edr-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Time (s) — Time returns an array of time instances corresponding to the start of the 50us blocks of the EDR portion of EDR packet at which the frequency error values are computed. This value is expressed in seconds. Frequency Error wi+w0 (Hz) — Frequency Error wi+w0 returns the array of frequency errors wi+w0 computed over the packet. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-trace-vi.html language=enus -->
## TOPIC 00265: RFmxBT ModAcc Fetch Frequency Trace VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-trace-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency versus time trace. This trace is valid for basic rate (BR), low energy (LE) and low energy - channel sounding (LE-CS) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do n

### RFmxBT ModAcc Fetch Frequency Trace VI

Fetches the frequency versus time trace. This trace is valid for basic rate (BR), low energy (LE) and low energy - channel sounding (LE-CS) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-frequency-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Frequency (Hz) — Frequency returns the frequency versus time trace. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the sample duration. This value is expressed in seconds. y — y returns the frequency at each time instance. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the sample duration. This value is expressed in seconds. y — y returns the frequency at each time instance. This value is expressed in Hz. |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-rms-devm-trace-vi.html language=enus -->
## TOPIC 00266: RFmxBT ModAcc Fetch RMS DEVM Trace VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-rms-devm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-rms-devm-trace-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This VI is valid only for enhanced data rate (EDR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify

### RFmxBT ModAcc Fetch RMS DEVM Trace VI

Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This VI is valid only for enhanced data rate (EDR) packets.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-rms-devm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS DEVM (%) — RMS DEVM returns the array of RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. This value is expressed in percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-vi.html language=enus -->
## TOPIC 00267: RFmxBT ModAcc Fetch VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc measurement results. icon

### RFmxBT ModAcc Fetch VI

Fetches the ModAcc measurement results.

[IMAGE alt='icon' src='rfmxbt-modacc-fetch-vi.png']

- [RFmxBT ModAcc Fetch df1 VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1-vi.html) Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.
- [RFmxBT ModAcc Fetch df1max Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df1max-trace-vi.html) Fetches the df1max versus the time trace. This VI is applicable only for basic rate (BR) and low energy (LE) packets.
- [RFmxBT ModAcc Fetch Frequency Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-trace-vi.html) Fetches the frequency versus time trace. This trace is valid for basic rate (BR), low energy (LE) and low energy - channel sounding (LE-CS) packets.
- [RFmxBT ModAcc Fetch df2 VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2-vi.html) Fetches the ModAcc df2 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.
- [RFmxBT ModAcc Fetch df2max Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df2max-trace-vi.html) Fetches the df2max versus the time trace. This VI is valid only for basic rate (BR) and low energy (LE) packets.
- [RFmxBT ModAcc Fetch df4avg Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-df4avg-trace-vi.html) Fetches the df4avg versus the time trace. This VI is valid only for LE-CS Packets.
- [RFmxBT ModAcc Fetch Frequency Error (BR) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-br-vi.html) Fetches the ModAcc frequency error trace for basic rate (BR) packets.
- [RFmxBT ModAcc Fetch Frequency Error Trace (BR) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-br-vi.html) Fetches the ModAcc frequency error trace for basic rate (BR) packets.
- [RFmxBT ModAcc Fetch Frequency Error (EDR) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-edr-vi.html) Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets.
- [RFmxBT ModAcc Fetch Frequency Error wi+w0 Trace (EDR) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-wi-w0-trace-edr-vi.html) Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets.
- [RFmxBT ModAcc Fetch Frequency Error (LE) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-le-vi.html) Fetches ModAcc frequency error measurement results for low energy (LE) or low energy - channel sounding (LE-CS) packets.
- [RFmxBT ModAcc Fetch Frequency Error Trace (LE) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-frequency-error-trace-le-vi.html) Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets.
- [RFmxBT ModAcc Fetch DEVM VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-vi.html) Fetches ModAcc differential EVM (DEVM) measurement results. These results are valid only for enhanced data rate (EDR) packets.
- [RFmxBT ModAcc Fetch DEVM Magnitude Error VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-magnitude-error-vi.html) Fetches ModAcc RMS magnitude error results. These results are valid only for enhanced data rate (EDR) packets.
- [RFmxBT ModAcc Fetch DEVM Phase Error VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-phase-error-vi.html) Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets.
- [RFmxBT ModAcc Fetch RMS DEVM Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-rms-devm-trace-vi.html) Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This VI is valid only for enhanced data rate (EDR) packets.
- [RFmxBT ModAcc Fetch DEVM Per Symbol Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-devm-per-symbol-trace-vi.html) Fetches the DEVM values for symbols from the enhanced data rate (EDR) portion of the EDR packet. This VI is valid only for EDR packets.
- [RFmxBT ModAcc Fetch EVM Per Symbol Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-evm-per-symbol-trace-vi.html) Fetches the EVM values for symbols from the payload portion including the payload header of the LE-HDT packet. This VI is valid only for LE-HDT packet.
- [RFmxBT ModAcc Fetch Constellation Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-constellation-trace-vi.html) Fetches the demodulated symbols from the enhanced data rate (EDR) portion of the EDR packet. This VI is valid only for EDR packets.
- [RFmxBT ModAcc Fetch CS Detrended Phase Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-cs-detrended-phase-trace-vi.html) Fetches the zero-mean Detrended Phase (deg) versus time trace. This VI is valid only for low energy CS (LE-CS) packets.
- [RFmxBT ModAcc Fetch CS Tone Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-cs-tone-trace-vi.html) Fetches the CS Tone Amplitude (dBm) versus time and CS Tone Phase (deg) versus time traces. This VI is valid only for low energy CS (LE-CS) packets.
- [RFmxBT ModAcc Fetch Demodulated Bit Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modacc-fetch-demodulated-bit-trace-vi.html) Fetches the ModAcc demodulated bit trace.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-configure-averaging-vi.html language=enus -->
## TOPIC 00268: RFmxBT ModSpectrum Configure Averaging VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-configure-averaging-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ModSpectrum measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples:

### RFmxBT ModSpectrum Configure Averaging VI

Configures averaging for the ModSpectrum measurement.

[IMAGE alt='icon' src='rfmxbt-modspectrum-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the ModSpectrum measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModSpectrum measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModSpectrum measurement is averaged. |

Parent topic:

ModSpectrum

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-configure-burst-synchronization-type-vi.html language=enus -->
## TOPIC 00269: RFmxBT ModSpectrum Configure Burst Synchronization Type VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-configure-burst-synchronization-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-configure-burst-synchronization-type-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the burst synchronization type for ModSpectrum measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty st

### RFmxBT ModSpectrum Configure Burst Synchronization Type VI

Configures the burst synchronization type for ModSpectrum measurement.

[IMAGE alt='icon' src='rfmxbt-modspectrum-configure-burst-synchronization-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Burst Synchronization Type — Burst Synchronization Type specifies the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |

Parent topic:

ModSpectrum

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-fetch-spectrum-vi.html language=enus -->
## TOPIC 00270: RFmxBT ModSpectrum Fetch Spectrum VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-modspectrum-fetch-spectrum-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModSpectrum spectrum trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, offset number, and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the re

### RFmxBT ModSpectrum Fetch Spectrum VI

Fetches the ModSpectrum spectrum trace.

[IMAGE alt='icon' src='rfmxbt-modspectrum-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, offset number, and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "signal::sig1/result::r1/offset0" "result::r1/offset0" You can use the RFmxBT Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum — Spectrum Returns the ModSpectrum spectrum trace. x0 — x0Returns the start frequency. This value is expressed in Hz. dx — dxReturns the frequency bin spacing. This value is expressed in Hz. y — yReturns the averaged power measured at each frequency bin. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0Returns the start frequency. This value is expressed in Hz. dx — dxReturns the frequency bin spacing. This value is expressed in Hz. y — yReturns the averaged power measured at each frequency bin. This value is expressed in dBm. |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-powerramp-configure-averaging-vi.html language=enus -->
## TOPIC 00271: RFmxBT PowerRamp Configure Averaging VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-powerramp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-powerramp-configure-averaging-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the PowerRamp measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: ""

### RFmxBT PowerRamp Configure Averaging VI

Configures averaging for the PowerRamp measurement.

[IMAGE alt='icon' src='rfmxbt-powerramp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the PowerRamp measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the PowerRamp measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the PowerRamp measurement is averaged. |

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-powerramp-configure-burst-synchronization-type-vi.html language=enus -->
## TOPIC 00272: RFmxBT PowerRamp Configure Burst Synchronization Type VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-powerramp-configure-burst-synchronization-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-powerramp-configure-burst-synchronization-type-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the burst synchronization type for PowerRamp measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty stri

### RFmxBT PowerRamp Configure Burst Synchronization Type VI

Configures the burst synchronization type for PowerRamp measurement.

[IMAGE alt='icon' src='rfmxbt-powerramp-configure-burst-synchronization-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Burst Synchronization Type — Burst Synchronization Type specifies the type of synchronization used for detecting the start of packet in the PowerRamp measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-property-node-vi.html language=enus -->
## TOPIC 00273: RFmxBT Property Node VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-property-node-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) RFmxBluetooth properties. icon Inputs/Outputs cgenclassrntag.png niRFmx Instrument Handle Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. cerrcodeclst.png

### RFmxBT Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) RFmxBluetooth properties.

[IMAGE alt='icon' src='rfmxbt-property-node-vi.png']

#### Inputs/Outputs

| niRFmx Instrument Handle — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx BT Property Node is used to get (read), set (write), or reset (set to default value) RFmx Bluetooth properties. niRFmx Instrument Handle — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Bluetooth

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-reset-to-default-vi.html language=enus -->
## TOPIC 00274: RFmxBT Reset to Default VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-reset-to-default-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig

### RFmxBT Reset to Default VI

Resets a signal to the default values.

[IMAGE alt='icon' src='rfmxbt-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-multiple-vi.html language=enus -->
## TOPIC 00275: RFmxBT Select Measurement (Multiple) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-multiple-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxBT Select Measurement (Multiple) VI

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxbt-select-measurement-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurements — Measurements specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array. TXP (0) Enables TXP measurement. ModAcc (1) Enables ModAcc measurement. 20dB Bandwidth (2) Enables 20dB Bandwidth measurement. FrequencyRange (3) Enables FrequencyRange measurement. ACP (4) Enables ACP measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TXP (0) | Enables TXP measurement. |
| ModAcc (1) | Enables ModAcc measurement. |
| 20dB Bandwidth (2) | Enables 20dB Bandwidth measurement. |
| FrequencyRange (3) | Enables FrequencyRange measurement. |
| ACP (4) | Enables ACP measurement. |

Parent topic:

RFmxBT Select Measurement VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-single-vi.html language=enus -->
## TOPIC 00276: RFmxBT Select Measurement (Single) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-single-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the single measurement that you specify in the Measurement parameter and disables all other measurements in the selected signal configuration. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the sig

### RFmxBT Select Measurement (Single) VI

Enables the single measurement that you specify in the **Measurement** parameter and disables all other measurements in the selected signal configuration.

[IMAGE alt='icon' src='rfmxbt-select-measurement-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement — Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is TXP. TXP (0) Enables TXP measurement. ModAcc (1) Enables ModAcc measurement. 20dB Bandwidth (2) Enables 20dB Bandwidth measurement. FrequencyRange (3) Enables FrequencyRange measurement. ACP (4) Enables ACP measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TXP (0) | Enables TXP measurement. |
| ModAcc (1) | Enables ModAcc measurement. |
| 20dB Bandwidth (2) | Enables 20dB Bandwidth measurement. |
| FrequencyRange (3) | Enables FrequencyRange measurement. |
| ACP (4) | Enables ACP measurement. |

Parent topic:

RFmxBT Select Measurement VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-vi.html language=enus -->
## TOPIC 00277: RFmxBT Select Measurement VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. icon

### RFmxBT Select Measurement VI

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

[IMAGE alt='icon' src='rfmxbt-select-measurement-vi.png']

- [RFmxBT Select Measurement (Single) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-single-vi.html) Enables the single measurement that you specify in the Measurement parameter and disables all other measurements in the selected signal configuration.
- [RFmxBT Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

Parent topic:

Bluetooth

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00278: RFmxBT Send Software Edge Trigger VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-send-software-edge-trigger-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxBT Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. This VI returns an error in the following situations: You configure an i

### RFmxBT Send Software Edge Trigger VI

Sends a trigger to the device when you use the [RFmxBT Configure Trigger](/csh?topicname=rfmxbt-configure-trigger-vi.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxBT Initiate VI.

[IMAGE alt='icon' src='rfmxbt-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-configure-averaging-vi.html language=enus -->
## TOPIC 00279: RFmxBT TXP Configure Averaging VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-configure-averaging-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the transmit power (TXP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). E

### RFmxBT TXP Configure Averaging VI

Configures averaging for the transmit power (TXP) measurement.

[IMAGE alt='icon' src='rfmxbt-txp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for TXP measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the TXP Averaging Count parameter as the number of acquisitions over which the TXP measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the TXP Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the TXP Averaging Count parameter as the number of acquisitions over which the TXP measurement is averaged. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-configure-burst-synchronization-type-vi.html language=enus -->
## TOPIC 00280: RFmxBT TXP Configure Burst Synchronization Type VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-configure-burst-synchronization-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-configure-burst-synchronization-type-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of synchronization used for detecting the start of the packet in the transmit power (TXP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal

### RFmxBT TXP Configure Burst Synchronization Type VI

Configures the type of synchronization used for detecting the start of the packet in the transmit power (TXP) measurement.

[IMAGE alt='icon' src='rfmxbt-txp-configure-burst-synchronization-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Burst Synchronization Type — Burst Synchronization Type specifies the type of synchronization used for detecting the start of packet in the measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-edr-powers-vi.html language=enus -->
## TOPIC 00281: RFmxBT TXP Fetch EDR Powers VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-edr-powers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-edr-powers-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches TXP measurement results for enhanced data rate (EDR) packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not

### RFmxBT TXP Fetch EDR Powers VI

Fetches TXP measurement results for enhanced data rate (EDR) packets.

[IMAGE alt='icon' src='rfmxbt-txp-fetch-edr-powers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. EDR GFSK Average Power Mean (dBm) — EDR GFSK Average Power Mean returns the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled property to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. EDR DPSK Average Power Mean (dBm) — EDR DPSK Average Power Mean returns the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled property to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. EDR DPSK GFSK Average Power Ratio Mean (dB) — EDR DPSK GFSK Average Power Ratio Mean returns the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled property to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT TXP Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-reference-period-powers-vi.html language=enus -->
## TOPIC 00282: RFmxBT TXP Fetch LE CTE Reference Period Powers VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-reference-period-powers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-reference-period-powers-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the transmit power (TXP) measurement results over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the Direction Finding Mode property to Angle of Departure. icon Inputs/Outputs cstr.png Selector String Selector String specifies a sel

### RFmxBT TXP Fetch LE CTE Reference Period Powers VI

Fetches the transmit power (TXP) measurement results over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the [Direction Finding Mode](/csh?context=rfmxbt_rfmxbtprop_attrb0002c) property to **Angle of Departure**.

[IMAGE alt='icon' src='rfmxbt-txp-fetch-le-cte-reference-period-powers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Reference Period Average Power Mean (dBm) — Reference Period Average Power Mean returns the average power computed over the reference period in the CTE portion of the LE packet. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. Reference Period Peak Absolute Power Deviation Maximum (%) — Reference Period Peak Absolute Power Deviation Maximum returns the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT TXP Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-array-vi.html language=enus -->
## TOPIC 00283: RFmxBT TXP Fetch LE CTE Transmit Slot Powers (Array) VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-array-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of transmit power (TXP) measurement results over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the Direction Finding Mode property to Angle of Departure. icon Inputs/Outputs cstr.png Selector String Selector String specifies

### RFmxBT TXP Fetch LE CTE Transmit Slot Powers (Array) VI

Fetches an array of transmit power (TXP) measurement results over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the [Direction Finding Mode](/csh?context=rfmxbt_rfmxbtprop_attrb0002c) property to **Angle of Departure**.

[IMAGE alt='icon' src='rfmxbt-txp-fetch-le-cte-transmit-slot-powers-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Transmit Slot Average Power Mean (dBm) — Transmit Slot Average Power Mean returns an array of average powers computed over every transmit slot in CTE portion of the LE packet. When you set the TXP Averaging Enabled property to True, it returns an array of mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. Transmit Slot Peak Absolute Power Deviation Maximum (%) — Transmit Slot Peak Absolute Power Deviation Maximum returns an array of peak absolute power deviations computed over every transmit slot in CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns an array of maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT TXP Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-vi.html language=enus -->
## TOPIC 00284: RFmxBT TXP Fetch LE CTE Transmit Slot Powers VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the transmit power (TXP) measurement results over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the Direction Finding Mode property to Angle of Departure. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selec

### RFmxBT TXP Fetch LE CTE Transmit Slot Powers VI

Fetches the transmit power (TXP) measurement results over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the [Direction Finding Mode](/csh?context=rfmxbt_rfmxbtprop_attrb0002c) property to **Angle of Departure**.

[IMAGE alt='icon' src='rfmxbt-txp-fetch-le-cte-transmit-slot-powers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "slot0" "signal::sig1/slot0" "signal::sig1/result::r1/slot0" "result::r1/slot0" You can use the RFmxBT Build Slot String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Transmit Slot Average Power Mean (dBm) — Transmit Slot Average Power Mean returns the average power computed over each transmit slot in CTE portion of the LE packet. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. Transmit Slot Peak Absolute Power Deviation Maximum (%) — Transmit Slot Peak Absolute Power Deviation Maximum returns the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT TXP Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-power-trace-vi.html language=enus -->
## TOPIC 00285: RFmxBT TXP Fetch Power Trace VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-power-trace-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power versus time trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defa

### RFmxBT TXP Fetch Power Trace VI

Fetches the power versus time trace.

[IMAGE alt='icon' src='rfmxbt-txp-fetch-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Power (dBm) — Power returns the power versus time trace. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the sample duration. This value is expressed in seconds. y — y returns the averaged power at each time instance. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the sample duration. This value is expressed in seconds. y — y returns the averaged power at each time instance. This value is expressed in dBm. |

Parent topic:

RFmxBT TXP Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-powers-vi.html language=enus -->
## TOPIC 00286: RFmxBT TXP Fetch Powers VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-powers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-powers-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches TXP measurement results. These results are valid for all packets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do

### RFmxBT TXP Fetch Powers VI

Fetches TXP measurement results. These results are valid for all packets.

[IMAGE alt='icon' src='rfmxbt-txp-fetch-powers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak to Average Power Ratio Maximum (dB) — Peak to Average Power Ratio Maximum returns the peak to average power ratio computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. For LE-HDT, PAPR is calculated using peak power calculated over active portion of burst and average power calculated from beginning of the payload portion. When you set the TXP Averaging Enabled property to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Average Power Mean (dBm) — Average Power Mean returns the average power computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled property to True, it returns the mean of the average power results computed for each averaging count. This value is expressed in dBm. Average Power Maximum (dBm) — Average Power Maximum returns the average power computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled property to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. Average Power Minimum (dBm) — Average Power Minimum returns the average power computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the average power computation. For LE-HDT, average power is calculated from beginning of the payload portion. When you set the TXP Averaging Enabled property to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxBT TXP Fetch VI

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-vi.html language=enus -->
## TOPIC 00287: RFmxBT TXP Fetch VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the TXP measurement results. icon

### RFmxBT TXP Fetch VI

Fetches the TXP measurement results.

[IMAGE alt='icon' src='rfmxbt-txp-fetch-vi.png']

- [RFmxBT TXP Fetch Powers VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-powers-vi.html) Fetches TXP measurement results. These results are valid for all packets.
- [RFmxBT TXP Fetch EDR Powers VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-edr-powers-vi.html) Fetches TXP measurement results for enhanced data rate (EDR) packets.
- [RFmxBT TXP Fetch LE CTE Reference Period Powers VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-reference-period-powers-vi.html) Fetches the transmit power (TXP) measurement results over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the Direction Finding Mode property to Angle of Departure .
- [RFmxBT TXP Fetch LE CTE Transmit Slot Powers VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-vi.html) Fetches the transmit power (TXP) measurement results over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the Direction Finding Mode property to Angle of Departure .
- [RFmxBT TXP Fetch LE CTE Transmit Slot Powers (Array) VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-le-cte-transmit-slot-powers-array-vi.html) Fetches an array of transmit power (TXP) measurement results over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the Direction Finding Mode property to Angle of Departure .
- [RFmxBT TXP Fetch Power Trace VI](../../../../../vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-txp-fetch-power-trace-vi.html) Fetches the power versus time trace.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00288: RFmxBT Wait for Measurement Complete VI

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/rfmxbt-wait-for-measurement-complete-vi.html
- document_id: `rfmxbluetooth-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If

### RFmxBT Wait for Measurement Complete VI

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxbt-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00289: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxbluetooth-labview-api-ref`
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

<!--NI_TOPIC bundle=rfmxbluetooth-labview-api-ref path=vi-lib/rfmx/bt/mx/rfmxbt-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00290: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxbluetooth-labview-api-ref`
- source_path: `vi-lib/rfmx/bt/mx/rfmxbt-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetooth-labview-api-ref/raw/resource/enus/vi-lib/rfmx/bt/mx/rfmxbt-llb/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxbluetooth-labview-api-ref`
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
