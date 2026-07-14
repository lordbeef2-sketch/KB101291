# NI DOCUMENT BUNDLE: ni-dcpower-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-csharp-api-ref start=251 end=451 -->
<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance.html language=enus -->
## TOPIC 00251: DCPowerOutputSourceConstantResistance Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceconstantresistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties that change channel settings when the channel is configured for ConstantResistance. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceConstantResistance : DCPowerSubObjectRemarksFor more information, refer

### DCPowerOutputSourceConstantResistance Class

Contains properties that change channel settings when the channel is configured for [ConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceConstantResistance : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Properties

| Name | Description |
| --- | --- |
| CurrentLimit | Specifies the current limit, in amps, that the output cannot exceed when generating the desired resistance level on the specified channel(s). |
| Level | Specifies the resistance level, in ohms, that the device attempts to generate on the specified channel(s). |
| LevelRange | Specifies the resistance level range, in ohms, for the specified channel(s). |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevel.html language=enus -->
## TOPIC 00252: CurrentLevel

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevel.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the current level, in amperes, that the specified channel(s) attempt to generate. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentLevel { get; set; }RemarksThe valid values for this property are defined by the values you specify for the CurrentLevel

### CurrentLevel

Gets or sets the current level, in amperes, that the specified channel(s) attempt to generate.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentLevel { get; set; }

#### Remarks

The valid values for this property are defined by the values you specify for the [CurrentLevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelrange.html) property.

CurrentLevel

Function

DCCurrent

Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Parent topic:

DCPowerOutputSourceCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelautorange.html language=enus -->
## TOPIC 00253: CurrentLevelAutorange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelautorange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to automatically select the current level range based on the desired current level for the specified channels. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceCurrentLevelAutorange CurrentLevelAutorange { get; set; }RemarksSpecifies an object

### CurrentLevelAutorange

Gets or sets whether to automatically select the current level range based on the desired current level for the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceCurrentLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecurrentlevelautorange.html) CurrentLevelAutorange { get; set; }

#### Remarks

Specifies an object of type [DCPowerSourceCurrentLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecurrentlevelautorange.html)

If this property is set to [On](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html), NI-DCPower ignores any changes you make to the [CurrentLevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelrange.html) property. If you change the CurrentLevelAutorange property from [On](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html) to [Off](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html), NI-DCPower remembers the last value the [CurrentLevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelrange.html) property was set to, or the default value if the property was never set and uses that value as the current level range. The [DCPowerSourceCurrentLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecurrentlevelautorange.html) property is applicable only if the [DCPowerSourceOutputFunction](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) property is set to [DCCurrent](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

Parent topic:

DCPowerOutputSourceCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelfallingslewrate.html language=enus -->
## TOPIC 00254: CurrentLevelFallingSlewRate

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelfallingslewrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelfallingslewrate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of decrease, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentLevelFallingSlewRate { get; set; }RemarksThe rate of decrease, in amps p

### CurrentLevelFallingSlewRate

Specifies the rate of decrease, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentLevelFallingSlewRate { get; set; }

#### Remarks

The rate of decrease, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).

Function

DCCurrent

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSourceCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelrisingslewrate.html language=enus -->
## TOPIC 00255: CurrentLevelRisingSlewRate

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelrisingslewrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-currentlevelrisingslewrate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of increase, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentLevelRisingSlewRate { get; set; }RemarksThe rate of increase, in amps pe

### CurrentLevelRisingSlewRate

Specifies the rate of increase, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentLevelRisingSlewRate { get; set; }

#### Remarks

The rate of increase, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).

Function

DCCurrent

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSourceCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-voltagelimit.html language=enus -->
## TOPIC 00256: VoltageLimit

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-voltagelimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-voltagelimit.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the voltage limit for the output to not exceed when generating the desired current level on the specified channels. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double VoltageLimit { get; set; }RemarksThe valid values for this property are defined by the value

### VoltageLimit

Gets or sets the voltage limit for the output to not exceed when generating the desired current level on the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double VoltageLimit { get; set; }

#### Remarks

The valid values for this property are defined by the values you specify for the [VoltageLimitRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-voltagelimitrange.html) property.

The VoltageLimit property is applicable only if the [DCPowerSourceOutputFunction](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) property is set to [DCCurrent](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the [DCPowerComplianceLimitSymmetry](nationalinstruments-modularinstruments-nidcpower-dcpowercompliancelimitsymmetry.html) property is set to [Symmetric](nationalinstruments-modularinstruments-nidcpower-dcpowercompliancelimitsymmetry.html).

The channel must be enabled for the specified voltage limit to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourceCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-voltagelimitautorange.html language=enus -->
## TOPIC 00257: VoltageLimitAutorange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-voltagelimitautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecurrent-voltagelimitautorange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to automatically select the voltage limit range based on the desired voltage limit for the specified channels. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceVoltageLimitAutorange VoltageLimitAutorange { get; set; }RemarksSpecifies an object

### VoltageLimitAutorange

Gets or sets whether to automatically select the voltage limit range based on the desired voltage limit for the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceVoltageLimitAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelimitautorange.html) VoltageLimitAutorange { get; set; }

#### Remarks

Specifies an object of type [DCPowerSourceVoltageLimitAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelimitautorange.html).

On

VoltageLimitRange

On

Off

VoltageLimitRange

VoltageLimitAutorange

DCCurrent

Function

Parent topic:

DCPowerOutputSourceCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponse-constantpower.html language=enus -->
## TOPIC 00258: ConstantPower

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponse-constantpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponse-constantpower.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DCPowerOutputSourceCustomTransientResponseConstantPower sub-object used to configure the constant power custom transient response properties of source unit channel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourceCustomTransientResponseConstan

### ConstantPower

Specifies the [DCPowerOutputSourceCustomTransientResponseConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower.html) sub-object used to configure the constant power custom transient response properties of source unit channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourceCustomTransientResponseConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower.html) ConstantPower { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourceCustomTransientResponseConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower.html).

Parent topic:

DCPowerOutputSourceCustomTransientResponse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponse-constantresistance.html language=enus -->
## TOPIC 00259: ConstantResistance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponse-constantresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponse-constantresistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DCPowerOutputSourceCustomTransientResponseConstantResistance sub-object used to configure the constant resistance custom transient response properties of source unit channel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourceCustomTransientRespo

### ConstantResistance

Specifies the [DCPowerOutputSourceCustomTransientResponseConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance.html) sub-object used to configure the constant resistance custom transient response properties of source unit channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourceCustomTransientResponseConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance.html) ConstantResistance { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourceCustomTransientResponseConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance.html).

Parent topic:

DCPowerOutputSourceCustomTransientResponse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-compensationfrequency.html language=enus -->
## TOPIC 00260: CompensationFrequency

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-compensationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-compensationfrequency.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency at which a pole-zero pair is added to the system when the Function property is set to ConstantPower and the output current is below the current limit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CompensationFrequency { get; set; }RemarksThis

### CompensationFrequency

Specifies the frequency at which a pole-zero pair is added to the system when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [ConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the output current is below the current limit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CompensationFrequency { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [TransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html) property.

Parent topic:

DCPowerOutputSourceCustomTransientResponseConstantPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-gainbandwidth.html language=enus -->
## TOPIC 00261: GainBandwidth

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-gainbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-gainbandwidth.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes when the Function property is set to ConstantPower and the output current is below the current limit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic dou

### GainBandwidth

Specifies the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [ConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the output current is below the current limit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double GainBandwidth { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [TransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html) property.

Parent topic:

DCPowerOutputSourceCustomTransientResponseConstantPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-polezeroratio.html language=enus -->
## TOPIC 00262: PoleZeroRatio

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-polezeroratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower-polezeroratio.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of the pole frequency to the zero frequency when the Function property is set to ConstantPower and the output current is below the current limit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double PoleZeroRatio { get; set; }RemarksThis property is not

### PoleZeroRatio

Specifies the ratio of the pole frequency to the zero frequency when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [ConstantPower](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the output current is below the current limit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double PoleZeroRatio { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [TransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html) property.

Parent topic:

DCPowerOutputSourceCustomTransientResponseConstantPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower.html language=enus -->
## TOPIC 00263: DCPowerOutputSourceCustomTransientResponseConstantPower Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantpower.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties used to configure the constant power custom transient response of source unit channel. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceCustomTransientResponseConstantPower : DCPowerSubObjectRemarksFor mo

### DCPowerOutputSourceCustomTransientResponseConstantPower Class

Contains properties used to configure the constant power custom transient response of source unit channel.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceCustomTransientResponseConstantPower : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Properties

| Name | Description |
| --- | --- |
| CompensationFrequency | Specifies the frequency at which a pole-zero pair is added to the system when the Function property is set to ConstantPower and the output current is below the current limit. |
| GainBandwidth | Specifies the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes when the Function property is set to ConstantPower and the output current is below the current limit. |
| PoleZeroRatio | Specifies the ratio of the pole frequency to the zero frequency when the Function property is set to ConstantPower and the output current is below the current limit. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-compensationfrequency.html language=enus -->
## TOPIC 00264: CompensationFrequency

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-compensationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-compensationfrequency.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency at which a pole-zero pair is added to the system when the Function property is set to ConstantResistance and the output current is below the current limit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CompensationFrequency { get; set; }Remark

### CompensationFrequency

Specifies the frequency at which a pole-zero pair is added to the system when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [ConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the output current is below the current limit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CompensationFrequency { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [TransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html) property.

Parent topic:

DCPowerOutputSourceCustomTransientResponseConstantResistance Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-gainbandwidth.html language=enus -->
## TOPIC 00265: GainBandwidth

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-gainbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-gainbandwidth.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes when the Function property is set to ConstantResistance and the output current is below the current limit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpubli

### GainBandwidth

Specifies the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [ConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the output current is below the current limit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double GainBandwidth { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [TransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html) property.

Parent topic:

DCPowerOutputSourceCustomTransientResponseConstantResistance Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-polezeroratio.html language=enus -->
## TOPIC 00266: PoleZeroRatio

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-polezeroratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance-polezeroratio.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of the pole frequency to the zero frequency when the Function property is set to ConstantResistance and the output current is below the current limit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double PoleZeroRatio { get; set; }RemarksThis property is

### PoleZeroRatio

Specifies the ratio of the pole frequency to the zero frequency when the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [ConstantResistance](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the output current is below the current limit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double PoleZeroRatio { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [TransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-transientresponse.html) property.

Parent topic:

DCPowerOutputSourceCustomTransientResponseConstantResistance Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance.html language=enus -->
## TOPIC 00267: DCPowerOutputSourceCustomTransientResponseConstantResistance Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponseconstantresistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties used to configure the constant resistance custom transient response of source unit channel. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceCustomTransientResponseConstantResistance : DCPowerSubObjectRem

### DCPowerOutputSourceCustomTransientResponseConstantResistance Class

Contains properties used to configure the constant resistance custom transient response of source unit channel.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceCustomTransientResponseConstantResistance : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Properties

| Name | Description |
| --- | --- |
| CompensationFrequency | Specifies the frequency at which a pole-zero pair is added to the system when the Function property is set to ConstantResistance and the output current is below the current limit. |
| GainBandwidth | Specifies the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes when the Function property is set to ConstantResistance and the output current is below the current limit. |
| PoleZeroRatio | Specifies the ratio of the pole frequency to the zero frequency when the Function property is set to ConstantResistance and the output current is below the current limit. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent-gainbandwidth.html language=enus -->
## TOPIC 00268: GainBandwidth

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent-gainbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent-gainbandwidth.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double GainBandwidth { get; set; }RemarksThis property is not supported by all instruments. Refer to

### GainBandwidth

Gets or sets the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double GainBandwidth { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [DCPowerSourceTransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) property.

Parent topic:

DCPowerOutputSourceCustomTransientResponseCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent-polezeroratio.html language=enus -->
## TOPIC 00269: PoleZeroRatio

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent-polezeroratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent-polezeroratio.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the ratio of the pole frequency to the zero frequency. This property takes effect when the channel is in DCCurrent mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double PoleZeroRatio { get; set; }RemarksThe default value is determined by the value of the N

### PoleZeroRatio

Gets or sets the ratio of the pole frequency to the zero frequency. This property takes effect when the channel is in [DCCurrent](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double PoleZeroRatio { get; set; }

#### Remarks

The default value is determined by the value of the [Normal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) setting of the [DCPowerSourceTransientResponse](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetransientresponse.html) property.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSourceCustomTransientResponseCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent.html language=enus -->
## TOPIC 00270: DCPowerOutputSourceCustomTransientResponseCurrent Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcecustomtransientresponsecurrent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties used to configure the custom transient response current of source unit channel. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceCustomTransientResponseCurrent : DCPowerSubObjectRemarksFor more informatio

### DCPowerOutputSourceCustomTransientResponseCurrent Class

Contains properties used to configure the custom transient response current of source unit channel.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceCustomTransientResponseCurrent : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| CompensationFrequency | Gets or sets the frequency at which a pole-zero pair is added to the system. This property takes effect when the channel is in DCCurrent mode. |
| GainBandwidth | Gets or sets the frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. |
| PoleZeroRatio | Gets or sets the ratio of the pole frequency to the zero frequency. This property takes effect when the channel is in DCCurrent mode. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-connected.html language=enus -->
## TOPIC 00271: Connected

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-connected.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-connected.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the output relay is connected (closed) or disconnected (open). The Enabled property does not change based on this property; they are independent of each other. Set this property to false to disconnect the output terminal from the output. SyntaxNamespace: NationalInstruments.Modu

### Connected

Gets or sets whether the output relay is connected (closed) or disconnected (open). The [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property does not change based on this property; they are independent of each other. Set this property to **false** to disconnect the output terminal from the output.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Connected { get; set; }

#### Remarks

The default value is **true**.

Note

The PXIe-4051 does not have an output relay. For the PXIe-4051, this property specifies whether the input MOSFETs are connected (ON) or disconnected (OFF).

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSourceOutput Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-resistance.html language=enus -->
## TOPIC 00272: Resistance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-resistance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output resistance that the device attempts to generate for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Resistance { get; set; }RemarksDepending on the instrument, output resistance is configurable only if you set the Function

### Resistance

Specifies the output resistance that the device attempts to generate for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Resistance { get; set; }

#### Remarks

Function

- PXIe-4141, PXIe-4143, PXIe-4145: [DCVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html)
- PXIe-4135, PXIe-4137, PXIe-4139, PXIe-4147, PXIe-4162, PXIe-4163: [DCCurrent](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) or [DCVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html)

Note

The channel must be enabled for the specified output resistance to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Note

Using the [MergedChannels](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsource-mergedchannels.html) property to merge instrument outputs affects the valid output resistance range you can program. Refer to the Merged Channels topic for your device for details.

Note

Function

ConstantResistance

Level

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Valid Values**: Vary by device. Refer to the device specifications for your device for more information about supported values.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerOutputSourceOutput Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentchangelimithigh.html language=enus -->
## TOPIC 00273: CurrentChangeLimitHigh

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentchangelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentchangelimithigh.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff. If the current increases at a rate that exceeds this limit, the output is disconnected. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentChangeLimitHigh { get; set; }Rem

### CurrentChangeLimitHigh

Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff. If the current increases at a rate that exceeds this limit, the output is disconnected.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentChangeLimitHigh { get; set; }

#### Remarks

To find out whether an output has exceeded this limit, call the [QueryLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method with OutputCutoffReasonCurrentChangeHigh as the outputCutoffReason.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Represents a threshold on positive current slew rate for output cutoff.

Parent topic:

DCPowerOutputSourceOutputCutoff Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentmeasurelimithigh.html language=enus -->
## TOPIC 00274: CurrentMeasureLimitHigh

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentmeasurelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentmeasurelimithigh.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a high limit current value, in amps, for output cutoff. If the measured current exceeds this limit, the output is disconnected. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentMeasureLimitHigh { get; set; }RemarksTo find out whether an output has excee

### CurrentMeasureLimitHigh

Specifies a high limit current value, in amps, for output cutoff. If the measured current exceeds this limit, the output is disconnected.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentMeasureLimitHigh { get; set; }

#### Remarks

To find out whether an output has exceeded this limit, call the [QueryLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method with OutputCutoffReasonCurrentMeasureHigh as the outputCutoffReason.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Represents a high current threshold for output cutoff.

Parent topic:

DCPowerOutputSourceOutputCutoff Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentmeasurelimitlow.html language=enus -->
## TOPIC 00275: CurrentMeasureLimitLow

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentmeasurelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentmeasurelimitlow.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a low limit current value, in amps, for output cutoff. If the measured current falls below this limit, the output is disconnected. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentMeasureLimitLow { get; set; }RemarksTo find out whether an output has fal

### CurrentMeasureLimitLow

Specifies a low limit current value, in amps, for output cutoff. If the measured current falls below this limit, the output is disconnected.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentMeasureLimitLow { get; set; }

#### Remarks

To find out whether an output has fallen below this limit, call the [QueryLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method with OutputCutoffReasonCurrentMeasureLow as the outputCutoffReason.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Represents a low current threshold for output cutoff.

Parent topic:

DCPowerOutputSourceOutputCutoff Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentoverrangeenabled.html language=enus -->
## TOPIC 00276: CurrentOverrangeEnabled

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentoverrangeenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-currentoverrangeenabled.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool CurrentOverrangeEnabled { get; set; }RemarksTo find out wh

### CurrentOverrangeEnabled

Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool CurrentOverrangeEnabled { get; set; }

#### Remarks

To find out whether an output has exceeded this limit, call the [QueryLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method with OutputCutoffReasonCurrentSaturated as the outputCutoffReason.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is false.

Parent topic:

DCPowerOutputSourceOutputCutoff Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltagemeasurelimitlow.html language=enus -->
## TOPIC 00277: VoltageMeasureLimitLow

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltagemeasurelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltagemeasurelimitlow.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a low limit voltage value, in volts, for output cutoff. If the measured voltage falls below this limit, the output is disconnected. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double VoltageMeasureLimitLow { get; set; }RemarksTo find out whether an output has fa

### VoltageMeasureLimitLow

Specifies a low limit voltage value, in volts, for output cutoff. If the measured voltage falls below this limit, the output is disconnected.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double VoltageMeasureLimitLow { get; set; }

#### Remarks

To find out whether an output has fallen below this limit, call the [QueryLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method with OutputCutoffReasonVoltageMeasureLow as the outputCutoffReason.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Represents a low voltage threshold for output cutoff.

Parent topic:

DCPowerOutputSourceOutputCutoff Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltageoutputlimithigh.html language=enus -->
## TOPIC 00278: VoltageOutputLimitHigh

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltageoutputlimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltageoutputlimithigh.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a high limit voltage value, in volts, for output cutoff. If the voltage output exceeds this limit, the output is disconnected. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double VoltageOutputLimitHigh { get; set; }RemarksTo find out whether an output has exceede

### VoltageOutputLimitHigh

Specifies a high limit voltage value, in volts, for output cutoff. If the voltage output exceeds this limit, the output is disconnected.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double VoltageOutputLimitHigh { get; set; }

#### Remarks

To find out whether an output has exceeded this limit, call the [QueryLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method with OutputCutoffReasonVoltageOutputHigh as the outputCutoffReason.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Represents a high voltage threshold for output cutoff.

Parent topic:

DCPowerOutputSourceOutputCutoff Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltageoutputlimitlow.html language=enus -->
## TOPIC 00279: VoltageOutputLimitLow

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltageoutputlimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff-voltageoutputlimitlow.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a low limit voltage value, in volts, for output cutoff. If the voltage output falls below this limit, the output is disconnected. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double VoltageOutputLimitLow { get; set; }RemarksTo find out whether an output has falle

### VoltageOutputLimitLow

Specifies a low limit voltage value, in volts, for output cutoff. If the voltage output falls below this limit, the output is disconnected.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double VoltageOutputLimitLow { get; set; }

#### Remarks

To find out whether an output has fallen below this limit, call the [QueryLatchedOutputCutoffState](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement-querylatchedoutputcutoffstate__string-dcpoweroutputcutoffreason.html) method with OutputCutoffReasonVoltageOutputLow as the outputCutoffReason.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Represents a low voltage threshold for output cutoff.

Parent topic:

DCPowerOutputSourceOutputCutoff Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff.html language=enus -->
## TOPIC 00280: DCPowerOutputSourceOutputCutoff Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutputcutoff.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties for controlling output cutoff limits for supported instruments. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceOutputCutoff : DCPowerSubObjectRemarksWhen an output cutoff is engaged, the output of the channel(s)

### DCPowerOutputSourceOutputCutoff Class

Properties for controlling output cutoff limits for supported instruments.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceOutputCutoff : DCPowerSubObject

#### Remarks

When an output cutoff is engaged, the output of the channel(s) is disconnected.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| CurrentChangeLimitHigh | Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff. If the current increases at a rate that exceeds this limit, the output is disconnected. |
| CurrentChangeLimitLow | Specifies a limit for negative current slew rate, in amps per microsecond, for output cutoff. If the current decreases at a rate that exceeds this limit, the output is disconnected. |
| CurrentMeasureLimitHigh | Specifies a high limit current value, in amps, for output cutoff. If the measured current exceeds this limit, the output is disconnected. |
| CurrentMeasureLimitLow | Specifies a low limit current value, in amps, for output cutoff. If the measured current falls below this limit, the output is disconnected. |
| CurrentOverrangeEnabled | Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range. |
| Delay | Delays disconnecting the output by the time you specify, in seconds, when a limit is exceeded. |
| Enabled | Enables or disables output cutoff functionality. If enabled, you can define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected. |
| VoltageChangeLimitHigh | Specifies a limit for positive voltage slew rate, in volts per microsecond, for output cutoff. If the voltage increases at a rate that exceeds this limit, the output is disconnected. |
| VoltageChangeLimitLow | Specifies a limit for negative voltage slew rate, in volts per microsecond, for output cutoff. If the voltage decreases at a rate that exceeds this limit, the output is disconnected. |
| VoltageMeasureLimitHigh | Specifies a high limit voltage value, in volts, for output cutoff. If the measured voltage exceeds this limit, the output is disconnected. |
| VoltageMeasureLimitLow | Specifies a low limit voltage value, in volts, for output cutoff. If the measured voltage falls below this limit, the output is disconnected. |
| VoltageOutputLimitHigh | Specifies a high limit voltage value, in volts, for output cutoff. If the voltage output exceeds this limit, the output is disconnected. |
| VoltageOutputLimitLow | Specifies a low limit voltage value, in volts, for output cutoff. If the voltage output falls below this limit, the output is disconnected. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-biasvoltagelimit.html language=enus -->
## TOPIC 00281: BiasVoltageLimit

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-biasvoltagelimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-biasvoltagelimit.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double BiasVoltageLimit { get; set; }RemarksThe valid

### BiasVoltageLimit

Gets or sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double BiasVoltageLimit { get; set; }

#### Remarks

The valid values for this property are defined by the values you specify for the [VoltageLimitRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-voltagelimitrange.html) property.

DCPowerSourceOutputFunction

PulseCurrent

DCPowerComplianceLimitSymmetry

Symmetric

Note

A channel must be enabled for the specified bias voltage limit to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerOutputSourcePulseCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-currentlevel.html language=enus -->
## TOPIC 00282: CurrentLevel

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-currentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-currentlevel.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse current level, in amperes, that the specified channel(s) attempt to generate during the on phase of a pulse. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double CurrentLevel { get; set; }RemarksThis property is applicable only if the DCPowerSourceOut

### CurrentLevel

Gets or sets the pulse current level, in amperes, that the specified channel(s) attempt to generate during the on phase of a pulse.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentLevel { get; set; }

#### Remarks

DCPowerSourceOutputFunction

PulseCurrent

Note

A channel must be enabled for the specified current level to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel. This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The valid values for this property are defined by the values you specify for the [CurrentLevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsecurrent-currentlevelrange.html) property.

Parent topic:

DCPowerOutputSourcePulseCurrent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-biascurrentlimit.html language=enus -->
## TOPIC 00283: BiasCurrentLimit

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-biascurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-biascurrentlimit.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage and the DCPowerComplianceLimitSymmetry property is

### BiasCurrentLimit

Specifies the current limit, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the off phase of a pulse. This property is applicable only if the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [PulseVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) and the [DCPowerComplianceLimitSymmetry](nationalinstruments-modularinstruments-nidcpower-dcpowercompliancelimitsymmetry.html) property is set to [Symmetric](nationalinstruments-modularinstruments-nidcpower-dcpowercompliancelimitsymmetry.html). A channel must be enabled for the specified bias current limit to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double BiasCurrentLimit { get; set; }

#### Remarks

The valid values for this property are defined by the values you specify for the [CurrentLimitRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-currentlimitrange.html) property.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Parent topic:

DCPowerOutputSourcePulseVoltage Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-currentlimitrange.html language=enus -->
## TOPIC 00284: CurrentLimitRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-currentlimitrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-currentlimitrange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit range, in amperes, for the specified channel(s). The CurrentLimitRange property is applicable only if you set the Function property to PulseVoltage. A channel must be enabled for the specified current limit to take effect. Refer to the Enabled property for more informatio

### CurrentLimitRange

Specifies the current limit range, in amperes, for the specified channel(s). The CurrentLimitRange property is applicable only if you set the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property to [PulseVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html). A channel must be enabled for the specified current limit to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double CurrentLimitRange { get; set; }

#### Remarks

Refer to the Ranges topic in the *Device User Manual* or to the instrument specifications for information about valid ranges.

Parent topic:

DCPowerOutputSourcePulseVoltage Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-voltagelevelrange.html language=enus -->
## TOPIC 00285: VoltageLevelRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-voltagelevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage-voltagelevelrange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse voltage level range, in volts, for the specified channel(s). The VoltageLevelRange property is applicable only if the Function property is set to PulseVoltage. A channel must be enabled for the specified voltage level range to take effect. Refer to the Enabled property for more i

### VoltageLevelRange

Specifies the pulse voltage level range, in volts, for the specified channel(s). The VoltageLevelRange property is applicable only if the [Function](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-function.html) property is set to [PulseVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html). A channel must be enabled for the specified voltage level range to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double VoltageLevelRange { get; set; }

#### Remarks

Refer to the Ranges topic in the *Device User Manual* or to the instrument specifications for information about valid ranges.

Parent topic:

DCPowerOutputSourcePulseVoltage Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage.html language=enus -->
## TOPIC 00286: DCPowerOutputSourcePulseVoltage Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcepulsevoltage.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties used to configure the pulse voltage of source unit channel. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourcePulseVoltage : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and S

### DCPowerOutputSourcePulseVoltage Class

Contains properties used to configure the pulse voltage of source unit channel.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourcePulseVoltage : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| BiasCurrentLimit | Specifies the current limit, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage and the DCPowerComplianceLimitSymmetry property is set to Symmetric. A channel must be enabled for the specified bias current limit to take effect. Refer to the Enabled property for more information about enabling the channel. |
| BiasCurrentLimitHigh | Specifies the current limit high, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage and the DCPowerComplianceLimitSymmetry property is set to Asymmetric. A channel must be enabled for the specified bias current limit high to take effect. Refer to the Enabled property for more information about enabling the channel. |
| BiasCurrentLimitLow | Specifies the current limit low, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage and the DCPowerComplianceLimitSymmetry property is set to Asymmetric. A channel must be enabled for the specified bias current limit low to take effect. Refer to the Enabled property for more information about enabling the channel. |
| BiasVoltageLevel | Specifies the voltage level, in volts, that the specified channel(s) attempt to generate during the off phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage. Note A channel must be enabled for the specified voltage level to take effect. Refer to the Enabled property for more information about enabling the channel. |
| CurrentLimit | Specifies the current limit, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage and the DCPowerComplianceLimitSymmetry property is set to Symmetric. A channel must be enabled for the specified current limit to take effect. Refer to the Enabled property for more information about enabling the channel. |
| CurrentLimitHigh | Specifies the current limit high, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage and the DCPowerComplianceLimitSymmetry property is set to Asymmetric. A channel must be enabled for the specified current limit high to take effect. Refer to the Enabled property for more information about enabling the channel. |
| CurrentLimitLow | Specifies the current limit low, in amperes, that the output cannot exceed when generating the desired voltage on the specified channel(s) during the on phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage and the DCPowerComplianceLimitSymmetry property is set to Asymmetric. A channel must be enabled for the specified current limit low to take effect. Refer to the Enabled property for more information about enabling the channel. |
| CurrentLimitRange | Specifies the current limit range, in amperes, for the specified channel(s). The CurrentLimitRange property is applicable only if you set the Function property to PulseVoltage. A channel must be enabled for the specified current limit to take effect. Refer to the Enabled property for more information about enabling the channel. |
| VoltageLevel | Specifies the voltage level, in volts, that specified channel(s) attempt to generate during the on phase of a pulse. This property is applicable only if the Function property is set to PulseVoltage. Note A channel must be enabled for the specified voltage level to take effect. Refer to the Enabled property for more information about enabling the channel. |
| VoltageLevelRange | Specifies the pulse voltage level range, in volts, for the specified channel(s). The VoltageLevelRange property is applicable only if the Function property is set to PulseVoltage. A channel must be enabled for the specified voltage level range to take effect. Refer to the Enabled property for more information about enabling the channel. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-configuresoftwareedgetrigger.html language=enus -->
## TOPIC 00287: ConfigureSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-configuresoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-configuresoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the SourceTrigger for software edge triggering for the specified channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ConfigureSoftwareEdgeTrigger()RemarksThis method cannot be called for channels that are in the Running state. Refer to the Programming

### ConfigureSoftwareEdgeTrigger()

Configures the [SourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html) for software edge triggering for the specified channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ConfigureSoftwareEdgeTrigger()

#### Remarks

Note

This method cannot be called for channels that are in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSourceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-digitaledge.html language=enus -->
## TOPIC 00288: DigitalEdge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-digitaledge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputDigitalEdgeSourceTrigger sub-object to configure the device to wait for digital edge SourceTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputDigitalEdgeSourceTrigger DigitalEdge { get; }RemarksReturns an object of type DCPowerOutputDi

### DigitalEdge

Gets the [DCPowerOutputDigitalEdgeSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesourcetrigger.html) sub-object to configure the device to wait for digital edge [SourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputDigitalEdgeSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesourcetrigger.html) DigitalEdge { get; }

#### Remarks

Returns an object of type [DCPowerOutputDigitalEdgeSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgesourcetrigger.html).

Parent topic:

DCPowerOutputSourceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-exportedoutputterminal.html language=enus -->
## TOPIC 00289: ExportedOutputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-exportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-exportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the SourceTrigger exported output terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceTriggerExportedOutputTerminal ExportedOutputTerminal { get; set; }RemarksSpecify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrum

### ExportedOutputTerminal

Gets or sets the [SourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html) exported output terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal.html) ExportedOutputTerminal { get; set; }

#### Remarks

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Returns the [DCPowerSourceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSourceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00290: SendSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger-sendsoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts the SourceTrigger for software triggering. This method can override an external edge trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SendSoftwareEdgeTrigger()RemarksThis method is not supported by all instruments. Refer to the Supported Functions by Devi

### SendSoftwareEdgeTrigger()

Asserts the [SourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html) for software triggering. This method can override an external edge trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputSourceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger.html language=enus -->
## TOPIC 00291: DCPowerOutputSourceTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties used to configure the SourceTrigger for NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputSourceTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies

### DCPowerOutputSourceTrigger Class

Represents the methods and properties used to configure the [SourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html) for NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputSourceTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DCPowerOutputDigitalEdgeSourceTrigger sub-object to configure the device to wait for digital edge SourceTrigger. |
| ExportedOutputTerminal | Gets or sets the SourceTrigger exported output terminal. |
| Type | Gets or sets the SourceTrigger type. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareEdgeTrigger() | Configures the SourceTrigger for software edge triggering for the specified channel(s). |
| Disable() | Disables the SourceTrigger. The specified channel(s) do not wait for a Source trigger before performing a source operation. |
| SendSoftwareEdgeTrigger() | Asserts the SourceTrigger for software triggering. This method can override an external edge trigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-currentlimitautorange.html language=enus -->
## TOPIC 00292: CurrentLimitAutorange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-currentlimitautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-currentlimitautorange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether or not NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channels. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceCurrentLimitAutorange CurrentLimitAutorange { get; set; }RemarksSpe

### CurrentLimitAutorange

Gets or sets whether or not NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceCurrentLimitAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecurrentlimitautorange.html) CurrentLimitAutorange { get; set; }

#### Remarks

Specifies an object of type [DCPowerSourceCurrentLimitAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecurrentlimitautorange.html).

Parent topic:

DCPowerOutputSourceVoltage Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelautorange.html language=enus -->
## TOPIC 00293: VoltageLevelAutorange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelautorange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether or not NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channels. If this property is set to On, NI-DCPower ignores any changes you make to the VoltageLevelRange property. If you change the DCPowerSourceVoltageLevelAut

### VoltageLevelAutorange

Gets or sets whether or not NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channels. If this property is set to [On](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html), NI-DCPower ignores any changes you make to the [VoltageLevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelrange.html) property. If you change the [DCPowerSourceVoltageLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html) property from [On](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html) to [Off](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html), NI-DCPower remembers the last value the [VoltageLevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelrange.html) property was set to (or the default value if the property was never set) and uses that value as the voltage level range. Query the [VoltageLevelRange](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelrange.html) property by getting the property value to find out which range NI-DCPower automatically selects. The [DCPowerSourceVoltageLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html) property is applicable only if the [DCPowerSourceOutputFunction](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) property is set to [DCVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceVoltageLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html) VoltageLevelAutorange { get; set; }

#### Remarks

Specifies an object of type [DCPowerSourceVoltageLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html).

Parent topic:

DCPowerOutputSourceVoltage Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelrange.html language=enus -->
## TOPIC 00294: VoltageLevelRange

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcevoltage-voltagelevelrange.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the voltage level range, in volts, for the specified channel(s). The range defines the valid values to which the voltage level can be set. Use the DCPowerSourceVoltageLevelAutorange property to enable automatic selection of the voltage level range. The VoltageLevelRange property is appl

### VoltageLevelRange

Gets or sets the voltage level range, in volts, for the specified channel(s). The range defines the valid values to which the voltage level can be set. Use the [DCPowerSourceVoltageLevelAutorange](nationalinstruments-modularinstruments-nidcpower-dcpowersourcevoltagelevelautorange.html) property to enable automatic selection of the voltage level range. The VoltageLevelRange property is applicable only if the [DCPowerSourceOutputFunction](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html) property is set to [DCVoltage](nationalinstruments-modularinstruments-nidcpower-dcpowersourceoutputfunction.html). The channel must be enabled for the specified voltage level range to take effect. Refer to the [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) property for more information about enabling the channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double VoltageLevelRange { get; set; }

#### Remarks

The valid values for this property are defined by the values you specify for the VoltageLevelRange property. Refer to the Ranges topic in the *Device User Manual* or to the instrument specifications for information about valid ranges.

Parent topic:

DCPowerOutputSourceVoltage Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-digitaledge.html language=enus -->
## TOPIC 00295: DigitalEdge

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-digitaledge.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputDigitalEdgeStartTrigger sub-object to configure the device to wait for digital edge StartTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputDigitalEdgeStartTrigger DigitalEdge { get; }RemarksReturns an object of type DCPowerOutputDigit

### DigitalEdge

Gets the [DCPowerOutputDigitalEdgeStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgestarttrigger.html) sub-object to configure the device to wait for digital edge [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-starttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputDigitalEdgeStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgestarttrigger.html) DigitalEdge { get; }

#### Remarks

Returns an object of type [DCPowerOutputDigitalEdgeStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputdigitaledgestarttrigger.html).

Parent topic:

DCPowerOutputStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-disable.html language=enus -->
## TOPIC 00296: Disable()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-disable.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the StartTrigger. The specified channel(s) do not wait for a Start trigger when starting generation or acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Disable()RemarksThis method is necessary only if you configured a StartTrigger in the past and now

### Disable()

Disables the [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-starttrigger.html). The specified channel(s) do not wait for a Start trigger when starting generation or acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Disable()

#### Remarks

StartTrigger

Note

This method cannot be called in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00297: SendSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-sendsoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts the StartTrigger for software triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SendSoftwareEdgeTrigger()RemarksThis method is not supported by all instruments. Refer to the Supported Functions by Device topic in the NI DC Power Supplies and SMUs Help f

### SendSoftwareEdgeTrigger()

Asserts the [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-starttrigger.html) for software triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The method was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The method was called to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The method was called with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-type.html language=enus -->
## TOPIC 00298: Type

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger-type.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the StartTrigger type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerStartTriggerType Type { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device topic in the NI DC Power Supplies and SMUs Help

### Type

Gets or sets the [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-starttrigger.html) type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerStartTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggertype.html) Type { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Note

To use the per-channel version of this property, you must first initialize the session with the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor. If the session was initialized with a deprecated constructor, use the per-session version of this property instead or include all channels.

Specifies the [DCPowerStartTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggertype.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The property was accessed after the associated NIDCPower object was disposed. |
| Ivi.Driver.OperationNotSupportedException | The property was accessed to unsupported hardware. |
| Ivi.Driver.SelectorNameException | The property was accessed with an unknown channel name. |
| Ivi.Driver.IviCDriverException | The underlying NI-DCPower driver returned an error. |

Parent topic:

DCPowerOutputStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger.html language=enus -->
## TOPIC 00299: DCPowerOutputStartTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputstarttrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties used to configure the StartTrigger for NI-DCPower. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputStartTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies an

### DCPowerOutputStartTrigger Class

Represents the methods and properties used to configure the [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-starttrigger.html) for NI-DCPower.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputStartTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DCPowerOutputDigitalEdgeStartTrigger sub-object to configure the device to wait for digital edge StartTrigger. |
| ExportedOutputTerminal | Gets or sets the StartTrigger exported output terminal. |
| Type | Gets or sets the StartTrigger type. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareEdgeTrigger() | Configures the StartTrigger for software edge triggering for the specified channel(s). |
| Disable() | Disables the StartTrigger. The specified channel(s) do not wait for a Start trigger when starting generation or acquisition. |
| SendSoftwareEdgeTrigger() | Asserts the StartTrigger for software triggering. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sequenceadvancetrigger.html language=enus -->
## TOPIC 00300: SequenceAdvanceTrigger

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sequenceadvancetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sequenceadvancetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputSequenceAdvanceTrigger sub-object that is used to configure the Sequence Advance Trigger of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSequenceAdvanceTrigger SequenceAdvanceTrigger { get; }RemarksReturns an object of type DC

### SequenceAdvanceTrigger

Gets the [DCPowerOutputSequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger.html) sub-object that is used to configure the Sequence Advance Trigger of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger.html) SequenceAdvanceTrigger { get; }

#### Remarks

Returns an object of type [DCPowerOutputSequenceAdvanceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsequenceadvancetrigger.html).

Parent topic:

DCPowerOutputTriggers Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-shutdowntrigger.html language=enus -->
## TOPIC 00301: ShutdownTrigger

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-shutdowntrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-shutdowntrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputShutdownTrigger sub-object that is used to configure the Shutdown Trigger of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputShutdownTrigger ShutdownTrigger { get; }RemarksReturns an object of type DCPowerOutputShutdownTrigger.

### ShutdownTrigger

Gets the [DCPowerOutputShutdownTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputshutdowntrigger.html) sub-object that is used to configure the Shutdown Trigger of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputShutdownTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputshutdowntrigger.html) ShutdownTrigger { get; }

#### Remarks

Returns an object of type [DCPowerOutputShutdownTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputshutdowntrigger.html).

Parent topic:

DCPowerOutputTriggers Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html language=enus -->
## TOPIC 00302: SourceTrigger

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers-sourcetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputSourceTrigger sub-object that is used to configure the Source Trigger of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputSourceTrigger SourceTrigger { get; }RemarksReturns an object of type DCPowerOutputSourceTrigger .

### SourceTrigger

Gets the [DCPowerOutputSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger.html) sub-object that is used to configure the Source Trigger of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger.html) SourceTrigger { get; }

#### Remarks

Returns an object of type [DCPowerOutputSourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourcetrigger.html) .

Parent topic:

DCPowerOutputTriggers Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers.html language=enus -->
## TOPIC 00303: DCPowerOutputTriggers Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpoweroutputtriggers.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides underlying triggers of specific types. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerOutputTriggers : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread SafetyAll members of this

### DCPowerOutputTriggers Class

Provides underlying triggers of specific types.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerOutputTriggers : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| MeasureTrigger | Gets the DCPowerOutputMeasureTrigger sub-object that is used to configure the Measure Trigger of NI-DCPower. |
| PulseTrigger | Gets the DCPowerOutputPulseTrigger sub-object that is used to configure the Pulse Trigger of NI-DCPower. |
| SequenceAdvanceTrigger | Gets the DCPowerOutputSequenceAdvanceTrigger sub-object that is used to configure the Sequence Advance Trigger of NI-DCPower. |
| ShutdownTrigger | Gets the DCPowerOutputShutdownTrigger sub-object that is used to configure the Shutdown Trigger of NI-DCPower. |
| SourceTrigger | Gets the DCPowerOutputSourceTrigger sub-object that is used to configure the Source Trigger of NI-DCPower. |
| StartTrigger | Gets the DCPowerOutputStartTrigger sub-object that is used to configure the Start Trigger for NI-DCPower. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteevent-outputterminal.html language=enus -->
## TOPIC 00304: OutputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteevent-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteevent-outputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output terminal for exporting the PulseCompleteEvent. Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened termina

### OutputTerminal

Gets or sets the output terminal for exporting the [PulseCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-pulsecompleteevent.html). Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) OutputTerminal { get; set; }

#### Remarks

Specifies the [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) value.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerPulseCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-equals__object.html language=enus -->
## TOPIC 00305: Equals(object)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-equals__object.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerPulseCompleteEventOutputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compa

### Equals(object)

Determines whether the current instance of [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of DCPowerPulseCompleteEventOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerPulseCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-operator_eq__dcpowerpulsecompleteeventoutputterminal-dcpowerpulsecompleteeventoutputterminal.html language=enus -->
## TOPIC 00306: operator==(DCPowerPulseCompleteEventOutputTerminal, DCPowerPulseCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-operator_eq__dcpowerpulsecompleteeventoutputterminal-dcpowerpulsecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-operator_eq__dcpowerpulsecompleteeventoutputterminal-dcpowerpulsecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerPulseCompleteEventOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerPulseCompleteEventOutputTerminal outputTerminal1, DCPowerPulseCompleteEventOutputTerminal outputTerminal2)Param

### operator==(DCPowerPulseCompleteEventOutputTerminal, DCPowerPulseCompleteEventOutputTerminal)

Checks whether the two instances of [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerPulseCompleteEventOutputTerminal outputTerminal1, DCPowerPulseCompleteEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerPulseCompleteEventOutputTerminal | Specifies a DCPowerPulseCompleteEventOutputTerminal object. |
| outputTerminal2 | DCPowerPulseCompleteEventOutputTerminal | Specifies a DCPowerPulseCompleteEventOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerPulseCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-operator_neq__dcpowerpulsecompleteeventoutputterminal-dcpowerpulsecompleteeventoutputterminal.html language=enus -->
## TOPIC 00307: operator!=(DCPowerPulseCompleteEventOutputTerminal, DCPowerPulseCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-operator_neq__dcpowerpulsecompleteeventoutputterminal-dcpowerpulsecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-operator_neq__dcpowerpulsecompleteeventoutputterminal-dcpowerpulsecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerPulseCompleteEventOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerPulseCompleteEventOutputTerminal outputTerminal1, DCPowerPulseCompleteEventOutputTerminal outputTerminal2)Par

### operator!=(DCPowerPulseCompleteEventOutputTerminal, DCPowerPulseCompleteEventOutputTerminal)

Checks whether the two instances of [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerPulseCompleteEventOutputTerminal outputTerminal1, DCPowerPulseCompleteEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerPulseCompleteEventOutputTerminal | Specifies DCPowerPulseCompleteEventOutputTerminal object. |
| outputTerminal2 | DCPowerPulseCompleteEventOutputTerminal | Specifies DCPowerPulseCompleteEventOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerPulseCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00308: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerPulseCompleteEventOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerPulseCompleteEventOutputTerminal repr

### PxiTriggerLine0

Gets the output terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerPulseCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00309: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerPulseCompleteEventOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerPulseCompleteEventOutputTerminal repr

### PxiTriggerLine1

Gets the output terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerPulseCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsecompleteeventoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerPulseCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00310: SendSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger-sendsoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts the specified trigger. This method can override an external edge trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SendSoftwareEdgeTrigger()RemarksThis method is not supported by all instruments. Refer to the Supported Functions by Device topic in the NI D

### SendSoftwareEdgeTrigger()

Asserts the specified trigger. This method can override an external edge trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerPulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger-type.html language=enus -->
## TOPIC 00311: Type

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger-type.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the DCPowerPulseTriggerType. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPulseTriggerType Type { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device topic in the NI DC Power Supplies and SMUs

### Type

Gets or sets the [DCPowerPulseTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulseTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggertype.html) Type { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is [None](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggertype.html). Specifies the [DCPowerPulseTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggertype.html) enumeration.

Parent topic:

DCPowerPulseTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger.html language=enus -->
## TOPIC 00312: DCPowerPulseTrigger Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines methods and properties used to configure the Pulse trigger. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerPulseTrigger : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread SafetyA

### DCPowerPulseTrigger Class

Defines methods and properties used to configure the Pulse trigger.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerPulseTrigger : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DCPowerDigitalEdgePulseTrigger sub-object to configure the device to wait for digital edge PulseTrigger. |
| ExportedOutputTerminal | Gets or sets the PulseTrigger exported output terminal. |
| Type | Gets or sets the DCPowerPulseTriggerType. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureSoftwareEdgeTrigger() | Configures the PulseTrigger trigger for software triggering. |
| Disable() | Disables the Pulse trigger. The device does not wait for a pulse trigger before performing a pulse operation. Refer to Pulse Mode and Sequence Source Mode for more information about the Pulse trigger. This method is necessary only if you configured a Pulse trigger in the past and now want to disable it. |
| SendSoftwareEdgeTrigger() | Asserts the specified trigger. This method can override an external edge trigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-donotexport.html language=enus -->
## TOPIC 00313: DoNotExport

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-donotexport.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-donotexport.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is not exported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerPulseTriggerExportedOutputTerminal DoNotExport { get; }RemarksReturns an object of type DCPowerPulseTriggerExportedOutputTerminal representing an empty stri

### DoNotExport

Gets the output terminal when the signal is not exported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) DoNotExport { get; }

#### Remarks

Returns an object of type [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) representing an empty string.

Parent topic:

DCPowerPulseTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00314: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerPulseTriggerExportedOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerPulseTriggerExportedOutputTerminal

### PxiTriggerLine1

Gets the output terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerPulseTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00315: PxiTriggerLine5

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline5.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerPulseTriggerExportedOutputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type DCPowerPulseTriggerExportedOutputTerminal

### PxiTriggerLine5

Gets the output terminal when the signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) representing the string "PXI_Trig5".

Parent topic:

DCPowerPulseTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00316: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerPulseTriggerExportedOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerPulseTriggerExportedOutputTerminal

### PxiTriggerLine6

Gets the output terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerPulseTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00317: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerPulseTriggerExportedOutputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerPulseTriggerExportedOutputTerminal

### PxiTriggerLine7

Gets the output terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerPulseTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetriggerexportedoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerPulseTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-donotexport.html language=enus -->
## TOPIC 00318: DoNotExport

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-donotexport.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-donotexport.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is not exported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerReadyForPulseTriggerEventOutputTerminal DoNotExport { get; }RemarksReturns an object of type DCPowerReadyForPulseTriggerEventOutputTerminal representing an

### DoNotExport

Gets the output terminal when the signal is not exported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) DoNotExport { get; }

#### Remarks

Returns an object of type [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) representing an empty string.

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-equals__dcpowerreadyforpulsetriggereventoutputterminal.html language=enus -->
## TOPIC 00319: Equals(DCPowerReadyForPulseTriggerEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-equals__dcpowerreadyforpulsetriggereventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-equals__dcpowerreadyforpulsetriggereventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal and the DCPowerReadyForPulseTriggerEventOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerReadyForPulseTriggerEventOutp

### Equals(DCPowerReadyForPulseTriggerEventOutputTerminal)

Determines whether the current instance of [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) and the [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerReadyForPulseTriggerEventOutputTerminal | Specifies the DCPowerReadyForPulseTriggerEventOutputTerminal object to be compared to the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-equals__object.html language=enus -->
## TOPIC 00320: Equals(object)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-equals__object.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to b

### Equals(object)

Determines whether the current instance of [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-gethashcode.html language=enus -->
## TOPIC 00321: GetHashCode()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-gethashcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of DCPowerRead

### GetHashCode()

Returns the hash code for the current instance of [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html).

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator-dcpowerreadyforpulsetriggereventoutputterminal__string.html language=enus -->
## TOPIC 00322: operator DCPowerReadyForPulseTriggerEventOutputTerminal(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator-dcpowerreadyforpulsetriggereventoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator-dcpowerreadyforpulsetriggereventoutputterminal__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent DCPowerReadyForPulseTriggerEventOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator DCPowerReadyForPulseTriggerEventOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionou

### operator DCPowerReadyForPulseTriggerEventOutputTerminal(string)

Converts the specified string to the equivalent [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator DCPowerReadyForPulseTriggerEventOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent DCPowerReadyForPulseTriggerEventOutputTerminal object. |

#### Returns

Returns an object of type [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) from the string passed in outputTerminal.

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator-string__dcpowerreadyforpulsetriggereventoutputterminal.html language=enus -->
## TOPIC 00323: operator string(DCPowerReadyForPulseTriggerEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator-string__dcpowerreadyforpulsetriggereventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator-string__dcpowerreadyforpulsetriggereventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the DCPowerReadyForPulseTriggerEventOutputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator string(DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal)ParametersNameTypeDescriptionoutputTermin

### operator string(DCPowerReadyForPulseTriggerEventOutputTerminal)

Converts the [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator string(DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerReadyForPulseTriggerEventOutputTerminal | Specifies the DCPowerReadyForPulseTriggerEventOutputTerminal object to be converted to string. |

#### Returns

Returns a String from the [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) object.

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator_eq__dcpowerreadyforpulsetriggereventoutputterminal-dcpowerreadyforpulsetriggerev...d786e398.html language=enus -->
## TOPIC 00324: operator==(DCPowerReadyForPulseTriggerEventOutputTerminal, DCPowerReadyForPulseTriggerEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator_eq__dcpowerreadyforpulsetriggereventoutputterminal-dcpowerreadyforpulsetriggerev...d786e398.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator_eq__dcpowerreadyforpulsetriggereventoutputterminal-dcpowerreadyforpulsetriggerev...d786e398.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerReadyForPulseTriggerEventOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal1, DCPowerReadyForPulseTriggerEventOutputTerminal

### operator==(DCPowerReadyForPulseTriggerEventOutputTerminal, DCPowerReadyForPulseTriggerEventOutputTerminal)

Checks whether the two instances of [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal1, DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerReadyForPulseTriggerEventOutputTerminal | Specifies a DCPowerReadyForPulseTriggerEventOutputTerminal object. |
| outputTerminal2 | DCPowerReadyForPulseTriggerEventOutputTerminal | Specifies a DCPowerReadyForPulseTriggerEventOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator_neq__dcpowerreadyforpulsetriggereventoutputterminal-dcpowerreadyforpulsetriggere...d786e343.html language=enus -->
## TOPIC 00325: operator!=(DCPowerReadyForPulseTriggerEventOutputTerminal, DCPowerReadyForPulseTriggerEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator_neq__dcpowerreadyforpulsetriggereventoutputterminal-dcpowerreadyforpulsetriggere...d786e343.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-operator_neq__dcpowerreadyforpulsetriggereventoutputterminal-dcpowerreadyforpulsetriggere...d786e343.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerReadyForPulseTriggerEventOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal1, DCPowerReadyForPulseTriggerEventOutputTermina

### operator!=(DCPowerReadyForPulseTriggerEventOutputTerminal, DCPowerReadyForPulseTriggerEventOutputTerminal)

Checks whether the two instances of [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal1, DCPowerReadyForPulseTriggerEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerReadyForPulseTriggerEventOutputTerminal | Specifies DCPowerReadyForPulseTriggerEventOutputTerminal object. |
| outputTerminal2 | DCPowerReadyForPulseTriggerEventOutputTerminal | Specifies DCPowerReadyForPulseTriggerEventOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00326: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerReadyForPulseTriggerEventOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type DCPowerReadyForPulseTriggerEventOutpu

### PxiTriggerLine0

Gets the output terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00327: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerReadyForPulseTriggerEventOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerReadyForPulseTriggerEventOutpu

### PxiTriggerLine1

Gets the output terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00328: PxiTriggerLine2

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal-pxitriggerline2.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerReadyForPulseTriggerEventOutputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type DCPowerReadyForPulseTriggerEventOutpu

### PxiTriggerLine2

Gets the output terminal when the signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [DCPowerReadyForPulseTriggerEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html) representing the string "PXI_Trig2".

Parent topic:

DCPowerReadyForPulseTriggerEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html language=enus -->
## TOPIC 00329: DCPowerReadyForPulseTriggerEventOutputTerminal Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the output terminal for DCPowerReadyForPulseTriggerEvent. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerReadyForPulseTriggerEventOutputTerminalRemarksSee OutputTerminal. Thread SafetyAll members of this type are safe for multithreaded

### DCPowerReadyForPulseTriggerEventOutputTerminal Class

Represents the output terminal for [DCPowerReadyForPulseTriggerEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggerevent.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerReadyForPulseTriggerEventOutputTerminal

#### Remarks

See [OutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggerevent-outputterminal.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DoNotExport | Gets the output terminal when the signal is not exported. |
| PxiTriggerLine0 | Gets the output terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the output terminal when the signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the output terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the output terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the output terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the output terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the output terminal when the signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the output terminal when the signal is exported to the PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates a DCPowerReadyForPulseTriggerEventOutputTerminal object from the specified string. |
| Equals(DCPowerReadyForPulseTriggerEventOutputTerminal) | Determines whether the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal and the DCPowerReadyForPulseTriggerEventOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal. |
| ToString() | Converts the current instance of DCPowerReadyForPulseTriggerEventOutputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator DCPowerReadyForPulseTriggerEventOutputTerminal(string) | Converts the specified string to the equivalent DCPowerReadyForPulseTriggerEventOutputTerminal object. |
| operator string(DCPowerReadyForPulseTriggerEventOutputTerminal) | Converts the DCPowerReadyForPulseTriggerEventOutputTerminal object to the equivalent string. |
| operator!=(DCPowerReadyForPulseTriggerEventOutputTerminal, DCPowerReadyForPulseTriggerEventOutputTerminal) | Checks whether the two instances of DCPowerReadyForPulseTriggerEventOutputTerminal are unequal. |
| operator==(DCPowerReadyForPulseTriggerEventOutputTerminal, DCPowerReadyForPulseTriggerEventOutputTerminal) | Checks whether the two instances of DCPowerReadyForPulseTriggerEventOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse-polarity.html language=enus -->
## TOPIC 00330: Polarity

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse-polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse-polarity.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the behavior of the DCPowerReadyForPulseTriggerEvent event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPulsePolarity Polarity { get; set; }RemarksThis property is not supported by all instruments. Refer to the Supported Properties by Device topic in t

### Polarity

Gets or sets the behavior of the [DCPowerReadyForPulseTriggerEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggerevent.html) event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) Polarity { get; set; }

#### Remarks

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

The default value is [ActiveHigh](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html). Specifies the [DCPowerPulsePolarity](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsepolarity.html) enumeration.

Parent topic:

DCPowerReadyForPulseTriggerEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse-width.html language=enus -->
## TOPIC 00331: Width

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse-width.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the width, in seconds, of the DCPowerReadyForPulseTriggerEvent event pulse. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic PrecisionTimeSpan Width { get; set; }RemarksValid values range from 1.5e-7 to 1.6e-6.The default value is 1.5e-7. This property is not supp

### Width

Gets or sets the width, in seconds, of the [DCPowerReadyForPulseTriggerEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggerevent.html) event pulse.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public PrecisionTimeSpan Width { get; set; }

#### Remarks

Valid values range from 1.5e-7 to 1.6e-6.

The default value is 1.5e-7.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerReadyForPulseTriggerEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse.html language=enus -->
## TOPIC 00332: DCPowerReadyForPulseTriggerEventPulse Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerreadyforpulsetriggereventpulse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the pulse of ReadyForPulseTriggerEvent. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerReadyForPulseTriggerEventPulse : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supp

### DCPowerReadyForPulseTriggerEventPulse Class

Represents the properties used to configure the pulse of [ReadyForPulseTriggerEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-readyforpulsetriggerevent.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerReadyForPulseTriggerEventPulse : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Polarity | Gets or sets the behavior of the DCPowerReadyForPulseTriggerEvent event. |
| Width | Gets or sets the width, in seconds, of the DCPowerReadyForPulseTriggerEvent event pulse. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal-operator_eq__dcpowersequenceadvancetriggerexportedoutputterminal-dcpowersequenceadva...d828e392.html language=enus -->
## TOPIC 00333: operator==(DCPowerSequenceAdvanceTriggerExportedOutputTerminal, DCPowerSequenceAdvanceTriggerExportedOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal-operator_eq__dcpowersequenceadvancetriggerexportedoutputterminal-dcpowersequenceadva...d828e392.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal-operator_eq__dcpowersequenceadvancetriggerexportedoutputterminal-dcpowersequenceadva...d828e392.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerSequenceAdvanceTriggerExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerSequenceAdvanceTriggerExportedOutputTerminal outputTerminal1, DCPowerSequenceAdvanceTriggerExported

### operator==(DCPowerSequenceAdvanceTriggerExportedOutputTerminal, DCPowerSequenceAdvanceTriggerExportedOutputTerminal)

Checks whether the two instances of [DCPowerSequenceAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerSequenceAdvanceTriggerExportedOutputTerminal outputTerminal1, DCPowerSequenceAdvanceTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerSequenceAdvanceTriggerExportedOutputTerminal | Specifies a DCPowerSequenceAdvanceTriggerExportedOutputTerminal object. |
| outputTerminal2 | DCPowerSequenceAdvanceTriggerExportedOutputTerminal | Specifies a DCPowerSequenceAdvanceTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerSequenceAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal-operator_neq__dcpowersequenceadvancetriggerexportedoutputterminal-dcpowersequenceadv...d828e337.html language=enus -->
## TOPIC 00334: operator!=(DCPowerSequenceAdvanceTriggerExportedOutputTerminal, DCPowerSequenceAdvanceTriggerExportedOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal-operator_neq__dcpowersequenceadvancetriggerexportedoutputterminal-dcpowersequenceadv...d828e337.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal-operator_neq__dcpowersequenceadvancetriggerexportedoutputterminal-dcpowersequenceadv...d828e337.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerSequenceAdvanceTriggerExportedOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerSequenceAdvanceTriggerExportedOutputTerminal outputTerminal1, DCPowerSequenceAdvanceTriggerExport

### operator!=(DCPowerSequenceAdvanceTriggerExportedOutputTerminal, DCPowerSequenceAdvanceTriggerExportedOutputTerminal)

Checks whether the two instances of [DCPowerSequenceAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceadvancetriggerexportedoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerSequenceAdvanceTriggerExportedOutputTerminal outputTerminal1, DCPowerSequenceAdvanceTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerSequenceAdvanceTriggerExportedOutputTerminal | Specifies DCPowerSequenceAdvanceTriggerExportedOutputTerminal object. |
| outputTerminal2 | DCPowerSequenceAdvanceTriggerExportedOutputTerminal | Specifies DCPowerSequenceAdvanceTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerSequenceAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator-dcpowersequenceenginedoneeventoutputterminal__string.html language=enus -->
## TOPIC 00335: operator DCPowerSequenceEngineDoneEventOutputTerminal(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator-dcpowersequenceenginedoneeventoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator-dcpowersequenceenginedoneeventoutputterminal__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent DCPowerSequenceEngineDoneEventOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator DCPowerSequenceEngineDoneEventOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutput

### operator DCPowerSequenceEngineDoneEventOutputTerminal(string)

Converts the specified string to the equivalent [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator DCPowerSequenceEngineDoneEventOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent DCPowerSequenceEngineDoneEventOutputTerminal object. |

#### Returns

Returns an object of type [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) from the string passed in outputTerminal.

Parent topic:

DCPowerSequenceEngineDoneEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator-string__dcpowersequenceenginedoneeventoutputterminal.html language=enus -->
## TOPIC 00336: operator string(DCPowerSequenceEngineDoneEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator-string__dcpowersequenceenginedoneeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator-string__dcpowersequenceenginedoneeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the DCPowerSequenceEngineDoneEventOutputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator string(DCPowerSequenceEngineDoneEventOutputTerminal outputTerminal)ParametersNameTypeDescriptionoutputTerminalDC

### operator string(DCPowerSequenceEngineDoneEventOutputTerminal)

Converts the [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator string(DCPowerSequenceEngineDoneEventOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerSequenceEngineDoneEventOutputTerminal | Specifies the DCPowerSequenceEngineDoneEventOutputTerminal object to be converted to string. |

#### Returns

Returns a string from the [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) object.

Parent topic:

DCPowerSequenceEngineDoneEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator_eq__dcpowersequenceenginedoneeventoutputterminal-dcpowersequenceenginedoneeventoutputterminal.html language=enus -->
## TOPIC 00337: operator==(DCPowerSequenceEngineDoneEventOutputTerminal, DCPowerSequenceEngineDoneEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator_eq__dcpowersequenceenginedoneeventoutputterminal-dcpowersequenceenginedoneeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-operator_eq__dcpowersequenceenginedoneeventoutputterminal-dcpowersequenceenginedoneeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerSequenceEngineDoneEventOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerSequenceEngineDoneEventOutputTerminal outputTerminal1, DCPowerSequenceEngineDoneEventOutputTerminal output

### operator==(DCPowerSequenceEngineDoneEventOutputTerminal, DCPowerSequenceEngineDoneEventOutputTerminal)

Checks whether the two instances of [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerSequenceEngineDoneEventOutputTerminal outputTerminal1, DCPowerSequenceEngineDoneEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerSequenceEngineDoneEventOutputTerminal | Specifies a DCPowerSequenceEngineDoneEventOutputTerminal object. |
| outputTerminal2 | DCPowerSequenceEngineDoneEventOutputTerminal | Specifies a DCPowerSequenceEngineDoneEventOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerSequenceEngineDoneEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-pxitriggerline3.html language=enus -->
## TOPIC 00338: PxiTriggerLine3

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-pxitriggerline3.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSequenceEngineDoneEventOutputTerminal PxiTriggerLine3 { get; }RemarksReturns an object of type DCPowerSequenceEngineDoneEventOutp

### PxiTriggerLine3

Gets the destination terminal when the signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) representing the string "PXI_Trig3".

Parent topic:

DCPowerSequenceEngineDoneEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00339: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSequenceEngineDoneEventOutputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerSequenceEngineDoneEventOutp

### PxiTriggerLine7

Gets the destination terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerSequenceEngineDoneEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerSequenceEngineDoneEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventpulse-width.html language=enus -->
## TOPIC 00340: Width

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventpulse-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventpulse-width.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the width, in seconds, of the SequenceEngineDoneEvent event pulse. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic PrecisionTimeSpan Width { get; set; }RemarksValid Values range from 1.5e-7 to 1.6e-6.The default value is 1.5e-7. This property is not supported by

### Width

Gets or sets the width, in seconds, of the [SequenceEngineDoneEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sequenceenginedoneevent.html) event pulse.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public PrecisionTimeSpan Width { get; set; }

#### Remarks

Valid Values range from 1.5e-7 to 1.6e-6.

The default value is 1.5e-7.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerSequenceEngineDoneEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventtoggle-initialstate.html language=enus -->
## TOPIC 00341: InitialState

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventtoggle-initialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventtoggle-initialstate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial toggle state of the event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEventToggleInitialState InitialState { get; set; }RemarksSpecifies the initial toggle state of the SequenceEngineDoneEvent if you set the OutputBehavior to Toggle. This pro

### InitialState

Specifies the initial toggle state of the event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEventToggleInitialState](nationalinstruments-modularinstruments-nidcpower-dcpowereventtoggleinitialstate.html) InitialState { get; set; }

#### Remarks

Specifies the initial toggle state of the [SequenceEngineDoneEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sequenceenginedoneevent.html) if you set the [OutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneevent-outputbehavior.html) to [Toggle](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerSequenceEngineDoneEventToggle Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventtoggle.html language=enus -->
## TOPIC 00342: DCPowerSequenceEngineDoneEventToggle Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventtoggle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceenginedoneeventtoggle.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the toggle for sequence engine done event. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerSequenceEngineDoneEventToggle : DCPowerSubObjectPropertiesNameDescriptionInitialStateSpecifies the i

### DCPowerSequenceEngineDoneEventToggle Class

Represents the properties used to configure the toggle for sequence engine done event.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerSequenceEngineDoneEventToggle : DCPowerSubObject

#### Properties

| Name | Description |
| --- | --- |
| InitialState | Specifies the initial toggle state of the event. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-outputbehavior.html language=enus -->
## TOPIC 00343: OutputBehavior

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-outputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-outputbehavior.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output behavior of the DCPowerSequenceIterationCompleteEventSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEventOutputBehavior OutputBehavior { get; set; }RemarksSpecifies the DCPowerEventOutputBehavior for exporting the DCPowerSequenceIterationComple

### OutputBehavior

Gets or sets the output behavior of the [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html)

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEventOutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html) OutputBehavior { get; set; }

#### Remarks

Specifies the [DCPowerEventOutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html) for exporting the [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerSequenceIterationCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-pulse.html language=enus -->
## TOPIC 00344: Pulse

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-pulse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse characteristics of the DCPowerSequenceIterationCompleteEvent event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSequenceIterationCompleteEventPulse Pulse { get; }RemarksSpecifies an object of type Pulse.

### Pulse

Gets the pulse characteristics of the [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html) event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSequenceIterationCompleteEventPulse](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventpulse.html) Pulse { get; }

#### Remarks

Specifies an object of type Pulse.

Parent topic:

DCPowerSequenceIterationCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-toggle.html language=enus -->
## TOPIC 00345: Toggle

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-toggle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-toggle.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets and sets the toggle characteristics of the DCPowerSequenceIterationCompleteEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSequenceIterationCompleteEventToggle Toggle { get; set; }RemarksReturns a DCPowerSequenceIterationCompleteEventToggle that is used to

### Toggle

Gets and sets the toggle characteristics of the [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSequenceIterationCompleteEventToggle](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventtoggle.html) Toggle { get; set; }

#### Remarks

Returns a [DCPowerSequenceIterationCompleteEventToggle](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventtoggle.html) that is used to configure the toggle characteristics of the [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerSequenceIterationCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-waitforevent__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00346: WaitForEvent(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-waitforevent__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-waitforevent__nationalinstruments.precisiontimespan.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the device has generated the specified event. The session monitors whether each type of event has occurred at least once since the last time this method or the Initiate method was called. If an event has only been generated once, and you call this method successively, the method times ou

### WaitForEvent(NationalInstruments.PrecisionTimeSpan)

Waits until the device has generated the specified event. The session monitors whether each type of event has occurred at least once since the last time this method or the [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html) method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void WaitForEvent(NationalInstruments.PrecisionTimeSpan timeout)

#### Remarks

Note

This method must only be called in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete, in seconds. If the method does not complete within this time interval, NIDCPower returns an error. |

Parent topic:

DCPowerSequenceIterationCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-gethashcode.html language=enus -->
## TOPIC 00347: GetHashCode()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-gethashcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of DCPowerSequenceIterationCompleteEventOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of DCPowe

### GetHashCode()

Returns the hash code for the current instance of [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html).

Parent topic:

DCPowerSequenceIterationCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-operator_eq__dcpowersequenceiterationcompleteeventoutputterminal-dcpowersequenceiter...d883e391.html language=enus -->
## TOPIC 00348: operator==(DCPowerSequenceIterationCompleteEventOutputTerminal, DCPowerSequenceIterationCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-operator_eq__dcpowersequenceiterationcompleteeventoutputterminal-dcpowersequenceiter...d883e391.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-operator_eq__dcpowersequenceiterationcompleteeventoutputterminal-dcpowersequenceiter...d883e391.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerSequenceIterationCompleteEventOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerSequenceIterationCompleteEventOutputTerminal outputTerminal1, DCPowerSequenceIterationCompleteEvent

### operator==(DCPowerSequenceIterationCompleteEventOutputTerminal, DCPowerSequenceIterationCompleteEventOutputTerminal)

Checks whether the two instances of [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerSequenceIterationCompleteEventOutputTerminal outputTerminal1, DCPowerSequenceIterationCompleteEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerSequenceIterationCompleteEventOutputTerminal | Specifies a DCPowerSequenceIterationCompleteEventOutputTerminal object. |
| outputTerminal2 | DCPowerSequenceIterationCompleteEventOutputTerminal | Specifies a DCPowerSequenceIterationCompleteEventOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerSequenceIterationCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00349: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSequenceIterationCompleteEventOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerSequenceIterationCom

### PxiTriggerLine6

Gets the destination terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerSequenceIterationCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00350: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSequenceIterationCompleteEventOutputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerSequenceIterationCom

### PxiTriggerLine7

Gets the destination terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerSequenceIterationCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-tostring.html language=enus -->
## TOPIC 00351: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerSequenceIterationCompleteEventOutputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a String that represents the current instance of DCPowerSequenceIterationCompleteEventOut

### ToString()

Converts the current instance of [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a String that represents the current instance of [DCPowerSequenceIterationCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html).

Parent topic:

DCPowerSequenceIterationCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html language=enus -->
## TOPIC 00352: DCPowerSequenceIterationCompleteEventOutputTerminal Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the destination terminal for DCPowerSequenceIterationCompleteEvent. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerSequenceIterationCompleteEventOutputTerminalRemarksSee OutputTerminal. Thread SafetyAll members of this type are safe fo

### DCPowerSequenceIterationCompleteEventOutputTerminal Class

Represents the destination terminal for [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerSequenceIterationCompleteEventOutputTerminal

#### Remarks

See [OutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-outputterminal.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DoNotExport | Gets the destination terminal when the signal is not exported. |
| PxiTriggerLine0 | Gets the destination terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the destination terminal when the signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the destination terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the destination terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the destination terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the destination terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the destination terminal when the signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the destination terminal when the signal is exported to the PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an DCPowerSequenceIterationCompleteEventOutputTerminal object from the specified string. |
| Equals(DCPowerSequenceIterationCompleteEventOutputTerminal) | Determines whether the current instance of DCPowerSequenceIterationCompleteEventOutputTerminal and the DCPowerSequenceIterationCompleteEventOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of DCPowerSequenceIterationCompleteEventOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of DCPowerSequenceIterationCompleteEventOutputTerminal. |
| ToString() | Converts the current instance of DCPowerSequenceIterationCompleteEventOutputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator DCPowerSequenceIterationCompleteEventOutputTerminal(string) | Converts the specified string to the equivalent DCPowerSequenceIterationCompleteEventOutputTerminal object. |
| operator string(DCPowerSequenceIterationCompleteEventOutputTerminal) | Converts the DCPowerSequenceIterationCompleteEventOutputTerminal object to the equivalent string. |
| operator!=(DCPowerSequenceIterationCompleteEventOutputTerminal, DCPowerSequenceIterationCompleteEventOutputTerminal) | Checks whether the two instances of DCPowerSequenceIterationCompleteEventOutputTerminal are unequal. |
| operator==(DCPowerSequenceIterationCompleteEventOutputTerminal, DCPowerSequenceIterationCompleteEventOutputTerminal) | Checks whether the two instances of DCPowerSequenceIterationCompleteEventOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventpulse.html language=enus -->
## TOPIC 00353: DCPowerSequenceIterationCompleteEventPulse Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventpulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventpulse.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the pulse of SequenceIterationCompleteEvent. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerSequenceIterationCompleteEventPulse : DCPowerSubObjectRemarksFor more information, refer to NI DC

### DCPowerSequenceIterationCompleteEventPulse Class

Represents the properties used to configure the pulse of [SequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sequenceiterationcompleteevent.html).

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerSequenceIterationCompleteEventPulse : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Polarity | Gets or sets the behavior of the SequenceIterationCompleteEvent. |
| Width | Gets or sets the width, in seconds, of the SequenceIterationCompleteEvent pulse. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventtoggle-initialstate.html language=enus -->
## TOPIC 00354: InitialState

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventtoggle-initialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteeventtoggle-initialstate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial toggle state of the event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEventToggleInitialState InitialState { get; set; }RemarksSpecifies the initial toggle state of the DCPowerSequenceIterationCompleteEvent if you set the OutputBehavior to To

### InitialState

Specifies the initial toggle state of the event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEventToggleInitialState](nationalinstruments-modularinstruments-nidcpower-dcpowereventtoggleinitialstate.html) InitialState { get; set; }

#### Remarks

Specifies the initial toggle state of the [DCPowerSequenceIterationCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent.html) if you set the [OutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowersequenceiterationcompleteevent-outputbehavior.html) to [Toggle](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerSequenceIterationCompleteEventToggle Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowershutdowntriggertype.html language=enus -->
## TOPIC 00355: DCPowerShutdownTriggerType Enumeration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowershutdowntriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowershutdowntriggertype.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for the Type property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic enum DCPowerShutdownTriggerTypeMembersNameValueDescriptionNone(int)1012Specifies that no trigger is configured. DigitalEdge(int)1014Specifies that the data operation starts when a digital

### DCPowerShutdownTriggerType Enumeration

Specifies values for the [Type](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputshutdowntrigger-type.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public enum DCPowerShutdownTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | (int)1012 | Specifies that no trigger is configured. |
| DigitalEdge | (int)1014 | Specifies that the data operation starts when a digital edge is detected. |
| SoftwareEdge | (int)1015 | Specifies that the data operation starts when a software trigger occurs. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersource-issequenceloopcountfinite.html language=enus -->
## TOPIC 00356: IsSequenceLoopCountFinite

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersource-issequenceloopcountfinite.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersource-issequenceloopcountfinite.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether a sequence should repeat indefinitely. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool IsSequenceLoopCountFinite { get; set; }RemarksThe default value is true. If this property is set to false, this property is ignored. Refer to the Sequence Source M

### IsSequenceLoopCountFinite

Gets or sets whether a sequence should repeat indefinitely.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool IsSequenceLoopCountFinite { get; set; }

#### Remarks

The default value is **true**. If this property is set to **false**, this property is ignored.

Sequence Source Mode

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersource-mode.html language=enus -->
## TOPIC 00357: Mode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersource-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersource-mode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to run a single output point or a sequence. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSourceMode Mode { get; set; }RemarksRefer to the Single Point Source Mode and Sequence Source Mode topics in the NI DC Power Supplies and SMUs Help for more

### Mode

Gets or sets whether to run a single output point or a sequence.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceMode](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html) Mode { get; set; }

#### Remarks

Refer to the [Single Point Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_singlept) and [Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing) topics in the *NI DC Power Supplies and SMUs Help* for more information about source modes.

The default value is [SinglePoint](nationalinstruments-modularinstruments-nidcpower-dcpowersourcemode.html).

Parent topic:

DCPowerSource Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent-outputterminal.html language=enus -->
## TOPIC 00358: OutputTerminal

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent-outputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output terminal for exporting the DCPowerSourceCompleteEvent. Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened

### OutputTerminal

Gets or sets the output terminal for exporting the [DCPowerSourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent.html). Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) OutputTerminal { get; set; }

#### Remarks

Specifies an object of type NationalInstruments.ModularInstruments.NIDCPower.DCPowerSourceCompleteEvent 
.OutputTerminal.

Note

The NI PXI-4110 and NI PXI-4130 do not support this property.

Parent topic:

DCPowerSourceCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent-waitforevent__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00359: WaitForEvent(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent-waitforevent__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent-waitforevent__nationalinstruments.precisiontimespan.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the device has generated the specified event. The session monitors whether each type of event has occurred at least once since the last time this method or the Initiate method was called. If an event has only been generated once, and you call this method successively, the method times ou

### WaitForEvent(NationalInstruments.PrecisionTimeSpan)

Waits until the device has generated the specified event. The session monitors whether each type of event has occurred at least once since the last time this method or the [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol-initiate.html) method was called. If an event has only been generated once, and you call this method successively, the method times out. Individual events must be generated between separate calls of this method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void WaitForEvent(NationalInstruments.PrecisionTimeSpan timeout)

#### Remarks

Note

This method must only be called in the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete, in seconds. If the method does not complete within this time interval, NIDCPower returns an error. |

Parent topic:

DCPowerSourceCompleteEvent Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-equals__dcpowersourcecompleteeventoutputterminal.html language=enus -->
## TOPIC 00360: Equals(DCPowerSourceCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-equals__dcpowersourcecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-equals__dcpowersourcecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerSourceCompleteEventOutputTerminal and the DCPowerSourceCompleteEventOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerSourceCompleteEventOutputTerminal outputT

### Equals(DCPowerSourceCompleteEventOutputTerminal)

Determines whether the current instance of [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) and the [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerSourceCompleteEventOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | DCPowerSourceCompleteEventOutputTerminal | Specifies the DCPowerSourceCompleteEventOutputTerminal object to be compared to the current instance of DCPowerSourceCompleteEventOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-equals__object.html language=enus -->
## TOPIC 00361: Equals(object)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-equals__object.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of DCPowerSourceCompleteEventOutputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be comp

### Equals(object)

Determines whether the current instance of [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of DCPowerSourceCompleteEventOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-operator-dcpowersourcecompleteeventoutputterminal__string.html language=enus -->
## TOPIC 00362: operator DCPowerSourceCompleteEventOutputTerminal(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-operator-dcpowersourcecompleteeventoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-operator-dcpowersourcecompleteeventoutputterminal__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent DCPowerSourceCompleteEventOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator DCPowerSourceCompleteEventOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutputTerminal

### operator DCPowerSourceCompleteEventOutputTerminal(string)

Converts the specified string to the equivalent [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator DCPowerSourceCompleteEventOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent DCPowerSourceCompleteEventOutputTerminal object. |

#### Returns

Returns an object of type [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) from the string passed in outputTerminal.

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-operator_neq__dcpowersourcecompleteeventoutputterminal-dcpowersourcecompleteeventoutputterminal.html language=enus -->
## TOPIC 00363: operator!=(DCPowerSourceCompleteEventOutputTerminal, DCPowerSourceCompleteEventOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-operator_neq__dcpowersourcecompleteeventoutputterminal-dcpowersourcecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-operator_neq__dcpowersourcecompleteeventoutputterminal-dcpowersourcecompleteeventoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerSourceCompleteEventOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerSourceCompleteEventOutputTerminal outputTerminal1, DCPowerSourceCompleteEventOutputTerminal outputTerminal2)

### operator!=(DCPowerSourceCompleteEventOutputTerminal, DCPowerSourceCompleteEventOutputTerminal)

Checks whether the two instances of [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerSourceCompleteEventOutputTerminal outputTerminal1, DCPowerSourceCompleteEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerSourceCompleteEventOutputTerminal | Specifies DCPowerSourceCompleteEventOutputTerminal object. |
| outputTerminal2 | DCPowerSourceCompleteEventOutputTerminal | Specifies DCPowerSourceCompleteEventOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00364: PxiTriggerLine0

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline0.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSourceCompleteEventOutputTerminal PxiTriggerLine0 { get; }RemarksAn object of type DCPowerSourceCompleteEventOutputTerminal repre

### PxiTriggerLine0

Gets the destination terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

An object of type [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00365: PxiTriggerLine1

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline1.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSourceCompleteEventOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type DCPowerSourceCompleteEventOutputTermin

### PxiTriggerLine1

Gets the destination terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00366: PxiTriggerLine5

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline5.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSourceCompleteEventOutputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type DCPowerSourceCompleteEventOutputTermin

### PxiTriggerLine5

Gets the destination terminal when the signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) representing the string "PXI_Trig5".

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00367: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSourceCompleteEventOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerSourceCompleteEventOutputTermin

### PxiTriggerLine6

Gets the destination terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00368: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSourceCompleteEventOutputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerSourceCompleteEventOutputTermin

### PxiTriggerLine7

Gets the destination terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-tostring.html language=enus -->
## TOPIC 00369: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerSourceCompleteEventOutputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a String that represents the current instance of DCPowerSourceCompleteEventOutputTerminal.

### ToString()

Converts the current instance of [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a String that represents the current instance of [DCPowerSourceCompleteEventOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventoutputterminal.html).

Parent topic:

DCPowerSourceCompleteEventOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventpulse-width.html language=enus -->
## TOPIC 00370: Width

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventpulse-width.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventpulse-width.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the width, in seconds, of the SourceCompleteEvent pulse. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic PrecisionTimeSpan Width { get; set; }RemarksValid values range from 1.5e-7 to 1.6e-6. The default value is 1.5e-7. This property is not supported by all instr

### Width

Gets or sets the width, in seconds, of the [SourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sourcecompleteevent.html) pulse.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public PrecisionTimeSpan Width { get; set; }

#### Remarks

Valid values range from 1.5e-7 to 1.6e-6.

The default value is 1.5e-7.

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

Parent topic:

DCPowerSourceCompleteEventPulse Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventtoggle-initialstate.html language=enus -->
## TOPIC 00371: InitialState

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventtoggle-initialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteeventtoggle-initialstate.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial toggle state of the event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEventToggleInitialState InitialState { get; set; }RemarksSpecifies the initial toggle state of the SourceCompleteEvent if you set the OutputBehavior to Toggle. This propert

### InitialState

Specifies the initial toggle state of the event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEventToggleInitialState](nationalinstruments-modularinstruments-nidcpower-dcpowereventtoggleinitialstate.html) InitialState { get; set; }

#### Remarks

Specifies the initial toggle state of the [SourceCompleteEvent](nationalinstruments-modularinstruments-nidcpower-dcpowerevents-sourcecompleteevent.html) if you set the [OutputBehavior](nationalinstruments-modularinstruments-nidcpower-dcpowersourcecompleteevent-outputbehavior.html) to [Toggle](nationalinstruments-modularinstruments-nidcpower-dcpowereventoutputbehavior.html).

Note

This property is not supported by all instruments. Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

**Default Value**:Refer to the [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) topic in the *NI DC Power Supplies and SMUs Help* for the default value by instrument.

Parent topic:

DCPowerSourceCompleteEventToggle Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcetrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00372: SendSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcetrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcetrigger-sendsoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a Software Edge SourceTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SendSoftwareEdgeTrigger()RemarksThis method can override an external edge trigger. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe SendSoftwareEdgeTrigger method was accessed

### SendSoftwareEdgeTrigger()

Sends a Software Edge [SourceTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-sourcetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

This method can override an external edge trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SendSoftwareEdgeTrigger method was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerSourceTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-operator_eq__dcpowersourcetriggerexportedoutputterminal-dcpowersourcetriggerexportedoutputterminal.html language=enus -->
## TOPIC 00373: operator==(DCPowerSourceTriggerExportedOutputTerminal, DCPowerSourceTriggerExportedOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-operator_eq__dcpowersourcetriggerexportedoutputterminal-dcpowersourcetriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-operator_eq__dcpowersourcetriggerexportedoutputterminal-dcpowersourcetriggerexportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerSourceTriggerExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerSourceTriggerExportedOutputTerminal outputTerminal1, DCPowerSourceTriggerExportedOutputTerminal outputTermin

### operator==(DCPowerSourceTriggerExportedOutputTerminal, DCPowerSourceTriggerExportedOutputTerminal)

Checks whether the two instances of [DCPowerSourceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerSourceTriggerExportedOutputTerminal outputTerminal1, DCPowerSourceTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerSourceTriggerExportedOutputTerminal | Specifies a DCPowerSourceTriggerExportedOutputTerminal object. |
| outputTerminal2 | DCPowerSourceTriggerExportedOutputTerminal | Specifies a DCPowerSourceTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerSourceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00374: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSourceTriggerExportedOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerSourceTriggerExportedOutputTermina

### PxiTriggerLine6

Gets the output terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSourceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerSourceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerSourceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00375: PxiTriggerLine7

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal-pxitriggerline7.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerSourceTriggerExportedOutputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type DCPowerSourceTriggerExportedOutputTermina

### PxiTriggerLine7

Gets the output terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerSourceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [DCPowerSourceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowersourcetriggerexportedoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

DCPowerSourceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00376: SendSoftwareEdgeTrigger()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger-sendsoftwareedgetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a Software Edge StartTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void SendSoftwareEdgeTrigger()RemarksThis method can override an external edge trigger. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe SendSoftwareEdgeTrigger method was accessed a

### SendSoftwareEdgeTrigger()

Sends a Software Edge [StartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-starttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

This method can override an external edge trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SendSoftwareEdgeTrigger method was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger-type.html language=enus -->
## TOPIC 00377: Type

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger-type.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the DCPowerStartTriggerType. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerStartTriggerType Type { get; set; }RemarksSpecifies the DCPowerStartTriggerType enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Type property was accessed

### Type

Gets or sets the [DCPowerStartTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerStartTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggertype.html) Type { get; set; }

#### Remarks

Specifies the [DCPowerStartTriggerType](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggertype.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Type property was accessed after the associated NIDCPower object was disposed. |

Parent topic:

DCPowerStartTrigger Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator-dcpowerstarttriggerexportedoutputterminal__string.html language=enus -->
## TOPIC 00378: operator DCPowerStartTriggerExportedOutputTerminal(string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator-dcpowerstarttriggerexportedoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator-dcpowerstarttriggerexportedoutputterminal__string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent DCPowerStartTriggerExportedOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static implicit operator DCPowerStartTriggerExportedOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutputTermin

### operator DCPowerStartTriggerExportedOutputTerminal(string)

Converts the specified string to the equivalent [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static implicit operator DCPowerStartTriggerExportedOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent DCPowerStartTriggerExportedOutputTerminal object. |

#### Returns

Returns an object of type [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) from the string passed in *outputTerminal*.

Parent topic:

DCPowerStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator_eq__dcpowerstarttriggerexportedoutputterminal-dcpowerstarttriggerexportedoutputterminal.html language=enus -->
## TOPIC 00379: operator==(DCPowerStartTriggerExportedOutputTerminal, DCPowerStartTriggerExportedOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator_eq__dcpowerstarttriggerexportedoutputterminal-dcpowerstarttriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator_eq__dcpowerstarttriggerexportedoutputterminal-dcpowerstarttriggerexportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerStartTriggerExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerStartTriggerExportedOutputTerminal outputTerminal1, DCPowerStartTriggerExportedOutputTerminal outputTerminal2

### operator==(DCPowerStartTriggerExportedOutputTerminal, DCPowerStartTriggerExportedOutputTerminal)

Checks whether the two instances of [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerStartTriggerExportedOutputTerminal outputTerminal1, DCPowerStartTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerStartTriggerExportedOutputTerminal | Specifies a DCPowerStartTriggerExportedOutputTerminal object. |
| outputTerminal2 | DCPowerStartTriggerExportedOutputTerminal | Specifies a DCPowerStartTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator_neq__dcpowerstarttriggerexportedoutputterminal-dcpowerstarttriggerexportedoutputterminal.html language=enus -->
## TOPIC 00380: operator!=(DCPowerStartTriggerExportedOutputTerminal, DCPowerStartTriggerExportedOutputTerminal)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator_neq__dcpowerstarttriggerexportedoutputterminal-dcpowerstarttriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-operator_neq__dcpowerstarttriggerexportedoutputterminal-dcpowerstarttriggerexportedoutputterminal.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerStartTriggerExportedOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerStartTriggerExportedOutputTerminal outputTerminal1, DCPowerStartTriggerExportedOutputTerminal outputTermina

### operator!=(DCPowerStartTriggerExportedOutputTerminal, DCPowerStartTriggerExportedOutputTerminal)

Checks whether the two instances of [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerStartTriggerExportedOutputTerminal outputTerminal1, DCPowerStartTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | DCPowerStartTriggerExportedOutputTerminal | Specifies DCPowerStartTriggerExportedOutputTerminal object. |
| outputTerminal2 | DCPowerStartTriggerExportedOutputTerminal | Specifies DCPowerStartTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00381: PxiTriggerLine2

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-pxitriggerline2.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerStartTriggerExportedOutputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type DCPowerStartTriggerExportedOutputTerminal

### PxiTriggerLine2

Gets the output terminal when the signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) representing the string "PXI_Trig2".

Parent topic:

DCPowerStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00382: PxiTriggerLine6

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-pxitriggerline6.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static DCPowerStartTriggerExportedOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type DCPowerStartTriggerExportedOutputTerminal

### PxiTriggerLine6

Gets the output terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

DCPowerStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-tostring.html language=enus -->
## TOPIC 00383: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerStartTriggerExportedOutputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a string that represents the current instance of DCPowerStartTriggerExportedOutputTerminal.

### ToString()

Converts the current instance of [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [DCPowerStartTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttriggerexportedoutputterminal.html).

Parent topic:

DCPowerStartTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-measuretrigger.html language=enus -->
## TOPIC 00384: MeasureTrigger

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-measuretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-measuretrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerMeasureTrigger sub-object that is used to configure the Measure Trigger of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerMeasureTrigger MeasureTrigger { get; }RemarksReturns an object of type DCPowerMeasureTrigger .

### MeasureTrigger

Gets the [DCPowerMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger.html) sub-object that is used to configure the Measure Trigger of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger.html) MeasureTrigger { get; }

#### Remarks

Returns an object of type [DCPowerMeasureTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowermeasuretrigger.html) .

Parent topic:

DCPowerTriggers Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-pulsetrigger.html language=enus -->
## TOPIC 00385: PulseTrigger

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-pulsetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-pulsetrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerPulseTrigger sub-object that is used to configure the Pulse Trigger of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerPulseTrigger PulseTrigger { get; }RemarksReturns an object of type DCPowerPulseTrigger .

### PulseTrigger

Gets the [DCPowerPulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger.html) sub-object that is used to configure the Pulse Trigger of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerPulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger.html) PulseTrigger { get; }

#### Remarks

Returns an object of type [DCPowerPulseTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerpulsetrigger.html) .

Parent topic:

DCPowerTriggers Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-starttrigger.html language=enus -->
## TOPIC 00386: StartTrigger

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-starttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowertriggers-starttrigger.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerStartTrigger sub-object that is used to configure the Start Trigger for NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerStartTrigger StartTrigger { get; }RemarksReturns an object of type DCPowerStartTrigger .

### StartTrigger

Gets the [DCPowerStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger.html) sub-object that is used to configure the Start Trigger for NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger.html) StartTrigger { get; }

#### Remarks

Returns an object of type [DCPowerStartTrigger](nationalinstruments-modularinstruments-nidcpower-dcpowerstarttrigger.html) .

Parent topic:

DCPowerTriggers Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowertriggers.html language=enus -->
## TOPIC 00387: DCPowerTriggers Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowertriggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowertriggers.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides underlying triggers of specific types. Derives fromDCPowerSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerTriggers : DCPowerSubObjectRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Thread SafetyAll members of this type

### DCPowerTriggers Class

Provides underlying triggers of specific types.

#### Derives from

- DCPowerSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerTriggers : DCPowerSubObject

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| MeasureTrigger | Gets the DCPowerMeasureTrigger sub-object that is used to configure the Measure Trigger of NI-DCPower. |
| PulseTrigger | Gets the DCPowerPulseTrigger sub-object that is used to configure the Pulse Trigger of NI-DCPower. |
| SequenceAdvanceTrigger | Gets the DCPowerSequenceAdvanceTrigger sub-object that is used to configure the Sequence Advance Trigger of NI-DCPower. |
| SourceTrigger | Gets the DCPowerSourceTrigger sub-object that is used to configure the Source Trigger of NI-DCPower. |
| StartTrigger | Gets the DCPowerStartTrigger sub-object that is used to configure the Start Trigger for NI-DCPower. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-code.html language=enus -->
## TOPIC 00388: Code

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-code.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-code.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the GUID code assigned to the warning. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic Guid Code { get; private set; }RemarksReturns the System.Guid code of the warning.

### Code

Gets the GUID code assigned to the warning.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public Guid Code { get; private set; }

#### Remarks

Returns the System.Guid code of the warning.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-equals__dcpowerwarning-bool.html language=enus -->
## TOPIC 00389: Equals(DCPowerWarning, bool)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-equals__dcpowerwarning-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-equals__dcpowerwarning-bool.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks for the equality for the two DCPowerWarning objects considering whether warning message should be compared or not. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool Equals(DCPowerWarning warning, bool ignoreWarningMessage)ParametersNameTypeDescriptionwarningDCPowerW

### Equals(DCPowerWarning, bool)

Checks for the equality for the two [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html) objects considering whether warning message should be compared or not.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool Equals(DCPowerWarning warning, bool ignoreWarningMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warning | DCPowerWarning | Specifies the DCPowerWarning object to which this object is compared. |
| ignoreWarningMessage | bool | Specifies if the warning message must be ignored. If the warning message is to be ignored,then value of ignoreWarningMessage is true. If warning message is to be compared then value of ignoreWarningMessage is false. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-errorquerynotsupportedwarningcode.html language=enus -->
## TOPIC 00390: ErrorQueryNotSupportedWarningCode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-errorquerynotsupportedwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-errorquerynotsupportedwarningcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when Error Query is not supported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static Guid ErrorQueryNotSupportedWarningCode { get; }RemarksReturns the GUID ("BE37BF5D-FAE5-44d0-8AA4-4B521D1D17DE") of the warning.

### ErrorQueryNotSupportedWarningCode

Gets the warning code when Error Query is not supported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static Guid ErrorQueryNotSupportedWarningCode { get; }

#### Remarks

Returns the GUID ("BE37BF5D-FAE5-44d0-8AA4-4B521D1D17DE") of the warning.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-gethashcode.html language=enus -->
## TOPIC 00391: GetHashCode()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-gethashcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of DCPowerWarning. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of DCPowerWarning.

### GetHashCode()

Returns the hash code for the current instance of [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html).

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-measurementoverrangewarningcode.html language=enus -->
## TOPIC 00392: MeasurementOverRangeWarningCode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-measurementoverrangewarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-measurementoverrangewarningcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when measurement is over range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static Guid MeasurementOverRangeWarningCode { get; }RemarksReturns the GUID ("c460573f-b0fc-43d4-a66c-96b25b90daa1") of the warning.

### MeasurementOverRangeWarningCode

Gets the warning code when measurement is over range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static Guid MeasurementOverRangeWarningCode { get; }

#### Remarks

Returns the GUID ("c460573f-b0fc-43d4-a66c-96b25b90daa1") of the warning.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-operator_eq__dcpowerwarning-dcpowerwarning.html language=enus -->
## TOPIC 00393: operator==(DCPowerWarning, DCPowerWarning)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-operator_eq__dcpowerwarning-dcpowerwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-operator_eq__dcpowerwarning-dcpowerwarning.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerWarning are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator==(DCPowerWarning warning1, DCPowerWarning warning2)ParametersNameTypeDescriptionwarning1DCPowerWarningSpecifies a DCPowerWarning object. warning2

### operator==(DCPowerWarning, DCPowerWarning)

Checks whether the two instances of [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator==(DCPowerWarning warning1, DCPowerWarning warning2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warning1 | DCPowerWarning | Specifies a DCPowerWarning object. |
| warning2 | DCPowerWarning | Specifies a DCPowerWarning object for the comparison. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-operator_neq__dcpowerwarning-dcpowerwarning.html language=enus -->
## TOPIC 00394: operator!=(DCPowerWarning, DCPowerWarning)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-operator_neq__dcpowerwarning-dcpowerwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-operator_neq__dcpowerwarning-dcpowerwarning.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of DCPowerWarning are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static bool operator!=(DCPowerWarning warning1, DCPowerWarning warning2)ParametersNameTypeDescriptionwarning1DCPowerWarningSpecifies a DCPowerWarning object. warnin

### operator!=(DCPowerWarning, DCPowerWarning)

Checks whether the two instances of [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static bool operator!=(DCPowerWarning warning1, DCPowerWarning warning2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warning1 | DCPowerWarning | Specifies a DCPowerWarning object. |
| warning2 | DCPowerWarning | Specifies a DCPowerWarning object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-rangecheckinprogresswarningcode.html language=enus -->
## TOPIC 00395: RangeCheckInProgressWarningCode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-rangecheckinprogresswarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-rangecheckinprogresswarningcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code when measurement was attempted while a range check was in progress. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static Guid RangeCheckInProgressWarningCode { get; }RemarksReturns the GUID ("aea65ab2-7f4d-4b02-bc19-ca5ca689f5d6") of the warning.

### RangeCheckInProgressWarningCode

Gets the warning code when measurement was attempted while a range check was in progress.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static Guid RangeCheckInProgressWarningCode { get; }

#### Remarks

Returns the GUID ("aea65ab2-7f4d-4b02-bc19-ca5ca689f5d6") of the warning.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-text.html language=enus -->
## TOPIC 00396: Text

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-text.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-text.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the message related to the warning. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string Text { get; private set; }RemarksReturns the warning message.

### Text

Gets the message related to the warning.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string Text { get; private set; }

#### Remarks

Returns the warning message.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-tostring.html language=enus -->
## TOPIC 00397: ToString()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-tostring.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of DCPowerWarning to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic override string ToString()ReturnsReturns a String that represents the current instance of DCPowerWarning.

### ToString()

Converts the current instance of [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public override string ToString()

#### Returns

Returns a String that represents the current instance of [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html).

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-unexpecteddriverwarningcode.html language=enus -->
## TOPIC 00398: UnexpectedDriverWarningCode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-unexpecteddriverwarningcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning-unexpecteddriverwarningcode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning code for an unexpected driver warning. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic static Guid UnexpectedDriverWarningCode { get; }RemarksReturns the GUID ("2cca167a-dbe8-4ba4-88dd-8b8faaf7b119") of the warning.

### UnexpectedDriverWarningCode

Gets the warning code for an unexpected driver warning.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public static Guid UnexpectedDriverWarningCode { get; }

#### Remarks

Returns the GUID ("2cca167a-dbe8-4ba4-88dd-8b8faaf7b119") of the warning.

Parent topic:

DCPowerWarning Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html language=enus -->
## TOPIC 00399: DCPowerWarning Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides warning codes for the warnings raised by the underlying driver. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerWarningRemarksRepresents the list of warnings returned by the driver. Thread SafetyAll members of this type are safe for multi

### DCPowerWarning Class

Provides warning codes for the warnings raised by the underlying driver.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerWarning

#### Remarks

Represents the list of warnings returned by the driver.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets the GUID code assigned to the warning. |
| ErrorQueryNotSupportedWarningCode | Gets the warning code when Error Query is not supported. |
| MeasurementOverRangeWarningCode | Gets the warning code when measurement is over range. |
| RangeCheckInProgressWarningCode | Gets the warning code when measurement was attempted while a range check was in progress. |
| Text | Gets the message related to the warning. |
| UnexpectedDriverWarningCode | Gets the warning code for an unexpected driver warning. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(DCPowerWarning, bool) | Checks for the equality for the two DCPowerWarning objects considering whether warning message should be compared or not. |
| Equals(DCPowerWarning) | Determines whether the current instance of DCPowerWarning and the DCPowerWarning object that you specify are equal. |
| Equals(object) | Determines whether the current instance of DCPowerWarning and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of DCPowerWarning. |
| ToString() | Converts the current instance of DCPowerWarning to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(DCPowerWarning, DCPowerWarning) | Checks whether the two instances of DCPowerWarning are unequal. |
| operator==(DCPowerWarning, DCPowerWarning) | Checks whether the two instances of DCPowerWarning are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-code.html language=enus -->
## TOPIC 00400: Code

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-code.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-code.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Warning Event Args code. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic Guid Code { get; }RemarksReturns the System.Guid code of the warning.

### Code

Gets the Warning Event Args code.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public Guid Code { get; }

#### Remarks

Returns the System.Guid code of the warning.

Parent topic:

DCPowerWarningEventArgs Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-message.html language=enus -->
## TOPIC 00401: Message

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-message.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-message.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Warning Event Args message. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic string Message { get; }RemarksReturns a String representing the message.

### Message

Gets the Warning Event Args message.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public string Message { get; }

#### Remarks

Returns a String representing the message.

Parent topic:

DCPowerWarningEventArgs Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-warning.html language=enus -->
## TOPIC 00402: Warning

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-warning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs-warning.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the warning set in the Warning Event Args. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerWarning Warning { get; private set; }RemarksReturns an object of type DCPowerWarning.

### Warning

Gets the warning set in the Warning Event Args.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html) Warning { get; private set; }

#### Remarks

Returns an object of type [DCPowerWarning](nationalinstruments-modularinstruments-nidcpower-dcpowerwarning.html).

Parent topic:

DCPowerWarningEventArgs Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs.html language=enus -->
## TOPIC 00403: DCPowerWarningEventArgs Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-dcpowerwarningeventargs.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties under the Warning Event Args raised during a driver warning. Derives fromEventArgsSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class DCPowerWarningEventArgs : EventArgsRemarksFor more information, refer to NI DC Power Supplies and SMUs Help. Threa

### DCPowerWarningEventArgs Class

Represents the properties under the Warning Event Args raised during a driver warning.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class DCPowerWarningEventArgs : EventArgs

#### Remarks

For more information, refer to [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets the Warning Event Args code. |
| Message | Gets the Warning Event Args message. |
| Warning | Gets the warning set in the Warning Event Args. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-advanced.html language=enus -->
## TOPIC 00404: Advanced

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-advanced.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerAdvanced sub-object that provides advanced properties of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerAdvanced Advanced { get; }RemarksReturns an object of type DCPowerAdvanced.

### Advanced

Gets the [DCPowerAdvanced](nationalinstruments-modularinstruments-nidcpower-dcpoweradvanced.html) sub-object that provides advanced properties of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerAdvanced](nationalinstruments-modularinstruments-nidcpower-dcpoweradvanced.html) Advanced { get; }

#### Remarks

Returns an object of type [DCPowerAdvanced](nationalinstruments-modularinstruments-nidcpower-dcpoweradvanced.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-calibration.html language=enus -->
## TOPIC 00405: Calibration

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-calibration.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerCalibration sub-object that allows calibration of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerCalibration Calibration { get; }RemarksReturns an object of type DCPowerCalibration.

### Calibration

Gets the [DCPowerCalibration](nationalinstruments-modularinstruments-nidcpower-dcpowercalibration.html) sub-object that allows calibration of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerCalibration](nationalinstruments-modularinstruments-nidcpower-dcpowercalibration.html) Calibration { get; }

#### Remarks

Returns an object of type [DCPowerCalibration](nationalinstruments-modularinstruments-nidcpower-dcpowercalibration.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-close.html language=enus -->
## TOPIC 00406: Close()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-close.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-close.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the instrument and deallocates the resources that NI-DCPower reserved. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Close()RemarksIf power output is enabled when you call this method, the channels remain in their existing state and continue provi

### Close()

Closes the session to the instrument and deallocates the resources that NI-DCPower reserved.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Close()

#### Remarks

If power output is enabled when you call this method, the channels remain in their existing state and continue providing power. Use [Reset](nationalinstruments-modularinstruments-nidcpower-dcpowerdriverutility-reset.html) or [Enabled](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputsourceoutput-enabled.html) to disable power output on a per-channel basis.

The Close method can be called safely more than once, even if the session is already closed.

Calling close, disposes the SafeHandle used to hold the instrument handle. The ReleaseHandle method of the SafeHandle is overridden in our concrete implementation of SafeHandle, which calls into the Close of the Underlying driver. If a call to this Close fails for any reason, the most common being the session being closed by some external means, the user won't be notified of the failure. In order to help users identify failures in ReleaseHandle method, managed debugging assistant (MDA) is activated to notify developers when ReleaseHandle fails. [Common ways of externally closing a session: paraInitializing a session with a resource name for which a session is already open, within the same process. Initializing a new session with the same resource name causes the instrument handle held by the existing session to become invalid. paraUser gets the instrument handle out using the method and closes this handle directly. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. 10/3/2012 6:28:00 PM NI False](http://msdn.microsoft.com/en-us/library/85eak4a0.aspx)

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-control.html language=enus -->
## TOPIC 00407: Control

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-control.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerControl sub-object that provides methods to control the programming state of NI-DCPower. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerControl Control { get; }RemarksReturns an object of type DCPowerControl.

### Control

Gets the [DCPowerControl](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol.html) sub-object that provides methods to control the programming state of NI-DCPower.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerControl](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol.html) Control { get; }

#### Remarks

Returns an object of type [DCPowerControl](nationalinstruments-modularinstruments-nidcpower-dcpowercontrol.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-dispose.html language=enus -->
## TOPIC 00408: Dispose()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-dispose.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the specified session and deallocates the reserved resources, if not already disposed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void Dispose()RemarksYou can call this method safely more than once, even if the session is already closed. A call to this method disp

### Dispose()

Closes the specified session and deallocates the reserved resources, if not already disposed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void Dispose()

#### Remarks

You can call this method safely more than once, even if the session is already closed.

A call to this method disposes the **SafeHandle** class used to hold the instrument handle. If the call to this method fails due to some reason, like the session being closed by some external means, you will not be notified about the failure. To help you identify failures in the **ReleaseHandle** method of the **SafeHandle** class, managed debugging assistant (MDA) is activated.

For details refer to [. The call to this method fails when you externally close a session by: Initializing a session with a resource name for which the session is already open, within the same process. This causes the instrument handle held by the existing session to become invalid. Getting the instrument handle out using the method and closing this handle directly.](http://msdn.microsoft.com/en-us/library/85eak4a0.aspx)

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-events.html language=enus -->
## TOPIC 00409: Events

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-events.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerEvents sub-object to configure NI-DCPower events. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerEvents Events { get; }RemarksReturns an object of type DCPowerEvents.

### Events

Gets the [DCPowerEvents](nationalinstruments-modularinstruments-nidcpower-dcpowerevents.html) sub-object to configure NI-DCPower events.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerEvents](nationalinstruments-modularinstruments-nidcpower-dcpowerevents.html) Events { get; }

#### Remarks

Returns an object of type [DCPowerEvents](nationalinstruments-modularinstruments-nidcpower-dcpowerevents.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-exportsignal__dcpowersignalsource-string.html language=enus -->
## TOPIC 00410: ExportSignal(DCPowerSignalSource, string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-exportsignal__dcpowersignalsource-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-exportsignal__dcpowersignalsource-string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ExportSignal(DCPowerSignalSource signalSource, string outputTerminal)RemarksThis method is not support

### ExportSignal(DCPowerSignalSource, string)

Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ExportSignal(DCPowerSignalSource signalSource, string outputTerminal)

#### Remarks

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

See [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

- or -

The destination terminal to be routed cannot be found on the device.

- or -

The underlying NI-DCPower driver returned an error.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalSource | DCPowerSignalSource | The trigger or event signal to export. |
| outputTerminal | string | The terminal to route the signal to. For example, if the device is named "<tt>Dev1</tt>" and your terminal is "<tt>PXI_Trig0</tt>", you can specify the terminal with the fully qualified terminal name, "<tt>/Dev1/PXI_Trig0</tt>", or with the shortened terminal name, "<tt>PXI_Trig0</tt>". |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OperationNotSupportedException | ExportSignal(DCPowerSignalSource, string) was called on a session to unsupported hardware. |
| System.ObjectDisposedException | ExportSignal(DCPowerSignalSource, string) was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.IviCDriverException | The value of signalSource is invalid. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-exportsignal__string-dcpowersignalsource-string.html language=enus -->
## TOPIC 00411: ExportSignal(string, DCPowerSignalSource, string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-exportsignal__string-dcpowersignalsource-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-exportsignal__string-dcpowersignalsource-string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic void ExportSignal(string channelString, DCPowerSignalSource signalSource, string outputTerminal)RemarksThis

### ExportSignal(string, DCPowerSignalSource, string)

Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public void ExportSignal(string channelString, DCPowerSignalSource signalSource, string outputTerminal)

#### Remarks

Note

This method is not supported by all instruments. Refer to the [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) topic in the *NI DC Power Supplies and SMUs Help* for information about supported instruments.

See [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

- or -

The destination terminal to be routed cannot be found on the device.

- or -

The underlying NI-DCPower driver returned an error.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelString | string | The channel to which you export the signal. You can only export a signal to one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. |
| signalSource | DCPowerSignalSource | The trigger or event signal to export. |
| outputTerminal | string | The terminal to route the signal to. You can supply a fully qualified terminal name to this parameter, for example, /Dev1/PXI_Trig0, or /Dev1/Engine0/PXI_Trig0, where Engine0 is channel 0. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OperationNotSupportedException | ExportSignal(DCPowerSignalSource, string) was called on a session to unsupported hardware. |
| System.ObjectDisposedException | ExportSignal(DCPowerSignalSource, string) was called after the associated NIDCPower object was disposed. |
| Ivi.Driver.SelectorNameException | ExportSignal(DCPowerSignalSource, string) was called with invalid channel. |
| Ivi.Driver.IviCDriverException | The value of signalSource is invalid. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-getinstrumenthandle.html language=enus -->
## TOPIC 00412: GetInstrumentHandle()

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-getinstrumenthandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-getinstrumenthandle.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the System.Runtime.InteropServices.SafeHandle to the NIDCPower instrument session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic SafeHandle GetInstrumentHandle()RemarksUsing the System.Runtime.InteropServices.SafeHandle, you can get the System.IntPtr to the session; ho

### GetInstrumentHandle()

Gets the System.Runtime.InteropServices.SafeHandle to the [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) instrument session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public SafeHandle GetInstrumentHandle()

#### Remarks

Using the System.Runtime.InteropServices.SafeHandle, you can get the System.IntPtr to the session; however, there are risks involved with using the System.IntPtr. It is difficult to know the state of the handle, and the handle could be recycled while you are using it. For more information, refer to System.Runtime.InteropServices.SafeHandle.DangerousGetHandle.

#### Returns

The System.Runtime.InteropServices.SafeHandle to the [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) instrument session.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | GetInstrumentHandle was called after the associated NIDCPower object was disposed. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-getservice__type.html language=enus -->
## TOPIC 00413: GetService(Type)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-getservice__type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-getservice__type.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the service object of the specified type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic object GetService(Type serviceType)ParametersNameTypeDescriptionserviceTypeTypeAn object that specifies the System.Type of service object to get. ReturnsA service object of type ser

### GetService(Type)

Gets the service object of the specified type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public object GetService(Type serviceType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| serviceType | Type | An object that specifies the System.Type of service object to get. |

#### Returns

A service object of type *serviceType*  or null if there is no service object of type *serviceType* .

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-instruments.html language=enus -->
## TOPIC 00414: Instruments

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-instruments.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-instruments.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerInstrumentCollection sub-object that represents a NI-DCPower channel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerInstrumentCollection Instruments { get; }RemarksReturns an object of type DCPowerInstrumentCollection.

### Instruments

Gets the [DCPowerInstrumentCollection](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection.html) sub-object that represents a NI-DCPower channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerInstrumentCollection](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection.html) Instruments { get; }

#### Remarks

Returns an object of type [DCPowerInstrumentCollection](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentcollection.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-isdisposed.html language=enus -->
## TOPIC 00415: IsDisposed

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-isdisposed.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the session has been disposed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool IsDisposed { get; }Remarkstrue if the session is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the session has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool IsDisposed { get; }

#### Remarks

true if the session is disposed; otherwise, false.

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-measurement.html language=enus -->
## TOPIC 00416: Measurement

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-measurement.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerMeasurement sub-object that represents properties related to all measurement unit channels in session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerMeasurement Measurement { get; }RemarksReturns an object of type DCPowerMeasurement.

### Measurement

Gets the [DCPowerMeasurement](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement.html) sub-object that represents properties related to all measurement unit channels in session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerMeasurement](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement.html) Measurement { get; }

#### Remarks

Returns an object of type [DCPowerMeasurement](nationalinstruments-modularinstruments-nidcpower-dcpowermeasurement.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__intptr.html language=enus -->
## TOPIC 00417: NIDCPower(IntPtr)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__intptr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__intptr.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instrument driver session from an existing instrument handle. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NIDCPower(IntPtr instrumentHandle)ParametersNameTypeDescriptioninstrumentHandleIntPtrSpecifies the pre-existing instrument handle used to create a new i

### NIDCPower(IntPtr)

Creates a new instrument driver session from an existing instrument handle.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public NIDCPower(IntPtr instrumentHandle)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrumentHandle | IntPtr | Specifies the pre-existing instrument handle used to create a new instrument driver session. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-bool-string.html language=enus -->
## TOPIC 00418: NIDCPower(string, bool, bool, string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-bool-string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: [IviDCPwr] Creates a new instrument driver session and sets the initial state of session properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NIDCPower(string resourceName, bool idQuery, bool resetDevice, string optionString)RemarksThis constructor is intended for use

### NIDCPower(string, bool, bool, string)

[IviDCPwr] Creates a new instrument driver session and sets the initial state of session properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public NIDCPower(string resourceName, bool idQuery, bool resetDevice, string optionString)

#### Remarks

Note

This constructor is intended for use only through the IVI.NET interface.

- If you intend to access this driver through the Ivi.DCPwr.IviDCPwr class interfaces, call one of the Ivi.DCPwr.IviDCPwr.Create method to construct the [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) class.
- If you intend to access this driver through the [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) class, use a constructor that accepts a channelString parameter.

For more information on the format of *optionString*, refer to the *NI DC Power Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | Specifies the name of the device in which the session is opened. |
| idQuery | bool | Specifies whether you want NI-DCPower to perform an ID query. If NI-DCPower performs an ID query, then value of idQuery is true; otherwise false. |
| resetDevice | bool | Specifies whether you want to reset NI-DCPower during the initialization procedure. If the device is reset, then value of resetDevice is true ; otherwise false. |
| optionString | string | Sets the initial state of the following session properties: RangeCheck, QueryInstrumentStatus, Cache, Simulate. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-bool.html language=enus -->
## TOPIC 00419: NIDCPower(string, bool, bool)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-bool.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: [IviDCPwr] Creates a new instrument driver session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NIDCPower(string resourceName, bool idQuery, bool resetDevice)RemarksThis constructor is intended for use only through the IVI.NET interface. National Instruments recommends th

### NIDCPower(string, bool, bool)

[IviDCPwr] Creates a new instrument driver session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public NIDCPower(string resourceName, bool idQuery, bool resetDevice)

#### Remarks

Note

This constructor is intended for use only through the IVI.NET interface.

- If you intend to access this driver through the Ivi.DCPwr.IviDCPwr class interfaces, call one of the Ivi.DCPwr.IviDCPwr.Create method to construct the [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) class.
- If you intend to access this driver through the [NIDCPower](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) class, use a constructor that accepts a channelString parameter.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | Specifies the name of the device in which the session is opened. |
| idQuery | bool | Specifies whether you want NI-DCPower to perform an ID query. If NI-DCPower performs an ID query, then value of idQuery is true; otherwise false. |
| resetDevice | bool | Specifies whether you want to reset NI-DCPower device during the initialization procedure. If the device is reset, then value of resetDevice is true ; otherwise false. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-string.html language=enus -->
## TOPIC 00420: NIDCPower(string, bool, string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-bool-string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new NI-DCPower session with independent channels to the specified instrument(s) and channel(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NIDCPower(string resourceName, bool resetDevice, string optionString)RemarksAfter calling this method, the specified chann

### NIDCPower(string, bool, string)

Creates a new NI-DCPower session with independent channels to the specified instrument(s) and channel(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public NIDCPower(string resourceName, bool resetDevice, string optionString)

#### Remarks

After calling this method, the specified channel or channels will be in the Uncommitted state.

With this method and channel-based methods and properties, you can use any channels in the session independently. For example, you can initiate a subset of channels in the ssion with the [Initiate](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcontrol-initiate.html) method, and the other channels in the session remain in the Uncommitted state.

When you initialize with independent channels, each channel steps through the NI-DCPower programming state model independently of all other channels, and you can specify a subset of channels for most operations.

Note

You can make concurrent calls to a session from multiple threads, but the session executes the calls one at a time. If you specify multiple channels for a method or property, the session may perform the operation on multiple channels in parallel, though this is not guaranteed, and some operations may execute sequentially.

The syntax for optionString is a list of properties with an assigned value where 1 is TRUE and 0 is False. For example:

Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector>

To simulate a multi-instrument session, set Simulate to 1 and list multiple instruments for DriverSetup. For example:

Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>; BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>; BoardType:<bus connector>

You do not have to specify a value for all the properties. If you do not specify a value for a property, the default value is used.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | Specifies the NI-DCPower resources to use in the session. NI-DCPower resources can be names of the instrument(s) assigned by Measurement and Automation Explorer (MAX) and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not specify channels, all channels of the instrument(s) are included in the session. |
| resetDevice | bool | Specifies whether you want to reset the channels during the initialization procedure. The default is false.To place channel(s) in a known startup state when creating a new session, set resetDevice to true. This action is equivalent to using the Reset method immediately after initializing the session.To open a session and leave the channel(s) in an existing configuration without passing through a transitional output state, set resetDevice to false. Next, configure the channel(s) as in the previous session, change the desired settings, and then call the Initiate method to write both settings. |
| optionString | string | Sets the initial state of the following session properties: RangeCheck, QueryInstrumentStatus, Cache, Simulate. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-string-bool-string.html language=enus -->
## TOPIC 00421: NIDCPower(string, string, bool, string)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-string-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-string-bool-string.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: [Deprecated] Creates a new instrument driver session and sets the initial state of session properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NIDCPower(string resourceName, string channelString, bool resetDevice, string optionString)RemarksThis constructor is depreca

### NIDCPower(string, string, bool, string)

[Deprecated] Creates a new instrument driver session and sets the initial state of session properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public NIDCPower(string resourceName, string channelString, bool resetDevice, string optionString)

#### Remarks

Note

This constructor is deprecated. Use the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor instead.

For more information on the format of *optionString*, refer to the *NI DC Power Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | Specifies the name of the device in which the session is opened. |
| channelString | string | Specifies the channels to be activated in this session. |
| resetDevice | bool | Specifies whether you want to reset NI-DCPower during the initialization procedure. If the device is reset, then value of resetDevice is true ; otherwise false |
| optionString | string | Sets the initial state of the following session properties: RangeCheck, QueryInstrumentStatus, Cache, Simulate. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-string-bool.html language=enus -->
## TOPIC 00422: NIDCPower(string, string, bool)

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-nidcpower__string-string-bool.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: [Deprecated] Creates a new instrument driver session and sets the initial state of session properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic NIDCPower(string resourceName, string channelString, bool resetDevice)RemarksThis constructor is deprecated. Use the NIDCPowe

### NIDCPower(string, string, bool)

[Deprecated] Creates a new instrument driver session and sets the initial state of session properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public NIDCPower(string resourceName, string channelString, bool resetDevice)

#### Remarks

Note

This constructor is deprecated. Use the [NIDCPower(string, bool, string)](nationalinstruments-modularinstruments-nidcpower-nidcpower.html) constructor instead.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | Specifies the name of the device in which the session is opened. |
| channelString | string | Specifies the channels to be activated in this session. |
| resetDevice | bool | Specifies whether you want to reset NI-DCPower during the initialization procedure. If the device is reset, then value of resetDevice is true ; otherwise false. |

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-outputs.html language=enus -->
## TOPIC 00423: Outputs

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-outputs.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-outputs.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerOutputCollection sub-object that represents a NI-DCPower channel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerOutputCollection Outputs { get; }RemarksReturns an object of type DCPowerOutputCollection.

### Outputs

Gets the [DCPowerOutputCollection](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcollection.html) sub-object that represents a NI-DCPower channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerOutputCollection](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcollection.html) Outputs { get; }

#### Remarks

Returns an object of type [DCPowerOutputCollection](nationalinstruments-modularinstruments-nidcpower-dcpoweroutputcollection.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-source.html language=enus -->
## TOPIC 00424: Source

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-source.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerSource sub-object that represents properties related to all source unit channels in session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerSource Source { get; }RemarksReturns an object of type DCPowerSource.

### Source

Gets the [DCPowerSource](nationalinstruments-modularinstruments-nidcpower-dcpowersource.html) sub-object that represents properties related to all source unit channels in session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerSource](nationalinstruments-modularinstruments-nidcpower-dcpowersource.html) Source { get; }

#### Remarks

Returns an object of type [DCPowerSource](nationalinstruments-modularinstruments-nidcpower-dcpowersource.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower-triggers.html language=enus -->
## TOPIC 00425: Triggers

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower-triggers.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DCPowerTriggers sub-object that is used to configure NI-DCPower triggers. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerTriggers Triggers { get; }RemarksReturns an object of type DCPowerTriggers.

### Triggers

Gets the [DCPowerTriggers](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers.html) sub-object that is used to configure NI-DCPower triggers.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerTriggers](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers.html) Triggers { get; }

#### Remarks

Returns an object of type [DCPowerTriggers](nationalinstruments-modularinstruments-nidcpower-dcpowertriggers.html).

Parent topic:

NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nidcpower.html language=enus -->
## TOPIC 00426: NIDCPower Class

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nidcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nidcpower.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class that is used to identify and control the instrument session. Derives fromIIviDCPwrIIviDriverIServiceProviderIDisposableSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic class NIDCPower : IIviDCPwr, IIviDriver, IServiceProvider, IDisposableRemarksAll propert

### NIDCPower Class

Defines a root class that is used to identify and control the instrument session.

#### Derives from

- IIviDCPwr
- IIviDriver
- IServiceProvider
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public class NIDCPower : IIviDCPwr, IIviDriver, IServiceProvider, IDisposable

#### Remarks

All properties, methods, and events fall under either the NIDCPower class or are the sub-objects of this class. To interact with the NI-DCPower, you must create an instance of this class.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| NIDCPower(string, bool, bool) | [IviDCPwr] Creates a new instrument driver session. |
| NIDCPower(string, bool, bool, string) | [IviDCPwr] Creates a new instrument driver session and sets the initial state of session properties. |
| NIDCPower(string, string, bool) | [Deprecated] Creates a new instrument driver session and sets the initial state of session properties. |
| NIDCPower(IntPtr) | Creates a new instrument driver session from an existing instrument handle. |
| NIDCPower(string, bool, string) | Creates a new NI-DCPower session with independent channels to the specified instrument(s) and channel(s). |
| NIDCPower(string, string, bool, string) | [Deprecated] Creates a new instrument driver session and sets the initial state of session properties. |

#### Properties

| Name | Description |
| --- | --- |
| Advanced | Gets the DCPowerAdvanced sub-object that provides advanced properties of NI-DCPower. |
| Calibration | Gets the DCPowerCalibration sub-object that allows calibration of NI-DCPower. |
| Control | Gets the DCPowerControl sub-object that provides methods to control the programming state of NI-DCPower. |
| Events | Gets the DCPowerEvents sub-object to configure NI-DCPower events. |
| Instruments | Gets the DCPowerInstrumentCollection sub-object that represents a NI-DCPower channel. |
| IsDisposed | Gets a value that indicates whether the session has been disposed. |
| Measurement | Gets the DCPowerMeasurement sub-object that represents properties related to all measurement unit channels in session. |
| Outputs | Gets the DCPowerOutputCollection sub-object that represents a NI-DCPower channel. |
| Source | Gets the DCPowerSource sub-object that represents properties related to all source unit channels in session. |
| Triggers | Gets the DCPowerTriggers sub-object that is used to configure NI-DCPower triggers. |

#### Methods

| Name | Description |
| --- | --- |
| Close() | Closes the session to the instrument and deallocates the resources that NI-DCPower reserved. |
| Dispose() | Closes the specified session and deallocates the reserved resources, if not already disposed. |
| ExportSignal(string, DCPowerSignalSource, string) | Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed. |
| ExportSignal(DCPowerSignalSource, string) | Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed. |
| GetInstrumentHandle() | Gets the System.Runtime.InteropServices.SafeHandle to the NIDCPower instrument session. |
| GetService(Type) | Gets the service object of the specified type. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-accurrent.html language=enus -->
## TOPIC 00427: ACCurrent

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-accurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-accurrent.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measured AC current, in amps RMS. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic ComplexDouble ACCurrent { get; }RemarksAC current level in amps RMS

### ACCurrent

Measured AC current, in amps RMS.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public ComplexDouble ACCurrent { get; }

#### Remarks

AC current level in amps RMS

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-acincompliance.html language=enus -->
## TOPIC 00428: acInCompliance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-acincompliance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-acincompliance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the output was in AC compliance at the time the measurement was taken. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool acInCompliance { get; }RemarksWhether the AC measurement is in compliance

### acInCompliance

Indicates whether the output was in AC compliance at the time the measurement was taken.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool acInCompliance { get; }

#### Remarks

Whether the AC measurement is in compliance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-acvoltage.html language=enus -->
## TOPIC 00429: ACVoltage

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-acvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-acvoltage.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measured AC voltage, in volts RMS. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic ComplexDouble ACVoltage { get; }RemarksAC voltage level in volts RMS

### ACVoltage

Measured AC voltage, in volts RMS.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public ComplexDouble ACVoltage { get; }

#### Remarks

AC voltage level in volts RMS

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-cp.html language=enus -->
## TOPIC 00430: Cp

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-cp.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-cp.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Capacitance, in farads, as measured using a parallel circuit model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Cp { get; }RemarksParallel capacitance

### Cp

Capacitance, in farads, as measured using a parallel circuit model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Cp { get; }

#### Remarks

Parallel capacitance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-cs.html language=enus -->
## TOPIC 00431: Cs

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-cs.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-cs.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Capacitance, in farads, as measured using a series circuit model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Cs { get; }RemarksSeries capacitance

### Cs

Capacitance, in farads, as measured using a series circuit model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Cs { get; }

#### Remarks

Series capacitance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-d.html language=enus -->
## TOPIC 00432: D

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-d.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Dissipation factor of the circuit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double D { get; }RemarksThe dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor.Dissipation

### D

Dissipation factor of the circuit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double D { get; }

#### Remarks

The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor.

Dissipation factor

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-dcincompliance.html language=enus -->
## TOPIC 00433: dcInCompliance

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-dcincompliance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-dcincompliance.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the output was in DC compliance at the time the measurement was taken. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool dcInCompliance { get; }RemarksWhether the DC measurement is in compliance

### dcInCompliance

Indicates whether the output was in DC compliance at the time the measurement was taken.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool dcInCompliance { get; }

#### Remarks

Whether the DC measurement is in compliance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-idc.html language=enus -->
## TOPIC 00434: Idc

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-idc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-idc.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measured DC current, in amps. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Idc { get; }RemarksDC current level in amps

### Idc

Measured DC current, in amps.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Idc { get; }

#### Remarks

DC current level in amps

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-lp.html language=enus -->
## TOPIC 00435: Lp

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-lp.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-lp.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inductance, in henrys, as measured using a parallel circuit model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Lp { get; }RemarksParallel inductance

### Lp

Inductance, in henrys, as measured using a parallel circuit model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Lp { get; }

#### Remarks

Parallel inductance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-ls.html language=enus -->
## TOPIC 00436: Ls

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-ls.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-ls.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inductance, in henrys, as measured using a series circuit model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Ls { get; }RemarksSeries inductance

### Ls

Inductance, in henrys, as measured using a series circuit model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Ls { get; }

#### Remarks

Series inductance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-measurementmode.html language=enus -->
## TOPIC 00437: measurementMode

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-measurementmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-measurementmode.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The measurement mode for the measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic DCPowerInstrumentMode measurementMode { get; }RemarksMeasurement mode

### measurementMode

The measurement mode for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public [DCPowerInstrumentMode](nationalinstruments-modularinstruments-nidcpower-dcpowerinstrumentmode.html) measurementMode { get; }

#### Remarks

Measurement mode

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-q.html language=enus -->
## TOPIC 00438: Q

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-q.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-q.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Quality factor of the circuit. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Q { get; }RemarksThe dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.Quality factor

### Q

Quality factor of the circuit.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Q { get; }

#### Remarks

The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.

Quality factor

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-rp.html language=enus -->
## TOPIC 00439: Rp

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-rp.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-rp.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resistance, in ohms, as measured using a parallel circuit model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Rp { get; }RemarksParallel resistance

### Rp

Resistance, in ohms, as measured using a parallel circuit model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Rp { get; }

#### Remarks

Parallel resistance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-rs.html language=enus -->
## TOPIC 00440: Rs

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-rs.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-rs.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resistance, in ohms, as measured using a series circuit model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Rs { get; }RemarksSeries resistance

### Rs

Resistance, in ohms, as measured using a series circuit model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Rs { get; }

#### Remarks

Series resistance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-stimulusfrequency.html language=enus -->
## TOPIC 00441: stimulusFrequency

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-stimulusfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-stimulusfrequency.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frequency of the LCR test signal, in Hz. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double stimulusFrequency { get; }RemarksAC stimulus frequency level in Hz

### stimulusFrequency

Frequency of the LCR test signal, in Hz.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double stimulusFrequency { get; }

#### Remarks

AC stimulus frequency level in Hz

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-unbalanced.html language=enus -->
## TOPIC 00442: unbalanced

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-unbalanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-unbalanced.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the bridge was unbalanced at the time the measurement was taken. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic bool unbalanced { get; }RemarksWhether the bridge is unbalanced during AC or DC measurement

### unbalanced

Indicates whether the bridge was unbalanced at the time the measurement was taken.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public bool unbalanced { get; }

#### Remarks

Whether the bridge is unbalanced during AC or DC measurement

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-vdc.html language=enus -->
## TOPIC 00443: Vdc

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-vdc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-vdc.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measured DC voltage, in volts. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double Vdc { get; }RemarksDC voltage level in volts

### Vdc

Measured DC voltage, in volts.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double Vdc { get; }

#### Remarks

DC voltage level in volts

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-y.html language=enus -->
## TOPIC 00444: Y

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-y.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-y.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complex admittance. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic ComplexDouble Y { get; }RemarksComplex admittance

### Y

Complex admittance.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public ComplexDouble Y { get; }

#### Remarks

Complex admittance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-ymagnitude.html language=enus -->
## TOPIC 00445: YMagnitude

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-ymagnitude.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-ymagnitude.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Magnitude of the complex admittance, in siemens. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double YMagnitude { get; }RemarksMagnitude of admittance

### YMagnitude

Magnitude of the complex admittance, in siemens.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double YMagnitude { get; }

#### Remarks

Magnitude of admittance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-yphase.html language=enus -->
## TOPIC 00446: YPhase

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-yphase.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-yphase.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Admittance phase angle, in degrees. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double YPhase { get; }RemarksPhase of admittance in degrees

### YPhase

Admittance phase angle, in degrees.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double YPhase { get; }

#### Remarks

Phase of admittance in degrees

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-z.html language=enus -->
## TOPIC 00447: Z

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-z.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-z.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complex impedance. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic ComplexDouble Z { get; }RemarksComplex impedance

### Z

Complex impedance.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public ComplexDouble Z { get; }

#### Remarks

Complex impedance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-zmagnitude.html language=enus -->
## TOPIC 00448: ZMagnitude

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-zmagnitude.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-zmagnitude.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Magnitude of the complex impedance, in ohms. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double ZMagnitude { get; }RemarksMagnitude of complex impedance

### ZMagnitude

Magnitude of the complex impedance, in ohms.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double ZMagnitude { get; }

#### Remarks

Magnitude of complex impedance

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-zphase.html language=enus -->
## TOPIC 00449: ZPhase

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-zphase.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement-zphase.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Impedance phase angle, in degrees. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic double ZPhase { get; }RemarksPhase of complex impedance in degrees

### ZPhase

Impedance phase angle, in degrees.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public double ZPhase { get; }

#### Remarks

Phase of complex impedance in degrees

Parent topic:

NILCRMeasurement Data Structure

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement.html language=enus -->
## TOPIC 00450: NILCRMeasurement Data Structure

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower-nilcrmeasurement.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a LCR measurement. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDCPowerpublic struct NILCRMeasurementRemarksFor more information, refer to the NI DC Power Supplies and SMUs Help. Thread SafetyAll members of this type are safe for multithreaded operations.Proper

### NILCRMeasurement Data Structure

Specifies a LCR measurement.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDCPower](nationalinstruments-modularinstruments-nidcpower.html)

public struct NILCRMeasurement

#### Remarks

For more information, refer to the [NI DC Power Supplies and SMUs Help](/csh?pubname=ni-dcpower&topicname=user-manual-welcome.html).

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| ACCurrent | Measured AC current, in amps RMS. |
| acInCompliance | Indicates whether the output was in AC compliance at the time the measurement was taken. |
| ACVoltage | Measured AC voltage, in volts RMS. |
| Cp | Capacitance, in farads, as measured using a parallel circuit model. |
| Cs | Capacitance, in farads, as measured using a series circuit model. |
| D | Dissipation factor of the circuit. |
| dcInCompliance | Indicates whether the output was in DC compliance at the time the measurement was taken. |
| Idc | Measured DC current, in amps. |
| Lp | Inductance, in henrys, as measured using a parallel circuit model. |
| Ls | Inductance, in henrys, as measured using a series circuit model. |
| measurementMode | The measurement mode for the measurement. |
| Q | Quality factor of the circuit. |
| Rp | Resistance, in ohms, as measured using a parallel circuit model. |
| Rs | Resistance, in ohms, as measured using a series circuit model. |
| stimulusFrequency | Frequency of the LCR test signal, in Hz. |
| unbalanced | Indicates whether the bridge was unbalanced at the time the measurement was taken. |
| Vdc | Measured DC voltage, in volts. |
| Y | Complex admittance. |
| YMagnitude | Magnitude of the complex admittance, in siemens. |
| YPhase | Admittance phase angle, in degrees. |
| Z | Complex impedance. |
| ZMagnitude | Magnitude of the complex impedance, in ohms. |
| ZPhase | Impedance phase angle, in degrees. |

Parent topic:

NationalInstruments.ModularInstruments.NIDCPower

<!--NI_TOPIC bundle=ni-dcpower-csharp-api-ref path=nationalinstruments-modularinstruments-nidcpower.html language=enus -->
## TOPIC 00451: NationalInstruments.ModularInstruments.NIDCPower

- bundle_id: `ni-dcpower-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidcpower.html
- document_id: `ni-dcpower-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionDCPowerAdvancedProvides advanced properties related to NI-DCPower. DCPowerCalibrationProvides objects of specific types to calibrate NI-DCPower. DCPowerCalibrationUtilityRepresents NI-DCPower calibration utility. DCPowerCoercionEventArgsRepresents the event data obtained when a

### NationalInstruments.ModularInstruments.NIDCPower

#### Classes

| Name | Description |
| --- | --- |
| DCPowerAdvanced | Provides advanced properties related to NI-DCPower. |
| DCPowerCalibration | Provides objects of specific types to calibrate NI-DCPower. |
| DCPowerCalibrationUtility | Represents NI-DCPower calibration utility. |
| DCPowerCoercionEventArgs | Represents the event data obtained when a coercion event occurs. |
| DCPowerControl | Provides methods to control the programming state of NI-DCPower. |
| DCPowerDigitalEdgeMeasureTrigger | Provides methods and properties to configure the Digital Edge Measure trigger. |
| DCPowerDigitalEdgeMeasureTriggerInputTerminal | Represents the input terminal for DCPowerDigitalEdgeMeasureTrigger. |
| DCPowerDigitalEdgePulseTrigger | Represents the methods and properties used to configure digital edge for the PulseTrigger. |
| DCPowerDigitalEdgePulseTriggerInputTerminal | Represents the input terminal for DCPowerDigitalEdgePulseTrigger. |
| DCPowerDigitalEdgeSequenceAdvanceTrigger | Represents the methods and properties used to configure digital edge for the SequenceAdvanceTrigger. |
| DCPowerDigitalEdgeSequenceAdvanceTriggerInputTerminal | Represents the input terminal for DCPowerDigitalEdgeSequenceAdvanceTrigger. |
| DCPowerDigitalEdgeShutdownTriggerInputTerminal | Represents the input terminal for DCPowerOutputDigitalEdgeShutdownTrigger. |
| DCPowerDigitalEdgeSourceTrigger | Represents the properties used to configure DCPowerDigitalEdgeSourceTrigger. |
| DCPowerDigitalEdgeSourceTriggerInputTerminal | Represents the input terminal for DCPowerDigitalEdgeSourceTrigger. |
| DCPowerDigitalEdgeStartTrigger | Represents the properties used to configure DCPowerDigitalEdgeStartTrigger. |
| DCPowerDigitalEdgeStartTriggerInputTerminal | Represents the input terminal for DCPowerDigitalEdgeStartTrigger. |
| DCPowerDriverIdentity | Provides the methods and properties that provide information about the instrument and the NI-DCPower driver. |
| DCPowerDriverLock | Provides synchronization locks obtained on the driver session. |
| DCPowerDriverOperation | Provides properties that affect the operation of the instrument driver. |
| DCPowerDriverUtility | Contains methods that provide a basic set of utility operations. |
| DCPowerEvents | Provides underlying hardware events of specific types. |
| DCPowerExternalCalibration | Provides the properties used in external calibration of NI-DCPower. |
| DCPowerInstrument | Provides properties and methods used to perform NI-DCPower instrument specific operations. |
| DCPowerInstrumentAdvanced | Provides advanced properties for the instrument. |
| DCPowerInstrumentCalibration | Provides objects of specific types to configure calibration of the instrument. |
| DCPowerInstrumentCollection | Represents a strongly typed collection of DCPowerInstrument objects. |
| DCPowerInstrumentIdentity | Provides the methods and properties that provide information about the instrument. |
| DCPowerInstrumentSelfCalibration | Defines properties used to configure self calibration of the instrument. |
| DCPowerInterchangeCheckWarningEventArgs | Provides NI-DCPower interchange check warning event arguments. |
| DCPowerMeasureCompleteEvent | Represents the properties used to configure the underlying hardware MeasureCompleteEvent. |
| DCPowerMeasureCompleteEventOutputTerminal | Represents the output terminal for DCPowerMeasureCompleteEvent. |
| DCPowerMeasureCompleteEventPulse | Represents the properties used to configure the pulse of DCPowerMeasureCompleteEvent. |
| DCPowerMeasureCompleteEventToggle | Represents the properties used to configure the toggle for measure complete event. |
| DCPowerMeasureTrigger | Represents the properties used to configure the Measure trigger for NI-DCPower. |
| DCPowerMeasureTriggerExportedOutputTerminal | Represents the output terminal for exporting the DCPowerMeasureTrigger. |
| DCPowerMeasurement | Represents properties related to all measurement channels in session. |
| DCPowerMeasurementConfiguration | Represents properties that apply to all measurement channels that are in Session. |
| DCPowerMeasurementEventArgs | Holds the event data obtained after asynchronous measurement completion. |
| DCPowerOutput | Provides properties and methods used to perform NI-DCPower channel specific operations. |
| DCPowerOutputCollection | Represents a strongly typed collection of DCPowerOutput objects. |
| DCPowerOutputControl | Provides methods to control the programming state of NI-DCPower. |
| DCPowerOutputDeviceSpecific | Provides device-specific properties related to NI-DCPower. |
| DCPowerOutputDeviceSpecificLCR | Provides LCR meter specific properties related to NI-DCPower. |
| DCPowerOutputDigitalEdgeMeasureTrigger | Represents the methods and properties used to configure the digital edge for the MeasureTrigger for the specified channel(s). |
| DCPowerOutputDigitalEdgePulseTrigger | Represents the methods and properties used to configure the digital edge for the PulseTrigger for the specified channel(s). |
| DCPowerOutputDigitalEdgeSequenceAdvanceTrigger | Represents the methods and properties used to configure the digital edge for the SequenceAdvanceTrigger for the specified channel(s). |
| DCPowerOutputDigitalEdgeShutdownTrigger | Represents the methods and properties used to configure digital edge for the ShutdownTrigger. |
| DCPowerOutputDigitalEdgeSourceTrigger | Represents the methods and properties used to configure the digital edge for the SourceTrigger for the specified channel(s). |
| DCPowerOutputDigitalEdgeStartTrigger | Represents the methods and properties used to configure the digital edge for the StartTrigger for the specified channel(s). |
| DCPowerOutputEvents | Provides underlying hardware events of specific types. |
| DCPowerOutputLCR | Contains properties related to NI-DCPower channel specific operations. |
| DCPowerOutputLCRAdvanced | Properties for controlling advanced features of LCR Output. |
| DCPowerOutputLCRCompensation | Contains properties related to NI-DCPower LCR compensation-specific operations. |
| DCPowerOutputMeasureCompleteEvent | Represents the properties used to configure the underlying hardware MeasureCompleteEvent. |
| DCPowerOutputMeasureCompleteEventPulse | Represents the properties used to configure the pulse of DCPowerOutputMeasureCompleteEvent. |
| DCPowerOutputMeasureCompleteEventToggle | Represents the properties used to configure the toggle for output measure complete event. |
| DCPowerOutputMeasureTrigger | Represents the methods and properties used to configure the MeasureTrigger for NI-DCPower. |
| DCPowerOutputMeasurement | Provides properties and methods used to perform operations related to NI-DCPower output measurements. |
| DCPowerOutputPulseCompleteEvent | Represents the properties used to configure the underlying hardware PulseCompleteEvent. |
| DCPowerOutputPulseCompleteEventPulse | Contains properties used to configure the pulse characteristics of the Pulse Complete event. |
| DCPowerOutputPulseTrigger | Represents the methods and properties used to configure the PulseTrigger for NI-DCPower. |
| DCPowerOutputReadyForPulseTriggerEvent | Contains properties used to configure the Ready For Pulse Trigger event. |
| DCPowerOutputReadyForPulseTriggerEventPulse | Represents the properties used to configure the pulse of ReadyForPulseTriggerEvent. |
| DCPowerOutputSequenceAdvanceTrigger | Represents the methods and properties used to configure the SequenceAdvanceTrigger for NI-DCPower. |
| DCPowerOutputSequenceEngineDoneEvent | Represents the properties used to configure the underlying hardware SequenceEngineDoneEvent. |
| DCPowerOutputSequenceEngineDoneEventPulse | Represents the properties used to configure the pulse of DCPowerOutputSequenceEngineDoneEvent. |
| DCPowerOutputSequenceEngineDoneEventToggle | Represents the properties used to configure the toggle for output sequence engine done event. |
| DCPowerOutputSequenceIterationCompleteEvent | Represents the properties used to configure the underlying hardware DCPowerOutputSequenceIterationCompleteEvent event. |
| DCPowerOutputSequenceIterationCompleteEventPulse | Represents the properties used to configure the pulse of SequenceIterationCompleteEvent. |
| DCPowerOutputSequenceIterationCompleteEventToggle | Represents the properties used to configure the toggle for output sequence iteration complete event. |
| DCPowerOutputShutdownTrigger | Represents the methods and properties used to configure the ShutdownTrigger for NI-DCPower. |
| DCPowerOutputSource | Represents the source unit channel. |
| DCPowerOutputSourceAdvanced | Properties for controlling the advanced features of the source unit. |
| DCPowerOutputSourceAdvancedSequencing | Provides methods and properties for configuring the source and measure unit with a series of property values. |
| DCPowerOutputSourceCompleteEvent | Represents the properties used to configure the underlying hardware SourceCompleteEvent. |
| DCPowerOutputSourceCompleteEventPulse | Represents the properties used to configure the pulse of SourceCompleteEvent. |
| DCPowerOutputSourceCompleteEventToggle | Represents the properties used to configure the toggle for output source complete event. |
| DCPowerOutputSourceConstantPower | Contains properties that change channel settings when the channel is configured for ConstantPower. |
| DCPowerOutputSourceConstantResistance | Contains properties that change channel settings when the channel is configured for ConstantResistance. |
| DCPowerOutputSourceCurrent | Contains properties used to configure the current of source unit channel. |
| DCPowerOutputSourceCustomTransientResponse | Contains properties used to configure the custom transient response of source unit channel. |
| DCPowerOutputSourceCustomTransientResponseConstantPower | Contains properties used to configure the constant power custom transient response of source unit channel. |
| DCPowerOutputSourceCustomTransientResponseConstantResistance | Contains properties used to configure the constant resistance custom transient response of source unit channel. |
| DCPowerOutputSourceCustomTransientResponseCurrent | Contains properties used to configure the custom transient response current of source unit channel. |
| DCPowerOutputSourceCustomTransientResponseVoltage | Contains properties used to configure the custom transient response voltage of source unit channel. |
| DCPowerOutputSourceOutput | Contains properties related to NI-DCPower channel specific operations. |
| DCPowerOutputSourceOutputCutoff | Properties for controlling output cutoff limits for supported instruments. |
| DCPowerOutputSourcePulseCurrent | Contains properties that change channel settings when the channel is configured for PulseCurrent. |
| DCPowerOutputSourcePulseVoltage | Contains properties used to configure the pulse voltage of source unit channel. |
| DCPowerOutputSourceTrigger | Represents the methods and properties used to configure the SourceTrigger for NI-DCPower. |
| DCPowerOutputSourceVoltage | Contains properties used to configure the voltage of source unit channel. |
| DCPowerOutputStartTrigger | Represents the methods and properties used to configure the StartTrigger for NI-DCPower. |
| DCPowerOutputTriggers | Provides underlying triggers of specific types. |
| DCPowerPulseCompleteEvent | Represents the properties used to configure the underlying hardware PulseCompleteEvent. |
| DCPowerPulseCompleteEventOutputTerminal | Represents the output terminal for DCPowerPulseCompleteEvent. |
| DCPowerPulseCompleteEventPulse | Contains properties used to configure the pulse characteristics of the Pulse Complete event. |
| DCPowerPulseTrigger | Defines methods and properties used to configure the Pulse trigger. |
| DCPowerPulseTriggerExportedOutputTerminal | Represents the output terminal for DCPowerSequenceAdvanceTrigger. |
| DCPowerReadyForPulseTriggerEvent | Contains properties used to configure the Ready For Pulse Trigger event. |
| DCPowerReadyForPulseTriggerEventOutputTerminal | Represents the output terminal for DCPowerReadyForPulseTriggerEvent. |
| DCPowerReadyForPulseTriggerEventPulse | Represents the properties used to configure the pulse of ReadyForPulseTriggerEvent. |
| DCPowerSelfCalibration | Defines methods and properties used to perform self calibration and query data related to self calibration. |
| DCPowerSequenceAdvanceTrigger | Represents the properties used to configure the SequenceAdvanceTrigger trigger for NI-DCPower. |
| DCPowerSequenceAdvanceTriggerExportedOutputTerminal | Represents the output terminal for DCPowerSequenceAdvanceTrigger. |
| DCPowerSequenceEngineDoneEvent | Represents the properties used to configure the underlying hardware SequenceEngineDoneEvent. |
| DCPowerSequenceEngineDoneEventOutputTerminal | Represents the destination terminal for DCPowerSequenceEngineDoneEvent. |
| DCPowerSequenceEngineDoneEventPulse | Represents the properties used to configure the pulse of DCPowerSequenceEngineDoneEvent. |
| DCPowerSequenceEngineDoneEventToggle | Represents the properties used to configure the toggle for sequence engine done event. |
| DCPowerSequenceIterationCompleteEvent | Represents the properties used to configure the underlying hardware DCPowerSequenceIterationCompleteEvent event. |
| DCPowerSequenceIterationCompleteEventOutputTerminal | Represents the destination terminal for DCPowerSequenceIterationCompleteEvent. |
| DCPowerSequenceIterationCompleteEventPulse | Represents the properties used to configure the pulse of SequenceIterationCompleteEvent. |
| DCPowerSequenceIterationCompleteEventToggle | Represents the properties used to configure the toggle for sequence iteration complete event. |
| DCPowerSource | Contains properties used to configure NI-DCPower for signal generation. |
| DCPowerSourceCompleteEvent | Represents the properties used to configure the underlying hardware SourceCompleteEvent. |
| DCPowerSourceCompleteEventOutputTerminal | Represents the destination terminal for DCPowerSourceCompleteEvent. |
| DCPowerSourceCompleteEventPulse | Represents the properties used to configure the pulse of SourceCompleteEvent. |
| DCPowerSourceCompleteEventToggle | Represents the properties used to configure the toggle for source complete event. |
| DCPowerSourceTrigger | Represents the properties used to configure the SourceTrigger for NI-DCPower. |
| DCPowerSourceTriggerExportedOutputTerminal | Represents the output terminal for DCPowerSourceTrigger. |
| DCPowerStartTrigger | Represents the properties used to configure the StartTrigger for NI-DCPower. |
| DCPowerStartTriggerExportedOutputTerminal | Represents the output terminal for DCPowerStartTrigger. |
| DCPowerSubObject | Represents members that are common to all sub-object NI-DCPower classes. This is an internal class and is not intended for external use. |
| DCPowerTriggers | Provides underlying triggers of specific types. |
| DCPowerWarning | Provides warning codes for the warnings raised by the underlying driver. |
| DCPowerWarningEventArgs | Represents the properties under the Warning Event Args raised during a driver warning. |
| NIDCPower | Defines a root class that is used to identify and control the instrument session. |

#### Interfaces

None

#### Structures

| Name | Description |
| --- | --- |
| DCPowerFetchResult | Represents the result of Fetch method. |
| DCPowerLCRLoadCompensationSpot | Specifies a load measurement for performing compensation. |
| DCPowerMeasureResult | Represents the result of Measure method. |
| DCPowerSelfTestResult | Represents the result of the SelfTest method. |
| NILCRMeasurement | Specifies a LCR measurement. |

#### Enumerations

| Name | Description |
| --- | --- |
| DCPowerAdvancedSequenceProperty | Specifies the properties that you can reconfigure per step in the advanced sequence. |
| DCPowerCableLength | Specifies values for the CableLength property. |
| DCPowerComplianceLimitSymmetry | Specifies whether compliance limits for current generation and voltage generation for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A. |
| DCPowerConductionVoltageMode | Specifies values for the ConductionVoltageMode property. |
| DCPowerEventOutputBehavior | Specifies values for the event output behavior property. |
| DCPowerEventToggleInitialState | Specifies values for the event toggle initial state property. |
| DCPowerInstrumentMode | Specifies values for the InstrumentMode property. |
| DCPowerIsolationState | Specifies values for the IsolationState property. |
| DCPowerLCRAutomaticLevelControl | Specifies values for the AutomaticLevelControl and DCBiasAutomaticLevelControl properties. |
| DCPowerLCRCompensationType | Specifies the type of compensation for LCR measurements. |
| DCPowerLCRDCBiasSource | Specifies values for the DCBiasSource property. |
| DCPowerLCRDCBiasTransientResponse | Specifies values for the DCBiasTransientResponse property. |
| DCPowerLCRImpedanceAutorange | Specifies values for the ImpedanceAutoRange property. |
| DCPowerLCRImpedanceRangeSource | Specifies the values for the ImpedanceRangeSource property. |
| DCPowerLCRMeasurementTime | Specifies values for the MeasurementTime property. |
| DCPowerLCROpenShortLoadCompensationDataSource | Specifies values for the OpenShortLoadCompensationDataSource property. |
| DCPowerLCRReferenceValueType | Specifies values for the DCPowerLCRLoadCompensationSpot property. |
| DCPowerLCRSourceDelayMode | Specifies values for the SourceDelayMode property. |
| DCPowerLCRStimulusFunction | Specifies values for the StimulusFunction property. |
| DCPowerMeasureApertureTimeUnits | Specifies values for ApertureTimeUnits property. |
| DCPowerMeasureTriggerType | Specifies the values of Type for data operations. |
| DCPowerMeasurementAutoZero | Specifies values for AutoZero property. |
| DCPowerMeasurementAutorange | Specifies values for the Autorange property. |
| DCPowerMeasurementAutorangeApertureTimeMode | Specifies values for the AutorangeApertureTimeMode property. |
| DCPowerMeasurementAutorangeBehavior | Specifies values for the AutorangeBehavior property. |
| DCPowerMeasurementAutorangeThresholdMode | Specifies values for the AutorangeThresholdMode property. |
| DCPowerMeasurementNoiseRejection | Specifies the type of NoiseRejection. |
| DCPowerMeasurementOutputState | Specifies return values for QueryState. |
| DCPowerMeasurementSense | Specifies values for the Sense property. |
| DCPowerMeasurementWhen | Specifies the values for the MeasureWhen property. |
| DCPowerOutputCutoffReason | The output cutoff conditions to query or clear. |
| DCPowerPowerAllocationMode | Determines whether the device sources the power its output configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device. |
| DCPowerPowerSource | Specifies values for the PowerSource property. |
| DCPowerPowerSourceInUse | Specifies the type of PowerSourceInUse. |
| DCPowerPulsePolarity | Specifies values for NI-DCPower pulse polarity. |
| DCPowerPulseTriggerType | Specifies values for the Type property. |
| DCPowerSelfCalibrationPersistence | Specifies values for SelfCalibrationPersistence property. |
| DCPowerSequenceAdvanceTriggerType | Specifies values for the Type property. |
| DCPowerShutdownTriggerType | Specifies values for the Type property. |
| DCPowerSignalSource | The trigger or event signal to route. |
| DCPowerSourceCurrentLevelAutorange | Specifies values for the CurrentLevelAutorange property. |
| DCPowerSourceCurrentLimitAutorange | Specifies values for the CurrentLimitAutorange property. |
| DCPowerSourceMode | Specifies values for the Mode property. |
| DCPowerSourceOutputCapacitance | Specifies values for the OutputCapacitance property. |
| DCPowerSourceOutputFunction | Specifies values for the Function property. |
| DCPowerSourceTransientResponse | Specifies values for the TransientResponse property. |
| DCPowerSourceTriggerType | Specifies values for the Type property. |
| DCPowerSourceVoltageLevelAutorange | Specifies values for the VoltageLevelAutorange property. |
| DCPowerSourceVoltageLimitAutorange | Specifies values for the VoltageLimitAutorange property. |
| DCPowerStartTriggerType | Specifies values for the Type property. |
| DCPowerTriggerEdge | Specifies the transitions of the signal from one discrete level to another. |

#### Delegates

None
