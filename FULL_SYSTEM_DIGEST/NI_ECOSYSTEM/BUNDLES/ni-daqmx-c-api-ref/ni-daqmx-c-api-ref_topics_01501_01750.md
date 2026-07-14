# NI DOCUMENT BUNDLE: ni-daqmx-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-c-api-ref start=1501 end=1750 -->
<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__input__configuration_1gabc76db67700d39060edc34ab85d57eb2.html language=enus -->
## TOPIC 01501: DAQmx_AI_Coupling

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__input__configuration_1gabc76db67700d39060edc34ab85d57eb2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__input__configuration_1gabc76db67700d39060edc34ab85d57eb2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_CouplingRemarksData TypeDescriptionRestrictionsint32Specifies the coupling for the channel.Valid valuesDAQmx_Val_AC10045Remove the DC offset from the signal.DAQmx_Val_DC10050Allow NI-DAQmx to measure all of the signal.DAQmx_Val_GND10066Remove the signal from the measurement and measur

### DAQmx_AI_Coupling

#### Syntax

DAQmx_AI_Coupling

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the coupling for the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_AC | 10045 | Remove the DC offset from the signal. |
| DAQmx_Val_DC | 10050 | Allow NI-DAQmx to measure all of the signal. |
| DAQmx_Val_GND | 10066 | Remove the signal from the measurement and measure only ground. |

You can get/set/reset this property using:

- [DAQmxGetAICoupling](group__ni-daqmx__c__functions__property__manipulation__getter_1gadd919305da52215f61a44089cecbe46c.html)
- [DAQmxSetAICoupling](group__ni-daqmx__c__functions__property__manipulation__setter_1ga09a94b1b31d76695e28d7d7c6c96027d.html)
- [DAQmxResetAICoupling](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaffc9bca7fde766422f5ffd506929f9d0.html)

Parent topic:

Input Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__input__configuration_1gae623c3dae1a7b8fdd2cd49b35eb8c505.html language=enus -->
## TOPIC 01502: DAQmx_AI_InputSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__input__configuration_1gae623c3dae1a7b8fdd2cd49b35eb8c505.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__input__configuration_1gae623c3dae1a7b8fdd2cd49b35eb8c505.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_InputSrcRemarksData TypeDescriptionRestrictionschar*Specifies the source of the channel. You can use the signal from the I/O connector or one of several calibration signals. Certain devices have a single calibration signal bus. For these devices, you must specify the same calibration

### DAQmx_AI_InputSrc

#### Syntax

DAQmx_AI_InputSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the source of the channel. You can use the signal from the I/O connector or one of several calibration signals. Certain devices have a single calibration signal bus. For these devices, you must specify the same calibration signal for all channels you connect to a calibration signal. |  |

You can get/set/reset this property using:

- [DAQmxGetAIInputSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4e46b1133e423bbeafbbb17bbbee6c61.html)
- [DAQmxSetAIInputSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1gad49fee9d6a9c2a1c9203676204425252.html)
- [DAQmxResetAIInputSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1gacaa4a9edfa6cb31220a5a4f695c41d30.html)

Parent topic:

Input Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning.html language=enus -->
## TOPIC 01503: Signal Conditioning

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsBridgeCurrent Shunt ResistorExcitationSensor PowerThermocoupleGroup membersNameDescriptionDAQmx_AI_LeadWireResistanceDAQmx_AI_ResistanceCfgAttachmentsNone

### Signal Conditioning

#### Groups

- Bridge
- Current Shunt Resistor
- Excitation
- Sensor Power
- Thermocouple

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_LeadWireResistance |  |
| DAQmx_AI_ResistanceCfg |  |

#### Attachments

None

Parent topic:

General Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning_1ga1ac2f761046b417588200a1a6747f2ed.html language=enus -->
## TOPIC 01504: DAQmx_AI_LeadWireResistance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning_1ga1ac2f761046b417588200a1a6747f2ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning_1ga1ac2f761046b417588200a1a6747f2ed.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_LeadWireResistanceRemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the resistance of the wires that lead to the sensor.You can get/set/reset this property using:DAQmxGetAILeadWireResistanceDAQmxSetAILeadWireResistanceDAQmxResetAILeadWireResistance

### DAQmx_AI_LeadWireResistance

#### Syntax

DAQmx_AI_LeadWireResistance

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the resistance of the wires that lead to the sensor. |  |

You can get/set/reset this property using:

- [DAQmxGetAILeadWireResistance](group__ni-daqmx__c__functions__property__manipulation__getter_1ga24e3ccc576b6391725a3a37c7b504914.html)
- [DAQmxSetAILeadWireResistance](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa577e15e6a839ff45babb3a29d89913f.html)
- [DAQmxResetAILeadWireResistance](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaff4341856efd6560a317919c3ad67996.html)

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning_1gaa1837f43d29e5d2158736509a340f44b.html language=enus -->
## TOPIC 01505: DAQmx_AI_ResistanceCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning_1gaa1837f43d29e5d2158736509a340f44b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning_1gaa1837f43d29e5d2158736509a340f44b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_ResistanceCfgRemarksData TypeDescriptionRestrictionsint32Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD.Valid valuesDAQmx_Val_2Wire22-wire mode.DAQmx_Va

### DAQmx_AI_ResistanceCfg

#### Syntax

DAQmx_AI_ResistanceCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_2Wire | 2 | 2-wire mode. |
| DAQmx_Val_3Wire | 3 | 3-wire mode. |
| DAQmx_Val_4Wire | 4 | 4-wire mode. |

You can get/set/reset this property using:

- [DAQmxGetAIResistanceCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7da860daffc2323c739f84a42758c965.html)
- [DAQmxSetAIResistanceCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga641b5b505503f7ff20159682a2c7e139.html)
- [DAQmxResetAIResistanceCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8b44cfc4d49645fa131ffc9bfa22062a.html)

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gad6789bd9db7f69465d2247d7f45cbf23.html language=enus -->
## TOPIC 01506: DAQmx_AI_Bridge_InitialVoltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gad6789bd9db7f69465d2247d7f45cbf23.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gad6789bd9db7f69465d2247d7f45cbf23.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_InitialVoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies in volts the output voltage of the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set Initial Bridge Ratio, NI-DAQmx coerces this pr

### DAQmx_AI_Bridge_InitialVoltage

#### Syntax

DAQmx_AI_Bridge_InitialVoltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in volts the output voltage of the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set Initial Bridge Ratio, NI-DAQmx coerces this property to Initial Bridge Ratio times Actual Excitation Value. This property is set by DAQmx Perform Bridge Offset Nulling Calibration. If you set this property, NI-DAQmx coerces Initial Bridge Ratio to the value of this property divided by Actual Excitation Value. If you set both this property and Initial Bridge Ratio, and their values conflict, NI-DAQmx returns an error. To avoid this error, reset one property to its default value before setting the other. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeInitialVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga122d5714232c3cce4cd4be3ecbeb6d5a.html)
- [DAQmxSetAIBridgeInitialVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1gab162b0d016c2dac246d481d3a517fd94.html)
- [DAQmxResetAIBridgeInitialVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab8360ac195a2738a2111b84d04c96745.html)

Parent topic:

Bridge

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gad7c0deba8f7662b67907fcba386af3ab.html language=enus -->
## TOPIC 01507: DAQmx_AI_Bridge_Cfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gad7c0deba8f7662b67907fcba386af3ab.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gad7c0deba8f7662b67907fcba386af3ab.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_CfgRemarksData TypeDescriptionRestrictionsint32Specifies the type of Wheatstone bridge connected to the channel.Valid valuesDAQmx_Val_FullBridge10182Sensor is a full bridge. If you set Use Excitation For Scaling to TRUE, NI-DAQmx divides the measurement by the excitation value.

### DAQmx_AI_Bridge_Cfg

#### Syntax

DAQmx_AI_Bridge_Cfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the type of Wheatstone bridge connected to the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_FullBridge | 10182 | Sensor is a full bridge. If you set Use Excitation For Scaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
| DAQmx_Val_HalfBridge | 10187 | Sensor is a half bridge. If you set Use Excitation For Scaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
| DAQmx_Val_QuarterBridge | 10270 | Sensor is a quarter bridge. If you set Use Excitation For Scaling to TRUE, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
| DAQmx_Val_NoBridge | 10228 | Sensor is not a Wheatstone bridge. |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1gad60bcd8aee767732adb7888e664e24cb.html)
- [DAQmxSetAIBridgeCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1dc8f032a1ac1637d09326d5d5701842.html)
- [DAQmxResetAIBridgeCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga01f8a378068b6ac2735c9d345284a52b.html)

Parent topic:

Bridge

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gae1597e23567f2d0765ed14b280736401.html language=enus -->
## TOPIC 01508: DAQmx_AI_Bridge_InitialRatio

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gae1597e23567f2d0765ed14b280736401.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge_1gae1597e23567f2d0765ed14b280736401.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_InitialRatioRemarksData TypeDescriptionRestrictionsfloat64Specifies in volts per volt the ratio of output voltage from the bridge to excitation voltage supplied to the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equat

### DAQmx_AI_Bridge_InitialRatio

#### Syntax

DAQmx_AI_Bridge_InitialRatio

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in volts per volt the ratio of output voltage from the bridge to excitation voltage supplied to the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set Initial Bridge Voltage, NI-DAQmx coerces this property to Initial Bridge Voltage divided by Actual Excitation Value. If you set this property, NI-DAQmx coerces Initial Bridge Voltage to the value of this property times Actual Excitation Value. If you set both this property and Initial Bridge Voltage, and their values conflict, NI-DAQmx returns an error. To avoid this error, reset one property to its default value before setting the other. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeInitialRatio](group__ni-daqmx__c__functions__property__manipulation__getter_1ga304aafa3c22fc451c841f93196e1a87d.html)
- [DAQmxSetAIBridgeInitialRatio](group__ni-daqmx__c__functions__property__manipulation__setter_1ga34e615c263ccff3397a7441fbbea32d4.html)
- [DAQmxResetAIBridgeInitialRatio](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga7f4980ec335855d0edab1bfc1cfade9e.html)

Parent topic:

Bridge

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__balance.html language=enus -->
## TOPIC 01509: Balance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__balance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__balance.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Bridge_Balance_CoarsePotDAQmx_AI_Bridge_Balance_FinePotAttachmentsNone

### Balance

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Bridge_Balance_CoarsePot |  |
| DAQmx_AI_Bridge_Balance_FinePot |  |

#### Attachments

None

Parent topic:

Bridge

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__balance_1gaa4bcaabde497733fbfc4d6b3f8487d32.html language=enus -->
## TOPIC 01510: DAQmx_AI_Bridge_Balance_FinePot

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__balance_1gaa4bcaabde497733fbfc4d6b3f8487d32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__balance_1gaa4bcaabde497733fbfc4d6b3f8487d32.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_Balance_FinePotRemarksData TypeDescriptionRestrictionsint32Specifies by how much to compensate for offset in the signal. This value can be between 0 and 4095.You can get/set/reset this property using:DAQmxGetAIBridgeBalanceFinePotDAQmxSetAIBridgeBalanceFinePotDAQmxResetAIBridge

### DAQmx_AI_Bridge_Balance_FinePot

#### Syntax

DAQmx_AI_Bridge_Balance_FinePot

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies by how much to compensate for offset in the signal. This value can be between 0 and 4095. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeBalanceFinePot](group__ni-daqmx__c__functions__property__manipulation__getter_1ga366028ed7bd64c0d63112c3587474726.html)
- [DAQmxSetAIBridgeBalanceFinePot](group__ni-daqmx__c__functions__property__manipulation__setter_1ga4d8c996d16b5017af8a2003f47edae4d.html)
- [DAQmxResetAIBridgeBalanceFinePot](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga2919925f90ee3b0b0a7e99a590419103.html)

Parent topic:

Balance

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal.html language=enus -->
## TOPIC 01511: Shunt Cal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Bridge_ShuntCal_EnableDAQmx_AI_Bridge_ShuntCal_GainAdjustDAQmx_AI_Bridge_ShuntCal_SelectDAQmx_AI_Bridge_ShuntCal_ShuntCalAActualResistanceDAQmx_AI_Bridge_ShuntCal_ShuntCalAResistanceDAQmx_AI_Bridge_ShuntCal_ShuntCalASrcDAQmx_AI_Bridge_ShuntCal_ShuntCalB

### Shunt Cal

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Bridge_ShuntCal_Enable |  |
| DAQmx_AI_Bridge_ShuntCal_GainAdjust |  |
| DAQmx_AI_Bridge_ShuntCal_Select |  |
| DAQmx_AI_Bridge_ShuntCal_ShuntCalAActualResistance |  |
| DAQmx_AI_Bridge_ShuntCal_ShuntCalAResistance |  |
| DAQmx_AI_Bridge_ShuntCal_ShuntCalASrc |  |
| DAQmx_AI_Bridge_ShuntCal_ShuntCalBActualResistance |  |
| DAQmx_AI_Bridge_ShuntCal_ShuntCalBResistance |  |

#### Attachments

None

Parent topic:

Bridge

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga536df46b5e15f41033cffc56532dacfa.html language=enus -->
## TOPIC 01512: DAQmx_AI_Bridge_ShuntCal_ShuntCalBResistance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga536df46b5e15f41033cffc56532dacfa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga536df46b5e15f41033cffc56532dacfa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_ShuntCal_ShuntCalBResistanceRemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the desired value of the internal shunt calibration B resistor.You can get/set/reset this property using:DAQmxGetAIBridgeShuntCalShuntCalBResistanceDAQmxSetAIBridgeShuntCalShuntCalBResis

### DAQmx_AI_Bridge_ShuntCal_ShuntCalBResistance

#### Syntax

DAQmx_AI_Bridge_ShuntCal_ShuntCalBResistance

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the desired value of the internal shunt calibration B resistor. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeShuntCalShuntCalBResistance](group__ni-daqmx__c__functions__property__manipulation__getter_1gab0f74733cdeb26e64787b4965206ee54.html)
- [DAQmxSetAIBridgeShuntCalShuntCalBResistance](group__ni-daqmx__c__functions__property__manipulation__setter_1gadbd2c66018d6659b3e73e3531f20a015.html)
- [DAQmxResetAIBridgeShuntCalShuntCalBResistance](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9e183ca85bc564e069b9f56216cf7d0e.html)

Parent topic:

Shunt Cal

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga5fc481dc340dad28f0c4816885b743a9.html language=enus -->
## TOPIC 01513: DAQmx_AI_Bridge_ShuntCal_GainAdjust

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga5fc481dc340dad28f0c4816885b743a9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga5fc481dc340dad28f0c4816885b743a9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_ShuntCal_GainAdjustRemarksData TypeDescriptionRestrictionsfloat64Specifies the result of a shunt calibration. This property is set by DAQmx Perform Shunt Calibration. NI-DAQmx multiplies data read from the channel by the value of this property. This value should be close to 1.0

### DAQmx_AI_Bridge_ShuntCal_GainAdjust

#### Syntax

DAQmx_AI_Bridge_ShuntCal_GainAdjust

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the result of a shunt calibration. This property is set by DAQmx Perform Shunt Calibration. NI-DAQmx multiplies data read from the channel by the value of this property. This value should be close to 1.0. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeShuntCalGainAdjust](group__ni-daqmx__c__functions__property__manipulation__getter_1ga34b0cfb21c8fd346bc5993e81e6c1a5b.html)
- [DAQmxSetAIBridgeShuntCalGainAdjust](group__ni-daqmx__c__functions__property__manipulation__setter_1gac51bc958f52ac0561c7f4368fb4185f4.html)
- [DAQmxResetAIBridgeShuntCalGainAdjust](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga7fa87418a63f87ff2f86675af8a4ecd8.html)

Parent topic:

Shunt Cal

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga6aabcee31bc10afbbf66ec668ca40ced.html language=enus -->
## TOPIC 01514: DAQmx_AI_Bridge_ShuntCal_ShuntCalBActualResistance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga6aabcee31bc10afbbf66ec668ca40ced.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1ga6aabcee31bc10afbbf66ec668ca40ced.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_ShuntCal_ShuntCalBActualResistanceRemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the actual value of the internal shunt calibration B resistor.You can get/set/reset this property using:DAQmxGetAIBridgeShuntCalShuntCalBActualResistanceDAQmxSetAIBridgeShuntCalShu

### DAQmx_AI_Bridge_ShuntCal_ShuntCalBActualResistance

#### Syntax

DAQmx_AI_Bridge_ShuntCal_ShuntCalBActualResistance

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the actual value of the internal shunt calibration B resistor. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeShuntCalShuntCalBActualResistance](group__ni-daqmx__c__functions__property__manipulation__getter_1ga868cb1961f0eb50c906e66d85ef79526.html)
- [DAQmxSetAIBridgeShuntCalShuntCalBActualResistance](group__ni-daqmx__c__functions__property__manipulation__setter_1ga14af6c2a251c07419e2ecdf04235645d.html)
- [DAQmxResetAIBridgeShuntCalShuntCalBActualResistance](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga2d341edc6ca51fefcdd3a59ad6fdce7a.html)

Parent topic:

Shunt Cal

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1gab85d2a7f07e76f86503856b51048390d.html language=enus -->
## TOPIC 01515: DAQmx_AI_Bridge_ShuntCal_ShuntCalAResistance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1gab85d2a7f07e76f86503856b51048390d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1gab85d2a7f07e76f86503856b51048390d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_ShuntCal_ShuntCalAResistanceRemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the desired value of the internal shunt calibration A resistor.You can get/set/reset this property using:DAQmxGetAIBridgeShuntCalShuntCalAResistanceDAQmxSetAIBridgeShuntCalShuntCalAResis

### DAQmx_AI_Bridge_ShuntCal_ShuntCalAResistance

#### Syntax

DAQmx_AI_Bridge_ShuntCal_ShuntCalAResistance

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the desired value of the internal shunt calibration A resistor. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeShuntCalShuntCalAResistance](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0863bc0e8f027e3da5ce5880fae66fc5.html)
- [DAQmxSetAIBridgeShuntCalShuntCalAResistance](group__ni-daqmx__c__functions__property__manipulation__setter_1ga01ea5a6ac6a347da02561e13f02c2710.html)
- [DAQmxResetAIBridgeShuntCalShuntCalAResistance](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga099e8ccc1f571ac0b4007382884c7e18.html)

Parent topic:

Shunt Cal

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1gaf92bd1eefecb0814750d4a4b334a89b2.html language=enus -->
## TOPIC 01516: DAQmx_AI_Bridge_ShuntCal_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1gaf92bd1eefecb0814750d4a4b334a89b2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__bridge__shunt__cal_1gaf92bd1eefecb0814750d4a4b334a89b2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Bridge_ShuntCal_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to enable a shunt calibration switch. Use Shunt Cal Select to select the switch(es) to enable.You can get/set/reset this property using:DAQmxGetAIBridgeShuntCalEnableDAQmxSetAIBridgeShuntCalEnableDAQm

### DAQmx_AI_Bridge_ShuntCal_Enable

#### Syntax

DAQmx_AI_Bridge_ShuntCal_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to enable a shunt calibration switch. Use Shunt Cal Select to select the switch(es) to enable. |  |

You can get/set/reset this property using:

- [DAQmxGetAIBridgeShuntCalEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga029bb4e5f63fcfa72ca383a9db9bc4c0.html)
- [DAQmxSetAIBridgeShuntCalEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga2c0d814ebd7134e2b7c917eebca266d2.html)
- [DAQmxResetAIBridgeShuntCalEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga513b8bd15b703b9f2a18812fb3596a94.html)

Parent topic:

Shunt Cal

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__current__shunt__resistor.html language=enus -->
## TOPIC 01517: Current Shunt Resistor

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__current__shunt__resistor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__current__shunt__resistor.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_CurrentShunt_LocDAQmx_AI_CurrentShunt_ResistanceAttachmentsNone

### Current Shunt Resistor

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_CurrentShunt_Loc |  |
| DAQmx_AI_CurrentShunt_Resistance |  |

#### Attachments

None

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation.html language=enus -->
## TOPIC 01518: Excitation

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAC ExcitationAdvancedGroup membersNameDescriptionDAQmx_AI_Excit_SenseDAQmx_AI_Excit_SrcDAQmx_AI_Excit_ValAttachmentsNone

### Excitation

#### Groups

- AC Excitation
- Advanced

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Excit_Sense |  |
| DAQmx_AI_Excit_Src |  |
| DAQmx_AI_Excit_Val |  |

#### Attachments

None

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation_1ga739f97378e854ec3fd679a8be1a78351.html language=enus -->
## TOPIC 01519: DAQmx_AI_Excit_Val

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation_1ga739f97378e854ec3fd679a8be1a78351.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation_1ga739f97378e854ec3fd679a8be1a78351.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_ValRemarksData TypeDescriptionRestrictionsfloat64Specifies the amount of excitation that the sensor requires. If Voltage or Current is DAQmx_Val_Voltage, this value is in volts. If Voltage or Current is DAQmx_Val_Current, this value is in amperes.You can get/set/reset this prope

### DAQmx_AI_Excit_Val

#### Syntax

DAQmx_AI_Excit_Val

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the amount of excitation that the sensor requires. If Voltage or Current is DAQmx_Val_Voltage, this value is in volts. If Voltage or Current is DAQmx_Val_Current, this value is in amperes. |  |

You can get/set/reset this property using:

- [DAQmxGetAIExcitVal](group__ni-daqmx__c__functions__property__manipulation__getter_1ga82c664a61b9fdea47512ebf5d7d6b6c8.html)
- [DAQmxSetAIExcitVal](group__ni-daqmx__c__functions__property__manipulation__setter_1ga8edc9d9dc12afe7eb5e1720cab4df6c3.html)
- [DAQmxResetAIExcitVal](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4948cfa1df02b00044a92f504a16c779.html)

Parent topic:

Excitation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation_1gaa50cd2d343daffd9daa27f7e4c929c60.html language=enus -->
## TOPIC 01520: DAQmx_AI_Excit_Src

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation_1gaa50cd2d343daffd9daa27f7e4c929c60.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation_1gaa50cd2d343daffd9daa27f7e4c929c60.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_SrcRemarksData TypeDescriptionRestrictionsint32Specifies the source of excitation.Valid valuesDAQmx_Val_Internal10200Use the built-in excitation source of the device. If you select this value, you must specify the amount of excitation.DAQmx_Val_External10167Use an excitation sou

### DAQmx_AI_Excit_Src

#### Syntax

DAQmx_AI_Excit_Src

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the source of excitation. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Internal | 10200 | Use the built-in excitation source of the device. If you select this value, you must specify the amount of excitation. |
| DAQmx_Val_External | 10167 | Use an excitation source other than the built-in excitation source of the device. If you select this value, you must specify the amount of excitation. |
| DAQmx_Val_None | 10230 | Supply no excitation to the channel. |

You can get/set/reset this property using:

- [DAQmxGetAIExcitSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga457eaf73c65fe3f11be6662db109f086.html)
- [DAQmxSetAIExcitSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1gaff67444b158a7dd68da8c9605a4339e2.html)
- [DAQmxResetAIExcitSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaaa2f04b843044c0bc7b9b8887a72f3b8.html)

Parent topic:

Excitation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation.html language=enus -->
## TOPIC 01521: AC Excitation

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_ACExcit_FreqDAQmx_AI_ACExcit_SyncEnableDAQmx_AI_ACExcit_WireModeAttachmentsNone

### AC Excitation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_ACExcit_Freq |  |
| DAQmx_AI_ACExcit_SyncEnable |  |
| DAQmx_AI_ACExcit_WireMode |  |

#### Attachments

None

Parent topic:

Excitation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1ga2141d96d094d8e4f62ae297af964696e.html language=enus -->
## TOPIC 01522: DAQmx_AI_ACExcit_WireMode

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1ga2141d96d094d8e4f62ae297af964696e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1ga2141d96d094d8e4f62ae297af964696e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_ACExcit_WireModeRemarksData TypeDescriptionRestrictionsint32Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.Valid valuesDAQmx_Val_4Wire44-wi

### DAQmx_AI_ACExcit_WireMode

#### Syntax

DAQmx_AI_ACExcit_WireMode

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_4Wire | 4 | 4-wire. |
| DAQmx_Val_5Wire | 5 | 5-wire. |
| DAQmx_Val_6Wire | 6 | 6-wire. |

You can get/set/reset this property using:

- [DAQmxGetAIACExcitWireMode](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0650c2fd167228f26c332147a654e753.html)
- [DAQmxSetAIACExcitWireMode](group__ni-daqmx__c__functions__property__manipulation__setter_1gac141dd2f805e3e05a1488480381ba0e3.html)
- [DAQmxResetAIACExcitWireMode](group__ni-daqmx__c__functions__property__manipulation__resetter_1gad081406eb997bcad42b639647528d991.html)

Parent topic:

AC Excitation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1gad2f616b5b0e55b72890e1f9fa7b36ba9.html language=enus -->
## TOPIC 01523: DAQmx_AI_ACExcit_SyncEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1gad2f616b5b0e55b72890e1f9fa7b36ba9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1gad2f616b5b0e55b72890e1f9fa7b36ba9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_ACExcit_SyncEnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to synchronize the AC excitation source of the channel to that of another channel. Synchronize the excitation sources of multiple channels to use multichannel sensors. Set this property to FALSE for the m

### DAQmx_AI_ACExcit_SyncEnable

#### Syntax

DAQmx_AI_ACExcit_SyncEnable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to synchronize the AC excitation source of the channel to that of another channel. Synchronize the excitation sources of multiple channels to use multichannel sensors. Set this property to FALSE for the master channel and to TRUE for the slave channels. |  |

You can get/set/reset this property using:

- [DAQmxGetAIACExcitSyncEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga52aaa949a26984e990db869a9c425bf0.html)
- [DAQmxSetAIACExcitSyncEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga04fc400fbaa92fdcfc441695fb5b2530.html)
- [DAQmxResetAIACExcitSyncEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga441f8a8fd4864a7399f702f9a4a6f735.html)

Parent topic:

AC Excitation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1gaf6d15a0e88540ca16a07f5abb36fe2ef.html language=enus -->
## TOPIC 01524: DAQmx_AI_ACExcit_Freq

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1gaf6d15a0e88540ca16a07f5abb36fe2ef.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__ac__excitation_1gaf6d15a0e88540ca16a07f5abb36fe2ef.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_ACExcit_FreqRemarksData TypeDescriptionRestrictionsfloat64Specifies the AC excitation frequency in Hertz.You can get/set/reset this property using:DAQmxGetAIACExcitFreqDAQmxSetAIACExcitFreqDAQmxResetAIACExcitFreq

### DAQmx_AI_ACExcit_Freq

#### Syntax

DAQmx_AI_ACExcit_Freq

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the AC excitation frequency in Hertz. |  |

You can get/set/reset this property using:

- [DAQmxGetAIACExcitFreq](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6c5a343968bcaefab66c407dfffcd180.html)
- [DAQmxSetAIACExcitFreq](group__ni-daqmx__c__functions__property__manipulation__setter_1ga90c28e7635c2bb9ede4fb169f38750f1.html)
- [DAQmxResetAIACExcitFreq](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga838e9c3ec9d62678c1fb6fe383d4bf17.html)

Parent topic:

AC Excitation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga218c41e414647df0d58fccb0a3e5fef9.html language=enus -->
## TOPIC 01525: DAQmx_AI_Excit_ActualVal

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga218c41e414647df0d58fccb0a3e5fef9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga218c41e414647df0d58fccb0a3e5fef9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_ActualValRemarksData TypeDescriptionRestrictionsfloat64Specifies the actual amount of excitation supplied by an internal excitation source. If you read an internal excitation source more precisely with an external device, set this property to the value you read. NI-DAQmx ignores

### DAQmx_AI_Excit_ActualVal

#### Syntax

DAQmx_AI_Excit_ActualVal

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the actual amount of excitation supplied by an internal excitation source. If you read an internal excitation source more precisely with an external device, set this property to the value you read. NI-DAQmx ignores this value for external excitation. When performing shunt calibration, some devices set this property automatically. |  |

You can get/set/reset this property using:

- [DAQmxGetAIExcitActualVal](group__ni-daqmx__c__functions__property__manipulation__getter_1gaaef89d4fd216792aa1e77a8dbaaf4ea8.html)
- [DAQmxSetAIExcitActualVal](group__ni-daqmx__c__functions__property__manipulation__setter_1gacfabf00c30baf6d2b8012e7cfbde536d.html)
- [DAQmxResetAIExcitActualVal](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga535d4f79e10073ed6dcdceeebf55db6f.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga51d08941ecc091ea84b05a199f0bd037.html language=enus -->
## TOPIC 01526: DAQmx_AI_Excit_IdleOutputBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga51d08941ecc091ea84b05a199f0bd037.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga51d08941ecc091ea84b05a199f0bd037.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_IdleOutputBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leave

### DAQmx_AI_Excit_IdleOutputBehavior

#### Syntax

DAQmx_AI_Excit_IdleOutputBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ZeroVoltsOrAmps | 12526 | Drive excitation output to zero. |
| DAQmx_Val_MaintainExistingValue | 12528 | Continue generating the current value. |

You can get/set/reset this property using:

- [DAQmxGetAIExcitIdleOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1gac2f070a7db36077c65f47570c243cf0f.html)
- [DAQmxSetAIExcitIdleOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1gad79511a2c29cc523779b6563288b652f.html)
- [DAQmxResetAIExcitIdleOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga3aedf9f921efebba5bcacb184a7629a8.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga89e79dbfdf43c7da84dd2ceb6d8ac70e.html language=enus -->
## TOPIC 01527: DAQmx_AI_Excit_UseMultiplexed

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga89e79dbfdf43c7da84dd2ceb6d8ac70e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga89e79dbfdf43c7da84dd2ceb6d8ac70e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_UseMultiplexedRemarksData TypeDescriptionRestrictionsbool32Specifies if the SCXI-1122 multiplexes the excitation to the upper half of the channels as it advances through the scan list.You can get/set/reset this property using:DAQmxGetAIExcitUseMultiplexedDAQmxSetAIExcitUseMultip

### DAQmx_AI_Excit_UseMultiplexed

#### Syntax

DAQmx_AI_Excit_UseMultiplexed

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies if the SCXI-1122 multiplexes the excitation to the upper half of the channels as it advances through the scan list. |  |

You can get/set/reset this property using:

- [DAQmxGetAIExcitUseMultiplexed](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf5481c334ded4f9be3ec50c74fe3284b.html)
- [DAQmxSetAIExcitUseMultiplexed](group__ni-daqmx__c__functions__property__manipulation__setter_1ga40310792afcd5ccde90c18e58eeac760.html)
- [DAQmxResetAIExcitUseMultiplexed](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga07558efcc4623bc9f6dbf430c6375e9a.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga9310ac1f78ef15eef17fb4a7866af524.html language=enus -->
## TOPIC 01528: DAQmx_AI_Excit_VoltageOrCurrent

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga9310ac1f78ef15eef17fb4a7866af524.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1ga9310ac1f78ef15eef17fb4a7866af524.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_VoltageOrCurrentRemarksData TypeDescriptionRestrictionsint32Specifies if the channel uses current or voltage excitation.Valid valuesDAQmx_Val_Voltage10322Voltage excitation.DAQmx_Val_Current10134Current excitation.You can get/set/reset this property using:DAQmxGetAIExcitVoltageO

### DAQmx_AI_Excit_VoltageOrCurrent

#### Syntax

DAQmx_AI_Excit_VoltageOrCurrent

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies if the channel uses current or voltage excitation. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Voltage | 10322 | Voltage excitation. |
| DAQmx_Val_Current | 10134 | Current excitation. |

You can get/set/reset this property using:

- [DAQmxGetAIExcitVoltageOrCurrent](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1cc8e2b9a0ff0028f61b5a47a0ec5bcc.html)
- [DAQmxSetAIExcitVoltageOrCurrent](group__ni-daqmx__c__functions__property__manipulation__setter_1ga145382e3f0b84bbf1271f60c0671f759.html)
- [DAQmxResetAIExcitVoltageOrCurrent](group__ni-daqmx__c__functions__property__manipulation__resetter_1gad4faa7943800f5d70414a0560b380cd2.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1gad57515244e7fe1e56c7e2c5801f36ccc.html language=enus -->
## TOPIC 01529: DAQmx_AI_Excit_UseForScaling

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1gad57515244e7fe1e56c7e2c5801f36ccc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1gad57515244e7fe1e56c7e2c5801f36ccc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_UseForScalingRemarksData TypeDescriptionRestrictionsbool32Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set this property to TRUE for ratiometric transducers. If you set this property to TRUE, set Maximum Value and Minimum Value to reflect

### DAQmx_AI_Excit_UseForScaling

#### Syntax

DAQmx_AI_Excit_UseForScaling

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set this property to TRUE for ratiometric transducers. If you set this property to TRUE, set Maximum Value and Minimum Value to reflect the scaling. |  |

You can get/set/reset this property using:

- [DAQmxGetAIExcitUseForScaling](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf6ca71e1e838ead80101d74d740f616c.html)
- [DAQmxSetAIExcitUseForScaling](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9ad7d073172f3883a5ad7e9f51400cc6.html)
- [DAQmxResetAIExcitUseForScaling](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga516f7289fc5a94659be9ceacd87ef366.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1gafc9a8b81cf565ba96bc8c683ef30472b.html language=enus -->
## TOPIC 01530: DAQmx_AI_Excit_DCorAC

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1gafc9a8b81cf565ba96bc8c683ef30472b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__excitation__advanced_1gafc9a8b81cf565ba96bc8c683ef30472b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Excit_DCorACRemarksData TypeDescriptionRestrictionsint32Specifies if the excitation supply is DC or AC.Valid valuesDAQmx_Val_DC10050DC excitation.DAQmx_Val_AC10045AC excitation.You can get/set/reset this property using:DAQmxGetAIExcitDCorACDAQmxSetAIExcitDCorACDAQmxResetAIExcitDCorAC

### DAQmx_AI_Excit_DCorAC

#### Syntax

DAQmx_AI_Excit_DCorAC

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies if the excitation supply is DC or AC. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_DC | 10050 | DC excitation. |
| DAQmx_Val_AC | 10045 | AC excitation. |

You can get/set/reset this property using:

- [DAQmxGetAIExcitDCorAC](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf01487b6d6ec40733c4a370c88140695.html)
- [DAQmxSetAIExcitDCorAC](group__ni-daqmx__c__functions__property__manipulation__setter_1ga7710192a1c777734c83bb8e25c3f1ded.html)
- [DAQmxResetAIExcitDCorAC](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga6774ab907fe979aaf42b174c0888ccd1.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power.html language=enus -->
## TOPIC 01531: Sensor Power

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_SensorPower_CfgDAQmx_AI_SensorPower_TypeDAQmx_AI_SensorPower_VoltageAttachmentsNone

### Sensor Power

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_SensorPower_Cfg |  |
| DAQmx_AI_SensorPower_Type |  |
| DAQmx_AI_SensorPower_Voltage |  |

#### Attachments

None

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1ga3214550571370c88f06f9b2543e2961e.html language=enus -->
## TOPIC 01532: DAQmx_AI_SensorPower_Voltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1ga3214550571370c88f06f9b2543e2961e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1ga3214550571370c88f06f9b2543e2961e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_SensorPower_VoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies the voltage level for the sensor's power supply.You can get/set/reset this property using:DAQmxGetAISensorPowerVoltageDAQmxSetAISensorPowerVoltageDAQmxResetAISensorPowerVoltage

### DAQmx_AI_SensorPower_Voltage

#### Syntax

DAQmx_AI_SensorPower_Voltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the voltage level for the sensor's power supply. |  |

You can get/set/reset this property using:

- [DAQmxGetAISensorPowerVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga25f4da6cc0e5af947785e8de9f08afda.html)
- [DAQmxSetAISensorPowerVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1gab6f427a3fac45c956ba180f5fa2fcae9.html)
- [DAQmxResetAISensorPowerVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga6fc5b3ff30f3bac2af30b69b30c95a61.html)

Parent topic:

Sensor Power

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1gae9f0fe826fbe0e23f4d98618b935b93c.html language=enus -->
## TOPIC 01533: DAQmx_AI_SensorPower_Cfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1gae9f0fe826fbe0e23f4d98618b935b93c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1gae9f0fe826fbe0e23f4d98618b935b93c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_SensorPower_CfgRemarksData TypeDescriptionRestrictionsint32Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged.Valid valuesDAQmx_Val_NoChange10160Sensor power supply configuration is not changed.DAQmx_Val_Enabled16145Sensor power supply is tu

### DAQmx_AI_SensorPower_Cfg

#### Syntax

DAQmx_AI_SensorPower_Cfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_NoChange | 10160 | Sensor power supply configuration is not changed. |
| DAQmx_Val_Enabled | 16145 | Sensor power supply is turned on. |
| DAQmx_Val_Disabled | 16146 | Sensor power supply is turned off. |

You can get/set/reset this property using:

- [DAQmxGetAISensorPowerCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1gae424be9fe5503770ea6501bcc8049bf6.html)
- [DAQmxSetAISensorPowerCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga7657781241ba5b75c12a327145c100a3.html)
- [DAQmxResetAISensorPowerCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaccaefde886fdb12dd4dfe5d89a5c5c7a.html)

Parent topic:

Sensor Power

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1gaf1ab06818ed18d50b7262efe596232dd.html language=enus -->
## TOPIC 01534: DAQmx_AI_SensorPower_Type

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1gaf1ab06818ed18d50b7262efe596232dd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__sensor__power_1gaf1ab06818ed18d50b7262efe596232dd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_SensorPower_TypeRemarksData TypeDescriptionRestrictionsint32Specifies the type of power supplied to the sensor.Valid valuesDAQmx_Val_DC10050Sensor power supply generates a single DC voltage level.DAQmx_Val_AC10045Sensor power supply generates an AC voltage.DAQmx_Val_BipolarDC16147Sens

### DAQmx_AI_SensorPower_Type

#### Syntax

DAQmx_AI_SensorPower_Type

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the type of power supplied to the sensor. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_DC | 10050 | Sensor power supply generates a single DC voltage level. |
| DAQmx_Val_AC | 10045 | Sensor power supply generates an AC voltage. |
| DAQmx_Val_BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

You can get/set/reset this property using:

- [DAQmxGetAISensorPowerType](group__ni-daqmx__c__functions__property__manipulation__getter_1gade213f98bca1e905dd3ab3e707a6455c.html)
- [DAQmxSetAISensorPowerType](group__ni-daqmx__c__functions__property__manipulation__setter_1ga193344ad44b1fed8a53be61a3668543f.html)
- [DAQmxResetAISensorPowerType](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga6a2a5c2ef2c2cbaf5037cd4bdecefd68.html)

Parent topic:

Sensor Power

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__thermocouple.html language=enus -->
## TOPIC 01535: Thermocouple

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__thermocouple.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__thermocouple.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_AttenDAQmx_AI_OpenThrmcplDetectEnableDAQmx_AI_ProbeAttenDAQmx_AI_Thrmcpl_LeadOffsetVoltageAttachmentsNone

### Thermocouple

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Atten |  |
| DAQmx_AI_OpenThrmcplDetectEnable |  |
| DAQmx_AI_ProbeAtten |  |
| DAQmx_AI_Thrmcpl_LeadOffsetVoltage |  |

#### Attachments

None

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__thermocouple_1ga30af0df5817eacb3203ca6467f2d36fa.html language=enus -->
## TOPIC 01536: DAQmx_AI_Thrmcpl_LeadOffsetVoltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__thermocouple_1ga30af0df5817eacb3203ca6467f2d36fa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__general__properties__signal__conditioning__thermocouple_1ga30af0df5817eacb3203ca6467f2d36fa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Thrmcpl_LeadOffsetVoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies the lead offset nulling voltage to subtract from measurements on a device. This property is ignored if open thermocouple detection is disabled.You can get/set/reset this property using:DAQmxGetAIThrmcplLe

### DAQmx_AI_Thrmcpl_LeadOffsetVoltage

#### Syntax

DAQmx_AI_Thrmcpl_LeadOffsetVoltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the lead offset nulling voltage to subtract from measurements on a device. This property is ignored if open thermocouple detection is disabled. |  |

You can get/set/reset this property using:

- [DAQmxGetAIThrmcplLeadOffsetVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga5bcd574a813ace15c84d1c14fb22fd85.html)
- [DAQmxSetAIThrmcplLeadOffsetVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1ga35db5aeb6f04530e4e063dfe03d9f037.html)
- [DAQmxResetAIThrmcplLeadOffsetVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf719b02e92758f931c3d0f427e01e0b9.html)

Parent topic:

Thermocouple

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position.html language=enus -->
## TOPIC 01537: Position

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsEddy Current Proximity ProbeLVDTRVDTGroup membersNoneAttachmentsNone

### Position

#### Groups

- Eddy Current Proximity Probe
- LVDT
- RVDT

#### Group members

None

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe.html language=enus -->
## TOPIC 01538: Eddy Current Proximity Probe

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_EddyCurrentProxProbe_SensitivityDAQmx_AI_EddyCurrentProxProbe_SensitivityUnitsDAQmx_AI_EddyCurrentProxProbe_UnitsAttachmentsNone

### Eddy Current Proximity Probe

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_EddyCurrentProxProbe_Sensitivity |  |
| DAQmx_AI_EddyCurrentProxProbe_SensitivityUnits |  |
| DAQmx_AI_EddyCurrentProxProbe_Units |  |

#### Attachments

None

Parent topic:

Position

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1ga4a223046241b3b95e97200b2ab5f06c3.html language=enus -->
## TOPIC 01539: DAQmx_AI_EddyCurrentProxProbe_Sensitivity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1ga4a223046241b3b95e97200b2ab5f06c3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1ga4a223046241b3b95e97200b2ab5f06c3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_EddyCurrentProxProbe_SensitivityRemarksData TypeDescriptionRestrictionsfloat64Specifies the sensitivity of the eddy current proximity probe . This value is in the units you specify with Sensitivity Units. Refer to the sensor documentation to determine this value.You can get/set/reset

### DAQmx_AI_EddyCurrentProxProbe_Sensitivity

#### Syntax

DAQmx_AI_EddyCurrentProxProbe_Sensitivity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the sensitivity of the eddy current proximity probe . This value is in the units you specify with Sensitivity Units. Refer to the sensor documentation to determine this value. |  |

You can get/set/reset this property using:

- [DAQmxGetAIEddyCurrentProxProbeSensitivity](group__ni-daqmx__c__functions__property__manipulation__getter_1ga689ddecb4d06c543309927e0c993701d.html)
- [DAQmxSetAIEddyCurrentProxProbeSensitivity](group__ni-daqmx__c__functions__property__manipulation__setter_1ga028995622ff9bfc052f728706682a64e.html)
- [DAQmxResetAIEddyCurrentProxProbeSensitivity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga25e0102d02ddb0b7b6853786bd11f845.html)

Parent topic:

Eddy Current Proximity Probe

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1ga91b6bf504792e0fcf3c0dffe29eeccda.html language=enus -->
## TOPIC 01540: DAQmx_AI_EddyCurrentProxProbe_SensitivityUnits

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1ga91b6bf504792e0fcf3c0dffe29eeccda.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1ga91b6bf504792e0fcf3c0dffe29eeccda.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_EddyCurrentProxProbe_SensitivityUnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units of Sensitivity.Valid valuesDAQmx_Val_mVoltsPerMil14836mVolts/mil.DAQmx_Val_VoltsPerMil14837Volts/mil.DAQmx_Val_mVoltsPerMillimeter14838mVolts/mMeter.DAQmx_Val_VoltsPerMillimeter14839Vo

### DAQmx_AI_EddyCurrentProxProbe_SensitivityUnits

#### Syntax

DAQmx_AI_EddyCurrentProxProbe_SensitivityUnits

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units of Sensitivity. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_mVoltsPerMil | 14836 | mVolts/mil. |
| DAQmx_Val_VoltsPerMil | 14837 | Volts/mil. |
| DAQmx_Val_mVoltsPerMillimeter | 14838 | mVolts/mMeter. |
| DAQmx_Val_VoltsPerMillimeter | 14839 | Volts/mMeter. |
| DAQmx_Val_mVoltsPerMicron | 14840 | mVolts/micron. |

You can get/set/reset this property using:

- [DAQmxGetAIEddyCurrentProxProbeSensitivityUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7ae7b9e5d39bf2e7c7e0518ed7d56027.html)
- [DAQmxSetAIEddyCurrentProxProbeSensitivityUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1gae98d68b32f8e8c3377b72d686c1ff347.html)
- [DAQmxResetAIEddyCurrentProxProbeSensitivityUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga17ec0043fc16cdc2f2973e7fb10d72e3.html)

Parent topic:

Eddy Current Proximity Probe

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1gab15c460f4146347770124e22435709a4.html language=enus -->
## TOPIC 01541: DAQmx_AI_EddyCurrentProxProbe_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1gab15c460f4146347770124e22435709a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__eddy__current__proximity__probe_1gab15c460f4146347770124e22435709a4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_EddyCurrentProxProbe_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return proximity measurements from the channel.Valid valuesDAQmx_Val_Meters10219Meters.DAQmx_Val_Inches10379Inches.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you s

### DAQmx_AI_EddyCurrentProxProbe_Units

#### Syntax

DAQmx_AI_EddyCurrentProxProbe_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return proximity measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Meters | 10219 | Meters. |
| DAQmx_Val_Inches | 10379 | Inches. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAIEddyCurrentProxProbeUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga61551aed98639b686473a56b86accecc.html)
- [DAQmxSetAIEddyCurrentProxProbeUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga642a362a170e1dcc4f8382eba4aadd7b.html)
- [DAQmxResetAIEddyCurrentProxProbeUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga1c3fc6bf9b397e3cee42df6663ba8a27.html)

Parent topic:

Eddy Current Proximity Probe

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__lvdt.html language=enus -->
## TOPIC 01542: LVDT

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__lvdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__lvdt.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_LVDT_SensitivityDAQmx_AI_LVDT_SensitivityUnitsDAQmx_AI_LVDT_UnitsAttachmentsNone

### LVDT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_LVDT_Sensitivity |  |
| DAQmx_AI_LVDT_SensitivityUnits |  |
| DAQmx_AI_LVDT_Units |  |

#### Attachments

None

Parent topic:

Position

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1ga8a3c54d00b9128c79ec54400cb7a5172.html language=enus -->
## TOPIC 01543: DAQmx_AI_LVDT_Sensitivity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1ga8a3c54d00b9128c79ec54400cb7a5172.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1ga8a3c54d00b9128c79ec54400cb7a5172.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_LVDT_SensitivityRemarksData TypeDescriptionRestrictionsfloat64Specifies the sensitivity of the LVDT. This value is in the units you specify with Sensitivity Units. Refer to the sensor documentation to determine this value.You can get/set/reset this property using:DAQmxGetAILVDTSensiti

### DAQmx_AI_LVDT_Sensitivity

#### Syntax

DAQmx_AI_LVDT_Sensitivity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the sensitivity of the LVDT. This value is in the units you specify with Sensitivity Units. Refer to the sensor documentation to determine this value. |  |

You can get/set/reset this property using:

- [DAQmxGetAILVDTSensitivity](group__ni-daqmx__c__functions__property__manipulation__getter_1ga379edffd20e777f7d041413a1287c5d1.html)
- [DAQmxSetAILVDTSensitivity](group__ni-daqmx__c__functions__property__manipulation__setter_1gac3a2e1535bd0ab6f41e7c002b3f390c1.html)
- [DAQmxResetAILVDTSensitivity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga605081ff70fc19df0409a515c22a6a04.html)

Parent topic:

LVDT

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1gac8dee55c109372f3d6f2b192ee9c1148.html language=enus -->
## TOPIC 01544: DAQmx_AI_LVDT_SensitivityUnits

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1gac8dee55c109372f3d6f2b192ee9c1148.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1gac8dee55c109372f3d6f2b192ee9c1148.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_LVDT_SensitivityUnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units of Sensitivity.Valid valuesDAQmx_Val_mVoltsPerVoltPerMillimeter12506mVolts/Volt/mMeter.DAQmx_Val_mVoltsPerVoltPerMilliInch12505mVolts/Volt/0.001 Inch.You can get/set/reset this property using:DAQmxGet

### DAQmx_AI_LVDT_SensitivityUnits

#### Syntax

DAQmx_AI_LVDT_SensitivityUnits

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units of Sensitivity. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_mVoltsPerVoltPerMillimeter | 12506 | mVolts/Volt/mMeter. |
| DAQmx_Val_mVoltsPerVoltPerMilliInch | 12505 | mVolts/Volt/0.001 Inch. |

You can get/set/reset this property using:

- [DAQmxGetAILVDTSensitivityUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga579237a24f775066d25044ef99b3d995.html)
- [DAQmxSetAILVDTSensitivityUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga002ebacb978f5ebc7be59c30128315a7.html)
- [DAQmxResetAILVDTSensitivityUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaaac3c8dece39c561c42464812e35433e.html)

Parent topic:

LVDT

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1gad12fd37119f1a55117ba4fded1a90b07.html language=enus -->
## TOPIC 01545: DAQmx_AI_LVDT_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1gad12fd37119f1a55117ba4fded1a90b07.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__lvdt_1gad12fd37119f1a55117ba4fded1a90b07.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_LVDT_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return linear position measurements from the channel.Valid valuesDAQmx_Val_Meters10219Meters.DAQmx_Val_Inches10379Inches.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select this

### DAQmx_AI_LVDT_Units

#### Syntax

DAQmx_AI_LVDT_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return linear position measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Meters | 10219 | Meters. |
| DAQmx_Val_Inches | 10379 | Inches. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAILVDTUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gadf07435a03c186a9a8f65777a831f986.html)
- [DAQmxSetAILVDTUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga2d486998a2d60dc0f0ffe3ad86baf290.html)
- [DAQmxResetAILVDTUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf285f26f9c4166412e66c2d3f7bf98c2.html)

Parent topic:

LVDT

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__rvdt.html language=enus -->
## TOPIC 01546: RVDT

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__rvdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__rvdt.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_RVDT_SensitivityDAQmx_AI_RVDT_SensitivityUnitsDAQmx_AI_RVDT_UnitsAttachmentsNone

### RVDT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_RVDT_Sensitivity |  |
| DAQmx_AI_RVDT_SensitivityUnits |  |
| DAQmx_AI_RVDT_Units |  |

#### Attachments

None

Parent topic:

Position

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__position__rvdt_1ga91044c099a047744cf526a46cf44913c.html language=enus -->
## TOPIC 01547: DAQmx_AI_RVDT_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__position__rvdt_1ga91044c099a047744cf526a46cf44913c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__position__rvdt_1ga91044c099a047744cf526a46cf44913c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_RVDT_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return angular position measurements from the channel.Valid valuesDAQmx_Val_Degrees10146Degrees.DAQmx_Val_Radians10273Radians.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select

### DAQmx_AI_RVDT_Units

#### Syntax

DAQmx_AI_RVDT_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return angular position measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Degrees | 10146 | Degrees. |
| DAQmx_Val_Radians | 10273 | Radians. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAIRVDTUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gad0f90c94f62d118b20ebb827e21e1a1a.html)
- [DAQmxSetAIRVDTUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1gaf2a4eaa599053a4d5ff316496b44d4cc.html)
- [DAQmxResetAIRVDTUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga41fa21890b38a9b2fe611b5149086aea.html)

Parent topic:

RVDT

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__pressure.html language=enus -->
## TOPIC 01548: Pressure

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__pressure.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__pressure.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Pressure_UnitsAttachmentsNone

### Pressure

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Pressure_Units |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__pressure_1ga6d1b0b09053c78c9b08f5a60ed88bc89.html language=enus -->
## TOPIC 01549: DAQmx_AI_Pressure_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__pressure_1ga6d1b0b09053c78c9b08f5a60ed88bc89.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__pressure_1ga6d1b0b09053c78c9b08f5a60ed88bc89.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Pressure_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies in which unit to return pressure measurements from the channel.Valid valuesDAQmx_Val_Pascals10081Pascals.DAQmx_Val_PoundsPerSquareInch15879Pounds per square inch.DAQmx_Val_Bar15880Bar.DAQmx_Val_FromCustomScale10065Uni

### DAQmx_AI_Pressure_Units

#### Syntax

DAQmx_AI_Pressure_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies in which unit to return pressure measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Pascals | 10081 | Pascals. |
| DAQmx_Val_PoundsPerSquareInch | 15879 | Pounds per square inch. |
| DAQmx_Val_Bar | 15880 | Bar. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAIPressureUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gab0e16a004e2aebd562d68c62737019fd.html)
- [DAQmxSetAIPressureUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga4ce270e8ae54a3b92face8aa97ed872e.html)
- [DAQmxResetAIPressureUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaeb5cbc167328bbab6270e33091e4dccd.html)

Parent topic:

Pressure

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__resistance.html language=enus -->
## TOPIC 01550: Resistance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__resistance.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Resistance_UnitsAttachmentsNone

### Resistance

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Resistance_Units |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__resistance_1ga6a1e987ee481b9cac1fc57e46a4ef838.html language=enus -->
## TOPIC 01551: DAQmx_AI_Resistance_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__resistance_1ga6a1e987ee481b9cac1fc57e46a4ef838.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__resistance_1ga6a1e987ee481b9cac1fc57e46a4ef838.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Resistance_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return resistance measurements.Valid valuesDAQmx_Val_Ohms10384Ohms.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select this value, you must specify a custom scale name.DAQ

### DAQmx_AI_Resistance_Units

#### Syntax

DAQmx_AI_Resistance_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return resistance measurements. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Ohms | 10384 | Ohms. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| DAQmx_Val_FromTEDS | 12516 | Units defined by TEDS information associated with the channel. |

You can get/set/reset this property using:

- [DAQmxGetAIResistanceUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gab1647e45248586234c9ab1e647356996.html)
- [DAQmxSetAIResistanceUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga38a76f06e3fd7b5fd4fcd9bc7ece23d0.html)
- [DAQmxResetAIResistanceUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gabf1eedbe83e5ffc9cf191aaade803a85.html)

Parent topic:

Resistance

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage.html language=enus -->
## TOPIC 01552: Rosette Strain Gage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_RosetteStrainGage_OrientationDAQmx_AI_RosetteStrainGage_RosetteMeasTypeDAQmx_AI_RosetteStrainGage_RosetteTypeDAQmx_AI_RosetteStrainGage_StrainChansAttachmentsNone

### Rosette Strain Gage

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_RosetteStrainGage_Orientation |  |
| DAQmx_AI_RosetteStrainGage_RosetteMeasType |  |
| DAQmx_AI_RosetteStrainGage_RosetteType |  |
| DAQmx_AI_RosetteStrainGage_StrainChans |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga4d6e017559a05365e0c048eb1869d6f0.html language=enus -->
## TOPIC 01553: DAQmx_AI_RosetteStrainGage_Orientation

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga4d6e017559a05365e0c048eb1869d6f0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga4d6e017559a05365e0c048eb1869d6f0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_RosetteStrainGage_OrientationRemarksData TypeDescriptionRestrictionsfloat64Specifies gage orientation in degrees with respect to the X axis.You can get/set/reset this property using:DAQmxGetAIRosetteStrainGageOrientationDAQmxSetAIRosetteStrainGageOrientationDAQmxResetAIRosetteStrainGa

### DAQmx_AI_RosetteStrainGage_Orientation

#### Syntax

DAQmx_AI_RosetteStrainGage_Orientation

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies gage orientation in degrees with respect to the X axis. |  |

You can get/set/reset this property using:

- [DAQmxGetAIRosetteStrainGageOrientation](group__ni-daqmx__c__functions__property__manipulation__getter_1ga26c63af085e1741093245db24caf9a0a.html)
- [DAQmxSetAIRosetteStrainGageOrientation](group__ni-daqmx__c__functions__property__manipulation__setter_1ga4b318f3f2fcac3e92de23280579dc1dd.html)
- [DAQmxResetAIRosetteStrainGageOrientation](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga611bdfb656d5b75880f6ca974a6f9d86.html)

Parent topic:

Rosette Strain Gage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga63f0b31d08962a0f3d0923524c4e94ce.html language=enus -->
## TOPIC 01554: DAQmx_AI_RosetteStrainGage_RosetteMeasType

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga63f0b31d08962a0f3d0923524c4e94ce.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga63f0b31d08962a0f3d0923524c4e94ce.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_RosetteStrainGage_RosetteMeasTypeRemarksData TypeDescriptionRestrictionsint32Specifies the type of rosette measurement.Valid valuesDAQmx_Val_PrincipalStrain115971The maximum tensile strain coplanar to the surface of the material under stress.DAQmx_Val_PrincipalStrain215972The minimum

### DAQmx_AI_RosetteStrainGage_RosetteMeasType

#### Syntax

DAQmx_AI_RosetteStrainGage_RosetteMeasType

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the type of rosette measurement. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_PrincipalStrain1 | 15971 | The maximum tensile strain coplanar to the surface of the material under stress. |
| DAQmx_Val_PrincipalStrain2 | 15972 | The minimum tensile strain coplanar to the surface of the material under stress. |
| DAQmx_Val_PrincipalStrainAngle | 15973 | The angle at which the principal strains of the rosette occur. |
| DAQmx_Val_CartesianStrainX | 15974 | The tensile strain coplanar to the surface of the material under stress in the X coordinate direction. |
| DAQmx_Val_CartesianStrainY | 15975 | The tensile strain coplanar to the surface of the material under stress in the Y coordinate direction. |
| DAQmx_Val_CartesianShearStrainXY | 15976 | The tensile strain coplanar to the surface of the material under stress in the XY coordinate direction. |
| DAQmx_Val_MaxShearStrain | 15977 | The maximum strain coplanar to the cross section of the material under stress. |
| DAQmx_Val_MaxShearStrainAngle | 15978 | The angle at which the maximum shear strain of the rosette occurs. |

You can get/set/reset this property using:

- [DAQmxGetAIRosetteStrainGageRosetteMeasType](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7ea628d05f4ca539e6faee485f7f28e5.html)
- [DAQmxSetAIRosetteStrainGageRosetteMeasType](group__ni-daqmx__c__functions__property__manipulation__setter_1gaf2f4f2925a4fa3e4a7c2df3ded84078a.html)
- [DAQmxResetAIRosetteStrainGageRosetteMeasType](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8183dcb82d6a6aafd13369e20b5c718a.html)

Parent topic:

Rosette Strain Gage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga993dda43a4af48ab3fbd900ceb263c09.html language=enus -->
## TOPIC 01555: DAQmx_AI_RosetteStrainGage_RosetteType

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga993dda43a4af48ab3fbd900ceb263c09.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1ga993dda43a4af48ab3fbd900ceb263c09.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_RosetteStrainGage_RosetteTypeRemarksData TypeDescriptionRestrictionsint32Indicates the type of rosette gage.Not SettableValid valuesDAQmx_Val_RectangularRosette15968A rectangular rosette consists of three strain gages, each separated by a 45 degree angle.DAQmx_Val_DeltaRosette15969A d

### DAQmx_AI_RosetteStrainGage_RosetteType

#### Syntax

DAQmx_AI_RosetteStrainGage_RosetteType

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the type of rosette gage. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_RectangularRosette | 15968 | A rectangular rosette consists of three strain gages, each separated by a 45 degree angle. |
| DAQmx_Val_DeltaRosette | 15969 | A delta rosette consists of three strain gages, each separated by a 60 degree angle. |
| DAQmx_Val_TeeRosette | 15970 | A tee rosette consists of two gages oriented at 90 degrees with respect to each other. |

You can get this property using:

- [DAQmxGetAIRosetteStrainGageRosetteType](group__ni-daqmx__c__functions__property__manipulation__getter_1gacb6e8f01ade1507b407e428dd0ce1186.html)

Parent topic:

Rosette Strain Gage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1gaeacf19f6b23b5fdaeba9a9ef800a3577.html language=enus -->
## TOPIC 01556: DAQmx_AI_RosetteStrainGage_StrainChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1gaeacf19f6b23b5fdaeba9a9ef800a3577.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__rosette__strain__gage_1gaeacf19f6b23b5fdaeba9a9ef800a3577.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_RosetteStrainGage_StrainChansRemarksData TypeDescriptionRestrictionschar*Indicates the raw strain channels that comprise the strain rosette.Not SettableYou can get this property using:DAQmxGetAIRosetteStrainGageStrainChans

### DAQmx_AI_RosetteStrainGage_StrainChans

#### Syntax

DAQmx_AI_RosetteStrainGage_StrainChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the raw strain channels that comprise the strain rosette. | Not Settable |

You can get this property using:

- [DAQmxGetAIRosetteStrainGageStrainChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga348874fa23b2c19d22325369aab459a2.html)

Parent topic:

Rosette Strain Gage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__sound__pressure.html language=enus -->
## TOPIC 01557: Sound Pressure

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__sound__pressure.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__sound__pressure.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsMicrophoneGroup membersNameDescriptionDAQmx_AI_SoundPressure_MaxSoundPressureLvlDAQmx_AI_SoundPressure_UnitsDAQmx_AI_SoundPressure_dBRefAttachmentsNone

### Sound Pressure

#### Groups

- Microphone

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_SoundPressure_MaxSoundPressureLvl |  |
| DAQmx_AI_SoundPressure_Units |  |
| DAQmx_AI_SoundPressure_dBRef |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1ga4bf1dd8b5b3938d553306809493fde9d.html language=enus -->
## TOPIC 01558: DAQmx_AI_SoundPressure_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1ga4bf1dd8b5b3938d553306809493fde9d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1ga4bf1dd8b5b3938d553306809493fde9d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_SoundPressure_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return sound pressure measurements from the channel.Valid valuesDAQmx_Val_Pascals10081Pascals.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select this value, you must s

### DAQmx_AI_SoundPressure_Units

#### Syntax

DAQmx_AI_SoundPressure_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return sound pressure measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Pascals | 10081 | Pascals. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAISoundPressureUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gafb16be86d27c9ba40f30d53772838084.html)
- [DAQmxSetAISoundPressureUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga4da40ef01c1be349fe10469794b90eff.html)
- [DAQmxResetAISoundPressureUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf68c0c62043f4bc0a1c41502a7c68291.html)

Parent topic:

Sound Pressure

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1ga74a00c7172323cac5c78bca2fbe37683.html language=enus -->
## TOPIC 01559: DAQmx_AI_SoundPressure_dBRef

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1ga74a00c7172323cac5c78bca2fbe37683.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1ga74a00c7172323cac5c78bca2fbe37683.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_SoundPressure_dBRefRemarksData TypeDescriptionRestrictionsfloat64Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. NI-DAQmx also uses the decibel reference level w

### DAQmx_AI_SoundPressure_dBRef

#### Syntax

DAQmx_AI_SoundPressure_dBRef

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. NI-DAQmx also uses the decibel reference level when converting Maximum Sound Pressure Level to a voltage level. |  |

You can get/set/reset this property using:

- [DAQmxGetAISoundPressuredBRef](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0e6a3b9ea36097e5060bfaa981b7c275.html)
- [DAQmxSetAISoundPressuredBRef](group__ni-daqmx__c__functions__property__manipulation__setter_1ga18ae5ef7c9281acceb73ae754c36f92c.html)
- [DAQmxResetAISoundPressuredBRef](group__ni-daqmx__c__functions__property__manipulation__resetter_1gad3f73de41a8805fe9dd3ae7e3d8196e2.html)

Parent topic:

Sound Pressure

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1gaf57d572f4b12d31de9e1876a290b7d36.html language=enus -->
## TOPIC 01560: DAQmx_AI_SoundPressure_MaxSoundPressureLvl

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1gaf57d572f4b12d31de9e1876a290b7d36.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__sound__pressure_1gaf57d572f4b12d31de9e1876a290b7d36.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_SoundPressure_MaxSoundPressureLvlRemarksData TypeDescriptionRestrictionsfloat64Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values i

### DAQmx_AI_SoundPressure_MaxSoundPressureLvl

#### Syntax

DAQmx_AI_SoundPressure_MaxSoundPressureLvl

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values in pascals for Maximum Value and Minimum Value for the channel. |  |

You can get/set/reset this property using:

- [DAQmxGetAISoundPressureMaxSoundPressureLvl](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4f75e95cb2bed3b07cd2744251ab46de.html)
- [DAQmxSetAISoundPressureMaxSoundPressureLvl](group__ni-daqmx__c__functions__property__manipulation__setter_1gafb87860de48f2104fb3b6fab736d7a34.html)
- [DAQmxResetAISoundPressureMaxSoundPressureLvl](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga87e6e5ccc9c3cfef460f787859827aac.html)

Parent topic:

Sound Pressure

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__sound__pressure__microphone.html language=enus -->
## TOPIC 01561: Microphone

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__sound__pressure__microphone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__sound__pressure__microphone.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Microphone_SensitivityAttachmentsNone

### Microphone

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Microphone_Sensitivity |  |

#### Attachments

None

Parent topic:

Sound Pressure

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__sound__pressure__microphone_1ga15e671dd4ed45847774317773a399a0c.html language=enus -->
## TOPIC 01562: DAQmx_AI_Microphone_Sensitivity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__sound__pressure__microphone_1ga15e671dd4ed45847774317773a399a0c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__sound__pressure__microphone_1ga15e671dd4ed45847774317773a399a0c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Microphone_SensitivityRemarksData TypeDescriptionRestrictionsfloat64Specifies the sensitivity of the microphone. This value is in mV/Pa. Refer to the sensor documentation to determine this value.You can get/set/reset this property using:DAQmxGetAIMicrophoneSensitivityDAQmxSetAIMicroph

### DAQmx_AI_Microphone_Sensitivity

#### Syntax

DAQmx_AI_Microphone_Sensitivity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the sensitivity of the microphone. This value is in mV/Pa. Refer to the sensor documentation to determine this value. |  |

You can get/set/reset this property using:

- [DAQmxGetAIMicrophoneSensitivity](group__ni-daqmx__c__functions__property__manipulation__getter_1gaca49c3636d3909ed5f1e23466010fb85.html)
- [DAQmxSetAIMicrophoneSensitivity](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3e0a93df3b9c219b311df2ae81daf2f3.html)
- [DAQmxResetAIMicrophoneSensitivity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga70e0ac076360cca36f3fa516184501fd.html)

Parent topic:

Microphone

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__strain.html language=enus -->
## TOPIC 01563: Strain

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__strain.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__strain.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsStrain GageGroup membersNameDescriptionDAQmx_AI_StrainGage_ForceReadFromChanDAQmx_AI_Strain_UnitsAttachmentsNone

### Strain

#### Groups

- Strain Gage

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_StrainGage_ForceReadFromChan |  |
| DAQmx_AI_Strain_Units |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__strain_1ga0a0ab0a0f76b8742a206e899ca93ace2.html language=enus -->
## TOPIC 01564: DAQmx_AI_StrainGage_ForceReadFromChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__strain_1ga0a0ab0a0f76b8742a206e899ca93ace2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__strain_1ga0a0ab0a0f76b8742a206e899ca93ace2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_StrainGage_ForceReadFromChanRemarksData TypeDescriptionRestrictionsbool32Specifies whether the data is returned by an NI-DAQmx Read function when set on a raw strain channel that is part of a rosette configuration.You can get/set/reset this property using:DAQmxGetAIStrainGageForceRead

### DAQmx_AI_StrainGage_ForceReadFromChan

#### Syntax

DAQmx_AI_StrainGage_ForceReadFromChan

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether the data is returned by an NI-DAQmx Read function when set on a raw strain channel that is part of a rosette configuration. |  |

You can get/set/reset this property using:

- [DAQmxGetAIStrainGageForceReadFromChan](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2fc44ec374fd0447b7e06787967336d4.html)
- [DAQmxSetAIStrainGageForceReadFromChan](group__ni-daqmx__c__functions__property__manipulation__setter_1gab0bc640849200457e871ae5f0f5b2f42.html)
- [DAQmxResetAIStrainGageForceReadFromChan](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga2ec5192229812b8d9827e416a2065e22.html)

Parent topic:

Strain

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__strain_1ga0ae44da6e4a20d1fcdb08034b6c74d8e.html language=enus -->
## TOPIC 01565: DAQmx_AI_Strain_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__strain_1ga0ae44da6e4a20d1fcdb08034b6c74d8e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__strain_1ga0ae44da6e4a20d1fcdb08034b6c74d8e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Strain_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return strain measurements from the channel.Valid valuesDAQmx_Val_Strain10299Strain.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select this value, you must specify a custom s

### DAQmx_AI_Strain_Units

#### Syntax

DAQmx_AI_Strain_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return strain measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Strain | 10299 | Strain. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAIStrainUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga5ec236c289f0a74b944249d28c715bb7.html)
- [DAQmxSetAIStrainUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1gadd27ff12e16975ac52c0238454a89b33.html)
- [DAQmxResetAIStrainUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae343062d8e39441690de1a21fe1e2dc6.html)

Parent topic:

Strain

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__strain__strain__gage_1gaf03fd6012b19835d3977c0307e1d3520.html language=enus -->
## TOPIC 01566: DAQmx_AI_StrainGage_GageFactor

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__strain__strain__gage_1gaf03fd6012b19835d3977c0307e1d3520.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__strain__strain__gage_1gaf03fd6012b19835d3977c0307e1d3520.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_StrainGage_GageFactorRemarksData TypeDescriptionRestrictionsfloat64Specifies the sensitivity of the strain gage. Gage factor relates the change in electrical resistance to the change in strain. Refer to the sensor documentation for this value.You can get/set/reset this property using:

### DAQmx_AI_StrainGage_GageFactor

#### Syntax

DAQmx_AI_StrainGage_GageFactor

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the sensitivity of the strain gage. Gage factor relates the change in electrical resistance to the change in strain. Refer to the sensor documentation for this value. |  |

You can get/set/reset this property using:

- [DAQmxGetAIStrainGageGageFactor](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8281c20c4f980372d3a414f71bafb5ec.html)
- [DAQmxSetAIStrainGageGageFactor](group__ni-daqmx__c__functions__property__manipulation__setter_1gafae1c9076d9d2a27287d324a3dea09aa.html)
- [DAQmxResetAIStrainGageGageFactor](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga75df02cc420b37a3bfe4555240655546.html)

Parent topic:

Strain Gage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__teds.html language=enus -->
## TOPIC 01567: TEDS

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__teds.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__teds.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Is_TEDSDAQmx_AI_TEDS_UnitsAttachmentsNone

### TEDS

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Is_TEDS |  |
| DAQmx_AI_TEDS_Units |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__teds_1gad84e727bd84654977d1557b00207a3bc.html language=enus -->
## TOPIC 01568: DAQmx_AI_Is_TEDS

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__teds_1gad84e727bd84654977d1557b00207a3bc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__teds_1gad84e727bd84654977d1557b00207a3bc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Is_TEDSRemarksData TypeDescriptionRestrictionsbool32Indicates if the virtual channel was initialized using a TEDS bitstream from the corresponding physical channel.Not SettableYou can get this property using:DAQmxGetAIIsTEDS

### DAQmx_AI_Is_TEDS

#### Syntax

DAQmx_AI_Is_TEDS

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the virtual channel was initialized using a TEDS bitstream from the corresponding physical channel. | Not Settable |

You can get this property using:

- [DAQmxGetAIIsTEDS](group__ni-daqmx__c__functions__property__manipulation__getter_1ga856bed561c64d93fa09d3267c3477fb2.html)

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__teds_1gae87cd5ce681014be7d72a6250f7fb38c.html language=enus -->
## TOPIC 01569: DAQmx_AI_TEDS_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__teds_1gae87cd5ce681014be7d72a6250f7fb38c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__teds_1gae87cd5ce681014be7d72a6250f7fb38c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_TEDS_UnitsRemarksData TypeDescriptionRestrictionschar*Indicates the units defined by TEDS information associated with the channel.Not SettableYou can get this property using:DAQmxGetAITEDSUnits

### DAQmx_AI_TEDS_Units

#### Syntax

DAQmx_AI_TEDS_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the units defined by TEDS information associated with the channel. | Not Settable |

You can get this property using:

- [DAQmxGetAITEDSUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gae912ac1ba05bb8247ea52ac21605d101.html)

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature.html language=enus -->
## TOPIC 01570: Temperature

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedRTDThermistorThermocoupleGroup membersNameDescriptionDAQmx_AI_Temp_UnitsAttachmentsNone

### Temperature

#### Groups

- Advanced
- RTD
- Thermistor
- Thermocouple

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Temp_Units |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature_1ga9785a5b9f9606fc85b6639101dcaa92a.html language=enus -->
## TOPIC 01571: DAQmx_AI_Temp_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature_1ga9785a5b9f9606fc85b6639101dcaa92a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature_1ga9785a5b9f9606fc85b6639101dcaa92a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Temp_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return temperature measurements from the channel.Valid valuesDAQmx_Val_DegC10143Degrees Celsius.DAQmx_Val_DegF10144Degrees Fahrenheit.DAQmx_Val_Kelvins10325Kelvins.DAQmx_Val_DegR10145Degrees Rankine.DA

### DAQmx_AI_Temp_Units

#### Syntax

DAQmx_AI_Temp_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return temperature measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_DegC | 10143 | Degrees Celsius. |
| DAQmx_Val_DegF | 10144 | Degrees Fahrenheit. |
| DAQmx_Val_Kelvins | 10325 | Kelvins. |
| DAQmx_Val_DegR | 10145 | Degrees Rankine. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAITempUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga99a2a34de179d6c6384c6f8ba7e705be.html)
- [DAQmxSetAITempUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3f49107889eacd8db4aa402c97edd8b9.html)
- [DAQmxResetAITempUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaba4ba05cfdab39ce1034a8a4fc02ba7c.html)

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__advanced.html language=enus -->
## TOPIC 01572: Advanced

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__advanced.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_ForceReadFromChanAttachmentsNone

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_ForceReadFromChan |  |

#### Attachments

None

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__advanced_1ga911d885c01d16a7f7ea5519bf283fb57.html language=enus -->
## TOPIC 01573: DAQmx_AI_ForceReadFromChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__advanced_1ga911d885c01d16a7f7ea5519bf283fb57.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__advanced_1ga911d885c01d16a7f7ea5519bf283fb57.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_ForceReadFromChanRemarksData TypeDescriptionRestrictionsbool32Specifies whether to read from the channel if it is a cold-junction compensation channel. By default, an NI-DAQmx Read function does not return data from cold-junction compensation channels. Setting this property to TRUE fo

### DAQmx_AI_ForceReadFromChan

#### Syntax

DAQmx_AI_ForceReadFromChan

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to read from the channel if it is a cold-junction compensation channel. By default, an NI-DAQmx Read function does not return data from cold-junction compensation channels. Setting this property to TRUE forces read operations to return the cold-junction compensation channel data with the other channels in the task. |  |

You can get/set/reset this property using:

- [DAQmxGetAIForceReadFromChan](group__ni-daqmx__c__functions__property__manipulation__getter_1ga45e34aa51463421ed9d1b1ecc92f435e.html)
- [DAQmxSetAIForceReadFromChan](group__ni-daqmx__c__functions__property__manipulation__setter_1ga373c6b0d5ec0d2745e9c8901c185bb4d.html)
- [DAQmxResetAIForceReadFromChan](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga7b311763dbe3f46a0f6d50d438d9d21d.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd.html language=enus -->
## TOPIC 01574: RTD

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCustomGroup membersNameDescriptionDAQmx_AI_RTD_R0DAQmx_AI_RTD_TypeAttachmentsNone

### RTD

#### Groups

- Custom

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_RTD_R0 |  |
| DAQmx_AI_RTD_Type |  |

#### Attachments

None

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd_1ga078f1cbaf64c8b346131522a53600f55.html language=enus -->
## TOPIC 01575: DAQmx_AI_RTD_R0

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd_1ga078f1cbaf64c8b346131522a53600f55.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd_1ga078f1cbaf64c8b346131522a53600f55.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_RTD_R0RemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the sensor resistance at 0 deg C. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value.You can get/set/reset this property using:DAQmxGetAIRTDR0DAQmxSetAIRT

### DAQmx_AI_RTD_R0

#### Syntax

DAQmx_AI_RTD_R0

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the sensor resistance at 0 deg C. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value. |  |

You can get/set/reset this property using:

- [DAQmxGetAIRTDR0](group__ni-daqmx__c__functions__property__manipulation__getter_1gad0d9b9f06593b1270f7c79fa3350b0af.html)
- [DAQmxSetAIRTDR0](group__ni-daqmx__c__functions__property__manipulation__setter_1gafd6a954c58ce29702f3d610359de0425.html)
- [DAQmxResetAIRTDR0](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafd7879823428c6a943f6d603286a28ab.html)

Parent topic:

RTD

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd__custom.html language=enus -->
## TOPIC 01576: Custom

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd__custom.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__rtd__custom.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_RTD_ADAQmx_AI_RTD_BDAQmx_AI_RTD_CAttachmentsNone

### Custom

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_RTD_A |  |
| DAQmx_AI_RTD_B |  |
| DAQmx_AI_RTD_C |  |

#### Attachments

None

Parent topic:

RTD

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor.html language=enus -->
## TOPIC 01577: Thermistor

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Thrmstr_ADAQmx_AI_Thrmstr_BDAQmx_AI_Thrmstr_CDAQmx_AI_Thrmstr_R1AttachmentsNone

### Thermistor

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Thrmstr_A |  |
| DAQmx_AI_Thrmstr_B |  |
| DAQmx_AI_Thrmstr_C |  |
| DAQmx_AI_Thrmstr_R1 |  |

#### Attachments

None

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1ga4667458ce28248468e504edb0def53b8.html language=enus -->
## TOPIC 01578: DAQmx_AI_Thrmstr_B

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1ga4667458ce28248468e504edb0def53b8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1ga4667458ce28248468e504edb0def53b8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Thrmstr_BRemarksData TypeDescriptionRestrictionsfloat64Specifies the 'B' constant of the Steinhart-Hart thermistor equation.You can get/set/reset this property using:DAQmxGetAIThrmstrBDAQmxSetAIThrmstrBDAQmxResetAIThrmstrB

### DAQmx_AI_Thrmstr_B

#### Syntax

DAQmx_AI_Thrmstr_B

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the 'B' constant of the Steinhart-Hart thermistor equation. |  |

You can get/set/reset this property using:

- [DAQmxGetAIThrmstrB](group__ni-daqmx__c__functions__property__manipulation__getter_1ga73cbc68f2ab86548ff2bb5e72847a4c9.html)
- [DAQmxSetAIThrmstrB](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1d1b783d442fcfc0e9708ac9c4704eeb.html)
- [DAQmxResetAIThrmstrB](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8826246513ec5d7be4d84d0ee650c720.html)

Parent topic:

Thermistor

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1ga643d647fbfb9e58af7de3152b10100db.html language=enus -->
## TOPIC 01579: DAQmx_AI_Thrmstr_A

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1ga643d647fbfb9e58af7de3152b10100db.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1ga643d647fbfb9e58af7de3152b10100db.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Thrmstr_ARemarksData TypeDescriptionRestrictionsfloat64Specifies the 'A' constant of the Steinhart-Hart thermistor equation.You can get/set/reset this property using:DAQmxGetAIThrmstrADAQmxSetAIThrmstrADAQmxResetAIThrmstrA

### DAQmx_AI_Thrmstr_A

#### Syntax

DAQmx_AI_Thrmstr_A

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the 'A' constant of the Steinhart-Hart thermistor equation. |  |

You can get/set/reset this property using:

- [DAQmxGetAIThrmstrA](group__ni-daqmx__c__functions__property__manipulation__getter_1gacde9fd4f2abae2709e7b088258285bd4.html)
- [DAQmxSetAIThrmstrA](group__ni-daqmx__c__functions__property__manipulation__setter_1ga8f8984cda12f32ee44100591806e78b9.html)
- [DAQmxResetAIThrmstrA](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae5ba8518010397e0cac9c8d81b6f214d.html)

Parent topic:

Thermistor

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1gaaec6e9dae7f5767a7589701f5e7cd810.html language=enus -->
## TOPIC 01580: DAQmx_AI_Thrmstr_R1

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1gaaec6e9dae7f5767a7589701f5e7cd810.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__thermistor_1gaaec6e9dae7f5767a7589701f5e7cd810.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Thrmstr_R1RemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the value of the reference resistor for the thermistor if you use voltage excitation. NI-DAQmx ignores this value for current excitation.You can get/set/reset this property using:DAQmxGetAIThrmstrR1DAQmxSetAIThr

### DAQmx_AI_Thrmstr_R1

#### Syntax

DAQmx_AI_Thrmstr_R1

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the value of the reference resistor for the thermistor if you use voltage excitation. NI-DAQmx ignores this value for current excitation. |  |

You can get/set/reset this property using:

- [DAQmxGetAIThrmstrR1](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2ed8caa2257a6af184be58b284bf4c7a.html)
- [DAQmxSetAIThrmstrR1](group__ni-daqmx__c__functions__property__manipulation__setter_1gace5715a33129b297900291f457602511.html)
- [DAQmxResetAIThrmstrR1](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga1da74133aea44035f06af6aec46c816a.html)

Parent topic:

Thermistor

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1ga26f52ec3ca82176fcd47bb9edf661cfb.html language=enus -->
## TOPIC 01581: DAQmx_AI_Thrmcpl_Type

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1ga26f52ec3ca82176fcd47bb9edf661cfb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1ga26f52ec3ca82176fcd47bb9edf661cfb.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Thrmcpl_TypeRemarksData TypeDescriptionRestrictionsint32Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range.Valid valuesDAQmx_Val_J_Type_TC10072J-type thermocouple.DAQmx_Val_K_Type_TC10073K-type thermocouple.DAQmx

### DAQmx_AI_Thrmcpl_Type

#### Syntax

DAQmx_AI_Thrmcpl_Type

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_J_Type_TC | 10072 | J-type thermocouple. |
| DAQmx_Val_K_Type_TC | 10073 | K-type thermocouple. |
| DAQmx_Val_N_Type_TC | 10077 | N-type thermocouple. |
| DAQmx_Val_R_Type_TC | 10082 | R-type thermocouple. |
| DAQmx_Val_S_Type_TC | 10085 | S-type thermocouple. |
| DAQmx_Val_T_Type_TC | 10086 | T-type thermocouple. |
| DAQmx_Val_B_Type_TC | 10047 | B-type thermocouple. |
| DAQmx_Val_E_Type_TC | 10055 | E-type thermocouple. |
| DAQmx_Val_A_Type_TC | 16208 | A-type thermocouple. |
| DAQmx_Val_C_Type_TC | 16209 | C-type thermocouple. |

You can get/set/reset this property using:

- [DAQmxGetAIThrmcplType](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8dc369b5ceddc7313617c3f420981aac.html)
- [DAQmxSetAIThrmcplType](group__ni-daqmx__c__functions__property__manipulation__setter_1ga118ceb0cb0696b2c2c38f035059643a0.html)
- [DAQmxResetAIThrmcplType](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae914253e359f2a69627b5c7793d6f27e.html)

Parent topic:

Thermocouple

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1ga8300f6f566424c3d599e076e968cfc04.html language=enus -->
## TOPIC 01582: DAQmx_AI_Thrmcpl_ScaleType

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1ga8300f6f566424c3d599e076e968cfc04.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1ga8300f6f566424c3d599e076e968cfc04.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Thrmcpl_ScaleTypeRemarksData TypeDescriptionRestrictionsint32Specifies the method or equation form that the thermocouple scale uses.Valid valuesDAQmx_Val_Polynomial10449Scale values by using an Nth order polynomial equation.DAQmx_Val_Table10450Map an array of prescaled values to an ar

### DAQmx_AI_Thrmcpl_ScaleType

#### Syntax

DAQmx_AI_Thrmcpl_ScaleType

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the method or equation form that the thermocouple scale uses. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |
| DAQmx_Val_Table | 10450 | Map an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. |

You can get/set/reset this property using:

- [DAQmxGetAIThrmcplScaleType](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2521ec9aa853a4df26aa586f965e1bc1.html)
- [DAQmxSetAIThrmcplScaleType](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa0140b4f3429ef83d13b92ca88d1adb8.html)
- [DAQmxResetAIThrmcplScaleType](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab29c197a0f0d96cb7f712eb14e4b6ae0.html)

Parent topic:

Thermocouple

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1gae8253eb86d6788435d146dd35d64d0ab.html language=enus -->
## TOPIC 01583: DAQmx_AI_Thrmcpl_CJCSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1gae8253eb86d6788435d146dd35d64d0ab.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__temperature__thermocouple_1gae8253eb86d6788435d146dd35d64d0ab.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Thrmcpl_CJCSrcRemarksData TypeDescriptionRestrictionsint32Indicates the source of cold-junction compensation.Not SettableValid valuesDAQmx_Val_BuiltIn10200Use a cold-junction compensation channel built into the terminal block.DAQmx_Val_ConstVal10116You must specify the cold-junction t

### DAQmx_AI_Thrmcpl_CJCSrc

#### Syntax

DAQmx_AI_Thrmcpl_CJCSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the source of cold-junction compensation. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_BuiltIn | 10200 | Use a cold-junction compensation channel built into the terminal block. |
| DAQmx_Val_ConstVal | 10116 | You must specify the cold-junction temperature. |
| DAQmx_Val_Chan | 10113 | Use a channel for cold-junction compensation. |

You can get this property using:

- [DAQmxGetAIThrmcplCJCSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1d9232b14f8f1a0a2343460ed30c5ebd.html)

Parent topic:

Thermocouple

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__torque.html language=enus -->
## TOPIC 01584: Torque

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__torque.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__torque.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Torque_UnitsAttachmentsNone

### Torque

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Torque_Units |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__velocity.html language=enus -->
## TOPIC 01585: Velocity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__velocity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__velocity.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsIEPE SensorGroup membersNameDescriptionDAQmx_AI_Velocity_UnitsAttachmentsNone

### Velocity

#### Groups

- IEPE Sensor

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Velocity_Units |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor.html language=enus -->
## TOPIC 01586: IEPE Sensor

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AI_Velocity_IEPESensor_SensitivityDAQmx_AI_Velocity_IEPESensor_SensitivityUnitsDAQmx_AI_Velocity_IEPESensor_dBRefAttachmentsNone

### IEPE Sensor

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Velocity_IEPESensor_Sensitivity |  |
| DAQmx_AI_Velocity_IEPESensor_SensitivityUnits |  |
| DAQmx_AI_Velocity_IEPESensor_dBRef |  |

#### Attachments

None

Parent topic:

Velocity

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor_1gab24689ed3e0d44ca34446c462cee8e81.html language=enus -->
## TOPIC 01587: DAQmx_AI_Velocity_IEPESensor_Sensitivity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor_1gab24689ed3e0d44ca34446c462cee8e81.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor_1gab24689ed3e0d44ca34446c462cee8e81.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Velocity_IEPESensor_SensitivityRemarksData TypeDescriptionRestrictionsfloat64Specifies the sensitivity of the IEPE velocity sensor connected to the channel. Specify this value in the unit indicated by Sensitivity Units.You can get/set/reset this property using:DAQmxGetAIVelocityIEPESe

### DAQmx_AI_Velocity_IEPESensor_Sensitivity

#### Syntax

DAQmx_AI_Velocity_IEPESensor_Sensitivity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the sensitivity of the IEPE velocity sensor connected to the channel. Specify this value in the unit indicated by Sensitivity Units. |  |

You can get/set/reset this property using:

- [DAQmxGetAIVelocityIEPESensorSensitivity](group__ni-daqmx__c__functions__property__manipulation__getter_1gab1e29c90e76435b8346b759f95c8da71.html)
- [DAQmxSetAIVelocityIEPESensorSensitivity](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa74cc2e21be0cc6393da6e0753a92399.html)
- [DAQmxResetAIVelocityIEPESensorSensitivity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga16e18e1fa131f78f0fd5f1d135d52f1b.html)

Parent topic:

IEPE Sensor

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor_1gadcf1ef30e3dc0cea36c43f875aadcaf7.html language=enus -->
## TOPIC 01588: DAQmx_AI_Velocity_IEPESensor_dBRef

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor_1gadcf1ef30e3dc0cea36c43f875aadcaf7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__velocity__iepe__sensor_1gadcf1ef30e3dc0cea36c43f875aadcaf7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Velocity_IEPESensor_dBRefRemarksData TypeDescriptionRestrictionsfloat64Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.You can get/set/reset this property using:D

### DAQmx_AI_Velocity_IEPESensor_dBRef

#### Syntax

DAQmx_AI_Velocity_IEPESensor_dBRef

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. |  |

You can get/set/reset this property using:

- [DAQmxGetAIVelocityIEPESensordBRef](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7ff9218a13f10330a003f4e0b0d8c401.html)
- [DAQmxSetAIVelocityIEPESensordBRef](group__ni-daqmx__c__functions__property__manipulation__setter_1gaad4f1cdaf66ba2beefc896b43039dc87.html)
- [DAQmxResetAIVelocityIEPESensordBRef](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga5c5e41d859927ddcc89aa1dd58bdce02.html)

Parent topic:

IEPE Sensor

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__voltage.html language=enus -->
## TOPIC 01589: Voltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__voltage.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAC RMS VoltageGroup membersNameDescriptionDAQmx_AI_Voltage_UnitsDAQmx_AI_Voltage_dBRefAttachmentsNone

### Voltage

#### Groups

- AC RMS Voltage

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AI_Voltage_Units |  |
| DAQmx_AI_Voltage_dBRef |  |

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__input__voltage__ac__rms__voltage_1gac159bba2b5d73c2e09af05cc4656b549.html language=enus -->
## TOPIC 01590: DAQmx_AI_Voltage_ACRMS_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__input__voltage__ac__rms__voltage_1gac159bba2b5d73c2e09af05cc4656b549.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__input__voltage__ac__rms__voltage_1gac159bba2b5d73c2e09af05cc4656b549.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AI_Voltage_ACRMS_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return voltage RMS measurements from the channel.Valid valuesDAQmx_Val_Volts10348Volts.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select this value, you must specify

### DAQmx_AI_Voltage_ACRMS_Units

#### Syntax

DAQmx_AI_Voltage_ACRMS_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return voltage RMS measurements from the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Volts | 10348 | Volts. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| DAQmx_Val_FromTEDS | 12516 | Units defined by TEDS information associated with the channel. |

You can get/set/reset this property using:

- [DAQmxGetAIVoltageACRMSUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gafdba1a03f292715be68b1caecab7b92d.html)
- [DAQmxSetAIVoltageACRMSUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga600aca961ad8dacc474571aa7064e05c.html)
- [DAQmxResetAIVoltageACRMSUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8f926c3410ad97b111c3301f45b35461.html)

Parent topic:

AC RMS Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output.html language=enus -->
## TOPIC 01591: Analog Output

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCurrentFunction GenerationGeneral PropertiesVoltageGroup membersNameDescriptionDAQmx_AO_CustomScaleNameDAQmx_AO_MaxDAQmx_AO_MinDAQmx_AO_OutputTypeAttachmentsNone

### Analog Output

#### Groups

- Current
- Function Generation
- General Properties
- Voltage

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_CustomScaleName |  |
| DAQmx_AO_Max |  |
| DAQmx_AO_Min |  |
| DAQmx_AO_OutputType |  |

#### Attachments

None

Parent topic:

Channel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output_1ga5bce267d88e4c455bd99d0a7ab497f44.html language=enus -->
## TOPIC 01592: DAQmx_AO_Min

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output_1ga5bce267d88e4c455bd99d0a7ab497f44.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output_1ga5bce267d88e4c455bd99d0a7ab497f44.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_MinRemarksData TypeDescriptionRestrictionsfloat64Specifies the minimum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value smaller than the minimum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value t

### DAQmx_AO_Min

#### Syntax

DAQmx_AO_Min

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the minimum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value smaller than the minimum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a larger value if other task settings restrict the device from generating the desired minimum. |  |

You can get/set/reset this property using:

- [DAQmxGetAOMin](group__ni-daqmx__c__functions__property__manipulation__getter_1gab58c4e5064b69d75eff12bb53d120629.html)
- [DAQmxSetAOMin](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3aa0dcffbd048f1bbc829df27489b168.html)
- [DAQmxResetAOMin](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga7e843e9f0621ab247a9acf2e02553eae.html)

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output_1gac74e714dd607711114b460c05722fe5a.html language=enus -->
## TOPIC 01593: DAQmx_AO_Max

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output_1gac74e714dd607711114b460c05722fe5a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output_1gac74e714dd607711114b460c05722fe5a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_MaxRemarksData TypeDescriptionRestrictionsfloat64Specifies the maximum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value larger than the maximum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to

### DAQmx_AO_Max

#### Syntax

DAQmx_AO_Max

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the maximum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value larger than the maximum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a smaller value if other task settings restrict the device from generating the desired maximum. |  |

You can get/set/reset this property using:

- [DAQmxGetAOMax](group__ni-daqmx__c__functions__property__manipulation__getter_1ga15adff621d3e018feddb96176f09af4b.html)
- [DAQmxSetAOMax](group__ni-daqmx__c__functions__property__manipulation__setter_1ga2a3716a8350f36c4ca455c502092d6e3.html)
- [DAQmxResetAOMax](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga49af779deb2ce551622fb9a045f5ff19.html)

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__current.html language=enus -->
## TOPIC 01594: Current

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__current.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__current.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_Current_UnitsAttachmentsNone

### Current

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_Current_Units |  |

#### Attachments

None

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__current_1ga45ee764d81b117eca078d80a0087b6fb.html language=enus -->
## TOPIC 01595: DAQmx_AO_Current_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__current_1ga45ee764d81b117eca078d80a0087b6fb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__current_1ga45ee764d81b117eca078d80a0087b6fb.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_Current_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies in what units to generate current on the channel. Write data to the channel in the units you select.Valid valuesDAQmx_Val_Amps10342Amperes.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select thi

### DAQmx_AO_Current_Units

#### Syntax

DAQmx_AO_Current_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies in what units to generate current on the channel. Write data to the channel in the units you select. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Amps | 10342 | Amperes. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| DAQmx_Val_FromTEDS | 12516 | Units defined by TEDS information associated with the channel. |

You can get/set/reset this property using:

- [DAQmxGetAOCurrentUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gab6be3d8cc55212409db1df496541a45f.html)
- [DAQmxSetAOCurrentUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1gae2625e97f51c7ced1281c62832aa3a89.html)
- [DAQmxResetAOCurrentUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga63a4f9efdd38e7747cf8dba1d82604f0.html)

Parent topic:

Current

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__function__generation.html language=enus -->
## TOPIC 01596: Function Generation

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__function__generation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__function__generation.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsModulationSquareGroup membersNameDescriptionDAQmx_AO_FuncGen_AmplitudeDAQmx_AO_FuncGen_FreqDAQmx_AO_FuncGen_OffsetDAQmx_AO_FuncGen_StartPhaseDAQmx_AO_FuncGen_TypeAttachmentsNone

### Function Generation

#### Groups

- Modulation
- Square

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_FuncGen_Amplitude |  |
| DAQmx_AO_FuncGen_Freq |  |
| DAQmx_AO_FuncGen_Offset |  |
| DAQmx_AO_FuncGen_StartPhase |  |
| DAQmx_AO_FuncGen_Type |  |

#### Attachments

None

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__function__generation_1ga1c9a3c6580e5426cd133379665a1c73b.html language=enus -->
## TOPIC 01597: DAQmx_AO_FuncGen_StartPhase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__function__generation_1ga1c9a3c6580e5426cd133379665a1c73b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__function__generation_1ga1c9a3c6580e5426cd133379665a1c73b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_FuncGen_StartPhaseRemarksData TypeDescriptionRestrictionsfloat64Specifies the starting phase in degrees of the waveform to generate.You can get/set/reset this property using:DAQmxGetAOFuncGenStartPhaseDAQmxSetAOFuncGenStartPhaseDAQmxResetAOFuncGenStartPhase

### DAQmx_AO_FuncGen_StartPhase

#### Syntax

DAQmx_AO_FuncGen_StartPhase

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the starting phase in degrees of the waveform to generate. |  |

You can get/set/reset this property using:

- [DAQmxGetAOFuncGenStartPhase](group__ni-daqmx__c__functions__property__manipulation__getter_1gad9e776ea0d212266935790e236412c8a.html)
- [DAQmxSetAOFuncGenStartPhase](group__ni-daqmx__c__functions__property__manipulation__setter_1ga87bd4685482b721d9111d505e5eed9f3.html)
- [DAQmxResetAOFuncGenStartPhase](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae0f155c1cbd8a1e2054c4ddf50a561a6.html)

Parent topic:

Function Generation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__function__generation_1ga1f82444adb1974661757f44654a7883a.html language=enus -->
## TOPIC 01598: DAQmx_AO_FuncGen_Offset

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__function__generation_1ga1f82444adb1974661757f44654a7883a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__function__generation_1ga1f82444adb1974661757f44654a7883a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_FuncGen_OffsetRemarksData TypeDescriptionRestrictionsfloat64Specifies the voltage offset of the waveform to generate.You can get/set/reset this property using:DAQmxGetAOFuncGenOffsetDAQmxSetAOFuncGenOffsetDAQmxResetAOFuncGenOffset

### DAQmx_AO_FuncGen_Offset

#### Syntax

DAQmx_AO_FuncGen_Offset

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the voltage offset of the waveform to generate. |  |

You can get/set/reset this property using:

- [DAQmxGetAOFuncGenOffset](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7d6c9f65dfc9108c959605d086f6b4aa.html)
- [DAQmxSetAOFuncGenOffset](group__ni-daqmx__c__functions__property__manipulation__setter_1ga12a9fdeeef928149c1db3e972f2c04dd.html)
- [DAQmxResetAOFuncGenOffset](group__ni-daqmx__c__functions__property__manipulation__resetter_1gad54c7a7bb17125c27c101799de19f7dd.html)

Parent topic:

Function Generation

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties.html language=enus -->
## TOPIC 01599: General Properties

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedDACFilterOutput ConfigurationGroup membersNoneAttachmentsNone

### General Properties

#### Groups

- Advanced
- DAC
- Filter
- Output Configuration

#### Group members

None

#### Attachments

None

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced.html language=enus -->
## TOPIC 01600: Advanced

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsData Transfer and MemoryDevice Scaling CoefficientsGainGroup membersNoneAttachmentsNone

### Advanced

#### Groups

- Data Transfer and Memory
- Device Scaling Coefficients
- Gain

#### Group members

None

#### Attachments

None

Parent topic:

General Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1ga66376606e9f3adb4abc32997318f8db4.html language=enus -->
## TOPIC 01601: DAQmx_AO_DataXferReqCond

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1ga66376606e9f3adb4abc32997318f8db4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1ga66376606e9f3adb4abc32997318f8db4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DataXferReqCondRemarksData TypeDescriptionRestrictionsint32Specifies under what condition to transfer data from the buffer to the onboard memory of the device.Valid valuesDAQmx_Val_OnBrdMemEmpty10235Transfer data to the device only when there is no data in the onboard memory of the de

### DAQmx_AO_DataXferReqCond

#### Syntax

DAQmx_AO_DataXferReqCond

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_OnBrdMemEmpty | 10235 | Transfer data to the device only when there is no data in the onboard memory of the device. |
| DAQmx_Val_OnBrdMemHalfFullOrLess | 10239 | Transfer data to the device any time the onboard memory is less than half full. |
| DAQmx_Val_OnBrdMemNotFull | 10242 | Transfer data to the device any time the onboard memory of the device is not full. |

You can get/set/reset this property using:

- [DAQmxGetAODataXferReqCond](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7f365359f423a3b662201df870777455.html)
- [DAQmxSetAODataXferReqCond](group__ni-daqmx__c__functions__property__manipulation__setter_1gae3336470e270fafc2e09aee5e28f8ba8.html)
- [DAQmxResetAODataXferReqCond](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga31fac83b043b7f619d667d963a757509.html)

Parent topic:

Data Transfer and Memory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1ga67d894bd8c5679fa48280a21e2845f34.html language=enus -->
## TOPIC 01602: DAQmx_AO_UseOnlyOnBrdMem

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1ga67d894bd8c5679fa48280a21e2845f34.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1ga67d894bd8c5679fa48280a21e2845f34.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_UseOnlyOnBrdMemRemarksData TypeDescriptionRestrictionsbool32Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs.Y

### DAQmx_AO_UseOnlyOnBrdMem

#### Syntax

DAQmx_AO_UseOnlyOnBrdMem

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. |  |

You can get/set/reset this property using:

- [DAQmxGetAOUseOnlyOnBrdMem](group__ni-daqmx__c__functions__property__manipulation__getter_1ga35299a2c5d7a26c7977450e945b90d72.html)
- [DAQmxSetAOUseOnlyOnBrdMem](group__ni-daqmx__c__functions__property__manipulation__setter_1gacec8d71a2d5185fc57f2921b3d57638a.html)
- [DAQmxResetAOUseOnlyOnBrdMem](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf93cef1c436ade4f3bee5570f5a4e9af.html)

Parent topic:

Data Transfer and Memory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gacb3d6ee64c4363f1e7bf596545092afb.html language=enus -->
## TOPIC 01603: DAQmx_AO_MemMapEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gacb3d6ee64c4363f1e7bf596545092afb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gacb3d6ee64c4363f1e7bf596545092afb.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_MemMapEnableRemarksData TypeDescriptionRestrictionsbool32Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space

### DAQmx_AO_MemMapEnable

#### Syntax

DAQmx_AO_MemMapEnable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |  |

You can get/set/reset this property using:

- [DAQmxGetAOMemMapEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1gab3dfd0fede406c89c34a1dba11f0714d.html)
- [DAQmxSetAOMemMapEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga769f67d2d9e5aa037458c65723a326a6.html)
- [DAQmxResetAOMemMapEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gad0bc5a70eb109714827b7109c357b6fe.html)

Parent topic:

Data Transfer and Memory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gad053a33160fedb8edcdeff188370a6b7.html language=enus -->
## TOPIC 01604: DAQmx_AO_UsbXferReqSize

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gad053a33160fedb8edcdeff188370a6b7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gad053a33160fedb8edcdeff188370a6b7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_UsbXferReqSizeRemarksData TypeDescriptionRestrictionsuInt32Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.You can get/set/reset this property using:DAQmxGetAOUsbXferReqS

### DAQmx_AO_UsbXferReqSize

#### Syntax

DAQmx_AO_UsbXferReqSize

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |  |

You can get/set/reset this property using:

- [DAQmxGetAOUsbXferReqSize](group__ni-daqmx__c__functions__property__manipulation__getter_1gae577892d8bf44c561fc4c3ad48295c28.html)
- [DAQmxSetAOUsbXferReqSize](group__ni-daqmx__c__functions__property__manipulation__setter_1gab69631cca38e3dc59fb1300d7753cb26.html)
- [DAQmxResetAOUsbXferReqSize](group__ni-daqmx__c__functions__property__manipulation__resetter_1gabd0f49e55c872c70b700fdac143a43a3.html)

Parent topic:

Data Transfer and Memory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gae6b297d6b3fd7e01ea1508478d221640.html language=enus -->
## TOPIC 01605: DAQmx_AO_UsbXferReqCount

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gae6b297d6b3fd7e01ea1508478d221640.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__data__transfer__and__memory_1gae6b297d6b3fd7e01ea1508478d221640.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_UsbXferReqCountRemarksData TypeDescriptionRestrictionsuInt32Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.You can get/set/reset this property using:DAQ

### DAQmx_AO_UsbXferReqCount

#### Syntax

DAQmx_AO_UsbXferReqCount

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |  |

You can get/set/reset this property using:

- [DAQmxGetAOUsbXferReqCount](group__ni-daqmx__c__functions__property__manipulation__getter_1ga95441a7dea26d5006dbefe14d901dfa5.html)
- [DAQmxSetAOUsbXferReqCount](group__ni-daqmx__c__functions__property__manipulation__setter_1gacb944810fe7045b015667d337fa7a509.html)
- [DAQmxResetAOUsbXferReqCount](group__ni-daqmx__c__functions__property__manipulation__resetter_1gac5b48163c979995c0ffdb3f1821b1e2e.html)

Parent topic:

Data Transfer and Memory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients.html language=enus -->
## TOPIC 01606: Device Scaling Coefficients

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_DevScalingCoeffDAQmx_AO_EnhancedImageRejectionEnableAttachmentsNone

### Device Scaling Coefficients

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_DevScalingCoeff |  |
| DAQmx_AO_EnhancedImageRejectionEnable |  |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients_1ga33b021ee08a33862afae748c9e5755ca.html language=enus -->
## TOPIC 01607: DAQmx_AO_EnhancedImageRejectionEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients_1ga33b021ee08a33862afae748c9e5755ca.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients_1ga33b021ee08a33862afae748c9e5755ca.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_EnhancedImageRejectionEnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection.You can get/set/reset this property using

### DAQmx_AO_EnhancedImageRejectionEnable

#### Syntax

DAQmx_AO_EnhancedImageRejectionEnable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio at the expense of degraded image rejection. |  |

You can get/set/reset this property using:

- [DAQmxGetAOEnhancedImageRejectionEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga34ec284f2c466dda1b32b09b4ae04fe0.html)
- [DAQmxSetAOEnhancedImageRejectionEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gad0761686a7e2ad8a9fed1c5031f45a29.html)
- [DAQmxResetAOEnhancedImageRejectionEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae638826738b9982924ecdea4ddf4ec6d.html)

Parent topic:

Device Scaling Coefficients

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients_1ga9718839889d6e4a4bb9c1ce6549fa3f6.html language=enus -->
## TOPIC 01608: DAQmx_AO_DevScalingCoeff

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients_1ga9718839889d6e4a4bb9c1ce6549fa3f6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__device__scaling__coefficients_1ga9718839889d6e4a4bb9c1ce6549fa3f6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DevScalingCoeffRemarksData TypeDescriptionRestrictionsfloat64*Indicates the coefficients of a linear equation that NI-DAQmx uses to scale values from a voltage to the native format of the device. Each element of the array corresponds to a term of the equation. The first element of the

### DAQmx_AO_DevScalingCoeff

#### Syntax

DAQmx_AO_DevScalingCoeff

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64* | Indicates the coefficients of a linear equation that NI-DAQmx uses to scale values from a voltage to the native format of the device. Each element of the array corresponds to a term of the equation. The first element of the array corresponds to the y-intercept, and the second element corresponds to the slope. Scaling coefficients do not account for any custom scales that may be applied to the channel. | Not Settable |

You can get this property using:

- [DAQmxGetAODevScalingCoeff](group__ni-daqmx__c__functions__property__manipulation__getter_1gad062b75812887587b737d924b245b5f0.html)

Parent topic:

Device Scaling Coefficients

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__gain.html language=enus -->
## TOPIC 01609: Gain

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__gain.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_GainAttachmentsNone

### Gain

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_Gain |  |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__gain_1ga8f6434fa9bcbf7f507d39399486dd8b8.html language=enus -->
## TOPIC 01610: DAQmx_AO_Gain

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__gain_1ga8f6434fa9bcbf7f507d39399486dd8b8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__advanced__gain_1ga8f6434fa9bcbf7f507d39399486dd8b8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_GainRemarksData TypeDescriptionRestrictionsfloat64Specifies in decibels the gain factor to apply to the channel.You can get/set/reset this property using:DAQmxGetAOGainDAQmxSetAOGainDAQmxResetAOGain

### DAQmx_AO_Gain

#### Syntax

DAQmx_AO_Gain

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in decibels the gain factor to apply to the channel. |  |

You can get/set/reset this property using:

- [DAQmxGetAOGain](group__ni-daqmx__c__functions__property__manipulation__getter_1ga3bf917a00d57a57b16036937541d0130.html)
- [DAQmxSetAOGain](group__ni-daqmx__c__functions__property__manipulation__setter_1gaf03464d0f8d2068cc567d5046ca60288.html)
- [DAQmxResetAOGain](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4c57cffb96ca8c69a83970c47b41d069.html)

Parent topic:

Gain

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac.html language=enus -->
## TOPIC 01611: DAC

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsOffset VoltageRangeReference VoltageGroup membersNameDescriptionDAQmx_AO_ResolutionDAQmx_AO_ResolutionUnitsAttachmentsNone

### DAC

#### Groups

- Offset Voltage
- Range
- Reference Voltage

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_Resolution |  |
| DAQmx_AO_ResolutionUnits |  |

#### Attachments

None

Parent topic:

General Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac_1gaae113c2907e18fb9a30ee187787366fa.html language=enus -->
## TOPIC 01612: DAQmx_AO_Resolution

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac_1gaae113c2907e18fb9a30ee187787366fa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac_1gaae113c2907e18fb9a30ee187787366fa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_ResolutionRemarksData TypeDescriptionRestrictionsfloat64Indicates the resolution of the digital-to-analog converter of the channel. This value is in the units you specify with Resolution Units.Not SettableYou can get this property using:DAQmxGetAOResolution

### DAQmx_AO_Resolution

#### Syntax

DAQmx_AO_Resolution

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Indicates the resolution of the digital-to-analog converter of the channel. This value is in the units you specify with Resolution Units. | Not Settable |

You can get this property using:

- [DAQmxGetAOResolution](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9c38dcb37bc3c74aec594887d0048c84.html)

Parent topic:

DAC

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac_1gaeef73e70a291908973770c07902934b9.html language=enus -->
## TOPIC 01613: DAQmx_AO_ResolutionUnits

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac_1gaeef73e70a291908973770c07902934b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac_1gaeef73e70a291908973770c07902934b9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_ResolutionUnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units of Resolution Value.Valid valuesDAQmx_Val_Bits10109Bits.You can get/set/reset this property using:DAQmxGetAOResolutionUnitsDAQmxSetAOResolutionUnitsDAQmxResetAOResolutionUnits

### DAQmx_AO_ResolutionUnits

#### Syntax

DAQmx_AO_ResolutionUnits

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units of Resolution Value. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Bits | 10109 | Bits. |

You can get/set/reset this property using:

- [DAQmxGetAOResolutionUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga29552b278f39b70a5525b44283a541a4.html)
- [DAQmxSetAOResolutionUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga5ff87dc92f516451298d622ce4cf6ed5.html)
- [DAQmxResetAOResolutionUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gac0b1aca643afd1104e67359b4a3d69a2.html)

Parent topic:

DAC

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage.html language=enus -->
## TOPIC 01614: Offset Voltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_DAC_Offset_ExtSrcDAQmx_AO_DAC_Offset_SrcDAQmx_AO_DAC_Offset_ValDAQmx_AO_ReglitchEnableAttachmentsNone

### Offset Voltage

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_DAC_Offset_ExtSrc |  |
| DAQmx_AO_DAC_Offset_Src |  |
| DAQmx_AO_DAC_Offset_Val |  |
| DAQmx_AO_ReglitchEnable |  |

#### Attachments

None

Parent topic:

DAC

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga083c48b2f2c0012684d9470de3b08337.html language=enus -->
## TOPIC 01615: DAQmx_AO_DAC_Offset_ExtSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga083c48b2f2c0012684d9470de3b08337.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga083c48b2f2c0012684d9470de3b08337.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Offset_ExtSrcRemarksData TypeDescriptionRestrictionschar*Specifies the source of the DAC offset voltage if Source is DAQmx_Val_External. The valid sources for this signal vary by device.You can get/set/reset this property using:DAQmxGetAODACOffsetExtSrcDAQmxSetAODACOffsetExtSrcDAQ

### DAQmx_AO_DAC_Offset_ExtSrc

#### Syntax

DAQmx_AO_DAC_Offset_ExtSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the source of the DAC offset voltage if Source is DAQmx_Val_External. The valid sources for this signal vary by device. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACOffsetExtSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2d928640f89889275d0172d806e39422.html)
- [DAQmxSetAODACOffsetExtSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1ga179f2a7d8de9195ceeb7039585bdb032.html)
- [DAQmxResetAODACOffsetExtSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga0dd16282b91dfac1e99facdbb3e29ad5.html)

Parent topic:

Offset Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga1fccfaa9cf211dc1922820a55ca13b1c.html language=enus -->
## TOPIC 01616: DAQmx_AO_DAC_Offset_Val

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga1fccfaa9cf211dc1922820a55ca13b1c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga1fccfaa9cf211dc1922820a55ca13b1c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Offset_ValRemarksData TypeDescriptionRestrictionsfloat64Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated.You can get/set/reset this property using:DAQmxGetAODACOffsetValDAQmxSetAODACOffsetValDAQmxReset

### DAQmx_AO_DAC_Offset_Val

#### Syntax

DAQmx_AO_DAC_Offset_Val

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in volts the value of the DAC offset voltage. To achieve best accuracy, the DAC offset value should be hand calibrated. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACOffsetVal](group__ni-daqmx__c__functions__property__manipulation__getter_1gac470d5755cb7983c7214e6837180ea47.html)
- [DAQmxSetAODACOffsetVal](group__ni-daqmx__c__functions__property__manipulation__setter_1ga69584dda8e3bf90a1d7e13fb0a7a83b0.html)
- [DAQmxResetAODACOffsetVal](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaac231f1acdb941e04456444675d175a4.html)

Parent topic:

Offset Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga46f2047ca719feeca63445b141b1cfd4.html language=enus -->
## TOPIC 01617: DAQmx_AO_ReglitchEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga46f2047ca719feeca63445b141b1cfd4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1ga46f2047ca719feeca63445b141b1cfd4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_ReglitchEnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to enable reglitching. The output of a DAC normally glitches whenever the DAC is updated with a new value. The amount of glitching differs from code to code and is generally largest at major code transitions.

### DAQmx_AO_ReglitchEnable

#### Syntax

DAQmx_AO_ReglitchEnable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to enable reglitching. The output of a DAC normally glitches whenever the DAC is updated with a new value. The amount of glitching differs from code to code and is generally largest at major code transitions. Reglitching generates uniform glitch energy at each code transition and provides for more uniform glitches. Uniform glitch energy makes it easier to filter out the noise introduced from glitching during spectrum analysis. |  |

You can get/set/reset this property using:

- [DAQmxGetAOReglitchEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8212230cae1fed955478523e0412394a.html)
- [DAQmxSetAOReglitchEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga80498f26021faa6e567cb90b11c3103b.html)
- [DAQmxResetAOReglitchEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga25027b76cc6cfdecf933611ee08d6ada.html)

Parent topic:

Offset Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1gaf7a6ff18a8ee616120e14139ac4b9eea.html language=enus -->
## TOPIC 01618: DAQmx_AO_DAC_Offset_Src

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1gaf7a6ff18a8ee616120e14139ac4b9eea.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__offset__voltage_1gaf7a6ff18a8ee616120e14139ac4b9eea.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Offset_SrcRemarksData TypeDescriptionRestrictionsint32Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC.Valid valuesDAQmx_Val_Internal10200Internal to the device.DAQmx_Val_External10167External to the device

### DAQmx_AO_DAC_Offset_Src

#### Syntax

DAQmx_AO_DAC_Offset_Src

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Internal | 10200 | Internal to the device. |
| DAQmx_Val_External | 10167 | External to the device. |

You can get/set/reset this property using:

- [DAQmxGetAODACOffsetSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1bf36877fccb302220bb9361d2c0fe96.html)
- [DAQmxSetAODACOffsetSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1ga5ab8907a1a1203939d81b4fb180142b5.html)
- [DAQmxResetAODACOffsetSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9c8d9d2ea1ab90295be18a67e8c113eb.html)

Parent topic:

Offset Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range.html language=enus -->
## TOPIC 01619: Range

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_DAC_Rng_HighDAQmx_AO_DAC_Rng_LowAttachmentsNone

### Range

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_DAC_Rng_High |  |
| DAQmx_AO_DAC_Rng_Low |  |

#### Attachments

None

Parent topic:

DAC

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range_1ga2c18254f32187fe078365f41e70140d5.html language=enus -->
## TOPIC 01620: DAQmx_AO_DAC_Rng_High

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range_1ga2c18254f32187fe078365f41e70140d5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range_1ga2c18254f32187fe078365f41e70140d5.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Rng_HighRemarksData TypeDescriptionRestrictionsfloat64Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.You can get/set/reset this property using:DAQmxGetAODACRn

### DAQmx_AO_DAC_Rng_High

#### Syntax

DAQmx_AO_DAC_Rng_High

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACRngHigh](group__ni-daqmx__c__functions__property__manipulation__getter_1ga941ce2abe8acd69ed361d3c2441d3602.html)
- [DAQmxSetAODACRngHigh](group__ni-daqmx__c__functions__property__manipulation__setter_1ga4c49f2e4685d6d78deacb7eccd721f3b.html)
- [DAQmxResetAODACRngHigh](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga46e982ed3ee81b398ec0bf35a37f0779.html)

Parent topic:

Range

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range_1ga4b5477aef6d2333cd603b9c21e71078a.html language=enus -->
## TOPIC 01621: DAQmx_AO_DAC_Rng_Low

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range_1ga4b5477aef6d2333cd603b9c21e71078a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__range_1ga4b5477aef6d2333cd603b9c21e71078a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Rng_LowRemarksData TypeDescriptionRestrictionsfloat64Specifies the lower limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.You can get/set/reset this property using:DAQmxGetAODACRng

### DAQmx_AO_DAC_Rng_Low

#### Syntax

DAQmx_AO_DAC_Rng_Low

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the lower limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACRngLow](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7dd7f7e2d5c897d3d4935a61a7215719.html)
- [DAQmxSetAODACRngLow](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1994d7bc5aae5da25075213141479c58.html)
- [DAQmxResetAODACRngLow](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf4d006d9f9bcab0a7b0ced0d8571658b.html)

Parent topic:

Range

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage.html language=enus -->
## TOPIC 01622: Reference Voltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_DAC_Ref_AllowConnToGndDAQmx_AO_DAC_Ref_ConnToGndDAQmx_AO_DAC_Ref_ExtSrcDAQmx_AO_DAC_Ref_SrcDAQmx_AO_DAC_Ref_ValAttachmentsNone

### Reference Voltage

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_DAC_Ref_AllowConnToGnd |  |
| DAQmx_AO_DAC_Ref_ConnToGnd |  |
| DAQmx_AO_DAC_Ref_ExtSrc |  |
| DAQmx_AO_DAC_Ref_Src |  |
| DAQmx_AO_DAC_Ref_Val |  |

#### Attachments

None

Parent topic:

DAC

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga1a49ca0394fa427a1cad23172c9836b3.html language=enus -->
## TOPIC 01623: DAQmx_AO_DAC_Ref_ExtSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga1a49ca0394fa427a1cad23172c9836b3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga1a49ca0394fa427a1cad23172c9836b3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Ref_ExtSrcRemarksData TypeDescriptionRestrictionschar*Specifies the source of the DAC reference voltage if Source is DAQmx_Val_External. The valid sources for this signal vary by device.You can get/set/reset this property using:DAQmxGetAODACRefExtSrcDAQmxSetAODACRefExtSrcDAQmxRese

### DAQmx_AO_DAC_Ref_ExtSrc

#### Syntax

DAQmx_AO_DAC_Ref_ExtSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the source of the DAC reference voltage if Source is DAQmx_Val_External. The valid sources for this signal vary by device. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACRefExtSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1gad03f13ba8aeb6eaded402f79ca55ce6f.html)
- [DAQmxSetAODACRefExtSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1ga40e31aac0707002a1be339e5fbda41ad.html)
- [DAQmxResetAODACRefExtSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga48ef2485ad4b934af08466a488a6a099.html)

Parent topic:

Reference Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga5bce500b699b598474e18d9f71752e54.html language=enus -->
## TOPIC 01624: DAQmx_AO_DAC_Ref_Val

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga5bce500b699b598474e18d9f71752e54.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga5bce500b699b598474e18d9f71752e54.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Ref_ValRemarksData TypeDescriptionRestrictionsfloat64Specifies in volts the value of the DAC reference voltage. This voltage determines the full-scale range of the DAC. Smaller reference voltages result in smaller ranges, but increased resolution.You can get/set/reset this propert

### DAQmx_AO_DAC_Ref_Val

#### Syntax

DAQmx_AO_DAC_Ref_Val

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in volts the value of the DAC reference voltage. This voltage determines the full-scale range of the DAC. Smaller reference voltages result in smaller ranges, but increased resolution. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACRefVal](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0f768d65e9cbdf86f8c51cc33afc85dc.html)
- [DAQmxSetAODACRefVal](group__ni-daqmx__c__functions__property__manipulation__setter_1ga75d7afd3dad3e88ad0706899a4f16fef.html)
- [DAQmxResetAODACRefVal](group__ni-daqmx__c__functions__property__manipulation__resetter_1gad55e53b809fdbd85fdfae370144654d6.html)

Parent topic:

Reference Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga7cdedf55ed230baea46f715a195686ee.html language=enus -->
## TOPIC 01625: DAQmx_AO_DAC_Ref_Src

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga7cdedf55ed230baea46f715a195686ee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1ga7cdedf55ed230baea46f715a195686ee.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Ref_SrcRemarksData TypeDescriptionRestrictionsint32Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC.Valid valuesDAQmx_Val_Internal10200Internal to the device.DAQmx_Val_External10167External to the device

### DAQmx_AO_DAC_Ref_Src

#### Syntax

DAQmx_AO_DAC_Ref_Src

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Internal | 10200 | Internal to the device. |
| DAQmx_Val_External | 10167 | External to the device. |

You can get/set/reset this property using:

- [DAQmxGetAODACRefSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4a39ae9412f17e42b670229b49d2dc2e.html)
- [DAQmxSetAODACRefSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1680e83c9b8ac9a0e97a120c61a9d3ca.html)
- [DAQmxResetAODACRefSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga59e84accb64d72db4d2098260d9be9d6.html)

Parent topic:

Reference Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1gad1b55e5953eff6a8e744eaea85de27f9.html language=enus -->
## TOPIC 01626: DAQmx_AO_DAC_Ref_AllowConnToGnd

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1gad1b55e5953eff6a8e744eaea85de27f9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1gad1b55e5953eff6a8e744eaea85de27f9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Ref_AllowConnToGndRemarksData TypeDescriptionRestrictionsbool32Specifies whether to allow grounding the internal DAC reference at run time. You must set this property to TRUE and set Source to DAQmx_Val_Internal before you can set Connect DAC Reference to Ground to TRUE.You can ge

### DAQmx_AO_DAC_Ref_AllowConnToGnd

#### Syntax

DAQmx_AO_DAC_Ref_AllowConnToGnd

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to allow grounding the internal DAC reference at run time. You must set this property to TRUE and set Source to DAQmx_Val_Internal before you can set Connect DAC Reference to Ground to TRUE. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACRefAllowConnToGnd](group__ni-daqmx__c__functions__property__manipulation__getter_1ga447d7c630d32df72f8f083cb99ff7396.html)
- [DAQmxSetAODACRefAllowConnToGnd](group__ni-daqmx__c__functions__property__manipulation__setter_1ga963eb1d61d22a0a0919be19b50288731.html)
- [DAQmxResetAODACRefAllowConnToGnd](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga86d25152a719e7e2c4ff06a1ddabdaca.html)

Parent topic:

Reference Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1gaf003a59c41ac84605c6b7bfe704ee139.html language=enus -->
## TOPIC 01627: DAQmx_AO_DAC_Ref_ConnToGnd

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1gaf003a59c41ac84605c6b7bfe704ee139.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__dac__reference__voltage_1gaf003a59c41ac84605c6b7bfe704ee139.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_DAC_Ref_ConnToGndRemarksData TypeDescriptionRestrictionsbool32Specifies whether to ground the internal DAC reference. Grounding the internal DAC reference has the effect of grounding all analog output channels and stopping waveform generation across all analog output channels regardle

### DAQmx_AO_DAC_Ref_ConnToGnd

#### Syntax

DAQmx_AO_DAC_Ref_ConnToGnd

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to ground the internal DAC reference. Grounding the internal DAC reference has the effect of grounding all analog output channels and stopping waveform generation across all analog output channels regardless of whether the channels belong to the current task. You can ground the internal DAC reference only when Source is DAQmx_Val_Internal and Allow Connecting DAC Reference to Ground at Runtime is TRUE. |  |

You can get/set/reset this property using:

- [DAQmxGetAODACRefConnToGnd](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa34655ef8e1bc2e8c71d67ba468643dc.html)
- [DAQmxSetAODACRefConnToGnd](group__ni-daqmx__c__functions__property__manipulation__setter_1gacb0b1e96184d69d40cff117c3e9798cc.html)
- [DAQmxResetAODACRefConnToGnd](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafab766693bb6f52e3ffaf9140f4287ab.html)

Parent topic:

Reference Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter.html language=enus -->
## TOPIC 01628: Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_FilterDelayDAQmx_AO_FilterDelayAdjustmentDAQmx_AO_FilterDelayUnitsAttachmentsNone

### Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_FilterDelay |  |
| DAQmx_AO_FilterDelayAdjustment |  |
| DAQmx_AO_FilterDelayUnits |  |

#### Attachments

None

Parent topic:

General Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1ga3a7c44e0c74acfa6e16a468e12d24963.html language=enus -->
## TOPIC 01629: DAQmx_AO_FilterDelayUnits

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1ga3a7c44e0c74acfa6e16a468e12d24963.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1ga3a7c44e0c74acfa6e16a468e12d24963.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_FilterDelayUnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units of Filter Delay and Filter Delay Adjustment.Valid valuesDAQmx_Val_Seconds10364Seconds.DAQmx_Val_SampleClkPeriods10286Sample Clock Periods.You can get/set/reset this property using:DAQmxGetAOFilterDelayUnit

### DAQmx_AO_FilterDelayUnits

#### Syntax

DAQmx_AO_FilterDelayUnits

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units of Filter Delay and Filter Delay Adjustment. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Seconds | 10364 | Seconds. |
| DAQmx_Val_SampleClkPeriods | 10286 | Sample Clock Periods. |

You can get/set/reset this property using:

- [DAQmxGetAOFilterDelayUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gadc142f0457256e77f6ea8159fee352e7.html)
- [DAQmxSetAOFilterDelayUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga688ad0fa22586e47f49859000e02de83.html)
- [DAQmxResetAOFilterDelayUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gacb221e259b3922af949b5053a2c818fd.html)

Parent topic:

Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1ga89f51fb07321a38f8c8cb5e2ed6c658a.html language=enus -->
## TOPIC 01630: DAQmx_AO_FilterDelayAdjustment

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1ga89f51fb07321a38f8c8cb5e2ed6c658a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1ga89f51fb07321a38f8c8cb5e2ed6c658a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_FilterDelayAdjustmentRemarksData TypeDescriptionRestrictionsfloat64Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by Filter Delay

### DAQmx_AO_FilterDelayAdjustment

#### Syntax

DAQmx_AO_FilterDelayAdjustment

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies an additional amount of time to wait between when the sample is written by the host device and when the sample is output by the DAC. This delay adjustment is in addition to the value indicated by Filter Delay. This delay adjustment is in the units you specify with Filter Delay Units. |  |

You can get/set/reset this property using:

- [DAQmxGetAOFilterDelayAdjustment](group__ni-daqmx__c__functions__property__manipulation__getter_1ga28cf5ef87dc174fe7b0e539f71cc2586.html)
- [DAQmxSetAOFilterDelayAdjustment](group__ni-daqmx__c__functions__property__manipulation__setter_1ga550b35196bf98bd860d9687f48ee4d36.html)
- [DAQmxResetAOFilterDelayAdjustment](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga5bd9a27e1eb7697cd738ff4a0789a828.html)

Parent topic:

Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1gab60d6ec926703b1a7161031c11636f78.html language=enus -->
## TOPIC 01631: DAQmx_AO_FilterDelay

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1gab60d6ec926703b1a7161031c11636f78.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__filter_1gab60d6ec926703b1a7161031c11636f78.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_FilterDelayRemarksData TypeDescriptionRestrictionsfloat64Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with Filter Delay Units.You can get/set/reset this property usin

### DAQmx_AO_FilterDelay

#### Syntax

DAQmx_AO_FilterDelay

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the amount of time between when the sample is written by the host device and when the sample is output by the DAC. This value is in the units you specify with Filter Delay Units. |  |

You can get/set/reset this property using:

- [DAQmxGetAOFilterDelay](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1bb25c7ee8a15d6203e3198d736bcb98.html)
- [DAQmxSetAOFilterDelay](group__ni-daqmx__c__functions__property__manipulation__setter_1ga539a6c5b8e6cdccbb794f1c36617d930.html)
- [DAQmxResetAOFilterDelay](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga05603ae5b9733f1f0ad3fe85f6c10d13.html)

Parent topic:

Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration.html language=enus -->
## TOPIC 01632: Output Configuration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_Common_Mode_OffsetDAQmx_AO_IdleOutputBehaviorDAQmx_AO_LoadImpedanceDAQmx_AO_OutputImpedanceDAQmx_AO_TermCfgAttachmentsNone

### Output Configuration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_Common_Mode_Offset |  |
| DAQmx_AO_IdleOutputBehavior |  |
| DAQmx_AO_LoadImpedance |  |
| DAQmx_AO_OutputImpedance |  |
| DAQmx_AO_TermCfg |  |

#### Attachments

None

Parent topic:

General Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga29821fa7449613f22133d7607eabd753.html language=enus -->
## TOPIC 01633: DAQmx_AO_Common_Mode_Offset

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga29821fa7449613f22133d7607eabd753.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga29821fa7449613f22133d7607eabd753.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_Common_Mode_OffsetRemarksData TypeDescriptionRestrictionsfloat64Specifies the common-mode offset of the AO channel. Use the property only when Terminal Configuration is set to Differential.You can get/set/reset this property using:DAQmxGetAOCommonModeOffsetDAQmxSetAOCommonModeOffsetDA

### DAQmx_AO_Common_Mode_Offset

#### Syntax

DAQmx_AO_Common_Mode_Offset

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the common-mode offset of the AO channel. Use the property only when Terminal Configuration is set to Differential. |  |

You can get/set/reset this property using:

- [DAQmxGetAOCommonModeOffset](group__ni-daqmx__c__functions__property__manipulation__getter_1ga96be93b3f0e2bbc8a727713fe4067221.html)
- [DAQmxSetAOCommonModeOffset](group__ni-daqmx__c__functions__property__manipulation__setter_1gabfb70caf2ccedc453610038e8530c42f.html)
- [DAQmxResetAOCommonModeOffset](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9db1b64eec704c605d5a5cce1d750d41.html)

Parent topic:

Output Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga83654e7a8b6edbbaf3680843031fa50c.html language=enus -->
## TOPIC 01634: DAQmx_AO_IdleOutputBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga83654e7a8b6edbbaf3680843031fa50c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga83654e7a8b6edbbaf3680843031fa50c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_IdleOutputBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies the state of the channel when no generation is in progress.Valid valuesDAQmx_Val_ZeroVolts12526Generate 0 V.DAQmx_Val_HighImpedance12527Set the channel to high-impedance, effectively disconnecting the analog outpu

### DAQmx_AO_IdleOutputBehavior

#### Syntax

DAQmx_AO_IdleOutputBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the state of the channel when no generation is in progress. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ZeroVolts | 12526 | Generate 0 V. |
| DAQmx_Val_HighImpedance | 12527 | Set the channel to high-impedance, effectively disconnecting the analog output circuitry from the I/O connector. |
| DAQmx_Val_MaintainExistingValue | 12528 | Continue generating the current value. |

You can get/set/reset this property using:

- [DAQmxGetAOIdleOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1gad2368d0c8c73cffd764b8c3ef59669e6.html)
- [DAQmxSetAOIdleOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1ga026a18c5c274a30198c6364aa81b3f6b.html)
- [DAQmxResetAOIdleOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga160b79f47199f08b2e9ab4f8843facdb.html)

Parent topic:

Output Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga98f95b42a27506877711836246207893.html language=enus -->
## TOPIC 01635: DAQmx_AO_LoadImpedance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga98f95b42a27506877711836246207893.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1ga98f95b42a27506877711836246207893.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_LoadImpedanceRemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the load impedance connected to the analog output channel.You can get/set/reset this property using:DAQmxGetAOLoadImpedanceDAQmxSetAOLoadImpedanceDAQmxResetAOLoadImpedance

### DAQmx_AO_LoadImpedance

#### Syntax

DAQmx_AO_LoadImpedance

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the load impedance connected to the analog output channel. |  |

You can get/set/reset this property using:

- [DAQmxGetAOLoadImpedance](group__ni-daqmx__c__functions__property__manipulation__getter_1gad3239960e6b051a786a0baa20fb178ca.html)
- [DAQmxSetAOLoadImpedance](group__ni-daqmx__c__functions__property__manipulation__setter_1ga61c1a1f229232418e3e414ea0c814f29.html)
- [DAQmxResetAOLoadImpedance](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga5849ecf45ec99692e400a46ab0ff5cdb.html)

Parent topic:

Output Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1gaa4dc87d5ad491a0575272e8076a8a58b.html language=enus -->
## TOPIC 01636: DAQmx_AO_OutputImpedance

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1gaa4dc87d5ad491a0575272e8076a8a58b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1gaa4dc87d5ad491a0575272e8076a8a58b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_OutputImpedanceRemarksData TypeDescriptionRestrictionsfloat64Specifies in ohms the impedance of the analog output stage of the device.You can get/set/reset this property using:DAQmxGetAOOutputImpedanceDAQmxSetAOOutputImpedanceDAQmxResetAOOutputImpedance

### DAQmx_AO_OutputImpedance

#### Syntax

DAQmx_AO_OutputImpedance

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in ohms the impedance of the analog output stage of the device. |  |

You can get/set/reset this property using:

- [DAQmxGetAOOutputImpedance](group__ni-daqmx__c__functions__property__manipulation__getter_1ga970ae07c432e33412180b189967650a4.html)
- [DAQmxSetAOOutputImpedance](group__ni-daqmx__c__functions__property__manipulation__setter_1ga92026b7f40fb08bbb96cd2dd38335464.html)
- [DAQmxResetAOOutputImpedance](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga50f720d3e1cda5f876d4e35b78a44c9a.html)

Parent topic:

Output Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1gaabaf88653f0f9b8a775466574cf4b1f9.html language=enus -->
## TOPIC 01637: DAQmx_AO_TermCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1gaabaf88653f0f9b8a775466574cf4b1f9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__general__properties__output__configuration_1gaabaf88653f0f9b8a775466574cf4b1f9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_TermCfgRemarksData TypeDescriptionRestrictionsint32Specifies the terminal configuration of the channel.Valid valuesDAQmx_Val_RSE10083Referenced Single-Ended.DAQmx_Val_Diff10106Differential.DAQmx_Val_PseudoDiff12529Pseudodifferential.You can get/set/reset this property using:DAQmxGetAO

### DAQmx_AO_TermCfg

#### Syntax

DAQmx_AO_TermCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the terminal configuration of the channel. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_RSE | 10083 | Referenced Single-Ended. |
| DAQmx_Val_Diff | 10106 | Differential. |
| DAQmx_Val_PseudoDiff | 12529 | Pseudodifferential. |

You can get/set/reset this property using:

- [DAQmxGetAOTermCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6dc7369fe86af8f2961adf63f3bc703f.html)
- [DAQmxSetAOTermCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga32ccddeca2f95887e96f51d0fe7c51a0.html)
- [DAQmxResetAOTermCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1gac4c72d964d2f1b1cd1ab35cde043e174.html)

Parent topic:

Output Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__voltage.html language=enus -->
## TOPIC 01638: Voltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__voltage.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_Voltage_CurrentLimitDAQmx_AO_Voltage_UnitsAttachmentsNone

### Voltage

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_Voltage_CurrentLimit |  |
| DAQmx_AO_Voltage_Units |  |

#### Attachments

None

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__voltage_1ga7573a4411bc59e06e037dd7e5019f714.html language=enus -->
## TOPIC 01639: DAQmx_AO_Voltage_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__voltage_1ga7573a4411bc59e06e037dd7e5019f714.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__voltage_1ga7573a4411bc59e06e037dd7e5019f714.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_Voltage_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select.Valid valuesDAQmx_Val_Volts10348Volts.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select this

### DAQmx_AO_Voltage_Units

#### Syntax

DAQmx_AO_Voltage_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Volts | 10348 | Volts. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetAOVoltageUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga721ab14916cd8a9508dd305936352c2f.html)
- [DAQmxSetAOVoltageUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1gafa6ada9bb6359a8513329b617123167a.html)
- [DAQmxResetAOVoltageUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga5ef1af79e4f43b8cd3f1ba568d7e8ebd.html)

Parent topic:

Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__analog__output__voltage_1gaa75d85cdcf5d5ffdfc937826f7e687d0.html language=enus -->
## TOPIC 01640: DAQmx_AO_Voltage_CurrentLimit

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__analog__output__voltage_1gaa75d85cdcf5d5ffdfc937826f7e687d0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__analog__output__voltage_1gaa75d85cdcf5d5ffdfc937826f7e687d0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_Voltage_CurrentLimitRemarksData TypeDescriptionRestrictionsfloat64Specifies the current limit, in amperes, for the voltage channel.You can get/set/reset this property using:DAQmxGetAOVoltageCurrentLimitDAQmxSetAOVoltageCurrentLimitDAQmxResetAOVoltageCurrentLimit

### DAQmx_AO_Voltage_CurrentLimit

#### Syntax

DAQmx_AO_Voltage_CurrentLimit

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the current limit, in amperes, for the voltage channel. |  |

You can get/set/reset this property using:

- [DAQmxGetAOVoltageCurrentLimit](group__ni-daqmx__c__functions__property__manipulation__getter_1ga60e4a0fcdd1d8badc9c9c3acebe5d5be.html)
- [DAQmxSetAOVoltageCurrentLimit](group__ni-daqmx__c__functions__property__manipulation__setter_1ga940596a86ccd818a60244a0940c4a43b.html)
- [DAQmxResetAOVoltageCurrentLimit](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga6e850da002599efa5c900cc5ad9e6091.html)

Parent topic:

Voltage

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input.html language=enus -->
## TOPIC 01641: Counter Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCount EdgesDuty CycleFrequencyGeneral PropertiesPeriodPositionPulsePulse WidthSemi-PeriodTimestampTwo Edge SeparationVelocityGroup membersNameDescriptionDAQmx_CI_CustomScaleNameDAQmx_CI_MaxDAQmx_CI_MeasTypeDAQmx_CI_MinAttachmentsNone

### Counter Input

#### Groups

- Count Edges
- Duty Cycle
- Frequency
- General Properties
- Period
- Position
- Pulse
- Pulse Width
- Semi-Period
- Timestamp
- Two Edge Separation
- Velocity

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CustomScaleName |  |
| DAQmx_CI_Max |  |
| DAQmx_CI_MeasType |  |
| DAQmx_CI_Min |  |

#### Attachments

None

Parent topic:

Channel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input_1ga08558879abc827f83b7e8de6059c3ccc.html language=enus -->
## TOPIC 01642: DAQmx_CI_CustomScaleName

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input_1ga08558879abc827f83b7e8de6059c3ccc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input_1ga08558879abc827f83b7e8de6059c3ccc.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CustomScaleNameRemarksData TypeDescriptionRestrictionschar*Specifies the name of a custom scale for the channel.You can get/set/reset this property using:DAQmxGetCICustomScaleNameDAQmxSetCICustomScaleNameDAQmxResetCICustomScaleName

### DAQmx_CI_CustomScaleName

#### Syntax

DAQmx_CI_CustomScaleName

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the name of a custom scale for the channel. |  |

You can get/set/reset this property using:

- [DAQmxGetCICustomScaleName](group__ni-daqmx__c__functions__property__manipulation__getter_1gac1ff3babc593d99c85b11e9e6159b02c.html)
- [DAQmxSetCICustomScaleName](group__ni-daqmx__c__functions__property__manipulation__setter_1ga6d5b829047c5c347739ed9f9e203c733.html)
- [DAQmxResetCICustomScaleName](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga72bde9bafb0af2dc5728d44a0d29599c.html)

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input_1ga6b76a6b4ace70389d43af52e4367e0c3.html language=enus -->
## TOPIC 01643: DAQmx_CI_MeasType

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input_1ga6b76a6b4ace70389d43af52e4367e0c3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input_1ga6b76a6b4ace70389d43af52e4367e0c3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_MeasTypeRemarksData TypeDescriptionRestrictionsint32Indicates the measurement to take with the channel.Not SettableValid valuesDAQmx_Val_CountEdges10125Count edges of a digital signal.DAQmx_Val_Freq10179Measure the frequency of a digital signal.DAQmx_Val_Period10256Measure the period

### DAQmx_CI_MeasType

#### Syntax

DAQmx_CI_MeasType

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the measurement to take with the channel. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_CountEdges | 10125 | Count edges of a digital signal. |
| DAQmx_Val_Freq | 10179 | Measure the frequency of a digital signal. |
| DAQmx_Val_Period | 10256 | Measure the period of a digital signal. |
| DAQmx_Val_PulseWidth | 10359 | Measure the width of a pulse of a digital signal. |
| DAQmx_Val_SemiPeriod | 10289 | Measure the time between state transitions of a digital signal. |
| DAQmx_Val_PulseFrequency | 15864 | Pulse measurement, returning the result as frequency and duty cycle. |
| DAQmx_Val_PulseTime | 15865 | Pulse measurement, returning the result as high time and low time. |
| DAQmx_Val_PulseTicks | 15866 | Pulse measurement, returning the result as high ticks and low ticks. |
| DAQmx_Val_DutyCycle | 16070 | Measure the duty cycle of a digital signal. |
| DAQmx_Val_Position_AngEncoder | 10360 | Angular position measurement using an angular encoder. |
| DAQmx_Val_Position_LinEncoder | 10361 | Linear position measurement using a linear encoder. |
| DAQmx_Val_Velocity_AngEncoder | 16078 | Angular velocity measurement using an angular encoder. |
| DAQmx_Val_Velocity_LinEncoder | 16079 | Linear velocity measurement using a linear encoder. |
| DAQmx_Val_TwoEdgeSep | 10267 | Measure time between edges of two digital signals. |
| DAQmx_Val_GPS_Timestamp | 10362 | Timestamp measurement, synchronizing the counter to a GPS receiver. |

You can get this property using:

- [DAQmxGetCIMeasType](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9e2fb1edd70d61cd1d8ee9c0fcaae38b.html)

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input_1ga7f3c892df560f032c8266127127ecb24.html language=enus -->
## TOPIC 01644: DAQmx_CI_Max

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input_1ga7f3c892df560f032c8266127127ecb24.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input_1ga7f3c892df560f032c8266127127ecb24.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_MaxRemarksData TypeDescriptionRestrictionsfloat64Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the hardware can measure with the current settings.

### DAQmx_CI_Max

#### Syntax

DAQmx_CI_Max

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the hardware can measure with the current settings. |  |

You can get/set/reset this property using:

- [DAQmxGetCIMax](group__ni-daqmx__c__functions__property__manipulation__getter_1ga28d6627d053fe73db78c5f4e414a9f87.html)
- [DAQmxSetCIMax](group__ni-daqmx__c__functions__property__manipulation__setter_1ga22281deb91feadbf0306f97fbfcfc9aa.html)
- [DAQmxResetCIMax](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga3ee19a60790addbbba99b8bc7db9bfa8.html)

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input_1gac36a96af59c65b5ada475f9fdb416f10.html language=enus -->
## TOPIC 01645: DAQmx_CI_Min

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input_1gac36a96af59c65b5ada475f9fdb416f10.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input_1gac36a96af59c65b5ada475f9fdb416f10.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_MinRemarksData TypeDescriptionRestrictionsfloat64Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the hardware can measure with the current settings.

### DAQmx_CI_Min

#### Syntax

DAQmx_CI_Min

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the hardware can measure with the current settings. |  |

You can get/set/reset this property using:

- [DAQmxGetCIMin](group__ni-daqmx__c__functions__property__manipulation__getter_1gac905e1cdf2438522cc9afad5c8eaeadd.html)
- [DAQmxSetCIMin](group__ni-daqmx__c__functions__property__manipulation__setter_1gae1df007e04ab3d0e4ae16ad1bf64ef1f.html)
- [DAQmxResetCIMin](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8122a29fed3a4de7b28d484ace633051.html)

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges.html language=enus -->
## TOPIC 01646: Count Edges

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCount DirectionCount ResetGateInputGroup membersNoneAttachmentsNone

### Count Edges

#### Groups

- Count Direction
- Count Reset
- Gate
- Input

#### Group members

None

#### Attachments

None

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction.html language=enus -->
## TOPIC 01647: Count Direction

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsInputGroup membersNameDescriptionDAQmx_CI_CountEdges_DirAttachmentsNone

### Count Direction

#### Groups

- Input

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_Dir |  |

#### Attachments

None

Parent topic:

Count Edges

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction_1ga2e990587f03106b60c759981d4f625ca.html language=enus -->
## TOPIC 01648: DAQmx_CI_CountEdges_Dir

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction_1ga2e990587f03106b60c759981d4f625ca.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction_1ga2e990587f03106b60c759981d4f625ca.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_DirRemarksData TypeDescriptionRestrictionsint32Specifies whether to increment or decrement the counter on each edge.Valid valuesDAQmx_Val_CountUp10128Increment counter.DAQmx_Val_CountDown10124Decrement counter.DAQmx_Val_ExtControlled10326The state of a digital line controls

### DAQmx_CI_CountEdges_Dir

#### Syntax

DAQmx_CI_CountEdges_Dir

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies whether to increment or decrement the counter on each edge. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_CountUp | 10128 | Increment counter. |
| DAQmx_Val_CountDown | 10124 | Decrement counter. |
| DAQmx_Val_ExtControlled | 10326 | The state of a digital line controls the count direction. Each counter has a default count direction terminal. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesDir](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8c72bc4122968f6ba40b2aee2cf3d71e.html)
- [DAQmxSetCICountEdgesDir](group__ni-daqmx__c__functions__property__manipulation__setter_1ga247f42bc2f3f4070a79dd66b0a37d216.html)
- [DAQmxResetCICountEdgesDir](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga467222d018079ebf297cd42e04ac20ef.html)

Parent topic:

Count Direction

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input.html language=enus -->
## TOPIC 01649: Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital FilterDigital SynchronizationGroup membersNameDescriptionDAQmx_CI_CountEdges_CountDir_HystDAQmx_CI_CountEdges_CountDir_LogicLvlBehaviorDAQmx_CI_CountEdges_CountDir_TermCfgDAQmx_CI_CountEdges_CountDir_ThreshVoltageDAQmx_CI_CountEdges_DirTermAttachmentsNone

### Input

#### Groups

- Digital Filter
- Digital Synchronization

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountDir_Hyst |  |
| DAQmx_CI_CountEdges_CountDir_LogicLvlBehavior |  |
| DAQmx_CI_CountEdges_CountDir_TermCfg |  |
| DAQmx_CI_CountEdges_CountDir_ThreshVoltage |  |
| DAQmx_CI_CountEdges_DirTerm |  |

#### Attachments

None

Parent topic:

Count Direction

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1ga25a397613751ae4404be1d7b56930eb9.html language=enus -->
## TOPIC 01650: DAQmx_CI_CountEdges_CountDir_TermCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1ga25a397613751ae4404be1d7b56930eb9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1ga25a397613751ae4404be1d7b56930eb9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_TermCfgRemarksData TypeDescriptionRestrictionsint32Specifies the input terminal configuration.Valid valuesDAQmx_Val_Diff10106Differential.DAQmx_Val_RSE10083Referenced Single-Ended.You can get/set/reset this property using:DAQmxGetCICountEdgesCountDirTermCfgDAQmxSet

### DAQmx_CI_CountEdges_CountDir_TermCfg

#### Syntax

DAQmx_CI_CountEdges_CountDir_TermCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the input terminal configuration. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Diff | 10106 | Differential. |
| DAQmx_Val_RSE | 10083 | Referenced Single-Ended. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirTermCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1gad9ec8006e33e0236daf75e7d6f6587a2.html)
- [DAQmxSetCICountEdgesCountDirTermCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga145b3ce73721b38a4abbe7eeaccd0689.html)
- [DAQmxResetCICountEdgesCountDirTermCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9519e24472394ba85bba3d13c05649a9.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1ga278fdcfc724474ff5fdf40afda2e7b68.html language=enus -->
## TOPIC 01651: DAQmx_CI_CountEdges_CountDir_Hyst

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1ga278fdcfc724474ff5fdf40afda2e7b68.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1ga278fdcfc724474ff5fdf40afda2e7b68.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_HystRemarksData TypeDescriptionRestrictionsfloat64Specifies a hysteresis level applied to the Threshold Level. The source signal must fall below Threshold Level minus the hysteresis before a change in count direction occurs.You can get/set/reset this property using

### DAQmx_CI_CountEdges_CountDir_Hyst

#### Syntax

DAQmx_CI_CountEdges_CountDir_Hyst

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies a hysteresis level applied to the Threshold Level. The source signal must fall below Threshold Level minus the hysteresis before a change in count direction occurs. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirHyst](group__ni-daqmx__c__functions__property__manipulation__getter_1ga643afcf0d5e7eec8f2e1f480c63ffdab.html)
- [DAQmxSetCICountEdgesCountDirHyst](group__ni-daqmx__c__functions__property__manipulation__setter_1gac71cd04191749aff80e4d761015080bc.html)
- [DAQmxResetCICountEdgesCountDirHyst](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4c0cfaf581cb4efb78f30a05d701cd96.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gad3afa0291ce24b816f02eef7230e922e.html language=enus -->
## TOPIC 01652: DAQmx_CI_CountEdges_CountDir_LogicLvlBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gad3afa0291ce24b816f02eef7230e922e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gad3afa0291ce24b816f02eef7230e922e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_LogicLvlBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies the logic level behavior on the count reset line.Valid valuesDAQmx_Val_LogicLevelPullUp16064High logic.DAQmx_Val_None10230Supply no excitation to the channel.You can get/set/reset this property u

### DAQmx_CI_CountEdges_CountDir_LogicLvlBehavior

#### Syntax

DAQmx_CI_CountEdges_CountDir_LogicLvlBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the logic level behavior on the count reset line. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_LogicLevelPullUp | 16064 | High logic. |
| DAQmx_Val_None | 10230 | Supply no excitation to the channel. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1gaae12c11d13955e6848fc479421af4fc2.html)
- [DAQmxSetCICountEdgesCountDirLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1gab240e0175406fe905658e10965269183.html)
- [DAQmxResetCICountEdgesCountDirLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga58dac7aad3989cde846402da0b23a98c.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gadc9e7eaf8c70e03ed5da01d663497d5e.html language=enus -->
## TOPIC 01653: DAQmx_CI_CountEdges_DirTerm

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gadc9e7eaf8c70e03ed5da01d663497d5e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gadc9e7eaf8c70e03ed5da01d663497d5e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_DirTermRemarksData TypeDescriptionRestrictionschar*Specifies the source terminal of the digital signal that controls the count direction if Direction is DAQmx_Val_ExtControlled.You can get/set/reset this property using:DAQmxGetCICountEdgesDirTermDAQmxSetCICountEdgesDirTermD

### DAQmx_CI_CountEdges_DirTerm

#### Syntax

DAQmx_CI_CountEdges_DirTerm

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the source terminal of the digital signal that controls the count direction if Direction is DAQmx_Val_ExtControlled. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesDirTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9013ae1175949a55dfe5fb3f5178d873.html)
- [DAQmxSetCICountEdgesDirTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1ga54cdcbef2b0b31e771f6018c056424dc.html)
- [DAQmxResetCICountEdgesDirTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf18b4394e1c3cb7520ccbb22fbe4eb10.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gaf8ba297758926df9334060029091574a.html language=enus -->
## TOPIC 01654: DAQmx_CI_CountEdges_CountDir_ThreshVoltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gaf8ba297758926df9334060029091574a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input_1gaf8ba297758926df9334060029091574a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_ThreshVoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies the voltage level applied to the Count Direction terminal. When the signal is above this threshold, the counter counts up. When the signal is below this threshold, the counter counts down.You can

### DAQmx_CI_CountEdges_CountDir_ThreshVoltage

#### Syntax

DAQmx_CI_CountEdges_CountDir_ThreshVoltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the voltage level applied to the Count Direction terminal. When the signal is above this threshold, the counter counts up. When the signal is below this threshold, the counter counts down. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga315b1645c8e415313dc1784f57d7ff99.html)
- [DAQmxSetCICountEdgesCountDirThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa6f4c1109369c7b9930bb7fc83925965.html)
- [DAQmxResetCICountEdgesCountDirThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4581338ab992ab35edf90e610e1e95c6.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter.html language=enus -->
## TOPIC 01655: Digital Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimebaseGroup membersNameDescriptionDAQmx_CI_CountEdges_CountDir_DigFltr_EnableDAQmx_CI_CountEdges_CountDir_DigFltr_MinPulseWidthAttachmentsNone

### Digital Filter

#### Groups

- Timebase

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountDir_DigFltr_Enable |  |
| DAQmx_CI_CountEdges_CountDir_DigFltr_MinPulseWidth |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter_1ga46177ddec0f57ee0357a4445704fceee.html language=enus -->
## TOPIC 01656: DAQmx_CI_CountEdges_CountDir_DigFltr_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter_1ga46177ddec0f57ee0357a4445704fceee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter_1ga46177ddec0f57ee0357a4445704fceee.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_DigFltr_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to apply the pulse width filter to the signal.You can get/set/reset this property using:DAQmxGetCICountEdgesCountDirDigFltrEnableDAQmxSetCICountEdgesCountDirDigFltrEnableDAQmxResetCICountE

### DAQmx_CI_CountEdges_CountDir_DigFltr_Enable

#### Syntax

DAQmx_CI_CountEdges_CountDir_DigFltr_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to apply the pulse width filter to the signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2f58084e7a5fc7bcd565ad4d5b6a7111.html)
- [DAQmxSetCICountEdgesCountDirDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga365063f44fa1111f21a7d35a8df5f53a.html)
- [DAQmxResetCICountEdgesCountDirDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga73ff5dc5b50a8e97b2eee3d895413b54.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter_1ga7cb39994673593ba2706c5046f2a66b9.html language=enus -->
## TOPIC 01657: DAQmx_CI_CountEdges_CountDir_DigFltr_MinPulseWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter_1ga7cb39994673593ba2706c5046f2a66b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter_1ga7cb39994673593ba2706c5046f2a66b9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_DigFltr_MinPulseWidthRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the minimum pulse width the filter recognizes.You can get/set/reset this property using:DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidthDAQmxSetCICountEdgesCountDirDigFltrMinPul

### DAQmx_CI_CountEdges_CountDir_DigFltr_MinPulseWidth

#### Syntax

DAQmx_CI_CountEdges_CountDir_DigFltr_MinPulseWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the minimum pulse width the filter recognizes. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga782f9e34482062c4044ae4b13a17e0c3.html)
- [DAQmxSetCICountEdgesCountDirDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1ga21604a4ee62d88a4ec36393832d369be.html)
- [DAQmxResetCICountEdgesCountDirDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga54bb69aa0645a5e813588022fa0c70c7.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase.html language=enus -->
## TOPIC 01658: Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseRateDAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseSrcAttachmentsNone

### Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseRate |  |
| DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseSrc |  |

#### Attachments

None

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase_1ga163c17e4aca967174bdf2387aa39b204.html language=enus -->
## TOPIC 01659: DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase_1ga163c17e4aca967174bdf2387aa39b204.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase_1ga163c17e4aca967174bdf2387aa39b204.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseRateRemarksData TypeDescriptionRestrictionsfloat64Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.You can get/set/reset this property using:DAQmxGetCICountEdgesCountDirDigFl

### DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseRate

#### Syntax

DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__getter_1gaeec17fc5f02328edd23db7e1f0c60ac6.html)
- [DAQmxSetCICountEdgesCountDirDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1bf4618eafb48613fdd50b1c9bb59400.html)
- [DAQmxResetCICountEdgesCountDirDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaaeb36751c5020fe2be6f29fe47f144e5.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase_1gaf712d3e5239994d35512f01c4f977faa.html language=enus -->
## TOPIC 01660: DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase_1gaf712d3e5239994d35512f01c4f977faa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__filter__timebase_1gaf712d3e5239994d35512f01c4f977faa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseSrcRemarksData TypeDescriptionRestrictionschar*Specifies the input terminal of the signal to use as the timebase of the pulse width filter.You can get/set/reset this property using:DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrcDAQmxSetCICountEdgesCo

### DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseSrc

#### Syntax

DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1gabfaf862e5c2cf2a789447356d99f044c.html)
- [DAQmxSetCICountEdgesCountDirDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1ga5f110ec856cc2379e2b9f8c1cf7e3d2b.html)
- [DAQmxResetCICountEdgesCountDirDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga3cea1d897c4a0db2d821b4d7b7d96aaa.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization.html language=enus -->
## TOPIC 01661: Digital Synchronization

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CountEdges_ActiveEdgeDAQmx_CI_CountEdges_CountDir_DigSync_EnableDAQmx_CI_CountEdges_InitialCntAttachmentsNone

### Digital Synchronization

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_ActiveEdge |  |
| DAQmx_CI_CountEdges_CountDir_DigSync_Enable |  |
| DAQmx_CI_CountEdges_InitialCnt |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1ga0d8a3f95a83fa8093d244f7c5dcd8d7d.html language=enus -->
## TOPIC 01662: DAQmx_CI_CountEdges_InitialCnt

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1ga0d8a3f95a83fa8093d244f7c5dcd8d7d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1ga0d8a3f95a83fa8093d244f7c5dcd8d7d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_InitialCntRemarksData TypeDescriptionRestrictionsuInt32Specifies the starting value from which to count.You can get/set/reset this property using:DAQmxGetCICountEdgesInitialCntDAQmxSetCICountEdgesInitialCntDAQmxResetCICountEdgesInitialCnt

### DAQmx_CI_CountEdges_InitialCnt

#### Syntax

DAQmx_CI_CountEdges_InitialCnt

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies the starting value from which to count. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesInitialCnt](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa4bb8a3aacefaf5fbfc5de488036afe1.html)
- [DAQmxSetCICountEdgesInitialCnt](group__ni-daqmx__c__functions__property__manipulation__setter_1gaaecd4503572261592b83de5fec80ff64.html)
- [DAQmxResetCICountEdgesInitialCnt](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8782e8fc429122f7acc2f9a7e6097295.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1ga29aad6847846c285a60f9951b39aefc6.html language=enus -->
## TOPIC 01663: DAQmx_CI_CountEdges_CountDir_DigSync_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1ga29aad6847846c285a60f9951b39aefc6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1ga29aad6847846c285a60f9951b39aefc6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountDir_DigSync_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.You can get/set/reset this property using:DAQmxGetCICountEdgesCountDirDigSyncEnableDAQmxSetCI

### DAQmx_CI_CountEdges_CountDir_DigSync_Enable

#### Syntax

DAQmx_CI_CountEdges_CountDir_DigSync_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountDirDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga43a495e5955ea3f3ce9ead44bc2106bf.html)
- [DAQmxSetCICountEdgesCountDirDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3056ea5308a2faea2d4846e1649e2f4a.html)
- [DAQmxResetCICountEdgesCountDirDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae0d8e02e8269b62a269c70e3679e5d1f.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1gabd9dc5fbe77dd3ce699aab312b79cd07.html language=enus -->
## TOPIC 01664: DAQmx_CI_CountEdges_ActiveEdge

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1gabd9dc5fbe77dd3ce699aab312b79cd07.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__direction__input__digital__synchronization_1gabd9dc5fbe77dd3ce699aab312b79cd07.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_ActiveEdgeRemarksData TypeDescriptionRestrictionsint32Specifies on which edges to increment or decrement the counter.Valid valuesDAQmx_Val_Rising10280Rising edge(s).DAQmx_Val_Falling10171Falling edge(s).You can get/set/reset this property using:DAQmxGetCICountEdgesActiveEdg

### DAQmx_CI_CountEdges_ActiveEdge

#### Syntax

DAQmx_CI_CountEdges_ActiveEdge

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies on which edges to increment or decrement the counter. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Rising | 10280 | Rising edge(s). |
| DAQmx_Val_Falling | 10171 | Falling edge(s). |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesActiveEdge](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1e88ebf40f9fff54d5f4827f953c4e88.html)
- [DAQmxSetCICountEdgesActiveEdge](group__ni-daqmx__c__functions__property__manipulation__setter_1ga5ed156d20de85749d12d327ceb0e6428.html)
- [DAQmxResetCICountEdgesActiveEdge](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8aaf4519d21a624837ea00f31cceff26.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset.html language=enus -->
## TOPIC 01665: Count Reset

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsInputGroup membersNameDescriptionDAQmx_CI_CountEdges_CountReset_EnableDAQmx_CI_CountEdges_CountReset_ResetCountAttachmentsNone

### Count Reset

#### Groups

- Input

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountReset_Enable |  |
| DAQmx_CI_CountEdges_CountReset_ResetCount |  |

#### Attachments

None

Parent topic:

Count Edges

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset_1ga642dd5f6ededf24573d7aaecade98f3a.html language=enus -->
## TOPIC 01666: DAQmx_CI_CountEdges_CountReset_ResetCount

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset_1ga642dd5f6ededf24573d7aaecade98f3a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset_1ga642dd5f6ededf24573d7aaecade98f3a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_ResetCountRemarksData TypeDescriptionRestrictionsuInt32Specifies the value to reset the count to.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetResetCountDAQmxSetCICountEdgesCountResetResetCountDAQmxResetCICountEdgesCountResetResetCount

### DAQmx_CI_CountEdges_CountReset_ResetCount

#### Syntax

DAQmx_CI_CountEdges_CountReset_ResetCount

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies the value to reset the count to. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetResetCount](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8b7e409ec90034ab12004f2e84896465.html)
- [DAQmxSetCICountEdgesCountResetResetCount](group__ni-daqmx__c__functions__property__manipulation__setter_1gaeb65496ef1cfc99dc22f2f99cae60f50.html)
- [DAQmxResetCICountEdgesCountResetResetCount](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga098379850db2eb5e307734c5307b71a1.html)

Parent topic:

Count Reset

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset_1gabcc2c5a1812b00ea615291d1f5c2c718.html language=enus -->
## TOPIC 01667: DAQmx_CI_CountEdges_CountReset_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset_1gabcc2c5a1812b00ea615291d1f5c2c718.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset_1gabcc2c5a1812b00ea615291d1f5c2c718.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to reset the count on the active edge specified with Terminal.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetEnableDAQmxSetCICountEdgesCountResetEnableDAQmxResetCICountE

### DAQmx_CI_CountEdges_CountReset_Enable

#### Syntax

DAQmx_CI_CountEdges_CountReset_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to reset the count on the active edge specified with Terminal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga68a00e3f141b2328a4e4704a24dd5dd2.html)
- [DAQmxSetCICountEdgesCountResetEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9f3a66f3b8aede5b95178f1f792758ca.html)
- [DAQmxResetCICountEdgesCountResetEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga20b40bcc9fc692e635280fb1157f735f.html)

Parent topic:

Count Reset

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input.html language=enus -->
## TOPIC 01668: Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital FilterDigital SynchronizationGroup membersNameDescriptionDAQmx_CI_CountEdges_CountReset_HystDAQmx_CI_CountEdges_CountReset_LogicLvlBehaviorDAQmx_CI_CountEdges_CountReset_TermDAQmx_CI_CountEdges_CountReset_TermCfgDAQmx_CI_CountEdges_CountReset_ThreshVoltageAttachmentsNone

### Input

#### Groups

- Digital Filter
- Digital Synchronization

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountReset_Hyst |  |
| DAQmx_CI_CountEdges_CountReset_LogicLvlBehavior |  |
| DAQmx_CI_CountEdges_CountReset_Term |  |
| DAQmx_CI_CountEdges_CountReset_TermCfg |  |
| DAQmx_CI_CountEdges_CountReset_ThreshVoltage |  |

#### Attachments

None

Parent topic:

Count Reset

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga10e21fd6f2674fc1e23670bffc70389b.html language=enus -->
## TOPIC 01669: DAQmx_CI_CountEdges_CountReset_TermCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga10e21fd6f2674fc1e23670bffc70389b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga10e21fd6f2674fc1e23670bffc70389b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_TermCfgRemarksData TypeDescriptionRestrictionsint32Specifies the input terminal configuration.Valid valuesDAQmx_Val_Diff10106Differential.DAQmx_Val_RSE10083Referenced Single-Ended.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetTermCfgDAQm

### DAQmx_CI_CountEdges_CountReset_TermCfg

#### Syntax

DAQmx_CI_CountEdges_CountReset_TermCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the input terminal configuration. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Diff | 10106 | Differential. |
| DAQmx_Val_RSE | 10083 | Referenced Single-Ended. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetTermCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1ga654cd3dc3fb609bd9d17265780f75651.html)
- [DAQmxSetCICountEdgesCountResetTermCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga380c5276496e347bb049617075df242c.html)
- [DAQmxResetCICountEdgesCountResetTermCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga302c5c1846fc0ae12a5b3f5b91cd7542.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga54520f5142779980c8bfa28616403b0c.html language=enus -->
## TOPIC 01670: DAQmx_CI_CountEdges_CountReset_ThreshVoltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga54520f5142779980c8bfa28616403b0c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga54520f5142779980c8bfa28616403b0c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_ThreshVoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies the voltage level at which to recognize the counter reset event.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetThreshVoltageDAQmxSetCICountEdgesCountResetThreshVoltageDA

### DAQmx_CI_CountEdges_CountReset_ThreshVoltage

#### Syntax

DAQmx_CI_CountEdges_CountReset_ThreshVoltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the voltage level at which to recognize the counter reset event. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2771d153ee1080b209d5b9da184c47ea.html)
- [DAQmxSetCICountEdgesCountResetThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1gab037eb1d335a0b3eacd2124398e60a9a.html)
- [DAQmxResetCICountEdgesCountResetThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafd949a752d614a709dd2a3b2ce053dbf.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga680bbff987a983d57b75647a14ca381c.html language=enus -->
## TOPIC 01671: DAQmx_CI_CountEdges_CountReset_Hyst

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga680bbff987a983d57b75647a14ca381c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga680bbff987a983d57b75647a14ca381c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_HystRemarksData TypeDescriptionRestrictionsfloat64Specifies a hysteresis level applied to Threshold Level. When Active Edge is rising, the source signal must first fall below Threshold Level minus the hysteresis before a rising edge is detected at Threshold Level

### DAQmx_CI_CountEdges_CountReset_Hyst

#### Syntax

DAQmx_CI_CountEdges_CountReset_Hyst

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies a hysteresis level applied to Threshold Level. When Active Edge is rising, the source signal must first fall below Threshold Level minus the hysteresis before a rising edge is detected at Threshold Level. When Active Edge is falling, the source signal must first rise above Threshold Level plus the hysteresis before a falling edge is detected at Threshold Level. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetHyst](group__ni-daqmx__c__functions__property__manipulation__getter_1gab64280a59f6822b26b12cf2f4284d3c9.html)
- [DAQmxSetCICountEdgesCountResetHyst](group__ni-daqmx__c__functions__property__manipulation__setter_1ga87458ee7987a47e1daa56bba8b66a2fa.html)
- [DAQmxResetCICountEdgesCountResetHyst](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaae8851b1ecc6c973c67b6a10a3876a3f.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga7e53443091177509ff503803f76455cb.html language=enus -->
## TOPIC 01672: DAQmx_CI_CountEdges_CountReset_Term

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga7e53443091177509ff503803f76455cb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1ga7e53443091177509ff503803f76455cb.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_TermRemarksData TypeDescriptionRestrictionschar*Specifies the input terminal of the signal to reset the count.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetTermDAQmxSetCICountEdgesCountResetTermDAQmxResetCICountEdgesCountResetTerm

### DAQmx_CI_CountEdges_CountReset_Term

#### Syntax

DAQmx_CI_CountEdges_CountReset_Term

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the input terminal of the signal to reset the count. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1ga688c8317efcada1bd03b5ee6b8f63d1f.html)
- [DAQmxSetCICountEdgesCountResetTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1gab901a4d31f47b95f05b6199d438d384b.html)
- [DAQmxResetCICountEdgesCountResetTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1gace97320ff783e877e4c533c0f3b91c47.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1gae24518b1efee66f34f943bb25635e38c.html language=enus -->
## TOPIC 01673: DAQmx_CI_CountEdges_CountReset_LogicLvlBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1gae24518b1efee66f34f943bb25635e38c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input_1gae24518b1efee66f34f943bb25635e38c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_LogicLvlBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies the logic level behavior on the count reset line.Valid valuesDAQmx_Val_LogicLevelPullUp16064High logic.DAQmx_Val_None10230Supply no excitation to the channel.You can get/set/reset this property

### DAQmx_CI_CountEdges_CountReset_LogicLvlBehavior

#### Syntax

DAQmx_CI_CountEdges_CountReset_LogicLvlBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the logic level behavior on the count reset line. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_LogicLevelPullUp | 16064 | High logic. |
| DAQmx_Val_None | 10230 | Supply no excitation to the channel. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1ga16f9a04da51e7a43a119e077fe68e750.html)
- [DAQmxSetCICountEdgesCountResetLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1ga08930a7be0a5c21f8120f1b6bb6e35b0.html)
- [DAQmxResetCICountEdgesCountResetLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae9df7f18eed2e34490a07f7fc783ff94.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter.html language=enus -->
## TOPIC 01674: Digital Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimebaseGroup membersNameDescriptionDAQmx_CI_CountEdges_CountReset_DigFltr_EnableDAQmx_CI_CountEdges_CountReset_DigFltr_MinPulseWidthAttachmentsNone

### Digital Filter

#### Groups

- Timebase

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountReset_DigFltr_Enable |  |
| DAQmx_CI_CountEdges_CountReset_DigFltr_MinPulseWidth |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter_1ga16250a2817aa02e23b265ad505fc8c85.html language=enus -->
## TOPIC 01675: DAQmx_CI_CountEdges_CountReset_DigFltr_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter_1ga16250a2817aa02e23b265ad505fc8c85.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter_1ga16250a2817aa02e23b265ad505fc8c85.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_DigFltr_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to apply the pulse width filter to the signal.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetDigFltrEnableDAQmxSetCICountEdgesCountResetDigFltrEnableDAQmxResetCI

### DAQmx_CI_CountEdges_CountReset_DigFltr_Enable

#### Syntax

DAQmx_CI_CountEdges_CountReset_DigFltr_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to apply the pulse width filter to the signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1gabe2eda3857f48e8b37457125e72dc7aa.html)
- [DAQmxSetCICountEdgesCountResetDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga4a5f7b07ad2f7e4c2d2a6e086ec1efe1.html)
- [DAQmxResetCICountEdgesCountResetDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaee8aaf7d22e2ee2bf5f8e8f9870beee4.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter_1ga9bc4134b59aa04e8e58672d1bd258140.html language=enus -->
## TOPIC 01676: DAQmx_CI_CountEdges_CountReset_DigFltr_MinPulseWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter_1ga9bc4134b59aa04e8e58672d1bd258140.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter_1ga9bc4134b59aa04e8e58672d1bd258140.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_DigFltr_MinPulseWidthRemarksData TypeDescriptionRestrictionsfloat64Specifies the minimum pulse width the filter recognizes.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetDigFltrMinPulseWidthDAQmxSetCICountEdgesCountResetDigFltrMinPulseWid

### DAQmx_CI_CountEdges_CountReset_DigFltr_MinPulseWidth

#### Syntax

DAQmx_CI_CountEdges_CountReset_DigFltr_MinPulseWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the minimum pulse width the filter recognizes. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1gabb0e0b919eb37254b71482979251cd17.html)
- [DAQmxSetCICountEdgesCountResetDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1ga7bcfe2c000d5e664c4126c47595692f3.html)
- [DAQmxResetCICountEdgesCountResetDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga596ee028f4ffd24c6afb59bf29248e68.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase.html language=enus -->
## TOPIC 01677: Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseRateDAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseSrcAttachmentsNone

### Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseRate |  |
| DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseSrc |  |

#### Attachments

None

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase_1ga118d4f1d0f95b89a64b025030f5f15af.html language=enus -->
## TOPIC 01678: DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase_1ga118d4f1d0f95b89a64b025030f5f15af.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase_1ga118d4f1d0f95b89a64b025030f5f15af.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseSrcRemarksData TypeDescriptionRestrictionschar*Specifies the input of the signal to use as the timebase of the pulse width filter.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetDigFltrTimebaseSrcDAQmxSetCICountEdgesCountRe

### DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseSrc

#### Syntax

DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the input of the signal to use as the timebase of the pulse width filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga62db59fba04c2e4e24cdd5179468285f.html)
- [DAQmxSetCICountEdgesCountResetDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3f5f241a861cf2a2eccbb00fb0de07c8.html)
- [DAQmxResetCICountEdgesCountResetDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga84e5bb2b78cec5550815e2e602320469.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase_1gaca0cf01085b1be196912b63600d9d018.html language=enus -->
## TOPIC 01679: DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase_1gaca0cf01085b1be196912b63600d9d018.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__filter__timebase_1gaca0cf01085b1be196912b63600d9d018.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseRateRemarksData TypeDescriptionRestrictionsfloat64Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetD

### DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseRate

#### Syntax

DAQmx_CI_CountEdges_CountReset_DigFltr_TimebaseRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__getter_1ga108bf55d895e25527bb495aae1d3a1a0.html)
- [DAQmxSetCICountEdgesCountResetDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa7f761272d3f28d9cb8eb0634fe4c244.html)
- [DAQmxResetCICountEdgesCountResetDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaff6ab702bde4cfc62c350f33897fbad8.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization.html language=enus -->
## TOPIC 01680: Digital Synchronization

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CountEdges_CountReset_ActiveEdgeDAQmx_CI_CountEdges_CountReset_DigSync_EnableAttachmentsNone

### Digital Synchronization

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_CountReset_ActiveEdge |  |
| DAQmx_CI_CountEdges_CountReset_DigSync_Enable |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization_1ga188db7da21fd667a316fb0636b5431bd.html language=enus -->
## TOPIC 01681: DAQmx_CI_CountEdges_CountReset_ActiveEdge

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization_1ga188db7da21fd667a316fb0636b5431bd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization_1ga188db7da21fd667a316fb0636b5431bd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_ActiveEdgeRemarksData TypeDescriptionRestrictionsint32Specifies on which edge of the signal to reset the count.Valid valuesDAQmx_Val_Rising10280Rising edge(s).DAQmx_Val_Falling10171Falling edge(s).You can get/set/reset this property using:DAQmxGetCICountEdgesCoun

### DAQmx_CI_CountEdges_CountReset_ActiveEdge

#### Syntax

DAQmx_CI_CountEdges_CountReset_ActiveEdge

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies on which edge of the signal to reset the count. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Rising | 10280 | Rising edge(s). |
| DAQmx_Val_Falling | 10171 | Falling edge(s). |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetActiveEdge](group__ni-daqmx__c__functions__property__manipulation__getter_1gafa22cce095b897d811c74e4eea44bc02.html)
- [DAQmxSetCICountEdgesCountResetActiveEdge](group__ni-daqmx__c__functions__property__manipulation__setter_1gab47d7270e6024c073c1eb820854b0652.html)
- [DAQmxResetCICountEdgesCountResetActiveEdge](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab3be50439b497875948d730cc3b265c2.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization_1ga4495924b3e98debea1ed13e888e6cfda.html language=enus -->
## TOPIC 01682: DAQmx_CI_CountEdges_CountReset_DigSync_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization_1ga4495924b3e98debea1ed13e888e6cfda.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__count__reset__input__digital__synchronization_1ga4495924b3e98debea1ed13e888e6cfda.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_CountReset_DigSync_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.You can get/set/reset this property using:DAQmxGetCICountEdgesCountResetDigSyncEnableDAQmxS

### DAQmx_CI_CountEdges_CountReset_DigSync_Enable

#### Syntax

DAQmx_CI_CountEdges_CountReset_DigSync_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesCountResetDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6f374fcea79ff45258746ff41741a4a0.html)
- [DAQmxSetCICountEdgesCountResetDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gac2a07aef250cdcb14e1c24a63aedb8ac.html)
- [DAQmxResetCICountEdgesCountResetDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga3fe1df751d107fccb0a9f650d070d138.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate.html language=enus -->
## TOPIC 01683: Gate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsInputGroup membersNameDescriptionDAQmx_CI_CountEdges_Gate_EnableAttachmentsNone

### Gate

#### Groups

- Input

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_Gate_Enable |  |

#### Attachments

None

Parent topic:

Count Edges

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate_1gaaa91aa5ae7b35b4bbdb2d5f2106b8e48.html language=enus -->
## TOPIC 01684: DAQmx_CI_CountEdges_Gate_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate_1gaaa91aa5ae7b35b4bbdb2d5f2106b8e48.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate_1gaaa91aa5ae7b35b4bbdb2d5f2106b8e48.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to enable the functionality to gate the counter input signal for a count edges measurement.You can get/set/reset this property using:DAQmxGetCICountEdgesGateEnableDAQmxSetCICountEdgesGateEnableDAQmxRe

### DAQmx_CI_CountEdges_Gate_Enable

#### Syntax

DAQmx_CI_CountEdges_Gate_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to enable the functionality to gate the counter input signal for a count edges measurement. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1687ffdddb3d6e09a72c01320e1675b3.html)
- [DAQmxSetCICountEdgesGateEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gaf3eea99b2351d12f59c09e6177653099.html)
- [DAQmxResetCICountEdgesGateEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga3d385e51cae13673e81f07e334ff5224.html)

Parent topic:

Gate

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input.html language=enus -->
## TOPIC 01685: Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital FilterGroup membersNameDescriptionDAQmx_CI_CountEdges_Gate_HystDAQmx_CI_CountEdges_Gate_LogicLvlBehaviorDAQmx_CI_CountEdges_Gate_TermDAQmx_CI_CountEdges_Gate_TermCfgDAQmx_CI_CountEdges_Gate_ThreshVoltageAttachmentsNone

### Input

#### Groups

- Digital Filter

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_Gate_Hyst |  |
| DAQmx_CI_CountEdges_Gate_LogicLvlBehavior |  |
| DAQmx_CI_CountEdges_Gate_Term |  |
| DAQmx_CI_CountEdges_Gate_TermCfg |  |
| DAQmx_CI_CountEdges_Gate_ThreshVoltage |  |

#### Attachments

None

Parent topic:

Gate

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga139cce738b9e664c6a768956b2087b71.html language=enus -->
## TOPIC 01686: DAQmx_CI_CountEdges_Gate_ThreshVoltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga139cce738b9e664c6a768956b2087b71.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga139cce738b9e664c6a768956b2087b71.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_ThreshVoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies the voltage level at which to recognize the counter gate signal.You can get/set/reset this property using:DAQmxGetCICountEdgesGateThreshVoltageDAQmxSetCICountEdgesGateThreshVoltageDAQmxResetCICountEdg

### DAQmx_CI_CountEdges_Gate_ThreshVoltage

#### Syntax

DAQmx_CI_CountEdges_Gate_ThreshVoltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the voltage level at which to recognize the counter gate signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6c5b71a51c8fc1447150753e73a6bacc.html)
- [DAQmxSetCICountEdgesGateThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1gac22f48ae5a845dd2f76a3574318629dd.html)
- [DAQmxResetCICountEdgesGateThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1gacc9fcfad850064d9ab7e40670e164d3c.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga3b87e517218e7bd8cf50b95fe5c5cacf.html language=enus -->
## TOPIC 01687: DAQmx_CI_CountEdges_Gate_Term

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga3b87e517218e7bd8cf50b95fe5c5cacf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga3b87e517218e7bd8cf50b95fe5c5cacf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_TermRemarksData TypeDescriptionRestrictionschar*Specifies the gate terminal.You can get/set/reset this property using:DAQmxGetCICountEdgesGateTermDAQmxSetCICountEdgesGateTermDAQmxResetCICountEdgesGateTerm

### DAQmx_CI_CountEdges_Gate_Term

#### Syntax

DAQmx_CI_CountEdges_Gate_Term

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the gate terminal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6668de24513748294b52b135799bad9f.html)
- [DAQmxSetCICountEdgesGateTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1ga2b4454586a8aa49535dffa8095db9546.html)
- [DAQmxResetCICountEdgesGateTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1gabd9f73cf71289a3da66413828c29e145.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga4f616c56d082995e5791a45c9a25e25f.html language=enus -->
## TOPIC 01688: DAQmx_CI_CountEdges_Gate_LogicLvlBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga4f616c56d082995e5791a45c9a25e25f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1ga4f616c56d082995e5791a45c9a25e25f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_LogicLvlBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies the logic level behavior on the gate input line.Valid valuesDAQmx_Val_LogicLevelPullUp16064High logic.DAQmx_Val_None10230Supply no excitation to the channel.You can get/set/reset this property using:

### DAQmx_CI_CountEdges_Gate_LogicLvlBehavior

#### Syntax

DAQmx_CI_CountEdges_Gate_LogicLvlBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the logic level behavior on the gate input line. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_LogicLevelPullUp | 16064 | High logic. |
| DAQmx_Val_None | 10230 | Supply no excitation to the channel. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf76e4248f750428c2ed7c7ef4ef5eab9.html)
- [DAQmxSetCICountEdgesGateLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1ga06611c5b18f0a87d00b65d17bddb293b.html)
- [DAQmxResetCICountEdgesGateLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga2f6461044fecf65b7ab117076c839abb.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1gaaf57a106e16017d9f5b9fd4528077c4d.html language=enus -->
## TOPIC 01689: DAQmx_CI_CountEdges_Gate_TermCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1gaaf57a106e16017d9f5b9fd4528077c4d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1gaaf57a106e16017d9f5b9fd4528077c4d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_TermCfgRemarksData TypeDescriptionRestrictionsint32Specifies the gate terminal configuration.Valid valuesDAQmx_Val_Diff10106Differential.DAQmx_Val_RSE10083Referenced Single-Ended.You can get/set/reset this property using:DAQmxGetCICountEdgesGateTermCfgDAQmxSetCICountEd

### DAQmx_CI_CountEdges_Gate_TermCfg

#### Syntax

DAQmx_CI_CountEdges_Gate_TermCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the gate terminal configuration. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Diff | 10106 | Differential. |
| DAQmx_Val_RSE | 10083 | Referenced Single-Ended. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateTermCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1gadff0efd090b7d4220c1778a0b271080f.html)
- [DAQmxSetCICountEdgesGateTermCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga99e16e5b6b4229e300fdca8b5ea241b2.html)
- [DAQmxResetCICountEdgesGateTermCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga59cda5f1f1a90b348480416c3ddd6b23.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1gad4f757934166ea028022a2b7e4ba23a6.html language=enus -->
## TOPIC 01690: DAQmx_CI_CountEdges_Gate_Hyst

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1gad4f757934166ea028022a2b7e4ba23a6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input_1gad4f757934166ea028022a2b7e4ba23a6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_HystRemarksData TypeDescriptionRestrictionsfloat64Specifies a hysteresis level applied to the Threshold Level. When Pause When is High, the source signal must fall below Threshold Level minus the hysteresis before the counter resumes counting. When Pause When is Low, t

### DAQmx_CI_CountEdges_Gate_Hyst

#### Syntax

DAQmx_CI_CountEdges_Gate_Hyst

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies a hysteresis level applied to the Threshold Level. When Pause When is High, the source signal must fall below Threshold Level minus the hysteresis before the counter resumes counting. When Pause When is Low, the source signal must rise above Threshold Level plus the hysteresis before the counter resumes counting. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateHyst](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4e740ac27d3c051896952cfa60933788.html)
- [DAQmxSetCICountEdgesGateHyst](group__ni-daqmx__c__functions__property__manipulation__setter_1ga0331437d50592064d83707b628c30b78.html)
- [DAQmxResetCICountEdgesGateHyst](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga259fbb647a13f0fba9cb13506f421c5c.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter.html language=enus -->
## TOPIC 01691: Digital Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimebaseGroup membersNameDescriptionDAQmx_CI_CountEdges_Gate_DigFltrEnableDAQmx_CI_CountEdges_Gate_DigFltrMinPulseWidthAttachmentsNone

### Digital Filter

#### Groups

- Timebase

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_Gate_DigFltrEnable |  |
| DAQmx_CI_CountEdges_Gate_DigFltrMinPulseWidth |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter_1gabac67cf15e52517f5107f6adf3bc453e.html language=enus -->
## TOPIC 01692: DAQmx_CI_CountEdges_Gate_DigFltrEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter_1gabac67cf15e52517f5107f6adf3bc453e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter_1gabac67cf15e52517f5107f6adf3bc453e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_DigFltrEnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to apply the pulse width filter to the gate input signal.You can get/set/reset this property using:DAQmxGetCICountEdgesGateDigFltrEnableDAQmxSetCICountEdgesGateDigFltrEnableDAQmxResetCICountEdg

### DAQmx_CI_CountEdges_Gate_DigFltrEnable

#### Syntax

DAQmx_CI_CountEdges_Gate_DigFltrEnable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to apply the pulse width filter to the gate input signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga091e55e14f440a5424ba766f1da57efb.html)
- [DAQmxSetCICountEdgesGateDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gadc1fdc87a31afb97aa56c6df755a94b7.html)
- [DAQmxResetCICountEdgesGateDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga898561abba630f37a925d04b552401ec.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter_1gad9213f8a0bfdf73a655dbd5cf9920cc8.html language=enus -->
## TOPIC 01693: DAQmx_CI_CountEdges_Gate_DigFltrMinPulseWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter_1gad9213f8a0bfdf73a655dbd5cf9920cc8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter_1gad9213f8a0bfdf73a655dbd5cf9920cc8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_DigFltrMinPulseWidthRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the minimum pulse width the digital filter recognizes.You can get/set/reset this property using:DAQmxGetCICountEdgesGateDigFltrMinPulseWidthDAQmxSetCICountEdgesGateDigFltrMinPulseWid

### DAQmx_CI_CountEdges_Gate_DigFltrMinPulseWidth

#### Syntax

DAQmx_CI_CountEdges_Gate_DigFltrMinPulseWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the minimum pulse width the digital filter recognizes. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga28e550b763e5547ec7c97f61ed508b7f.html)
- [DAQmxSetCICountEdgesGateDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1205bab7072bf6e91127fdf1c3aafa60.html)
- [DAQmxResetCICountEdgesGateDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga16df3eece989897ae03ba352015cb556.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase.html language=enus -->
## TOPIC 01694: Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CountEdges_GateWhenDAQmx_CI_CountEdges_Gate_DigFltrTimebaseRateDAQmx_CI_CountEdges_Gate_DigFltrTimebaseSrcAttachmentsNone

### Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_GateWhen |  |
| DAQmx_CI_CountEdges_Gate_DigFltrTimebaseRate |  |
| DAQmx_CI_CountEdges_Gate_DigFltrTimebaseSrc |  |

#### Attachments

None

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1ga534415f5c4035b5ad6cacbd6c9db6c2f.html language=enus -->
## TOPIC 01695: DAQmx_CI_CountEdges_Gate_DigFltrTimebaseSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1ga534415f5c4035b5ad6cacbd6c9db6c2f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1ga534415f5c4035b5ad6cacbd6c9db6c2f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_DigFltrTimebaseSrcRemarksData TypeDescriptionRestrictionschar*Specifies the input terminal of the signal to use as the timebase of the pulse width filter.You can get/set/reset this property using:DAQmxGetCICountEdgesGateDigFltrTimebaseSrcDAQmxSetCICountEdgesGateDigFltr

### DAQmx_CI_CountEdges_Gate_DigFltrTimebaseSrc

#### Syntax

DAQmx_CI_CountEdges_Gate_DigFltrTimebaseSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf2282736ba4474a0d1d2edcb90741f4c.html)
- [DAQmxSetCICountEdgesGateDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9ae53f7c19175d8a1270bf7f41f60b45.html)
- [DAQmxResetCICountEdgesGateDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaee09c87a36237b95d2e838439728603d.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1ga5b67dc46dcea2f6a008b83fba8383b13.html language=enus -->
## TOPIC 01696: DAQmx_CI_CountEdges_Gate_DigFltrTimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1ga5b67dc46dcea2f6a008b83fba8383b13.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1ga5b67dc46dcea2f6a008b83fba8383b13.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_Gate_DigFltrTimebaseRateRemarksData TypeDescriptionRestrictionsfloat64Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.You can get/set/reset this property using:DAQmxGetCICountEdgesGateDigFltrTimebas

### DAQmx_CI_CountEdges_Gate_DigFltrTimebaseRate

#### Syntax

DAQmx_CI_CountEdges_Gate_DigFltrTimebaseRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__getter_1gacd14b584484f719bdc5e9b5f4c1ef382.html)
- [DAQmxSetCICountEdgesGateDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__setter_1ga765dc09c8f5146a90248a53c847ad283.html)
- [DAQmxResetCICountEdgesGateDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafbfff0efd585db518dd83d353544fa04.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1gafb2db4ee3af4bedda97f94f263a0fdc7.html language=enus -->
## TOPIC 01697: DAQmx_CI_CountEdges_GateWhen

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1gafb2db4ee3af4bedda97f94f263a0fdc7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__gate__input__digital__filter__timebase_1gafb2db4ee3af4bedda97f94f263a0fdc7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_GateWhenRemarksData TypeDescriptionRestrictionsint32Specifies whether the counter gates input pulses while the signal is high or low.Valid valuesDAQmx_Val_High10192High state.DAQmx_Val_Low10214Low state.You can get/set/reset this property using:DAQmxGetCICountEdgesGateWhenD

### DAQmx_CI_CountEdges_GateWhen

#### Syntax

DAQmx_CI_CountEdges_GateWhen

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies whether the counter gates input pulses while the signal is high or low. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_High | 10192 | High state. |
| DAQmx_Val_Low | 10214 | Low state. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesGateWhen](group__ni-daqmx__c__functions__property__manipulation__getter_1ga445532c72a0bbf62b6d6bcca05de6bfe.html)
- [DAQmxSetCICountEdgesGateWhen](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9d90313c0fc86792c43860a4bcb2dc52.html)
- [DAQmxResetCICountEdgesGateWhen](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga6730454bf37709ec3b799e3a9e0ad7ce.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input.html language=enus -->
## TOPIC 01698: Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital FilterDigital SynchronizationGroup membersNameDescriptionDAQmx_CI_CountEdges_HystDAQmx_CI_CountEdges_LogicLvlBehaviorDAQmx_CI_CountEdges_TermDAQmx_CI_CountEdges_TermCfgDAQmx_CI_CountEdges_ThreshVoltageAttachmentsNone

### Input

#### Groups

- Digital Filter
- Digital Synchronization

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_Hyst |  |
| DAQmx_CI_CountEdges_LogicLvlBehavior |  |
| DAQmx_CI_CountEdges_Term |  |
| DAQmx_CI_CountEdges_TermCfg |  |
| DAQmx_CI_CountEdges_ThreshVoltage |  |

#### Attachments

None

Parent topic:

Count Edges

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga0b7e35dca1f83fb0de350f3a93a082ae.html language=enus -->
## TOPIC 01699: DAQmx_CI_CountEdges_Hyst

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga0b7e35dca1f83fb0de350f3a93a082ae.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga0b7e35dca1f83fb0de350f3a93a082ae.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_HystRemarksData TypeDescriptionRestrictionsfloat64Specifies a hysteresis level to apply to Threshold Level. When Active Edge is rising, the source signal must first fall below Threshold Level minus the hysteresis before a rising edge is detected at Threshold Level. When Act

### DAQmx_CI_CountEdges_Hyst

#### Syntax

DAQmx_CI_CountEdges_Hyst

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies a hysteresis level to apply to Threshold Level. When Active Edge is rising, the source signal must first fall below Threshold Level minus the hysteresis before a rising edge is detected at Threshold Level. When Active Edge is falling, the source signal must first rise above Threshold Level plus the hysteresis before a falling edge is detected at Threshold Level. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesHyst](group__ni-daqmx__c__functions__property__manipulation__getter_1ga3f6dda19b8b5a4ff4981877224ab322d.html)
- [DAQmxSetCICountEdgesHyst](group__ni-daqmx__c__functions__property__manipulation__setter_1ga6e28c7a0573a386e5429120146e065ca.html)
- [DAQmxResetCICountEdgesHyst](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga43bfed32421ade2c9948c8719f22af49.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga608bd432e9f15529041059f3b14cde77.html language=enus -->
## TOPIC 01700: DAQmx_CI_CountEdges_Term

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga608bd432e9f15529041059f3b14cde77.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga608bd432e9f15529041059f3b14cde77.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_TermRemarksData TypeDescriptionRestrictionschar*Specifies the input terminal of the signal to measure.You can get/set/reset this property using:DAQmxGetCICountEdgesTermDAQmxSetCICountEdgesTermDAQmxResetCICountEdgesTerm

### DAQmx_CI_CountEdges_Term

#### Syntax

DAQmx_CI_CountEdges_Term

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the input terminal of the signal to measure. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf93fcf828afe66251a3f3d7978d53706.html)
- [DAQmxSetCICountEdgesTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1gacb253cbd06d6ad90c0b85ac765ace3ab.html)
- [DAQmxResetCICountEdgesTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga0fc61de638799839c9ed3359b756a294.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga8855d069ca555ea99b0dd1d572c375e1.html language=enus -->
## TOPIC 01701: DAQmx_CI_CountEdges_ThreshVoltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga8855d069ca555ea99b0dd1d572c375e1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1ga8855d069ca555ea99b0dd1d572c375e1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_ThreshVoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while

### DAQmx_CI_CountEdges_ThreshVoltage

#### Syntax

DAQmx_CI_CountEdges_ThreshVoltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf4e921fbe13440b8f6d508a15f164c6e.html)
- [DAQmxSetCICountEdgesThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1gabc9cc940a481bd20b4fdecb99dc849d5.html)
- [DAQmxResetCICountEdgesThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae2bdca1eb4fc6dd587ef3d316099d92c.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1gaa51db63fdfad60558966580c9ff5b490.html language=enus -->
## TOPIC 01702: DAQmx_CI_CountEdges_TermCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1gaa51db63fdfad60558966580c9ff5b490.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1gaa51db63fdfad60558966580c9ff5b490.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_TermCfgRemarksData TypeDescriptionRestrictionsint32Specifies the input terminal configuration.Valid valuesDAQmx_Val_Diff10106Differential.DAQmx_Val_RSE10083Referenced Single-Ended.You can get/set/reset this property using:DAQmxGetCICountEdgesTermCfgDAQmxSetCICountEdgesTermC

### DAQmx_CI_CountEdges_TermCfg

#### Syntax

DAQmx_CI_CountEdges_TermCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the input terminal configuration. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Diff | 10106 | Differential. |
| DAQmx_Val_RSE | 10083 | Referenced Single-Ended. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesTermCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1ga127e211dc84ee0934692db148b2b6cfa.html)
- [DAQmxSetCICountEdgesTermCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga64bf6f16cef736d351380e11f218eaf9.html)
- [DAQmxResetCICountEdgesTermCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1gabff263b430a4f2b88c0c99bb033b1e95.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1gacca77854fce00eb3e5239c3f3c2d6da1.html language=enus -->
## TOPIC 01703: DAQmx_CI_CountEdges_LogicLvlBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1gacca77854fce00eb3e5239c3f3c2d6da1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input_1gacca77854fce00eb3e5239c3f3c2d6da1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_LogicLvlBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies the logic level behavior on the input line.Valid valuesDAQmx_Val_LogicLevelPullUp16064High logic.DAQmx_Val_None10230Supply no excitation to the channel.You can get/set/reset this property using:DAQmxGetCI

### DAQmx_CI_CountEdges_LogicLvlBehavior

#### Syntax

DAQmx_CI_CountEdges_LogicLvlBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the logic level behavior on the input line. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_LogicLevelPullUp | 16064 | High logic. |
| DAQmx_Val_None | 10230 | Supply no excitation to the channel. |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1gaeedbd9853c20f15f89ec4ee1ede66ace.html)
- [DAQmxSetCICountEdgesLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9f45d3a814c26034d77636efd92132f0.html)
- [DAQmxResetCICountEdgesLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1gad177bc209ce67df6e0bd9e6c97c8ee2a.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter.html language=enus -->
## TOPIC 01704: Digital Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimebaseGroup membersNameDescriptionDAQmx_CI_CountEdges_DigFltr_EnableDAQmx_CI_CountEdges_DigFltr_MinPulseWidthAttachmentsNone

### Digital Filter

#### Groups

- Timebase

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_DigFltr_Enable |  |
| DAQmx_CI_CountEdges_DigFltr_MinPulseWidth |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter_1ga27d5d34f043b5ba22bcf2829e465dcd5.html language=enus -->
## TOPIC 01705: DAQmx_CI_CountEdges_DigFltr_MinPulseWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter_1ga27d5d34f043b5ba22bcf2829e465dcd5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter_1ga27d5d34f043b5ba22bcf2829e465dcd5.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_DigFltr_MinPulseWidthRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the minimum pulse width the filter recognizes.You can get/set/reset this property using:DAQmxGetCICountEdgesDigFltrMinPulseWidthDAQmxSetCICountEdgesDigFltrMinPulseWidthDAQmxResetCICountE

### DAQmx_CI_CountEdges_DigFltr_MinPulseWidth

#### Syntax

DAQmx_CI_CountEdges_DigFltr_MinPulseWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the minimum pulse width the filter recognizes. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2352b694ef397d5ceb6a5253e2c46937.html)
- [DAQmxSetCICountEdgesDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1ga397a31c15b1b884c3e1f7e0d6c203415.html)
- [DAQmxResetCICountEdgesDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9965ccb8abca9c87335859342013f317.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter_1gaa6ce7d25312720d34e04916a13c3c073.html language=enus -->
## TOPIC 01706: DAQmx_CI_CountEdges_DigFltr_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter_1gaa6ce7d25312720d34e04916a13c3c073.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter_1gaa6ce7d25312720d34e04916a13c3c073.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_DigFltr_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to apply the pulse width filter to the signal.You can get/set/reset this property using:DAQmxGetCICountEdgesDigFltrEnableDAQmxSetCICountEdgesDigFltrEnableDAQmxResetCICountEdgesDigFltrEnable

### DAQmx_CI_CountEdges_DigFltr_Enable

#### Syntax

DAQmx_CI_CountEdges_DigFltr_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to apply the pulse width filter to the signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga5656b0dfbb3f7fc52678647a7778f16a.html)
- [DAQmxSetCICountEdgesDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gad4e24f9e4f435aae560665e9cdeb7b1e.html)
- [DAQmxResetCICountEdgesDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga073202a7d7a9bb3ce57856d8da524bbd.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase.html language=enus -->
## TOPIC 01707: Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CountEdges_DigFltr_TimebaseRateDAQmx_CI_CountEdges_DigFltr_TimebaseSrcAttachmentsNone

### Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_DigFltr_TimebaseRate |  |
| DAQmx_CI_CountEdges_DigFltr_TimebaseSrc |  |

#### Attachments

None

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase_1gabf169f3f262322715117ee063bc19569.html language=enus -->
## TOPIC 01708: DAQmx_CI_CountEdges_DigFltr_TimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase_1gabf169f3f262322715117ee063bc19569.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase_1gabf169f3f262322715117ee063bc19569.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_DigFltr_TimebaseRateRemarksData TypeDescriptionRestrictionsfloat64Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.You can get/set/reset this property using:DAQmxGetCICountEdgesDigFltrTimebaseRateDAQ

### DAQmx_CI_CountEdges_DigFltr_TimebaseRate

#### Syntax

DAQmx_CI_CountEdges_DigFltr_TimebaseRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__getter_1ga08479166f0e09aea220edc6c4a032337.html)
- [DAQmxSetCICountEdgesDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__setter_1ga49ef5f00d3c5b063000c702f3831c1b3.html)
- [DAQmxResetCICountEdgesDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab98e07109ce95e9fee8c2c0d483cc128.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase_1gaddd1a38e5ad9b6347140a31f5297bb72.html language=enus -->
## TOPIC 01709: DAQmx_CI_CountEdges_DigFltr_TimebaseSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase_1gaddd1a38e5ad9b6347140a31f5297bb72.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__filter__timebase_1gaddd1a38e5ad9b6347140a31f5297bb72.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_DigFltr_TimebaseSrcRemarksData TypeDescriptionRestrictionschar*Specifies the input terminal of the signal to use as the timebase of the pulse width filter.You can get/set/reset this property using:DAQmxGetCICountEdgesDigFltrTimebaseSrcDAQmxSetCICountEdgesDigFltrTimebaseSrcD

### DAQmx_CI_CountEdges_DigFltr_TimebaseSrc

#### Syntax

DAQmx_CI_CountEdges_DigFltr_TimebaseSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1gac720bedaaf6ffef94ca2e76937a01c53.html)
- [DAQmxSetCICountEdgesDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1gaafdb3191a83a98a24fed47bac2481427.html)
- [DAQmxResetCICountEdgesDigFltrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafca725a60f3c61e69cf8e22de1139198.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__synchronization.html language=enus -->
## TOPIC 01710: Digital Synchronization

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__synchronization.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CountEdges_DigSync_EnableAttachmentsNone

### Digital Synchronization

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CountEdges_DigSync_Enable |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__synchronization_1gad9c81752a7d60fa1e6f5449cc4ef69d6.html language=enus -->
## TOPIC 01711: DAQmx_CI_CountEdges_DigSync_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__synchronization_1gad9c81752a7d60fa1e6f5449cc4ef69d6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__count__edges__input__digital__synchronization_1gad9c81752a7d60fa1e6f5449cc4ef69d6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CountEdges_DigSync_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.You can get/set/reset this property using:DAQmxGetCICountEdgesDigSyncEnableDAQmxSetCICountEdgesDigSync

### DAQmx_CI_CountEdges_DigSync_Enable

#### Syntax

DAQmx_CI_CountEdges_DigSync_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |  |

You can get/set/reset this property using:

- [DAQmxGetCICountEdgesDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga63586344569c2980b2a2a8642d3ddccc.html)
- [DAQmxSetCICountEdgesDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gad6dc3e4eb2993ca0b569506484780010.html)
- [DAQmxResetCICountEdgesDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga5ef8be1272dbdf1b7f8fff781e27f528.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle.html language=enus -->
## TOPIC 01712: Duty Cycle

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsInputGroup membersNoneAttachmentsNone

### Duty Cycle

#### Groups

- Input

#### Group members

None

#### Attachments

None

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input.html language=enus -->
## TOPIC 01713: Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital FilterGroup membersNameDescriptionDAQmx_CI_DutyCycle_LogicLvlBehaviorDAQmx_CI_DutyCycle_TermDAQmx_CI_DutyCycle_TermCfgAttachmentsNone

### Input

#### Groups

- Digital Filter

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_DutyCycle_LogicLvlBehavior |  |
| DAQmx_CI_DutyCycle_Term |  |
| DAQmx_CI_DutyCycle_TermCfg |  |

#### Attachments

None

Parent topic:

Duty Cycle

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1ga2d74237ce0bcfcddbc74bfc8368b16c1.html language=enus -->
## TOPIC 01714: DAQmx_CI_DutyCycle_TermCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1ga2d74237ce0bcfcddbc74bfc8368b16c1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1ga2d74237ce0bcfcddbc74bfc8368b16c1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_DutyCycle_TermCfgRemarksData TypeDescriptionRestrictionsint32Specifies the input terminal configuration.Valid valuesDAQmx_Val_Diff10106Differential.DAQmx_Val_RSE10083Referenced Single-Ended.You can get/set/reset this property using:DAQmxGetCIDutyCycleTermCfgDAQmxSetCIDutyCycleTermCfgD

### DAQmx_CI_DutyCycle_TermCfg

#### Syntax

DAQmx_CI_DutyCycle_TermCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the input terminal configuration. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Diff | 10106 | Differential. |
| DAQmx_Val_RSE | 10083 | Referenced Single-Ended. |

You can get/set/reset this property using:

- [DAQmxGetCIDutyCycleTermCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4798f50bced1fbe23713ac6146394f6d.html)
- [DAQmxSetCIDutyCycleTermCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1gad0ea63793add291d846718fde84de3f2.html)
- [DAQmxResetCIDutyCycleTermCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1gadd49f4b100b0c1816443991810597743.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1ga5a0c09a6c4a4fed5d8a5a3a02551453d.html language=enus -->
## TOPIC 01715: DAQmx_CI_DutyCycle_LogicLvlBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1ga5a0c09a6c4a4fed5d8a5a3a02551453d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1ga5a0c09a6c4a4fed5d8a5a3a02551453d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_DutyCycle_LogicLvlBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies the logic level behavior on the input line.Valid valuesDAQmx_Val_LogicLevelPullUp16064High logic.DAQmx_Val_None10230Supply no excitation to the channel.You can get/set/reset this property using:DAQmxGetCID

### DAQmx_CI_DutyCycle_LogicLvlBehavior

#### Syntax

DAQmx_CI_DutyCycle_LogicLvlBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the logic level behavior on the input line. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_LogicLevelPullUp | 16064 | High logic. |
| DAQmx_Val_None | 10230 | Supply no excitation to the channel. |

You can get/set/reset this property using:

- [DAQmxGetCIDutyCycleLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0fcf4b9e9767004269c9ed4899796d91.html)
- [DAQmxSetCIDutyCycleLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1ga83cb0723b33ad0c80fe3d0759961d078.html)
- [DAQmxResetCIDutyCycleLogicLvlBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4492f59517b9bd4f9dfff5b3f9ff3fd1.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1gac1ce3a3521e7d38490bbe35328564878.html language=enus -->
## TOPIC 01716: DAQmx_CI_DutyCycle_Term

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1gac1ce3a3521e7d38490bbe35328564878.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input_1gac1ce3a3521e7d38490bbe35328564878.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_DutyCycle_TermRemarksData TypeDescriptionRestrictionschar*Specifies the input terminal of the signal to measure.You can get/set/reset this property using:DAQmxGetCIDutyCycleTermDAQmxSetCIDutyCycleTermDAQmxResetCIDutyCycleTerm

### DAQmx_CI_DutyCycle_Term

#### Syntax

DAQmx_CI_DutyCycle_Term

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the input terminal of the signal to measure. |  |

You can get/set/reset this property using:

- [DAQmxGetCIDutyCycleTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7f615a88eb450d40aaf590c476407a69.html)
- [DAQmxSetCIDutyCycleTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1gaabacd86bb7350f4640e7fe3b55f07f5e.html)
- [DAQmxResetCIDutyCycleTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf6c49360011bad8ffdab3895df577692.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter.html language=enus -->
## TOPIC 01717: Digital Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimebaseGroup membersNameDescriptionDAQmx_CI_DutyCycle_DigFltr_EnableDAQmx_CI_DutyCycle_DigFltr_MinPulseWidthAttachmentsNone

### Digital Filter

#### Groups

- Timebase

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_DutyCycle_DigFltr_Enable |  |
| DAQmx_CI_DutyCycle_DigFltr_MinPulseWidth |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter_1ga18adac8a273a79b7c785d8c913ffbcaf.html language=enus -->
## TOPIC 01718: DAQmx_CI_DutyCycle_DigFltr_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter_1ga18adac8a273a79b7c785d8c913ffbcaf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter_1ga18adac8a273a79b7c785d8c913ffbcaf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_DutyCycle_DigFltr_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to apply the pulse width filter to the signal.You can get/set/reset this property using:DAQmxGetCIDutyCycleDigFltrEnableDAQmxSetCIDutyCycleDigFltrEnableDAQmxResetCIDutyCycleDigFltrEnable

### DAQmx_CI_DutyCycle_DigFltr_Enable

#### Syntax

DAQmx_CI_DutyCycle_DigFltr_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to apply the pulse width filter to the signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCIDutyCycleDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1gab3b622f70fbfef8a09afbd0ae3f62ffa.html)
- [DAQmxSetCIDutyCycleDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga6e051d32acec329e136f5e53c6b675ba.html)
- [DAQmxResetCIDutyCycleDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf63a547390e06f63c865f0f70fddcbc9.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter_1ga71a76ea901a0bacd6dc4677ccaa0c6b2.html language=enus -->
## TOPIC 01719: DAQmx_CI_DutyCycle_DigFltr_MinPulseWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter_1ga71a76ea901a0bacd6dc4677ccaa0c6b2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter_1ga71a76ea901a0bacd6dc4677ccaa0c6b2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_DutyCycle_DigFltr_MinPulseWidthRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the minimum pulse width the digital filter recognizes.You can get/set/reset this property using:DAQmxGetCIDutyCycleDigFltrMinPulseWidthDAQmxSetCIDutyCycleDigFltrMinPulseWidthDAQmxResetCID

### DAQmx_CI_DutyCycle_DigFltr_MinPulseWidth

#### Syntax

DAQmx_CI_DutyCycle_DigFltr_MinPulseWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the minimum pulse width the digital filter recognizes. |  |

You can get/set/reset this property using:

- [DAQmxGetCIDutyCycleDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1de0620eef91b34713be7318e9bcd9c3.html)
- [DAQmxSetCIDutyCycleDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1gacfde2147fa98591cc0d46c857ae561ff.html)
- [DAQmxResetCIDutyCycleDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga7b8a4c55c1b2f664565c625fbca3c8e3.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase.html language=enus -->
## TOPIC 01720: Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_DutyCycle_DigFltr_TimebaseRateDAQmx_CI_DutyCycle_DigFltr_TimebaseSrcDAQmx_CI_DutyCycle_StartingEdgeAttachmentsNone

### Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_DutyCycle_DigFltr_TimebaseRate |  |
| DAQmx_CI_DutyCycle_DigFltr_TimebaseSrc |  |
| DAQmx_CI_DutyCycle_StartingEdge |  |

#### Attachments

None

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase_1ga371cf60d1ebb5c6fe65da140d34903d1.html language=enus -->
## TOPIC 01721: DAQmx_CI_DutyCycle_StartingEdge

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase_1ga371cf60d1ebb5c6fe65da140d34903d1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase_1ga371cf60d1ebb5c6fe65da140d34903d1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_DutyCycle_StartingEdgeRemarksData TypeDescriptionRestrictionsint32Specifies which edge of the input signal to begin the duty cycle measurement.Valid valuesDAQmx_Val_Rising10280Rising edge(s).DAQmx_Val_Falling10171Falling edge(s).You can get/set/reset this property using:DAQmxGetCIDuty

### DAQmx_CI_DutyCycle_StartingEdge

#### Syntax

DAQmx_CI_DutyCycle_StartingEdge

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies which edge of the input signal to begin the duty cycle measurement. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Rising | 10280 | Rising edge(s). |
| DAQmx_Val_Falling | 10171 | Falling edge(s). |

You can get/set/reset this property using:

- [DAQmxGetCIDutyCycleStartingEdge](group__ni-daqmx__c__functions__property__manipulation__getter_1ga04c9364aeb31feb560c7c2979e113cb9.html)
- [DAQmxSetCIDutyCycleStartingEdge](group__ni-daqmx__c__functions__property__manipulation__setter_1ga822e54c9aaa012519ec3fe6cc939c0c7.html)
- [DAQmxResetCIDutyCycleStartingEdge](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga3fe8ae0b23a2149ebf145d5f9d78049d.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase_1gac8b7e575289c83663802ddc84c63ff5b.html language=enus -->
## TOPIC 01722: DAQmx_CI_DutyCycle_DigFltr_TimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase_1gac8b7e575289c83663802ddc84c63ff5b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__duty__cycle__input__digital__filter__timebase_1gac8b7e575289c83663802ddc84c63ff5b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_DutyCycle_DigFltr_TimebaseRateRemarksData TypeDescriptionRestrictionsfloat64Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.You can get/set/reset this property using:DAQmxGetCIDutyCycleDigFltrTimebaseRateDAQmx

### DAQmx_CI_DutyCycle_DigFltr_TimebaseRate

#### Syntax

DAQmx_CI_DutyCycle_DigFltr_TimebaseRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCIDutyCycleDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__getter_1gabc025cee7bd880f0c4517f5d04a83467.html)
- [DAQmxSetCIDutyCycleDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__setter_1ga554989445f3ef2c26b20275eac3331ba.html)
- [DAQmxResetCIDutyCycleDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__resetter_1gac1d3497a147a9705df646f218e8779f5.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency_1ga3798d0624630921753b4d5ae7e7ea708.html language=enus -->
## TOPIC 01723: DAQmx_CI_Freq_Units

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency_1ga3798d0624630921753b4d5ae7e7ea708.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency_1ga3798d0624630921753b4d5ae7e7ea708.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_UnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units to use to return frequency measurements.Valid valuesDAQmx_Val_Hz10373Hertz.DAQmx_Val_Ticks10304Timebase ticks.DAQmx_Val_FromCustomScale10065Units a custom scale specifies. If you select this value, you must spec

### DAQmx_CI_Freq_Units

#### Syntax

DAQmx_CI_Freq_Units

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units to use to return frequency measurements. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Hz | 10373 | Hertz. |
| DAQmx_Val_Ticks | 10304 | Timebase ticks. |
| DAQmx_Val_FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

You can get/set/reset this property using:

- [DAQmxGetCIFreqUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1gaacd06e8fb404d960fc694142d410aaac.html)
- [DAQmxSetCIFreqUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1ga6c61f7d1625c7b169781b8cf6d3788cb.html)
- [DAQmxResetCIFreqUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga12435a2fd21a68e0fb3b39caa39e6682.html)

Parent topic:

Frequency

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input.html language=enus -->
## TOPIC 01724: Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital FilterDigital SynchronizationGroup membersNameDescriptionDAQmx_CI_Freq_HystDAQmx_CI_Freq_LogicLvlBehaviorDAQmx_CI_Freq_TermDAQmx_CI_Freq_TermCfgDAQmx_CI_Freq_ThreshVoltageAttachmentsNone

### Input

#### Groups

- Digital Filter
- Digital Synchronization

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_Freq_Hyst |  |
| DAQmx_CI_Freq_LogicLvlBehavior |  |
| DAQmx_CI_Freq_Term |  |
| DAQmx_CI_Freq_TermCfg |  |
| DAQmx_CI_Freq_ThreshVoltage |  |

#### Attachments

None

Parent topic:

Frequency

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1ga699a2a8505a00209b288add21d128015.html language=enus -->
## TOPIC 01725: DAQmx_CI_Freq_Hyst

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1ga699a2a8505a00209b288add21d128015.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1ga699a2a8505a00209b288add21d128015.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_HystRemarksData TypeDescriptionRestrictionsfloat64Specifies a hysteresis level to apply to Threshold Level. When Starting Edge is rising, the source signal must first fall below Threshold Level minus the hysteresis before a rising edge is detected at Threshold Level. When Startin

### DAQmx_CI_Freq_Hyst

#### Syntax

DAQmx_CI_Freq_Hyst

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies a hysteresis level to apply to Threshold Level. When Starting Edge is rising, the source signal must first fall below Threshold Level minus the hysteresis before a rising edge is detected at Threshold Level. When Starting Edge is falling, the source signal must first rise above Threshold Level plus the hysteresis before a falling edge is detected at Threshold Level. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqHyst](group__ni-daqmx__c__functions__property__manipulation__getter_1gafe8436b1e54e61d296931da627a5f866.html)
- [DAQmxSetCIFreqHyst](group__ni-daqmx__c__functions__property__manipulation__setter_1gabe537300a017915355bb77df2ee10cc4.html)
- [DAQmxResetCIFreqHyst](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga42d35af28fa06c2315616ea8f630f2af.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1ga78853ef5d8b4a59dae91b6ca6db59a06.html language=enus -->
## TOPIC 01726: DAQmx_CI_Freq_TermCfg

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1ga78853ef5d8b4a59dae91b6ca6db59a06.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1ga78853ef5d8b4a59dae91b6ca6db59a06.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_TermCfgRemarksData TypeDescriptionRestrictionsint32Specifies the input terminal configuration.Valid valuesDAQmx_Val_Diff10106Differential.DAQmx_Val_RSE10083Referenced Single-Ended.You can get/set/reset this property using:DAQmxGetCIFreqTermCfgDAQmxSetCIFreqTermCfgDAQmxResetCIFreq

### DAQmx_CI_Freq_TermCfg

#### Syntax

DAQmx_CI_Freq_TermCfg

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the input terminal configuration. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Diff | 10106 | Differential. |
| DAQmx_Val_RSE | 10083 | Referenced Single-Ended. |

You can get/set/reset this property using:

- [DAQmxGetCIFreqTermCfg](group__ni-daqmx__c__functions__property__manipulation__getter_1gab18f93f3b0e8aa1c3f504ee26db584ab.html)
- [DAQmxSetCIFreqTermCfg](group__ni-daqmx__c__functions__property__manipulation__setter_1ga17fdea79b6091757c6503dfda9adf468.html)
- [DAQmxResetCIFreqTermCfg](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaed02ae65df4cf262b5cdd00bc8a62c15.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1gae9aa0e0b26b82fdcccfc8f9c770243e9.html language=enus -->
## TOPIC 01727: DAQmx_CI_Freq_ThreshVoltage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1gae9aa0e0b26b82fdcccfc8f9c770243e9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input_1gae9aa0e0b26b82fdcccfc8f9c770243e9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_ThreshVoltageRemarksData TypeDescriptionRestrictionsfloat64Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the vo

### DAQmx_CI_Freq_ThreshVoltage

#### Syntax

DAQmx_CI_Freq_ThreshVoltage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__getter_1gac49f020db81a7c1a27176bec3ee2d9cd.html)
- [DAQmxSetCIFreqThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3669ec0f1bb9ab2d25587e3db2be020b.html)
- [DAQmxResetCIFreqThreshVoltage](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf43f9d8a687a0c2044cb970fa0eef7ff.html)

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter.html language=enus -->
## TOPIC 01728: Digital Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimebaseGroup membersNameDescriptionDAQmx_CI_Freq_DigFltr_EnableDAQmx_CI_Freq_DigFltr_MinPulseWidthAttachmentsNone

### Digital Filter

#### Groups

- Timebase

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_Freq_DigFltr_Enable |  |
| DAQmx_CI_Freq_DigFltr_MinPulseWidth |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter_1gabb8cbe70aa48bb64b823a626913f0a1c.html language=enus -->
## TOPIC 01729: DAQmx_CI_Freq_DigFltr_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter_1gabb8cbe70aa48bb64b823a626913f0a1c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter_1gabb8cbe70aa48bb64b823a626913f0a1c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_DigFltr_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to apply the pulse width filter to the signal.You can get/set/reset this property using:DAQmxGetCIFreqDigFltrEnableDAQmxSetCIFreqDigFltrEnableDAQmxResetCIFreqDigFltrEnable

### DAQmx_CI_Freq_DigFltr_Enable

#### Syntax

DAQmx_CI_Freq_DigFltr_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to apply the pulse width filter to the signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga77d4773acdd0c158aced27d2d92068ea.html)
- [DAQmxSetCIFreqDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga96d5fb0654fb18fe0d0140a9d177e102.html)
- [DAQmxResetCIFreqDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4b7700fa40e28a5efdf6762a35063561.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter__timebase.html language=enus -->
## TOPIC 01730: Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_Freq_DigFltr_TimebaseRateDAQmx_CI_Freq_DigFltr_TimebaseSrcAttachmentsNone

### Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_Freq_DigFltr_TimebaseRate |  |
| DAQmx_CI_Freq_DigFltr_TimebaseSrc |  |

#### Attachments

None

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter__timebase_1gad5d365ad8a9b1d21b5d94efcb5931148.html language=enus -->
## TOPIC 01731: DAQmx_CI_Freq_DigFltr_TimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter__timebase_1gad5d365ad8a9b1d21b5d94efcb5931148.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__filter__timebase_1gad5d365ad8a9b1d21b5d94efcb5931148.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_DigFltr_TimebaseRateRemarksData TypeDescriptionRestrictionsfloat64Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.You can get/set/reset this property using:DAQmxGetCIFreqDigFltrTimebaseRateDAQmxSetCIFreqD

### DAQmx_CI_Freq_DigFltr_TimebaseRate

#### Syntax

DAQmx_CI_Freq_DigFltr_TimebaseRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2735bdfccb0a50003f1674e036ef73e7.html)
- [DAQmxSetCIFreqDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__setter_1gad962493d100d0c0e1582c61f20e8fa8a.html)
- [DAQmxResetCIFreqDigFltrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__resetter_1gace1fb95d2cc09739ea870b91c43f9ca7.html)

Parent topic:

Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization.html language=enus -->
## TOPIC 01732: Digital Synchronization

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_Freq_DigSync_EnableDAQmx_CI_Freq_StartingEdgeAttachmentsNone

### Digital Synchronization

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_Freq_DigSync_Enable |  |
| DAQmx_CI_Freq_StartingEdge |  |

#### Attachments

None

Parent topic:

Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization_1ga8927d2031c4edf5a8bc72cf0936209d4.html language=enus -->
## TOPIC 01733: DAQmx_CI_Freq_DigSync_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization_1ga8927d2031c4edf5a8bc72cf0936209d4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization_1ga8927d2031c4edf5a8bc72cf0936209d4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_DigSync_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.You can get/set/reset this property using:DAQmxGetCIFreqDigSyncEnableDAQmxSetCIFreqDigSyncEnableDAQmxResetCI

### DAQmx_CI_Freq_DigSync_Enable

#### Syntax

DAQmx_CI_Freq_DigSync_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf62176fd12065b853989ec0545bb93af.html)
- [DAQmxSetCIFreqDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gab15af0e3385a39968b705a13b8862c46.html)
- [DAQmxResetCIFreqDigSyncEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4b435f9e5b92e3b4c82db4611a3cc48a.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization_1ga8e579dd034f1cb2e0755ea298c9b3463.html language=enus -->
## TOPIC 01734: DAQmx_CI_Freq_StartingEdge

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization_1ga8e579dd034f1cb2e0755ea298c9b3463.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__input__digital__synchronization_1ga8e579dd034f1cb2e0755ea298c9b3463.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_StartingEdgeRemarksData TypeDescriptionRestrictionsint32Specifies between which edges to measure the frequency of the signal.Valid valuesDAQmx_Val_Rising10280Rising edge(s).DAQmx_Val_Falling10171Falling edge(s).You can get/set/reset this property using:DAQmxGetCIFreqStartingEdgeD

### DAQmx_CI_Freq_StartingEdge

#### Syntax

DAQmx_CI_Freq_StartingEdge

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies between which edges to measure the frequency of the signal. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Rising | 10280 | Rising edge(s). |
| DAQmx_Val_Falling | 10171 | Falling edge(s). |

You can get/set/reset this property using:

- [DAQmxGetCIFreqStartingEdge](group__ni-daqmx__c__functions__property__manipulation__getter_1ga74dbebe1ce5e5ddc02e8b5eb9492e3d2.html)
- [DAQmxSetCIFreqStartingEdge](group__ni-daqmx__c__functions__property__manipulation__setter_1ga30ade65d8459fe4ea033e5502ed1bf31.html)
- [DAQmxResetCIFreqStartingEdge](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga3d9423b2766dda05e37a8f179eed20ea.html)

Parent topic:

Digital Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications.html language=enus -->
## TOPIC 01735: Measurement Specifications

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsHigh FrequencyLarge RangeGroup membersNameDescriptionDAQmx_CI_Freq_EnableAveragingDAQmx_CI_Freq_MeasMethAttachmentsNone

### Measurement Specifications

#### Groups

- High Frequency
- Large Range

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_Freq_EnableAveraging |  |
| DAQmx_CI_Freq_MeasMeth |  |

#### Attachments

None

Parent topic:

Frequency

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications_1gaae6a3753bf59dd39e3e142ddc05ed185.html language=enus -->
## TOPIC 01736: DAQmx_CI_Freq_EnableAveraging

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications_1gaae6a3753bf59dd39e3e142ddc05ed185.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications_1gaae6a3753bf59dd39e3e142ddc05ed185.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_EnableAveragingRemarksData TypeDescriptionRestrictionsbool32Specifies whether to enable averaging mode for Sample Clock-timed frequency measurements.You can get/set/reset this property using:DAQmxGetCIFreqEnableAveragingDAQmxSetCIFreqEnableAveragingDAQmxResetCIFreqEnableAveraging

### DAQmx_CI_Freq_EnableAveraging

#### Syntax

DAQmx_CI_Freq_EnableAveraging

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to enable averaging mode for Sample Clock-timed frequency measurements. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqEnableAveraging](group__ni-daqmx__c__functions__property__manipulation__getter_1gadc4bb1105561359986fbb29100d71660.html)
- [DAQmxSetCIFreqEnableAveraging](group__ni-daqmx__c__functions__property__manipulation__setter_1ga762b57bca30529a09ef5a123c9270767.html)
- [DAQmxResetCIFreqEnableAveraging](group__ni-daqmx__c__functions__property__manipulation__resetter_1gac7a438264beebb40b7ef9a99912ee606.html)

Parent topic:

Measurement Specifications

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications_1gac25cf6c76f2de88cea618ae6ab05d976.html language=enus -->
## TOPIC 01737: DAQmx_CI_Freq_MeasMeth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications_1gac25cf6c76f2de88cea618ae6ab05d976.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications_1gac25cf6c76f2de88cea618ae6ab05d976.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_MeasMethRemarksData TypeDescriptionRestrictionsint32Specifies the method to use to measure the frequency of the signal.Valid valuesDAQmx_Val_LowFreq1Ctr10105Use one counter that uses a constant timebase to measure the input signal.DAQmx_Val_HighFreq2Ctr10157Use two counters, one

### DAQmx_CI_Freq_MeasMeth

#### Syntax

DAQmx_CI_Freq_MeasMeth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the method to use to measure the frequency of the signal. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_LowFreq1Ctr | 10105 | Use one counter that uses a constant timebase to measure the input signal. |
| DAQmx_Val_HighFreq2Ctr | 10157 | Use two counters, one of which counts pulses of the signal to measure during the specified measurement time. |
| DAQmx_Val_LargeRng2Ctr | 10205 | Use one counter to divide the frequency of the input signal to create a lower-frequency signal that the second counter can more easily measure. |
| DAQmx_Val_DynAvg | 16065 | Uses one counter with configuration options to control the amount of averaging or filtering applied to the counter measurements. Set filtering options to balance measurement accuracy and noise versus latency. |

You can get/set/reset this property using:

- [DAQmxGetCIFreqMeasMeth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga03ec26b60c50cba3f7dda45dc6b446b1.html)
- [DAQmxSetCIFreqMeasMeth](group__ni-daqmx__c__functions__property__manipulation__setter_1ga33a002029bdd6a0eddddb3e8a1280930.html)
- [DAQmxResetCIFreqMeasMeth](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga89441249355d8279ab556e64d79610e2.html)

Parent topic:

Measurement Specifications

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__high__frequency.html language=enus -->
## TOPIC 01738: High Frequency

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__high__frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__high__frequency.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_Freq_MeasTimeAttachmentsNone

### High Frequency

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_Freq_MeasTime |  |

#### Attachments

None

Parent topic:

Measurement Specifications

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__high__frequency_1gacb62a9e7a6cd8d8a7f389f93a4ce31a7.html language=enus -->
## TOPIC 01739: DAQmx_CI_Freq_MeasTime

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__high__frequency_1gacb62a9e7a6cd8d8a7f389f93a4ce31a7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__high__frequency_1gacb62a9e7a6cd8d8a7f389f93a4ce31a7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_MeasTimeRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the length of time to measure the frequency of the signal if Method is DAQmx_Val_HighFreq2Ctr. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you mea

### DAQmx_CI_Freq_MeasTime

#### Syntax

DAQmx_CI_Freq_MeasTime

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the length of time to measure the frequency of the signal if Method is DAQmx_Val_HighFreq2Ctr. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqMeasTime](group__ni-daqmx__c__functions__property__manipulation__getter_1gaacdb76e2c752b9a672fba04f2a84396c.html)
- [DAQmxSetCIFreqMeasTime](group__ni-daqmx__c__functions__property__manipulation__setter_1gafe8c1ecd6832f01856791fcdbead82e2.html)
- [DAQmxResetCIFreqMeasTime](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga98cfc07e7290193ecac95618c60515fb.html)

Parent topic:

High Frequency

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__large__range.html language=enus -->
## TOPIC 01740: Large Range

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__large__range.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__large__range.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_Freq_DivAttachmentsNone

### Large Range

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_Freq_Div |  |

#### Attachments

None

Parent topic:

Measurement Specifications

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__large__range_1gad2449e9d2df3590fee4c07e3c72fd7f1.html language=enus -->
## TOPIC 01741: DAQmx_CI_Freq_Div

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__large__range_1gad2449e9d2df3590fee4c07e3c72fd7f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__frequency__measurement__specifications__large__range_1gad2449e9d2df3590fee4c07e3c72fd7f1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_Freq_DivRemarksData TypeDescriptionRestrictionsuInt32Specifies the value by which to divide the input signal if Method is DAQmx_Val_LargeRng2Ctr. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which re

### DAQmx_CI_Freq_Div

#### Syntax

DAQmx_CI_Freq_Div

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies the value by which to divide the input signal if Method is DAQmx_Val_LargeRng2Ctr. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement. |  |

You can get/set/reset this property using:

- [DAQmxGetCIFreqDiv](group__ni-daqmx__c__functions__property__manipulation__getter_1gac23999f890f085e7da39f81427858cce.html)
- [DAQmxSetCIFreqDiv](group__ni-daqmx__c__functions__property__manipulation__setter_1gabfc958b725dfcb69a0bdc0b8ce65f7ef.html)
- [DAQmxResetCIFreqDiv](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab7d87ec7759dec635e4f63f02639ed19.html)

Parent topic:

Large Range

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties.html language=enus -->
## TOPIC 01742: General Properties

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCounter TimebaseFilterInput ConfigurationMoreGroup membersNoneAttachmentsNone

### General Properties

#### Groups

- Counter Timebase
- Filter
- Input Configuration
- More

#### Group members

None

#### Attachments

None

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase.html language=enus -->
## TOPIC 01743: Counter Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital FilterDigital SynchronizationGroup membersNameDescriptionDAQmx_CI_CtrTimebaseActiveEdgeDAQmx_CI_CtrTimebaseRateDAQmx_CI_CtrTimebaseSrcAttachmentsNone

### Counter Timebase

#### Groups

- Digital Filter
- Digital Synchronization

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CtrTimebaseActiveEdge |  |
| DAQmx_CI_CtrTimebaseRate |  |
| DAQmx_CI_CtrTimebaseSrc |  |

#### Attachments

None

Parent topic:

General Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1ga33be5e03e6a69a84743307dcbb8c2753.html language=enus -->
## TOPIC 01744: DAQmx_CI_CtrTimebaseRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1ga33be5e03e6a69a84743307dcbb8c2753.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1ga33be5e03e6a69a84743307dcbb8c2753.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CtrTimebaseRateRemarksData TypeDescriptionRestrictionsfloat64Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to take measurements in terms of time or frequency rather than in ticks of the timebase. If you use an external t

### DAQmx_CI_CtrTimebaseRate

#### Syntax

DAQmx_CI_CtrTimebaseRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to take measurements in terms of time or frequency rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can take measurements only in terms of ticks of the timebase. |  |

You can get/set/reset this property using:

- [DAQmxGetCICtrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__getter_1gad3774b1c256d43458685b63efa96e724.html)
- [DAQmxSetCICtrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__setter_1gac5c25a22c0cc0a3a13a19e00e682fc2e.html)
- [DAQmxResetCICtrTimebaseRate](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga00f8046550881f34dbbd6c90bf690d01.html)

Parent topic:

Counter Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1ga8479b3bbc1d62ff4e95c3567f60c74cd.html language=enus -->
## TOPIC 01745: DAQmx_CI_CtrTimebaseActiveEdge

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1ga8479b3bbc1d62ff4e95c3567f60c74cd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1ga8479b3bbc1d62ff4e95c3567f60c74cd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CtrTimebaseActiveEdgeRemarksData TypeDescriptionRestrictionsint32Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge.Valid valuesDAQmx_Val_Rising10280Rising edge(s).DAQmx_Val_Falling10171Falling edge(s).You can get/set/reset this

### DAQmx_CI_CtrTimebaseActiveEdge

#### Syntax

DAQmx_CI_CtrTimebaseActiveEdge

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Rising | 10280 | Rising edge(s). |
| DAQmx_Val_Falling | 10171 | Falling edge(s). |

You can get/set/reset this property using:

- [DAQmxGetCICtrTimebaseActiveEdge](group__ni-daqmx__c__functions__property__manipulation__getter_1gacb6e5787bcf5d06c650145b0522ed8a2.html)
- [DAQmxSetCICtrTimebaseActiveEdge](group__ni-daqmx__c__functions__property__manipulation__setter_1ga98f47cda84384b74c0464df9a1ac9cb6.html)
- [DAQmxResetCICtrTimebaseActiveEdge](group__ni-daqmx__c__functions__property__manipulation__resetter_1gacb274fc22e9d61b9b2fbcf8346202725.html)

Parent topic:

Counter Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1gac894bcf52f0b832eeea8c6777c97deb3.html language=enus -->
## TOPIC 01746: DAQmx_CI_CtrTimebaseSrc

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1gac894bcf52f0b832eeea8c6777c97deb3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase_1gac894bcf52f0b832eeea8c6777c97deb3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CtrTimebaseSrcRemarksData TypeDescriptionRestrictionschar*Specifies the terminal of the timebase to use for the counter.You can get/set/reset this property using:DAQmxGetCICtrTimebaseSrcDAQmxSetCICtrTimebaseSrcDAQmxResetCICtrTimebaseSrc

### DAQmx_CI_CtrTimebaseSrc

#### Syntax

DAQmx_CI_CtrTimebaseSrc

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the terminal of the timebase to use for the counter. |  |

You can get/set/reset this property using:

- [DAQmxGetCICtrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__getter_1ga217ccc088389fd726603fc8fb448c81b.html)
- [DAQmxSetCICtrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa139f1d697050d0476f78cc56a822ec5.html)
- [DAQmxResetCICtrTimebaseSrc](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga13b14d78590f1e75856ef3afacec72a0.html)

Parent topic:

Counter Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter.html language=enus -->
## TOPIC 01747: Digital Filter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimebaseGroup membersNameDescriptionDAQmx_CI_CtrTimebase_DigFltr_EnableDAQmx_CI_CtrTimebase_DigFltr_MinPulseWidthAttachmentsNone

### Digital Filter

#### Groups

- Timebase

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CtrTimebase_DigFltr_Enable |  |
| DAQmx_CI_CtrTimebase_DigFltr_MinPulseWidth |  |

#### Attachments

None

Parent topic:

Counter Timebase

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter_1ga86031643ab836a1fd9df81fe1f25faa0.html language=enus -->
## TOPIC 01748: DAQmx_CI_CtrTimebase_DigFltr_MinPulseWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter_1ga86031643ab836a1fd9df81fe1f25faa0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter_1ga86031643ab836a1fd9df81fe1f25faa0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CtrTimebase_DigFltr_MinPulseWidthRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the minimum pulse width the filter recognizes.You can get/set/reset this property using:DAQmxGetCICtrTimebaseDigFltrMinPulseWidthDAQmxSetCICtrTimebaseDigFltrMinPulseWidthDAQmxResetCICtr

### DAQmx_CI_CtrTimebase_DigFltr_MinPulseWidth

#### Syntax

DAQmx_CI_CtrTimebase_DigFltr_MinPulseWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the minimum pulse width the filter recognizes. |  |

You can get/set/reset this property using:

- [DAQmxGetCICtrTimebaseDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1gab6340d4c5f43995af666cb64530fe8de.html)
- [DAQmxSetCICtrTimebaseDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1gaba58063d5f437f7d3d051a142a3f0a16.html)
- [DAQmxResetCICtrTimebaseDigFltrMinPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab91e9b448015143dcaf923cfa4938b27.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter_1gaa0fbd0eb07fdb6b7ded8eb95aa283009.html language=enus -->
## TOPIC 01749: DAQmx_CI_CtrTimebase_DigFltr_Enable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter_1gaa0fbd0eb07fdb6b7ded8eb95aa283009.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter_1gaa0fbd0eb07fdb6b7ded8eb95aa283009.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_CI_CtrTimebase_DigFltr_EnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to apply the pulse width filter to the signal.You can get/set/reset this property using:DAQmxGetCICtrTimebaseDigFltrEnableDAQmxSetCICtrTimebaseDigFltrEnableDAQmxResetCICtrTimebaseDigFltrEnable

### DAQmx_CI_CtrTimebase_DigFltr_Enable

#### Syntax

DAQmx_CI_CtrTimebase_DigFltr_Enable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to apply the pulse width filter to the signal. |  |

You can get/set/reset this property using:

- [DAQmxGetCICtrTimebaseDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga30930f9c9d42f2a1205b412be46251dc.html)
- [DAQmxSetCICtrTimebaseDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga58f9462063e55fe7d3b5fcb70648e351.html)
- [DAQmxResetCICtrTimebaseDigFltrEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafdf185e86f354e2f0e9c0a961196661c.html)

Parent topic:

Digital Filter

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter__timebase.html language=enus -->
## TOPIC 01750: Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__channel__counter__input__general__properties__counter__timebase__digital__filter__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_CI_CtrTimebase_DigFltr_TimebaseRateDAQmx_CI_CtrTimebase_DigFltr_TimebaseSrcAttachmentsNone

### Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_CI_CtrTimebase_DigFltr_TimebaseRate |  |
| DAQmx_CI_CtrTimebase_DigFltr_TimebaseSrc |  |

#### Attachments

None

Parent topic:

Digital Filter
