# NI DOCUMENT BUNDLE: rfmx-vna

<!--NI_BUNDLE_CHUNK bundle=rfmx-vna start=1 end=34 -->
<!--NI_TOPIC bundle=rfmx-vna path=applying-error-corrections.html language=enus -->
## TOPIC 00001: Applying Error Correction

- bundle_id: `rfmx-vna`
- source_path: `applying-error-corrections.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/applying-error-corrections.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Acquisitions For Uncorrected S-Parameters The following example scenario is measuring the S11 of a two port DUT using a two port VNA. With error correction turned off, the VNA measures the uncorrected S11 of the DUT by stepping through the configured frequency points, returning the uncorrected S11 a

### Applying Error Correction

#### Acquisitions For Uncorrected
 S-Parameters

The following example scenario is measuring the S11 of a two port DUT using a two
 port VNA. With error correction turned off, the VNA measures the uncorrected S11 of
 the DUT by stepping through the configured frequency points, returning the
 uncorrected S11 as the following ratio:

[IMAGE alt='image' src='GUID-BC4003C3-16B5-499B-B72D-EC9D2EDE2935-a5.png']

where

- the subscript m in S 11m stands for measured,
- S ij denotes the intensity of the scattered wave traveling away from
 the DUT at port [i] when the VNA generates the stimulus signal at port [j],
- r ij denotes the intensity of the incident wave traveling away from
 the DUT at port [i] when the VNA generates the stimulus signal at port [j].

,Computing the uncorrected S<sub>11</sub>, that is S<sub>11m</sub>, requires the VNA
 source to measure the DUT response by generating the signal only at port 1.

Note

Note

11m

21m

Note

12m

22m

#### Acquisitions For Corrected
 S-Parameters

Computing an error-corrected s-parameter of a two port DUT using a two port VNA
 requires measuring the DUT in both the forward and reverse port directions. The
 error corrected s-parameters S<sub>〈i〉〈j〉</sub> are obtained from uncorrected
 S<sub>〈i〉〈j〉m</sub> as shown in the equations below.

[IMAGE alt='image' src='GUID-A4CAA167-9932-4220-971E-A22165AB82DA-a5.png']

Note

11m

12m

21m

22m

#### Port Subset For Error
 Correction

When measuring the error-corrected S11 of a 1-port DUT connected to port 1 of a
 two-port VNA, the VNA still performs both forward and reverse sweeps. However, since
 the DUT is a 1-port network connected to port 1 of the VNA and is completely
 isolated from port 2 of the VNA, the reverse sweep is unnecessary.

You can avoid this extra sweep by setting the Correction:Port
 Subset:Enabled property to True and the
 Correction:Port Subset:Ports property to port
 1. With error-correction limited to the specified set of ports, the
 VNA performs only a forward sweep to compute the error corrected S11 of the DUT.

[IMAGE alt='image' src='GUID-658D874A-CBC5-4C2A-B469-2E1EE664DF15-a5.png']

Parent topic:

Network Analysis

<!--NI_TOPIC bundle=rfmx-vna path=calibration-and-correction.html language=enus -->
## TOPIC 00002: Calibration and Correction

- bundle_id: `rfmx-vna`
- source_path: `calibration-and-correction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/calibration-and-correction.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: In pulse mode, you cannot set the IF Bandwidth property directly because it is derived indirectly from the Pulse Acquisition Width property. If you choose to calibrate with pulse mode enabled, calibration is performed with the IF Bandwidth derived from the Pulse Acquisition Width property, ignoring

### Calibration and Correction

In pulse mode, you cannot set the IF Bandwidth property directly
 because it is derived indirectly from the Pulse Acquisition Width
 property. If you choose to calibrate with pulse mode enabled, calibration is performed
 with the IF Bandwidth derived from the Pulse
 Acquisition Width property, ignoring the user defined IF
 Bandwidth value.

Note

IF
 Bandwidth

IF
 Bandwidth

The calset obtained from this calibration can be used for performing error corrected
 measurements regardless of whether the source is pulsed or not.

The calsets
 obtained with the pulse mode disabled can be used for performing error correction on
 pulsed measurements if the values of the stimulus properties (such as IF
 Bandwidth, Test Receiver Attenuation) used at the
 time of calibration match the values during measurement.

Parent topic:

Pulse Mode

<!--NI_TOPIC bundle=rfmx-vna path=calibration-elements.html language=enus -->
## TOPIC 00003: Calibration Elements Tab

- bundle_id: `rfmx-vna`
- source_path: `calibration-elements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/calibration-elements.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Calibration Elements tab shows the currently defined calibration elements for the calkit. You can add, edit and remove calibration elements of the current calkit. The Add and Edit buttons open the dialog for defining the properties of a calibration element.

### Calibration Elements Tab

The Calibration Elements tab shows the currently defined
 calibration elements for the calkit. You can add, edit and remove calibration elements
 of the current calkit.

The Add and Edit buttons open the dialog
 for defining the properties of a calibration element.

[IMAGE alt='image' src='GUID-515ADD45-ED7F-4E27-B3A4-418035A4299F-a5.png']

Parent topic:

Calkit Editor

<!--NI_TOPIC bundle=rfmx-vna path=calkit-editor.html language=enus -->
## TOPIC 00004: Calkit Editor

- bundle_id: `rfmx-vna`
- source_path: `calkit-editor.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/calkit-editor.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Calkit files define the properties of the calibration elements (or calibration standards) of a calibration kit and the connectors of these calibration elements. Typical calibration standards collected in a calibration kit include: (Offset) Shorts (Offset) Opens (Offset) Loads Thrus Lines The RFmx VN

### Calkit Editor

Calkit files define the properties of the calibration elements (or calibration standards)
 of a calibration kit and the connectors of these calibration elements. Typical
 calibration standards collected in a calibration kit include:

- (Offset) Shorts
- (Offset) Opens
- (Offset) Loads
- Thrus
- Lines

The RFmx VNA requires a calkit file to perform a VNA calibration using a mechanical
 calibration kit. Depending on the selected calibration method (SOL, SOLT, TRL), RFmx VNA
 expects specific elements in a calibration kit.

<!--NI_TOPIC bundle=rfmx-vna path=configure-calibration-element.html language=enus -->
## TOPIC 00005: Configure Calibration Element Dialog

- bundle_id: `rfmx-vna`
- source_path: `configure-calibration-element.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/configure-calibration-element.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The dialog to configure a calibration element consists of three parts. Defines common parameters, such as Name, Description, Minimum, and Maximum Frequency and the connectors of the calibration element. Identifies model-specific parameters to configure the physical properties of a calibration elemen

### Configure Calibration Element
 Dialog

The dialog to configure a calibration element consists of three parts.

[IMAGE alt='image' src='GUID-9314842D-541D-415F-89E3-AFB9BD0091C5-a5.png']

1. Defines common parameters, such as Name ,
 Description , Minimum , and
 Maximum Frequency and the connectors of the calibration
 element.
2. Identifies model-specific parameters to configure the physical properties of a
 calibration element. The available options depend on the
 Characteristics and Model Type .
3. Specifies how the calibration method uses the calibration element. For example,
 define how a particular calibration method uses the specific calibration element.
 For example, if you configure RFmx VNA to perform a one-port SOL calibration, it
 checks the calibration kit for three calibration elements with usage that is marked
 as Short , Open and
 Load , respectively.

The characteristics of the calibration elements are either Model
 Based or S-Parameter based.

Parent topic:

Calibration Elements Tab

<!--NI_TOPIC bundle=rfmx-vna path=configure-connector-dialog.html language=enus -->
## TOPIC 00006: Configure Connector Dialog

- bundle_id: `rfmx-vna`
- source_path: `configure-connector-dialog.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/configure-connector-dialog.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configure Connector dialog to define the following connector properties. Connector Name Connector Type Gender Impedance Minimum/Maximum Frequency Optionally, you can provide a description. The Connector Type dropdown list provides a predefined list of typical RF connectors. Choose from the f

### Configure Connector Dialog

Use the Configure Connector dialog to define the following
 connector properties.

[IMAGE alt='image' src='GUID-96277EF0-5160-4CF3-8AFE-337FE2C493F3-a5.png']

- Connector Name
- Connector Type
- Gender
- Impedance
- Minimum/Maximum Frequency

Optionally, you can provide a description.

The Connector Type dropdown list provides a predefined list of
 typical RF connectors.

Choose from the following gender options.

- Female
- Male
- No Gender

Parent topic:

Connector List Tab

<!--NI_TOPIC bundle=rfmx-vna path=connector-list-tab.html language=enus -->
## TOPIC 00007: Connector List Tab

- bundle_id: `rfmx-vna`
- source_path: `connector-list-tab.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/connector-list-tab.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Connector List Tab shows the currently defined connectors for the calkit. You can add, edit and remove connectors of the calkit. The Add and Edit buttons open the dialog for defining the properties of a connector.

### Connector List Tab

The Connector List Tab shows the currently defined connectors for the calkit. You can
 add, edit and remove connectors of the calkit.

[IMAGE alt='image' src='GUID-81F661C7-5041-4C32-9948-B9AF29FDC4AA-a5.png']

The Add and Edit buttons open the dialog
 for defining the properties of a connector.

Parent topic:

Calkit Editor

<!--NI_TOPIC bundle=rfmx-vna path=creating-calkits.html language=enus -->
## TOPIC 00008: Creating Calkits for Calibration Methods

- bundle_id: `rfmx-vna`
- source_path: `creating-calkits.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/creating-calkits.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Depending on the calibration method, RFmx VNA calibration expects a combination of calibration elements having a specific Usage type defined in the calkit file. The usage type of a calibration element is in the Type(s) column of the Calibration Element tab. Define the usage type by enabling one or m

### Creating Calkits for Calibration
 Methods

Depending on the calibration method, RFmx VNA calibration expects a combination of
 calibration elements having a specific Usage type defined in the
 calkit file.

The usage type of a calibration element is in the Type(s) column
 of the Calibration Element tab. Define the usage type by enabling
 one or more checkboxes in the Usage section of thecalibration element configuration dialog.

[IMAGE alt='image' src='GUID-D67D6538-0ED2-4173-BA51-3A8208E6A648-a5.png']

The Usage area includes the following options.

Short, Open, or Load

Thru

Reflect

Termination

The following table summarizes which calibration element usage types are expected by a
 particular RFmx VNA calibration method.

| Usage | SOLT | Overdetermined SOL | TRL / LRL |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Known Thru | Unknown Thru (SOLR) | Known Thru | Unknown Thru (SOLR) |  |
| Short | 1 | 1 |  |  |  |
| Open | 1 | 1 |  |  |  |
| Load | 1 | 1 |  |  |  |
| Thru | 1 |  | 1 |  | 1 |
| Line |  |  |  |  | N (N≥1) |
| Reflect |  |  |  |  | 1 |
| Termination |  |  | N (N≥3) | N (N≥3) |  |

Note

Parent topic:

Calkit Editor

<!--NI_TOPIC bundle=rfmx-vna path=error-models.html language=enus -->
## TOPIC 00009: Error Models

- bundle_id: `rfmx-vna`
- source_path: `error-models.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/error-models.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The two-port VNA typically uses one of the following error models. 12 Term Error Model For a two-port VNA in the forward state, the 12-term error model represents systematic errors in the measurements as shown in the figure below. In the context of a two-port VNA, the forward and reverse states are

### Error Models

The two-port VNA typically uses one of the following error models.

#### 12 Term Error Model

For a two-port VNA in the forward state, the 12-term error model represents
 systematic errors in the measurements as shown in the figure below.

[IMAGE alt='image' src='GUID-9E6B2C65-4CAF-431A-9C98-DFE8EB3CAD1E-a5.png']

In the context of a two-port VNA, the forward and reverse states are defined as
 follows:

- The forward state is where the VNA source generates a stimulus signal on port 1
 while port 2 is terminated.
- The reverse state is where the VNA source generates a stimulus signal on port 2
 while port 1 is terminated.

The error terms depicted in the forward state are as follows.

| Error | Description |
| --- | --- |
| ED(1,1) | Forward directivity; an ideal directional coupler produces an output signal in the coupled arm that is proportional to the measured signal traveling in one direction of the main arm, while producing no output for a signal traveling in the opposite direction. |
| ES(1,1) | Forward source match; the mismatch between the DUT input and the network analyzer port 1. |
| ERT(1,1) | Forward reflection tracking; reflected signal loss across frequency. |
| EL(2,1) | Forward load match; the mismatch between the DUT output and the network analyzer port 2. |
| ETT(2,1) | Forward transmission tracking; the transmitted signal loss across frequency. |
| EX(2,1) | Forward isolation; a fraction of incident signal may be radiated or conducted from port one and detected at the port two receiver. This causes isolation error or crosstalk. |

Note

The reverse state error model is shown below.

[IMAGE alt='image' src='GUID-BAACF8E4-8763-4163-BE7F-CEA5B110571F-a5.png']

The forward and reverse error terms sum-up to a total of 12 errors. User calibration
 needs to adequately account for these 12 error terms so that the VNA can apply the
 proper correction factors to the measured data.

#### 10 Term Error Model

Many applications do not require additional isolation calibration as the VNA
 isolation is sufficient. The 10-term error model is same as 12 term error model with
 the isolation error terms E_X (2,1) and E_X (1,2) set to 0. Forward and reverse
 state 10 term error model is shown in the following figures.

[IMAGE alt='image' src='GUID-DF08B459-DA7F-4D8C-ADA6-900A5235FE0C-a5.png']

[IMAGE alt='image' src='GUID-9BEAFB9B-6ECC-427D-AC40-0DC28A46CE9D-a5.png']

#### 8 Term Error Model

The 8-term error model differs from the 10-term model in requiring measurements at
 all four test receivers when performing error correction for a two-port VNA: the two
 incident waves r_1 and r_2 and the two scattered waves s_1 and s_2, as shown in the
 following figure.

[IMAGE alt='image' src='GUID-72826ABC-839F-4166-95CE-CC2C2F04A9FF-a5.png']

In practice, the load match at each port changes depending upon whether the port is a
 source or a load. Therefore, 10-term and 12-term error models have different error
 terms depending upon forward or reverse source direction. However, the 8-term model
 does not change with source direction, because the change in load impedance is
 captured in changes in the incident waves at each port.

#### Wave Formalism Error Model

You can also model error correction with T-parameters. The table below shows an
 example of the transformation of the wave-formalism error model.

| Uncorrected waves | Corrected waves |
| --- | --- |
| Incident wave r | Incident wave a |
| Scattered wave s | Scattered wave b |

For a two-port VNA, the wave-formalism model is shown in the following equation.

[IMAGE alt='image' src='GUID-8AAF18FD-CFE7-4F45-B835-163A523BF2E5-a5.png']

In general, for each port i in any N-port VNA, the wave-formalism error model
 simplifies to

[IMAGE alt='image' src='GUID-2E639CBA-C99D-4DE4-AF49-32469586774F-a5.png']

Here, error correction transforms the measured waves r_i,s_i (uncorrected) to the
 corrected waves a_i,b_i at VNA port i. By convention, the error model is normalized
 such that α_i=1 for all ports i. For measurements expressed in ratios, the
 correction model is overdetermined and you can set one carriable independently.

Note

[IMAGE alt='image' src='GUID-55439C6B-AF30-4AE9-86A9-9661D01B2C15-a5.png']

Parent topic:

Network Analysis

<!--NI_TOPIC bundle=rfmx-vna path=guidelines-for-performing-user-calibration.html language=enus -->
## TOPIC 00010: Guidelines For Performing User Calibration

- bundle_id: `rfmx-vna`
- source_path: `guidelines-for-performing-user-calibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/guidelines-for-performing-user-calibration.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many factors determine how often user calibration is performed, such as the required measurement accuracy, environmental conditions, and the repeatability of the DUT connection. Typically, network analyzers need user calibration every few hours to every few days. To ensure accurate measurements, rec

### Guidelines For Performing User
 Calibration

Many factors determine how often user calibration is performed, such as the required
 measurement accuracy, environmental conditions, and the repeatability of the DUT
 connection. Typically, network analyzers need user calibration every few hours to every
 few days. To ensure accurate measurements, recalibrate the VNA whenever there are
 changes in any of the following factors:

- ambient or instrument temperature,
- test port extension cable is added, removed, or replaced
- the instrument setup, such as
  - IF bandwidth
  - source power level
  - test port attenuation
  - instrument firmware
  - frequency points

For accurate error correction, observe the following guidelines:

- To change the gender of a connector to make a through connection, use phase-equal
 adapters during all steps of calibration to keep the reference plane constant.
- Perform calibration under the lowest noise scenario, when you have a low IF
 bandwidth configured, high power, and averaging is enabled.
- Keep the measurement configuration parameters such as power level, IF bandwidth,
 frequency points, test port attenuation the same between calibration and
 measurement.

Parent topic:

User Calibration

<!--NI_TOPIC bundle=rfmx-vna path=lrl-calkit-example.html language=enus -->
## TOPIC 00011: LRL Calkit Example

- bundle_id: `rfmx-vna`
- source_path: `lrl-calkit-example.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/lrl-calkit-example.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: If Thru usage has a non-zero delay, Thru becomes a Line and the TRL calibration with non-zero delay Thru is referred to as LRL calibration (Line-Reflect-Line). Since the TRL calibration algorithm places the calibration plane in the middle of the non-zero Thru, for LRL it is required to shift the ref

### LRL Calkit Example

If Thru usage has a non-zero delay, Thru becomes a Line and the TRL calibration with
 non-zero delay Thru is referred to as LRL calibration (Line-Reflect-Line).

Since the TRL calibration algorithm places the calibration plane in the middle of the
 non-zero Thru, for LRL it is required to shift the reference plane back to the
 calibration ports. Thus, the following additional requirement to the Calkit definition
 applies:

- The Thru delay has to be accurately known to shift the reference plane from
 the center of the non-zero delay Thru to the calibration ports.
- If the Reflect standard is more accurate than the Thru standard, use the
 Reflect standard instead to establish the calibration plane at the calibration
 ports. Refer to TRL/LRL Options for more information.

The following figure shows an LRL Calkit with a Thru having a delay of 100 ps and the
 Line with delay of 200 ps. The effective delay is the difference of the Line delay and
 the Thru delay. With this example, the effective delay is the same as the previous TRL
 Calkit example, so the supported frequency range of this Calkit is the same, ranging
 from 556 MHz to 4.4 GHz.

[IMAGE alt='image' src='GUID-5110D545-FD67-4125-AF20-97BC31594743-a5.png']

Parent topic:

Creating Calkits for Calibration Methods

<!--NI_TOPIC bundle=rfmx-vna path=model-based-def.html language=enus -->
## TOPIC 00012: Model-Based Calibration Element Definition

- bundle_id: `rfmx-vna`
- source_path: `model-based-def.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/model-based-def.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following models are available for calibration elements. One-port models Reflect ShortModels the Short calibration standard as a cascade of a transmission line. The transmission line is characterized by delay, loss and impedance Z_0 and a frequency dependent inductance modeled by a third order p

### Model-Based Calibration Element
 Definition

The following models are available for calibration elements.

#### One-port models

- Reflect Short Models the Short calibration standard as a cascade of a
 transmission line. The transmission line is characterized by delay, loss and
 impedance Z_0 and a frequency dependent inductance modeled by a third order
 polynomial with coefficients L_0, L_1, L_2, and L_3.
- Reflect Open Models the Open calibration standard as a cascade of a
 transmission line characterized by delay, loss and
 impedance Z_0 and a frequency dependent capacitance
 modeled by a third order polynomial with
 coefficients C_0, C_1, C_2, and C_3.
- Load Models the Load calibration standard as a cascade of a transmission line
 characterized by delay, loss and impedance Z_0 and
 an ideal Load.

#### Two-port models

- Delay You can model a two port calibration standard as a transmission line
 characterized by a specific delay.

Parent topic:

Calibration Elements Tab

<!--NI_TOPIC bundle=rfmx-vna path=multiline-trl-lrl-example.html language=enus -->
## TOPIC 00013: Multiline TRL/LRL Calkit

- bundle_id: `rfmx-vna`
- source_path: `multiline-trl-lrl-example.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/multiline-trl-lrl-example.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Due to the 20/160 degrees rule, a TRL calibration with a single line can only cover a certain frequency range. Use multiple lines to extend the frequency range. To support multiline TRL/LRL, RFmxVNA calibration internally selects the proper line for each calibration frequency out of a set of lines d

### Multiline TRL/LRL Calkit

Due to the 20/160 degrees rule, a TRL calibration with a single line can only cover a
 certain frequency range.

Use multiple lines to extend the frequency range. To support multiline TRL/LRL, RFmxVNA
 calibration internally selects the proper line for each calibration frequency out of a
 set of lines defined in the Calkit.

The following table shows an example multiline LRL Calkit with 2 Lines.

| Standard | Delay | Effective Line Delay | fmin | fmax |
| --- | --- | --- | --- | --- |
| Thru | 100 ps | - | - | - |
| Line1 | 110 ps | 10 ps | 5.56 GHz | 44.4 GHz |
| Line2 | 150 ps | 50 ps | 1.1 GHz | 8.9 GHz |

The frequency range of the two lines overlaps. The RFmx VNA algorithm automatically
 selects the line that is closer to a phase of 90 degrees. For this example, the
 frequency at which it switches between two lines in 8.3 GHz.

[IMAGE alt='image' src='GUID-53162D9B-AD31-4C1F-B826-3E8E299F8F30-a5.png']

The following figure illustrates the multiline LRL Calkit in this example.

[IMAGE alt='image' src='GUID-7F8B7DD9-EDD4-45CF-B917-AE76A778D3A8-a5.png']

Parent topic:

Creating Calkits for Calibration Methods

<!--NI_TOPIC bundle=rfmx-vna path=network-analysis.html language=enus -->
## TOPIC 00014: Network Analysis

- bundle_id: `rfmx-vna`
- source_path: `network-analysis.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/network-analysis.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Background In RF and microwave engineering, the distributed-element model is used to model and characterize electrical circuits and networks of interconnected electrical components. The distributed model is employed when the wavelength becomes comparable to the physical dimensions of the circuit, re

### Network Analysis

#### Background

In RF and microwave engineering, the distributed-element model is used to model and
 characterize electrical circuits and networks of interconnected electrical
 components. The distributed model is employed when the wavelength becomes comparable
 to the physical dimensions of the circuit, rendering the lumped model inaccurate.
 This phenomenon occurs at high frequencies, where the wavelength is extremely short,
 or on low frequency, yet very long, transmission lines like overhead power
 lines.

#### Transmission lines

Propagation of electromagnetic waves in a device whose physical dimensions are
 comparable to or smaller than the signal wavelength can be illustrated with a
 transmission line using the distributed-element model, as shown in the following
 figure.

[IMAGE alt='image' src='GUID-B2CB0C02-1B29-4584-ADE0-EFA840A8611B-a5.png']

Here, R is the resistance per unit distance, expressed in ohms/m. Similarly, L, C and
 G are distributed inductance, capacitance and conductance per meter of the
 transmission line. Voltage and current are a function of time, t and position, z.
 Partial differential equations relating the two are as follows.

[IMAGE alt='image' src='GUID-76F79546-4815-4596-BB7F-5DD9D88BB23C-a5.png']

Solving these equations leads to the voltage phasor

[IMAGE alt='image' src='GUID-4B1F12CF-58CA-49FE-A2AD-391249E55403-a5.png']

where

[IMAGE alt='image' src='GUID-2C984CDA-8706-405D-AD2E-38EAD83F33F7-a5.png']

V<sub>_+ (z,ω)</sub> and V<sub>_-
 (z,ω)</sub> represent the complex-valued phasors of the waveforms traveling in
 the +z (forward direction) and -z directions respectively, and propagation constant
 γ is

[IMAGE alt='image' src='GUID-A2BA2981-65EC-46CF-A993-F6CA4ABF4BA4-a5.png']

The real part of the propagation constant, α, is called the attenuation constant and
 the imaginary part, β is called the phase constant.

Similarly, the equations for current are as follows:

[IMAGE alt='image' src='GUID-30003A18-4AC5-4C8E-AC31-018F74E80A40-a5.png']

with

4

B

I

+

z

,

ω

=

1

Z

0

V

+

z

0

,

ω

e

-

γ

z

-

z

0

4

C

I

-

z

,

ω

=

-

1

Z

0

V

-

z

0

,

ω

e

+

γ

(

z

-

z

0

)

where

[IMAGE alt='image' src='GUID-85853372-6DE8-4677-9929-1B1E6FA545D8-a5.png']

Z<sub>0</sub> denotes the characteristic impedance of the transmission line and is
 equal to the ratio of the voltage and current travelling in one direction along the
 line.

[IMAGE alt='image' src='GUID-D9DD071C-902A-48F7-AEBD-7C4C5981BD0A-a5.png']

All symbols and their definitions are summarized below.

| Symbol | Definition |
| --- | --- |
| z | By convention, the direction of wave propagation is along the z-axis. |
| z_0 | The point at which the values of forward and reverse waves are known. |
| ω | The frequency of the signal in radians per second. |
| V(z,ω) | The total complex voltage phasor at point z. |
| V_+ (z,ω) | The complex voltage phasor of the forward wave at point z. |
| V_- (z,ω) | The complex voltage phasor of the reverse wave at point z. |
| I(z,ω) | The total complex current phasor at point z. |
| I_+ (z,ω) | The complex current phasor of the forward wave at point z. |
| I_- (z,ω) | The complex current phasor of the reverse wave at point z. |
| γ | The propagation constant. |
| α | The attenuation constant. |
| β | The phase constant. |
| R | Resistance per unit distance (Ωm^(-1) ). |
| L | Inductance per unit distance (Hm^(-1) ). |
| C | Capacitance per unit distance (Fm^(-1) ). |
| G | Conductance per unit distance (℧m^(-1)). |
| Z_0 | Characteristic impedance of the transmission line. |

The voltage equation in the time domain can be written as follows.

[IMAGE alt='image' src='GUID-A9EB50C1-5DB4-441F-85B9-00762C39BB0D-a5.png']

where V_+ (0,ω)=Re{V_+ (0,ω)} is the amplitude of the forward wave at point z=0 and
 V_- (0,ω)=Re{V_- (0,ω)} is the amplitude of the reverse wave at the same point.

<!--NI_TOPIC bundle=rfmx-vna path=new-features-and-changes.html language=enus -->
## TOPIC 00015: RFmx VNA New Features and Changes

- bundle_id: `rfmx-vna`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx VNA. Discover what is new in the latest releases of RFmx VNA.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might includ

### RFmx VNA
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx VNA.

RFmx VNA

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx VNA
 2026 Q2 Changes

This version of the RFmx VNA adds support for
 two-port Calibration & Measurement with a Switch Module for rack-mount use cases,
 automatic port extension, and Python API. These updates help you automate workflows and
 simplify common measurement setups.

##### New
 Features

This version of RFmx VNA adds support for the following
 features:

- Two port Calibration & Measurement with Switch modules for rack-mount use
 cases.
- Automatic port extension.
- Python API.

#### RFmx VNA 2025 Q4 New Features and
 Changes

##### New
 Features

- Support for one path two port measurement.
- Support for correction level API.

##### Behavior Changes

- Correction Port Subset Ports has been renamed to
 Correction Port Subset Full Ports . When the
 Correction Port Subset is
 Enabled , the ports specified in this subset are full
 N-Port corrected, where N is the number of specified ports.
 Correction State is made per measurement.
- RFmxVNA Configure Correction Port Subset.vi has been
 deprecated. Use Correction Port Subset Full Ports 
 attributes to configure the port subset.

#### RFmx VNA 2025 Q3 New Features and
 Changes

##### New
 Features

- Support for CW Time Sweep Type to measure DUT parameters (S-parameters or Waves)
 versus Time at a fixed frequency .
- Support for measuring group-delay using Group Delay format.
- Support for configuring group-delay aperture as Points, Percentage or Frequency
 Span using the Aperture Mode property.
- Support for Segment Trigger Mode .

#### RFmx VNA 2025 Q2 New Features and
 Changes

##### New
 Features

- Support for Trace Math.
- Support for Auto Detection of vCal Orientation.
- Support for events:
  - Ready for Trigger Event.
  - Index after last sweep point acquisition complete.
- Support for Trigger Delay.
- Support for Distance-Velocity factor based definition for Port Extension.
- Support for placing Normal, Fixed and Delta Markers on memory traces.
- Support for Max, Min, Peak, Next Left Peak, Next Right Peak Marker search
 operations on memory traces.

##### Behavior Changes

- Obsoleted property Number of Frequency Points . Use
 Number of Points instead.

#### RFmx VNA 2025 Q1 New Features and
 Changes

##### New
 Features

- Support for copying measured S-parameter data and loading data from SnP file into a user-defined named memory trace.
- Support for placing Normal, Fixed and Delta Markers on measurement traces.
- Support for Max, Min, Peak, Next Left Peak, Next Right Peak Marker search operations on Real Data traces.
- Support for coaxial cable loss model based Port Extension with user-defined losses for up to two frequency points.
- Concept help documentation added.

#### RFmx VNA 2024 Q4 New Features and
 Changes

##### New
 Features

- Support to specify polar format for S-parameters and Waves.
- Support to query S-parameters and waves in concise notation.
- Support for interpolation of corrected S-parameters and waves measurements.
- Support to query correction state.

##### Changes

- The following fetch VIs are deprecated:
  - RFmxVNA SParams Fetch Real Data.vi
  - RFmxVNA SParams Fetch Complex Data.vi
  - RFmxVNA Waves Fetch Real Data.vi
  - RFmxVNA Waves Fetch Complex Data.vi
- Tip Use the
 following VIs to fetch measurement data:RFmxVNA SParams Fetch Y Data.vi
 RFmxVNA Waves Fetch Y Data.vi 
 Tip Use the
 following VIs to fetch measurement frequency:RFmxVNA SParams Fetch X Data.vi
 RFmxVNA Waves Fetch X Data.vi
- The Undefined Thru Using Defined Thru option for
 Correction:Calibration:Thru:Method is deprecated.
- The Delay Thru Using Defined Thru option for
 Correction:Calibration:Thru:Method has been replaced by
 vCal Thru as Unknown Thru .
- Uninstalling RFmx VNA software also removes any previous versions of RFmx VNA
 .NET runtimes that were leaked in .NET Global Assembly Cache directory.

#### RFmx VNA 2024 Q3 New Features and
 Changes

##### New Features

- Support for List, Linear, and Segmented Sweep types
- Support for exporting S-parameter measurement results as SnP files
- Support for SWR, Impedance, and Admittance formats for S-parameters
- Support for exporting Pulse Generator events
- Support for aborting an ongoing calibration step

##### Behavior Changes

- Deprecated RFmxVNA Configure Frequency List (Start Stop
 Points).vi . Note To work around this change, configure
 Sweep Type to Linear, and
 configure Start Frequency (Hz), Stop
 Frequency (Hz), and Number of
 Frequency properties.
- You can no longer obtain the underlying list of aggregated frequencies across
 all active segments using the Sweep:Frequency List attribute.
 Note Use the Sweep:X-Axis Values read-only attribute
 instead.
- The Complex format in InstrumentStudio is no longer plotted as
 a Smith Chart. It is now plotted as a polar chart. Note To plot a Smith chart,
 set the format to Smith Impedance or Smith
 Admittance.

#### RFmx VNA 2024 Q2 New Features and
 Changes

- Support for external triggers for VNA measurements
- Support for saving and loading stimulus settings along with Calset
- Support for enabling and disabling automatic scaling down of Intermediate Frequency
 Bandwidth (IFBW) at low frequencies for measurement speed
- Support for caching multiple signal switch for measurement speed
- Support for guided calibration using Mechanical Calkits defined by NI Calkit files
 (.nckt )
- Support for basic pulsed S-parameter and waves measurements with internal
 pulse-trigger
- Support for embed fixtures to Calsets
- Support for creating and editing Calkit files for Mechanical Calkits using the
 standalone Calkit Editor application.
- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the appropriate
 RFmxInstr Load Options property, instead.

#### RFmx VNA 2024 Q1 New Features and
 Changes

- Calibration: User-defined orientation for Cal-5501
- Calsets
  - Load one or more named calsets from calset files previously saved
  - Select an active calset from the pool of loaded named calsets
  - Query the names of all loaded named calsets
  - Create a named copy of another named or unnamed calset
  - Query the error terms stored in a calset
- Support for RFmxVNA SParams and RFmxVNA Waves measurements to perform as composite measurements
- Added port extension support to specify electrical-length as delay (in seconds) and compensate for constant loss
- IVI simulation support for PXIe-5633

#### RFmx VNA 2023 Q4 Features Overview

- Measure corrected and uncorrected 1-port or 2-port S-parameters and receiver waves
 for non-frequency-converting RF devices over a list of frequencies
- Fixture de-embedding
- Point averaging
- Automatic Short-Open-Load (SOL) and Short-Open-Load-Through (SOLT) calibration using
 Cal-5501 Vector Calibration Module
- Saving and loading calibration error terms as a calset file
- Support for PXIe-5633

<!--NI_TOPIC bundle=rfmx-vna path=notes-on-calset-interpolation.html language=enus -->
## TOPIC 00016: Notes On Calset Interpolation

- bundle_id: `rfmx-vna`
- source_path: `notes-on-calset-interpolation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/notes-on-calset-interpolation.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the frequency points used for measurement deviate from the calibrated frequency points, error term interpolation can be enabled to obtain corrected measurements. However, interpolated error correction entails a reduction in measurement accuracy and should be used judiciously. Interpolation errors

### Notes On Calset Interpolation

- If the frequency points used for measurement deviate from the calibrated frequency
 points, error term interpolation can be enabled to obtain corrected measurements.
 However, interpolated error correction entails a reduction in measurement accuracy
 and should be used judiciously.
- Interpolation errors can be significant when the calibration frequency grid spacing
 is sufficiently large to result in a phase shift exceeding 180 degrees. One rule of
 thumb is to keep the point around 25 points per cycle (phase shift of 360 degrees),
 ensuring that the phase shift between adjacent points is less than 15 degrees.
- In test setups with long cables or fixtures with long electrical lengths, the phase
 of error terms is expected to change at a faster rate across adjacent points. Longer
 test fixtures require proportionally denser frequency grids for satisfactory
 interpolation results. (3)Δf≅vpcΔϕ720L 
 In the above equation, the approximate frequency step size, Δf Hz for a fixture
 of length L meters, keeping phase change across adjacent points to around Δϕ
 degrees. v_p is fixture’s velocity factor and c is the speed of light in
 vacuum. 
 For example, calibrating with a 1 meter long cable requires a frequency-grid step
 size of 5 MHz or smaller, assuming phase difference between adjacent points is
 kept to around 15 degrees or less.

Parent topic:

User Calibration

<!--NI_TOPIC bundle=rfmx-vna path=overdetermined-solt-calkit-example.html language=enus -->
## TOPIC 00017: Overdetermined SOLT Calkit Example

- bundle_id: `rfmx-vna`
- source_path: `overdetermined-solt-calkit-example.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/overdetermined-solt-calkit-example.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using more than the minimum required calibration standards results in a over-determined calibration. RFmx VNA supports overdetermined calibration for the one-port SOL calibration which is also part of the SOLT calibration. The example below shows a calkit for 2.4 mm Female connector type having one-

### Overdetermined SOLT Calkit Example

Using more than the minimum required calibration standards results in a over-determined
 calibration. RFmx VNA supports overdetermined calibration for the one-port SOL
 calibration which is also part of the SOLT calibration.

The example below shows a calkit for 2.4 mm Female connector type having one-port
 standards Short, Open Load and two additional Offset Shorts. Set the usage type for all
 one-port elements to Termination to indicate to the RFmx VNA
 calibration to use all of the elements during calibration.

[IMAGE alt='image' src='GUID-27A4F65F-E53D-436A-84BF-BC127205C491-a5.png']

Parent topic:

Creating Calkits for Calibration Methods

<!--NI_TOPIC bundle=rfmx-vna path=pulse-acquisition.html language=enus -->
## TOPIC 00018: Pulse Acquisition

- bundle_id: `rfmx-vna`
- source_path: `pulse-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/pulse-acquisition.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generally, it is desirable to perform pulse measurements by ensuring that acquisitions are performed within the stable portions of the generated pulses to avoid transients. By default, RFmx tries to use 75% of the configured pulse width, avoiding the first 20% and last 5% of the pulse width. To achi

### Pulse Acquisition

Generally, it is desirable to perform pulse measurements by ensuring that acquisitions
 are performed within the stable portions of the generated pulses to avoid transients.

By default, RFmx tries to use 75% of the configured pulse width, avoiding the
 first 20% and last 5% of the pulse width. To achieve this, RFmx automatically sets
 Pulse Acquisition Delay and Pulse Acquisition
 Width properties based on the user-defined Pulse Modulator
 Width as follows:

- Pulse Acquisition Delay is set as the sum of Pulse
 Modulator Delay and ~20% of the Pulse Modulator
 Width , and
- Pulse Acquisition Width is set to ~75% of the
 Pulse Modulator Width .

You can manually set or adjust the acquisition width and delay by setting
 Pulse Acquisition Auto to False and
 configuring Pulse Acquisition Delay and Pulse
 Acquisition Width properties as desired.

Note

In pulse mode, you cannot set IF Bandwidth directly. Instead,
 IF Bandwidth is always derived from the Pulse
 Acquisition Width property. Derived IF bandwidth can be obtained by
 querying the IF Bandwidth property.

Note

Desired Pulse Acquisition Width may not always be honored.
 This is because there are only a finite number of supported IF
 Bandwidth values, and each supported IF
 Bandwidth is uniquely associated with a corresponding supported
 Pulse Acquisition Width. If the desired Pulse
 Acquisition Width matches exactly with one of the supported pulse
 acquisition widths, then it is used without any coercion. Otherwise, it coerced to
 the nearest supported pulse acquisition width whose value is less than the desired
 Pulse Acquisition Width. You can read the actual value of
 the pulse acquisition width used for pulse measurements by querying the
 Pulse Acquisition Width property.

Parent topic:

Pulse Mode

<!--NI_TOPIC bundle=rfmx-vna path=pulse-generators.html language=enus -->
## TOPIC 00019: Pulse Generators

- bundle_id: `rfmx-vna`
- source_path: `pulse-generators.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/pulse-generators.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: VNA supports up to four onboard digital pulse generators, which can generate pulses for synchronizing external devices to the VNA Pulse Trigger. Each pulse generator outputs a digital pulse for each asserted pulse trigger. Pulse generators operate independently, allowing you to set different delays

### Pulse Generators

VNA supports up to four onboard digital pulse generators, which can generate pulses for
 synchronizing external devices to the VNA Pulse Trigger.

Each pulse generator outputs a digital pulse for each asserted pulse trigger.
 Pulse generators operate independently, allowing you to set different delays and pulse
 widths for each. You can export generated pulses to PFI ports or to PXI trigger
 lines.

Your application may require a digital pulse with its ON duration
 coinciding with the active duration of the RF pulse. An onboard pulse generator can be
 used to generate such a pulse, by setting the value of the Pulse Generator
 Delay attribute to match the Pulse Modulator
 Delay attribute and setting the value of the Pulse Generator
 Width attribute to match the Pulse Modulator
 Width attribute. RF Modulator Delay is the time
 it takes for the RF pulse to settle after the Pulse Modulator Drive signal is turned
 ON. RFmx automatically adjusts each pulse generator’s delay
 to compensate for the RF Modulator Delay. However, reading back
 the Pulse Generator Delay attribute returns the user-configured
 value of the pulse generator delay only, and not modulator-delay compensated value.

Parent topic:

Pulse Mode

<!--NI_TOPIC bundle=rfmx-vna path=pulse-mode.html language=enus -->
## TOPIC 00020: Pulse Mode

- bundle_id: `rfmx-vna`
- source_path: `pulse-mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/pulse-mode.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: In pulse mode, the VNA measures the s-parameters of devices under test (DUTs) using pulsed RF signals. VNA generates a pulsed RF signal by modulating the continuous wave source on and off as per the configured pulse period and width. The acquisitions in pulse mode are synchronized with the pulse gen

### Pulse Mode

In pulse mode, the VNA measures the s-parameters of devices under test (DUTs) using
 pulsed RF signals. VNA generates a pulsed RF signal by modulating the continuous wave
 source on and off as per the configured pulse period and width. The acquisitions in
 pulse mode are synchronized with the pulse generation.

<!--NI_TOPIC bundle=rfmx-vna path=pulse-timing.html language=enus -->
## TOPIC 00021: Pulse Timing Diagram

- bundle_id: `rfmx-vna`
- source_path: `pulse-timing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/pulse-timing.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The figure below shows the timing of various digital and RF pulses relative to the pulse trigger. For each asserted pulse trigger, the VNA generates various signals as described in the table below. Signal Description Ports / Terminals Pulse Modulator Drive Internal digital pulse that drives the RF p

### Pulse Timing Diagram

The figure below shows the timing of various digital and RF pulses relative to the pulse
 trigger.

[IMAGE alt='image' src='GUID-A55FAFA1-622A-482E-8B4A-861584FE421B-a5.png']

For each asserted pulse trigger, the VNA generates various signals as described in the
 table below.

| Signal | Description | Ports / Terminals |
| --- | --- | --- |
| Pulse Modulator Drive | Internal digital pulse that drives the RF pulse modulator. | None (internal only) |
| RF Pulse | RF signal put out by RF pulse modulator. | VNA RF source port |
| Acquisition Pulse | A simplified representation of the digital signal that triggers the VNA ADCs. Pulse delay and width illustrate the portion of the RF pulse acquired for measurements. | None |
| Pulse Generator (1-4) | Flexible user-defined digital pulse signals. | PFI ports, PXI trigger lines |

Parent topic:

Pulse Mode

<!--NI_TOPIC bundle=rfmx-vna path=pulse-trigger.html language=enus -->
## TOPIC 00022: Pulse Trigger

- bundle_id: `rfmx-vna`
- source_path: `pulse-trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/pulse-trigger.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you first enable the pulse mode, the VNA continuously generates a pulsed RF signal with user-defined pulse repetition interval and duty cycle. The VNA achieves this by continuously generating a periodic digital impulse. The period is defined by the specified Pulse Period. A rising edge of each

### Pulse Trigger

When you first enable the pulse mode, the VNA continuously generates a pulsed RF signal
 with user-defined pulse repetition interval and duty cycle. The VNA achieves this by
 continuously generating a periodic digital impulse. The period is defined by the
 specified Pulse Period. A rising edge of each such impulse
 triggers the generation of one instance of all the required digital pulses (such as
 Pulse Modulator Drive, Acquisition Pulse) as shown in the pulse timing illustration
 above. Each instance of this digital impulse is referred to as a Pulse
 Trigger.

Apart from generating pulse triggers internally, the VNA can be
 configured to receive external digital triggers. In RFmx VNA, you can use external
 digital triggers as pulse triggers by setting the Pulse Trigger
 Type property to Digital Edge and specifying the
 desired Pulse Trigger Source terminal. Instead of continuously
 generating pulse signals, the VNA waits until it receives an external digital edge pulse
 trigger. For each asserted external digital pulse trigger, the VNA generates one
 instance of all the required pulses such as Pulse Modulator
 Drive, Acquisition Pulse as shown in the Pulse Timing
 diagram above.

When using external pulse triggers, the VNA does not automatically
 generate pulses on a periodic basis. To achieve periodic pulse generation, ensure that
 external pulse triggers are continuously generated, with a separation interval equal to
 the desired pulse period.

Parent topic:

Pulse Mode

<!--NI_TOPIC bundle=rfmx-vna path=s-param-calibration-element-def.html language=enus -->
## TOPIC 00023: S-Parameter-Based Definition of a Calibration Element

- bundle_id: `rfmx-vna`
- source_path: `s-param-calibration-element-def.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/s-param-calibration-element-def.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: For S-Parameter-based definition of a calibration element, either import the S-parameter from an SnP file, or enter the S-parameters directly in a table.

### S-Parameter-Based Definition of a Calibration Element

For S-Parameter-based definition of a calibration element, either import the S-parameter
 from an SnP file, or enter the S-parameters directly in a
 table.

[IMAGE alt='image' src='GUID-031B7E7D-B22D-430F-9CC9-D0F7DC43C316-a5.png']

Parent topic:

Calibration Elements Tab

<!--NI_TOPIC bundle=rfmx-vna path=s-parameters.html language=enus -->
## TOPIC 00024: S-Parameters

- bundle_id: `rfmx-vna`
- source_path: `s-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/s-parameters.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: S-parameters are employed to characterize any N- port linear electrical network as an N×N matrix of complex numbers. This matrix is used to express reflected wave amplitudes at each port as a linear combination of the incident wave amplitudes at all ports. In a two-port network, S-parameters help ex

### S-Parameters

S-parameters are employed to characterize any N- port linear electrical network as an N×N
 matrix of complex numbers. This matrix is used to express reflected wave amplitudes at
 each port as a linear combination of the incident wave amplitudes at all ports.

[IMAGE alt='image' src='GUID-4F18F9F6-D940-4CA0-9BBD-8D44B024EC13-a5.png']

[IMAGE alt='image' src='GUID-26C15A75-4FD0-40F4-8687-957554C65496-a5.jpg']

In a two-port network, S-parameters help express the scattered waves b_1 and b_2 as
 linear combinations of incident waves a_1 and a_2 as follows

[IMAGE alt='image' src='GUID-BAAD1F2D-998E-4C03-A4C0-2CD603D78FB4-a5.png']

The figure below illustrates the concept of “reflected” and “transmitted” waves when
 “incident” wave (stimulus) is directed towards port 1 of a two-port DUT. Setting a_2=0,
 equation 9 states that S_11 is the ratio of reflected and incident waves, while S_21 is
 the ratio of transmitted and incident waves

[IMAGE alt='image' src='GUID-07F507AF-3997-4573-9CBE-D2A8E873BFCD-a5.png']

[IMAGE alt='image' src='GUID-07A40CAC-9EA3-4A7F-80E9-FE92E5672ECE-a5.png']

Assuming a_1=0, S_22 can be interpreted as the ratio b_2/a_2, and S_12 can be interpreted
 as the ratio b_1/a_2.

In the context of a two-port DUT S11 and S21, are sometimes referred to as forward
 S-parameters because the incident signal originates from the RF source on port one. With
 the incident source on port two, S22 and S12 are called the reverse S-parameters.

| S-Parameter | Direction | Description |
| --- | --- | --- |
| S11 | Reflected | The ratio of the voltage reflected at port one to the incident voltage placed on port one. |
| S21 | Transmitted | The ratio of the voltage transmitted through the DUT present at port two to the incident voltage placed on port one. |
| S22 | Reflected | The ratio of the voltage reflected at port two to the incident voltage placed on port two. |
| S12 | Transmitted | The ratio of the voltage transmitted through the DUT present at port one to the incident voltage placed on port two. |

Generalizing to N-port DUTs, S-parameters are represented using the notation S_ij and can
 be interpreted as the ratio of the voltage transmitted to port i to the voltage incident
 on port j assuming that incident waves at all other ports are 0, as represented in the
 following equation:

[IMAGE alt='image' src='GUID-7CFBCCA8-B8C7-429D-91BD-A36DE6F1CB85-a5.png']

Parent topic:

Network Analysis

<!--NI_TOPIC bundle=rfmx-vna path=solt-calkit-example.html language=enus -->
## TOPIC 00025: Example SOLT Calkit

- bundle_id: `rfmx-vna`
- source_path: `solt-calkit-example.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/solt-calkit-example.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following image shows a typical coaxial SOLT Calkit composed of: the one-port calibration standards Short, Open and Load for a specific connector type (2.4 mm) both genders (Female and Male) 3 two-port Thru standards, one for each combination of genders

### Example SOLT Calkit

The following image shows a typical coaxial SOLT Calkit composed of:

- the one-port calibration standards Short, Open and Load for a specific connector
 type (2.4 mm)
- both genders (Female and Male)
- 3 two-port Thru standards, one for each combination of genders

[IMAGE alt='image' src='GUID-F29E1626-194B-485C-B6A7-0ADB9BC62BF9-a5.png']

Parent topic:

Creating Calkits for Calibration Methods

<!--NI_TOPIC bundle=rfmx-vna path=system-requirements.html language=enus -->
## TOPIC 00026: RFmx VNA System Requirements

- bundle_id: `rfmx-vna`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/system-requirements.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx VNA has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory may be required

### RFmx VNA System Requirements

RFmx VNA has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-vna path=systematic-errors-in-vna-measurements.html language=enus -->
## TOPIC 00027: Systematic Errors in VNA Measurements

- bundle_id: `rfmx-vna`
- source_path: `systematic-errors-in-vna-measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/systematic-errors-in-vna-measurements.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Factory calibrated VNAs still return measurements that are impacted by systematic errors due to non-ideal instrumentation, cables, connectors/adapters, and other test fixtures etc. For making accurate measurements, users must characterize such systematic errors. Once characterized, subsequent VNA me

### Systematic Errors in VNA
 Measurements

Factory calibrated VNAs still return measurements that are impacted by systematic errors
 due to non-ideal instrumentation, cables, connectors/adapters, and other test fixtures
 etc. For making accurate measurements, users must characterize such systematic errors.
 Once characterized, subsequent VNA measurements are compensated for such errors.
 Characterization of these errors is referred to as user-calibration or simply
 calibration.

The set of error-terms obtained after performing calibration is referred to as
 calset.

Refer to the relevant error model topic for a brief description of that model.

Parent topic:

Network Analysis

<!--NI_TOPIC bundle=rfmx-vna path=timing-diagrams.html language=enus -->
## TOPIC 00028: Timing Diagrams

- bundle_id: `rfmx-vna`
- source_path: `timing-diagrams.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/timing-diagrams.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: OverviewUnless specified otherwise, timing diagrams in this section use the following notations. TRIGGER Active edge of the digital signal that triggers data acquisition. Timing diagrams assume the active edge is Rising. READY The Ready For Trigger digital signal represents the readiness of the inst

### Timing Diagrams

#### Overview

Unless specified otherwise,
 timing diagrams in this section use the following notations.

| TRIGGER | Active edge of the digital signal that triggers data acquisition. Timing diagrams assume the active edge is Rising. |
| --- | --- |
| READY | The Ready For Trigger digital signal represents the readiness of the instrument to receive a trigger. The timing diagrams assume default polarity for this signal in which a LOW level indicates that the VNA is ready to receive a trigger. |
| DATA | The data acquired by the instrument. |
| INDEX | Indicates that the instrument has completed all acquisitions needed for the configured measurements. The timing diagrams assume default polarity in which the digital signal remains HIGH until the VNA completes all the acquisitions for the DUT and then switches to LOW. |
| ttrig | Trigger delay. |
| tsweep | Sweep delay. |
| tdwell | Dwell time. |
| f1, f2, ... fx. | Indicates that the instrument is acquiring data for the first frequency point, second frequency point and so on. |

Note

- Timing diagrams illustrating data acquisition assume a value of 2 for the
 following parameters.
  - Number of segments (for the Segment trigger
 mode)
  - Ports
  - Number of frequency points (per segment for the
 Segment trigger mode)
  - Averaging count
- For the Segment trigger mode, the first segment
 consists of frequencies f 1 and f 2 , while the second
 segment consists of frequencies f 3 and f 4 .

#### Trigger Mode: Signal

Data for all points, averaging iterations, and
 source directions are acquired after asserting just one Signal
 trigger. The Sweep Sequence determines the order for performing
 acquisitions.

Sweep Sequence: Standard

In the
 Standard sweep sequence, the analyzer measures all
 frequency points for one source port, before moving on to the next source
 port.

[IMAGE alt='image' src='GUID-1F068E34-00A9-4803-AA5B-5695C1888D00-a5.svg']

Sweep Sequence: Point

The analyzer measures a frequency point from all
 source port directions before moving to the next frequency point.

[IMAGE alt='image' src='GUID-A7B340E6-57BB-49B7-B963-D8B7B6C239F8-a5.svg']

#### Trigger Mode: Point

All averaging iterations for a frequency point and
 source port combination are acquired by one trigger instance. The Sweep
 Sequence determines the order of acquisitions.

Sweep Sequence:
 Standard

The analyzer measures all frequency points for one source port,
 before moving on to the next source port.

[IMAGE alt='image' src='GUID-0402393C-426E-4E00-855B-911047E2B59D-a5.svg']

Sweep Sequence: Point

The analyzer measures a frequency point from all
 source port directions before moving to the next frequency point.

[IMAGE alt='image' src='GUID-660BD388-E28F-4D67-8B15-FEBD0302EDBC-a5.svg']

#### Trigger Mode: Sweep

Each change in source port direction requires a
 trigger.

Sweep Sequence: Standard

The analyzer measures all frequency
 points for one source port, before moving on to the next source port.

[IMAGE alt='image' src='GUID-EA8B1417-A38A-4593-BEE4-D2015442D644-a5.svg']

Sweep Sequence: Point

The analyzer measures a frequency point from all
 source port directions before moving to the next frequency point.

[IMAGE alt='image' src='GUID-660BD388-E28F-4D67-8B15-FEBD0302EDBC-a5.svg']

#### Trigger Mode: Segment

Each change in segment requires a trigger.

Sweep Sequence: Standard

The analyzer measures all frequency points for
 one source port, before moving on to the next source port.

[IMAGE alt='image' src='GUID-A991EA24-F2FC-40A9-88DA-1B5E8CED7ADE-a5.svg']

Sweep Sequence: Point

The analyzer measures a frequency point from all
 source port directions before moving to the next frequency point.

[IMAGE alt='image' src='GUID-F82914C6-A7ED-484B-BDD0-F0D85D5D1AD2-a5.svg']

<!--NI_TOPIC bundle=rfmx-vna path=trl-calkit-example.html language=enus -->
## TOPIC 00029: TRL Calkit Example

- bundle_id: `rfmx-vna`
- source_path: `trl-calkit-example.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/trl-calkit-example.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: A TRL calibration is performed by measuring a Thru connection, an Reflect standard which has to be identical at both ports, and a Line standard. The TRL algorithm defines the calibration plane at the center of the Thru and the characteristic impedance is defined by the Line impedance (TRL algorithm

### TRL Calkit Example

A TRL calibration is performed by measuring a Thru connection, an Reflect standard which
 has to be identical at both ports, and a Line standard.

The TRL algorithm defines the calibration plane at the center of the Thru and the
 characteristic impedance is defined by the Line impedance (TRL algorithm defines the
 Line with zero reflections).

The calibration elements must meet the following requirements.

- The Thru has to be a zero length Thru. The ports are directly connected.
- The Reflect standard does not need to be specific. Specify the phase within a range
 of ±90 degrees. The Phase must be identical for both ports.
- The TRL algorithm does not require the line parameters. The TRL algorithm requires
 the phase difference between Line and Thru within the range of 20 to 160 degrees
 such that the frequency range for the algorithm is determined by the line
 length/delay. [IMAGE alt='image' src='GUID-C24EE689-90E3-4E30-8B7D-7F3EFA6781CF-a5.png']

The following figure shows a TRL Calkit using a Line with a delay of 100 ps. This results
 in a frequency range of 556 MHz to 4.4 GHz.

[IMAGE alt='image' src='GUID-40988457-DEAE-4B58-BE9A-AD059ACD092A-a5.png']

- The Thru is configured as ideal Thru using the Delay model with the delay configured
 as zero. Set the Usage flag to Thru to indicate for the RFmxVNA calibration that
 this calibration element can be used as a Thru.
- Reflect is configured as an ideal Short using the Reflect Short model having all
 inductance coefficients set to zero. The Offset Delay is also configured as zero.
 The Usage flag is checked as Reflect to indicate to the RFmxVNA calibration that
 this calibration element can be used as Reflect for TRL calibration.
 Note If you have a Offset Reflect with some
 Offset Delay, the accuracy of the delay follows from the TRL requirement knowing
 the phase of the reflect with accuracy of ±90 degrees.
 [IMAGE alt='image' src='GUID-9410F5F6-E1D2-4C48-82F3-64C81F4E64CF-a5.png']
- The Line is configured using the two-port delay model with the delay configured as
 100 ps and the minimum and maximum frequency derived from the 20/160 degree rule.
 The Usage flag is checked as Line to indicate to the RFmxVNA calibration that this
 calibration element can be used as Line for TRL calibration.

Parent topic:

Creating Calkits for Calibration Methods

<!--NI_TOPIC bundle=rfmx-vna path=trl-lrl-options.html language=enus -->
## TOPIC 00030: TRL/LRL Options

- bundle_id: `rfmx-vna`
- source_path: `trl-lrl-options.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/trl-lrl-options.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the TRL algorithm along with the calkit. TRL Reference PlaneFor a non-zero length Thru, the reference plane of the calibration needs to get shifted from the center of the Thru to the calibration ports. Select from these options. Thru Default and recommended mode. The reference plane is shi

### TRL/LRL Options

Configure the TRL algorithm along with the calkit.

- TRL Reference Plane For a non-zero length Thru, the reference plane of the
 calibration needs to get shifted from the center of the Thru to the calibration
 ports. Select from these options.
- Thru —Default and recommended mode. The reference plane is shifted by the Thru
 delay.
- Reflect —In case the Reflect delay is more accurately known than the Thru delay,
 the TRL algorithm shifts the calibration plane according to the
 definition of the Reflect.
- LRL Line Auto Characterization If the Thru/Line have some loss, this option can be
 checked to let the TRL calibration algorithm estimate the loss and use it when
 shifting the reference plane from the center of the Thru to the calibration
 ports. This option does not work when the propagation constant of the Thru and
 the Line standards differ.

[IMAGE alt='image' src='GUID-BD39CBA1-C4AF-40E7-B414-D690E2F3CBDE-a5.png']

Parent topic:

Calkit Editor

<!--NI_TOPIC bundle=rfmx-vna path=user-calibration.html language=enus -->
## TOPIC 00031: User Calibration

- bundle_id: `rfmx-vna`
- source_path: `user-calibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/user-calibration.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: User calibration refers to the process of characterizing systematic errors in VNA measurements. Error terms in the correction model are found by comparing known and measured S-parameters of calibration standards—specialized electrical reference devices. A collection of calibration standards that can

### User Calibration

User calibration refers to the process of characterizing systematic errors in VNA
 measurements. Error terms in the correction model are found by comparing known and
 measured S-parameters of calibration standards—specialized electrical reference
 devices.

A collection of calibration standards that can be used to perform user calibration is
 called a calibration kit or simply calkit.

Perform user calibration to identify error terms in the correction model and apply these
 user calibrations to correct future VNA measurements.

Note

#### Calibration Procedures

#### Short Open Load (SOL)

SOL cal requires short, open, and load calibration standards. The exact standard
 values are provided to the VNA in the form of a calibration kit file. The connection
 point for calibration standards is called the reference plane or calibration plane.
 This calibration plane can be a port, cable end, or test fixture. SOL cal is a
 one-port calibration procedure and is suitable for performing error corrected
 measurements of one-port DUTs.

#### Short Open Load Thru
 (SOLT)

For two-port VNA calibration, in addition to performing SOL calibrations on each
 port, you must measure an insertable through connection. Use a male-to-female cable
 or similar connection during SOLT calibration. Avoid external adapters or devices
 when completing the through connection. The inserted thru can be known or unknown.

Known Thru

Unknown Thru

Known Thru and Unknown Thru calibrations are abbreviated as SOLT and SOLR
 respectively. The R in SOLR stands for Reciprocal Thru, emphasizing the reciprocity
 assumption stated above.

#### Thru Reflect Line (TRL)

TRL is one type in a family of two-port calibrations that better support noncoaxial
 environments such as on-wafer measurements and test fixturing. In this family, the
 name of the calibration is an acronym that identifies the following necessary
 calibration standards.

- Through-Reflect-Line (TRL)
- Line-Reflect-Match (LRM)
- Line-Reflect-Line (LRL)
- Through-Reflect-Match (TRM)

These calibrations derive error terms for the same error model as SOLT
 calibrations.

Compared to SOLT, TRL requires fewer calibration standards. Typically, three
 standards are required for performing a TRL calibration. In noncoaxial environments,
 standards are often harder to obtain but still easier to fabricate than performing a
 calibration and measurement with coaxial connections. Calibration standards must be
 precisely made, as measurement accuracy depends on their quality and repeatability.
 These calibrations generally use combinations of through, line, reflection, and
 match standards. The following table defines the standards that are used in these
 calibrations.

| Standard | Description |
| --- | --- |
| Through | Ideally, a zero length through line where the measurement ports are directly connected. An alternative would be a line with electrical length, but this line must be electrically distinct from any other line standard. The intrinsic impedance of the through and line standards set the impedance of the calibration. |
| Reflection | A highly reflective device (most often a short or open). The absolute reflection coefficient comes from extra standard measurements. Phase knowledge must be within ±90° (¼ wavelength) to correctly identify the standard. It is important that you use the equivalent reflection standards to calibrate both ports. |
| Line | A nonzero length through line with the same intrinsic impedance as the through standard. The difference between the phase shifts of the line and through standards requires a minimum of 10 degrees to 170 degrees. Alternatively, a preferred 20 degrees to 160 degrees for each frequency. Knowledge of the propagation constant is not necessary because you can derive it from the extra measurement information. The required phase relationship between through and line standards limits the measurable frequency span. Each standard pair supports only a specific frequency range. If you need larger frequency spans, use multiple through and line pairs. |
| Match | If a match standard is used in place of a line standard, you can use its impedance to set the impedance of the calibration. The match standard should be identical for each port and should generally use characterized data or assume data to be a perfect match. |

TRL is a calibration form that makes use of fewer standards, requiring less knowledge
 about the standards. TRL calibration is highly suited for noncoaxial environments
 where traditional standards may be hard to fabricate and fully characterize. TRL
 calibration requires high-quality, repeatable standards to ensure accurate
 calibrations. Phase-based standard identification limits the frequency span. You can
 extend it by adding more calibration standards as needed. Much of the standard
 characterization is extracted during measurement. This improves calibration accuracy
 compared to SOLT.

#### Electronic Calibration

Electronic calibration (vCal) units simplify SOL and SOLT calibrations. They offer
 faster setup, better repeatability, and greater ease of use. vCal units also remove
 most manual interaction, greatly reducing the chance of a human error during
 calibration. These vCal units typically house several one-port and or two-port
 calibration standards that can be switched electronically.

The VNA uses the standards of the vCal module to take RF measurements for
 calibration. VNA then automatically switches to the next standard. During
 calibration, the VNA measures vCal standards. VNA compares these results with known
 data to calculate the error terms.

Parent topic:

Network Analysis

<!--NI_TOPIC bundle=rfmx-vna path=user-manual-welcome.html language=enus -->
## TOPIC 00032: RFmx VNA User Manual

- bundle_id: `rfmx-vna`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx VNA User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx VNA
 User Manual

The RFmx VNA User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx VNA
- Interactive Activation Guide
- RFmx VNA Release Notes
- Getting Started with RFmx
- RFmx VNA LabVIEW Reference
- RFmx VNA .NET Reference
- RFmx VNA C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference

<!--NI_TOPIC bundle=rfmx-vna path=vector-network-analyzers.html language=enus -->
## TOPIC 00033: Vector Network Analyzers

- bundle_id: `rfmx-vna`
- source_path: `vector-network-analyzers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/vector-network-analyzers.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: A vector network analyzer (VNA) is piece of test equipment used in radio frequency (RF) engineering. A VNA can characterize the response of a device under test (DUT) by simultaneously measuring both forward and backward propagating waves. The figure below shows the simplified block diagram of a two-

### Vector Network Analyzers

A vector network analyzer (VNA) is piece of test equipment used in radio frequency (RF)
 engineering. A VNA can characterize the response of a device under test (DUT) by
 simultaneously measuring both forward and backward propagating waves. The figure below
 shows the simplified block diagram of a two-port VNA and its key signal processing
 components.

[IMAGE alt='image' src='GUID-EE630ED3-88E5-4247-9EA6-F1750D7A76A5-a5.png']

RF
 Source serves as the excitation source for the Device Under Test (DUT).
 The source can be programmed to generate a sinusoidal signal at a desired frequency and
 power level.

Signal separation devices like directional couplers isolate
 incident and reflected waves at each port. This enables the VNA to quantify the incident
 waves (a_1 and a_2) measured by the reference receiver (labelled REF RX 1 and REF RX 1)
 and reflected wave (b_1 and b_2) measured by the test receiver (labelled TEST RX 1 and
 TEST RX 2).

Receivers measure the incident, reflected, and transmitted
 signals. The signals that are separated out by directional couplers are down converted
 to IF. Reference receivers r_1 and r_2 measure the signal travelling from VNA towards
 the DUT (Incident signal). Test port receivers s_1 and s_2 measure the signal travelling
 away from the DUT towards VNA (reflected and transmitted signals). IF signals are
 digitized and digitally down-converted to baseband, followed by further DSP to return
 the complex traveling wave amplitudes. These steps are not shown in the simplified block
 diagram above.

Parent topic:

Network Analysis

<!--NI_TOPIC bundle=rfmx-vna path=warnings-and-errors.html language=enus -->
## TOPIC 00034: Warnings and Errors

- bundle_id: `rfmx-vna`
- source_path: `warnings-and-errors.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna/raw/resource/enus/warnings-and-errors.html
- document_id: `rfmx-vna`
- page_type: `leaf`
- content_type: `concept`
- source_description: The measurement throws a warning if the acquisition occurs outside the pulse ON duration. The measurement throws an error in the following scenarios. The sum of modulator delay and width exceeds the pulse period. The sum of acquisition delay and acquisition width exceeds the pulse period.

### Warnings and Errors

- The measurement throws a warning if the acquisition occurs outside the pulse ON
 duration.
- The measurement throws an error in the following scenarios.
  - The sum of modulator delay and width exceeds the pulse period.
  - The sum of acquisition delay and acquisition width exceeds the pulse
 period.

Parent topic:

Pulse Mode
