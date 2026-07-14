# NI DOCUMENT BUNDLE: ni-dcpower-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-labview-api-ref start=251 end=362 -->
<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimithigh.html language=enus -->
## TOPIC 00251: Source:Pulse Voltage:Pulse Bias Current Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property

### Source:Pulse Voltage:Pulse Bias Current Limit High

Specifies the maximum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the
 *off*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

You must also specify a
 [Pulse Bias Current Limit Low](pnidcpower-pulsebiascurrentlimitlow.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [1% of
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 ,
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Current Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimitlow.html language=enus -->
## TOPIC 00252: Source:Pulse Voltage:Pulse Bias Current Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property

### Source:Pulse Voltage:Pulse Bias Current Limit Low

Specifies the minimum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the
 *off*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

You must also specify a
 [Pulse Bias Current Limit High](pnidcpower-pulsebiascurrentlimithigh.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [-
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 , -1% of
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Current Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasdelay.html language=enus -->
## TOPIC 00253: Source:Advanced:Pulse Bias Delay

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasdelay.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse. Refer to Supported Properties by Device for information about supported devices. Valid Values : 0 to 167 seconds Default Value :Refer to Supported Properties by Device for the defaul

### Source:Advanced:Pulse Bias Delay

Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.

Note

Supported Properties by Device

**Valid Values**
 : 0 to 167 seconds

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelevel.html language=enus -->
## TOPIC 00254: Source:Pulse Voltage:Pulse Bias Voltage Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Output Function property is set to Pulse Voltage . The channel must be enabled for the specified voltage level t

### Source:Pulse Voltage:Pulse Bias Voltage Level

Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

Note

Output Enabled

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Voltage Level Range](pnidcpower-pulsevoltagelevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Voltage Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Bias Voltage Level |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimit.html language=enus -->
## TOPIC 00255: Source:Pulse Current:Pulse Bias Voltage Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. This property is

### Source:Pulse Current:Pulse Bias Voltage Limit

Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Voltage Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Bias Voltage Limit |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimithigh.html language=enus -->
## TOPIC 00256: Source:Pulse Current:Pulse Bias Voltage Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property

### Source:Pulse Current:Pulse Bias Voltage Limit High

Specifies the maximum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the
 *off*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

You must also specify a
 [Pulse Bias Voltage Limit Low](pnidcpower-pulsebiasvoltagelimitlow.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [1% of
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 ,
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Voltage Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimitlow.html language=enus -->
## TOPIC 00257: Source:Pulse Current:Pulse Bias Voltage Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property

### Source:Pulse Current:Pulse Bias Voltage Limit Low

Specifies the minimum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the
 *off*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

You must also specify a
 [Pulse Bias Voltage Limit High](pnidcpower-pulsebiasvoltagelimithigh.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [-
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 , -1% of
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Voltage Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventouputterminal.html language=enus -->
## TOPIC 00258: Events:Pulse Complete Event:Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventouputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventouputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Pulse Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Specify the output terminal using the form /Dev1/PXI_Trig0 , where Dev1 is the instrument and PXI_Trig

### Events:Pulse Complete Event:Output Terminal

Specifies the output terminal for exporting the Pulse Complete event.

Note

Supported Properties by Device

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Complete Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsepolarity.html language=enus -->
## TOPIC 00259: Events:Pulse Complete Event:Pulse:Polarity

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsepolarity.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Pulse Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channel name when a

### Events:Pulse Complete Event:Pulse:Polarity

Specifies the behavior of the Pulse Complete event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Complete Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Active High | 1018 | A high pulse occurs when the event is generated. The exported signal is low level both before and after the event is generated. |
| --- | --- | --- |
| Active Low | 1019 | A low pulse occurs when the event is generated. The exported signal is high level both before and after the event is generated. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsewidth.html language=enus -->
## TOPIC 00260: Events:Pulse Complete Event:Pulse:Width

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsewidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the Pulse Complete event, in seconds. The minimum event pulse width value for PXI Express devices is 250 ns. The maximum event pulse width value for all devices is 1.6 microseconds. This property is not supported by all devices. Refer to Supported Properties by Device for info

### Events:Pulse Complete Event:Pulse:Width

Specifies the width of the Pulse Complete event, in seconds.

The minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Complete Event Pulse Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevel.html language=enus -->
## TOPIC 00261: Source:Pulse Current:Pulse Current Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Output Function property is set to Pulse Current . The channel must be enabled for the specified pulse current level to

### Source:Pulse Current:Pulse Current Level

Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

Note

Output Enabled

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Current Level Range](pnidcpower-pulsecurrentlevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Current Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Current Level |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevelrange.html language=enus -->
## TOPIC 00262: Source:Pulse Current:Pulse Current Level Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevelrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse current level range, in amps, for the specified channel(s). The range defines the valid values to which you can set the pulse current level and pulse bias current level . The Pulse Current Level Range property is applicable only if the Output Function property is set to Pulse Cur

### Source:Pulse Current:Pulse Current Level Range

Specifies the pulse current level range, in amps, for the specified channel(s).

The range defines the valid values to which you can set the
 **pulse current level**
 and
 **pulse bias current level**
 .

The Pulse Current Level Range property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

Note

Output Enabled

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Current Level Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Current Level Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimit.html language=enus -->
## TOPIC 00263: Source:Pulse Voltage:Pulse Current Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. This propert

### Source:Pulse Voltage:Pulse Current Limit

Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Current Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Current Limit |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimithigh.html language=enus -->
## TOPIC 00264: Source:Pulse Voltage:Pulse Current Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property i

### Source:Pulse Voltage:Pulse Current Limit High

Specifies the maximum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the
 *on*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

You must also specify a
 [Pulse Current Limit Low](pnidcpower-pulsecurrentlimitlow.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [1% of
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 ,
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Current Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitlow.html language=enus -->
## TOPIC 00265: Source:Pulse Voltage:Pulse Current Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property i

### Source:Pulse Voltage:Pulse Current Limit Low

Specifies the minimum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the
 *on*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

You must also specify a
 [Pulse Current Limit High](pnidcpower-pulsecurrentlimithigh.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [-
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 , -1% of
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Current Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitrange.html language=enus -->
## TOPIC 00266: Source:Pulse Voltage:Pulse Current Limit Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse current limit range, in amps, for the specified channel(s). The range defines the valid values to which you can set the pulse current limit and pulse bias current limit . This property is applicable only if the Output Function property is set to Pulse Voltage . The channel must b

### Source:Pulse Voltage:Pulse Current Limit Range

Specifies the pulse current limit range, in amps, for the specified channel(s).

The range defines the valid values to which you can set the
 **pulse current limit**
 and
 **pulse bias current limit**
 .

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

Note

Output Enabled

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Current Limit Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Current Limit Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseofftime.html language=enus -->
## TOPIC 00267: Source:Advanced:Pulse Off Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseofftime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseofftime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the length, in seconds, of the off phase of a pulse. Refer to Supported Properties by Device for information about supported devices. Valid Values : 50 microseconds to 167 seconds Default Value :Refer to Supported Properties by Device for the default value by device. Remarks The following

### Source:Advanced:Pulse Off Time

Determines the length, in seconds, of the off phase of a pulse.

Note

Supported Properties by Device

**Valid Values**
 : 50 microseconds to 167 seconds

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Off Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseontime.html language=enus -->
## TOPIC 00268: Source:Advanced:Pulse On Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseontime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseontime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the length, in seconds, of the on phase of a pulse. Refer to Supported Properties by Device for information about supported devices. Valid Values Device Values PXIe-4135, PXIe-4136/4137, PXIe-4138/4139 [50 μs to 167 s] PXIe-4139 (40W) [10 μs to 167 s] Default Value :Refer to Supported Pro

### Source:Advanced:Pulse On Time

Determines the length, in seconds, of the on phase of a pulse.

Note

Supported Properties by Device

**Valid Values**

| Device | Values |
| --- | --- |
| PXIe-4135, PXIe-4136/4137, PXIe-4138/4139 | [50 μs to 167 s] |
| PXIe-4139 (40W) | [10 μs to 167 s] |

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse On Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeedge.html language=enus -->
## TOPIC 00269: Triggers:Pulse Trigger:Digital Edge:Edge

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeedge.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Pulse trigger to assert on the rising or falling edge. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by de

### Triggers:Pulse Trigger:Digital Edge:Edge

Specifies whether to configure the Pulse trigger to assert on the rising or falling edge.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Pulse Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Rising | 1016 | Asserts the trigger on the rising edge of the digital signal. |
| --- | --- | --- |
| Falling | 1017 | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeinputterminal.html language=enus -->
## TOPIC 00270: Triggers:Pulse Trigger:Digital Edge:Input Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeinputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Pulse trigger. This property is used only when the Pulse Trigger Type property is set to Digital Edge . This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. You can specify any valid input

### Triggers:Pulse Trigger:Digital Edge:Input Terminal

Specifies the input terminal for the Pulse trigger. This property is used only when the
 [Pulse Trigger Type](/csh?topicname=pnidcpower-starttriggertype.html)
 property is set to
 **Digital Edge**
 .

Note

Supported Properties by Device

You can specify any valid input terminal for this property, and the driver will create a route between it and the Pulse Trigger terminal at Commit. Valid terminals are listed in Measurement & Automation Explorer under the
 **Device Routes**
 tab.

Specify the input terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be
 /Dev2/Engine0/SourceCompleteEvent
 , where
 Engine0
 is channel 0.

Note

/Dev1/PXI_Trig0

Dev1

PXI_Trig0

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Trigger Digital Edge - Input Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Pulse Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggertype.html language=enus -->
## TOPIC 00271: Triggers:Pulse Trigger:Trigger Type

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggertype.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Pulse trigger. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channel name when accessin

### Triggers:Pulse Trigger:Trigger Type

Specifies the behavior of the Pulse trigger.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Pulse Trigger, niDCPower Configure Software Edge Pulse Trigger, niDCPower Disable Pulse Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Digital Edge | 1014 | The data operation starts when a digital edge is detected. |
| --- | --- | --- |
| Software Edge | 1015 | The data operation starts when a software trigger occurs. |
| None | 1012 | No trigger is configured. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevel.html language=enus -->
## TOPIC 00272: Source:Pulse Voltage:Pulse Voltage Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse voltage level, in volts, that the device attempts to generate on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Output Function property is set to Pulse Voltage . The channel must be enabled for the specified pulse voltage level t

### Source:Pulse Voltage:Pulse Voltage Level

Specifies the pulse voltage level, in volts, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

Note

Output Enabled

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Voltage Level Range](pnidcpower-pulsevoltagelevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Voltage Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Voltage Level |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevelrange.html language=enus -->
## TOPIC 00273: Source:Pulse Voltage:Pulse Voltage Level Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevelrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse voltage level range, in volts, for the specified channel(s). The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level . This property is applicable only if the Output Function property is set to Pulse Voltage . The channel must

### Source:Pulse Voltage:Pulse Voltage Level Range

Specifies the pulse voltage level range, in volts, for the specified channel(s).

The range defines the valid values at which you can set the
 **pulse voltage level**
 and
 **pulse bias voltage level**
 .

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 .

Note

Output Enabled

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Voltage Level Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Voltage Level Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimit.html language=enus -->
## TOPIC 00274: Source:Pulse Current:Pulse Voltage Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. This proper

### Source:Pulse Current:Pulse Voltage Limit

Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Voltage Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Voltage Limit |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimithigh.html language=enus -->
## TOPIC 00275: Source:Pulse Current:Pulse Voltage Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property

### Source:Pulse Current:Pulse Voltage Limit High

Specifies the maximum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the
 *on*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

You must also specify a
 [Pulse Voltage Limit Low](pnidcpower-pulsevoltagelimitlow.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [1% of
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 ,
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Voltage Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitlow.html language=enus -->
## TOPIC 00276: Source:Pulse Current:Pulse Voltage Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property

### Source:Pulse Current:Pulse Voltage Limit Low

Specifies the minimum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the
 *on*
 phase of a pulse.

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

You must also specify a
 [Pulse Voltage Limit High](pnidcpower-pulsevoltagelimithigh.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [-
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 , -1% of
 [Pulse Voltage Limit Range](pnidcpower-pulsevoltagelimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

Output Function

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Voltage Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitrange.html language=enus -->
## TOPIC 00277: Source:Pulse Current:Pulse Voltage Limit Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse voltage limit range, in volts, for the specified channel(s). The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit . This property is applicable only if the Output Function property is set to Pulse Current . The channel must

### Source:Pulse Current:Pulse Voltage Limit Range

Specifies the pulse voltage limit range, in volts, for the specified channel(s).

The range defines the valid values to which you can set the
 **pulse voltage limit**
 and
 **pulse bias voltage limit**
 .

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

Note

Output Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Voltage Limit Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Voltage Limit Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-queryinstrumentstatus.html language=enus -->
## TOPIC 00278: Inherent IVI Attributes:User Options:Query Instrument Status

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-queryinstrumentstatus.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-DCPower queries instrument status after each operation. Querying instrument status is useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize performance. NI-DCPower ignores status checking for particular

### Inherent IVI Attributes:User Options:Query Instrument Status

Specifies whether NI-DCPower queries instrument status after each operation.

Querying instrument status is useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize performance.

NI-DCPower ignores status checking for particular properties regardless of the setting of this property.

Use the
 [niDCPower Initialize With Independent Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_initialize_with_channels)
 VI to override this value.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Query Instrument Status |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-rangecheck.html language=enus -->
## TOPIC 00279: Inherent IVI Attributes:User Options:Range Check

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-rangecheck.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to validate property values and VI parameters. If this property is enabled, NI-DCPower validates the parameter values that you pass to NI-DCPower VIs. Range-checking parameters is useful for debugging. After you validate your program, you can set this property to FALSE to disable r

### Inherent IVI Attributes:User Options:Range Check

Specifies whether to validate property values and VI parameters.

If this property is enabled, NI-DCPower validates the parameter values that you pass to NI-DCPower VIs. Range-checking parameters is useful for debugging. After you validate your program, you can set this property to FALSE to disable range checking and maximize performance.

Use the
 [niDCPower Initialize with Independent Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_initialize_with_channels)
 VI to override the default value.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Range Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventouputterminal.html language=enus -->
## TOPIC 00280: Events:Ready For Pulse Trigger Event:Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventouputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventouputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Ready For Pulse Trigger event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Specify the output terminal using the form /Dev1/PXI_Trig0 , where Dev1 is the instrument and

### Events:Ready For Pulse Trigger Event:Output Terminal

Specifies the output terminal for exporting the Ready For Pulse Trigger event.

Note

Supported Properties by Device

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Pulse Trigger Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsepolarity.html language=enus -->
## TOPIC 00281: Events:Ready For Pulse Trigger Event:Pulse:Polarity

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsepolarity.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Ready For Pulse Trigger event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channel na

### Events:Ready For Pulse Trigger Event:Pulse:Polarity

Specifies the behavior of the Ready For Pulse Trigger event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Pulse Trigger Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Active High | 1018 | A high pulse occurs when the event is generated. The exported signal is low level both before and after the event is generated. |
| --- | --- | --- |
| Active Low | 1019 | A low pulse occurs when the event is generated. The exported signal is high level both before and after the event is generated. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsewidth.html language=enus -->
## TOPIC 00282: Events:Ready For Pulse Trigger Event:Pulse:Width

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsewidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the Ready For Pulse Trigger event, in seconds. The minimum event pulse width value for PXI Express devices is 250 ns. The maximum event pulse width value for all devices is 1.6 microseconds. This property is not supported by all devices. Refer to Supported Properties by Device

### Events:Ready For Pulse Trigger Event:Pulse:Width

Specifies the width of the Ready For Pulse Trigger event, in seconds.

The minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Pulse Trigger Event Pulse Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-recordvaluecoercions.html language=enus -->
## TOPIC 00283: Inherent IVI Attributes:User Options:Record Value Coercions

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-recordvaluecoercions.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the IVI engine records the value coercions it makes for ViInt32 and ViReal64 properties. Call the niDCPower Get Next Coercion Record VI to read and delete the earliest coercion record from the list. Use the niDCPower Initialize With Independent Channels VI to override this value. D

### Inherent IVI Attributes:User Options:Record Value Coercions

Specifies whether the IVI engine records the value coercions it makes for ViInt32 and ViReal64 properties.

Call the
 [niDCPower Get Next Coercion Record](/csh?context=nidcpower_nidcpowerviref_nidcpower_get_next_coercion_record)
 VI to read and delete the earliest coercion record from the list.

Use the
 [niDCPower Initialize With Independent Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_initialize_with_channels)
 VI to override this value.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Record Value Coercions |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-requestedpowerallocation.html language=enus -->
## TOPIC 00284: Source:Advanced:Requested Power Allocation

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-requestedpowerallocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-requestedpowerallocation.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power, in watts, to request the device to source from each active channel. This property defines the power to source from the device only if the Power Allocation Mode property is set to Manual . The power you request with this property may be incompatible with the power a given source

### Source:Advanced:Requested Power Allocation

Specifies the power, in watts, to request the device to source from each active channel.

This property defines the power to source from the device only if the
 [Power Allocation Mode](pnidcpower-powerallocationmode.html)
 property is set to
 **Manual**
 .

The power you request with this property may be incompatible with the power a given source configuration requires or the power the device can provide:

| Incompatibility | Behavior |
| --- | --- |
| Requested power < power required for source configuration | Device does not exceed the requested power NI-DCPower returns an error |
| Requested power > maximum per-channel or overall sourcing power | Device does not exceed the allowed power NI-DCPower returns an error |

Note

Note

Supported Properties by Device

**Valid Values**
 : [0, device per-channel maximum power]

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Requested Power Allocation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resetaveragebeforemeasurement.html language=enus -->
## TOPIC 00285: Measurement:Advanced:Reset Average Before Measurement

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resetaveragebeforemeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resetaveragebeforemeasurement.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement returned from any measurement call starts with a new measurement call (TRUE) or returns a measurement that has already begun or completed (FALSE). This property is not supported by all devices. Refer to Supported Properties by Device for information about supported

### Measurement:Advanced:Reset Average Before Measurement

Specifies whether the measurement returned from any measurement call starts with a new measurement call (TRUE) or returns a measurement that has already begun or completed (FALSE).

Note

Supported Properties by Device

When you set the
 [Samples to Average](pnidcpower-samplestoaverage.html)
 property in the
 [Running state](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)
 , the channel measurements might move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a session, you can force a synchronization in the running state before you run the
 [niDCPower Measure Multiple](/csh?context=nidcpower_nidcpowerviref_nidcpower_measure_multiple)
 VI. To force a synchronization in the running state, set the Reset Average Before Measurement property to TRUE, and then run the niDCPower Measure Multiple VI specifying all channels in the
 **channel name**
 parameter. You can set the Reset Average Before Measurement property to FALSE after the niDCPower Measure Multiple VI completes.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reset Average Before Measurement |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resourcedescriptor.html language=enus -->
## TOPIC 00286: Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resourcedescriptor.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the resource descriptor NI-DCPower uses to identify the resource(s) used by the NI-DCPower session. The resource name specified with the niDCPower Initialize With Independent Channels VI can include instrument(s) and/or channel(s) but does not support logical names. If you initialize NI-DC

### Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

Indicates the resource descriptor NI-DCPower uses to identify the resource(s) used by the NI-DCPower session.

The resource name specified with the niDCPower Initialize With Independent Channels VI can include instrument(s) and/or channel(s) but does not support logical names.

If you initialize NI-DCPower with a logical name using a deprecated initialize VI, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-DCPower with the resource descriptor, this property contains that value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Resource Descriptor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-revision.html language=enus -->
## TOPIC 00287: Inherent IVI Attributes:Driver Identification:Revision

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-revision.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains additional version information about NI-DCPower. Remarks The following table lists the characteristics of this property. Short Name Revision Data type cstr.png Permissions Read Only High-level VIs niDCPower Revision Query Channel-based No Instrument-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Revision

Contains additional version information about NI-DCPower.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niDCPower Revision Query |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-samplestoaverage.html language=enus -->
## TOPIC 00288: Measurement:Samples To Average

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-samplestoaverage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-samplestoaverage.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples to average when you take a measurement. Increasing the number of samples to average decreases measurement noise but increases the time required to take a measurement. Device Range of Samples to Average NI PXI-4110 and NI PXI-4130 1 to 511 NI PXI-4132 1 to 127 NI PXIe-

### Measurement:Samples To Average

Specifies the number of samples to average when you take a measurement.

Increasing the number of samples to average decreases measurement noise but increases the time required to take a measurement.

| Device | Range of Samples to Average |
| --- | --- |
| NI PXI-4110 and NI PXI-4130 | 1 to 511 |
| NI PXI-4132 | 1 to 127 |
| NI PXIe-4154 | 1 to 65,535 |
| All other supported instruments | 1 |

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Samples To Average |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-selfcalibrationpersistence.html language=enus -->
## TOPIC 00289: Advanced:Self-Calibration Persistence

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-selfcalibrationpersistence.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-selfcalibrationpersistence.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the values calculated during self-calibration should be written to hardware to be used until the next self-calibration or only used until the niDCPower Reset Device VI is called or the machine is powered down. This property affects the behavior of the niDCPower Cal Self Calibrate V

### Advanced:Self-Calibration Persistence

Specifies whether the values calculated during self-calibration should be written to hardware to be used until the next self-calibration or only used until the
 [niDCPower Reset Device](/csh?context=nidcpower_nidcpowerviref_nidcpower_reset_device)
 VI is called or the machine is powered down.

This property affects the behavior of the
 [niDCPower Cal Self Calibrate](/csh?context=nidcpower_nidcpowerviref_nidcpower_cal_self_calibrate)
 VI. When set to
 **Keep in Memory**
 , the values calculated by the niDCPower Cal Self Calibrate VI are used in the existing session, as well as in all further sessions until you call the niDCPower Reset Device VI or restart the machine. When you set this property to
 **Write to EEPROM**
 , the values calculated by the niDCPower Cal Self Calibrate VI are written to hardware and used in the existing session and in all subsequent sessions until another call to the niDCPower Cal Self Calibrate VI is made.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Self-Cal Persistence |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | Yes |
| Resettable | No |

| Keep in Memory | 1045 | Keep new self-calibration values in memory only. |
| --- | --- | --- |
| Write to EEPROM | 1046 | Write new self-calibration values to hardware. Refer to your device documentation for more information about the implications of frequent writes to the EEPROM. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sense.html language=enus -->
## TOPIC 00290: Measurement:Sense

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sense.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sense.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects either local or remote sensing of the output voltage for the specified channel(s). NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. Default Value :Refer to Supported Properties by D

### Measurement:Sense

Selects either local or remote sensing of the output voltage for the specified channel(s).

Note

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sense |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Sense |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Local | 1008 | Local sensing is selected. |
| --- | --- | --- |
| Remote | 1009 | Remote sensing is selected. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeedge.html language=enus -->
## TOPIC 00291: Triggers:Sequence Advance Trigger:Digital Edge:Edge

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeedge.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Sequence trigger to assert on the rising or falling edge. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by

### Triggers:Sequence Advance Trigger:Digital Edge:Edge

Specifies whether to configure the Sequence trigger to assert on the rising or falling edge.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Advance Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Sequence Advance Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Rising | 1016 | Asserts the trigger on the rising edge of the digital signal. |
| --- | --- | --- |
| Falling | 1017 | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeinputterminal.html language=enus -->
## TOPIC 00292: Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeinputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Sequence Advance trigger. This property is used only when the Sequence Advance Trigger Type property is set to Digital Edge . This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. You can s

### Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal

Specifies the input terminal for the Sequence Advance trigger. This property is used only when the
 [Sequence Advance Trigger Type](/csh?topicname=pnidcpower-sequenceadvancetriggertype.html)
 property is set to
 **Digital Edge**
 .

Note

Supported Properties by Device

You can specify any valid input terminal for this property, and the driver will create a route between it and the Sequence Advance Trigger terminal at Commit. Valid terminals are listed in Measurement & Automation Explorer under the
 **Device Routes**
 tab. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the input terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be
 /Dev2/Engine0/SourceCompleteEvent
 , where
 Engine0
 is channel 0.

Note

/Dev1/PXI_Trig0

Dev1

PXI_Trig0

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Advance Trigger Digital Edge - Input Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Sequence Advance Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggertype.html language=enus -->
## TOPIC 00293: Triggers:Sequence Advance Trigger:Trigger Type

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggertype.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Sequence Advance trigger. Refer to the Configure Triggers and Events topic in your instrument user manual for more information about triggers and events. This property is not supported by all devices. Refer to Supported Properties by Device for information about support

### Triggers:Sequence Advance Trigger:Trigger Type

Specifies the behavior of the Sequence Advance trigger.

Refer to the *Configure Triggers and Events* topic in your instrument user manual for more information about triggers and events.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Advance Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Sequence Advance Trigger, niDCPower Configure Software Edge Sequence Advance Trigger, niDCPower Disable Sequence Advance Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Digital Edge | 1014 | The data operation starts when a digital edge is detected. |
| --- | --- | --- |
| Software Edge | 1015 | The data operation starts when a software trigger occurs. |
| None | 1012 | No trigger is configured. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventouputterminal.html language=enus -->
## TOPIC 00294: Events:Sequence Engine Done Event:Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventouputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventouputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Sequence Engine Done Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Specify the output terminal using the form /Dev1/PXI_Trig0 , where Dev1 is the instrume

### Events:Sequence Engine Done Event:Output Terminal

Specifies the output terminal for exporting the Sequence Engine Done Complete event.

Note

Supported Properties by Device

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Engine Done Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventoutputbehavior.html language=enus -->
## TOPIC 00295: Events:Sequence Engine Done Event:Output Behavior

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventoutputbehavior.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior for exporting the Sequence Engine Done event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To speci

### Events:Sequence Engine Done Event:Output Behavior

Specifies the output behavior for exporting the Sequence Engine Done event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Engine Done Event Output Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Pulse Event Output | 1147 | A single 250ns pulse is transmitted. |
| --- | --- | --- |
| Toggle Event Output | 1148 | The output level toggles between low and high, The initial output level is determined by Sequence Engine Done Event Toggle Initial State . |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsepolarity.html language=enus -->
## TOPIC 00296: Events:Sequence Engine Done Event:Pulse:Polarity

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsepolarity.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Sequence Engine Done event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channel name

### Events:Sequence Engine Done Event:Pulse:Polarity

Specifies the behavior of the Sequence Engine Done event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Engine Done Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Active High | 1018 | A high pulse occurs when the event is generated. The exported signal is low level both before and after the event is generated. |
| --- | --- | --- |
| Active Low | 1019 | A low pulse occurs when the event is generated. The exported signal is high level both before and after the event is generated. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsewidth.html language=enus -->
## TOPIC 00297: Events:Sequence Engine Done Event:Pulse:Width

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsewidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the Sequence Engine Done event, in seconds. The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns. The maximum event pulse width value for all devices is 1.6 microseconds. This property is n

### Events:Sequence Engine Done Event:Pulse:Width

Specifies the width of the Sequence Engine Done event, in seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Engine Done Event Pulse Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventtoggleinitialstate.html language=enus -->
## TOPIC 00298: Events:Sequence Engine Done Event:Toggle:Initial State

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventtoggleinitialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventtoggleinitialstate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the Sequence Engine Done event if you set the Sequence Engine Done Event Output Behavior to Toggle Event Output. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supp

### Events:Sequence Engine Done Event:Toggle:Initial State

Specifies the initial state of the Sequence Engine Done event if you set the [Sequence Engine Done Event Output Behavior](/csh?topicname=pnidcpower-sequenceenginedoneeventoutputbehavior.html) to **Toggle Event Output**.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Engine Done Event Toggle Initial State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Initial State Low | 1149 | The output is set to low at session commit. For operation in Single Point source mode, the output switches to high when the event occurs during the acquisition. The output then switches to low if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to high the first time an event occurs during the acquisition. It then switches to low the second time an event occurs. This pattern repeats for any subsequent event occurrences. |
| --- | --- | --- |
| Initial State High | 1150 | The output is set to high at session commit. For operation in Single Point source mode, the output switches to low when the event occurs during the acquisition. The output then switches to high if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to low the first time an event occurs during the acquisition. It then switches to high the second time an event occurs. This pattern repeats for any subsequent event occurrences. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputbehavior.html language=enus -->
## TOPIC 00299: Events:Sequence Iteration Complete Event:Output Behavior

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputbehavior.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior for exporting the Sequence Iteration Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. T

### Events:Sequence Iteration Complete Event:Output Behavior

Specifies the output behavior for exporting the Sequence Iteration Complete event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Iteration Complete Event Output Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Pulse Event Output | 1147 | A single 250ns pulse is transmitted. |
| --- | --- | --- |
| Toggle Event Output | 1148 | The output level toggles between low and high, The initial output level is determined by Sequence Iteration Complete Event Toggle Initial State . |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputterminal.html language=enus -->
## TOPIC 00300: Events:Sequence Iteration Complete Event:Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Sequence Iteration Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Specify the output terminal using the form /Dev1/PXI_Trig0 , where Dev1 is the instrument

### Events:Sequence Iteration Complete Event:Output Terminal

Specifies the output terminal for exporting the Sequence Iteration Complete event.

Note

Supported Properties by Device

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Iteration Complete Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsepolarity.html language=enus -->
## TOPIC 00301: Events:Sequence Iteration Complete Event:Pulse:Polarity

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsepolarity.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Sequence Iteration Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channe

### Events:Sequence Iteration Complete Event:Pulse:Polarity

Specifies the behavior of the Sequence Iteration Complete event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Iteration Complete Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Active High | 1018 | A high pulse occurs when the event is generated. The exported signal is low level both before and after the event is generated. |
| --- | --- | --- |
| Active Low | 1019 | A low pulse occurs when the event is generated. The exported signal is high level both before and after the event is generated. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsewidth.html language=enus -->
## TOPIC 00302: Events:Sequence Iteration Complete Event:Pulse:Width

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsewidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the Sequence Iteration Complete event, in seconds. The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns. The maximum event pulse width value for all devices is 1.6 microseconds. This proper

### Events:Sequence Iteration Complete Event:Pulse:Width

Specifies the width of the Sequence Iteration Complete event, in seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Iteration Complete Event Pulse Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventtoggleinitialstate.html language=enus -->
## TOPIC 00303: Events:Sequence Iteration Complete Event:Toggle:Initial State

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventtoggleinitialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventtoggleinitialstate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the Sequence Iteration Complete event if you set the Sequence Iteration Complete Event Output Behavior to Toggle Event Output. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value

### Events:Sequence Iteration Complete Event:Toggle:Initial State

Specifies the initial state of the Sequence Iteration Complete event if you set the [Sequence Iteration Complete Event Output Behavior](/csh?topicname=pnidcpower-sequenceiterationcompleteeventoutputbehavior.html) to **Toggle Event Output**.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Iteration Complete Event Toggle Initial State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Initial State Low | 1149 | The output is set to low at session commit. For operation in Single Point source mode, the output switches to high when the event occurs during the acquisition. The output then switches to low if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to high the first time an event occurs during the acquisition. It then switches to low the second time an event occurs. This pattern repeats for any subsequent event occurrences. |
| --- | --- | --- |
| Initial State High | 1150 | The output is set to high at session commit. For operation in Single Point source mode, the output switches to low when the event occurs during the acquisition. The output then switches to high if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to low the first time an event occurs during the acquisition. It then switches to high the second time an event occurs. This pattern repeats for any subsequent event occurrences. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcount.html language=enus -->
## TOPIC 00304: Source:Advanced:Sequence Loop Count

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcount.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of times a sequence is run after initiation. Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence loop count. This property is not supported by all devices. Refer to Supported Properties by Device for informati

### Source:Advanced:Sequence Loop Count

Specifies the number of times a sequence is run after initiation.

Refer to the
 [Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)
 topic in the
 *NI DC Power Supplies and SMUs Help*
 for more information about the sequence loop count.

Note

Supported Properties by Device

Sequence Loop Count Is Finite

**Valid Range**

- For all supported instruments, 1 to 2147483647.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Loop Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcountisfinite.html language=enus -->
## TOPIC 00305: Source:Advanced:Sequence Loop Count Is Finite

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcountisfinite.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcountisfinite.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a sequence should repeat indefinitely. Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about infinite sequencing. This property is not supported by all devices. Refer to Supported Properties by Device for information about supp

### Source:Advanced:Sequence Loop Count Is Finite

Specifies whether a sequence should repeat indefinitely.

Refer to the
 [Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)
 topic in the
 *NI DC Power Supplies and SMUs Help*
 for more information about infinite sequencing.

Note

Supported Properties by Device

Sequence Loop Count

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Loop Count Is Finite |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatime.html language=enus -->
## TOPIC 00306: Source:Advanced:Sequence Step Delta Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time, in seconds, between the start of two consecutive steps in a sequence. You can specify this property as one of the advanced sequence properties when calling the niDCPower Create Advanced Sequence With Channels VI. In this case, this property specifies the amount of time

### Source:Advanced:Sequence Step Delta Time

Specifies the amount of time, in seconds, between the start of two consecutive steps in a sequence.

You can specify this property as one of the
 **advanced sequence properties**
 when calling the
 [niDCPower Create Advanced Sequence With Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_create_advanced_sequence)
 VI. In this case, this property specifies the amount of time between the start of the active step and the start of the next step.

Note

Supported Properties by Device

This property is applicable only if the
 [Sequence Step dt Enabled](pnidcpower-sequencestepdeltatimeenabled.html)
 property is set to TRUE. Refer to the
 [Sequence Step dt Enabled](pnidcpower-sequencestepdeltatimeenabled.html)
 property for more information about the settings with which this property is compatible. This property does not apply to the last step of the last iteration of a sequence.

Note

Source Delay

Measure When

Automatically After Source Complete

NI recommends that you configure other attributes in the Commit step when configuring Sequence Step dt using the
 [niDCPower_Create_Advanced_Sequence_Commit_Step_With_Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_create_advanced_sequence_step_(poly))
 function to reduce the setup time in the first step of sequence.

Note

Sequence Step Delta Time Timing Issues

**Valid Values**

| Device | Values |
| --- | --- |
| PXIe-4135, PXIe-4136/4137, PXIe-4138/4139 | [12.5 μs, 60 s] |
| PXIe-4140/4141, PXIe-4142/4143, PXIe-4144/4145 | [10 μs, 60 s] |
| PXIe-4147 | [10 μs, 26.512 s] |

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

| Device | Selected Value | Resolution |
| --- | --- | --- |
| PXIe-4135, PXIe-4136/4137, PXIe-4138/4139 | [12.5 μs, 21.4748 s] | 10 ns |
| PXIe-4135, PXIe-4136/4137, PXIe-4138/4139 | (21.4748 s, 60 s] | 10 μs |
| PXIe-4140/4141, PXIe-4142/4143, PXIe-4144/4145 | [10 μs, 233.0169 ms] | 27.7778 ns |
| PXIe-4140/4141, PXIe-4142/4143, PXIe-4144/4145 | (233.0169 ms, 60 s] | 10 μs |
| PXIe-4147 | [10 μs, 26.512 s] | 6.17 ns |

**Related Topics:**

[Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)

[Advanced Sequencing](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Step dt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatimeenabled.html language=enus -->
## TOPIC 00307: Source:Advanced:Sequence Step Delta Time Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatimeenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatimeenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Sequence Step dt property is enabled (TRUE) or disabled (FALSE). When this property is set to TRUE, you can set the Sequence Step dt property to control the time between consecutive steps in the sequence. This property is not supported by all devices. Refer to Supported Propert

### Source:Advanced:Sequence Step Delta Time Enabled

Specifies whether the
 [Sequence Step dt](/csh?topicname=pnidcpower-sequencestepdeltatime.html)
 property is enabled (TRUE) or disabled (FALSE).

When this property is set to TRUE, you can set the
 [Sequence Step dt](pnidcpower-sequencestepdeltatime.html)
 property to control the time between consecutive steps in the sequence.

Note

Supported Properties by Device

This property is applicable only if the
 [Source Mode](pnidcpower-sourcemode.html)
 property is set to
 **Sequence**
 and may be set to TRUE only if:

- The
 Source Trigger Type 
 property is set to
 None 
 ;
- The
 Sequence Advance Trigger Type 
 property is set to
 None 
 ; and
- The
 Output Function 
 property is set to
 DC Voltage 
 or
 DC Current 
 .

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

**Related Topics:**

[Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)

[Advanced Sequencing](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequence Step dt Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-serialnumber.html language=enus -->
## TOPIC 00308: Inherent IVI Attributes:Instrument Identification:Serial Number

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-serialnumber.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the serial number information for the device you are currently using. To specify an instrument name when accessing this property, you must first initialize the session using the Initialize With Independent Channels VI. Remarks The following table lists the characteristics of this property.

### Inherent IVI Attributes:Instrument Identification:Serial Number

Contains the serial number information for the device you are currently using.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Serial Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | Yes |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeedge.html language=enus -->
## TOPIC 00309: Triggers:Shutdown Trigger:Digital Edge:Edge

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeedge.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Shutdown trigger to assert on the rising or falling edge. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by

### Triggers:Shutdown Trigger:Digital Edge:Edge

Specifies whether to configure the Shutdown trigger to assert on the rising or falling edge.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Shutdown Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Rising | 1016 | Asserts the trigger on the rising edge of the digital signal. |
| --- | --- | --- |
| Falling | 1017 | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeinputterminal.html language=enus -->
## TOPIC 00310: Triggers:Shutdown Trigger:Digital Edge:Input Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeinputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Shutdown trigger. This property is used only when the Shutdown Trigger Type property is set to Digital Edge . This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. You can specify any valid

### Triggers:Shutdown Trigger:Digital Edge:Input Terminal

Specifies the input terminal for the Shutdown trigger. This property is used only when the
 [Shutdown Trigger Type](/csh?topicname=pnidcpower-shutdowntriggertype.html)
 property is set to
 **Digital Edge**
 .

Note

Supported Properties by Device

You can specify any valid input terminal for this property, and the driver will create a route between it and the Shutdown Trigger terminal at Commit. Valid terminals are listed in Measurement & Automation Explorer under the
 **Device Routes**
 tab.

Specify the input terminal using the form
 /Dev1/Engine0/PXI_Trig0
 , where
 Dev1
 is the instrument,
 Engine0
 is channel 0, and
 PXI_Trig0
 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be
 /Dev2/Engine0/SourceCompleteEvent
 .

Note

/Dev1/PXI_Trig0

Dev1

PXI_Trig0

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Shutdown Trigger Digital Edge - Input Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggertype.html language=enus -->
## TOPIC 00311: Triggers:Shutdown Trigger:Trigger Type

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggertype.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Shutdown trigger. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. If you specify a channel name when a

### Triggers:Shutdown Trigger:Trigger Type

Specifies the behavior of the Shutdown trigger.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Shutdown Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Digital Edge | 1014 | The data operation starts when a digital edge is detected. |
| --- | --- | --- |
| Software Edge | 1015 | The data operation starts when a software trigger occurs. |
| None | 1012 | No trigger is configured. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-simulate.html language=enus -->
## TOPIC 00312: Inherent IVI Attributes:User Options:Simulate

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-simulate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to simulate NI-DCPower I/O operations. TRUE specifies that operation is simulated. Default Value :Refer to Supported Properties by Device for the default value by device. Remarks The following table lists the characteristics of this property. Short Name Simulate Data type cbool.png

### Inherent IVI Attributes:User Options:Simulate

Specifies whether to simulate NI-DCPower I/O operations. TRUE specifies that operation is simulated.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Simulate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputbehavior.html language=enus -->
## TOPIC 00313: Events:Source Complete Event:Output Behavior

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputbehavior.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior for exporting the Source Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a

### Events:Source Complete Event:Output Behavior

Specifies the output behavior for exporting the Source Complete event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Complete Event Output Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Pulse Event Output | 1147 | A single 250ns pulse is transmitted. |
| --- | --- | --- |
| Toggle Event Output | 1148 | The output level toggles between low and high, The initial output level is determined by Source Complete Event Toggle Initial State . |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputterminal.html language=enus -->
## TOPIC 00314: Events:Source Complete Event:Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Source Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Specify the output terminal using the form /Dev1/PXI_Trig0 , where Dev1 is the instrument and PXI_Tri

### Events:Source Complete Event:Output Terminal

Specifies the output terminal for exporting the Source Complete event.

Note

Supported Properties by Device

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Complete Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsepolarity.html language=enus -->
## TOPIC 00315: Events:Source Complete Event:Pulse:Polarity

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsepolarity.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Source Complete event. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This property is not supported by all devices. Refer to Supported Properties by Device

### Events:Source Complete Event:Pulse:Polarity

Specifies the behavior of the Source Complete event.

Note

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Complete Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Active High | 1018 | A high pulse occurs when the event is generated. The exported signal is low level both before and after the event is generated. |
| --- | --- | --- |
| Active Low | 1019 | A low pulse occurs when the event is generated. The exported signal is high level both before and after the event is generated. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsewidth.html language=enus -->
## TOPIC 00316: Events:Source Complete Event:Pulse:Width

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsewidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the Source Complete event, in seconds. The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns. The maximum event pulse width value for all devices is 1.6 microseconds. NI-DCPower uses the ter

### Events:Source Complete Event:Pulse:Width

Specifies the width of the Source Complete event, in seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

Note

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Complete Event Pulse Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventtoggleinitialstate.html language=enus -->
## TOPIC 00317: Events:Source Complete Event:Toggle:Initial State

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventtoggleinitialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventtoggleinitialstate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the Source Complete event if you set the Source Complete Event Output Behavior to Toggle Event Output. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This p

### Events:Source Complete Event:Toggle:Initial State

Specifies the initial state of the Source Complete event if you set the [Source Complete Event Output Behavior](/csh?topicname=pnidcpower-sourcecompleteeventoutputbehavior.html) to **Toggle Event Output**.

Note

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Complete Event Toggle Initial State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Initial State Low | 1149 | The output is set to low at session commit. For operation in Single Point source mode, the output switches to high when the event occurs during the acquisition. The output then switches to low if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to high the first time an event occurs during the acquisition. It then switches to low the second time an event occurs. This pattern repeats for any subsequent event occurrences. |
| --- | --- | --- |
| Initial State High | 1150 | The output is set to high at session commit. For operation in Single Point source mode, the output switches to low when the event occurs during the acquisition. The output then switches to high if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to low the first time an event occurs during the acquisition. It then switches to high the second time an event occurs. This pattern repeats for any subsequent event occurrences. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcedelay.html language=enus -->
## TOPIC 00318: Source:Advanced:Source Delay

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcedelay.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the Measure When property is set to Automatically After Source Complete . Refer to the Single Point source mode and Sequence source mode topics in the NI DC Power Supplies and SMUs Help

### Source:Advanced:Source Delay

Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the
 [Measure When](/csh?topicname=pnidcpower-measurewhen.html)
 property is set to
 **Automatically After Source Complete**
 .

Refer to the
 [Single Point source mode](/csh?context=nidcpower_ni_dc_power_supplies_help_singlept)
 and
 [Sequence source mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)
 topics in the
 *NI DC Power Supplies and SMUs Help*
 for more information.

Note

Note

Supported Properties by Device

**Valid Values:**

- For the PXIe-4051, 0 to 39 seconds.
- For the PXIe-4150/4151, 0 to 42 seconds.
- For the PXI-4132, PXIe-4135/4136/4137/4138/4139, and PXIe-4140/4141/4142/4143/4144/4145/4154, 0 to 167 seconds.
- For the PXIe-4147, 0 to 26.5 seconds.
- For the PXIe-4162/4163 and PXIe-4190, 0 to 23 seconds.

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcemode.html language=enus -->
## TOPIC 00319: Source:Source Mode

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcemode.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to run a single output point or a sequence. Refer to the Single Point source mode and Sequence source mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes. Default Value : Refer to Supported Properties by Device for the default value by devi

### Source:Source Mode

Specifies whether to run a single output point or a sequence. Refer to the
 [Single Point source mode](/csh?context=nidcpower_ni_dc_power_supplies_help_singlept)
 and
 [Sequence source mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)
 topics in the
 *NI DC Power Supplies and SMUs Help*
 for more information about source modes.

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Source Mode With Channels |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Single Point | 1020 | The source unit applies a single source configuration. |
| --- | --- | --- |
| Sequence | 1021 | The source unit sequentially applies a list of voltage or current configurations. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeedge.html language=enus -->
## TOPIC 00320: Triggers:Source Trigger:Digital Edge:Edge

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeedge.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Source trigger to assert on the rising or falling edge. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This property is not supported by all devices. Re

### Triggers:Source Trigger:Digital Edge:Edge

Specifies whether to configure the Source trigger to assert on the rising or falling edge.

Note

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Source Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Rising | 1016 | Asserts the trigger on the rising edge of the digital signal. |
| --- | --- | --- |
| Falling | 1017 | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeinputterminal.html language=enus -->
## TOPIC 00321: Triggers:Source Trigger:Digital Edge:Input Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeinputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Source trigger. This property is used only when the Source Trigger Type property is set to Digital Edge . NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectivel

### Triggers:Source Trigger:Digital Edge:Input Terminal

Specifies the input terminal for the Source trigger. This property is used only when the
 [Source Trigger Type](/csh?topicname=pnidcpower-sourcetriggertype.html)
 property is set to
 **Digital Edge**
 .

Note

Note

Supported Properties by Device

You can specify any valid input terminal for this property, and the driver will create a route between it and the Source Trigger terminal at Commit. Valid terminals are listed in Measurement & Automation Explorer under the
 **Device Routes**
 tab. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the input terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be
 /Dev2/Engine0/SourceCompleteEvent
 , where
 Engine0
 is channel 0.

Note

/Dev1/PXI_Trig0

Dev1

PXI_Trig0

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Trigger Digital Edge - Input Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Source Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggertype.html language=enus -->
## TOPIC 00322: Triggers:Source Trigger:Trigger Type

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggertype.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Source trigger. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This property is not supported by all devices. Refer to Supported Properties by Device for inf

### Triggers:Source Trigger:Trigger Type

Specifies the behavior of the Source trigger.

Note

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Source Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Source Trigger, niDCPower Configure Software Edge Source Trigger, niDCPower Disable Source Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Digital Edge | 1014 | The data operation starts when a digital edge is detected. |
| --- | --- | --- |
| Software Edge | 1015 | The data operation starts when a software trigger occurs. |
| None | 1012 | No trigger is configured. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeedge.html language=enus -->
## TOPIC 00323: Triggers:Start Trigger:Digital Edge:Edge

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeedge.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Start trigger to assert on the rising or falling edge. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by de

### Triggers:Start Trigger:Digital Edge:Edge

Specifies whether to configure the Start trigger to assert on the rising or falling edge.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Start Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Rising | 1016 | Asserts the trigger on the rising edge of the digital signal. |
| --- | --- | --- |
| Falling | 1017 | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeinputterminal.html language=enus -->
## TOPIC 00324: Triggers:Start Trigger:Digital Edge:Input Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeinputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Start trigger. This property is used only when the Start Trigger Type property is set to Digital Edge . This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. You can specify any valid termi

### Triggers:Start Trigger:Digital Edge:Input Terminal

Specifies the input terminal for the Start trigger. This property is used only when the
 [Start Trigger Type](/csh?topicname=pnidcpower-starttriggertype.html)
 property is set to
 **Digital Edge**
 .

Note

Supported Properties by Device

You can specify any valid terminal for this property, and the driver will create a route between it and the Start Trigger terminal at Commit. Valid terminals are listed in Measurement & Automation Explorer under the
 **Device Routes**
 tab. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the input terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be
 /Dev2/Engine0/SourceCompleteEvent
 , where
 Engine0
 is channel 0.

Note

/Dev1/PXI_Trig0

Dev1

PXI_Trig0

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge - Input Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Start Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggertype.html language=enus -->
## TOPIC 00325: Triggers:Start Trigger:Trigger Type

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggertype.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Start trigger. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channel name when accessin

### Triggers:Start Trigger:Trigger Type

Specifies the behavior of the Start trigger.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Start Trigger, niDCPower Configure Software Edge Start Trigger, niDCPower Disable Start Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Digital Edge | 1014 | The data operation starts when a digital edge is detected. |
| --- | --- | --- |
| Software Edge | 1015 | The data operation starts when a software trigger occurs. |
| None | 1012 | No trigger is configured. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-supportedinstrumentmodels.html language=enus -->
## TOPIC 00326: Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-supportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-supportedinstrumentmodels.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a comma-separated (,) list of supported NI-DCPower device models. Remarks The following table lists the characteristics of this property. Short Name Supported Instrument Models Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Instrument-based No Resettable No

### Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

Contains a comma-separated (,) list of supported NI-DCPower device models.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Supported Instrument Models |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-transientresponse.html language=enus -->
## TOPIC 00327: Source:Transient Response

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-transientresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-transientresponse.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help for more information about transient response. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Val

### Source:Transient Response

Specifies the transient response. Refer to the
 Transient Response topic in the
 *NI DC Power Supplies and SMUs Help*
 for more information about transient response.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Transient Response |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Slow | 1041 | Slow transient response time. |
| --- | --- | --- |
| Normal | 1038 | Normal transient response time. |
| Fast | 1039 | Fast transient response time. |
| Custom | 1042 | Custom transient response time. If you select this value, you can then specify values for the Voltage Gain Bandwidth , Voltage Compensation Frequency , Voltage Pole-Zero Ratio , Current Gain Bandwidth , Current Compensation Frequency , and Current Pole-Zero Ratio properties. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagecompensationfrequency.html language=enus -->
## TOPIC 00328: Source:Custom Transient Response:Voltage:Compensation Frequency

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagecompensationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagecompensationfrequency.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which a pole-zero pair is added to the system when the channel is in Constant Voltage mode. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the

### Source:Custom Transient Response:Voltage:Compensation Frequency

The frequency at which a pole-zero pair is added to the system when the channel is in
 Constant Voltage mode.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Compensation Freq |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagegainbandwidth.html language=enus -->
## TOPIC 00329: Source:Custom Transient Response:Voltage:Gain Bandwidth

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagegainbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagegainbandwidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Voltage mode. This property is not supported by all devices. Refer to Supported Properties by Device for information about supp

### Source:Custom Transient Response:Voltage:Gain Bandwidth

The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in
 Constant Voltage mode.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage GBW |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevel.html language=enus -->
## TOPIC 00330: Source:DC Voltage:Voltage Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s). This property is applicable only if the Output Function property is set to DC Voltage . The channel must be enabled for the specified voltage level to take effect. Refer to the Output Enabled pro

### Source:DC Voltage:Voltage Level

Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage**
 .

Note

Output Enabled

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Voltage Level Range](pnidcpower-voltagelevelrange.html)
 property.

**Related topics:**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Voltage Level |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelautorange.html language=enus -->
## TOPIC 00331: Source:DC Voltage:Voltage Level Autorange

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelautorange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channel(s). If you set this property to On , NI-DCPower ignores any changes you make to the Voltage Level Range property. If you change the Voltage Level Autorange property

### Source:DC Voltage:Voltage Level Autorange

Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channel(s).

If you set this property to
 **On**
 , NI-DCPower ignores any changes you make to the
 [Voltage Level Range](pnidcpower-voltagelevelrange.html)
 property. If you change the Voltage Level Autorange property from
 **On**
 to
 **Off**
 , NI-DCPower retains the last value that the
 [Voltage Level Range](pnidcpower-voltagelevelrange.html)
 property was set to (or the default value if it was never set) and uses that value as the voltage level range.

Refer to the
 [Voltage Level Range](pnidcpower-voltagelevelrange.html)
 property for information about which range NI-DCPower automatically selects.

The Voltage Level Autorange property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage**
 .

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Level Autorange |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 0 | NI-DCPower does not automatically select the voltage level range. |
| --- | --- | --- |
| On | 1 | NI-DCPower automatically selects the voltage level range. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelrange.html language=enus -->
## TOPIC 00332: Source:DC Voltage:Voltage Level Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level range, in volts, for the specified channel(s). The range defines the valid values to which the voltage level can be set. Use the Voltage Level Autorange property to enable automatic selection of the voltage level range. The Voltage Level Range property is applicable only

### Source:DC Voltage:Voltage Level Range

Specifies the voltage level range, in volts, for the specified channel(s).

The range defines the valid values to which the voltage level can be set. Use the
 [Voltage Level Autorange](pnidcpower-voltagelevelautorange.html)
 property to enable automatic selection of the voltage level range.

The Voltage Level Range property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage**
 .

Note

Output Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Level Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Voltage Level Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimit.html language=enus -->
## TOPIC 00333: Source:DC Current:Voltage Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level on the specified channels. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. This property is applicable only if the Output Fun

### Source:DC Current:Voltage Limit

Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level on the specified channels. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

**Valid Values:**
 The valid values for this property are defined by the values to which the
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 is set.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Voltage Limit |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitautorange.html language=enus -->
## TOPIC 00334: Source:DC Current:Voltage Limit Autorange

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitautorange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for the specified channel(s). If you set this property to On , NI-DCPower ignores any changes you make to the Voltage Limit Range property. If you change the Voltage Limit Autorange property

### Source:DC Current:Voltage Limit Autorange

Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for the specified channel(s).

If you set this property to
 **On**
 , NI-DCPower ignores any changes you make to the
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 property. If you change the Voltage Limit Autorange property from
 **On**
 to
 **Off**
 , NI-DCPower retains the last value that the
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 property was set to (or the default value if it was never set) and uses that value as the voltage limit range.

Refer to the
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 property for information about which range NI-DCPower automatically selects.

The Voltage Limit Autorange property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 .

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Limit Autorange |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 0 | NI-DCPower does not automatically select the voltage limit range. |
| --- | --- | --- |
| On | 1 | NI-DCPower automatically selects the voltage limit range. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimithigh.html language=enus -->
## TOPIC 00335: Source:DC Current:Voltage Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum voltage, in volts, that the output can produce when generating the desired current on the specified channel(s). This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property is set to DC Current . You must also

### Source:DC Current:Voltage Limit High

Specifies the maximum voltage, in volts, that the output can produce when generating the desired current on the specified channel(s).

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 .

You must also specify a
 [Voltage Limit Low](pnidcpower-voltagelimitlow.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [1% of
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 ,
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitlow.html language=enus -->
## TOPIC 00336: Source:DC Current:Voltage Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum voltage, in volts, that the output can produce when generating the desired current on the specified channel(s). This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property is set to DC Current . You must also

### Source:DC Current:Voltage Limit Low

Specifies the minimum voltage, in volts, that the output can produce when generating the desired current on the specified channel(s).

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 .

You must also specify a
 [Voltage Limit High](pnidcpower-voltagelimithigh.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [-
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 , -1% of
 [Voltage Limit Range](pnidcpower-voltagelimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitrange.html language=enus -->
## TOPIC 00337: Source:DC Current:Voltage Limit Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage limit range, in volts, for the specified channel(s). The range defines the valid values to which the voltage limit can be set. Use the Voltage Limit Autorange property to enable automatic selection of the voltage limit range. The Voltage Limit Range property is applicable only

### Source:DC Current:Voltage Limit Range

Specifies the voltage limit range, in volts, for the specified channel(s).

The range defines the valid values to which the voltage limit can be set. Use the
 [Voltage Limit Autorange](pnidcpower-voltagelimitautorange.html)
 property to enable automatic selection of the voltage limit range.

The Voltage Limit Range property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 .

Note

Output Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Limit Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Voltage Limit Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagepolezeroratio.html language=enus -->
## TOPIC 00338: Source:Custom Transient Response:Voltage:Pole-Zero Ratio

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagepolezeroratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagepolezeroratio.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ratio of the pole frequency to the zero frequency when the channel is in Constant Voltage mode. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value : Refer to Supported Properties by Device for the default

### Source:Custom Transient Response:Voltage:Pole-Zero Ratio

The ratio of the pole frequency to the zero frequency when the channel is in
 Constant Voltage mode.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voltage Pole-Zero Ratio |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4051.html language=enus -->
## TOPIC 00339: Properties Supported by the PXIe-4051

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4051.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4051.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4051 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4051 Supports Advanced Sequence Active Channel "" Advanced:Auxiliary Power Source

### Properties Supported by the PXIe-4051

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4051 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4051 | Supports Advanced Sequence |
| --- | --- | --- |
| Active Channel | "" |  |
| Advanced:Auxiliary Power Source Available | N/A |  |
| Advanced:Interlock Input Open |  |  |
| Advanced:Isolation State |  |  |
| Advanced:Power Source |  |  |
| Advanced:Power Source In Use |  |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM |  |
| Device Specific:LCR:Cable Length |  |  |
| Events:Measure Complete Event:Event Delay | 0 s |  |
| Events:Measure Complete Event:Output Behavior | Pulse Event Output[2] |  |
| Events:Measure Complete Event:Output Terminal | "" |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High[2] |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns[2] |  |
| Events:Measure Complete Event:Toggle:Initial State | Initial State Low[2] |  |
| Events:Pulse Complete Event:Output Terminal |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |
| Events:Sequence Engine Done Event:Output Behavior | Pulse Event Output[2] |  |
| Events:Sequence Engine Done Event:Output Terminal | "" |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High[2] |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns[2] |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | Initial State Low[2] |  |
| Events:Sequence Iteration Complete Event:Output Behavior | Pulse Event Output[2] |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High[2] |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns[2] |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | Initial State Low[2] |  |
| Events:Source Complete Event:Output Behavior | Pulse Event Output[2] |  |
| Events:Source Complete Event:Output Terminal | "" |  |
| Events:Source Complete Event:Pulse:Polarity | Active High[2] |  |
| Events:Source Complete Event:Pulse:Width | 250 ns[2] |  |
| Events:Source Complete Event:Toggle:Initial State | Initial State Low[2] |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |  |
| Inherent IVI Attributes:User Options:Cache | TRUE |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |
| LCR:AC Stimulus:Frequency |  |  |
| LCR:AC Stimulus:Function |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |
| LCR:Compensation:Load:Enabled |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |
| LCR:Compensation:Open:Conductance |  |  |
| LCR:Compensation:Open:Enabled |  |  |
| LCR:Compensation:Open:Susceptance |  |  |
| LCR:Compensation:Short:Enabled |  |  |
| LCR:Compensation:Short:Reactance |  |  |
| LCR:Compensation:Short:Resistance |  |  |
| LCR:Custom Measurement Time |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |
| LCR:DC Bias:Current Level |  |  |
| LCR:DC Bias:Source |  |  |
| LCR:DC Bias:Voltage Level |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |
| LCR:Impedance Range:Impedance Range |  |  |
| LCR:Instrument Mode | E-Load[2] |  |
| LCR:Measurement Time |  |  |
| LCR:Source Delay Mode |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |  |
| Measurement:Advanced:Autorange Behavior |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |  |
| Measurement:Advanced:Autorange Threshold Mode |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal |  |
| Measurement:Advanced:Measure Buffer Size | 1800130 |  |
| Measurement:Advanced:Measure When | On Demand[1] |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |
| Measurement:Aperture Time | 0.01666666 s |  |
| Measurement:Aperture Time Auto Mode |  |  |
| Measurement:Aperture Time Units | Seconds |  |
| Measurement:Auto Zero | Off[2] |  |
| Measurement:Autorange | Off[2] |  |
| Measurement:Fetch Backlog | N/A |  |
| Measurement:Measure Record Delta Time | N/A |  |
| Measurement:Measure Record Length | 1 |  |
| Measurement:Measure Record Length Is Finite | TRUE |  |
| Measurement:Power Line Frequency | 60 Hz |  |
| Measurement:Samples To Average | 1 |  |
| Measurement:Sense | Local |  |
| Source:Advanced:Active Advanced Sequence | "" |  |
| Source:Advanced:Active Advanced Sequence Step | 0 |  |
| Source:Advanced:Actual Power Allocation |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric[2] |  |
| Source:Advanced:Conduction Voltage:Mode | Automatic |  |
| Source:Advanced:Conduction Voltage:Off Threshold | 0.05 V |  |
| Source:Advanced:Conduction Voltage:On Threshold | 0.15 V |  |
| Source:Advanced:Merged Channels | ""[2] |  |
| Source:Advanced:OVP Enabled | FALSE[2] |  |
| Source:Advanced:OVP Limit | 0.0[2] |  |
| Source:Advanced:Output Capacitance |  |  |
| Source:Advanced:Output Shorted | FALSE |  |
| Source:Advanced:Overranging Enabled | FALSE |  |
| Source:Advanced:Power Allocation Mode |  |  |
| Source:Advanced:Pulse Bias Delay |  |  |
| Source:Advanced:Pulse Off Time |  |  |
| Source:Advanced:Pulse On Time |  |  |
| Source:Advanced:Requested Power Allocation |  |  |
| Source:Advanced:Sequence Loop Count | 1 |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE |  |
| Source:Advanced:Sequence Step Delta Time |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE[2] |  |
| Source:Advanced:Source Delay | 0.01666666 s |  |
| Source:Constant Power:Current Limit | 0.8 A |  |
| Source:Constant Power:Level | 0.0 W |  |
| Source:Constant Power:Level Range | 300.0 W[4] |  |
| Source:Constant Resistance:Current Limit | 0.8 A |  |
| Source:Constant Resistance:Level | 1000.0 Ω |  |
| Source:Constant Resistance:Level Range | 1000.0 Ω |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:DC Current:Current Level | 0.0 |  |
| Source:DC Current:Current Level Autorange | Off |  |
| Source:DC Current:Current Level Range | 40 A |  |
| Source:DC Current:Current Level Slew Rate:Falling | 24.0 A/μs |  |
| Source:DC Current:Current Level Slew Rate:Rising | 24.0 A/μs |  |
| Source:DC Current:Voltage Limit | Inf[2] |  |
| Source:DC Current:Voltage Limit Autorange | Off[2] |  |
| Source:DC Current:Voltage Limit High |  |  |
| Source:DC Current:Voltage Limit Low |  |  |
| Source:DC Current:Voltage Limit Range | 60 V |  |
| Source:DC Voltage:Current Limit | 0.8 A |  |
| Source:DC Voltage:Current Limit Autorange | Off |  |
| Source:DC Voltage:Current Limit High |  |  |
| Source:DC Voltage:Current Limit Low |  |  |
| Source:DC Voltage:Current Limit Range | 40 A |  |
| Source:DC Voltage:Voltage Level | 60.0 |  |
| Source:DC Voltage:Voltage Level Autorange | Off |  |
| Source:DC Voltage:Voltage Level Range | 60 V |  |
| Source:Output Connected | TRUE |  |
| Source:Output Cutoff:Current Change Limit High |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |
| Source:Output Cutoff:Delay |  |  |
| Source:Output Cutoff:Enabled |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |
| Source:Output Enabled | TRUE[3] |  |
| Source:Output Function | DC Current |  |
| Source:Output Resistance | 0.0[2] |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |
| Source:Source Mode | Single Point |  |
| Source:Transient Response | Normal |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising[2] |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Measure Trigger:Export Output Terminal | "" |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising[2] |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising[2] |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Source Trigger:Export Output Terminal | "" |  |
| Triggers:Source Trigger:Trigger Type | None |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising[2] |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Start Trigger:Export Output Terminal | "" |  |
| Triggers:Start Trigger:Trigger Type | None |  |

1

On Demand

Single Point

Automatically After Source Complete

Sequence

2

Only valid value.

3

The default value is TRUE if you use the niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

4

Default depends on the max DC sinking power of the instrument.
 Refer to the specifications for your instrument for more information.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> 
 The default value is TRUE if you use the niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<sup>4</sup> 
 Default depends on the max DC sinking power of the instrument.
 Refer to the specifications for your instrument for more information.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4110.html language=enus -->
## TOPIC 00340: Properties Supported by the PXIe-4110

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4110.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4110.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property you can configure for your device. An in a table cell indicates that the listed property is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed property because it is a read-only

### Properties Supported by the PXIe-4110

The following table lists the default values for each property
 you can configure for your device.
 An [IMAGE alt='image' src='../../../../images/xmark.gif'] in a table cell
 indicates that the listed property is not supported for that device.
 N/A in a table cell indicates that there is not a default value for
 the listed property because it is a read-only property.

| Property | PXI-4110 |
| --- | --- |
| Active Channel | "" |
| Advanced:Auxiliary Power Source Available | N/A |
| Advanced:Interlock Input Open |  |
| Advanced:Isolation State |  |
| Advanced:Power Source | Automatic |
| Advanced:Power Source In Use | N/A |
| Advanced:Self-Calibration Persistence |  |
| Device Specific:LCR:Cable Length |  |
| Events:Measure Complete Event:Event Delay |  |
| Events:Measure Complete Event:Output Behavior | N/A |
| Events:Measure Complete Event:Output Terminal |  |
| Events:Measure Complete Event:Pulse:Polarity |  |
| Events:Measure Complete Event:Pulse:Width |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A |
| Events:Pulse Complete Event:Output Terminal |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |
| Events:Pulse Complete Event:Pulse:Width |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A |
| Events:Sequence Engine Done Event:Output Terminal |  |
| Events:Sequence Engine Done Event:Pulse:Polarity |  |
| Events:Sequence Engine Done Event:Pulse:Width |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A |
| Events:Sequence Iteration Complete Event:Output Terminal |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity |  |
| Events:Sequence Iteration Complete Event:Pulse:Width |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A |
| Events:Source Complete Event:Output Behavior | N/A |
| Events:Source Complete Event:Output Terminal |  |
| Events:Source Complete Event:Pulse:Polarity |  |
| Events:Source Complete Event:Pulse:Width |  |
| Events:Source Complete Event:Toggle:Initial State | N/A |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |
| Inherent IVI Attributes:Driver Identification:Description | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |
| Inherent IVI Attributes:User Options:Cache | TRUE |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE |
| Inherent IVI Attributes:User Options:Range Check | TRUE |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |
| Inherent IVI Attributes:User Options:Simulate | FALSE |
| LCR:AC Stimulus:Advanced:Current Range |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |
| LCR:AC Stimulus:Automatic Level Control |  |
| LCR:AC Stimulus:Current Amplitude |  |
| LCR:AC Stimulus:Frequency |  |
| LCR:AC Stimulus:Function |  |
| LCR:AC Stimulus:Voltage Amplitude |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |
| LCR:Compensation:Load:Actual Reactance |  |
| LCR:Compensation:Load:Actual Resistance |  |
| LCR:Compensation:Load:Enabled |  |
| LCR:Compensation:Load:Measured Reactance |  |
| LCR:Compensation:Load:Measured Resistance |  |
| LCR:Compensation:Open:Conductance |  |
| LCR:Compensation:Open:Enabled |  |
| LCR:Compensation:Open:Susceptance |  |
| LCR:Compensation:Short:Enabled |  |
| LCR:Compensation:Short:Reactance |  |
| LCR:Compensation:Short:Resistance |  |
| LCR:Custom Measurement Time |  |
| LCR:DC Bias:Advanced:Current Range |  |
| LCR:DC Bias:Advanced:Transient Response |  |
| LCR:DC Bias:Advanced:Voltage Range |  |
| LCR:DC Bias:Automatic Level Control |  |
| LCR:DC Bias:Current Level |  |
| LCR:DC Bias:Source |  |
| LCR:DC Bias:Voltage Level |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |
| LCR:Impedance Range:Impedance Autorange |  |
| LCR:Impedance Range:Impedance Range |  |
| LCR:Instrument Mode | SMU PS |
| LCR:Measurement Time |  |
| LCR:Source Delay Mode |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |
| Measurement:Advanced:Autorange Behavior |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |
| Measurement:Advanced:Autorange Threshold Mode |  |
| Measurement:Advanced:DC Noise Rejection | Normal |
| Measurement:Advanced:Measure Buffer Size |  |
| Measurement:Advanced:Measure When | On Demand |
| Measurement:Advanced:Reset Average Before Measurement | TRUE |
| Measurement:Aperture Time |  |
| Measurement:Aperture Time Auto Mode |  |
| Measurement:Aperture Time Units |  |
| Measurement:Auto Zero | Off |
| Measurement:Autorange |  |
| Measurement:Fetch Backlog |  |
| Measurement:Measure Record Delta Time |  |
| Measurement:Measure Record Length |  |
| Measurement:Measure Record Length Is Finite |  |
| Measurement:Power Line Frequency |  |
| Measurement:Samples To Average | 10 |
| Measurement:Sense | Local |
| Source:Advanced:Active Advanced Sequence |  |
| Source:Advanced:Active Advanced Sequence Step |  |
| Source:Advanced:Actual Power Allocation |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric |
| Source:Advanced:Conduction Voltage:Mode |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |
| Source:Advanced:Merged Channels |  |
| Source:Advanced:OVP Enabled |  |
| Source:Advanced:OVP Limit |  |
| Source:Advanced:Output Capacitance | High |
| Source:Advanced:Output Shorted |  |
| Source:Advanced:Overranging Enabled | FALSE |
| Source:Advanced:Power Allocation Mode |  |
| Source:Advanced:Pulse Bias Delay |  |
| Source:Advanced:Pulse Off Time |  |
| Source:Advanced:Pulse On Time |  |
| Source:Advanced:Requested Power Allocation |  |
| Source:Advanced:Sequence Loop Count |  |
| Source:Advanced:Sequence Loop Count Is Finite |  |
| Source:Advanced:Sequence Step Delta Time |  |
| Source:Advanced:Sequence Step Delta Time Enabled |  |
| Source:Advanced:Source Delay | 0.01666666 s[1] |
| Source:Constant Power:Current Limit |  |
| Source:Constant Power:Level |  |
| Source:Constant Power:Level Range |  |
| Source:Constant Resistance:Current Limit |  |
| Source:Constant Resistance:Level |  |
| Source:Constant Resistance:Level Range |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  |
| Source:DC Current:Current Level | Channel 0: 0.01 Channel 1: 0.01 Channel 2: ‑0.01 |
| Source:DC Current:Current Level Autorange | Off |
| Source:DC Current:Current Level Range | 1.0 |
| Source:DC Current:Current Level Slew Rate:Falling |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |
| Source:DC Current:Voltage Limit | Channel 0: 6 Channel 1: 20 Channel 2: 20 |
| Source:DC Current:Voltage Limit Autorange | Off |
| Source:DC Current:Voltage Limit High |  |
| Source:DC Current:Voltage Limit Low |  |
| Source:DC Current:Voltage Limit Range | Channel 0: 6 Channel 1: 20 Channel 2: 20 |
| Source:DC Voltage:Current Limit | 0.1 |
| Source:DC Voltage:Current Limit Autorange | Off |
| Source:DC Voltage:Current Limit High |  |
| Source:DC Voltage:Current Limit Low |  |
| Source:DC Voltage:Current Limit Range | 1 |
| Source:DC Voltage:Voltage Level | 0 |
| Source:DC Voltage:Voltage Level Autorange | Off |
| Source:DC Voltage:Voltage Level Range | Channel 0: 6 Channel 1: 20 Channel 2: ‑20 |
| Source:Output Connected |  |
| Source:Output Cutoff:Current Change Limit High |  |
| Source:Output Cutoff:Current Change Limit Low |  |
| Source:Output Cutoff:Current Measure Limit High |  |
| Source:Output Cutoff:Current Measure Limit Low |  |
| Source:Output Cutoff:Current Overrange Enabled |  |
| Source:Output Cutoff:Delay |  |
| Source:Output Cutoff:Enabled |  |
| Source:Output Cutoff:Voltage Change Limit High |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |
| Source:Output Cutoff:Voltage Output Limit High |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |
| Source:Output Enabled | TRUE[2] |
| Source:Output Function | DC Voltage |
| Source:Output Resistance |  |
| Source:Pulse Current:Pulse Bias Current Level |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |
| Source:Pulse Current:Pulse Current Level |  |
| Source:Pulse Current:Pulse Current Level Range |  |
| Source:Pulse Current:Pulse Voltage Limit |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |
| Source:Pulse Voltage:Pulse Current Limit |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |
| Source:Source Mode | Single Point |
| Source:Transient Response |  |
| Triggers:Measure Trigger:Digital Edge:Edge |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal |  |
| Triggers:Measure Trigger:Export Output Terminal |  |
| Triggers:Measure Trigger:Trigger Type |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |
| Triggers:Pulse Trigger:Trigger Type |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal |  |
| Triggers:Sequence Advance Trigger:Trigger Type |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |
| Triggers:Shutdown Trigger:Trigger Type |  |
| Triggers:Source Trigger:Digital Edge:Edge |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal |  |
| Triggers:Source Trigger:Export Output Terminal |  |
| Triggers:Source Trigger:Trigger Type |  |
| Triggers:Start Trigger:Digital Edge:Edge |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal |  |
| Triggers:Start Trigger:Export Output Terminal |  |
| Triggers:Start Trigger:Trigger Type |  |

1

Software timed.

2

The default value is TRUE if you use the niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> Software timed.

<sup>2</sup> 
 The default value is TRUE if you use the niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4112-4113.html language=enus -->
## TOPIC 00341: Properties Supported by the PXIe-4112/4113

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4112-4113.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4112-4113.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property you can configure for your device. An in a table cell indicates that the listed property is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed property because it is a read-only

### Properties Supported by the PXIe-4112/4113

The following table lists the default values for each property
 you can configure for your device.
 An [IMAGE alt='image' src='../../../../images/xmark.gif'] in a table cell
 indicates that the listed property is not supported for that device.
 N/A in a table cell indicates that there is not a default value for
 the listed property because it is a read-only property.

| Property | PXIe-4112 | PXIe-4113 |
| --- | --- | --- |
| Active Channel | "" | "" |
| Advanced:Auxiliary Power Source Available | N/A | N/A |
| Advanced:Interlock Input Open |  |  |
| Advanced:Isolation State |  |  |
| Advanced:Power Source | External[1] | External[1] |
| Advanced:Power Source In Use | N/A | N/A |
| Advanced:Self-Calibration Persistence |  |  |
| Device Specific:LCR:Cable Length |  |  |
| Events:Measure Complete Event:Event Delay | 0 | 0 |
| Events:Measure Complete Event:Output Behavior | N/A | N/A |
| Events:Measure Complete Event:Output Terminal | "" | "" |
| Events:Measure Complete Event:Pulse:Polarity | Active High | Active High |
| Events:Measure Complete Event:Pulse:Width | 250 ns | 250 ns |
| Events:Measure Complete Event:Toggle:Initial State | N/A | N/A |
| Events:Pulse Complete Event:Output Terminal |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A | N/A |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High | Active High |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns | 250 ns |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A | N/A |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A | N/A |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High | Active High |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns | 250 ns |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A | N/A |
| Events:Source Complete Event:Output Behavior | N/A | N/A |
| Events:Source Complete Event:Output Terminal | "" | "" |
| Events:Source Complete Event:Pulse:Polarity | Active High | Active High |
| Events:Source Complete Event:Pulse:Width | 250 ns | 250 ns |
| Events:Source Complete Event:Toggle:Initial State | N/A | N/A |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |
| LCR:AC Stimulus:Advanced:Current Range |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |
| LCR:AC Stimulus:Frequency |  |  |
| LCR:AC Stimulus:Function |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |
| LCR:Compensation:Load:Enabled |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |
| LCR:Compensation:Open:Conductance |  |  |
| LCR:Compensation:Open:Enabled |  |  |
| LCR:Compensation:Open:Susceptance |  |  |
| LCR:Compensation:Short:Enabled |  |  |
| LCR:Compensation:Short:Reactance |  |  |
| LCR:Compensation:Short:Resistance |  |  |
| LCR:Custom Measurement Time |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |
| LCR:DC Bias:Current Level |  |  |
| LCR:DC Bias:Source |  |  |
| LCR:DC Bias:Voltage Level |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |
| LCR:Impedance Range:Impedance Range |  |  |
| LCR:Instrument Mode | SMU PS | SMU PS |
| LCR:Measurement Time |  |  |
| LCR:Source Delay Mode |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |  |
| Measurement:Advanced:Autorange Behavior |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |  |
| Measurement:Advanced:Autorange Threshold Mode |  |  |
| Measurement:Advanced:DC Noise Rejection |  |  |
| Measurement:Advanced:Measure Buffer Size | 10500 | 10500 |
| Measurement:Advanced:Measure When | On Demand[2] | On Demand[2] |
| Measurement:Advanced:Reset Average Before Measurement |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |
| Measurement:Aperture Time Auto Mode |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |
| Measurement:Auto Zero | Off | Off |
| Measurement:Autorange |  |  |
| Measurement:Fetch Backlog | N/A | N/A |
| Measurement:Measure Record Delta Time | N/A | N/A |
| Measurement:Measure Record Length | 1 | 1 |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |
| Measurement:Power Line Frequency | 60 Hertz | 60 Hertz |
| Measurement:Samples To Average | 1 | 1 |
| Measurement:Sense | Remote[3] | Remote[3] |
| Source:Advanced:Active Advanced Sequence |  |  |
| Source:Advanced:Active Advanced Sequence Step |  |  |
| Source:Advanced:Actual Power Allocation |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |
| Source:Advanced:Conduction Voltage:Mode |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |
| Source:Advanced:Merged Channels |  |  |
| Source:Advanced:OVP Enabled |  |  |
| Source:Advanced:OVP Limit |  |  |
| Source:Advanced:Output Capacitance |  |  |
| Source:Advanced:Output Shorted |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |
| Source:Advanced:Power Allocation Mode |  |  |
| Source:Advanced:Pulse Bias Delay |  |  |
| Source:Advanced:Pulse Off Time |  |  |
| Source:Advanced:Pulse On Time |  |  |
| Source:Advanced:Requested Power Allocation |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |
| Source:Advanced:Sequence Step Delta Time |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled |  |  |
| Source:Advanced:Source Delay | 0.08 s | 0.08 s |
| Source:Constant Power:Current Limit |  |  |
| Source:Constant Power:Level |  |  |
| Source:Constant Power:Level Range |  |  |
| Source:Constant Resistance:Current Limit |  |  |
| Source:Constant Resistance:Level |  |  |
| Source:Constant Resistance:Level Range |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  |  |
| Source:DC Current:Current Level | 0.01 | 0.02 |
| Source:DC Current:Current Level Autorange | Off | Off |
| Source:DC Current:Current Level Range | 1 | 6 |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |
| Source:DC Current:Voltage Limit | 10 | 10 |
| Source:DC Current:Voltage Limit Autorange | Off | Off |
| Source:DC Current:Voltage Limit High |  |  |
| Source:DC Current:Voltage Limit Low |  |  |
| Source:DC Current:Voltage Limit Range | 60 | 10 |
| Source:DC Voltage:Current Limit | 0.1 | 0.1 |
| Source:DC Voltage:Current Limit Autorange | Off | Off |
| Source:DC Voltage:Current Limit High |  |  |
| Source:DC Voltage:Current Limit Low |  |  |
| Source:DC Voltage:Current Limit Range | 1 | 6 |
| Source:DC Voltage:Voltage Level | 0.1 | 0.03 |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |
| Source:DC Voltage:Voltage Level Range | 60 | 10 |
| Source:Output Connected | TRUE | TRUE |
| Source:Output Cutoff:Current Change Limit High |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |
| Source:Output Cutoff:Delay |  |  |
| Source:Output Cutoff:Enabled |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |
| Source:Output Enabled | TRUE[4] | TRUE[4] |
| Source:Output Function | DC Voltage | DC Voltage |
| Source:Output Resistance |  |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |
| Source:Source Mode | Single Point | Single Point |
| Source:Transient Response |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising | Rising |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising | Rising |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising | Rising |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |
| Triggers:Source Trigger:Trigger Type | None | None |
| Triggers:Start Trigger:Digital Edge:Edge | Rising | Rising |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |
| Triggers:Start Trigger:Trigger Type | None | None |

1

External

2

On Demand

Single Point

Automatically After Source Complete

Sequence

3

Remote

4

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> External is the only valid value.

<sup>2</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>3</sup> Remote is the only valid value.

<sup>4</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4130.html language=enus -->
## TOPIC 00342: Properties Supported by the PXI-4130

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4130.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4130.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property you can configure for your device. An in a table cell indicates that the listed property is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed property because it is a read-only

### Properties Supported by the PXI-4130

The following table lists the default values for each property
 you can configure for your device.
 An [IMAGE alt='image' src='../../../../images/xmark.gif'] in a table cell
 indicates that the listed property is not supported for that device.
 N/A in a table cell indicates that there is not a default value for
 the listed property because it is a read-only property.

| Property | PXI-4130 |
| --- | --- |
| Active Channel | "" |
| Advanced:Auxiliary Power Source Available | N/A |
| Advanced:Interlock Input Open |  |
| Advanced:Isolation State |  |
| Advanced:Power Source | Automatic |
| Advanced:Power Source In Use | N/A |
| Advanced:Self-Calibration Persistence |  |
| Device Specific:LCR:Cable Length |  |
| Events:Measure Complete Event:Event Delay |  |
| Events:Measure Complete Event:Output Behavior | N/A |
| Events:Measure Complete Event:Output Terminal |  |
| Events:Measure Complete Event:Pulse:Polarity |  |
| Events:Measure Complete Event:Pulse:Width |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A |
| Events:Pulse Complete Event:Output Terminal |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |
| Events:Pulse Complete Event:Pulse:Width |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A |
| Events:Sequence Engine Done Event:Output Terminal |  |
| Events:Sequence Engine Done Event:Pulse:Polarity |  |
| Events:Sequence Engine Done Event:Pulse:Width |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A |
| Events:Sequence Iteration Complete Event:Output Terminal |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity |  |
| Events:Sequence Iteration Complete Event:Pulse:Width |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A |
| Events:Source Complete Event:Output Behavior | N/A |
| Events:Source Complete Event:Output Terminal |  |
| Events:Source Complete Event:Pulse:Polarity |  |
| Events:Source Complete Event:Pulse:Width |  |
| Events:Source Complete Event:Toggle:Initial State | N/A |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |
| Inherent IVI Attributes:Driver Identification:Description | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |
| Inherent IVI Attributes:User Options:Cache | TRUE |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE |
| Inherent IVI Attributes:User Options:Range Check | TRUE |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |
| Inherent IVI Attributes:User Options:Simulate | FALSE |
| LCR:AC Stimulus:Advanced:Current Range |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |
| LCR:AC Stimulus:Automatic Level Control |  |
| LCR:AC Stimulus:Current Amplitude |  |
| LCR:AC Stimulus:Frequency |  |
| LCR:AC Stimulus:Function |  |
| LCR:AC Stimulus:Voltage Amplitude |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |
| LCR:Compensation:Load:Actual Reactance |  |
| LCR:Compensation:Load:Actual Resistance |  |
| LCR:Compensation:Load:Enabled |  |
| LCR:Compensation:Load:Measured Reactance |  |
| LCR:Compensation:Load:Measured Resistance |  |
| LCR:Compensation:Open:Conductance |  |
| LCR:Compensation:Open:Enabled |  |
| LCR:Compensation:Open:Susceptance |  |
| LCR:Compensation:Short:Enabled |  |
| LCR:Compensation:Short:Reactance |  |
| LCR:Compensation:Short:Resistance |  |
| LCR:Custom Measurement Time |  |
| LCR:DC Bias:Advanced:Current Range |  |
| LCR:DC Bias:Advanced:Transient Response |  |
| LCR:DC Bias:Advanced:Voltage Range |  |
| LCR:DC Bias:Automatic Level Control |  |
| LCR:DC Bias:Current Level |  |
| LCR:DC Bias:Source |  |
| LCR:DC Bias:Voltage Level |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |
| LCR:Impedance Range:Impedance Autorange |  |
| LCR:Impedance Range:Impedance Range |  |
| LCR:Instrument Mode | SMU PS |
| LCR:Measurement Time |  |
| LCR:Source Delay Mode |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |
| Measurement:Advanced:Autorange Behavior |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |
| Measurement:Advanced:Autorange Threshold Mode |  |
| Measurement:Advanced:DC Noise Rejection | Normal |
| Measurement:Advanced:Measure Buffer Size |  |
| Measurement:Advanced:Measure When | On Demand |
| Measurement:Advanced:Reset Average Before Measurement | TRUE |
| Measurement:Aperture Time |  |
| Measurement:Aperture Time Auto Mode |  |
| Measurement:Aperture Time Units |  |
| Measurement:Auto Zero | Off |
| Measurement:Autorange |  |
| Measurement:Fetch Backlog |  |
| Measurement:Measure Record Delta Time |  |
| Measurement:Measure Record Length |  |
| Measurement:Measure Record Length Is Finite |  |
| Measurement:Power Line Frequency |  |
| Measurement:Samples To Average | 10 |
| Measurement:Sense | Local |
| Source:Advanced:Active Advanced Sequence |  |
| Source:Advanced:Active Advanced Sequence Step |  |
| Source:Advanced:Actual Power Allocation |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric |
| Source:Advanced:Conduction Voltage:Mode |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |
| Source:Advanced:Merged Channels |  |
| Source:Advanced:OVP Enabled |  |
| Source:Advanced:OVP Limit |  |
| Source:Advanced:Output Capacitance | High[1] |
| Source:Advanced:Output Shorted |  |
| Source:Advanced:Overranging Enabled | FALSE |
| Source:Advanced:Power Allocation Mode |  |
| Source:Advanced:Pulse Bias Delay |  |
| Source:Advanced:Pulse Off Time |  |
| Source:Advanced:Pulse On Time |  |
| Source:Advanced:Requested Power Allocation |  |
| Source:Advanced:Sequence Loop Count |  |
| Source:Advanced:Sequence Loop Count Is Finite |  |
| Source:Advanced:Sequence Step Delta Time |  |
| Source:Advanced:Sequence Step Delta Time Enabled |  |
| Source:Advanced:Source Delay | 0.01666666 s[2] |
| Source:Constant Power:Current Limit |  |
| Source:Constant Power:Level |  |
| Source:Constant Power:Level Range |  |
| Source:Constant Resistance:Current Limit |  |
| Source:Constant Resistance:Level |  |
| Source:Constant Resistance:Level Range |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  |
| Source:DC Current:Current Level | Channel 0: 0.02 Channel 1: 0.04 |
| Source:DC Current:Current Level Autorange | Off |
| Source:DC Current:Current Level Range | Channel 1: 1.0 Channel 2: 2.0 |
| Source:DC Current:Current Level Slew Rate:Falling |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |
| Source:DC Current:Voltage Limit | Channel 0: 6 Channel 1: 20 |
| Source:DC Current:Voltage Limit Autorange | Off |
| Source:DC Current:Voltage Limit High |  |
| Source:DC Current:Voltage Limit Low |  |
| Source:DC Current:Voltage Limit Range | Channel 0: 6 Channel 1: 20 |
| Source:DC Voltage:Current Limit | 0.1 |
| Source:DC Voltage:Current Limit Autorange | Off |
| Source:DC Voltage:Current Limit High |  |
| Source:DC Voltage:Current Limit Low |  |
| Source:DC Voltage:Current Limit Range | Channel 1: 1 Channel 2: 2 |
| Source:DC Voltage:Voltage Level | 0 |
| Source:DC Voltage:Voltage Level Autorange | Off |
| Source:DC Voltage:Voltage Level Range | Channel 0: 6 Channel 1: 20 |
| Source:Output Connected |  |
| Source:Output Cutoff:Current Change Limit High |  |
| Source:Output Cutoff:Current Change Limit Low |  |
| Source:Output Cutoff:Current Measure Limit High |  |
| Source:Output Cutoff:Current Measure Limit Low |  |
| Source:Output Cutoff:Current Overrange Enabled |  |
| Source:Output Cutoff:Delay | 0.0 |
| Source:Output Cutoff:Enabled |  |
| Source:Output Cutoff:Voltage Change Limit High |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |
| Source:Output Cutoff:Voltage Output Limit High |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |
| Source:Output Enabled | TRUE[3] |
| Source:Output Function | DC Voltage |
| Source:Output Resistance |  |
| Source:Pulse Current:Pulse Bias Current Level |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |
| Source:Pulse Current:Pulse Current Level |  |
| Source:Pulse Current:Pulse Current Level Range |  |
| Source:Pulse Current:Pulse Voltage Limit |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |
| Source:Pulse Voltage:Pulse Current Limit |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |
| Source:Source Mode | Single Point |
| Source:Transient Response |  |
| Triggers:Measure Trigger:Digital Edge:Edge |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal |  |
| Triggers:Measure Trigger:Export Output Terminal |  |
| Triggers:Measure Trigger:Trigger Type |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |
| Triggers:Pulse Trigger:Trigger Type |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal |  |
| Triggers:Sequence Advance Trigger:Trigger Type |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |
| Triggers:Shutdown Trigger:Trigger Type |  |
| Triggers:Source Trigger:Digital Edge:Edge |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal |  |
| Triggers:Source Trigger:Export Output Terminal |  |
| Triggers:Source Trigger:Trigger Type |  |
| Triggers:Start Trigger:Digital Edge:Edge |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal |  |
| Triggers:Start Trigger:Export Output Terminal |  |
| Triggers:Start Trigger:Trigger Type |  |

1

The default value for channel 1 is Low.

2

Software timed.

3

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> The default value for channel 1 is Low.

<sup>2</sup> Software timed.

<sup>3</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4132.html language=enus -->
## TOPIC 00343: Properties Supported by the PXI-4132

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4132.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4132.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property you can configure for your device. An in a table cell indicates that the listed property is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed property because it is a read-only

### Properties Supported by the PXI-4132

The following table lists the default values for each property
 you can configure for your device.
 An [IMAGE alt='image' src='../../../../images/xmark.gif'] in a table cell
 indicates that the listed property is not supported for that device.
 N/A in a table cell indicates that there is not a default value for
 the listed property because it is a read-only property.

| Property | PXI-4132 |
| --- | --- |
| Active Channel | "" |
| Advanced:Auxiliary Power Source Available | N/A |
| Advanced:Interlock Input Open |  |
| Advanced:Isolation State |  |
| Advanced:Power Source | Internal |
| Advanced:Power Source In Use | N/A |
| Advanced:Self-Calibration Persistence | Write to EEPROM |
| Device Specific:LCR:Cable Length |  |
| Events:Measure Complete Event:Event Delay | 0 |
| Events:Measure Complete Event:Output Behavior | N/A |
| Events:Measure Complete Event:Output Terminal | "" |
| Events:Measure Complete Event:Pulse:Polarity | Active High |
| Events:Measure Complete Event:Pulse:Width | 150 ns |
| Events:Measure Complete Event:Toggle:Initial State | N/A |
| Events:Pulse Complete Event:Output Terminal |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |
| Events:Pulse Complete Event:Pulse:Width |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A |
| Events:Sequence Engine Done Event:Output Terminal | "" |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High |
| Events:Sequence Engine Done Event:Pulse:Width | 150 ns |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A |
| Events:Sequence Iteration Complete Event:Output Terminal | "" |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High |
| Events:Sequence Iteration Complete Event:Pulse:Width | 150 ns |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A |
| Events:Source Complete Event:Output Behavior | N/A |
| Events:Source Complete Event:Output Terminal | "" |
| Events:Source Complete Event:Pulse:Polarity | Active High |
| Events:Source Complete Event:Pulse:Width | 150 ns |
| Events:Source Complete Event:Toggle:Initial State | N/A |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |
| Inherent IVI Attributes:Driver Identification:Description | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |
| Inherent IVI Attributes:User Options:Cache | TRUE |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE |
| Inherent IVI Attributes:User Options:Range Check | TRUE |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |
| Inherent IVI Attributes:User Options:Simulate | FALSE |
| LCR:AC Stimulus:Advanced:Current Range |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |
| LCR:AC Stimulus:Automatic Level Control |  |
| LCR:AC Stimulus:Current Amplitude |  |
| LCR:AC Stimulus:Frequency |  |
| LCR:AC Stimulus:Function |  |
| LCR:AC Stimulus:Voltage Amplitude |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |
| LCR:Compensation:Load:Actual Reactance |  |
| LCR:Compensation:Load:Actual Resistance |  |
| LCR:Compensation:Load:Enabled |  |
| LCR:Compensation:Load:Measured Reactance |  |
| LCR:Compensation:Load:Measured Resistance |  |
| LCR:Compensation:Open:Conductance |  |
| LCR:Compensation:Open:Enabled |  |
| LCR:Compensation:Open:Susceptance |  |
| LCR:Compensation:Short:Enabled |  |
| LCR:Compensation:Short:Reactance |  |
| LCR:Compensation:Short:Resistance |  |
| LCR:Custom Measurement Time |  |
| LCR:DC Bias:Advanced:Current Range |  |
| LCR:DC Bias:Advanced:Transient Response |  |
| LCR:DC Bias:Advanced:Voltage Range |  |
| LCR:DC Bias:Automatic Level Control |  |
| LCR:DC Bias:Current Level |  |
| LCR:DC Bias:Source |  |
| LCR:DC Bias:Voltage Level |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |
| LCR:Impedance Range:Impedance Autorange |  |
| LCR:Impedance Range:Impedance Range |  |
| LCR:Instrument Mode | SMU PS |
| LCR:Measurement Time |  |
| LCR:Source Delay Mode |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |
| Measurement:Advanced:Autorange Behavior |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |
| Measurement:Advanced:Autorange Threshold Mode |  |
| Measurement:Advanced:DC Noise Rejection | Normal |
| Measurement:Advanced:Measure Buffer Size | 64000 |
| Measurement:Advanced:Measure When | On Demand[1] |
| Measurement:Advanced:Reset Average Before Measurement |  |
| Measurement:Aperture Time | 0.01666666 s |
| Measurement:Aperture Time Auto Mode |  |
| Measurement:Aperture Time Units | Seconds |
| Measurement:Auto Zero | On |
| Measurement:Autorange |  |
| Measurement:Fetch Backlog | N/A |
| Measurement:Measure Record Delta Time | N/A |
| Measurement:Measure Record Length | 1 |
| Measurement:Measure Record Length Is Finite | TRUE |
| Measurement:Power Line Frequency | 60 Hertz |
| Measurement:Samples To Average | 1 |
| Measurement:Sense | Local |
| Source:Advanced:Active Advanced Sequence |  |
| Source:Advanced:Active Advanced Sequence Step |  |
| Source:Advanced:Actual Power Allocation |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric |
| Source:Advanced:Conduction Voltage:Mode |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |
| Source:Advanced:Merged Channels |  |
| Source:Advanced:OVP Enabled |  |
| Source:Advanced:OVP Limit |  |
| Source:Advanced:Output Capacitance | High |
| Source:Advanced:Output Shorted |  |
| Source:Advanced:Overranging Enabled | FALSE |
| Source:Advanced:Power Allocation Mode |  |
| Source:Advanced:Pulse Bias Delay |  |
| Source:Advanced:Pulse Off Time |  |
| Source:Advanced:Pulse On Time |  |
| Source:Advanced:Requested Power Allocation |  |
| Source:Advanced:Sequence Loop Count | 1 |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE |
| Source:Advanced:Sequence Step Delta Time |  |
| Source:Advanced:Sequence Step Delta Time Enabled |  |
| Source:Advanced:Source Delay | 0.01666666 s |
| Source:Constant Power:Current Limit |  |
| Source:Constant Power:Level |  |
| Source:Constant Power:Level Range |  |
| Source:Constant Resistance:Current Limit |  |
| Source:Constant Resistance:Level |  |
| Source:Constant Resistance:Level Range |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  |
| Source:DC Current:Current Level | 0.002 |
| Source:DC Current:Current Level Autorange | Off |
| Source:DC Current:Current Level Range | 0.1 |
| Source:DC Current:Current Level Slew Rate:Falling |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |
| Source:DC Current:Voltage Limit | 10 |
| Source:DC Current:Voltage Limit Autorange | Off |
| Source:DC Current:Voltage Limit High |  |
| Source:DC Current:Voltage Limit Low |  |
| Source:DC Current:Voltage Limit Range | 10 |
| Source:DC Voltage:Current Limit | 0.02 |
| Source:DC Voltage:Current Limit Autorange | Off |
| Source:DC Voltage:Current Limit High |  |
| Source:DC Voltage:Current Limit Low |  |
| Source:DC Voltage:Current Limit Range | 0.1 |
| Source:DC Voltage:Voltage Level | 0 |
| Source:DC Voltage:Voltage Level Autorange | Off |
| Source:DC Voltage:Voltage Level Range | 10 |
| Source:Output Connected | TRUE |
| Source:Output Cutoff:Current Change Limit High |  |
| Source:Output Cutoff:Current Change Limit Low |  |
| Source:Output Cutoff:Current Measure Limit High |  |
| Source:Output Cutoff:Current Measure Limit Low |  |
| Source:Output Cutoff:Current Overrange Enabled |  |
| Source:Output Cutoff:Delay | 0.0 |
| Source:Output Cutoff:Enabled |  |
| Source:Output Cutoff:Voltage Change Limit High |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |
| Source:Output Cutoff:Voltage Output Limit High |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |
| Source:Output Enabled | TRUE[2] |
| Source:Output Function | DC Voltage |
| Source:Output Resistance |  |
| Source:Pulse Current:Pulse Bias Current Level |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |
| Source:Pulse Current:Pulse Current Level |  |
| Source:Pulse Current:Pulse Current Level Range |  |
| Source:Pulse Current:Pulse Voltage Limit |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |
| Source:Pulse Voltage:Pulse Current Limit |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |
| Source:Source Mode | Single Point |
| Source:Transient Response |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Measure Trigger:Export Output Terminal | "" |
| Triggers:Measure Trigger:Trigger Type | Digital Edge |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |
| Triggers:Pulse Trigger:Trigger Type |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" |
| Triggers:Sequence Advance Trigger:Trigger Type | None |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |
| Triggers:Shutdown Trigger:Trigger Type |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Source Trigger:Export Output Terminal | "" |
| Triggers:Source Trigger:Trigger Type | None |
| Triggers:Start Trigger:Digital Edge:Edge | Rising |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Start Trigger:Export Output Terminal | "" |
| Triggers:Start Trigger:Trigger Type | None |

1

On Demand

Single Point

Automatically After Source Complete

Sequence

2

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>2</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4135.html language=enus -->
## TOPIC 00344: Properties Supported by the PXIe-4135

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4135.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4135.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4135 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4135 Supports Advanced Sequence Active Channel "" Advanced:Auxiliary Power Source

### Properties Supported by the PXIe-4135

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4135 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4135 | Supports Advanced Sequence |
| --- | --- | --- |
| Active Channel | "" |  |
| Advanced:Auxiliary Power Source Available | N/A |  |
| Advanced:Interlock Input Open | N/A |  |
| Advanced:Isolation State |  |  |
| Advanced:Power Source | Internal |  |
| Advanced:Power Source In Use | N/A |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM[1] |  |
| Device Specific:LCR:Cable Length |  |  |
| Events:Measure Complete Event:Event Delay | 0 |  |
| Events:Measure Complete Event:Output Behavior | N/A |  |
| Events:Measure Complete Event:Output Terminal | "" |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A |  |
| Events:Pulse Complete Event:Output Terminal | "" |  |
| Events:Pulse Complete Event:Pulse:Polarity | Active High |  |
| Events:Pulse Complete Event:Pulse:Width | 250 ns |  |
| Events:Ready For Pulse Trigger Event:Output Terminal | "" |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity | Active High |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width | 250 ns |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A |  |
| Events:Sequence Engine Done Event:Output Terminal | "" |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A |  |
| Events:Source Complete Event:Output Behavior | N/A |  |
| Events:Source Complete Event:Output Terminal | "" |  |
| Events:Source Complete Event:Pulse:Polarity | Active High |  |
| Events:Source Complete Event:Pulse:Width | 250 ns |  |
| Events:Source Complete Event:Toggle:Initial State | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |  |
| Inherent IVI Attributes:User Options:Cache | TRUE |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | FALSE |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |  |
| Inherent IVI Attributes:User Options:Simulate | TRUE |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |
| LCR:AC Stimulus:Frequency |  |  |
| LCR:AC Stimulus:Function |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |
| LCR:Compensation:Load:Enabled |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |
| LCR:Compensation:Open:Conductance |  |  |
| LCR:Compensation:Open:Enabled |  |  |
| LCR:Compensation:Open:Susceptance |  |  |
| LCR:Compensation:Short:Enabled |  |  |
| LCR:Compensation:Short:Reactance |  |  |
| LCR:Compensation:Short:Resistance |  |  |
| LCR:Custom Measurement Time |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |
| LCR:DC Bias:Current Level |  |  |
| LCR:DC Bias:Source |  |  |
| LCR:DC Bias:Voltage Level |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |
| LCR:Impedance Range:Impedance Range |  |  |
| LCR:Instrument Mode | SMU PS |  |
| LCR:Measurement Time |  |  |
| LCR:Source Delay Mode |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode | Auto |  |
| Measurement:Advanced:Autorange Behavior | Range up to limit then down |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change | 0.5 s |  |
| Measurement:Advanced:Autorange Minimum Aperture Time | 0 s |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units | Seconds |  |
| Measurement:Advanced:Autorange Minimum Current Range | 0 |  |
| Measurement:Advanced:Autorange Minimum Voltage Range | 0 |  |
| Measurement:Advanced:Autorange Threshold Mode | Normal |  |
| Measurement:Advanced:DC Noise Rejection | Normal |  |
| Measurement:Advanced:Measure Buffer Size | 1800000 |  |
| Measurement:Advanced:Measure When | On Demand[2] |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |
| Measurement:Aperture Time | 0.01666666 s |  |
| Measurement:Aperture Time Auto Mode | Off |  |
| Measurement:Aperture Time Units | Seconds |  |
| Measurement:Auto Zero | Off |  |
| Measurement:Autorange | FALSE |  |
| Measurement:Fetch Backlog | N/A |  |
| Measurement:Measure Record Delta Time | N/A |  |
| Measurement:Measure Record Length | 1 |  |
| Measurement:Measure Record Length Is Finite | TRUE |  |
| Measurement:Power Line Frequency | 60 Hertz |  |
| Measurement:Samples To Average | 1 |  |
| Measurement:Sense | Local |  |
| Source:Advanced:Active Advanced Sequence | "" |  |
| Source:Advanced:Active Advanced Sequence Step | 0 |  |
| Source:Advanced:Actual Power Allocation |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |
| Source:Advanced:Merged Channels |  |  |
| Source:Advanced:OVP Enabled | FALSE |  |
| Source:Advanced:OVP Limit | 210 V |  |
| Source:Advanced:Output Capacitance |  |  |
| Source:Advanced:Output Shorted |  |  |
| Source:Advanced:Overranging Enabled | FALSE |  |
| Source:Advanced:Power Allocation Mode |  |  |
| Source:Advanced:Pulse Bias Delay | 0.01666666 s |  |
| Source:Advanced:Pulse Off Time | 34 ms |  |
| Source:Advanced:Pulse On Time | 34 ms |  |
| Source:Advanced:Requested Power Allocation |  |  |
| Source:Advanced:Sequence Loop Count | 1 |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE |  |
| Source:Advanced:Sequence Step Delta Time | 50 ms |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE |  |
| Source:Advanced:Source Delay | 0.01666666 s |  |
| Source:Constant Power:Current Limit |  |  |
| Source:Constant Power:Level |  |  |
| Source:Constant Power:Level Range |  |  |
| Source:Constant Resistance:Current Limit |  |  |
| Source:Constant Resistance:Level |  |  |
| Source:Constant Resistance:Level Range |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:DC Current:Current Level | 0 A |  |
| Source:DC Current:Current Level Autorange | Off |  |
| Source:DC Current:Current Level Range | 1 A |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |
| Source:DC Current:Voltage Limit | 20 V |  |
| Source:DC Current:Voltage Limit Autorange | Off |  |
| Source:DC Current:Voltage Limit High | 20 V |  |
| Source:DC Current:Voltage Limit Low | -20 V |  |
| Source:DC Current:Voltage Limit Range | 20 V |  |
| Source:DC Voltage:Current Limit | 100 mA |  |
| Source:DC Voltage:Current Limit Autorange | Off |  |
| Source:DC Voltage:Current Limit High | 100 mA |  |
| Source:DC Voltage:Current Limit Low | -100 mA |  |
| Source:DC Voltage:Current Limit Range | 100 mA |  |
| Source:DC Voltage:Voltage Level | 0 V |  |
| Source:DC Voltage:Voltage Level Autorange | Off |  |
| Source:DC Voltage:Voltage Level Range | 20 V |  |
| Source:Output Connected | TRUE |  |
| Source:Output Cutoff:Current Change Limit High |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |
| Source:Output Cutoff:Delay | 0.0 |  |
| Source:Output Cutoff:Enabled |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |
| Source:Output Enabled | TRUE[3] |  |
| Source:Output Function | DC Voltage |  |
| Source:Output Resistance | 0 Ω |  |
| Source:Pulse Current:Pulse Bias Current Level | 0 A |  |
| Source:Pulse Current:Pulse Bias Voltage Limit | 6 V |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High | 6 V |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low | -6 V |  |
| Source:Pulse Current:Pulse Current Level | 0 A |  |
| Source:Pulse Current:Pulse Current Level Range | 1 A |  |
| Source:Pulse Current:Pulse Voltage Limit | 20 V |  |
| Source:Pulse Current:Pulse Voltage Limit High | 20 V |  |
| Source:Pulse Current:Pulse Voltage Limit Low | -20 V |  |
| Source:Pulse Current:Pulse Voltage Limit Range | 20 V |  |
| Source:Pulse Voltage:Pulse Bias Current Limit | 100 mA |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High | 100 mA |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low | -100 mA |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level | 0 V |  |
| Source:Pulse Voltage:Pulse Current Limit | 100 mA |  |
| Source:Pulse Voltage:Pulse Current Limit High | 100 mA |  |
| Source:Pulse Voltage:Pulse Current Limit Low | -100 mA |  |
| Source:Pulse Voltage:Pulse Current Limit Range | 100 mA |  |
| Source:Pulse Voltage:Pulse Voltage Level | 0 V |  |
| Source:Pulse Voltage:Pulse Voltage Level Range | 20 V |  |
| Source:Source Mode | Single Point |  |
| Source:Transient Response | Normal |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Measure Trigger:Export Output Terminal | "" |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge |  |
| Triggers:Pulse Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Pulse Trigger:Export Output Terminal | "" |  |
| Triggers:Pulse Trigger:Trigger Type | Digital Edge |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Source Trigger:Export Output Terminal | "" |  |
| Triggers:Source Trigger:Trigger Type | None |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Start Trigger:Export Output Terminal | "" |  |
| Triggers:Start Trigger:Trigger Type | None |  |

1

Write to EEPROM

2

On Demand

Single Point

Automatically After Source Complete

Sequence

3

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Write to EEPROM is the only valid value.

<sup>2</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>3</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4136-4137.html language=enus -->
## TOPIC 00345: Properties Supported by the PXIe-4136/4137

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4136-4137.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4136-4137.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4136/4137 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4136 PXIe-4137 Supports Advanced Sequence (PXIe-4136) Supports Advanced Seque

### Properties Supported by the PXIe-4136/4137

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4136/4137 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4136 | PXIe-4137 | Supports Advanced Sequence (PXIe-4136) | Supports Advanced Sequence (PXIe-4137) |
| --- | --- | --- | --- | --- |
| Active Channel | "" | "" |  |  |
| Advanced:Auxiliary Power Source Available | N/A | N/A |  |  |
| Advanced:Interlock Input Open | N/A | N/A |  |  |
| Advanced:Isolation State |  |  |  |  |
| Advanced:Power Source | Internal | Internal |  |  |
| Advanced:Power Source In Use | N/A | N/A |  |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM[1] | Write to EEPROM[1] |  |  |
| Device Specific:LCR:Cable Length |  |  |  |  |
| Events:Measure Complete Event:Event Delay | 0 | 0 |  |  |
| Events:Measure Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Measure Complete Event:Output Terminal | "" | "" |  |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Pulse Complete Event:Output Terminal | "" | "" |  |  |
| Events:Pulse Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Pulse Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal | "" | "" |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Source Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Source Complete Event:Output Terminal | "" | "" |  |  |
| Events:Source Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Source Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Source Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |  |  |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |  |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |  |  |
| LCR:AC Stimulus:Frequency |  |  |  |  |
| LCR:AC Stimulus:Function |  |  |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |  |  |
| LCR:Compensation:Load:Enabled |  |  |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |  |  |
| LCR:Compensation:Open:Conductance |  |  |  |  |
| LCR:Compensation:Open:Enabled |  |  |  |  |
| LCR:Compensation:Open:Susceptance |  |  |  |  |
| LCR:Compensation:Short:Enabled |  |  |  |  |
| LCR:Compensation:Short:Reactance |  |  |  |  |
| LCR:Compensation:Short:Resistance |  |  |  |  |
| LCR:Custom Measurement Time |  |  |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |  |  |
| LCR:DC Bias:Current Level |  |  |  |  |
| LCR:DC Bias:Source |  |  |  |  |
| LCR:DC Bias:Voltage Level |  |  |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |  |  |
| LCR:Impedance Range:Impedance Range |  |  |  |  |
| LCR:Instrument Mode | SMU PS | SMU PS |  |  |
| LCR:Measurement Time |  |  |  |  |
| LCR:Source Delay Mode |  |  |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode | Auto | Auto |  |  |
| Measurement:Advanced:Autorange Behavior | Range up to limit then down | Range up to limit then down |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change | 0.5 s | 0.5 s |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time | 0 s | 0 s |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Advanced:Autorange Minimum Current Range | 0 | 0 |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range | 0 | 0 |  |  |
| Measurement:Advanced:Autorange Threshold Mode | Normal | Normal |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal[2] | Normal |  |  |
| Measurement:Advanced:Measure Buffer Size | 1800000 | 1800000 |  |  |
| Measurement:Advanced:Measure When | On Demand[3] | On Demand[3] |  |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |  |  |
| Measurement:Aperture Time Auto Mode | Off | Off |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Auto Zero | Off | Off |  |  |
| Measurement:Autorange | FALSE | FALSE |  |  |
| Measurement:Fetch Backlog | N/A | N/A |  |  |
| Measurement:Measure Record Delta Time | N/A | N/A |  |  |
| Measurement:Measure Record Length | 1 | 1 |  |  |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |  |  |
| Measurement:Power Line Frequency | 60 Hertz | 60 Hertz |  |  |
| Measurement:Samples To Average | 1 | 1 |  |  |
| Measurement:Sense | Local | Local |  |  |
| Source:Advanced:Active Advanced Sequence | "" | "" |  |  |
| Source:Advanced:Active Advanced Sequence Step | 0 | 0 |  |  |
| Source:Advanced:Actual Power Allocation |  |  |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |  |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |  |  |
| Source:Advanced:Merged Channels |  |  |  |  |
| Source:Advanced:OVP Enabled | FALSE | FALSE |  |  |
| Source:Advanced:OVP Limit | 210 V | 210 V |  |  |
| Source:Advanced:Output Capacitance |  |  |  |  |
| Source:Advanced:Output Shorted |  |  |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Power Allocation Mode |  |  |  |  |
| Source:Advanced:Pulse Bias Delay | 16.67 mS | 16.67 mS |  |  |
| Source:Advanced:Pulse Off Time | 34 ms | 34 ms |  |  |
| Source:Advanced:Pulse On Time | 34 ms | 34 ms |  |  |
| Source:Advanced:Requested Power Allocation |  |  |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |  |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |  |  |
| Source:Advanced:Sequence Step Delta Time | 50 ms | 50 ms |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Source Delay | 0.01666666 s | 0.01666666 s |  |  |
| Source:Constant Power:Current Limit |  |  |  |  |
| Source:Constant Power:Level |  |  |  |  |
| Source:Constant Power:Level Range |  |  |  |  |
| Source:Constant Resistance:Current Limit |  |  |  |  |
| Source:Constant Resistance:Level |  |  |  |  |
| Source:Constant Resistance:Level Range |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:DC Current:Current Level | 0.0 | 0.0 |  |  |
| Source:DC Current:Current Level Autorange | Off | Off |  |  |
| Source:DC Current:Current Level Range | 3 | 3 |  |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |  |  |
| Source:DC Current:Voltage Limit | 6 | 6 |  |  |
| Source:DC Current:Voltage Limit Autorange | Off | Off |  |  |
| Source:DC Current:Voltage Limit High | 6 | 6 |  |  |
| Source:DC Current:Voltage Limit Low | -6 | -6 |  |  |
| Source:DC Current:Voltage Limit Range | 6 | 6 |  |  |
| Source:DC Voltage:Current Limit | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Autorange | Off | Off |  |  |
| Source:DC Voltage:Current Limit High | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Low | -0.1 | -0.1 |  |  |
| Source:DC Voltage:Current Limit Range | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Voltage Level | 0 | 0 |  |  |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |  |  |
| Source:DC Voltage:Voltage Level Range | 6 | 6 |  |  |
| Source:Output Connected | TRUE | TRUE |  |  |
| Source:Output Cutoff:Current Change Limit High |  |  |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |  |  |
| Source:Output Cutoff:Delay | 0.0 | 0.0 |  |  |
| Source:Output Cutoff:Enabled |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |  |  |
| Source:Output Enabled | TRUE[4] | TRUE[4] |  |  |
| Source:Output Function | DC Voltage | DC Voltage |  |  |
| Source:Output Resistance |  | 0.0 |  |  |
| Source:Pulse Current:Pulse Bias Current Level | 0 A | 0 A |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low | -6 V | -6 V |  |  |
| Source:Pulse Current:Pulse Current Level | 0 A | 0 A |  |  |
| Source:Pulse Current:Pulse Current Level Range | 10 A | 10 A |  |  |
| Source:Pulse Current:Pulse Voltage Limit | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Voltage Limit High | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low | -6 V | -6 V |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range | 6 V | 6 V |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low | -100 mA | -100 mA |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level | 0 V | 0 V |  |  |
| Source:Pulse Voltage:Pulse Current Limit | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Current Limit High | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low | -100 mA | -100 mA |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range | 3 A | 3 A |  |  |
| Source:Pulse Voltage:Pulse Voltage Level | 0 V | 0 V |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range | 6 V | 6 V |  |  |
| Source:Source Mode | Single Point | Single Point |  |  |
| Source:Transient Response | Normal | Normal |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Pulse Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Pulse Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Trigger Type | None | None |  |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Trigger Type | None | None |  |  |

1

Write to EEPROM

2

Normal

3

On Demand

Single Point

Automatically After Source Complete

Sequence

4

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Write to EEPROM is the only valid value.

<sup>2</sup> 
 Normal is the only valid value.

<sup>3</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>4</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4138-4139.html language=enus -->
## TOPIC 00346: Properties Supported by the PXIe-4138/4139

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4138-4139.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4138-4139.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4138/4139 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4138 PXIe-4139 Supports Advanced Sequence (PXIe-4138) Supports Advanced Seque

### Properties Supported by the PXIe-4138/4139

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4138/4139 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4138 | PXIe-4139 | Supports Advanced Sequence (PXIe-4138) | Supports Advanced Sequence (PXIe-4139) |
| --- | --- | --- | --- | --- |
| Active Channel | "" | "" |  |  |
| Advanced:Auxiliary Power Source Available | N/A | N/A |  |  |
| Advanced:Interlock Input Open |  |  |  |  |
| Advanced:Isolation State |  |  |  |  |
| Advanced:Power Source | Internal | Internal |  |  |
| Advanced:Power Source In Use | N/A | N/A |  |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM[1] | Write to EEPROM[1] |  |  |
| Device Specific:LCR:Cable Length |  |  |  |  |
| Events:Measure Complete Event:Event Delay | 0 | 0 |  |  |
| Events:Measure Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Measure Complete Event:Output Terminal | "" | "" |  |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Pulse Complete Event:Output Terminal | "" | "" |  |  |
| Events:Pulse Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Pulse Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal | "" | "" |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Source Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Source Complete Event:Output Terminal | "" | "" |  |  |
| Events:Source Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Source Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Source Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |  |  |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |  |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |  |  |
| LCR:AC Stimulus:Frequency |  |  |  |  |
| LCR:AC Stimulus:Function |  |  |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |  |  |
| LCR:Compensation:Load:Enabled |  |  |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |  |  |
| LCR:Compensation:Open:Conductance |  |  |  |  |
| LCR:Compensation:Open:Enabled |  |  |  |  |
| LCR:Compensation:Open:Susceptance |  |  |  |  |
| LCR:Compensation:Short:Enabled |  |  |  |  |
| LCR:Compensation:Short:Reactance |  |  |  |  |
| LCR:Compensation:Short:Resistance |  |  |  |  |
| LCR:Custom Measurement Time |  |  |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |  |  |
| LCR:DC Bias:Current Level |  |  |  |  |
| LCR:DC Bias:Source |  |  |  |  |
| LCR:DC Bias:Voltage Level |  |  |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |  |  |
| LCR:Impedance Range:Impedance Range |  |  |  |  |
| LCR:Instrument Mode | SMU PS | SMU PS |  |  |
| LCR:Measurement Time |  |  |  |  |
| LCR:Source Delay Mode |  |  |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode | Auto | Auto |  |  |
| Measurement:Advanced:Autorange Behavior | Range up to limit then down | Range up to limit then down |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change | 0.5 s | 0.5 s |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time | 0 s | 0 s |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Advanced:Autorange Minimum Current Range | 0 | 0 |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range | 0 | 0 |  |  |
| Measurement:Advanced:Autorange Threshold Mode | Normal | Normal |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal[2] | Normal |  |  |
| Measurement:Advanced:Measure Buffer Size | 1800000 | 1800000 |  |  |
| Measurement:Advanced:Measure When | On Demand[3] | On Demand[3] |  |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |  |  |
| Measurement:Aperture Time Auto Mode |  |  |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Auto Zero | Off | Off |  |  |
| Measurement:Autorange | Off | Off |  |  |
| Measurement:Fetch Backlog | N/A | N/A |  |  |
| Measurement:Measure Record Delta Time | N/A | N/A |  |  |
| Measurement:Measure Record Length | 1 | 1 |  |  |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |  |  |
| Measurement:Power Line Frequency | 60 Hertz | 60 Hertz |  |  |
| Measurement:Samples To Average | 1 | 1 |  |  |
| Measurement:Sense | Local | Local |  |  |
| Source:Advanced:Active Advanced Sequence | "" | "" |  |  |
| Source:Advanced:Active Advanced Sequence Step | 0 | 0 |  |  |
| Source:Advanced:Actual Power Allocation |  |  |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |  |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |  |  |
| Source:Advanced:Merged Channels |  |  |  |  |
| Source:Advanced:OVP Enabled |  |  |  |  |
| Source:Advanced:OVP Limit |  |  |  |  |
| Source:Advanced:Output Capacitance |  |  |  |  |
| Source:Advanced:Output Shorted |  |  |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Power Allocation Mode |  |  |  |  |
| Source:Advanced:Pulse Bias Delay | 16.67 mS | 16.67 mS |  |  |
| Source:Advanced:Pulse Off Time | 34 ms | 34 ms |  |  |
| Source:Advanced:Pulse On Time | 34 ms | 34 ms |  |  |
| Source:Advanced:Requested Power Allocation |  |  |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |  |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |  |  |
| Source:Advanced:Sequence Step Delta Time | 50 ms | 50 ms |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Source Delay | 0.01666666 s | 0.01666666 s |  |  |
| Source:Constant Power:Current Limit |  |  |  |  |
| Source:Constant Power:Level |  |  |  |  |
| Source:Constant Power:Level Range |  |  |  |  |
| Source:Constant Resistance:Current Limit |  |  |  |  |
| Source:Constant Resistance:Level |  |  |  |  |
| Source:Constant Resistance:Level Range |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:DC Current:Current Level | 0.0 | 0.0 |  |  |
| Source:DC Current:Current Level Autorange | Off | Off |  |  |
| Source:DC Current:Current Level Range | 3 | 3 |  |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |  |  |
| Source:DC Current:Voltage Limit | 6 | 6 |  |  |
| Source:DC Current:Voltage Limit Autorange | Off | Off |  |  |
| Source:DC Current:Voltage Limit High | 6 | 6 |  |  |
| Source:DC Current:Voltage Limit Low | -6 | -6 |  |  |
| Source:DC Current:Voltage Limit Range | 6 | 6 |  |  |
| Source:DC Voltage:Current Limit | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Autorange | Off | Off |  |  |
| Source:DC Voltage:Current Limit High | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Low | -0.1 | -0.1 |  |  |
| Source:DC Voltage:Current Limit Range | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Voltage Level | 0 | 0 |  |  |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |  |  |
| Source:DC Voltage:Voltage Level Range | 6 | 6 |  |  |
| Source:Output Connected | TRUE | TRUE |  |  |
| Source:Output Cutoff:Current Change Limit High |  |  |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |  |  |
| Source:Output Cutoff:Delay | 0.0 | 0.0 |  |  |
| Source:Output Cutoff:Enabled |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |  |  |
| Source:Output Enabled | TRUE[4] | TRUE[4] |  |  |
| Source:Output Function | DC Voltage | DC Voltage |  |  |
| Source:Output Resistance |  | 0.0 |  |  |
| Source:Pulse Current:Pulse Bias Current Level | 0 A | 0 A |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low | -6 V | -6 V |  |  |
| Source:Pulse Current:Pulse Current Level | 0 A | 0 A |  |  |
| Source:Pulse Current:Pulse Current Level Range | 10 A | 10 A |  |  |
| Source:Pulse Current:Pulse Voltage Limit | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Voltage Limit High | 6 V | 6 V |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low | -6 V | -6 V |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range | 6 V | 6 V |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low | -100 mA | -100 mA |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level | 0 V | 0 V |  |  |
| Source:Pulse Voltage:Pulse Current Limit | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Current Limit High | 100 mA | 100 mA |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low | -100 mA | -100 mA |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range | 3 A | 3 A |  |  |
| Source:Pulse Voltage:Pulse Voltage Level | 0 V | 0 V |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range | 6 V | 6 V |  |  |
| Source:Source Mode | Single Point | Single Point |  |  |
| Source:Transient Response | Normal | Normal |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Pulse Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Pulse Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  | Rising |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  | "" |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  | Digital Edge |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Trigger Type | None | None |  |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Trigger Type | None | None |  |  |

1

Write to EEPROM

2

Normal

3

On Demand

Single Point

Automatically After Source Complete

Sequence

4

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Write to EEPROM is the only valid value.

<sup>2</sup> 
 Normal is the only valid value.

<sup>3</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>4</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4140-4141.html language=enus -->
## TOPIC 00347: Properties Supported by the PXIe-4140/4141

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4140-4141.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4140-4141.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4140/4141 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4140 PXIe-4141 Supports Advanced Sequence (PXIe-4140) Supports Advanced Seque

### Properties Supported by the PXIe-4140/4141

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4140/4141 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4140 | PXIe-4141 | Supports Advanced Sequence (PXIe-4140) | Supports Advanced Sequence (PXIe-4141) |
| --- | --- | --- | --- | --- |
| Active Channel | "" | "" |  |  |
| Advanced:Auxiliary Power Source Available | N/A | N/A |  |  |
| Advanced:Interlock Input Open |  |  |  |  |
| Advanced:Isolation State |  |  |  |  |
| Advanced:Power Source | Internal | Internal |  |  |
| Advanced:Power Source In Use | N/A | N/A |  |  |
| Advanced:Self-Calibration Persistence | Keep in Memory | Keep in Memory |  |  |
| Device Specific:LCR:Cable Length |  |  |  |  |
| Events:Measure Complete Event:Event Delay | 0 | 0 |  |  |
| Events:Measure Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Measure Complete Event:Output Terminal | "" | "" |  |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Pulse Complete Event:Output Terminal |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Source Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Source Complete Event:Output Terminal | "" | "" |  |  |
| Events:Source Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Source Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Source Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |  |  |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |  |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |  |  |
| LCR:AC Stimulus:Frequency |  |  |  |  |
| LCR:AC Stimulus:Function |  |  |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |  |  |
| LCR:Compensation:Load:Enabled |  |  |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |  |  |
| LCR:Compensation:Open:Conductance |  |  |  |  |
| LCR:Compensation:Open:Enabled |  |  |  |  |
| LCR:Compensation:Open:Susceptance |  |  |  |  |
| LCR:Compensation:Short:Enabled |  |  |  |  |
| LCR:Compensation:Short:Reactance |  |  |  |  |
| LCR:Compensation:Short:Resistance |  |  |  |  |
| LCR:Custom Measurement Time |  |  |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |  |  |
| LCR:DC Bias:Current Level |  |  |  |  |
| LCR:DC Bias:Source |  |  |  |  |
| LCR:DC Bias:Voltage Level |  |  |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |  |  |
| LCR:Impedance Range:Impedance Range |  |  |  |  |
| LCR:Instrument Mode | SMU PS | SMU PS |  |  |
| LCR:Measurement Time |  |  |  |  |
| LCR:Source Delay Mode |  |  |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |  |  |  |
| Measurement:Advanced:Autorange Behavior |  |  |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |  |  |  |
| Measurement:Advanced:Autorange Threshold Mode |  |  |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal[1] | Normal |  |  |
| Measurement:Advanced:Measure Buffer Size | 600000 | 600000 |  |  |
| Measurement:Advanced:Measure When | On Demand[2] | On Demand[2] |  |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |  |  |
| Measurement:Aperture Time Auto Mode |  |  |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Auto Zero | Off | Off |  |  |
| Measurement:Autorange |  |  |  |  |
| Measurement:Fetch Backlog | N/A | N/A |  |  |
| Measurement:Measure Record Delta Time | N/A | N/A |  |  |
| Measurement:Measure Record Length | 1 | 1 |  |  |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |  |  |
| Measurement:Power Line Frequency | 60 Hertz | 60 Hertz |  |  |
| Measurement:Samples To Average | 1 | 1 |  |  |
| Measurement:Sense | Local | Local |  |  |
| Source:Advanced:Active Advanced Sequence | "" | "" |  |  |
| Source:Advanced:Active Advanced Sequence Step | 0 | 0 |  |  |
| Source:Advanced:Actual Power Allocation |  |  |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |  |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |  |  |
| Source:Advanced:Merged Channels |  |  |  |  |
| Source:Advanced:OVP Enabled |  |  |  |  |
| Source:Advanced:OVP Limit |  |  |  |  |
| Source:Advanced:Output Capacitance | High[3] | High[3] |  |  |
| Source:Advanced:Output Shorted |  |  |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Power Allocation Mode |  |  |  |  |
| Source:Advanced:Pulse Bias Delay |  |  |  |  |
| Source:Advanced:Pulse Off Time |  |  |  |  |
| Source:Advanced:Pulse On Time |  |  |  |  |
| Source:Advanced:Requested Power Allocation |  |  |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |  |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |  |  |
| Source:Advanced:Sequence Step Delta Time | 50 ms | 50 ms |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Source Delay | 0.01666666 s | 0.01666666 s |  |  |
| Source:Constant Power:Current Limit |  |  |  |  |
| Source:Constant Power:Level |  |  |  |  |
| Source:Constant Power:Level Range |  |  |  |  |
| Source:Constant Resistance:Current Limit |  |  |  |  |
| Source:Constant Resistance:Level |  |  |  |  |
| Source:Constant Resistance:Level Range |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:DC Current:Current Level | 0.1 | 0.1 |  |  |
| Source:DC Current:Current Level Autorange | Off | Off |  |  |
| Source:DC Current:Current Level Range | 0.1 | 0.1 |  |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |  |  |
| Source:DC Current:Voltage Limit | 10 | 10 |  |  |
| Source:DC Current:Voltage Limit Autorange | Off | Off |  |  |
| Source:DC Current:Voltage Limit High | 10 | 10 |  |  |
| Source:DC Current:Voltage Limit Low | -10 | -10 |  |  |
| Source:DC Current:Voltage Limit Range | 10 | 10 |  |  |
| Source:DC Voltage:Current Limit | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Autorange | Off | Off |  |  |
| Source:DC Voltage:Current Limit High | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Low | -0.1 | -0.1 |  |  |
| Source:DC Voltage:Current Limit Range | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Voltage Level | 0 | 0 |  |  |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |  |  |
| Source:DC Voltage:Voltage Level Range | 10 | 10 |  |  |
| Source:Output Connected |  |  |  |  |
| Source:Output Cutoff:Current Change Limit High |  |  |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |  |  |
| Source:Output Cutoff:Delay |  |  |  |  |
| Source:Output Cutoff:Enabled |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |  |  |
| Source:Output Enabled | TRUE[4] | TRUE[4] |  |  |
| Source:Output Function | DC Voltage | DC Voltage |  |  |
| Source:Output Resistance |  | 0.0 |  |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |  |  |
| Source:Source Mode | Single Point | Single Point |  |  |
| Source:Transient Response | Normal | Normal |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Trigger Type | None | None |  |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Trigger Type | None | None |  |  |

1

Normal

2

On Demand

Single Point

Automatically After Source Complete

Sequence

3

High

4

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> Normal is the only valid value.

<sup>2</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>3</sup> High is the only valid value.

<sup>4</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4142-4143.html language=enus -->
## TOPIC 00348: Properties Supported by the PXIe-4142/4143

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4142-4143.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4142-4143.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4142/4143 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4142 PXIe-4143 Supports Advanced Sequence (PXIe-4142) Supports Advanced Seque

### Properties Supported by the PXIe-4142/4143

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4142/4143 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4142 | PXIe-4143 | Supports Advanced Sequence (PXIe-4142) | Supports Advanced Sequence (PXIe-4143) |
| --- | --- | --- | --- | --- |
| Active Channel | "" | "" |  |  |
| Advanced:Auxiliary Power Source Available | N/A | N/A |  |  |
| Advanced:Interlock Input Open |  |  |  |  |
| Advanced:Isolation State |  |  |  |  |
| Advanced:Power Source | Internal | Internal |  |  |
| Advanced:Power Source In Use | N/A | N/A |  |  |
| Advanced:Self-Calibration Persistence | Keep in Memory | Keep in Memory |  |  |
| Device Specific:LCR:Cable Length |  |  |  |  |
| Events:Measure Complete Event:Event Delay | 0 | 0 |  |  |
| Events:Measure Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Measure Complete Event:Output Terminal | "" | "" |  |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Pulse Complete Event:Output Terminal |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Source Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Source Complete Event:Output Terminal | "" | "" |  |  |
| Events:Source Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Source Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Source Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |  |  |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |  |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |  |  |
| LCR:AC Stimulus:Frequency |  |  |  |  |
| LCR:AC Stimulus:Function |  |  |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |  |  |
| LCR:Compensation:Load:Enabled |  |  |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |  |  |
| LCR:Compensation:Open:Conductance |  |  |  |  |
| LCR:Compensation:Open:Enabled |  |  |  |  |
| LCR:Compensation:Open:Susceptance |  |  |  |  |
| LCR:Compensation:Short:Enabled |  |  |  |  |
| LCR:Compensation:Short:Reactance |  |  |  |  |
| LCR:Compensation:Short:Resistance |  |  |  |  |
| LCR:Custom Measurement Time |  |  |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |  |  |
| LCR:DC Bias:Current Level |  |  |  |  |
| LCR:DC Bias:Source |  |  |  |  |
| LCR:DC Bias:Voltage Level |  |  |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |  |  |
| LCR:Impedance Range:Impedance Range |  |  |  |  |
| LCR:Instrument Mode | SMU PS | SMU PS |  |  |
| LCR:Measurement Time |  |  |  |  |
| LCR:Source Delay Mode |  |  |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |  |  |  |
| Measurement:Advanced:Autorange Behavior |  |  |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |  |  |  |
| Measurement:Advanced:Autorange Threshold Mode |  |  |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal[1] | Normal |  |  |
| Measurement:Advanced:Measure Buffer Size | 600000 | 600000 |  |  |
| Measurement:Advanced:Measure When | On Demand[2] | On Demand[2] |  |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |  |  |
| Measurement:Aperture Time Auto Mode |  |  |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Auto Zero | Off | Off |  |  |
| Measurement:Autorange |  |  |  |  |
| Measurement:Fetch Backlog | N/A | N/A |  |  |
| Measurement:Measure Record Delta Time | N/A | N/A |  |  |
| Measurement:Measure Record Length | 1 | 1 |  |  |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |  |  |
| Measurement:Power Line Frequency | 60 Hertz | 60 Hertz |  |  |
| Measurement:Samples To Average | 1 | 1 |  |  |
| Measurement:Sense | Local | Local |  |  |
| Source:Advanced:Active Advanced Sequence | "" | "" |  |  |
| Source:Advanced:Active Advanced Sequence Step | 0 | 0 |  |  |
| Source:Advanced:Actual Power Allocation |  |  |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |  |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |  |  |
| Source:Advanced:Merged Channels |  |  |  |  |
| Source:Advanced:OVP Enabled |  |  |  |  |
| Source:Advanced:OVP Limit |  |  |  |  |
| Source:Advanced:Output Capacitance |  |  |  |  |
| Source:Advanced:Output Shorted |  |  |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Power Allocation Mode |  |  |  |  |
| Source:Advanced:Pulse Bias Delay |  |  |  |  |
| Source:Advanced:Pulse Off Time |  |  |  |  |
| Source:Advanced:Pulse On Time |  |  |  |  |
| Source:Advanced:Requested Power Allocation |  |  |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |  |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |  |  |
| Source:Advanced:Sequence Step Delta Time | 50 ms | 50 ms |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Source Delay | 0.01666666 s | 0.01666666 s |  |  |
| Source:Constant Power:Current Limit |  |  |  |  |
| Source:Constant Power:Level |  |  |  |  |
| Source:Constant Power:Level Range |  |  |  |  |
| Source:Constant Resistance:Current Limit |  |  |  |  |
| Source:Constant Resistance:Level |  |  |  |  |
| Source:Constant Resistance:Level Range |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:DC Current:Current Level | 0.1 | 0.1 |  |  |
| Source:DC Current:Current Level Autorange | Off | Off |  |  |
| Source:DC Current:Current Level Range | 0.1 | 0.1 |  |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |  |  |
| Source:DC Current:Voltage Limit | 10 | 10 |  |  |
| Source:DC Current:Voltage Limit Autorange | Off | Off |  |  |
| Source:DC Current:Voltage Limit High | 10 | 10 |  |  |
| Source:DC Current:Voltage Limit Low | -10 | -10 |  |  |
| Source:DC Current:Voltage Limit Range | 10 | 10 |  |  |
| Source:DC Voltage:Current Limit | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Autorange | Off | Off |  |  |
| Source:DC Voltage:Current Limit High | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Low | -0.1 | -0.1 |  |  |
| Source:DC Voltage:Current Limit Range | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Voltage Level | 0 | 0 |  |  |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |  |  |
| Source:DC Voltage:Voltage Level Range | 10 | 10 |  |  |
| Source:Output Connected |  |  |  |  |
| Source:Output Cutoff:Current Change Limit High |  |  |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |  |  |
| Source:Output Cutoff:Delay |  |  |  |  |
| Source:Output Cutoff:Enabled |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |  |  |
| Source:Output Enabled | TRUE[3] | TRUE[3] |  |  |
| Source:Output Function | DC Voltage | DC Voltage |  |  |
| Source:Output Resistance |  | 0.0 |  |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |  |  |
| Source:Source Mode | Single Point | Single Point |  |  |
| Source:Transient Response | Normal | Normal |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Trigger Type | None | None |  |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Trigger Type | None | None |  |  |

1

Normal

2

On Demand

Single Point

Automatically After Source Complete

Sequence

3

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> Normal is the only valid value.

<sup>2</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>3</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4144-4145.html language=enus -->
## TOPIC 00349: Properties Supported by the PXIe-4144/4145

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4144-4145.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4144-4145.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4144/4145 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4144 PXIe-4145 Supports Advanced Sequence (PXIe-4144) Supports Advanced Seque

### Properties Supported by the PXIe-4144/4145

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4144/4145 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4144 | PXIe-4145 | Supports Advanced Sequence (PXIe-4144) | Supports Advanced Sequence (PXIe-4145) |
| --- | --- | --- | --- | --- |
| Active Channel | "" | "" |  |  |
| Advanced:Auxiliary Power Source Available | N/A | N/A |  |  |
| Advanced:Interlock Input Open |  |  |  |  |
| Advanced:Isolation State |  |  |  |  |
| Advanced:Power Source | Internal | Internal |  |  |
| Advanced:Power Source In Use | N/A | N/A |  |  |
| Advanced:Self-Calibration Persistence | Keep in Memory | Keep in Memory |  |  |
| Device Specific:LCR:Cable Length |  |  |  |  |
| Events:Measure Complete Event:Event Delay | 0 | 0 |  |  |
| Events:Measure Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Measure Complete Event:Output Terminal | "" | "" |  |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Pulse Complete Event:Output Terminal |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Source Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Source Complete Event:Output Terminal | "" | "" |  |  |
| Events:Source Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Source Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Source Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |  |  |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |  |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |  |  |
| LCR:AC Stimulus:Frequency |  |  |  |  |
| LCR:AC Stimulus:Function |  |  |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |  |  |
| LCR:Compensation:Load:Enabled |  |  |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |  |  |
| LCR:Compensation:Open:Conductance |  |  |  |  |
| LCR:Compensation:Open:Enabled |  |  |  |  |
| LCR:Compensation:Open:Susceptance |  |  |  |  |
| LCR:Compensation:Short:Enabled |  |  |  |  |
| LCR:Compensation:Short:Reactance |  |  |  |  |
| LCR:Compensation:Short:Resistance |  |  |  |  |
| LCR:Custom Measurement Time |  |  |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |  |  |
| LCR:DC Bias:Current Level |  |  |  |  |
| LCR:DC Bias:Source |  |  |  |  |
| LCR:DC Bias:Voltage Level |  |  |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |  |  |
| LCR:Impedance Range:Impedance Range |  |  |  |  |
| LCR:Instrument Mode | SMU PS | SMU PS |  |  |
| LCR:Measurement Time |  |  |  |  |
| LCR:Source Delay Mode |  |  |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |  |  |  |
| Measurement:Advanced:Autorange Behavior |  |  |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |  |  |  |
| Measurement:Advanced:Autorange Threshold Mode |  |  |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal[1] | Normal |  |  |
| Measurement:Advanced:Measure Buffer Size | 600000 | 600000 |  |  |
| Measurement:Advanced:Measure When | On Demand[2] | On Demand[2] |  |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |  |  |
| Measurement:Aperture Time Auto Mode |  |  |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Auto Zero | Off | Off |  |  |
| Measurement:Autorange |  |  |  |  |
| Measurement:Fetch Backlog | N/A | N/A |  |  |
| Measurement:Measure Record Delta Time | N/A | N/A |  |  |
| Measurement:Measure Record Length | 1 | 1 |  |  |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |  |  |
| Measurement:Power Line Frequency | 60 Hertz | 60 Hertz |  |  |
| Measurement:Samples To Average | 1 | 1 |  |  |
| Measurement:Sense | Local | Local |  |  |
| Source:Advanced:Active Advanced Sequence | "" | "" |  |  |
| Source:Advanced:Active Advanced Sequence Step | 0 | 0 |  |  |
| Source:Advanced:Actual Power Allocation |  |  |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |  |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |  |  |
| Source:Advanced:Merged Channels |  |  |  |  |
| Source:Advanced:OVP Enabled |  |  |  |  |
| Source:Advanced:OVP Limit |  |  |  |  |
| Source:Advanced:Output Capacitance |  |  |  |  |
| Source:Advanced:Output Shorted |  |  |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Power Allocation Mode |  |  |  |  |
| Source:Advanced:Pulse Bias Delay |  |  |  |  |
| Source:Advanced:Pulse Off Time |  |  |  |  |
| Source:Advanced:Pulse On Time |  |  |  |  |
| Source:Advanced:Requested Power Allocation |  |  |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |  |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |  |  |
| Source:Advanced:Sequence Step Delta Time | 50 ms | 50 ms |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Source Delay | 0.01666666 s | 0.01666666 s |  |  |
| Source:Constant Power:Current Limit |  |  |  |  |
| Source:Constant Power:Level |  |  |  |  |
| Source:Constant Power:Level Range |  |  |  |  |
| Source:Constant Resistance:Current Limit |  |  |  |  |
| Source:Constant Resistance:Level |  |  |  |  |
| Source:Constant Resistance:Level Range |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:DC Current:Current Level | 0.1 | 0.1 |  |  |
| Source:DC Current:Current Level Autorange | Off | Off |  |  |
| Source:DC Current:Current Level Range | 0.1 | 0.1 |  |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |  |  |
| Source:DC Current:Voltage Limit | 6 | 6 |  |  |
| Source:DC Current:Voltage Limit Autorange | Off | Off |  |  |
| Source:DC Current:Voltage Limit High | 6 | 6 |  |  |
| Source:DC Current:Voltage Limit Low | -6 | -6 |  |  |
| Source:DC Current:Voltage Limit Range | 6 | 6 |  |  |
| Source:DC Voltage:Current Limit | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Autorange | Off | Off |  |  |
| Source:DC Voltage:Current Limit High | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Current Limit Low | -0.1 | -0.1 |  |  |
| Source:DC Voltage:Current Limit Range | 0.1 | 0.1 |  |  |
| Source:DC Voltage:Voltage Level | 0 | 0 |  |  |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |  |  |
| Source:DC Voltage:Voltage Level Range | 6 | 6 |  |  |
| Source:Output Connected |  |  |  |  |
| Source:Output Cutoff:Current Change Limit High |  |  |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |  |  |
| Source:Output Cutoff:Delay |  |  |  |  |
| Source:Output Cutoff:Enabled |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |  |  |
| Source:Output Enabled | TRUE[3] | TRUE[3] |  |  |
| Source:Output Function | DC Voltage | DC Voltage |  |  |
| Source:Output Resistance |  | 0.0 |  |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |  |  |
| Source:Source Mode | Single Point | Single Point |  |  |
| Source:Transient Response | Normal | Normal |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Trigger Type | None | None |  |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Trigger Type | None | None |  |  |

1

Normal

2

On Demand

Single Point

Automatically After Source Complete

Sequence

3

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Normal is the only valid value.

<sup>2</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>3</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4147.html language=enus -->
## TOPIC 00350: Properties Supported by the PXIe-4147

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4147.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4147.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4147 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4147 Supports Advanced Sequence Active Channel "" Advanced:Auxiliary Power Source

### Properties Supported by the PXIe-4147

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4147 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4147 | Supports Advanced Sequence |
| --- | --- | --- |
| Active Channel | "" |  |
| Advanced:Auxiliary Power Source Available | N/A |  |
| Advanced:Interlock Input Open |  |  |
| Advanced:Isolation State |  |  |
| Advanced:Power Source | Internal |  |
| Advanced:Power Source In Use | N/A |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM |  |
| Device Specific:LCR:Cable Length |  |  |
| Events:Measure Complete Event:Event Delay | 0 s |  |
| Events:Measure Complete Event:Output Behavior | N/A |  |
| Events:Measure Complete Event:Output Terminal | "" |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A |  |
| Events:Pulse Complete Event:Output Terminal |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A |  |
| Events:Sequence Engine Done Event:Output Terminal | "" |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A |  |
| Events:Source Complete Event:Output Behavior | N/A |  |
| Events:Source Complete Event:Output Terminal | "" |  |
| Events:Source Complete Event:Pulse:Polarity | Active High |  |
| Events:Source Complete Event:Pulse:Width | 250 ns |  |
| Events:Source Complete Event:Toggle:Initial State | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |  |
| Inherent IVI Attributes:User Options:Cache | TRUE |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |
| LCR:AC Stimulus:Frequency |  |  |
| LCR:AC Stimulus:Function |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |
| LCR:Compensation:Load:Enabled |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |
| LCR:Compensation:Open:Conductance |  |  |
| LCR:Compensation:Open:Enabled |  |  |
| LCR:Compensation:Open:Susceptance |  |  |
| LCR:Compensation:Short:Enabled |  |  |
| LCR:Compensation:Short:Reactance |  |  |
| LCR:Compensation:Short:Resistance |  |  |
| LCR:Custom Measurement Time |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |
| LCR:DC Bias:Current Level |  |  |
| LCR:DC Bias:Source |  |  |
| LCR:DC Bias:Voltage Level |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |
| LCR:Impedance Range:Impedance Range |  |  |
| LCR:Instrument Mode | SMU PS |  |
| LCR:Measurement Time |  |  |
| LCR:Source Delay Mode |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode | Auto |  |
| Measurement:Advanced:Autorange Behavior | Range Up To Limit Then Down |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change | 0.5 s |  |
| Measurement:Advanced:Autorange Minimum Aperture Time | 0 |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units | Seconds |  |
| Measurement:Advanced:Autorange Minimum Current Range | 0 |  |
| Measurement:Advanced:Autorange Minimum Voltage Range | 0 |  |
| Measurement:Advanced:Autorange Threshold Mode | Normal |  |
| Measurement:Advanced:DC Noise Rejection | Normal |  |
| Measurement:Advanced:Measure Buffer Size | 100096 |  |
| Measurement:Advanced:Measure When | On Demand[1] |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |
| Measurement:Aperture Time | 0.01666666 s |  |
| Measurement:Aperture Time Auto Mode |  |  |
| Measurement:Aperture Time Units | Seconds |  |
| Measurement:Auto Zero | Off |  |
| Measurement:Autorange | Off |  |
| Measurement:Fetch Backlog | N/A |  |
| Measurement:Measure Record Delta Time | N/A |  |
| Measurement:Measure Record Length | 1 |  |
| Measurement:Measure Record Length Is Finite | TRUE |  |
| Measurement:Power Line Frequency | 60 Hz |  |
| Measurement:Samples To Average | 1 |  |
| Measurement:Sense | Local |  |
| Source:Advanced:Active Advanced Sequence | "" |  |
| Source:Advanced:Active Advanced Sequence Step | 0 |  |
| Source:Advanced:Actual Power Allocation | 0 W |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |
| Source:Advanced:Merged Channels | "" |  |
| Source:Advanced:OVP Enabled |  |  |
| Source:Advanced:OVP Limit |  |  |
| Source:Advanced:Output Capacitance |  |  |
| Source:Advanced:Output Shorted |  |  |
| Source:Advanced:Overranging Enabled | FALSE |  |
| Source:Advanced:Power Allocation Mode | Automatic |  |
| Source:Advanced:Pulse Bias Delay |  |  |
| Source:Advanced:Pulse Off Time |  |  |
| Source:Advanced:Pulse On Time |  |  |
| Source:Advanced:Requested Power Allocation | 0 |  |
| Source:Advanced:Sequence Loop Count | 1 |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE |  |
| Source:Advanced:Sequence Step Delta Time | 50 ms |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE |  |
| Source:Advanced:Source Delay | 0.01666666 s |  |
| Source:Constant Power:Current Limit |  |  |
| Source:Constant Power:Level |  |  |
| Source:Constant Power:Level Range |  |  |
| Source:Constant Resistance:Current Limit |  |  |
| Source:Constant Resistance:Level |  |  |
| Source:Constant Resistance:Level Range |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:DC Current:Current Level | 0.0 |  |
| Source:DC Current:Current Level Autorange | Off |  |
| Source:DC Current:Current Level Range | 3 A |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |
| Source:DC Current:Voltage Limit | 8 V |  |
| Source:DC Current:Voltage Limit Autorange | Off |  |
| Source:DC Current:Voltage Limit High | 8 V |  |
| Source:DC Current:Voltage Limit Low | -8 V |  |
| Source:DC Current:Voltage Limit Range | 8 V |  |
| Source:DC Voltage:Current Limit | 0.001 A |  |
| Source:DC Voltage:Current Limit Autorange | Off |  |
| Source:DC Voltage:Current Limit High | 0.001 A |  |
| Source:DC Voltage:Current Limit Low | -0.001 A |  |
| Source:DC Voltage:Current Limit Range | 3 A |  |
| Source:DC Voltage:Voltage Level | 0 |  |
| Source:DC Voltage:Voltage Level Autorange | Off |  |
| Source:DC Voltage:Voltage Level Range | 8 V |  |
| Source:Output Connected | TRUE |  |
| Source:Output Cutoff:Current Change Limit High |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |
| Source:Output Cutoff:Delay |  |  |
| Source:Output Cutoff:Enabled |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |
| Source:Output Enabled | TRUE[2] |  |
| Source:Output Function | DC Voltage |  |
| Source:Output Resistance | 0.0 |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |
| Source:Source Mode | Single Point |  |
| Source:Transient Response | Normal |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Measure Trigger:Export Output Terminal | "" |  |
| Triggers:Measure Trigger:Trigger Type | None |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Source Trigger:Export Output Terminal | "" |  |
| Triggers:Source Trigger:Trigger Type | None |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Start Trigger:Export Output Terminal | "" |  |
| Triggers:Start Trigger:Trigger Type | None |  |

1

On Demand

Single Point

Automatically After Source Complete

Sequence

2

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>2</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4150-4151.html language=enus -->
## TOPIC 00351: Properties Supported by the PXIe-4150/4151

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4150-4151.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4150-4151.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4150/4151 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4150 PXIe-4151 Supports Advanced Sequence (PXIe-4150) Supports Advanced Seque

### Properties Supported by the PXIe-4150/4151

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4150/4151 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4150 | PXIe-4151 | Supports Advanced Sequence (PXIe-4150) | Supports Advanced Sequence (PXIe-4151) |
| --- | --- | --- | --- | --- |
| Active Channel | "" | "" |  |  |
| Advanced:Auxiliary Power Source Available | N/A | N/A |  |  |
| Advanced:Interlock Input Open |  |  |  |  |
| Advanced:Isolation State |  |  |  |  |
| Advanced:Power Source |  |  |  |  |
| Advanced:Power Source In Use |  |  |  |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM | Write to EEPROM |  |  |
| Device Specific:LCR:Cable Length |  |  |  |  |
| Events:Measure Complete Event:Event Delay | 0 s | 0 s |  |  |
| Events:Measure Complete Event:Output Behavior | Pulse Event Output[2] | Pulse Event Output[2] |  |  |
| Events:Measure Complete Event:Output Terminal | "" | "" |  |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High[2] | Active High[2] |  |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns[2] | 250 ns[2] |  |  |
| Events:Measure Complete Event:Toggle:Initial State | Initial State Low[2] | Initial State Low[2] |  |  |
| Events:Pulse Complete Event:Output Terminal |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |  |  |
| Events:Sequence Engine Done Event:Output Behavior | Pulse Event Output[2] | Pulse Event Output[2] |  |  |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High[2] | Active High[2] |  |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns[2] | 250 ns[2] |  |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | Initial State Low[2] | Initial State Low[2] |  |  |
| Events:Sequence Iteration Complete Event:Output Behavior | Pulse Event Output[2] | Pulse Event Output[2] |  |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High[2] | Active High[2] |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns[2] | 250 ns[2] |  |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | Initial State Low[2] | Initial State Low[2] |  |  |
| Events:Source Complete Event:Output Behavior | Pulse Event Output[2] | Pulse Event Output[2] |  |  |
| Events:Source Complete Event:Output Terminal | "" | "" |  |  |
| Events:Source Complete Event:Pulse:Polarity | Active High[2] | Active High[2] |  |  |
| Events:Source Complete Event:Pulse:Width | 250 ns[2] | 250 ns[2] |  |  |
| Events:Source Complete Event:Toggle:Initial State | Initial State Low[2] | Initial State Low[2] |  |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |  |  |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |  |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |  |  |
| LCR:AC Stimulus:Frequency |  |  |  |  |
| LCR:AC Stimulus:Function |  |  |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |  |  |
| LCR:Compensation:Load:Enabled |  |  |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |  |  |
| LCR:Compensation:Open:Conductance |  |  |  |  |
| LCR:Compensation:Open:Enabled |  |  |  |  |
| LCR:Compensation:Open:Susceptance |  |  |  |  |
| LCR:Compensation:Short:Enabled |  |  |  |  |
| LCR:Compensation:Short:Reactance |  |  |  |  |
| LCR:Compensation:Short:Resistance |  |  |  |  |
| LCR:Custom Measurement Time |  |  |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |  |  |
| LCR:DC Bias:Current Level |  |  |  |  |
| LCR:DC Bias:Source |  |  |  |  |
| LCR:DC Bias:Voltage Level |  |  |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |  |  |
| LCR:Impedance Range:Impedance Range |  |  |  |  |
| LCR:Instrument Mode | SMU PS[2] | SMU PS[2] |  |  |
| LCR:Measurement Time |  |  |  |  |
| LCR:Source Delay Mode |  |  |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |  |  |  |
| Measurement:Advanced:Autorange Behavior |  |  |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |  |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |  |  |  |
| Measurement:Advanced:Autorange Threshold Mode |  |  |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal | Normal |  |  |
| Measurement:Advanced:Measure Buffer Size | 1800130 | 1800130 |  |  |
| Measurement:Advanced:Measure When | On Demand[1] | On Demand[1] |  |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |  |  |
| Measurement:Aperture Time Auto Mode |  |  |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Auto Zero | Off[2] | Off[2] |  |  |
| Measurement:Autorange | Off[2] | Off[2] |  |  |
| Measurement:Fetch Backlog | N/A | N/A |  |  |
| Measurement:Measure Record Delta Time | N/A | N/A |  |  |
| Measurement:Measure Record Length | 1 | 1 |  |  |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |  |  |
| Measurement:Power Line Frequency | 60 Hz | 60 Hz |  |  |
| Measurement:Samples To Average | 1 | 1 |  |  |
| Measurement:Sense | Local | Local |  |  |
| Source:Advanced:Active Advanced Sequence | "" | "" |  |  |
| Source:Advanced:Active Advanced Sequence Step | 0 | 0 |  |  |
| Source:Advanced:Actual Power Allocation | N/A | N/A |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |  |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |  |  |
| Source:Advanced:Merged Channels | ""[2] | ""[2] |  |  |
| Source:Advanced:OVP Enabled | FALSE[2] | FALSE[2] |  |  |
| Source:Advanced:OVP Limit | 0.0[2] | 0.0[2] |  |  |
| Source:Advanced:Output Capacitance |  |  |  |  |
| Source:Advanced:Output Shorted |  |  |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Power Allocation Mode | Automatic | Automatic |  |  |
| Source:Advanced:Pulse Bias Delay |  |  |  |  |
| Source:Advanced:Pulse Off Time |  |  |  |  |
| Source:Advanced:Pulse On Time |  |  |  |  |
| Source:Advanced:Requested Power Allocation | N/A | N/A |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |  |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |  |  |
| Source:Advanced:Sequence Step Delta Time |  |  |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled | FALSE[2] | FALSE[2] |  |  |
| Source:Advanced:Source Delay | 0.01666666 s | 0.01666666 s |  |  |
| Source:Constant Power:Current Limit |  |  |  |  |
| Source:Constant Power:Level |  |  |  |  |
| Source:Constant Power:Level Range |  |  |  |  |
| Source:Constant Resistance:Current Limit |  |  |  |  |
| Source:Constant Resistance:Level |  |  |  |  |
| Source:Constant Resistance:Level Range |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:DC Current:Current Level | 0.0 | 0.0 |  |  |
| Source:DC Current:Current Level Autorange | Off | Off |  |  |
| Source:DC Current:Current Level Range | 1 A | 1 A |  |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |  |  |
| Source:DC Current:Voltage Limit | 6 V | 6 V |  |  |
| Source:DC Current:Voltage Limit Autorange | Off | Off |  |  |
| Source:DC Current:Voltage Limit High | 6 V | 6 V |  |  |
| Source:DC Current:Voltage Limit Low | -6 V | -6 V |  |  |
| Source:DC Current:Voltage Limit Range | 6 V | 6 V |  |  |
| Source:DC Voltage:Current Limit | 0.1 A | 0.1 A |  |  |
| Source:DC Voltage:Current Limit Autorange | Off | Off |  |  |
| Source:DC Voltage:Current Limit High | 0.1 A | 0.1 A |  |  |
| Source:DC Voltage:Current Limit Low | -0.1 A | -0.1 A |  |  |
| Source:DC Voltage:Current Limit Range | 1 A | 1 A |  |  |
| Source:DC Voltage:Voltage Level | 0.01 V | 0.01 V |  |  |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |  |  |
| Source:DC Voltage:Voltage Level Range | 6 V | 6 V |  |  |
| Source:Output Connected | TRUE | TRUE |  |  |
| Source:Output Cutoff:Current Change Limit High |  |  |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |  |  |
| Source:Output Cutoff:Delay |  |  |  |  |
| Source:Output Cutoff:Enabled |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |  |  |
| Source:Output Enabled | TRUE[3] | TRUE[3] |  |  |
| Source:Output Function | DC Voltage | DC Voltage |  |  |
| Source:Output Resistance | 0.0[2] | 0.0[2] |  |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |  |  |
| Source:Source Mode | Single Point | Single Point |  |  |
| Source:Transient Response | Normal | Normal |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising[2] | Rising[2] |  |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising[2] | Rising[2] |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising[2] | Rising[2] |  |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Trigger Type | None | None |  |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising[2] | Rising[2] |  |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Trigger Type | None | None |  |  |

1

On Demand

Single Point

Automatically After Source Complete

Sequence

2

Only valid value.

3

The default value is TRUE if you use the niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>2</sup> 
 Only valid value.

<sup>3</sup> 
 The default value is TRUE if you use the niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4154.html language=enus -->
## TOPIC 00352: Properties Supported by the PXIe-4154

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4154.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4154.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property you can configure for your device. An in a table cell indicates that the listed property is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed property because it is a read-only

### Properties Supported by the PXIe-4154

The following table lists the default values for each property
 you can configure for your device.
 An [IMAGE alt='image' src='../../../../images/xmark.gif'] in a table cell
 indicates that the listed property is not supported for that device.
 N/A in a table cell indicates that there is not a default value for
 the listed property because it is a read-only property.

| Property | PXIe-4154 |
| --- | --- |
| Active Channel | "" |
| Advanced:Auxiliary Power Source Available | N/A |
| Advanced:Interlock Input Open |  |
| Advanced:Isolation State |  |
| Advanced:Power Source | Internal |
| Advanced:Power Source In Use | N/A |
| Advanced:Self-Calibration Persistence |  |
| Device Specific:LCR:Cable Length |  |
| Events:Measure Complete Event:Event Delay | 0 |
| Events:Measure Complete Event:Output Behavior | N/A |
| Events:Measure Complete Event:Output Terminal | "" |
| Events:Measure Complete Event:Pulse:Polarity | Active High |
| Events:Measure Complete Event:Pulse:Width | 250 ns |
| Events:Measure Complete Event:Toggle:Initial State | N/A |
| Events:Pulse Complete Event:Output Terminal |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |
| Events:Pulse Complete Event:Pulse:Width |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A |
| Events:Sequence Engine Done Event:Output Terminal | "" |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A |
| Events:Sequence Iteration Complete Event:Output Terminal | "" |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A |
| Events:Source Complete Event:Output Behavior | N/A |
| Events:Source Complete Event:Output Terminal | "" |
| Events:Source Complete Event:Pulse:Polarity | Active High |
| Events:Source Complete Event:Pulse:Width | 250 ns |
| Events:Source Complete Event:Toggle:Initial State | N/A |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |
| Inherent IVI Attributes:Driver Identification:Description | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |
| Inherent IVI Attributes:User Options:Cache | TRUE |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE |
| Inherent IVI Attributes:User Options:Range Check | TRUE |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |
| Inherent IVI Attributes:User Options:Simulate | FALSE |
| LCR:AC Stimulus:Advanced:Current Range |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |
| LCR:AC Stimulus:Automatic Level Control |  |
| LCR:AC Stimulus:Current Amplitude |  |
| LCR:AC Stimulus:Frequency |  |
| LCR:AC Stimulus:Function |  |
| LCR:AC Stimulus:Voltage Amplitude |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |
| LCR:Compensation:Load:Actual Reactance |  |
| LCR:Compensation:Load:Actual Resistance |  |
| LCR:Compensation:Load:Enabled |  |
| LCR:Compensation:Load:Measured Reactance |  |
| LCR:Compensation:Load:Measured Resistance |  |
| LCR:Compensation:Open:Conductance |  |
| LCR:Compensation:Open:Enabled |  |
| LCR:Compensation:Open:Susceptance |  |
| LCR:Compensation:Short:Enabled |  |
| LCR:Compensation:Short:Reactance |  |
| LCR:Compensation:Short:Resistance |  |
| LCR:Custom Measurement Time |  |
| LCR:DC Bias:Advanced:Current Range |  |
| LCR:DC Bias:Advanced:Transient Response |  |
| LCR:DC Bias:Advanced:Voltage Range |  |
| LCR:DC Bias:Automatic Level Control |  |
| LCR:DC Bias:Current Level |  |
| LCR:DC Bias:Source |  |
| LCR:DC Bias:Voltage Level |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |
| LCR:Impedance Range:Impedance Autorange |  |
| LCR:Impedance Range:Impedance Range |  |
| LCR:Instrument Mode | SMU PS |
| LCR:Measurement Time |  |
| LCR:Source Delay Mode |  |
| Measurement:Advanced:Autorange Aperture Time Mode |  |
| Measurement:Advanced:Autorange Behavior |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change |  |
| Measurement:Advanced:Autorange Minimum Aperture Time |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units |  |
| Measurement:Advanced:Autorange Minimum Current Range |  |
| Measurement:Advanced:Autorange Minimum Voltage Range |  |
| Measurement:Advanced:Autorange Threshold Mode |  |
| Measurement:Advanced:DC Noise Rejection | Normal |
| Measurement:Advanced:Measure Buffer Size | 200000 |
| Measurement:Advanced:Measure When | On Demand[1] |
| Measurement:Advanced:Reset Average Before Measurement |  |
| Measurement:Aperture Time |  |
| Measurement:Aperture Time Auto Mode |  |
| Measurement:Aperture Time Units |  |
| Measurement:Auto Zero | Off |
| Measurement:Autorange |  |
| Measurement:Fetch Backlog | N/A |
| Measurement:Measure Record Delta Time | N/A |
| Measurement:Measure Record Length | 1 |
| Measurement:Measure Record Length Is Finite | TRUE |
| Measurement:Power Line Frequency |  |
| Measurement:Samples To Average | 500 |
| Measurement:Sense | Local |
| Source:Advanced:Active Advanced Sequence |  |
| Source:Advanced:Active Advanced Sequence Step |  |
| Source:Advanced:Actual Power Allocation |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric |
| Source:Advanced:Conduction Voltage:Mode |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |
| Source:Advanced:Merged Channels |  |
| Source:Advanced:OVP Enabled | TRUE |
| Source:Advanced:OVP Limit |  |
| Source:Advanced:Output Capacitance | High |
| Source:Advanced:Output Shorted |  |
| Source:Advanced:Overranging Enabled | FALSE |
| Source:Advanced:Power Allocation Mode |  |
| Source:Advanced:Pulse Bias Delay |  |
| Source:Advanced:Pulse Off Time |  |
| Source:Advanced:Pulse On Time |  |
| Source:Advanced:Requested Power Allocation |  |
| Source:Advanced:Sequence Loop Count | 1 |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE |
| Source:Advanced:Sequence Step Delta Time |  |
| Source:Advanced:Sequence Step Delta Time Enabled |  |
| Source:Advanced:Source Delay | 0.01666666 s |
| Source:Constant Power:Current Limit |  |
| Source:Constant Power:Level |  |
| Source:Constant Power:Level Range |  |
| Source:Constant Resistance:Current Limit |  |
| Source:Constant Resistance:Level |  |
| Source:Constant Resistance:Level Range |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Current:Compensation Frequency |  |
| Source:Custom Transient Response:Current:Gain Bandwidth |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio |  |
| Source:DC Current:Current Level | 0.1 |
| Source:DC Current:Current Level Autorange | Off |
| Source:DC Current:Current Level Range | Channel 1: 3.0 Channel 2: 1.5 |
| Source:DC Current:Current Level Slew Rate:Falling |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |
| Source:DC Current:Voltage Limit | Channel 0: 6 Channel 1: 8 |
| Source:DC Current:Voltage Limit Autorange | Off |
| Source:DC Current:Voltage Limit High |  |
| Source:DC Current:Voltage Limit Low |  |
| Source:DC Current:Voltage Limit Range | Channel 0: 6 Channel 1: 8 |
| Source:DC Voltage:Current Limit | 0.1 |
| Source:DC Voltage:Current Limit Autorange | Off |
| Source:DC Voltage:Current Limit High |  |
| Source:DC Voltage:Current Limit Low |  |
| Source:DC Voltage:Current Limit Range | Channel 1: 3 Channel 2: 1.5 |
| Source:DC Voltage:Voltage Level | 0 |
| Source:DC Voltage:Voltage Level Autorange | Off |
| Source:DC Voltage:Voltage Level Range | Channel 0: 6 Channel 1: 8 |
| Source:Output Connected | TRUE |
| Source:Output Cutoff:Current Change Limit High |  |
| Source:Output Cutoff:Current Change Limit Low |  |
| Source:Output Cutoff:Current Measure Limit High |  |
| Source:Output Cutoff:Current Measure Limit Low |  |
| Source:Output Cutoff:Current Overrange Enabled |  |
| Source:Output Cutoff:Delay |  |
| Source:Output Cutoff:Enabled |  |
| Source:Output Cutoff:Voltage Change Limit High |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |
| Source:Output Cutoff:Voltage Output Limit High |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |
| Source:Output Enabled | TRUE[2] |
| Source:Output Function | DC Voltage |
| Source:Output Resistance | 0.0[] |
| Source:Pulse Current:Pulse Bias Current Level |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |
| Source:Pulse Current:Pulse Current Level |  |
| Source:Pulse Current:Pulse Current Level Range |  |
| Source:Pulse Current:Pulse Voltage Limit |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |
| Source:Pulse Voltage:Pulse Current Limit |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |
| Source:Source Mode | Single Point |
| Source:Transient Response | Normal[] |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Measure Trigger:Export Output Terminal | "" |
| Triggers:Measure Trigger:Trigger Type | Digital Edge |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |
| Triggers:Pulse Trigger:Trigger Type |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" |
| Triggers:Sequence Advance Trigger:Trigger Type | None |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |
| Triggers:Shutdown Trigger:Trigger Type |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Source Trigger:Export Output Terminal | "" |
| Triggers:Source Trigger:Trigger Type | None |
| Triggers:Start Trigger:Digital Edge:Edge | Rising |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" |
| Triggers:Start Trigger:Export Output Terminal | "" |
| Triggers:Start Trigger:Trigger Type | None |

1

On Demand

Single Point

Automatically After Source Complete

Sequence

2

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

[]

Channel 0.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>2</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4162-4163.html language=enus -->
## TOPIC 00353: Properties Supported by the PXIe-4162/4163

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4162-4163.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4162-4163.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4162/4163 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4162 PXIe-4163 Supports Advanced Sequence (PXIe-4162) Supports Advanced Seque

### Properties Supported by the PXIe-4162/4163

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4162/4163 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4162 | PXIe-4163 | Supports Advanced Sequence (PXIe-4162) | Supports Advanced Sequence (PXIe-4163) |
| --- | --- | --- | --- | --- |
| Active Channel | "" | "" |  |  |
| Advanced:Auxiliary Power Source Available | N/A | N/A |  |  |
| Advanced:Interlock Input Open |  |  |  |  |
| Advanced:Isolation State |  |  |  |  |
| Advanced:Power Source | Internal | Internal |  |  |
| Advanced:Power Source In Use | N/A | N/A |  |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM | Write to EEPROM |  |  |
| Device Specific:LCR:Cable Length |  |  |  |  |
| Events:Measure Complete Event:Event Delay | 0 | 0 |  |  |
| Events:Measure Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Measure Complete Event:Output Terminal | "" | "" |  |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Measure Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Pulse Complete Event:Output Terminal |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |  |  |
| Events:Sequence Engine Done Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Engine Done Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" | "" |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Events:Source Complete Event:Output Behavior | N/A | N/A |  |  |
| Events:Source Complete Event:Output Terminal | "" | "" |  |  |
| Events:Source Complete Event:Pulse:Polarity | Active High | Active High |  |  |
| Events:Source Complete Event:Pulse:Width | 250 ns | 250 ns |  |  |
| Events:Source Complete Event:Toggle:Initial State | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A | N/A |  |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A | N/A |  |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A | N/A |  |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A | N/A |  |  |
| Inherent IVI Attributes:User Options:Cache | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE | TRUE |  |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE | FALSE |  |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE | FALSE |  |  |
| LCR:AC Stimulus:Advanced:Current Range |  |  |  |  |
| LCR:AC Stimulus:Advanced:Dither Enabled |  |  |  |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time |  |  |  |  |
| LCR:AC Stimulus:Advanced:Voltage Range |  |  |  |  |
| LCR:AC Stimulus:Automatic Level Control |  |  |  |  |
| LCR:AC Stimulus:Current Amplitude |  |  |  |  |
| LCR:AC Stimulus:Frequency |  |  |  |  |
| LCR:AC Stimulus:Function |  |  |  |  |
| LCR:AC Stimulus:Voltage Amplitude |  |  |  |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay |  |  |  |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source |  |  |  |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled |  |  |  |  |
| LCR:Compensation:Load:Actual Reactance |  |  |  |  |
| LCR:Compensation:Load:Actual Resistance |  |  |  |  |
| LCR:Compensation:Load:Enabled |  |  |  |  |
| LCR:Compensation:Load:Measured Reactance |  |  |  |  |
| LCR:Compensation:Load:Measured Resistance |  |  |  |  |
| LCR:Compensation:Open:Conductance |  |  |  |  |
| LCR:Compensation:Open:Enabled |  |  |  |  |
| LCR:Compensation:Open:Susceptance |  |  |  |  |
| LCR:Compensation:Short:Enabled |  |  |  |  |
| LCR:Compensation:Short:Reactance |  |  |  |  |
| LCR:Compensation:Short:Resistance |  |  |  |  |
| LCR:Custom Measurement Time |  |  |  |  |
| LCR:DC Bias:Advanced:Current Range |  |  |  |  |
| LCR:DC Bias:Advanced:Transient Response |  |  |  |  |
| LCR:DC Bias:Advanced:Voltage Range |  |  |  |  |
| LCR:DC Bias:Automatic Level Control |  |  |  |  |
| LCR:DC Bias:Current Level |  |  |  |  |
| LCR:DC Bias:Source |  |  |  |  |
| LCR:DC Bias:Voltage Level |  |  |  |  |
| LCR:Impedance Range:Advanced:Impedance Range Source |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Capacitance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Inductance |  |  |  |  |
| LCR:Impedance Range:Advanced:Load Resistance |  |  |  |  |
| LCR:Impedance Range:Impedance Autorange |  |  |  |  |
| LCR:Impedance Range:Impedance Range |  |  |  |  |
| LCR:Instrument Mode | SMU PS | SMU PS |  |  |
| LCR:Measurement Time |  |  |  |  |
| LCR:Source Delay Mode |  |  |  |  |
| Measurement:Advanced:Autorange Aperture Time Mode | Auto | Auto |  |  |
| Measurement:Advanced:Autorange Behavior | Range up to limit then down | Range up to limit then down |  |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change | 0.1 s | 0.1 s |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time | 0 s | 0 s |  |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Advanced:Autorange Minimum Current Range | 0 | 0 |  |  |
| Measurement:Advanced:Autorange Minimum Voltage Range | 0 | 0 |  |  |
| Measurement:Advanced:Autorange Threshold Mode | Normal | Normal |  |  |
| Measurement:Advanced:DC Noise Rejection | Normal | Normal |  |  |
| Measurement:Advanced:Measure Buffer Size | 100096 | 100096 |  |  |
| Measurement:Advanced:Measure When | On Demand[1] | On Demand[1] |  |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |  |  |
| Measurement:Aperture Time | 0.01666666 s | 0.01666666 s |  |  |
| Measurement:Aperture Time Auto Mode |  |  |  |  |
| Measurement:Aperture Time Units | Seconds | Seconds |  |  |
| Measurement:Auto Zero | Off | Off |  |  |
| Measurement:Autorange | Off | Off |  |  |
| Measurement:Fetch Backlog | N/A | N/A |  |  |
| Measurement:Measure Record Delta Time | N/A | N/A |  |  |
| Measurement:Measure Record Length | 1 | 1 |  |  |
| Measurement:Measure Record Length Is Finite | TRUE | TRUE |  |  |
| Measurement:Power Line Frequency | 60 Hertz | 60 Hertz |  |  |
| Measurement:Samples To Average | 1 | 1 |  |  |
| Measurement:Sense | Local | Local |  |  |
| Source:Advanced:Active Advanced Sequence | "" | "" |  |  |
| Source:Advanced:Active Advanced Sequence Step | 0 | 0 |  |  |
| Source:Advanced:Actual Power Allocation |  |  |  |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric | Symmetric |  |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |  |  |
| Source:Advanced:Merged Channels |  |  |  |  |
| Source:Advanced:OVP Enabled |  |  |  |  |
| Source:Advanced:OVP Limit |  |  |  |  |
| Source:Advanced:Output Capacitance |  |  |  |  |
| Source:Advanced:Output Shorted |  |  |  |  |
| Source:Advanced:Overranging Enabled | FALSE | FALSE |  |  |
| Source:Advanced:Power Allocation Mode |  |  |  |  |
| Source:Advanced:Pulse Bias Delay |  |  |  |  |
| Source:Advanced:Pulse Off Time |  |  |  |  |
| Source:Advanced:Pulse On Time |  |  |  |  |
| Source:Advanced:Requested Power Allocation |  |  |  |  |
| Source:Advanced:Sequence Loop Count | 1 | 1 |  |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE | TRUE |  |  |
| Source:Advanced:Sequence Step Delta Time |  |  |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled |  |  |  |  |
| Source:Advanced:Source Delay | 0.01666666 s | 0.01666666 s |  |  |
| Source:Constant Power:Current Limit |  |  |  |  |
| Source:Constant Power:Level |  |  |  |  |
| Source:Constant Power:Level Range |  |  |  |  |
| Source:Constant Resistance:Current Limit |  |  |  |  |
| Source:Constant Resistance:Level |  |  |  |  |
| Source:Constant Resistance:Level Range |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. | Determined by the value of the Normal setting of the Transient Response property. |  |  |
| Source:DC Current:Current Level | 0.0 | 0.0 |  |  |
| Source:DC Current:Current Level Autorange | Off | Off |  |  |
| Source:DC Current:Current Level Range | 0.001 | 0.001 |  |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |  |  |
| Source:DC Current:Voltage Limit | 24 | 24 |  |  |
| Source:DC Current:Voltage Limit Autorange | Off | Off |  |  |
| Source:DC Current:Voltage Limit High | 24.0 | 24.0 |  |  |
| Source:DC Current:Voltage Limit Low | -24.0 | -24.0 |  |  |
| Source:DC Current:Voltage Limit Range | 24 | 24 |  |  |
| Source:DC Voltage:Current Limit | 0.001 | 0.001 |  |  |
| Source:DC Voltage:Current Limit Autorange | Off | Off |  |  |
| Source:DC Voltage:Current Limit High | 0.001 | 0.001 |  |  |
| Source:DC Voltage:Current Limit Low | -0.001 | -0.001 |  |  |
| Source:DC Voltage:Current Limit Range | 0.001 | 0.001 |  |  |
| Source:DC Voltage:Voltage Level | 0 | 0 |  |  |
| Source:DC Voltage:Voltage Level Autorange | Off | Off |  |  |
| Source:DC Voltage:Voltage Level Range | 24 | 24 |  |  |
| Source:Output Connected | TRUE | TRUE |  |  |
| Source:Output Cutoff:Current Change Limit High |  |  |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |  |  |
| Source:Output Cutoff:Delay |  |  |  |  |
| Source:Output Cutoff:Enabled |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |  |  |
| Source:Output Enabled | TRUE[2] | TRUE[2] |  |  |
| Source:Output Function | DC Voltage | DC Voltage |  |  |
| Source:Output Resistance | 0.0 | 0.0 |  |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |  |  |
| Source:Source Mode | Single Point | Single Point |  |  |
| Source:Transient Response | Normal | Normal |  |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Measure Trigger:Trigger Type | Digital Edge | Digital Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None | None |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Source Trigger:Trigger Type | None | None |  |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising | Rising |  |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Export Output Terminal | "" | "" |  |  |
| Triggers:Start Trigger:Trigger Type | None | None |  |  |

1

On Demand

Single Point

Automatically After Source Complete

Sequence

2

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>2</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4190.html language=enus -->
## TOPIC 00354: Properties Supported by the PXIe-4190

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4190.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4190.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each property and support for advanced sequence on the PXIe-4190 device. N/A in the table cell indicates that the listed property is a read-only property. Property PXIe-4190 Supports Advanced Sequence Active Channel "" Advanced:Auxiliary Power Source

### Properties Supported by the PXIe-4190

The following table lists the default values for each property and
 support for advanced sequence on the PXIe-4190 device.
 N/A in the table cell indicates that the listed property is a read-only property.

| Property | PXIe-4190 | Supports Advanced Sequence |
| --- | --- | --- |
| Active Channel | "" |  |
| Advanced:Auxiliary Power Source Available | N/A |  |
| Advanced:Interlock Input Open |  |  |
| Advanced:Isolation State | Isolated |  |
| Advanced:Power Source | Internal |  |
| Advanced:Power Source In Use | N/A |  |
| Advanced:Self-Calibration Persistence | Write to EEPROM |  |
| Device Specific:LCR:Cable Length | NI Standard 1m |  |
| Events:Measure Complete Event:Event Delay | 0 s |  |
| Events:Measure Complete Event:Output Behavior | Pulse Event Output |  |
| Events:Measure Complete Event:Output Terminal | "" |  |
| Events:Measure Complete Event:Pulse:Polarity | Active High |  |
| Events:Measure Complete Event:Pulse:Width | 250 ns |  |
| Events:Measure Complete Event:Toggle:Initial State | Initial State Low |  |
| Events:Pulse Complete Event:Output Terminal |  |  |
| Events:Pulse Complete Event:Pulse:Polarity |  |  |
| Events:Pulse Complete Event:Pulse:Width |  |  |
| Events:Ready For Pulse Trigger Event:Output Terminal |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Polarity |  |  |
| Events:Ready For Pulse Trigger Event:Pulse:Width |  |  |
| Events:Sequence Engine Done Event:Output Behavior | Pulse Event Output |  |
| Events:Sequence Engine Done Event:Output Terminal | "" |  |
| Events:Sequence Engine Done Event:Pulse:Polarity | Active High |  |
| Events:Sequence Engine Done Event:Pulse:Width | 250 ns |  |
| Events:Sequence Engine Done Event:Toggle:Initial State | Initial State Low |  |
| Events:Sequence Iteration Complete Event:Output Behavior | Pulse Event Output |  |
| Events:Sequence Iteration Complete Event:Output Terminal | "" |  |
| Events:Sequence Iteration Complete Event:Pulse:Polarity | Active High |  |
| Events:Sequence Iteration Complete Event:Pulse:Width | 250 ns |  |
| Events:Sequence Iteration Complete Event:Toggle:Initial State | Initial State Low |  |
| Events:Source Complete Event:Output Behavior | Pulse Event Output |  |
| Events:Source Complete Event:Output Terminal | "" |  |
| Events:Source Complete Event:Pulse:Polarity | Active High |  |
| Events:Source Complete Event:Pulse:Width | 250 ns |  |
| Events:Source Complete Event:Toggle:Initial State | Initial State Low |  |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | N/A |  |
| Inherent IVI Attributes:Advanced Session Information:Resource Descriptor | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | N/A |  |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | N/A |  |
| Inherent IVI Attributes:Driver Identification:Description | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | N/A |  |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | N/A |  |
| Inherent IVI Attributes:Driver Identification:Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Model | N/A |  |
| Inherent IVI Attributes:Instrument Identification:Serial Number | N/A |  |
| Inherent IVI Attributes:User Options:Cache | TRUE |  |
| Inherent IVI Attributes:User Options:Interchange Check | FALSE |  |
| Inherent IVI Attributes:User Options:Query Instrument Status | TRUE |  |
| Inherent IVI Attributes:User Options:Range Check | TRUE |  |
| Inherent IVI Attributes:User Options:Record Value Coercions | FALSE |  |
| Inherent IVI Attributes:User Options:Simulate | FALSE |  |
| LCR:AC Stimulus:Advanced:Current Range | 700.0e-6 A |  |
| LCR:AC Stimulus:Advanced:Dither Enabled | TRUE |  |
| LCR:AC Stimulus:Advanced:Source Aperture Time | 50.0e-6 s |  |
| LCR:AC Stimulus:Advanced:Voltage Range | 7 V |  |
| LCR:AC Stimulus:Automatic Level Control | On |  |
| LCR:AC Stimulus:Current Amplitude | 7.08e-9 |  |
| LCR:AC Stimulus:Frequency | 1000 |  |
| LCR:AC Stimulus:Function | AC Voltage |  |
| LCR:AC Stimulus:Voltage Amplitude | 7.08e-3 |  |
| LCR:Compensation:LCR AC Electrical Cable Length Delay | Determined by the value of the Cable Length property. |  |
| LCR:Compensation:LCR Open/Short/Load Compensation Data Source | Onboard Storage |  |
| LCR:Compensation:LCR Short Custom Cable Compensation Enabled | TRUE |  |
| LCR:Compensation:Load:Actual Reactance | 0.0 |  |
| LCR:Compensation:Load:Actual Resistance | 0.0 |  |
| LCR:Compensation:Load:Enabled | FALSE |  |
| LCR:Compensation:Load:Measured Reactance | 0.0 |  |
| LCR:Compensation:Load:Measured Resistance | 0.0 |  |
| LCR:Compensation:Open:Conductance | 0.0 |  |
| LCR:Compensation:Open:Enabled | FALSE |  |
| LCR:Compensation:Open:Susceptance | 0.0 |  |
| LCR:Compensation:Short:Enabled | FALSE |  |
| LCR:Compensation:Short:Reactance | 0.0 |  |
| LCR:Compensation:Short:Resistance | 0.0 |  |
| LCR:Custom Measurement Time | 0.01 s |  |
| LCR:DC Bias:Advanced:Current Range | 1.0e-3 A |  |
| LCR:DC Bias:Advanced:Transient Response | Normal |  |
| LCR:DC Bias:Advanced:Voltage Range | 10 V |  |
| LCR:DC Bias:Automatic Level Control | On |  |
| LCR:DC Bias:Current Level | 0.0 |  |
| LCR:DC Bias:Source | Off |  |
| LCR:DC Bias:Voltage Level | 0.0 |  |
| LCR:Impedance Range:Advanced:Impedance Range Source | LCR Impedance Range |  |
| LCR:Impedance Range:Advanced:Load Capacitance | 0.0 |  |
| LCR:Impedance Range:Advanced:Load Inductance | 0.0 |  |
| LCR:Impedance Range:Advanced:Load Resistance | 0.0 |  |
| LCR:Impedance Range:Impedance Autorange | Off |  |
| LCR:Impedance Range:Impedance Range | 100.0 |  |
| LCR:Instrument Mode | SMU PS |  |
| LCR:Measurement Time | Medium |  |
| LCR:Source Delay Mode | Automatic |  |
| Measurement:Advanced:Autorange Aperture Time Mode | Auto |  |
| Measurement:Advanced:Autorange Behavior | Range Up To Limit Then Down |  |
| Measurement:Advanced:Autorange Maximum Delay After Range Change | 5.0 s |  |
| Measurement:Advanced:Autorange Minimum Aperture Time | 0 |  |
| Measurement:Advanced:Autorange Minimum Aperture Time Units | Seconds |  |
| Measurement:Advanced:Autorange Minimum Current Range | 0 |  |
| Measurement:Advanced:Autorange Minimum Voltage Range | 0 |  |
| Measurement:Advanced:Autorange Threshold Mode | Normal |  |
| Measurement:Advanced:DC Noise Rejection | Normal |  |
| Measurement:Advanced:Measure Buffer Size | 60078 |  |
| Measurement:Advanced:Measure When | On Demand[1] |  |
| Measurement:Advanced:Reset Average Before Measurement |  |  |
| Measurement:Aperture Time | 0.01666666 s |  |
| Measurement:Aperture Time Auto Mode |  |  |
| Measurement:Aperture Time Units | Seconds |  |
| Measurement:Auto Zero | Off |  |
| Measurement:Autorange | Off |  |
| Measurement:Fetch Backlog | N/A |  |
| Measurement:Measure Record Delta Time | N/A |  |
| Measurement:Measure Record Length | 1 |  |
| Measurement:Measure Record Length Is Finite | TRUE |  |
| Measurement:Power Line Frequency | 60 Hz |  |
| Measurement:Samples To Average | 1 |  |
| Measurement:Sense | Remote |  |
| Source:Advanced:Active Advanced Sequence | "" |  |
| Source:Advanced:Active Advanced Sequence Step | 0 |  |
| Source:Advanced:Actual Power Allocation | 0 W |  |
| Source:Advanced:Compliance Limit Symmetry | Symmetric |  |
| Source:Advanced:Conduction Voltage:Mode |  |  |
| Source:Advanced:Conduction Voltage:Off Threshold |  |  |
| Source:Advanced:Conduction Voltage:On Threshold |  |  |
| Source:Advanced:Merged Channels | "" |  |
| Source:Advanced:OVP Enabled |  |  |
| Source:Advanced:OVP Limit |  |  |
| Source:Advanced:Output Capacitance |  |  |
| Source:Advanced:Output Shorted |  |  |
| Source:Advanced:Overranging Enabled | FALSE |  |
| Source:Advanced:Power Allocation Mode | Automatic |  |
| Source:Advanced:Pulse Bias Delay |  |  |
| Source:Advanced:Pulse Off Time |  |  |
| Source:Advanced:Pulse On Time |  |  |
| Source:Advanced:Requested Power Allocation | 0 |  |
| Source:Advanced:Sequence Loop Count | 1 |  |
| Source:Advanced:Sequence Loop Count Is Finite | TRUE |  |
| Source:Advanced:Sequence Step Delta Time |  |  |
| Source:Advanced:Sequence Step Delta Time Enabled |  |  |
| Source:Advanced:Source Delay | 0.01666666 s |  |
| Source:Constant Power:Current Limit |  |  |
| Source:Constant Power:Level |  |  |
| Source:Constant Power:Level Range |  |  |
| Source:Constant Resistance:Current Limit |  |  |
| Source:Constant Resistance:Level |  |  |
| Source:Constant Resistance:Level Range |  |  |
| Source:Custom Transient Response:Constant Power:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Power:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Power:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Constant Resistance:Compensation Frequency |  |  |
| Source:Custom Transient Response:Constant Resistance:Gain Bandwidth |  |  |
| Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio |  |  |
| Source:Custom Transient Response:Current:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Current:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Compensation Frequency | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Gain Bandwidth | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:Custom Transient Response:Voltage:Pole-Zero Ratio | Determined by the value of the Normal setting of the Transient Response property. |  |
| Source:DC Current:Current Level | 0.0 |  |
| Source:DC Current:Current Level Autorange | Off |  |
| Source:DC Current:Current Level Range | 1.0e-3 A |  |
| Source:DC Current:Current Level Slew Rate:Falling |  |  |
| Source:DC Current:Current Level Slew Rate:Rising |  |  |
| Source:DC Current:Voltage Limit | 10 V |  |
| Source:DC Current:Voltage Limit Autorange | Off |  |
| Source:DC Current:Voltage Limit High | 10 V |  |
| Source:DC Current:Voltage Limit Low | -10 V |  |
| Source:DC Current:Voltage Limit Range | 10 V |  |
| Source:DC Voltage:Current Limit | 0.001 A |  |
| Source:DC Voltage:Current Limit Autorange | Off |  |
| Source:DC Voltage:Current Limit High | 0.001 A |  |
| Source:DC Voltage:Current Limit Low | -0.001 A |  |
| Source:DC Voltage:Current Limit Range | 1.0e-3 A |  |
| Source:DC Voltage:Voltage Level | 0 |  |
| Source:DC Voltage:Voltage Level Autorange | Off |  |
| Source:DC Voltage:Voltage Level Range | 10 V |  |
| Source:Output Connected | TRUE |  |
| Source:Output Cutoff:Current Change Limit High |  |  |
| Source:Output Cutoff:Current Change Limit Low |  |  |
| Source:Output Cutoff:Current Measure Limit High |  |  |
| Source:Output Cutoff:Current Measure Limit Low |  |  |
| Source:Output Cutoff:Current Overrange Enabled |  |  |
| Source:Output Cutoff:Delay |  |  |
| Source:Output Cutoff:Enabled |  |  |
| Source:Output Cutoff:Voltage Change Limit High |  |  |
| Source:Output Cutoff:Voltage Change Limit Low |  |  |
| Source:Output Cutoff:Voltage Output Limit High |  |  |
| Source:Output Cutoff:Voltage Output Limit Low |  |  |
| Source:Output Cutoff:Voltage Measure Limit High |  |  |
| Source:Output Cutoff:Voltage Measure Limit Low |  |  |
| Source:Output Enabled | TRUE[2] |  |
| Source:Output Function | DC Voltage |  |
| Source:Output Resistance | 0.0[3] |  |
| Source:Pulse Current:Pulse Bias Current Level |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Bias Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Current Level |  |  |
| Source:Pulse Current:Pulse Current Level Range |  |  |
| Source:Pulse Current:Pulse Voltage Limit |  |  |
| Source:Pulse Current:Pulse Voltage Limit High |  |  |
| Source:Pulse Current:Pulse Voltage Limit Low |  |  |
| Source:Pulse Current:Pulse Voltage Limit Range |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Bias Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Bias Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Current Limit |  |  |
| Source:Pulse Voltage:Pulse Current Limit High |  |  |
| Source:Pulse Voltage:Pulse Current Limit Low |  |  |
| Source:Pulse Voltage:Pulse Current Limit Range |  |  |
| Source:Pulse Voltage:Pulse Voltage Level |  |  |
| Source:Pulse Voltage:Pulse Voltage Level Range |  |  |
| Source:Source Mode | Single Point |  |
| Source:Transient Response | Normal |  |
| Triggers:Measure Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Measure Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Measure Trigger:Export Output Terminal | "" |  |
| Triggers:Measure Trigger:Trigger Type | None |  |
| Triggers:Pulse Trigger:Digital Edge:Edge |  |  |
| Triggers:Pulse Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Pulse Trigger:Export Output Terminal |  |  |
| Triggers:Pulse Trigger:Trigger Type |  |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Export Output Terminal | "" |  |
| Triggers:Sequence Advance Trigger:Trigger Type | None |  |
| Triggers:Shutdown Trigger:Digital Edge:Edge |  |  |
| Triggers:Shutdown Trigger:Digital Edge:Input Terminal |  |  |
| Triggers:Shutdown Trigger:Trigger Type |  |  |
| Triggers:Source Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Source Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Source Trigger:Export Output Terminal | "" |  |
| Triggers:Source Trigger:Trigger Type | None |  |
| Triggers:Start Trigger:Digital Edge:Edge | Rising |  |
| Triggers:Start Trigger:Digital Edge:Input Terminal | "" |  |
| Triggers:Start Trigger:Export Output Terminal | "" |  |
| Triggers:Start Trigger:Trigger Type | None |  |

1

On Demand

Single Point

Automatically After Source Complete

Sequence

2

The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

3

0.0

Parent topic:

Supported Properties by Device

<sup>1</sup> 
 Default depends on the setting of the
 Source Mode property.
 The default is On Demand if the Source Mode property is set to Single Point,
 or the default is Automatically After Source Complete if the
 Source Mode property is set to Sequence.

<sup>2</sup> 
 The default value is TRUE if you use the
 niDCPower Initialize With Independent Channels VI or
 niDCPower Initialize With Channels VI
 to open the session, otherwise the default value is FALSE.

<sup>3</sup> 
 0.0 is the only valid value.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties.html language=enus -->
## TOPIC 00355: Supported Properties by Device

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following topics for information about property support and default values.

### Supported Properties by Device

Refer to the following topics for information about property support and default values.

- [Properties Supported by the PXIe-4051](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4051.html)
- [Properties Supported by the PXIe-4110](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4110.html)
- [Properties Supported by the PXIe-4112/4113](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4112-4113.html)
- [Properties Supported by the PXI-4130](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4130.html)
- [Properties Supported by the PXI-4132](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4132.html)
- [Properties Supported by the PXIe-4135](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4135.html)
- [Properties Supported by the PXIe-4136/4137](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4136-4137.html)
- [Properties Supported by the PXIe-4138/4139](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4138-4139.html)
- [Properties Supported by the PXIe-4140/4141](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4140-4141.html)
- [Properties Supported by the PXIe-4142/4143](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4142-4143.html)
- [Properties Supported by the PXIe-4144/4145](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4144-4145.html)
- [Properties Supported by the PXIe-4147](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4147.html)
- [Properties Supported by the PXIe-4150/4151](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4150-4151.html)
- [Properties Supported by the PXIe-4154](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4154.html)
- [Properties Supported by the PXIe-4162/4163](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4162-4163.html)
- [Properties Supported by the PXIe-4190](../../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/supported-properties-4190.html)

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/otherivi-mnu.html language=enus -->
## TOPIC 00356: Other IVI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/otherivi-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/otherivi-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower IVI Other VIs to access the IVI Utility functionality. icon

### Other IVI

Use the NI-DCPower IVI Other VIs to access the IVI Utility functionality.

[IMAGE alt='icon' src='otherivi-mnu.png']

- [niDCPower Revision Query VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-revision-query-vi.html) Returns the revision information of NI-DCPower and the device firmware.
- [niDCPower Reset with Defaults VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-defaults-vi.html) Resets all channels in the session to a known state. This VI disables power generation, resets session properties to their default values, commits the session properties, and leaves the session in the Running state. In addition to exhibiting the behavior of the niDCPower Reset With Channels VI, this VI can assign user-defined default values for configurable properties from the IVI configuration.
- [niDCPower Get Next Coercion Record VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-next-coercion-record-vi.html) Returns the coercion information associated with the IVI session and clears the earliest instance in which NI-DCPower coerced a value you specified.
- [niDCPower Reset Interchange Check VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-interchange-check-vi.html) Configures interchangeability-checking algorithms to ignore all previous configuration options.
- [niDCPower Clear Interchange Warnings VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-interchange-warnings-vi.html) Clears the list of current interchange warnings.
- [niDCPower Get Next Interchange Warning VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-next-interchange-warning-vi.html) Returns the interchangeability warning associated with the IVI session. It retrieves and clears the earliest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different device may cause a different behavior.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/pulsecurrent-mnu.html language=enus -->
## TOPIC 00357: Pulse Current

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/pulsecurrent-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/pulsecurrent-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Pulse Current VIs for changing channel settings when the channel is configured for the Pulse Current output function. icon

### Pulse Current

Use the NI-DCPower Pulse Current VIs for changing channel settings when the channel is configured for the Pulse Current output function.

[IMAGE alt='icon' src='pulsecurrent-mnu.png']

- [niDCPower Configure Pulse Current Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-level-vi.html) Configures the pulse current level that the specified channel(s) attempt to generate during the on phase of a pulse. A channel must be enabled for the specified current level to take effect.
- [niDCPower Configure Pulse Current Level Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-level-range-vi.html) Configures the pulse current level range for the specified channel(s).
- [niDCPower Configure Pulse Bias Current Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-level-vi.html) Configures the pulse bias current level that the specified channel(s) attempt to generate during the off phase of a pulse. A channel must be enabled for the specified current level to take effect.
- [niDCPower Configure Pulse Voltage Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-voltage-limit-vi.html) Configures the pulse voltage limit for the specified channel(s). A channel must be enabled for the specified voltage limit to take effect.
- [niDCPower Configure Pulse Voltage Limit Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-voltage-limit-range-vi.html) Configures the pulse voltage limit range for the specified channel(s).
- [niDCPower Configure Pulse Bias Voltage Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-limit-vi.html) Configures the pulse bias voltage limit for the specified channel(s). A channel must be enabled for the specified voltage limit to take effect.

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/pulsevoltage-mnu.html language=enus -->
## TOPIC 00358: Pulse Voltage

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/pulsevoltage-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/pulsevoltage-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Pulse Voltage VIs for changing channel settings when the channel is configured for the Pulse Voltage output function. icon

### Pulse Voltage

Use the NI-DCPower Pulse Voltage VIs for changing channel settings when the channel is configured for the Pulse Voltage output function.

[IMAGE alt='icon' src='pulsevoltage-mnu.png']

- [niDCPower Configure Pulse Voltage Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-voltage-level-vi.html) Configures the pulse voltage level that the specified channel(s) attempt to generate during the on phase of a pulse. A channel must be enabled for the specified voltage level to take effect.
- [niDCPower Configure Pulse Voltage Level Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-voltage-level-range-vi.html) Configures the pulse voltage level range for the specified channel(s).
- [niDCPower Configure Pulse Bias Voltage Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-level-vi.html) Configures the pulse bias voltage level that specified channel(s) attempt to generate during the off phase of a pulse. A channel must be enabled for the specified voltage level to take effect.
- [niDCPower Configure Pulse Current Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-vi.html) Configures the pulse current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect.
- [niDCPower Configure Pulse Current Limit Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-range-vi.html) Configures the pulse current limit range for the specified channel(s).
- [niDCPower Configure Pulse Bias Current Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-limit-vi.html) Configures the pulse bias current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect.

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/query-mnu.html language=enus -->
## TOPIC 00359: Query

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/query-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/query-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Query VIs to query information about the capabilities and state of the device. icon

### Query

Use the NI-DCPower Query VIs to query information about the capabilities and state of the device.

[IMAGE alt='icon' src='query-mnu.png']

- [niDCPower Query Max Voltage Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-voltage-level-vi.html) Queries the maximum voltage level on a channel if the channel is set to the specified current limit .
- [niDCPower Query Min Current Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-min-current-limit-vi.html) Queries the minimum current limit on a channel if the channel is set to the specified voltage level .
- [niDCPower Query Max Current Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-current-limit-vi.html) Queries the maximum current limit on a channel if the channel is set to the specified voltage level .
- [niDCPower Query Latched Output Cutoff State VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-latched-output-cutoff-state-vi.html) Discovers if an output cutoff limit was exceeded for the specified reason.
- [niDCPower Clear Latched Output Cutoff State VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-latched-output-cutoff-state-vi.html) Clears the state of an output cutoff that was engaged.
- [niDCPower Query Output State VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-output-state-vi.html) Queries the specified channel to determine if the channel is currently in the state specified by output state .
- [niDCPower Query In Compliance VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-in-compliance-vi.html) Queries the specified channel to determine if it is operating at the compliance limit.

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/source-mnu.html language=enus -->
## TOPIC 00360: Source

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/source-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/source-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Source VIs to configure the source unit. icon

### Source

Use the NI-DCPower Source VIs to configure the source unit.

[IMAGE alt='icon' src='source-mnu.png']

- [DC Voltage](../../instr-lib/nidcpower/dcvoltage-mnu.html) Use the NI-DCPower DC Voltage VIs for changing channel settings when the channel is configured for the DC Voltage output function.
- [DC Current](../../instr-lib/nidcpower/dccurrent-mnu.html) Use the NI-DCPower DC Current VIs for changing channel settings when the channel is configured for the DC Current output function.
- [Pulse Voltage](../../instr-lib/nidcpower/pulsevoltage-mnu.html) Use the NI-DCPower Pulse Voltage VIs for changing channel settings when the channel is configured for the Pulse Voltage output function.
- [Pulse Current](../../instr-lib/nidcpower/pulsecurrent-mnu.html) Use the NI-DCPower Pulse Current VIs for changing channel settings when the channel is configured for the Pulse Current output function.
- [Advanced Sequencing](../../instr-lib/nidcpower/advancedsequencing-mnu.html) Use the NI-DCPower Advanced Sequence VIs for configuring the source and measure unit with a series of property or attribute values. You must set the source mode to Sequence.
- [niDCPower Configure Source Mode With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-source-mode-with-channels-vi.html) Configures the Source Mode property. Specifies whether to run a single output point or a sequence.
- [niDCPower Set Sequence VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-set-sequence-vi.html) Configures a series of voltage, current, resistance or power outputs and corresponding source delays. The source mode must be set to Sequence for this VI to take effect.
- [niDCPower Configure Output Function VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-function-vi.html) Configures the function that the specified channels attempt to generate.
- [niDCPower Configure Output Enabled VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-enabled-vi.html) Enables or disables generation on the specified channel(s).

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/triggersevents-mnu.html language=enus -->
## TOPIC 00361: Triggers and Events

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/triggersevents-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/triggersevents-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Triggers and Events VIs to configure triggers and events. icon

### Triggers and Events

Use the NI-DCPower Triggers and Events VIs to configure triggers and events.

[IMAGE alt='icon' src='triggersevents-mnu.png']

- [niDCPower Configure Trigger With Channels (Poly) VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-trigger-with-channels-poly-vi.html) Configures triggers for the specified channel(s).
- [niDCPower Export Signal With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-export-signal-with-channels-vi.html) Routes signals (triggers and events) to the output terminal you specify.
- [niDCPower Send Software Edge Trigger With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-send-software-edge-trigger-with-channels-vi.html) Asserts the specified trigger. This VI can override an external edge trigger.
- [niDCPower Wait For Event With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-wait-for-event-with-channels-vi.html) Waits until the specified channel(s) have generated the specified event.

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/utility-mnu.html language=enus -->
## TOPIC 00362: Utility

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/utility-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Utility VIs for miscellaneous functionality. icon

### Utility

Use the NI-DCPower Utility VIs for miscellaneous functionality.

[IMAGE alt='icon' src='utility-mnu.png']

- [niDCPower Reset With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-channels-vi.html) Resets the specified channel(s) to a known state. This VI disables power generation, resets channel properties to their default values, commits the channel properties, and leaves the channel(s) in the Uncommitted state. You can use this VI to clear certain errors in less time than using the niDCPower Reset Device VI.
- [niDCPower Reset Device VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-device-vi.html) Resets all instruments in the session to a known state. This VI disables power generation, resets all properties for all instruments included in the session to their default values, clears errors such as overtemperature and unexpected loss of auxiliary power, commits the instrument properties, and leaves the instrument(s) in the Uncommitted state. This VI also performs a hard reset on the instrument(s) and driver software. This VI has the same functionality as using reset in Measurement & Automation Explorer (MAX).
- [niDCPower Disable VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-vi.html) This VI performs the same actions as the niDCPower Reset With Channels VI, except that this VI also immediately sets the Output Enabled property to FALSE.
- [niDCPower Self Test VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-self-test-vi.html) Performs the device self-test routine and returns the test result(s). Calling this VI implicitly calls the niDCPower Reset With Channels VI.
- [niDCPower Export Attribute Configuration (Poly) VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-poly-vi.html) Exports a session configuration to either a file or a buffer.
- [niDCPower Import Attribute Configuration (Poly) VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-poly-vi.html) Imports a configuration to the session from either a file or a buffer.
- [niDCPower Get Channel Name (Poly) VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-channel-name-poly-vi.html) Converts channel indices to channel names.
- [Other IVI](../../instr-lib/nidcpower/otherivi-mnu.html) Use the NI-DCPower IVI Other VIs to access the IVI Utility functionality.
- [MeasurementLink](../../instr-lib/nidcpower/measurementlink-mnu.html) Use the VIs on this palette in conjunction with MeasurementLink Session Management.

Parent topic:

NI-DCPower
