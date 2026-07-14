# NI DOCUMENT BUNDLE: ni_rfsa-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni_rfsa-csharp-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-mechanicalattenuatorenabled.html language=enus -->
## TOPIC 00001: MechanicalAttenuatorEnabled Enumeration

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-mechanicalattenuatorenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-mechanicalattenuatorenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the mechanical attenuator is enabled or disabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic enum MechanicalAttenuatorEnabledMembersNameValueDescriptionDisabled(int)1900Mechanical attenuator is disabled. Enabled(int)1901Mechanical attenuator is enabled.

### MechanicalAttenuatorEnabled Enumeration

Specifies whether the mechanical attenuator is enabled or disabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public enum MechanicalAttenuatorEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | (int)1900 | Mechanical attenuator is disabled. |
| Enabled | (int)1901 | Mechanical attenuator is enabled. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-nirfsa-acquisition.html language=enus -->
## TOPIC 00002: Acquisition

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-nirfsa-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-nirfsa-acquisition.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Acquisition sub-object that allows acquisition of the I/Q and spectrum data. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaAcquisition Acquisition { get; }RemarksReturns an object of type RfsaAcquisition.

### Acquisition

Gets the Acquisition sub-object that allows acquisition of the I/Q and spectrum data.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaAcquisition](nationalinstruments-modularinstruments-nirfsa-rfsaacquisition.html) Acquisition { get; }

#### Remarks

Returns an object of type [RfsaAcquisition](nationalinstruments-modularinstruments-nirfsa-rfsaacquisition.html).

Parent topic:

NIRfsa Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-nirfsa-calibration.html language=enus -->
## TOPIC 00003: Calibration

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-nirfsa-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-nirfsa-calibration.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Calibration sub-object that allows calibration of the NI-RFSA. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaCalibration Calibration { get; }RemarksReturns an object of type RfsaCalibration.

### Calibration

Gets the Calibration sub-object that allows calibration of the NI-RFSA.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaCalibration](nationalinstruments-modularinstruments-nirfsa-rfsacalibration.html) Calibration { get; }

#### Remarks

Returns an object of type [RfsaCalibration](nationalinstruments-modularinstruments-nirfsa-rfsacalibration.html).

Parent topic:

NIRfsa Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-nirfsa-close.html language=enus -->
## TOPIC 00004: Close()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-nirfsa-close.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-nirfsa-close.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void Close()RemarksThis method calls the Dispose method.

### Close()

Closes the session to the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void Close()

#### Remarks

This method calls the **Dispose** method.

Parent topic:

NIRfsa Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-nirfsa-dispose.html language=enus -->
## TOPIC 00005: Dispose()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-nirfsa-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-nirfsa-dispose.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the specified session and deallocates the reserved resources, if not already disposed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void Dispose()RemarksYou can call this method safely more than once, even if the session is already closed. A call to this method dispose

### Dispose()

Closes the specified session and deallocates the reserved resources, if not already disposed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void Dispose()

#### Remarks

You can call this method safely more than once, even if the session is already closed.

A call to this method disposes the **SafeHandle** class used to hold the instrument handle. If the call to this method fails due to some reason, like the session being closed by some external means, you will not be notified about the failure. To help you identify failures in the **ReleaseHandle** method of the **SafeHandle** class, managed debugging assistant (MDA) is activated.

For details refer to [. The call to this method fails when you externally close a session by: Initializing a session with a resource name for which the session is already open, within the same process. This causes the instrument handle held by the existing session to become invalid. Getting the instrument handle out using the method and closing this handle directly. 12/30/2011 6:00:16 PM NI True](http://msdn.microsoft.com/en-us/library/85eak4a0.aspx)

Parent topic:

NIRfsa Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-nirfsa-driveroperation.html language=enus -->
## TOPIC 00006: DriverOperation

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-nirfsa-driveroperation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-nirfsa-driveroperation.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.DriverOperation sub-object that affects the operation of the NI-RFSA instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaDriverOperation DriverOperation { get; }RemarksReturns an object of type Rfsa

### DriverOperation

Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.DriverOperation sub-object that affects the operation of the NI-RFSA instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaDriverOperation](nationalinstruments-modularinstruments-nirfsa-rfsadriveroperation.html) DriverOperation { get; }

#### Remarks

Returns an object of type [RfsaDriverOperation](nationalinstruments-modularinstruments-nirfsa-rfsadriveroperation.html).

Parent topic:

NIRfsa Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-nirfsa-identity.html language=enus -->
## TOPIC 00007: Identity

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-nirfsa-identity.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-nirfsa-identity.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.Identity sub-object that provides identity and version information about the NI-RFSA. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaDriverIdentity Identity { get; }RemarksReturns an object of type RfsaDriverIden

### Identity

Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.Identity sub-object that provides identity and version information about the NI-RFSA.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaDriverIdentity](nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity.html) Identity { get; }

#### Remarks

Returns an object of type [RfsaDriverIdentity](nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity.html).

Parent topic:

NIRfsa Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-nirfsa.html language=enus -->
## TOPIC 00008: NIRfsa Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-nirfsa.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-nirfsa.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class that is used to identify and control the instrument session. Derives fromIDisposableIServiceProviderIIviDriverITClockSynchronizableDeviceSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class NIRfsa : IDisposable, IServiceProvider, IIviDriver, ITClockSynchron

### NIRfsa Class

Defines a root class that is used to identify and control the instrument session.

#### Derives from

- IDisposable
- IServiceProvider
- IIviDriver
- ITClockSynchronizableDevice

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class NIRfsa : IDisposable, IServiceProvider, IIviDriver, ITClockSynchronizableDevice

#### Remarks

All properties, methods, and events fall under either the **NIRfsa**class or are the sub-objects of this class. To interact with the NI-RFSA, you must create an instance of this class.

#### Constructors

| Name | Description |
| --- | --- |
| NIRfsa(string, bool, bool, string) | Creates a new instrument driver session and sets the initial state of session properties. |
| NIRfsa(IntPtr) | Creates a new instrument driver session from an existing instrument handle. |
| NIRfsa(string, bool, bool) | Creates a new instrument driver session. |

#### Properties

| Name | Description |
| --- | --- |
| Acquisition | Gets the Acquisition sub-object that allows acquisition of the I/Q and spectrum data. |
| Calibration | Gets the Calibration sub-object that allows calibration of the NI-RFSA. |
| Configuration | Gets the Configuration sub-object that allows configuration of the NI-RFSA. |
| DeviceCharacteristics | Gets the DeviceCharacteristics sub-object to get device characteristics such as MemorySize, ModuleRevision, and SerialNumber. An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeviceCharacteristics.this[string]. |
| DriverIdentity | Gets the DriverIdentity sub-object that provides identity and version information about the NI-RFSA. |
| DriverOperation | Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.DriverOperation sub-object that affects the operation of the NI-RFSA instrument driver. |
| DriverUtility | Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.Utility sub-object to access the utility features of NI-RFSA. |
| Identity | Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.Identity sub-object that provides identity and version information about the NI-RFSA. |
| IsDisposed | Gets a value that indicates whether the session has been disposed. |
| Utility | Gets the NationalInstruments.ModularInstruments.NIRfsa.NIRfsa.Utility sub-object to access the utility features of NI-RFSA. |

#### Methods

| Name | Description |
| --- | --- |
| Close() | Closes the session to the device. |
| Dispose() | Closes the specified session and deallocates the reserved resources, if not already disposed. |
| GetInstrumentHandle() | Gets the SafeHandle to the NIRfsa instrument session. |
| GetService(Type) | Defines a mechanism for retrieving a service object; that is, an object that provides custom support to other objects. It supports the type NationalInstruments.ModularInstruments.AdvancedPropertyAccessService, Ivi.Driver.IIviDriver and NIRfsa. |
| VstSelfCalibrate(string) | Self-calibrates the device. If self-calibration is performed successfully, the new calibration constants are stored in the nonvolatile memory of the device. NI recommends that no external signals are present on the RF In port while the calibration is taking place. Refer to the specification document for your device for more information on self-calibration. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaacquisition-spectrum.html language=enus -->
## TOPIC 00009: Spectrum

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaacquisition-spectrum.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaacquisition-spectrum.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Spectrum sub-object to access spectral acquisition related properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaSpectrumAcquisition Spectrum { get; }RemarksReturns an object of type RfsaSpectrumAcquisition.

### Spectrum

Gets the Spectrum sub-object to access spectral acquisition related properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaSpectrumAcquisition](nationalinstruments-modularinstruments-nirfsa-rfsaspectrumacquisition.html) Spectrum { get; }

#### Remarks

Returns an object of type [RfsaSpectrumAcquisition](nationalinstruments-modularinstruments-nirfsa-rfsaspectrumacquisition.html).

Parent topic:

RfsaAcquisition Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedacquisition-datatransferblocksize.html language=enus -->
## TOPIC 00010: DataTransferBlockSize

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedacquisition-datatransferblocksize.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedacquisition-datatransferblocksize.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum number of samples to transfer at a time from the device to host memory. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic int DataTransferBlockSize { get; set; }RemarksIncreasing the number of samples results in better fetching performance because the driv

### DataTransferBlockSize

Gets or sets the maximum number of samples to transfer at a time from the device to host memory.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public int DataTransferBlockSize { get; set; }

#### Remarks

Increasing the number of samples results in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may increase the amount of page-locked memory required from the system.

Specifies an [Int32](https://learn.microsoft.com/dotnet/api/system.int32) representing the maximum number of samples to transfer at a time from the device to host memory.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DataTransferBlockSize property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedAcquisition Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedconfigurationlist.html language=enus -->
## TOPIC 00011: RfsaAdvancedConfigurationList Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedconfigurationlist.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedconfigurationlist.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the advanced methods and properties used to work with configuration list and its related steps. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaAdvancedConfigurationList : RfsaSubObjectRemarksFor more information, refer to NI RF Vect

### RfsaAdvancedConfigurationList Class

Represents the advanced methods and properties used to work with configuration list and its related steps.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaAdvancedConfigurationList : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| MinimumReconfigurationTime | This property is not for customer use. |
| TimerStartSource | This property is not for customer use. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedreferencetrigger-triggerdelay.html language=enus -->
## TOPIC 00012: TriggerDelay

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedreferencetrigger-triggerdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedreferencetrigger-triggerdelay.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the trigger delay time. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double TriggerDelay { get; set; }RemarksSpecifies a Double representing the trigger delay time. The trigger delay time is the length of time the IF digitizer waits after it receives the trigger

### TriggerDelay

Gets or sets the trigger delay time.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double TriggerDelay { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the trigger delay time.

The trigger delay time is the length of time the IF digitizer waits after it receives the trigger before it asserts the Reference event.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The TriggerDelay property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedReferenceTrigger Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-looutpower.html language=enus -->
## TOPIC 00013: LOOutPower

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-looutpower.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-looutpower.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the power level, in dBm, of the signal at the LO OUT terminal when the LOExportEnabled property is set to true. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double LOOutPower { get; set; }RemarksReturns a Double representing LO Out Power property. ExceptionsTypeD

### LOOutPower

Gets or sets the power level, in dBm, of the signal at the LO OUT terminal when the [LOExportEnabled](nationalinstruments-modularinstruments-nirfsa-rfsasignalpath-loexportenabled.html) property is set to **true**.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double LOOutPower { get; set; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing LO Out Power property.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOOutPower property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedSignalPath Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-lopllfractionalmodeenabled.html language=enus -->
## TOPIC 00014: LOPllFractionalModeEnabled

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-lopllfractionalmodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-lopllfractionalmodeenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to use fractional mode for the LO PLL. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaLOPllFractionalModeEnabled LOPllFractionalModeEnabled { get; set; }RemarksSpecifies the RfsaLOPllFractionalModeEnabled enumeration. Fractional mode gives a finer frequ

### LOPllFractionalModeEnabled

Gets or sets whether to use fractional mode for the LO PLL.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaLOPllFractionalModeEnabled](nationalinstruments-modularinstruments-nirfsa-rfsalopllfractionalmodeenabled.html) LOPllFractionalModeEnabled { get; set; }

#### Remarks

Specifies the [RfsaLOPllFractionalModeEnabled](nationalinstruments-modularinstruments-nirfsa-rfsalopllfractionalmodeenabled.html) enumeration.

Fractional mode gives a finer frequency step resolution, but it may result in non-harmonic spurs. Refer to the *NI PXIe-5644R Specifications* or the *NI PXIe-5645R Specifications* for more information about fractional mode and non-harmonic spurs.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOPllFractionalModeEnabled property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedSignalPath Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-lowfrequencybypassenabled.html language=enus -->
## TOPIC 00015: LowFrequencyBypassEnabled

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-lowfrequencybypassenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-lowfrequencybypassenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to use the low-frequency bypass path for the incoming RF signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaLowFrequencyBypassEnabled LowFrequencyBypassEnabled { get; set; }RemarksSpecifies the RfsaLowFrequencyBypassEnabled enumeration. ExceptionsTy

### LowFrequencyBypassEnabled

Gets or sets whether to use the low-frequency bypass path for the incoming RF signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaLowFrequencyBypassEnabled](nationalinstruments-modularinstruments-nirfsa-rfsalowfrequencybypassenabled.html) LowFrequencyBypassEnabled { get; set; }

#### Remarks

Specifies the [RfsaLowFrequencyBypassEnabled](nationalinstruments-modularinstruments-nirfsa-rfsalowfrequencybypassenabled.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LowFrequencyBypassEnabled property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedSignalPath Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-minfundamentalsilofrequency.html language=enus -->
## TOPIC 00016: MinFundamentalSiloFrequency

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-minfundamentalsilofrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-minfundamentalsilofrequency.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum fundamental silo frequency. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double MinFundamentalSiloFrequency { get; }RemarksSpecifies the minimum fundamental silo frequency in Hz. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe MinFundamentalSiloFre

### MinFundamentalSiloFrequency

Gets the minimum fundamental silo frequency.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double MinFundamentalSiloFrequency { get; }

#### Remarks

Specifies the minimum fundamental silo frequency in Hz.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The MinFundamentalSiloFrequency property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedSignalPath Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-notchfilterenabled.html language=enus -->
## TOPIC 00017: NotchFilterEnabled

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-notchfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath-notchfilterenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the notch filter is enabled on the RF conditioning module. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaNotchFilterEnabled NotchFilterEnabled { get; set; }RemarksSpecifies the RfsaNotchFilterEnabled enumeration. ExceptionsTypeDescriptionSystem.ObjectD

### NotchFilterEnabled

Gets or sets whether the notch filter is enabled on the RF conditioning module.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaNotchFilterEnabled](nationalinstruments-modularinstruments-nirfsa-rfsanotchfilterenabled.html) NotchFilterEnabled { get; set; }

#### Remarks

Specifies the [RfsaNotchFilterEnabled](nationalinstruments-modularinstruments-nirfsa-rfsanotchfilterenabled.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The NotchFilterEnabled property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedSignalPath Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath.html language=enus -->
## TOPIC 00018: RfsaAdvancedSignalPath Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedsignalpath.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides advanced properties related to signal path. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaAdvancedSignalPath : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionAbsoluteDe

### RfsaAdvancedSignalPath Class

Provides advanced properties related to signal path.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaAdvancedSignalPath : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| AbsoluteDelay | Gets or sets the sub-sample clock delay, in seconds, to apply to the acquired signal. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session. To set this property, the NI-RFSA device must be in the Configuration state. Note If this value is set, NI-TClk cannot do any sub-sample clock adjustment. |
| AvailablePaths | Returns a comma separated list of the configurable paths available for use based on your instrument configuration. |
| DownconverterLoopBandwidth | Gets or sets the loop bandwidth of the downconverter tuning phase-locked loops (PLL). |
| DownconverterPreselectorEnabled | Gets or sets whether the tunable preselector is enabled on the downconverter. |
| FrequencySettlingTime | Gets or sets the value used for LO frequency settling. |
| FrequencySettlingUnits | Gets or sets the delay duration units and interpretation for LO settling. |
| IFConditioningDownconversionEnabled | Gets or sets whether downconversion to 21.4 MHz is enabled for the IF conditioning module. |
| InputIsolationEnabled | Gets or sets whether input isolation is enabled. |
| InputPort | Gets or sets the connector(s) to acquire the signal. |
| LOFrequencyStepSize | Gets or sets the step size for tuning the local oscillator (LO) phase-locked loop (PLL). |
| LOInjectionSide | Gets or sets the LO injection side. |
| LOInPower | Gets the power level, in dBm, expected at the LO terminal when the LOSource property is set to LOIn. |
| LOOutPower | Gets or sets the power level, in dBm, of the signal at the LO OUT terminal when the LOExportEnabled property is set to true. |
| LOPllFractionalModeEnabled | Gets or sets whether to use fractional mode for the LO PLL. |
| LowFrequencyBypassEnabled | Gets or sets whether to use the low-frequency bypass path for the incoming RF signal. |
| MaxFundamentalSiloFrequency | Gets the maximum fundamental silo frequency. |
| MinFundamentalSiloFrequency | Gets the minimum fundamental silo frequency. |
| NotchFilterEnabled | Gets or sets whether the notch filter is enabled on the RF conditioning module. |
| RFHighPassFiltering | Gets or sets the maximum corner frequency of the high pass filter in the RF signal path. |
| RFPreselectorFilter | Gets or sets the RF preselector filter to use. |
| SelectedPath | Gets or sets which path to configure to acquire a signal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-amplitudesettling.html language=enus -->
## TOPIC 00019: AmplitudeSettling

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-amplitudesettling.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-amplitudesettling.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amplitude settling accuracy in decibels. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double AmplitudeSettling { get; set; }RemarksSpecifies a Double representing the the amplitude settling accuracy in decibels.The default value is 0.5 dB. NI-RFSA waits until

### AmplitudeSettling

Gets or sets the amplitude settling accuracy in decibels.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double AmplitudeSettling { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the the amplitude settling accuracy in decibels.The default value is 0.5 dB.

NI-RFSA waits until the RF power settles within the specified accuracy level after calling the [Initiate](nationalinstruments-modularinstruments-nirfsa-rfsaiqacquisition-initiate.html) method. Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AmplitudeSettling property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedVertical Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-digitalgain.html language=enus -->
## TOPIC 00020: DigitalGain

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-digitalgain.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-digitalgain.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the scaling factor, in decibels, applied to the time-domain voltage data in the digitizer. NI-RFSA does not compensate for the specified digital gain. NI-RFSA does not compensate for the specified digital gain. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double

### DigitalGain

Gets or sets the scaling factor, in decibels, applied to the time-domain voltage data in the digitizer. NI-RFSA does not compensate for the specified digital gain. NI-RFSA does not compensate for the specified digital gain.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double DigitalGain { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the scaling factor, in decibels, applied to the time-domain voltage data in the digitizer. The default value is 0 dB.

You can use this property to account for external gain changes without changing the analog signal path.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DigitalGain property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedVertical Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-mechanicalattenuation.html language=enus -->
## TOPIC 00021: MechanicalAttenuation

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-mechanicalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-mechanicalattenuation.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the level of mechanical attenuation, in dB, for the RF path. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double MechanicalAttenuation { get; set; }RemarksSpecifies a Double representing the level of mechanical attenuation, in dB, for the RF path. ExceptionsTypeD

### MechanicalAttenuation

Gets or sets the level of mechanical attenuation, in dB, for the RF path.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double MechanicalAttenuation { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the level of mechanical attenuation, in dB, for the RF path.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The MechanicalAttenuation property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedVertical Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-minimumacpr.html language=enus -->
## TOPIC 00022: MinimumAcpr

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-minimumacpr.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-minimumacpr.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double MinimumAcpr { get; set; }RemarksSpecifies an Int32 representing the minimum adjacent channel power ratio (ACP

### MinimumAcpr

Gets or sets the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double MinimumAcpr { get; set; }

#### Remarks

Specifies an [Int32](https://learn.microsoft.com/dotnet/api/system.int32) representing the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The MinimumAcpr property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedVertical Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-ni5663.html language=enus -->
## TOPIC 00023: NI5663

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-ni5663.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-ni5663.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the object used to access the advanced vertical properties specific to NI 5663. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaNI5663AdvancedVertical NI5663 { get; }RemarksReturns an object of type RfsaNI5663AdvancedVertical.

### NI5663

Gets the object used to access the advanced vertical properties specific to NI 5663.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaNI5663AdvancedVertical](nationalinstruments-modularinstruments-nirfsa-rfsani5663advancedvertical.html) NI5663 { get; }

#### Remarks

Returns an object of type [RfsaNI5663AdvancedVertical](nationalinstruments-modularinstruments-nirfsa-rfsani5663advancedvertical.html).

Parent topic:

RfsaAdvancedVertical Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-rfattenuation.html language=enus -->
## TOPIC 00024: RFAttenuation

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-rfattenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-rfattenuation.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the downconverter module attenuation setting. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double RFAttenuation { get; set; }RemarksSpecifies a Double representing the downconverter module attenuation setting. NI-RFSA automatically chooses an attenuation setting

### RFAttenuation

Gets or sets the downconverter module attenuation setting.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double RFAttenuation { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the downconverter module attenuation setting.

NI-RFSA automatically chooses an attenuation setting for the reference level that you configure.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The RFAttenuation property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedVertical Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-thermalcorrectionheadroomrange.html language=enus -->
## TOPIC 00025: ThermalCorrectionHeadroomRange

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-thermalcorrectionheadroomrange.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancedvertical-thermalcorrectionheadroomrange.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from GetDeviceTemperature. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double ThermalCorrectionHeadroomRange { get; set; }RemarksThe defaul

### ThermalCorrectionHeadroomRange

Gets or sets the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from [GetDeviceTemperature](nationalinstruments-modularinstruments-nirfsa-rfsadevicecharacteristics-getdevicetemperature.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double ThermalCorrectionHeadroomRange { get; set; }

#### Remarks

The default value for the PXIe-5830/5831/5832 is 5. The default value for the PXIe-5840 is 10.

For example, if this property is set to 5.0, and the device is self-calibrated at 35 degrees Celsius, then you can expect to run the device from 30 degrees Celsius to 40 degrees Celsius with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ThermalCorrectionHeadroomRange property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvancedVertical Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-disable.html language=enus -->
## TOPIC 00026: Disable()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-disable.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not use an Advance trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void Disable()RemarksUse this method only if you have to disable a previously configured Advance trigger. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Disable metho

### Disable()

Configures the device to not use an Advance trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void Disable()

#### Remarks

Use this method only if you have to disable a previously configured Advance trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Disable method was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvanceTrigger Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00027: SendSoftwareEdgeTrigger()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-sendsoftwareedgetrigger.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use a software version of Advance trigger and the device is waiting for the trigger to be sent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void SendSoftwareEdgeTrigger()RemarksThis method returns an error in the following situations: Y

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use a software version of Advance trigger and the device is waiting for the trigger to be sent.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void SendSoftwareEdgeTrigger()

#### Remarks

- You configure an invalid trigger.
- You set the [AcquisitionType](nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-acquisitiontype.html) to [Spectrum](nationalinstruments-modularinstruments-nirfsa-rfsaacquisitiontype.html).
- You have not previously called the [Initiate](nationalinstruments-modularinstruments-nirfsa-rfsaiqacquisition-initiate.html) method.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SendSoftwareEdgeTrigger method was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvanceTrigger Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-type.html language=enus -->
## TOPIC 00028: Type

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger-type.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether you want the Advance trigger to be a digital edge or software trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaAdvanceTriggerType Type { get; set; }RemarksSpecifies the RfsaAdvanceTriggerType enumeration. ExceptionsTypeDescriptionSystem.ObjectDis

### Type

Gets or sets whether you want the Advance trigger to be a digital edge or software trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaAdvanceTriggerType](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggertype.html) Type { get; set; }

#### Remarks

Specifies the [RfsaAdvanceTriggerType](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggertype.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Type property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaAdvanceTrigger Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronization.html language=enus -->
## TOPIC 00029: RfsaAdvanceTriggerSynchronization Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronization.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to synchronize the Advance Trigger. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaAdvanceTriggerSynchronization : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. Properties

### RfsaAdvanceTriggerSynchronization Class

Represents the properties used to synchronize the Advance Trigger.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaAdvanceTriggerSynchronization : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| DistributionLine | Gets or sets the external trigger line that distributes the synchronized Advance Trigger signal. When synchronizing the Advance Trigger, configure all devices to use the same Advance Trigger distribution line. |
| IsMaster | Gets or sets whether the device is the master for synchronizing the shared Advance Trigger among multiple devices. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-equals__rfsaadvancetriggersynchronizationdistributionline.html language=enus -->
## TOPIC 00030: Equals(RfsaAdvanceTriggerSynchronizationDistributionLine)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-equals__rfsaadvancetriggersynchronizationdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-equals__rfsaadvancetriggersynchronizationdistributionline.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaAdvanceTriggerSynchronizationDistributionLine and the RfsaAdvanceTriggerSynchronizationDistributionLine object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaAdvanceTriggerSynchronization

### Equals(RfsaAdvanceTriggerSynchronizationDistributionLine)

Determines whether the current instance of [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) and the [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaAdvanceTriggerSynchronizationDistributionLine source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsaAdvanceTriggerSynchronizationDistributionLine | Specifies the RfsaAdvanceTriggerSynchronizationDistributionLine object to be compared to the current instance of RfsaAdvanceTriggerSynchronizationDistributionLine. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaAdvanceTriggerSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-fromstring__string.html language=enus -->
## TOPIC 00031: FromString(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-fromstring__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsaAdvanceTriggerSynchronizationDistributionLine object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaAdvanceTriggerSynchronizationDistributionLine FromString(string source)ParametersNameTypeDescriptionsourcestringSpecifies a s

### FromString(string)

Creates an [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies a string representing the source of RfsaIQPowerEdge. |

#### Returns

Returns an object of type [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html).

Parent topic:

RfsaAdvanceTriggerSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-operator_eq__rfsaadvancetriggersynchronizationdistributionline-rfsaadvancetriggersynchron...d115e346.html language=enus -->
## TOPIC 00032: operator==(RfsaAdvanceTriggerSynchronizationDistributionLine, RfsaAdvanceTriggerSynchronizationDistributionLine)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-operator_eq__rfsaadvancetriggersynchronizationdistributionline-rfsaadvancetriggersynchron...d115e346.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-operator_eq__rfsaadvancetriggersynchronizationdistributionline-rfsaadvancetriggersynchron...d115e346.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaAdvanceTriggerSynchronizationDistributionLine are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaAdvanceTriggerSynchronizationDistributionLine source1, RfsaAdvanceTriggerSynchronizationDistributionLine so

### operator==(RfsaAdvanceTriggerSynchronizationDistributionLine, RfsaAdvanceTriggerSynchronizationDistributionLine)

Checks whether the two instances of [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaAdvanceTriggerSynchronizationDistributionLine source1, RfsaAdvanceTriggerSynchronizationDistributionLine source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsaAdvanceTriggerSynchronizationDistributionLine | Specifies a RfsaAdvanceTriggerSynchronizationDistributionLine object. |
| source2 | RfsaAdvanceTriggerSynchronizationDistributionLine | Specifies a RfsaAdvanceTriggerSynchronizationDistributionLine object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaAdvanceTriggerSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-operator_neq__rfsaadvancetriggersynchronizationdistributionline-rfsaadvancetriggersynchro...d115e294.html language=enus -->
## TOPIC 00033: operator!=(RfsaAdvanceTriggerSynchronizationDistributionLine, RfsaAdvanceTriggerSynchronizationDistributionLine)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-operator_neq__rfsaadvancetriggersynchronizationdistributionline-rfsaadvancetriggersynchro...d115e294.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-operator_neq__rfsaadvancetriggersynchronizationdistributionline-rfsaadvancetriggersynchro...d115e294.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaAdvanceTriggerSynchronizationDistributionLine are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaAdvanceTriggerSynchronizationDistributionLine source1, RfsaAdvanceTriggerSynchronizationDistributionLine

### operator!=(RfsaAdvanceTriggerSynchronizationDistributionLine, RfsaAdvanceTriggerSynchronizationDistributionLine)

Checks whether the two instances of [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaAdvanceTriggerSynchronizationDistributionLine source1, RfsaAdvanceTriggerSynchronizationDistributionLine source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsaAdvanceTriggerSynchronizationDistributionLine | Specifies a RfsaAdvanceTriggerSynchronizationDistributionLine object. |
| source2 | RfsaAdvanceTriggerSynchronizationDistributionLine | Specifies RfsaAdvanceTriggerSynchronizationDistributionLine object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsaAdvanceTriggerSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-pxitrig5.html language=enus -->
## TOPIC 00034: PxiTrig5

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-pxitrig5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-pxitrig5.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external trigger line which is set to PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaAdvanceTriggerSynchronizationDistributionLine PxiTrig5 { get; }RemarksReturns an object of type RfsaAdvanceTriggerSynchronizationDistributionLine represe

### PxiTrig5

Gets the external trigger line which is set to PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) PxiTrig5 { get; }

#### Remarks

Returns an object of type [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) representing the string "PXI_Trig5".

Parent topic:

RfsaAdvanceTriggerSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-pxitrig6.html language=enus -->
## TOPIC 00035: PxiTrig6

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-pxitrig6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-pxitrig6.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external trigger line which is set to PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaAdvanceTriggerSynchronizationDistributionLine PxiTrig6 { get; }RemarksReturns an object of type RfsaAdvanceTriggerSynchronizationDistributionLine represe

### PxiTrig6

Gets the external trigger line which is set to PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) PxiTrig6 { get; }

#### Remarks

Returns an object of type [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) representing the string "PXI_Trig6".

Parent topic:

RfsaAdvanceTriggerSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-tostring.html language=enus -->
## TOPIC 00036: ToString()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline-tostring.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsaAdvanceTriggerSynchronizationDistributionLine to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override string ToString()ReturnsReturns a string that represents the current instance of RfsaAdvanceTriggerSynchronizationDistributionLi

### ToString()

Converts the current instance of [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsaAdvanceTriggerSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html).

Parent topic:

RfsaAdvanceTriggerSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html language=enus -->
## TOPIC 00037: RfsaAdvanceTriggerSynchronizationDistributionLine Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronizationdistributionline.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the RfsaAdvanceTriggerSynchronization signal. When synchronizing the RfsaAdvanceTrigger, configure all devices to use the same Advance Trigger distribution line. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic cla

### RfsaAdvanceTriggerSynchronizationDistributionLine Class

Specifies which external trigger line distributes the [RfsaAdvanceTriggerSynchronization](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronization.html) signal. When synchronizing the [RfsaAdvanceTrigger](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetrigger.html), configure all devices to use the same Advance Trigger distribution line.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaAdvanceTriggerSynchronizationDistributionLine

#### Remarks

Refer to [DistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsaadvancetriggersynchronization-distributionline.html).

#### Properties

| Name | Description |
| --- | --- |
| Pfi0 | Gets the external trigger line that is set to PFI 0 connector. |
| PxiTrig0 | Gets the external trigger line which is set to PXI trigger line 0. |
| PxiTrig1 | Gets the external trigger line which is set to PXI trigger line 1. |
| PxiTrig2 | Gets the external trigger line which is set to PXI trigger line 2. |
| PxiTrig3 | Gets the external trigger line which is set to PXI trigger line 3. |
| PxiTrig4 | Gets the external trigger line which is set to PXI trigger line 4. |
| PxiTrig5 | Gets the external trigger line which is set to PXI trigger line 5. |
| PxiTrig6 | Gets the external trigger line which is set to PXI trigger line 6. |
| PxiTrig7 | Gets the external trigger line which is set to PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsaAdvanceTriggerSynchronizationDistributionLine object from the specified string. |
| Equals(RfsaAdvanceTriggerSynchronizationDistributionLine) | Determines whether the current instance of RfsaAdvanceTriggerSynchronizationDistributionLine and the RfsaAdvanceTriggerSynchronizationDistributionLine object that you specify are equal. |
| Equals(object) | Determines whether the current instance RfsaAdvanceTriggerSynchronizationDistributionLine and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaAdvanceTriggerSynchronizationDistributionLine. |
| ToString() | Converts the current instance of RfsaAdvanceTriggerSynchronizationDistributionLine to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsaAdvanceTriggerSynchronizationDistributionLine(string) | Converts the specified string to its RfsaAdvanceTriggerSynchronizationDistributionLine equivalent. |
| operator string(RfsaAdvanceTriggerSynchronizationDistributionLine) | Converts the RfsaAdvanceTriggerSynchronizationDistributionLine object to its string equivalent. |
| operator!=(RfsaAdvanceTriggerSynchronizationDistributionLine, RfsaAdvanceTriggerSynchronizationDistributionLine) | Checks whether the two instances of RfsaAdvanceTriggerSynchronizationDistributionLine are unequal. |
| operator==(RfsaAdvanceTriggerSynchronizationDistributionLine, RfsaAdvanceTriggerSynchronizationDistributionLine) | Checks whether the two instances of RfsaAdvanceTriggerSynchronizationDistributionLine are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacalibration-self.html language=enus -->
## TOPIC 00038: Self

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacalibration-self.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacalibration-self.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RfsaSelfCalibration sub-object that provides properties and methods for self calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaSelfCalibration Self { get; }RemarksReturns an object of type RfsaSelfCalibration.

### Self

Gets the [RfsaSelfCalibration](nationalinstruments-modularinstruments-nirfsa-rfsaselfcalibration.html) sub-object that provides properties and methods for self calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaSelfCalibration](nationalinstruments-modularinstruments-nirfsa-rfsaselfcalibration.html) Self { get; }

#### Remarks

Returns an object of type [RfsaSelfCalibration](nationalinstruments-modularinstruments-nirfsa-rfsaselfcalibration.html).

Parent topic:

RfsaCalibration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding-deembeddingcompensationgain.html language=enus -->
## TOPIC 00039: DeembeddingCompensationGain

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding-deembeddingcompensationgain.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding-deembeddingcompensationgain.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double DeembeddingCompensationGain { get; }RemarksSpecifies a Double representing the de-embeddin

### DeembeddingCompensationGain

Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double DeembeddingCompensationGain { get; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the de-embedding compensation gain.

To use this property, you must set the channelName of the [RfsaChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding.html) sub-object to specify the name of the port to configure for de-embedding.

A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeembedding.this[string].

If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT. Use the [CreateDeembeddingSParameterTableS2pFile](nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertables2pfile__string-string-rfsasparameterorientation.html) to create tables.

Parent topic:

RfsaChannelBasedDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding-deletedeembeddingtable__string.html language=enus -->
## TOPIC 00040: DeleteDeembeddingTable(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding-deletedeembeddingtable__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding-deletedeembeddingtable__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the selected de-embedding table. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void DeleteDeembeddingTable(string tableName)ParametersNameTypeDescriptiontableNamestringSpecifies the name of the table.

### DeleteDeembeddingTable(string)

Deletes the selected de-embedding table.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void DeleteDeembeddingTable(string tableName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. |

Parent topic:

RfsaChannelBasedDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-loexportenabled.html language=enus -->
## TOPIC 00041: LOExportEnabled

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-loexportenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-loexportenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to enable the LO OUT terminals on the installed devices. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool LOExportEnabled { get; set; }Remarkstrue if the LO OUT terminals are enabled; otherwise, false. PXIe-5601: The only valid value is true.PXIe-5603/56

### LOExportEnabled

Gets or sets whether to enable the LO OUT terminals on the installed devices.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool LOExportEnabled { get; set; }

#### Remarks

true if the LO OUT terminals are enabled; otherwise, false.

PXIe-5601: The only valid value is true.

PXIe-5603/5605/5606: By default, the LO OUT terminals are not enabled. If you want to daisy-chain multiple devices together using the same LO source, set this property to true to export the LO input signals on the LO1, LO2, and LO3 terminals to LO1 OUT, LO2 OUT, and LO3 OUT, respectively.

PXIe-5694: You can enable this property if you set the [LOSource](nationalinstruments-modularinstruments-nirfsa-rfsasignalpath-losource.html) property to [LOIn](nationalinstruments-modularinstruments-nirfsa-rfsalosource-loin.html), or if you set the [LOSource](nationalinstruments-modularinstruments-nirfsa-rfsasignalpath-losource.html) to [Onboard](nationalinstruments-modularinstruments-nirfsa-rfsalosource-onboard.html) and the [RfsaIFConditioningDownconversionEnabled](nationalinstruments-modularinstruments-nirfsa-rfsaifconditioningdownconversionenabled.html) to [Enabled](nationalinstruments-modularinstruments-nirfsa-rfsaifconditioningdownconversionenabled.html).

PXIe-5830/5831: To use this property, you must specify the the channelName of the [RfsaChannelBasedLO](nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaLocalOscillator.this[string]

Note

If you are sharing an LO for the PXIe-5830/5831/5832 between and NI-RFSA and NI-RFSG session, ensure both sessions use the same shared setting.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOExportEnabled property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaChannelBasedLO Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-looutpower.html language=enus -->
## TOPIC 00042: LOOutPower

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-looutpower.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-looutpower.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the power level, in dBm, of the signal at the LO OUT terminal when the LOExportEnabled property is set to true. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double LOOutPower { get; set; }RemarksReturns a Double representing LO Out Power property. PXIe-5830/5831/

### LOOutPower

Gets or sets the power level, in dBm, of the signal at the LO OUT terminal when the [LOExportEnabled](nationalinstruments-modularinstruments-nirfsa-rfsasignalpath-loexportenabled.html) property is set to **true**.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double LOOutPower { get; set; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing LO Out Power property.

PXIe-5830/5831/5832: To use this property, you must specify the the channelName of the [RfsaChannelBasedLO](nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string). An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaLocalOscillator.this[string]

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOOutPower property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaChannelBasedLO Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-lopllfractionalmodeenabled.html language=enus -->
## TOPIC 00043: LOPllFractionalModeEnabled

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-lopllfractionalmodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-lopllfractionalmodeenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to use fractional mode for the LO PLL. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaLOPllFractionalModeEnabled LOPllFractionalModeEnabled { get; set; }RemarksSpecifies the RfsaLOPllFractionalModeEnabled enumeration. PXIe-5830/5831/5832: To use this pr

### LOPllFractionalModeEnabled

Gets or sets whether to use fractional mode for the LO PLL.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaLOPllFractionalModeEnabled](nationalinstruments-modularinstruments-nirfsa-rfsalopllfractionalmodeenabled.html) LOPllFractionalModeEnabled { get; set; }

#### Remarks

Specifies the [RfsaLOPllFractionalModeEnabled](nationalinstruments-modularinstruments-nirfsa-rfsalopllfractionalmodeenabled.html) enumeration.

PXIe-5830/5831/5832: To use this property, you must specify the the channelName of the [RfsaChannelBasedLO](nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaLocalOscillator.this[string]

Note

For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this attribute is ignored if the PXIe-5653 is used as the LO source.

Fractional mode gives a finer frequency step resolution, but it may result in non-harmonic spurs. Refer to the *NI PXIe-5644R Specifications* or the *NI PXIe-5645R Specifications* for more information about fractional mode and non-harmonic spurs.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOPllFractionalModeEnabled property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaChannelBasedLO Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-losource.html language=enus -->
## TOPIC 00044: LOSource

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-losource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo-losource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the LO Source for the device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaLOSource LOSource { get; set; }RemarksSpecifies the RfsaLOSource enumeration. Specifies the LO signal source used to downconvert the RF input signal. If no signal downconversion is req

### LOSource

Gets or sets the LO Source for the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaLOSource](nationalinstruments-modularinstruments-nirfsa-rfsalosource.html) LOSource { get; set; }

#### Remarks

Specifies the [RfsaLOSource](nationalinstruments-modularinstruments-nirfsa-rfsalosource.html) enumeration.

Specifies the LO signal source used to downconvert the RF input signal. If no signal downconversion is required, this property is ignored.

To use this property for the PXIe-5830/5831/5832, you must specify the the channelName of the [RfsaChannelBasedLO](nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaLocalOscillator.this[string]

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOSource property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaChannelBasedLO Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo.html language=enus -->
## TOPIC 00045: RfsaChannelBasedLO Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelbasedlo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure channel based LO. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaChannelBasedLO : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionDownc

### RfsaChannelBasedLO Class

Represents the properties used to configure channel based LO.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaChannelBasedLO : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa_Help.html).

#### Properties

| Name | Description |
| --- | --- |
| DownconverterLoopBandwidth | Gets or sets the loop bandwidth of the downconverter tuning phase-locked loops (PLL). |
| LOExportEnabled | Gets or sets whether to enable the LO OUT terminals on the installed devices. |
| LOFrequency | Gets or sets the LO signal frequency for the configured center frequency. |
| LOInPower | Gets the power level, in dBm, expected at the LO terminal when the LOSource property is set to LOIn. |
| LOOutPower | Gets or sets the power level, in dBm, of the signal at the LO OUT terminal when the LOExportEnabled property is set to true. |
| LOPllFractionalModeEnabled | Gets or sets whether to use fractional mode for the LO PLL. |
| LOSource | Gets or sets the LO Source for the device. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsachannelcoupling.html language=enus -->
## TOPIC 00046: RfsaChannelCoupling Enumeration

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsachannelcoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsachannelcoupling.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RF input channel is AC-coupled or DC-coupled on a downconverter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic enum RfsaChannelCouplingMembersNameValueDescriptionAC(int)3001The RF input channel is AC-coupled. For low frequencies (less than 10 MHz), accura

### RfsaChannelCoupling Enumeration

Specifies whether the RF input channel is AC-coupled or DC-coupled on a downconverter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public enum RfsaChannelCoupling

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | (int)3001 | The RF input channel is AC-coupled. For low frequencies (less than 10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration. |
| DC | (int)3002 | The RF input channel is DC-coupled. NI-RFSA enforces a minimum RF attenuation for device protection. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-equals__object.html language=enus -->
## TOPIC 00047: Equals(object)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-equals__object.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaCoefficientInfo and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to the current inst

### Equals(object)

Determines whether the current instance of [RfsaCoefficientInfo](nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsaCoefficientInfo. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-equals__rfsacoefficientinfo.html language=enus -->
## TOPIC 00048: Equals(RfsaCoefficientInfo)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-equals__rfsacoefficientinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-equals__rfsacoefficientinfo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaCoefficientInfo and the RfsaCoefficientInfo object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaCoefficientInfo coefficientInfo)ParametersNameTypeDescriptioncoefficientInfoRfsaCoefficie

### Equals(RfsaCoefficientInfo)

Determines whether the current instance of [RfsaCoefficientInfo](nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html) and the [RfsaCoefficientInfo](nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaCoefficientInfo coefficientInfo)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| coefficientInfo | RfsaCoefficientInfo | Specifies the RfsaCoefficientInfo object to be compared to the current instance of RfsaCoefficientInfo. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-gain.html language=enus -->
## TOPIC 00049: Gain

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-gain.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the multiplier that you must use to scale data obtained from a peer-to-peer stream. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double Gain { get; }RemarksReturns a Double representing the multiplier that you must use to scale data obtained from a peer-to-peer stream.

### Gain

Gets the multiplier that you must use to scale data obtained from a peer-to-peer stream.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double Gain { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the multiplier that you must use to scale data obtained from a peer-to-peer stream.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-gethashcode.html language=enus -->
## TOPIC 00050: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsaCoefficientInfo. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of RfsaCoefficientInfo.

### GetHashCode()

Returns the hash code for the current instance of [RfsaCoefficientInfo](nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [RfsaCoefficientInfo](nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html).

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-offset.html language=enus -->
## TOPIC 00051: Offset

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-offset.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number that must be added to the data from a peer-to-peer stream after the gain has been applied, if you want to scale unscaled data. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double Offset { get; }RemarksReturns a Double representing the number that should be add

### Offset

Gets the number that must be added to the data from a peer-to-peer stream after the gain has been applied, if you want to scale unscaled data.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double Offset { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the number that should be added to the data from a peer-to-peer stream after the gain has been applied, if you want to scale unscaled data.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-operator_eq__rfsacoefficientinfo-rfsacoefficientinfo.html language=enus -->
## TOPIC 00052: operator==(RfsaCoefficientInfo, RfsaCoefficientInfo)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-operator_eq__rfsacoefficientinfo-rfsacoefficientinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-operator_eq__rfsacoefficientinfo-rfsacoefficientinfo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaCoefficientInfo are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaCoefficientInfo coefficientInfo1, RfsaCoefficientInfo coefficientInfo2)ParametersNameTypeDescriptioncoefficientInfo1RfsaCoefficientInfoSp

### operator==(RfsaCoefficientInfo, RfsaCoefficientInfo)

Checks whether the two instances of [RfsaCoefficientInfo](nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaCoefficientInfo coefficientInfo1, RfsaCoefficientInfo coefficientInfo2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| coefficientInfo1 | RfsaCoefficientInfo | Specifies a RfsaCoefficientInfo object. |
| coefficientInfo2 | RfsaCoefficientInfo | Specifies a RfsaCoefficientInfo object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-operator_neq__rfsacoefficientinfo-rfsacoefficientinfo.html language=enus -->
## TOPIC 00053: operator!=(RfsaCoefficientInfo, RfsaCoefficientInfo)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-operator_neq__rfsacoefficientinfo-rfsacoefficientinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-operator_neq__rfsacoefficientinfo-rfsacoefficientinfo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaCoefficientInfo are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaCoefficientInfo coefficientInfo1, RfsaCoefficientInfo coefficientInfo2)ParametersNameTypeDescriptioncoefficientInfo1RfsaCoefficientInfo

### operator!=(RfsaCoefficientInfo, RfsaCoefficientInfo)

Checks whether the two instances of [RfsaCoefficientInfo](nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaCoefficientInfo coefficientInfo1, RfsaCoefficientInfo coefficientInfo2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| coefficientInfo1 | RfsaCoefficientInfo | Specifies a RfsaCoefficientInfo object. |
| coefficientInfo2 | RfsaCoefficientInfo | Specifies a RfsaCoefficientInfo object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-reserved1.html language=enus -->
## TOPIC 00054: Reserved1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-reserved1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-reserved1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Reserved1 for coefficient info. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double Reserved1 { get; }RemarksReturns a Double representing the Reserved1 for coefficient info.

### Reserved1

Gets the Reserved1 for coefficient info.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double Reserved1 { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the Reserved1 for coefficient info.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-reserved2.html language=enus -->
## TOPIC 00055: Reserved2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-reserved2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo-reserved2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Reserved2 for coefficient info. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double Reserved2 { get; }RemarksReturns a Double representing the Reserved2 for coefficient info.

### Reserved2

Gets the Reserved2 for coefficient info.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double Reserved2 { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the Reserved2 for coefficient info.

Parent topic:

RfsaCoefficientInfo Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html language=enus -->
## TOPIC 00056: RfsaCoefficientInfo Data Structure

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacoefficientinfo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the coefficient info struct of the underlying driver. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic struct RfsaCoefficientInfoRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionGainGets the multiplier t

### RfsaCoefficientInfo Data Structure

Represents the coefficient info struct of the underlying driver.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public struct RfsaCoefficientInfo

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| Gain | Gets the multiplier that you must use to scale data obtained from a peer-to-peer stream. |
| Offset | Gets the number that must be added to the data from a peer-to-peer stream after the gain has been applied, if you want to scale unscaled data. |
| Reserved1 | Gets the Reserved1 for coefficient info. |
| Reserved2 | Gets the Reserved2 for coefficient info. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(RfsaCoefficientInfo) | Determines whether the current instance of RfsaCoefficientInfo and the RfsaCoefficientInfo object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsaCoefficientInfo and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaCoefficientInfo. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(RfsaCoefficientInfo, RfsaCoefficientInfo) | Checks whether the two instances of RfsaCoefficientInfo are unequal. |
| operator==(RfsaCoefficientInfo, RfsaCoefficientInfo) | Checks whether the two instances of RfsaCoefficientInfo are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-acquisitiontype.html language=enus -->
## TOPIC 00057: AcquisitionType

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-acquisitiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-acquisitiontype.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the session to either acquire I/Q data or to compute a power spectrum over the specified frequency range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaAcquisitionType AcquisitionType { get; set; }RemarksSpecifies the RfsaAcquisitionType enumeration. Exception

### AcquisitionType

Gets or sets the session to either acquire I/Q data or to compute a power spectrum over the specified frequency range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaAcquisitionType](nationalinstruments-modularinstruments-nirfsa-rfsaacquisitiontype.html) AcquisitionType { get; set; }

#### Remarks

Specifies the [RfsaAcquisitionType](nationalinstruments-modularinstruments-nirfsa-rfsaacquisitiontype.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AcquisitionType property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-basicconfigurationlist.html language=enus -->
## TOPIC 00058: BasicConfigurationList

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-basicconfigurationlist.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-basicconfigurationlist.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the configuration list used to configure RF list mode operations with the NI-RFSA. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaBasicConfigurationList BasicConfigurationList { get; }RemarksReturns an object of type RfsaBasicConfigurationList.

### BasicConfigurationList

Gets the configuration list used to configure RF list mode operations with the NI-RFSA.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaBasicConfigurationList](nationalinstruments-modularinstruments-nirfsa-rfsabasicconfigurationlist.html) BasicConfigurationList { get; }

#### Remarks

Returns an object of type [RfsaBasicConfigurationList](nationalinstruments-modularinstruments-nirfsa-rfsabasicconfigurationlist.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-calibrationdigitizerid.html language=enus -->
## TOPIC 00059: CalibrationDigitizerId

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-calibrationdigitizerid.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-calibrationdigitizerid.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the digitizer ID used during self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic string CalibrationDigitizerId { get; }RemarksSpecifies the String that represents the calibration digitizer ID. The default value is "" (empty string). Supported Devices: NI 5603/

### CalibrationDigitizerId

Gets the digitizer ID used during self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public string CalibrationDigitizerId { get; }

#### Remarks

Specifies the [String](https://learn.microsoft.com/dotnet/api/system.string) that represents the calibration digitizer ID. The default value is "" (empty string).

Supported Devices: NI 5603/5605/5606 (external digitizer mode)

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CalibrationDigitizerId property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-deembedding.html language=enus -->
## TOPIC 00060: Deembedding

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-deembedding.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-deembedding.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Deembedding sub-object used to configure Deembedding. A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeembedding.this[string]. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaDeembedding Deembedding { get; }RemarksReturns an

### Deembedding

Gets the Deembedding sub-object used to configure Deembedding. A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeembedding.this[string].

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsadeembedding.html) Deembedding { get; }

#### Remarks

Returns an object of type [RfsaDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsadeembedding.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-digitizersampleclock.html language=enus -->
## TOPIC 00061: DigitizerSampleClock

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-digitizersampleclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-digitizersampleclock.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an instance of the Digitizer Sample Clock. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaDigitizerSampleClock DigitizerSampleClock { get; }RemarksReturns an object of type RfsaDigitizerSampleClock.

### DigitizerSampleClock

Gets an instance of the Digitizer Sample Clock.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaDigitizerSampleClock](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock.html) DigitizerSampleClock { get; }

#### Remarks

Returns an object of type [RfsaDigitizerSampleClock](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-events.html language=enus -->
## TOPIC 00062: Events

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-events.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-events.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Events sub-object used to configure hardware events. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaEvents Events { get; }RemarksReturns an object of type RfsaEvents.

### Events

Gets the Events sub-object used to configure hardware events.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaEvents](nationalinstruments-modularinstruments-nirfsa-rfsaevents.html) Events { get; }

#### Remarks

Returns an object of type [RfsaEvents](nationalinstruments-modularinstruments-nirfsa-rfsaevents.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-exportsignal__rfsasignaltype-rfsasignalidentifier-rfsaoutputterminal.html language=enus -->
## TOPIC 00063: ExportSignal(RfsaSignalType, RfsaSignalIdentifier, RfsaOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-exportsignal__rfsasignaltype-rfsasignalidentifier-rfsaoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-exportsignal__rfsasignaltype-rfsasignalidentifier-rfsaoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (triggers, clocks, and events) to the specified output terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void ExportSignal(RfsaSignalType signal, RfsaSignalIdentifier signalIdentifier, RfsaOutputTerminal outputTerminal)ParametersNameTypeDescriptionsignalRf

### ExportSignal(RfsaSignalType, RfsaSignalIdentifier, RfsaOutputTerminal)

Routes signals (triggers, clocks, and events) to the specified output terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void ExportSignal(RfsaSignalType signal, RfsaSignalIdentifier signalIdentifier, RfsaOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signal | RfsaSignalType | Specifies the RfsaSignalType to route. |
| signalIdentifier | RfsaSignalIdentifier | Specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions. |
| outputTerminal | RfsaOutputTerminal | Specifies the RfsaOutputTerminal where the signal will be exported. You can also choose not to export any signal. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportSignal method was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-iq.html language=enus -->
## TOPIC 00064: IQ

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-iq.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-iq.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the IQ sub-object used to configure the RF vector signal analyzer for an I/Q acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaIQAcquisitionConfiguration IQ { get; }RemarksReturns an object of type RfsaIQAcquisitionConfiguration.

### IQ

Gets the IQ sub-object used to configure the RF vector signal analyzer for an I/Q acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaIQAcquisitionConfiguration](nationalinstruments-modularinstruments-nirfsa-rfsaiqacquisitionconfiguration.html) IQ { get; }

#### Remarks

Returns an object of type [RfsaIQAcquisitionConfiguration](nationalinstruments-modularinstruments-nirfsa-rfsaiqacquisitionconfiguration.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-iqinportchannels.html language=enus -->
## TOPIC 00065: IQInPortChannels

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-iqinportchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-iqinportchannels.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the IQInPortChannels sub-object used to access the IQInPort property. To retrieve channel-specific objects of Type RfsaIQInPortChannel, pass the channel name to the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaIQInPortChannelCollection.this[string]. SyntaxNamespace: NationalInstrum

### IQInPortChannels

Gets the IQInPortChannels sub-object used to access the IQInPort property. To retrieve channel-specific objects of Type [RfsaIQInPortChannel](nationalinstruments-modularinstruments-nirfsa-rfsaiqinportchannel.html), pass the channel name to the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaIQInPortChannelCollection.this[string].

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaIQInPortChannelCollection](nationalinstruments-modularinstruments-nirfsa-rfsaiqinportchannelcollection.html) IQInPortChannels { get; }

#### Remarks

Returns an object of type [RfsaIQInPortChannelCollection](nationalinstruments-modularinstruments-nirfsa-rfsaiqinportchannelcollection.html)

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-noisesourcepowerenabled.html language=enus -->
## TOPIC 00066: NoiseSourcePowerEnabled

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-noisesourcepowerenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-noisesourcepowerenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to enable the 28 V DC source, in dB, on the device front panel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaNoiseSourcePowerEnabled NoiseSourcePowerEnabled { get; set; }RemarksSupported Devices: NI 5606, NI 5668R Specifies the RfsaNoiseSourcePowerEna

### NoiseSourcePowerEnabled

Gets or sets whether to enable the 28 V DC source, in dB, on the device front panel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaNoiseSourcePowerEnabled](nationalinstruments-modularinstruments-nirfsa-rfsanoisesourcepowerenabled.html) NoiseSourcePowerEnabled { get; set; }

#### Remarks

Supported Devices: NI 5606, NI 5668R

Specifies the [RfsaNoiseSourcePowerEnabled](nationalinstruments-modularinstruments-nirfsa-rfsanoisesourcepowerenabled.html) enumeration.

The default value is [Disabled](nationalinstruments-modularinstruments-nirfsa-rfsanoisesourcepowerenabled.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The NoiseSourcePowerEnabled property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-referenceclock.html language=enus -->
## TOPIC 00067: ReferenceClock

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-referenceclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-referenceclock.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ReferenceClock sub-object used to configure reference clock to ensure that the device is operating from a common time base. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaReferenceClock ReferenceClock { get; }RemarksReturns an object of type RfsaReferenceClock.

### ReferenceClock

Gets the ReferenceClock sub-object used to configure reference clock to ensure that the device is operating from a common time base.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaReferenceClock](nationalinstruments-modularinstruments-nirfsa-rfsareferenceclock.html) ReferenceClock { get; }

#### Remarks

Returns an object of type [RfsaReferenceClock](nationalinstruments-modularinstruments-nirfsa-rfsareferenceclock.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-signalpath.html language=enus -->
## TOPIC 00068: SignalPath

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-signalpath.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-signalpath.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SignalPath sub-object used to configure the signal path from the RF vector signal analyzer front panel to the PXI controller. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaSignalPath SignalPath { get; }RemarksReturns an object of type RfsaSignalPath.

### SignalPath

Gets the SignalPath sub-object used to configure the signal path from the RF vector signal analyzer front panel to the PXI controller.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaSignalPath](nationalinstruments-modularinstruments-nirfsa-rfsasignalpath.html) SignalPath { get; }

#### Remarks

Returns an object of type [RfsaSignalPath](nationalinstruments-modularinstruments-nirfsa-rfsasignalpath.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-spectrum.html language=enus -->
## TOPIC 00069: Spectrum

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-spectrum.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-spectrum.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Spectrum sub-object used to configure and acquire data in the spectrum mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaSpectrumAcquisitionConfiguration Spectrum { get; }RemarksReturns an object of type RfsaSpectrumAcquisitionConfiguration.

### Spectrum

Gets the Spectrum sub-object used to configure and acquire data in the spectrum mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaSpectrumAcquisitionConfiguration](nationalinstruments-modularinstruments-nirfsa-rfsaspectrumacquisitionconfiguration.html) Spectrum { get; }

#### Remarks

Returns an object of type [RfsaSpectrumAcquisitionConfiguration](nationalinstruments-modularinstruments-nirfsa-rfsaspectrumacquisitionconfiguration.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-triggers.html language=enus -->
## TOPIC 00070: Triggers

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-triggers.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Triggers sub-object used to configure the NI-RFSA triggers. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaTriggers Triggers { get; }RemarksReturns an object of type RfsaTriggers.

### Triggers

Gets the Triggers sub-object used to configure the NI-RFSA triggers.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaTriggers](nationalinstruments-modularinstruments-nirfsa-rfsatriggers.html) Triggers { get; }

#### Remarks

Returns an object of type [RfsaTriggers](nationalinstruments-modularinstruments-nirfsa-rfsatriggers.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-vertical.html language=enus -->
## TOPIC 00071: Vertical

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-vertical.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration-vertical.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Vertical sub-object used to configure vertical. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaVertical Vertical { get; }RemarksReturns an object of type RfsaVertical.

### Vertical

Gets the Vertical sub-object used to configure vertical.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaVertical](nationalinstruments-modularinstruments-nirfsa-rfsavertical.html) Vertical { get; }

#### Remarks

Returns an object of type [RfsaVertical](nationalinstruments-modularinstruments-nirfsa-rfsavertical.html).

Parent topic:

RfsaConfiguration Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration.html language=enus -->
## TOPIC 00072: RfsaConfiguration Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfiguration.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides objects of specific types used to configure the NI-RFSA. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaConfiguration : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionAc

### RfsaConfiguration Class

Provides objects of specific types used to configure the NI-RFSA.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaConfiguration : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| AcquisitionType | Gets or sets the session to either acquire I/Q data or to compute a power spectrum over the specified frequency range. |
| BasicConfigurationList | Gets the configuration list used to configure RF list mode operations with the NI-RFSA. |
| CalibrationDigitizerId | Gets the digitizer ID used during self-calibration. |
| Deembedding | Gets the Deembedding sub-object used to configure Deembedding. A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeembedding.this[string]. |
| DigitizerSampleClock | Gets an instance of the Digitizer Sample Clock. |
| Events | Gets the Events sub-object used to configure hardware events. |
| IQ | Gets the IQ sub-object used to configure the RF vector signal analyzer for an I/Q acquisition. |
| IQInPortChannels | Gets the IQInPortChannels sub-object used to access the IQInPort property. To retrieve channel-specific objects of Type RfsaIQInPortChannel, pass the channel name to the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaIQInPortChannelCollection.this[string]. |
| NoiseSourcePowerEnabled | Gets or sets whether to enable the 28 V DC source, in dB, on the device front panel. |
| ReferenceClock | Gets the ReferenceClock sub-object used to configure reference clock to ensure that the device is operating from a common time base. |
| SignalPath | Gets the SignalPath sub-object used to configure the signal path from the RF vector signal analyzer front panel to the PXI controller. |
| Spectrum | Gets the Spectrum sub-object used to configure and acquire data in the spectrum mode. |
| Triggers | Gets the Triggers sub-object used to configure the NI-RFSA triggers. |
| Vertical | Gets the Vertical sub-object used to configure vertical. |

#### Methods

| Name | Description |
| --- | --- |
| ExportSignal(RfsaSignalType, RfsaSignalIdentifier, RfsaOutputTerminal) | Routes signals (triggers, clocks, and events) to the specified output terminal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationlistproperties.html language=enus -->
## TOPIC 00073: RfsaConfigurationListProperties Enumeration

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationlistproperties.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationlistproperties.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configuration list properties that the user can change between configuration list steps. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic enum RfsaConfigurationListPropertiesMembersNameValueDescriptionIQCarrierFrequencyRefers to the CarrierFrequency property. Refere

### RfsaConfigurationListProperties Enumeration

Specifies the configuration list properties that the user can change between configuration list steps.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public enum RfsaConfigurationListProperties

#### Members

| Name | Value | Description |
| --- | --- | --- |
| IQCarrierFrequency |  | Refers to the CarrierFrequency property. |
| ReferenceLevel |  | Refers to the ReferenceLevel property. |
| DownconverterCenterFrequency |  | Refers to the DownconverterCenterFrequency property. |
| DownConverterCenterFrequency |  | Refers to the DownconverterCenterFrequency property. Use DownconverterCenterFrequency instead of this enumeration constant. |
| IQPowerEdgeRefTriggerLevel |  | Refers to the Level property. |
| TimerEventInterval |  | Refers to the TimerEventInterval property. |
| FrequencySettlingTime |  | Refers to the FrequencySettlingTime property. |
| MechanicalAttenuation |  | Refers to the MechanicalAttenuation property. |
| MechanicalAttenuationEnabled |  | Refers to the MechanicalAttenuatorEnabled property. Use MechanicalAttenuatorEnabled instead of this enumeration constant. |
| MechanicalAttenuatorEnabled |  | Refers to the MechanicalAttenuatorEnabled property. |
| Attenuation |  | Refers to the RFAttenuation property. Use RFAttenuation instead of this enumeration constant. |
| RFAttenuation |  | Refers to the RFAttenuation property. |
| RFPreampEnabled |  | Refers to the RFPreampEnabled property. |
| IFOutputPowerLevel | (int)RfsaPropertyId.IfOutputPowerLevel | Refers to the IFOutputPowerLevel property. |
| IFOutputPowerLevelOffset | (int)RfsaPropertyId.IfOutputPowerLevelOffset | Refers to the IFOutputPowerLevelOffset property. |
| MinimumAcpr | (int)RfsaPropertyId.MinimumAcpr | Refers to the MinimumAcpr property. |
| ExternalGain | (int)RfsaPropertyId.ExternalGain | Refers to the ExternalGain property. |
| DeviceInstantaneousBandwidth |  | Refers to the DeviceInstantaneousBandwidth property. |
| DownconverterPreselectorEnabled |  | Refers to the DownconverterPreselectorEnabled property. |
| OspDataScalingFactor |  | Refers to the OspDataScalingFactor property. |
| RFPreselectorFilter |  | Refers to the RFPreselectorFilter property. |
| IFFilterBandwidth |  | Refers to the IFFilterBandwidth property. |
| LowFrequencyBypassEnabled |  | Refers to the LowFrequencyBypassEnabled property. |
| NotchFilterEnabled |  | Refers to the NotchFilterEnabled property. |
| DdcReferenceTriggerOverride |  | Refers to the DdcReferenceTriggerOverride property. |
| MinimumReconfigurationTime |  | Refers to the MinimumReconfigurationTime property. |
| NumberOfSamples |  | Refers to the NumberOfSamples property. |
| ChannelCoupling |  | Refers to the ChannelCoupling property. |
| IqInPortCarrierFrequency |  | Refers to the CarrierFrequency property. |
| IqInPortVerticalRange |  | Refers to the VerticalRange property. |
| DownconverterFrequencyOffset |  | Refers to the DownconverterFrequencyOffset property. |
| RFOutLOExportEnabled |  | Refers to the RFOutLOExportEnabled property. |
| LOSource |  | Refers to the LOSource property. |
| DownconverterFrequencyOffsetMode |  | Refers to the DownconverterFrequencyOffsetMode property. |
| SignalBandwidth |  | Refers to the SignalBandwidth property. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationliststeptrigger-digitaledge.html language=enus -->
## TOPIC 00074: DigitalEdge

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationliststeptrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationliststeptrigger-digitaledge.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RfsaDigitalEdgeConfigurationListStepTrigger sub-object to configure the digital edge of the RfsaConfigurationListStepTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaDigitalEdgeConfigurationListStepTrigger DigitalEdge { get; }RemarksReturns an object of type

### DigitalEdge

Gets the [RfsaDigitalEdgeConfigurationListStepTrigger](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptrigger.html) sub-object to configure the digital edge of the [RfsaConfigurationListStepTrigger](nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationliststeptrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaDigitalEdgeConfigurationListStepTrigger](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptrigger.html) DigitalEdge { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeConfigurationListStepTrigger](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptrigger.html).

Parent topic:

RfsaConfigurationListStepTrigger Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationliststeptrigger.html language=enus -->
## TOPIC 00075: RfsaConfigurationListStepTrigger Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationliststeptrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaconfigurationliststeptrigger.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure the Configuration List Step trigger. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaConfigurationListStepTrigger : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Hel

### RfsaConfigurationListStepTrigger Class

Represents the properties used to configure the Configuration List Step trigger.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaConfigurationListStepTrigger : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the RfsaDigitalEdgeConfigurationListStepTrigger sub-object to configure the digital edge of the RfsaConfigurationListStepTrigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsacontiguousmultirecordenabled.html language=enus -->
## TOPIC 00076: RfsaContiguousMultiRecordEnabled Enumeration

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsacontiguousmultirecordenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsacontiguousmultirecordenabled.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable contiguous multirecord acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic enum RfsaContiguousMultiRecordEnabledMembersNameValueDescriptionDisabled(int)1900Disables contiguous multirecord acquisition. Enabled(int)1901Enables contiguous multir

### RfsaContiguousMultiRecordEnabled Enumeration

Specifies whether to enable contiguous multirecord acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public enum RfsaContiguousMultiRecordEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | (int)1900 | Disables contiguous multirecord acquisition. |
| Enabled | (int)1901 | Enables contiguous multirecord acquisition. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationlinear__string-rfsalinearinterpolationformat.html language=enus -->
## TOPIC 00077: ConfigureDeembeddingTableInterpolationLinear(string, RfsaLinearInterpolationFormat)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationlinear__string-rfsalinearinterpolationformat.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationlinear__string-rfsalinearinterpolationformat.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the linear interpolation method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void ConfigureDeembeddingTableInterpolationLinear(string tableName, RfsaLinearInterpolationFormat format)RemarksIf the carrier frequency does not match a row in the de-embedding table, this

### ConfigureDeembeddingTableInterpolationLinear(string, RfsaLinearInterpolationFormat)

Selects the linear interpolation method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void ConfigureDeembeddingTableInterpolationLinear(string tableName, RfsaLinearInterpolationFormat format)

#### Remarks

If the carrier frequency does not match a row in the de-embedding table, this method performs a linear interpolation based on the entries above and below in the de-embedding table to determine the parameters used for de-embedding.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. |
| format | RfsaLinearInterpolationFormat | Specifies the format of parameters to interpolate. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationnearest__string.html language=enus -->
## TOPIC 00078: ConfigureDeembeddingTableInterpolationNearest(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationnearest__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationnearest__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the nearest interpolation method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void ConfigureDeembeddingTableInterpolationNearest(string tableName)RemarksThe parameters of the table nearest the carrier frequency are used for de-embedding. ParametersNameTypeDescription

### ConfigureDeembeddingTableInterpolationNearest(string)

Selects the nearest interpolation method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void ConfigureDeembeddingTableInterpolationNearest(string tableName)

#### Remarks

The parameters of the table nearest the carrier frequency are used for de-embedding.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationspline__string.html language=enus -->
## TOPIC 00079: ConfigureDeembeddingTableInterpolationSpline(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationspline__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-configuredeembeddingtableinterpolationspline__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the spline interpolation method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void ConfigureDeembeddingTableInterpolationSpline(string tableName)RemarksIf the carrier frequency does not match a row in the de-embedding table, this method performs a spline interpolation

### ConfigureDeembeddingTableInterpolationSpline(string)

Selects the spline interpolation method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void ConfigureDeembeddingTableInterpolationSpline(string tableName)

#### Remarks

If the carrier frequency does not match a row in the de-embedding table, this method performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertablearray__string-double_arr1-complexdouble_arr3-rfsasparameterorientation.html language=enus -->
## TOPIC 00080: CreateDeembeddingSParameterTableArray(string, double[], ComplexDouble, RfsaSParameterOrientation)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertablearray__string-double_arr1-complexdouble_arr3-rfsasparameterorientation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertablearray__string-double_arr1-complexdouble_arr3-rfsasparameterorientation.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an s-parameter de-embedding table from the input data. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void CreateDeembeddingSParameterTableArray(string tableName, double[] frequencies, ComplexDouble[,,] sParameterTable, RfsaSParameterOrientation sParameterOrientation)Re

### CreateDeembeddingSParameterTableArray(string, double[], ComplexDouble, RfsaSParameterOrientation)

Creates an s-parameter de-embedding table from the input data.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void CreateDeembeddingSParameterTableArray(string tableName, double[] frequencies, ComplexDouble[,,] sParameterTable, RfsaSParameterOrientation sParameterOrientation)

#### Remarks

If only one table is created, the table is automatically selected and used to de-embed the measurement.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. The name of the table must be unique. |
| frequencies | double[] | Specifies the frequencies for the S-parameter table rows. Frequencies must be unique and in ascending order. |
| sParameterTable | ComplexDouble | Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22. |
| sParameterOrientation | RfsaSParameterOrientation | Specifies the orientation of the data in the S2P file. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertables2pfile__string-string-rfsasparameterorientation.html language=enus -->
## TOPIC 00081: CreateDeembeddingSParameterTableS2pFile(string, string, RfsaSParameterOrientation)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertables2pfile__string-string-rfsasparameterorientation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertables2pfile__string-string-rfsasparameterorientation.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an S-parameter de-embedding table based on the specified S2P file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void CreateDeembeddingSParameterTableS2pFile(string tableName, string s2pFilePath, RfsaSParameterOrientation sParameterOrientation)RemarksIf only one table

### CreateDeembeddingSParameterTableS2pFile(string, string, RfsaSParameterOrientation)

Creates an S-parameter de-embedding table based on the specified S2P file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void CreateDeembeddingSParameterTableS2pFile(string tableName, string s2pFilePath, RfsaSParameterOrientation sParameterOrientation)

#### Remarks

If only one table is created, the table is automatically selected and used to de-embed the measurement.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. The name of the table must be unique. If you use the same name as an existing table, the table is replaced. |
| s2pFilePath | string | Specifies the path to the S2P file that contains de-embedding information. |
| sParameterOrientation | RfsaSParameterOrientation | Specifies the orientation of the data in the S2P file. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingcompensationgain.html language=enus -->
## TOPIC 00082: DeembeddingCompensationGain

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingcompensationgain.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingcompensationgain.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double DeembeddingCompensationGain { get; }RemarksSpecifies a Double representing the de-embeddin

### DeembeddingCompensationGain

Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double DeembeddingCompensationGain { get; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the de-embedding compensation gain.

To use this property, you must set the channelName of the [RfsaChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding.html) sub-object to specify the name of the port to configure for de-embedding.

A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeembedding.this[string].

If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT. Use the [CreateDeembeddingSParameterTableS2pFile](nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertables2pfile__string-string-rfsasparameterorientation.html) to create tables.

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingselectedtable.html language=enus -->
## TOPIC 00083: DeembeddingSelectedTable

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingselectedtable.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingselectedtable.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the de-embedding table to apply to the measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic string DeembeddingSelectedTable { get; set; }RemarksSpecifies a String representing the de-embedding type.To use this property, you must set the channelName of the R

### DeembeddingSelectedTable

Gets or sets the de-embedding table to apply to the measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public string DeembeddingSelectedTable { get; set; }

#### Remarks

Specifies a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the de-embedding type.

To use this property, you must set the channelName of the [RfsaChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding.html) sub-object to specify the name of the port to configure for de-embedding.

A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeembedding.this[string].

If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT. Use the [CreateDeembeddingSParameterTableS2pFile](nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-createdeembeddingsparametertables2pfile__string-string-rfsasparameterorientation.html) to create tables.

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingtype.html language=enus -->
## TOPIC 00084: DeembeddingType

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingtype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deembeddingtype.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of de-embedding to apply to measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaDeembeddingType DeembeddingType { get; set; }RemarksSpecifies a RfsaDeembeddingType representing the de-embedding type.To use this property, you must set the chann

### DeembeddingType

Gets or sets the type of de-embedding to apply to measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaDeembeddingType](nationalinstruments-modularinstruments-nirfsa-rfsadeembeddingtype.html) DeembeddingType { get; set; }

#### Remarks

Specifies a [RfsaDeembeddingType](nationalinstruments-modularinstruments-nirfsa-rfsadeembeddingtype.html) representing the de-embedding type.

To use this property, you must set the channelName of the [RfsaChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding.html) sub-object to specify the name of the port to configure for de-embedding.

A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsa.RfsaDeembedding.this[string].

If you set this property to Scalar or Vector, NI-RFSA adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deletealldeembeddingtables.html language=enus -->
## TOPIC 00085: DeleteAllDeembeddingTables()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deletealldeembeddingtables.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deletealldeembeddingtables.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all configured de-embedding tables for the session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void DeleteAllDeembeddingTables()

### DeleteAllDeembeddingTables()

Deletes all configured de-embedding tables for the session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void DeleteAllDeembeddingTables()

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deletedeembeddingtable__string.html language=enus -->
## TOPIC 00086: DeleteDeembeddingTable(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deletedeembeddingtable__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-deletedeembeddingtable__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the selected de-embedding table. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void DeleteDeembeddingTable(string tableName)ParametersNameTypeDescriptiontableNamestringSpecifies the name of the table.

### DeleteDeembeddingTable(string)

Deletes the selected de-embedding table.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void DeleteDeembeddingTable(string tableName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-getdeembeddingsparameters__ref.html language=enus -->
## TOPIC 00087: GetDeembeddingSParameters(ref ComplexDouble)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-getdeembeddingsparameters__ref.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-getdeembeddingsparameters__ref.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-parameters used for de-embedding a measurement. This includes interpolation of the parameters based on the configured carrier frequency. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void GetDeembeddingSParameters(ref ComplexDouble[,] sParameters)RemarksThis meth

### GetDeembeddingSParameters(ref ComplexDouble)

Returns the S-parameters used for de-embedding a measurement. This includes interpolation of the parameters based on the configured carrier frequency.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void GetDeembeddingSParameters(ref ComplexDouble[,] sParameters)

#### Remarks

This method returns an empty array if no de-embedding is done.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sParameters | ref ComplexDouble | Returns an array of S-parameters. The S-parameters are returned in the following order, s11, s12, s21, s22. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-this__string.html language=enus -->
## TOPIC 00088: this[string channelName]

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding-this__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RfsaChannelBasedDeembedding sub-object to configure channel based Deembedding properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaChannelBasedDeembedding this[string channelName] { get; }RemarksReturns an object of type RfsaChannelBasedDeembedding. Parameter

### this[string channelName]

Gets the [RfsaChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding.html) sub-object to configure channel based Deembedding properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding.html) this[string channelName] { get; }

#### Remarks

Returns an object of type [RfsaChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsa-rfsachannelbaseddeembedding.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | Specifies the port to be used for the channel based properties. |

Parent topic:

RfsaDeembedding Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembedding.html language=enus -->
## TOPIC 00089: RfsaDeembedding Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembedding.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembedding.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties and methods used to configure Deembedding. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaDeembedding : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionD

### RfsaDeembedding Class

Represents the properties and methods used to configure Deembedding.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaDeembedding : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa_Help.html).

#### Properties

| Name | Description |
| --- | --- |
| DeembeddingCompensationGain | Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables. |
| DeembeddingSelectedTable | Gets or sets the de-embedding table to apply to the measurements. |
| DeembeddingType | Gets or sets the type of de-embedding to apply to measurements. |
| this[string channelName] | Gets the RfsaChannelBasedDeembedding sub-object to configure channel based Deembedding properties. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureDeembeddingTableInterpolationLinear(string, RfsaLinearInterpolationFormat) | Selects the linear interpolation method. |
| ConfigureDeembeddingTableInterpolationNearest(string) | Selects the nearest interpolation method. |
| ConfigureDeembeddingTableInterpolationSpline(string) | Selects the spline interpolation method. |
| CreateDeembeddingSParameterTableArray(string, double[], ComplexDouble, RfsaSParameterOrientation) | Creates an s-parameter de-embedding table from the input data. |
| CreateDeembeddingSParameterTableS2pFile(string, string, RfsaSParameterOrientation) | Creates an S-parameter de-embedding table based on the specified S2P file. |
| DeleteAllDeembeddingTables() | Deletes all configured de-embedding tables for the session. |
| DeleteDeembeddingTable(string) | Deletes the selected de-embedding table. |
| GetDeembeddingSParameters(ref ComplexDouble) | Returns the S-parameters used for de-embedding a measurement. This includes interpolation of the parameters based on the configured carrier frequency. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadeembeddingtype.html language=enus -->
## TOPIC 00090: RfsaDeembeddingType Enumeration

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadeembeddingtype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadeembeddingtype.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of de-embedding to apply to measurements on the specified port. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic enum RfsaDeembeddingTypeMembersNameValueDescriptionNone(int)3900De-embedding is not applied to the measurement. Scalar(int)3901De-embeds the measure

### RfsaDeembeddingType Enumeration

Specifies the type of de-embedding to apply to measurements on the specified port.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public enum RfsaDeembeddingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | (int)3900 | De-embedding is not applied to the measurement. |
| Scalar | (int)3901 | De-embeds the measurement using only the gain term. |
| Vector | (int)3902 | De-embeds the measurement using the gain term and the reflection term. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-dio7.html language=enus -->
## TOPIC 00091: Dio7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-dio7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeAdvanceTriggerSource Dio7 { get; }RemarksReturns an object of type RfsaDigitalEdgeAdvanceTriggerSource representing the string "DIO/PFI7".

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) representing the string "DIO/PFI7".

Parent topic:

RfsaDigitalEdgeAdvanceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-dioo.html language=enus -->
## TOPIC 00092: DioO

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-dioo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeAdvanceTriggerSource DioO { get; }RemarksReturns an object of type RfsaDigitalEdgeAdvanceTriggerSource representing the string "DIO/PFI0".

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) DioO { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) representing the string "DIO/PFI0".

Parent topic:

RfsaDigitalEdgeAdvanceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-fromstring__string.html language=enus -->
## TOPIC 00093: FromString(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-fromstring__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsaDigitalEdgeAdvanceTriggerSource object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeAdvanceTriggerSource FromString(string source)ParametersNameTypeDescriptionsourcestringSpecifies a string representing the sourc

### FromString(string)

Creates an [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies a string representing the source of RfsaDigitalEdgeAdvanceTrigger. |

#### Returns

Returns an object of type [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html).

Parent topic:

RfsaDigitalEdgeAdvanceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-operator_eq__rfsadigitaledgeadvancetriggersource-rfsadigitaledgeadvancetriggersource.html language=enus -->
## TOPIC 00094: operator==(RfsaDigitalEdgeAdvanceTriggerSource, RfsaDigitalEdgeAdvanceTriggerSource)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-operator_eq__rfsadigitaledgeadvancetriggersource-rfsadigitaledgeadvancetriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-operator_eq__rfsadigitaledgeadvancetriggersource-rfsadigitaledgeadvancetriggersource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaDigitalEdgeAdvanceTriggerSource are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaDigitalEdgeAdvanceTriggerSource source1, RfsaDigitalEdgeAdvanceTriggerSource source2)ParametersNameTypeDescriptionsource1

### operator==(RfsaDigitalEdgeAdvanceTriggerSource, RfsaDigitalEdgeAdvanceTriggerSource)

Checks whether the two instances of [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaDigitalEdgeAdvanceTriggerSource source1, RfsaDigitalEdgeAdvanceTriggerSource source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsaDigitalEdgeAdvanceTriggerSource | Specifies a RfsaDigitalEdgeAdvanceTriggerSource object. |
| source2 | RfsaDigitalEdgeAdvanceTriggerSource | Specifies a RfsaDigitalEdgeAdvanceTriggerSource object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDigitalEdgeAdvanceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-pxiedstarb.html language=enus -->
## TOPIC 00095: PXIeDStarB

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-pxiedstarb.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource-pxiedstarb.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeAdvanceTriggerSource PXIeDStarB { get; }RemarksReturns an

### PXIeDStarB

Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) PXIeDStarB { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeAdvanceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html) representing the string "PXIe_DStarB".

Parent topic:

RfsaDigitalEdgeAdvanceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html language=enus -->
## TOPIC 00096: RfsaDigitalEdgeAdvanceTriggerSource Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetriggersource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source terminal for RfsaDigitalEdgeAdvanceTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaDigitalEdgeAdvanceTriggerSourceRemarksSee Source. PropertiesNameDescriptionDio1Gets the source terminal when the trigger is received on the

### RfsaDigitalEdgeAdvanceTriggerSource Class

Represents the source terminal for [RfsaDigitalEdgeAdvanceTrigger](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaDigitalEdgeAdvanceTriggerSource

#### Remarks

See [Source](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeadvancetrigger-source.html).

#### Properties

| Name | Description |
| --- | --- |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| Pfi0 | Gets the source terminal when the trigger is received on the PFI 0 connector. |
| Pfi1 | Gets the source terminal when the trigger is received on the PFI 1 connector. |
| PXIeDStarB | Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. |
| PxiStarLine | Gets the source terminal when the trigger is received on the PXI Star trigger line. |
| PxiTriggerLine0 | Gets the source terminal when the trigger is received on the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the source terminal when the trigger is received on the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the source terminal when the trigger is received on the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the source terminal when the trigger is received on the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the source terminal when the trigger is received on the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the source terminal when the trigger is received on the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the source terminal when the trigger is received on the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the source terminal when the trigger is received on the PXI trigger line 7. |
| TimerEvent | Gets the source terminal when the trigger is received from the Timer event. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsaDigitalEdgeAdvanceTriggerSource object from the specified string. |
| Equals(RfsaDigitalEdgeAdvanceTriggerSource) | Determines whether the current instance of RfsaDigitalEdgeAdvanceTriggerSource and the RfsaDigitalEdgeAdvanceTriggerSource object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsaDigitalEdgeAdvanceTriggerSource and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaDigitalEdgeAdvanceTriggerSource. |
| ToString() | Converts the current instance of RfsaDigitalEdgeAdvanceTriggerSource to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsaDigitalEdgeAdvanceTriggerSource(string) | Converts the specified string to the equivalent RfsaDigitalEdgeAdvanceTriggerSource object. |
| operator string(RfsaDigitalEdgeAdvanceTriggerSource) | Converts the RfsaDigitalEdgeAdvanceTriggerSource object to an equivalent string. |
| operator!=(RfsaDigitalEdgeAdvanceTriggerSource, RfsaDigitalEdgeAdvanceTriggerSource) | Check whether the two instances of RfsaDigitalEdgeAdvanceTriggerSource are unequal. |
| operator==(RfsaDigitalEdgeAdvanceTriggerSource, RfsaDigitalEdgeAdvanceTriggerSource) | Checks whether the two instances of RfsaDigitalEdgeAdvanceTriggerSource are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio2.html language=enus -->
## TOPIC 00097: Dio2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeArmReferenceTriggerSource Dio2 { get; }RemarksReturns an object of type RfsaDigitalEdgeArmReferenceTriggerSource representing the string "

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) representing the string "DIO/PFI2".

Parent topic:

RfsaDigitalEdgeArmReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio3.html language=enus -->
## TOPIC 00098: Dio3

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio3.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeArmReferenceTriggerSource Dio3 { get; }RemarksReturns an object of type RfsaDigitalEdgeArmReferenceTriggerSource representing the string "

### Dio3

Gets the source terminal when the trigger is received on the DIO PFI3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) Dio3 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) representing the string "DIO/PFI3".

Parent topic:

RfsaDigitalEdgeArmReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio7.html language=enus -->
## TOPIC 00099: Dio7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dio7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeArmReferenceTriggerSource Dio7 { get; }RemarksReturns an object of type RfsaDigitalEdgeArmReferenceTriggerSource representing the string "

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) representing the string "DIO/PFI7".

Parent topic:

RfsaDigitalEdgeArmReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dioo.html language=enus -->
## TOPIC 00100: DioO

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-dioo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeArmReferenceTriggerSource DioO { get; }RemarksReturns an object of type RfsaDigitalEdgeArmReferenceTriggerSource representing the string "

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) DioO { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) representing the string "DIO/PFI0".

Parent topic:

RfsaDigitalEdgeArmReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-operator_neq__rfsadigitaledgearmreferencetriggersource-rfsadigitaledgearmreferencetriggersource.html language=enus -->
## TOPIC 00101: operator!=(RfsaDigitalEdgeArmReferenceTriggerSource, RfsaDigitalEdgeArmReferenceTriggerSource)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-operator_neq__rfsadigitaledgearmreferencetriggersource-rfsadigitaledgearmreferencetriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-operator_neq__rfsadigitaledgearmreferencetriggersource-rfsadigitaledgearmreferencetriggersource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaDigitalEdgeArmReferenceTriggerSource are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaDigitalEdgeArmReferenceTriggerSource source1, RfsaDigitalEdgeArmReferenceTriggerSource source2)Remarks > Parameter

### operator!=(RfsaDigitalEdgeArmReferenceTriggerSource, RfsaDigitalEdgeArmReferenceTriggerSource)

Checks whether the two instances of [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaDigitalEdgeArmReferenceTriggerSource source1, RfsaDigitalEdgeArmReferenceTriggerSource source2)

#### Remarks

>

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsaDigitalEdgeArmReferenceTriggerSource | Specifies a RfsaDigitalEdgeArmReferenceTriggerSource object. |
| source2 | RfsaDigitalEdgeArmReferenceTriggerSource | Specifies a RfsaDigitalEdgeArmReferenceTriggerSource object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsaDigitalEdgeArmReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-pxitriggerline2.html language=enus -->
## TOPIC 00102: PxiTriggerLine2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource-pxitriggerline2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeArmReferenceTriggerSource PxiTriggerLine2 { get; }RemarksReturns an object of type RfsaDigitalEdgeArmReferenceTriggerSource repr

### PxiTriggerLine2

Gets the source terminal when the trigger is received on the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeArmReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgearmreferencetriggersource.html) representing the string "PXI_Trig2".

Parent topic:

RfsaDigitalEdgeArmReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-equals__rfsadigitaledgeconfigurationliststeptriggersource.html language=enus -->
## TOPIC 00103: Equals(RfsaDigitalEdgeConfigurationListStepTriggerSource)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-equals__rfsadigitaledgeconfigurationliststeptriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-equals__rfsadigitaledgeconfigurationliststeptriggersource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaDigitalEdgeConfigurationListStepTriggerSource and the RfsaDigitalEdgeConfigurationListStepTriggerSource object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaDigitalEdgeConfigurationListS

### Equals(RfsaDigitalEdgeConfigurationListStepTriggerSource)

Determines whether the current instance of [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html) and the [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaDigitalEdgeConfigurationListStepTriggerSource source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsaDigitalEdgeConfigurationListStepTriggerSource | Specifies the RfsaDigitalEdgeConfigurationListStepTriggerSource object to compare to the current instance of RfsaDigitalEdgeConfigurationListStepTriggerSource. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-operator_eq__rfsadigitaledgeconfigurationliststeptriggersource-rfsadigitaledgeconfigurati...d298e213.html language=enus -->
## TOPIC 00104: operator==(RfsaDigitalEdgeConfigurationListStepTriggerSource, RfsaDigitalEdgeConfigurationListStepTriggerSource)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-operator_eq__rfsadigitaledgeconfigurationliststeptriggersource-rfsadigitaledgeconfigurati...d298e213.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-operator_eq__rfsadigitaledgeconfigurationliststeptriggersource-rfsadigitaledgeconfigurati...d298e213.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaDigitalEdgeConfigurationListStepTriggerSource are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaDigitalEdgeConfigurationListStepTriggerSource source1, RfsaDigitalEdgeConfigurationListStepTriggerSource so

### operator==(RfsaDigitalEdgeConfigurationListStepTriggerSource, RfsaDigitalEdgeConfigurationListStepTriggerSource)

Checks whether the two instances of [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaDigitalEdgeConfigurationListStepTriggerSource source1, RfsaDigitalEdgeConfigurationListStepTriggerSource source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsaDigitalEdgeConfigurationListStepTriggerSource | Specifies a RfsaDigitalEdgeConfigurationListStepTriggerSource object. |
| source2 | RfsaDigitalEdgeConfigurationListStepTriggerSource | Specifies a RfsaDigitalEdgeConfigurationListStepTriggerSource object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-operator_neq__rfsadigitaledgeconfigurationliststeptriggersource-rfsadigitaledgeconfigurat...d298e161.html language=enus -->
## TOPIC 00105: operator!=(RfsaDigitalEdgeConfigurationListStepTriggerSource, RfsaDigitalEdgeConfigurationListStepTriggerSource)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-operator_neq__rfsadigitaledgeconfigurationliststeptriggersource-rfsadigitaledgeconfigurat...d298e161.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-operator_neq__rfsadigitaledgeconfigurationliststeptriggersource-rfsadigitaledgeconfigurat...d298e161.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaDigitalEdgeConfigurationListStepTriggerSource are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaDigitalEdgeConfigurationListStepTriggerSource source1, RfsaDigitalEdgeConfigurationListStepTriggerSource

### operator!=(RfsaDigitalEdgeConfigurationListStepTriggerSource, RfsaDigitalEdgeConfigurationListStepTriggerSource)

Checks whether the two instances of [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaDigitalEdgeConfigurationListStepTriggerSource source1, RfsaDigitalEdgeConfigurationListStepTriggerSource source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsaDigitalEdgeConfigurationListStepTriggerSource | Specifies a RfsaDigitalEdgeConfigurationListStepTriggerSource object. |
| source2 | RfsaDigitalEdgeConfigurationListStepTriggerSource | Specifies a RfsaDigitalEdgeConfigurationListStepTriggerSource object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsaDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-timerevent.html language=enus -->
## TOPIC 00106: TimerEvent

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-timerevent.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value which indicates that the device is reconfigured when the timer expires. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeConfigurationListStepTriggerSource TimerEvent { get; }RemarksReturns an object of type RfsaDigitalEdgeConfigurationListStepT

### TimerEvent

Gets a value which indicates that the device is reconfigured when the timer expires.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html) TimerEvent { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html) representing the string "TimerEvent".

Parent topic:

RfsaDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-tostring.html language=enus -->
## TOPIC 00107: ToString()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource-tostring.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsaDigitalEdgeConfigurationListStepTriggerSource to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override string ToString()ReturnsReturns a string that represents the current instance of RfsaDigitalEdgeConfigurationListStepTriggerSour

### ToString()

Converts the current instance of [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsaDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgeconfigurationliststeptriggersource.html).

Parent topic:

RfsaDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-dio2.html language=enus -->
## TOPIC 00108: Dio2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-dio2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeReferenceTriggerSource Dio2 { get; }RemarksReturns an object of type RfsaDigitalEdgeReferenceTriggerSource representing the string "DIO/PF

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) representing the string "DIO/PFI2".

Parent topic:

RfsaDigitalEdgeReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-fromstring__string.html language=enus -->
## TOPIC 00109: FromString(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-fromstring__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsaDigitalEdgeReferenceTriggerSource object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeReferenceTriggerSource FromString(string source)ParametersNameTypeDescriptionsourcestringSpecifies a string that is the source

### FromString(string)

Creates an [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies a string that is the source of RfsaDigitalEdgeReferenceTrigger. |

#### Returns

Returns an object of type [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html).

Parent topic:

RfsaDigitalEdgeReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-operator-rfsadigitaledgereferencetriggersource__string.html language=enus -->
## TOPIC 00110: operator RfsaDigitalEdgeReferenceTriggerSource(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-operator-rfsadigitaledgereferencetriggersource__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-operator-rfsadigitaledgereferencetriggersource__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent RfsaDigitalEdgeReferenceTriggerSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator RfsaDigitalEdgeReferenceTriggerSource(string source)ParametersNameTypeDescriptionsourcestringSpecifies the strin

### operator RfsaDigitalEdgeReferenceTriggerSource(string)

Converts the specified string to the equivalent [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator RfsaDigitalEdgeReferenceTriggerSource(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies the string to be converted to the equivalent RfsaDigitalEdgeReferenceTriggerSource object. |

#### Returns

Returns an object of type [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) from the string passed in *source*.

Parent topic:

RfsaDigitalEdgeReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-pxitriggerline0.html language=enus -->
## TOPIC 00111: PxiTriggerLine0

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-pxitriggerline0.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeReferenceTriggerSource PxiTriggerLine0 { get; }RemarksReturns an object of type RfsaDigitalEdgeReferenceTriggerSource representi

### PxiTriggerLine0

Gets the source terminal when the trigger is received on the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) representing the string "PXI_Trig0".

Parent topic:

RfsaDigitalEdgeReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-pxitriggerline2.html language=enus -->
## TOPIC 00112: PxiTriggerLine2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-pxitriggerline2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeReferenceTriggerSource PxiTriggerLine2 { get; }RemarksReturns an object of type RfsaDigitalEdgeReferenceTriggerSource representi

### PxiTriggerLine2

Gets the source terminal when the trigger is received on the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) representing the string "PXI_Trig2".

Parent topic:

RfsaDigitalEdgeReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-tostring.html language=enus -->
## TOPIC 00113: ToString()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource-tostring.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsaDigitalEdgeReferenceTriggerSource to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override string ToString()ReturnsReturns a string that represents the current instance of RfsaDigitalEdgeReferenceTriggerSource.

### ToString()

Converts the current instance of [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsaDigitalEdgeReferenceTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html).

Parent topic:

RfsaDigitalEdgeReferenceTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html language=enus -->
## TOPIC 00114: RfsaDigitalEdgeReferenceTriggerSource Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetriggersource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source terminal for RfsaDigitalEdgeReferenceTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaDigitalEdgeReferenceTriggerSourceRemarksSee Source. PropertiesNameDescriptionDio1Gets the source terminal when the trigger is received on

### RfsaDigitalEdgeReferenceTriggerSource Class

Represents the source terminal for [RfsaDigitalEdgeReferenceTrigger](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaDigitalEdgeReferenceTriggerSource

#### Remarks

See [Source](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgereferencetrigger-source.html).

#### Properties

| Name | Description |
| --- | --- |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| Pfi0 | Gets the source terminal when the trigger is received on the PFI 0 connector. |
| Pfi1 | Gets the source terminal when the trigger is received on the PFI 1 connector. |
| PXIeDStarB | Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. |
| PxiStarLine | Gets the source terminal when the trigger is received on the PXI Star trigger line. |
| PxiTriggerLine0 | Gets the source terminal when the trigger is received on the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the source terminal when the trigger is received on the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the source terminal when the trigger is received on the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the source terminal when the trigger is received on the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the source terminal when the trigger is received on the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the source terminal when the trigger is received on the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the source terminal when the trigger is received on the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the source terminal when the trigger is received on the PXI trigger line 7. |
| TimerEvent | Gets the source terminal when the trigger is received from the Timer event. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsaDigitalEdgeReferenceTriggerSource object from the specified string. |
| Equals(RfsaDigitalEdgeReferenceTriggerSource) | Determines whether the current instance of RfsaDigitalEdgeReferenceTriggerSource and the RfsaDigitalEdgeReferenceTriggerSource object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsaDigitalEdgeReferenceTriggerSource and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaDigitalEdgeReferenceTriggerSource. |
| ToString() | Converts the current instance of RfsaDigitalEdgeReferenceTriggerSource to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsaDigitalEdgeReferenceTriggerSource(string) | Converts the specified string to the equivalent RfsaDigitalEdgeReferenceTriggerSource object. |
| operator string(RfsaDigitalEdgeReferenceTriggerSource) | Converts the RfsaDigitalEdgeReferenceTriggerSource object to the equivalent string. |
| operator!=(RfsaDigitalEdgeReferenceTriggerSource, RfsaDigitalEdgeReferenceTriggerSource) | Checks whether the two instances of RfsaDigitalEdgeReferenceTriggerSource are unequal. |
| operator==(RfsaDigitalEdgeReferenceTriggerSource, RfsaDigitalEdgeReferenceTriggerSource) | Checks whether the two instances of RfsaDigitalEdgeReferenceTriggerSource are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-dioo.html language=enus -->
## TOPIC 00115: DioO

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-dioo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeStartTriggerSource DioO { get; }RemarksReturns an object of type RfsaDigitalEdgeStartTriggerSource representing the string "DIO/PFI0".

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) DioO { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) representing the string "DIO/PFI0".

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-equals__object.html language=enus -->
## TOPIC 00116: Equals(object)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-equals__object.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaDigitalEdgeStartTriggerSource and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to th

### Equals(object)

Determines whether the current instance of [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsaDigitalEdgeStartTriggerSource. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-equals__rfsadigitaledgestarttriggersource.html language=enus -->
## TOPIC 00117: Equals(RfsaDigitalEdgeStartTriggerSource)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-equals__rfsadigitaledgestarttriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-equals__rfsadigitaledgestarttriggersource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaDigitalEdgeStartTriggerSource and the RfsaDigitalEdgeStartTriggerSource object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaDigitalEdgeStartTriggerSource source)ParametersNameTypeDescri

### Equals(RfsaDigitalEdgeStartTriggerSource)

Determines whether the current instance of [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) and the [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaDigitalEdgeStartTriggerSource source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsaDigitalEdgeStartTriggerSource | Specifies the RfsaDigitalEdgeStartTriggerSource object to compare to the current instance of RfsaDigitalEdgeStartTriggerSource. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-operator-rfsadigitaledgestarttriggersource__string.html language=enus -->
## TOPIC 00118: operator RfsaDigitalEdgeStartTriggerSource(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-operator-rfsadigitaledgestarttriggersource__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-operator-rfsadigitaledgestarttriggersource__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specifies string to the equivalent RfsaDigitalEdgeStartTriggerSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator RfsaDigitalEdgeStartTriggerSource(string source)ParametersNameTypeDescriptionsourcestringSpecifies the string to be

### operator RfsaDigitalEdgeStartTriggerSource(string)

Converts the specifies string to the equivalent [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator RfsaDigitalEdgeStartTriggerSource(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies the string to be converted to the equivalent RfsaDigitalEdgeStartTriggerSource object. |

#### Returns

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) from the string passed in *source*.

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pfi0.html language=enus -->
## TOPIC 00119: Pfi0

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pfi0.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeStartTriggerSource Pfi0 { get; }RemarksReturns an object of type RfsaDigitalEdgeStartTriggerSource representing the string "PFI0".

### Pfi0

Gets the source terminal when the trigger is received on the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) representing the string "PFI0".

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pfi1.html language=enus -->
## TOPIC 00120: Pfi1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pfi1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PFI 1 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeStartTriggerSource Pfi1 { get; }RemarksReturns an object of type RfsaDigitalEdgeStartTriggerSource representing the string "PFI1".

### Pfi1

Gets the source terminal when the trigger is received on the PFI 1 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) Pfi1 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) representing the string "PFI1".

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxiedstarb.html language=enus -->
## TOPIC 00121: PXIeDStarB

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxiedstarb.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxiedstarb.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeStartTriggerSource PXIeDStarB { get; }RemarksReturns an ob

### PXIeDStarB

Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) PXIeDStarB { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) representing the string "PXIe_DStarB".

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxistarline.html language=enus -->
## TOPIC 00122: PxiStarLine

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxistarline.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI Star trigger line. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeStartTriggerSource PxiStarLine { get; }RemarksReturns an object of type RfsaDigitalEdgeStartTriggerSource representing the st

### PxiStarLine

Gets the source terminal when the trigger is received on the PXI Star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) PxiStarLine { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) representing the string "PXI_STAR".

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxitriggerline5.html language=enus -->
## TOPIC 00123: PxiTriggerLine5

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-pxitriggerline5.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeStartTriggerSource PxiTriggerLine5 { get; }RemarksReturns an object of type RfsaDigitalEdgeStartTriggerSource representing the s

### PxiTriggerLine5

Gets the source terminal when the trigger is received on the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) representing the string "PXI_Trig5".

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-timerevent.html language=enus -->
## TOPIC 00124: TimerEvent

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource-timerevent.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received from the Timer event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitalEdgeStartTriggerSource TimerEvent { get; }RemarksReturns an object of type RfsaDigitalEdgeStartTriggerSource representing the string "Tim

### TimerEvent

Gets the source terminal when the trigger is received from the Timer event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) TimerEvent { get; }

#### Remarks

Returns an object of type [RfsaDigitalEdgeStartTriggerSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitaledgestarttriggersource.html) representing the string "TimerEvent".

Parent topic:

RfsaDigitalEdgeStartTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock-export.html language=enus -->
## TOPIC 00125: Export

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock-export.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock-export.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RfsaExportDigitizerSampleClock sub-object to configure the export of Digitizer Sample Clock of the NI-RFSA. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaExportDigitizerSampleClock Export { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClock. Exc

### Export

Gets the [RfsaExportDigitizerSampleClock](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclock.html) sub-object to configure the export of Digitizer Sample Clock of the NI-RFSA.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaExportDigitizerSampleClock](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclock.html) Export { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClock](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclock.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Export property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDigitizerSampleClock Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock-timebasesource.html language=enus -->
## TOPIC 00126: TimebaseSource

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock-timebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock-timebasesource.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the source of the Sample clock timebase, which is the timebase used to control waveform sampling. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaDigitizerSampleClockTimebaseSource TimebaseSource { get; set; }RemarksSpecifies an object of type RfsaDigitizerSampl

### TimebaseSource

Gets or sets the source of the Sample clock timebase, which is the timebase used to control waveform sampling.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html) TimebaseSource { get; set; }

#### Remarks

Specifies an object of type [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The TimebaseSource property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDigitizerSampleClock Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock.html language=enus -->
## TOPIC 00127: RfsaDigitizerSampleClock Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties used to configure Digitizer Sample Clock. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaDigitizerSampleClock : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDesc

### RfsaDigitizerSampleClock Class

Represents the properties used to configure Digitizer Sample Clock.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaDigitizerSampleClock : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| ClockRate | Gets or sets the frequency, in hertz (Hz), of the Digitizer Sample Clock. |
| Export | Gets the RfsaExportDigitizerSampleClock sub-object to configure the export of Digitizer Sample Clock of the NI-RFSA. |
| TimebaseRate | Gets or sets the frequency, in hertz (Hz), of the external clock used as the timebase source, if you set the TimebaseSource property to an external source, such as "ClkIn" or "LORefClk". |
| TimebaseSource | Gets or sets the source of the Sample clock timebase, which is the timebase used to control waveform sampling. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-equals__object.html language=enus -->
## TOPIC 00128: Equals(object)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-equals__object.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance RfsaDigitizerSampleClockSynchronizationDistributionLine and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object t

### Equals(object)

Determines whether the current instance [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsaDigitizerSampleClockSynchronizationDistributionLine. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDigitizerSampleClockSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-equals__rfsadigitizersampleclocksynchronizationdistributionline.html language=enus -->
## TOPIC 00129: Equals(RfsaDigitizerSampleClockSynchronizationDistributionLine)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-equals__rfsadigitizersampleclocksynchronizationdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-equals__rfsadigitizersampleclocksynchronizationdistributionline.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaDigitizerSampleClockSynchronizationDistributionLine and the RfsaDigitizerSampleClockSynchronizationDistributionLine object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaDigitizerSampleCl

### Equals(RfsaDigitizerSampleClockSynchronizationDistributionLine)

Determines whether the current instance of [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) and the [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaDigitizerSampleClockSynchronizationDistributionLine source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsaDigitizerSampleClockSynchronizationDistributionLine | Specifies the RfsaDigitizerSampleClockSynchronizationDistributionLine object to be compared to the current instance of RfsaDigitizerSampleClockSynchronizationDistributionLine. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDigitizerSampleClockSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-gethashcode.html language=enus -->
## TOPIC 00130: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsaDigitizerSampleClockSynchronizationDistributionLine. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of RfsaD

### GetHashCode()

Returns the hash code for the current instance of [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html).

Parent topic:

RfsaDigitizerSampleClockSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-operator_neq__rfsadigitizersampleclocksynchronizationdistributionline-rfsadigitizer...d385e294.html language=enus -->
## TOPIC 00131: operator!=(RfsaDigitizerSampleClockSynchronizationDistributionLine, RfsaDigitizerSampleClockSynchronizationDistributionLine)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-operator_neq__rfsadigitizersampleclocksynchronizationdistributionline-rfsadigitizer...d385e294.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-operator_neq__rfsadigitizersampleclocksynchronizationdistributionline-rfsadigitizer...d385e294.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaDigitizerSampleClockSynchronizationDistributionLine are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaDigitizerSampleClockSynchronizationDistributionLine source1, RfsaDigitizerSampleClockSynchronizatio

### operator!=(RfsaDigitizerSampleClockSynchronizationDistributionLine, RfsaDigitizerSampleClockSynchronizationDistributionLine)

Checks whether the two instances of [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaDigitizerSampleClockSynchronizationDistributionLine source1, RfsaDigitizerSampleClockSynchronizationDistributionLine source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsaDigitizerSampleClockSynchronizationDistributionLine | Specifies a RfsaDigitizerSampleClockSynchronizationDistributionLine object. |
| source2 | RfsaDigitizerSampleClockSynchronizationDistributionLine | Specifies RfsaDigitizerSampleClockSynchronizationDistributionLine object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsaDigitizerSampleClockSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig2.html language=enus -->
## TOPIC 00132: PxiTrig2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external trigger line which is set to PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitizerSampleClockSynchronizationDistributionLine PxiTrig2 { get; }RemarksReturns an object of type RfsaDigitizerSampleClockSynchronizationDistribution

### PxiTrig2

Gets the external trigger line which is set to PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) PxiTrig2 { get; }

#### Remarks

Returns an object of type [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) representing the string "PXI_Trig2".

Parent topic:

RfsaDigitizerSampleClockSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig4.html language=enus -->
## TOPIC 00133: PxiTrig4

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig4.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external trigger line which is set to PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitizerSampleClockSynchronizationDistributionLine PxiTrig4 { get; }RemarksReturns an object of type RfsaDigitizerSampleClockSynchronizationDistribution

### PxiTrig4

Gets the external trigger line which is set to PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) PxiTrig4 { get; }

#### Remarks

Returns an object of type [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) representing the string "PXI_Trig4".

Parent topic:

RfsaDigitizerSampleClockSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig6.html language=enus -->
## TOPIC 00134: PxiTrig6

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline-pxitrig6.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the external trigger line which is set to PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitizerSampleClockSynchronizationDistributionLine PxiTrig6 { get; }RemarksReturns an object of type RfsaDigitizerSampleClockSynchronizationDistribution

### PxiTrig6

Gets the external trigger line which is set to PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) PxiTrig6 { get; }

#### Remarks

Returns an object of type [RfsaDigitizerSampleClockSynchronizationDistributionLine](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html) representing the string "PXI_Trig6".

Parent topic:

RfsaDigitizerSampleClockSynchronizationDistributionLine Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html language=enus -->
## TOPIC 00135: RfsaDigitizerSampleClockSynchronizationDistributionLine Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocksynchronizationdistributionline.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the RfsaDigitizerSampleClockSynchronizationDistributionLine signal. When synchronizing the RfsaDigitizerSampleClock, configure all devices to use the same Digitizer Sample Clock distribution line. Derives fromNoneSyntaxNamespace: NationalInstruments.

### RfsaDigitizerSampleClockSynchronizationDistributionLine Class

Specifies which external trigger line distributes the RfsaDigitizerSampleClockSynchronizationDistributionLine signal. When synchronizing the [RfsaDigitizerSampleClock](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclock.html), configure all devices to use the same Digitizer Sample Clock distribution line.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaDigitizerSampleClockSynchronizationDistributionLine

#### Remarks

Refer to RfsaDigitizerSampleClockSynchronizationDistributionLine.

#### Properties

| Name | Description |
| --- | --- |
| Pfi0 | Gets the external trigger line that is set to PFI 0 connector. |
| PxiTrig0 | Gets the external trigger line which is set to PXI trigger line 0. |
| PxiTrig1 | Gets the external trigger line which is set to PXI trigger line 1. |
| PxiTrig2 | Gets the external trigger line which is set to PXI trigger line 2. |
| PxiTrig3 | Gets the external trigger line which is set to PXI trigger line 3. |
| PxiTrig4 | Gets the external trigger line which is set to PXI trigger line 4. |
| PxiTrig5 | Gets the external trigger line which is set to PXI trigger line 5. |
| PxiTrig6 | Gets the external trigger line which is set to PXI trigger line 6. |
| PxiTrig7 | Gets the external trigger line which is set to PXI trigger line 7. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsaDigitizerSampleClockSynchronizationDistributionLine object from the specified string. |
| Equals(RfsaDigitizerSampleClockSynchronizationDistributionLine) | Determines whether the current instance of RfsaDigitizerSampleClockSynchronizationDistributionLine and the RfsaDigitizerSampleClockSynchronizationDistributionLine object that you specify are equal. |
| Equals(object) | Determines whether the current instance RfsaDigitizerSampleClockSynchronizationDistributionLine and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaDigitizerSampleClockSynchronizationDistributionLine. |
| ToString() | Converts the current instance of RfsaDigitizerSampleClockSynchronizationDistributionLine to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsaDigitizerSampleClockSynchronizationDistributionLine(string) | Converts the specified string to its RfsaDigitizerSampleClockSynchronizationDistributionLine equivalent. |
| operator string(RfsaDigitizerSampleClockSynchronizationDistributionLine) | Converts the RfsaDigitizerSampleClockSynchronizationDistributionLine object to its string equivalent. |
| operator!=(RfsaDigitizerSampleClockSynchronizationDistributionLine, RfsaDigitizerSampleClockSynchronizationDistributionLine) | Checks whether the two instances of RfsaDigitizerSampleClockSynchronizationDistributionLine are unequal. |
| operator==(RfsaDigitizerSampleClockSynchronizationDistributionLine, RfsaDigitizerSampleClockSynchronizationDistributionLine) | Checks whether the two instances of RfsaDigitizerSampleClockSynchronizationDistributionLine are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-gethashcode.html language=enus -->
## TOPIC 00136: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsaDigitizerSampleClockTimebaseSource. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsaDigitizerSampleClockTimebaseS

### GetHashCode()

Returns the hash code for the current instance of [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html).

Parent topic:

RfsaDigitizerSampleClockTimebaseSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-onboardclock.html language=enus -->
## TOPIC 00137: OnboardClock

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-onboardclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-onboardclock.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the digitizer that uses its onboard clock as the Sample clock timebase. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDigitizerSampleClockTimebaseSource OnboardClock { get; }RemarksReturns an object of type RfsaDigitizerSampleClockTimebaseSource representing th

### OnboardClock

Gets the digitizer that uses its onboard clock as the Sample clock timebase.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html) OnboardClock { get; }

#### Remarks

Returns an object of type [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html) representing the string "OnboardClock".

Parent topic:

RfsaDigitizerSampleClockTimebaseSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-operator-rfsadigitizersampleclocktimebasesource__string.html language=enus -->
## TOPIC 00138: operator RfsaDigitizerSampleClockTimebaseSource(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-operator-rfsadigitizersampleclocktimebasesource__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource-operator-rfsadigitizersampleclocktimebasesource__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent RfsaDigitizerSampleClockTimebaseSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator RfsaDigitizerSampleClockTimebaseSource(string timebaseSource)ParametersNameTypeDescriptiontimebaseSourcestringS

### operator RfsaDigitizerSampleClockTimebaseSource(string)

Converts the specified string to the equivalent [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator RfsaDigitizerSampleClockTimebaseSource(string timebaseSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timebaseSource | string | Specifies the string to be converted to the equivalent RfsaDigitizerSampleClockTimebaseSource object. |

#### Returns

Returns a [RfsaDigitizerSampleClockTimebaseSource](nationalinstruments-modularinstruments-nirfsa-rfsadigitizersampleclocktimebasesource.html) object from the string passed in *timebaseSource*.

Parent topic:

RfsaDigitizerSampleClockTimebaseSource Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dio3.html language=enus -->
## TOPIC 00139: Dio3

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dio3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dio3.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal Dio3 { get; }RemarksReturns an object of type RfsaDoneEventExportedOutputTerminal representing the string "DIO/PFI3".

### Dio3

Gets the source terminal when the trigger is received on the DIO PFI3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) Dio3 { get; }

#### Remarks

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) representing the string "DIO/PFI3".

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dio4.html language=enus -->
## TOPIC 00140: Dio4

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dio4.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal Dio4 { get; }RemarksReturns an object of type RfsaDoneEventExportedOutputTerminal representing the string "DIO/PFI4".

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) representing the string "DIO/PFI4".

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dioo.html language=enus -->
## TOPIC 00141: DioO

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-dioo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal DioO { get; }RemarksReturns an object of type RfsaDoneEventExportedOutputTerminal representing the string "DIO/PFI0".

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) DioO { get; }

#### Remarks

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) representing the string "DIO/PFI0".

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-donotexport.html language=enus -->
## TOPIC 00142: DoNotExport

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-donotexport.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-donotexport.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal signal when the signal is not exported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal DoNotExport { get; }RemarksReturns an object of type RfsaDoneEventExportedOutputTerminal representing an empty string.

### DoNotExport

Gets the destination terminal signal when the signal is not exported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) DoNotExport { get; }

#### Remarks

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) representing an empty string.

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-equals__rfsadoneeventexportedoutputterminal.html language=enus -->
## TOPIC 00143: Equals(RfsaDoneEventExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-equals__rfsadoneeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-equals__rfsadoneeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaDoneEventExportedOutputTerminal and the RfsaDoneEventExportedOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaDoneEventExportedOutputTerminal outputTerminal)Parameters

### Equals(RfsaDoneEventExportedOutputTerminal)

Determines whether the current instance of [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) and the [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaDoneEventExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsaDoneEventExportedOutputTerminal | Specifies the RfsaDoneEventExportedOutputTerminal object to be compared to the current instance of RfsaDoneEventExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-fromstring__string.html language=enus -->
## TOPIC 00144: FromString(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-fromstring__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsaDoneEventExportedOutputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal FromString(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpecifies a string that i

### FromString(string)

Creates an [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) FromString(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies a string that is the output terminal of RfsaDoneEvent. |

#### Returns

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html).

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-gethashcode.html language=enus -->
## TOPIC 00145: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsaDoneEventExportedOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsaDoneEventExportedOutputTerminal.

### GetHashCode()

Returns the hash code for the current instance of [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html).

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-operator-rfsadoneeventexportedoutputterminal__string.html language=enus -->
## TOPIC 00146: operator RfsaDoneEventExportedOutputTerminal(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-operator-rfsadoneeventexportedoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-operator-rfsadoneeventexportedoutputterminal__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent RfsaDoneEventExportedOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator RfsaDoneEventExportedOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpecifi

### operator RfsaDoneEventExportedOutputTerminal(string)

Converts the specified string to the equivalent [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator RfsaDoneEventExportedOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent RfsaDoneEventExportedOutputTerminal object. |

#### Returns

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) from the string passed in *outputTerminal*.

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-operator_neq__rfsadoneeventexportedoutputterminal-rfsadoneeventexportedoutputterminal.html language=enus -->
## TOPIC 00147: operator!=(RfsaDoneEventExportedOutputTerminal, RfsaDoneEventExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-operator_neq__rfsadoneeventexportedoutputterminal-rfsadoneeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-operator_neq__rfsadoneeventexportedoutputterminal-rfsadoneeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaDoneEventExportedOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaDoneEventExportedOutputTerminal outputTerminal1, RfsaDoneEventExportedOutputTerminal outputTerminal2)ParametersNameType

### operator!=(RfsaDoneEventExportedOutputTerminal, RfsaDoneEventExportedOutputTerminal)

Checks whether the two instances of [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaDoneEventExportedOutputTerminal outputTerminal1, RfsaDoneEventExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsaDoneEventExportedOutputTerminal | Specifies a RfsaDoneEventExportedOutputTerminal object. |
| outputTerminal2 | RfsaDoneEventExportedOutputTerminal | Specifies a RfsaDoneEventExportedOutputTerminal object. |

#### Returns

true if the two instances are not equal; otherwise, false.

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00148: PxiTriggerLine1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the the destination terminal when signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type RfsaDoneEventExportedOutputTerminal representi

### PxiTriggerLine1

Gets the the destination terminal when signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00149: PxiTriggerLine2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type RfsaDoneEventExportedOutputTerminal representi

### PxiTriggerLine2

Gets the destination terminal when the signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) representing the string "PXI_Trig2".

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00150: PxiTriggerLine7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal-pxitriggerline7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaDoneEventExportedOutputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type RfsaDoneEventExportedOutputTerminal representi

### PxiTriggerLine7

Gets the destination terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [RfsaDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

RfsaDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html language=enus -->
## TOPIC 00151: RfsaDoneEventExportedOutputTerminal Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadoneeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the destination terminal for RfsaDoneEvent. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaDoneEventExportedOutputTerminalRemarksSee OutputTerminal. PropertiesNameDescriptionClockOutGets the destination terminal when the signal is exported t

### RfsaDoneEventExportedOutputTerminal Class

Represents the destination terminal for [RfsaDoneEvent](nationalinstruments-modularinstruments-nirfsa-rfsadoneevent.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaDoneEventExportedOutputTerminal

#### Remarks

See [OutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsadoneevent-outputterminal.html).

#### Properties

| Name | Description |
| --- | --- |
| ClockOut | Gets the destination terminal when the signal is exported to the CLK OUT connector on the front panel. |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| DoNotExport | Gets the destination terminal signal when the signal is not exported. |
| Pfi0 | Gets the destination terminal when the signal is exported to the PFI 0 connector. |
| Pfi1 | Gets the destination terminal when the signal is exported to the PFI 1 connector. |
| PXIeDStarC | Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. |
| PxiStarLine | Gets the destination terminal when the signal is exported signal to the PXI Star trigger line. |
| PxiTriggerLine0 | Gets the destination terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the the destination terminal when signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the destination terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the destination terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the destination terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the destination terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the destination terminal when the signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the destination terminal when the signal is exported to the PXI trigger line 7. |
| ReferenceOut | Gets the destination terminal when the signal is exported to the REF IN/OUT terminal. |
| ReferenceOut2 | Gets the destination terminal when the signal is exported to the REF OUT2 terminal on the LO. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsaDoneEventExportedOutputTerminal object from the specified string. |
| Equals(RfsaDoneEventExportedOutputTerminal) | Determines whether the current instance of RfsaDoneEventExportedOutputTerminal and the RfsaDoneEventExportedOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsaDoneEventExportedOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaDoneEventExportedOutputTerminal. |
| ToString() | Converts the current instance of RfsaDoneEventExportedOutputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsaDoneEventExportedOutputTerminal(string) | Converts the specified string to the equivalent RfsaDoneEventExportedOutputTerminal object. |
| operator string(RfsaDoneEventExportedOutputTerminal) | Converts the RfsaDoneEventExportedOutputTerminal object to the equivalent string. |
| operator!=(RfsaDoneEventExportedOutputTerminal, RfsaDoneEventExportedOutputTerminal) | Checks whether the two instances of RfsaDoneEventExportedOutputTerminal are unequal. |
| operator==(RfsaDoneEventExportedOutputTerminal, RfsaDoneEventExportedOutputTerminal) | Checks whether the two instances of RfsaDoneEventExportedOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity-instrumentfirmwarerevision.html language=enus -->
## TOPIC 00152: InstrumentFirmwareRevision

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity-instrumentfirmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity-instrumentfirmwarerevision.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the firmware revision information for the NI-RFSA device currently in use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic string InstrumentFirmwareRevision { get; }RemarksReturns a String that contains the firmware revision information for the NI-RFSA device in use. Except

### InstrumentFirmwareRevision

Gets the firmware revision information for the NI-RFSA device currently in use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public string InstrumentFirmwareRevision { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) that contains the firmware revision information for the NI-RFSA device in use.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The NationalInstruments.ModularInstruments.NIRfsa.RfsaDriverIdentity.InstrumentFirmwareRevision property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverIdentity Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity-specificdriverdescription.html language=enus -->
## TOPIC 00153: SpecificDriverDescription

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity-specificdriverdescription.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriveridentity-specificdriverdescription.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string that contains a brief description of NI-RFSA driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic string SpecificDriverDescription { get; }RemarksReturns a String that contains a brief description about NI-RFSA driver. ExceptionsTypeDescriptionSystem.ObjectDispo

### SpecificDriverDescription

Gets a string that contains a brief description of NI-RFSA driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public string SpecificDriverDescription { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) that contains a brief description about NI-RFSA driver.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | TheSpecificDriverDescription property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverIdentity Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriveroperation-rangecheck.html language=enus -->
## TOPIC 00154: RangeCheck

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriveroperation-rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriveroperation-rangecheck.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to validate proper values and method parameters. If you enable this property, NI-RFSA validates the parameter values that you pass to NI-RFSA methods. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool RangeCheck { get; set; }Remarkstrue if validating prop

### RangeCheck

Gets or sets whether to validate proper values and method parameters. If you enable this property, NI-RFSA validates the parameter values that you pass to NI-RFSA methods.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool RangeCheck { get; set; }

#### Remarks

true if validating property values and method parameters are enabled; otherwise, false.

Range checking parameters is very useful for debugging. After you validate your program, you can set this property to false to disable range checking and maximize performance.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The RangeCheck property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverOperation Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-getrelayname__int.html language=enus -->
## TOPIC 00155: GetRelayName(int)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-getrelayname__int.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-getrelayname__int.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of a relay for your device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic string GetRelayName(int indexOfRelay)ParametersNameTypeDescriptionindexOfRelayintSpecifies the index of the relay. ReturnsReturns a String representing the name of a relay. ExceptionsTyp

### GetRelayName(int)

Returns the name of a relay for your device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public string GetRelayName(int indexOfRelay)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| indexOfRelay | int | Specifies the index of the relay. |

#### Returns

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the name of a relay.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetRelayName method was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-loadconfigurationsfromfileresetoptions.html language=enus -->
## TOPIC 00156: LoadConfigurationsFromFileResetOptions

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-loadconfigurationsfromfileresetoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-loadconfigurationsfromfileresetoptions.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configurations to skip resetting while loading configurations from a file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaLoadConfigurationsFromFileResetOptions LoadConfigurationsFromFileResetOptions { get; set; }RemarksReturns or sets a RfsaLoadConfigurations

### LoadConfigurationsFromFileResetOptions

Specifies the configurations to skip resetting while loading configurations from a file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaLoadConfigurationsFromFileResetOptions](nationalinstruments-modularinstruments-nirfsa-rfsaloadconfigurationsfromfileresetoptions.html) LoadConfigurationsFromFileResetOptions { get; set; }

#### Remarks

Returns or sets a [RfsaLoadConfigurationsFromFileResetOptions](nationalinstruments-modularinstruments-nirfsa-rfsaloadconfigurationsfromfileresetoptions.html) value specifying the reset options.

**Default Value:**[SkipNone](nationalinstruments-modularinstruments-nirfsa-rfsaloadconfigurationsfromfileresetoptions.html)

**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LoadConfigurationsFromFileResetOptions property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-resetattribute__propertyinfo.html language=enus -->
## TOPIC 00157: ResetAttribute(PropertyInfo)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-resetattribute__propertyinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-resetattribute__propertyinfo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the property to its default value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void ResetAttribute(PropertyInfo property)ParametersNameTypeDescriptionpropertyPropertyInfoSpecifies the property to be reset. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Res

### ResetAttribute(PropertyInfo)

Resets the property to its default value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void ResetAttribute(PropertyInfo property)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| property | PropertyInfo | Specifies the property to be reset. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ResetAttribute method was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-saveconfigurationstofile__string-string.html language=enus -->
## TOPIC 00158: SaveConfigurationsToFile(string, string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-saveconfigurationstofile__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-saveconfigurationstofile__string-string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the configurations of the session to the specified file. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic void SaveConfigurationsToFile(string channelName, string filePath)ParametersNameTypeDescriptionchannelN

### SaveConfigurationsToFile(string, string)

Saves the configurations of the session to the specified file. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public void SaveConfigurationsToFile(string channelName, string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | Specifies the name of the channel. This string is case-insensitive and alphanumeric, and it cannot use reserved words. |
| filePath | string | Specifies the absolute path of the file to which the NI-RFSG saves the configurations. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SaveConfigurationsToFile method was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-selftest.html language=enus -->
## TOPIC 00159: SelfTest()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-selftest.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-selftest.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test on the NI-RFSA device and returns the test result. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaSelfTestResult SelfTest()RemarksThis method performs a simple series of tests verifying that the NI-RFSA device is powered on and responding. This method c

### SelfTest()

Performs a self-test on the NI-RFSA device and returns the test result.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaSelfTestResult](nationalinstruments-modularinstruments-nirfsa-rfsaselftestresult.html) SelfTest()

#### Remarks

Note

This method calls the [Reset](nationalinstruments-modularinstruments-nirfsa-rfsadriverutility-reset.html) method, which resets the software state.

#### Returns

Returns an object of type [RfsaSelfTestResult](nationalinstruments-modularinstruments-nirfsa-rfsaselftestresult.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The NationalInstruments.ModularInstruments.NIRfsa.RfsaDriverUtility.SelfTest method was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio5.html language=enus -->
## TOPIC 00160: Dio5

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio5.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal Dio5 { get; }RemarksReturns an object of type RfsaEndOfRecordEventExportedOutputTerminal representing the stri

### Dio5

Gets the source terminal when the trigger is received on the DIO PFI5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) Dio5 { get; }

#### Remarks

Returns an object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "DIO/PFI5".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio6.html language=enus -->
## TOPIC 00161: Dio6

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio6.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal Dio6 { get; }RemarksReturns an object of type RfsaEndOfRecordEventExportedOutputTerminal representing the stri

### Dio6

Gets the source terminal when the trigger is received on the DIO PFI6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) Dio6 { get; }

#### Remarks

Returns an object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "DIO/PFI6".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio7.html language=enus -->
## TOPIC 00162: Dio7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dio7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal Dio7 { get; }RemarksReturns an object of type RfsaEndOfRecordEventExportedOutputTerminal representing the stri

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "DIO/PFI7".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dioo.html language=enus -->
## TOPIC 00163: DioO

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-dioo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal DioO { get; }RemarksReturns an object of type RfsaEndOfRecordEventExportedOutputTerminal representing the stri

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) DioO { get; }

#### Remarks

Returns an object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "DIO/PFI0".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-donotexport.html language=enus -->
## TOPIC 00164: DoNotExport

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-donotexport.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-donotexport.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is not exported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal DoNotExport { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal representing an empty string.

### DoNotExport

Gets the destination terminal when the signal is not exported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) DoNotExport { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing an empty string.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-equals__object.html language=enus -->
## TOPIC 00165: Equals(object)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-equals__object.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaEndOfRecordEventExportedOutputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compa

### Equals(object)

Determines whether the current instance of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsaEndOfRecordEventExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-equals__rfsaendofrecordeventexportedoutputterminal.html language=enus -->
## TOPIC 00166: Equals(RfsaEndOfRecordEventExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-equals__rfsaendofrecordeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-equals__rfsaendofrecordeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaEndOfRecordEventExportedOutputTerminal and the RfsaEndOfRecordEventExportedOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaEndOfRecordEventExportedOutputTerminal outp

### Equals(RfsaEndOfRecordEventExportedOutputTerminal)

Determines whether the current instance of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) and the [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaEndOfRecordEventExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsaEndOfRecordEventExportedOutputTerminal | Specifies the RfsaEndOfRecordEventExportedOutputTerminal object to be compared to the current instance of RfsaEndOfRecordEventExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-fromstring__string.html language=enus -->
## TOPIC 00167: FromString(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-fromstring__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsaEndOfRecordEventExportedOutputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal FromString(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpecifies a

### FromString(string)

Creates an [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) FromString(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies a string that is the output terminal of RfsaEndOfRecordEvent |

#### Returns

Returns an object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html).

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-gethashcode.html language=enus -->
## TOPIC 00168: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsaEndOfRecordEventExportedOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash value generated for the current instance of RfsaEndOfRecordEve

### GetHashCode()

Returns the hash code for the current instance of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash value generated for the current instance of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html).

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator-rfsaendofrecordeventexportedoutputterminal__string.html language=enus -->
## TOPIC 00169: operator RfsaEndOfRecordEventExportedOutputTerminal(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator-rfsaendofrecordeventexportedoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator-rfsaendofrecordeventexportedoutputterminal__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent RfsaEndOfRecordEventExportedOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator RfsaEndOfRecordEventExportedOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutputTermina

### operator RfsaEndOfRecordEventExportedOutputTerminal(string)

Converts the specified string to the equivalent [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator RfsaEndOfRecordEventExportedOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent RfsaEndOfRecordEventExportedOutputTerminal object. |

#### Returns

Returns an object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) from the string passed in *outputTerminal*.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator-string__rfsaendofrecordeventexportedoutputterminal.html language=enus -->
## TOPIC 00170: operator string(RfsaEndOfRecordEventExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator-string__rfsaendofrecordeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator-string__rfsaendofrecordeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the RfsaEndOfRecordEventExportedOutputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator string(RfsaEndOfRecordEventExportedOutputTerminal outputTerminal)ParametersNameTypeDescriptionoutputTerminalRfsaEndOf

### operator string(RfsaEndOfRecordEventExportedOutputTerminal)

Converts the [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator string(RfsaEndOfRecordEventExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsaEndOfRecordEventExportedOutputTerminal | Specifies the RfsaEndOfRecordEventExportedOutputTerminal object to be converted to string. |

#### Returns

Returns a string from the [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) object.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator_eq__rfsaendofrecordeventexportedoutputterminal-rfsaendofrecordeventexportedoutputterminal.html language=enus -->
## TOPIC 00171: operator==(RfsaEndOfRecordEventExportedOutputTerminal, RfsaEndOfRecordEventExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator_eq__rfsaendofrecordeventexportedoutputterminal-rfsaendofrecordeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator_eq__rfsaendofrecordeventexportedoutputterminal-rfsaendofrecordeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaEndOfRecordEventExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaEndOfRecordEventExportedOutputTerminal outputTerminal1, RfsaEndOfRecordEventExportedOutputTerminal outputTerminal2

### operator==(RfsaEndOfRecordEventExportedOutputTerminal, RfsaEndOfRecordEventExportedOutputTerminal)

Checks whether the two instances of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaEndOfRecordEventExportedOutputTerminal outputTerminal1, RfsaEndOfRecordEventExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsaEndOfRecordEventExportedOutputTerminal | Specifies a RfsaEndOfRecordEventExportedOutputTerminal object. |
| outputTerminal2 | RfsaEndOfRecordEventExportedOutputTerminal | Specifies a RfsaEndOfRecordEventExportedOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator_neq__rfsaendofrecordeventexportedoutputterminal-rfsaendofrecordeventexportedoutputterminal.html language=enus -->
## TOPIC 00172: operator!=(RfsaEndOfRecordEventExportedOutputTerminal, RfsaEndOfRecordEventExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator_neq__rfsaendofrecordeventexportedoutputterminal-rfsaendofrecordeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-operator_neq__rfsaendofrecordeventexportedoutputterminal-rfsaendofrecordeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaEndOfRecordEventExportedOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaEndOfRecordEventExportedOutputTerminal outputTerminal1, RfsaEndOfRecordEventExportedOutputTerminal outputTermina

### operator!=(RfsaEndOfRecordEventExportedOutputTerminal, RfsaEndOfRecordEventExportedOutputTerminal)

Checks whether the two instances of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaEndOfRecordEventExportedOutputTerminal outputTerminal1, RfsaEndOfRecordEventExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsaEndOfRecordEventExportedOutputTerminal | Specifies RfsaEndOfRecordEventExportedOutputTerminal object. |
| outputTerminal2 | RfsaEndOfRecordEventExportedOutputTerminal | Specifies RfsaEndOfRecordEventExportedOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pfi0.html language=enus -->
## TOPIC 00173: Pfi0

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pfi0.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal Pfi0 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal representing the s

### Pfi0

Gets the destination terminal when the signal is exported to the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) Pfi0 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PFI0".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pfi1.html language=enus -->
## TOPIC 00174: Pfi1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pfi1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 1 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal Pfi1 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal representing the s

### Pfi1

Gets the destination terminal when the signal is exported to the PFI 1 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) Pfi1 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PFI1".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxiedstarc.html language=enus -->
## TOPIC 00175: PXIeDStarC

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxiedstarc.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxiedstarc.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PXIeDStarC { get; }Remarks

### PXIeDStarC

Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PXIeDStarC { get; }

#### Remarks

Returns an object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXIe_DStarC".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxistarline.html language=enus -->
## TOPIC 00176: PxiStarLine

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxistarline.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI Star trigger line. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiStarLine { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repre

### PxiStarLine

Gets the destination terminal when the signal is exported to the PXI Star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiStarLine { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_STAR".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00177: PxiTriggerLine0

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline0.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine0 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine0

Gets the destination terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00178: PxiTriggerLine1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine1 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine1

Gets the destination terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00179: PxiTriggerLine2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine2 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine2

Gets the destination terminal when the signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig2".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline3.html language=enus -->
## TOPIC 00180: PxiTriggerLine3

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline3.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine3 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine3

Gets the destination terminal when the signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine3 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig3".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00181: PxiTriggerLine4

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline4.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine4 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine4

Gets the destination terminal when the signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig4".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00182: PxiTriggerLine5

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline5.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine5 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine5

Gets the destination terminal when the signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig5".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00183: PxiTriggerLine6

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline6.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine6 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine6

Gets the destination terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00184: PxiTriggerLine7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-pxitriggerline7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal PxiTriggerLine7 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repr

### PxiTriggerLine7

Gets the destination terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-referenceout.html language=enus -->
## TOPIC 00185: ReferenceOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-referenceout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-referenceout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the REF IN/OUT terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal ReferenceOut { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTerminal repres

### ReferenceOut

Gets the destination terminal when the signal is exported to the REF IN/OUT terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) ReferenceOut { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "RefOut".

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-referenceout2.html language=enus -->
## TOPIC 00186: ReferenceOut2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-referenceout2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-referenceout2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the REF OUT2 terminal on the LO. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaEndOfRecordEventExportedOutputTerminal ReferenceOut2 { get; }RemarksAn object of type RfsaEndOfRecordEventExportedOutputTermin

### ReferenceOut2

Gets the destination terminal when the signal is exported to the REF OUT2 terminal on the LO.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) ReferenceOut2 { get; }

#### Remarks

An object of type [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) representing the string "RefOut2".

This connector does not exist on some versions of the NI 5652.

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-tostring.html language=enus -->
## TOPIC 00187: ToString()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal-tostring.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsaEndOfRecordEventExportedOutputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override string ToString()ReturnsReturns a string that represents the current instance of RfsaEndOfRecordEventExportedOutputTerminal.

### ToString()

Converts the current instance of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsaEndOfRecordEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html).

Parent topic:

RfsaEndOfRecordEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html language=enus -->
## TOPIC 00188: RfsaEndOfRecordEventExportedOutputTerminal Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordeventexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the destination terminal for RfsaEndOfRecordEvent. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaEndOfRecordEventExportedOutputTerminalRemarksSee OutputTerminal. PropertiesNameDescriptionClockOutGets the destination terminal when the signal

### RfsaEndOfRecordEventExportedOutputTerminal Class

Represents the destination terminal for [RfsaEndOfRecordEvent](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordevent.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaEndOfRecordEventExportedOutputTerminal

#### Remarks

See [OutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaendofrecordevent-outputterminal.html).

#### Properties

| Name | Description |
| --- | --- |
| ClockOut | Gets the destination terminal when the signal is exported to the CLK OUT connector on the front panel. |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| DoNotExport | Gets the destination terminal when the signal is not exported. |
| Pfi0 | Gets the destination terminal when the signal is exported to the PFI 0 connector. |
| Pfi1 | Gets the destination terminal when the signal is exported to the PFI 1 connector. |
| PXIeDStarC | Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. |
| PxiStarLine | Gets the destination terminal when the signal is exported to the PXI Star trigger line. |
| PxiTriggerLine0 | Gets the destination terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the destination terminal when the signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the destination terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the destination terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the destination terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the destination terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the destination terminal when the signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the destination terminal when the signal is exported to the PXI trigger line 7. |
| ReferenceOut | Gets the destination terminal when the signal is exported to the REF IN/OUT terminal. |
| ReferenceOut2 | Gets the destination terminal when the signal is exported to the REF OUT2 terminal on the LO. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsaEndOfRecordEventExportedOutputTerminal object from the specified string. |
| Equals(RfsaEndOfRecordEventExportedOutputTerminal) | Determines whether the current instance of RfsaEndOfRecordEventExportedOutputTerminal and the RfsaEndOfRecordEventExportedOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsaEndOfRecordEventExportedOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaEndOfRecordEventExportedOutputTerminal. |
| ToString() | Converts the current instance of RfsaEndOfRecordEventExportedOutputTerminal to a string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsaEndOfRecordEventExportedOutputTerminal(string) | Converts the specified string to the equivalent RfsaEndOfRecordEventExportedOutputTerminal object. |
| operator string(RfsaEndOfRecordEventExportedOutputTerminal) | Converts the RfsaEndOfRecordEventExportedOutputTerminal object to the equivalent string. |
| operator!=(RfsaEndOfRecordEventExportedOutputTerminal, RfsaEndOfRecordEventExportedOutputTerminal) | Checks whether the two instances of RfsaEndOfRecordEventExportedOutputTerminal are unequal. |
| operator==(RfsaEndOfRecordEventExportedOutputTerminal, RfsaEndOfRecordEventExportedOutputTerminal) | Checks whether the two instances of RfsaEndOfRecordEventExportedOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-equals__object.html language=enus -->
## TOPIC 00189: Equals(object)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-equals__object.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaErrorQueryResult and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to the current ins

### Equals(object)

Determines whether the current instance of [RfsaErrorQueryResult](nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsaErrorQueryResult. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-equals__rfsaerrorqueryresult.html language=enus -->
## TOPIC 00190: Equals(RfsaErrorQueryResult)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-equals__rfsaerrorqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-equals__rfsaerrorqueryresult.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaErrorQueryResult and the RfsaErrorQueryResult object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaErrorQueryResult result)ParametersNameTypeDescriptionresultRfsaErrorQueryResultSpecifie

### Equals(RfsaErrorQueryResult)

Determines whether the current instance of [RfsaErrorQueryResult](nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html) and the [RfsaErrorQueryResult](nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaErrorQueryResult result)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result | RfsaErrorQueryResult | Specifies the RfsaErrorQueryResult object to be compared to the current instance of RfsaErrorQueryResult. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-errorcode.html language=enus -->
## TOPIC 00191: ErrorCode

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-errorcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-errorcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the error code returned by the driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic int ErrorCode { get; }RemarksReturns an Int32 representing the error code.

### ErrorCode

Gets the error code returned by the driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public int ErrorCode { get; }

#### Remarks

Returns an [Int32](https://learn.microsoft.com/dotnet/api/system.int32) representing the error code.

Parent topic:

RfsaErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-errormessage.html language=enus -->
## TOPIC 00192: ErrorMessage

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-errormessage.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-errormessage.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the user readable error string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic string ErrorMessage { get; }RemarksReturns a String representing the error string.

### ErrorMessage

Gets the user readable error string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public string ErrorMessage { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the error string.

Parent topic:

RfsaErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-gethashcode.html language=enus -->
## TOPIC 00193: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsaErrorQueryResult. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 representing the hash value generated for the current instance of RfsaErrorQueryResult.

### GetHashCode()

Returns the hash code for the current instance of [RfsaErrorQueryResult](nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 representing the hash value generated for the current instance of [RfsaErrorQueryResult](nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html).

Parent topic:

RfsaErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-operator_eq__rfsaerrorqueryresult-rfsaerrorqueryresult.html language=enus -->
## TOPIC 00194: operator==(RfsaErrorQueryResult, RfsaErrorQueryResult)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-operator_eq__rfsaerrorqueryresult-rfsaerrorqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-operator_eq__rfsaerrorqueryresult-rfsaerrorqueryresult.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaErrorQueryResult are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaErrorQueryResult result1, RfsaErrorQueryResult result2)ParametersNameTypeDescriptionresult1RfsaErrorQueryResultSpecifies a RfsaErrorQuer

### operator==(RfsaErrorQueryResult, RfsaErrorQueryResult)

Checks whether the two instances of [RfsaErrorQueryResult](nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaErrorQueryResult result1, RfsaErrorQueryResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | RfsaErrorQueryResult | Specifies a RfsaErrorQueryResult object. |
| result2 | RfsaErrorQueryResult | Specifies a RfsaErrorQueryResult object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-operator_neq__rfsaerrorqueryresult-rfsaerrorqueryresult.html language=enus -->
## TOPIC 00195: operator!=(RfsaErrorQueryResult, RfsaErrorQueryResult)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-operator_neq__rfsaerrorqueryresult-rfsaerrorqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult-operator_neq__rfsaerrorqueryresult-rfsaerrorqueryresult.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaErrorQueryResult are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator!=(RfsaErrorQueryResult result1, RfsaErrorQueryResult result2)ParametersNameTypeDescriptionresult1RfsaErrorQueryResultSpecifies a RfsaErrorQu

### operator!=(RfsaErrorQueryResult, RfsaErrorQueryResult)

Checks whether the two instances of [RfsaErrorQueryResult](nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator!=(RfsaErrorQueryResult result1, RfsaErrorQueryResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | RfsaErrorQueryResult | Specifies a RfsaErrorQueryResult object. |
| result2 | RfsaErrorQueryResult | Specifies a RfsaErrorQueryResult object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsaErrorQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html language=enus -->
## TOPIC 00196: RfsaErrorQueryResult Data Structure

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaerrorqueryresult.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the the result of an error query. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic struct RfsaErrorQueryResultRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionErrorCodeGets the error code returned by the

### RfsaErrorQueryResult Data Structure

Represents the the result of an error query.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public struct RfsaErrorQueryResult

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| ErrorCode | Gets the error code returned by the driver. |
| ErrorMessage | Gets the user readable error string. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(RfsaErrorQueryResult) | Determines whether the current instance of RfsaErrorQueryResult and the RfsaErrorQueryResult object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsaErrorQueryResult and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsaErrorQueryResult. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(RfsaErrorQueryResult, RfsaErrorQueryResult) | Checks whether the two instances of RfsaErrorQueryResult are unequal. |
| operator==(RfsaErrorQueryResult, RfsaErrorQueryResult) | Checks whether the two instances of RfsaErrorQueryResult are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetrigger-outputterminal.html language=enus -->
## TOPIC 00197: OutputTerminal

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetrigger-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetrigger-outputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination terminal for the exported Advance trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic RfsaExportAdvanceTriggerExportedOutputTerminal OutputTerminal { get; set; }RemarksSpecifies an object of type RfsaExportAdvanceTriggerExportedOutputTerminal. E

### OutputTerminal

Gets or sets the destination terminal for the exported Advance trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) OutputTerminal { get; set; }

#### Remarks

Specifies an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The OutputTerminal property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaExportAdvanceTrigger Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-clockout.html language=enus -->
## TOPIC 00198: ClockOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-clockout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-clockout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the CLK OUT connector on the front panel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal ClockOut { get; }RemarksReturns an object of type RfsaExportAdvanceTrigger

### ClockOut

Gets the destination terminal when the signal is exported to the CLK OUT connector on the front panel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) ClockOut { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "ClkOut".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio1.html language=enus -->
## TOPIC 00199: Dio1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal Dio1 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOutputTerminal representing

### Dio1

Gets the source terminal when the trigger is received on the DIO PFI1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) Dio1 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "DIO/PFI1".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio2.html language=enus -->
## TOPIC 00200: Dio2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal Dio2 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOutputTerminal representing

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "DIO/PFI2".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio4.html language=enus -->
## TOPIC 00201: Dio4

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio4.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal Dio4 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOutputTerminal representing

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "DIO/PFI4".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio7.html language=enus -->
## TOPIC 00202: Dio7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-dio7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal Dio7 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOutputTerminal representing

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "DIO/PFI7".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-fromstring__string.html language=enus -->
## TOPIC 00203: FromString(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-fromstring__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsaExportAdvanceTriggerExportedOutputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal FromString(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpe

### FromString(string)

Creates an [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) FromString(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies a string that is the output terminal of RfsaExportAdvanceTrigger. |

#### Returns

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html).

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-operator-rfsaexportadvancetriggerexportedoutputterminal__string.html language=enus -->
## TOPIC 00204: operator RfsaExportAdvanceTriggerExportedOutputTerminal(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-operator-rfsaexportadvancetriggerexportedoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-operator-rfsaexportadvancetriggerexportedoutputterminal__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent RfsaExportAdvanceTriggerExportedOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator RfsaExportAdvanceTriggerExportedOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutpu

### operator RfsaExportAdvanceTriggerExportedOutputTerminal(string)

Converts the specified string to the equivalent [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator RfsaExportAdvanceTriggerExportedOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent RfsaExportAdvanceTriggerExportedOutputTerminal object. |

#### Returns

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) from the string passed in *outputTerminal*.

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-operator_eq__rfsaexportadvancetriggerexportedoutputterminal-rfsaexportadvancetriggerexportedoutputterminal.html language=enus -->
## TOPIC 00205: operator==(RfsaExportAdvanceTriggerExportedOutputTerminal, RfsaExportAdvanceTriggerExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-operator_eq__rfsaexportadvancetriggerexportedoutputterminal-rfsaexportadvancetriggerexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-operator_eq__rfsaexportadvancetriggerexportedoutputterminal-rfsaexportadvancetriggerexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaExportAdvanceTriggerExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaExportAdvanceTriggerExportedOutputTerminal outputTerminal1, RfsaExportAdvanceTriggerExportedOutputTerminal out

### operator==(RfsaExportAdvanceTriggerExportedOutputTerminal, RfsaExportAdvanceTriggerExportedOutputTerminal)

Checks whether the two instances of [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaExportAdvanceTriggerExportedOutputTerminal outputTerminal1, RfsaExportAdvanceTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsaExportAdvanceTriggerExportedOutputTerminal | Specifies a RfsaExportAdvanceTriggerExportedOutputTerminal object. |
| outputTerminal2 | RfsaExportAdvanceTriggerExportedOutputTerminal | Specifies a RfsaExportAdvanceTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pfi0.html language=enus -->
## TOPIC 00206: Pfi0

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pfi0.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal Pfi0 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOutputTerminal re

### Pfi0

Gets the destination terminal when the signal is exported to the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "PFI0".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxiedstarc.html language=enus -->
## TOPIC 00207: PXIeDStarC

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxiedstarc.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxiedstarc.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal PXIeDStarC { get; }Rem

### PXIeDStarC

Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) PXIeDStarC { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "PXIe_DStarC".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxistarline.html language=enus -->
## TOPIC 00208: PxiStarLine

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxistarline.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI Star trigger line. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal PxiStarLine { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOutp

### PxiStarLine

Gets the destination terminal when the signal is exported to the PXI Star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) PxiStarLine { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "PXI_STAR".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00209: PxiTriggerLine0

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline0.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOut

### PxiTriggerLine0

Gets the destination terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00210: PxiTriggerLine1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOut

### PxiTriggerLine1

Gets the destination terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline3.html language=enus -->
## TOPIC 00211: PxiTriggerLine3

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal-pxitriggerline3.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportAdvanceTriggerExportedOutputTerminal PxiTriggerLine3 { get; }RemarksReturns an object of type RfsaExportAdvanceTriggerExportedOut

### PxiTriggerLine3

Gets the destination terminal when the signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [RfsaExportAdvanceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportadvancetriggerexportedoutputterminal.html) representing the string "PXI_Trig3".

Parent topic:

RfsaExportAdvanceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-clockout.html language=enus -->
## TOPIC 00212: ClockOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-clockout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-clockout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the CLK OUT connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal ClockOut { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExporte

### ClockOut

Gets the destination terminal when the signal is exported to the CLK OUT connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) ClockOut { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "ClkOut".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio1.html language=enus -->
## TOPIC 00213: Dio1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal Dio1 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### Dio1

Gets the source terminal when the trigger is received on the DIO PFI1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) Dio1 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI1".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio2.html language=enus -->
## TOPIC 00214: Dio2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal Dio2 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI2".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio3.html language=enus -->
## TOPIC 00215: Dio3

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio3.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal Dio3 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### Dio3

Gets the source terminal when the trigger is received on the DIO PFI3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) Dio3 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI3".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio4.html language=enus -->
## TOPIC 00216: Dio4

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio4.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal Dio4 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI4".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio5.html language=enus -->
## TOPIC 00217: Dio5

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio5.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal Dio5 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### Dio5

Gets the source terminal when the trigger is received on the DIO PFI5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) Dio5 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI5".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio6.html language=enus -->
## TOPIC 00218: Dio6

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio6.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal Dio6 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### Dio6

Gets the source terminal when the trigger is received on the DIO PFI6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) Dio6 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI6".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio7.html language=enus -->
## TOPIC 00219: Dio7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dio7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal Dio7 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI7".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dioo.html language=enus -->
## TOPIC 00220: DioO

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-dioo.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal DioO { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal r

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) DioO { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "DIO/PFI0".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-donotexport.html language=enus -->
## TOPIC 00221: DoNotExport

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-donotexport.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-donotexport.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is not exported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal DoNotExport { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockExportedOutputTerminal re

### DoNotExport

Gets the destination terminal when the signal is not exported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) DoNotExport { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing an empty string.

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-equals__object.html language=enus -->
## TOPIC 00222: Equals(object)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-equals__object.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaExportDigitizerSampleClockExportedOutputTerminal and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object t

### Equals(object)

Determines whether the current instance of [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsaExportDigitizerSampleClockExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-equals__rfsaexportdigitizersampleclockexportedoutputterminal.html language=enus -->
## TOPIC 00223: Equals(RfsaExportDigitizerSampleClockExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-equals__rfsaexportdigitizersampleclockexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-equals__rfsaexportdigitizersampleclockexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaExportDigitizerSampleClockExportedOutputTerminal object and the user specified RfsaExportDigitizerSampleClockExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaExportDigitizerSampleCloc

### Equals(RfsaExportDigitizerSampleClockExportedOutputTerminal)

Determines whether the current instance of [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) object and the user specified [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaExportDigitizerSampleClockExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsaExportDigitizerSampleClockExportedOutputTerminal | Specifies the RfsaExportDigitizerSampleClockExportedOutputTerminal object to be compared to the current instance of RfsaExportDigitizerSampleClockExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-gethashcode.html language=enus -->
## TOPIC 00224: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for RfsaExportDigitizerSampleClockExportedOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 containing the the hash code for RfsaExportDigitizerSampleClockExportedOutputTerminal.

### GetHashCode()

Returns the hash code for [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 containing the the hash code for [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html).

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-operator-string__rfsaexportdigitizersampleclockexportedoutputterminal.html language=enus -->
## TOPIC 00225: operator string(RfsaExportDigitizerSampleClockExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-operator-string__rfsaexportdigitizersampleclockexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-operator-string__rfsaexportdigitizersampleclockexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the RfsaExportDigitizerSampleClockExportedOutputTerminal object to the equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator string(RfsaExportDigitizerSampleClockExportedOutputTerminal outputTerminal)ParametersNameTypeDescriptionout

### operator string(RfsaExportDigitizerSampleClockExportedOutputTerminal)

Converts the [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) object to the equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator string(RfsaExportDigitizerSampleClockExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsaExportDigitizerSampleClockExportedOutputTerminal | Specifies the RfsaExportDigitizerSampleClockExportedOutputTerminal object to be converted to string. |

#### Returns

Returns a string from the [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) object.

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00226: PxiTriggerLine1

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline1.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleCloc

### PxiTriggerLine1

Gets the destination terminal when the signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline2.html language=enus -->
## TOPIC 00227: PxiTriggerLine2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal PxiTriggerLine2 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleCloc

### PxiTriggerLine2

Gets the destination terminal when the signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "PXI_Trig2".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline3.html language=enus -->
## TOPIC 00228: PxiTriggerLine3

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline3.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal PxiTriggerLine3 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleCloc

### PxiTriggerLine3

Gets the destination terminal when the signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "PXI_Trig3".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline4.html language=enus -->
## TOPIC 00229: PxiTriggerLine4

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline4.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal PxiTriggerLine4 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleCloc

### PxiTriggerLine4

Gets the destination terminal when the signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "PXI_Trig4".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline5.html language=enus -->
## TOPIC 00230: PxiTriggerLine5

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline5.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal PxiTriggerLine5 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleCloc

### PxiTriggerLine5

Gets the destination terminal when the signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "PXI_Trig5".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline6.html language=enus -->
## TOPIC 00231: PxiTriggerLine6

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline6.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal PxiTriggerLine6 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleCloc

### PxiTriggerLine6

Gets the destination terminal when the signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "PXI_Trig6".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline7.html language=enus -->
## TOPIC 00232: PxiTriggerLine7

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-pxitriggerline7.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal PxiTriggerLine7 { get; }RemarksReturns an object of type RfsaExportDigitizerSampleCloc

### PxiTriggerLine7

Gets the destination terminal when the signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "PXI_Trig7".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-referenceout.html language=enus -->
## TOPIC 00233: ReferenceOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-referenceout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-referenceout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the REF IN/OUT terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportDigitizerSampleClockExportedOutputTerminal ReferenceOut { get; }RemarksReturns an object of type RfsaExportDigitizerSampleClockE

### ReferenceOut

Gets the destination terminal when the signal is exported to the REF IN/OUT terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) ReferenceOut { get; }

#### Remarks

Returns an object of type [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) representing the string "RefOut".

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-tostring.html language=enus -->
## TOPIC 00234: ToString()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal-tostring.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsaExportDigitizerSampleClockExportedOutputTerminal to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override string ToString()ReturnsReturns a string that represents the current instance of RfsaExportDigitizerSampleClockExportedOutput

### ToString()

Converts the current instance of [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsaExportDigitizerSampleClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportdigitizersampleclockexportedoutputterminal.html).

Parent topic:

RfsaExportDigitizerSampleClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclock-exportrate.html language=enus -->
## TOPIC 00235: ExportRate

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclock-exportrate.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclock-exportrate.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the rate of the Reference clock export, in hertz (Hz). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic double ExportRate { get; set; }RemarksSpecifies a Double representing the rate of the Reference clock export. ExceptionsTypeDescriptionSystem.ObjectDisposedExcepti

### ExportRate

Gets or sets the rate of the Reference clock export, in hertz (Hz).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public double ExportRate { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the rate of the Reference clock export.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportRate property was accessed after the associated NIRfsa object was disposed. |

Parent topic:

RfsaExportReferenceClock Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclock.html language=enus -->
## TOPIC 00236: RfsaExportReferenceClock Class

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclock.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents properties used to export Reference clock. Derives fromRfsaSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic class RfsaExportReferenceClock : RfsaSubObjectRemarksFor more information, refer to NI RF Vector Signal Analyzers Help. PropertiesNameDescriptionExportR

### RfsaExportReferenceClock Class

Represents properties used to export Reference clock.

#### Derives from

- RfsaSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public class RfsaExportReferenceClock : RfsaSubObject

#### Remarks

For more information, refer to [NI RF Vector Signal Analyzers Help](https://nirfsa.chm::/nirfsa-help.html).

#### Properties

| Name | Description |
| --- | --- |
| ExportRate | Gets or sets the rate of the Reference clock export, in hertz (Hz). |
| OutputTerminal | Gets or sets a comma-separated list of the terminals at which to export the Reference clock. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsa

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-clockout.html language=enus -->
## TOPIC 00237: ClockOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-clockout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-clockout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the clock on the CLK OUT terminal on the LO. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceClockExportedOutputTerminal ClockOut { get; }RemarksReturns an object of type RfsaExportReferenceClockExportedOutputTerminal representing the string "ClkOu

### ClockOut

Gets the clock on the CLK OUT terminal on the LO.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) ClockOut { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) representing the string "ClkOut".

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-equals__rfsaexportreferenceclockexportedoutputterminal.html language=enus -->
## TOPIC 00238: Equals(RfsaExportReferenceClockExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-equals__rfsaexportreferenceclockexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-equals__rfsaexportreferenceclockexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsaExportReferenceClockExportedOutputTerminal and the RfsaExportReferenceClockExportedOutputTerminal object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic bool Equals(RfsaExportReferenceClockExportedOutputT

### Equals(RfsaExportReferenceClockExportedOutputTerminal)

Determines whether the current instance of [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) and the [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public bool Equals(RfsaExportReferenceClockExportedOutputTerminal outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | RfsaExportReferenceClockExportedOutputTerminal | Specifies the RfsaExportReferenceClockExportedOutputTerminal object to be compared to the current instance of RfsaExportReferenceClockExportedOutputTerminal. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-fromstring__string.html language=enus -->
## TOPIC 00239: FromString(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-fromstring__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsaExportReferenceClockExportedOutputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceClockExportedOutputTerminal FromString(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpe

### FromString(string)

Creates an [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) FromString(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies a string that is the outputTerminal of RfsaExportReferenceClock. |

#### Returns

Returns an object of type [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html).

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-gethashcode.html language=enus -->
## TOPIC 00240: GetHashCode()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-gethashcode.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsaExportReferenceClockExportedOutputTerminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override int GetHashCode()ReturnsReturns an Int32 containing the hash value generated for the current instance of RfsaExportReference

### GetHashCode()

Returns the hash code for the current instance of [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override int GetHashCode()

#### Returns

Returns an Int32 containing the hash value generated for the current instance of [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html).

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-ifcondrefout.html language=enus -->
## TOPIC 00241: IFCondRefOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-ifcondrefout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-ifcondrefout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets that the Reference clock is IfCondRefOut. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceClockExportedOutputTerminal IFCondRefOut { get; }RemarksReturns an object of type RfsaExportReferenceClockExportedOutputTerminal representing the string "IFCo

### IFCondRefOut

Gets that the Reference clock is IfCondRefOut.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) IFCondRefOut { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) representing the string "IFCondRefOut".

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-operator-rfsaexportreferenceclockexportedoutputterminal__string.html language=enus -->
## TOPIC 00242: operator RfsaExportReferenceClockExportedOutputTerminal(string)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-operator-rfsaexportreferenceclockexportedoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-operator-rfsaexportreferenceclockexportedoutputterminal__string.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to the equivalent RfsaExportReferenceClockExportedOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static implicit operator RfsaExportReferenceClockExportedOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutpu

### operator RfsaExportReferenceClockExportedOutputTerminal(string)

Converts the specified string to the equivalent [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static implicit operator RfsaExportReferenceClockExportedOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to the equivalent RfsaExportReferenceClockExportedOutputTerminal object. |

#### Returns

Returns an object of type [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) from the string passed in *outputTerminal*.

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-operator_eq__rfsaexportreferenceclockexportedoutputterminal-rfsaexportreferenceclockexportedoutputterminal.html language=enus -->
## TOPIC 00243: operator==(RfsaExportReferenceClockExportedOutputTerminal, RfsaExportReferenceClockExportedOutputTerminal)

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-operator_eq__rfsaexportreferenceclockexportedoutputterminal-rfsaexportreferenceclockexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-operator_eq__rfsaexportreferenceclockexportedoutputterminal-rfsaexportreferenceclockexportedoutputterminal.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsaExportReferenceClockExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static bool operator==(RfsaExportReferenceClockExportedOutputTerminal outputTerminal1, RfsaExportReferenceClockExportedOutputTerminal out

### operator==(RfsaExportReferenceClockExportedOutputTerminal, RfsaExportReferenceClockExportedOutputTerminal)

Checks whether the two instances of [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static bool operator==(RfsaExportReferenceClockExportedOutputTerminal outputTerminal1, RfsaExportReferenceClockExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsaExportReferenceClockExportedOutputTerminal | Specifies a RfsaExportReferenceClockExportedOutputTerminal object. |
| outputTerminal2 | RfsaExportReferenceClockExportedOutputTerminal | Specifies a RfsaExportReferenceClockExportedOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-referenceout.html language=enus -->
## TOPIC 00244: ReferenceOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-referenceout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-referenceout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the clock on the REF IN/OUT terminal or the REF OUT terminals. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceClockExportedOutputTerminal ReferenceOut { get; }RemarksReturns an object of type RfsaExportReferenceClockExportedOutputTerminal represen

### ReferenceOut

Gets the clock on the REF IN/OUT terminal or the REF OUT terminals.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) ReferenceOut { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) representing the string "RefOut".

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-tostring.html language=enus -->
## TOPIC 00245: ToString()

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal-tostring.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsaExportReferenceClockExportedOutputTerminal to a string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic override string ToString()ReturnsReturns a string that represents the current instance of RfsaExportReferenceClockExportedOutputTerminal.

### ToString()

Converts the current instance of [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html) to a string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsaExportReferenceClockExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferenceclockexportedoutputterminal.html).

Parent topic:

RfsaExportReferenceClockExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-clockout.html language=enus -->
## TOPIC 00246: ClockOut

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-clockout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-clockout.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the CLK OUT connector on the front panel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceTriggerExportedOutputTerminal ClockOut { get; }RemarksReturns an object of type RfsaExportReferenceTri

### ClockOut

Gets the destination terminal when the signal is exported to the CLK OUT connector on the front panel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) ClockOut { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) representing the string "ClkOut".

Parent topic:

RfsaExportReferenceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio2.html language=enus -->
## TOPIC 00247: Dio2

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio2.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceTriggerExportedOutputTerminal Dio2 { get; }RemarksReturns an object of type RfsaExportReferenceTriggerExportedOutputTerminal represent

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) representing the string "DIO/PFI2".

Parent topic:

RfsaExportReferenceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio3.html language=enus -->
## TOPIC 00248: Dio3

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio3.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceTriggerExportedOutputTerminal Dio3 { get; }RemarksReturns an object of type RfsaExportReferenceTriggerExportedOutputTerminal represent

### Dio3

Gets the source terminal when the trigger is received on the DIO PFI3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) Dio3 { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) representing the string "DIO/PFI3".

Parent topic:

RfsaExportReferenceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio4.html language=enus -->
## TOPIC 00249: Dio4

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio4.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceTriggerExportedOutputTerminal Dio4 { get; }RemarksReturns an object of type RfsaExportReferenceTriggerExportedOutputTerminal represent

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) representing the string "DIO/PFI4".

Parent topic:

RfsaExportReferenceTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsa-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio5.html language=enus -->
## TOPIC 00250: Dio5

- bundle_id: `ni_rfsa-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsa-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal-dio5.html
- document_id: `ni_rfsa-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsapublic static RfsaExportReferenceTriggerExportedOutputTerminal Dio5 { get; }RemarksReturns an object of type RfsaExportReferenceTriggerExportedOutputTerminal represent

### Dio5

Gets the source terminal when the trigger is received on the DIO PFI5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsa](nationalinstruments-modularinstruments-nirfsa.html)

public static [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) Dio5 { get; }

#### Remarks

Returns an object of type [RfsaExportReferenceTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsa-rfsaexportreferencetriggerexportedoutputterminal.html) representing the string "DIO/PFI5".

Parent topic:

RfsaExportReferenceTriggerExportedOutputTerminal Class
