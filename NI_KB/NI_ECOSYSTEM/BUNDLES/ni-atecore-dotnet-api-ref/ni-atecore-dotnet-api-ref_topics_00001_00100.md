# NI DOCUMENT BUNDLE: ni-atecore-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-atecore-dotnet-api-ref start=1 end=100 -->
<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session.html language=enus -->
## TOPIC 00001: AteCoreSession Class

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the session used to interact with the ATECCGEN2. Derives fromIAteCoreSessionSyntaxNamespace: NationalInstruments.AteCorepublic class AteCoreSession : IAteCoreSessionRemarks<threadsafety safety="unsafe"> To create a session, user application calls the static function CreateAteCoreSessionAs

### AteCoreSession Class

Represents the session used to interact with the ATECCGEN2.

#### Derives from

- IAteCoreSession

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public class AteCoreSession : IAteCoreSession

#### Remarks

<threadsafety safety="unsafe">

To create a session, user application calls the static function [CreateAteCoreSessionAsync](class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad8ed811ece9d56012572c73303aaffe1.html) by passing in the hostnameOrIPAddress and password as the input parameters, it will establish the network connection to the ATECCGEN2. If the network connection is succesfully established, a session will be returned. Subsequently, user can call other functions through the session to execute an operation on the ATECCGEN2. When user has completed tasks on ATECCGEN2, user calls the function [Dispose](class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad1dd307859bb12c591605459bbbdd676.html) to close the network connection.

#### Properties

| Name | Description |
| --- | --- |
| ACPowerDistributionUnits | Gets the array of AC Power Distribution Unit (IACPowerDistributionUnit). |
| DCPowerDistributionUnits | Gets the array of DC Power Distribution Unit (IDCPowerDistributionUnit). |
| FanDomains | Gets the array of Fan Domain (IFanDomain). Every Fan Domain contains a list of Fan Panel. |
| PowerEntryPanel | Gets the Power Entry Panel (IPowerEntryPanel). |
| RackControlUnit | Gets the Rack Control Unit (IRackControlUnit). |
| RackTemperatureSensorUnits | Gets the array of Rack Temperature Sensor Unit (IRackTemperatureSensorUnit). |
| UninterruptiblePowerSupplies | Gets the array of Uninterruptible Power Supply(UPS) (IUninterruptiblePowerSupply). |

#### Methods

| Name | Description |
| --- | --- |
| CreateAteCoreSessionAsync(string, string, bool) | Creates a new instance of the IAteCoreSession class by opening a session connected to the ATECCGEN2. |
| ChangeRackPasswordAsync(string, string) | Changes password on ATECCGEN2. |
| Dispose() | Close the session to ATECCGEN2. |
| GenerateAndApplyCertificateKeyPairAsync(int) | Generates and applies private and public key pair on ATECCGEN2. |
| GetFirmwareUpdateStatusAsync() | Gets the last firmware update status. |
| GetRackPowerStateAsync() | Gets the ATECCGEN2 power state. |
| GetRackSystemErrorsAsync() | Gets the ATECCGEN2 system errors. |
| GetRackSystemStateAsync() | Gets the ATECCGEN2 system state. |
| InitiateRackRestartAsync(RackRestartLevel) | Initiates a restart operation on ATECCGEN2. |
| IsInterlockConnectedAsync(Interlock) | Checks if Interlock is connected. |
| RefreshDCPowerDistributionUnitsAsync() | Refresh DC Power Distribution Units (DC PDU). |
| RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int) | Registers a UPS to the ATECCGEN2 system after physically installing a UPS. After registering a UPS, the UPS related monitoring features will not start until the rack is rebooted. |
| SetRackPowerStateToRunningAsync() | Sets ATECCGEN2 power state to Running. |
| SetRackPowerStateToStandbyAsync(bool) | Sets ATECCGEN2 power state to Standby. |
| SetTowerLightAsync(TowerLight, bool) | Sets Tower Light to be turned on or off. |
| UnregisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int) | Unregisters a UPS from the ATECCGEN2 system after physically uninstalling a UPS. A UPS should be unregistered using this function before physically removing it from a rack. |
| UpdateFirmwareAsync(string) | Updates firmware on ATECCGEN2. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a149d40acdfa2cc773d15306fb0edf434.html language=enus -->
## TOPIC 00002: RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a149d40acdfa2cc773d15306fb0edf434.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a149d40acdfa2cc773d15306fb0edf434.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers a UPS to the ATECCGEN2 system after physically installing a UPS. After registering a UPS, the UPS related monitoring features will not start until the rack is rebooted. SyntaxNamespace: NationalInstruments.AteCorepublic Task RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType poweredPha

### RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int)

Registers a UPS to the ATECCGEN2 system after physically installing a UPS. After registering a UPS, the UPS related monitoring features will not start until the rack is rebooted.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType poweredPhase, int poweredPhaseOutlet)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| poweredPhase | PowerPhaseType | Specifies the PEP power phase which the UPS is installed on (PowerPhaseType). |
| poweredPhaseOutlet | int | Specifies the PEP phase outlet which the UPS is installed on. Can be either 1 or 2. |

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a2bc861d9aac8fef86cb0f5691ec344ec.html language=enus -->
## TOPIC 00003: SetTowerLightAsync(TowerLight, bool)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a2bc861d9aac8fef86cb0f5691ec344ec.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a2bc861d9aac8fef86cb0f5691ec344ec.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Tower Light to be turned on or off. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetTowerLightAsync(TowerLight towerLight, bool isTurnedOn)ParametersNameTypeDescriptiontowerLightTowerLightSpecifies the Tower Light types (TowerLight). isTurnedOnboolSpecifies whether to turn on or off

### SetTowerLightAsync(TowerLight, bool)

Sets Tower Light to be turned on or off.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetTowerLightAsync(TowerLight towerLight, bool isTurnedOn)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| towerLight | TowerLight | Specifies the Tower Light types (TowerLight). |
| isTurnedOn | bool | Specifies whether to turn on or off the Tower Light. |

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a491ceaabe0f03cf2af855a81d9db6b1d.html language=enus -->
## TOPIC 00004: SetRackPowerStateToStandbyAsync(bool)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a491ceaabe0f03cf2af855a81d9db6b1d.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a491ceaabe0f03cf2af855a81d9db6b1d.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets ATECCGEN2 power state to Standby. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetRackPowerStateToStandbyAsync(bool forceStandby)ParametersNameTypeDescriptionforceStandbyboolSpecifies whether to force power down.

### SetRackPowerStateToStandbyAsync(bool)

Sets ATECCGEN2 power state to Standby.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetRackPowerStateToStandbyAsync(bool forceStandby)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| forceStandby | bool | Specifies whether to force power down. |

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a77030595e20b5b01ba4e1f14ba99b29f.html language=enus -->
## TOPIC 00005: UninterruptiblePowerSupplies

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a77030595e20b5b01ba4e1f14ba99b29f.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a77030595e20b5b01ba4e1f14ba99b29f.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of Uninterruptible Power Supply(UPS) (IUninterruptiblePowerSupply). SyntaxNamespace: NationalInstruments.AteCorepublic IUninterruptiblePowerSupply[] UninterruptiblePowerSupplies { get; }ReturnsReturns the array of Uninterruptible Power Supply(UPS) (IUninterruptiblePowerSupply).

### UninterruptiblePowerSupplies

Gets the array of Uninterruptible Power Supply(UPS) ([IUninterruptiblePowerSupply](interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IUninterruptiblePowerSupply](interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply.html)[] UninterruptiblePowerSupplies { get; }

#### Returns

Returns the array of Uninterruptible Power Supply(UPS) ([IUninterruptiblePowerSupply](interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply.html)).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a79b3baf729888606785e2e5480345060.html language=enus -->
## TOPIC 00006: GetRackSystemStateAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a79b3baf729888606785e2e5480345060.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a79b3baf729888606785e2e5480345060.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ATECCGEN2 system state. SyntaxNamespace: NationalInstruments.AteCorepublic Task< RackSystemState > GetRackSystemStateAsync()ReturnsReturns the ATECCGEN2 system state value (RackSystemState).

### GetRackSystemStateAsync()

Gets the ATECCGEN2 system state.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< [RackSystemState](namespace_national_instruments_1_1_ate_core_1a47c1db590f789e3a71ee8da2f5a9ea02.html) > GetRackSystemStateAsync()

#### Returns

Returns the ATECCGEN2 system state value ([RackSystemState](namespace_national_instruments_1_1_ate_core_1a47c1db590f789e3a71ee8da2f5a9ea02.html)).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a90b6fd110a16b14a89834070475fd915.html language=enus -->
## TOPIC 00007: FanDomains

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a90b6fd110a16b14a89834070475fd915.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a90b6fd110a16b14a89834070475fd915.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of Fan Domain (IFanDomain). Every Fan Domain contains a list of Fan Panel. SyntaxNamespace: NationalInstruments.AteCorepublic IFanDomain[] FanDomains { get; }ReturnsReturns the array of Fan Domain (IFanDomain).

### FanDomains

Gets the array of Fan Domain ([IFanDomain](interface_national_instruments_1_1_ate_core_1_1_i_fan_domain.html)). Every Fan Domain contains a list of Fan Panel.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IFanDomain](interface_national_instruments_1_1_ate_core_1_1_i_fan_domain.html)[] FanDomains { get; }

#### Returns

Returns the array of Fan Domain ([IFanDomain](interface_national_instruments_1_1_ate_core_1_1_i_fan_domain.html)).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aa7d33057fc4c6d9665648b47c7b3710b.html language=enus -->
## TOPIC 00008: RefreshDCPowerDistributionUnitsAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aa7d33057fc4c6d9665648b47c7b3710b.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aa7d33057fc4c6d9665648b47c7b3710b.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refresh DC Power Distribution Units (DC PDU). SyntaxNamespace: NationalInstruments.AteCorepublic Task RefreshDCPowerDistributionUnitsAsync()RemarksUpdates the DC Power Distribution Units detected. Use this method to update the DC Power Distribution Units detected after the ATECCGEN2 power state is s

### RefreshDCPowerDistributionUnitsAsync()

Refresh DC Power Distribution Units (DC PDU).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task RefreshDCPowerDistributionUnitsAsync()

#### Remarks

Updates the DC Power Distribution Units detected. Use this method to update the DC Power Distribution Units detected after the ATECCGEN2 power state is set to Running state.

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aaa8f9cd72f27ff7631bb9d4ebcee5fac.html language=enus -->
## TOPIC 00009: GetFirmwareUpdateStatusAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aaa8f9cd72f27ff7631bb9d4ebcee5fac.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aaa8f9cd72f27ff7631bb9d4ebcee5fac.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the last firmware update status. SyntaxNamespace: NationalInstruments.AteCorepublic Task< FirmwareUpdateStatus > GetFirmwareUpdateStatusAsync()ReturnsReturns the firmware update status (FirmwareUpdateStatus).

### GetFirmwareUpdateStatusAsync()

Gets the last firmware update status.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< [FirmwareUpdateStatus](namespace_national_instruments_1_1_ate_core_1ad3e7c808bcd6d68be8e40deba6b02fca.html) > GetFirmwareUpdateStatusAsync()

#### Returns

Returns the firmware update status ([FirmwareUpdateStatus](namespace_national_instruments_1_1_ate_core_1ad3e7c808bcd6d68be8e40deba6b02fca.html)).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1abe4ecc28308c6a39d29a6deb66919a15.html language=enus -->
## TOPIC 00010: ACPowerDistributionUnits

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1abe4ecc28308c6a39d29a6deb66919a15.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1abe4ecc28308c6a39d29a6deb66919a15.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of AC Power Distribution Unit (IACPowerDistributionUnit). SyntaxNamespace: NationalInstruments.AteCorepublic IACPowerDistributionUnit[] ACPowerDistributionUnits { get; }ReturnsReturns the array of AC Power Distribution Unit (IACPowerDistributionUnit).

### ACPowerDistributionUnits

Gets the array of AC Power Distribution Unit ([IACPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IACPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit.html)[] ACPowerDistributionUnits { get; }

#### Returns

Returns the array of AC Power Distribution Unit ([IACPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit.html)).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aca436b0ea5d231a37cfe770b69265373.html language=enus -->
## TOPIC 00011: UnregisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aca436b0ea5d231a37cfe770b69265373.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aca436b0ea5d231a37cfe770b69265373.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters a UPS from the ATECCGEN2 system after physically uninstalling a UPS. A UPS should be unregistered using this function before physically removing it from a rack. SyntaxNamespace: NationalInstruments.AteCorepublic Task UnregisterUninterruptiblePowerSupplyAsync(PowerPhaseType poweredPhase,

### UnregisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int)

Unregisters a UPS from the ATECCGEN2 system after physically uninstalling a UPS. A UPS should be unregistered using this function before physically removing it from a rack.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task UnregisterUninterruptiblePowerSupplyAsync(PowerPhaseType poweredPhase, int poweredPhaseOutlet)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| poweredPhase | PowerPhaseType | Specifies the PEP power phase which the UPS is installed on (PowerPhaseType). |
| poweredPhaseOutlet | int | Specifies the PEP phase outlet which the UPS is installed on. Can be either 1 or 2. |

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1acd149459bd033c26a710ec51430c92ca.html language=enus -->
## TOPIC 00012: InitiateRackRestartAsync(RackRestartLevel)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1acd149459bd033c26a710ec51430c92ca.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1acd149459bd033c26a710ec51430c92ca.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a restart operation on ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic Task InitiateRackRestartAsync(RackRestartLevel restartLevel)ParametersNameTypeDescriptionrestartLevelRackRestartLevelSpecifies restart level (RackRestartLevel).

### InitiateRackRestartAsync(RackRestartLevel)

Initiates a restart operation on ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task InitiateRackRestartAsync(RackRestartLevel restartLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| restartLevel | RackRestartLevel | Specifies restart level (RackRestartLevel). |

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad1dd307859bb12c591605459bbbdd676.html language=enus -->
## TOPIC 00013: Dispose()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad1dd307859bb12c591605459bbbdd676.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad1dd307859bb12c591605459bbbdd676.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Close the session to ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic void Dispose()

### Dispose()

Close the session to ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public void Dispose()

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad8ed811ece9d56012572c73303aaffe1.html language=enus -->
## TOPIC 00014: CreateAteCoreSessionAsync(string, string, bool)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad8ed811ece9d56012572c73303aaffe1.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ad8ed811ece9d56012572c73303aaffe1.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the IAteCoreSession class by opening a session connected to the ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic static Task< IAteCoreSession > CreateAteCoreSessionAsync(string hostnameOrIPAddress, string password="", bool rememberPassword=false)ParametersNameT

### CreateAteCoreSessionAsync(string, string, bool)

Creates a new instance of the [IAteCoreSession](interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session.html) class by opening a session connected to the ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public static Task< [IAteCoreSession](interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session.html) > CreateAteCoreSessionAsync(string hostnameOrIPAddress, string password="", bool rememberPassword=false)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| hostnameOrIPAddress | string | Specifies the hostname or IP address of ATECCGEN2. |
| password | string | Specifies the password to authenticate to the ATECCGEN2. |
| rememberPassword | bool | Set to true to remember password. Default value set to false |

#### Returns

Returns the instance of [IAteCoreSession](interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session.html).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ada7a6e84cb8d4c4c6f8f062e7b7a79dd.html language=enus -->
## TOPIC 00015: GetRackPowerStateAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ada7a6e84cb8d4c4c6f8f062e7b7a79dd.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ada7a6e84cb8d4c4c6f8f062e7b7a79dd.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ATECCGEN2 power state. SyntaxNamespace: NationalInstruments.AteCorepublic Task< RackPowerState > GetRackPowerStateAsync()ReturnsReturns the ATECCGEN2 power state value (RackPowerState).

### GetRackPowerStateAsync()

Gets the ATECCGEN2 power state.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< [RackPowerState](namespace_national_instruments_1_1_ate_core_1ae5923dd725b7af4a3b59c5d351be4598.html) > GetRackPowerStateAsync()

#### Returns

Returns the ATECCGEN2 power state value ([RackPowerState](namespace_national_instruments_1_1_ate_core_1ae5923dd725b7af4a3b59c5d351be4598.html)).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ada8db4f6ebde7fc7cc4d3662f153a5da.html language=enus -->
## TOPIC 00016: RackControlUnit

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ada8db4f6ebde7fc7cc4d3662f153a5da.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1ada8db4f6ebde7fc7cc4d3662f153a5da.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Rack Control Unit (IRackControlUnit). SyntaxNamespace: NationalInstruments.AteCorepublic IRackControlUnit RackControlUnit { get; }ReturnsReturns the Rack Control Unit (IRackControlUnit).

### RackControlUnit

Gets the Rack Control Unit ([IRackControlUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_control_unit.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IRackControlUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_control_unit.html) RackControlUnit { get; }

#### Returns

Returns the Rack Control Unit ([IRackControlUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_control_unit.html)).

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_ate_core_session_1adda33ff453a1bdcaecb8054976ccfe15.html language=enus -->
## TOPIC 00017: UpdateFirmwareAsync(string)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_ate_core_session_1adda33ff453a1bdcaecb8054976ccfe15.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_ate_core_session_1adda33ff453a1bdcaecb8054976ccfe15.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates firmware on ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic Task UpdateFirmwareAsync(string firmwareFilePath)ParametersNameTypeDescriptionfirmwareFilePathstringSpecifies firmware file path to update to.

### UpdateFirmwareAsync(string)

Updates firmware on ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task UpdateFirmwareAsync(string firmwareFilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| firmwareFilePath | string | Specifies firmware file path to update to. |

Parent topic:

AteCoreSession Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a065b3df60c99d72f9dc0a90b574918b3.html language=enus -->
## TOPIC 00018: NIATECORE_ERROR_INVALID_ARGUMENT

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a065b3df60c99d72f9dc0a90b574918b3.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a065b3df60c99d72f9dc0a90b574918b3.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: One or more of the provided arguments are invalid. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERROR_INVALID_ARGUMENT

### NIATECORE_ERROR_INVALID_ARGUMENT

One or more of the provided arguments are invalid.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERROR_INVALID_ARGUMENT

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a26642abc8514954c28ffb575d340c884.html language=enus -->
## TOPIC 00019: NIATECORE_ERR_CONNECTION_TIMEOUT

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a26642abc8514954c28ffb575d340c884.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a26642abc8514954c28ffb575d340c884.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A timeout occurred when connecting to the target rack. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_CONNECTION_TIMEOUT

### NIATECORE_ERR_CONNECTION_TIMEOUT

A timeout occurred when connecting to the target rack.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_CONNECTION_TIMEOUT

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a31759dbbef4b459ecb93fee9a69f3693.html language=enus -->
## TOPIC 00020: NIATECORE_UNSUPPORTED_OPERATION

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a31759dbbef4b459ecb93fee9a69f3693.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a31759dbbef4b459ecb93fee9a69f3693.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The requested operation is not supported. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_UNSUPPORTED_OPERATION

### NIATECORE_UNSUPPORTED_OPERATION

The requested operation is not supported.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_UNSUPPORTED_OPERATION

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a4f5398d5380bda63db24ff27ea7b1c6b.html language=enus -->
## TOPIC 00021: NIATECORE_ERR_CHANNEL_ERROR

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a4f5398d5380bda63db24ff27ea7b1c6b.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a4f5398d5380bda63db24ff27ea7b1c6b.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: An error occurred on the communication channel processing this request. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_CHANNEL_ERROR

### NIATECORE_ERR_CHANNEL_ERROR

An error occurred on the communication channel processing this request.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_CHANNEL_ERROR

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a809a32876698df8f6780cc8f7b163548.html language=enus -->
## TOPIC 00022: NIATECORE_ERR_MCU_ERROR

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a809a32876698df8f6780cc8f7b163548.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a809a32876698df8f6780cc8f7b163548.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: An error occurred on the target rack's MCU. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_MCU_ERROR

### NIATECORE_ERR_MCU_ERROR

An error occurred on the target rack's MCU.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_MCU_ERROR

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a93b4abfb81c80cd95a4c4b93c07b4fdb.html language=enus -->
## TOPIC 00023: NIATECORE_SUCCESS

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a93b4abfb81c80cd95a4c4b93c07b4fdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1a93b4abfb81c80cd95a4c4b93c07b4fdb.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Successfully execute an operation. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_SUCCESS

### NIATECORE_SUCCESS

Successfully execute an operation.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_SUCCESS

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aa6817b8fdfad59102f3fbdb7ec31fce2.html language=enus -->
## TOPIC 00024: NIATECORE_ERR_PASSWORD_DELETE_FAILED

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aa6817b8fdfad59102f3fbdb7ec31fce2.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aa6817b8fdfad59102f3fbdb7ec31fce2.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Failed to delete saved password. Users should ensure correct hostname or IP address is specified. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_PASSWORD_DELETE_FAILED

### NIATECORE_ERR_PASSWORD_DELETE_FAILED

Failed to delete saved password. Users should ensure correct hostname or IP address is specified.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_PASSWORD_DELETE_FAILED

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab60c19ff457563cc407e7cafa68aa991.html language=enus -->
## TOPIC 00025: NIATECORE_ERR_INVALID_SESSION

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab60c19ff457563cc407e7cafa68aa991.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab60c19ff457563cc407e7cafa68aa991.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The specified session could not be found. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_INVALID_SESSION

### NIATECORE_ERR_INVALID_SESSION

The specified session could not be found.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_INVALID_SESSION

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab6ca09d5333769ad5371a0e98cdacd95.html language=enus -->
## TOPIC 00026: NIATECORE_ERR_TLS_CERT_NOT_FOUND

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab6ca09d5333769ad5371a0e98cdacd95.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab6ca09d5333769ad5371a0e98cdacd95.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: TLS certificate for gRPC channel cannot be found. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_TLS_CERT_NOT_FOUND

### NIATECORE_ERR_TLS_CERT_NOT_FOUND

TLS certificate for gRPC channel cannot be found.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_TLS_CERT_NOT_FOUND

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab802e286167226233e6c9bd022420ba1.html language=enus -->
## TOPIC 00027: NIATECORE_ERR_PASSWORD_SAVE_FAILED

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab802e286167226233e6c9bd022420ba1.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ab802e286167226233e6c9bd022420ba1.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Failed to save password due to an internal error. Users can retry the operation. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_PASSWORD_SAVE_FAILED

### NIATECORE_ERR_PASSWORD_SAVE_FAILED

Failed to save password due to an internal error. Users can retry the operation.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_PASSWORD_SAVE_FAILED

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1acebdafbd3e88942e44b1062b43b938b5.html language=enus -->
## TOPIC 00028: NIATECORE_ERR_RCU_NATIVE_ERROR

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1acebdafbd3e88942e44b1062b43b938b5.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1acebdafbd3e88942e44b1062b43b938b5.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: An error occurred on the target rack's RCU. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_RCU_NATIVE_ERROR

### NIATECORE_ERR_RCU_NATIVE_ERROR

An error occurred on the target rack's RCU.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_RCU_NATIVE_ERROR

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ad044084179bee1916a0ff7132e1ff703.html language=enus -->
## TOPIC 00029: NIATECORE_ERR_INVALID_FIRMWARE_FILE

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ad044084179bee1916a0ff7132e1ff703.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ad044084179bee1916a0ff7132e1ff703.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The provided firmware update file is invalid. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_INVALID_FIRMWARE_FILE

### NIATECORE_ERR_INVALID_FIRMWARE_FILE

The provided firmware update file is invalid.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_INVALID_FIRMWARE_FILE

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ad96c5f504b0f88739f31d8bf8813b620.html language=enus -->
## TOPIC 00030: NIATECORE_ERR_INVALID_ATTRIBUTE_TYPE

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ad96c5f504b0f88739f31d8bf8813b620.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1ad96c5f504b0f88739f31d8bf8813b620.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The expected return type of the provided attribute does not match the return type of the requested function. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_INVALID_ATTRIBUTE_TYPE

### NIATECORE_ERR_INVALID_ATTRIBUTE_TYPE

The expected return type of the provided attribute does not match the return type of the requested function.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_INVALID_ATTRIBUTE_TYPE

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aee6cda2a27c49460baa34c82d380ec25.html language=enus -->
## TOPIC 00031: NIATECORE_ERR_INSUFFICIENT_BUFFER

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aee6cda2a27c49460baa34c82d380ec25.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aee6cda2a27c49460baa34c82d380ec25.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The buffer is too small for the requested data. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_INSUFFICIENT_BUFFER

### NIATECORE_ERR_INSUFFICIENT_BUFFER

The buffer is too small for the requested data.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_INSUFFICIENT_BUFFER

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aeff279c993c95318854ec902a822c562.html language=enus -->
## TOPIC 00032: NIATECORE_ERR_DLL_ERROR

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aeff279c993c95318854ec902a822c562.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_status_code_1_1_ate_core_status_code_1aeff279c993c95318854ec902a822c562.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: An incompatible driver version is installed or driver is not found. SyntaxNamespace: NationalInstruments.AteCore.StatusCodepublic static readonly int NIATECORE_ERR_DLL_ERROR

### NIATECORE_ERR_DLL_ERROR

An incompatible driver version is installed or driver is not found.

#### Syntax

**Namespace:**[NationalInstruments.AteCore.StatusCode](namespace_national_instruments_1_1_ate_core_1_1_status_code.html)

public static readonly int NIATECORE_ERR_DLL_ERROR

Parent topic:

AteCoreStatusCode Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_system_status.html language=enus -->
## TOPIC 00033: SystemStatus Class

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_system_status.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_system_status.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides System Status for ATECCGEN2. Derives fromNoneSyntaxNamespace: NationalInstruments.AteCorepublic class SystemStatusRemarksContains properties of StatusCode and StatusMessage and use to get system error list from ATECCGEN2 using GetRackSystemErrorsAsync. ConstructorsNameDescriptionSystemStatu

### SystemStatus Class

Provides System Status for ATECCGEN2.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public class SystemStatus

#### Remarks

Contains properties of [StatusCode](class_national_instruments_1_1_ate_core_1_1_system_status_1a7cbbfcdb6cee191df382d86631b48b9a.html) and [StatusMessage](class_national_instruments_1_1_ate_core_1_1_system_status_1ab2502afae36a2ffb0645a381eae4a62b.html) and use to get system error list from ATECCGEN2 using [GetRackSystemErrorsAsync](class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a5c918d768e12b98d1432d6c2841fd235.html).

#### Constructors

| Name | Description |
| --- | --- |
| SystemStatus(int, string) | Constructor for System Status class. |

#### Properties

| Name | Description |
| --- | --- |
| StatusCode | Specifies the status code. |
| StatusMessage | Specifies the status message. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=class_national_instruments_1_1_ate_core_1_1_system_status_1ab2502afae36a2ffb0645a381eae4a62b.html language=enus -->
## TOPIC 00034: StatusMessage

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `class_national_instruments_1_1_ate_core_1_1_system_status_1ab2502afae36a2ffb0645a381eae4a62b.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/class_national_instruments_1_1_ate_core_1_1_system_status_1ab2502afae36a2ffb0645a381eae4a62b.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the status message. SyntaxNamespace: NationalInstruments.AteCorepublic string StatusMessage { get; }RemarksError message happens in ATECCGEN2.

### StatusMessage

Specifies the status message.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string StatusMessage { get; }

#### Remarks

Error message happens in ATECCGEN2.

Parent topic:

SystemStatus Class

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit_1a587dba6092e70e71822499c4b38940f9.html language=enus -->
## TOPIC 00035: this[int index]

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit_1a587dba6092e70e71822499c4b38940f9.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit_1a587dba6092e70e71822499c4b38940f9.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the specified Power Bank by index (IPowerBank). SyntaxNamespace: NationalInstruments.AteCorepublic IPowerBank this[int index] { get; }ParametersNameTypeDescriptionindexintSpecifies the index of the Power Bank to get. ReturnsReturns the power bank object corresponding the index (IPowerBank).

### this[int index]

Gets the specified Power Bank by index ([IPowerBank](interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IPowerBank](interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html) this[int index] { get; }

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | int | Specifies the index of the Power Bank to get. |

#### Returns

Returns the power bank object corresponding the index ([IPowerBank](interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html)).

Parent topic:

IACPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit_1a75e65aefb4129f39ee30d84161184834.html language=enus -->
## TOPIC 00036: PowerBanks

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit_1a75e65aefb4129f39ee30d84161184834.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit_1a75e65aefb4129f39ee30d84161184834.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of the power banks (IPowerBank). SyntaxNamespace: NationalInstruments.AteCorepublic IPowerBank[] PowerBanks { get; }ReturnsReturns the array of the power banks (IPowerBank).

### PowerBanks

Gets the array of the power banks ([IPowerBank](interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IPowerBank](interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html)[] PowerBanks { get; }

#### Returns

Returns the array of the power banks ([IPowerBank](interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html)).

Parent topic:

IACPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session.html language=enus -->
## TOPIC 00037: IAteCoreSession Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface for session used to interact with the ATECCGEN2. Derives fromIDisposableSyntaxNamespace: NationalInstruments.AteCorepublic interface IAteCoreSession : IDisposableRemarks<threadsafety safety="unsafe"> PropertiesNameDescriptionACPowerDistributionUnitsGets the array of AC Power

### IAteCoreSession Interface

Represents the interface for session used to interact with the ATECCGEN2.

#### Derives from

- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface IAteCoreSession : IDisposable

#### Remarks

<threadsafety safety="unsafe">

#### Properties

| Name | Description |
| --- | --- |
| ACPowerDistributionUnits | Gets the array of AC Power Distribution Unit (IACPowerDistributionUnit). |
| DCPowerDistributionUnits | Gets the array of DC Power Distribution Unit (IDCPowerDistributionUnit). |
| FanDomains | Gets the array of Fan Domain (IFanDomain). Every Fan Domain contains a list of Fan Panel. |
| PowerEntryPanel | Gets the Power Entry Panel (IPowerEntryPanel). |
| RackControlUnit | Gets the Rack Control Unit (IRackControlUnit). |
| RackTemperatureSensorUnits | Gets the array of Rack Temperature Sensor Unit (IRackTemperatureSensorUnit). |
| UninterruptiblePowerSupplies | Gets the array of Uninterruptible Power Supply(UPS) (IUninterruptiblePowerSupply). |

#### Methods

| Name | Description |
| --- | --- |
| ChangeRackPasswordAsync(string, string) | Changes password on ATECCGEN2. |
| GenerateAndApplyCertificateKeyPairAsync(int) | Generates and applies private and public key pair on ATECCGEN2. |
| GetFirmwareUpdateStatusAsync() | Gets the last firmware update status. |
| GetRackPowerStateAsync() | Gets the ATECCGEN2 power state. |
| GetRackSystemErrorsAsync() | Gets the ATECCGEN2 system errors. |
| GetRackSystemStateAsync() | Gets the ATECCGEN2 system state. |
| InitiateRackRestartAsync(RackRestartLevel) | Initiates a restart operation on ATECCGEN2. |
| IsInterlockConnectedAsync(Interlock) | Checks if Interlock is connected. |
| RefreshDCPowerDistributionUnitsAsync() | Refresh DC Power Distribution Units (DC PDU). |
| RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int) | Registers a UPS to the ATECCGEN2 system after physically installing a UPS. After registering a UPS, the UPS related monitoring features will not start until the rack is rebooted. |
| SetRackPowerStateToRunningAsync() | Sets ATECCGEN2 power state to Running. |
| SetRackPowerStateToStandbyAsync(bool) | Sets ATECCGEN2 power state to Standby. |
| SetTowerLightAsync(TowerLight, bool) | Sets Tower Light to be turned on or off. |
| UnregisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int) | Unregisters a UPS from the ATECCGEN2 system after physically uninstalling a UPS. A UPS should be unregistered using this function before physically removing it from a rack. |
| UpdateFirmwareAsync(string) | Updates firmware on ATECCGEN2. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a5d6a70c584c03714967dd50d426fc3f7.html language=enus -->
## TOPIC 00038: SetRackPowerStateToStandbyAsync(bool)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a5d6a70c584c03714967dd50d426fc3f7.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a5d6a70c584c03714967dd50d426fc3f7.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets ATECCGEN2 power state to Standby. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetRackPowerStateToStandbyAsync(bool forceStandby)ParametersNameTypeDescriptionforceStandbyboolSpecifies whether to force power down.

### SetRackPowerStateToStandbyAsync(bool)

Sets ATECCGEN2 power state to Standby.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetRackPowerStateToStandbyAsync(bool forceStandby)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| forceStandby | bool | Specifies whether to force power down. |

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a612234219381d1f7da27f4ee6a22237a.html language=enus -->
## TOPIC 00039: PowerEntryPanel

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a612234219381d1f7da27f4ee6a22237a.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a612234219381d1f7da27f4ee6a22237a.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Power Entry Panel (IPowerEntryPanel). SyntaxNamespace: NationalInstruments.AteCorepublic IPowerEntryPanel PowerEntryPanel { get; }ReturnsReturns the Power Entry Panel (IPowerEntryPanel).

### PowerEntryPanel

Gets the Power Entry Panel ([IPowerEntryPanel](interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IPowerEntryPanel](interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel.html) PowerEntryPanel { get; }

#### Returns

Returns the Power Entry Panel ([IPowerEntryPanel](interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel.html)).

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a617d569eb622f9bf09318fa8e4fc6183.html language=enus -->
## TOPIC 00040: GetRackSystemStateAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a617d569eb622f9bf09318fa8e4fc6183.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a617d569eb622f9bf09318fa8e4fc6183.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ATECCGEN2 system state. SyntaxNamespace: NationalInstruments.AteCorepublic Task< RackSystemState > GetRackSystemStateAsync()ReturnsReturns the ATECCGEN2 system state value (RackSystemState).

### GetRackSystemStateAsync()

Gets the ATECCGEN2 system state.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< [RackSystemState](namespace_national_instruments_1_1_ate_core_1a47c1db590f789e3a71ee8da2f5a9ea02.html) > GetRackSystemStateAsync()

#### Returns

Returns the ATECCGEN2 system state value ([RackSystemState](namespace_national_instruments_1_1_ate_core_1a47c1db590f789e3a71ee8da2f5a9ea02.html)).

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a73c5bbde61f1d173330de98d958bb23f.html language=enus -->
## TOPIC 00041: RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a73c5bbde61f1d173330de98d958bb23f.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a73c5bbde61f1d173330de98d958bb23f.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers a UPS to the ATECCGEN2 system after physically installing a UPS. After registering a UPS, the UPS related monitoring features will not start until the rack is rebooted. SyntaxNamespace: NationalInstruments.AteCorepublic Task RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType poweredPha

### RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType, int)

Registers a UPS to the ATECCGEN2 system after physically installing a UPS. After registering a UPS, the UPS related monitoring features will not start until the rack is rebooted.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task RegisterUninterruptiblePowerSupplyAsync(PowerPhaseType poweredPhase, int poweredPhaseOutlet)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| poweredPhase | PowerPhaseType | Specifies the PEP power phase which the UPS is installed on (PowerPhaseType). |
| poweredPhaseOutlet | int | Specifies the PEP phase outlet which the UPS is installed on. Can be either 1 or 2. |

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a75067e38da9f5c95b1740f13953e58d7.html language=enus -->
## TOPIC 00042: GenerateAndApplyCertificateKeyPairAsync(int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a75067e38da9f5c95b1740f13953e58d7.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a75067e38da9f5c95b1740f13953e58d7.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates and applies private and public key pair on ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic Task GenerateAndApplyCertificateKeyPairAsync(int daysValid)ParametersNameTypeDescriptiondaysValidintSpecifies the number of days to certify the new certificate for.

### GenerateAndApplyCertificateKeyPairAsync(int)

Generates and applies private and public key pair on ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task GenerateAndApplyCertificateKeyPairAsync(int daysValid)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| daysValid | int | Specifies the number of days to certify the new certificate for. |

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a7ddb7e23f86535474cb5103d70fed39b.html language=enus -->
## TOPIC 00043: DCPowerDistributionUnits

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a7ddb7e23f86535474cb5103d70fed39b.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a7ddb7e23f86535474cb5103d70fed39b.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of DC Power Distribution Unit (IDCPowerDistributionUnit). SyntaxNamespace: NationalInstruments.AteCorepublic IDCPowerDistributionUnit[] DCPowerDistributionUnits { get; }ReturnsReturns the array of DC Power Distribution Unit (IDCPowerDistributionUnit).

### DCPowerDistributionUnits

Gets the array of DC Power Distribution Unit ([IDCPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IDCPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit.html)[] DCPowerDistributionUnits { get; }

#### Returns

Returns the array of DC Power Distribution Unit ([IDCPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit.html)).

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a866fa0492197e4a3a3ba72b11cc4be75.html language=enus -->
## TOPIC 00044: UpdateFirmwareAsync(string)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a866fa0492197e4a3a3ba72b11cc4be75.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a866fa0492197e4a3a3ba72b11cc4be75.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates firmware on ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic Task UpdateFirmwareAsync(string firmwareFilePath)ParametersNameTypeDescriptionfirmwareFilePathstringSpecifies firmware file path to update to.

### UpdateFirmwareAsync(string)

Updates firmware on ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task UpdateFirmwareAsync(string firmwareFilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| firmwareFilePath | string | Specifies firmware file path to update to. |

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a97e1a249c8cb0901c800f36a6989bafe.html language=enus -->
## TOPIC 00045: SetRackPowerStateToRunningAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a97e1a249c8cb0901c800f36a6989bafe.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a97e1a249c8cb0901c800f36a6989bafe.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets ATECCGEN2 power state to Running. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetRackPowerStateToRunningAsync()

### SetRackPowerStateToRunningAsync()

Sets ATECCGEN2 power state to Running.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetRackPowerStateToRunningAsync()

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a9baaec665ae3adf7e49a11742245df82.html language=enus -->
## TOPIC 00046: RackTemperatureSensorUnits

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a9baaec665ae3adf7e49a11742245df82.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1a9baaec665ae3adf7e49a11742245df82.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of Rack Temperature Sensor Unit (IRackTemperatureSensorUnit). SyntaxNamespace: NationalInstruments.AteCorepublic IRackTemperatureSensorUnit[] RackTemperatureSensorUnits { get; }ReturnsReturns the array of Rack Temperature Sensor Unit (IRackTemperatureSensorUnit).

### RackTemperatureSensorUnits

Gets the array of Rack Temperature Sensor Unit ([IRackTemperatureSensorUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_temperature_sensor_unit.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IRackTemperatureSensorUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_temperature_sensor_unit.html)[] RackTemperatureSensorUnits { get; }

#### Returns

Returns the array of Rack Temperature Sensor Unit ([IRackTemperatureSensorUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_temperature_sensor_unit.html)).

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1aa180c093de1d5e40aad851eb5f68965e.html language=enus -->
## TOPIC 00047: FanDomains

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1aa180c093de1d5e40aad851eb5f68965e.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1aa180c093de1d5e40aad851eb5f68965e.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of Fan Domain (IFanDomain). Every Fan Domain contains a list of Fan Panel. SyntaxNamespace: NationalInstruments.AteCorepublic IFanDomain[] FanDomains { get; }ReturnsReturns the array of Fan Domain (IFanDomain).

### FanDomains

Gets the array of Fan Domain ([IFanDomain](interface_national_instruments_1_1_ate_core_1_1_i_fan_domain.html)). Every Fan Domain contains a list of Fan Panel.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IFanDomain](interface_national_instruments_1_1_ate_core_1_1_i_fan_domain.html)[] FanDomains { get; }

#### Returns

Returns the array of Fan Domain ([IFanDomain](interface_national_instruments_1_1_ate_core_1_1_i_fan_domain.html)).

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ab9f0b38453b57ccd8ed4cf32e5afee34.html language=enus -->
## TOPIC 00048: ACPowerDistributionUnits

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ab9f0b38453b57ccd8ed4cf32e5afee34.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ab9f0b38453b57ccd8ed4cf32e5afee34.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of AC Power Distribution Unit (IACPowerDistributionUnit). SyntaxNamespace: NationalInstruments.AteCorepublic IACPowerDistributionUnit[] ACPowerDistributionUnits { get; }ReturnsReturns the array of AC Power Distribution Unit (IACPowerDistributionUnit).

### ACPowerDistributionUnits

Gets the array of AC Power Distribution Unit ([IACPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IACPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit.html)[] ACPowerDistributionUnits { get; }

#### Returns

Returns the array of AC Power Distribution Unit ([IACPowerDistributionUnit](interface_national_instruments_1_1_ate_core_1_1_i_a_c_power_distribution_unit.html)).

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ac6f32d666ed4c4c6eadc794853f69c2d.html language=enus -->
## TOPIC 00049: SetTowerLightAsync(TowerLight, bool)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ac6f32d666ed4c4c6eadc794853f69c2d.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ac6f32d666ed4c4c6eadc794853f69c2d.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Tower Light to be turned on or off. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetTowerLightAsync(TowerLight towerLight, bool isTurnedOn)ParametersNameTypeDescriptiontowerLightTowerLightSpecifies the Tower Light types (TowerLight). isTurnedOnboolSpecifies whether to turn on or off

### SetTowerLightAsync(TowerLight, bool)

Sets Tower Light to be turned on or off.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetTowerLightAsync(TowerLight towerLight, bool isTurnedOn)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| towerLight | TowerLight | Specifies the Tower Light types (TowerLight). |
| isTurnedOn | bool | Specifies whether to turn on or off the Tower Light. |

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ae38d890e7da95c377e9e4298c017ccb4.html language=enus -->
## TOPIC 00050: RefreshDCPowerDistributionUnitsAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ae38d890e7da95c377e9e4298c017ccb4.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1ae38d890e7da95c377e9e4298c017ccb4.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refresh DC Power Distribution Units (DC PDU). SyntaxNamespace: NationalInstruments.AteCorepublic Task RefreshDCPowerDistributionUnitsAsync()RemarksUpdates the DC Power Distribution Units detected. Use this method to update the DC Power Distribution Units detected after the ATECCGEN2 power state is s

### RefreshDCPowerDistributionUnitsAsync()

Refresh DC Power Distribution Units (DC PDU).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task RefreshDCPowerDistributionUnitsAsync()

#### Remarks

Updates the DC Power Distribution Units detected. Use this method to update the DC Power Distribution Units detected after the ATECCGEN2 power state is set to Running state.

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1af799ab88d41db01d899e2ae7f4575ca6.html language=enus -->
## TOPIC 00051: ChangeRackPasswordAsync(string, string)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1af799ab88d41db01d899e2ae7f4575ca6.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1af799ab88d41db01d899e2ae7f4575ca6.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes password on ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic Task ChangeRackPasswordAsync(string currentPassword, string newPassword)ParametersNameTypeDescriptioncurrentPasswordstringSpecifies current password. newPasswordstringSpecifies new password to be changed.

### ChangeRackPasswordAsync(string, string)

Changes password on ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task ChangeRackPasswordAsync(string currentPassword, string newPassword)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| currentPassword | string | Specifies current password. |
| newPassword | string | Specifies new password to be changed. |

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1afea89752e838c984dbcc02ec621dc07a.html language=enus -->
## TOPIC 00052: RackControlUnit

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1afea89752e838c984dbcc02ec621dc07a.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session_1afea89752e838c984dbcc02ec621dc07a.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Rack Control Unit (IRackControlUnit). SyntaxNamespace: NationalInstruments.AteCorepublic IRackControlUnit RackControlUnit { get; }ReturnsReturns the Rack Control Unit (IRackControlUnit).

### RackControlUnit

Gets the Rack Control Unit ([IRackControlUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_control_unit.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IRackControlUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_control_unit.html) RackControlUnit { get; }

#### Returns

Returns the Rack Control Unit ([IRackControlUnit](interface_national_instruments_1_1_ate_core_1_1_i_rack_control_unit.html)).

Parent topic:

IAteCoreSession Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_component.html language=enus -->
## TOPIC 00053: IComponent Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_component.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_component.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface for the component. Derives fromNoneSyntaxNamespace: NationalInstruments.AteCorepublic interface IComponentRemarks<threadsafety safety="unsafe"> The components detected on an ATECCGEN2 are stored in the corresponding property (ACPowerDistributionUnits, DCPowerDistributionUnit

### IComponent Interface

Represents the interface for the component.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface IComponent

#### Remarks

<threadsafety safety="unsafe">

The components detected on an ATECCGEN2 are stored in the corresponding property (ACPowerDistributionUnits, DCPowerDistributionUnits, PowerEntryPanel, RackControlUnit, FanDomains) of [IAteCoreSession](interface_national_instruments_1_1_ate_core_1_1_i_ate_core_session.html).

#### Properties

| Name | Description |
| --- | --- |
| Location | Gets the location of the component in the ATECCGEN2. |
| ModelName | Gets the model name of the component. |
| Name | Gets the name of the component. |
| VendorName | Gets the vendor name of the component. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_component_1a4b8865e73ebd597ca5aa487fd61494bf.html language=enus -->
## TOPIC 00054: VendorName

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_component_1a4b8865e73ebd597ca5aa487fd61494bf.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_component_1a4b8865e73ebd597ca5aa487fd61494bf.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the vendor name of the component. SyntaxNamespace: NationalInstruments.AteCorepublic string VendorName { get; }ReturnsReturns the vendor name of the component in string.

### VendorName

Gets the vendor name of the component.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string VendorName { get; }

#### Returns

Returns the vendor name of the component in string.

Parent topic:

IComponent Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_component_1a781247f30b07af31fba1be86015bb348.html language=enus -->
## TOPIC 00055: ModelName

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_component_1a781247f30b07af31fba1be86015bb348.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_component_1a781247f30b07af31fba1be86015bb348.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the model name of the component. SyntaxNamespace: NationalInstruments.AteCorepublic string ModelName { get; }ReturnsReturns the model name of the component in string.

### ModelName

Gets the model name of the component.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string ModelName { get; }

#### Returns

Returns the model name of the component in string.

Parent topic:

IComponent Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_component_1aa1328d18c4f7fb93e5d23fe98ee44bc2.html language=enus -->
## TOPIC 00056: Location

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_component_1aa1328d18c4f7fb93e5d23fe98ee44bc2.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_component_1aa1328d18c4f7fb93e5d23fe98ee44bc2.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the location of the component in the ATECCGEN2. SyntaxNamespace: NationalInstruments.AteCorepublic string Location { get; }ReturnsReturns the location of the component in string.

### Location

Gets the location of the component in the ATECCGEN2.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string Location { get; }

#### Returns

Returns the location of the component in string.

Parent topic:

IComponent Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_component_1af0fa44743db5e0986ac23b63f575913b.html language=enus -->
## TOPIC 00057: Name

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_component_1af0fa44743db5e0986ac23b63f575913b.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_component_1af0fa44743db5e0986ac23b63f575913b.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the component. SyntaxNamespace: NationalInstruments.AteCorepublic string Name { get; }ReturnsReturns the name of the component in string.

### Name

Gets the name of the component.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string Name { get; }

#### Returns

Returns the name of the component in string.

Parent topic:

IComponent Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit.html language=enus -->
## TOPIC 00058: IDCPowerDistributionUnit Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface for the DC Power Distribution Unit. Derives fromIComponentSyntaxNamespace: NationalInstruments.AteCorepublic interface IDCPowerDistributionUnit : IComponentRemarks<threadsafety safety="unsafe"> A DC Power Distribution Unit contains a number of outlets. Each outlet has a curr

### IDCPowerDistributionUnit Interface

Represents the interface for the DC Power Distribution Unit.

#### Derives from

- IComponent

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface IDCPowerDistributionUnit : IComponent

#### Remarks

<threadsafety safety="unsafe">

A DC Power Distribution Unit contains a number of outlets. Each outlet has a current sensor and a voltage sensor measuring the DC current and voltage.

A DC Power Distribution Unit is only functional when the ATECCGEN2 is powered on (power state set to [Running](namespace_national_instruments_1_1_ate_core_1ae5923dd725b7af4a3b59c5d351be4598.html)). When the ATECCGEN2 is powered on, the DC Power Distribution Units connected as discovered, all outlets of the DC Power Distribution Units are turned on by default and sensor monitoring starts to run. Each outlet can then be turned on and off independantly.

If a session is opened before the ATECCGEN2 is powered on, [AteCoreSession](class_national_instruments_1_1_ate_core_1_1_ate_core_session.html) may return an empty DCPowerDistributionUnits. User can use [RefreshDCPowerDistributionUnitsAsync](class_national_instruments_1_1_ate_core_1_1_ate_core_session_1aa7d33057fc4c6d9665648b47c7b3710b.html) to update the list of DC Power Distribution Units detected after the ATECCGEN2 is powered on.

#### Properties

| Name | Description |
| --- | --- |
| OutletCurrentSensors | Gets the array of IOutletSensor objects for current sensors. |
| OutletNumbers | Gets the list of outlet numbers on this DC PDU. |
| OutletVoltageSensors | Gets the array of IOutletSensor objects for voltage sensors. |

#### Methods

| Name | Description |
| --- | --- |
| GetOutletStateAsync(int) | Gets the state of the outlet whether is on or off. |
| TurnOffOutletAsync(int) | Turns off the specified outlet. |
| TurnOnOutletAsync(int) | Turns on the specified outlet. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a068f48af772aa96284109102f32ac110.html language=enus -->
## TOPIC 00059: TurnOffOutletAsync(int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a068f48af772aa96284109102f32ac110.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a068f48af772aa96284109102f32ac110.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Turns off the specified outlet. SyntaxNamespace: NationalInstruments.AteCorepublic Task TurnOffOutletAsync(int outletNumber)ParametersNameTypeDescriptionoutletNumberintSpecifies the outlet number to turn off.

### TurnOffOutletAsync(int)

Turns off the specified outlet.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task TurnOffOutletAsync(int outletNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outletNumber | int | Specifies the outlet number to turn off. |

Parent topic:

IDCPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a1a0694cc5efedfd71c7746f04684d2de.html language=enus -->
## TOPIC 00060: TurnOnOutletAsync(int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a1a0694cc5efedfd71c7746f04684d2de.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a1a0694cc5efedfd71c7746f04684d2de.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Turns on the specified outlet. SyntaxNamespace: NationalInstruments.AteCorepublic Task TurnOnOutletAsync(int outletNumber)ParametersNameTypeDescriptionoutletNumberintSpecifies the outlet number to turn on.

### TurnOnOutletAsync(int)

Turns on the specified outlet.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task TurnOnOutletAsync(int outletNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outletNumber | int | Specifies the outlet number to turn on. |

Parent topic:

IDCPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a2acca1da72256eb5de832572e3700fc3.html language=enus -->
## TOPIC 00061: OutletNumbers

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a2acca1da72256eb5de832572e3700fc3.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a2acca1da72256eb5de832572e3700fc3.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of outlet numbers on this DC PDU. SyntaxNamespace: NationalInstruments.AteCorepublic int[] OutletNumbers { get; }ReturnsReturns the list of outlet numbers on this DC PDU.

### OutletNumbers

Gets the list of outlet numbers on this DC PDU.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public int[] OutletNumbers { get; }

#### Returns

Returns the list of outlet numbers on this DC PDU.

Parent topic:

IDCPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a61d98c58546dfb7db546292f83ad81df.html language=enus -->
## TOPIC 00062: OutletVoltageSensors

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a61d98c58546dfb7db546292f83ad81df.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a61d98c58546dfb7db546292f83ad81df.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of IOutletSensor objects for voltage sensors. SyntaxNamespace: NationalInstruments.AteCorepublic IOutletSensor[] OutletVoltageSensors { get; }ReturnsReturns the array of IOutletSensor objects for voltage sensors.

### OutletVoltageSensors

Gets the array of [IOutletSensor](interface_national_instruments_1_1_ate_core_1_1_i_outlet_sensor.html) objects for voltage sensors.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IOutletSensor](interface_national_instruments_1_1_ate_core_1_1_i_outlet_sensor.html)[] OutletVoltageSensors { get; }

#### Returns

Returns the array of [IOutletSensor](interface_national_instruments_1_1_ate_core_1_1_i_outlet_sensor.html) objects for voltage sensors.

Parent topic:

IDCPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a9f61bd43ca5746faf3bb88ce837482d5.html language=enus -->
## TOPIC 00063: OutletCurrentSensors

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a9f61bd43ca5746faf3bb88ce837482d5.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1a9f61bd43ca5746faf3bb88ce837482d5.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of IOutletSensor objects for current sensors. SyntaxNamespace: NationalInstruments.AteCorepublic IOutletSensor[] OutletCurrentSensors { get; }ReturnsReturns the array of IOutletSensor objects for current sensors.

### OutletCurrentSensors

Gets the array of [IOutletSensor](interface_national_instruments_1_1_ate_core_1_1_i_outlet_sensor.html) objects for current sensors.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IOutletSensor](interface_national_instruments_1_1_ate_core_1_1_i_outlet_sensor.html)[] OutletCurrentSensors { get; }

#### Returns

Returns the array of [IOutletSensor](interface_national_instruments_1_1_ate_core_1_1_i_outlet_sensor.html) objects for current sensors.

Parent topic:

IDCPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1acf0622f724598f15f6038c1ca96c05df.html language=enus -->
## TOPIC 00064: GetOutletStateAsync(int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1acf0622f724598f15f6038c1ca96c05df.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_d_c_power_distribution_unit_1acf0622f724598f15f6038c1ca96c05df.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the state of the outlet whether is on or off. SyntaxNamespace: NationalInstruments.AteCorepublic Task< PowerState > GetOutletStateAsync(int outletNumber)ParametersNameTypeDescriptionoutletNumberintSpecifies the outlet number to read. ReturnsReturns the state of the power phase (PowerState).

### GetOutletStateAsync(int)

Gets the state of the outlet whether is on or off.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< [PowerState](namespace_national_instruments_1_1_ate_core_1a2d8c4506d34bed774d8fa6c57671b5f8.html) > GetOutletStateAsync(int outletNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outletNumber | int | Specifies the outlet number to read. |

#### Returns

Returns the state of the power phase ([PowerState](namespace_national_instruments_1_1_ate_core_1a2d8c4506d34bed774d8fa6c57671b5f8.html)).

Parent topic:

IDCPowerDistributionUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_1a0e927f2389ebdd01e40e81631a7fdaf7.html language=enus -->
## TOPIC 00065: Name

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_1a0e927f2389ebdd01e40e81631a7fdaf7.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_1a0e927f2389ebdd01e40e81631a7fdaf7.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets fan name. SyntaxNamespace: NationalInstruments.AteCorepublic string Name { get; }ReturnsReturns the fan name in string.

### Name

Gets fan name.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string Name { get; }

#### Returns

Returns the fan name in string.

Parent topic:

IFan Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_1a35779089d9330a0267b403a35697e785.html language=enus -->
## TOPIC 00066: ReadRpmAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_1a35779089d9330a0267b403a35697e785.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_1a35779089d9330a0267b403a35697e785.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fan speed in RPM. SyntaxNamespace: NationalInstruments.AteCorepublic Task< int > ReadRpmAsync()ReturnsReturns the fan speed in RPM.

### ReadRpmAsync()

Gets the fan speed in RPM.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< int > ReadRpmAsync()

#### Returns

Returns the fan speed in RPM.

Parent topic:

IFan Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_1a766ee317c4b34e3f480cb5b456c430f7.html language=enus -->
## TOPIC 00067: OwningComponent

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_1a766ee317c4b34e3f480cb5b456c430f7.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_1a766ee317c4b34e3f480cb5b456c430f7.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the component instance that the fan connects to. SyntaxNamespace: NationalInstruments.AteCorepublic IComponent OwningComponent { get; }ReturnsReturns the component instance that the fan connects to (IComponent).

### OwningComponent

Gets the component instance that the fan connects to.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IComponent](interface_national_instruments_1_1_ate_core_1_1_i_component.html) OwningComponent { get; }

#### Returns

Returns the component instance that the fan connects to ([IComponent](interface_national_instruments_1_1_ate_core_1_1_i_component.html)).

Parent topic:

IFan Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a0193a4a782f6c47ca5e90d0fea84355d.html language=enus -->
## TOPIC 00068: Name

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a0193a4a782f6c47ca5e90d0fea84355d.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a0193a4a782f6c47ca5e90d0fea84355d.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets fan domain name. SyntaxNamespace: NationalInstruments.AteCorepublic string Name { get; }ReturnsReturns fan domain name in string.

### Name

Gets fan domain name.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string Name { get; }

#### Returns

Returns fan domain name in string.

Parent topic:

IFanDomain Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a415a6b061d8d7e9a15c8a31a4672d45d.html language=enus -->
## TOPIC 00069: SetFanDomainUserDefinedRpmAsync(int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a415a6b061d8d7e9a15c8a31a4672d45d.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a415a6b061d8d7e9a15c8a31a4672d45d.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the user defined RPM for fan domain. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetFanDomainUserDefinedRpmAsync(int desiredRpm)ParametersNameTypeDescriptiondesiredRpmintSpecifies desired fan rpm.

### SetFanDomainUserDefinedRpmAsync(int)

Sets the user defined RPM for fan domain.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetFanDomainUserDefinedRpmAsync(int desiredRpm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| desiredRpm | int | Specifies desired fan rpm. |

Parent topic:

IFanDomain Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a57c02105e21a3874b62525a35060c4e8.html language=enus -->
## TOPIC 00070: FanDomainType

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a57c02105e21a3874b62525a35060c4e8.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a57c02105e21a3874b62525a35060c4e8.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FanDomainType. SyntaxNamespace: NationalInstruments.AteCorepublic FanDomainType FanDomainType { get; }ReturnsReturns the FanDomainType.

### FanDomainType

Gets the [FanDomainType](namespace_national_instruments_1_1_ate_core_1a86e3eb95ef5eafc15be83f790ebe89eb.html).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [FanDomainType](namespace_national_instruments_1_1_ate_core_1a86e3eb95ef5eafc15be83f790ebe89eb.html) FanDomainType { get; }

#### Returns

Returns the [FanDomainType](namespace_national_instruments_1_1_ate_core_1a86e3eb95ef5eafc15be83f790ebe89eb.html).

Parent topic:

IFanDomain Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a6301649097745b104b564250ce5fac6d.html language=enus -->
## TOPIC 00071: SetFanDomainModeAsync(FanDomainMode)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a6301649097745b104b564250ce5fac6d.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a6301649097745b104b564250ce5fac6d.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the fan domain mode. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetFanDomainModeAsync(FanDomainMode fanDomainMode)ParametersNameTypeDescriptionfanDomainModeFanDomainModeSpecifies fan domain mode.

### SetFanDomainModeAsync(FanDomainMode)

Sets the fan domain mode.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetFanDomainModeAsync(FanDomainMode fanDomainMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| fanDomainMode | FanDomainMode | Specifies fan domain mode. |

Parent topic:

IFanDomain Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a87b0a863af46b23896379a3a0cca9f89.html language=enus -->
## TOPIC 00072: GetFanDomainModeAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a87b0a863af46b23896379a3a0cca9f89.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1a87b0a863af46b23896379a3a0cca9f89.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fan domain mode (FanDomainMode). SyntaxNamespace: NationalInstruments.AteCorepublic Task< FanDomainMode > GetFanDomainModeAsync()ReturnsReturns the fan domain mode (FanDomainMode).

### GetFanDomainModeAsync()

Gets the fan domain mode ([FanDomainMode](namespace_national_instruments_1_1_ate_core_1a328d82723c06620404ff9e9e6362f244.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< [FanDomainMode](namespace_national_instruments_1_1_ate_core_1a328d82723c06620404ff9e9e6362f244.html) > GetFanDomainModeAsync()

#### Returns

Returns the fan domain mode ([FanDomainMode](namespace_national_instruments_1_1_ate_core_1a328d82723c06620404ff9e9e6362f244.html)).

Parent topic:

IFanDomain Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1ac60c68ffaa2d446b13144085382d69e9.html language=enus -->
## TOPIC 00073: FanDomainMinRpm

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1ac60c68ffaa2d446b13144085382d69e9.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1ac60c68ffaa2d446b13144085382d69e9.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum fan domain rpm. SyntaxNamespace: NationalInstruments.AteCorepublic int FanDomainMinRpm { get; }ReturnsReturns the minimum fan domain rpm.

### FanDomainMinRpm

Gets the minimum fan domain rpm.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public int FanDomainMinRpm { get; }

#### Returns

Returns the minimum fan domain rpm.

Parent topic:

IFanDomain Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1ad2b92867ce130f29b123056b2ab23fac.html language=enus -->
## TOPIC 00074: FanDomainMaxRpm

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1ad2b92867ce130f29b123056b2ab23fac.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_fan_domain_1ad2b92867ce130f29b123056b2ab23fac.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum fan domain rpm. SyntaxNamespace: NationalInstruments.AteCorepublic int FanDomainMaxRpm { get; }ReturnsReturns the maximum fan domain rpm.

### FanDomainMaxRpm

Gets the maximum fan domain rpm.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public int FanDomainMaxRpm { get; }

#### Returns

Returns the maximum fan domain rpm.

Parent topic:

IFanDomain Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html language=enus -->
## TOPIC 00075: IPowerBank Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_power_bank.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface for the Power Bank. Derives fromNoneSyntaxNamespace: NationalInstruments.AteCorepublic interface IPowerBankRemarks<threadsafety safety="unsafe"> The AC Power Distribution Unit contains a number of power banks. Every power bank contains a number of outlets and each outlet is

### IPowerBank Interface

Represents the interface for the Power Bank.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface IPowerBank

#### Remarks

<threadsafety safety="unsafe">

The AC Power Distribution Unit contains a number of power banks. Every power bank contains a number of outlets and each outlet is monitored by a current sensor. Each power bank can be turned off and on individually. When a power bank is turned on/off, the outlets in the bank are turned on/off as well. The initial state of the power bank depends on the power setting being set in the firmware configuration file in the ATECCGEN2.

#### Properties

| Name | Description |
| --- | --- |
| OutletCurrentSensors | Get the array of IOutletSensor outlet current sensors. |
| PowerBankNumber | Gets the power bank number. |

#### Methods

| Name | Description |
| --- | --- |
| GetPowerBankStateAsync() | Gets the power state of the power bank whether is on or off. |
| TurnOffPowerBankAsync() | Turns off the specified power bank. |
| TurnOnPowerBankAsync() | Turns on the specified power bank. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel.html language=enus -->
## TOPIC 00076: IPowerEntryPanel Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface for the Power Entry Panel. Derives fromIComponentISerialNumberProviderSyntaxNamespace: NationalInstruments.AteCorepublic interface IPowerEntryPanel : IComponent, ISerialNumberProviderRemarks<threadsafety safety="unsafe"> Power Entry Panel consists of a three-phase AC power s

### IPowerEntryPanel Interface

Represents the interface for the Power Entry Panel.

#### Derives from

- IComponent
- ISerialNumberProvider

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface IPowerEntryPanel : IComponent, ISerialNumberProvider

#### Remarks

<threadsafety safety="unsafe">

Power Entry Panel consists of a three-phase AC power supply or a single-phase AC power supply. For each phase, there are different sensors used to monitor the status of AC power supply for that particular phase. When the ATECCGEN2 is turned on, the three-phase AC power supply defaults to turning on the power supplies for all the phases. The temperature sensors are used to monitor the temperature of the entire Power Entry Panel component. Implements the [IComponent](interface_national_instruments_1_1_ate_core_1_1_i_component.html) and [ISerialNumberProvider](interface_national_instruments_1_1_ate_core_1_1_i_serial_number_provider.html) interfaces.

#### Properties

| Name | Description |
| --- | --- |
| C13OutletCurrentSensor | Gets the C13 Outlet Current sensor (ISensor). |
| PowerPhases | Gets the array of Power Phase Sensors (IPowerPhase). |
| PowerSupplyPhaseType | Gets the PowerSupplyPhaseType on this Power Entry Panel. |
| TemperatureSensors | Gets the array of temperature sensors connected to this Power Entry Panel (ISensor). |
| this[PowerPhaseType powerPhaseType] | Gets the specified Power Phase Sensor (IPowerPhase) by phase type (PowerPhaseType). |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1a60097e0364547e61ffc4f5e2ff42372e.html language=enus -->
## TOPIC 00077: PowerSupplyPhaseType

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1a60097e0364547e61ffc4f5e2ff42372e.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1a60097e0364547e61ffc4f5e2ff42372e.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the PowerSupplyPhaseType on this Power Entry Panel. SyntaxNamespace: NationalInstruments.AteCorepublic PowerSupplyPhaseType PowerSupplyPhaseType { get; }ReturnsReturns the Power Supply Phase Type (PowerSupplyPhaseType).

### PowerSupplyPhaseType

Gets the [PowerSupplyPhaseType](namespace_national_instruments_1_1_ate_core_1a71f97e92eb7b53050c6dace0594d256a.html) on this Power Entry Panel.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [PowerSupplyPhaseType](namespace_national_instruments_1_1_ate_core_1a71f97e92eb7b53050c6dace0594d256a.html) PowerSupplyPhaseType { get; }

#### Returns

Returns the Power Supply Phase Type ([PowerSupplyPhaseType](namespace_national_instruments_1_1_ate_core_1a71f97e92eb7b53050c6dace0594d256a.html)).

Parent topic:

IPowerEntryPanel Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1aad6569a1c8908861379ddfdd60b4cd0e.html language=enus -->
## TOPIC 00078: PowerPhases

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1aad6569a1c8908861379ddfdd60b4cd0e.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1aad6569a1c8908861379ddfdd60b4cd0e.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of Power Phase Sensors (IPowerPhase). SyntaxNamespace: NationalInstruments.AteCorepublic IPowerPhase[] PowerPhases { get; }RemarksFor three-phase AC power supply, the array contains objects for PhaseA, PhaseB and PhaseC with their respective sensors. For single-phase AC power supply,

### PowerPhases

Gets the array of Power Phase Sensors ([IPowerPhase](interface_national_instruments_1_1_ate_core_1_1_i_power_phase.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IPowerPhase](interface_national_instruments_1_1_ate_core_1_1_i_power_phase.html)[] PowerPhases { get; }

#### Remarks

For three-phase AC power supply, the array contains objects for PhaseA, PhaseB and PhaseC with their respective sensors. For single-phase AC power supply, the array only contains PhaseA object. For three-phase AC power supply, to access the properties and methods in [IThreePhase](interface_national_instruments_1_1_ate_core_1_1_i_three_phase.html), the [IPowerPhase](interface_national_instruments_1_1_ate_core_1_1_i_power_phase.html) objects are required to be downcasted to [IThreePhase](interface_national_instruments_1_1_ate_core_1_1_i_three_phase.html) during runtime.

#### Returns

Returns the array of the Power Phase sensors ([IPowerPhase](interface_national_instruments_1_1_ate_core_1_1_i_power_phase.html)).

Parent topic:

IPowerEntryPanel Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1af11593e22556ddd25401b3277d137133.html language=enus -->
## TOPIC 00079: this[PowerPhaseType powerPhaseType]

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1af11593e22556ddd25401b3277d137133.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_power_entry_panel_1af11593e22556ddd25401b3277d137133.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the specified Power Phase Sensor (IPowerPhase) by phase type (PowerPhaseType). SyntaxNamespace: NationalInstruments.AteCorepublic IPowerPhase this[PowerPhaseType powerPhaseType] { get; }ParametersNameTypeDescriptionpowerPhaseTypePowerPhaseTypeEnum of Power phase type (PowerPhaseType). ReturnsRe

### this[PowerPhaseType powerPhaseType]

Gets the specified Power Phase Sensor ([IPowerPhase](interface_national_instruments_1_1_ate_core_1_1_i_power_phase.html)) by phase type ([PowerPhaseType](namespace_national_instruments_1_1_ate_core_1a1e1ec2cf8a0cf6a85d6ee3713d37f280.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IPowerPhase](interface_national_instruments_1_1_ate_core_1_1_i_power_phase.html) this[PowerPhaseType powerPhaseType] { get; }

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| powerPhaseType | PowerPhaseType | Enum of Power phase type (PowerPhaseType). |

#### Returns

Returns the specified Power Phase Sensor by phase type ([IPowerPhase](interface_national_instruments_1_1_ate_core_1_1_i_power_phase.html)).

Parent topic:

IPowerEntryPanel Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_rack_temperature_sensor_unit_1ab98608c36c1c1d8b6d982695107daf10.html language=enus -->
## TOPIC 00080: TemperatureSensor

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_rack_temperature_sensor_unit_1ab98608c36c1c1d8b6d982695107daf10.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_rack_temperature_sensor_unit_1ab98608c36c1c1d8b6d982695107daf10.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the temperature sensor (ISensor). SyntaxNamespace: NationalInstruments.AteCorepublic ISensor TemperatureSensor { get; }ReturnsReturns the temperature sensor (ISensor).

### TemperatureSensor

Gets the temperature sensor ([ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html) TemperatureSensor { get; }

#### Returns

Returns the temperature sensor ([ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)).

Parent topic:

IRackTemperatureSensorUnit Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_sensor.html language=enus -->
## TOPIC 00081: ISensor Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_sensor.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_sensor.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface for the sensor. Derives fromNoneSyntaxNamespace: NationalInstruments.AteCorepublic interface ISensorRemarks<threadsafety safety="unsafe"> PropertiesNameDescriptionNameGets sensor name. OwningComponentGets the component this sensor connects to (IComponent). SensorTypeGets sen

### ISensor Interface

Represents the interface for the sensor.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface ISensor

#### Remarks

<threadsafety safety="unsafe">

#### Properties

| Name | Description |
| --- | --- |
| Name | Gets sensor name. |
| OwningComponent | Gets the component this sensor connects to (IComponent). |
| SensorType | Gets sensor type (SensorType). |

#### Methods

| Name | Description |
| --- | --- |
| ReadSensorAsync() | Reads the sensor reading. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_sensor_1a2ca7876e8500d689f810adeaa7b81167.html language=enus -->
## TOPIC 00082: ReadSensorAsync()

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_sensor_1a2ca7876e8500d689f810adeaa7b81167.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_sensor_1a2ca7876e8500d689f810adeaa7b81167.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the sensor reading. SyntaxNamespace: NationalInstruments.AteCorepublic Task< double > ReadSensorAsync()ReturnsReturns the sensor reading. Physical unit of the sensor reading for each sensor type:Voltage sensor will return sensor reading measured in Volts.Current sensor will return sensor readi

### ReadSensorAsync()

Reads the sensor reading.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task< double > ReadSensorAsync()

#### Returns

- Voltage sensor will return sensor reading measured in Volts.
- Current sensor will return sensor reading measured in Ampere.
- Temperature sensor will return sensor reading measured in degree Celsius.
- Line frequency sensor will return sensor reading measured in Hz.
- Voltage current phase angle sensor reading measured in degree.
- Voltage phase angle sensor reading measured in degree.
- Current phase angle sensor reading measured in degree.

Parent topic:

ISensor Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_sensor_1a3621734d024f42b01624539791832d55.html language=enus -->
## TOPIC 00083: OwningComponent

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_sensor_1a3621734d024f42b01624539791832d55.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_sensor_1a3621734d024f42b01624539791832d55.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the component this sensor connects to (IComponent). SyntaxNamespace: NationalInstruments.AteCorepublic IComponent OwningComponent { get; }ReturnsReturns the component this sensor connects to (IComponent).

### OwningComponent

Gets the component this sensor connects to ([IComponent](interface_national_instruments_1_1_ate_core_1_1_i_component.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [IComponent](interface_national_instruments_1_1_ate_core_1_1_i_component.html) OwningComponent { get; }

#### Returns

Returns the component this sensor connects to ([IComponent](interface_national_instruments_1_1_ate_core_1_1_i_component.html)).

Parent topic:

ISensor Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_serial_number_provider.html language=enus -->
## TOPIC 00084: ISerialNumberProvider Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_serial_number_provider.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_serial_number_provider.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface that provides serial number. Derives fromNoneSyntaxNamespace: NationalInstruments.AteCorepublic interface ISerialNumberProviderRemarks<threadsafety safety="unsafe"> PropertiesNameDescriptionSerialNumberGets the serial number.

### ISerialNumberProvider Interface

Represents the interface that provides serial number.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface ISerialNumberProvider

#### Remarks

<threadsafety safety="unsafe">

#### Properties

| Name | Description |
| --- | --- |
| SerialNumber | Gets the serial number. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_serial_number_provider_1ade12d18ad02ee63c6316327843b3f671.html language=enus -->
## TOPIC 00085: SerialNumber

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_serial_number_provider_1ade12d18ad02ee63c6316327843b3f671.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_serial_number_provider_1ade12d18ad02ee63c6316327843b3f671.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the serial number. SyntaxNamespace: NationalInstruments.AteCorepublic string SerialNumber { get; }ReturnsReturns the serial number in string.

### SerialNumber

Gets the serial number.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public string SerialNumber { get; }

#### Returns

Returns the serial number in string.

Parent topic:

ISerialNumberProvider Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_three_phase_1a00d0894fc33e1bd55fd39907ad67bea4.html language=enus -->
## TOPIC 00086: VoltagePhaseAngleSensors

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_three_phase_1a00d0894fc33e1bd55fd39907ad67bea4.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_three_phase_1a00d0894fc33e1bd55fd39907ad67bea4.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the main and internal (available on certain PEP models) voltage phase angle sensors (ISensor). SyntaxNamespace: NationalInstruments.AteCorepublic ISensor[] VoltagePhaseAngleSensors { get; }ReturnsReturns the main and internal (available on certain PEP models) voltage phase angle sensors (ISenso

### VoltagePhaseAngleSensors

Gets the main and internal (available on certain PEP models) voltage phase angle sensors ([ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)[] VoltagePhaseAngleSensors { get; }

#### Returns

Returns the main and internal (available on certain PEP models) voltage phase angle sensors ([ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)).

Parent topic:

IThreePhase Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_three_phase_1ae8e10dff1e313a78736b8f09549e8ef1.html language=enus -->
## TOPIC 00087: CurrentPhaseAngleSensors

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_three_phase_1ae8e10dff1e313a78736b8f09549e8ef1.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_three_phase_1ae8e10dff1e313a78736b8f09549e8ef1.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the main and internal (available on certain PEP models) current phase angle sensors (ISensor). SyntaxNamespace: NationalInstruments.AteCorepublic ISensor[] CurrentPhaseAngleSensors { get; }ReturnsReturns the main and internal (available on certain PEP models) current phase angle sensors (ISenso

### CurrentPhaseAngleSensors

Gets the main and internal (available on certain PEP models) current phase angle sensors ([ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)[] CurrentPhaseAngleSensors { get; }

#### Returns

Returns the main and internal (available on certain PEP models) current phase angle sensors ([ISensor](interface_national_instruments_1_1_ate_core_1_1_i_sensor.html)).

Parent topic:

IThreePhase Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply.html language=enus -->
## TOPIC 00088: IUninterruptiblePowerSupply Interface

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the interface for the Uninterruptible Power Supply(UPS). Derives fromNoneSyntaxNamespace: NationalInstruments.AteCorepublic interface IUninterruptiblePowerSupplyRemarks<threadsafety safety="unsafe"> UPS is a device that provides emergency power to a load when the input power source, typic

### IUninterruptiblePowerSupply Interface

Represents the interface for the Uninterruptible Power Supply(UPS).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public interface IUninterruptiblePowerSupply

#### Remarks

<threadsafety safety="unsafe">

UPS is a device that provides emergency power to a load when the input power source, typically the facility mains, fails.

There can be more than one UPS in a single rack. But each PEP phase outlet can only be powered by one UPS.

#### Properties

| Name | Description |
| --- | --- |
| MaximumInputVoltage | Gets the rated maximum input voltage of the UPS installed on the rack. |
| MinimumInputVoltage | Gets the rated minimum input voltage of the UPS installed on the rack. |
| PoweredPhase |  |
| PoweredPhaseOutlet |  |

#### Methods

| Name | Description |
| --- | --- |
| SetMaximumInputVoltageAsync(int) | Sets the rated maximum input voltage of the UPS installed on the rack. |
| SetMinimumInputVoltageAsync(int) | Sets the rated minimum input voltage of the UPS installed on the rack. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a38fb321c79f23b34eaa42a39dd0d3d55.html language=enus -->
## TOPIC 00089: MaximumInputVoltage

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a38fb321c79f23b34eaa42a39dd0d3d55.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a38fb321c79f23b34eaa42a39dd0d3d55.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the rated maximum input voltage of the UPS installed on the rack. SyntaxNamespace: NationalInstruments.AteCorepublic int MaximumInputVoltage { get; }RemarksThis value must be set after calling RegisterUninterruptiblePowerSupplyAsync (RegisterUninterruptiblePowerSupplyAsync) to enable monitoring

### MaximumInputVoltage

Gets the rated maximum input voltage of the UPS installed on the rack.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public int MaximumInputVoltage { get; }

#### Remarks

This value must be set after calling RegisterUninterruptiblePowerSupplyAsync ([RegisterUninterruptiblePowerSupplyAsync](class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a149d40acdfa2cc773d15306fb0edf434.html)) to enable monitoring of correct input voltage to UPS. Use SetMaximumInputVoltageAsync ([SetMaximumInputVoltageAsync](interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a5641208ba2430edc4eafb17cd076eafc.html)) to set the value.

#### Returns

Returns the rated maximum input voltage of the UPS.

Parent topic:

IUninterruptiblePowerSupply Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a5641208ba2430edc4eafb17cd076eafc.html language=enus -->
## TOPIC 00090: SetMaximumInputVoltageAsync(int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a5641208ba2430edc4eafb17cd076eafc.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a5641208ba2430edc4eafb17cd076eafc.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the rated maximum input voltage of the UPS installed on the rack. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetMaximumInputVoltageAsync(int maximumInputVoltage)ParametersNameTypeDescriptionmaximumInputVoltageintSpecifies the rated maximum input voltage of the UPS.

### SetMaximumInputVoltageAsync(int)

Sets the rated maximum input voltage of the UPS installed on the rack.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetMaximumInputVoltageAsync(int maximumInputVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumInputVoltage | int | Specifies the rated maximum input voltage of the UPS. |

Parent topic:

IUninterruptiblePowerSupply Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a6f91ab57844245d212575abcc659bd1b.html language=enus -->
## TOPIC 00091: PoweredPhase

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a6f91ab57844245d212575abcc659bd1b.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a6f91ab57844245d212575abcc659bd1b.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.AteCorepublic PowerPhaseType PoweredPhase { get; }RemarksGets the power phase (PowerPhaseType) the UPS will power in the event of facility power loss. For single phase systems, the value should default to PhaseA. ReturnsReturns the power phase type (PowerPhaseTyp

### PoweredPhase

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public [PowerPhaseType](namespace_national_instruments_1_1_ate_core_1a1e1ec2cf8a0cf6a85d6ee3713d37f280.html) PoweredPhase { get; }

#### Remarks

Gets the power phase ([PowerPhaseType](namespace_national_instruments_1_1_ate_core_1a1e1ec2cf8a0cf6a85d6ee3713d37f280.html)) the UPS will power in the event of facility power loss.

For single phase systems, the value should default to PhaseA.

#### Returns

Returns the power phase type ([PowerPhaseType](namespace_national_instruments_1_1_ate_core_1a1e1ec2cf8a0cf6a85d6ee3713d37f280.html)).

Parent topic:

IUninterruptiblePowerSupply Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a86f2f5cddd5cd3ea56b36c6a3e6b92f1.html language=enus -->
## TOPIC 00092: SetMinimumInputVoltageAsync(int)

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a86f2f5cddd5cd3ea56b36c6a3e6b92f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a86f2f5cddd5cd3ea56b36c6a3e6b92f1.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the rated minimum input voltage of the UPS installed on the rack. SyntaxNamespace: NationalInstruments.AteCorepublic Task SetMinimumInputVoltageAsync(int minimumInputVoltage)ParametersNameTypeDescriptionminimumInputVoltageintSpecifies the rated minimum input voltage of the UPS.

### SetMinimumInputVoltageAsync(int)

Sets the rated minimum input voltage of the UPS installed on the rack.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public Task SetMinimumInputVoltageAsync(int minimumInputVoltage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minimumInputVoltage | int | Specifies the rated minimum input voltage of the UPS. |

Parent topic:

IUninterruptiblePowerSupply Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1ad0e330beceaa5f500afadf791895bdd2.html language=enus -->
## TOPIC 00093: MinimumInputVoltage

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1ad0e330beceaa5f500afadf791895bdd2.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1ad0e330beceaa5f500afadf791895bdd2.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the rated minimum input voltage of the UPS installed on the rack. SyntaxNamespace: NationalInstruments.AteCorepublic int MinimumInputVoltage { get; }RemarksThis value must be set after calling RegisterUninterruptiblePowerSupplyAsync (RegisterUninterruptiblePowerSupplyAsync) to enable monitoring

### MinimumInputVoltage

Gets the rated minimum input voltage of the UPS installed on the rack.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public int MinimumInputVoltage { get; }

#### Remarks

This value must be set after calling RegisterUninterruptiblePowerSupplyAsync ([RegisterUninterruptiblePowerSupplyAsync](class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a149d40acdfa2cc773d15306fb0edf434.html)) to enable monitoring of correct input voltage to UPS. Use SetMinimumInputVoltageAsync ([SetMinimumInputVoltageAsync](interface_national_instruments_1_1_ate_core_1_1_i_uninterruptible_power_supply_1a86f2f5cddd5cd3ea56b36c6a3e6b92f1.html)) to set the value.

#### Returns

Returns the rated minimum input voltage of the UPS.

Parent topic:

IUninterruptiblePowerSupply Interface

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=namespace_national_instruments_1_1_ate_core_1_1_status_code.html language=enus -->
## TOPIC 00094: NationalInstruments.AteCore.StatusCode

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `namespace_national_instruments_1_1_ate_core_1_1_status_code.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/namespace_national_instruments_1_1_ate_core_1_1_status_code.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionAteCoreStatusCodeRepresents the list of error codes for ATE Core. InterfacesNoneStructuresNoneEnumerationsNone

### NationalInstruments.AteCore.StatusCode

#### Classes

| Name | Description |
| --- | --- |
| AteCoreStatusCode | Represents the list of error codes for ATE Core. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=namespace_national_instruments_1_1_ate_core_1a1e1ec2cf8a0cf6a85d6ee3713d37f280.html language=enus -->
## TOPIC 00095: PowerPhaseType Enumeration

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `namespace_national_instruments_1_1_ate_core_1a1e1ec2cf8a0cf6a85d6ee3713d37f280.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/namespace_national_instruments_1_1_ate_core_1a1e1ec2cf8a0cf6a85d6ee3713d37f280.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the types of power phase. SyntaxNamespace: NationalInstruments.AteCorepublic enum PowerPhaseTypeMembersNameValueDescriptionPhaseAPower Phase A. PhaseBPower Phase B. PhaseCPower Phase C.

### PowerPhaseType Enumeration

Specifies the types of power phase.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public enum PowerPhaseType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PhaseA |  | Power Phase A. |
| PhaseB |  | Power Phase B. |
| PhaseC |  | Power Phase C. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=namespace_national_instruments_1_1_ate_core_1a328d82723c06620404ff9e9e6362f244.html language=enus -->
## TOPIC 00096: FanDomainMode Enumeration

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `namespace_national_instruments_1_1_ate_core_1a328d82723c06620404ff9e9e6362f244.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/namespace_national_instruments_1_1_ate_core_1a328d82723c06620404ff9e9e6362f244.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the types of fan domain modes. SyntaxNamespace: NationalInstruments.AteCorepublic enum FanDomainModeMembersNameValueDescriptionInvalid0Invalid fan domain mode. High2The fan speed of the fans (in a fan panels) in a domain are set to FanDomainMaxRpm. Manual11Allow customer to manually set th

### FanDomainMode Enumeration

Specifies the types of fan domain modes.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public enum FanDomainMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Invalid | 0 | Invalid fan domain mode. |
| High | 2 | The fan speed of the fans (in a fan panels) in a domain are set to FanDomainMaxRpm. |
| Manual | 11 | Allow customer to manually set the desired fan RPM for a domain. The desired RPM cannot be set higher or lower than the FanDomainMaxRpm and FanDomainMinRpm respectively. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=namespace_national_instruments_1_1_ate_core_1a71f97e92eb7b53050c6dace0594d256a.html language=enus -->
## TOPIC 00097: PowerSupplyPhaseType Enumeration

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `namespace_national_instruments_1_1_ate_core_1a71f97e92eb7b53050c6dace0594d256a.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/namespace_national_instruments_1_1_ate_core_1a71f97e92eb7b53050c6dace0594d256a.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the types of power supply based on phase. SyntaxNamespace: NationalInstruments.AteCorepublic enum PowerSupplyPhaseTypeMembersNameValueDescriptionSinglePhaseSingle-phase power supply. ThreePhaseThree-phase power supply.

### PowerSupplyPhaseType Enumeration

Specifies the types of power supply based on phase.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public enum PowerSupplyPhaseType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SinglePhase |  | Single-phase power supply. |
| ThreePhase |  | Three-phase power supply. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=namespace_national_instruments_1_1_ate_core_1a84f7de6112d53c7120a3f013a82132cb.html language=enus -->
## TOPIC 00098: RackRestartLevel Enumeration

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `namespace_national_instruments_1_1_ate_core_1a84f7de6112d53c7120a3f013a82132cb.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/namespace_national_instruments_1_1_ate_core_1a84f7de6112d53c7120a3f013a82132cb.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the types of rack restart levels. SyntaxNamespace: NationalInstruments.AteCorepublic enum RackRestartLevelMembersNameValueDescriptionServiceLevelRestartInstructs the operating system to terminate and restart RCU Service. FullRestartInstructs the operating system to terminate all processes

### RackRestartLevel Enumeration

Specifies the types of rack restart levels.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public enum RackRestartLevel

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ServiceLevelRestart |  | Instructs the operating system to terminate and restart RCU Service. |
| FullRestart |  | Instructs the operating system to terminate all processes and initiate a system reboot. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=namespace_national_instruments_1_1_ate_core_1ad3e7c808bcd6d68be8e40deba6b02fca.html language=enus -->
## TOPIC 00099: FirmwareUpdateStatus Enumeration

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `namespace_national_instruments_1_1_ate_core_1ad3e7c808bcd6d68be8e40deba6b02fca.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/namespace_national_instruments_1_1_ate_core_1ad3e7c808bcd6d68be8e40deba6b02fca.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the values for firmware update status. SyntaxNamespace: NationalInstruments.AteCorepublic enum FirmwareUpdateStatusMembersNameValueDescriptionUnknown0Unknown status. Succeeded1Firmware update succeeded. Failed2Firmware update failed. Staged3Firmware is staged, rack is required to reboot fo

### FirmwareUpdateStatus Enumeration

Specifies the values for firmware update status.

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public enum FirmwareUpdateStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Unknown | 0 | Unknown status. |
| Succeeded | 1 | Firmware update succeeded. |
| Failed | 2 | Firmware update failed. |
| Staged | 3 | Firmware is staged, rack is required to reboot for new firmware to take effect. |
| Installing | 4 | Firmware is being installed. |

Parent topic:

NationalInstruments.AteCore

<!--NI_TOPIC bundle=ni-atecore-dotnet-api-ref path=namespace_national_instruments_1_1_ate_core_1af8820d3d3d0a2d8ddc980403e53e7ad0.html language=enus -->
## TOPIC 00100: Interlock Enumeration

- bundle_id: `ni-atecore-dotnet-api-ref`
- source_path: `namespace_national_instruments_1_1_ate_core_1af8820d3d3d0a2d8ddc980403e53e7ad0.html`
- source_url: https://docs-be.ni.com/bundle/ni-atecore-dotnet-api-ref/raw/resource/enus/namespace_national_instruments_1_1_ate_core_1af8820d3d3d0a2d8ddc980403e53e7ad0.html
- document_id: `ni-atecore-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the values for interlock. The interlocks that are connected to the rack and the connection can be monitored by the rack using IsInterlockConnectedAsync. SyntaxNamespace: NationalInstruments.AteCorepublic enum InterlockMembersNameValueDescriptionInterlock11First interlock. Interlock22Second

### Interlock Enumeration

Specifies the values for interlock. The interlocks that are connected to the rack and the connection can be monitored by the rack using [IsInterlockConnectedAsync](class_national_instruments_1_1_ate_core_1_1_ate_core_session_1a081c7355228554130bd2c285bf93be33.html).

#### Syntax

**Namespace:**[NationalInstruments.AteCore](namespace_national_instruments_1_1_ate_core.html)

public enum Interlock

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Interlock1 | 1 | First interlock. |
| Interlock2 | 2 | Second interlock. |
| Interlock3 | 3 | Third interlock. |
| Interlock4 | 4 | Fourth interlock. |

Parent topic:

NationalInstruments.AteCore
