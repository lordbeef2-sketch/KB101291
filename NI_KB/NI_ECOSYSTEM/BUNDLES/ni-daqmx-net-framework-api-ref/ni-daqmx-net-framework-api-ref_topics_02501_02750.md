# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=2501 end=2750 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-polynomialscale.html language=enus -->
## TOPIC 02501: PolynomialScale Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-polynomialscale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-polynomialscale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a custom scale that scales values by using an n^th-order polynomial equation. Derives fromScaleSyntaxNamespace: NationalInstruments.DAQmxpublic class PolynomialScale : ScaleRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\DotNET4.x d

### PolynomialScale Class

Encapsulates a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) that scales values by using an *n*<sup>th</sup>-order polynomial equation.

#### Derives from

- Scale

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class PolynomialScale : Scale

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| PolynomialScale(string, PolynomialDirection, double[], double, double, int, int) | Creates a new instance of the PolynomialScale class with the specified forward or reverse coefficients and automatically computes the other set of coefficients. |
| PolynomialScale(string, PolynomialDirection, double[], double, double) | Creates a new instance of the PolynomialScale class with the specified forward or reverse coefficients and automatically computes the other set of coefficients with the same order as the provided coefficients, using 1000 points in the specified range. |
| PolynomialScale(string, double[], double[]) | Creates a new instance of the PolynomialScale class with the specified forward and reverse coefficients. |

#### Properties

| Name | Description |
| --- | --- |
| ForwardCoefficients | Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. |
| ReverseCoefficients | Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y^3. |

#### See Also

- LoadScale(string)

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-powercalibrationtype.html language=enus -->
## TOPIC 02502: PowerCalibrationType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-powercalibrationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-powercalibrationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the calibration type. SyntaxNamespace: NationalInstruments.DAQmxpublic enum PowerCalibrationTypeMembersNameValueDescriptionRemoteVoltage15100Calibrate remote voltage for the power module. LocalVoltage15101Calibrate local voltage for the power module. Current15102Calibrate current for the p

### PowerCalibrationType Enumeration

Specifies the calibration type.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum PowerCalibrationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RemoteVoltage | 15100 | Calibrate remote voltage for the power module. |
| LocalVoltage | 15101 | Calibrate local voltage for the power module. |
| Current | 15102 | Calibrate current for the power module. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-poweridleoutputbehavior.html language=enus -->
## TOPIC 02503: PowerIdleOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-poweridleoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-poweridleoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to disable the output or maintain the existing value after the task is uncommitted. SyntaxNamespace: NationalInstruments.DAQmxpublic enum PowerIdleOutputBehaviorRemarksSpecifies whether to disable the output or maintain the existing value after the task is uncommitted. Use this enu

### PowerIdleOutputBehavior Enumeration

Specifies whether to disable the output or maintain the existing value after the task is uncommitted.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum PowerIdleOutputBehavior

#### Remarks

Specifies whether to disable the output or maintain the existing value after the task is uncommitted. Use this enumeration to get or set the value of [PowerIdleOutputBehavior](nationalinstruments-daqmx-aichannel-poweridleoutputbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OutputDisabled | 15503 | Disable power output. |
| MaintainExistingValue | 12528 | Continue generating the current power. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-poweroutputstate.html language=enus -->
## TOPIC 02504: PowerOutputState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-poweroutputstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-poweroutputstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates power channel operating state. Can be read at any time during a task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum PowerOutputStateRemarksIndicates power channel operating state. Can be read at any time during a task. Use this enumeration to get or set the value of PowerOutputStat

### PowerOutputState Enumeration

Indicates power channel operating state. Can be read at any time during a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum PowerOutputState

#### Remarks

Indicates power channel operating state. Can be read at any time during a task. Use this enumeration to get or set the value of [PowerOutputState](nationalinstruments-daqmx-aichannel-poweroutputstate.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ConstantVoltage | 15500 | Power output is maintaining a constant voltage by adjusting the current. |
| ConstantCurrent | 15501 | Power output is maintaining a constant current by adjusting the voltage. |
| Overvoltage | 15502 | Voltage output has exceeded its limit. |
| OutputDisabled | 15503 | Power output is disabled. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-productcategory.html language=enus -->
## TOPIC 02505: ProductCategory Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-productcategory.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-productcategory.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ProductCategoryRemarksIndicates the product category of the device. This category corresponds to th

### ProductCategory Enumeration

Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ProductCategory

#### Remarks

Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices. Use this enumeration to get or set the value of [ProductCategory](nationalinstruments-daqmx-device-productcategory.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MSeriesDaq | 14643 | M Series DAQ. |
| XSeriesDaq | 15858 | X Series DAQ. |
| ESeriesDaq | 14642 | E Series DAQ. |
| SSeriesDaq | 14644 | S Series DAQ. |
| BSeriesDaq | 14662 | B Series DAQ. |
| SCSeriesDaq | 14645 | SC Series DAQ. |
| UsbDaq | 14646 | USB DAQ. |
| AOSeries | 14647 | AO Series. |
| DigitalIO | 14648 | Digital I/O. |
| TioSeries | 14661 | TIO Series. |
| DynamicSignalAcquisition | 14649 | Dynamic Signal Acquisition. |
| Switches | 14650 | Switches. |
| CompactDaqChassis | 14658 | CompactDAQ chassis. |
| CompactRioChassis | 16144 | CompactRIO Chassis. |
| CSeriesModule | 14659 | C Series I/O module. |
| ScxiModule | 14660 | SCXI module. |
| SccConnectorBlock | 14704 | SCC Connector Block. |
| SccModule | 14705 | SCC Module. |
| NIElvis | 14755 | NI ELVIS. |
| NetworkDAQ | 14829 | Network DAQ. |
| SCExpress | 15886 | SC Express. |
| FieldDaq | 16151 | FieldDAQ. |
| TestScaleChassis | 16180 | TestScale chassis. |
| TestScaleModule | 16181 | TestScale I/O module. |
| mioDAQ | 16182 | mioDAQ. |
| Unknown | 12588 | Unknown category. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-propertyfilterflags.html language=enus -->
## TOPIC 02506: PropertyFilterFlags Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-propertyfilterflags.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-propertyfilterflags.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a set of property filtering options. SyntaxNamespace: NationalInstruments.DAQmxpublic enum PropertyFilterFlagsMembersNameValueDescriptionNone0x0No additional filtering options. Volatile0x1The property filtering only returns properties that can be modified by the DAQmx driver while the task

### PropertyFilterFlags Enumeration

Specifies a set of property filtering options.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum PropertyFilterFlags

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0x0 | No additional filtering options. |
| Volatile | 0x1 | The property filtering only returns properties that can be modified by the DAQmx driver while the task is running. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-propertyfiltertype.html language=enus -->
## TOPIC 02507: PropertyFilterType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-propertyfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-propertyfiltertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of property filtering to perform. SyntaxNamespace: NationalInstruments.DAQmxpublic enum PropertyFilterTypeMembersNameValueDescriptionAll0Returns all of the properties that belong to the Task subobject. ConfiguredDevices1Returns only the properties that apply to the configured devi

### PropertyFilterType Enumeration

Specifies the type of property filtering to perform.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum PropertyFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| All | 0 | Returns all of the properties that belong to the Task subobject. |
| ConfiguredDevices | 1 | Returns only the properties that apply to the configured devices on the system and belong to the Task subobject. |
| DevicesInTask | 2 | Returns only the properties that apply to the devices being used in the task and belong to the Task subobject. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-rangemapscale-prescaledmax.html language=enus -->
## TOPIC 02508: PreScaledMax

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-rangemapscale-prescaledmax.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-rangemapscale-prescaledmax.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to ScaledMax. SyntaxNamespace: NationalInstruments.DAQmxpublic double PreScaledMax { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PreScaledMax

Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to [ScaledMax](nationalinstruments-daqmx-rangemapscale-scaledmax.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PreScaledMax { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

RangeMapScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-rangemapscale-prescaledmin.html language=enus -->
## TOPIC 02509: PreScaledMin

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-rangemapscale-prescaledmin.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-rangemapscale-prescaledmin.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to ScaledMin. SyntaxNamespace: NationalInstruments.DAQmxpublic double PreScaledMin { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PreScaledMin

Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to [ScaledMin](nationalinstruments-daqmx-rangemapscale-scaledmin.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PreScaledMin { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

RangeMapScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-rangemapscale-rangemapscale__string-double-double-double-double.html language=enus -->
## TOPIC 02510: RangeMapScale(string, double, double, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-rangemapscale-rangemapscale__string-double-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-rangemapscale-rangemapscale__string-double-double-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the RangeMapScale class with the prescaled minimum and maximum values and the scaled minimum and maximum values. SyntaxNamespace: NationalInstruments.DAQmxpublic RangeMapScale(string name, double prescaledMinimum, double prescaledMaximum, double scaledMinimum, double scaled

### RangeMapScale(string, double, double, double, double)

Creates a new instance of the [RangeMapScale](nationalinstruments-daqmx-rangemapscale.html) class with the prescaled minimum and maximum values and the scaled minimum and maximum values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public RangeMapScale(string name, double prescaledMinimum, double prescaledMaximum, double scaledMinimum, double scaledMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the custom scale for later use, such as when you create a virtual channel. |
| prescaledMinimum | double | The smallest value in the range of prescaled values. |
| prescaledMaximum | double | The largest value in the range of prescaled values. |
| scaledMinimum | double | The smallest value in the range of scaled values. |
| scaledMaximum | double | The largest value in the range of scaled values. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

RangeMapScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-rangemapscale-scaledmax.html language=enus -->
## TOPIC 02511: ScaledMax

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-rangemapscale-scaledmax.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-rangemapscale-scaledmax.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to PreScaledMax. Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double S

### ScaledMax

Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to [PreScaledMax](nationalinstruments-daqmx-rangemapscale-prescaledmax.html). Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ScaledMax { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

RangeMapScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-rangemapscale-scaledmin.html language=enus -->
## TOPIC 02512: ScaledMin

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-rangemapscale-scaledmin.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-rangemapscale-scaledmin.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to PreScaledMin. Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value. SyntaxNamespace: NationalInstruments.DAQmxpublic doubl

### ScaledMin

Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to [PreScaledMin](nationalinstruments-daqmx-rangemapscale-prescaledmin.html). Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ScaledMin { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

RangeMapScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-rangemapscale.html language=enus -->
## TOPIC 02513: RangeMapScale Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-rangemapscale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-rangemapscale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a custom scale that scales values proportionally from a range of prescaled values to a range of scaled values. Derives fromScaleSyntaxNamespace: NationalInstruments.DAQmxpublic class RangeMapScale : ScaleRemarksExample applications are located in the <Public Documents>\National Instrume

### RangeMapScale Class

Encapsulates a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) that scales values proportionally from a range of prescaled values to a range of scaled values.

#### Derives from

- Scale

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class RangeMapScale : Scale

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| RangeMapScale(string, double, double, double, double) | Creates a new instance of the RangeMapScale class with the prescaled minimum and maximum values and the scaled minimum and maximum values. |

#### Properties

| Name | Description |
| --- | --- |
| PreScaledMax | Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to ScaledMax. |
| PreScaledMin | Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to ScaledMin. |
| ScaledMax | Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to PreScaledMax. Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value. |
| ScaledMin | Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to PreScaledMin. Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value. |

#### See Also

- LoadScale(string)

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-readoverwritemode.html language=enus -->
## TOPIC 02514: ReadOverwriteMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-readoverwritemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-readoverwritemode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to overwrite samples in the buffer that you have not yet read. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReadOverwriteModeRemarksSpecifies whether to overwrite samples in the buffer that you have not yet read. Use this enumeration to get or set the value of ReadOverwrit

### ReadOverwriteMode Enumeration

Specifies whether to overwrite samples in the buffer that you have not yet read.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReadOverwriteMode

#### Remarks

Specifies whether to overwrite samples in the buffer that you have not yet read. Use this enumeration to get or set the value of [ReadOverwriteMode](nationalinstruments-daqmx-daqstream-readoverwritemode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OverwriteUnreadSamples | 10252 | When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting ReadRelativeTo to MostRecentSample and setting ReadOffset to the appropriate number of samples. |
| DoNotOverwriteUnreadSamples | 10159 | The acquisition stops when it encounters a sample in the buffer that you have not read. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-readrelativeto.html language=enus -->
## TOPIC 02515: ReadRelativeTo Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-readrelativeto.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-readrelativeto.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with ReadOffset, the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a Reference Trigger for the

### ReadRelativeTo Enumeration

Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with [ReadOffset](nationalinstruments-daqmx-daqstream-readoffset.html), the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) for the task. If you configure a Reference Trigger, the default value is FirstPretriggerSample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReadRelativeTo

#### Remarks

Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with [ReadOffset](nationalinstruments-daqmx-daqstream-readoffset.html), the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) for the task. If you configure a Reference Trigger, the default value is FirstPretriggerSample. Use this enumeration to get or set the value of [ReadRelativeTo](nationalinstruments-daqmx-daqstream-readrelativeto.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FirstSample | 10424 | Start reading samples relative to the first sample acquired. |
| CurrentReadPosition | 10425 | Start reading samples relative to the last sample returned by the previous read. For the first read operation, this position is the first sample acquired or the first pretrigger sample if you configured a reference trigger for the task. |
| ReferenceTrigger | 10426 | Start reading samples relative to the first sample after the reference trigger occurred. |
| FirstPretriggerSample | 10427 | Start reading samples relative to the first pretrigger sample. You specify the number of pretrigger samples to acquire when you configure a reference trigger. |
| MostRecentSample | 10428 | Start reading samples relative to the next sample acquired. For example, use this value and set ReadOffset to -1 to read the last sample acquired. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-readwaitmode.html language=enus -->
## TOPIC 02516: ReadWaitMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-readwaitmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-readwaitmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how reading from the task waits for samples to become available. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReadWaitModeRemarksSpecifies how reading from the task waits for samples to become available. Use this enumeration to get or set the value of ReadWaitMode.MembersNameValue

### ReadWaitMode Enumeration

Specifies how reading from the task waits for samples to become available.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReadWaitMode

#### Remarks

Specifies how reading from the task waits for samples to become available. Use this enumeration to get or set the value of [ReadWaitMode](nationalinstruments-daqmx-daqstream-readwaitmode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| WaitForInterrupt | 12523 | Check for available samples when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates. |
| Poll | 12524 | Repeatedly check for available samples as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |
| Yield | 12525 | Repeatedly check for available samples, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency. |
| Sleep | 12547 | Check for available samples once per the amount of time specified in ReadSleepTime. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-readyforstarteventlevelactivelevel.html language=enus -->
## TOPIC 02517: ReadyForStartEventLevelActiveLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-readyforstarteventlevelactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-readyforstarteventlevelactivelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Ready for Start Event. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReadyForStartEventLevelActiveLevelRemarksSpecifies the polarity of the exported Ready for Start Event. Use this enumeration to get or set the value of ReadyForStartEventLevelActiveLeve

### ReadyForStartEventLevelActiveLevel Enumeration

Specifies the polarity of the exported Ready for Start Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReadyForStartEventLevelActiveLevel

#### Remarks

Specifies the polarity of the exported Ready for Start Event. Use this enumeration to get or set the value of [ReadyForStartEventLevelActiveLevel](nationalinstruments-daqmx-exportsignals-readyforstarteventlevelactivelevel.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-readyfortransfereventdeassertcondition.html language=enus -->
## TOPIC 02518: ReadyForTransferEventDeassertCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-readyfortransfereventdeassertcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-readyfortransfereventdeassertcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when the ready for transfer event deasserts. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReadyForTransferEventDeassertConditionRemarksSpecifies when the ready for transfer event deasserts. Use this enumeration to get or set the value of ReadyForTransferEventDeassertCondition.Memb

### ReadyForTransferEventDeassertCondition Enumeration

Specifies when the ready for transfer event deasserts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReadyForTransferEventDeassertCondition

#### Remarks

Specifies when the ready for transfer event deasserts. Use this enumeration to get or set the value of [ReadyForTransferEventDeassertCondition](nationalinstruments-daqmx-exportsignals-readyfortransfereventdeassertcondition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnboardMemoryMoreThanHalfFull | 10237 | Deassert the signal when more than half of the onboard memory of the device fills. |
| OnboardMemoryFull | 10236 | Deassert the signal when the onboard memory fills. |
| OnboardMemoryCustomThreshold | 12577 | Deassert the signal when the amount of space available in the onboard memory is below the value specified with ReadyForTransferEventDeassertConditionCustomThreshold. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-readyfortransfereventlevelactivelevel.html language=enus -->
## TOPIC 02519: ReadyForTransferEventLevelActiveLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-readyfortransfereventlevelactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-readyfortransfereventlevelactivelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active level of the exported Ready for Transfer Event. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReadyForTransferEventLevelActiveLevelRemarksSpecifies the active level of the exported Ready for Transfer Event. Use this enumeration to get or set the value of ReadyForTransfer

### ReadyForTransferEventLevelActiveLevel Enumeration

Specifies the active level of the exported Ready for Transfer Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReadyForTransferEventLevelActiveLevel

#### Remarks

Specifies the active level of the exported Ready for Transfer Event. Use this enumeration to get or set the value of [ReadyForTransferEventLevelActiveLevel](nationalinstruments-daqmx-exportsignals-readyfortransfereventlevelactivelevel.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-reallocationpolicy.html language=enus -->
## TOPIC 02520: ReallocationPolicy Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of a memory-optimized read method operation when the operation yields more samples than the current capacity of the buffer can allocate. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReallocationPolicyMembersNameValueDescriptionDoNotReallocate0The read operation is lim

### ReallocationPolicy Enumeration

Specifies the behavior of a memory-optimized read method operation when the operation yields more samples than the current capacity of the buffer can allocate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReallocationPolicy

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DoNotReallocate | 0 | The read operation is limited to read up to the capacity of the provided buffer. |
| ToGrow | 1 | The read operation can request more memory if the operation yields more samples than the capacity of the provided buffer. You must use initialized data; otherwise, your application could throw a DaqException. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-analogedge.html language=enus -->
## TOPIC 02521: AnalogEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-analogedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-analogedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AnalogEdgeReferenceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogEdgeReferenceTrigger AnalogEdge { get; }RemarksThe AnalogEdgeReferenceTrigger.

### AnalogEdge

Gets the [AnalogEdgeReferenceTrigger](nationalinstruments-daqmx-analogedgereferencetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogEdgeReferenceTrigger](nationalinstruments-daqmx-analogedgereferencetrigger.html) AnalogEdge { get; }

#### Remarks

The [AnalogEdgeReferenceTrigger](nationalinstruments-daqmx-analogedgereferencetrigger.html).

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-analogmultiedge.html language=enus -->
## TOPIC 02522: AnalogMultiEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-analogmultiedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-analogmultiedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AnalogMultiEdgeReferenceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogMultiEdgeReferenceTrigger AnalogMultiEdge { get; }RemarksThe AnalogMultiEdgeReferenceTrigger.

### AnalogMultiEdge

Gets the [AnalogMultiEdgeReferenceTrigger](nationalinstruments-daqmx-analogmultiedgereferencetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogMultiEdgeReferenceTrigger](nationalinstruments-daqmx-analogmultiedgereferencetrigger.html) AnalogMultiEdge { get; }

#### Remarks

The [AnalogMultiEdgeReferenceTrigger](nationalinstruments-daqmx-analogmultiedgereferencetrigger.html).

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-analogwindow.html language=enus -->
## TOPIC 02523: AnalogWindow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-analogwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-analogwindow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AnalogWindowReferenceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowReferenceTrigger AnalogWindow { get; }RemarksThe AnalogWindowReferenceTrigger.

### AnalogWindow

Gets the [AnalogWindowReferenceTrigger](nationalinstruments-daqmx-analogwindowreferencetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowReferenceTrigger](nationalinstruments-daqmx-analogwindowreferencetrigger.html) AnalogWindow { get; }

#### Remarks

The [AnalogWindowReferenceTrigger](nationalinstruments-daqmx-analogwindowreferencetrigger.html).

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-autotriggered.html language=enus -->
## TOPIC 02524: AutoTriggered

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-autotriggered.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-autotriggered.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns false. This property is only applicable when AutoTriggerEnable is true. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AutoTriggered {

### AutoTriggered

Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns false. This property is only applicable when [AutoTriggerEnable](nationalinstruments-daqmx-referencetrigger-autotriggerenable.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AutoTriggered { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-autotriggerenable.html language=enus -->
## TOPIC 02525: AutoTriggerEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-autotriggerenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-autotriggerenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AutoTriggerEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx drive

### AutoTriggerEnable

Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AutoTriggerEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-configureanalogedgetrigger__string-analogedgereferencetriggerslope-double-long.html language=enus -->
## TOPIC 02526: ConfigureAnalogEdgeTrigger(string, AnalogEdgeReferenceTriggerSlope, double, long)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-configureanalogedgetrigger__string-analogedgereferencetriggerslope-double-long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-configureanalogedgetrigger__string-analogedgereferencetriggerslope-double-long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal reaches the level you specify; and the device acquires all post-trigger samples. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureAnalogEdgeTrigger(string source, AnalogEdgeRef

### ConfigureAnalogEdgeTrigger(string, AnalogEdgeReferenceTriggerSlope, double, long)

Configures the task to stop the acquisition when the device acquires all pretrigger samples; an [analog signal reaches the level you specify](/csh?context=nidaqmx_mxcncpts_analogtriggering); and the device acquires all post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureAnalogEdgeTrigger(string source, AnalogEdgeReferenceTriggerSlope slope, double level, long pretriggerSamples)

#### Remarks

The number of post-trigger samples is equal to the value of [SamplesPerChannel](nationalinstruments-daqmx-timing-samplesperchannel.html) minus the value of *pretriggerSamples* . If *pretriggerSamples*  equals [SamplesPerChannel](nationalinstruments-daqmx-timing-samplesperchannel.html), the measurement or generation stops when the reference trigger occurs.

When you use a [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger), the default value of the [ReadRelativeTo](nationalinstruments-daqmx-daqstream-readrelativeto.html) property is [FirstPretriggerSample](nationalinstruments-daqmx-readrelativeto.html) with a [ReadOffset](nationalinstruments-daqmx-daqstream-readoffset.html) value of 0.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureAnalogEdgeTrigger(string, AnalogEdgeReferenceTriggerSlope, double, long) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. For E Series devices, if you use a virtual channel, it must be the only channel in the task. The only terminal you can use for E Series devices is PFI0. |
| slope | AnalogEdgeReferenceTriggerSlope | The slope of the signal on which the reference trigger occurs. |
| level | double | The threshold, in the units of the measurement or generation, to trigger. Use slope to specify on which slope to trigger at this threshold. |
| pretriggerSamples | long | The minimum number of samples per channel to acquire before recognizing the reference trigger. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-configureanalogmultiedgetrigger__string-analogmultiedgereferencetriggerslope_arr1-double_arr1-long.html language=enus -->
## TOPIC 02527: ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeReferenceTriggerSlope[], double[], long)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-configureanalogmultiedgetrigger__string-analogmultiedgereferencetriggerslope_arr1-double_arr1-long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-configureanalogmultiedgetrigger__string-analogmultiedgereferencetriggerslope_arr1-double_arr1-long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to stop the acquisition when the device acquires all pretrigger samples, any of the configured analog signals reaches the levels you specify, and the device acquires all post-trigger samples. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureAnalogMultiEdgeTrigger(st

### ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeReferenceTriggerSlope[], double[], long)

Configures the task to stop the acquisition when the device acquires all pretrigger samples, any of the configured analog signals reaches the levels you specify, and the device acquires all post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureAnalogMultiEdgeTrigger(string sources, AnalogMultiEdgeReferenceTriggerSlope[] slopes, double[] levels, long pretriggerSamples)

#### Remarks

When you use a [ReferenceTrigger](nationalinstruments-daqmx-referencetrigger.html), the default for [ReadRelativeTo](nationalinstruments-daqmx-daqstream-readrelativeto.html) is [FirstPretriggerSample](nationalinstruments-daqmx-readrelativeto.html) with a [ReadOffset](nationalinstruments-daqmx-daqstream-readoffset.html) of 0. Multi-edge triggering treats the specified triggers as if they are logically **OR**ed.

The number of trigger sources represented by *sources*  and the number of elements in *slopes*  and *levels*  must all be the same.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sources | string | A string specifying a list of terminals, physical channel names, or ranges of physical channels where there are analog signals to use as the sources of the trigger. |
| slopes | AnalogMultiEdgeReferenceTriggerSlope[] | An array containing the slopes of the signals to start acquiring or generating samples when the respective signal crosses the respective trigger level. Each element corresponds to the sources specified in sources and elements in the other array parameters. |
| levels | double[] | An array containing the thresholds at which to start acquiring or generating samples. Each element corresponds to the sources specified in sources and elements in the other array parameters. Specify these values in the units of the measurement or generation. Use slopes to specify on which slopes to trigger at the respective thresholds. |
| pretriggerSamples | long | The minimum number of samples per channel to acquire before recognizing the reference trigger. The number of posttrigger samples per channel is equal to SamplesPerChannel minus pretriggerSamples . |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-configureanalogwindowtrigger__string-analogwindowreferencetriggercondition-double-double-long.html language=enus -->
## TOPIC 02528: ConfigureAnalogWindowTrigger(string, AnalogWindowReferenceTriggerCondition, double, double, long)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-configureanalogwindowtrigger__string-analogwindowreferencetriggercondition-double-double-long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-configureanalogwindowtrigger__string-analogwindowreferencetriggercondition-double-double-long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal enters or leaves a range you specify; and the device acquires all post-trigger samples. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureAnalogWindowTrigger(string source, Anal

### ConfigureAnalogWindowTrigger(string, AnalogWindowReferenceTriggerCondition, double, double, long)

Configures the task to stop the acquisition when the device acquires all pretrigger samples; an [analog signal enters or leaves a range you specify](/csh?context=nidaqmx_mxcncpts_algwindowtrig); and the device acquires all post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureAnalogWindowTrigger(string source, AnalogWindowReferenceTriggerCondition condition, double top, double bottom, long pretriggerSamples)

#### Remarks

The number of post-trigger samples is equal to the value of [SamplesPerChannel](nationalinstruments-daqmx-timing-samplesperchannel.html) minus the value of *pretriggerSamples* . If *pretriggerSamples*  equals [SamplesPerChannel](nationalinstruments-daqmx-timing-samplesperchannel.html), the measurement or generation stops when the reference trigger occurs.

When you use a [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger), the default value of the [ReadRelativeTo](nationalinstruments-daqmx-daqstream-readrelativeto.html) property is [FirstPretriggerSample](nationalinstruments-daqmx-readrelativeto.html) with a [ReadOffset](nationalinstruments-daqmx-daqstream-readoffset.html) value of 0.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureAnalogWindowTrigger(string, AnalogWindowReferenceTriggerCondition, double, double, long) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger. For E Series devices, if you use a virtual channel, it must be the only channel in the task. The only terminal you can use for E Series devices is PFI0. |
| condition | AnalogWindowReferenceTriggerCondition | Specifies if the reference trigger occurs when the signal enters the window or leaves the window. Use bottom and top to specify the limits of the window. |
| top | double | The upper limit of the voltage window, in the units of the measurement or generation. |
| bottom | double | The lower limit of the voltage window, in the units of the measurement or generation. |
| pretriggerSamples | long | The minimum number of samples per channel to acquire before recognizing the reference trigger. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-configuredigitaledgetrigger__string-digitaledgereferencetriggeredge-long.html language=enus -->
## TOPIC 02529: ConfigureDigitalEdgeTrigger(string, DigitalEdgeReferenceTriggerEdge, long)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-configuredigitaledgetrigger__string-digitaledgereferencetriggeredge-long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-configuredigitaledgetrigger__string-digitaledgereferencetriggeredge-long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to stop the acquisition when the device acquires all pretrigger samples, detects a rising or falling edge of a digital signal, and acquires all post-trigger samples. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeRefere

### ConfigureDigitalEdgeTrigger(string, DigitalEdgeReferenceTriggerEdge, long)

Configures the task to stop the acquisition when the device acquires all pretrigger samples, [detects a rising or falling edge of a digital signal](/csh?context=nidaqmx_mxcncpts_digtrigger), and acquires all post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeReferenceTriggerEdge edge, long pretriggerSamples)

#### Remarks

The number of post-trigger samples is equal to the value of [SamplesPerChannel](nationalinstruments-daqmx-timing-samplesperchannel.html) minus the value of *pretriggerSamples* . If *pretriggerSamples*  equals [SamplesPerChannel](nationalinstruments-daqmx-timing-samplesperchannel.html), the measurement or generation stops when the reference trigger occurs.

When you use a [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger), the default value of the [ReadRelativeTo](nationalinstruments-daqmx-daqstream-readrelativeto.html) property is [FirstPretriggerSample](nationalinstruments-daqmx-readrelativeto.html) with a [ReadOffset](nationalinstruments-daqmx-daqstream-readoffset.html) value of 0.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalEdgeTrigger(string, DigitalEdgeReferenceTriggerEdge, long) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of the terminal where there is a digital signal to use as the source of the trigger. |
| edge | DigitalEdgeReferenceTriggerEdge | The edge of the digital signal on which the reference trigger occurs. |
| pretriggerSamples | long | The minimum number of samples to acquire per channel before recognizing the reference trigger. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-configuredigitalpatterntrigger__string-string-digitalpatternreferencetriggercondition-long.html language=enus -->
## TOPIC 02530: ConfigureDigitalPatternTrigger(string, string, DigitalPatternReferenceTriggerCondition, long)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-configuredigitalpatterntrigger__string-string-digitalpatternreferencetriggercondition-long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-configuredigitalpatterntrigger__string-string-digitalpatternreferencetriggercondition-long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a task to stop the acquisition when the device acquires all pretrigger samples, matches a digital pattern, and acquires all posttrigger samples. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureDigitalPatternTrigger(string source, string pattern, DigitalPatternReferenceTrigg

### ConfigureDigitalPatternTrigger(string, string, DigitalPatternReferenceTriggerCondition, long)

Configures a task to stop the acquisition when the device acquires all pretrigger samples, matches a [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern), and acquires all posttrigger samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureDigitalPatternTrigger(string source, string pattern, DigitalPatternReferenceTriggerCondition condition, long pretriggerSamples)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalPatternTrigger(string, string, DigitalPatternReferenceTriggerCondition, long) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. |
| pattern | string | The digital pattern that must be met for the trigger to occur. |
| condition | DigitalPatternReferenceTriggerCondition | The condition under which the trigger occurs. |
| pretriggerSamples | long | The minimum number of samples to acquire per channel before recognizing the reference trigger. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-configurenone.html language=enus -->
## TOPIC 02531: ConfigureNone()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-configurenone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-configurenone.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables reference triggering for the measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureNone()RemarksThe NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does not throw an exception for parameter values that

### ConfigureNone()

Disables [reference triggering](/csh?context=nidaqmx_mxcncpts_referencetrigger) for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureNone()

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-delay.html language=enus -->
## TOPIC 02532: Delay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-delay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double Delay { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver

### Delay

Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Delay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-digitaledge.html language=enus -->
## TOPIC 02533: DigitalEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-digitaledge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalEdgeReferenceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeReferenceTrigger DigitalEdge { get; }RemarksThe DigitalEdgeReferenceTrigger.

### DigitalEdge

Gets the [DigitalEdgeReferenceTrigger](nationalinstruments-daqmx-digitaledgereferencetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeReferenceTrigger](nationalinstruments-daqmx-digitaledgereferencetrigger.html) DigitalEdge { get; }

#### Remarks

The [DigitalEdgeReferenceTrigger](nationalinstruments-daqmx-digitaledgereferencetrigger.html).

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-digitalpattern.html language=enus -->
## TOPIC 02534: DigitalPattern

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-digitalpattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-digitalpattern.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalPatternReferenceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalPatternReferenceTrigger DigitalPattern { get; }RemarksThe DigitalPatternReferenceTrigger.

### DigitalPattern

Gets the [DigitalPatternReferenceTrigger](nationalinstruments-daqmx-digitalpatternreferencetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalPatternReferenceTrigger](nationalinstruments-daqmx-digitalpatternreferencetrigger.html) DigitalPattern { get; }

#### Remarks

The [DigitalPatternReferenceTrigger](nationalinstruments-daqmx-digitalpatternreferencetrigger.html).

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-maximumnumberoftriggerstodetect.html language=enus -->
## TOPIC 02535: MaximumNumberOfTriggersToDetect

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-maximumnumberoftriggerstodetect.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-maximumnumberoftriggerstodetect.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum

### MaximumNumberOfTriggersToDetect

Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of [Triggers](nationalinstruments-daqmx-triggers.html) to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long MaximumNumberOfTriggersToDetect { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-pretriggersamples.html language=enus -->
## TOPIC 02536: PretriggerSamples

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-pretriggersamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-pretriggersamples.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger. Post-trigger samples per channel are equal to SamplesPerChannel minus the number of pretrigger samples per channel. SyntaxNamespace: NationalInstruments.DAQmxpublic long Pretrigg

### PretriggerSamples

Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the [reference trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger). Post-trigger samples per channel are equal to [SamplesPerChannel](nationalinstruments-daqmx-timing-samplesperchannel.html) minus the number of pretrigger samples per channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long PretriggerSamples { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-retriggerable.html language=enus -->
## TOPIC 02537: Retriggerable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-retriggerable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-retriggerable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until

### Retriggerable

Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring signals.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Retriggerable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-retriggerwindow.html language=enus -->
## TOPIC 02538: RetriggerWindow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-retriggerwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-retriggerwindow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 caus

### RetriggerWindow

Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 causes the window to be infinite.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RetriggerWindow { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-terminal.html language=enus -->
## TOPIC 02539: Terminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-terminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic string Terminal { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driv

### Terminal

Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Terminal { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-timestamp.html language=enus -->
## TOPIC 02540: Timestamp

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-timestamp.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference trigger timestamp. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime Timestamp { get; }RemarksThe reference trigger timestamp.The timestamp returned is expressed as a UTC time. For more information on timestamps in NI-DAQmx, see Timestamps.ExceptionsTypeDescriptio

### Timestamp

Gets the reference trigger timestamp.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime Timestamp { get; }

#### Remarks

The reference trigger timestamp.

Note

The timestamp returned is expressed as a UTC time.

Timestamps

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-timestampenable.html language=enus -->
## TOPIC 02541: TimestampEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-timestampenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-timestampenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. SyntaxNamespace: NationalInstruments.DAQmxpublic bool TimestampEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqEx

### TimestampEnable

Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool TimestampEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-timestamptimescale.html language=enus -->
## TOPIC 02542: TimestampTimescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-timestamptimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-timestamptimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference trigger timestamp timescale. SyntaxNamespace: NationalInstruments.DAQmxpublic ReferenceTriggerTimestampTimescale TimestampTimescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TimestampTimescale

Specifies the reference trigger timestamp timescale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReferenceTriggerTimestampTimescale](nationalinstruments-daqmx-referencetriggertimestamptimescale.html) TimestampTimescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-tostring.html language=enus -->
## TOPIC 02543: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-triggerwindow.html language=enus -->
## TOPIC 02544: TriggerWindow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-triggerwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-triggerwindow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during th

### TriggerWindow

Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double TriggerWindow { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger-type.html language=enus -->
## TOPIC 02545: Type

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger-type.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to mark a reference point for the measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic ReferenceTriggerType Type { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Type

Specifies the [type](/csh?context=nidaqmx_mxcncpts_triggertypes) of trigger to use to mark a [reference](/csh?context=nidaqmx_mxcncpts_referencetrigger) point for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReferenceTriggerType](nationalinstruments-daqmx-referencetriggertype.html) Type { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetrigger.html language=enus -->
## TOPIC 02546: ReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods that configure the trigger that creates the reference point between the pretrigger samples and the post-trigger samples. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class ReferenceTrigger : MarshalByRefObject,

### ReferenceTrigger Class

Contains properties and methods that configure the trigger that creates the [reference point between the pretrigger samples and the post-trigger samples](/csh?context=nidaqmx_mxcncpts_referencetrigger).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class ReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AnalogEdge | Gets the AnalogEdgeReferenceTrigger. |
| AnalogMultiEdge | Gets the AnalogMultiEdgeReferenceTrigger. |
| AnalogWindow | Gets the AnalogWindowReferenceTrigger. |
| AutoTriggered | Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns false. This property is only applicable when AutoTriggerEnable is true. |
| AutoTriggerEnable | Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout. |
| Delay | Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples. |
| DigitalEdge | Gets the DigitalEdgeReferenceTrigger. |
| DigitalPattern | Gets the DigitalPatternReferenceTrigger. |
| MaximumNumberOfTriggersToDetect | Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger. |
| PretriggerSamples | Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger. Post-trigger samples per channel are equal to SamplesPerChannel minus the number of pretrigger samples per channel. |
| Retriggerable | Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring signals. |
| RetriggerWindow | Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 causes the window to be infinite. |
| Terminal | Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
| Timestamp | Gets the reference trigger timestamp. |
| TimestampEnable | Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
| TimestampTimescale | Specifies the reference trigger timestamp timescale. |
| TriggerWindow | Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite. |
| Type | Specifies the type of trigger to use to mark a reference point for the measurement. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAnalogEdgeTrigger(string, AnalogEdgeReferenceTriggerSlope, double, long) | Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal reaches the level you specify; and the device acquires all post-trigger samples. |
| ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeReferenceTriggerSlope[], double[], long) | Configures the task to stop the acquisition when the device acquires all pretrigger samples, any of the configured analog signals reaches the levels you specify, and the device acquires all post-trigger samples. |
| ConfigureAnalogWindowTrigger(string, AnalogWindowReferenceTriggerCondition, double, double, long) | Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal enters or leaves a range you specify; and the device acquires all post-trigger samples. |
| ConfigureDigitalEdgeTrigger(string, DigitalEdgeReferenceTriggerEdge, long) | Configures the task to stop the acquisition when the device acquires all pretrigger samples, detects a rising or falling edge of a digital signal, and acquires all post-trigger samples. |
| ConfigureDigitalPatternTrigger(string, string, DigitalPatternReferenceTriggerCondition, long) | Configures a task to stop the acquisition when the device acquires all pretrigger samples, matches a digital pattern, and acquires all posttrigger samples. |
| ConfigureNone() | Disables reference triggering for the measurement. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Triggers
- ReferenceTrigger

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetriggerpulsepolarity.html language=enus -->
## TOPIC 02547: ReferenceTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetriggerpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetriggerpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Reference Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReferenceTriggerPulsePolarityRemarksSpecifies the polarity of the exported Reference Trigger. Use this enumeration to get or set the value of ReferenceTriggerPulsePolarity.MembersNameValue

### ReferenceTriggerPulsePolarity Enumeration

Specifies the polarity of the exported Reference Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReferenceTriggerPulsePolarity

#### Remarks

Specifies the polarity of the exported Reference Trigger. Use this enumeration to get or set the value of [ReferenceTriggerPulsePolarity](nationalinstruments-daqmx-exportsignals-referencetriggerpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetriggertimestamptimescale.html language=enus -->
## TOPIC 02548: ReferenceTriggerTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetriggertimestamptimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetriggertimestamptimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference trigger timestamp timescale. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReferenceTriggerTimestampTimescaleRemarksSpecifies the reference trigger timestamp timescale. Use this enumeration to get or set the value of TimestampTimescale.MembersNameValueDescriptionHostT

### ReferenceTriggerTimestampTimescale Enumeration

Specifies the reference trigger timestamp timescale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReferenceTriggerTimestampTimescale

#### Remarks

Specifies the reference trigger timestamp timescale. Use this enumeration to get or set the value of [TimestampTimescale](nationalinstruments-daqmx-referencetrigger-timestamptimescale.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HostTime | 16126 | Use the host device. |
| IODeviceTime | 16127 | Use the I/O device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-referencetriggertype.html language=enus -->
## TOPIC 02549: ReferenceTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-referencetriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-referencetriggertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to mark a reference point for the measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ReferenceTriggerTypeRemarksSpecifies the type of trigger to use to mark a reference point for the measurement. Use this enumeration to get or set the value of Typ

### ReferenceTriggerType Enumeration

Specifies the [type](/csh?context=nidaqmx_mxcncpts_triggertypes) of trigger to use to mark a [reference](/csh?context=nidaqmx_mxcncpts_referencetrigger) point for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ReferenceTriggerType

#### Remarks

Specifies the [type](/csh?context=nidaqmx_mxcncpts_triggertypes) of trigger to use to mark a [reference](/csh?context=nidaqmx_mxcncpts_referencetrigger) point for the measurement. Use this enumeration to get or set the value of [Type](nationalinstruments-daqmx-referencetrigger-type.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AnalogEdge | 10099 | Trigger when an analog signal signal crosses a threshold. |
| AnalogMultiEdge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
| DigitalEdge | 10150 | Trigger on the rising or falling edge of a digital signal. |
| DigitalPattern | 10398 | Trigger when digital physical channels match a digital pattern. |
| AnalogWindow | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable triggering for the task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockactiveedge.html language=enus -->
## TOPIC 02550: SampleClockActiveEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleClockActiveEdgeRemarksSpecifies on which edge of a clock pulse sampling ta

### SampleClockActiveEdge Enumeration

Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleClockActiveEdge

#### Remarks

Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock. Use this enumeration to get or set the value of [SampleClockActiveEdge](nationalinstruments-daqmx-timing-sampleclockactiveedge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockeventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 02551: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockeventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockeventargs-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxprotected void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStream

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

SampleClockEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockeventargs-sampleclockeventargs.html language=enus -->
## TOPIC 02552: SampleClockEventArgs()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockeventargs-sampleclockeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockeventargs-sampleclockeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SampleClockEventArgs class. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockEventArgs()

### SampleClockEventArgs()

Initializes a new instance of the [SampleClockEventArgs](nationalinstruments-daqmx-sampleclockeventargs.html) class.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public SampleClockEventArgs()

Parent topic:

SampleClockEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockeventargs.html language=enus -->
## TOPIC 02553: SampleClockEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the SampleClock event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class SampleClockEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\DotNET4.x directory

### SampleClockEventArgs Class

Provides data for the [SampleClock](nationalinstruments-daqmx-task-sampleclock.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SampleClockEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| SampleClockEventArgs() | Initializes a new instance of the SampleClockEventArgs class. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockeventhandler__object-sampleclockeventargs.html language=enus -->
## TOPIC 02554: SampleClockEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockeventhandler__object-sampleclockeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockeventhandler__object-sampleclockeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the SampleClock event. SyntaxNamespace: NationalInstrumentspublic delegate void SampleClockEventHandler(object sender, SampleClockEventArgs e)ParametersNameTypeDescriptionsenderobjectThe Task that caused this event.eSampleClockEventArgsA SampleClockEventArgs that c

### SampleClockEventHandler Delegate

Represents the method that handles the [SampleClock](nationalinstruments-daqmx-task-sampleclock.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void SampleClockEventHandler(object sender, SampleClockEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The Task that caused this event. |
| e | SampleClockEventArgs | A SampleClockEventArgs that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockoutputbehavior.html language=enus -->
## TOPIC 02555: SampleClockOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleClockOutputBehaviorRemarksSpecifies whether the exported Sample Clock issues a pulse at the b

### SampleClockOutputBehavior Enumeration

Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleClockOutputBehavior

#### Remarks

Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample. Use this enumeration to get or set the value of [SampleClockOutputBehavior](nationalinstruments-daqmx-exportsignals-sampleclockoutputbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pulse | 10265 | The exported Sample Clock pulses at the beginning of each sample. |
| Level | 10210 | The exported Sample Clock goes high at the beginning of the sample and goes low when the last AI Convert begins. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockoverrunbehavior.html language=enus -->
## TOPIC 02556: SampleClockOverrunBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockoverrunbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockoverrunbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take if Sample Clock edges occur faster than the device can handle them. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleClockOverrunBehaviorRemarksSpecifies the action to take if Sample Clock edges occur faster than the device can handle them. Use this enumeratio

### SampleClockOverrunBehavior Enumeration

Specifies the action to take if Sample Clock edges occur faster than the device can handle them.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleClockOverrunBehavior

#### Remarks

Specifies the action to take if Sample Clock edges occur faster than the device can handle them. Use this enumeration to get or set the value of [SampleClockOverrunBehavior](nationalinstruments-daqmx-timing-sampleclockoverrunbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| StopTaskAndError | 15862 | Stop task and return an error. |
| IgnoreOverruns | 15863 | NI-DAQmx ignores Sample Clock overruns, and the task continues to run. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockpulsepolarity.html language=enus -->
## TOPIC 02557: SampleClockPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Sample Clock if SampleClockOutputBehavior is Pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleClockPulsePolarityRemarksSpecifies the polarity of the exported Sample Clock if SampleClockOutputBehavior is Pulse. Use this enumeration to get or se

### SampleClockPulsePolarity Enumeration

Specifies the polarity of the exported Sample Clock if [SampleClockOutputBehavior](nationalinstruments-daqmx-exportsignals-sampleclockoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-sampleclockoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleClockPulsePolarity

#### Remarks

Specifies the polarity of the exported Sample Clock if [SampleClockOutputBehavior](nationalinstruments-daqmx-exportsignals-sampleclockoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-sampleclockoutputbehavior.html). Use this enumeration to get or set the value of [SampleClockPulsePolarity](nationalinstruments-daqmx-exportsignals-sampleclockpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclocktimebaseactiveedge.html language=enus -->
## TOPIC 02558: SampleClockTimebaseActiveEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclocktimebaseactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclocktimebaseactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleClockTimebaseActiveEdgeRemarksSpecifies on which edge to rec

### SampleClockTimebaseActiveEdge Enumeration

Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleClockTimebaseActiveEdge

#### Remarks

Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock. Use this enumeration to get or set the value of [SampleClockTimebaseActiveEdge](nationalinstruments-daqmx-timing-sampleclocktimebaseactiveedge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclocktimingresponsemode.html language=enus -->
## TOPIC 02559: SampleClockTimingResponseMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclocktimingresponsemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclocktimingresponsemode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the device responds to the sample clock and to triggers. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleClockTimingResponseModeMembersNameValueDescriptionSingleCycle14613Device responds by the next sample clock edge. Multicycle14614Device acquires or generates samples on t

### SampleClockTimingResponseMode Enumeration

Specifies how the device responds to the sample clock and to triggers.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleClockTimingResponseMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SingleCycle | 14613 | Device responds by the next sample clock edge. |
| Multicycle | 14614 | Device acquires or generates samples on the next sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Refer to device documentation for information about which triggers the multicycle response mode affects. This response mode allows higher data transfer rates at the cost of increased latency for responding to triggers. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampleclockunderflowbehavior.html language=enus -->
## TOPIC 02560: SampleClockUnderflowBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampleclockunderflowbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampleclockunderflowbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleClockUnderflowBehaviorRemarksSpecifies the action to take when the onboard memory of the device becomes empty.

### SampleClockUnderflowBehavior Enumeration

Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleClockUnderflowBehavior

#### Remarks

Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop. Use this enumeration to get or set the value of [SampleClockUnderflowBehavior](nationalinstruments-daqmx-timing-sampleclockunderflowbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HaltOutputAndError | 14615 | Stop generating samples and return an error. |
| PauseUntilDataAvailable | 14616 | Pause the task until samples are available in the FIFO. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-samplecompleteeventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 02561: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-samplecompleteeventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-samplecompleteeventargs-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxprotected void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStream

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

SampleCompleteEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-samplecompleteeventargs-samplecompleteeventargs.html language=enus -->
## TOPIC 02562: SampleCompleteEventArgs()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-samplecompleteeventargs-samplecompleteeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-samplecompleteeventargs-samplecompleteeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SampleCompleteEventArgs class. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleCompleteEventArgs()

### SampleCompleteEventArgs()

Initializes a new instance of the [SampleCompleteEventArgs](nationalinstruments-daqmx-samplecompleteeventargs.html) class.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public SampleCompleteEventArgs()

Parent topic:

SampleCompleteEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-samplecompleteeventargs.html language=enus -->
## TOPIC 02563: SampleCompleteEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-samplecompleteeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-samplecompleteeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the SampleComplete event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class SampleCompleteEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\DotNET4.x dire

### SampleCompleteEventArgs Class

Provides data for the [SampleComplete](nationalinstruments-daqmx-task-samplecomplete.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SampleCompleteEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| SampleCompleteEventArgs() | Initializes a new instance of the SampleCompleteEventArgs class. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-samplecompleteeventhandler__object-samplecompleteeventargs.html language=enus -->
## TOPIC 02564: SampleCompleteEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-samplecompleteeventhandler__object-samplecompleteeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-samplecompleteeventhandler__object-samplecompleteeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the SampleComplete event. SyntaxNamespace: NationalInstrumentspublic delegate void SampleCompleteEventHandler(object sender, SampleCompleteEventArgs e)ParametersNameTypeDescriptionsenderobjectThe Task that caused this event.eSampleCompleteEventArgsA SampleCompleteE

### SampleCompleteEventHandler Delegate

Represents the method that handles the [SampleComplete](nationalinstruments-daqmx-task-samplecomplete.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void SampleCompleteEventHandler(object sender, SampleCompleteEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The Task that caused this event. |
| e | SampleCompleteEventArgs | A SampleCompleteEventArgs that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-samplequantitymode.html language=enus -->
## TOPIC 02565: SampleQuantityMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-samplequantitymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-samplequantitymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleQuantityModeRemarksSpecifies if a task acquires or generates a finite number of samples or if it continuously acquires

### SampleQuantityMode Enumeration

Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleQuantityMode

#### Remarks

Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples. Use this enumeration to get or set the value of [SampleQuantityMode](nationalinstruments-daqmx-timing-samplequantitymode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FiniteSamples | 10178 | Acquire or generate a finite number of samples. |
| ContinuousSamples | 10123 | Acquire or generate samples until you stop the task. |
| HardwareTimedSinglePoint | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sampletimingtype.html language=enus -->
## TOPIC 02566: SampleTimingType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sampletimingtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sampletimingtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of sample timing to use for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SampleTimingTypeRemarksSpecifies the type of sample timing to use for the task. Use this enumeration to get or set the value of SampleTimingType.MembersNameValueDescriptionSampleClock10388A

### SampleTimingType Enumeration

Specifies the [type of sample timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype) to use for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SampleTimingType

#### Remarks

Specifies the [type of sample timing](/csh?context=nidaqmx_mxcncpts_smpletimingtype) to use for the task. Use this enumeration to get or set the value of [SampleTimingType](nationalinstruments-daqmx-timing-sampletimingtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SampleClock | 10388 | Acquire or generate samples on the specified edge of the sample clock. |
| BurstHandshake | 12548 | Determine sample timing using burst handshaking between the device and a peripheral device. |
| Handshake | 10389 | Determine sample timing by using digital handshaking between the device and a peripheral device. |
| Implicit | 10451 | Configure only the duration of the task. |
| OnDemand | 10390 | Acquire or generate a sample on each read or write operation. This timing type is also referred to as static or software-timed. |
| ChangeDetection | 12504 | Acquire samples when a change occurs in the state of one or more digital input lines. The lines must be contained within a digital input channel. |
| PipelinedSampleClock | 14668 | Device acquires or generates samples on each sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Pipelining allows higher data transfer rates at the cost of increased trigger response latency. Refer to the device documentation for information about which triggers pipelining affects. This timing type allows handshaking with some devices using the Pause trigger, the Ready for Transfer event, or the Data Active event. Refer to the device documentation for more information. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo-allowinteractivedeletion.html language=enus -->
## TOPIC 02567: AllowInteractiveDeletion

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo-allowinteractivedeletion.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo-allowinteractivedeletion.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the global channel can be deleted through MAX. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AllowInteractiveDeletion { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AllowInteractiveDeletion

Indicates whether the global channel can be deleted through MAX.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AllowInteractiveDeletion { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedChannelInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo-allowinteractiveediting.html language=enus -->
## TOPIC 02568: AllowInteractiveEditing

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo-allowinteractiveediting.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo-allowinteractiveediting.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the global channel can be edited in the DAQ Assistant. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AllowInteractiveEditing { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AllowInteractiveEditing

Indicates whether the global channel can be edited in the DAQ Assistant.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AllowInteractiveEditing { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedChannelInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo-author.html language=enus -->
## TOPIC 02569: Author

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo-author.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo-author.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the author of the global channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string Author { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Author

Indicates the author of the global channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Author { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedChannelInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo-dispose.html language=enus -->
## TOPIC 02570: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by SavedChannelInfo. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Dispose()

Releases all resources used by [SavedChannelInfo](nationalinstruments-daqmx-savedchannelinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedChannelInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo-dispose__bool.html language=enus -->
## TOPIC 02571: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by SavedChannelInfo or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on i

### Dispose(bool)

Releases the managed and unmanaged resources used by [SavedChannelInfo](nationalinstruments-daqmx-savedchannelinfo.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by SavedChannelInfo; false to release only unmanaged resources used by SavedChannelInfo. |

Parent topic:

SavedChannelInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo-name.html language=enus -->
## TOPIC 02572: Name

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo-name.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string Name { get; }RemarksA String that represents the name of the channel.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Name

Gets the name of the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Name { get; }

#### Remarks

A String that represents the name of the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedChannelInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo-tostring.html language=enus -->
## TOPIC 02573: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedChannelInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedchannelinfo.html language=enus -->
## TOPIC 02574: SavedChannelInfo Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedchannelinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedchannelinfo.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates information about a global channel stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling GetSavedChannelInfo(string). Derives fromMarshalByRefObjectIDisposableSyntaxNamespace: NationalInstruments.DAQmxpublic class SavedChannelInfo : Mar

### SavedChannelInfo Class

Encapsulates information about a global channel stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling [GetSavedChannelInfo(string)](nationalinstruments-daqmx-daqsystem-getsavedchannelinfo__string.html).

#### Derives from

- MarshalByRefObject
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SavedChannelInfo : MarshalByRefObject, IDisposable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AllowInteractiveDeletion | Indicates whether the global channel can be deleted through MAX. |
| AllowInteractiveEditing | Indicates whether the global channel can be edited in the DAQ Assistant. |
| Author | Indicates the author of the global channel. |
| Name | Gets the name of the channel. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Releases all resources used by SavedChannelInfo. |
| ToString() | Returns a string representation of the object. |
| Dispose(bool) | Releases the managed and unmanaged resources used by SavedChannelInfo or optionally releases only the unmanaged resources. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo-allowinteractivedeletion.html language=enus -->
## TOPIC 02575: AllowInteractiveDeletion

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo-allowinteractivedeletion.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo-allowinteractivedeletion.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the custom scale can be deleted through MAX. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AllowInteractiveDeletion { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AllowInteractiveDeletion

Indicates whether the custom scale can be deleted through MAX.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AllowInteractiveDeletion { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedScaleInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo-allowinteractiveediting.html language=enus -->
## TOPIC 02576: AllowInteractiveEditing

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo-allowinteractiveediting.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo-allowinteractiveediting.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the custom scale can be edited in the DAQ Assistant. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AllowInteractiveEditing { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AllowInteractiveEditing

Indicates whether the custom scale can be edited in the DAQ Assistant.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AllowInteractiveEditing { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedScaleInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo-author.html language=enus -->
## TOPIC 02577: Author

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo-author.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo-author.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the author of the custom scale. SyntaxNamespace: NationalInstruments.DAQmxpublic string Author { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Author

Indicates the author of the custom scale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Author { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedScaleInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo-dispose.html language=enus -->
## TOPIC 02578: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by SavedScaleInfo. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Dispose()

Releases all resources used by [SavedScaleInfo](nationalinstruments-daqmx-savedscaleinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedScaleInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo-dispose__bool.html language=enus -->
## TOPIC 02579: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by SavedScaleInfo or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on imp

### Dispose(bool)

Releases the managed and unmanaged resources used by [SavedScaleInfo](nationalinstruments-daqmx-savedscaleinfo.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by SavedScaleInfo; false to release only unmanaged resources used by SavedScaleInfo. |

Parent topic:

SavedScaleInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo-name.html language=enus -->
## TOPIC 02580: Name

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo-name.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the scale. SyntaxNamespace: NationalInstruments.DAQmxpublic string Name { get; }RemarksA String that represents the name of the scale.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Name

Gets the name of the scale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Name { get; }

#### Remarks

A String that represents the name of the scale.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedScaleInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo-tostring.html language=enus -->
## TOPIC 02581: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedScaleInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedscaleinfo.html language=enus -->
## TOPIC 02582: SavedScaleInfo Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedscaleinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedscaleinfo.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates information about a custom scale stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling GetSavedScaleInfo(string). Derives fromMarshalByRefObjectIDisposableSyntaxNamespace: NationalInstruments.DAQmxpublic class SavedScaleInfo : MarshalBy

### SavedScaleInfo Class

Encapsulates information about a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling [GetSavedScaleInfo(string)](nationalinstruments-daqmx-daqsystem-getsavedscaleinfo__string.html).

#### Derives from

- MarshalByRefObject
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SavedScaleInfo : MarshalByRefObject, IDisposable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AllowInteractiveDeletion | Indicates whether the custom scale can be deleted through MAX. |
| AllowInteractiveEditing | Indicates whether the custom scale can be edited in the DAQ Assistant. |
| Author | Indicates the author of the custom scale. |
| Name | Gets the name of the scale. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Releases all resources used by SavedScaleInfo. |
| ToString() | Returns a string representation of the object. |
| Dispose(bool) | Releases the managed and unmanaged resources used by SavedScaleInfo or optionally releases only the unmanaged resources. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo-allowinteractivedeletion.html language=enus -->
## TOPIC 02583: AllowInteractiveDeletion

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo-allowinteractivedeletion.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo-allowinteractivedeletion.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the task can be deleted through MAX. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AllowInteractiveDeletion { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AllowInteractiveDeletion

Indicates whether the task can be deleted through MAX.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AllowInteractiveDeletion { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedTaskInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo-allowinteractiveediting.html language=enus -->
## TOPIC 02584: AllowInteractiveEditing

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo-allowinteractiveediting.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo-allowinteractiveediting.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the task can be edited in the DAQ Assistant. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AllowInteractiveEditing { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AllowInteractiveEditing

Indicates whether the task can be edited in the DAQ Assistant.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AllowInteractiveEditing { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedTaskInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo-author.html language=enus -->
## TOPIC 02585: Author

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo-author.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo-author.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the author of the task. SyntaxNamespace: NationalInstruments.DAQmxpublic string Author { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Author

Indicates the author of the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Author { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedTaskInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo-dispose.html language=enus -->
## TOPIC 02586: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by SavedTaskInfo. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Dispose()

Releases all resources used by [SavedTaskInfo](nationalinstruments-daqmx-savedtaskinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedTaskInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo-dispose__bool.html language=enus -->
## TOPIC 02587: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by SavedTaskInfo or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on impl

### Dispose(bool)

Releases the managed and unmanaged resources used by [SavedTaskInfo](nationalinstruments-daqmx-savedtaskinfo.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by SavedTaskInfo; false to release only unmanaged resources used by SavedTaskInfo. |

Parent topic:

SavedTaskInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo-name.html language=enus -->
## TOPIC 02588: Name

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo-name.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the task. SyntaxNamespace: NationalInstruments.DAQmxpublic string Name { get; }RemarksA String that represents the name of the task.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Name

Gets the name of the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Name { get; }

#### Remarks

A String that represents the name of the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedTaskInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo-tostring.html language=enus -->
## TOPIC 02589: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SavedTaskInfo Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-savedtaskinfo.html language=enus -->
## TOPIC 02590: SavedTaskInfo Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-savedtaskinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-savedtaskinfo.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates information about a task stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling GetSavedTaskInfo(string). Derives fromMarshalByRefObjectIDisposableSyntaxNamespace: NationalInstruments.DAQmxpublic class SavedTaskInfo : MarshalByRefObject,

### SavedTaskInfo Class

Encapsulates information about a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) stored in Measurement & Automation Explorer (MAX). You can retrieve an instance of this class by calling [GetSavedTaskInfo(string)](nationalinstruments-daqmx-daqsystem-getsavedtaskinfo__string.html).

#### Derives from

- MarshalByRefObject
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SavedTaskInfo : MarshalByRefObject, IDisposable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AllowInteractiveDeletion | Indicates whether the task can be deleted through MAX. |
| AllowInteractiveEditing | Indicates whether the task can be edited in the DAQ Assistant. |
| Author | Indicates the author of the task. |
| Name | Gets the name of the task. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Releases all resources used by SavedTaskInfo. |
| ToString() | Returns a string representation of the object. |
| Dispose(bool) | Releases the managed and unmanaged resources used by SavedTaskInfo or optionally releases only the unmanaged resources. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-saveoptions.html language=enus -->
## TOPIC 02591: SaveOptions Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-saveoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-saveoptions.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies various options used to save a task, a local or global channel , or a custom scale to Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic enum SaveOptionsRemarksYou can specify multiple options by using bitwise or combining individual values.MembersNam

### SaveOptions Enumeration

Specifies various options used to save a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx), a [local or global channel](/csh?context=nidaqmx_mxcncpts_chans) , or a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) to Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SaveOptions

#### Remarks

You can specify multiple options by using bitwise or combining individual values.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AllowInteractiveEditing | 0x1 | The saved object may be edited through an interactive tool, such as Measurement & Automation Explorer (MAX). |
| AllowInteractiveDeletion | 0x2 | The saved object may be deleted through an interactive tool, such as Measurement & Automation Explorer (MAX). |
| OverwriteExisting | 0x4 | If a saved object already exists in Measurement & Automation Explorer (MAX) with the same name as the new object, the new object overwrites the old object. |
| None | 0x0 | No options are enabled. |
| Default | 0x3 | The AllowInteractiveDeletion and AllowInteractiveEditing options are enabled. |
| All | 0x7 | All options are enabled. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-description.html language=enus -->
## TOPIC 02592: Description

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-description.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a description for the scale. SyntaxNamespace: NationalInstruments.DAQmxpublic string Description { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Description

Specifies a description for the scale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Description { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-dispose.html language=enus -->
## TOPIC 02593: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by Scale. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()RemarksUse this method only if the application you create runs on a low memory system.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Dispose()

Releases all resources used by [Scale](nationalinstruments-daqmx-scale.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Remarks

Use this method only if the application you create runs on a low memory system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-dispose__bool.html language=enus -->
## TOPIC 02594: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by Scale or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on implementing

### Dispose(bool)

Releases the managed and unmanaged resources used by [Scale](nationalinstruments-daqmx-scale.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by Scale; false to release only unmanaged resources used by Scale. |

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-name.html language=enus -->
## TOPIC 02595: Name

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-name.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the scale. SyntaxNamespace: NationalInstruments.DAQmxpublic string Name { get; set; }RemarksA String that represents the name of the scale.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Name

Gets the name of the [scale](/csh?context=nidaqmx_mxcncpts_customscales).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Name { get; set; }

#### Remarks

A String that represents the name of the [scale](/csh?context=nidaqmx_mxcncpts_customscales).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-prescaledunits.html language=enus -->
## TOPIC 02596: PreScaledUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-prescaledunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-prescaledunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the values that you want to scale. SyntaxNamespace: NationalInstruments.DAQmxpublic ScalePreScaledUnits PreScaledUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PreScaledUnits

Specifies the units of the values that you want to scale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ScalePreScaledUnits](nationalinstruments-daqmx-scaleprescaledunits.html) PreScaledUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-scaledunits.html language=enus -->
## TOPIC 02597: ScaledUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-scaledunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-scaledunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use for scaled values. You can use an arbitrary string. SyntaxNamespace: NationalInstruments.DAQmxpublic string ScaledUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ScaledUnits

Specifies the units to use for scaled values. You can use an arbitrary string.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ScaledUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-tostring.html language=enus -->
## TOPIC 02598: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale-type.html language=enus -->
## TOPIC 02599: Type

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale-type.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of scale. SyntaxNamespace: NationalInstruments.DAQmxpublic ScaleType Type { get; }RemarksThe type of scale.

### Type

Gets the type of scale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ScaleType](nationalinstruments-daqmx-scaletype.html) Type { get; }

#### Remarks

The type of scale.

Parent topic:

Scale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scale.html language=enus -->
## TOPIC 02600: Scale Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a custom scale that translates between prescaled quantities in device units and quantities scaled to the units of interest. Derives fromMarshalByRefObjectIDisposableSyntaxNamespace: NationalInstruments.DAQmxpublic class Scale : MarshalByRefObject, IDisposableRemarksScale is the base cla

### Scale Class

Encapsulates a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) that translates between prescaled quantities in device units and quantities scaled to the units of interest.

#### Derives from

- MarshalByRefObject
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Scale : MarshalByRefObject, IDisposable

#### Remarks

Scale is the base class for [LinearScale](nationalinstruments-daqmx-linearscale.html), [PolynomialScale](nationalinstruments-daqmx-polynomialscale.html), [RangeMapScale](nationalinstruments-daqmx-rangemapscale.html), and [TableScale](nationalinstruments-daqmx-tablescale.html). All instances of Scale are of one of the derived class types. Refer to the derived class documentation for more information.

When you create a scale, you must provide the scale with a name because the scale is associated with channels through its name. You can create and configure a scale in Measurement & Automation Explorer (MAX) or with the constructor of a class that derives from Scale.

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Description | Specifies a description for the scale. |
| Name | Gets the name of the scale. |
| PreScaledUnits | Specifies the units of the values that you want to scale. |
| ScaledUnits | Specifies the units to use for scaled values. You can use an arbitrary string. |
| Type | Gets the type of scale. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Releases all resources used by Scale. |
| ToString() | Returns a string representation of the object. |
| Dispose(bool) | Releases the managed and unmanaged resources used by Scale or optionally releases only the unmanaged resources. |

#### See Also

- LoadScale(string)
- LinearScale
- PolynomialScale
- RangeMapScale
- TableScale

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scaleprescaledunits.html language=enus -->
## TOPIC 02601: ScalePreScaledUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scaleprescaledunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scaleprescaledunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the values that you want to scale. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ScalePreScaledUnitsRemarksSpecifies the units of the values that you want to scale. Use this enumeration to get or set the value of PreScaledUnits.MembersNameValueDescriptionVolts10348Volt

### ScalePreScaledUnits Enumeration

Specifies the units of the values that you want to scale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ScalePreScaledUnits

#### Remarks

Specifies the units of the values that you want to scale. Use this enumeration to get or set the value of [PreScaledUnits](nationalinstruments-daqmx-scale-prescaledunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Volts | 10348 | Volts. |
| Amps | 10342 | Amperes. |
| Watts | 16203 | Watts. |
| DegreesF | 10144 | Degrees Fahrenheit. |
| DegreesC | 10143 | Degrees Celsius. |
| DegreesR | 10145 | Degrees Rankine. |
| Kelvins | 10325 | Kelvins. |
| Strain | 10299 | Strain. |
| Ohms | 10384 | Ohms. |
| Hertz | 10373 | Hertz. |
| Seconds | 10364 | Seconds. |
| Meters | 10219 | Meters. |
| Inches | 10379 | Inches. |
| Degrees | 10146 | Degrees. |
| Radians | 10273 | Radians. |
| Ticks | 10304 | Ticks. |
| RPM | 16080 | Revolutions per minute. |
| RadiansPerSecond | 16081 | Radians per second. |
| DegreesPerSecond | 16082 | Degrees per second. |
| G | 10186 | 1 g is approximately equal to 9.81 m/s/s. |
| MetersPerSecondSquared | 12470 | Meters per second per second. |
| InchesPerSecondSquared | 12471 | Inches per second per second. |
| MetersPerSecond | 15959 | Meters per second. |
| InchesPerSecond | 15960 | Inches per second. |
| Pascals | 10081 | Pascals. |
| Newtons | 15875 | Newtons. |
| Pounds | 15876 | Pounds. |
| KilogramForce | 15877 | Kilograms-force. |
| PoundsPerSquareInch | 15879 | Pounds per square inch. |
| Bar | 15880 | Bar. |
| NewtonMeters | 15881 | Newton meters. |
| InchOunces | 15882 | Ounce-inches. |
| InchPounds | 15883 | Pound-inches. |
| FootPounds | 15884 | Pound-feet. |
| VoltsPerVolt | 15896 | Volts per volt. |
| MillivoltsPerVolt | 15897 | Millivolts per volt. |
| Coulombs | 16102 | Coulombs. |
| PicoCoulombs | 16103 | PicoCoulombs. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scaletype.html language=enus -->
## TOPIC 02602: ScaleType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scaletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scaletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of custom scale. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ScaleTypeMembersNameValueDescriptionLinear10447Values are scaled linearly. Polynomial10449Values are scaled by using an nth order polynomial equation. RangeMap10448Values are scaled proportionally from a range

### ScaleType Enumeration

Specifies the type of [custom scale](/csh?context=nidaqmx_mxcncpts_customscales).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ScaleType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Linear | 10447 | Values are scaled linearly. |
| Polynomial | 10449 | Values are scaled by using an nth order polynomial equation. |
| RangeMap | 10448 | Values are scaled proportionally from a range of raw values to a range of scaled values. |
| Table | 10450 | An array of raw values is mapped to an array of corresponding scaled values, with all other values scaled proportionally. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-scxi1124range.html language=enus -->
## TOPIC 02603: Scxi1124Range Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-scxi1124range.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-scxi1124range.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the range for the SCXI 1124 calibration values. SyntaxNamespace: NationalInstruments.DAQmxpublic enum Scxi1124RangeMembersNameValueDescriptionRange0to1V14629Range is from 0 volts to 1 volt. Range0to5V14630Range is from 0 volts to 5 volts. Range0to10V14631Range is from 0 volts to 10 volts.

### Scxi1124Range Enumeration

Specifies the range for the SCXI 1124 calibration values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum Scxi1124Range

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Range0to1V | 14629 | Range is from 0 volts to 1 volt. |
| Range0to5V | 14630 | Range is from 0 volts to 5 volts. |
| Range0to10V | 14631 | Range is from 0 volts to 10 volts. |
| RangeNeg1to1V | 14632 | Range is from -1 volt to 1 volt. |
| RangeNeg5to5V | 14633 | Range is from -5 volts to 5 volts. |
| RangeNeg10to10V | 14634 | Range is from -10 volts to 10 volts. |
| Range0to20mA | 14635 | Range is from 0 mA to 20 mA. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-sense.html language=enus -->
## TOPIC 02604: Sense Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-sense.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-sense.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use local or remote sense to sense the output voltage. DAQmx Read (Power Supply) will return remote or local voltage based on the Remote Sense attribute value. Reading this property will return the user-defined value. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SenseRe

### Sense Enumeration

Specifies whether to use local or remote sense to sense the output voltage. [DAQmx](nationalinstruments-daqmx.html) Read (Power Supply) will return remote or local voltage based on the Remote Sense attribute value. Reading this property will return the user-defined value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum Sense

#### Remarks

Specifies whether to use local or remote sense to sense the output voltage. [DAQmx](nationalinstruments-daqmx.html) Read (Power Supply) will return remote or local voltage based on the Remote Sense attribute value. Reading this property will return the user-defined value. Use this enumeration to get or set the value of [PowerRemoteSense](nationalinstruments-daqmx-aichannel-powerremotesense.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Local | 16095 | Local. |
| Remote | 16096 | Remote. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-shuntcalibrationselect.html language=enus -->
## TOPIC 02605: ShuntCalibrationSelect Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-shuntcalibrationselect.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-shuntcalibrationselect.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shunt calibration switch(es) to enable. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ShuntCalibrationSelectMembersNameValueDescriptionA12513Switch A. B12514Switch B.

### ShuntCalibrationSelect Enumeration

Specifies the shunt calibration switch(es) to enable.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ShuntCalibrationSelect

#### Members

| Name | Value | Description |
| --- | --- | --- |
| A | 12513 | Switch A. |
| B | 12514 | Switch B. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-shuntelementlocation.html language=enus -->
## TOPIC 02606: ShuntElementLocation Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-shuntelementlocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-shuntelementlocation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which resistor to use to calibrate the channel(s). SyntaxNamespace: NationalInstruments.DAQmxpublic enum ShuntElementLocationMembersNameValueDescriptionR112465Resistor 1. R212466Resistor 2. R312467Resistor 3. R414813Resistor 4. None10230No resistor.

### ShuntElementLocation Enumeration

Specifies which resistor to use to calibrate the channel(s).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ShuntElementLocation

#### Members

| Name | Value | Description |
| --- | --- | --- |
| R1 | 12465 | Resistor 1. |
| R2 | 12466 | Resistor 2. |
| R3 | 12467 | Resistor 3. |
| R4 | 14813 | Resistor 4. |
| None | 10230 | No resistor. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-shuntresistorsource.html language=enus -->
## TOPIC 02607: ShuntResistorSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-shuntresistorsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-shuntresistorsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use internal or external shunt. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ShuntResistorSourceMembersNameValueDescriptionUserProvided10167Use an external shunt. BuiltIn10200Use the internal shunt. Default-1Use the default shunt.

### ShuntResistorSource Enumeration

Specifies whether to use internal or external shunt.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ShuntResistorSource

#### Members

| Name | Value | Description |
| --- | --- | --- |
| UserProvided | 10167 | Use an external shunt. |
| BuiltIn | 10200 | Use the internal shunt. |
| Default | -1 | Use the default shunt. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-signalroutingmodifiers.html language=enus -->
## TOPIC 02608: SignalRoutingModifiers Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-signalroutingmodifiers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-signalroutingmodifiers.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the signal routed from the source terminal to the destination terminal is inverted. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SignalRoutingModifiersRemarksIf the device is not capable of signal inversion or if a previous route reserved the inversion circuitry in an incompati

### SignalRoutingModifiers Enumeration

Specifies if the signal routed from the source terminal to the destination terminal is [inverted](/csh?context=nidaqmx_mxcncpts_inversionsignals).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SignalRoutingModifiers

#### Remarks

If the device is not capable of signal inversion or if a previous route reserved the inversion circuitry in an incompatible configuration, attempting to invert the signal causes an error.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| InvertPolarity | 0x1 | The signal is inverted. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-convertlateerrorstowarnings.html language=enus -->
## TOPIC 02609: ConvertLateErrorsToWarnings

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-convertlateerrorstowarnings.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-convertlateerrorstowarnings.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if WaitForNextSampleClock(double), reading from the task, and writing to the task convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with NumberOfWarmupIterations execute. SyntaxNamespace: NationalInstruments.DAQmx

### ConvertLateErrorsToWarnings

Specifies if [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html), reading from the task, and writing to the task convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with [NumberOfWarmupIterations](nationalinstruments-daqmx-singlepoint-numberofwarmupiterations.html) execute.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ConvertLateErrorsToWarnings { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-numberofwarmupiterations.html language=enus -->
## TOPIC 02610: NumberOfWarmupIterations

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-numberofwarmupiterations.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-numberofwarmupiterations.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of loop iterations that must occur before WaitForNextSampleClock(double) and reading from the task return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes

### NumberOfWarmupIterations

Specifies the number of loop iterations that must occur before [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html) and reading from the task return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfWarmupIterations { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-reportmissedsamples.html language=enus -->
## TOPIC 02611: ReportMissedSamples

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-reportmissedsamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-reportmissedsamples.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether reading from the task returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect WaitForNextSampleClock(double). Set this property to true for applications that need to detect lateness without using WaitForNextSampleClock(double). S

### ReportMissedSamples

Specifies whether reading from the task returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html). Set this property to true for [applications](/csh?context=nidaqmx_mxcncpts_readwritelate) that need to detect lateness without using [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReportMissedSamples { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-tostring.html language=enus -->
## TOPIC 02612: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-waitfornextsampleclock.html language=enus -->
## TOPIC 02613: WaitForNextSampleClock()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-waitfornextsampleclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-waitfornextsampleclock.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the next pulse of the sample clock occurs, with a timeout value of 10 seconds. SyntaxNamespace: NationalInstruments.DAQmxpublic bool WaitForNextSampleClock()RemarksIf an extra sample clock pulse occurs between calls to this method, the second call returns an error or warning and waits fo

### WaitForNextSampleClock()

Waits until the next pulse of the [sample clock](/csh?context=nidaqmx_mxcncpts_sampclock) occurs, with a timeout value of 10 seconds.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WaitForNextSampleClock()

#### Remarks

If an extra sample clock pulse occurs between calls to this method, the second call returns an error or warning and waits for the next sample clock pulse. Use the [ConvertLateErrorsToWarnings](nationalinstruments-daqmx-singlepoint-convertlateerrorstowarnings.html) property to specify whether this method returns errors or warnings.

Use this method to ensure [I/O cycles](/csh?context=nidaqmx_mxcncpts_iocycles) complete within sample clock periods. National Instruments recommends you use this method for certain applications only.

#### Returns

Specifies whether the next sample clock is late.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html language=enus -->
## TOPIC 02614: WaitForNextSampleClock(double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the next pulse of the sample clock occurs. SyntaxNamespace: NationalInstruments.DAQmxpublic bool WaitForNextSampleClock(double timeout)RemarksIf an extra sample clock pulse occurs between calls to this method, the second call returns an error or warning and waits for the next sample cloc

### WaitForNextSampleClock(double)

Waits until the next pulse of the [sample clock](/csh?context=nidaqmx_mxcncpts_sampclock) occurs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WaitForNextSampleClock(double timeout)

#### Remarks

If an extra sample clock pulse occurs between calls to this method, the second call returns an error or warning and waits for the next sample clock pulse. Use the [ConvertLateErrorsToWarnings](nationalinstruments-daqmx-singlepoint-convertlateerrorstowarnings.html) property to specify whether this method returns errors or warnings.

Use this method to ensure [I/O cycles](/csh?context=nidaqmx_mxcncpts_iocycles) complete within sample clock periods. National Instruments recommends you use this method for certain applications only.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | double | The maximum amount of time, in seconds, to wait for the next sample clock pulse. If the time elapses, this method returns an error. If you set timeout to -1, this method waits indefinitely. |

#### Returns

Specifies whether the next sample clock is late.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-waitfornextsampleclockwaitmode.html language=enus -->
## TOPIC 02615: WaitForNextSampleClockWaitMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-waitfornextsampleclockwaitmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-waitfornextsampleclockwaitmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how WaitForNextSampleClock(double) waits for the next Sample Clock pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic WaitForNextSampleClockWaitMode WaitForNextSampleClockWaitMode { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned

### WaitForNextSampleClockWaitMode

Specifies how [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html) waits for the next Sample Clock pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WaitForNextSampleClockWaitMode](nationalinstruments-daqmx-waitfornextsampleclockwaitmode.html) WaitForNextSampleClockWaitMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint-writerecoverymode.html language=enus -->
## TOPIC 02616: WriteRecoveryMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint-writerecoverymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint-writerecoverymode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. SyntaxNamespace: NationalInstruments.DAQmxpublic WriteRecoveryMode WriteRecoveryMode { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned

### WriteRecoveryMode

Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WriteRecoveryMode](nationalinstruments-daqmx-writerecoverymode.html) WriteRecoveryMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-singlepoint.html language=enus -->
## TOPIC 02617: SinglePoint Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-singlepoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-singlepoint.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods that configure how to align to the sample clock of the Task. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class SinglePoint : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample applications are located in

### SinglePoint Class

Contains properties and methods that configure how to align to the sample clock of the [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SinglePoint : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| ConvertLateErrorsToWarnings | Specifies if WaitForNextSampleClock(double), reading from the task, and writing to the task convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with NumberOfWarmupIterations execute. |
| NumberOfWarmupIterations | Specifies the number of loop iterations that must occur before WaitForNextSampleClock(double) and reading from the task return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system. |
| ReportMissedSamples | Specifies whether reading from the task returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect WaitForNextSampleClock(double). Set this property to true for applications that need to detect lateness without using WaitForNextSampleClock(double). |
| WaitForNextSampleClockWaitMode | Specifies how WaitForNextSampleClock(double) waits for the next Sample Clock pulse. |
| WriteRecoveryMode | Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |
| WaitForNextSampleClock() | Waits until the next pulse of the sample clock occurs, with a timeout value of 10 seconds. |
| WaitForNextSampleClock(double) | Waits until the next pulse of the sample clock occurs. |

#### See Also

- Timing
- SinglePoint

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-analogedge.html language=enus -->
## TOPIC 02618: AnalogEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-analogedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-analogedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AnalogEdgeStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogEdgeStartTrigger AnalogEdge { get; }RemarksThe AnalogEdgeStartTrigger.

### AnalogEdge

Gets the [AnalogEdgeStartTrigger](nationalinstruments-daqmx-analogedgestarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogEdgeStartTrigger](nationalinstruments-daqmx-analogedgestarttrigger.html) AnalogEdge { get; }

#### Remarks

The [AnalogEdgeStartTrigger](nationalinstruments-daqmx-analogedgestarttrigger.html).

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-analogmultiedge.html language=enus -->
## TOPIC 02619: AnalogMultiEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-analogmultiedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-analogmultiedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AnalogMultiEdgeStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogMultiEdgeStartTrigger AnalogMultiEdge { get; }RemarksThe AnalogMultiEdgeStartTrigger.

### AnalogMultiEdge

Gets the [AnalogMultiEdgeStartTrigger](nationalinstruments-daqmx-analogmultiedgestarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogMultiEdgeStartTrigger](nationalinstruments-daqmx-analogmultiedgestarttrigger.html) AnalogMultiEdge { get; }

#### Remarks

The [AnalogMultiEdgeStartTrigger](nationalinstruments-daqmx-analogmultiedgestarttrigger.html).

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-analogwindow.html language=enus -->
## TOPIC 02620: AnalogWindow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-analogwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-analogwindow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the AnalogWindowStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic AnalogWindowStartTrigger AnalogWindow { get; }RemarksThe AnalogWindowStartTrigger.

### AnalogWindow

Gets the [AnalogWindowStartTrigger](nationalinstruments-daqmx-analogwindowstarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AnalogWindowStartTrigger](nationalinstruments-daqmx-analogwindowstarttrigger.html) AnalogWindow { get; }

#### Remarks

The [AnalogWindowStartTrigger](nationalinstruments-daqmx-analogwindowstarttrigger.html).

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-configureanalogedgetrigger__string-analogedgestarttriggerslope-double.html language=enus -->
## TOPIC 02621: ConfigureAnalogEdgeTrigger(string, AnalogEdgeStartTriggerSlope, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-configureanalogedgetrigger__string-analogedgestarttriggerslope-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-configureanalogedgetrigger__string-analogedgestarttriggerslope-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to start acquiring or generating samples when an analog signal crosses the level you specify. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureAnalogEdgeTrigger(string source, AnalogEdgeStartTriggerSlope slope, double level)RemarksThe NI-DAQmx driver does not determ

### ConfigureAnalogEdgeTrigger(string, AnalogEdgeStartTriggerSlope, double)

Configures the task to start acquiring or generating samples when an [analog signal crosses the level you specify](/csh?context=nidaqmx_mxcncpts_analogtriggering).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureAnalogEdgeTrigger(string source, AnalogEdgeStartTriggerSlope slope, double level)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureAnalogEdgeTrigger(string, AnalogEdgeStartTriggerSlope, double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a virtual channel or terminal where there is a digital signal to use as the source of the trigger. For E Series devices, if you use a channel name, the channel must be the first channel in the task. The only terminal you can use for E Series devices is PFI0. |
| slope | AnalogEdgeStartTriggerSlope | The slope of the signal to start acquiring or generating samples when the signal crosses level . |
| level | double | The threshold to start acquiring or generating samples, in the units of the measurement or generation. Use slope to specify on which slope to trigger at this threshold. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-configureanalogmultiedgetrigger__string-analogmultiedgestarttriggerslope_arr1-double_arr1.html language=enus -->
## TOPIC 02622: ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeStartTriggerSlope[], double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-configureanalogmultiedgetrigger__string-analogmultiedgestarttriggerslope_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-configureanalogmultiedgetrigger__string-analogmultiedgestarttriggerslope_arr1-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to start acquiring or generating samples when any of the configured analog signals cross the respective levels you specify. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureAnalogMultiEdgeTrigger(string sources, AnalogMultiEdgeStartTriggerSlope[] slopes, double[] le

### ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeStartTriggerSlope[], double[])

Configures the task to start acquiring or generating samples when any of the configured analog signals cross the respective levels you specify.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureAnalogMultiEdgeTrigger(string sources, AnalogMultiEdgeStartTriggerSlope[] slopes, double[] levels)

#### Remarks

Multi-edge triggering treats the specified triggers as if they are logically **OR**ed.

The number of trigger sources represented by *sources*  and the number of elements in *slopes*  and *levels*  must all be the same.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sources | string | A string specifying a list of terminals, physical channel names, or ranges of physical channels where there are analog signals to use as the sources of the trigger. |
| slopes | AnalogMultiEdgeStartTriggerSlope[] | An array containing the slopes of the signals to start acquiring or generating samples when the respective signal crosses the respective trigger level. Each element corresponds to the sources specified in sources and elements in the other array parameters. |
| levels | double[] | An array containing the thresholds at which to start acquiring or generating samples. Each element corresponds to the sources specified in sources and elements in the other array parameters. Specify these values in the units of the measurement or generation. Use slopes to specify on which slopes to trigger at the respective thresholds. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-configureanalogwindowtrigger__string-analogwindowstarttriggercondition-double-double.html language=enus -->
## TOPIC 02623: ConfigureAnalogWindowTrigger(string, AnalogWindowStartTriggerCondition, double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-configureanalogwindowtrigger__string-analogwindowstarttriggercondition-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-configureanalogwindowtrigger__string-analogwindowstarttriggercondition-double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to start acquiring or generating samples when an analog signal enters or leaves a range you specify. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureAnalogWindowTrigger(string source, AnalogWindowStartTriggerCondition condition, double top, double bottom)RemarksThe

### ConfigureAnalogWindowTrigger(string, AnalogWindowStartTriggerCondition, double, double)

Configures the task to start acquiring or generating samples when an [analog signal enters or leaves a range you specify](/csh?context=nidaqmx_mxcncpts_algwindowtrig).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureAnalogWindowTrigger(string source, AnalogWindowStartTriggerCondition condition, double top, double bottom)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureAnalogWindowTrigger(string, AnalogWindowStartTriggerCondition, double, double) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a virtual channel or terminal where there is a digital signal to use as the source of the trigger. For E Series devices, if you use a channel name, the channel must be the first channel in the task. The only terminal you can use for E Series devices is PFI0. |
| condition | AnalogWindowStartTriggerCondition | Specifies if the reference trigger occurs when the signal enters the window or leaves the window. Use bottom and top to specify the limits of the window. |
| top | double | The upper limit of the voltage window, in the units of the measurement or generation. |
| bottom | double | The lower limit of the voltage window, in the units of the measurement or generation. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-configuredigitaledgetrigger__string-digitaledgestarttriggeredge.html language=enus -->
## TOPIC 02624: ConfigureDigitalEdgeTrigger(string, DigitalEdgeStartTriggerEdge)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-configuredigitaledgetrigger__string-digitaledgestarttriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-configuredigitaledgetrigger__string-digitaledgestarttriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to start acquiring or generating samples on a rising or falling edge of a digital signal. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeStartTriggerEdge edge)RemarksThe NI-DAQmx driver does not determine if the request

### ConfigureDigitalEdgeTrigger(string, DigitalEdgeStartTriggerEdge)

Configures the task to start acquiring or generating samples on a [rising or falling edge of a digital signal](/csh?context=nidaqmx_mxcncpts_digtrigger).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeStartTriggerEdge edge)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalEdgeTrigger(string, DigitalEdgeStartTriggerEdge) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a terminal where there is a digital signal to use as the source of the trigger. |
| edge | DigitalEdgeStartTriggerEdge | The edge of the digital signal to start acquiring or generating samples. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-configuredigitalpatterntrigger__string-string-digitalpatternstarttriggercondition.html language=enus -->
## TOPIC 02625: ConfigureDigitalPatternTrigger(string, string, DigitalPatternStartTriggerCondition)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-configuredigitalpatterntrigger__string-string-digitalpatternstarttriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-configuredigitalpatterntrigger__string-string-digitalpatternstarttriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to start acquiring or generating samples when a digital pattern is matched. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureDigitalPatternTrigger(string source, string pattern, DigitalPatternStartTriggerCondition condition)RemarksThe NI-DAQmx driver does not determ

### ConfigureDigitalPatternTrigger(string, string, DigitalPatternStartTriggerCondition)

Configures the task to start acquiring or generating samples when a [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) is matched.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureDigitalPatternTrigger(string source, string pattern, DigitalPatternStartTriggerCondition condition)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalPatternTrigger(string, string, DigitalPatternStartTriggerCondition) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. |
| pattern | string | The digital pattern that must be met for the trigger to occur. |
| condition | DigitalPatternStartTriggerCondition | The condition under which the trigger occurs. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-configurenone.html language=enus -->
## TOPIC 02626: ConfigureNone()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-configurenone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-configurenone.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to start acquiring or generating samples immediately upon starting the task. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureNone()RemarksThe NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does no

### ConfigureNone()

Configures the task to start acquiring or generating samples immediately upon starting the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureNone()

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-configuretimetrigger__precisiondatetime-timestarttriggertimescale.html language=enus -->
## TOPIC 02627: ConfigureTimeTrigger(PrecisionDateTime, TimeStartTriggerTimescale)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-configuretimetrigger__precisiondatetime-timestarttriggertimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-configuretimetrigger__precisiondatetime-timestarttriggertimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the task to start acquiring or generating samples at a the specified triggerTime . SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureTimeTrigger(PrecisionDateTime triggerTime, TimeStartTriggerTimescale timescale)RemarksThe trigger time is represented by a PrecisionDateTime ex

### ConfigureTimeTrigger(PrecisionDateTime, TimeStartTriggerTimescale)

Configures the task to start acquiring or generating samples at a the specified *triggerTime* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureTimeTrigger(PrecisionDateTime triggerTime, TimeStartTriggerTimescale timescale)

#### Remarks

Note

The trigger time is represented by a PrecisionDateTime expressed as a UTC time. To set a trigger time based on the current system time, use PrecisionDateTime.UtcNow, adding an offset, rather than PrecisionDateTime.Now.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| triggerTime | PrecisionDateTime | The start trigger time. |
| timescale | TimeStartTriggerTimescale | The timescale of the triggerTime . For more information, see TimeStartTriggerTimescale. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-delay.html language=enus -->
## TOPIC 02628: Delay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-delay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with DelayUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double Delay { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQ

### Delay

Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with [DelayUnits](nationalinstruments-daqmx-starttrigger-delayunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Delay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-delayunits.html language=enus -->
## TOPIC 02629: DelayUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-delayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-delayunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of Delay. SyntaxNamespace: NationalInstruments.DAQmxpublic StartTriggerDelayUnits DelayUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DelayUnits

Specifies the units of [Delay](nationalinstruments-daqmx-starttrigger-delay.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [StartTriggerDelayUnits](nationalinstruments-daqmx-starttriggerdelayunits.html) DelayUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-digitaledge.html language=enus -->
## TOPIC 02630: DigitalEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-digitaledge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalEdgeStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeStartTrigger DigitalEdge { get; }RemarksThe DigitalEdgeStartTrigger.

### DigitalEdge

Gets the [DigitalEdgeStartTrigger](nationalinstruments-daqmx-digitaledgestarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeStartTrigger](nationalinstruments-daqmx-digitaledgestarttrigger.html) DigitalEdge { get; }

#### Remarks

The [DigitalEdgeStartTrigger](nationalinstruments-daqmx-digitaledgestarttrigger.html).

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-digitalpattern.html language=enus -->
## TOPIC 02631: DigitalPattern

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-digitalpattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-digitalpattern.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalPatternStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalPatternStartTrigger DigitalPattern { get; }RemarksThe DigitalPatternStartTrigger.

### DigitalPattern

Gets the [DigitalPatternStartTrigger](nationalinstruments-daqmx-digitalpatternstarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalPatternStartTrigger](nationalinstruments-daqmx-digitalpatternstarttrigger.html) DigitalPattern { get; }

#### Remarks

The [DigitalPatternStartTrigger](nationalinstruments-daqmx-digitalpatternstarttrigger.html).

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-maximumnumberoftriggerstodetect.html language=enus -->
## TOPIC 02632: MaximumNumberOfTriggersToDetect

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-maximumnumberoftriggerstodetect.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-maximumnumberoftriggerstodetect.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Numb

### MaximumNumberOfTriggersToDetect

Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of [Triggers](nationalinstruments-daqmx-triggers.html) to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long MaximumNumberOfTriggersToDetect { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-retriggerable.html language=enus -->
## TOPIC 02633: Retriggerable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-retriggerable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-retriggerable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to true, the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the proces

### Retriggerable

Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to true, the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring or generating signals.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Retriggerable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-retriggerwindow.html language=enus -->
## TOPIC 02634: RetriggerWindow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-retriggerwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-retriggerwindow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time speci

### RetriggerWindow

Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time specified covers the entire time span desired for retrigger detection to avoid missed triggers. Specifying a Retrigger Window of -1 causes the window to be infinite.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RetriggerWindow { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-terminal.html language=enus -->
## TOPIC 02635: Terminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-terminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic string Terminal { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### Terminal

Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Terminal { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-time.html language=enus -->
## TOPIC 02636: Time

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-time.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the TimeStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic TimeStartTrigger Time { get; }RemarksThe TimeStartTrigger.

### Time

Gets the [TimeStartTrigger](nationalinstruments-daqmx-timestarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TimeStartTrigger](nationalinstruments-daqmx-timestarttrigger.html) Time { get; }

#### Remarks

The [TimeStartTrigger](nationalinstruments-daqmx-timestarttrigger.html).

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-timestamp.html language=enus -->
## TOPIC 02637: Timestamp

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-timestamp.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start trigger timestamp. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime Timestamp { get; }RemarksThe start trigger timestamp.The timestamp returned is expressed as a UTC time. For more information on timestamps in NI-DAQmx, see Timestamps.ExceptionsTypeDescriptionNationa

### Timestamp

Gets the start trigger timestamp.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime Timestamp { get; }

#### Remarks

The start trigger timestamp.

Note

The timestamp returned is expressed as a UTC time.

Timestamps

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-timestampenable.html language=enus -->
## TOPIC 02638: TimestampEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-timestampenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-timestampenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. SyntaxNamespace: NationalInstruments.DAQmxpublic bool TimestampEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExcept

### TimestampEnable

Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool TimestampEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-timestamptimescale.html language=enus -->
## TOPIC 02639: TimestampTimescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-timestamptimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-timestamptimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start trigger timestamp timescale. SyntaxNamespace: NationalInstruments.DAQmxpublic StartTriggerTimestampTimescale TimestampTimescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TimestampTimescale

Specifies the start trigger timestamp timescale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [StartTriggerTimestampTimescale](nationalinstruments-daqmx-starttriggertimestamptimescale.html) TimestampTimescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-tostring.html language=enus -->
## TOPIC 02640: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-triggerwindow.html language=enus -->
## TOPIC 02641: TriggerWindow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-triggerwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-triggerwindow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detecte

### TriggerWindow

Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double TriggerWindow { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger-type.html language=enus -->
## TOPIC 02642: Type

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger-type.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to start a task. SyntaxNamespace: NationalInstruments.DAQmxpublic StartTriggerType Type { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Type

Specifies the [type](/csh?context=nidaqmx_mxcncpts_triggertypes) of trigger to use to start a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [StartTriggerType](nationalinstruments-daqmx-starttriggertype.html) Type { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

StartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttrigger.html language=enus -->
## TOPIC 02643: StartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods that configure how the task begins measurement or generation. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class StartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample applications are located

### StartTrigger Class

Contains properties and methods that configure [how the task begins measurement or generation](/csh?context=nidaqmx_mxcncpts_starttrig).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class StartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AnalogEdge | Gets the AnalogEdgeStartTrigger. |
| AnalogMultiEdge | Gets the AnalogMultiEdgeStartTrigger. |
| AnalogWindow | Gets the AnalogWindowStartTrigger. |
| Delay | Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with DelayUnits. |
| DelayUnits | Specifies the units of Delay. |
| DigitalEdge | Gets the DigitalEdgeStartTrigger. |
| DigitalPattern | Gets the DigitalPatternStartTrigger. |
| MaximumNumberOfTriggersToDetect | Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger. |
| Retriggerable | Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to true, the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring or generating signals. |
| RetriggerWindow | Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time specified covers the entire time span desired for retrigger detection to avoid missed triggers. Specifying a Retrigger Window of -1 causes the window to be infinite. |
| Terminal | Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
| Time | Gets the TimeStartTrigger. |
| Timestamp | Gets the start trigger timestamp. |
| TimestampEnable | Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
| TimestampTimescale | Specifies the start trigger timestamp timescale. |
| TriggerWindow | Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite. |
| Type | Specifies the type of trigger to use to start a task. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAnalogEdgeTrigger(string, AnalogEdgeStartTriggerSlope, double) | Configures the task to start acquiring or generating samples when an analog signal crosses the level you specify. |
| ConfigureAnalogMultiEdgeTrigger(string, AnalogMultiEdgeStartTriggerSlope[], double[]) | Configures the task to start acquiring or generating samples when any of the configured analog signals cross the respective levels you specify. |
| ConfigureAnalogWindowTrigger(string, AnalogWindowStartTriggerCondition, double, double) | Configures the task to start acquiring or generating samples when an analog signal enters or leaves a range you specify. |
| ConfigureDigitalEdgeTrigger(string, DigitalEdgeStartTriggerEdge) | Configures the task to start acquiring or generating samples on a rising or falling edge of a digital signal. |
| ConfigureDigitalPatternTrigger(string, string, DigitalPatternStartTriggerCondition) | Configures the task to start acquiring or generating samples when a digital pattern is matched. |
| ConfigureNone() | Configures the task to start acquiring or generating samples immediately upon starting the task. |
| ConfigureTimeTrigger(PrecisionDateTime, TimeStartTriggerTimescale) | Configures the task to start acquiring or generating samples at a the specified triggerTime . |
| ToString() | Returns a string representation of the object. |

#### See Also

- Triggers
- StartTrigger

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttriggerdelayunits.html language=enus -->
## TOPIC 02644: StartTriggerDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttriggerdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttriggerdelayunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of Delay. SyntaxNamespace: NationalInstruments.DAQmxpublic enum StartTriggerDelayUnitsRemarksSpecifies the units of Delay. Use this enumeration to get or set the value of DelayUnits.MembersNameValueDescriptionSampleClockPeriods10286Complete periods of the Sample Clock. Seconds103

### StartTriggerDelayUnits Enumeration

Specifies the units of [Delay](nationalinstruments-daqmx-starttrigger-delay.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum StartTriggerDelayUnits

#### Remarks

Specifies the units of [Delay](nationalinstruments-daqmx-starttrigger-delay.html). Use this enumeration to get or set the value of [DelayUnits](nationalinstruments-daqmx-starttrigger-delayunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SampleClockPeriods | 10286 | Complete periods of the Sample Clock. |
| Seconds | 10364 | Seconds. |
| Ticks | 10304 | Timebase ticks. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttriggerpulsepolarity.html language=enus -->
## TOPIC 02645: StartTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttriggerpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttriggerpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic enum StartTriggerPulsePolarityRemarksSpecifies the polarity of the exported Start Trigger. Use this enumeration to get or set the value of StartTriggerPulsePolarity.MembersNameValueDescriptionActiv

### StartTriggerPulsePolarity Enumeration

Specifies the polarity of the exported Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum StartTriggerPulsePolarity

#### Remarks

Specifies the polarity of the exported Start Trigger. Use this enumeration to get or set the value of [StartTriggerPulsePolarity](nationalinstruments-daqmx-exportsignals-starttriggerpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttriggertimestamptimescale.html language=enus -->
## TOPIC 02646: StartTriggerTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttriggertimestamptimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttriggertimestamptimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start trigger timestamp timescale. SyntaxNamespace: NationalInstruments.DAQmxpublic enum StartTriggerTimestampTimescaleRemarksSpecifies the start trigger timestamp timescale. Use this enumeration to get or set the value of TimestampTimescale.MembersNameValueDescriptionHostTime16126Use

### StartTriggerTimestampTimescale Enumeration

Specifies the start trigger timestamp timescale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum StartTriggerTimestampTimescale

#### Remarks

Specifies the start trigger timestamp timescale. Use this enumeration to get or set the value of [TimestampTimescale](nationalinstruments-daqmx-starttrigger-timestamptimescale.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HostTime | 16126 | Use the host device. |
| IODeviceTime | 16127 | Use the I/O device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-starttriggertype.html language=enus -->
## TOPIC 02647: StartTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-starttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-starttriggertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to start a task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum StartTriggerTypeRemarksSpecifies the type of trigger to use to start a task. Use this enumeration to get or set the value of Type.MembersNameValueDescriptionAnalogEdge10099Trigger when an anal

### StartTriggerType Enumeration

Specifies the [type](/csh?context=nidaqmx_mxcncpts_triggertypes) of trigger to use to start a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum StartTriggerType

#### Remarks

Specifies the [type](/csh?context=nidaqmx_mxcncpts_triggertypes) of trigger to use to start a task. Use this enumeration to get or set the value of [Type](nationalinstruments-daqmx-starttrigger-type.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AnalogEdge | 10099 | Trigger when an analog signal signal crosses a threshold. |
| AnalogMultiEdge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
| DigitalEdge | 10150 | Trigger on the rising or falling edge of a digital signal. |
| DigitalPattern | 10398 | Trigger when digital physical channels match a digital pattern. |
| AnalogWindow | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable triggering for the task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-autoconnectanalogbus.html language=enus -->
## TOPIC 02648: AutoConnectAnalogBus

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-autoconnectanalogbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-autoconnectanalogbus.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AutoConnectAnalogBus { get; set; }RemarksSpecifies if NI-DAQmx routes multiplexed channels to the analog bus ba

### AutoConnectAnalogBus

Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AutoConnectAnalogBus { get; set; }

#### Remarks

Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-issettled.html language=enus -->
## TOPIC 02649: IsSettled

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-issettled.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-issettled.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates when SettlingTime has expired. SyntaxNamespace: NationalInstruments.DAQmxpublic bool IsSettled { get; }

### IsSettled

Indicates when [SettlingTime](nationalinstruments-daqmx-switch-settlingtime.html) has expired.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsSettled { get; }

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-numberofcolumns.html language=enus -->
## TOPIC 02650: NumberOfColumns

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-numberofcolumns.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-numberofcolumns.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfColumns { get; }RemarksIndicates the number of columns on a device in a matrix switch topology. This value is a

### NumberOfColumns

Gets the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfColumns { get; }

#### Remarks

Indicates the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-numberofrelays.html language=enus -->
## TOPIC 02651: NumberOfRelays

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-numberofrelays.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-numberofrelays.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of relays on the device. This value matches the number of relay names in RelayList. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfRelays { get; }RemarksIndicates the number of relays on the device. This value matches the number of relay names in RelayList.

### NumberOfRelays

Indicates the number of relays on the device. This value matches the number of relay names in [RelayList](nationalinstruments-daqmx-switch-relaylist.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfRelays { get; }

#### Remarks

Indicates the number of relays on the device. This value matches the number of relay names in [RelayList](nationalinstruments-daqmx-switch-relaylist.html).

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-numberofrows.html language=enus -->
## TOPIC 02652: NumberOfRows

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-numberofrows.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-numberofrows.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfRows { get; }RemarksIndicates the number of rows on a device in a matrix switch topology. In

### NumberOfRows

Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfRows { get; }

#### Remarks

Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-numberofswitchchannels.html language=enus -->
## TOPIC 02653: NumberOfSwitchChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-numberofswitchchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-numberofswitchchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in SwitchChannelList. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfSwitchChannels { get; }

### NumberOfSwitchChannels

Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in [SwitchChannelList](nationalinstruments-daqmx-switch-switchchannellist.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfSwitchChannels { get; }

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-powerdownlatchingrelaysaftersettling.html language=enus -->
## TOPIC 02654: PowerDownLatchingRelaysAfterSettling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-powerdownlatchingrelaysaftersettling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-powerdownlatchingrelaysaftersettling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if WaitForSettling powers down latching relays after waiting for the device to settle. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PowerDownLatchingRelaysAfterSettling { get; set; }

### PowerDownLatchingRelaysAfterSettling

Specifies if [WaitForSettling](nationalinstruments-daqmx-switch-waitforsettling.html) powers down latching relays after waiting for the device to settle.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PowerDownLatchingRelaysAfterSettling { get; set; }

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-relaylist.html language=enus -->
## TOPIC 02655: RelayList

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-relaylist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-relaylist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a comma-delimited list of relay names. SyntaxNamespace: NationalInstruments.DAQmxpublic string RelayList { get; }RemarksIndicates a comma-delimited list of relay names.

### RelayList

Indicates a comma-delimited list of relay names.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string RelayList { get; }

#### Remarks

Indicates a comma-delimited list of relay names.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-settlingtime.html language=enus -->
## TOPIC 02656: SettlingTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-settlingtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-settlingtime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported se

### SettlingTime

Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SettlingTime { get; set; }

#### Remarks

Specifies in seconds the amount of time to wait for the switch to settle (or debounce).

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-settopologyandreset__string.html language=enus -->
## TOPIC 02657: SetTopologyAndReset(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-settopologyandreset__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-settopologyandreset__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a switch device and sets its topology. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetTopologyAndReset(string newTopology)RemarksThis method differs from Reset because it uses the value of newTopology rather than the topology specified in Measurement & Automation Explorer (MAX). How

### SetTopologyAndReset(string)

Resets a switch device and sets its [topology](/csh?context=nidaqmx_mxcncpts_topology).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetTopologyAndReset(string newTopology)

#### Remarks

This method differs from [Reset](nationalinstruments-daqmx-device-reset.html) because it uses the value of *newTopology*  rather than the topology specified in Measurement & Automation Explorer (MAX). However, this method maintains the channel usage defaults that you configure in MAX.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newTopology | string | The switch topology to use on the device. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-supportedtopologies.html language=enus -->
## TOPIC 02658: SupportedTopologies

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-supportedtopologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-supportedtopologies.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of the names of all switch topologies supported by this switch device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] SupportedTopologies { get; }RemarksAn array of String that contains the names of all switch topologies supported by this switch device.ExceptionsTypeDescript

### SupportedTopologies

Gets an array of the names of all [switch topologies](/csh?context=nidaqmx_mxcncpts_topology) supported by this switch device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] SupportedTopologies { get; }

#### Remarks

An array of String that contains the names of all switch topologies supported by this switch device.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-switchchannellist.html language=enus -->
## TOPIC 02659: SwitchChannelList

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-switchchannellist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-switchchannellist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a comma-delimited list of channel names for the current topology of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string SwitchChannelList { get; }

### SwitchChannelList

Indicates a comma-delimited list of channel names for the current topology of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SwitchChannelList { get; }

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-temperature.html language=enus -->
## TOPIC 02660: Temperature

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-temperature.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information. SyntaxNamespace: NationalInstruments.DAQmxpublic double Temperature { get; }

### Temperature

Indicates the current temperature as read by the [Switch](nationalinstruments-daqmx-switch.html) module in degrees Celsius. Refer to your device documentation for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Temperature { get; }

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-topology.html language=enus -->
## TOPIC 02661: Topology

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-topology.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current topology of the device. This value is one of the topology options in SetTopologyAndReset(string). SyntaxNamespace: NationalInstruments.DAQmxpublic string Topology { get; }

### Topology

Indicates the current topology of the device. This value is one of the topology options in [SetTopologyAndReset(string)](nationalinstruments-daqmx-switch-settopologyandreset__string.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Topology { get; }

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-tostring.html language=enus -->
## TOPIC 02662: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch-waitforsettling.html language=enus -->
## TOPIC 02663: WaitForSettling()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch-waitforsettling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch-waitforsettling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the settling time on the device to expire. SyntaxNamespace: NationalInstruments.DAQmxpublic void WaitForSettling()RemarksThe settling time is reset and begins counting down upon a switch operation. Therefore, this method might return immediately if no operation happened recently.Exceptions

### WaitForSettling()

Waits for the settling time on the device to expire.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WaitForSettling()

#### Remarks

The settling time is reset and begins counting down upon a switch operation. Therefore, this method might return immediately if no operation happened recently.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Switch Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switch.html language=enus -->
## TOPIC 02664: Switch Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switch.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switch.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This type is obsolete. Will warn if used Encapsulates a switch device and contains properties and methods that operate on switch devices outside the context of a task. Derives fromMarshalByRefObjectSyntaxNamespace: NationalInstruments.DAQmxpublic class Switch : MarshalByRefObjectRemarksExa

### Switch Class

**Obsolete: This type is obsolete. Will warn if used** 
Encapsulates a switch device and contains properties and methods that operate on switch devices outside the context of a task.

#### Derives from

- MarshalByRefObject

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Switch : MarshalByRefObject

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AutoConnectAnalogBus | Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property. |
| IsSettled | Indicates when SettlingTime has expired. |
| NumberOfColumns | Gets the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology. |
| NumberOfRelays | Indicates the number of relays on the device. This value matches the number of relay names in RelayList. |
| NumberOfRows | Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology. |
| NumberOfSwitchChannels | Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in SwitchChannelList. |
| PowerDownLatchingRelaysAfterSettling | Specifies if WaitForSettling powers down latching relays after waiting for the device to settle. |
| RelayList | Indicates a comma-delimited list of relay names. |
| SettlingTime | Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times. |
| SupportedTopologies | Gets an array of the names of all switch topologies supported by this switch device. |
| SwitchChannelList | Indicates a comma-delimited list of channel names for the current topology of the device. |
| Temperature | Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information. |
| Topology | Indicates the current topology of the device. This value is one of the topology options in SetTopologyAndReset(string). |

#### Methods

| Name | Description |
| --- | --- |
| SetTopologyAndReset(string) | Resets a switch device and sets its topology. |
| ToString() | Returns a string representation of the object. |
| WaitForSettling() | Waits for the settling time on the device to expire. |

#### See Also

- Switch

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-analogbussharingenable.html language=enus -->
## TOPIC 02665: AnalogBusSharingEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-analogbussharingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-analogbussharingenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to true to enable sharing on the channel that connects to the analog bus line. Analog bus sharing is disa

### AnalogBusSharingEnable

Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to true to enable sharing on the channel that connects to the analog bus line. Analog bus sharing is disabled by default.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AnalogBusSharingEnable { get; set; }

#### Remarks

Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously.

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-bandwidth.html language=enus -->
## TOPIC 02666: Bandwidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-bandwidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration. SyntaxNamespace: NationalInstruments.DAQmxpublic double Bandwidth { get; }

### Bandwidth

Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Bandwidth { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-dispose.html language=enus -->
## TOPIC 02667: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by SwitchChannel. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()RemarksUse this method only if the application you create runs on a low memory system.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an e

### Dispose()

Releases all resources used by [SwitchChannel](nationalinstruments-daqmx-switchchannel.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Remarks

Use this method only if the application you create runs on a low memory system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-dispose__bool.html language=enus -->
## TOPIC 02668: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by SwitchChannel or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on impl

### Dispose(bool)

Releases the managed and unmanaged resources used by [SwitchChannel](nationalinstruments-daqmx-switchchannel.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by SwitchChannel; false to release only unmanaged resources used by SwitchChannel. |

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-impedance.html language=enus -->
## TOPIC 02669: Impedance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-impedance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads. SyntaxNamespace: NationalInstruments.DAQmxpublic double Impedance { get; }

### Impedance

Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Impedance { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxaccarrycurrent.html language=enus -->
## TOPIC 02670: MaxACCarryCurrent

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxaccarrycurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxaccarrycurrent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in amperes the maximum AC current that the device can carry. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxACCarryCurrent { get; }

### MaxACCarryCurrent

Indicates in amperes the maximum AC current that the device can carry.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxACCarryCurrent { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxaccarrypower.html language=enus -->
## TOPIC 02671: MaxACCarryPower

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxaccarrypower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxaccarrypower.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in watts the maximum AC power that the device can carry. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxACCarryPower { get; }

### MaxACCarryPower

Indicates in watts the maximum AC power that the device can carry.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxACCarryPower { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxacswitchcurrent.html language=enus -->
## TOPIC 02672: MaxACSwitchCurrent

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxacswitchcurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxacswitchcurrent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxACSwitchCurrent { get; }

### MaxACSwitchCurrent

Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxACSwitchCurrent { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxacswitchpower.html language=enus -->
## TOPIC 02673: MaxACSwitchPower

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxacswitchpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxacswitchpower.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in watts the maximum AC power that the device can switch. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxACSwitchPower { get; }

### MaxACSwitchPower

Indicates in watts the maximum AC power that the device can switch.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxACSwitchPower { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxacvoltage.html language=enus -->
## TOPIC 02674: MaxACVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxacvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxacvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in volts the maximum AC RMS voltage that the device can switch. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxACVoltage { get; }

### MaxACVoltage

Indicates in volts the maximum AC RMS voltage that the device can switch.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxACVoltage { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxdccarrycurrent.html language=enus -->
## TOPIC 02675: MaxDCCarryCurrent

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxdccarrycurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxdccarrycurrent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in amperes the maximum DC current that the device can carry. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxDCCarryCurrent { get; }

### MaxDCCarryCurrent

Indicates in amperes the maximum DC current that the device can carry.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxDCCarryCurrent { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxdccarrypower.html language=enus -->
## TOPIC 02676: MaxDCCarryPower

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxdccarrypower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxdccarrypower.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in watts the maximum DC power that the device can carry. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxDCCarryPower { get; }

### MaxDCCarryPower

Indicates in watts the maximum DC power that the device can carry.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxDCCarryPower { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxdcswitchcurrent.html language=enus -->
## TOPIC 02677: MaxDCSwitchCurrent

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxdcswitchcurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxdcswitchcurrent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxDCSwitchCurrent { get; }

### MaxDCSwitchCurrent

Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxDCSwitchCurrent { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxdcswitchpower.html language=enus -->
## TOPIC 02678: MaxDCSwitchPower

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxdcswitchpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxdcswitchpower.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in watts the maximum DC power that the device can switch. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxDCSwitchPower { get; }

### MaxDCSwitchPower

Indicates in watts the maximum DC power that the device can switch.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxDCSwitchPower { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-maxdcvoltage.html language=enus -->
## TOPIC 02679: MaxDCVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-maxdcvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-maxdcvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in volts the maximum DC voltage that the device can switch. SyntaxNamespace: NationalInstruments.DAQmxpublic double MaxDCVoltage { get; }

### MaxDCVoltage

Indicates in volts the maximum DC voltage that the device can switch.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaxDCVoltage { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-tostring.html language=enus -->
## TOPIC 02680: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-usage.html language=enus -->
## TOPIC 02681: Usage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-usage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-usage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. SyntaxNamespace: NationalInstruments.DAQmxpublic SwitchChannelUsage Usage { get; set; }RemarksSpecifies how you can use the channel.

### Usage

Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SwitchChannelUsage](nationalinstruments-daqmx-switchchannelusage.html) Usage { get; set; }

#### Remarks

Specifies how you can use the channel.

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel-wiremode.html language=enus -->
## TOPIC 02682: WireMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel-wiremode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel-wiremode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of wires that the channel switches. SyntaxNamespace: NationalInstruments.DAQmxpublic long WireMode { get; }

### WireMode

Indicates the number of wires that the channel switches.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long WireMode { get; }

Parent topic:

SwitchChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannel.html language=enus -->
## TOPIC 02683: SwitchChannel Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This type is obsolete. Will warn if used Encapsulates a channel on a switch device and contains properties and methods that operate on switch channels outside the context of a task. This class also defines the intended use of particular switch channels in tasks. Derives fromMarshalByRefObj

### SwitchChannel Class

**Obsolete: This type is obsolete. Will warn if used** 
Encapsulates a channel on a switch device and contains properties and methods that operate on switch channels outside the context of a task. This class also defines the intended use of particular switch channels in tasks.

#### Derives from

- MarshalByRefObject
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SwitchChannel : MarshalByRefObject, IDisposable

#### Remarks

LoadSwitchChannel(string)

Local

DaqSystem

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AnalogBusSharingEnable | Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to true to enable sharing on the channel that connects to the analog bus line. Analog bus sharing is disabled by default. |
| Bandwidth | Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration. |
| Impedance | Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads. |
| MaxACCarryCurrent | Indicates in amperes the maximum AC current that the device can carry. |
| MaxACCarryPower | Indicates in watts the maximum AC power that the device can carry. |
| MaxACSwitchCurrent | Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level. |
| MaxACSwitchPower | Indicates in watts the maximum AC power that the device can switch. |
| MaxACVoltage | Indicates in volts the maximum AC RMS voltage that the device can switch. |
| MaxDCCarryCurrent | Indicates in amperes the maximum DC current that the device can carry. |
| MaxDCCarryPower | Indicates in watts the maximum DC power that the device can carry. |
| MaxDCSwitchCurrent | Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level. |
| MaxDCSwitchPower | Indicates in watts the maximum DC power that the device can switch. |
| MaxDCVoltage | Indicates in volts the maximum DC voltage that the device can switch. |
| Usage | Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. |
| WireMode | Indicates the number of wires that the channel switches. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Releases all resources used by SwitchChannel. |
| ToString() | Returns a string representation of the object. |
| Dispose(bool) | Releases the managed and unmanaged resources used by SwitchChannel or optionally releases only the unmanaged resources. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchchannelusage.html language=enus -->
## TOPIC 02684: SwitchChannelUsage Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchchannelusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchchannelusage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This enum is obsolete. Will warn if used Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SwitchChannelUsageMembersNameValueDescriptio

### SwitchChannelUsage Enumeration

**Obsolete: This enum is obsolete. Will warn if used** 
 Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SwitchChannelUsage

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Source | 10439 | You can use the channel only as an input for a signal. |
| Load | 10440 | You can use the channel only as the output for a signal passing through the switch. |
| ReservedForRouting | 10441 | You can use the channel only to complete routes within a switch. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchpathstatus.html language=enus -->
## TOPIC 02685: SwitchPathStatus Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchpathstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchpathstatus.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This enum is obsolete. Will warn if used Specifies the status of the requested path. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SwitchPathStatusMembersNameValueDescriptionPathAvailable10431A path is available between the channels. PathAlreadyExists10432The channels are already c

### SwitchPathStatus Enumeration

**Obsolete: This enum is obsolete. Will warn if used** 
Specifies the status of the requested path.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SwitchPathStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PathAvailable | 10431 | A path is available between the channels. |
| PathAlreadyExists | 10432 | The channels are already connected. |
| PathUnsupported | 10433 | No path is available between the channels. You might need to reserve more channels for routing to create an available path. |
| ChannelInUse | 10434 | The path between the two endpoints is unavailable because another connection is already using a channel needed for routing. |
| SourceChannelConflict | 10435 | No path is available between the two channels because connecting the channels would directly or indirectly connect two source channels. |
| ChannelReservedForRouting | 10436 | One of the endpoint channels is reserved for routing. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchrelayposition.html language=enus -->
## TOPIC 02686: SwitchRelayPosition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchrelayposition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchrelayposition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This enum is obsolete. Will warn if used Specifies the position of each specified relay. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SwitchRelayPositionMembersNameValueDescriptionOpen10437The relay is open. Closed10438The relay is closed.

### SwitchRelayPosition Enumeration

**Obsolete: This enum is obsolete. Will warn if used** 
Specifies the position of each specified relay.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SwitchRelayPosition

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Open | 10437 | The relay is open. |
| Closed | 10438 | The relay is closed. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchscan-breakmode.html language=enus -->
## TOPIC 02687: BreakMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchscan-breakmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchscan-breakmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take between each entry in a scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic SwitchScanBreakMode BreakMode { get; set; }

### BreakMode

Specifies the action to take between each entry in a scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SwitchScanBreakMode](nationalinstruments-daqmx-switchscanbreakmode.html) BreakMode { get; set; }

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchscan-iswaitingforadvance.html language=enus -->
## TOPIC 02688: IsWaitingForAdvance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchscan-iswaitingforadvance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchscan-iswaitingforadvance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic bool IsWaitingForAdvance { get; }

### IsWaitingForAdvance

Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsWaitingForAdvance { get; }

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchscan-repeatmode.html language=enus -->
## TOPIC 02689: RepeatMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchscan-repeatmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchscan-repeatmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the task advances through the scan list multiple times. SyntaxNamespace: NationalInstruments.DAQmxpublic SwitchScanRepeatMode RepeatMode { get; set; }

### RepeatMode

Specifies if the task advances through the scan list multiple times.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SwitchScanRepeatMode](nationalinstruments-daqmx-switchscanrepeatmode.html) RepeatMode { get; set; }

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchscan-tostring.html language=enus -->
## TOPIC 02690: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchscan-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchscan-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

SwitchScan Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchscan.html language=enus -->
## TOPIC 02691: SwitchScan Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchscan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchscan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This type is obsolete. Will warn if used Contains properties for a switch scan list. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class SwitchScan : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample applications are located i

### SwitchScan Class

**Obsolete: This type is obsolete. Will warn if used** 
Contains properties for a [switch scan list](/csh?context=nidaqmx_mxcncpts_switchscanning).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class SwitchScan : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| BreakMode | Specifies the action to take between each entry in a scan list. |
| IsWaitingForAdvance | Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list. |
| RepeatMode | Specifies if the task advances through the scan list multiple times. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- SwitchScan

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchscanbreakmode.html language=enus -->
## TOPIC 02692: SwitchScanBreakMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchscanbreakmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchscanbreakmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This enum is obsolete. Will warn if used Specifies the action to take between each entry in a scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SwitchScanBreakModeMembersNameValueDescriptionNoAction10227When advancing to the next entry in the scan list, leave all previous co

### SwitchScanBreakMode Enumeration

**Obsolete: This enum is obsolete. Will warn if used** 
 Specifies the action to take between each entry in a scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SwitchScanBreakMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NoAction | 10227 | When advancing to the next entry in the scan list, leave all previous connections intact. |
| BreakBeforeMake | 10110 | When advancing to the next entry in the scan list, disconnect all previous connections before making any new connections. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-switchscanrepeatmode.html language=enus -->
## TOPIC 02693: SwitchScanRepeatMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-switchscanrepeatmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-switchscanrepeatmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This enum is obsolete. Will warn if used Specifies if the task advances through the scan list multiple times. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SwitchScanRepeatModeMembersNameValueDescriptionFinite10172The task advances through the scan list one time only. NI-DAQmx igno

### SwitchScanRepeatMode Enumeration

**Obsolete: This enum is obsolete. Will warn if used** 
 Specifies if the task advances through the scan list multiple times.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SwitchScanRepeatMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Finite | 10172 | The task advances through the scan list one time only. NI-DAQmx ignores any Advance Triggers after completing the scan list. |
| Continuous | 10117 | The task returns to the beginning of the scan list when it reaches the end of the scan list. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-synchronizationpulsetimescale.html language=enus -->
## TOPIC 02694: SynchronizationPulseTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-synchronizationpulsetimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-synchronizationpulsetimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timescale to be used for timestamps for a sync pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SynchronizationPulseTimescaleRemarksSpecifies the timescale to be used for timestamps for a sync pulse. Use this enumeration to get or set the value of SynchronizationPulseTimesc

### SynchronizationPulseTimescale Enumeration

Specifies the timescale to be used for timestamps for a sync pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SynchronizationPulseTimescale

#### Remarks

Specifies the timescale to be used for timestamps for a sync pulse. Use this enumeration to get or set the value of [SynchronizationPulseTimescale](nationalinstruments-daqmx-timing-synchronizationpulsetimescale.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HostTime | 16126 | Use the host device. |
| IODeviceTime | 16127 | Use the I/O device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-synchronizationpulsetype.html language=enus -->
## TOPIC 02695: SynchronizationPulseType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-synchronizationpulsetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-synchronizationpulsetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of sync pulse used in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum SynchronizationPulseTypeRemarksSpecifies the type of sync pulse used in the task. Use this enumeration to get or set the value of SynchronizationPulseType.MembersNameValueDescriptionOnboard16128U

### SynchronizationPulseType Enumeration

Specifies the type of sync pulse used in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum SynchronizationPulseType

#### Remarks

Specifies the type of sync pulse used in the task. Use this enumeration to get or set the value of [SynchronizationPulseType](nationalinstruments-daqmx-timing-synchronizationpulsetype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Onboard | 16128 | Use the synchronization pulse type specified by the device. |
| DigitalEdge | 10150 | Digital Edge synchronization. |
| Time | 15996 | Time synchronization. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-tablescale-prescaledvalues.html language=enus -->
## TOPIC 02696: PreScaledValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-tablescale-prescaledvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-tablescale-prescaledvalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of pre-scaled values. These values map directly to the values in ScaledValues. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] PreScaledValues { get; set; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it c

### PreScaledValues

Specifies an array of pre-scaled values. These values map directly to the values in [ScaledValues](nationalinstruments-daqmx-tablescale-scaledvalues.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] PreScaledValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

TableScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-tablescale-scaledvalues.html language=enus -->
## TOPIC 02697: ScaledValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-tablescale-scaledvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-tablescale-scaledvalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of scaled values. These values map directly to the values in PreScaledValues. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] ScaledValues { get; set; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creat

### ScaledValues

Specifies an array of scaled values. These values map directly to the values in [PreScaledValues](nationalinstruments-daqmx-tablescale-prescaledvalues.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] ScaledValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

TableScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-tablescale-tablescale__string-double_arr1-double_arr1.html language=enus -->
## TOPIC 02698: TableScale(string, double[], double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-tablescale-tablescale__string-double_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-tablescale-tablescale__string-double_arr1-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the TableScale class with the specified scaled and prescaled values. SyntaxNamespace: NationalInstruments.DAQmxpublic TableScale(string name, double[] preScaledValues, double[] scaledValues)ParametersNameTypeDescriptionnamestringThe name of the custom scale for later use, s

### TableScale(string, double[], double[])

Creates a new instance of the [TableScale](nationalinstruments-daqmx-tablescale.html) class with the specified scaled and prescaled values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public TableScale(string name, double[] preScaledValues, double[] scaledValues)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the custom scale for later use, such as when you create a virtual channel. |
| preScaledValues | double[] | An array of prescaled values that map to the scaled values in scaledValues . |
| scaledValues | double[] | An array of scaled values that map to the prescaled values in prescaledValues . |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

TableScale Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-tablescale.html language=enus -->
## TOPIC 02699: TableScale Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-tablescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-tablescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a custom scale that maps an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally. Derives fromScaleSyntaxNamespace: NationalInstruments.DAQmxpublic class TableScale : ScaleRemarksThe following example explains how to update th

### TableScale Class

Encapsulates a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) that maps an array of prescaled values to an array of corresponding scaled values, with all other values scaled proportionally.

#### Derives from

- Scale

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class TableScale : Scale

#### Remarks

The following example explains how to update the [PreScaledValues](nationalinstruments-daqmx-tablescale-prescaledvalues.html) property that returns an array:

```text
Dim preScaledValues As Double() = New Double() {0.11, 0.12, 0.13}Dim scaledValues As Double() = New Double() {1.1, 1.2, 1.3}Dim tablescale As New TableScale("DAQmxTableScale", preScaledValues, scaledValues)' To update the value at specific index in tablescale.PreScaledValues' change the source array and assign it back to the property.preScaledValues(0) = 0.1tablescale.PreScaledValues = preScaledValues
```

```text
double[] preScaledValues = new double[] { .11, .12, .13 };double[] scaledValues = new double[] { 1.1, 1.2, 1.3 };TableScale tablescale = new TableScale("DAQmxTableScale", preScaledValues, scaledValues);// To update the value at specific index in tablescale.PreScaledValues// change the source array and assign it back to the property.preScaledValues[0] = 0.1;tablescale.PreScaledValues = preScaledValues;
```

The following example explains how to update the [ScaledValues](nationalinstruments-daqmx-tablescale-scaledvalues.html) property that returns an array:

```text
Dim preScaledValues As Double() = New Double() {0.11, 0.12, 0.13}Dim scaledValues As Double() = New Double() {1.1, 1.2, 1.3}Dim tablescale As New TableScale("DAQmxTableScale", preScaledValues, scaledValues)' To update the value at specific index in tablescale.ScaledValues' change the source array and assign it back to the property.scaledValues(0) = 1.12tablescale.ScaledValues = scaledValues
```

```text
double[] preScaledValues = new double[] { .11, .12, .13 };double[] scaledValues = new double[] { 1.1, 1.2, 1.3 };TableScale tablescale = new TableScale("DAQmxTableScale", preScaledValues, scaledValues);// To update the value at specific index in tablescale.ScaledValues// change the source array and assign it back to the property.scaledValues[0] = 1.12;tablescale.ScaledValues = scaledValues;
```

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| TableScale(string, double[], double[]) | Creates a new instance of the TableScale class with the specified scaled and prescaled values. |

#### Properties

| Name | Description |
| --- | --- |
| PreScaledValues | Specifies an array of pre-scaled values. These values map directly to the values in ScaledValues. |
| ScaledValues | Specifies an array of scaled values. These values map directly to the values in PreScaledValues. |

#### See Also

- LoadScale(string)

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-accessoryinsertionorremovaldetected.html language=enus -->
## TOPIC 02700: AccessoryInsertionOrRemovalDetected

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-accessoryinsertionorremovaldetected.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-accessoryinsertionorremovaldetected.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if any devices in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevicesWithInsertedOrRemovedAccessories. Otherwise, you wi

### AccessoryInsertionOrRemovalDetected

Indicates if any devices in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read [DevicesWithInsertedOrRemovedAccessories](nationalinstruments-daqmx-task-deviceswithinsertedorremovedaccessories.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AccessoryInsertionOrRemovalDetected { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-addglobalchannel__string.html language=enus -->
## TOPIC 02701: AddGlobalChannel(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-addglobalchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-addglobalchannel__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a preconfigured, global channel to the task. SyntaxNamespace: NationalInstruments.DAQmxpublic Channel AddGlobalChannel(string channelName)RemarksA task can contain global or local channels. Global channels are accessible to all tasks on the system. Local channels are accessible only to the task

### AddGlobalChannel(string)

Adds a preconfigured, global channel to the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Channel](nationalinstruments-daqmx-channel.html) AddGlobalChannel(string channelName)

#### Remarks

A task can contain global or local channels. Global channels are accessible to all tasks on the system. Local channels are accessible only to the task you use to create them.

Use local channels in a typical application. Use the create channel methods on [AIChannels](nationalinstruments-daqmx-task-aichannels.html), [AOChannels](nationalinstruments-daqmx-task-aochannels.html), [DIChannels](nationalinstruments-daqmx-task-dichannels.html), [DOChannels](nationalinstruments-daqmx-task-dochannels.html), [CIChannels](nationalinstruments-daqmx-task-cichannels.html), or [COChannels](nationalinstruments-daqmx-task-cochannels.html) to create local channels and add them to the task. Use Measurement & Automation Explorer (MAX) to create, configure, and store global channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | The name of the global channel to add to the task. |

#### Returns

The global [Channel](nationalinstruments-daqmx-channel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- AIChannels
- AOChannels
- DIChannels
- DOChannels
- CIChannels
- COChannels

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-aichannels.html language=enus -->
## TOPIC 02702: AIChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-aichannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-aichannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the collection of analog input channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannelCollection AIChannels { get; }RemarksAn AIChannelCollection that contains the AIChannel objects in the task. Each task can contain only one type of channel. You must use the channels p

### AIChannels

Gets the collection of analog input channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html) AIChannels { get; }

#### Remarks

An [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html) that contains the [AIChannel](nationalinstruments-daqmx-aichannel.html) objects in the task.

Each task can contain only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

#### See Also

- AIChannelCollection
- AOChannels
- DIChannels
- DOChannels
- CIChannels
- COChannels

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-aochannels.html language=enus -->
## TOPIC 02703: AOChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-aochannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-aochannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the collection of analog output channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic AOChannelCollection AOChannels { get; }RemarksAn AIChannelCollection that contains the AOChannel objects in the task. Each task can contain only one type of channel. You must use the channels

### AOChannels

Gets the collection of analog output channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOChannelCollection](nationalinstruments-daqmx-aochannelcollection.html) AOChannels { get; }

#### Remarks

An [AIChannelCollection](nationalinstruments-daqmx-aichannelcollection.html) that contains the [AOChannel](nationalinstruments-daqmx-aochannel.html) objects in the task.

Each task can contain only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

#### See Also

- AIChannelCollection
- AIChannels
- DIChannels
- DOChannels
- CIChannels
- COChannels

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-cichannels.html language=enus -->
## TOPIC 02704: CIChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-cichannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-cichannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the collection of counter input channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIChannelCollection CIChannels { get; }RemarksA CIChannelCollection that contains the CIChannel objects in the task. Each task can contain only one type of channel. You must use the channels p

### CIChannels

Gets the collection of counter input channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIChannelCollection](nationalinstruments-daqmx-cichannelcollection.html) CIChannels { get; }

#### Remarks

A [CIChannelCollection](nationalinstruments-daqmx-cichannelcollection.html) that contains the [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in the task.

Each task can contain only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

#### See Also

- CIChannelCollection
- AIChannels
- AOChannels
- DIChannels
- DOChannels
- COChannels

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-cochannels.html language=enus -->
## TOPIC 02705: COChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-cochannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-cochannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the collection of counter output channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic COChannelCollection COChannels { get; }RemarksA COChannelCollection that contains the COChannel objects in the task. Each task can contain only one type of channel. You must use the channels

### COChannels

Gets the collection of counter output channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [COChannelCollection](nationalinstruments-daqmx-cochannelcollection.html) COChannels { get; }

#### Remarks

A [COChannelCollection](nationalinstruments-daqmx-cochannelcollection.html) that contains the [COChannel](nationalinstruments-daqmx-cochannel.html) objects in the task.

Each task can contain only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

#### See Also

- COChannelCollection
- AIChannels
- AOChannels
- DIChannels
- DOChannels
- CIChannels

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-configurelogging__string-tdmsloggingoperation-loggingmode-string.html language=enus -->
## TOPIC 02706: ConfigureLogging(string, TdmsLoggingOperation, LoggingMode, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-configurelogging__string-tdmsloggingoperation-loggingmode-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-configurelogging__string-tdmsloggingoperation-loggingmode-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures logging to a .tdms file when the acquisition starts with the specified TDMS channel group name. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureLogging(string filePath, TdmsLoggingOperation loggingOperation, LoggingMode loggingMode, string groupName)RemarksWhen you enable T

### ConfigureLogging(string, TdmsLoggingOperation, LoggingMode, string)

Configures logging to a .tdms file when the acquisition starts with the specified TDMS channel group name.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureLogging(string filePath, TdmsLoggingOperation loggingOperation, LoggingMode loggingMode, string groupName)

#### Remarks

When you enable TDMS logging, NI-DAQmx streams the data acquired to the specified file once the acquisition starts. The data written on the file is in TDMS file format, and the driver also creates a TDMS index file. Refer to [TDMS Streaming](/csh?context=nidaqmx_mxcncpts_datalogging) for more information.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path to the .tdms file to which you want to log data. If you use this method to create a new file, the file extension of the filename you specify in filePath must be .tdms. Otherwise, this method automatically appends .tdms to the filename you specify. If you use this method to open or update an existing file, you do not have to ensure that the file extension is .tdms. |
| loggingOperation | TdmsLoggingOperation | A TdmsLoggingOperation value which specifies how to open the .tdms file. |
| loggingMode | LoggingMode | A LoggingMode value which specifies how to log data. |
| groupName | string | The name of the channel group to create within the .tdms file for data from this task. When set to null, Empty, or a string with only white space, the driver sets the TDMS channel group name to the task name. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-configurelogging__string-tdmsloggingoperation-loggingmode.html language=enus -->
## TOPIC 02707: ConfigureLogging(string, TdmsLoggingOperation, LoggingMode)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-configurelogging__string-tdmsloggingoperation-loggingmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-configurelogging__string-tdmsloggingoperation-loggingmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures logging to a .tdms file when the acquisition starts. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureLogging(string filePath, TdmsLoggingOperation loggingOperation, LoggingMode loggingMode)RemarksWhen you enable TDMS logging, NI-DAQmx streams the data acquired to the specif

### ConfigureLogging(string, TdmsLoggingOperation, LoggingMode)

Configures logging to a .tdms file when the acquisition starts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureLogging(string filePath, TdmsLoggingOperation loggingOperation, LoggingMode loggingMode)

#### Remarks

When you enable TDMS logging, NI-DAQmx streams the data acquired to the specified file once the acquisition starts. The data written on the file is in TDMS file format, and the driver also creates a TDMS index file. The name of the TDMS channel group that the driver creates is the same as the task name. Refer to [TDMS Streaming](/csh?context=nidaqmx_mxcncpts_datalogging) for more information.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path to the .tdms file to which you want to log data. If you use this method to create a new file, the file extension of the filename you specify in filePath must be .tdms. Otherwise, this method automatically appends .tdms to the filename you specify. If you use this method to open or update an existing file, you do not have to ensure that the file extension is .tdms. |
| loggingOperation | TdmsLoggingOperation | A TdmsLoggingOperation value that specifies how to open the .tdms file. |
| loggingMode | LoggingMode | A LoggingMode value that specifies how to log data. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-control__taskaction.html language=enus -->
## TOPIC 02708: Control(TaskAction)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-control__taskaction.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-control__taskaction.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Alters the state of the task according to the mode you specify. SyntaxNamespace: NationalInstruments.DAQmxpublic void Control(TaskAction mode)RemarksTo start a task more quickly, set mode to Commit to program the hardware with all parameters of the task prior to starting it.If the task is in the run

### Control(TaskAction)

Alters the [state](/csh?context=nidaqmx_mxcncpts_taskstatemodel) of the task according to the mode you specify.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Control(TaskAction mode)

#### Remarks

To start a task more quickly, set *mode*  to [Commit](nationalinstruments-daqmx-taskaction.html) to program the hardware with all parameters of the task prior to starting it.

If the task is in the running state and an asynchronous read or write on the task is in progress, calling Control(TaskAction) to move the task out of the running state does not return until the data from the pending read or write has been transferred to or from the task buffer. However, if *mode*  is [Abort](nationalinstruments-daqmx-taskaction.html), then Control(TaskAction) does not wait for the asynchronous read or write callback methods to finish. The pending asynchronous call stops immediately and raises a [DaqException](nationalinstruments-daqmx-daqexception.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| mode | TaskAction | The action to use to alter the state of the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- TaskAction

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-counteroutput.html language=enus -->
## TOPIC 02709: CounterOutput

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-counteroutput.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-counteroutput.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when any of the counters used in the task reaches its terminal count. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterOutputEventHandler CounterOutputRemarksFor more information about events in NI-DAQmx, refer to Events.EventsExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExcep

### CounterOutput

Occurs when any of the counters used in the task reaches its terminal count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CounterOutputEventHandler](nationalinstruments-daqmx-counteroutputeventhandler__object-counteroutputeventargs.html) CounterOutput

#### Remarks

For more information about events in NI-DAQmx, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-devices.html language=enus -->
## TOPIC 02710: Devices

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-devices.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of all devices in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] Devices { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loo

### Devices

Indicates an array containing the names of all devices in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] Devices { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-deviceswithinsertedorremovedaccessories.html language=enus -->
## TOPIC 02711: DevicesWithInsertedOrRemovedAccessories

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-deviceswithinsertedorremovedaccessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-deviceswithinsertedorremovedaccessories.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] DevicesWi

### DevicesWithInsertedOrRemovedAccessories

Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read [AccessoryInsertionOrRemovalDetected](nationalinstruments-daqmx-task-accessoryinsertionorremovaldetected.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] DevicesWithInsertedOrRemovedAccessories { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-dichannels.html language=enus -->
## TOPIC 02712: DIChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-dichannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-dichannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the collection of digital input channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic DIChannelCollection DIChannels { get; }RemarksA DIChannelCollection that contains the DIChannel objects in the task. Each task can contain only one type of channel. You must use the channels p

### DIChannels

Gets the collection of digital input channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIChannelCollection](nationalinstruments-daqmx-dichannelcollection.html) DIChannels { get; }

#### Remarks

A [DIChannelCollection](nationalinstruments-daqmx-dichannelcollection.html) that contains the [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in the task.

Each task can contain only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

#### See Also

- DIChannelCollection
- AIChannels
- AOChannels
- DOChannels
- CIChannels
- COChannels

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-digitalchangedetection.html language=enus -->
## TOPIC 02713: DigitalChangeDetection

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-digitalchangedetection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-digitalchangedetection.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when a digital change is detected on any of the digital lines used in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalChangeDetectionEventHandler DigitalChangeDetectionRemarksFor more information about events in NI-DAQmx, refer to Events.EventsExceptionsTypeDescriptionNation

### DigitalChangeDetection

Occurs when a digital change is detected on any of the digital lines used in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalChangeDetectionEventHandler](nationalinstruments-daqmx-digitalchangedetectioneventhandler__object-digitalchangedetectioneventargs.html) DigitalChangeDetection

#### Remarks

For more information about events in NI-DAQmx, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-dispose.html language=enus -->
## TOPIC 02714: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by Task. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Dispose()

Releases all resources used by [Task](nationalinstruments-daqmx-task.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-dispose__bool.html language=enus -->
## TOPIC 02715: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by Task or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on implementing

### Dispose(bool)

Releases the managed and unmanaged resources used by [Task](nationalinstruments-daqmx-task.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by SwitchChannel; false to release only unmanaged resources used by SwitchChannel. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-dochannels.html language=enus -->
## TOPIC 02716: DOChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-dochannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-dochannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the collection of digital output channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic DOChannelCollection DOChannels { get; }RemarksAn DOChannelCollection that contains the DOChannel objects in the task. Each task can contain only one type of channel. You must use the channels

### DOChannels

Gets the collection of digital output channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DOChannelCollection](nationalinstruments-daqmx-dochannelcollection.html) DOChannels { get; }

#### Remarks

An [DOChannelCollection](nationalinstruments-daqmx-dochannelcollection.html) that contains the [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in the task.

Each task can contain only one type of channel. You must use the channels property that corresponds to the type of channels in the task to access the channels in the task.

#### See Also

- DOChannelCollection
- AIChannels
- AOChannels
- DIChannels
- CIChannels
- COChannels

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-done.html language=enus -->
## TOPIC 02717: Done

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-done.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-done.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when the task completes. SyntaxNamespace: NationalInstruments.DAQmxpublic TaskDoneEventHandler DoneRemarksThis event occurs whether the task completed successfully or stopped prematurely due to an error. If the task stops due to a call to Stop or Control(TaskAction), this event does not occur

### Done

Occurs when the task completes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TaskDoneEventHandler](nationalinstruments-daqmx-taskdoneeventhandler__object-taskdoneeventargs.html) Done

#### Remarks

Stop

Control(TaskAction)

Note

For more information about events in NI-DAQmx, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-everynsamplesread.html language=enus -->
## TOPIC 02718: EveryNSamplesRead

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-everynsamplesread.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-everynsamplesread.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when N number of samples per channel, as defined by EveryNSamplesReadEventInterval, is written from the device to the PC buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic EveryNSamplesReadEventHandler EveryNSamplesReadRemarksYou must set EveryNSamplesReadEventInterval to a value greate

### EveryNSamplesRead

Occurs when N number of samples per channel, as defined by [EveryNSamplesReadEventInterval](nationalinstruments-daqmx-task-everynsamplesreadeventinterval.html), is written from the device to the PC buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [EveryNSamplesReadEventHandler](nationalinstruments-daqmx-everynsamplesreadeventhandler__object-everynsamplesreadeventargs.html) EveryNSamplesRead

#### Remarks

You must set [EveryNSamplesReadEventInterval](nationalinstruments-daqmx-task-everynsamplesreadeventinterval.html) to a value greater than zero before registering this event.

Note

For more information about events in NI-DAQmx, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- EveryNSamplesReadEventInterval

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-everynsamplesreadeventinterval.html language=enus -->
## TOPIC 02719: EveryNSamplesReadEventInterval

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-everynsamplesreadeventinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-everynsamplesreadeventinterval.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the interval, in number of samples per channel, at which EveryNSamplesRead is called. SyntaxNamespace: NationalInstruments.DAQmxpublic int EveryNSamplesReadEventInterval { get; set; }RemarksThe interval, in number of samples per channel.If this property is set to zero, registering the E

### EveryNSamplesReadEventInterval

Gets or sets the interval, in number of samples per channel, at which [EveryNSamplesRead](nationalinstruments-daqmx-task-everynsamplesread.html) is called.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int EveryNSamplesReadEventInterval { get; set; }

#### Remarks

The interval, in number of samples per channel.

If this property is set to zero, registering the [EveryNSamplesRead](nationalinstruments-daqmx-task-everynsamplesread.html) event is not successful.

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-everynsampleswritten.html language=enus -->
## TOPIC 02720: EveryNSamplesWritten

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-everynsampleswritten.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-everynsampleswritten.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when N number of samples per channel, as defined by EveryNSamplesWrittenEventInterval, have been written from the PC buffer to the device. SyntaxNamespace: NationalInstruments.DAQmxpublic EveryNSamplesWrittenEventHandler EveryNSamplesWrittenRemarksYou must set EveryNSamplesWrittenEventInterva

### EveryNSamplesWritten

Occurs when N number of samples per channel, as defined by [EveryNSamplesWrittenEventInterval](nationalinstruments-daqmx-task-everynsampleswritteneventinterval.html), have been written from the PC buffer to the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [EveryNSamplesWrittenEventHandler](nationalinstruments-daqmx-everynsampleswritteneventhandler__object-everynsampleswritteneventargs.html) EveryNSamplesWritten

#### Remarks

You must set [EveryNSamplesWrittenEventInterval](nationalinstruments-daqmx-task-everynsampleswritteneventinterval.html) to a value greater than zero before registering this event.

Note

For more information about events in NI-DAQmx, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- EveryNSamplesWrittenEventInterval

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-everynsampleswritteneventinterval.html language=enus -->
## TOPIC 02721: EveryNSamplesWrittenEventInterval

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-everynsampleswritteneventinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-everynsampleswritteneventinterval.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the interval, in number of samples per channel, at which EveryNSamplesWritten is called. SyntaxNamespace: NationalInstruments.DAQmxpublic int EveryNSamplesWrittenEventInterval { get; set; }RemarksThe interval, in number of samples.If this property is set to zero, registering the EveryNS

### EveryNSamplesWrittenEventInterval

Gets or sets the interval, in number of samples per channel, at which [EveryNSamplesWritten](nationalinstruments-daqmx-task-everynsampleswritten.html) is called.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int EveryNSamplesWrittenEventInterval { get; set; }

#### Remarks

The interval, in number of samples.

If this property is set to zero, registering the [EveryNSamplesWritten](nationalinstruments-daqmx-task-everynsampleswritten.html) event is not successful.

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-exportsignals.html language=enus -->
## TOPIC 02722: ExportSignals

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-exportsignals.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-exportsignals.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the exported signal configuration for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic ExportSignals ExportSignals { get; }RemarksThe ExportSignals for the task.

### ExportSignals

Gets the exported signal configuration for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ExportSignals](nationalinstruments-daqmx-exportsignals.html) ExportSignals { get; }

#### Remarks

The [ExportSignals](nationalinstruments-daqmx-exportsignals.html) for the task.

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-isdone.html language=enus -->
## TOPIC 02723: IsDone

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-isdone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-isdone.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the task completed execution. SyntaxNamespace: NationalInstruments.DAQmxpublic bool IsDone { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### IsDone

Indicates whether the task [completed execution](/csh?context=nidaqmx_mxcncpts_whentaskdone).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsDone { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-name.html language=enus -->
## TOPIC 02724: Name

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-name.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the task. SyntaxNamespace: NationalInstruments.DAQmxpublic string Name { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Name

Indicates the name of the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Name { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-sampleclock.html language=enus -->
## TOPIC 02725: SampleClock

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-sampleclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-sampleclock.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs on each pulse of the task's sample clock. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleClockEventHandler SampleClockRemarksFor more information about events in NI-DAQmx, refer to Events.EventsExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned

### SampleClock

Occurs on each pulse of the task's sample clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleClockEventHandler](nationalinstruments-daqmx-sampleclockeventhandler__object-sampleclockeventargs.html) SampleClock

#### Remarks

For more information about events in NI-DAQmx, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-samplecomplete.html language=enus -->
## TOPIC 02726: SampleComplete

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-samplecomplete.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-samplecomplete.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when each sample is acquired into the NI-DAQmx driver buffer and is ready for reading. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleCompleteEventHandler SampleCompleteRemarksFor more information about events in NI-DAQmx, refer to Events.EventsExceptionsTypeDescriptionNationalInstrum

### SampleComplete

Occurs when each sample is acquired into the NI-DAQmx driver buffer and is ready for reading.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleCompleteEventHandler](nationalinstruments-daqmx-samplecompleteeventhandler__object-samplecompleteeventargs.html) SampleComplete

#### Remarks

For more information about events in NI-DAQmx, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-start.html language=enus -->
## TOPIC 02727: Start()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-start.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-start.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transitions the task to the running state, which begins the measurement or generation. SyntaxNamespace: NationalInstruments.DAQmxpublic void Start()RemarksIf you do not use this method, a measurement task starts automatically when you call a read method. How you set the write method autoStart parame

### Start()

Transitions the task to the running [state](/csh?context=nidaqmx_mxcncpts_taskstatemodel), which begins the measurement or generation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Start()

#### Remarks

If you do not use this method, a measurement task starts automatically when you call a read method. How you set the write method *autoStart*  parameter determines if calling the write method automatically starts a generation task. If you do not use Start and [Stop](nationalinstruments-daqmx-task-stop.html) when you use a read or write method multiple times, the task starts and stops repeatedly, which reduces the performance of the application. Refer to [When Should You Use the Start Function](/csh?context=nidaqmx_mxcncpts_startfunction) for more information.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- AnalogSingleChannelReader
- AnalogMultiChannelReader
- DigitalSingleChannelReader
- DigitalMultiChannelReader
- CounterSingleChannelReader
- CounterMultiChannelReader
- AnalogUnscaledReader
- AnalogSingleChannelWriter
- AnalogMultiChannelWriter
- DigitalSingleChannelWriter
- DigitalMultiChannelWriter
- AnalogUnscaledWriter

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-startnewfile__string.html language=enus -->
## TOPIC 02728: StartNewFile(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-startnewfile__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-startnewfile__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts a new TDMS file the next time data is written to disk. SyntaxNamespace: NationalInstruments.DAQmxpublic void StartNewFile(string filePath)ParametersNameTypeDescriptionfilePathstringThe path to the TDMS file to which you want to log data.

### StartNewFile(string)

Starts a new TDMS file the next time data is written to disk.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void StartNewFile(string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path to the TDMS file to which you want to log data. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-stop.html language=enus -->
## TOPIC 02729: Stop()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-stop.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transitions the task from the running to the committed state, which ends the measurement or generation. SyntaxNamespace: NationalInstruments.DAQmxpublic void Stop()RemarksIf you do not use this method, the read method ends a measurement task automatically before returning. How you set the autoStart

### Stop()

Transitions the task from the running to the committed [state](/csh?context=nidaqmx_mxcncpts_taskstatemodel), which ends the measurement or generation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Stop()

#### Remarks

If you do not use this method, the read method ends a measurement task automatically before returning. How you set the *autoStart*  parameter of the write method determines if calling the write method automatically ends a generation task before returning. If you do not use [Start](nationalinstruments-daqmx-task-start.html) and Stop when you use a read or write method multiple times, the task starts and stops repeatedly, which reduces the performance of the application.

If an asynchronous read or write on the task is in progress, Stop does not return until the data from the pending read or write has been transferred to or from the task buffer. Stop does not wait for read or write asynchronous callback methods to finish, however.

You may pass [Abort](nationalinstruments-daqmx-taskaction.html) to the [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) method stop the task immediately, without waiting for any currently running operation to complete.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- AnalogSingleChannelReader
- AnalogMultiChannelReader
- DigitalSingleChannelReader
- DigitalMultiChannelReader
- CounterSingleChannelReader
- CounterMultiChannelReader
- AnalogUnscaledReader
- AnalogSingleChannelWriter
- AnalogMultiChannelWriter
- DigitalSingleChannelWriter
- DigitalMultiChannelWriter
- AnalogUnscaledWriter

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-stream.html language=enus -->
## TOPIC 02730: Stream

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-stream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stream for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqStream Stream { get; }RemarksThe DaqStream for the task.

### Stream

Gets the stream for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DaqStream](nationalinstruments-daqmx-daqstream.html) Stream { get; }

#### Remarks

The [DaqStream](nationalinstruments-daqmx-daqstream.html) for the task.

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-switchscan.html language=enus -->
## TOPIC 02731: SwitchScan

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-switchscan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-switchscan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the switch scan configuration for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic SwitchScan SwitchScan { get; }RemarksThe SwitchScan for the task.

### SwitchScan

Gets the switch scan configuration for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SwitchScan](nationalinstruments-daqmx-switchscan.html) SwitchScan { get; }

#### Remarks

The [SwitchScan](nationalinstruments-daqmx-switchscan.html) for the task.

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-synchronizecallbacks.html language=enus -->
## TOPIC 02732: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-synchronizingobject.html language=enus -->
## TOPIC 02733: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set;

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Control

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries. For more information about the effects and purpose of SynchronizingObject, refer to [Events](https://#).

Events

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-task.html language=enus -->
## TOPIC 02734: Task()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-task.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-task.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the Task class with a unique name. SyntaxNamespace: NationalInstruments.DAQmxpublic Task()RemarksThis constructor creates a new task in the current process. To load a task from Measurement & Automation Explorer (MAX), use the LoadTask(string) method on the Local instanc

### Task()

Initializes a new instance of the [Task](nationalinstruments-daqmx-task.html) class with a unique name.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public Task()

#### Remarks

This constructor creates a new task in the current process. To load a task from Measurement & Automation Explorer (MAX), use the [LoadTask(string)](nationalinstruments-daqmx-daqsystem-loadtask__string.html) method on the [Local](nationalinstruments-daqmx-daqsystem-local.html) instance of [DaqSystem](nationalinstruments-daqmx-daqsystem.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-task__string.html language=enus -->
## TOPIC 02735: Task(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-task__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-task__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the Task class with the specified name. SyntaxNamespace: NationalInstruments.DAQmxpublic Task(string name)RemarksThis constructor creates a new task in the current process. To load a task from Measurement & Automation Explorer (MAX), use the LoadTask(string) method on t

### Task(string)

Initializes a new instance of the [Task](nationalinstruments-daqmx-task.html) class with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public Task(string name)

#### Remarks

This constructor creates a new task in the current process. To load a task from Measurement & Automation Explorer (MAX), use the [LoadTask(string)](nationalinstruments-daqmx-daqsystem-loadtask__string.html) method on the [Local](nationalinstruments-daqmx-daqsystem-local.html) instance of [DaqSystem](nationalinstruments-daqmx-daqsystem.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the task to create. If you specify Empty or null, the NI-DAQmx driver assigns a unique name to the new task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-timing.html language=enus -->
## TOPIC 02736: Timing

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-timing.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the timing configurations for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic Timing Timing { get; }RemarksThe Timing for the task.See AlsoTiming

### Timing

Gets the timing configurations for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Timing](nationalinstruments-daqmx-timing.html) Timing { get; }

#### Remarks

The [Timing](nationalinstruments-daqmx-timing.html) for the task.

#### See Also

- Timing

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-tostring.html language=enus -->
## TOPIC 02737: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-triggers.html language=enus -->
## TOPIC 02738: Triggers

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-triggers.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the triggers for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic Triggers Triggers { get; }RemarksThe Triggers for the task.See AlsoTriggers

### Triggers

Gets the triggers for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Triggers](nationalinstruments-daqmx-triggers.html) Triggers { get; }

#### Remarks

The [Triggers](nationalinstruments-daqmx-triggers.html) for the task.

#### See Also

- Triggers

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-waitforvalidtimestamp__timestampevent-timespan.html language=enus -->
## TOPIC 02739: WaitForValidTimestamp(TimestampEvent, TimeSpan)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-waitforvalidtimestamp__timestampevent-timespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-waitforvalidtimestamp__timestampevent-timespan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the specified timestampEvent has a value. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime WaitForValidTimestamp(TimestampEvent timestampEvent, TimeSpan timeout)RemarksTo avoid an exception, use this method to ensure a timestamp has a valid value before querying it.To u

### WaitForValidTimestamp(TimestampEvent, TimeSpan)

Waits until the specified *timestampEvent*  has a value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime WaitForValidTimestamp(TimestampEvent timestampEvent, TimeSpan timeout)

#### Remarks

To avoid an exception, use this method to ensure a timestamp has a valid value before querying it.

To use this method, you must first enable timestamps for the timestamp event type specified by *timestampEvent* . The following code demonstrates how to do this for [StartTrigger](nationalinstruments-daqmx-timestampevent.html).

```text
// Using an instance of Task called 'myTask'.myTask.Triggers.StartTrigger.TimestampEnable = true;myTask.Start();myTimestamp = myTask.WaitForValidTimestamp(TimestampEvent.StartTrigger);
```

```text
' Using an instance of Task called 'myTask'.myTask.Triggers.StartTrigger.TimestampEnable = TruemyTask.Start()myTimestamp = myTask.WaitForValidTimestamp(TimestampEvent.StartTrigger)
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timestampEvent | TimestampEvent | The timestamp event type to wait on. For more information see TimestampEvent. |
| timeout | TimeSpan | The maximum amount of time to wait for a valid timestamp. To wait indefinitely, use the overload of this method that does not take a timeout. |

#### Returns

The requested timestamp value.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the timeout provided was less than Zero. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-waitforvalidtimestamp__timestampevent.html language=enus -->
## TOPIC 02740: WaitForValidTimestamp(TimestampEvent)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-waitforvalidtimestamp__timestampevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-waitforvalidtimestamp__timestampevent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits indefinitely until the specified timestampEvent has a value. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime WaitForValidTimestamp(TimestampEvent timestampEvent)RemarksTo avoid an exception, use this method to ensure a timestamp has a valid value before querying it.To use th

### WaitForValidTimestamp(TimestampEvent)

Waits indefinitely until the specified *timestampEvent*  has a value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime WaitForValidTimestamp(TimestampEvent timestampEvent)

#### Remarks

To avoid an exception, use this method to ensure a timestamp has a valid value before querying it.

To use this method, you must first enable timestamps for the timestamp event type specified by *timestampEvent* . The following code demonstrates how to do this for [StartTrigger](nationalinstruments-daqmx-timestampevent.html).

```text
// Using an instance of Task called 'myTask'.myTask.Triggers.StartTrigger.TimestampEnable = true;myTask.Start();myTimestamp = myTask.WaitForValidTimestamp(TimestampEvent.StartTrigger);
```

```text
' Using an instance of Task called 'myTask'.myTask.Triggers.StartTrigger.TimestampEnable = TruemyTask.Start()myTimestamp = myTask.WaitForValidTimestamp(TimestampEvent.StartTrigger)
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timestampEvent | TimestampEvent | Specifies the timestamp event type to wait on. For more information see TimestampEvent. |

#### Returns

The requested timestamp value.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-waituntildone.html language=enus -->
## TOPIC 02741: WaitUntilDone()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-waituntildone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-waituntildone.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the measurement or generation to complete, regardless of the amount of time needed, and returns if it has completed execution. SyntaxNamespace: NationalInstruments.DAQmxpublic void WaitUntilDone()RemarksWaitUntilDone waits for the task to finish acquiring or generating the number of sample

### WaitUntilDone()

Waits for the measurement or generation to complete, regardless of the amount of time needed, and returns if it has completed execution.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WaitUntilDone()

#### Remarks

[WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) waits for the task to finish acquiring or generating the number of samples per channel specified on the [Timing](nationalinstruments-daqmx-timing.html) class. [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) does not wait for pending asynchronous operations to complete. Use the methods and properties on IAsyncResult to verify that asynchronous reads and writes are complete.

#### Returns

true if the task has completed execution.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-waituntildone__int.html language=enus -->
## TOPIC 02742: WaitUntilDone(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-waituntildone__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-waituntildone__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the measurement or generation to complete and returns if it has completed execution before the specified time elapses. SyntaxNamespace: NationalInstruments.DAQmxpublic void WaitUntilDone(int millisecToWait)RemarksWaitUntilDone(int) waits for the task to finish acquiring or generating the n

### WaitUntilDone(int)

Waits for the measurement or generation to complete and returns if it has completed execution before the specified time elapses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WaitUntilDone(int millisecToWait)

#### Remarks

WaitUntilDone(int) waits for the task to finish acquiring or generating the number of samples per channel specified on the [Timing](nationalinstruments-daqmx-timing.html) class. WaitUntilDone(int) does not wait for pending asynchronous operations to complete. Use the methods and properties on the IAsyncResult to verify that asynchronous reads and writes are complete.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| millisecToWait | int | The maximum amount of time in milliseconds to wait for the measurement or generation to complete. This method returns an error if the time elapses. If you set the timeout to -1, the method always waits for the task to complete, regardless of the amount of time needed. |

#### Returns

true if the task has completed execution.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-waituntildone__timespan.html language=enus -->
## TOPIC 02743: WaitUntilDone(TimeSpan)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-waituntildone__timespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-waituntildone__timespan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the measurement or generation to complete and returns if it has completed execution before the specified TimeSpan elapses. SyntaxNamespace: NationalInstruments.DAQmxpublic void WaitUntilDone(TimeSpan timeout)RemarksWaitUntilDone(TimeSpan) waits for the task to finish acquiring or generatin

### WaitUntilDone(TimeSpan)

Waits for the measurement or generation to complete and returns if it has completed execution before the specified TimeSpan elapses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WaitUntilDone(TimeSpan timeout)

#### Remarks

WaitUntilDone(TimeSpan) waits for the task to finish acquiring or generating the number of samples per channel specified on the [Timing](nationalinstruments-daqmx-timing.html) class. WaitUntilDone(TimeSpan) does not wait for pending asynchronous operations to complete. Use the methods and properties on the IAsyncResult to verify that asynchronous reads and writes are complete.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | TimeSpan | The maximum TimeSpan to wait for the measurement or generation to complete. This method returns an error if the time elapses. |

#### Returns

true if the task has completed execution.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- System.TimeSpan

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task-watchdog.html language=enus -->
## TOPIC 02744: Watchdog

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task-watchdog.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task-watchdog.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the watchdog configuration and control object for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic Watchdog Watchdog { get; }RemarksThe Watchdog for the task.

### Watchdog

Gets the watchdog configuration and control object for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Watchdog](nationalinstruments-daqmx-watchdog.html) Watchdog { get; }

#### Remarks

The [Watchdog](nationalinstruments-daqmx-watchdog.html) for the task.

Parent topic:

Task Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-task.html language=enus -->
## TOPIC 02745: Task Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-task.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-task.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a collection of virtual channels and their per-channel properties and timing, triggering, and other properties that apply to the DAQmx Task. Derives fromMarshalByRefObjectIDisposableISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class T

### Task Class

Represents a collection of [virtual channels](/csh?context=nidaqmx_mxcncpts_virtchantypes) and their per-channel properties and timing, triggering, and other properties that apply to the [DAQmx Task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Derives from

- MarshalByRefObject
- IDisposable
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Task : MarshalByRefObject, IDisposable, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Task

Task

DaqStream

Task

Stream

Task

Note

Some DAQ devices are not currently supported by the NI-DAQmx driver. Refer to *NI-DAQ Readme* for a complete listing of supported hardware.

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

Tasks

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| Task() | Initializes a new instance of the Task class with a unique name. |
| Task(string) | Initializes a new instance of the Task class with the specified name. |

#### Properties

| Name | Description |
| --- | --- |
| AccessoryInsertionOrRemovalDetected | Indicates if any devices in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevicesWithInsertedOrRemovedAccessories. Otherwise, you will receive an error. |
| AIChannels | Gets the collection of analog input channels in the task. |
| AOChannels | Gets the collection of analog output channels in the task. |
| CIChannels | Gets the collection of counter input channels in the task. |
| COChannels | Gets the collection of counter output channels in the task. |
| Devices | Indicates an array containing the names of all devices in the task. |
| DevicesWithInsertedOrRemovedAccessories | Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. |
| DIChannels | Gets the collection of digital input channels in the task. |
| DOChannels | Gets the collection of digital output channels in the task. |
| EveryNSamplesReadEventInterval | Gets or sets the interval, in number of samples per channel, at which EveryNSamplesRead is called. |
| EveryNSamplesWrittenEventInterval | Gets or sets the interval, in number of samples per channel, at which EveryNSamplesWritten is called. |
| ExportSignals | Gets the exported signal configuration for the task. |
| IsDone | Indicates whether the task completed execution. |
| Name | Indicates the name of the task. |
| Stream | Gets the stream for the task. |
| SwitchScan | Gets the switch scan configuration for the task. |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |
| Timing | Gets the timing configurations for the task. |
| Triggers | Gets the triggers for the task. |
| Watchdog | Gets the watchdog configuration and control object for the task. |

#### Methods

| Name | Description |
| --- | --- |
| AddGlobalChannel(string) | Adds a preconfigured, global channel to the task. |
| ConfigureLogging(string, TdmsLoggingOperation, LoggingMode) | Configures logging to a .tdms file when the acquisition starts. |
| ConfigureLogging(string, TdmsLoggingOperation, LoggingMode, string) | Configures logging to a .tdms file when the acquisition starts with the specified TDMS channel group name. |
| Control(TaskAction) | Alters the state of the task according to the mode you specify. |
| Dispose() | Releases all resources used by Task. |
| Start() | Transitions the task to the running state, which begins the measurement or generation. |
| StartNewFile(string) | Starts a new TDMS file the next time data is written to disk. |
| Stop() | Transitions the task from the running to the committed state, which ends the measurement or generation. |
| ToString() | Returns a string representation of the object. |
| WaitForValidTimestamp(TimestampEvent) | Waits indefinitely until the specified timestampEvent has a value. |
| WaitForValidTimestamp(TimestampEvent, TimeSpan) | Waits until the specified timestampEvent has a value. |
| WaitUntilDone(TimeSpan) | Waits for the measurement or generation to complete and returns if it has completed execution before the specified TimeSpan elapses. |
| WaitUntilDone() | Waits for the measurement or generation to complete, regardless of the amount of time needed, and returns if it has completed execution. |
| WaitUntilDone(int) | Waits for the measurement or generation to complete and returns if it has completed execution before the specified time elapses. |
| Dispose(bool) | Releases the managed and unmanaged resources used by Task or optionally releases only the unmanaged resources. |

#### Events

| Name | Description |
| --- | --- |
| CounterOutput | Occurs when any of the counters used in the task reaches its terminal count. |
| DigitalChangeDetection | Occurs when a digital change is detected on any of the digital lines used in the task. |
| Done | Occurs when the task completes. |
| EveryNSamplesRead | Occurs when N number of samples per channel, as defined by EveryNSamplesReadEventInterval, is written from the device to the PC buffer. |
| EveryNSamplesWritten | Occurs when N number of samples per channel, as defined by EveryNSamplesWrittenEventInterval, have been written from the PC buffer to the device. |
| SampleClock | Occurs on each pulse of the task's sample clock. |
| SampleComplete | Occurs when each sample is acquired into the NI-DAQmx driver buffer and is ready for reading. |

#### See Also

- LoadTask(string)
- AnalogSingleChannelReader
- AnalogMultiChannelReader
- AnalogUnscaledReader
- CounterSingleChannelReader
- CounterMultiChannelReader
- DigitalSingleChannelReader
- DigitalMultiChannelReader
- AnalogSingleChannelWriter
- AnalogMultiChannelWriter
- AnalogUnscaledWriter
- DigitalSingleChannelWriter
- DigitalMultiChannelWriter

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-taskaction.html language=enus -->
## TOPIC 02746: TaskAction Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-taskaction.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-taskaction.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to alter the state of the task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum TaskActionMembersNameValueDescriptionStart0Transitions the task to the running state, which begins device input or output. Stop1Transitions the task from the running state to the committed state, whic

### TaskAction Enumeration

Specifies how to alter the state of the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum TaskAction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Start | 0 | Transitions the task to the running state, which begins device input or output. |
| Stop | 1 | Transitions the task from the running state to the committed state, which ends device input or output. |
| Verify | 2 | Verifies that all task parameters are valid for the hardware. |
| Commit | 3 | Programs the hardware with all parameters of the task. |
| Reserve | 4 | Marks the hardware resources that are needed for the task as in use. No other tasks can reserve these same resources. |
| Unreserve | 5 | Releases all previously reserved resources. |
| Abort | 6 | Aborts execution of the task. Aborting a task immediately terminates the currently active operation, such as a read or a write. Aborting a task puts the task into an unstable but recoverable state. To recover the task, use Start to restart the task or use Stop to reset the task without starting it. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-taskdoneeventargs-checkforexception.html language=enus -->
## TOPIC 02747: CheckForException()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-taskdoneeventargs-checkforexception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-taskdoneeventargs-checkforexception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Throws the Exception that occurred, if any exists. SyntaxNamespace: NationalInstruments.DAQmxpublic void CheckForException()RemarksIf the task stopped due to an error, an Exception is thrown that represents the particular error. If the task did not stop due to an error, the method returns. As an alt

### CheckForException()

Throws the Exception that occurred, if any exists.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void CheckForException()

#### Remarks

If the task stopped due to an error, an Exception is thrown that represents the particular error. If the task did not stop due to an error, the method returns. As an alternative to calling this method, you can check the [Error](nationalinstruments-daqmx-taskdoneeventargs-error.html) property.

Parent topic:

TaskDoneEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-taskdoneeventargs-error.html language=enus -->
## TOPIC 02748: Error

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-taskdoneeventargs-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-taskdoneeventargs-error.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Exception that occurred, if any. SyntaxNamespace: NationalInstruments.DAQmxpublic Exception Error { get; }RemarksIf the task stopped due to an error, an Exception is returned that represents the particular error. If the task did not stop due to an error, this value is null.As an alternative

### Error

Gets the Exception that occurred, if any.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public Exception Error { get; }

#### Remarks

If the task stopped due to an error, an Exception is returned that represents the particular error. If the task did not stop due to an error, this value is null.

As an alternative to checking this property, you can call the [CheckForException](nationalinstruments-daqmx-taskdoneeventargs-checkforexception.html) method.

Parent topic:

TaskDoneEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-taskdoneeventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 02749: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-taskdoneeventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-taskdoneeventargs-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxprotected void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStream

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

TaskDoneEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-taskdoneeventargs-taskdoneeventargs__exception.html language=enus -->
## TOPIC 02750: TaskDoneEventArgs(Exception)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-taskdoneeventargs-taskdoneeventargs__exception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-taskdoneeventargs-taskdoneeventargs__exception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TaskDoneEventArgs class with the specified exception. SyntaxNamespace: NationalInstruments.DAQmxpublic TaskDoneEventArgs(Exception exception)ParametersNameTypeDescriptionexceptionExceptionThe Exception that explains why the task stopped, or null if the task complete

### TaskDoneEventArgs(Exception)

Initializes a new instance of the [TaskDoneEventArgs](nationalinstruments-daqmx-taskdoneeventargs.html) class with the specified exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public TaskDoneEventArgs(Exception exception)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| exception | Exception | The Exception that explains why the task stopped, or null if the task completed successfully. |

Parent topic:

TaskDoneEventArgs Class
