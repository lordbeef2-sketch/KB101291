# NI DOCUMENT BUNDLE: ni-fgen-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-fgen-labview-api-ref start=251 end=400 -->
<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-errorelaboration.html language=enus -->
## TOPIC 00251: Instrument:Obsolete:Error Elaboration

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-errorelaboration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-errorelaboration.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains an optional string with additional information concerning the primary error condition. Remarks The following table lists the characteristics of this property. Short Name Error Elaboration Data type cstr.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable No

### Instrument:Obsolete:Error Elaboration

Contains an optional string with additional information concerning the primary error condition.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Error Elaboration |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedonboardreferenceclockoutputterminal.html language=enus -->
## TOPIC 00252: Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedonboardreferenceclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedonboardreferenceclockoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal at which to export the onboard Reference Clock. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of this property. Short Name Exported Onboard

### Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal

Specifies the terminal at which to export the onboard Reference Clock.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Onboard Reference Clock Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedreferenceclockoutputterminal.html language=enus -->
## TOPIC 00253: Clocks:Reference Clock:Export Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedreferenceclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedreferenceclockoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal at which to export the Reference Clock. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of this property. Short Name Exported Reference Clock

### Clocks:Reference Clock:Export Output Terminal

Specifies the terminal at which to export the Reference Clock.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Reference Clock Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockdivisor.html language=enus -->
## TOPIC 00254: Clocks:Sample Clock:Exported Sample Clock Divisor

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockdivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockdivisor.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which to divide the update (Sample) Clock before it is exported. To export the Sample Clock, use the niFgen Export Signal VI or the Exported Sample Clock Output Terminal property. Valid Values: 1 to 4,096 Default Value: 1 You cannot change this property while the device is ge

### Clocks:Sample Clock:Exported Sample Clock Divisor

Specifies the factor by which to divide the update (Sample) Clock before it is exported.

To export the Sample Clock, use the [niFgen Export Signal](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI or the [Exported Sample Clock Output Terminal](pnifgen-exportedsampleclockoutputterminal.html) property.

**Valid Values**: 1 to 4,096

**Default Value**: 1

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Sample Clock Divisor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockoutputterminal.html language=enus -->
## TOPIC 00255: Clocks:Sample Clock:Export Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal at which to export the Sample Clock. If you specify a divisor with the Exported Sample Clock Divisor property, the Sample Clock exported with this property is the value of the Sample Clock after it is divided-down. For a list of the terminals available on your device, refer to

### Clocks:Sample Clock:Export Output Terminal

Specifies the terminal at which to export the Sample Clock. If you specify a divisor with the [Exported Sample Clock Divisor](/csh?topicname=pnifgen-exportedsampleclockdivisor.html) property, the Sample Clock exported with this property is the value of the Sample Clock after it is divided-down.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Sample Clock Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebasedivisor.html language=enus -->
## TOPIC 00256: Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebasedivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebasedivisor.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which to divide the device clock (Sample Clock timebase) before it is exported. To export the Sample Clock timebase, use the niFgen Export Signal VI or the Exported Sample Clock Timebase Output Terminal property. Valid Values: 1 to 4,194,304 Not all devices support a divisor

### Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor

Specifies the factor by which to divide the device clock (Sample Clock timebase) before it is exported.

To export the Sample Clock timebase, use the [niFgen Export Signal](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI or the [Exported Sample Clock Timebase Output Terminal](pnifgen-exportedsampleclocktimebaseoutputterminal.html) property.

**Valid Values**: 1 to 4,194,304

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Sample Clock Timebase Divisor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebaseoutputterminal.html language=enus -->
## TOPIC 00257: Clocks:Sample Clock Timebase:Export Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebaseoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebaseoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal at which to export the Sample Clock Timebase. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. If you specify a divisor with the Exported Sample Clock Timebase Divisor property, the Sample Clock ti

### Clocks:Sample Clock Timebase:Export Output Terminal

Specifies the terminal at which to export the Sample Clock Timebase.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

If you specify a divisor with the [Exported Sample Clock Timebase Divisor](pnifgen-exportedsampleclocktimebasedivisor.html) property, the Sample Clock timebase exported with the Exported Sample Clock Timebase Output Terminal property is the value of the Sample Clock timebase after it is divided down.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Sample Clock Timebase Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedscripttriggeroutputterminal.html language=enus -->
## TOPIC 00258: Triggers:Script:Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedscripttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedscripttriggeroutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for the exported Script Trigger. Setting this property to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated. For a list of the terminals available on your device, refer to the Rou

### Triggers:Script:Output Terminal

Specifies the output terminal for the exported Script Trigger.

Setting this property to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Script Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedstarttriggeroutputterminal.html language=enus -->
## TOPIC 00259: Triggers:Start:Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedstarttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedstarttriggeroutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for exporting the Start Trigger. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of this property. Short Name Exported Start Trigg

### Triggers:Start:Output Terminal

Specifies the destination terminal for exporting the Start Trigger.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Start Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalclockdelaybinaryvalue.html language=enus -->
## TOPIC 00260: Clocks:Advanced:External Clock Delay Binary Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalclockdelaybinaryvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalclockdelaybinaryvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the external clock delay binary value. Remarks The following table lists the characteristics of this property. Short Name External Clock Delay Binary Value Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Clocks:Advanced:External Clock Delay Binary Value

Specifies the external clock delay binary value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Clock Delay Binary Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalsampleclockmultiplier.html language=enus -->
## TOPIC 00261: Clocks:Advanced:External Sample Clock Multiplier

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalsampleclockmultiplier.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalsampleclockmultiplier.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample Clock. The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When u

### Clocks:Advanced:External Sample Clock Multiplier

Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample Clock.

The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When using this property, you do not need to explicitly set the external clock rate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Sample Clock Multiplier |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filetransferblocksize.html language=enus -->
## TOPIC 00262: Arbitrary Waveform:Data Transfer:File Transfer Block Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filetransferblocksize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filetransferblocksize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of samples to transfer at one time from the device to host memory. This property is used in conjunction with the niFgen Create Waveform From File VI and the niFgen Write Waveform From File VI. If the requested value is not evenly divisible by the required increment, this

### Arbitrary Waveform:Data Transfer:File Transfer Block Size

Specifies the maximum number of samples to transfer at one time from the device to host memory. This property is used in conjunction with the [niFgen Create Waveform From File](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI and the [niFgen Write Waveform From File](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI.

If the requested value is not evenly divisible by the required increment, this property is coerced up to the next 64-sample increment (32-sample increment for complex samples).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | File Transfer Block Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtercorrectionfrequency.html language=enus -->
## TOPIC 00263: Instrument:5401/5411/5431:Filter Correction Frequency

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtercorrectionfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtercorrectionfrequency.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the filter correction frequency of the analog filter. This property can correct for the ripples in the analog filter frequency response at the frequency specified. When using the Standard Waveform output mode, this property should be set to the same frequency as the standard waveform. To d

### Instrument:5401/5411/5431:Filter Correction Frequency

Specifies the filter correction frequency of the analog filter. This property can correct for the ripples in the analog filter frequency response at the frequency specified.

When using the Standard Waveform output mode, this property should be set to the same frequency as the standard waveform. To disable filter correction, set this property to 0.

**Units**: hertz (Hz)

**Default Value**: 0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Correction Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Analog Filter |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtertype.html language=enus -->
## TOPIC 00264: Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Filter Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtertype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse-shaping filter type for the FIR filter. Remarks The following table lists the characteristics of this property. Short Name Filter Type Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes Flat 0 Applies a flat filter to the data with the p

### Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Filter Type

Specifies the pulse-shaping filter type for the FIR filter.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Flat | 0 | Applies a flat filter to the data with the passband value specified in the Flat Filter Passband property. |
| --- | --- | --- |
| Raised Cosine | 1 | Applies a raised cosine filter to the data with the alpha value specified in the Raised Cosine Filter Alpha property. |
| Root Raised Cosine | 2 | Applies a root raised cosine filter to the data with the alpha value specified in the Root Raised Cosine Filter Alpha property. |
| Gaussian | 3 | Applies a Gaussian filter to the data with the BT value specified in the Gaussian Filter BT property. |
| Custom | 4 | Applies a custom filter to the data. If Custom is selected, you must provide a set of FIR filter coefficients with the niFgen Configure Custom FIR Filter Coefficients VI. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firfilterenabled.html language=enus -->
## TOPIC 00265: Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Filter Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firfilterenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specify TRUE to enables the FIR filter. Specify FALSE to disable the FIR filter. You must set the CIC Filter Enabled property and the FIR Filter Enabled property to the same value. Remarks The following table lists the characteristics of this property. Short Name FIR Filter Enabled Data type cbool.p

### Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Filter Enabled

Specify TRUE to enables the FIR filter. Specify FALSE to disable the FIR filter.

Note

CIC Filter Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FIR Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firinterpolation.html language=enus -->
## TOPIC 00266: Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Interpolation Factor

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firinterpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firinterpolation.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interpolation factor for the FIR filter. If you do not set this value, NI-FGEN calculates the appropriate value based on the value of the IQ Rate property. Remarks The following table lists the characteristics of this property. Short Name FIR Interpolation Data type cdbl.png Permission

### Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Interpolation Factor

Specifies the interpolation factor for the FIR filter. If you do not set this value, NI-FGEN calculates the appropriate value based on the value of the [IQ Rate](/csh?topicname=pnifgen-iqrate.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FIR Interpolation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firmwarerevision.html language=enus -->
## TOPIC 00267: Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firmwarerevision.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the firmware revision information for the instrument you are currently using. Remarks The following table lists the characteristics of this property. Short Name Firmware Revision Data type cstr.png Permissions Read Only High-level VIs niFgen Revision Query Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision

Returns the firmware revision information for the instrument you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Firmware Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Revision Query |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatfilterpassband.html language=enus -->
## TOPIC 00268: Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatfilterpassband.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatfilterpassband.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the passband value to use when calculating the FIR filter coefficients. The FIR filter is designed to be flat to passband × I/Q rate. This property is used only when the Filter Type property is set to Flat. Remarks The following table lists the characteristics of this property. Short Name

### Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband

Specifies the passband value to use when calculating the FIR filter coefficients. The FIR filter is designed to be flat to passband × I/Q rate. This property is used only when the [Filter Type](/csh?topicname=pnifgen-filtertype.html) property is set to **Flat**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Flat Filter Passband |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatnesscorrectionenabled.html language=enus -->
## TOPIC 00269: Output:Filters:Flatness Correction Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatnesscorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatnesscorrectionenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specify a value of TRUE to enable flatness correction. When flatness correction is enabled, the signal generator applies a flatness correction factor to the generated sine wave to ensure the same output power level at all frequencies. Set this property to FALSE when performing flatness calibration.

### Output:Filters:Flatness Correction Enabled

Specify a value of TRUE to enable flatness correction. When flatness correction is enabled, the signal generator applies a flatness correction factor to the generated sine wave to ensure the same output power level at all frequencies.

Set this property to FALSE when performing flatness calibration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Flatness Correction Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-fpgabitfilepath.html language=enus -->
## TOPIC 00270: Instrument:FPGA Bitfile Path

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-fpgabitfilepath.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-fpgabitfilepath.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute file path to the bitfile loaded on the FPGA. Remarks The following table lists the characteristics of this property. Short Name FPGA Bitfile Path Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Instrument:FPGA Bitfile Path

Gets the absolute file path to the bitfile loaded on the FPGA.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA Bitfile Path |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequency.html language=enus -->
## TOPIC 00271: Standard Function:Standard Function Mode:Frequency

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequency.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the frequency of the standard waveform that the signal generator produces. Units: hertz (Hz) Default Value: None This parameter does not affect signal generator behavior when you set the Waveform property to NIFGEN_VAL_WFM_DC. For NIFGEN_VAL_WFM_SINE , the range is between 0 MHz and 16 MHz,

### Standard Function:Standard Function Mode:Frequency

Controls the frequency of the standard waveform that the signal generator produces.

**Units**: hertz (Hz)

**Default Value**: None

Note

Waveform

NIFGEN_VAL_WFM_DC

NIFGEN_VAL_WFM_SINE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Standard Waveform |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylistdurationquantum.html language=enus -->
## TOPIC 00272: Standard Function:Frequency List Mode:Frequency List Duration Quantum

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylistdurationquantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylistdurationquantum.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the quantum that all durations must be a multiple of in a frequency list. Remarks The following table lists the characteristics of this property. Short Name Frequency List Duration Quantum Data type cdbl.png Permissions Read/Write High-level VIs niFgen Query Freq List Capabilities Channel-ba

### Standard Function:Frequency List Mode:Frequency List Duration Quantum

Returns the quantum that all durations must be a multiple of in a frequency list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency List Duration Quantum |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Query Freq List Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylisthandle.html language=enus -->
## TOPIC 00273: Standard Function:Frequency List Mode:Frequency List Handle

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylisthandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylisthandle.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets which frequency list the signal generator produces. You create a frequency list using the niFgen Create Frequency List VI. The niFgen Create Frequency List VI returns a handle that you use to identify the list. Default Value: None You cannot change this property while the device is generating a

### Standard Function:Frequency List Mode:Frequency List Handle

Sets which frequency list the signal generator produces. You create a frequency list using the [niFgen Create Frequency List](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI. The niFgen Create Frequency List VI returns a handle that you use to identify the list.

**Default Value**: None

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency List Handle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Frequency List |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencyshift.html language=enus -->
## TOPIC 00274: Arbitrary Waveform:Onboard Signal Processing:Frequency Shift

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencyshift.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencyshift.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of frequency shift applied to the baseband signal. When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN restricts this property value to 0. Remarks The following table lists the characteristics of this property. Short Name Frequency Shift Data type cdbl.png P

### Arbitrary Waveform:Onboard Signal Processing:Frequency Shift

Specifies the amount of frequency shift applied to the baseband signal.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency Shift |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaindacvalue.html language=enus -->
## TOPIC 00275: Instrument:Calibration:Gain DAC Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaindacvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaindacvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value programmed to the Gain DAC. The value should be treated as an unsigned, right-justified number. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generatio

### Instrument:Calibration:Gain DAC Value

Specifies the value programmed to the Gain DAC. The value should be treated as an unsigned, right-justified number.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Gain DAC Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaussianfilterbt.html language=enus -->
## TOPIC 00276: Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Gaussian:BT

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaussianfilterbt.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaussianfilterbt.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the BT value to use when calculating the pulse-shaping FIR filter coefficients. The BT value is the product of the -3 dB bandwidth and the symbol period. This property is used only when the Filter Type property is set to Gaussian. Remarks The following table lists the characteristics of th

### Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Gaussian:BT

Specifies the BT value to use when calculating the pulse-shaping FIR filter coefficients. The BT value is the product of the -3 dB bandwidth and the symbol period. This property is used only when the [Filter Type](/csh?topicname=pnifgen-filtertype.html) property is set to **Gaussian**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Gaussian Filter BT |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlebehavior.html language=enus -->
## TOPIC 00277: Output:Advanced:Idle Behavior

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlebehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlebehavior.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the output during the Idle state. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The following table lists the cha

### Output:Advanced:Idle Behavior

Specifies the behavior of the output during the Idle state.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Idle Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Hold Last Value | 400 | While in the Idle state, the output signal remains at the last voltage generated prior to entering the Idle state. |
| --- | --- | --- |
| Jump To Value | 401 | While in the Idle state, the output signal remains at the value configured in the Idle Value property. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlevalue.html language=enus -->
## TOPIC 00278: Output:Advanced:Idle Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlevalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlevalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value to generate in the Idle state. You must set the Idle Behavior property to Jump To Value to use this property. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for

### Output:Advanced:Idle Value

Specifies the value to generate in the Idle state. You must set the [Idle Behavior](/csh?topicname=pnifgen-idlebehavior.html) property to **Jump To Value** to use this property.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Idle Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-interchangecheck.html language=enus -->
## TOPIC 00279: Instrument:Inherent IVI Attributes:User Options:Interchange Check

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-interchangecheck.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to perform interchangeability checking and log interchangeability warnings when you call VIs. Set this property to TRUE to enable interchangeability checking. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior

### Instrument:Inherent IVI Attributes:User Options:Interchange Check

Specifies whether to perform interchangeability checking and log interchangeability warnings when you call VIs. Set this property to TRUE to enable interchangeability checking.

Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Interchangeability checking examines the properties in a capability group only if you specify a value for at least one property within that group. Interchangeability warnings can occur when a property affects the behavior of the instrument and you have not set that property or the property has been invalidated since you set it.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interchange Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Initialize With Options |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-iqrate.html language=enus -->
## TOPIC 00280: Arbitrary Waveform:Onboard Signal Processing:IQ Rate

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-iqrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-iqrate.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate at which the user-provided waveform data is generated when the OSP Enabled property is set to TRUE. NI-FGEN sets the Sample Rate property of the signal generator to the product of the IQ Rate, FIR Interpolation Factor, and CIC Interpolation Factor properties. When the Data Process

### Arbitrary Waveform:Onboard Signal Processing:IQ Rate

Specifies the rate at which the user-provided waveform data is generated when the [OSP Enabled](/csh?topicname=pnifgen-ospenabled.html) property is set to TRUE.

NI-FGEN sets the [Sample Rate](pnifgen-samplerate.html) property of the signal generator to the product of the IQ Rate, [FIR Interpolation Factor](pnifgen-firinterpolation.html), and [CIC Interpolation Factor](pnifgen-cicinterpolation.html) properties. When the [Data Processing Mode](pnifgen-dataprocessingmode.html) property is set to **Real**, the IQ Rate value is the rate at which the signal generator processes real (I) data. When the Data Processing Mode property is set to **Complex**, the IQ Rate value is the rate at which the signal generator processes complex (I/Q) data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-loadimpedance.html language=enus -->
## TOPIC 00281: Output:Load Impedance

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-loadimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-loadimpedance.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the load impedance connected to the analog output of the channel. If the load impedance is set to -1.0, NI-FGEN matches the load impedance to the Output Impedance property value. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V). You

### Output:Load Impedance

Specifies the load impedance connected to the analog output of the channel.

If the load impedance is set to -1.0, NI-FGEN matches the load impedance to the [Output Impedance](pnifgen-outputimpedance.html) property value. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Load Impedance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-logicalname.html language=enus -->
## TOPIC 00282: Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-logicalname.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the logical name you specified when opening the current IVI session. You may pass a logical name to the niFgen Initialize VI or the niFgen Initialize With Options VI. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrume

### Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name

Returns the logical name you specified when opening the current IVI session.

You may pass a logical name to the [niFgen Initialize](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI or the [niFgen Initialize With Options](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logical Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-majorversion.html language=enus -->
## TOPIC 00283: Instrument:Obsolete:Major Version

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-majorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-majorversion.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the major version number of NI-FGEN. Remarks The following table lists the characteristics of this property. Short Name Major Version Data type ci32.png Permissions Read Only High-level VIs niFgen Revision Query Channel-based Yes Resettable No

### Instrument:Obsolete:Major Version

Returns the major version number of NI-FGEN.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Major Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Revision Query |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manualconfigurationenabled.html language=enus -->
## TOPIC 00284: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Manual Configuration Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manualconfigurationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manualconfigurationenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables (TRUE) or disables (FALSE) manual configuration for a peer-to-peer endpoint. Enabling this property disables automatic NI-P2P stream manager flow control and Done Notifications. Remarks The following table lists the characteristics of this property. Short Name Manual Configuration Enabled Da

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Manual Configuration Enabled

Enables (TRUE) or disables (FALSE) manual configuration for a peer-to-peer endpoint. Enabling this property disables automatic NI-P2P stream manager flow control and Done Notifications.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Manual Configuration Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manufacturer.html language=enus -->
## TOPIC 00285: Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manufacturer.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of the instrument manufacturer you are currently using. Remarks The following table lists the characteristics of this property. Short Name Manufacturer Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer

Returns the name of the instrument manufacturer you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Manufacturer |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayunits.html language=enus -->
## TOPIC 00286: Events:Marker:Advanced:Delay Units

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayunits.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units used for the Marker Event Delay Value property. Remarks The following table lists the characteristics of this property. Short Name Marker Event Delay Units Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes Sample Clock Periods 101 The d

### Events:Marker:Advanced:Delay Units

Specifies the units used for the [Marker Event Delay Value](/csh?topicname=pnifgen-markereventdelayvalue.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Delay Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Sample Clock Periods | 101 | The delay is specified in Sample Clock periods and then coerced up by NI-FGEN to the nearest Sample Clock period. |
| --- | --- | --- |
| Seconds | 102 | The delay is specified in seconds and then coerced up by NI-FGEN to the nearest Sample Clock period. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayvalue.html language=enus -->
## TOPIC 00287: Events:Marker:Advanced:Delay Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of delay applied to a Marker Event with respect to the analog output of the signal generator. A positive delay value indicates that the Marker Event occurs after the analog data, while a negative delay value indicates that the Marker Event occurs before the analog data. The defa

### Events:Marker:Advanced:Delay Value

Specifies the amount of delay applied to a Marker Event with respect to the analog output of the signal generator.

A positive delay value indicates that the Marker Event occurs after the analog data, while a negative delay value indicates that the Marker Event occurs before the analog data. The default value is zero, which aligns the Marker Event with the analog output.

You can specify the units of the delay value using the [Marker Event Delay Units](pnifgen-markereventdelayunits.html) property.

**Default Value**: 0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Delay Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlatchedstatus.html language=enus -->
## TOPIC 00288: Events:Marker:Advanced:Latched Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlatchedstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlatchedstatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the latched status of the specified Marker Event. Set this property to FALSE to clear the latched status of the Marker Event. Remarks The following table lists the characteristics of this property. Short Name Marker Event Latched Status Data type cbool.png Permissions Read/Write High-level

### Events:Marker:Advanced:Latched Status

Specifies the latched status of the specified Marker Event. Set this property to FALSE to clear the latched status of the Marker Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Latched Status |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlivestatus.html language=enus -->
## TOPIC 00289: Events:Marker:Advanced:Live Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlivestatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlivestatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns TRUE if the status of the specified Marker Event is live, and FALSE otherwise. Remarks The following table lists the characteristics of this property. Short Name Marker Event Live Status Data type cbool.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Events:Marker:Advanced:Live Status

Returns TRUE if the status of the specified Marker Event is live, and FALSE otherwise.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Live Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputbehavior.html language=enus -->
## TOPIC 00290: Events:Marker:Output Behavior

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputbehavior.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior for the Marker Event. Remarks The following table lists the characteristics of this property. Short Name Marker Event Output Behavior Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes Pulse 101 Triggers a pulse for a specified

### Events:Marker:Output Behavior

Specifies the output behavior for the Marker Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Output Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Pulse | 101 | Triggers a pulse for a specified period of time. |
| --- | --- | --- |
| Toggle | 103 | Changes to high or low while the event is active, depending on the active state you specify. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputterminal.html language=enus -->
## TOPIC 00291: Events:Marker:Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Marker Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of this property. Short Name Marker Event Output Terminal Da

### Events:Marker:Output Terminal

Specifies the destination terminal for the Marker Event.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsepolarity.html language=enus -->
## TOPIC 00292: Events:Marker:Pulse:Polarity

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsepolarity.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output polarity of the Marker Event. Remarks The following table lists the characteristics of this property. Short Name Marker Event Pulse Polarity Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes Active High 101 The Marker Event level is hi

### Events:Marker:Pulse:Polarity

Specifies the output polarity of the Marker Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Active High | 101 | The Marker Event level is high at the marker position. |
| --- | --- | --- |
| Active Low | 102 | The Marker Event level is low at the marker position. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthunits.html language=enus -->
## TOPIC 00293: Events:Marker:Pulse:Width Units

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthunits.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse width units of the Marker Event. Remarks The following table lists the characteristics of this property. Short Name Marker Event Pulse Width Units Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes Sample Clock Periods 101 Specifies the

### Events:Marker:Pulse:Width Units

Specifies the pulse width units of the Marker Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Pulse Width Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Sample Clock Periods | 101 | Specifies the pulse width in Sample Clock periods. |
| --- | --- | --- |
| Seconds | 102 | Specifies the pulse width in seconds. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthvalue.html language=enus -->
## TOPIC 00294: Events:Marker:Pulse:Width Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse width value of the Marker Event. Set the units for the values with the Marker Event Pulse Width Units property. Remarks The following table lists the characteristics of this property. Short Name Marker Event Pulse Width Value Data type cdbl.png Permissions Read/Write High-level V

### Events:Marker:Pulse:Width Value

Specifies the pulse width value of the Marker Event. Set the units for the values with the [Marker Event Pulse Width Units](/csh?topicname=pnifgen-markereventpulsewidthunits.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Pulse Width Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventtoggleinitialstate.html language=enus -->
## TOPIC 00295: Events:Marker:Toggle:Initial State

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventtoggleinitialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventtoggleinitialstate.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the Marker Event. Remarks The following table lists the characteristics of this property. Short Name Marker Event Toggle Initial State Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes High 101 Sets the initial state of the M

### Events:Marker:Toggle:Initial State

Specifies the initial state of the Marker Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Event Toggle Initial State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| High | 101 | Sets the initial state of the Marker Event to high. |
| --- | --- | --- |
| Low | 102 | Sets the initial state of the Marker Event to low. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markerscount.html language=enus -->
## TOPIC 00296: Instrument:Marker Events Count

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markerscount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markerscount.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of markers supported by the device. Use this property when the Output Mode property is set to NIFGEN_VAL_OUTPUT_SCRIPT. Remarks The following table lists the characteristics of this property. Short Name Markers Count Data type ci32.png Permissions Read Only High-level VIs N/A Chan

### Instrument:Marker Events Count

Returns the number of markers supported by the device. Use this property when the [Output Mode](/csh?topicname=pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_SCRIPT**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Markers Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbandwidth.html language=enus -->
## TOPIC 00297: Arbitrary Waveform:Data Transfer:Maximum Bandwidth

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbandwidth.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum amount of bus bandwidth to use for data transfers. The signal generator limits data transfer speeds on the PCI Express bus to the value you specify for this property. Set this property to optimize bus bandwidth usage for multidevice streaming applications by preventing the sign

### Arbitrary Waveform:Data Transfer:Maximum Bandwidth

Specifies the maximum amount of bus bandwidth to use for data transfers.

The signal generator limits data transfer speeds on the PCI Express bus to the value you specify for this property. Set this property to optimize bus bandwidth usage for multidevice streaming applications by preventing the signal generator from consuming all the available bandwidth on a PCI Express link when waveforms are being written to the onboard memory of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbuffersize.html language=enus -->
## TOPIC 00298: Standard Function:Standard Function Mode:Maximum Buffer Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbuffersize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of samples that can be used in the standard function waveform buffer. Increasing this value may increase the quality of the waveform but may also increase the amount of time required to change the waveform while running. This property is valid only on devices that implement S

### Standard Function:Standard Function Mode:Maximum Buffer Size

Sets the maximum number of samples that can be used in the standard function waveform buffer. Increasing this value may increase the quality of the waveform but may also increase the amount of time required to change the waveform while running.

This property is valid only on devices that implement Standard Function output mode in software, and it is read-only for all other devices.

Note

Standard Function Mode

NI Signal Generators Help

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Buffer Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistduration.html language=enus -->
## TOPIC 00299: Standard Function:Frequency List Mode:Maximum Frequency List Duration

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistduration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistduration.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum duration, in seconds, of any one step in the frequency list. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The followin

### Standard Function:Frequency List Mode:Maximum Frequency List Duration

Returns the maximum duration, in seconds, of any one step in the frequency list.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Frequency List Duration |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Freq List Capabilities |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistlength.html language=enus -->
## TOPIC 00300: Standard Function:Frequency List Mode:Maximum Frequency List Length

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistlength.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistlength.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of steps that can be in a frequency list. Remarks The following table lists the characteristics of this property. Short Name Max Frequency List Length Data type ci32.png Permissions Read Only High-level VIs niFgen Query Freq List Capabilities Channel-based Yes Resettable N

### Standard Function:Frequency List Mode:Maximum Frequency List Length

Returns the maximum number of steps that can be in a frequency list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Frequency List Length |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Freq List Capabilities |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumin-flightreadrequests.html language=enus -->
## TOPIC 00301: Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumin-flightreadrequests.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumin-flightreadrequests.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue. When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the numb

### Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests

Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.

When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this property is set to the highest value the signal generator supports.

If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This change helps to reduce the amount of data the signal generator reads at one time.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum In-Flight Read Requests |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumnumberoffrequencylists.html language=enus -->
## TOPIC 00302: Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumnumberoffrequencylists.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumnumberoffrequencylists.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of frequency lists that the signal generator allows. Remarks The following table lists the characteristics of this property. Short Name Max Number Of Frequency Lists Data type ci32.png Permissions Read Only High-level VIs niFgen Query Freq List Capabilities Channel-based N

### Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists

Returns the maximum number of frequency lists that the signal generator allows.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Number Of Frequency Lists |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Freq List Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxloopcount.html language=enus -->
## TOPIC 00303: Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxloopcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxloopcount.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of times the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator. Remarks The following table lists the characteristics of this property. Short Name Max Loop Count Data type ci32.png Permissions Read Only High-le

### Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count

Returns the maximum number of times the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Loop Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Sequence Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofsequences.html language=enus -->
## TOPIC 00304: Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofsequences.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofsequences.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of arbitrary sequences the signal generator allows. Remarks The following table lists the characteristics of this property. Short Name Max Number of Sequences Data type ci32.png Permissions Read Only High-level VIs niFgen Query Arb Sequence Capabilities Channel-based No Re

### Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences

Returns the maximum number of arbitrary sequences the signal generator allows.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Number of Sequences |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Sequence Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofwaveforms.html language=enus -->
## TOPIC 00305: Arbitrary Waveform:Capabilities:Max Number of Waveforms

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofwaveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofwaveforms.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators, this value may vary with remaining onboard memory. Remarks The following table lists the characteristics of this property. Short Name Max Number of Waveforms Data type ci32.png Permissions

### Arbitrary Waveform:Capabilities:Max Number of Waveforms

Returns the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators, this value may vary with remaining onboard memory.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Number of Waveforms |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Waveform Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxsequencelength.html language=enus -->
## TOPIC 00306: Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxsequencelength.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxsequencelength.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of arbitrary waveforms the signal generator allows in a sequence. Remarks The following table lists the characteristics of this property. Short Name Max Sequence Length Data type ci32.png Permissions Read Only High-level VIs niFgen Query Arb Sequence Capabilities Channel-b

### Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length

Returns the maximum number of arbitrary waveforms the signal generator allows in a sequence.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Sequence Length |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Sequence Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxwaveformsize.html language=enus -->
## TOPIC 00307: Arbitrary Waveform:Capabilities:Max Waveform Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxwaveformsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxwaveformsize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of points the signal generator allows in an arbitrary waveform. On some signal generators, this value may vary with remaining onboard memory. Remarks The following table lists the characteristics of this property. Short Name Max Waveform Size Data type ci32.png Permissions

### Arbitrary Waveform:Capabilities:Max Waveform Size

Returns the maximum number of points the signal generator allows in an arbitrary waveform. On some signal generators, this value may vary with remaining onboard memory.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Max Waveform Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Waveform Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-memorysize.html language=enus -->
## TOPIC 00308: Instrument:Memory Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-memorysize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-memorysize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the amount of memory in bytes on the signal generator. Remarks The following table lists the characteristics of this property. Short Name Memory Size Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Memory Size

Returns the amount of memory in bytes on the signal generator.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Memory Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistduration.html language=enus -->
## TOPIC 00309: Standard Function:Frequency List Mode:Minimum Frequency List Duration

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistduration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistduration.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum duration, in seconds, of any one step in a frequency list. Remarks The following table lists the characteristics of this property. Short Name Min Frequency List Duration Data type cdbl.png Permissions Read Only High-level VIs niFgen Query Freq List Capabilities Channel-based Yes

### Standard Function:Frequency List Mode:Minimum Frequency List Duration

Returns the minimum duration, in seconds, of any one step in a frequency list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Min Frequency List Duration |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Freq List Capabilities |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistlength.html language=enus -->
## TOPIC 00310: Standard Function:Frequency List Mode:Minimum Frequency List Length

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistlength.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistlength.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum number of frequency lists that the signal generator allows. Remarks The following table lists the characteristics of this property. Short Name Min Frequency List Length Data type ci32.png Permissions Read Only High-level VIs niFgen Query Freq List Capabilities Channel-based Yes R

### Standard Function:Frequency List Mode:Minimum Frequency List Length

Returns the minimum number of frequency lists that the signal generator allows.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Min Frequency List Length |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Freq List Capabilities |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minorversion.html language=enus -->
## TOPIC 00311: Instrument:Obsolete:Minor Version

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minorversion.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minor version number of NI-FGEN. Remarks The following table lists the characteristics of this property. Short Name Minor Version Data type ci32.png Permissions Read Only High-level VIs niFgen Revision Query Channel-based Yes Resettable No

### Instrument:Obsolete:Minor Version

Returns the minor version number of NI-FGEN.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Minor Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Revision Query |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minsequencelength.html language=enus -->
## TOPIC 00312: Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minsequencelength.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minsequencelength.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum number of arbitrary waveforms the signal generator allows in a sequence. Typically, this value is constant for the signal generator. Remarks The following table lists the characteristics of this property. Short Name Min Sequence Length Data type ci32.png Permissions Read Only Hig

### Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length

Returns the minimum number of arbitrary waveforms the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Min Sequence Length |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Sequence Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minwaveformsize.html language=enus -->
## TOPIC 00313: Arbitrary Waveform:Capabilities:Min Waveform Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minwaveformsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minwaveformsize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum number of points the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator. In some cases, you may need to supply a larger waveform than the value specified by this property. Refer to the "Features Supported" topic for your d

### Arbitrary Waveform:Capabilities:Min Waveform Size

Returns the minimum number of points the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.

Note

NI Signal Generators Help

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Min Waveform Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Waveform Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-model.html language=enus -->
## TOPIC 00314: Instrument:Inherent IVI Attributes:Instrument Identification:Model

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-model.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the model number or name of the instrument that you are currently using. Remarks The following table lists the characteristics of this property. Short Name Model Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Instrument Identification:Model

Returns the model number or name of the instrument that you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Model |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-modulerevision.html language=enus -->
## TOPIC 00315: Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-modulerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-modulerevision.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision letter of the module you are using. Remarks The following table lists the characteristics of this property. Short Name Module Revision Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision

Returns the revision letter of the module you are using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Module Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-mostspaceavailableinendpoint.html language=enus -->
## TOPIC 00316: Arbitrary Waveform:Peer-to-Peer:Most Space Available In Endpoint

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-mostspaceavailableinendpoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-mostspaceavailableinendpoint.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the largest number of samples per channel available in the endpoint since this property was last read. This property can be used to determine how much endpoint space to use as a buffer against PCI Express bus traffic latencies by reading the property and keeping track of the largest value re

### Arbitrary Waveform:Peer-to-Peer:Most Space Available In Endpoint

Returns the largest number of samples per channel available in the endpoint since this property was last read. This property can be used to determine how much endpoint space to use as a buffer against PCI Express bus traffic latencies by reading the property and keeping track of the largest value returned. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

If you want to minimize the latency for data to move through the endpoint and be generated by the signal generator, use the [Data Transfer Permission Initial Credits](pnifgen-datatransferpermissioninitialcredits.html) property to grant fewer initial credits than the default of the entire endpoint size.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Most Space Available In Endpoint |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-offsetdacvalue.html language=enus -->
## TOPIC 00317: Instrument:Calibration:Offset DAC Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-offsetdacvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-offsetdacvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value programmed to the Offset DAC. The value should be treated as an unsigned, right-justified number. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generat

### Instrument:Calibration:Offset DAC Value

Specifies the value programmed to the Offset DAC. The value should be treated as an unsigned, right-justified number.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Offset DAC Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-operationmode.html language=enus -->
## TOPIC 00318: Instrument:Obsolete:Operation Mode

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-operationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-operationmode.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the signal generator produces waveforms. NI signal generators currently support only one value: NIFGEN_VAL_OPERATE_CONTINUOUS. To control trigger mode, set the Trigger Mode property. Remarks The following table lists the characteristics of this property. Short Name Operation Mode Data

### Instrument:Obsolete:Operation Mode

Specifies how the signal generator produces waveforms. NI signal generators currently support only one value: **NIFGEN_VAL_OPERATE_CONTINUOUS**. To control trigger mode, set the [Trigger Mode](/csh?topicname=pnifgen-triggermode.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Operation Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

| NIFGEN_VAL_OPERATE_CONTINUOUS | 0 | Continuous operation |
| --- | --- | --- |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorfreqdacvalue.html language=enus -->
## TOPIC 00319: Instrument:Calibration:Oscillator Freq DAC Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorfreqdacvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorfreqdacvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value programmed to the Oscillator DAC. The value should be treated as an unsigned, right-justified number. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the gen

### Instrument:Calibration:Oscillator Freq DAC Value

Specifies the value programmed to the Oscillator DAC. The value should be treated as an unsigned, right-justified number.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Oscillator Freq DAC Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorphasedacvalue.html language=enus -->
## TOPIC 00320: Clocks:Advanced:Oscillator Phase DAC Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorphasedacvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorphasedacvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the oscillator phase DAC value. Remarks The following table lists the characteristics of this property. Short Name Oscillator Phase DAC Value Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Clocks:Advanced:Oscillator Phase DAC Value

Specifies the oscillator phase DAC value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Oscillator Phase DAC Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospenabled.html language=enus -->
## TOPIC 00321: Arbitrary Waveform:Onboard Signal Processing:OSP Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables (TRUE) or disables (FALSE) the OSP block of the signal generator. When the OSP block is disabled, all OSP-related properties are disabled and have no effect on the generated signal. Remarks The following table lists the characteristics of this property. Short Name OSP Enabled Data type cbool

### Arbitrary Waveform:Onboard Signal Processing:OSP Enabled

Enables (TRUE) or disables (FALSE) the OSP block of the signal generator. When the OSP block is disabled, all OSP-related properties are disabled and have no effect on the generated signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OSP Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospmode.html language=enus -->
## TOPIC 00322: Arbitrary Waveform:Onboard Signal Processing:OSP Mode

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospmode.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the generation mode of the OSP, which determines the type of data contained in the output signal. For more information about the OSP modes your device supports, refer to Devices section of the NI Signal Generators Help. When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FG

### Arbitrary Waveform:Onboard Signal Processing:OSP Mode

Specifies the generation mode of the OSP, which determines the type of data contained in the output signal.

For more information about the OSP modes your device supports, refer to [Devices](/csh?context=nifgen_siggenhelp_device_specific) section of the *NI Signal Generators Help*.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OSP Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| IF | 0 | Specifies that the OSP block generates intermediate frequency (IF) data. |
| --- | --- | --- |
| BaseBand | 1 | Specifies that the OSP block generates baseband data. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowerrorreporting.html language=enus -->
## TOPIC 00323: Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Error Reporting

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowerrorreporting.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowerrorreporting.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures error reporting when the OSP block detects an overflow in any of its stages. Overflows lead to waveform clipping. You can use the OSP Overflow Status property to query for overflow conditions regardless of the setting of the OSP Overflow Error Reporting property. The device continues to g

### Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Error Reporting

Configures error reporting when the OSP block detects an overflow in any of its stages. Overflows lead to waveform clipping.

You can use the [OSP Overflow Status](pnifgen-ospoverflowstatus.html) property to query for overflow conditions regardless of the setting of the OSP Overflow Error Reporting property. The device continues to generate after an overflow regardless of the setting of the OSP Overflow Error Reporting property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OSP Overflow Error Reporting |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Error | 0 | Specifies that NI-FGEN returns errors whenever an overflow has occurred in the OSP block. |
| --- | --- | --- |
| Disabled | 2 | Specifies that NI-FGEN does not return errors when an overflow occurs in the OSP block. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowstatus.html language=enus -->
## TOPIC 00324: Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowstatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a bit field of the overflow status in any stage of the OSP block. This property is functional regardless of the value for the OSP Overflow Error Reporting property. Set this property to 0 to clear the current OSP overflow status. Remarks The following table lists the characteristics of this

### Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Status

Returns a bit field of the overflow status in any stage of the OSP block. This property is functional regardless of the value for the [OSP Overflow Error Reporting](/csh?topicname=pnifgen-ospoverflowerrorreporting.html) property.

Set this property to 0 to clear the current OSP overflow status.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OSP Overflow Status |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputenabled.html language=enus -->
## TOPIC 00325: Output:Output Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal that the signal generator produces appears at the output connector. Remarks The following table lists the characteristics of this property. Short Name Output Enabled Data type cbool.png Permissions Read/Write High-level VIs niFgen Output Enable Channel-based Yes Resettab

### Output:Output Enabled

Specifies whether the signal that the signal generator produces appears at the output connector.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Output Enable |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputimpedance.html language=enus -->
## TOPIC 00326: Output:Output Impedance

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputimpedance.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output impedance of the signal generator at the output connector. NI signal generators have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the Load Impedance property value matches the output impedance, the voltage at the signal output connector is at the

### Output:Output Impedance

Specifies the output impedance of the signal generator at the output connector. NI signal generators have an output impedance of 50 ohms and an optional 75 ohms on select modules.

If the [Load Impedance](pnifgen-loadimpedance.html) property value matches the output impedance, the voltage at the signal output connector is at the necessary level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Impedance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Output Impedance |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputmode.html language=enus -->
## TOPIC 00327: Output:Output Mode

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputmode.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output mode the signal generator uses. The output mode you specify determines which VIs and properties you use to configure the waveform the signal generator produces. You cannot change this property while the device is generating a waveform. If you want to change the device configurat

### Output:Output Mode

Specifies the output mode the signal generator uses. The output mode you specify determines which VIs and properties you use to configure the waveform the signal generator produces.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Output Mode |
| Channel-based | No |
| Resettable | No |

| NIFGEN_VAL_OUTPUT_FUNC | 0 | Standard Function mode—Generates standard function waveforms such as sine, square, triangle, and so on. |
| --- | --- | --- |
| NIFGEN_VAL_OUTPUT_FREQ_LIST | 101 | Frequency List mode—Generates a standard function using a list of frequencies you define. |
| NIFGEN_VAL_OUTPUT_ARB | 1 | Arbitrary Waveform mode—Generates waveforms from user-created/provided waveform arrays of numeric data. |
| NIFGEN_VAL_OUTPUT_SEQ | 2 | Arbitrary Sequence mode—Generates downloaded waveforms in an order your specify. |
| NIFGEN_VAL_OUTPUT_SCRIPT | 102 | Script mode—Allows you to use scripting to link and loop multiple waveforms in complex combinations. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2penabled.html language=enus -->
## TOPIC 00328: Arbitrary Waveform:Peer-to-Peer:P2P Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2penabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2penabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal generator reads data from the peer-to-peer endpoint (TRUE) instead of reading it from the onboard memory. This property is endpoint based. Default Value: FALSE Remarks The following table lists the characteristics of this property. Short Name P2P Enabled Data type cbool.

### Arbitrary Waveform:Peer-to-Peer:P2P Enabled

Specifies whether the signal generator reads data from the peer-to-peer endpoint (TRUE) instead of reading it from the onboard memory. This property is [endpoint based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2pendpointfullnessstarttriggerlevel.html language=enus -->
## TOPIC 00329: Triggers:Start:P2P Endpoint Fullness:Level

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2pendpointfullnessstarttriggerlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2pendpointfullnessstarttriggerlevel.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples the endpoint needs to receive before the signal generator starts generation. This property applies only when the Start Trigger Type property is set to P2P Endpoint Fullness. Refer to the Flow Control topic in the NI Signal Generators Help for more information about pe

### Triggers:Start:P2P Endpoint Fullness:Level

Specifies the number of samples the endpoint needs to receive before the signal generator starts generation. This property applies only when the [Start Trigger Type](/csh?topicname=pnifgen-starttriggertype.html) property is set to **P2P Endpoint Fullness**. Refer to the [Flow Control](/csh?context=nifgen_siggenhelp_p2p_flow_control) topic in the *NI Signal Generators Help* for more information about peer-to-peer operations. This property is coerced down to 8-byte boundaries.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Endpoint Fullness Start Trigger Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pcidmaoptimizationsenabled.html language=enus -->
## TOPIC 00330: Arbitrary Waveform:Data Transfer:Advanced:PCI DMA Optimizations Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pcidmaoptimizationsenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pcidmaoptimizationsenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls whether NI-FGEN allows performance optimizations for DMA transfers. This property is only valid for PCI and PXI SMC-based devices. This property is enabled (TRUE) by default, and NI recommends leaving it enabled. You cannot change this property while the device is generating a waveform. If

### Arbitrary Waveform:Data Transfer:Advanced:PCI DMA Optimizations Enabled

Controls whether NI-FGEN allows performance optimizations for DMA transfers. This property is only valid for PCI and PXI SMC-based devices. This property is enabled (TRUE) by default, and NI recommends leaving it enabled.

Note

niFgen Abort Generation

**Default Value**: TRUE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PCI DMA Optimizations Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-post-amplifierattenuation.html language=enus -->
## TOPIC 00331: Instrument:Calibration:Post-Amplifier Attenuation

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-post-amplifierattenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-post-amplifierattenuation.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of post-amplifier attenuation to apply to the signal, in dB. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The followi

### Instrument:Calibration:Post-Amplifier Attenuation

Specifies the amount of post-amplifier attenuation to apply to the signal, in dB.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Post-Amplifier Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-amplifierattenuation.html language=enus -->
## TOPIC 00332: Instrument:Calibration:Pre-Amplifier Attenuation

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-amplifierattenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-amplifierattenuation.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of preamplifier attenuation to apply to the signal, in dB. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The following

### Instrument:Calibration:Pre-Amplifier Attenuation

Specifies the amount of preamplifier attenuation to apply to the signal, in dB.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pre-Amplifier Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergaini.html language=enus -->
## TOPIC 00333: Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain I

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergaini.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergaini.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital gain to apply to the I data stream before any filtering by the OSP block. Valid Values: -2.0 to 2.0 Default Value: 1.0 Remarks The following table lists the characteristics of this property. Short Name Pre-filter Gain I Data type cdbl.png Permissions Read/Write High-level VIs N

### Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain I

Specifies the digital gain to apply to the I data stream before any filtering by the OSP block.

**Valid Values**: -2.0 to 2.0

**Default Value**: 1.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pre-filter Gain I |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergainq.html language=enus -->
## TOPIC 00334: Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain Q

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergainq.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergainq.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital gain to apply to the Q data stream before any filtering by the OSP block. This property is used only when the Data Processing Mode property is set to Complex. Valid Values: -2.0 to 2.0 Default Value: 1.0 Remarks The following table lists the characteristics of this property. Sh

### Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain Q

Specifies the digital gain to apply to the Q data stream before any filtering by the OSP block. This property is used only when the [Data Processing Mode](/csh?topicname=pnifgen-dataprocessingmode.html) property is set to **Complex**.

**Valid Values**: -2.0 to 2.0

**Default Value**: 1.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pre-filter Gain Q |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffseti.html language=enus -->
## TOPIC 00335: Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset I

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffseti.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffseti.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital offset to apply to the I data stream. This offset is applied after the prefilter gain and before any filtering. Valid Values: -1.0 to 1.0 Default Value: 0.9 Remarks The following table lists the characteristics of this property. Short Name Pre-filter Offset I Data type cdbl.png

### Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset I

Specifies the digital offset to apply to the I data stream. This offset is applied after the prefilter gain and before any filtering.

**Valid Values**: -1.0 to 1.0

**Default Value**: 0.9

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pre-filter Offset I |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffsetq.html language=enus -->
## TOPIC 00336: Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset Q

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffsetq.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffsetq.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital offset to apply to the Q data stream. This offset is applied after the prefilter gain and before any filtering. This property is only used when the Data Processing Mode property is set to Complex. Valid Values: -1.0 to 1.0 Default Value: 0.0 Remarks The following table lists th

### Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset Q

Specifies the digital offset to apply to the Q data stream. This offset is applied after the prefilter gain and before any filtering. This property is only used when the [Data Processing Mode](/csh?topicname=pnifgen-dataprocessingmode.html) property is set to **Complex**.

**Valid Values**: -1.0 to 1.0

**Default Value**: 0.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pre-filter Offset Q |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-preferredpacketsize.html language=enus -->
## TOPIC 00337: Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-preferredpacketsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-preferredpacketsize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementati

### Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size

Specifies the preferred size of the data field in a PCI Express read request packet.

In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.

Recommended values for this property are powers of two between 64 and 512.

Note

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Preferred Packet Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-primaryerror.html language=enus -->
## TOPIC 00338: Instrument:Obsolete:Primary Error

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-primaryerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-primaryerror.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Describes the first error that occurred since the last call to the niFgen Error Message VI on the session. The value follows the VXIplug&play completion code conventions. A negative value (0x80000000 or higher in hex) describes an error condition. A positive value describes a warning condition and i

### Instrument:Obsolete:Primary Error

Describes the first error that occurred since the last call to the [niFgen Error Message](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI on the session.

The value follows the VXIplug&play completion code conventions. A negative value (0x80000000 or higher in hex) describes an error condition. A positive value describes a warning condition and indicates that no error occurred. A zero indicates that no error or warning occurred. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Primary Error |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-quantum.html language=enus -->
## TOPIC 00339: Arbitrary Waveform:Capabilities:Waveform Quantum

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-quantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-quantum.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the quantum value the signal generator allows. The size of each arbitrary waveform must be a multiple of this quantum value. For example, when this property returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator. Remarks T

### Arbitrary Waveform:Capabilities:Waveform Quantum

Returns the quantum value the signal generator allows. The size of each arbitrary waveform must be a multiple of this quantum value.

For example, when this property returns a value of **8**, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waveform Quantum |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niFgen Query Arb Waveform Capabilities |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-queryinstrumentstatus.html language=enus -->
## TOPIC 00340: Instrument:Inherent IVI Attributes:User Options:Query Instrument Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-queryinstrumentstatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-FGEN retains instrument status after each operation. Set this property to TRUE to query the instrument status. Querying the instrument status is very useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize

### Instrument:Inherent IVI Attributes:User Options:Query Instrument Status

Specifies whether NI-FGEN retains instrument status after each operation. Set this property to TRUE to query the instrument status.

Querying the instrument status is very useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize performance. However, the effect on NI-FGEN is minor.

NI-FGEN can choose to ignore status checking for particular properties regardless of the setting of this property. Use the [niFgen Initialize With Options](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to override this value.

**Default Value**: TRUE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Query Instrument Status |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-raisedcosinefilteralpha.html language=enus -->
## TOPIC 00341: Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Raised Cosine:Alpha

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-raisedcosinefilteralpha.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-raisedcosinefilteralpha.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. This property is used only when the Filter Type property is set to Raised Cosine. Remarks The following table lists the characteristics of this property. Short Name Raised Cosine Filter Alpha Data type cdbl.

### Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Raised Cosine:Alpha

Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. This property is used only when the [Filter Type](/csh?topicname=pnifgen-filtertype.html) property is set to **Raised Cosine**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Raised Cosine Filter Alpha |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rangecheck.html language=enus -->
## TOPIC 00342: Instrument:Inherent IVI Attributes:User Options:Range Check

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rangecheck.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to validate property values and VI parameters. Set this property to TRUE to enable range-checking. If enabled, in some cases, NI-FGEN does extra validation of parameter values that you pass to NI-FGEN VIs. Range checking parameters is useful for debugging. After you validate your p

### Instrument:Inherent IVI Attributes:User Options:Range Check

Specifies whether to validate property values and VI parameters. Set this property to TRUE to enable range-checking.

If enabled, in some cases, NI-FGEN does extra validation of parameter values that you pass to NI-FGEN VIs. Range checking parameters is useful for debugging. After you validate your program, you can set this property to FALSE to disable range checking and maximize performance.

Use the [niFgen Initialize With Options](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to override the value of this property.

**Default Value**: TRUE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Range Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Initialize With Options |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventactivelevel.html language=enus -->
## TOPIC 00343: Events:Ready For Start:Level:Active Level

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventactivelevel.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output polarity of the Ready for Start Event. Remarks The following table lists the characteristics of this property. Short Name Ready For Start Event Active Level Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Active High 101 When the oper

### Events:Ready For Start:Level:Active Level

Specifies the output polarity of the Ready for Start Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Start Event Active Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Active High | 101 | When the operation is ready to start, the Ready for Start Event level is high. |
| --- | --- | --- |
| Active Low | 102 | When the operation is ready to start, the Ready for Start Event level is low. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventlivestatus.html language=enus -->
## TOPIC 00344: Events:Ready For Start:Advanced:Live Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventlivestatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventlivestatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns TRUE if the status of the specified Ready for Start Event is live, and FALSE otherwise. Remarks The following table lists the characteristics of this property. Short Name Ready For Start Event Live Status Data type cbool.png Permissions Read Only High-level VIs N/A Channel-based No Resettabl

### Events:Ready For Start:Advanced:Live Status

Returns TRUE if the status of the specified Ready for Start Event is live, and FALSE otherwise.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Start Event Live Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventoutputterminal.html language=enus -->
## TOPIC 00345: Events:Ready For Start:Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Start Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of this property. Short Name Ready For Start Event

### Events:Ready For Start:Output Terminal

Specifies the destination terminal for the Ready for Start Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Start Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-recordvaluecoercions.html language=enus -->
## TOPIC 00346: Instrument:Inherent IVI Attributes:User Options:Record Value Coercions

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-recordvaluecoercions.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 properties. Set this property to TRUE to record the coercions. Use the niFgen Initialize With Options VI to override this value. Default Value: FALSE Remarks The following table lists the character

### Instrument:Inherent IVI Attributes:User Options:Record Value Coercions

Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 properties. Set this property to TRUE to record the coercions. Use the [niFgen Initialize With Options](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to override this value.

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Record Value Coercions |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-refclocksource.html language=enus -->
## TOPIC 00347: Instrument:Obsolete:Ref Clock Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-refclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-refclocksource.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the Reference Clock source the signal generator uses. The signal generator derives the frequencies and sample rates that it uses to generate waveforms from the source you specify. For example, when you set this attribute to Clock In, the signal generator uses the signal it receives at the C

### Instrument:Obsolete:Ref Clock Source

Controls the Reference Clock source the signal generator uses.

The signal generator derives the frequencies and sample rates that it uses to generate waveforms from the source you specify. For example, when you set this attribute to **Clock In**, the signal generator uses the signal it receives at the Clk In front panel connector as its Reference Clock.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclockfrequency.html language=enus -->
## TOPIC 00348: Clocks:Reference Clock:Frequency

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclockfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclockfrequency.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Reference Clock frequency. The signal generator uses the Reference Clock to derive frequencies and sample rates when generating output. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Gener

### Clocks:Reference Clock:Frequency

Specifies the Reference Clock frequency. The signal generator uses the Reference Clock to derive frequencies and sample rates when generating output.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Clock Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Reference Clock |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclocksource.html language=enus -->
## TOPIC 00349: Clocks:Reference Clock:Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclocksource.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Reference Clock source used by the signal generator. The signal generator derives the frequencies and sample rates that it uses to generate waveforms from the source you specify. For example, when you set this property to Clock In, the signal generator uses the signal it receives at it

### Clocks:Reference Clock:Source

Specifies the Reference Clock source used by the signal generator.

The signal generator derives the frequencies and sample rates that it uses to generate waveforms from the source you specify. For example, when you set this property to **Clock In**, the signal generator uses the signal it receives at its CLK In front panel connector as its Reference Clock.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Reference Clock |
| Channel-based | No |
| Resettable | Yes |

| None | None | Specifies that a Reference Clock is not used. |
| --- | --- | --- |
| PXI Clock | PXI_Clk | Specifies the PXI Clock is used as the Reference Clock source. |
| Clock In | ClkIn | Specifies that the CLK IN input signal from the front panel connector is used as the Reference Clock source. |
| Onboard Reference Clock | OnboardRefClk | Specifies that the onboard Reference Clock is used as the Reference Clock source. |
| RTSI 7 | RTSI7 | Specifies that the RTSI line 7 is used as the Reference Clock source. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-resourcedescriptor.html language=enus -->
## TOPIC 00350: Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-resourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-resourcedescriptor.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the resource descriptor NI-FGEN uses to identify the physical device. If you initialize NI-FGEN with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility. If you initialize NI-FGEN with the resource descriptor, this pro

### Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

Returns the resource descriptor NI-FGEN uses to identify the physical device.

If you initialize NI-FGEN with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.

If you initialize NI-FGEN with the resource descriptor, this property contains that value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Resource Descriptor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-revision.html language=enus -->
## TOPIC 00351: Instrument:Inherent IVI Attributes:Driver Identification:Revision

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-revision.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains additional version information about NI-FGEN. Remarks The following table lists the characteristics of this property. Short Name Revision Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Driver Identification:Revision

Contains additional version information about NI-FGEN.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rootraisedcosinefilteralpha.html language=enus -->
## TOPIC 00352: Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Root Raised Cosine:Alpha

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rootraisedcosinefilteralpha.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rootraisedcosinefilteralpha.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. This property is used only when the Filter Type property is set to Root Raised Cosine. Remarks The following table lists the characteristics of this property. Short Name Root Raised Cosine Filter Alpha Data

### Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Root Raised Cosine:Alpha

Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. This property is used only when the [Filter Type](/csh?topicname=pnifgen-filtertype.html) property is set to **Root Raised Cosine**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Root Raised Cosine Filter Alpha |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclockabsolutedelay.html language=enus -->
## TOPIC 00353: Clocks:Advanced:Sample Clock Absolute Delay

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclockabsolutedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclockabsolutedelay.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay in seconds to apply to an external Sample Clock. This property is useful when trying to align the output of two devices. For the NI 5421, absolute delay can only be applied when an external Sample Clock is used. Remarks The following table lists the characteristics of this proper

### Clocks:Advanced:Sample Clock Absolute Delay

Specifies the delay in seconds to apply to an external Sample Clock. This property is useful when trying to align the output of two devices.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Absolute Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocksource.html language=enus -->
## TOPIC 00354: Clocks:Sample Clock:Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocksource.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Sample Clock source. The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The following table lists the characteristics of this pro

### Clocks:Sample Clock:Source

Specifies the Sample Clock source.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Sample Clock Source |
| Channel-based | No |
| Resettable | Yes |

| Onboard Clock | OnboardClock | Specifies that the onboard clock is used as the Sample Clock source. |
| --- | --- | --- |
| Clock In | ClkIn | Specifies that the signal at the CLK IN front panel connector is used as the Sample Clock source. |
| PXI STAR Line | PXI_Star | Specifies that the PXI_STAR trigger line is used as the Sample Clock source. |
| PXI Trigger Line 0/RTSI 0 | PXI_Trig0 | Specifies that the PXI or RTSI line 0 is used as the Sample Clock source. |
| PXI Trigger Line 1/RTSI 1 | PXI_Trig1 | Specifies that the PXI or RTSI line 1 is used as the Sample Clock source. |
| PXI Trigger Line 2/RTSI 2 | PXI_Trig2 | Specifies that the PXI or RTSI line 2 is used as the Sample Clock source. |
| PXI Trigger Line 3/RTSI 3 | PXI_Trig3 | Specifies that the PXI or RTSI line 3 is used as the Sample Clock source. |
| PXI Trigger Line 4/RTSI 4 | PXI_Trig4 | Specifies that the PXI or RTSI line 4 is used as the Sample Clock source. |
| PXI Trigger Line 5/RTSI 5 | PXI_Trig5 | Specifies that the PXI or RTSI line 5 is used as the Sample Clock source. |
| PXI Trigger Line 6/RTSI 6 | PXI_Trig6 | Specifies that the PXI or RTSI line 6 is used as the Sample Clock source. |
| PXI Trigger Line 7/RTSI 7 | PXI_Trig7 | Specifies that the PXI or RTSI line 7 is used as the Sample Clock source. |
| DDC Clock In | DDC_ClkIn | Specifies that the Sample Clock from DDC connector is used as the Sample Clock source. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebaserate.html language=enus -->
## TOPIC 00355: Clocks:Sample Clock Timebase:Rate

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebaserate.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Sample Clock Timebase rate. This property applies only to external Sample Clock timebases. The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to compl

### Clocks:Sample Clock Timebase:Rate

Specifies the Sample Clock Timebase rate. This property applies only to external Sample Clock timebases.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Timebase Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebasesource.html language=enus -->
## TOPIC 00356: Clocks:Sample Clock Timebase:Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebasesource.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Sample Clock Timebase source. The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The following table lists the characteristics of

### Clocks:Sample Clock Timebase:Source

Specifies the Sample Clock Timebase source.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Timebase Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Onboard Clock | OnboardClock | Specifies that the onboard Sample Clock timebase is used as the source. |
| --- | --- | --- |
| Clock In | ClkIn | Specifies that the external signal on the CLK IN front panel connector is used as the source. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-samplerate.html language=enus -->
## TOPIC 00357: Clocks:Sample Clock:Rate

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-samplerate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-samplerate.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms. Use this property when the Output Mode property is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ. You cannot change this property while the device is generating a waveform. I

### Clocks:Sample Clock:Rate

Specifies the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms.

Use this property when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_ARB** or **NIFGEN_VAL_OUTPUT_SEQ**.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Set Sample Rate |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttogenerate.html language=enus -->
## TOPIC 00358: Arbitrary Waveform:Script Mode:Script to Generate

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttogenerate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttogenerate.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which script the signal generator uses. To configure the signal generator to run a particular script, set this property to the name of the script. Use the niFgen Write Script VI to create multiple scripts. Use this property when the Output Mode property is set to NIFGEN_VAL_OUTPUT_SCRIPT.

### Arbitrary Waveform:Script Mode:Script to Generate

Specifies which script the signal generator uses. To configure the signal generator to run a particular script, set this property to the name of the script.

Use the [niFgen Write Script](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to create multiple scripts. Use this property when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_SCRIPT**.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Script to Generate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-edge.html language=enus -->
## TOPIC 00359: Triggers:Script:Digital Edge:Edge

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-edge.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Edge. Remarks The following table lists the characteristics of this property. Short Name Script Trigger Digital Edge - Edge Data type ci32.png Permissions Read/Write High-l

### Triggers:Script:Digital Edge:Edge

Specifies the active edge for the Script Trigger. This property is used when the [Script Trigger Type](/csh?topicname=pnifgen-scripttriggertype.html) property is set to **Digital Edge**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Script Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

| Rising Edge | 101 | Occurs when the signal transitions from low level to high level. |
| --- | --- | --- |
| Falling Edge | 102 | Occurs when the signal transitions from high level to low level. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-source.html language=enus -->
## TOPIC 00360: Triggers:Script:Digital Edge:Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-source.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Edge. Remarks The following table lists the characteristics of this property. Short Name Script Trigger Digital Edge - Source Data type cstr.png Permissions Read/Write

### Triggers:Script:Digital Edge:Source

Specifies the source terminal for the Script Trigger. This property is used when the [Script Trigger Type](/csh?topicname=pnifgen-scripttriggertype.html) property is set to **Digital Edge**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Script Trigger Digital Edge - Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-activelevel.html language=enus -->
## TOPIC 00361: Triggers:Script:Digital Level:Active Level

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-activelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-activelevel.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active level for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Level. Remarks The following table lists the characteristics of this property. Short Name Script Trigger Digital Level - Active Level Data type ci32.png Permissions Read/W

### Triggers:Script:Digital Level:Active Level

Specifies the active level for the Script Trigger. This property is used when the [Script Trigger Type](/csh?topicname=pnifgen-scripttriggertype.html) property is set to **Digital Level**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Script Trigger Digital Level - Active Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

| High Level | 101 | The high level is the active level. |
| --- | --- | --- |
| Low Level | 102 | The low level is the active level. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-source.html language=enus -->
## TOPIC 00362: Triggers:Script:Digital Level:Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-source.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Level. Remarks The following table lists the characteristics of this property. Short Name Script Trigger Digital Level - Source Data type cstr.png Permissions Read/Writ

### Triggers:Script:Digital Level:Source

Specifies the source terminal for the Script Trigger. This property is used when the [Script Trigger Type](/csh?topicname=pnifgen-scripttriggertype.html) property is set to **Digital Level**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Script Trigger Digital Level - Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerscount.html language=enus -->
## TOPIC 00363: Instrument:Script Triggers Count

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerscount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerscount.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of Script Triggers supported by the device. Use this property when the Output Mode property is set to NIFGEN_VAL_OUTPUT_SCRIPT. Remarks The following table lists the characteristics of this property. Short Name Script Triggers Count Data type ci32.png Permissions Read Only High-le

### Instrument:Script Triggers Count

Returns the number of Script Triggers supported by the device. Use this property when the [Output Mode](/csh?topicname=pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_SCRIPT**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Script Triggers Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggertype.html language=enus -->
## TOPIC 00364: Triggers:Script:Trigger Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggertype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Script trigger type. Depending upon the value of this property, additional properties may be needed to fully configure the trigger. Remarks The following table lists the characteristics of this property. Short Name Script Trigger Type Data type ci32.png Permissions Read/Write High-leve

### Triggers:Script:Trigger Type

Specifies the Script trigger type. Depending upon the value of this property, additional properties may be needed to fully configure the trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Script Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None | 101 | No trigger is configured. Signal generation starts immediately. |
| --- | --- | --- |
| Digital Edge | 102 | Trigger is asserted when a digital edge is detected. |
| Digital Level | 103 | Trigger is asserted when a digital level is detected. |
| Software Edge | 104 | Trigger is asserted when a software edge is detected. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-secondaryerror.html language=enus -->
## TOPIC 00365: Instrument:Obsolete:Secondary Error

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-secondaryerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-secondaryerror.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides an optional code with additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Zero indicates no additional information. Remarks The following table lists the characteristics of

### Instrument:Obsolete:Secondary Error

Provides an optional code with additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Zero indicates no additional information.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Secondary Error |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-serialnumber.html language=enus -->
## TOPIC 00366: Instrument:Serial Number

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-serialnumber.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the serial number of the signal generator. Remarks The following table lists the characteristics of this property. Short Name Serial Number Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Serial Number

Returns the serial number of the signal generator.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Serial Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-simulate.html language=enus -->
## TOPIC 00367: Instrument:Inherent IVI Attributes:User Options:Simulate

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-simulate.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether or not to simulate NI-FGEN I/O operations. Set this property to TRUE to enable simulation. If simulation is enabled, NI-FGEN VIs perform range checking and can get and set properties, but they do not perform instrument I/O. For output parameters that represent instrument data, NI-F

### Instrument:Inherent IVI Attributes:User Options:Simulate

Specifies whether or not to simulate NI-FGEN I/O operations. Set this property to TRUE to enable simulation.

If simulation is enabled, NI-FGEN VIs perform range checking and can get and set properties, but they do not perform instrument I/O. For output parameters that represent instrument data, NI-FGEN VIs return calculated values.

Use the [niFgen Initialize With Options](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to override the value of this property.

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Simulate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Initialize With Options |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailableinendpoint.html language=enus -->
## TOPIC 00368: Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailableinendpoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailableinendpoint.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current space available in the endpoint in samples per channel. You can use this property when priming the endpoint with initial data through the niFgen Write P2P Endpoint I16 VI to determine how many samples you can write. You also can use this property to characterize the performance a

### Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint

Returns the current space available in the endpoint in samples per channel. You can use this property when priming the endpoint with initial data through the [niFgen Write P2P Endpoint I16](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to determine how many samples you can write. You also can use this property to characterize the performance and measure the latency of the peer-to-peer stream as data moves across the bus. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Space Available In Endpoint |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailinstreamingwfm.html language=enus -->
## TOPIC 00369: Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailinstreamingwfm.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailinstreamingwfm.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the space available in the streaming waveform for writing new data. Use this property in conjunction with the Streaming Waveform Handle property or the Streaming Waveform Name property. Remarks The following table lists the characteristics of this property. Short Name Space Available in Stre

### Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform

Returns the space available in the streaming waveform for writing new data.

Use this property in conjunction with the [Streaming Waveform Handle](pnifgen-streamingwaveformhandle.html) property or the [Streaming Waveform Name](pnifgen-streamingwaveformname.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Space Available in Streaming Waveform |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventactivelevel.html language=enus -->
## TOPIC 00370: Events:Started:Level:Active Level

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventactivelevel.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output polarity of the Started Event. Remarks The following table lists the characteristics of this property. Short Name Started Event Active Level Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Active High 101 When the operation has starte

### Events:Started:Level:Active Level

Specifies the output polarity of the Started Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Active Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Active High | 101 | When the operation has started, the Started Event level is high. |
| --- | --- | --- |
| Active Low | 102 | When the operation has started, the Started Event level is high. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayunits.html language=enus -->
## TOPIC 00371: Events:Started:Advanced:Delay Units

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayunits.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units used for the Started Event Delay Value property. Remarks The following table lists the characteristics of this property. Short Name Started Event Delay Units Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Sample Clock Periods 101 The

### Events:Started:Advanced:Delay Units

Specifies the units used for the [Started Event Delay Value](/csh?topicname=pnifgen-startedeventdelayvalue.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Delay Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Sample Clock Periods | 101 | The delay is specified in Sample Clock periods and then coerced up by NI-FGEN to the nearest Sample Clock period. |
| --- | --- | --- |
| Seconds | 102 | The delay is specified in seconds and then coerced up by NI-FGEN to the nearest Sample Clock period. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayvalue.html language=enus -->
## TOPIC 00372: Events:Started:Advanced:Delay Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of delay applied to a Started Event with respect to the analog output of the signal generator. A positive delay value indicates that the Started Event occurs after the analog data, while a negative delay value indicates that the Started Event occurs before the analog data. The d

### Events:Started:Advanced:Delay Value

Specifies the amount of delay applied to a Started Event with respect to the analog output of the signal generator.

A positive delay value indicates that the Started Event occurs after the analog data, while a negative delay value indicates that the Started Event occurs before the analog data. The default value is zero, which aligns the Started Event with the analog output.

You can specify the units of the delay value by setting the [Started Event Delay Units](pnifgen-startedeventdelayunits.html) property.

**Default Value**: 0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Delay Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventlatchedstatus.html language=enus -->
## TOPIC 00373: Events:Started:Advanced:Latched Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventlatchedstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventlatchedstatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the latched status of the specified Started Event. Remarks The following table lists the characteristics of this property. Short Name Started Event Latched Status Data type cbool.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Events:Started:Advanced:Latched Status

Returns the latched status of the specified Started Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Latched Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputbehavior.html language=enus -->
## TOPIC 00374: Events:Started:Output Behavior

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputbehavior.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior for the Started Event. Remarks The following table lists the characteristics of this property. Short Name Started Event Output Behavior Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Pulse 101 Triggers a pulse for a specifie

### Events:Started:Output Behavior

Specifies the output behavior for the Started Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Output Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Pulse | 101 | Triggers a pulse for a specified period of time. |
| --- | --- | --- |
| Level | 102 | Shifts high or low while the event is active, depending on the active state you specify. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputterminal.html language=enus -->
## TOPIC 00375: Events:Started:Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Started Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of this property. Short Name Started Event Output Terminal

### Events:Started:Output Terminal

Specifies the destination terminal for the Started Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsepolarity.html language=enus -->
## TOPIC 00376: Events:Started:Pulse:Polarity

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsepolarity.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output polarity of the Started Event. Remarks The following table lists the characteristics of this property. Short Name Started Event Pulse Polarity Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Active High 101 When the operation has star

### Events:Started:Pulse:Polarity

Specifies the output polarity of the Started Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Active High | 101 | When the operation has started, the Started Event level is high. |
| --- | --- | --- |
| Active Low | 102 | When the operation has started, the Started Event level is low. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthunits.html language=enus -->
## TOPIC 00377: Events:Started:Pulse:Width Units

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthunits.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse width units for the Started Event. Remarks The following table lists the characteristics of this property. Short Name Started Event Pulse Width Units Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Sample Clock Periods 101 Specifies th

### Events:Started:Pulse:Width Units

Specifies the pulse width units for the Started Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Pulse Width Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Sample Clock Periods | 101 | Specifies the pulse width in Sample Clock periods. |
| --- | --- | --- |
| Seconds | 102 | Specifies the pulse width in seconds. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthvalue.html language=enus -->
## TOPIC 00378: Events:Started:Pulse:Width Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse width value for the Started Event. Remarks The following table lists the characteristics of this property. Short Name Started Event Pulse Width Value Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Events:Started:Pulse:Width Value

Specifies the pulse width value for the Started Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Started Event Pulse Width Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startphase.html language=enus -->
## TOPIC 00379: Standard Function:Start Phase

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startphase.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startphase.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls horizontal offset of the standard waveform the signal generator produces. Specify this property in degrees of one waveform cycle. A start phase of 180 degrees means output generation begins halfway through the waveform. A start phase of 360 degrees offsets the output by an entire waveform c

### Standard Function:Start Phase

Controls horizontal offset of the standard waveform the signal generator produces. Specify this property in degrees of one waveform cycle.

A start phase of 180 degrees means output generation begins halfway through the waveform. A start phase of 360 degrees offsets the output by an entire waveform cycle, which is identical to a start phase of 0 degrees.

**Units**: Degrees of one cycle

**Default Value**: None

Note

Waveform

NIFGEN_VAL_WFM_DC

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Phase |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Frequency List, niFgen Configure Standard Waveform |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-edge.html language=enus -->
## TOPIC 00380: Triggers:Start:Digital Edge:Edge

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-edge.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the Start Trigger. This property is used only when the Start Trigger Type property is set to Digital Edge. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Digital Edge - Edge Data type ci32.png Permissions Read/Write High

### Triggers:Start:Digital Edge:Edge

Specifies the active edge for the Start Trigger. This property is used only when the [Start Trigger Type](/csh?topicname=pnifgen-starttriggertype.html) property is set to **Digital Edge**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

| Rising Edge | 101 | Occurs when the signal transitions from low level to high level. |
| --- | --- | --- |
| Falling Edge | 102 | Occurs when the signal transitions from high level to low level. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-source.html language=enus -->
## TOPIC 00381: Triggers:Start:Digital Edge:Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-source.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the Start Trigger. This property is used only when the Start Trigger Type property is set to Digital Edge. You can specify any valid source terminal for this property. Valid sources can be found in the Routes topic for your device or in Measurement & Automation Expl

### Triggers:Start:Digital Edge:Source

Specifies the source terminal for the Start Trigger. This property is used only when the [Start Trigger Type](/csh?topicname=pnifgen-starttriggertype.html) property is set to **Digital Edge**.

You can specify any valid source terminal for this property. Valid sources can be found in the Routes topic for your device or in Measurement & Automation Explorer under the **Device Routes** tab.

Source terminals can be specified in two ways. If your device is named Dev1 and your terminal is PFI0, then the terminal can be specified as a fully qualified terminal name, "/Dev1/PFI0". You can also specify the terminal using PFI 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge - Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggertype.html language=enus -->
## TOPIC 00382: Triggers:Start:Trigger Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggertype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of Start Trigger you want to use. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Type Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes None 101 No trigger is configured. Signal generation

### Triggers:Start:Trigger Type

Specifies the type of Start Trigger you want to use.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None | 101 | No trigger is configured. Signal generation starts immediately. |
| --- | --- | --- |
| Digital Edge | 102 | Operation begins when a digital edge is detected. |
| Software Edge | 104 | Operation begins when a software edge is detected. |
| P2P Endpoint Fullness | 106 | Operation begins when the FIFO reaches the threshold specified in the P2P Endpoint Fullness Start Trigger Level property. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformhandle.html language=enus -->
## TOPIC 00383: Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformhandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformhandle.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the waveform handle of the waveform used to continuously stream data during generation. This property is used in conjunction with the Space Available in Streaming Waveform property. You cannot change this property while the device is generating a waveform. If you want to change the device

### Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle

Specifies the waveform handle of the waveform used to continuously stream data during generation.

This property is used in conjunction with the [Space Available in Streaming Waveform](pnifgen-spaceavailinstreamingwfm.html) property.

Note

niFgen Abort Generation

**Default Value**: -1

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Streaming Waveform Handle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformname.html language=enus -->
## TOPIC 00384: Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformname.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformname.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the waveform used to continuously stream data during generation. This property defaults to an empty string when no streaming waveform is specified. Use this property in conjunction with the Space Available in Streaming Waveform property. You cannot change this property while th

### Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name

Specifies the name of the waveform used to continuously stream data during generation. This property defaults to an empty string when no streaming waveform is specified.

Use this property in conjunction with the [Space Available in Streaming Waveform](pnifgen-spaceavailinstreamingwfm.html) property.

Note

niFgen Abort Generation

**Default Value**: ""

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Streaming Waveform Name |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwritetimeout.html language=enus -->
## TOPIC 00385: Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwritetimeout.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwritetimeout.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum amount of time allowed to complete a streaming write operation. Units: seconds (s) Remarks The following table lists the characteristics of this property. Short Name Streaming Write Timeout Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable

### Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout

Specifies the maximum amount of time allowed to complete a streaming write operation.

**Units**: seconds (s)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Streaming Write Timeout |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-supportedinstrumentmodels.html language=enus -->
## TOPIC 00386: Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-supportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-supportedinstrumentmodels.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a model code of the instrument. For drivers that support more than one device, this property contains a comma-separated list of supported instrument models. Remarks The following table lists the characteristics of this property. Short Name Supported Instrument Models Data type cstr.png Permi

### Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

Returns a model code of the instrument. For drivers that support more than one device, this property contains a comma-separated list of supported instrument models.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Supported Instrument Models |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncdutycyclehigh.html language=enus -->
## TOPIC 00387: Standard Function:Sync Duty Cycle High

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncdutycyclehigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncdutycyclehigh.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duty cycle of the square wave the signal generator produces on the SYNC OUT connector. Specify this property as a percentage of the time the square wave is high in each cycle. Units: Percentage of time the waveform is high Default Value: 50% Remarks The following table lists the charac

### Standard Function:Sync Duty Cycle High

Specifies the duty cycle of the square wave the signal generator produces on the SYNC OUT connector. Specify this property as a percentage of the time the square wave is high in each cycle.

**Units**: Percentage of time the waveform is high

**Default Value**: 50%

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Duty Cycle High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-synchronizationsource.html language=enus -->
## TOPIC 00388: Instrument:5401/5411/5431:Synchronization Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-synchronizationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-synchronizationsource.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the synchronization signal to use. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The following table lists the char

### Instrument:5401/5411/5431:Synchronization Source

Specifies the source of the synchronization signal to use.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Synchronization Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

| NIFGEN_VAL_NONE | 1000 | No synchronization source is used. |
| --- | --- | --- |
| NIFGEN_VAL_RTSI_0 | 141 | RTSI line 0 |
| NIFGEN_VAL_RTSI_1 | 142 | RTSI line 1 |
| NIFGEN_VAL_RTSI_2 | 143 | RTSI line 2 |
| NIFGEN_VAL_RTSI_3 | 144 | RTSI line 3 |
| NIFGEN_VAL_RTSI_4 | 145 | RTSI line 4 |
| NIFGEN_VAL_RTSI_5 | 146 | RTSI line 5 |
| NIFGEN_VAL_RTSI_6 | 147 | RTSI line 6 |
| NIFGEN_VAL_TTL0 | 111 | PXI TRIG0 or VXI TTL0 |
| NIFGEN_VAL_TTL1 | 112 | PXI TRIG1 or VXI TTL1 |
| NIFGEN_VAL_TTL2 | 113 | PXI TRIG2 or VXI TTL2 |
| NIFGEN_VAL_TTL3 | 114 | PXI TRIG3 or VXI TTL3 |
| NIFGEN_VAL_TTL4 | 115 | PXI TRIG4 or VXI TTL4 |
| NIFGEN_VAL_TTL5 | 116 | PXI TRIG5 or VXI TTL5 |
| NIFGEN_VAL_TTL6 | 117 | PXI TRIG6 or VXI TTL6 |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncoutoutputterminal.html language=enus -->
## TOPIC 00389: Standard Function:Sync Out Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncoutoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncoutoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal at which to export the SYNC OUT signal. This property is not supported for all devices. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of thi

### Standard Function:Sync Out Output Terminal

Specifies the terminal at which to export the SYNC OUT signal. This property is not supported for all devices. For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Out Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-terminalconfiguration.html language=enus -->
## TOPIC 00390: Output:Terminal Configuration

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-terminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-terminalconfiguration.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to analyze gain and offset values based on single-ended or differential operation. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete.

### Output:Terminal Configuration

Specifies whether to analyze gain and offset values based on single-ended or [differential](/csh?context=nifgen_siggenhelp_fund_differential_output) operation.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Terminal Configuration |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Single Ended | 300 | Specifies single-ended operation. |
| --- | --- | --- |
| Differential | 301 | Specifies differential operation. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggermode.html language=enus -->
## TOPIC 00391: Triggers:Trigger Mode

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggermode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggermode.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the trigger mode. Default Value: NIFGEN_VAL_CONTINUOUS Remarks The following table lists the characteristics of this property. Short Name Trigger Mode Data type ci32.png Permissions Read/Write High-level VIs niFgen Configure Trigger Mode Channel-based Yes Resettable No NIFGEN_VAL_SINGLE 1 S

### Triggers:Trigger Mode

Controls the trigger mode.

**Default Value**: **NIFGEN_VAL_CONTINUOUS**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger Mode |
| Channel-based | Yes |
| Resettable | No |

| NIFGEN_VAL_SINGLE | 1 | Specifies that the signal generator operates in Single Trigger mode. |
| --- | --- | --- |
| NIFGEN_VAL_CONTINUOUS | 2 | Specifies that the signal generator operates in Continuous Trigger mode. |
| NIFGEN_VAL_STEPPED | 3 | Specifies that the signal generator operates in Stepped Trigger mode. |
| NIFGEN_VAL_BURST | 4 | Specifies that the signal generator operates in Burst Trigger mode. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggersource.html language=enus -->
## TOPIC 00392: Instrument:5401/5411/5431:Trigger Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggersource.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which trigger source the signal generator uses. After you call the niFgen Initiate Generation VI, the signal generator waits for the trigger you specify in this parameter. After it receives a trigger, the signal generator produces the number of cycles you specify in the Repeat Count proper

### Instrument:5401/5411/5431:Trigger Source

Specifies which trigger source the signal generator uses.

After you call the [niFgen Initiate Generation](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI, the signal generator waits for the trigger you specify in this parameter. After it receives a trigger, the signal generator produces the number of cycles you specify in the [Repeat Count](pnifgen-arbwfm-repeatcount.html) property.

The value you select for this property is also the source for the trigger in the other trigger modes as specified by the [Trigger Mode](pnifgen-triggermode.html) property.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | Yes |
| Resettable | Yes |

| NIFGEN_VAL_IMMEDIATE | 0 | The signal generator does not wait for a trigger of any kind. |
| --- | --- | --- |
| NIFGEN_VAL_EXTERNAL | 1 | The signal generator waits for a trigger on the external trigger input. |
| NIFGEN_VAL_PFI_0 | 1011 | Specifies that PFI 0 is used as the trigger source. |
| NIFGEN_VAL_PFI_1 | 1012 | Specifies that PFI 1 is used as the trigger source. |
| NIFGEN_VAL_PFI_2 | 1013 | Specifies that PFI 2 is used as the trigger source. |
| NIFGEN_VAL_PFI_3 | 1014 | Specifies that PFI 3 is used as the trigger source. |
| NIFGEN_VAL_SOFTWARE_TRIG | 2 | Specifies that the signal generator waits until you call the niFgen Send Software Trigger VI. |
| NIFGEN_VAL_RTSI_0 | 141 | Specifies that RTSI line 0 is used as the trigger source. |
| NIFGEN_VAL_RTSI_1 | 142 | Specifies that RTSI line 1 is used as the trigger source. |
| NIFGEN_VAL_RTSI_2 | 143 | Specifies that RTSI line 2 is used as the trigger source. |
| NIFGEN_VAL_RTSI_3 | 144 | Specifies that RTSI line 3 is used as the trigger source. |
| NIFGEN_VAL_RTSI_4 | 145 | Specifies that RTSI line 4 is used as the trigger source. |
| NIFGEN_VAL_RTSI_5 | 146 | Specifies that RTSI line 5 is used as the trigger source. |
| NIFGEN_VAL_RTSI_6 | 147 | Specifies that RTSI line 6 is used as the trigger source. |
| NIFGEN_VAL_RTSI_7 | 1010 | Specifies that RTSI line 7 is used as the trigger source. |
| NIFGEN_VAL_PXI_STAR | 131 | Specifies that the PXI star trigger line is used as the trigger source. |
| NIFGEN_VAL_TTL0 | 111 | Specifies that the PXI_TRIG0 or VXI_TTL0 line is used as the trigger source. |
| NIFGEN_VAL_TTL1 | 112 | Specifies that the PXI_TRIG1 or VXI_TTL1 line is used as the trigger source. |
| NIFGEN_VAL_TTL2 | 113 | Specifies that the PXI_TRIG2 or VXI_TTL2 line is used as the trigger source. |
| NIFGEN_VAL_TTL3 | 114 | Specifies that the PXI_TRIG3 or VXI_TTL3 line is used as the trigger source. |
| NIFGEN_VAL_TTL4 | 115 | Specifies that the PXI_TRIG4 or VXI_TTL4 line is used as the trigger source. |
| NIFGEN_VAL_TTL5 | 116 | Specifies that the PXI_TRIG5 or VXI_TTL5 line is used as the trigger source. |
| NIFGEN_VAL_TTL6 | 117 | Specifies that the PXI_TRIG6 or VXI_TTL6 line is used as the trigger source. |
| NIFGEN_VAL_OTHER_TERMINAL | 1018 | Specifies that another terminal is used. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-updateclocksource.html language=enus -->
## TOPIC 00393: Instrument:Obsolete:Update Clock Source

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-updateclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-updateclocksource.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the Update Clock source. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Remarks The following table lists the characteristics of this prope

### Instrument:Obsolete:Update Clock Source

Controls the Update Clock source.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Update Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| NIFGEN_VAL_INTERNAL | 0 | Internal update clock |
| --- | --- | --- |
| NIFGEN_VAL_EXTERNAL | 1 | External update clock given on the IO connector |
| NIFGEN_VAL_CLK_IN | 1202 | Coaxial CLK IN connector on the board front panel |
| NIFGEN_VAL_DDC_CLK_IN | 1203 | DDC CLK IN line of the Digital Data & Control connector |
| NIFGEN_VAL_PXI_STAR | 131 | (PXI only) PXI star trigger line. This choice is valid only in PXI chassis slots 3 through 15. |
| NIFGEN_VAL_RTSI_0 | 141 | RTSI line 0 |
| NIFGEN_VAL_RTSI_1 | 142 | RTSI line 1 |
| NIFGEN_VAL_RTSI_2 | 143 | RTSI line 2 |
| NIFGEN_VAL_RTSI_3 | 144 | RTSI line 3 |
| NIFGEN_VAL_RTSI_4 | 145 | RTSI line 4 |
| NIFGEN_VAL_RTSI_5 | 146 | RTSI line 5 |
| NIFGEN_VAL_RTSI_6 | 147 | RTSI line 6 |
| NIFGEN_VAL_RTSI_7 | 1010 | (PCI only) RTSI line 7 |
| NIFGEN_VAL_OTHER_TERMINAL | 1018 | Uses another device terminal. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-videowaveformtype.html language=enus -->
## TOPIC 00394: Instrument:5401/5411/5431:Video Waveform Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-videowaveformtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-videowaveformtype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the waveform type the NI 5431 generates. Setting this property ensures the oscillator crystal is set to the proper frequency. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wa

### Instrument:5401/5411/5431:Video Waveform Type

Specifies the waveform type the NI 5431 generates. Setting this property ensures the oscillator crystal is set to the proper frequency.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Video Waveform Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

| NIFGEN_VAL_PAL_B | 0 | PAL B Video Type |
| --- | --- | --- |
| NIFGEN_VAL_PAL_D | 1 | PAL D Video Type |
| NIFGEN_VAL_PAL_G | 2 | PAL G Video Type |
| NIFGEN_VAL_PAL_H | 3 | PAL H Video Type |
| NIFGEN_VAL_PAL_I | 4 | PAL I Video Type |
| NIFGEN_VAL_PAL_M | 5 | PAL M Video Type |
| NIFGEN_VAL_PAL_N | 6 | PAL N Video Type |
| NIFGEN_VAL_NTSC_M | 7 | NTSC M Video Type |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitbehavior.html language=enus -->
## TOPIC 00395: Output:Advanced:Wait Behavior

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitbehavior.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the output while waiting for a Script Trigger or during a wait instruction. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete.

### Output:Advanced:Wait Behavior

Specifies the behavior of the output while waiting for a Script Trigger or during a wait instruction.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Wait Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Hold Last Value | 400 | While in a wait state, the output signal remains at the last voltage generated prior to entering the wait state. |
| --- | --- | --- |
| Jump To Value | 401 | While in a wait state, the output signal remains at the value configured in the Wait Value property. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitvalue.html language=enus -->
## TOPIC 00396: Output:Advanced:Wait Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value to generate while waiting. You must set the Wait Behavior property to Jump To Value to use this property. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the

### Output:Advanced:Wait Value

Specifies the value to generate while waiting. You must set the [Wait Behavior](/csh?topicname=pnifgen-waitbehavior.html) property to **Jump To Value** to use this property.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Wait Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waveform.html language=enus -->
## TOPIC 00397: Standard Function:Waveform

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waveform.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which standard waveform the signal generator produces. Use this property only when the Output Mode property is set to NIFGEN_VAL_OUTPUT_FUNC. Default Value: NIFGEN_VAL_WFM_DC Remarks The following table lists the characteristics of this property. Short Name Waveform Data type ci32.png Perm

### Standard Function:Waveform

Specifies which standard waveform the signal generator produces. Use this property only when the [Output Mode](/csh?topicname=pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_FUNC**.

**Default Value**: **NIFGEN_VAL_WFM_DC**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waveform |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Standard Waveform |
| Channel-based | Yes |
| Resettable | No |

| Sine | 1 | Specifies that the signal generator produces a sinusoid waveform. |
| --- | --- | --- |
| Square | 2 | Specifies that the signal generator produces a square waveform. |
| Triangle | 3 | Specifies that the signal generator produces a triangle waveform. |
| Ramp Up | 4 | Specifies that the signal generator produces a positive ramp waveform. |
| Ramp Down | 5 | Specifies that the signal generator produces a negative ramp waveform. |
| DC | 6 | Specifies that the signal generator produces a constant voltage. |
| Noise | 101 | Specifies that the signal generator produces white noise. |
| User | 102 | Specifies that the signal generator produces a user-defined waveform, defined by the niFgen Define User Standard Waveform VI. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-script-mnu.html language=enus -->
## TOPIC 00398: Script

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-script-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-script-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Script VIs to create, configure, and clear scripts. icon

### Script

Use the NI-FGEN Script VIs to create, configure, and clear scripts.

[IMAGE alt='icon' src='nifgen-script-mnu.png']

- [niFgen Allocate Named Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-allocate-named-waveform-vi.html) Specifies the initial size of a named waveform so that it can be allocated in onboard memory before loading the associated data. Data can then be loaded in smaller blocks with the niFgen Write Waveform (poly) VI.
- [niFgen Set Named Waveform Next Write Position VI](../../instr-lib/nifgen/nifgen-llb/nifgen-set-named-waveform-next-write-position-vi.html) Sets the position in the named waveform to which data is written at the next write. This VI allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the Waveform Name parameter. Subsequent writes to that waveform begin where the last write ended, unless this VI is called again. The Waveform Name passed in must have been created by a call to the niFgen Allocate Waveform VI or the niFgen Clear Arbitrary Waveform VI.
- [niFgen Write Named Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-vi.html) By default, the subsequent call to the niFgen Write Named Waveform (poly) VI continues writing data from the position of the last sample written. The write position and offset can be set using the niFgen Set Named Waveform Next Write Position VI. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Delete Named Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-delete-named-waveform-vi.html) Deletes the specified named waveform from onboard memory.
- [niFgen Write Script VI](../../instr-lib/nifgen/nifgen-llb/nifgen-write-script-vi.html) Writes a string containing one or more scripts that govern the generation of waveforms.
- [niFgen Delete Script VI](../../instr-lib/nifgen/nifgen-llb/nifgen-delete-script-vi.html) Deletes the specified script from onboard memory.

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-standard-waveform-mnu.html language=enus -->
## TOPIC 00399: Standard Waveform

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-standard-waveform-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-standard-waveform-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Standard Waveform VIs to configure, define, and clear a standard waveform. icon

### Standard Waveform

Use the NI-FGEN Standard Waveform VIs to configure, define, and clear a standard waveform.

[IMAGE alt='icon' src='nifgen-standard-waveform-mnu.png']

- [niFgen Configure Standard Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-standard-waveform-vi.html) Configures the properties of the signal generator that affect standard waveform generation. These settings are the waveform, amplitude, DC offset, frequency, and start phase.
- [niFgen Define User Standard Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-define-user-standard-waveform-vi.html) Defines a user waveform for either Standard Function or Frequency List output mode.
- [niFgen Clear User Standard Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-clear-user-standard-waveform-vi.html) Clears the user-defined waveform created by the niFgen Define User Standard Waveform VI.

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-utility-mnu.html language=enus -->
## TOPIC 00400: Utility

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-utility-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Utility VIs to control common instrument operations. These operations include many that VXIplug&play require, such as reset, self-test, revision query, and error message. This palette also contains VIs that create waveform data. icon

### Utility

Use the NI-FGEN Utility VIs to control common instrument operations. These operations include many that VXIplug&play require, such as reset, self-test, revision query, and error message. This palette also contains VIs that create waveform data.

[IMAGE alt='icon' src='nifgen-utility-mnu.png']

- [niFgen Reset VI](../../instr-lib/nifgen/nifgen-llb/nifgen-reset-vi.html) Resets the instrument to a known state. This VI aborts the generation, clears all routes, and resets session properties to the default values. This VI does not, however, commit the session properties or configure the device hardware to its default state.
- [niFgen Reset Device VI](../../instr-lib/nifgen/nifgen-llb/nifgen-reset-device-vi.html) Performs a hard reset on the device. Generation is stopped, all routes are released, external bidirectional terminals are tri-stated, FPGAs are reset, hardware is configured to its default state, and all session properties are reset to their default states.
- [niFgen Disable VI](../../instr-lib/nifgen/nifgen-llb/nifgen-disable-vi.html) Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected. The analog output and all exported signals are disabled.
- [niFgen Revision Query VI](../../instr-lib/nifgen/nifgen-llb/nifgen-revision-query-vi.html) Returns the revision numbers of NI-FGEN and the instrument firmware.
- [niFgen Get Session Reference VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-session-reference-vi.html) Extracts a session that can be passed to NI-TClk VIs. Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions.
- [niFgen Util Create Waveform Data VI](../../instr-lib/nifgen/nifgen-llb/nifgen-util-create-waveform-data-vi.html) Creates an array of doubles filled with the specified waveform.
- [niFgen Util Create Frequency Sweep Data VI](../../instr-lib/nifgen/nifgen-llb/nifgen-util-create-frequency-sweep-data-vi.html) Creates an array of doubles filled with the frequencies specified. The frequencies are created in a logarithmic progression from Start Frequency to Stop Frequency .
- [niFgen Util Create Bin16 Waveform Data VI](../../instr-lib/nifgen/nifgen-llb/nifgen-util-create-bin16-waveform-data-vi.html) Creates an array of 16-bit integers (I16) corresponding to the selected waveform. The number 1.0 is scaled to full range of 32,767.
- [niFgen Error Message VI](../../instr-lib/nifgen/nifgen-llb/nifgen-error-message-vi.html) Converts a status code returned by an NI-FGEN VI into a user-readable string.
- [niFgen Self-Test VI](../../instr-lib/nifgen/nifgen-llb/nifgen-self-test-vi.html) Runs the instrument self-test routine and returns the test results.
- [MeasurementLink](../../instr-lib/nifgen/nifgen-measurementlink-mnu.html) Use the VIs on this palette in conjunction with MeasurementLink Session Management.

Parent topic:

NI-FGEN
