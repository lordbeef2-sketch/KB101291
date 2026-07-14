# NI DOCUMENT BUNDLE: rfmxvna-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxvna-c-api-ref start=1 end=130 -->
<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga16477e306821d8f921cd5e97ac578ca3.html language=enus -->
## TOPIC 00001: RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga16477e306821d8f921cd5e97ac578ca3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga16477e306821d8f921cd5e97ac578ca3.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the port extension delay in physical length. This value is expressed in meters by default. The unit can be chosen by setting the RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT attribute. This attribute is used only when you set the RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED attri

### RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE

Specifies the port extension delay in physical length. This value is expressed in meters by default. The unit can be chosen by setting the [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga79dd91be630335500f6931588dcb42ad.html) attribute. This attribute is used only when you set the [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga3f6a08cd7b1523ec61f75a40ea84f356.html) attribute to **True** and [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1gaf9ccb01f48b00cd31cbedea69fc1a9c0.html) attribute to **Distance**.

#### Syntax

RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631584 | float64 | Read/Write | Port |

#### Remarks

Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port. Use "port::all" to configure the same distance value for all VNA ports.

The default value is 0 m.

Parent topic:

Port Extension

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga272fbed8269ab1cd152531be18e7b30f.html language=enus -->
## TOPIC 00002: RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_VELOCITY_FACTOR

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga272fbed8269ab1cd152531be18e7b30f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga272fbed8269ab1cd152531be18e7b30f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the speed of light in the port extension medium relative to speed of light in vacuum. Velocity Factor of 1 represents speed of light in vacuum. This attribute is used in conjuction with RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE attribute to compute electrical delay. This value is uni

### RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_VELOCITY_FACTOR

Specifies the speed of light in the port extension medium relative to speed of light in vacuum. Velocity Factor of 1 represents speed of light in vacuum. This attribute is used in conjuction with [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga16477e306821d8f921cd5e97ac578ca3.html) attribute to compute electrical delay. This value is unitless. This attribute is used only when you set the [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga3f6a08cd7b1523ec61f75a40ea84f356.html) attribute to **True** and [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1gaf9ccb01f48b00cd31cbedea69fc1a9c0.html) attribute to **Distance**.

#### Syntax

RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_VELOCITY_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631586 | float64 | Read/Write | Port |

#### Remarks

Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port. Use "port::all" to configure the same velocity factor for all VNA ports.

The default value is 1.

Parent topic:

Port Extension

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga79dd91be630335500f6931588dcb42ad.html language=enus -->
## TOPIC 00003: RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga79dd91be630335500f6931588dcb42ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga79dd91be630335500f6931588dcb42ad.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit of the port extension delay in physical length. This attribute is used only when you set the RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED attribute to True and RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN attribute to Distance. SyntaxRFMXVNA_ATTR_CORRECTION_PORT_EXTENSION

### RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT

Specifies the unit of the port extension delay in physical length. This attribute is used only when you set the [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga3f6a08cd7b1523ec61f75a40ea84f356.html) attribute to **True** and [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1gaf9ccb01f48b00cd31cbedea69fc1a9c0.html) attribute to **Distance**.

#### Syntax

RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631585 | int32 | Read/Write | Port |

#### Remarks

Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port. Use "port::all" to configure the same distance unit for all VNA ports.

The default value is **Meters**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT_METERS | 0 (0x0) | The port extension physical length is expressed in meters. |
| RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT_FEET | 1 (0x1) | The port extension physical length is expressed in feet. |
| RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT_INCHES | 2 (0x2) | The port extension physical length is expressed in inches. |

Parent topic:

Port Extension

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1gaf9ccb01f48b00cd31cbedea69fc1a9c0.html language=enus -->
## TOPIC 00004: RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1gaf9ccb01f48b00cd31cbedea69fc1a9c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1gaf9ccb01f48b00cd31cbedea69fc1a9c0.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether port extension utilizes delay-based or distance-velocity factor-based definition. This attribute is used only when you set the RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED attribute to True. SyntaxRFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAINNumeric ValueData TypeAccessAppl

### RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN

Specifies whether port extension utilizes delay-based or distance-velocity factor-based definition. This attribute is used only when you set the [RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__correction__port__extension_1ga3f6a08cd7b1523ec61f75a40ea84f356.html) attribute to **True**.

#### Syntax

RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631583 | int32 | Read/Write | Port |

#### Remarks

Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port. Use "port::all" to configure for all VNA ports.

The default value is **Delay**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN_DELAY | 0 (0x0) | The port extension is specified in terms of its electrical delay. |
| RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN_DISTANCE | 1 (0x1) | The port extension is specified in terms of its physical length. |

Parent topic:

Port Extension

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__correction__port__subset_1ga36f0270619d0323dd0b444cecee7b084.html language=enus -->
## TOPIC 00005: RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_RESPONSE_PORTS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__correction__port__subset_1ga36f0270619d0323dd0b444cecee7b084.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__correction__port__subset_1ga36f0270619d0323dd0b444cecee7b084.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this attribute. Alternatively, measurement is

### RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_RESPONSE_PORTS

Specifies the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this attribute. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this attribute and another is specified using [RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_FULL_PORTS](group____root__ni_r_fmx_v_n_a__attributes__correction__port__subset_1ga5f36112bb12a29a82cbc026a59d72960.html). Measurements involving the ports outside the [RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_RESPONSE_PORTS](group____root__ni_r_fmx_v_n_a__attributes__correction__port__subset_1ga36f0270619d0323dd0b444cecee7b084.html) and [RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_FULL_PORTS](group____root__ni_r_fmx_v_n_a__attributes__correction__port__subset_1ga5f36112bb12a29a82cbc026a59d72960.html) return error.

#### Syntax

RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_RESPONSE_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631609 | char[] | Read/Write | N/A |

#### Remarks

This attribute is used only when you set the [RFMXVNA_ATTR_CORRECTION_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__correction_1gabbbb54e0e194a2a591851d51eed17b57.html) attribute to **True** and [RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__correction__port__subset_1ga34c82a229504a6e0de00a033c78d3edd.html) attribute to **True**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty string.

For example, when performing S21 error-corrected measurement for a 2-port DUT using a 2-port VNA and a 2-port calset, VNA generally acquires data by setting the source to port1 first and then to port2. To perform S21 one-path two-port error corrected measurement and to achieve faster measurement speed, set this attribute to **port1, port2**. VNA then acquires data using source port1 and skips acquiring data with source port2.

Parent topic:

Port Subset

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams_1ga680429775357cb85de5e0215f524425f.html language=enus -->
## TOPIC 00006: RFMXVNA_ATTR_SPARAMS_NUMBER_OF_SPARAMETERS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams_1ga680429775357cb85de5e0215f524425f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams_1ga680429775357cb85de5e0215f524425f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of S-Parameters to measure. SyntaxRFMXVNA_ATTR_SPARAMS_NUMBER_OF_SPARAMETERSNumeric ValueData TypeAccessApplies To13635586int32Read/WriteN/ARemarksNote1: S-Parameters of a N-port DUT can be represented by N^2 canonical S-Parameters viz. S11, S12,...,S1N, S21, S22,...,S2N, SN1, S

### RFMXVNA_ATTR_SPARAMS_NUMBER_OF_SPARAMETERS

Specifies the number of S-Parameters to measure.

#### Syntax

RFMXVNA_ATTR_SPARAMS_NUMBER_OF_SPARAMETERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13635586 | int32 | Read/Write | N/A |

#### Remarks

**Note1**: S-Parameters of a N-port DUT can be represented by N^2 canonical S-Parameters viz. S11, S12,...,S1N, S21, S22,...,S2N, SN1, SN2,...,SNN such that **B = S A** where **S** denotes the S-Parameter matrix with Sij being the element in the i<sup>th</sup> row and j<sup>th</sup> column. Similarly **A** denotes the matrix composed of the incident waves. Element Aij denotes the wave parameter a<sub>ij</sub> i.e., wave measured at the reference reciever on port *with port <j> as the source. Similarly **B** denotes the matrix composed of the scatterred waves. Element Bij denotes the wave parameter b<sub>ij</sub> i.e., wave measured at the test reciever on port *with port <j> as the source.**

**You can configure each measured S-Parameter in RFmxVNA SParams measurement to be returned in one of several supported formats using [RFMXVNA_ATTR_SPARAMS_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html) attribute. Example1: If you want to fetch magnitude and phase information of S11, then set Number of S-Parameters attribute to 2, then for both SParam indices 0 and 1, set Parameter attribute to "S11". Then set [RFMXVNA_ATTR_SPARAMS_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html) attribute to Magnitude for Sparam index 0 and to Phase for SParam index 1.**

****Note2**: You can set many SParam indices to share the same Parameter and Format attribute values making them duplicates of each other.**

**If you increase this attribute value from N to N+K, then existing N SParams are not affected but K new SParams are added. If you reduce number of SParams from N to N-K, then last K SParams are deleted without affecting the remaining N-K SParams.**

**You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.**

**The default value is 1.**

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams_1ga8414da40fec144bc721391c171848012.html language=enus -->
## TOPIC 00007: RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams_1ga8414da40fec144bc721391c171848012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams_1ga8414da40fec144bc721391c171848012.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the magnitude units for all S-Parameters for which you set RFMXVNA_ATTR_SPARAMS_FORMAT attribute to Magnitude. SyntaxRFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITSNumeric ValueData TypeAccessApplies To13635590int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read thi

### RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS

Specifies the magnitude units for all S-Parameters for which you set [RFMXVNA_ATTR_SPARAMS_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html) attribute to **Magnitude**.

#### Syntax

RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13635590 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_DB | 0 (0x0) | Sets S-Parameter magnitude units to dB. |
| RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_LINEAR | 1 (0x1) | Sets S-Parameter magnitude units to linear such that S-Parameters are reported in linear scale (V/V). |

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams_1gaa63ec80be552f6e7250def17f934955a.html language=enus -->
## TOPIC 00008: RFMXVNA_ATTR_SPARAMS_SOURCE_PORT

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams_1gaa63ec80be552f6e7250def17f934955a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams_1gaa63ec80be552f6e7250def17f934955a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_<<i>receiver port name</i>>_<<i>source port name</i>>". SyntaxRFMXVNA_ATTR_SPARAMS_SOURCE_PORTNumeric ValueData TypeAccessApplies To13635588char[]Read/WriteSparameterRemarks For example, to measure S21, set this attribut

### RFMXVNA_ATTR_SPARAMS_SOURCE_PORT

Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_<<i>receiver port name</i>>_<<i>source port name</i>>".

#### Syntax

RFMXVNA_ATTR_SPARAMS_SOURCE_PORT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13635588 | char[] | Read/Write | Sparameter |

#### Remarks

For example, to measure S21, set this attribute to "port1".

Use "sparam<n>" as the selector string to configure or read this attribute.

The default value is "port1".

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html language=enus -->
## TOPIC 00009: RFMXVNA_ATTR_SPARAMS_FORMAT

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the format of S-Parameter measurement. SyntaxRFMXVNA_ATTR_SPARAMS_FORMATNumeric ValueData TypeAccessApplies To13635589int32Read/WriteSparameterRemarks Use "sparam<n>" as the selector string to configure or read this attribute.The default value is Magnitude.NameValueDescriptionRFMXVNA_VAL_S

### RFMXVNA_ATTR_SPARAMS_FORMAT

Specifies the format of S-Parameter measurement.

#### Syntax

RFMXVNA_ATTR_SPARAMS_FORMAT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13635589 | int32 | Read/Write | Sparameter |

#### Remarks

Use "sparam<n>" as the selector string to configure or read this attribute.

The default value is **Magnitude**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_SPARAMS_FORMAT_MAGNITUDE | 0 (0x0) | Sets the format of the selected S-Parameter to Magnitude. You can specify RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS. |
| RFMXVNA_VAL_SPARAMS_FORMAT_PHASE | 1 (0x1) | Sets the format of the selected S-Parameter to Phase. Phase values are expressed in degrees. Phase can be represented in various, mathematically equivalent ways such as phase wrapped between the range [-180, 180) degrees, or phase can be represented in an unwrapped manner. You can specify the phase representation by configuring RFMXVNA_ATTR_SPARAMS_PHASE_TRACE_TYPE. |
| RFMXVNA_VAL_SPARAMS_FORMAT_COMPLEX | 2 (0x2) | Sets the format of the selected S-Parameter as complex numbers in cartesian co-ordinates. |
| RFMXVNA_VAL_SPARAMS_FORMAT_SWR | 3 (0x3) | Sets the format of the selected S-Parameter to Standing Wave Ratio (SWR). SWR is a unitless quantity. |
| RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_IMPEDANCE | 4 (0x4) | Sets the format of the selected S-Parameter to Smith Impedance. S-Parameter values are transformed into impedence values. Impedence values are expressed in ohms. You can use these values to plot on a Smith Chart. |
| RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_ADMITTANCE | 5 (0x5) | Sets the format of the selected S-Parameter to Smith Admittance. S-Parameter values are transformed into admittance values. Admittance values are expressed in siemens. You can use these values to plot on an Inverted Smith Chart. |
| RFMXVNA_VAL_SPARAMS_FORMAT_POLAR | 6 (0x6) | Sets the format of the selected S-Parameter as complex numbers in polar co-ordinates, where the radial axis (i.e., magnitude of the complex numbers) is always in linear scale and angular axis (phase) is represented in degrees and always wrapped between ±180 deg. |
| RFMXVNA_VAL_SPARAMS_FORMAT_GROUP_DELAY | 7 (0x7) | Sets the format of the selected S-Parameter to Group Delay. Group delay represents the time it takes for the signal to pass through a device under test. The delay is expressed in seconds. Group delay vs. frequency is derived from phase vs. frequency response. At a given frequency point, group delay is computed by selecting two nearby frequency points and taking the ratio of the phase difference to the frequency separation between them. The frequency separation between the two selected points is called the group delay aperture. You can control the aperture by first configuring RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE and once the mode is selected, you can set the aperture by configuring RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_POINTS, RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_PERCENTAGE or RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_FREQUENCY_SPAN. For example, if the number of aperture points is equal to 3, then group delay at a nth frequency point is computed by selecting the (n-1)th frequency point and (n+1)th frequency point. |

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams_1gac86f73dbef7669ef1361551f72eeb95a.html language=enus -->
## TOPIC 00010: RFMXVNA_ATTR_SPARAMS_MEASUREMENT_ENABLED

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams_1gac86f73dbef7669ef1361551f72eeb95a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams_1gac86f73dbef7669ef1361551f72eeb95a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Sparams measurement. SyntaxRFMXVNA_ATTR_SPARAMS_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To13635584int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXVNA_ATTR_SPARAMS_MEASUREMENT_ENABLED

Specifies whether to enable the Sparams measurement.

#### Syntax

RFMXVNA_ATTR_SPARAMS_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13635584 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture.html language=enus -->
## TOPIC 00011: Group Delay Aperture

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_FREQUENCY_SPANSpecifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attri

### Group Delay Aperture

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_FREQUENCY_SPAN | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attribute is set to Group Delay and RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE attribute is set to Frequency Span. |
| RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE | Specifies the aperture mode to be used for the computation of group delay for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attribute is set to Group Delay. |
| RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_PERCENTAGE | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attribute is set to Group Delay and RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE attribute is set to Percentage. |
| RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_POINTS | Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attribute is set to Group Delay and RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE attribute is set to Points. You must set the value of this attribute between 2 and the total number of frequency points in the measurement frequency range. |

#### Attachments

None

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga1f5eeeef8d9d729b7fea88f90dce665a.html language=enus -->
## TOPIC 00012: RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_POINTS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga1f5eeeef8d9d729b7fea88f90dce665a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga1f5eeeef8d9d729b7fea88f90dce665a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attribute is set to Group Delay and RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE attribute is set to Points. You must set

### RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_POINTS

Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which [RFMXVNA_ATTR_SPARAMS_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html) attribute is set to **Group Delay** and [RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE](group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga26a1918a7a1b712db89fedcb09ed25a0.html) attribute is set to **Points**. You must set the value of this attribute between 2 and the total number of frequency points in the measurement frequency range.

#### Syntax

RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_POINTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13635613 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 11.

Parent topic:

Group Delay Aperture

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga729bfe857299d272d86d8be27b8cfd37.html language=enus -->
## TOPIC 00013: RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_PERCENTAGE

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga729bfe857299d272d86d8be27b8cfd37.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga729bfe857299d272d86d8be27b8cfd37.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which RFMXVNA_ATTR_SPARAMS_FORMAT attribute i

### RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_PERCENTAGE

Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which [RFMXVNA_ATTR_SPARAMS_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html) attribute is set to **Group Delay** and [RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE](group____root__ni_r_fmx_v_n_a__attributes__sparams__group__delay__aperture_1ga26a1918a7a1b712db89fedcb09ed25a0.html) attribute is set to **Percentage**.

#### Syntax

RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_PERCENTAGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13635614 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 5 %.

Parent topic:

Group Delay Aperture

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sparams__math.html language=enus -->
## TOPIC 00014: Math

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sparams__math.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sparams__math.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXVNA_ATTR_SPARAMS_MATH_ACTIVE_MEASUREMENT_MEMORYSpecifies the active measurement memory for performing mathematical operations when several measurement memories are associated with the configured S-Parameter. If only one measurement memory is associated with

### Math

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXVNA_ATTR_SPARAMS_MATH_ACTIVE_MEASUREMENT_MEMORY | Specifies the active measurement memory for performing mathematical operations when several measurement memories are associated with the configured S-Parameter. If only one measurement memory is associated with the configured S-Parameter, that measurement memory will be used for mathematical operations. |
| RFMXVNA_ATTR_SPARAMS_MATH_FUNCTION | Specifies the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. |

#### Attachments

None

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga6b5613751d6c6e2b408f2782e977790f.html language=enus -->
## TOPIC 00015: RFMXVNA_ATTR_POWER_LEVEL

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga6b5613751d6c6e2b408f2782e977790f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga6b5613751d6c6e2b408f2782e977790f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level for the VNA source port. This value is expressed in dBm. SyntaxRFMXVNA_ATTR_POWER_LEVELNumeric ValueData TypeAccessApplies To13631491float64Read/WritePortRemarks Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port

### RFMXVNA_ATTR_POWER_LEVEL

Specifies the power level for the VNA source port. This value is expressed in dBm.

#### Syntax

RFMXVNA_ATTR_POWER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631491 | float64 | Read/Write | Port |

#### Remarks

Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port. Use "port::all" to configure same power level for all VNA ports.

The default value is -10 dBm.

Parent topic:

Sweep

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga7d4387923c9577aab1b3a42bbf59e924.html language=enus -->
## TOPIC 00016: RFMXVNA_ATTR_NUMBER_OF_POINTS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga7d4387923c9577aab1b3a42bbf59e924.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga7d4387923c9577aab1b3a42bbf59e924.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of points at which measurements are performed. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to Linear or CW Time. SyntaxRFMXVNA_ATTR_NUMBER_OF_POINTSNumeric ValueData TypeAccessApplies To13631571int32Read/WriteN/ARemarks You do not need to use a

### RFMXVNA_ATTR_NUMBER_OF_POINTS

Specifies the number of points at which measurements are performed. This attribute is used only when you set the [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute to **Linear** or **CW Time**.

#### Syntax

RFMXVNA_ATTR_NUMBER_OF_POINTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631571 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 201.

Parent topic:

Sweep

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga8af1bcb4a6d735206fa688304a1558ca.html language=enus -->
## TOPIC 00017: RFMXVNA_ATTR_TEST_RECEIVER_ATTENUATION

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga8af1bcb4a6d735206fa688304a1558ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep_1ga8af1bcb4a6d735206fa688304a1558ca.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. The receiver that measures the scattered waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This

### RFMXVNA_ATTR_TEST_RECEIVER_ATTENUATION

Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. The receiver that measures the scattered waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB.

#### Syntax

RFMXVNA_ATTR_TEST_RECEIVER_ATTENUATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631498 | float64 | Read/Write | Port |

#### Remarks

Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port. Use "port::all" to configure same test receiver attenuation for all VNA ports.

The default value is 0 dB.

Parent topic:

Sweep

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep_1gad4c7876b28902a0267d103924b89818b.html language=enus -->
## TOPIC 00018: RFMXVNA_ATTR_X_AXIS_VALUES

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep_1gad4c7876b28902a0267d103924b89818b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep_1gad4c7876b28902a0267d103924b89818b.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of frequency values when you perform measurements with RFMXVNA_ATTR_SWEEP_TYPE attribute set to List or Linear or Segment or an array of time values when you perform measurements with RFMXVNA_ATTR_SWEEP_TYPE attribute set to CW Time. SyntaxRFMXVNA_ATTR_X_AXIS_VALUESNumeric ValueData

### RFMXVNA_ATTR_X_AXIS_VALUES

Returns an array of frequency values when you perform measurements with [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute set to **List** or **Linear** or **Segment** or an array of time values when you perform measurements with [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute set to **CW Time**.

#### Syntax

RFMXVNA_ATTR_X_AXIS_VALUES

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631575 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Sweep

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep_1gae4b05b9ca00eb9e6cd92a9faf46182b6.html language=enus -->
## TOPIC 00019: RFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLED

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep_1gae4b05b9ca00eb9e6cd92a9faf46182b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep_1gae4b05b9ca00eb9e6cd92a9faf46182b6.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether IF Bandwidth is automatically scaled down to account for the increased VNA receiver noise at low frequencies. This attribute will automatically set to False when RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute is set to True. SyntaxRFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLEDNumeric Va

### RFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLED

Specifies whether IF Bandwidth is automatically scaled down to account for the increased VNA receiver noise at low frequencies. This attribute will automatically set to **False** when [RFMXVNA_ATTR_PULSE_MODE_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse_1gaefe3f9f4370a981f6cfd6838835142bc.html) attribute is set to **True**.

#### Syntax

RFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631558 | int32 | Read/Write | N/A |

#### Remarks

Consider disabling automatic IF Bandwidth scaling by setting this attribute to False if you want faster measurement speed but with higher measurment noise at low frequencies.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_FALSE | 0 (0x0) | Disables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. |
| RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_TRUE | 1 (0x1) | Enables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. |

Parent topic:

Sweep

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse.html language=enus -->
## TOPIC 00020: Pulse

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAcquisitionGeneratorModulatorTriggerGroup membersNameDescriptionRFMXVNA_ATTR_PULSE_MODE_ENABLEDSpecifies whether to use pulsed RF signal as stimulus and/or export pulse generator digital signals. RFMXVNA_ATTR_PULSE_PERIODSpecifies the time interval after which the pulse repeats. This attribute

### Pulse

#### Groups

- Acquisition
- Generator
- Modulator
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFMXVNA_ATTR_PULSE_MODE_ENABLED | Specifies whether to use pulsed RF signal as stimulus and/or export pulse generator digital signals. |
| RFMXVNA_ATTR_PULSE_PERIOD | Specifies the time interval after which the pulse repeats. This attribute is used only when you set the RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute to True. If you set RFMXVNA_ATTR_PULSE_TRIGGER_TYPE attribute to Digital Edge, pulses are generated only when an external pulse digital edge trigger is received by the VNA. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

Sweep

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse_1ga6ece46238dab9f244e23c902cf8baab5.html language=enus -->
## TOPIC 00021: RFMXVNA_ATTR_PULSE_PERIOD

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse_1ga6ece46238dab9f244e23c902cf8baab5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse_1ga6ece46238dab9f244e23c902cf8baab5.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time interval after which the pulse repeats. This attribute is used only when you set the RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute to True. If you set RFMXVNA_ATTR_PULSE_TRIGGER_TYPE attribute to Digital Edge, pulses are generated only when an external pulse digital edge trigger is re

### RFMXVNA_ATTR_PULSE_PERIOD

Specifies the time interval after which the pulse repeats. This attribute is used only when you set the [RFMXVNA_ATTR_PULSE_MODE_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse_1gaefe3f9f4370a981f6cfd6838835142bc.html) attribute to **True**. If you set [RFMXVNA_ATTR_PULSE_TRIGGER_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse__trigger_1ga3015614a01439f17179530a7d081341b.html) attribute to **Digital Edge**, pulses are generated only when an external pulse digital edge trigger is received by the VNA. This value is expressed in seconds.

#### Syntax

RFMXVNA_ATTR_PULSE_PERIOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631541 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 ms.

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse__generator_1ga6abe159f61027156f0664717ec6f42b8.html language=enus -->
## TOPIC 00022: RFMXVNA_ATTR_PULSE_GENERATOR_EXPORT_OUTPUT_TERMINAL

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse__generator_1ga6abe159f61027156f0664717ec6f42b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse__generator_1ga6abe159f61027156f0664717ec6f42b8.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for an exported Pulse Generator. This attribute is used only when you set RFMXVNA_ATTR_PULSE_MODE_ENABLED attribute to True and RFMXVNA_ATTR_PULSE_GENERATOR_ENABLED attribute to True. SyntaxRFMXVNA_ATTR_PULSE_GENERATOR_EXPORT_OUTPUT_TERMINALNumeric ValueData TypeAc

### RFMXVNA_ATTR_PULSE_GENERATOR_EXPORT_OUTPUT_TERMINAL

Specifies the destination terminal for an exported Pulse Generator. This attribute is used only when you set [RFMXVNA_ATTR_PULSE_MODE_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse_1gaefe3f9f4370a981f6cfd6838835142bc.html) attribute to **True** and [RFMXVNA_ATTR_PULSE_GENERATOR_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__sweep__pulse__generator_1ga054eb77d5d8b69027503c14e033a2136.html) attribute to **True**.

#### Syntax

RFMXVNA_ATTR_PULSE_GENERATOR_EXPORT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631551 | char[] | Read/Write | Pulsegenerator |

#### Remarks

Use "pulsegen<n>" as the selector string to configure or read this attribute.

The default value is **Do not export signal**.

Parent topic:

Generator

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1ga0883ffd6b33e5b66cefe0adcf75346e3.html language=enus -->
## TOPIC 00023: RFMXVNA_ATTR_SEGMENT_POWER_LEVEL

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1ga0883ffd6b33e5b66cefe0adcf75346e3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1ga0883ffd6b33e5b66cefe0adcf75346e3.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source power level for the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to Segment and RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED attribute to True. This value is expressed in dBm. SyntaxRFMXVNA_ATTR_SEGMENT_POWER_LEVELNumeric ValueData

### RFMXVNA_ATTR_SEGMENT_POWER_LEVEL

Specifies the source power level for the selected segment. This attribute is used only when you set the [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute to **Segment** and [RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gab62410564a92bb3e83e9bfea690054ca.html) attribute to **True**. This value is expressed in dBm.

#### Syntax

RFMXVNA_ATTR_SEGMENT_POWER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631561 | float64 | Read/Write | Port |

#### Remarks

Use "port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific VNA port for segment0. Use "port::<i>all</i>" to configure this attribute for all VNA ports for segment0. Use "segment::<<i>segmentnumber</i>>/port::<<i>portname</i>>" as the selector string to configure or read this attribute for a specific segment and for a specific VNA port. Use "segment::<i>all</i>/port::<i>all</i>" as the selector string to configure this attribute for all segments and for all VNA ports.

The default value is -10 dBm.

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gab62410564a92bb3e83e9bfea690054ca.html language=enus -->
## TOPIC 00024: RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gab62410564a92bb3e83e9bfea690054ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gab62410564a92bb3e83e9bfea690054ca.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether VNA performs measurements using the same source power level for all segments or uses different source power level for each segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to Segment. SyntaxRFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLEDNumeric Value

### RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED

Specifies whether VNA performs measurements using the same source power level for all segments or uses different source power level for each segment. This attribute is used only when you set the [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute to **Segment**.

#### Syntax

RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631560 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_FALSE | 0 (0x0) | All segments are measured with the source power level that you specify using RFMXVNA_ATTR_POWER_LEVEL attribute. |
| RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_TRUE | 1 (0x1) | The selected segment is measured with the source power level that you specify using RFMXVNA_ATTR_SEGMENT_POWER_LEVEL attribute. |

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gae0b3f4e989d0728c7641f99f6c0c5f9f.html language=enus -->
## TOPIC 00025: RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gae0b3f4e989d0728c7641f99f6c0c5f9f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gae0b3f4e989d0728c7641f99f6c0c5f9f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether VNA performs measurements using the same dwell time value for all segments or uses different dwell time for each segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to Segment. SyntaxRFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLEDNumeric ValueData TypeAc

### RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED

Specifies whether VNA performs measurements using the same dwell time value for all segments or uses different dwell time for each segment. This attribute is used only when you set the [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute to **Segment**.

#### Syntax

RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631566 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_FALSE | 0 (0x0) | All segments are measured with the dwell time that you specify using RFMXVNA_ATTR_DWELL_TIME attribute. |
| RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_TRUE | 1 (0x1) | The selected segment is measured with the dwell time that you specify using RFMXVNA_ATTR_SEGMENT_DWELL_TIME attribute. |

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gaf562e691f5e47986fcdecbd7cd095509.html language=enus -->
## TOPIC 00026: RFMXVNA_ATTR_SEGMENT_DWELL_TIME

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gaf562e691f5e47986fcdecbd7cd095509.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gaf562e691f5e47986fcdecbd7cd095509.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the dwell time for the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to Segment and RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED attribute to True. This value is expressed in seconds. SyntaxRFMXVNA_ATTR_SEGMENT_DWELL_TIMENumeric ValueData TypeA

### RFMXVNA_ATTR_SEGMENT_DWELL_TIME

Specifies the dwell time for the selected segment. This attribute is used only when you set the [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute to **Segment** and [RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED](group____root__ni_r_fmx_v_n_a__attributes__sweep__segment_1gae0b3f4e989d0728c7641f99f6c0c5f9f.html) attribute to **True**. This value is expressed in seconds.

#### Syntax

RFMXVNA_ATTR_SEGMENT_DWELL_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631567 | float64 | Read/Write | Segment |

#### Remarks

Dwell Time specifies the time for which the analyzer waits before acquiring the signal for each measured frequency point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer.

Use "segment::<<i>segmentnumber</i>>" as the selector string to configure or read this attribute for a specific segment. Use "segment::<i>all</i>" as the selector string to configure this attribute for all segments.

The default value is 0 s.

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__segment__frequency_1ga4d294260fd6dceb85d0a412459c94291.html language=enus -->
## TOPIC 00027: RFMXVNA_ATTR_SEGMENT_NUMBER_OF_FREQUENCY_POINTS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__segment__frequency_1ga4d294260fd6dceb85d0a412459c94291.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__segment__frequency_1ga4d294260fd6dceb85d0a412459c94291.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of frequency points measured in the selected segment. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to Segment. SyntaxRFMXVNA_ATTR_SEGMENT_NUMBER_OF_FREQUENCY_POINTSNumeric ValueData TypeAccessApplies To13631574int32Read/WriteSegmentRemarks Use "

### RFMXVNA_ATTR_SEGMENT_NUMBER_OF_FREQUENCY_POINTS

Specifies the number of frequency points measured in the selected segment. This attribute is used only when you set the [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute to **Segment**.

#### Syntax

RFMXVNA_ATTR_SEGMENT_NUMBER_OF_FREQUENCY_POINTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631574 | int32 | Read/Write | Segment |

#### Remarks

Use "segment::<<i>segmentnumber</i>>" as the selector string to configure or read this attribute for a specific segment.

The default value is 21.

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__segment__frequency_1ga8bd0d012aba80556aed36d7e7ecdf503.html language=enus -->
## TOPIC 00028: RFMXVNA_ATTR_SEGMENT_STOP_FREQUENCY

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__segment__frequency_1ga8bd0d012aba80556aed36d7e7ecdf503.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__segment__frequency_1ga8bd0d012aba80556aed36d7e7ecdf503.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the highest frequency of the selected segment at which measurements are performed. This attribute is used only when you set the RFMXVNA_ATTR_SWEEP_TYPE attribute to Segment. This value is expressed in Hz. SyntaxRFMXVNA_ATTR_SEGMENT_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To136315

### RFMXVNA_ATTR_SEGMENT_STOP_FREQUENCY

Specifies the highest frequency of the selected segment at which measurements are performed. This attribute is used only when you set the [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute to **Segment**. This value is expressed in Hz.

#### Syntax

RFMXVNA_ATTR_SEGMENT_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631573 | float64 | Read/Write | Segment |

#### Remarks

Use "segment::<<i>segmentnumber</i>>" as the selector string to configure or read this attribute for a specific segment.

The default value is 2 GHz.

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__timing.html language=enus -->
## TOPIC 00029: Timing

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__timing.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__timing.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXVNA_ATTR_DWELL_TIMESpecifies the time for which the analyzer waits before acquiring the signal for each measurement point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency chang

### Timing

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXVNA_ATTR_DWELL_TIME | Specifies the time for which the analyzer waits before acquiring the signal for each measurement point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |
| RFMXVNA_ATTR_SWEEP_DELAY | Specifies the time for which VNA waits before it starts acquiring data for each sweep. Total delay for acquiring the first point in each sweep is sum of this delay and RFMXVNA_ATTR_DWELL_TIME. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

Sweep

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__timing_1gaf3468a4b9844eec76b01ed95c2183b37.html language=enus -->
## TOPIC 00030: RFMXVNA_ATTR_SWEEP_DELAY

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__timing_1gaf3468a4b9844eec76b01ed95c2183b37.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__timing_1gaf3468a4b9844eec76b01ed95c2183b37.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time for which VNA waits before it starts acquiring data for each sweep. Total delay for acquiring the first point in each sweep is sum of this delay and RFMXVNA_ATTR_DWELL_TIME. This value is expressed in seconds. SyntaxRFMXVNA_ATTR_SWEEP_DELAYNumeric ValueData TypeAccessApplies To136

### RFMXVNA_ATTR_SWEEP_DELAY

Specifies the time for which VNA waits before it starts acquiring data for each sweep. Total delay for acquiring the first point in each sweep is sum of this delay and [RFMXVNA_ATTR_DWELL_TIME](group____root__ni_r_fmx_v_n_a__attributes__sweep__timing_1gafd55bc7e61ce4d6aae901c314c8ff76f.html). This value is expressed in seconds.

#### Syntax

RFMXVNA_ATTR_SWEEP_DELAY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631493 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0 s.

Parent topic:

Timing

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__sweep__timing_1gafd55bc7e61ce4d6aae901c314c8ff76f.html language=enus -->
## TOPIC 00031: RFMXVNA_ATTR_DWELL_TIME

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__sweep__timing_1gafd55bc7e61ce4d6aae901c314c8ff76f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__sweep__timing_1gafd55bc7e61ce4d6aae901c314c8ff76f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time for which the analyzer waits before acquiring the signal for each measurement point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. Th

### RFMXVNA_ATTR_DWELL_TIME

Specifies the time for which the analyzer waits before acquiring the signal for each measurement point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.

#### Syntax

RFMXVNA_ATTR_DWELL_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631494 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0 s.

Parent topic:

Timing

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge.html language=enus -->
## TOPIC 00032: Digital Edge

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGESpecifies the edge of the digital-signal used to assert a digital edge trigger. This attribute is used only when you set the RFMXVNA_ATTR_TRIGGER_TYPE attribute to Digital Edge. RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCESpecif

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE | Specifies the edge of the digital-signal used to assert a digital edge trigger. This attribute is used only when you set the RFMXVNA_ATTR_TRIGGER_TYPE attribute to Digital Edge. |
| RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE | Specifies the terminal name used as the source for asserting a digital edge trigger. This attribute is used only when you set the RFMXVNA_ATTR_TRIGGER_TYPE attribute to Digital Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge_1ga8c2c9b0c0220a8ee9746a9049f0128fe.html language=enus -->
## TOPIC 00033: RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge_1ga8c2c9b0c0220a8ee9746a9049f0128fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge_1ga8c2c9b0c0220a8ee9746a9049f0128fe.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge of the digital-signal used to assert a digital edge trigger. This attribute is used only when you set the RFMXVNA_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGENumeric ValueData TypeAccessApplies To13631556int32Read/WriteN/ARemarks You do

### RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

Specifies the edge of the digital-signal used to assert a digital edge trigger. This attribute is used only when you set the [RFMXVNA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_v_n_a__attributes__trigger_1gab93668ad4178dd8ec3d9f303cb28ed44.html) attribute to **Digital Edge**.

#### Syntax

RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631556 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the digital-signal. |
| RFMXVNA_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the digital-signal. |

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge_1gae3ebfb9fb7e21adfdae142d2c92f7f9b.html language=enus -->
## TOPIC 00034: RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge_1gae3ebfb9fb7e21adfdae142d2c92f7f9b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__trigger__digital__edge_1gae3ebfb9fb7e21adfdae142d2c92f7f9b.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name used as the source for asserting a digital edge trigger. This attribute is used only when you set the RFMXVNA_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To13631555char[]Read/WriteN/ARemark

### RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

Specifies the terminal name used as the source for asserting a digital edge trigger. This attribute is used only when you set the [RFMXVNA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_v_n_a__attributes__trigger_1gab93668ad4178dd8ec3d9f303cb28ed44.html) attribute to **Digital Edge**.

#### Syntax

RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13631555 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is "" (empty string).

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__waves_1ga96aae2b45eec1c4e5533d1fec2b7866a.html language=enus -->
## TOPIC 00035: RFMXVNA_ATTR_WAVES_MAGNITUDE_UNITS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__waves_1ga96aae2b45eec1c4e5533d1fec2b7866a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__waves_1ga96aae2b45eec1c4e5533d1fec2b7866a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the magnitude units for all waves for which RFMXVNA_ATTR_WAVES_FORMAT attribute is set to Magnitude. SyntaxRFMXVNA_ATTR_WAVES_MAGNITUDE_UNITSNumeric ValueData TypeAccessApplies To13639687int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute

### RFMXVNA_ATTR_WAVES_MAGNITUDE_UNITS

Specifies the magnitude units for all waves for which [RFMXVNA_ATTR_WAVES_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__waves_1ga2c742a51f4c46df8b38f675de78a703e.html) attribute is set to **Magnitude**.

#### Syntax

RFMXVNA_ATTR_WAVES_MAGNITUDE_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13639687 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dBm**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBM | 0 (0x0) | Sets wave magnitude units to dBm. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMV | 1 (0x1) | Sets wave magnitude units to dBmV. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBUV | 2 (0x2) | Sets wave magnitude units to dBuV. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMA | 3 (0x3) | Sets wave magnitude units to dBmA. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_W | 4 (0x4) | Sets wave magnitude units to watts. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_V | 5 (0x5) | Sets wave magnitude units to volts. |
| RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_A | 6 (0x6) | Sets wave magnitude units to ampere. |

Parent topic:

Waves

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__waves_1gaf57f38f377f9bd809673bc0b74709032.html language=enus -->
## TOPIC 00036: RFMXVNA_ATTR_WAVES_PHASE_TRACE_TYPE

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__waves_1gaf57f38f377f9bd809673bc0b74709032.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__waves_1gaf57f38f377f9bd809673bc0b74709032.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase type for all waves for which RFMXVNA_ATTR_WAVES_FORMAT attribute is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. SyntaxRFMXVNA_ATTR_WAVES

### RFMXVNA_ATTR_WAVES_PHASE_TRACE_TYPE

Specifies the phase type for all waves for which [RFMXVNA_ATTR_WAVES_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__waves_1ga2c742a51f4c46df8b38f675de78a703e.html) attribute is set to **Phase**. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.

#### Syntax

RFMXVNA_ATTR_WAVES_PHASE_TRACE_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13639688 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Wrapped**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_WRAPPED | 0 (0x0) | The reported wave phase is wrapped between -180 degress to +180 degrees. |
| RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_UNWRAPPED | 1 (0x1) | The reported wave phase is unwrapped. |

Parent topic:

Waves

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga92a7a1198345082ffe94bb2d7c0a74ef.html language=enus -->
## TOPIC 00037: RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_POINTS

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga92a7a1198345082ffe94bb2d7c0a74ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga92a7a1198345082ffe94bb2d7c0a74ef.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which RFMXVNA_ATTR_WAVES_FORMAT attribute is set to Group Delay and RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE attribute is set to Points. You must set the value

### RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_POINTS

Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which [RFMXVNA_ATTR_WAVES_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__waves_1ga2c742a51f4c46df8b38f675de78a703e.html) attribute is set to **Group Delay** and [RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE](group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga9a50da0bee2aa4d1961aa379cb0569cb.html) attribute is set to **Points**. You must set the value of this attribute between 2 and the total number of frequency points in the measurement frequency range.

#### Syntax

RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_POINTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13639702 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 11.

Parent topic:

Group Delay Aperture

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga9a50da0bee2aa4d1961aa379cb0569cb.html language=enus -->
## TOPIC 00038: RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga9a50da0bee2aa4d1961aa379cb0569cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga9a50da0bee2aa4d1961aa379cb0569cb.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the aperture mode to be used for the computation of group delay for all waves for which RFMXVNA_ATTR_WAVES_FORMAT attribute is set to Group Delay. SyntaxRFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODENumeric ValueData TypeAccessApplies To13639701int32Read/WriteN/ARemarks You do not need to us

### RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE

Specifies the aperture mode to be used for the computation of group delay for all waves for which [RFMXVNA_ATTR_WAVES_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__waves_1ga2c742a51f4c46df8b38f675de78a703e.html) attribute is set to **Group Delay**.

#### Syntax

RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13639701 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Points**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXVNA_VAL_WAVES_GROUP_DELAY_APERTURE_MODE_POINTS | 0 (0x0) | Sets group delay aperture mode to Points. You can specify the aperture in terms of the number of frequency points by configuring RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_POINTS. |
| RFMXVNA_VAL_WAVES_GROUP_DELAY_APERTURE_MODE_PERCENTAGE | 1 (0x1) | Sets group delay aperture mode to Percentage. You can specify the aperture in terms of the frequency separation expressed in percentage by configuring RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_PERCENTAGE. |
| RFMXVNA_VAL_WAVES_GROUP_DELAY_APERTURE_MODE_FREQUENCY_SPAN | 2 (0x2) | Sets group delay aperture to Frequency Span. You can specify the aperture in terms of the frequency separation by configuring RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_FREQUENCY_SPAN. |

Parent topic:

Group Delay Aperture

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1gaeb100a5cfb9c8904c7f3de3f49203645.html language=enus -->
## TOPIC 00039: RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_FREQUENCY_SPAN

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1gaeb100a5cfb9c8904c7f3de3f49203645.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1gaeb100a5cfb9c8904c7f3de3f49203645.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which RFMXVNA_ATTR_WAVES_FORMAT attribute is set to Group Delay and RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE attribute is set to Frequen

### RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_FREQUENCY_SPAN

Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which [RFMXVNA_ATTR_WAVES_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__waves_1ga2c742a51f4c46df8b38f675de78a703e.html) attribute is set to **Group Delay** and [RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE](group____root__ni_r_fmx_v_n_a__attributes__waves__group__delay__aperture_1ga9a50da0bee2aa4d1961aa379cb0569cb.html) attribute is set to **Frequency Span**.

#### Syntax

RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_FREQUENCY_SPAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13639704 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 50 MHz.

Parent topic:

Group Delay Aperture

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions_1gab761c5becfda71ee0f7acc35f530fd27.html language=enus -->
## TOPIC 00040: RFmxVNA_Initialize

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions_1gab761c5becfda71ee0f7acc35f530fd27.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions_1gab761c5becfda71ee0f7acc35f530fd27.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxVNA_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSes

### RFmxVNA_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxVNA_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Initialize](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize) function.

Note

Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| resourceName | [in] | char[] | Specifies the resource name of the device to initialize.The following table shows examples of how to specify the resource name.Example #Device TypeSyntax1myRFmxDeviceRFmx device, device name is "myRFmxDevice"2myLogicalNameIVI logical name or virtual instrument, name is "myLogicalName"For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |
| Example # | Device Type | Syntax |  |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |  |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |  |
| optionString | [in] | char[] | Sets the initial value of certain attributes for the session.The following attributes are used in this parameter:RFmxSetupSimulateAnalysisOnlyFor more information about attributes used in this parameter, refer to the NI RF Vector Signal Analyzers Help.The format of this string is "AttributeName=Value", where AttributeName is the name of the attribute and Value is the value to which the attribute is set. For example, you can simulate an PXIe-5663E using either of the following strings:"Simulate=1, RFmxSetup=Model:5663E""Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe"To set multiple attributes, separate their assignments with a comma.To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx uses yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session.To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". In this mode, user is responsible for waveform acquisition and RFmx driver will perform analysis on user specified IQ waveform or Spectrum. Use personality specific Analyze functions to perform measurements.Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665.To use external NI Source Measure Units (SMU) as the noise source power supply for the noise figure (NF) measurement, use the "NoiseSourcePowerSupply" specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx.Note RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs. |
| handleOut | [out] | niRFmxInstrHandle * | Identifies your instrument session. |
| isNewSession | [out] | int32 * | Returns RFMXVNA_VAL_TRUE if the function created a new session, or RFMXVNA_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions_1gac1e6596625d8e74ba3fcb1ce2772f30f.html language=enus -->
## TOPIC 00041: RFmxVNA_IQFetchData

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions_1gac1e6596625d8e74ba3fcb1ce2772f30f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions_1gac1e6596625d8e74ba3fcb1ce2772f30f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __stdcall RFmxVNA_IQFetchData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle data[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleselectorString[in

### RFmxVNA_IQFetchData

#### Syntax

int32 __stdcall RFmxVNA_IQFetchData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle data[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle |  |
| selectorString | [in] | char[] |  |
| timeout | [in] | float64 |  |
| x0 | [out] | float64 * |  |
| dx | [out] | float64 * |  |
| data | [out] | NIComplexSingle[] |  |
| arraySize | [in] | int32 |  |
| actualArraySize | [out] | int32 * |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html language=enus -->
## TOPIC 00042: RFmxVNA_GetError

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxVNA_GetError(niRFmxInstrHan

### RFmxVNA_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxVNA_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxVNA_GetErrorString](group____root__ni_r_fmx_v_n_a__functions_1ga64ae95b37cf623a78b3ee4ea0b4dbd7f.html) function if the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function does not return an error message.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Specifies the RFmx session. If a valid session handle is passed, the last error stored in that session is retrieved. You can pass NULL to retrieve the last error stored in the current execution thread. |
| errorCode | [out] | int32 * | Returns the error code for the session or execution thread. If you pass 0 for the errorDescriptionBufferSize parameter, you can pass NULL for the errorCode parameter. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescriptionIf the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the error description for the session or execution thread. If there is no description, this function returns an empty string.The buffer must contain at least as many elements as the value you specify with the errorDescriptionBufferSize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__advanced_1ga75c4c91e53748e164e00f58ea9d3d8da.html language=enus -->
## TOPIC 00043: RFmxVNA_ClearAllNamedResults

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__advanced_1ga75c4c91e53748e164e00f58ea9d3d8da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__advanced_1ga75c4c91e53748e164e00f58ea9d3d8da.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxVNA_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RF

### RFmxVNA_ClearAllNamedResults

Clears all results for the signal that you specify in the Selector String parameter.

#### Syntax

int32 __stdcall RFmxVNA_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__advanced_1ga7d5874a65b1d612a2695cd873227135e.html language=enus -->
## TOPIC 00044: RFmxVNA_CreateSignalConfiguration

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__advanced_1ga7d5874a65b1d612a2695cd873227135e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__advanced_1ga7d5874a65b1d612a2695cd873227135e.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. RFmxVNA Signal concept is same as Channel concept in third party software. Syntaxint32 __stdcall RFmxVNA_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxVNA_CreateSignalConfiguration

Creates a new instance of a signal. RFmxVNA Signal concept is same as Channel concept in third party software.

#### Syntax

int32 __stdcall RFmxVNA_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| signalName | [in] | char[] | This parameter specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Example:"""signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__advanced_1ga80967b0b9885229d19d643adb996b31c.html language=enus -->
## TOPIC 00045: RFmxVNA_AbortMeasurements

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__advanced_1ga80967b0b9885229d19d643adb996b31c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__advanced_1ga80967b0b9885229d19d643adb996b31c.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxVNA_Initiate or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete.

### RFmxVNA_AbortMeasurements

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxVNA_Initiate](group____root__ni_r_fmx_v_n_a__functions_1ga3e08aa7c74c3b6be242bbca971a23b4a.html) or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxVNA_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__advanced_1ga97d6a1b70dc4890cb3b1ccce5423f1c2.html language=enus -->
## TOPIC 00046: RFmxVNA_ClearNamedResult

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__advanced_1ga97d6a1b70dc4890cb3b1ccce5423f1c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__advanced_1ga97d6a1b70dc4890cb3b1ccce5423f1c2.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. Syntaxint32 __stdcall RFmxVNA_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFm

### RFmxVNA_ClearNamedResult

Clears a result instance specified by the result name in the Selector String parameter.

#### Syntax

int32 __stdcall RFmxVNA_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__build__string_1ga57b80469283bfa3151ae5113198fd76a.html language=enus -->
## TOPIC 00047: RFmxVNA_BuildSegmentString

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__build__string_1ga57b80469283bfa3151ae5113198fd76a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__build__string_1ga57b80469283bfa3151ae5113198fd76a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string specifying the segment number for use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxVNA_BuildSegmentString(char selectorString[], int32 segmentNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescri

### RFmxVNA_BuildSegmentString

Creates a selector string specifying the segment number for use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxVNA_BuildSegmentString(char selectorString[], int32 segmentNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| segmentNumber | [in] | int32 | This parameter specifies the segment for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__build__string_1ga5d096be7bba241fe752b2fb83959e92f.html language=enus -->
## TOPIC 00048: RFmxVNA_BuildSParameterString

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__build__string_1ga5d096be7bba241fe752b2fb83959e92f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__build__string_1ga5d096be7bba241fe752b2fb83959e92f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the selector string to use with S-Parameter configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxVNA_BuildSParameterString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 sParameterNumber)ParametersNameDirectionTypeDescriptionselect

### RFmxVNA_BuildSParameterString

Creates the selector string to use with S-Parameter configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxVNA_BuildSParameterString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 sParameterNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |
| sParameterNumber | [in] | int32 | This parameter specifies the s-parameter index for building the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__build__string_1ga9e958d9d344fb3d3215342ae8a390d4e.html language=enus -->
## TOPIC 00049: RFmxVNA_BuildSignalString

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__build__string_1ga9e958d9d344fb3d3215342ae8a390d4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__build__string_1ga9e958d9d344fb3d3215342ae8a390d4e.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxVNA_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])ParametersNameDirectionTypeDescriptionsignalName[in]char[]This parameter speci

### RFmxVNA_BuildSignalString

Creates selector string for use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxVNA_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Example:"""signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance.Example:"""result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Example:"""signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__build__string_1gaa9e44156129ff8526a3df75c7bb6f513.html language=enus -->
## TOPIC 00050: RFmxVNA_BuildCalibrationElementString

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__build__string_1gaa9e44156129ff8526a3df75c7bb6f513.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__build__string_1gaa9e44156129ff8526a3df75c7bb6f513.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string specifying the Calibration Element within the Calkit. Syntaxint32 __stdcall RFmxVNA_BuildCalibrationElementString(int32 selectorStringOutLength, char calkitSelectorString, char calibrationElementId, char calkitCalibrationElementSelectorStringOut)ParametersNameDirectionTypeD

### RFmxVNA_BuildCalibrationElementString

Creates a selector string specifying the Calibration Element within the Calkit.

#### Syntax

int32 __stdcall RFmxVNA_BuildCalibrationElementString(int32 selectorStringOutLength, char calkitSelectorString, char calibrationElementId, char calkitCalibrationElementSelectorStringOut)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| calkitSelectorString | [in] | char | This parameter specifies a selector string comprising of the Calkit ID.Example:"ckit::MyCkitID"You can use the RFmxVNA_BuildCalkitString function to build the selector string. |
| calibrationElementId | [in] | char | This parameter specifies the ID of the Calibration Element within the Calkit. |
| calkitCalibrationElementSelectorStringOut | [out] | char | This parameter returns the selector string created by this function. The selector string comprises of the Calkit ID and the Calibration Element ID.Example:"ckit::MyCkitID/calel::MyCalelID" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__build__string_1gac25f57d00fa193334f658d72061f29fe.html language=enus -->
## TOPIC 00051: RFmxVNA_BuildPortString

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__build__string_1gac25f57d00fa193334f658d72061f29fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__build__string_1gac25f57d00fa193334f658d72061f29fe.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string specifying the port(s) for use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxVNA_BuildPortString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], char portName)ParametersNameDirectionTypeDescriptionselectorStrin

### RFmxVNA_BuildPortString

Creates selector string specifying the port(s) for use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxVNA_BuildPortString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], char portName)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |
| portName | [in] | char | This parameter specifies the signal name for building the selector string. This input accepts the port name with or without the "port::" prefix. The default value is "" (empty string).Example:"""port::port1""port1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__build__string_1gac30b8d93ed9672fcf871a2b7d8bc9998.html language=enus -->
## TOPIC 00052: RFmxVNA_BuildPulseGeneratorString

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__build__string_1gac30b8d93ed9672fcf871a2b7d8bc9998.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__build__string_1gac30b8d93ed9672fcf871a2b7d8bc9998.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the selector string specifying the Pulse Generator for use with configuration or fetch attributes. Syntaxint32 __stdcall RFmxVNA_BuildPulseGeneratorString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 pulseGeneratorNumber)ParametersNameDirectionTypeDes

### RFmxVNA_BuildPulseGeneratorString

Creates the selector string specifying the Pulse Generator for use with configuration or fetch attributes.

#### Syntax

int32 __stdcall RFmxVNA_BuildPulseGeneratorString(char selectorString[], int32 selectorStringOutLength, char selectorStringOut[], int32 pulseGeneratorNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |
| pulseGeneratorNumber | [in] | int32 | This parameter specifies the pulse generator index for building the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration_1ga5749351a4c5225cee87591ac253c1c70.html language=enus -->
## TOPIC 00053: RFmxVNA_AutoDetectvCalOrientation

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration_1ga5749351a4c5225cee87591ac253c1c70.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration_1ga5749351a4c5225cee87591ac253c1c70.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically detects the vCal ports connected to the VNA ports and writes the RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_ORIENTATION attribute. Call this function before calling RFmxVNA_CalibrationInitiate. Syntaxint32 __stdcall RFmxVNA_AutoDetectvCalOrientation(niRFmxInstrHandle instrum

### RFmxVNA_AutoDetectvCalOrientation

Automatically detects the vCal ports connected to the VNA ports and writes the [RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_ORIENTATION](group____root__ni_r_fmx_v_n_a__attributes__correction__calibration__calkit__electronic_1gae297db86a748011bed45349283b70e57.html) attribute. Call this function before calling [RFmxVNA_CalibrationInitiate](group____root__ni_r_fmx_v_n_a__functions__calibration_1ga76b4a5e5a501fa02b7be5b6aa530ccc6.html).

#### Syntax

int32 __stdcall RFmxVNA_AutoDetectvCalOrientation(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Remarks

Auto detection of vCal orientation initially occurs at the midpoint of the frequency range specified for the calibration. If the connection is not detected, it retries at the lowest frequnecy in the configured range.

RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_ORIENTATION

Note

You must select SParams or Wave measurement before calling this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration_1ga76b4a5e5a501fa02b7be5b6aa530ccc6.html language=enus -->
## TOPIC 00054: RFmxVNA_CalibrationInitiate

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration_1ga76b4a5e5a501fa02b7be5b6aa530ccc6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration_1ga76b4a5e5a501fa02b7be5b6aa530ccc6.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the set of calibration standard measurements required for performing calibration with the sweep and calibration settings that you configure. Call this function after configuring all the appropriate sweep and calibration settings such as Frequency Settings, Power Level and Test Receiver at

### RFmxVNA_CalibrationInitiate

Determines the set of calibration standard measurements required for performing calibration with the sweep and calibration settings that you configure. Call this function after configuring all the appropriate sweep and calibration settings such as Frequency Settings, Power Level and Test Receiver attenuation settings, IF Bandwidth, Calkit and Cal Method related settings etc.

#### Syntax

int32 __stdcall RFmxVNA_CalibrationInitiate(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Remarks

After you call this function, you can query number of distinct physical connection steps using [RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_COUNT](group____root__ni_r_fmx_v_n_a__attributes__correction__calibration__step_1ga3b8d4e3d2a166a3fd43f13aee0825796.html). To understand the physical connection required in a given cal step, query [RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_DESCRIPTION](group____root__ni_r_fmx_v_n_a__attributes__correction__calibration__step_1gad88f4839e742c8d14d85039a930f3eaf.html) attribute. You can refer to following sequence of operations to better understand the usage of this function in a typical calibration routine.

RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_COUNT

RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_DESCRIPTION

m

RFmxVNA_CalibrationAcquire

m

RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_DESCRIPTION

RFmxVNA_CalibrationAcquire

RFmxVNA_CalibrationSave

RFmxVNA_CalsetSaveToFile

Note

- You must select SParams or Wave measurement before calling this function.
- After calling this function, if you change any sweep and calibration setting, you must call this function again to commit the change(s) to said sweep and calibration setting(s).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration_1gae63d156e0d6e312a96e8502e8c62ce07.html language=enus -->
## TOPIC 00055: RFmxVNA_CalibrationAbort

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration_1gae63d156e0d6e312a96e8502e8c62ce07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration_1gae63d156e0d6e312a96e8502e8c62ce07.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the calibration, which was previously initiated by RFmxVNA_CalibrationInitiate, for the signal instance that you specify in the Selector String parameter. Calling this function is optional, unless you want to stop a calibration before it is complete. This function executes even if there is an

### RFmxVNA_CalibrationAbort

Stops the calibration, which was previously initiated by [RFmxVNA_CalibrationInitiate](group____root__ni_r_fmx_v_n_a__functions__calibration_1ga76b4a5e5a501fa02b7be5b6aa530ccc6.html), for the signal instance that you specify in the **Selector String** parameter. Calling this function is optional, unless you want to stop a calibration before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxVNA_CalibrationAbort(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager.html language=enus -->
## TOPIC 00056: Calkitmanager

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCalkitGroup membersNameDescriptionRFmxVNA_CalkitManagerCreateCalkitCreates a new empty Calkit with the user defined Calkit ID in Calkit Manager. The user defined Calkit ID has to be unique among all Calkits in Calkit Manager. RFmxVNA_CalkitManagerExportCalkitExports a Calkit to file. RFmxVNA_C

### Calkitmanager

#### Groups

- Calkit

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_CalkitManagerCreateCalkit | Creates a new empty Calkit with the user defined Calkit ID in Calkit Manager. The user defined Calkit ID has to be unique among all Calkits in Calkit Manager. |
| RFmxVNA_CalkitManagerExportCalkit | Exports a Calkit to file. |
| RFmxVNA_CalkitManagerGetCalkitIDs | Returns a list of Calkit IDs for all Calkits currently loaded in Calkit Manager. |
| RFmxVNA_CalkitManagerImportCalkit | Imports a Calkit file into the Calkit Manager. |
| RFmxVNA_CalkitManagerRemoveCalkit | Removes a Calkit from Calkit Manager. |
| RFmxVNA_CalkitManagerValidateCalkit | Validates the consistency of a Calkit definition and returns the status of the validation. |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager_1ga110c99713b9eb988e8e7961bc49cbee7.html language=enus -->
## TOPIC 00057: RFmxVNA_CalkitManagerValidateCalkit

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager_1ga110c99713b9eb988e8e7961bc49cbee7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager_1ga110c99713b9eb988e8e7961bc49cbee7.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Validates the consistency of a Calkit definition and returns the status of the validation. Syntaxint32 __stdcall RFmxVNA_CalkitManagerValidateCalkit(niRFmxInstrHandle instrumentHandle, char selectorString[], char calkitId[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleT

### RFmxVNA_CalkitManagerValidateCalkit

Validates the consistency of a Calkit definition and returns the status of the validation.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerValidateCalkit(niRFmxInstrHandle instrumentHandle, char selectorString[], char calkitId[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| calkitId | [in] | char[] | This parameter specifies the ID for the Calkit in Calkit Manager. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calkitmanager

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit.html language=enus -->
## TOPIC 00058: Calkit

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsConnectorElementOptionsGroup membersNameDescriptionRFmxVNA_CalkitManagerCalkitAddCalibrationElementAdds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit. RFm

### Calkit

#### Groups

- Connector
- Element
- Options

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_CalkitManagerCalkitAddCalibrationElement | Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit. |
| RFmxVNA_CalkitManagerCalkitAddConnector | Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit. |
| RFmxVNA_CalkitManagerCalkitGetCalibrationElementIDs | Returns a list of Calibration Element IDs of all Calibration Elements of the Calkit. |
| RFmxVNA_CalkitManagerCalkitGetConnectorIDs | Returns the list of Connector IDs for all connectors in the Calkit. |
| RFmxVNA_CalkitManagerCalkitGetDescription | Returns the description of the Calkit. |
| RFmxVNA_CalkitManagerCalkitGetVersion | Returns the version string of the Calkit. |
| RFmxVNA_CalkitManagerCalkitRemoveCalibrationElement | Removes the Calibration Element identified by its Calibration Element ID from the Calkit. |
| RFmxVNA_CalkitManagerCalkitRemoveConnector | Removes a Connector element from the Calkit. |
| RFmxVNA_CalkitManagerCalkitSetDescription | Sets the description for the Calkit. |
| RFmxVNA_CalkitManagerCalkitSetVersion | Sets the version string for the Calkit. |

#### Attachments

None

Parent topic:

Calkitmanager

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga08d1eb4f688511cff479aa1f2a60c64d.html language=enus -->
## TOPIC 00059: RFmxVNA_CalkitManagerCalkitGetConnectorIDs

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga08d1eb4f688511cff479aa1f2a60c64d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga08d1eb4f688511cff479aa1f2a60c64d.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the list of Connector IDs for all connectors in the Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitGetConnectorIDs(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char connectorIds[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHa

### RFmxVNA_CalkitManagerCalkitGetConnectorIDs

Returns the list of Connector IDs for all connectors in the Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetConnectorIDs(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char connectorIds[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| connectorIds | [out] | char[] | This parameter returns the list of Connector IDs for all connectors in the Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga1d91c1507375671b1e1a30611d0c43a5.html language=enus -->
## TOPIC 00060: RFmxVNA_CalkitManagerCalkitSetDescription

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga1d91c1507375671b1e1a30611d0c43a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga1d91c1507375671b1e1a30611d0c43a5.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the description for the Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitSetDescription(niRFmxInstrHandle instrumentHandle, char selectorString[], char calkitDescription[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx sessio

### RFmxVNA_CalkitManagerCalkitSetDescription

Sets the description for the Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitSetDescription(niRFmxInstrHandle instrumentHandle, char selectorString[], char calkitDescription[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| calkitDescription | [in] | char[] | This parameter specifies the description of the Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga21bc60b1478e7007dc52888674792f3c.html language=enus -->
## TOPIC 00061: RFmxVNA_CalkitManagerCalkitAddConnector

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga21bc60b1478e7007dc52888674792f3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga21bc60b1478e7007dc52888674792f3c.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitAddConnector(niRFmxInstrHandle instrumentHandle, char selectorString[], char connectorId[])Paramete

### RFmxVNA_CalkitManagerCalkitAddConnector

Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitAddConnector(niRFmxInstrHandle instrumentHandle, char selectorString[], char connectorId[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| connectorId | [in] | char[] | This parameter specifies the ID of the Connector within the Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga422aad258a2b7f314f67b7e8496f36f3.html language=enus -->
## TOPIC 00062: RFmxVNA_CalkitManagerCalkitRemoveCalibrationElement

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga422aad258a2b7f314f67b7e8496f36f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga422aad258a2b7f314f67b7e8496f36f3.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the Calibration Element identified by its Calibration Element ID from the Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitRemoveCalibrationElement(niRFmxInstrHandle instrumentHandle, char selectorString[], char calibrationElementId[])ParametersNameDirectionTypeDescriptioninstrumentH

### RFmxVNA_CalkitManagerCalkitRemoveCalibrationElement

Removes the Calibration Element identified by its Calibration Element ID from the Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitRemoveCalibrationElement(niRFmxInstrHandle instrumentHandle, char selectorString[], char calibrationElementId[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| calibrationElementId | [in] | char[] | This parameter specifies the ID of the Calibration Element within the Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga55cf63d690b614b1f9b8ebcef073bfe3.html language=enus -->
## TOPIC 00063: RFmxVNA_CalkitManagerCalkitGetVersion

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga55cf63d690b614b1f9b8ebcef073bfe3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1ga55cf63d690b614b1f9b8ebcef073bfe3.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the version string of the Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitGetVersion(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char calkitVersion[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies t

### RFmxVNA_CalkitManagerCalkitGetVersion

Returns the version string of the Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetVersion(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char calkitVersion[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| calkitVersion | [out] | char[] | This parameter returns the version string of the Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1gadb092b198826ff3c167dd9d111f7cce8.html language=enus -->
## TOPIC 00064: RFmxVNA_CalkitManagerCalkitRemoveConnector

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1gadb092b198826ff3c167dd9d111f7cce8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit_1gadb092b198826ff3c167dd9d111f7cce8.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a Connector element from the Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitRemoveConnector(niRFmxInstrHandle instrumentHandle, char selectorString[], char connectorId[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx ses

### RFmxVNA_CalkitManagerCalkitRemoveConnector

Removes a Connector element from the Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitRemoveConnector(niRFmxInstrHandle instrumentHandle, char selectorString[], char connectorId[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| connectorId | [in] | char[] | This parameter specifies the ID of the Connector within the Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga67e1f5f08ef126ef07d50e13afd07f52.html language=enus -->
## TOPIC 00065: RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga67e1f5f08ef126ef07d50e13afd07f52.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga67e1f5f08ef126ef07d50e13afd07f52.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Minimum Frequency of a Connector of a specific Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *minimumFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrH

### RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency

Returns the Minimum Frequency of a Connector of a specific Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *minimumFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| minimumFrequency | [out] | float64 * | This parameter returns the Minimum Frequency of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Connector

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga7e482fb3275c4d03c7744a9b333cf44f.html language=enus -->
## TOPIC 00066: RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga7e482fb3275c4d03c7744a9b333cf44f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga7e482fb3275c4d03c7744a9b333cf44f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Minimum Frequency of a Connector of a specific Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 minimumFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandl

### RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency

Sets the Minimum Frequency of a Connector of a specific Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 minimumFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| minimumFrequency | [in] | float64 | This parameter specifies the Minimum Frequency of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Connector

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga806a7e9fdff0dfff0e41db9c62b99b0f.html language=enus -->
## TOPIC 00067: RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga806a7e9fdff0dfff0e41db9c62b99b0f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1ga806a7e9fdff0dfff0e41db9c62b99b0f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Maximum Frequency of a Connector of a specific Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 maximumFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandl

### RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency

Sets the Maximum Frequency of a Connector of a specific Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 maximumFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| maximumFrequency | [in] | float64 | This parameter specifies the Maximum Frequency of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Connector

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1gac7f95b5cc6aeed022008fb1e81651b76.html language=enus -->
## TOPIC 00068: RFmxVNA_CalkitManagerCalkitConnectorSetGender

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1gac7f95b5cc6aeed022008fb1e81651b76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1gac7f95b5cc6aeed022008fb1e81651b76.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Gender of a Connector of a specific Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetGender(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 connectorGender)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifie

### RFmxVNA_CalkitManagerCalkitConnectorSetGender

Sets the Gender of a Connector of a specific Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetGender(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 connectorGender)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| connectorGender | [in] | int32 | This parameter specifies the Gender of a Connector of a specific Calkit.Name (Value)DescriptionMale (0)Female (1)NoGender (2) |
| Name (Value) | Description |  |  |
| Male (0) |  |  |  |
| Female (1) |  |  |  |
| NoGender (2) |  |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Connector

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1gad7d8a3241496b3ac908c5a199e4c1873.html language=enus -->
## TOPIC 00069: RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1gad7d8a3241496b3ac908c5a199e4c1873.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__connector_1gad7d8a3241496b3ac908c5a199e4c1873.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Maximum Frequency of a Connector of a specific Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *maximumFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrH

### RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency

Returns the Maximum Frequency of a Connector of a specific Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *maximumFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| maximumFrequency | [out] | float64 * | This parameter returns the Maximum Frequency of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Connector

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element.html language=enus -->
## TOPIC 00070: Element

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDelaymodelReflectmodelSparamGroup membersNameDescriptionRFmxVNA_CalkitManagerCalkitCalibrationElementGetDescriptionReturns the description for a Calibration Element of a specific Calkit. RFmxVNA_CalkitManagerCalkitCalibrationElementGetMaximumFrequencyReturns the Maximum Frequency of the Calibr

### Element

#### Groups

- Delaymodel
- Reflectmodel
- Sparam

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_CalkitManagerCalkitCalibrationElementGetDescription | Returns the description for a Calibration Element of a specific Calkit. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementGetMaximumFrequency | Returns the Maximum Frequency of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementGetMinimumFrequency | Returns the Minimum Frequency of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors | Returns the array of Connectors associated with the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementGetSParameterDefinition | Returns the S-Parameter definition of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementGetTypes | Returns the type(s) of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSetDescription | Sets the description for a Calibration Element of a specific Calkit. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSetMaximumFrequency | Sets the Maximum Frequency of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency | Sets the Minimum Frequency of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSetPortConnectors | Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSetSParameterDefinition | Defines the way how the S-Parameters of the Calibration Element are specified. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSetTypes | Sets the type(s) of the Calibration Element. |

#### Attachments

None

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1ga07800eb8d09b8664b85c2659af75f2c9.html language=enus -->
## TOPIC 00071: RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1ga07800eb8d09b8664b85c2659af75f2c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1ga07800eb8d09b8664b85c2659af75f2c9.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of Connectors associated with the Calibration Element. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char connectorIds[])ParametersNameDirectionTypeDescriptioninstrume

### RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors

Returns the array of Connectors associated with the Calibration Element.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char connectorIds[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| connectorIds | [out] | char[] | This parameter returns the array of Connectors associated with the Calibration Element. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Element

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gaaa8b0f26da0d8e2be4e3241262c89645.html language=enus -->
## TOPIC 00072: RFmxVNA_CalkitManagerCalkitCalibrationElementSetDescription

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gaaa8b0f26da0d8e2be4e3241262c89645.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gaaa8b0f26da0d8e2be4e3241262c89645.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the description for a Calibration Element of a specific Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetDescription(niRFmxInstrHandle instrumentHandle, char selectorString[], char description[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHa

### RFmxVNA_CalkitManagerCalkitCalibrationElementSetDescription

Sets the description for a Calibration Element of a specific Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetDescription(niRFmxInstrHandle instrumentHandle, char selectorString[], char description[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| description | [in] | char[] | This parameter specifies the description for a Calibration Element of a specific Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Element

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gab3e9e841c42d21cec5aa8421aecba622.html language=enus -->
## TOPIC 00073: RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gab3e9e841c42d21cec5aa8421aecba622.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gab3e9e841c42d21cec5aa8421aecba622.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Minimum Frequency of the Calibration Element. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 minimumFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandl

### RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency

Sets the Minimum Frequency of the Calibration Element.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 minimumFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| minimumFrequency | [in] | float64 | This parameter specifies the Minimum Frequency of the Calibration Element. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Element

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gab9dd85a6e6c2a6d6f9971e666785e3aa.html language=enus -->
## TOPIC 00074: RFmxVNA_CalkitManagerCalkitCalibrationElementGetDescription

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gab9dd85a6e6c2a6d6f9971e666785e3aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element_1gab9dd85a6e6c2a6d6f9971e666785e3aa.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the description for a Calibration Element of a specific Calkit. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetDescription(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char description[])ParametersNameDirectionTypeDescriptioninstrumentHan

### RFmxVNA_CalkitManagerCalkitCalibrationElementGetDescription

Returns the description for a Calibration Element of a specific Calkit.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetDescription(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char description[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| description | [out] | char[] | This parameter returns the description for a Calibration Element of a specific Calkit. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Element

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1ga117a5ce5e7eecdc457edec70f9f5d12f.html language=enus -->
## TOPIC 00075: RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetOffsetZ0

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1ga117a5ce5e7eecdc457edec70f9f5d12f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1ga117a5ce5e7eecdc457edec70f9f5d12f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the impedance of the offset. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetOffsetZ0(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetZ0)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter spec

### RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetOffsetZ0

Specifies the impedance of the offset.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetOffsetZ0(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetZ0)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| offsetZ0 | [in] | float64 | This parameter specifies the impedance of the offset. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Reflectmodel

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1ga1400c7c4102e10ad0ff4353fec7619c1.html language=enus -->
## TOPIC 00076: RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetModelType

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1ga1400c7c4102e10ad0ff4353fec7619c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1ga1400c7c4102e10ad0ff4353fec7619c1.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the model type of the 1-port reflect standard. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetModelType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 modelType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleT

### RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetModelType

Specifies the model type of the 1-port reflect standard.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetModelType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 modelType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| modelType | [in] | int32 | This parameter specifies the model type of of the 1-port reflect standard.Name (Value)DescriptionReflect Open (0)Models an Offset Open by specifying the offset parameters and the parameters of the Open (3rd order polynomial model of the capacitance).Reflect Short (1)Models an Offset Short by specifying the offset parameters and the parameters of the short (3rd order polynomial model of the inductance).Load (2)Models an Offset Load by specifying the offset parameters. |
| Name (Value) | Description |  |  |
| Reflect Open (0) | Models an Offset Open by specifying the offset parameters and the parameters of the Open (3rd order polynomial model of the capacitance). |  |  |
| Reflect Short (1) | Models an Offset Short by specifying the offset parameters and the parameters of the short (3rd order polynomial model of the inductance). |  |  |
| Load (2) | Models an Offset Load by specifying the offset parameters. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Reflectmodel

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1gab2674ff69ffc459949c5a478512a26f6.html language=enus -->
## TOPIC 00077: RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC1

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1gab2674ff69ffc459949c5a478512a26f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__reflectmodel_1gab2674ff69ffc459949c5a478512a26f6.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. Syntaxint32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC1(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 c1)Param

### RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC1

Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Syntax

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC1(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 c1)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| c1 | [in] | float64 | This parameter specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Reflectmodel

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__sparam.html language=enus -->
## TOPIC 00078: Sparam

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__sparam.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__calibration__calkitmanager__calkit__element__sparam.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetFrequencyReturns the frequency array for the S-Parameter definition of the Calibration Element. RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11Returns the S11 S-Parameter for the calibration

### Sparam

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetFrequency | Returns the frequency array for the S-Parameter definition of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11 | Returns the S11 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11Split | Returns the S11 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12 | Returns the S12 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12Split | Returns the S12 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21 | Returns the S21 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21Split | Returns the S21 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22 | Returns the S22 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22Split | Returns the S22 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability | Returns the S-Parameter availability. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetFrequency | Defines the frequency array for the S-Parameter definition of the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetFromFile | Defines the touchstone file name from which the S-Parameter shall be read and assigned to the Calibration Element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS11 | Sets the S11 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS11Split | Sets the S11 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS12 | Sets the S12 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS12Split | Sets the S12 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS21 | Sets the S21 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS21Split | Sets the S21 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS22 | Sets the S22 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS22Split | Sets the S22 S-Parameter for the calibration element. |
| RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability | Defines the S-Parameter availability. |

#### Attachments

None

Parent topic:

Element

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration_1ga50f65ace5b5d653ef5b7fbac332348b7.html language=enus -->
## TOPIC 00079: RFmxVNA_SendSoftwareEdgeTrigger

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration_1ga50f65ace5b5d653ef5b7fbac332348b7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration_1ga50f65ace5b5d653ef5b7fbac332348b7.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you set RFMXVNA_ATTR_TRIGGER_TYPE to Software and the device is waiting for the trigger to be sent. RFmxVNA ignores Software Edge Trigger when performing calibration.Syntaxint32 __stdcall RFmxVNA_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)Parameters

### RFmxVNA_SendSoftwareEdgeTrigger

Sends a trigger to the device when you set [RFMXVNA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_v_n_a__attributes__trigger_1gab93668ad4178dd8ec3d9f303cb28ed44.html) to Software and the device is waiting for the trigger to be sent.

Note

RFmxVNA ignores Software Edge Trigger when performing calibration.

#### Syntax

int32 __stdcall RFmxVNA_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga576d9ab52f637844e50662f5869fc390.html language=enus -->
## TOPIC 00080: RFmxVNA_CalsetLoadFromFile

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga576d9ab52f637844e50662f5869fc390.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga576d9ab52f637844e50662f5869fc390.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads calset from a calset file (*.ncst), either to the default calset of the specified signal or to a named calset accessible across all signals. Syntaxint32 __stdcall RFmxVNA_CalsetLoadFromFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[], char calsetFilePath[])Rema

### RFmxVNA_CalsetLoadFromFile

Loads calset from a calset file (*.ncst), either to the default calset of the specified signal or to a named calset accessible across all signals.

#### Syntax

int32 __stdcall RFmxVNA_CalsetLoadFromFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[], char calsetFilePath[])

#### Remarks

- Calset Name is "" (empty string): RFmx loads calset from file to the default calset of the signal instance specified in the Selector String and selects the default calset as active calset for the signal. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx loads calset from file to a named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

Note

This function will overwrite the contents of the calset if it already exists.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calsetName | [in] | char[] | This parameter specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. |
| calsetFilePath | [in] | char[] | This parameter specifies the complete path to the file with .ncst extension from which the calset is to be loaded. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga5c569f35363039b830645462df64ab70.html language=enus -->
## TOPIC 00081: RFmxVNA_GetAllCalsetNames

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga5c569f35363039b830645462df64ab70.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga5c569f35363039b830645462df64ab70.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of calset names of all the available named calsets which are accessible across all signals. Syntaxint32 __stdcall RFmxVNA_GetAllCalsetNames(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char calsetNames[])ParametersNameDirectionTypeDescriptioninstrument

### RFmxVNA_GetAllCalsetNames

Returns an array of calset names of all the available named calsets which are accessible across all signals.

#### Syntax

int32 __stdcall RFmxVNA_GetAllCalsetNames(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char calsetNames[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter is ignored currently by this VI |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| calsetNames | [out] | char[] | This parameter returns an array of calset names for all the available named calsets. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga7e8515941763f4ab170c9e344f57fd8f.html language=enus -->
## TOPIC 00082: RFmxVNA_CalsetGetFrequencyGrid

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga7e8515941763f4ab170c9e344f57fd8f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga7e8515941763f4ab170c9e344f57fd8f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals. Syntaxint32 __stdcall RFmxVNA_CalsetGetFrequencyGrid(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[], int32 errorTermIdentifier,

### RFmxVNA_CalsetGetFrequencyGrid

Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals.

#### Syntax

int32 __stdcall RFmxVNA_CalsetGetFrequencyGrid(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[], int32 errorTermIdentifier, float64 frequencyGrid[], int32 arraySize, int32 *actualArraySize)

#### Remarks

- Calset Name is "" (empty string): RFmx returns the calibration frequency grid from the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx returns the calibration frequency grid from the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calsetName | [in] | char[] | This parameter specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. |
| errorTermIdentifier | [in] | int32 | This parameter specifies the type of error term in the calset.The error term can take the following values:Name (Value)DescriptionDirectivity (0)Directivity measured at Measurement Port (Source Port ignored).Source Match (1)Source Match measured at Measurement Port (Source Port ignored).Reflection Tracking (2)Reflection Tracking measured at Measurement Port (Source Port ignored).Transmission Tracking (3)Transmission Tracking measured at Measurement Port with Source Port being the source port.Load Match (4)Load Match measured at Measurement Port with Source Port being the source port.K (5)K measured at Measurement Port (Source Port ignored).alpha (6)alpha measured at Measurement Port (Source Port ignored).beta (7)beta measured at Measurement Port (Source Port ignored).gamma (8)gamma measured at Measurement Port (Source Port ignored).delta (9)delta measured at Measurement Port (Source Port ignored).Switch Term (10)Switch term measured at Measurement Port (Source Port ignored).The error term K, alpha, beta, gamma, and delta describe the relation of the scattered and incident waves at the calibration plane (denoted as waves a and b respectively) and the waves measured at VNA reference and test receivers (denoted as waves r and s respectively) by the following equations:a = K[alpha r + beta s] b = K[gamma r + delta s], where alpha, beta, gamma, and delta represent the complex elements of a transmission matrix and K represents a complex scaling factor. |
| Name (Value) | Description |  |  |
| Directivity (0) | Directivity measured at Measurement Port (Source Port ignored). |  |  |
| Source Match (1) | Source Match measured at Measurement Port (Source Port ignored). |  |  |
| Reflection Tracking (2) | Reflection Tracking measured at Measurement Port (Source Port ignored). |  |  |
| Transmission Tracking (3) | Transmission Tracking measured at Measurement Port with Source Port being the source port. |  |  |
| Load Match (4) | Load Match measured at Measurement Port with Source Port being the source port. |  |  |
| K (5) | K measured at Measurement Port (Source Port ignored). |  |  |
| alpha (6) | alpha measured at Measurement Port (Source Port ignored). |  |  |
| beta (7) | beta measured at Measurement Port (Source Port ignored). |  |  |
| gamma (8) | gamma measured at Measurement Port (Source Port ignored). |  |  |
| delta (9) | delta measured at Measurement Port (Source Port ignored). |  |  |
| Switch Term (10) | Switch term measured at Measurement Port (Source Port ignored). |  |  |
| frequencyGrid | [out] | float64[] | This parameter returns the calibration frequency grid from the calset. This value is expressed in Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga9372d194e58a6ca84704505c9ceb9b66.html language=enus -->
## TOPIC 00083: RFmxVNA_CalsetEmbedFixtureS2p

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga9372d194e58a6ca84704505c9ceb9b66.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1ga9372d194e58a6ca84704505c9ceb9b66.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Embeds the inverse of a given fixture network into a specified calset. The typical use case for this utility is to remove the effect of an adapter that was present during calibration but is not present during later measurements from the Calset itself such that corrected measurements can be performed

### RFmxVNA_CalsetEmbedFixtureS2p

Embeds the inverse of a given fixture network into a specified calset. The typical use case for this utility is to remove the effect of an adapter that was present during calibration but is not present during later measurements from the Calset itself such that corrected measurements can be performed without considering the calibration adapter in the measurement de-embedding.

#### Syntax

int32 __stdcall RFmxVNA_CalsetEmbedFixtureS2p(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[], char fixtureS2PFilePath[], char vnaPort[], int32 sParameterOrientation, char newCalsetName[])

#### Remarks

- Both Calset Name and New Calset Name are "" (empty string): RFmx modifies the default calset of the signal instance specified in the Selector String, with embedding data. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is "" (empty string) and New Calset Name is non-empty string: RFmx creates a new named calset with the name specified by New Calset Name from the default calset of the signal instance specified in the Selector String and modifies the new named calset with embedding data. This newly created named calset is made accessible across all signals. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string and New Calset Name is "" (empty string): If you do not specify a Signal Name, then RFmx modifies the existing named calset with embedding data. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.
- Both Calset Name and New Calset Name are non-empty string: If you do not specify a Signal Name, then RFmx creates a new named calset with the name specified by New Calset Name from the existing named calset specified by Calset Name and modifies the new named calset with embedding data. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calsetName | [in] | char[] | This parameter specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. |
| fixtureS2PFilePath | [in] | char[] | This parameter Specifies the path to the s2p file containing the fixture S-parameters. |
| vnaPort | [in] | char[] | This parameter specifies the port name of the Calset VNA port. |
| sParameterOrientation | [in] | int32 | This parameter specifies the orientation of the configured fixture network with respect to VNA port.Name (Value)DescriptionPort1 Towards VNA (0)Specifies that port1 of the fixture is towards VNA port.Port2 Towards VNA (1)Specifies that port2 of the fixture is towards VNA port. |
| Name (Value) | Description |  |  |
| Port1 Towards VNA (0) | Specifies that port1 of the fixture is towards VNA port. |  |  |
| Port2 Towards VNA (1) | Specifies that port2 of the fixture is towards VNA port. |  |  |
| newCalsetName | [in] | char[] | This parameter specifies the name under which the result Calset (with updated error coefficients) is to be saved. If empty string is provided, the updated Calset is saved back into the original Calset. That is, the original Calset is overwritten. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1gab7fa33f86b0accac3eb81abe9385f1a2.html language=enus -->
## TOPIC 00084: RFmxVNA_ClearCalset

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1gab7fa33f86b0accac3eb81abe9385f1a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1gab7fa33f86b0accac3eb81abe9385f1a2.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears either the default calset of the specified signal or a named calset accessible across all signals. Syntaxint32 __stdcall RFmxVNA_ClearCalset(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[])RemarksBehaviors for different combinations of Calset Name and Signal Name

### RFmxVNA_ClearCalset

Clears either the default calset of the specified signal or a named calset accessible across all signals.

#### Syntax

int32 __stdcall RFmxVNA_ClearCalset(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[])

#### Remarks

- Calset Name is "" (empty string): RFmx clears the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx clears the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calsetName | [in] | char[] | This parameter specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1gae4ddb55ac2e26b97149e0380ccb92c39.html language=enus -->
## TOPIC 00085: RFmxVNA_CalsetSaveToFile

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1gae4ddb55ac2e26b97149e0380ccb92c39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__calset_1gae4ddb55ac2e26b97149e0380ccb92c39.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves to a calset file (*.ncst), either the default calset of the specified signal or a named calset accessible across all signals and corresponding relevant stimulus settings that were used to perform calibration. Syntaxint32 __stdcall RFmxVNA_CalsetSaveToFile(niRFmxInstrHandle instrumentHandle, ch

### RFmxVNA_CalsetSaveToFile

Saves to a calset file (*.ncst), either the default calset of the specified signal or a named calset accessible across all signals and corresponding relevant stimulus settings that were used to perform calibration.

#### Syntax

int32 __stdcall RFmxVNA_CalsetSaveToFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char calsetName[], char calsetFilePath[])

#### Remarks

- Calset Name is "" (empty string): RFmx saves to file, the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx saves the named calset to file. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

RFmxVNA_SelectActiveCalset

Restore Configuration

- SweepType
- **List** Sweep Type: IF Bandwidth, Power Level per Port, Test Receiver Attenuation per Port, Frequency List
- **Linear** Sweep Type: IF Bandwidth, Power Level per Port, Test Receiver Attenuation per Port, Start Frequency, Stop Frequency and Number of Frequency Points
- **Segment** Sweep Type: Segment IF Bandwidth, Segment Power Level per Port, Segment Test Receiver Attenuation per Port, Segment Start Frequency, Segment Stop Frequency and Segment Number of Frequency Points

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| calsetName | [in] | char[] | This parameter specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. |
| calsetFilePath | [in] | char[] | This parameter specifies the absolute path to the calset file (*.ncst). If the path you specified does not end with '.ncst' file extension, then RFmx automatically adds the extension before saving the file to disk. If the path you specify points to an already existing calset file, then RFmx overwrites that file without warning. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__sparams.html language=enus -->
## TOPIC 00086: SParams

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__sparams.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__sparams.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxVNA_SParamsCfgSParameterConfigures the S-Parameter to be measured in format S<receiver port number><source port number> RFmxVNA_SParamsExportToSnPFileExports the measured S-parameters to a SnP file. RFmxVNA_SParamsGetSParameterReturns the S-Parameter being m

### SParams

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_SParamsCfgSParameter | Configures the S-Parameter to be measured in format S<receiver port number><source port number> |
| RFmxVNA_SParamsExportToSnPFile | Exports the measured S-parameters to a SnP file. |
| RFmxVNA_SParamsGetSParameter | Returns the S-Parameter being measured in format S<receiver port number><source port number> |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__sparams_1ga1b14cf9d7a706786b7f71b0d6ce8786f.html language=enus -->
## TOPIC 00087: RFmxVNA_SParamsGetSParameter

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__sparams_1ga1b14cf9d7a706786b7f71b0d6ce8786f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__sparams_1ga1b14cf9d7a706786b7f71b0d6ce8786f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-Parameter being measured in format S<receiver port number><source port number> Syntaxint32 __stdcall RFmxVNA_SParamsGetSParameter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char sParameter[])RemarksUse "sparam<n>" as the selector string for this functio

### RFmxVNA_SParamsGetSParameter

Returns the S-Parameter being measured in format S<*receiver port number*><*source port number*>

#### Syntax

int32 __stdcall RFmxVNA_SParamsGetSParameter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char sParameter[])

#### Remarks

Use "sparam<n>" as the selector string for this function.

**Supported devices**: NI PXIe-5633

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"sparam0""signal::sig1/sparam0""result::r1/sparam0""signal::sig1/result::r1/sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| sParameter | [out] | char[] | This parameter returns the S-Parameter being measured in format S<receiver port number><source port number>. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__sparams_1ga8a9f313ea652af7924b90ace436d0582.html language=enus -->
## TOPIC 00088: RFmxVNA_SParamsCfgSParameter

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__sparams_1ga8a9f313ea652af7924b90ace436d0582.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__sparams_1ga8a9f313ea652af7924b90ace436d0582.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-Parameter to be measured in format S<receiver port number><source port number> Syntaxint32 __stdcall RFmxVNA_SParamsCfgSParameter(niRFmxInstrHandle instrumentHandle, char selectorString[], char sParameter[])RemarksUse "sparam<n>" as the selector string to configure this function.Thi

### RFmxVNA_SParamsCfgSParameter

Configures the S-Parameter to be measured in format S<*receiver port number*><*source port number*>

#### Syntax

int32 __stdcall RFmxVNA_SParamsCfgSParameter(niRFmxInstrHandle instrumentHandle, char selectorString[], char sParameter[])

#### Remarks

Use "sparam<n>" as the selector string to configure this function.

This function sets [RFMXVNA_ATTR_SPARAMS_SOURCE_PORT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gaa63ec80be552f6e7250def17f934955a.html) and [RFMXVNA_ATTR_SPARAMS_RECEIVER_PORT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1ga1720714e19307f9d42a31ddbf279cb80.html) attributes.

**Supported devices**: NI PXIe-5633

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"sparam0""signal::sig1/sparam0""result::r1/sparam0""signal::sig1/result::r1/sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| sParameter | [in] | char[] | This parameter specifies the S-Parameter to be measured in format S<receiver port number><source port number>. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__configuration__waves_1gaceda3f096bdd1ba8b5c5ee9763de3fbf.html language=enus -->
## TOPIC 00089: RFmxVNA_WavesCfgWave

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__configuration__waves_1gaceda3f096bdd1ba8b5c5ee9763de3fbf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__configuration__waves_1gaceda3f096bdd1ba8b5c5ee9763de3fbf.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the wave to be measured in format a<receiver port number><source port number> or b<receiver port number><source port number>, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. Syntaxint32 __stdcall RFmxVNA_WavesCfgWave(niRFmx

### RFmxVNA_WavesCfgWave

Configures the wave to be measured in format a<*receiver port number*><*source port number*> or b<*receiver port number*><*source port number*>, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver.

#### Syntax

int32 __stdcall RFmxVNA_WavesCfgWave(niRFmxInstrHandle instrumentHandle, char selectorString[], char wave[])

#### Remarks

Use "wave<n>" as the selector string to configure this function.

**Supported devices**: NI PXIe-5633

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name, result name, and wave number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used."wave0""signal::sig1/wave0""result::r1/wave0""signal::sig1/result::r1/wave0"You can use the RFmxVNA_BuildWaveString function to build the selector string. |
| wave | [in] | char[] | This parameter specifies the wave to be measured in format a<receiver port number><source port number> or b<receiver port number><source port number>, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Waves

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__fetch.html language=enus -->
## TOPIC 00090: Fetch

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__fetch.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsSParams DataWaves DataGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- SParams Data
- Waves Data

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data.html language=enus -->
## TOPIC 00091: SParams Data

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxVNA_SParamsFetchXDataFetches an array of frequency values when you perform S-Parameter measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to List or Linear or Segment. It fetches an array of time values when you perform S-Parameter measurement with RFMXV

### SParams Data

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_SParamsFetchXData | Fetches an array of frequency values when you perform S-Parameter measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to List or Linear or Segment. It fetches an array of time values when you perform S-Parameter measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to CW Time. |
| RFmxVNA_SParamsFetchYData | Fetches the S-Parameter data for all RFMXVNA_ATTR_SPARAMS_FORMAT types. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data_1ga2d3dbe2dd5113cbd2f814e04597729e6.html language=enus -->
## TOPIC 00092: RFmxVNA_SParamsFetchXData

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data_1ga2d3dbe2dd5113cbd2f814e04597729e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data_1ga2d3dbe2dd5113cbd2f814e04597729e6.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of frequency values when you perform S-Parameter measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to List or Linear or Segment. It fetches an array of time values when you perform S-Parameter measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to CW Time. Syntaxint32 __stdc

### RFmxVNA_SParamsFetchXData

Fetches an array of frequency values when you perform S-Parameter measurement with [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute set to **List** or **Linear** or **Segment**. It fetches an array of time values when you perform S-Parameter measurement with [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute set to **CW Time**.

#### Syntax

int32 __stdcall RFmxVNA_SParamsFetchXData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 x[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x | [out] | float64[] | This parameter returns X-Axis Data. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SParams Data

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data_1gad5cb44a07bd16bac9433120345e8942f.html language=enus -->
## TOPIC 00093: RFmxVNA_SParamsFetchYData

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data_1gad5cb44a07bd16bac9433120345e8942f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__fetch__sparams____data_1gad5cb44a07bd16bac9433120345e8942f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the S-Parameter data for all RFMXVNA_ATTR_SPARAMS_FORMAT types. Syntaxint32 __stdcall RFmxVNA_SParamsFetchYData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 y1[], float32 y2[], int32 arraySize, int32 *actualArraySize)RemarksUse "sparam<n>" as the select

### RFmxVNA_SParamsFetchYData

Fetches the S-Parameter data for all [RFMXVNA_ATTR_SPARAMS_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html) types.

#### Syntax

int32 __stdcall RFmxVNA_SParamsFetchYData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 y1[], float32 y2[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "sparam<n>" as the selector string to read results from this function.

For different [RFMXVNA_ATTR_SPARAMS_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__sparams_1gab303c827dcf1a4b1295a04f396c52309.html), the data is returned as follows:

| SParam Format | Y1 | Y2 |
| --- | --- | --- |
| Magnitude (0) | Magnitude of the S-Parameter data | Empty array |
| Phase (1) | Phase of the S-Parameter data | Empty array |
| Complex (2) | Real part of the complex S-Parameter data | Imaginary part of the complex S-Parameter data |
| SWR (3) | Standing wave ratio computed from the S-Parameter data | Empty array |
| Smith Impedance (4) | Real part of the complex impedance computed from the S-Parameter data | Imaginary part of the complex impedance computed from the S-Parameter data |
| Smith Admittance (5) | Real part of the complex admittance computed from the S-Parameter data | Imaginary part of the complex admittance computed from the S-Parameter data |
| Polar (6) | Magnitude of the S-Parameter data | Phase of the S-Parameter data |
| Group Delay (7) | Group delay computed from the S-Parameter data | Empty array |

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"sparam0""signal::sig1/sparam0""result::r1/sparam0""signal::sig1/result::r1/sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| y1 | [out] | float32[] | This parameter returns Y1 data array. You can refer to the function description for interpreting Y data based on RFMXVNA_ATTR_SPARAMS_FORMAT type. |
| y2 | [out] | float32[] | This parameter returns Y2 data array. You can refer to the function description for interpreting Y data based on RFMXVNA_ATTR_SPARAMS_FORMAT type. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SParams Data

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data.html language=enus -->
## TOPIC 00094: Waves Data

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxVNA_WavesFetchXDataFetches an array of frequency values when you perform wave measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to List or Linear or Segment. It fetches an array of time values when you perform wave measurement with RFMXVNA_ATTR_SWEEP_TY

### Waves Data

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_WavesFetchXData | Fetches an array of frequency values when you perform wave measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to List or Linear or Segment. It fetches an array of time values when you perform wave measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to CW Time. |
| RFmxVNA_WavesFetchYData | Fetches the wave data for all RFMXVNA_ATTR_WAVES_FORMAT types. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data_1ga59f9e4d532c005767ad66cf6f18a76ca.html language=enus -->
## TOPIC 00095: RFmxVNA_WavesFetchYData

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data_1ga59f9e4d532c005767ad66cf6f18a76ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data_1ga59f9e4d532c005767ad66cf6f18a76ca.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the wave data for all RFMXVNA_ATTR_WAVES_FORMAT types. Syntaxint32 __stdcall RFmxVNA_WavesFetchYData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 y1[], float32 y2[], int32 arraySize, int32 *actualArraySize)RemarksUse "wave<n>" as the selector string to

### RFmxVNA_WavesFetchYData

Fetches the wave data for all [RFMXVNA_ATTR_WAVES_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__waves_1ga2c742a51f4c46df8b38f675de78a703e.html) types.

#### Syntax

int32 __stdcall RFmxVNA_WavesFetchYData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 y1[], float32 y2[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "wave<n>" as the selector string to read results from this function.

For different [RFMXVNA_ATTR_WAVES_FORMAT](group____root__ni_r_fmx_v_n_a__attributes__waves_1ga2c742a51f4c46df8b38f675de78a703e.html), the data is returned as follows:

| Waves Format | Y1 | Y2 |
| --- | --- | --- |
| Magnitude (0) | Magnitude of the wave data | Empty array |
| Phase (1) | Phase of the wave data | Empty array |
| Complex (2) | Real part of the complex wave data | Imaginary part of the complex wave data |
| SWR (3) | Standing wave ratio computed from the wave data | Empty array |
| Smith Impedance (4) | Real part of the complex impedance computed from the wave data | Imaginary part of the complex impedance computed from the wave data |
| Smith Admittance (5) | Real part of the complex admittance computed from the wave data | Imaginary part of the complex admittance computed from the wave data |
| Polar (6) | Magnitude of the wave data | Phase of the wave data |
| Group Delay (7) | Group delay computed from the wave data | Empty array |

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"sparam0""signal::sig1/sparam0""result::r1/sparam0""signal::sig1/result::r1/sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| y1 | [out] | float32[] | This parameter returns Y1 data array. You can refer to the function description for interpreting Y data based on RFMXVNA_ATTR_WAVES_FORMAT type. |
| y2 | [out] | float32[] | This parameter returns Y2 data array. You can refer to the function description for interpreting Y data based on RFMXVNA_ATTR_WAVES_FORMAT type. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Waves Data

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data_1ga722fc30e469bea5afebce005466b2354.html language=enus -->
## TOPIC 00096: RFmxVNA_WavesFetchXData

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data_1ga722fc30e469bea5afebce005466b2354.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__fetch__waves____data_1ga722fc30e469bea5afebce005466b2354.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of frequency values when you perform wave measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to List or Linear or Segment. It fetches an array of time values when you perform wave measurement with RFMXVNA_ATTR_SWEEP_TYPE attribute set to CW Time. Syntaxint32 __stdcall RFmxVNA_Wa

### RFmxVNA_WavesFetchXData

Fetches an array of frequency values when you perform wave measurement with [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute set to **List** or **Linear** or **Segment**. It fetches an array of time values when you perform wave measurement with [RFMXVNA_ATTR_SWEEP_TYPE](group____root__ni_r_fmx_v_n_a__attributes__sweep_1gadb1bbd32468e11561d188063a09d6025.html) attribute set to **CW Time**.

#### Syntax

int32 __stdcall RFmxVNA_WavesFetchXData(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 x[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x | [out] | float64[] | This parameter returns X-Axis Data. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Waves Data

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker.html language=enus -->
## TOPIC 00097: Marker

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxVNA_MarkerCfgDataSourceConfigures the data source on which marker operations are performed. Use "marker<n>" as the selector string to configure this function. RFmxVNA_MarkerCfgModeConfigures the marker mode. Use "marker<n>" as the selector string to configur

### Marker

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_MarkerCfgDataSource | Configures the data source on which marker operations are performed. Use "marker<n>" as the selector string to configure this function. |
| RFmxVNA_MarkerCfgMode | Configures the marker mode. Use "marker<n>" as the selector string to configure this function. |
| RFmxVNA_MarkerCfgNumberOfMarkers | Configures the number of markers. |
| RFmxVNA_MarkerCfgPeakSearchExcursion | Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search function finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value. |
| RFmxVNA_MarkerCfgPeakSearchThreshold | Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search function in peak search mode finds the peaks that exceed this value and discards all other peaks. |
| RFmxVNA_MarkerCfgReferenceMarker | Configures an associated reference marker for a delta marker. Markers with Marker Type attribute set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta. |
| RFmxVNA_MarkerCfgTargetValue | Configures the target value for the specified marker when performing Target search using Marker Search function. |
| RFmxVNA_MarkerCfgType | Configures the marker type. Use "marker<n>" as the selector string to configure this function. |
| RFmxVNA_MarkerCfgX | Configures the X value of the marker. You must configure the X value of reference marker or perform any marker search operation on the reference marker before configuring the X value for the Delta marker. |
| RFmxVNA_MarkerCfgY | Configures the Y value of the marker. You can configure the Y location of Fixed markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number. |
| RFmxVNA_MarkerFetchX | Returns the X value of the marker. X value of the Delta marker is relative to its reference marker. |
| RFmxVNA_MarkerFetchY | Returns the Y value of the marker. Y value of a Delta marker is relative to its reference marker. |
| RFmxVNA_MarkerSearch | Performs the marker search operation that you specify using Search Mode. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga033c4007144475627f368f5d065c6131.html language=enus -->
## TOPIC 00098: RFmxVNA_MarkerCfgType

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga033c4007144475627f368f5d065c6131.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga033c4007144475627f368f5d065c6131.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker type. Use "marker<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxVNA_MarkerCfgType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 markerType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxVNA_MarkerCfgType

Configures the marker type. Use "marker<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 markerType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| markerType | [in] | int32 | This parameter specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. The default value is Off.Name (Value)DescriptionOff (0)The marker is disabled.Normal (1)The marker is enabled as a normal marker.Delta (3)The marker is enabled as a delta marker.Fixed (4)The marker is enabled as a fixed marker. |
| Name (Value) | Description |  |  |
| Off (0) | The marker is disabled. |  |  |
| Normal (1) | The marker is enabled as a normal marker. |  |  |
| Delta (3) | The marker is enabled as a delta marker. |  |  |
| Fixed (4) | The marker is enabled as a fixed marker. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga081d6dabcc9ebdd6206e88cb481787a7.html language=enus -->
## TOPIC 00099: RFmxVNA_MarkerCfgMode

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga081d6dabcc9ebdd6206e88cb481787a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga081d6dabcc9ebdd6206e88cb481787a7.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker mode. Use "marker<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxVNA_MarkerCfgMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 markerMode)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxVNA_MarkerCfgMode

Configures the marker mode. Use "marker<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 markerMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| markerMode | [in] | int32 | This parameter specifies the mode for placing the marker.Name (Value)DescriptionContinuous (0)Marker can be placed at any point and its response value is obtained by interpolation of actual measured data points.Discrete (1)Marker can be placed only at actual measured data points. |
| Name (Value) | Description |  |  |
| Continuous (0) | Marker can be placed at any point and its response value is obtained by interpolation of actual measured data points. |  |  |
| Discrete (1) | Marker can be placed only at actual measured data points. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga244e3e906dce0588654cfdfa3306111f.html language=enus -->
## TOPIC 00100: RFmxVNA_MarkerFetchY

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga244e3e906dce0588654cfdfa3306111f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga244e3e906dce0588654cfdfa3306111f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Y value of the marker. Y value of a Delta marker is relative to its reference marker. Syntaxint32 __stdcall RFmxVNA_MarkerFetchY(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *markerY1, float64 *markerY2)RemarksY value can be a real or a complex number depending on f

### RFmxVNA_MarkerFetchY

Returns the Y value of the marker. Y value of a **Delta** marker is relative to its reference marker.

#### Syntax

int32 __stdcall RFmxVNA_MarkerFetchY(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *markerY1, float64 *markerY2)

#### Remarks

Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number. If Y value is a complex number, Marker Y1 and Marker Y2 return its real and imaginary components respectively. If Y value is a real number, Marker Y1 returns the Y location and Marker Y2 returns 0.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| markerY1 | [out] | float64 * | This parameter returns the Y1 component of marker's Y value. |
| markerY2 | [out] | float64 * | This parameter returns the Y2 component of marker's Y value.Y value is always returned as two components (Y1,Y2). The format of the Y value depends on the format of the selected measurement.If the format is Complex, Smith or Polar (Y1,Y2) are (Real, Imaginary).For all other formats (Y1,Y2) are (Value,0). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga28efcfa1ca85534430fe994da3208898.html language=enus -->
## TOPIC 00101: RFmxVNA_MarkerCfgTargetValue

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga28efcfa1ca85534430fe994da3208898.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga28efcfa1ca85534430fe994da3208898.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the target value for the specified marker when performing Target search using Marker Search function. Syntaxint32 __stdcall RFmxVNA_MarkerCfgTargetValue(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 targetValue)RemarksUse "marker<n>" as the selector string to configur

### RFmxVNA_MarkerCfgTargetValue

Configures the target value for the specified marker when performing Target search using Marker Search function.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgTargetValue(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 targetValue)

#### Remarks

Use "marker<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| targetValue | [in] | float64 | This parameter specifies the target value for target search. The target value is expressed in the same units as the source data. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga4e1d1341f01333ac226155da74eeaa27.html language=enus -->
## TOPIC 00102: RFmxVNA_MarkerCfgPeakSearchExcursion

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga4e1d1341f01333ac226155da74eeaa27.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga4e1d1341f01333ac226155da74eeaa27.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search function finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value. Syntaxint32 __stdcall RFmxVNA_MarkerCfgPeakSearchExcursion(niRFmxInstrH

### RFmxVNA_MarkerCfgPeakSearchExcursion

Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search function finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgPeakSearchExcursion(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 peakExcursionEnabled, float64 peakExcursion)

#### Remarks

Use "marker<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| peakExcursionEnabled | [in] | int32 | This parameter specifies whether RFmxVNA_MarkerSearch finds a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value or finds a peak without considering any peak excursion constraint.Name (Value)DescriptionFalse (0)Disables the peak excursion.True (1)Enables the peak excursion. |
| Name (Value) | Description |  |  |
| False (0) | Disables the peak excursion. |  |  |
| True (1) | Enables the peak excursion. |  |  |
| peakExcursion | [in] | float64 | This parameter specifies the peak excursion value that RFmxVNA_MarkerSearch uses to find a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value. The threshold is expressed in the same units as the source data. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga4e4c3aa25b1bffc13492ea55923752a6.html language=enus -->
## TOPIC 00103: RFmxVNA_MarkerSearch

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga4e4c3aa25b1bffc13492ea55923752a6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga4e4c3aa25b1bffc13492ea55923752a6.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the marker search operation that you specify using Search Mode. Syntaxint32 __stdcall RFmxVNA_MarkerSearch(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 searchMode)RemarksMarker search operation is performed on real-valued data only. No search operation is performed on co

### RFmxVNA_MarkerSearch

Performs the marker search operation that you specify using Search Mode.

#### Syntax

int32 __stdcall RFmxVNA_MarkerSearch(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 searchMode)

#### Remarks

Note

Marker search operation is performed on real-valued data only. No search operation is performed on complex-valued data.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| searchMode | [in] | int32 | This parameter specifies the search-target. If search is successful, RFmx updates the marker X and Y values to the location at which search-target is found.Name (Value)DescriptionNone (0)No search operation is performed.Max (1)Moves the marker to the highest measured value on the configured data source.Min (2)Moves the marker to the lowest measured value on the configured data source.Peak (3)Moves the marker to the highest peak that satisfies peak threshold and peak excursion criteria.Next Peak (4)Moves the marker to the next peak that satisfies peak threshold and peak excursion criteria.Next Left Peak (5)Moves the marker to the next left peak that satisfies peak threshold and peak excursion criteria.Next Right Peak (6)Moves the marker to the next right peak that satisfies peak threshold and peak excursion criteria.Target (7)Moves the marker to the first right target encountered from the current marker position, wraps around if no target found. If marker mode is Discrete,marker moves to the data point closest to the first right target.Next Left Target (8)Moves the marker to the next left target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next left target.Next Right Target (9)Moves the marker to the next right target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next right target. |
| Name (Value) | Description |  |  |
| None (0) | No search operation is performed. |  |  |
| Max (1) | Moves the marker to the highest measured value on the configured data source. |  |  |
| Min (2) | Moves the marker to the lowest measured value on the configured data source. |  |  |
| Peak (3) | Moves the marker to the highest peak that satisfies peak threshold and peak excursion criteria. |  |  |
| Next Peak (4) | Moves the marker to the next peak that satisfies peak threshold and peak excursion criteria. |  |  |
| Next Left Peak (5) | Moves the marker to the next left peak that satisfies peak threshold and peak excursion criteria. |  |  |
| Next Right Peak (6) | Moves the marker to the next right peak that satisfies peak threshold and peak excursion criteria. |  |  |
| Target (7) | Moves the marker to the first right target encountered from the current marker position, wraps around if no target found. If marker mode is Discrete,marker moves to the data point closest to the first right target. |  |  |
| Next Left Target (8) | Moves the marker to the next left target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next left target. |  |  |
| Next Right Target (9) | Moves the marker to the next right target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next right target. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga549544ab45c44b5ff89f1595ca235950.html language=enus -->
## TOPIC 00104: RFmxVNA_MarkerCfgReferenceMarker

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga549544ab45c44b5ff89f1595ca235950.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga549544ab45c44b5ff89f1595ca235950.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an associated reference marker for a delta marker. Markers with Marker Type attribute set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta. Syntaxint32 __stdcall RFmxVNA_MarkerCfgReferenceMarker(n

### RFmxVNA_MarkerCfgReferenceMarker

Configures an associated reference marker for a delta marker. Markers with Marker Type attribute set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgReferenceMarker(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 referenceMarker)

#### Remarks

Use "marker<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| referenceMarker | [in] | int32 | This parameter specifies the marker index to be used as reference for the specified delta marker. All types of markers including Normal, Delta and Fixed can be used as a reference marker. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1ga626ead0a19a9649096287541a940f720.html language=enus -->
## TOPIC 00105: RFmxVNA_MarkerCfgPeakSearchThreshold

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1ga626ead0a19a9649096287541a940f720.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1ga626ead0a19a9649096287541a940f720.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search function in peak search mode finds the peaks that exceed this value and discards all other peaks. Syntaxint32 __stdcall RFmxVNA_MarkerCfgPeakSearchThreshold(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxVNA_MarkerCfgPeakSearchThreshold

Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search function in peak search mode finds the peaks that exceed this value and discards all other peaks.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgPeakSearchThreshold(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 thresholdEnabled, float64 threshold)

#### Remarks

Use "marker<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| thresholdEnabled | [in] | int32 | This parameter specifies whether RFmxVNA_MarkerSearch finds a peak above specified Threshold or finds a peak without considering any Threshold constraint.Name (Value)DescriptionFalse (0)Disables peak-thresholding.True (1)Enables peak-thresholding. |
| Name (Value) | Description |  |  |
| False (0) | Disables peak-thresholding. |  |  |
| True (1) | Enables peak-thresholding. |  |  |
| threshold | [in] | float64 | This parameter specifies the threshold value that a valid peak must exceed when you use RFmxVNA_MarkerSearch to find peaks. The threshold is expressed in the same units as the source data. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1gaa271bc25fe99e1bce5e6f7899f1a4d3c.html language=enus -->
## TOPIC 00106: RFmxVNA_MarkerCfgY

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1gaa271bc25fe99e1bce5e6f7899f1a4d3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1gaa271bc25fe99e1bce5e6f7899f1a4d3c.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Y value of the marker. You can configure the Y location of Fixed markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y

### RFmxVNA_MarkerCfgY

Configures the Y value of the marker. You can configure the Y location of **Fixed** markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgY(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 markerY1, float64 markerY2)

#### Remarks

If Y value is a complex number, use Marker Y1 and Marker Y2 to set its real and imaginary components respectively. If Y value is a real number, use Marker Y1 to set the Y location and set Marker Y2 to 0.

When you want to use a **Fixed** marker as a reference marker for a Delta marker, then you must configure the Y value of the **Fixed** reference marker by calling this function or by performing any marker search operation on the reference marker before configuring the X value of the **Delta** marker.

Use "marker<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| markerY1 | [in] | float64 | This parameter specifies the Y1 component of the (Fixed) marker's Y value. |
| markerY2 | [in] | float64 | This parameter specifies the Y2 component of the (Fixed) marker's Y value.. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1gaa86e700e96ec1d19930a7064987ebf81.html language=enus -->
## TOPIC 00107: RFmxVNA_MarkerCfgNumberOfMarkers

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1gaa86e700e96ec1d19930a7064987ebf81.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1gaa86e700e96ec1d19930a7064987ebf81.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of markers. Syntaxint32 __stdcall RFmxVNA_MarkerCfgNumberOfMarkers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfMarkers)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This

### RFmxVNA_MarkerCfgNumberOfMarkers

Configures the number of markers.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgNumberOfMarkers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfMarkers)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| numberOfMarkers | [in] | int32 | This parameter specifies the number of markers. If you increase number of markers from N to N+K, then existing N markers are not affected but K new markers are added. If you reduce number of markers from N to N-K, then last K markers are deleted without affecting the remaining N-K markers. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1gab1cac9cde4b063d586bda1ad06216954.html language=enus -->
## TOPIC 00108: RFmxVNA_MarkerFetchX

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1gab1cac9cde4b063d586bda1ad06216954.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1gab1cac9cde4b063d586bda1ad06216954.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the X value of the marker. X value of the Delta marker is relative to its reference marker. Syntaxint32 __stdcall RFmxVNA_MarkerFetchX(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *markerX)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis p

### RFmxVNA_MarkerFetchX

Returns the X value of the marker. X value of the **Delta** marker is relative to its reference marker.

#### Syntax

int32 __stdcall RFmxVNA_MarkerFetchX(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *markerX)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| markerX | [out] | float64 * | This parameter returns the marker X value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1gad5f605b4cb73aaafd134ef91b45007db.html language=enus -->
## TOPIC 00109: RFmxVNA_MarkerCfgDataSource

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1gad5f605b4cb73aaafd134ef91b45007db.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1gad5f605b4cb73aaafd134ef91b45007db.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the data source on which marker operations are performed. Use "marker<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxVNA_MarkerCfgDataSource(niRFmxInstrHandle instrumentHandle, char selectorString[], char dataSource[])ParametersNameDirectionTypeDescriptio

### RFmxVNA_MarkerCfgDataSource

Configures the data source on which marker operations are performed. Use "marker<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgDataSource(niRFmxInstrHandle instrumentHandle, char selectorString[], char dataSource[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| dataSource | [in] | char[] | This parameter specifies the measurement or memory data on which markers are placed. If you want to place markers on SParams measurement data, then specify this parameter as "sparam<n>". If you want to place markers on SParams measurement memory data, then specify this parameter as "sparam<n>/measmem::<<i>measMemoryName</i>>". Similarly, if you want to place markers on Wave measurement data, then specify this parameter as "wave<n>". |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__marker_1gaf39000f50d12873bf4a8e06ad187fd60.html language=enus -->
## TOPIC 00110: RFmxVNA_MarkerCfgX

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__marker_1gaf39000f50d12873bf4a8e06ad187fd60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__marker_1gaf39000f50d12873bf4a8e06ad187fd60.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the X value of the marker. You must configure the X value of reference marker or perform any marker search operation on the reference marker before configuring the X value for the Delta marker. Syntaxint32 __stdcall RFmxVNA_MarkerCfgX(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxVNA_MarkerCfgX

Configures the X value of the marker. You must configure the X value of reference marker or perform any marker search operation on the reference marker before configuring the X value for the **Delta** marker.

#### Syntax

int32 __stdcall RFmxVNA_MarkerCfgX(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 markerX)

#### Remarks

Use "marker<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | Specifies a selector string. Pass an empty string. |
| markerX | [in] | float64 | This parameter specifies the X value of the marker on the trace when you set the Marker Type to Normal or Fixed. The X value of the delta marker is relative to the X value of the reference marker when you set the Marker Type to Delta. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__memory_1ga2b81958b47c31aa18566838e853a8c60.html language=enus -->
## TOPIC 00111: RFmxVNA_ClearMeasurementMemoryNames

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__memory_1ga2b81958b47c31aa18566838e853a8c60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__memory_1ga2b81958b47c31aa18566838e853a8c60.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the measurement memory for the measurement number specified by the Selector String. Syntaxint32 __stdcall RFmxVNA_ClearMeasurementMemoryNames(niRFmxInstrHandle instrumentHandle, char selectorString[])RemarksIf Measurement memory name is "" (empty string): RFmx clears all the measurement memor

### RFmxVNA_ClearMeasurementMemoryNames

Clears the measurement memory for the measurement number specified by the Selector String.

#### Syntax

int32 __stdcall RFmxVNA_ClearMeasurementMemoryNames(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Remarks

Note

- If Measurement memory name is "" (empty string): RFmx clears all the measurement memories associated with the measurement number.
- If measurement memory name is non-empty string: RFmx clears the specified measurement memory.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name, measurement number and the measurement memory name. If you do not specify the signal name, the default signal instance is used. You must specify the measurement number.Example:"signal::sig1/sparam0/measmem::<<i>measMemoryName</i>>""signal::sig1/sparam0""sparam0"You can use the RFmxVNA_BuildMeasurementMemoryString along withRFmxVNA_BuildSParameterString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Memory

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__memory_1ga82541cac15314b4f153ce9b94ad11722.html language=enus -->
## TOPIC 00112: RFmxVNA_LoadDataToMeasurementMemoryFromFile

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__memory_1ga82541cac15314b4f153ce9b94ad11722.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__memory_1ga82541cac15314b4f153ce9b94ad11722.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the data from the input file to the measurement memory specified by the Selector String. Syntaxint32 __stdcall RFmxVNA_LoadDataToMeasurementMemoryFromFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], char parameter[], char measurementMemoryName[])RemarksThis func

### RFmxVNA_LoadDataToMeasurementMemoryFromFile

Loads the data from the input file to the measurement memory specified by the Selector String.

#### Syntax

int32 __stdcall RFmxVNA_LoadDataToMeasurementMemoryFromFile(niRFmxInstrHandle instrumentHandle, char selectorString[], char filePath[], char parameter[], char measurementMemoryName[])

#### Remarks

Note

This function will overwrite the contents of the measurement memory if it already exists.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name and the measurement number. If you do not specify the signal name, the default signal instance is used. You must specify the measurement number.Example:"signal::sig1/sparam0""sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| filePath | [in] | char[] | This parameter specifies the path to the file that contains the measurement data.Example:For S-Parameter measurement use a *.SnP file. |
| parameter | [in] | char[] | This parameter specifies the measurement parameter to load from the file.Example:Specify S11 for an *.S1P file.Specify 'S11 or S12 or S21 or S22 for an *.S2P file. |
| measurementMemoryName | [in] | char[] | This parameter Measurement Memory Name specifies the name to associate with the data you load to the measurement memory. Provide a unique name. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Memory

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__memory_1gac7de4f2d754e7a3b7ac7afc67dee2bf0.html language=enus -->
## TOPIC 00113: RFmxVNA_GetMeasurementMemoryNames

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__memory_1gac7de4f2d754e7a3b7ac7afc67dee2bf0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__memory_1gac7de4f2d754e7a3b7ac7afc67dee2bf0.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement memory names for the given signal and the measurement number. Syntaxint32 __stdcall RFmxVNA_GetMeasurementMemoryNames(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char measurementMemoryNames[])ParametersNameDirectionTypeDescriptioninstru

### RFmxVNA_GetMeasurementMemoryNames

Returns an array of measurement memory names for the given signal and the measurement number.

#### Syntax

int32 __stdcall RFmxVNA_GetMeasurementMemoryNames(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 arraySize, char measurementMemoryNames[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name and measurement number. If you do not specify the signal name, the default signal instance is used.Example:"signal::sig1/sparam0""sparam0"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| measurementMemoryNames | [out] | char[] | This parameter returns an array of Measurement Memory Names for the given measurement number. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Memory

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__select__measurement.html language=enus -->
## TOPIC 00114: Select Measurement

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__select__measurement.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxVNA_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__select__measurement_1ga6e384f3d0a83452c17a67fb81ca360ca.html language=enus -->
## TOPIC 00115: RFmxVNA_SelectMeasurements

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__select__measurement_1ga6e384f3d0a83452c17a67fb81ca360ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__select__measurement_1ga6e384f3d0a83452c17a67fb81ca360ca.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxVNA_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescripti

### RFmxVNA_SelectMeasurements

Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxVNA_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurement(s) to perform. You can specify one or more of the following measurements. The default is an empty array.Name (Value)DescriptionSParams (0)Enables S-Parameter measurement.Waves (1)Enables Wave measurement. |
| Name (Value) | Description |  |  |
| SParams (0) | Enables S-Parameter measurement. |  |  |
| Waves (1) | Enables Wave measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurement. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00116: Set and Get Attributes

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsGet AttributesSet AttributesGroup membersNoneAttachmentsNone

### Set and Get Attributes

#### Groups

- Get Attributes
- Set Attributes

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__get__attributes_1ga7888dba1c959b5ce3e900c569608ab25.html language=enus -->
## TOPIC 00117: RFmxVNA_GetAttributeU32

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__get__attributes_1ga7888dba1c959b5ce3e900c569608ab25.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__get__attributes_1ga7888dba1c959b5ce3e900c569608ab25.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxVNA_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies t

### RFmxVNA_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxVNA_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__get__attributes_1gae28f8fb37b5b4b760d45553e37c82d04.html language=enus -->
## TOPIC 00118: RFmxVNA_GetAttributeU32Array

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__get__attributes_1gae28f8fb37b5b4b760d45553e37c82d04.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__get__attributes_1gae28f8fb37b5b4b760d45553e37c82d04.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxVNA_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxVNA_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga0ba19868e27102f535f23aad5c2d10e4.html language=enus -->
## TOPIC 00119: RFmxVNA_SetAttributeU16

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga0ba19868e27102f535f23aad5c2d10e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga0ba19868e27102f535f23aad5c2d10e4.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxVNA_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the R

### RFmxVNA_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxVNA_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga2bf90c030d6e995ac813ea1e7d44c97f.html language=enus -->
## TOPIC 00120: RFmxVNA_SetAttributeI16

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga2bf90c030d6e995ac813ea1e7d44c97f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga2bf90c030d6e995ac813ea1e7d44c97f.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxVNA_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxVNA_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxVNA_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga76003fb4c15b510973d89dce97c88ddf.html language=enus -->
## TOPIC 00121: RFmxVNA_SetAttributeU64Array

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga76003fb4c15b510973d89dce97c88ddf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1ga76003fb4c15b510973d89dce97c88ddf.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxVNA_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selec

### RFmxVNA_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxVNA_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gac68a788cae44803a5c3cd59d2b33f754.html language=enus -->
## TOPIC 00122: RFmxVNA_SetAttributeI32

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gac68a788cae44803a5c3cd59d2b33f754.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gac68a788cae44803a5c3cd59d2b33f754.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxVNA_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxVNA_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxVNA_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gaef12ae3f7fa358c5884d56d1de3bc0b2.html language=enus -->
## TOPIC 00123: RFmxVNA_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gaef12ae3f7fa358c5884d56d1de3bc0b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gaef12ae3f7fa358c5884d56d1de3bc0b2.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxVNA_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxVNA_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxVNA_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gaf56a58130df163653498a9f266f5618e.html language=enus -->
## TOPIC 00124: RFmxVNA_SetAttributeI64

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gaf56a58130df163653498a9f266f5618e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__set__and__get__attributes__set__attributes_1gaf56a58130df163653498a9f266f5618e.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxVNA_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxVNA_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxVNA_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__utility.html language=enus -->
## TOPIC 00125: Utility

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__utility.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxVNA_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxVNA_CommitCommits settings to the hardw

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxVNA_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxVNA_Commit | Commits settings to the hardware. Calling this function is optional. RFmxVNA commits settings to the hardware when you call the RFmxVNA_Initiate function. |
| RFmxVNA_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxVNA_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxVNA_ResetToDefault | Resets a signal to the default values. |
| RFmxVNA_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxVNA_WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__utility_1ga0fe630c162b71104dca7fd3c97d437cd.html language=enus -->
## TOPIC 00126: RFmxVNA_WaitForAcquisitionComplete

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__utility_1ga0fe630c162b71104dca7fd3c97d437cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__utility_1ga0fe630c162b71104dca7fd3c97d437cd.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxVNA_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instrumen

### RFmxVNA_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxVNA_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__utility_1ga1a950c9113820fe19a54b508bceca9ac.html language=enus -->
## TOPIC 00127: RFmxVNA_CheckMeasurementStatus

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__utility_1ga1a950c9113820fe19a54b508bceca9ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__utility_1ga1a950c9113820fe19a54b508bceca9ac.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxVNA_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxVNA_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxVNA_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *isDone)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxVNA_BuildSParameterString function to build the selector string. |
| isDone | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__utility_1ga502394b1760c64065d2a7bf234a17720.html language=enus -->
## TOPIC 00128: RFmxVNA_ResetAttribute

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__utility_1ga502394b1760c64065d2a7bf234a17720.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__utility_1ga502394b1760c64065d2a7bf234a17720.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an attribute that you specify in the attributeID parameter to default values. Syntaxint32 __stdcall RFmxVNA_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFm

### RFmxVNA_ResetAttribute

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Syntax

int32 __stdcall RFmxVNA_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxVNA_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being reset. Refer to the Selector String (C or LabWindows/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group____root__ni_r_fmx_v_n_a__functions__utility_1ga5c13557b2776bc9d8b63dac991ba5d8a.html language=enus -->
## TOPIC 00129: RFmxVNA_Commit

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group____root__ni_r_fmx_v_n_a__functions__utility_1ga5c13557b2776bc9d8b63dac991ba5d8a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_v_n_a__functions__utility_1ga5c13557b2776bc9d8b63dac991ba5d8a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this function is optional. RFmxVNA commits settings to the hardware when you call the RFmxVNA_Initiate function. Syntaxint32 __stdcall RFmxVNA_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHa

### RFmxVNA_Commit

Commits settings to the hardware. Calling this function is optional. RFmxVNA commits settings to the hardware when you call the [RFmxVNA_Initiate](group____root__ni_r_fmx_v_n_a__functions_1ga3e08aa7c74c3b6be242bbca971a23b4a.html) function.

#### Syntax

int32 __stdcall RFmxVNA_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::mysignal1"You can use the RFmxVNA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxVNA_GetError](group____root__ni_r_fmx_v_n_a__functions_1gaeb76fff9732dba3d968cb7a84b0e4b9a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxvna-c-api-ref path=group__root__ni_r_fmx_v_n_a.html language=enus -->
## TOPIC 00130: niRFmxVNA.h

- bundle_id: `rfmxvna-c-api-ref`
- source_path: `group__root__ni_r_fmx_v_n_a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_v_n_a.html
- document_id: `rfmxvna-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxVNA.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
