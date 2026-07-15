# NI DOCUMENT BUNDLE: diadem

<!--NI_BUNDLE_CHUNK bundle=diadem start=1251 end=1500 -->
<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_propertyname_ireferencechannelproperty.htm language=enus -->
## TOPIC 01251: Property: PropertyName for ReferenceChannelProperty

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_propertyname_ireferencechannelproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_propertyname_ireferencechannelproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: PropertyName for ReferenceChannelProperty

Property: PropertyName for ReferenceChannelProperty

Specifies the name of the channel property with which DIAdem replaces an input or an output when a calculation is executed.

You can add the contents of a DIAdem variable or a calculator expression to the channel group property if you enclose the variable or the calculator expression in @@ characters.

If the input of the calculation is dependent on an output from another calculation, you cannot change the PropertyName property.

```text
Object.PropertyName
```

| Object | ReferenceChannelPropertyObject with this property |
| --- | --- |
| Object.PropertyName | String with read and write access |

The following example generates the R input, which is a Value data type, in the first calculation of the first calculation group. The example then defines a channel property reference for this input and specifies the channel group, the property, and the associated unit.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.ReferenceType = eReferenceTypeChannelProperty
oMyInput.Reference.Channel = "Revs"
oMyInput.Reference.PropertyName = "Maximum"
oMyInput.Reference.UnitPropertyName = "unit_string"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.ReferenceType = dd.eReferenceTypeChannelProperty 
oMyInput.Reference.Channel = "Revs" 
oMyInput.Reference.PropertyName = "Maximum" 
oMyInput.Reference.UnitPropertyName = "unit_string" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_propertyname_ireferencedatasetproperty.htm language=enus -->
## TOPIC 01252: Property: PropertyName for ReferenceDatasetProperty

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_propertyname_ireferencedatasetproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_propertyname_ireferencedatasetproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: PropertyName for ReferenceDatasetProperty

Property: PropertyName for ReferenceDatasetProperty

Specifies the name of the data set property with which DIAdem replaces an input or an output when a calculation is executed.

You can add the contents of a DIAdem variable or a calculator expression to the channel group property if you enclose the variable or the calculator expression in @@ characters.

If the input of the calculation is dependent on an output from another calculation, you cannot change the PropertyName property.

```text
Object.PropertyName
```

| Object | ReferenceDatasetPropertyObject with this property |
| --- | --- |
| Object.PropertyName | String with read and write access |

The following example generates the R input, which is a Value data type, in the first calculation of the first calculation group. The example then defines a data set property reference for this input and specifies the property and the associated unit.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.ReferenceType = eReferenceTypeDatasetProperty
oMyInput.Reference.PropertyName = "Duration"
oMyInput.Reference.UnitSymbol = "ms"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.ReferenceType = dd.eReferenceTypeDatasetProperty 
oMyInput.Reference.PropertyName = "Duration" 
oMyInput.Reference.UnitSymbol = "ms" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_reference_iinput.htm language=enus -->
## TOPIC 01253: Property: Reference for Input

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_reference_iinput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_reference_iinput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Reference for Input

Property: Reference for Input

Specifies the reference object, which is dependent on the reference type, for the input of a calculation.

```text
Set oReference = Object.Reference
```

| Object | InputObject with this property |
| --- | --- |
| oReference | ReferenceReturned object |

The following example changes the name of the channel with which DIAdem replaces the R input when DIAdem executes the first calculation from the first calculation group, if the input is defined with the Channel data type.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs("R")
If oMyInput.ReferenceType = eReferenceTypeChannel Then
  oMyInput.Reference.Channel = "Revs"
End If
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs("R") 
if oMyInput.ReferenceType == dd.eReferenceTypeChannel : 
    oMyInput.Reference.Channel = "Revs" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_reference_ioutput.htm language=enus -->
## TOPIC 01254: Property: Reference for Output

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_reference_ioutput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_reference_ioutput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Reference for Output

Property: Reference for Output

Specifies the reference object, which is dependent on the reference type, for the output of a calculation.

```text
Set oReference = Object.Reference
```

| Object | OutputObject with this property |
| --- | --- |
| oReference | ReferenceReturned object |

The following example changes the name of the channel with which DIAdem replaces the R output when DIAdem executes the first calculation from the first calculation group, if the output is defined with the Channel data type.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyOutput
Set oMyOutput = CalculationSet.CalculationGroups(1).Calculations(1).Outputs("R")
If oMyOutput.ReferenceType = eReferenceTypeChannel Then
  oMyOutput.Reference.Channel = "Revs"
End If
```

[Copy script](javascript:void(0);)

```text
oMyOutput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs("R") 
if oMyOutput.ReferenceType == dd.eReferenceTypeChannel : 
    oMyOutput.Reference.Channel = "Revs" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_referencetype_iformulaadaptor.htm language=enus -->
## TOPIC 01255: Property: ReferenceType for InputOrOutput

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_referencetype_iformulaadaptor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_referencetype_iformulaadaptor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: ReferenceType for InputOrOutput

Property: ReferenceType for InputOrOutput

Specifies the reference type, which is dependent on the data type, of the input or output of a calculation.

```text
Object.ReferenceType
```

| Object | InputOrOutputObject with this property |  |
| --- | --- | --- |
| Object.ReferenceType | The selection terms depend on the data type (AdaptorType).Enumeration with read and write access and the following selection terms: 110eReferenceTypeValueThe input refers to any value (Value data type). 111eReferenceTypeDatasetPropertyThe input refers to a data set property (Value data type). 112eReferenceTypeChannelGroupPropertyThe input refers to a channel group property (Value data type). 113eReferenceTypeChannelPropertyThe input refers to a channel property (Value data type). 114eReferenceTypeChannelThe input refers to a channel (Channel data type). 115eReferenceTypeChannelListThe input refers to a channel list (Channel list data type). |  |
| 110 | eReferenceTypeValue | The input refers to any value (Value data type). |
| 111 | eReferenceTypeDatasetProperty | The input refers to a data set property (Value data type). |
| 112 | eReferenceTypeChannelGroupProperty | The input refers to a channel group property (Value data type). |
| 113 | eReferenceTypeChannelProperty | The input refers to a channel property (Value data type). |
| 114 | eReferenceTypeChannel | The input refers to a channel (Channel data type). |
| 115 | eReferenceTypeChannelList | The input refers to a channel list (Channel list data type). |

The pages of the objects [Input](../objects/formulacalc_objects_iinput.htm) and [Output](../objects/formulacalc_objects_ioutput.htm) contain examples.

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_referencetype_iinput.htm language=enus -->
## TOPIC 01256: Property: ReferenceType for Input

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_referencetype_iinput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_referencetype_iinput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: ReferenceType for Input

Property: ReferenceType for Input

Specifies the reference type, which is dependent on the data type, of the input of a calculation.

If the input of the calculation is dependent on an output from another calculation, you cannot change the ReferenceType property.

```text
Object.ReferenceType
```

| Object | InputObject with this property |  |
| --- | --- | --- |
| Object.ReferenceType | The selection terms depend on the data type (AdaptorType).Enumeration with read and write access and the following selection terms: 110eReferenceTypeValueThe input refers to any value (Value data type). 111eReferenceTypeDatasetPropertyThe input refers to a data set property (Value data type). 112eReferenceTypeChannelGroupPropertyThe input refers to a channel group property (Value data type). 113eReferenceTypeChannelPropertyThe input refers to a channel property (Value data type). 114eReferenceTypeChannelThe input refers to a channel (Channel data type). 115eReferenceTypeChannelListThe input refers to a channel list (Channel list data type). |  |
| 110 | eReferenceTypeValue | The input refers to any value (Value data type). |
| 111 | eReferenceTypeDatasetProperty | The input refers to a data set property (Value data type). |
| 112 | eReferenceTypeChannelGroupProperty | The input refers to a channel group property (Value data type). |
| 113 | eReferenceTypeChannelProperty | The input refers to a channel property (Value data type). |
| 114 | eReferenceTypeChannel | The input refers to a channel (Channel data type). |
| 115 | eReferenceTypeChannelList | The input refers to a channel list (Channel list data type). |

The following example defines the input R which is a Value data type for the first calculation in the first calculation group. Then the example defines with which value DIAdem replaces the input when the calculation is executed:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.ReferenceType = eReferenceTypeValue
oMyInput.Reference.ValueExpression = "R1"
oMyInput.Reference.UnitSymbol = "mm"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.ReferenceType = dd.eReferenceTypeValue 
oMyInput.Reference.ValueExpression = "R1" 
oMyInput.Reference.UnitSymbol = "mm" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_referencetype_ioutput.htm language=enus -->
## TOPIC 01257: Property: ReferenceType for Output

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_referencetype_ioutput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_referencetype_ioutput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: ReferenceType for Output

Property: ReferenceType for Output

Specifies the reference type, which is dependent on the data type, of the output of a calculation.

```text
Object.ReferenceType
```

| Object | OutputObject with this property |  |
| --- | --- | --- |
| Object.ReferenceType | The selection terms depend on the data type (AdaptorType).Enumeration with read and write access and the following selection terms: 110eReferenceTypeValueThe input refers to any value (Value data type). 111eReferenceTypeDatasetPropertyThe input refers to a data set property (Value data type). 112eReferenceTypeChannelGroupPropertyThe input refers to a channel group property (Value data type). 113eReferenceTypeChannelPropertyThe input refers to a channel property (Value data type). 114eReferenceTypeChannelThe input refers to a channel (Channel data type). 115eReferenceTypeChannelListThe input refers to a channel list (Channel list data type). |  |
| 110 | eReferenceTypeValue | The input refers to any value (Value data type). |
| 111 | eReferenceTypeDatasetProperty | The input refers to a data set property (Value data type). |
| 112 | eReferenceTypeChannelGroupProperty | The input refers to a channel group property (Value data type). |
| 113 | eReferenceTypeChannelProperty | The input refers to a channel property (Value data type). |
| 114 | eReferenceTypeChannel | The input refers to a channel (Channel data type). |
| 115 | eReferenceTypeChannelList | The input refers to a channel list (Channel list data type). |

The following example defines the output R which is a Channel data type for the first calculation in the first calculation group. The example then defines which channel DIAdem replaces the output with when the calculation is executed.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyOutput
Set oMyOutput = CalculationSet.CalculationGroups(1).Calculations(1).Outputs.Add("R",eAdaptorTypeChannel)
oMyOutput.ReferenceType = eReferenceTypeChannel
oMyOutput.Reference.Channel = "Revs"
```

[Copy script](javascript:void(0);)

```text
oMyOutput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs.Add("R",dd.eAdaptorTypeChannel) 
oMyOutput.ReferenceType = dd.eReferenceTypeChannel 
oMyOutput.Reference.Channel = "Revs" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_runcount_icalculation.htm language=enus -->
## TOPIC 01258: Property: RunCount for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_runcount_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_runcount_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: RunCount for Calculation

Property: RunCount for Calculation

Specifies the number of cycles for a calculation. Instead of a number, you also can assign a variable name, such as Data.Root.ChannelGroups.Count, to this property.

If you execute more than one cycle for a calculation, use expressions with @@[CCR](../../varoff/ccr.htm)@@ in the references of the inputs and/or outputs. This gives you variable inputs or variable outputs. If you define a calculation with two cycles and the reference "[1]/Cycle_@@CCR@@" for an input channel, for example, DIAdem adds the current increment number to the channel name during each calculation cycle. DIAdem executes the respective cycle when the corresponding channel is in the Data Portal. Otherwise, DIAdem skips this cycle. If the Data Portal does not contain a corresponding channel in any cycle, DIAdem displays an error message.

```text
Object.RunCount
```

| Object | CalculationObject with this property |
| --- | --- |
| Object.RunCount | String with read and write access |

The following example defines two cycles for the first calculation in the first calculation group and executes the cycles:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Set oMyCalc = CalculationSet.CalculationGroups(1).Calculations(1)
oMyCalc.RunCount = 2
oMyCalc.Inputs(1).Reference.Channel = "[1]/Cycle_@@CCR@@"
Call oMyCalc.Run()
```

[Copy script](javascript:void(0);)

```text
oMyCalc = dd.CalculationSet.CalculationGroups(1).Calculations(1) 
oMyCalc.RunCount = 2 
oMyCalc.Inputs(1).Reference.Channel = "[1]/Cycle_@@CCR@@" 
oMyCalc.Run() 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_unitsymbol_ireferencedatasetproperty.htm language=enus -->
## TOPIC 01259: Property: UnitSymbol for ReferenceDatasetProperty

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_unitsymbol_ireferencedatasetproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_unitsymbol_ireferencedatasetproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: UnitSymbol for ReferenceDatasetProperty

Property: UnitSymbol for ReferenceDatasetProperty

Specifies the unit symbol of the data set property with which DIAdem replaces an output or an input when DIAdem executes a calculation, when the [UnitPropertyName](../properties/formulacalc_property_unitpropertyname_ireferencedatasetproperty.htm) property contains an empty string.

At an input DIAdem assigns the default unit symbol to the numeric value and assigns it to a unit. At an output DIAdem converts the value into the default unit and uses the resulting numeric value. If you assign an empty string to the UnitSymbol property, the unit of the input is undefined. At an output DIAdem uses the numeric value unchanged.

You can add the contents of a DIAdem variable or a calculator expression to the unit symbol if you enclose the variable or the calculator expression in @@ characters.

If the input of the calculation is dependent on an output from another calculation, you cannot change the UnitSymbol property.

```text
Object.UnitSymbol
```

| Object | ReferenceDatasetPropertyObject with this property |
| --- | --- |
| Object.UnitSymbol | String with read and write access |

The following example generates the R input, which is a Value data type, in the first calculation of the first calculation group. The example then defines a data set property reference for this input and specifies the data set property and the associated unit.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.ReferenceType = eReferenceTypeDatasetProperty
oMyInput.Reference.PropertyName = "Duration"
oMyInput.Reference.UnitSymbol = "ms"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.ReferenceType = dd.eReferenceTypeDatasetProperty 
oMyInput.Reference.PropertyName = "Duration" 
oMyInput.Reference.UnitSymbol = "ms" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_validationscript_icalculation.htm language=enus -->
## TOPIC 01260: Property: ValidationScript for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_validationscript_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_validationscript_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: ValidationScript for Calculation

Property: ValidationScript for Calculation

Specifies the validation script of a calculation.

If the calculation is encrypted ([IsCrypted](../methods/formulacalc_method_iscrypted_icalculation.htm)  = TRUE), you can neither change nor read out the ValidationScript property. You can use the names of the non-dependent inputs in the calculation to access these inputs in the validation script.

In validation scripts the following variables are also available:

| This | Calculation object of the calculation |
| --- | --- |
| Failed | Return value that contains a message if the test failed. |

|  | Note The validation script is the same as the contents of a VBS procedure. You cannot define functions or procedures in a validation script. Do not use Exit Sub or an error output to finish the script so that DIAdem can process the test correctly. |
| --- | --- |

```text
Object.ValidationScript
```

| Object | CalculationObject with this property |
| --- | --- |
| Object.ValidationScript | String with read and write access |

The following example defines the validation script for the first calculation of the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalc
Set oMyCalc = CalculationSet.CalculationGroups(1).Calculations(1) 
oMyCalc.ValidationScript = "If N.Size>0 Then" & vbCrLf & " Failed = ""Channel not empty""" & vbCrLf & "End If"
```

[Copy script](javascript:void(0);)

```text
oMyCalc = dd.CalculationSet.CalculationGroups(1).Calculations(1) 
oMyCalc.ValidationScript = "If N.Size>0 Then" + "\r\n" + " Failed = ""Channel not None""" + "\r\n" + "End If" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_valueexpression_ireferencevalue.htm language=enus -->
## TOPIC 01261: Property: ValueExpression for ReferenceValue

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_valueexpression_ireferencevalue.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_valueexpression_ireferencevalue.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: ValueExpression for ReferenceValue

Property: ValueExpression for ReferenceValue

Specifies the expression with which DIAdem replaces an input or an output when a calculation is executed. You can use a numeric value or a variable name as the expression.

If the input of the calculation is dependent on an output from another calculation, you cannot change the ValueExpression property.

```text
Object.ValueExpression
```

| Object | ReferenceValueObject with this property |
| --- | --- |
| Object.ValueExpression | String with read and write access |

The following example generates the R input, which is a Value data type, in the first calculation of the first calculation group. The example then defines a value reference for this input and specifies the value and the associated unit.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.ReferenceType = eReferenceTypeValue
oMyInput.Reference.ValueExpression = "1.23"
oMyInput.Reference.UnitSymbol = "mm"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.ReferenceType = dd.eReferenceTypeValue 
oMyInput.Reference.ValueExpression = "1.23" 
oMyInput.Reference.UnitSymbol = "mm" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/canconverterapi_overview.htm language=enus -->
## TOPIC 01262: Bus Log Converter

- bundle_id: `diadem`
- source_path: `icanconverter/canconverterapi_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/canconverterapi_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Bus Log Converter

Bus Log Converter

The subordinate topics contained in the tree on the contents tab of the Help describe the object-oriented script interface for the [Bus Log Converter](../dlgcanconverter/dlgcanconverter/canconverter_overview.htm). The topics provide information about all objects, collections, methods, and properties, and examples that demonstrate how to use the interface.

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_add_ibuscollection.htm language=enus -->
## TOPIC 01263: Method: Add for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_add_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_add_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Add for Buses

Method: Add for Buses

Use the [AddByType](../methods/canconverter_method_addbytype_ibuscollection.htm) instead of the Add method in order to add a bus to the Buses collection and to specify the bus type. 
Adds a bus to the Buses collection in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Set oBus = Object.Add(Name, BusNumber)
```

| Object | BusesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the bus. |
| BusNumber | LongIntegerSpecifies the number of the bus.Value range: 0 <= BusNumber<= 255 |
| oBus | BusReturned object |

The following example adds the CAN bus named NewCANBus and the bus number 1 to the collection of busses and then outputs the name of the added buses:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyBus
Set oMyBus = BusLogToTDM.BusDbConfig.Buses.Add("NewCANBus",1)
Call MsgBoxDisp (oMyBus.Name)
```

[Copy script](javascript:void(0);)

```text
oMyBus = dd.BusLogToTDM.BusDbConfig.Buses.Add("NewCANBus",1) 
dd.MsgBoxDisp (oMyBus.Name) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_add_ibusfilterbuscollection.htm language=enus -->
## TOPIC 01264: Method: Add for UsedBuses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_add_ibusfilterbuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_add_ibusfilterbuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Add for UsedBuses

Method: Add for UsedBuses

Adds a bus to the [UsedBuses collection](../objects/canconverter_objects_ibusfilterbuscollection.htm) in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Set oBus = Object.Add(Name)
```

| Object | UsedBusesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the bus. The bus must exist in the Buses collection. |
| oBus | BusReturned object |

The following example adds a bus to the filtered bus collection:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.ResultSettings.BusFilter.UsedBuses.Add("Bus2")
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.ResultSettings.BusFilter.UsedBuses.Add("Bus2") 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_add_idbfilecollection.htm language=enus -->
## TOPIC 01265: Method: Add for DbFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_add_idbfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_add_idbfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Add for DbFiles

Method: Add for DbFiles

Adds a database file to the [DbFiles collection](../objects/canconverter_objects_idbfilecollection.htm) in the [Bus Logfile Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Set oDbFile = Object.Add(Name)
```

| Object | DbFilesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the database file, including the complete path and the filename extension. If DIAdem does not find the specified folder of the database file, DIAdem also searches for the file in the folder of the TCC file. |
| oDbFile | DbFileReturned object |

The following example adds the database file C:\Accelerator.dbc to the CAN1 bus:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.BusDBConfig.Buses("CAN1").DbFiles.Add("C:\Accelerator.dbc")
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.BusDBConfig.Buses("CAN1").DbFiles.Add("C:\\Accelerator.dbc") 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_add_ilogfilecollection.htm language=enus -->
## TOPIC 01266: Method: Add for LogFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_add_ilogfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_add_ilogfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Add for LogFiles

Method: Add for LogFiles

Adds a database file to the [LogFiles collection](../objects/canconverter_objects_ilogfilecollection.htm) in the [Bus Logfile Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Set oLogFile = Object.Add(Name)
```

| Object | LogFilesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the logfile, including the path and the filename extension. |
| oLogFile | LogFileReturned object |

The following example adds the logfile C:\MyLogFile.log to the collection of logfiles:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.LogSettings.LogFiles.Add("C:\MyLogFile.log")
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.LogSettings.LogFiles.Add("C:\\MyLogFile.log") 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_add_itostringitemvecint.htm language=enus -->
## TOPIC 01267: Method: Add for StringVector

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_add_itostringitemvecint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_add_itostringitemvecint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Add for StringVector

Method: Add for StringVector

Adds a text to the [StringVector collection](../objects/canconverter_objects_itostringitemvecint.htm) in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.Add(Value)
```

| Object | StringVectorObject with this method |
| --- | --- |
| Value | StringSpecifies the name of a cluster or of an XNET channel |

The following example adds the cluster HighBusLoad to the string vector:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Set oDbFile = BusLogToTDM.BusDbConfig.Buses("CANBus").DbFiles.Add("D:\Logfiles\XNET_TDMS\TDMS_Test.xml")
oDbFile.IdMode = eDbFileIdModeDefault
Call oDbFile.Clusters.Add("HighBusLoad")
```

[Copy script](javascript:void(0);)

```text
oDbFile = dd.BusLogToTDM.BusDbConfig.Buses("CANBus").DbFiles.Add("D:\\Logfiles\\XNET_TDMS\\TDMS_Test.xml") 
oDbFile.IdMode = dd.eDbFileIdModeDefault 
oDbFile.Clusters.Add("HighBusLoad") 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_addbytype_ibuscollection.htm language=enus -->
## TOPIC 01268: Method: AddByType for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_addbytype_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_addbytype_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: AddByType for Buses

Method: AddByType for Buses

Adds a bus of a specific type to the Buses collection in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Set oBus = Object.AddByType(Name, BusNumber, BusType)
```

| Object | BusesObject with this method |  |
| --- | --- | --- |
| Name | StringSpecifies the name of the bus. |  |
| BusNumber | LongIntegerSpecifies the number of the bus.Value range: 0 <= BusNumber<= 255 |  |
| BusType | Specifies the bus type.Enumeration with the following selection terms: 0eBusTypeUndefined Not defined 1eBusTypeCAN CAN 2eBusTypeLIN LIN 3eBusTypeFLEXRAY Flexray |  |
| 0 | eBusTypeUndefined | Not defined |
| 1 | eBusTypeCAN | CAN |
| 2 | eBusTypeLIN | LIN |
| 3 | eBusTypeFLEXRAY | Flexray |
| oBus | BusReturned object |  |

The following example adds the CAN bus called NewCANBus with the bus number 1 and the type CAN to the bus collection and then outputs the name of the added bus:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyBus
Set oMyBus = BusLogToTDM.BusDbConfig.Buses.AddByType("NewCANBus",1,eBusTypeCAN)
Call MsgBoxDisp (oMyBus.Name)
```

[Copy script](javascript:void(0);)

```text
oMyBus = dd.BusLogToTDM.BusDbConfig.Buses.AddByType("NewCANBus",1,dd.eBusTypeCAN) 
dd.MsgBoxDisp (oMyBus.Name) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_clear_icanconverter.htm language=enus -->
## TOPIC 01269: Method: Clear for BusLogToTDM

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_clear_icanconverter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_clear_icanconverter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Clear for BusLogToTDM

Method: Clear for BusLogToTDM

Deletes all settings of the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.Clear
```

| Object | BusLogToTDMObject with this method |
| --- | --- |

The following example deletes all the settings of the Bus Log Converter:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.Clear()
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.Clear() 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_convert_icanconverter.htm language=enus -->
## TOPIC 01270: Method: Convert for BusLogToTDM

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_convert_icanconverter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_convert_icanconverter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Convert for BusLogToTDM

Method: Convert for BusLogToTDM

[Converts](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm) logfiles into the TDM format.

```text
Object.Convert
```

| Object | BusLogToTDMObject with this method |
| --- | --- |

The following example executes a conversion with the previously added settings:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.Convert()
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.Convert() 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_exists_ibuscollection.htm language=enus -->
## TOPIC 01271: Method: Exists for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_exists_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_exists_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Exists for Buses

Method: Exists for Buses

Checks whether a bus with a specific name already exists in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
bExists = Object.Exists(Name)
```

| Object | BusesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the bus. |
| bExists | BooleanSpecifies whether the bus already exists (TRUE) or not (FALSE). |

The following example displays whether a bus called CAN1 already exists:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp (BusLogToTDM.BusDbConfig.Buses.Exists("CAN1"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp (dd.BusLogToTDM.BusDbConfig.Buses.Exists("CAN1")) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_exists_ibusfilterbuscollection.htm language=enus -->
## TOPIC 01272: Method: Exists for UsedBuses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_exists_ibusfilterbuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_exists_ibusfilterbuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Exists for UsedBuses

Method: Exists for UsedBuses

Checks in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm) whether a bus with a specific name already exists in the filtered bus collection.

```text
bExists = Object.Exists(Name)
```

| Object | UsedBusesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the bus. |
| bExists | BooleanSpecifies whether the bus already exists (TRUE) or not (FALSE) in the filtered collection. |

The following example displays whether the CAN3 bus already exists in the filtered bus collection:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.ResultSettings.BusFilter.UsedBuses.Exists("CAN3"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.ResultSettings.BusFilter.UsedBuses.Exists("CAN3")) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_exists_idbfilecollection.htm language=enus -->
## TOPIC 01273: Method: Exists for DbFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_exists_idbfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_exists_idbfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Exists for DbFiles

Method: Exists for DbFiles

Checks in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm) whether a database file with a specific name already exists for a bus.

```text
bExists = Object.Exists(Name)
```

| Object | DbFilesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the database file, including the path and the filename extension. |
| bExists | BooleanSpecifies whether the database file already exists (TRUE) or not (FALSE). |

The following example displays whether the database file called C:\CAN1.ncd already exists for the CAN1 bus:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.BusDbConfig.Buses("CAN1").DbFiles.Exists("C:\CAN1.ncd"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.BusDbConfig.Buses("CAN1").DbFiles.Exists("C:\\CAN1.ncd")) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_exists_ilogfilecollection.htm language=enus -->
## TOPIC 01274: Method: Exists for LogFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_exists_ilogfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_exists_ilogfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Exists for LogFiles

Method: Exists for LogFiles

Checks in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm) whether a logfile file with a specific name already exists.

```text
bExists = Object.Exists(Name)
```

| Object | LogFilesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the logfile, including the path and the filename extension. |
| bExists | BooleanSpecifies whether the logfile already exists (TRUE) or not (FALSE). |

The following example displays whether a logfile called C:\MyLogFile.log already exists:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.LogSettings.LogFiles.Exists("C:\MyLogFile.log"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.LogSettings.LogFiles.Exists("C:\\MyLogFile.log")) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_existsbusno_ibuscollection.htm language=enus -->
## TOPIC 01275: Method: ExistsBusNo for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_existsbusno_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_existsbusno_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: ExistsBusNo for Buses

Method: ExistsBusNo for Buses

Use the [ExistsBusNoByType](../methods/canconverter_method_existsbusnobytype_ibuscollection.htm) method instead of the ExistsBusNo method to check whether a bus with a certain number and a specific type already exists in the Buses collection. Checks in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm) whether a CAN bus with a specific number already exists.

```text
bExistsBusNo = Object.ExistsBusNo(BusNumber)
```

| Object | BusesObject with this method |
| --- | --- |
| BusNumber | LongIntegerSpecifies the number of the CAN bus. |
| bExistsBusNo | BooleanSpecifies whether the CAN bus already exists (TRUE) or not (FALSE). |

The following example displays whether a CAN bus with the number 2 already exists:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.BusDbConfig.Buses.ExistsBusNo(2))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.BusDbConfig.Buses.ExistsBusNo(2)) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_existsbusnobytype_ibuscollection.htm language=enus -->
## TOPIC 01276: Method: ExistsBusNoByType for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_existsbusnobytype_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_existsbusnobytype_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: ExistsBusNoByType for Buses

Method: ExistsBusNoByType for Buses

Checks in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm) whether a bus with a certain number and a specific type already exists in the Buses collection.

```text
bExistsBusNoByType = Object.ExistsBusNoByType(BusNumber, BusType)
```

| Object | BusesObject with this method |  |
| --- | --- | --- |
| BusNumber | LongIntegerSpecifies the number of the bus. |  |
| BusType | Specifies the bus type.Enumeration with the following selection terms: 0eBusTypeUndefined Not defined 1eBusTypeCAN CAN 2eBusTypeLIN LIN 3eBusTypeFLEXRAY Flexray |  |
| 0 | eBusTypeUndefined | Not defined |
| 1 | eBusTypeCAN | CAN |
| 2 | eBusTypeLIN | LIN |
| 3 | eBusTypeFLEXRAY | Flexray |
| bExistsBusNoByType | BooleanSpecifies whether the bus already exists (TRUE) or not (FALSE). |  |

The following example displays whether a bus with the number 2 and type CAN already exists:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.BusDbConfig.Buses.ExistsBusNoByType(2,eBusTypeCAN))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.BusDbConfig.Buses.ExistsBusNoByType(2,dd.eBusTypeCAN)) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_getindex_ibuscollection.htm language=enus -->
## TOPIC 01277: Method: GetIndex for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_getindex_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_getindex_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: GetIndex for Buses

Method: GetIndex for Buses

Returns the index of a bus from the [Buses collection](../objects/canconverter_objects_ibuscollection.htm) in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
iGetIndex = Object.GetIndex(Name)
```

| Object | BusesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the bus. |
| iGetIndex | LongIntegerReceives the index of the bus. |

The following example returns the index of the CAN2 bus:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.BusDbConfig.Buses.GetIndex("CAN2"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.BusDbConfig.Buses.GetIndex("CAN2")) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_getindex_idbfilecollection.htm language=enus -->
## TOPIC 01278: Method: GetIndex for DbFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_getindex_idbfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_getindex_idbfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: GetIndex for DbFiles

Method: GetIndex for DbFiles

Returns the index of a database file from the [DbFiles collection](../objects/canconverter_objects_idbfilecollection.htm) in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
iGetIndex = Object.GetIndex(Name)
```

| Object | DbFilesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the database file, including the path and the filename extension. |
| iGetIndex | LongIntegerReceives the index of the database file. |

The following example displays the index of the database file C:\Accelerator.dbc in the first bus collection:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBox(BusLogToTDM.BusDbConfig.Buses(1).DbFiles.GetIndex("C:\Accelerator.dbc"))
```

[Copy script](javascript:void(0);)

```text
print(dd.BusLogToTDM.BusDbConfig.Buses(1).DbFiles.GetIndex("C:\\Accelerator.dbc")) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_getindex_ilogfilecollection.htm language=enus -->
## TOPIC 01279: Method: GetIndex for LogFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_getindex_ilogfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_getindex_ilogfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: GetIndex for LogFiles

Method: GetIndex for LogFiles

Returns the index of a logfile from the [LogFiles collection](../objects/canconverter_objects_ilogfilecollection.htm) in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
iGetIndex = Object.GetIndex(Name)
```

| Object | LogFilesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the logfile, including the path and the filename extension. |
| iGetIndex | LongIntegerReceives the index of the logfile. |

The following example returns the index of the C:\MyLogFile.log logfile:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.LogSettings.LogFiles.GetIndex("C:\MyLogFile.log"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.LogSettings.LogFiles.GetIndex("C:\\MyLogFile.log")) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_ismodified_icanconverter.htm language=enus -->
## TOPIC 01280: Method: IsModified for BusLogToTDM

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_ismodified_icanconverter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_ismodified_icanconverter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: IsModified for BusLogToTDM

Method: IsModified for BusLogToTDM

Specifies in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm), whether the configuration of the Bus Log Converter has been modified.

```text
bIsModified = Object.IsModified
```

| Object | BusLogToTDMObject with this method |
| --- | --- |
| bIsModified | BooleanSpecifies whether the configuration has been modified (TRUE) or not (FALSE). |

The following example displays whether the configuration of the Bus Log Converter has been modified:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp (BusLogToTDM.IsModified)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp (dd.BusLogToTDM.IsModified()) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_item_ibuscollection.htm language=enus -->
## TOPIC 01281: Method: Item for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_item_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_item_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Item for Buses

Method: Item for Buses

Returns the bus that is associated with a specific index or name in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Set oBus = Object.Item(NameOrIndex)
```

| Object | BusesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the bus within the collection. |
| oBus | BusReturned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example assigns the first bus to the oMyBus object:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyBus
Set oMyBus = BusLogToTDM.BusDbConfig.Buses.Item(1)

Dim oMyBus
Set oMyBus = BusLogToTDM.BusDbConfig.Buses(1)
```

[Copy script](javascript:void(0);)

```text

```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_overview.htm language=enus -->
## TOPIC 01282: Methods

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > Methods

Methods

Use methods to execute actions. For example, you can use a method to add a new element to a collection. Many methods return an object that contains the accessed element in the collection.

The subordinate topics contained in the tree on the contents tab of the Help describe all the methods of the script interface of the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_remove_ibuscollection.htm language=enus -->
## TOPIC 01283: Method: Remove for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_remove_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_remove_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Remove for Buses

Method: Remove for Buses

Deletes an element from the [Buses collection](../objects/canconverter_objects_ibuscollection.htm), in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.Remove(NameOrIndex)
```

| Object | BusesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the bus. |

The following example deletes the CAN1 bus:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.BusDbConfig.Buses.Remove("CAN1")
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.BusDbConfig.Buses.Remove("CAN1") 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_remove_ibusfilterbuscollection.htm language=enus -->
## TOPIC 01284: Method: Remove for UsedBuses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_remove_ibusfilterbuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_remove_ibusfilterbuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Remove for UsedBuses

Method: Remove for UsedBuses

Deletes an element from the [UsedBuses collection](../objects/canconverter_objects_ibusfilterbuscollection.htm), in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.Remove(NameOrIndex)
```

| Object | UsedBusesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the bus. |

The following example deletes the first bus from the filtered bus collection:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.ResultSettings.BusFilter.UsedBuses.Remove(1)
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.ResultSettings.BusFilter.UsedBuses.Remove(1) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_remove_idbfilecollection.htm language=enus -->
## TOPIC 01285: Method: Remove for DbFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_remove_idbfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_remove_idbfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Remove for DbFiles

Method: Remove for DbFiles

Deletes an element from the [DbFiles collection](../objects/canconverter_objects_idbfilecollection.htm), in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.Remove(NameOrIndex)
```

| Object | DbFilesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the database file. |

The following example deletes the C:\Accelerator.dbc database file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.BusDBConfig.Buses(1).DbFiles.Remove("C:\Accelerator.dbc")
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.BusDBConfig.Buses(1).DbFiles.Remove("C:\\Accelerator.dbc") 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_remove_ilogfilecollection.htm language=enus -->
## TOPIC 01286: Method: Remove for LogFiles

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_remove_ilogfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_remove_ilogfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: Remove for LogFiles

Method: Remove for LogFiles

Deletes an element from the [LogFiles collection](../objects/canconverter_objects_ilogfilecollection.htm), in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.Remove(NameOrIndex)
```

| Object | LogFilesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the logfile. |

|  | Note It is recommended to specify several logfiles only when you convert GIN files. |
| --- | --- |

The following example deletes the first logfile from the Bus Log Converter:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.LogSettings.LogFiles.Remove(1)
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.LogSettings.LogFiles.Remove(1) 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_removeall_ibuscollection.htm language=enus -->
## TOPIC 01287: Method: RemoveAll for Buses

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_removeall_ibuscollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_removeall_ibuscollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: RemoveAll for Buses

Method: RemoveAll for Buses

Deletes all elements from the [Buses collection](../objects/canconverter_objects_ibuscollection.htm), in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.RemoveAll
```

| Object | BusesObject with this method |
| --- | --- |

The following example removes all buses from the Bus Log Converter:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call BusLogToTDM.BusDbConfig.Buses.RemoveAll()
```

[Copy script](javascript:void(0);)

```text
dd.BusLogToTDM.BusDbConfig.Buses.RemoveAll() 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/methods/canconverter_method_removeall_itostringitemvecint.htm language=enus -->
## TOPIC 01288: Method: RemoveAll for StringVector

- bundle_id: `diadem`
- source_path: `icanconverter/methods/canconverter_method_removeall_itostringitemvecint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/methods/canconverter_method_removeall_itostringitemvecint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Methods](../methods/canconverter_method_overview.htm) > Method: RemoveAll for StringVector

Method: RemoveAll for StringVector

Deletes all elements in the StringVector object in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

```text
Object.RemoveAll
```

| Object | StringVectorObject with this method |
| --- | --- |

The following example uses the method:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Set oDbFile = BusLogToTDM.BusDbConfig.Buses(1).DbFiles(1)
Call oDbFile.Clusters.RemoveAll
```

[Copy script](javascript:void(0);)

```text
oDbFile = dd.BusLogToTDM.BusDbConfig.Buses(1).DbFiles(1) 
oDbFile.Clusters.RemoveAll() 
```

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/objects/canconverter_objects_ilogfile.htm language=enus -->
## TOPIC 01289: Object: LogFile

- bundle_id: `diadem`
- source_path: `icanconverter/objects/canconverter_objects_ilogfile.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/objects/canconverter_objects_ilogfile.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/canconverter_collections_overview.htm) | [LogSettings](../objects/canconverter_objects_ilogsettings.htm)) > [LogFiles](../objects/canconverter_objects_ilogfilecollection.htm) > Object: LogFile

Object: LogFile

The LogFile object provides a logfile in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

The following example displays the full name of the first logfile:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.LogSettings.LogFiles(1).File)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.LogSettings.LogFiles(1).File) 
```

#### Properties

[DisplayFile](../properties/canconverter_property_displayfile_ilogfile.htm) | [File](../properties/canconverter_property_file_ilogfile.htm) | [XnetTdmsChannels](../properties/canconverter_property_xnettdmschannels_ilogfile.htm)

#### Returned From

[LogFiles](../objects/canconverter_objects_ilogfilecollection.htm).[Add](../methods/canconverter_method_add_ilogfilecollection.htm) | [LogFiles](../objects/canconverter_objects_ilogfilecollection.htm).[Item](../methods/canconverter_method_item_ilogfilecollection.htm)

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/objects/canconverter_objects_ilogfilecollection.htm language=enus -->
## TOPIC 01290: Collection: LogFiles

- bundle_id: `diadem`
- source_path: `icanconverter/objects/canconverter_objects_ilogfilecollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/objects/canconverter_objects_ilogfilecollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/canconverter_collections_overview.htm) | [LogSettings](../objects/canconverter_objects_ilogsettings.htm)) > Collection: LogFiles

Collection: LogFiles

Collection of all logfiles that the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm) converts to the TDM format. You only can enter multiple logfiles in GIN-Multilogger files. Every element in the LogFiles collection is a [LogFile object](../objects/canconverter_objects_ilogfile.htm).

The following example displays the number of logfiles to be converted:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBox(BusLogToTDM.LogSettings.LogFiles.Count)
```

[Copy script](javascript:void(0);)

```text
print(dd.BusLogToTDM.LogSettings.LogFiles.Count) 
```

#### Properties

[Count](../properties/canconverter_property_count_ilogfilecollection.htm)

#### Methods

[Add](../methods/canconverter_method_add_ilogfilecollection.htm) | [Exists](../methods/canconverter_method_exists_ilogfilecollection.htm) | [GetIndex](../methods/canconverter_method_getindex_ilogfilecollection.htm) | [Item](../methods/canconverter_method_item_ilogfilecollection.htm) | [Move](../methods/canconverter_method_move_ilogfilecollection.htm) | [Remove](../methods/canconverter_method_remove_ilogfilecollection.htm) | [RemoveAll](../methods/canconverter_method_removeall_ilogfilecollection.htm)

#### Returned From

[LogSettings](../objects/canconverter_objects_ilogsettings.htm).[LogFiles](../properties/canconverter_property_logfiles_ilogsettings.htm)

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/objects/canconverter_objects_ilogsettings.htm language=enus -->
## TOPIC 01291: Object: LogSettings

- bundle_id: `diadem`
- source_path: `icanconverter/objects/canconverter_objects_ilogsettings.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/objects/canconverter_objects_ilogsettings.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Objects](../objects/icanconverter_objects_overview.htm) > [BusLogToTDM](../objects/canconverter_objects_icanconverter.htm) > Object: LogSettings

Object: LogSettings

The LogSettings object makes the logfiles that are to be converted, and the file type of these files, available in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

The following example displays the file type of the logfiles that are to be converted:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.LogSettings.FileType)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.LogSettings.FileType) 
```

#### Properties

[FileType](../properties/canconverter_property_filetype_ilogsettings.htm) | [LogFiles](../properties/canconverter_property_logfiles_ilogsettings.htm)

#### Returned From

[BusLogToTDM](../objects/canconverter_objects_icanconverter.htm).[LogSettings](../properties/canconverter_property_logsettings_icanconverter.htm)

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=icanconverter/objects/canconverter_objects_iresultsettings.htm language=enus -->
## TOPIC 01292: Object: ResultSettings

- bundle_id: `diadem`
- source_path: `icanconverter/objects/canconverter_objects_iresultsettings.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icanconverter/objects/canconverter_objects_iresultsettings.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../canconverterapi_overview.htm) > [Objects](../objects/icanconverter_objects_overview.htm) > [BusLogToTDM](../objects/canconverter_objects_icanconverter.htm) > Object: ResultSettings

Object: ResultSettings

The ResultSettings object makes the settings for the conversion results available in the [Bus Log Converter](../../dlgcanconverter/dlgcanconverter/canconverter_overview.htm).

The following example displays whether the bus filter is active:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(BusLogToTDM.ResultSettings.BusFilter.Active)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.BusLogToTDM.ResultSettings.BusFilter.Active) 
```

#### Properties

[BusFilter](../properties/canconverter_property_busfilter_iresultsettings.htm) | [EnumSubstitution](../properties/canconverter_property_enumsubstitution_iresultsettings.htm) | [NumberOfSkippedFrames](../properties/canconverter_property_numberofskippedframes_iresultsettings.htm) | [ResultFile](../properties/canconverter_property_resultfile_iresultsettings.htm) | [SequenceChannel](../properties/canconverter_property_sequencechannel_iresultsettings.htm) | [SkipFirstFrames](../properties/canconverter_property_skipfirstframes_iresultsettings.htm) | [TimeFilter](../properties/canconverter_property_timefilter_iresultsettings.htm)

#### Returned From

[BusLogToTDM](../objects/canconverter_objects_icanconverter.htm).[ResultSettings](../properties/canconverter_property_resultsettings_icanconverter.htm)

#### See Also

[Objects Overview](../objects/icanconverter_objects_overview.htm)

#### Procedures

[Converting a Bus Logfile into the TDM Format](../../procnavigator/procnavigator/proccanconverter_convert_file.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_add_iassignmentlist.htm language=enus -->
## TOPIC 01293: Method: Add for AssignmentList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_add_iassignmentlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_add_iassignmentlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Add for AssignmentList <Data>

Method: Add for AssignmentList <Data>

Creates a new assignment in the assignment list of an assignment channel in the script interface for internal data .

```text
Set oAssignment = Object.Add(Value, Definition)
```

| Object | AssignmentList <Data>Object with this method |
| --- | --- |
| Value | StringSpecifies the text value of an assignment. |
| Definition | VariantSpecifies the single value or the value range of the assignment. Use a visual basic array with two values, for example, Array(1,2) to specify a value range. |
| oAssignment | Assignment <Data>Returned object |

|  | Note DIAdem always orders the list of assignments in the ascending order of the Definition property. If you used the methods Add or Remove to change the list of assignments, the index no longer corresponds with the previous position of the assignment in the list. |
| --- | --- |

The following example generates an assignment channel with three assignments and displays the definition values and the associated texts:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList, Assignment
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", DataTypeChnFloat64, 1)
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",1)
Call oMyAssgnList.Add("text2",2)
Call oMyAssgnList.Add("text3",3)
For Each Assignment in oMyAssgnList
  Call MsgBoxDisp("Definition Value: " & Assignment.Definition & vbCrLf & "Text: " & Assignment.Value)
Next
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", dd.DataTypeChnFloat64, 1) 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",1) 
oMyAssgnList.Add("text2",2) 
oMyAssgnList.Add("text3",3) 
for Assignment in oMyAssgnList: 
    dd.MsgBoxDisp("Definition Value: " + Assignment.Definition + "\r\n" + "Text: " + Assignment.Value) 
```

The following example generates an assignment channel, in which texts are assigned to three value ranges, and outputs the value ranges and the associated text:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList, Assignment, vRange
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", DataTypeChnFloat64, 1)
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",Array(1,2))
Call oMyAssgnList.Add("text2",Array(3,4))
Call oMyAssgnList.Add("text3",Array(5,6))
For Each Assignment in oMyAssgnList
  vRange = Assignment.DefinitionRange
  Call MsgBoxDisp("Definition Range " & vRange(0) & " - " & vRange(1) & ": " & Assignment.Value)
Next
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", dd.DataTypeChnFloat64, 1) 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",Array(1,2)) 
oMyAssgnList.Add("text2",Array(3,4)) 
oMyAssgnList.Add("text3",Array(5,6)) 
for Assignment in oMyAssgnList: 
    vRange = Assignment.DefinitionRange 
    dd.MsgBoxDisp("Definition Range " + vRange(0) + " - " + vRange(1) + ": " + Assignment.Value) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_add_idiademchannelgroups.htm language=enus -->
## TOPIC 01294: Method: Add for ChannelGroups <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_add_idiademchannelgroups.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_add_idiademchannelgroups.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Add for ChannelGroups <Data>

Method: Add for ChannelGroups <Data>

Creates a new channel group in the script interface for internal data and adds the channel group to the ChannelGroups collection. The Add method returns a ChannelGroup object.

```text
Set oChannelGroup = Object.Add(Name, [DestIndex])
```

| Object | ChannelGroups <Data>Object with this method |
| --- | --- |
| Name | StringSpecifies the name of the channel group. The name must conform to the DIAdem naming conventions for channel groups. If the name does not conform to the name conventions, DIAdem corrects the name. |
| [DestIndex] | LongIntegerSpecifies the position of the new channel group in the collection of existing channel groups. If you do not specify the DestIndex parameter, DIAdem creates the new channel group at the end of the collection. |
| oChannelGroup | ChannelGroup <Data>Returned object |

The following example first deletes all channel groups and then generates the MyChnGroup channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Data.Root.ChannelGroups.RemoveAll()
Call Data.Root.ChannelGroups.Add("MyChnGroup")
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.ChannelGroups.RemoveAll() 
dd.Data.Root.ChannelGroups.Add("MyChnGroup") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_add_idiademchannels.htm language=enus -->
## TOPIC 01295: Method: Add for Channels <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_add_idiademchannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_add_idiademchannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Add for Channels <Data>

Method: Add for Channels <Data>

Creates a new channel in the script interface for internal data and adds the channel to the Channels collection. The Add method returns a Channel object.

```text
Set oChannel = Object.Add(Name, DataType, [DestIndex])
```

| Object | Channels <Data>Object with this method |  |
| --- | --- | --- |
| Name | StringSpecifies the name of the channel. The name must conform to the DIAdem naming conventions for channels. If the name does not conform to the name conventions, DIAdem corrects the name. |  |
| DataType | Specifies the data type of the channel.Enumeration with the following selection terms: 10 DataTypeChnFloat64 64-bit real values 23 DataTypeChnString Text 30 DataTypeChnDate Time values |  |
| 10 | DataTypeChnFloat64 | 64-bit real values |
| 23 | DataTypeChnString | Text |
| 30 | DataTypeChnDate | Time values |
| [DestIndex] | LongIntegerSpecifies the position of the new channel in the collection of existing channels. If you do not specify the DestIndex parameter, DIAdem creates the new channel at the end of the collection. |  |
| oChannel | Channel <Data>Returned object |  |

The following example generates the DataTypeFloat64 data type channel MyChn in the MyChnGrp channel group.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oGroupChns, oMyChn
Set oGroupChns = Data.Root.ChannelGroups(1).Channels

If not oGroupChns.Exists("MyChnName") Then
  Set oMyChn = oGroupChns.Add("MyChnName",DataTypeChnFloat64)
Else
  Set oMyChn = oGroupChns("MyChnName")
End If
```

[Copy script](javascript:void(0);)

```text
oGroupChns = dd.Data.Root.ChannelGroups(1).Channels 
if not oGroupChns.Exists("MyChnName") : 
    oMyChn = oGroupChns.Add("MyChnName",dd.DataTypeChnFloat64) 
else: 
    oMyChn = oGroupChns("MyChnName") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_exists_iassignmentlist.htm language=enus -->
## TOPIC 01296: Method: Exists for AssignmentList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_exists_iassignmentlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_exists_iassignmentlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Exists for AssignmentList <Data>

Method: Exists for AssignmentList <Data>

Checks in the script interface for internal data whether an assignment with the specified text value already exists in an assignment channel.

```text
bExists = Object.Exists(Value)
```

| Object | AssignmentList <Data>Object with this method |
| --- | --- |
| Value | StringSpecifies which text value of the assignment to check. |
| bExists | BooleanThe value is TRUE if an assignment with the specified text value already exists. |

The following example generates an assignment channel with three assignments and displays whether an assignment with the textual value text2 already exists:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList 
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",1)
Call oMyAssgnList.Add("text2",2)
Call oMyAssgnList.Add("text3",3)
Call MsgBoxDisp(oMyAssgnList.Exists("text2"))
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",1) 
oMyAssgnList.Add("text2",2) 
oMyAssgnList.Add("text3",3) 
dd.MsgBoxDisp(oMyAssgnList.Exists("text2")) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_exists_idiademchannelgroups.htm language=enus -->
## TOPIC 01297: Method: Exists for ChannelGroups <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_exists_idiademchannelgroups.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_exists_idiademchannelgroups.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Exists for ChannelGroups <Data>

Method: Exists for ChannelGroups <Data>

Checks whether a ChannelGroup object with a specific name already exists in the channel groups collection in the script interface for internal data.

```text
bExists = Object.Exists(Name)
```

| Object | ChannelGroups <Data>Object with this method |
| --- | --- |
| Name | StringSpecifies the name of the channel group to be checked. DIAdem does not check the name in accordance with the DIAdem Name conventions. |
| bExists | BooleanThe value is TRUE if the collection contains an object with the specified name. |

The following example generates the SecondChnGroup channel group only if the FirstChnGroup channel group already exists:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Data.Root.ChannelGroups.Exists("FirstChnGroup") Then
  Call Data.Root.ChannelGroups.Add("SecondChnGroup")
End If
```

[Copy script](javascript:void(0);)

```text
if dd.Data.Root.ChannelGroups.Exists("FirstChnGroup") : 
    dd.Data.Root.ChannelGroups.Add("SecondChnGroup") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_iskindof_idiademimplicitchannel.htm language=enus -->
## TOPIC 01298: Method: IsKindOf for ImplicitChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_iskindof_idiademimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_iskindof_idiademimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: IsKindOf for ImplicitChannel <Data>

Method: IsKindOf for ImplicitChannel <Data>

Checks the type of an implicit channel in the script interface for internal data.

```text
bIsKindOf = Object.IsKindOf(Type)
```

| Object | ImplicitChannel <Data>Object with this method |
| --- | --- |
| Type | StringSpecifies the type of the element to be checked.Enumeration with the following selection terms: eDataRoot Root type object eDataChannelGroup ChannelGroup type object eDataChannel Channel type object eDataChannelWF Waveform channel type object eDataAssignmentChannel Assignment channel type object eDataImplicitChannel Implicit channel type object eDataChannelPair XY-channel type object eDataCalculationChannel Calculation channel type object eDataCalculationChannelFormula Calculation channel type object of Formula type eDataCalculationChannelReference Calculation channel type object of Calculation Manager calculations type. eDataVideoChannel Video channel type object eDataComplexChannel Complex channel type object |
| eDataRoot | Root type object |
| eDataChannelGroup | ChannelGroup type object |
| eDataChannel | Channel type object |
| eDataChannelWF | Waveform channel type object |
| eDataAssignmentChannel | Assignment channel type object |
| eDataImplicitChannel | Implicit channel type object |
| eDataChannelPair | XY-channel type object |
| eDataCalculationChannel | Calculation channel type object |
| eDataCalculationChannelFormula | Calculation channel type object of Formula type |
| eDataCalculationChannelReference | Calculation channel type object of Calculation Manager calculations type. |
| eDataVideoChannel | Video channel type object |
| eDataComplexChannel | Complex channel type object |
| bIsKindOf | BooleanThe value is TRUE if the object is the specified type. |

The following example checks whether the first channel of the first channel group is an implicit channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel
Set oMyChannel = Data.Root.ChannelGroups(1).Channels(1)
If oMyChannel.IsKindOf(eDataImplicitChannel) Then
  Call MsgBoxDisp("Implicit Channel")
Else
  Call MsgBoxDisp("No Implicit Channel")
End If
```

[Copy script](javascript:void(0);)

```text
oMyChannel = dd.Data.Root.ChannelGroups(1).Channels(1) 
if oMyChannel.IsKindOf(dd.eDataImplicitChannel) : 
    dd.MsgBoxDisp("Implicit Channel") 
else: 
    dd.MsgBoxDisp("No Implicit Channel") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_iskindof_idiademroot.htm language=enus -->
## TOPIC 01299: Method: IsKindOf for Root <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_iskindof_idiademroot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_iskindof_idiademroot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: IsKindOf for Root <Data>

Method: IsKindOf for Root <Data>

Checks the type of an element in the script interface for internal data.

```text
bIsKindOf = Object.IsKindOf(Type)
```

| Object | Root <Data>Object with this method |
| --- | --- |
| Type | StringSpecifies the type of the element to be checked.Enumeration with the following selection terms: eDataRoot Root type object eDataChannelGroup ChannelGroup type object eDataChannel Channel type object eDataChannelWF Waveform channel type object eDataAssignmentChannel Assignment channel type object eDataImplicitChannel Implicit channel type object eDataChannelPair XY-channel type object eDataCalculationChannel Calculation channel type object eDataCalculationChannelFormula Calculation channel type object of Formula type eDataCalculationChannelReference Calculation channel type object of Calculation Manager calculations type. eDataVideoChannel Video channel type object eDataComplexChannel Complex channel type object |
| eDataRoot | Root type object |
| eDataChannelGroup | ChannelGroup type object |
| eDataChannel | Channel type object |
| eDataChannelWF | Waveform channel type object |
| eDataAssignmentChannel | Assignment channel type object |
| eDataImplicitChannel | Implicit channel type object |
| eDataChannelPair | XY-channel type object |
| eDataCalculationChannel | Calculation channel type object |
| eDataCalculationChannelFormula | Calculation channel type object of Formula type |
| eDataCalculationChannelReference | Calculation channel type object of Calculation Manager calculations type. |
| eDataVideoChannel | Video channel type object |
| eDataComplexChannel | Complex channel type object |
| bIsKindOf | BooleanThe value is TRUE if the object is the specified type. |

The following example prompts you to select an item from the Data Portal and then to disable the interaction mode. The example displays whether you have selected the data set (root), a channel group, or a channel, in the Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyElement
Call MsgBoxDisp ("Please select one element in the Data Portal. Click 'interaction off' after selecting.")
Call InteractionOn()
Set oMyElement = Portal.ActiveView.Selection(1)
If oMyElement.IsKindOf(eDataRoot) Then
  Call MsgBoxDisp ("Selected element: Root")
ElseIf oMyElement.IsKindOf(eDataChannelGroup) Then
  Call MsgBoxDisp ("Selected element: ChannelGroup")
ElseIf oMyElement.IsKindOf(eDataChannel) Then
  Call MsgBoxDisp ("Selected element: Channel")
End If
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp ("Please select one element in the Data Portal. Click 'interaction off' after selecting.") 
dd.InteractionOn() 
oMyElement = dd.Portal.ActiveView.Selection(1) 
if oMyElement.IsKindOf(dd.eDataRoot) : 
    dd.MsgBoxDisp ("Selected element: Root") 
elif oMyElement.IsKindOf(dd.eDataChannelGroup) : 
    dd.MsgBoxDisp ("Selected element: ChannelGroup") 
elif oMyElement.IsKindOf(dd.eDataChannel) : 
    dd.MsgBoxDisp ("Selected element: Channel") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_iskindof_idiademusielement.htm language=enus -->
## TOPIC 01300: Method: IsKindOf for Element <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_iskindof_idiademusielement.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_iskindof_idiademusielement.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: IsKindOf for Element <Data>

Method: IsKindOf for Element <Data>

Checks the type of an element in the script interface for internal data.

```text
bIsKindOf = Object.IsKindOf(Type)
```

| Object | Element <Data>Object with this method |
| --- | --- |
| Type | StringSpecifies the type of the element to be checked.Enumeration with the following selection terms: eDataRoot Root type object eDataChannelGroup ChannelGroup type object eDataChannel Channel type object eDataChannelWF Waveform channel type object eDataAssignmentChannel Assignment channel type object eDataImplicitChannel Implicit channel type object eDataChannelPair XY-channel type object eDataCalculationChannel Calculation channel type object eDataCalculationChannelFormula Calculation channel type object of Formula type eDataCalculationChannelReference Calculation channel type object of Calculation Manager calculations type. eDataVideoChannel Video channel type object eDataComplexChannel Complex channel type object |
| eDataRoot | Root type object |
| eDataChannelGroup | ChannelGroup type object |
| eDataChannel | Channel type object |
| eDataChannelWF | Waveform channel type object |
| eDataAssignmentChannel | Assignment channel type object |
| eDataImplicitChannel | Implicit channel type object |
| eDataChannelPair | XY-channel type object |
| eDataCalculationChannel | Calculation channel type object |
| eDataCalculationChannelFormula | Calculation channel type object of Formula type |
| eDataCalculationChannelReference | Calculation channel type object of Calculation Manager calculations type. |
| eDataVideoChannel | Video channel type object |
| eDataComplexChannel | Complex channel type object |
| bIsKindOf | BooleanThe value is TRUE if the object is the specified type. |

The following example prompts you to select an item from the Data Portal and then to disable the interaction mode. The example displays whether you have selected the data set (root), a channel group, or a channel, in the Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyElement
Call MsgBoxDisp ("Please select one element in the Data Portal. Click 'interaction off' after selecting.")
Call InteractionOn()
Set oMyElement = Portal.ActiveView.Selection(1)
If oMyElement.IsKindOf(eDataRoot) Then
  Call MsgBoxDisp ("Selected element: Root")
ElseIf oMyElement.IsKindOf(eDataChannelGroup) Then
  Call MsgBoxDisp ("Selected element: ChannelGroup")
ElseIf oMyElement.IsKindOf(eDataChannel) Then
  Call MsgBoxDisp ("Selected element: Channel")
End If
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp ("Please select one element in the Data Portal. Click 'interaction off' after selecting.") 
dd.InteractionOn() 
oMyElement = dd.Portal.ActiveView.Selection(1) 
if oMyElement.IsKindOf(dd.eDataRoot) : 
    dd.MsgBoxDisp ("Selected element: Root") 
elif oMyElement.IsKindOf(dd.eDataChannelGroup) : 
    dd.MsgBoxDisp ("Selected element: ChannelGroup") 
elif oMyElement.IsKindOf(dd.eDataChannel) : 
    dd.MsgBoxDisp ("Selected element: Channel") 
```

The following example determines whether an element selected in the Data Portal is a waveform channel and if so, displays the name and the unit of the waveform channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyElement
Set oMyElement = Portal.ActiveView.Selection(1)
If oMyElement.IsKindOf(eDataChannelWF) Then
  Call MsgBoxDisp("Property name: " & oMyElement.Properties("wf_xname").Value & VBCrLf & _
  "Property unit: " & oMyElement.Properties("wf_xunit_string").Value)
Else
  Call MsgBoxDisp ("Selected element is no waveform channel")
End If
```

[Copy script](javascript:void(0);)

```text
oMyElement = dd.Portal.ActiveView.Selection(1) 
if oMyElement.IsKindOf(dd.eDataChannelWF) : 
    dd.MsgBoxDisp("Property name: " + oMyElement.Properties("wf_xname").Value + "\r\n" + "Property unit: " + oMyElement.Properties("wf_xunit_string").Value) 
else: 
    dd.MsgBoxDisp ("Selected element is no waveform channel") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_iskindof_idiademvideochannel.htm language=enus -->
## TOPIC 01301: Method: IsKindOf for VideoChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_iskindof_idiademvideochannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_iskindof_idiademvideochannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: IsKindOf for VideoChannel <Data>

Method: IsKindOf for VideoChannel <Data>

Checks the type of an element in the script interface for internal data.

```text
bIsKindOf = Object.IsKindOf(Type)
```

| Object | VideoChannel <Data>Object with this method |
| --- | --- |
| Type | StringSpecifies the type of the element to be checked.Enumeration with the following selection terms: eDataRoot Root type object eDataChannelGroup ChannelGroup type object eDataChannel Channel type object eDataChannelWF Waveform channel type object eDataAssignmentChannel Assignment channel type object eDataImplicitChannel Implicit channel type object eDataChannelPair XY-channel type object eDataCalculationChannel Calculation channel type object eDataCalculationChannelFormula Calculation channel type object of Formula type eDataCalculationChannelReference Calculation channel type object of Calculation Manager calculations type. eDataVideoChannel Video channel type object eDataComplexChannel Complex channel type object |
| eDataRoot | Root type object |
| eDataChannelGroup | ChannelGroup type object |
| eDataChannel | Channel type object |
| eDataChannelWF | Waveform channel type object |
| eDataAssignmentChannel | Assignment channel type object |
| eDataImplicitChannel | Implicit channel type object |
| eDataChannelPair | XY-channel type object |
| eDataCalculationChannel | Calculation channel type object |
| eDataCalculationChannelFormula | Calculation channel type object of Formula type |
| eDataCalculationChannelReference | Calculation channel type object of Calculation Manager calculations type. |
| eDataVideoChannel | Video channel type object |
| eDataComplexChannel | Complex channel type object |
| bIsKindOf | BooleanThe value is TRUE if the object is the specified type. |

The following example prompts you to select an item from the Data Portal and then to disable the interaction mode. The example displays whether you have selected the data set (root), a channel group, or a channel, in the Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyElement
Call MsgBoxDisp ("Please select one element in the Data Portal. Click 'interaction off' after selecting.")
Call InteractionOn()
Set oMyElement = Portal.ActiveView.Selection(1)
If oMyElement.IsKindOf(eDataRoot) Then
  Call MsgBoxDisp ("Selected element: Root")
ElseIf oMyElement.IsKindOf(eDataChannelGroup) Then
  Call MsgBoxDisp ("Selected element: ChannelGroup")
Else
  If oMyElement.IsKindOf(eDataChannelWF) Then
    Call MsgBoxDisp ("Selected element: Waveform channel")
  End If
  If oMyElement.IsKindOf(eDataImplicitChannel) Then
    Call MsgBoxDisp ("Selected element: Implicit channel")
  End If
  If oMyElement.IsKindOf(eDataAssignmentChannel) Then
    Call MsgBoxDisp ("Selected element: Assignment channel")
  End If
  If oMyElement.IsKindOf(eDataChannelPair) Then
    Call MsgBoxDisp ("Selected element: XY channel")
  End If
  If oMyElement.IsKindOf(eDataCalculationChannel) Then
    Call MsgBoxDisp ("Selected element: Calculation channel")
  End If
  If oMyElement.IsKindOf(eDataVideoChannel) Then
    Call MsgBoxDisp ("Selected element: Video channel")
  End If
  If oMyElement.IsKindOf(eDataComplexChannel) Then
    Call MsgBoxDisp ("Selected element: Complex channel")
  End If
  If oMyElement.IsKindOf(eDataChannel) Then
    Call MsgBoxDisp ("Selected element: Channel")
  End If
End If
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp ("Please select one element in the Data Portal. Click 'interaction off' after selecting.") 
dd.InteractionOn() 
oMyElement = dd.Portal.ActiveView.Selection(1) 
if oMyElement.IsKindOf(dd.eDataRoot) : 
    dd.MsgBoxDisp ("Selected element: Root") 
elif oMyElement.IsKindOf(dd.eDataChannelGroup) : 
    dd.MsgBoxDisp ("Selected element: ChannelGroup") 
else: 
    if oMyElement.IsKindOf(dd.eDataChannelWF) : 
        dd.MsgBoxDisp ("Selected element: Waveform channel") 
    if oMyElement.IsKindOf(dd.eDataImplicitChannel) : 
        dd.MsgBoxDisp ("Selected element: Implicit channel") 
    if oMyElement.IsKindOf(dd.eDataAssignmentChannel) : 
        dd.MsgBoxDisp ("Selected element: Assignment channel") 
    if oMyElement.IsKindOf(dd.eDataChannelPair) : 
        dd.MsgBoxDisp ("Selected element: XY channel") 
    if oMyElement.IsKindOf(dd.eDataCalculationChannel) : 
        dd.MsgBoxDisp ("Selected element: Calculation channel") 
    if oMyElement.IsKindOf(dd.eDataVideoChannel) : 
        dd.MsgBoxDisp ("Selected element: Video channel") 
    if oMyElement.IsKindOf(dd.eDataComplexChannel) : 
        dd.MsgBoxDisp ("Selected element: Complex channel") 
    if oMyElement.IsKindOf(dd.eDataChannel) : 
        dd.MsgBoxDisp ("Selected element: Channel") 
```

The following example checks whether the first channel of the first channel group is a video channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel
Set oMyChannel = Data.Root.ChannelGroups(1).Channels(1)
If oMyChannel.IsKindOf(eDataVideoChannel) Then
  Call MsgBoxDisp("Video Channel")
Else
  Call MsgBoxDisp("No Video Channel")
End If
```

[Copy script](javascript:void(0);)

```text
oMyChannel = dd.Data.Root.ChannelGroups(1).Channels(1) 
if oMyChannel.IsKindOf(dd.eDataVideoChannel) : 
    dd.MsgBoxDisp("Video Channel") 
else: 
    dd.MsgBoxDisp("No Video Channel") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_iskindof_idropinformation.htm language=enus -->
## TOPIC 01302: Method: IsKindOf for DropInformation

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_iskindof_idropinformation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_iskindof_idropinformation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: IsKindOf for DropInformation

Method: IsKindOf for DropInformation

Checks whether a DropInformation object is a certain type.

```text
bIsKindOf = Object.IsKindOf(sObjectType)
```

| Object | DropInformationObject with this method |
| --- | --- |
| sObjectType | StringSpecifies the type to be checked. DropInformation objects that are eDropText and eDropDataStoreElement type can only be dragged onto an XTable. eDropDIAdemElement PropertyList <Data> type DropInformation eDropDIAdemPropertyElementList <Data> type DropInformation eDropTextText type DropInformation eDropDataStoreElementElementList <DataStore> type DropInformation eDropFileListFileList <DataStore> type DropInformation |
| eDropDIAdemElement | PropertyList <Data> type DropInformation |
| eDropDIAdemProperty | ElementList <Data> type DropInformation |
| eDropText | Text type DropInformation |
| eDropDataStoreElement | ElementList <DataStore> type DropInformation |
| eDropFileList | FileList <DataStore> type DropInformation |
| bIsKindOf | BooleanThe return value of the IsKindOf method is TRUE if the DropInformation object is the specified type, otherwise it is FALSE. |

The example executes the user command MyOnDropPageEvent when dragging groups, channels, or properties onto a worksheet. The user command displays the names of the elements that you dragged onto an object. After you have dragged the properties onto an object, the user command displays the names and the display names of the properties. The dummy commands for CodeCompletion depend on the type of elements and properties that you drag onto an object:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Report.Events.Drop.OnPage = "MyOnDropPageEvent"

Sub MyOnDropPageEvent(Context, DropInformation)
  Dim sOutput, oMyDropElements, oMyDropElement, oMyDropProperties, oMyDropProperty 
  If DropInformation.IsKindOf(eDropDIAdemElement) Then
    Set oMyDropElements = DropInformation.DiademElements
    sOutput = oMyDropElements.Count & " dropped elements:"
    For Each oMyDropElement in oMyDropElements
      If oMyDropElement.IsKindOf(eDataRoot) Then
        sOutput = sOutput & VBCrLf & "Root name:" & VBTab &  oMyDropElement.Name
      ElseIf oMyDropElement.IsKindOf(eDataChannelGroup) Then
        sOutput = sOutput & VBCrLf & "Group name:" & VBTab &  oMyDropElement.Name
      ElseIf oMyDropElement.IsKindOf(eDataChannel) Then
        sOutput = sOutput & VBCrLf & "Channel name:" & VBTab &  oMyDropElement.Name
      End If      
    Next
  ElseIf  DropInformation.IsKindOf(eDropDIAdemProperty) Then 
    Set oMyDropProperties = DropInformation.DiademProperties
    sOutput = oMyDropProperties.Count & " dropped properties:"
    For Each oMyDropProperty in oMyDropProperties
      If oMyDropProperty.Element.IsKindOf(eDataRoot) Then
        sOutput = sOutput & VBCrLf & "Root property:" & VBTab & oMyDropProperty.Name & VBTab & "; DisplayName: " & oMyDropProperty.DisplayName
      ElseIf oMyDropProperty.Element.IsKindOf(eDataChannelGroup) Then
        sOutput = sOutput & VBCrLf & "Group property:" & VBTab & oMyDropProperty.Name & VBTab & "; DisplayName: " & oMyDropProperty.DisplayName
      ElseIf oMyDropProperty.Element.IsKindOf(eDataChannel) Then
        sOutput = sOutput & VBCrLf & "Channel property:" & VBTab & oMyDropProperty.Name & VBTab & "; DisplayName: " & oMyDropProperty.DisplayName
      End If      
    Next
  End If
  Call Msgbox(sOutput)
  Context.DoProceed = False
End Sub
```

[Copy script](javascript:void(0);)

```text
Report.Events.Drop.OnPage = "MyOnDropPageEvent" 
def MyOnDropPageEvent(Context, DropInformation): 
    if DropInformation.IsKindOf(dd.eDropDIAdemElement) : 
        oMyDropElements = DropInformation.DiademElements 
        sOutput = oMyDropElements.Count + " dropped elements:" 
        for oMyDropElement in oMyDropElements: 
            if oMyDropElement.IsKindOf(dd.eDataRoot) : 
                sOutput = sOutput + "\r\n" + "Root name:" + "\t" +  oMyDropElement.Name 
            elif oMyDropElement.IsKindOf(dd.eDataChannelGroup) : 
                sOutput = sOutput + "\r\n" + "Group name:" + "\t" +  oMyDropElement.Name 
            elif oMyDropElement.IsKindOf(dd.eDataChannel) : 
                sOutput = sOutput + "\r\n" + "Channel name:" + "\t" +  oMyDropElement.Name 
    elif DropInformation.IsKindOf(dd.eDropDIAdemProperty) : 
        oMyDropProperties = DropInformation.DiademProperties 
        sOutput = oMyDropProperties.Count + " dropped properties:" 
        for oMyDropProperty in oMyDropProperties: 
            if oMyDropProperty.Element.IsKindOf(dd.eDataRoot) : 
                sOutput = sOutput + "\r\n" + "Root property:" + "\t" + oMyDropProperty.Name + "\t" + "; DisplayName: " + oMyDropProperty.DisplayName 
            elif oMyDropProperty.Element.IsKindOf(dd.eDataChannelGroup) : 
                sOutput = sOutput + "\r\n" + "Group property:" + "\t" + oMyDropProperty.Name + "\t" + "; DisplayName: " + oMyDropProperty.DisplayName 
            elif oMyDropProperty.Element.IsKindOf(dd.eDataChannel) : 
                sOutput = sOutput + "\r\n" + "Channel property:" + "\t" + oMyDropProperty.Name + "\t" + "; DisplayName: " + oMyDropProperty.DisplayName 
    print(sOutput) 
    Context.DoProceed = False 
```

The following example executes the XTable1_EventDrop event when texts, for example from text processing, or elements from a data storage are dragged onto an XTable. The event outputs the text which you drag onto the XTable. If you drag elements from a data storage onto the XTable, the event displays the number of elements:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub XTable1_EventDrop(ByRef This, Row, Col, DropInformation)
  If DropInformation.IsKindOf(eDropText) Then
    Call Msgbox(DropInformation.Text)
  ElseIf DropInformation.IsKindOf(eDropDataStoreElement) Then
    Call Msgbox(DropInformation.DataStoreElements.Count)
  End If
End Sub

Sub XTable1_EventValGet(ByRef This, Row, Col, ByRef Cell, IsInputCell)
  Cell.Text = ""
End Sub

Sub XTable1_EventDropAllowed(ByRef This, Row, Col, DropInformation, ByRef DropEffect)
 DropEffect = eDropEffectCopy
End Sub
```

[Copy script](javascript:void(0);)

```text
def XTable1_EventDrop(ByRef This, Row, Col, DropInformation): 
    if DropInformation.IsKindOf(dd.eDropText) : 
        print(DropInformation.Text) 
    elif DropInformation.IsKindOf(dd.eDropDataStoreElement) : 
        print(DropInformation.DataStoreElements.Count) 
def XTable1_EventValGet(ByRef This, Row, Col, ByRef Cell, IsInputCell): 
    Cell.Text = "" 
def XTable1_EventDropAllowed(ByRef This, Row, Col, DropInformation, ByRef DropEffect): 
    DropEffect = eDropEffectCopy 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_iassignmentlist.htm language=enus -->
## TOPIC 01303: Method: Item for AssignmentList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_iassignmentlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_iassignmentlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for AssignmentList <Data>

Method: Item for AssignmentList <Data>

Returns the assignment of a specified index in the script interface for internal data.

```text
Set oAssignment = Object.Item(Index)
```

| Object | AssignmentList <Data>Object with this method |
| --- | --- |
| Index | VariantSpecifies the index or the text value (property Value) of the assignment. |
| oAssignment | Assignment <Data>Returned object |

|  | Note DIAdem always orders the list of assignments in the ascending order of the Definition property. If you used the methods Add or Remove to change the list of assignments, the index no longer corresponds with the previous position of the assignment in the list. |
| --- | --- |

|  | Note If you use a text (property Value) to access an assignment, DIAdem returns the first element in the list if the texts have the same name within the list. |
| --- | --- |

The following example generates an assignment channel with three assignments and displays the definition value and the text value of the second assignment:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",10)
Call oMyAssgnList.Add("text2",20)
Call oMyAssgnList.Add("text3",30)
Call MsgBoxDisp(oMyAssgnList.Item(2).Value & " - " & oMyAssgnList.Item("text2").Definition)
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",10) 
oMyAssgnList.Add("text2",20) 
oMyAssgnList.Add("text3",30) 
dd.MsgBoxDisp(oMyAssgnList.Item(2).Value + " - " + oMyAssgnList.Item("text2").Definition) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_idiademchannelgroups.htm language=enus -->
## TOPIC 01304: Method: Item for ChannelGroups <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_idiademchannelgroups.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_idiademchannelgroups.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for ChannelGroups <Data>

Method: Item for ChannelGroups <Data>

Returns the ChannelGroup object of a specific name or of a specific index in the script interface for internal data.

```text
Set oChannelGroup = Object.Item(NameOrIndex)
```

| Object | ChannelGroups <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the channel group. |
| oChannelGroup | ChannelGroup <Data>Returned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example creates the MyOffset channel property if the second channel in the FirstChnGroup channel group is called speed:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn
Set oMyGrp = Data.Root.ChannelGroups.Item("FirstChnGroup")
Set oMyChn = oMyGrp.Channels.Item(2)
If oMyChn.Name = "speed" Then
  Call oMyChn.Properties.Add("MyOffset",-5)
End If
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups.Item("FirstChnGroup") 
oMyChn = oMyGrp.Channels.Item(2) 
if oMyChn.Name == "speed" : 
    oMyChn.Properties.Add("MyOffset",-5) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_idiademchannels.htm language=enus -->
## TOPIC 01305: Method: Item for Channels <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_idiademchannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_idiademchannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for Channels <Data>

Method: Item for Channels <Data>

Returns the Channel object of a specific name or of a specific index in the script interface for internal data.

```text
Set oBaseChannel = Object.Item(NameOrIndex)
```

| Object | Channels <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the channel. |
| oBaseChannel | BaseChannel <Data>Returned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example creates the MyOffset channel property if the second channel in the FirstChnGroup channel group is called speed:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn
Set oMyGrp = Data.Root.ChannelGroups.Item("FirstChnGroup")
Set oMyChn = oMyGrp.Channels.Item(2)
If oMyChn.Name = "speed" Then
  Call oMyChn.Properties.Add("MyOffset",-5)
End If
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups.Item("FirstChnGroup") 
oMyChn = oMyGrp.Channels.Item(2) 
if oMyChn.Name == "speed" : 
    +nbsp; Call oMyChn.Properties.Add("MyOffset",-5) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_idiademelementlist.htm language=enus -->
## TOPIC 01306: Method: Item for ElementList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_idiademelementlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_idiademelementlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for ElementList <Data>

Method: Item for ElementList <Data>

Returns the ElementList object of a specific index in the script interface for internal data.

```text
Set oElement = Object.Item(Index)
```

| Object | ElementList <Data>Object with this method |
| --- | --- |
| Index | LongIntegerSpecifies the index of the element |
| oElement | Element <Data>Returned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example searches for all channels that start with the letter T and adds them to the ElementList collection. Then, the example displays the name of the first channel found in the collection. The fourth line of the example is the simplified form of the third line:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChns
Set oMyChns = Data.GetChannels("T*")
Call MsgBoxDisp("Name of first channel: " & oMyChns.Item(1).Name)
Call MsgBoxDisp("Name of first channel: " & oMyChns(1).Name)
```

[Copy script](javascript:void(0);)

```text
oMyChns = dd.Data.GetChannels("T*") 
dd.MsgBoxDisp("Name of first channel: " + oMyChns.Item(1).Name) 
dd.MsgBoxDisp("Name of first channel: " + oMyChns(1).Name) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_idiademproperties.htm language=enus -->
## TOPIC 01307: Method: Item for Properties <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_idiademproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_idiademproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for Properties <Data>

Method: Item for Properties <Data>

Returns the Property object of a specific name or of a specific index in the script interface for internal data.

```text
Set oProperty = Object.Item(NameOrIndex)
```

| Object | Properties <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the property. |
| oProperty | Property <Data>Returned object |

|  | Note You can always omit the Item method because this method is always the standard element of the collection. |
| --- | --- |

The following example changes the value of the Description data set property.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyProp
Set oMyProp = Data.Root.Properties.Item("Description")
oMyProp.Value = "Example"
```

[Copy script](javascript:void(0);)

```text
oMyProp = dd.Data.Root.Properties.Item("Description") 
oMyProp.Value = "Example" 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_idiadempropertylist.htm language=enus -->
## TOPIC 01308: Method: Item for PropertyList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_idiadempropertylist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_idiadempropertylist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for PropertyList <Data>

Method: Item for PropertyList <Data>

Returns a single property of the Root object, the ChannelGroup object, or the Channel object which belongs to a specified index.

```text
Set oProperty = Object.Item(Index)
```

| Object | PropertyList <Data>Object with this method |
| --- | --- |
| Index | LongIntegerSpecifies the index of the property. |
| oProperty | Property <Data>Returned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The example executes the user command MyOnDropPageEvent when dragging groups, channels, or properties onto a worksheet. The user command displays the names of the elements that you dragged onto an object. After you have dragged the properties onto an object, the user command displays the names and the display names of the properties. The dummy commands for CodeCompletion depend on which type the elements and properties are that you drag onto an object:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Report.Events.OnDropPage = "MyOnDropPageEvent"

Sub MyOnDropPageEvent(Context, DropContext)
  Dim sOutput, oMyDropElements, oMyDropProperties, i
  If DropContext.IsKindOf(eDropDIAdemElement) Then
    If False Then Set oMyDropElements = Data.Root.ActiveChannelGroup.Channels(1) 'This is a dummy statement for autocompletion
    Set oMyDropElements = DropContext.DiademElements
    sOutput = oMyDropElements.Count & " dropped elements:"
    For i = 1 to oMyDropElements.Count
      sOutput = sOutput & VBCrLf & "Name: " & oMyDropElements.Item(i).Name 
    Next
  ElseIf  DropContext.IsKindOf(eDropDIAdemProperty) Then 
    If False Then Set oMyDropProperties = Data.Root.ChannelGroups(1).Channels(1).Properties  'This is a dummy statement for autocompletion
    Set oMyDropProperties = DropContext.DiademProperties
    sOutput = oMyDropProperties.Count & " dropped properties:"
    For  i = 1 to oMyDropProperties.Count
      sOutput = sOutput & VBCrLf & "Name: " & oMyDropProperties.Item(i).Name & VBTab & "DisplayName: " & oMyDropProperties.Item(i).DisplayName
    Next
  End If
  Call Msgbox(sOutput)
  Context.DoProceed = False
End Sub
```

[Copy script](javascript:void(0);)

```text
Report.Events.OnDropPage = "MyOnDropPageEvent" 
def MyOnDropPageEvent(Context, DropContext): 
    if DropContext.IsKindOf(dd.eDropDIAdemElement) : 
        if False : oMyDropElements = dd.Data.Root.ActiveChannelGroup.Channels(1) #This is a dummy statement for autocompletion
            oMyDropElements = DropContext.DiademElements 
            sOutput = oMyDropElements.Count + " dropped elements:" 
            for i in range( 1, oMyDropElements.Count + 1): 
                sOutput = sOutput + "\r\n" + "Name: " + oMyDropElements.Item(i).Name 
        elif DropContext.IsKindOf(dd.eDropDIAdemProperty) : 
            if False : oMyDropProperties = dd.Data.Root.ChannelGroups(1).Channels(1).Properties #This is a dummy statement for autocompletion
                oMyDropProperties = DropContext.DiademProperties 
                sOutput = oMyDropProperties.Count + " dropped properties:" 
                for i in range( 1, oMyDropProperties.Count + 1): 
                    sOutput = sOutput + "\r\n" + "Name: " + oMyDropProperties.Item(i).Name + "\t" + "DisplayName: " + oMyDropProperties.Item(i).DisplayName 
            print(sOutput) 
            Context.DoProceed = False 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_ifilelist.htm language=enus -->
## TOPIC 01309: Method: Item for FileList <DropInformation>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_ifilelist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_ifilelist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for FileList <DropInformation>

Method: Item for FileList <DropInformation>

Returns in a file list that you drag and drop to another object the file or folder associated with a specific index.

```text
sItem = Object.Item(Index)
```

| Object | FileList <DropInformation>Object with this method |
| --- | --- |
| Index | LongIntegerSpecifies the file index. |
| sItem | StringSpecifies the file name and the file path. |

|  | Note You can always omit the Item property because it is the standard element of the collection. |
| --- | --- |

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub Tree1_EventDropAllowed(ByRef This, DropInformation, ByRef DropEffect) 'Created Event Handler
  If (DropInformation.FileList.Count >0) Then
    DropEffect = eDropEffectCopy
  End If
End Sub

Sub Tree1_EventDrop(ByRef This, DropInformation, ByRef DropEffect, ByRef Node)
  Dim oMyFile, oMyFileList, iCount
  Set oMyFileList = DropInformation.FileList
  If (oMyFileList.Count > 0) Then
    If (Not Node Is Nothing) Then
      For iCount = 1 to oMyFileList.Count
        Call Node.Nodes.Add(oMyFileList(iCount))
      Next
      Node.Expanded = True        
      Call Node.Update(eUpdateModeNodeAndChilds)
    Else
      For iCount = 1 to oMyFileList.Count
        Call This.Nodes.Add(oMyFileList(iCount))
      Next
      Call This.Refresh
    End If
  Else
    DropEffect = eDropEffectNone
  End If
End Sub
```

[Copy script](javascript:void(0);)

```text
def Tree1_EventDropAllowed(ByRef This, DropInformation, ByRef DropEffect): #Created Event Handler
    if (DropInformation.FileList.Count >0) : 
        DropEffect = eDropEffectCopy 
def Tree1_EventDrop(ByRef This, DropInformation, ByRef DropEffect, ByRef Node): 
    oMyFileList = DropInformation.FileList 
    if (oMyFileList.Count > 0) : 
        if (not Node is None) : 
            for iCount in range( 1, oMyFileList.Count + 1): 
                Node.Nodes.Add(oMyFileList(iCount)) 
            Node.Expanded = True 
            Node.Update(dd.eUpdateModeNodeAndChilds) 
        else: 
            for iCount in range( 1, oMyFileList.Count + 1): 
                This.Nodes.Add(oMyFileList(iCount)) 
            This.Refresh() 
    else: 
        DropEffect = eDropEffectNone 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_item_itemplateproperties.htm language=enus -->
## TOPIC 01310: Method: Item for TemplateProperties

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_item_itemplateproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_item_itemplateproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Item for TemplateProperties

Method: Item for TemplateProperties

Returns the TemplateProperty object that is associated with a specific name or a specific index, in the script interface for internal data.

```text
Set oTemplateProperty = Object.Item(NameOrIndex)
```

| Object | TemplatePropertiesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the property. |
| oTemplateProperty | TemplatePropertyReturned object |

|  | Note You can always omit the Item method because this method is always the standard element of the collection. |
| --- | --- |

The following example displays the name of the first custom properties template in the data set (root):

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyProp
Set oMyProp = Data.Settings.CustomPropertyTemplate.RootProperties.Item(1)
Call MsgBoxDisp ("Property name: " & oMyProp.Name)
```

[Copy script](javascript:void(0);)

```text
oMyProp = dd.Data.Settings.CustomPropertyTemplate.RootProperties.Item(1) 
dd.MsgBoxDisp ("Property name: " + oMyProp.Name) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_move_inavidata.htm language=enus -->
## TOPIC 01311: Method: Move for Data

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_move_inavidata.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_move_inavidata.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Move for Data

Method: Move for Data

Moves in the script interface for internal data a channel group or a channel to a different position in the Data Portal.

```text
Object.Move(Source, Destination, [DestIndex], [UseChnXRelations])
```

| Object | DataObject with this method |
| --- | --- |
| Source | Element <Data>Specifies the channel group or channel to be moved. |
| Destination | VariantElementList <Data> or Element <Data>If you assign an ElementList <Data> type object to the Destination parameter, the parameter determines the collection of channel groups or channels to which you move a channel group or a channel.If you assign an Element <Data> type object to the Destination parameter, the parameter determines the object behind which DIAdem moves the object you want to move. In this case, DIAdem ignores the DestIndex parameter. |
| [DestIndex] | LongIntegerSpecifies the index of the position to where you move a channel group or a channel. If you do not assign a value to the DestIndex parameter, DIAdem moves the channel group or the channel to the end of the collection. |
| [UseChnXRelations] | VariantSpecifies whether DIAdem uses the xy-channel references. If the value is TRUE, the method also copies the corresponding x-channel and retains the channel references. If the value is FALSE or if you do not specify the value, DIAdem does not use channel references. |

The following example moves the first channel of the first channel group to the second position in the second channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel, oMyChannels
Set oMyChannel = Data.Root.ChannelGroups(1).Channels(1)
Set oMyChannels = Data.Root.ChannelGroups(2).Channels
Call Data.Move(oMyChannel, oMyChannels, 2)
```

[Copy script](javascript:void(0);)

```text
oMyChannel = dd.Data.Root.ChannelGroups(1).Channels(1) 
oMyChannels = dd.Data.Root.ChannelGroups(2).Channels 
dd.Data.Move(oMyChannel, oMyChannels, 2) 
```

The following example moves the first channel of the first channel group behind the first channel of the second channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel1, oMyChannel2
Set oMyChannel1 = Data.Root.ChannelGroups(1).Channels(1)
Set oMyChannel2 = Data.Root.ChannelGroups(2).Channels(1)
Call Data.Move(oMyChannel1, oMyChannel2)
```

[Copy script](javascript:void(0);)

```text
oMyChannel1 = dd.Data.Root.ChannelGroups(1).Channels(1) 
oMyChannel2 = dd.Data.Root.ChannelGroups(2).Channels(1) 
dd.Data.Move(oMyChannel1, oMyChannel2) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_remove_iassignmentlist.htm language=enus -->
## TOPIC 01312: Method: Remove for AssignmentList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_remove_iassignmentlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_remove_iassignmentlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Remove for AssignmentList <Data>

Method: Remove for AssignmentList <Data>

Deletes an assignment from the assignment list of an assignment channel in the script interface for internal data.

```text
Object.Remove(Index)
```

| Object | AssignmentList <Data>Object with this method |
| --- | --- |
| Index | VariantSpecifies the index or the text value (property Value) of the assignment to be deleted. |

|  | Note DIAdem always orders the list of assignments in the ascending order of the Definition property. If you used the methods Add or Remove to change the list of assignments, the index no longer corresponds with the previous position of the assignment in the list. |
| --- | --- |

The following example generates an assignment channel with three assignments and then deletes the second assignment:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",1)
Call oMyAssgnList.Add("text2",2)
Call oMyAssgnList.Add("text3",3)
Call oMyAssgnList.Remove(2)
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",1) 
oMyAssgnList.Add("text2",2) 
oMyAssgnList.Add("text3",3) 
oMyAssgnList.Remove(2) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_remove_idiademchannelgroups.htm language=enus -->
## TOPIC 01313: Method: Remove for ChannelGroups <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_remove_idiademchannelgroups.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_remove_idiademchannelgroups.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Remove for ChannelGroups <Data>

Method: Remove for ChannelGroups <Data>

Deletes one element from the ChannelGroups collection in the script interface for internal data.

```text
Object.Remove(NameOrIndex)
```

| Object | ChannelGroups <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the channel group that is to be deleted. |

The following example deletes the MyChnGroup channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Data.Root.ChannelGroups.Remove("MyChnGroup")
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.ChannelGroups.Remove("MyChnGroup") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_remove_idiademchannels.htm language=enus -->
## TOPIC 01314: Method: Remove for Channels <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_remove_idiademchannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_remove_idiademchannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Remove for Channels <Data>

Method: Remove for Channels <Data>

Deletes one element from the Channels collection in the script interface for internal data.

```text
Object.Remove(NameOrIndex)
```

| Object | Channels <Data>Object with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the channel that is to be deleted. |

The following example deletes the MyChannel channel from the first channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Data.Root.ChannelGroups(1).Channels.Remove("MyChannel")
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.ChannelGroups(1).Channels.Remove("MyChannel") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_remove_idiademelementlist.htm language=enus -->
## TOPIC 01315: Method: Remove for ElementList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_remove_idiademelementlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_remove_idiademelementlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: Remove for ElementList <Data>

Method: Remove for ElementList <Data>

Deletes one element from the ElementList collection in the script interface for internal data. This method is not available if the ElementList collection is read-only.

```text
Object.Remove(Index)
```

| Object | ElementList <Data>Object with this method |
| --- | --- |
| Index | VariantSpecifies the index of the object to be deleted or an Element of the Data Portal. An element can be a data set (Root), a channel group (ChannelGroup), or a channel (Channel). |

The following example searches for all channels that start with the letter T and adds them to the ElementList collection. Then the example deletes all channels containing the string Temperature in their name from the collection:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChns, i
Set oMyChns = Data.GetChannels("T*")
For i = oMyChns.Count to 1 Step -1
  If InStr(oMyChns(i).Name,"Temperature") Then
    Call oMyChns.Remove(i)
  End If
Next
```

[Copy script](javascript:void(0);)

```text
oMyChns = dd.Data.GetChannels("T*") 
for i in range( oMyChns.Count, 1, -1): 
    if InStr(oMyChns(i).Name,"Temperature") : 
        oMyChns.Remove(i) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_removeall_iassignmentlist.htm language=enus -->
## TOPIC 01316: Method: RemoveAll for AssignmentList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_removeall_iassignmentlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_removeall_iassignmentlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: RemoveAll for AssignmentList <Data>

Method: RemoveAll for AssignmentList <Data>

Deletes all assignments of an assignment channel in the script interface for internal data.

```text
Object.RemoveAll()
```

| Object | AssignmentList <Data>Object with this method |
| --- | --- |

The following example generates an assignment channel with three assignments and then deletes all assignments:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyAssignChn, oMyAssgnList
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyAssignChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyAssignChn.AssignmentList
Call oMyAssignChn.AssignmentList.Add("text1",Array(0,1))
Call oMyAssignChn.AssignmentList.Add("text2",Array(2,3))
Call oMyAssignChn.AssignmentList.Add("text3",Array(4,5))
Call oMyAssgnList.RemoveAll()
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyAssignChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyAssignChn.AssignmentList 
oMyAssignChn.AssignmentList.Add("text1",Array(0,1)) 
oMyAssignChn.AssignmentList.Add("text2",Array(2,3)) 
oMyAssignChn.AssignmentList.Add("text3",Array(4,5)) 
oMyAssgnList.RemoveAll() 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_removeall_idiadempropertylist.htm language=enus -->
## TOPIC 01317: Method: RemoveAll for PropertyList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_removeall_idiadempropertylist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_removeall_idiadempropertylist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: RemoveAll for PropertyList <Data>

Method: RemoveAll for PropertyList <Data>

Deletes all elements from the PropertyList collection in the script interface for internal data. This method is not available if the PropertyList collection is read-only.

```text
Object.RemoveAll()
```

| Object | PropertyList <Data>Object with this method |
| --- | --- |

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_removeall_ifilelist.htm language=enus -->
## TOPIC 01318: Method: RemoveAll for FileList <DropInformation>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_removeall_ifilelist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_removeall_ifilelist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: RemoveAll for FileList <DropInformation>

Method: RemoveAll for FileList <DropInformation>

Deletes all elements of a file list you drag to another object. You can use this method in the [EventDragStart](../../sudref/events/sud_event_eventdragstart.htm) event in order to edit a file list.

```text
Object.RemoveAll()
```

| Object | FileList <DropInformation>Object with this method |
| --- | --- |

The following example deletes the entire file list in the [EventDragStart](../../sudref/events/sud_event_eventdragstart.htm)event and then adds a file to this file list.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub Tree1_EventDragStart(ByRef This, ByRef DropInformation, ByRef DropEffect)
  Dim oMyFileList
  Set oMyFileList = DropInformation.FileList
  Call oMyFileList.RemoveAll
  Call oMyFileList.Add("C:\Test")
End Sub
```

[Copy script](javascript:void(0);)

```text
def Tree1_EventDragStart(ByRef This, ByRef DropInformation, ByRef DropEffect): 
    oMyFileList = DropInformation.FileList 
    oMyFileList.RemoveAll() 
    oMyFileList.Add("C:\\Test") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_removeall_itemplateproperties.htm language=enus -->
## TOPIC 01319: Method: RemoveAll for TemplateProperties

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_removeall_itemplateproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_removeall_itemplateproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: RemoveAll for TemplateProperties

Method: RemoveAll for TemplateProperties

Deletes all custom properties from the TemplateProperties collection in the script interface for internal data.

```text
Object.RemoveAll()
```

| Object | TemplatePropertiesObject with this method |
| --- | --- |

The following example deletes all custom property templates for the data set (root):

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyPropTemplate
Set oMyPropTemplate = Data.Settings.CustomPropertyTemplate
Call oMyPropTemplate.RootProperties.RemoveAll
```

[Copy script](javascript:void(0);)

```text
oMyPropTemplate = dd.Data.Settings.CustomPropertyTemplate 
oMyPropTemplate.RootProperties.RemoveAll() 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/methods/diacmpnt_method_setboundarylimits_iassignmentlist.htm language=enus -->
## TOPIC 01320: Method: SetBoundaryLimits for AssignmentList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/methods/diacmpnt_method_setboundarylimits_iassignmentlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/methods/diacmpnt_method_setboundarylimits_iassignmentlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Methods](../methods/inavidata_method_overview.htm) > Method: SetBoundaryLimits for AssignmentList <Data>

Method: SetBoundaryLimits for AssignmentList <Data>

Specifies the behavior at the interval limits of the minimum and maximum values of an assignment, in the script interface for internal data.

```text
Object.SetBoundaryLimits(LimitsLeft, LimitsRight)
```

| Object | AssignmentList <Data>Object with this method |  |
| --- | --- | --- |
| LimitsLeft | Enumeration with the following selection terms: 1BoundsOpen Interval limit open. DIAdem also includes the minimum value in the assignments. 2BoundsClose Interval limit closed. DIAdem only includes the values that are larger than the specified minimum value in the assignments. |  |
| 1 | BoundsOpen | Interval limit open. DIAdem also includes the minimum value in the assignments. |
| 2 | BoundsClose | Interval limit closed. DIAdem only includes the values that are larger than the specified minimum value in the assignments. |
| LimitsRight | Enumeration with the following selection terms: 1BoundsOpen Interval limit open. DIAdem also includes the maximum value in the assignments. 2BoundsClose Interval limit closed. DIAdem only includes the values that are smaller than the specified maximum value in the assignments. |  |
| 1 | BoundsOpen | Interval limit open. DIAdem also includes the maximum value in the assignments. |
| 2 | BoundsClose | Interval limit closed. DIAdem only includes the values that are smaller than the specified maximum value in the assignments. |

|  | Note Specify the interval limits in a script before you generate individual assignments. |
| --- | --- |

|  | Note If you define assignments with single values, use the BoundsClose setting for the minimum and the maximum. |
| --- | --- |

The following example specifies the interval limits for the minimum and the maximum, generates an assignment channel with three assignments, and displays the settings for the interval limits:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.SetBoundaryLimits(BoundsOpen, BoundsClose) 
Call oMyAssgnList.Add("text1",10)
Call oMyAssgnList.Add("text2",20)
Call oMyAssgnList.Add("text3",30)
Call MsgBoxDisp("Left Limits: " & LimitsAsText(oMyAssgnList.BoundaryLimitsLeft) & vbCrLf & _
   "Right Limits: " & LimitsAsText(oMyAssgnList.BoundaryLimitsRight))

' Function to convert Boundary Limits from integer into text
Function LimitsAsText(eMyType)
 Select Case eMyType
  Case BoundsOpen
   LimitsAsText = "BoundsOpen"
  Case BoundsClose
   LimitsAsText = "BoundsClose"
 End Select
End Function
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.SetBoundaryLimits(dd.BoundsOpen, dd.BoundsClose) 
oMyAssgnList.Add("text1",10) 
oMyAssgnList.Add("text2",20) 
oMyAssgnList.Add("text3",30) 
dd.MsgBoxDisp("Left Limits: " + LimitsAsText(oMyAssgnList.BoundaryLimitsLeft) + "\r\n" + "Right Limits: " + LimitsAsText(oMyAssgnList.BoundaryLimitsRight)) 
# Function to convert Boundary Limits from integer into text
def LimitsAsText(eMyType): 
    select_variable_0 = eMyType 
    if (select_variable_0 == dd.BoundsOpen) : 
        LimitsAsText = "BoundsOpen" 
    elif (select_variable_0 == dd.BoundsClose) : 
        LimitsAsText = "BoundsClose" 
    return LimitsAsText
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademassignmentchannel.htm language=enus -->
## TOPIC 01321: Object: AssignmentChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademassignmentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademassignmentchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Channels](../objects/diacmpnt_objects_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: AssignmentChannel <Data>

Object: AssignmentChannel <Data>

The AssignmentChannel object provides an assignment channel in the script interface for internal data.

|  | Note Assignment channels do not support assignments to time values. |
| --- | --- |

The following example generates an assignment channel and displays the data type of this channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", DataTypeChnFloat64, 1)
If oMyChn.IsKindOf(eDataAssignmentChannel) Then 
   Call MsgBoxDisp("assignment channel")
Else
   Call MsgBoxDisp("no assignment channel")
End If
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", dd.DataTypeChnFloat64, 1) 
if oMyChn.IsKindOf(dd.eDataAssignmentChannel) : 
    dd.MsgBoxDisp("assignment channel") 
else: 
    dd.MsgBoxDisp("no assignment channel") 
```

#### Properties

[AssignmentList](../properties/diacmpnt_property_assignmentlist_idiademassignmentchannel.htm) | [ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademassignmentchannel.htm) | [DataType](../properties/diacmpnt_property_datatype_idiademassignmentchannel.htm) | [DefaultValue](../properties/diacmpnt_property_defaultvalue_idiademassignmentchannel.htm) | [dValues](../properties/diacmpnt_property_dvalues_idiademassignmentchannel.htm) | [IsReadOnly](../properties/diacmpnt_property_isreadonly_idiademassignmentchannel.htm) | [Maximum](../properties/diacmpnt_property_maximum_idiademassignmentchannel.htm) | [Minimum](../properties/diacmpnt_property_minimum_idiademassignmentchannel.htm) | [Name](../properties/diacmpnt_property_name_idiademassignmentchannel.htm) | [NoValues](../properties/diacmpnt_property_novalues_idiademassignmentchannel.htm) | [OperationalFlags](../properties/diacmpnt_property_operationalflags_idiademassignmentchannel.htm) | [Properties](../properties/diacmpnt_property_properties_idiademassignmentchannel.htm) | [ReservedSize](../properties/diacmpnt_property_reservedsize_idiademassignmentchannel.htm) | [Size](../properties/diacmpnt_property_size_idiademassignmentchannel.htm) | [UnitSymbol](../properties/diacmpnt_property_unitsymbol_idiademassignmentchannel.htm) | [Values](../properties/diacmpnt_property_values_idiademassignmentchannel.htm)

#### Methods

[GetReference](../methods/diacmpnt_method_getreference_idiademassignmentchannel.htm) | [GetValuesBlock](../methods/diacmpnt_method_getvaluesblock_idiademassignmentchannel.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademassignmentchannel.htm) | [RemoveValues](../methods/diacmpnt_method_removevalues_idiademassignmentchannel.htm) | [SetValues](../methods/diacmpnt_method_setvalues_idiademassignmentchannel.htm) | [SetValuesBlock](../methods/diacmpnt_method_setvaluesblock_idiademassignmentchannel.htm) | [XRelation](../methods/diacmpnt_method_xrelation_idiademassignmentchannel.htm)

#### Returned From

[Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddAssignmentChannel](../methods/diacmpnt_method_addassignmentchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddChannel](../methods/diacmpnt_method_addchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[Item](../methods/diacmpnt_method_item_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[GetChannel](../methods/diacmpnt_method_getchannel_inavidata.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademcalculationchannel.htm language=enus -->
## TOPIC 01322: Object: CalculationChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademcalculationchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademcalculationchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Channels](../objects/diacmpnt_objects_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: CalculationChannel <Data>

Object: CalculationChannel <Data>

The CalculationChannel <Data> object provides a [calculation channel](../../genshell/genshell/genshell_channeltypes.htm). Use the [AddCalculationChannel](../methods/diacmpnt_method_addcalculationchannel_idiademchannels.htm) method to create a new calculation channel using a simple single-line formula and the [AddCalculationChannelRef](../methods/diacmpnt_method_addcalculationchannelref_idiademchannels.htm) method to create a new calculation channel with a reference to a [calculation](../../icalculationset/objects/formulacalc_objects_icalculation.htm) of the calculation manager.

The following example generates a calculation channel from a formula with the unit "m/s".

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalculationChn
Set oMyCalculationChn = Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1)
```

[Copy script](javascript:void(0);)

```text
oMyCalculationChn = dd.Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1) 
```

#### Properties

[CalculationReference](../properties/diacmpnt_property_calculationreference_idiademcalculationchannel.htm) | [ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademcalculationchannel.htm) | [DataType](../properties/diacmpnt_property_datatype_idiademcalculationchannel.htm) | [DestUnit](../properties/diacmpnt_property_destunit_idiademcalculationchannel.htm) | [Formula](../properties/diacmpnt_property_formula_idiademcalculationchannel.htm) | [IsReadOnly](../properties/diacmpnt_property_isreadonly_idiademcalculationchannel.htm) | [Maximum](../properties/diacmpnt_property_maximum_idiademcalculationchannel.htm) | [Minimum](../properties/diacmpnt_property_minimum_idiademcalculationchannel.htm) | [Name](../properties/diacmpnt_property_name_idiademcalculationchannel.htm) | [NoValues](../properties/diacmpnt_property_novalues_idiademcalculationchannel.htm) | [OperationalFlags](../properties/diacmpnt_property_operationalflags_idiademcalculationchannel.htm) | [Properties](../properties/diacmpnt_property_properties_idiademcalculationchannel.htm) | [QuantityBased](../properties/diacmpnt_property_quantitybased_idiademcalculationchannel.htm) | [UnitSymbol](../properties/diacmpnt_property_unitsymbol_idiademcalculationchannel.htm) | [Values](../properties/diacmpnt_property_values_idiademcalculationchannel.htm)

#### Methods

[GetReference](../methods/diacmpnt_method_getreference_idiademcalculationchannel.htm) | [GetValuesBlock](../methods/diacmpnt_method_getvaluesblock_idiademcalculationchannel.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademcalculationchannel.htm) | [RunCalculation](../methods/diacmpnt_method_runcalculation_idiademcalculationchannel.htm) | [XRelation](../methods/diacmpnt_method_xrelation_idiademcalculationchannel.htm)

#### Returned From

[Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddCalculationChannel](../methods/diacmpnt_method_addcalculationchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddCalculationChannelRef](../methods/diacmpnt_method_addcalculationchannelref_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddChannel](../methods/diacmpnt_method_addchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[Item](../methods/diacmpnt_method_item_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[GetChannel](../methods/diacmpnt_method_getchannel_inavidata.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademchannel.htm language=enus -->
## TOPIC 01323: Object: Channel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AssignmentChannel](../objects/diacmpnt_objects_idiademassignmentchannel.htm) | [CalculationChannel](../objects/diacmpnt_objects_idiademcalculationchannel.htm) | [Channel](../objects/diacmpnt_objects_idiademchannel.htm) | [Channels](../objects/diacmpnt_objects_idiademchannels.htm) | [ComplexChannel](../objects/diacmpnt_objects_idiademcomplexchannel.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [ImplicitChannel](../objects/diacmpnt_objects_idiademimplicitchannel.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: Channel <Data>

Object: Channel <Data>

The Channel object provides a channel and the associated [Properties](../../genshell/genshell/genshell_dd_properties.htm) in the script interface for internal data. The Channel object is an element of the [Channels](../objects/diacmpnt_objects_idiademchannels.htm) collection.

The following example creates a new channel group, inserts a channel into the channel group, and fills this channel with values:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, i
Set oMyGrp = Data.Root.ChannelGroups.Add("MyChannelGroup")
Set oMyChn = oMyGrp.Channels.Add("MyChannel",DataTypeFloat64)
For i = 1 to 100
  oMyChn(i) = CDbl(i/100000)
Next
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups.Add("MyChannelGroup") 
oMyChn = oMyGrp.Channels.Add("MyChannel",dd.DataTypeFloat64) 
for i in range( 1, 100 + 1): 
    oMyChn[i] = float(i/100000) 
```

#### Properties

[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademchannel.htm) | [DataType](../properties/diacmpnt_property_datatype_idiademchannel.htm) | [IsReadOnly](../properties/diacmpnt_property_isreadonly_idiademchannel.htm) | [Maximum](../properties/diacmpnt_property_maximum_idiademchannel.htm) | [Minimum](../properties/diacmpnt_property_minimum_idiademchannel.htm) | [Name](../properties/diacmpnt_property_name_idiademchannel.htm) | [NoValues](../properties/diacmpnt_property_novalues_idiademchannel.htm) | [OperationalFlags](../properties/diacmpnt_property_operationalflags_idiademchannel.htm) | [Properties](../properties/diacmpnt_property_properties_idiademchannel.htm) | [ReservedSize](../properties/diacmpnt_property_reservedsize_idiademchannel.htm) | [Size](../properties/diacmpnt_property_size_idiademchannel.htm) | [UnitSymbol](../properties/diacmpnt_property_unitsymbol_idiademchannel.htm) | [Values](../properties/diacmpnt_property_values_idiademchannel.htm)

#### Methods

[GetReference](../methods/diacmpnt_method_getreference_idiademchannel.htm) | [GetValuesBlock](../methods/diacmpnt_method_getvaluesblock_idiademchannel.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademchannel.htm) | [RemoveValues](../methods/diacmpnt_method_removevalues_idiademchannel.htm) | [SetValues](../methods/diacmpnt_method_setvalues_idiademchannel.htm) | [SetValuesBlock](../methods/diacmpnt_method_setvaluesblock_idiademchannel.htm) | [XRelation](../methods/diacmpnt_method_xrelation_idiademchannel.htm)

#### Returned From

[AssignmentChannel <Data>](../objects/diacmpnt_objects_idiademassignmentchannel.htm).[XRelation](../methods/diacmpnt_method_xrelation_idiademassignmentchannel.htm) | [CalculationChannel <Data>](../objects/diacmpnt_objects_idiademcalculationchannel.htm).[XRelation](../methods/diacmpnt_method_xrelation_idiademcalculationchannel.htm) | [Channel <Data>](../objects/diacmpnt_objects_idiademchannel.htm).[XRelation](../methods/diacmpnt_method_xrelation_idiademchannel.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[Add](../methods/diacmpnt_method_add_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddChannel](../methods/diacmpnt_method_addchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[Item](../methods/diacmpnt_method_item_idiademchannels.htm) | [ComplexChannel <Data>](../objects/diacmpnt_objects_idiademcomplexchannel.htm).[XRelation](../methods/diacmpnt_method_xrelation_idiademcomplexchannel.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[GetChannel](../methods/diacmpnt_method_getchannel_inavidata.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [ImplicitChannel <Data>](../objects/diacmpnt_objects_idiademimplicitchannel.htm).[XRelation](../methods/diacmpnt_method_xrelation_idiademimplicitchannel.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademchannelgroup.htm language=enus -->
## TOPIC 01324: Object: ChannelGroup <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademchannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademchannelgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AssignmentChannel](../objects/diacmpnt_objects_idiademassignmentchannel.htm) | [CalculationChannel](../objects/diacmpnt_objects_idiademcalculationchannel.htm) | [Channel](../objects/diacmpnt_objects_idiademchannel.htm) | [ChannelGroups](../objects/diacmpnt_objects_idiademchannelgroups.htm) | [ComplexChannel](../objects/diacmpnt_objects_idiademcomplexchannel.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [ImplicitChannel](../objects/diacmpnt_objects_idiademimplicitchannel.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm) | [Root](../objects/diacmpnt_objects_idiademroot.htm) | [VideoChannel](../objects/diacmpnt_objects_idiademvideochannel.htm)) > Object: ChannelGroup <Data>

Object: ChannelGroup <Data>

The ChannelGroup object provides a channel group and the associated channels and [Properties](../../genshell/genshell/genshell_dd_properties.htm) in the script interface for internal data. The ChannelGroup object is an element of the [ChannelGroups](../objects/diacmpnt_objects_idiademchannelgroups.htm) collection.

The following example creates a new channel group, inserts a channel into the channel group, and fills this channel with values:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, i
Set oMyGrp = Data.Root.ChannelGroups.Add("MyChannelGroup")
Set oMyChn = oMyGrp.Channels.Add("MyChannel",DataTypeFloat64)
For i = 1 to 100
  oMyChn.Values(i) = CDbl(i/100000)
Next
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups.Add("MyChannelGroup") 
oMyChn = oMyGrp.Channels.Add("MyChannel",dd.DataTypeFloat64) 
for i in range( 1, 100 + 1): 
    oMyChn.Values[i] = float(i/100000) 
```

#### Properties

[Channels](../properties/diacmpnt_property_channels_idiademchannelgroup.htm) | [IsActive](../properties/diacmpnt_property_isactive_idiademchannelgroup.htm) | [Name](../properties/diacmpnt_property_name_idiademchannelgroup.htm) | [Properties](../properties/diacmpnt_property_properties_idiademchannelgroup.htm) | [Root](../properties/diacmpnt_property_root_idiademchannelgroup.htm)

#### Methods

[Activate](../methods/diacmpnt_method_activate_idiademchannelgroup.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademchannelgroup.htm)

#### Returned From

[AssignmentChannel <Data>](../objects/diacmpnt_objects_idiademassignmentchannel.htm).[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademassignmentchannel.htm) | [CalculationChannel <Data>](../objects/diacmpnt_objects_idiademcalculationchannel.htm).[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademcalculationchannel.htm) | [Channel <Data>](../objects/diacmpnt_objects_idiademchannel.htm).[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademchannel.htm) | [ChannelGroups <Data>](../objects/diacmpnt_objects_idiademchannelgroups.htm).[Add](../methods/diacmpnt_method_add_idiademchannelgroups.htm) | [ChannelGroups <Data>](../objects/diacmpnt_objects_idiademchannelgroups.htm).[AddChannelGroup](../methods/diacmpnt_method_addchannelgroup_idiademchannelgroups.htm) | [ChannelGroups <Data>](../objects/diacmpnt_objects_idiademchannelgroups.htm).[Item](../methods/diacmpnt_method_item_idiademchannelgroups.htm) | [ComplexChannel <Data>](../objects/diacmpnt_objects_idiademcomplexchannel.htm).[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademcomplexchannel.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [ImplicitChannel <Data>](../objects/diacmpnt_objects_idiademimplicitchannel.htm).[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademimplicitchannel.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm) | [Root <Data>](../objects/diacmpnt_objects_idiademroot.htm).[ActiveChannelGroup](../properties/diacmpnt_property_activechannelgroup_idiademroot.htm) | [VideoChannel <Data>](../objects/diacmpnt_objects_idiademvideochannel.htm).[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademvideochannel.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademchannelgroups.htm language=enus -->
## TOPIC 01325: Collection: ChannelGroups <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademchannelgroups.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademchannelgroups.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/inavidata_collections_overview.htm) | [Root](../objects/diacmpnt_objects_idiademroot.htm)) > Collection: ChannelGroups <Data>

Collection: ChannelGroups <Data>

Collection of all channel groups of a data set in the script interface for internal data. You use the ChannelGroups collection to access channel groups, to delete channel groups, or to add new channel groups. Each element of the ChannelGroups collection is a [ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm).

The following example first deletes all channel groups and then creates the MyChannelGroup channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Data.Root.ChannelGroups.RemoveAll
Call Data.Root.ChannelGroups.Add("MyChannelGroup")
```

[Copy script](javascript:void(0);)

```text
Data.Root.ChannelGroups.RemoveAll() 
dd.Data.Root.ChannelGroups.Add("MyChannelGroup") 
```

#### Properties

[Count](../properties/diacmpnt_property_count_idiademchannelgroups.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_idiademchannelgroups.htm) | [AddChannelGroup](../methods/diacmpnt_method_addchannelgroup_idiademchannelgroups.htm) | [Exists](../methods/diacmpnt_method_exists_idiademchannelgroups.htm) | [Item](../methods/diacmpnt_method_item_idiademchannelgroups.htm) | [Remove](../methods/diacmpnt_method_remove_idiademchannelgroups.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_idiademchannelgroups.htm) | [Sort](../methods/diacmpnt_method_sort_idiademchannelgroups.htm)

#### Returned From

[Root <Data>](../objects/diacmpnt_objects_idiademroot.htm).[ChannelGroups](../properties/diacmpnt_property_channelgroups_idiademroot.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademchannels.htm language=enus -->
## TOPIC 01326: Collection: Channels <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademchannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademchannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm) | [Collections](../objects/inavidata_collections_overview.htm)) > Collection: Channels <Data>

Collection: Channels <Data>

Collection of all channels of a channel group in the script interface for internal data. You use the Channels collection to access channels, to delete channels, or to add new channels. Each element of the Channels collection is a [Channel](../objects/diacmpnt_objects_idiademchannel.htm).

The following example generates a new channel in the first channel group and fills the channel with values:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, i
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.Add("MyChannel",DataTypeFloat64)
For i = 1 to 100
  oMyChn(i) = CDbl(i/100000)
Next
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.Add("MyChannel",dd.DataTypeFloat64) 
for i in range( 1, 100 + 1): 
    oMyChn[i] = float(i/100000) 
```

#### Properties

[Count](../properties/diacmpnt_property_count_idiademchannels.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_idiademchannels.htm) | [AddAssignmentChannel](../methods/diacmpnt_method_addassignmentchannel_idiademchannels.htm) | [AddCalculationChannel](../methods/diacmpnt_method_addcalculationchannel_idiademchannels.htm) | [AddCalculationChannelRef](../methods/diacmpnt_method_addcalculationchannelref_idiademchannels.htm) | [AddChannel](../methods/diacmpnt_method_addchannel_idiademchannels.htm) | [AddImplicitChannel](../methods/diacmpnt_method_addimplicitchannel_idiademchannels.htm) | [AddVideoChannel](../methods/diacmpnt_method_addvideochannel_idiademchannels.htm) | [Exists](../methods/diacmpnt_method_exists_idiademchannels.htm) | [GetReference](../methods/diacmpnt_method_getreference_idiademchannels.htm) | [Item](../methods/diacmpnt_method_item_idiademchannels.htm) | [Remove](../methods/diacmpnt_method_remove_idiademchannels.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_idiademchannels.htm) | [Sort](../methods/diacmpnt_method_sort_idiademchannels.htm)

#### Returned From

[ChannelGroup <Data>](../objects/diacmpnt_objects_idiademchannelgroup.htm).[Channels](../properties/diacmpnt_property_channels_idiademchannelgroup.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademcomplexchannel.htm language=enus -->
## TOPIC 01327: Object: ComplexChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademcomplexchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademcomplexchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Channels](../objects/diacmpnt_objects_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: ComplexChannel <Data>

Object: ComplexChannel <Data>

ComplexChannel <Data> object provides a [complex channel](../../genshell/genshell/genshell_channeltypes.htm) in the script interface for internal data. The Channel object is an element of the [Channels](../objects/diacmpnt_objects_idiademchannels.htm) collection. 
Complex channels are a preview feature. Preview features are new developments that will be available as a full feature in one of the upcoming DIAdem versions. The user interface, the API, and the scope of functions is subject to change.

The following example determines whether an element selected in the Data Portal is a complex channel, in which case it displays the name and the unit of the complex channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyElement
Set oMyElement = Portal.ActiveView.Selection(1)
If oMyElement.IsKindOf(eDataComplexChannel) Then
  Call MsgBoxDisp("Property name: " & oMyElement.Name & VBCrLf & _
  "Property unit: " & oMyElement.UnitSymbol)
Else
  Call MsgBoxDisp ("Selected element is no complex channel")
End If
```

[Copy script](javascript:void(0);)

```text
oMyElement = dd.Portal.ActiveView.Selection(1) 
if oMyElement.IsKindOf(dd.eDataComplexChannel) : 
    dd.MsgBoxDisp("Property name: " + oMyElement.Name + "\r\n" + "Property unit: " + oMyElement.UnitSymbol) 
else: 
    dd.MsgBoxDisp ("Selected element is no complex channel") 
```

#### Properties

[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademcomplexchannel.htm) | [DataType](../properties/diacmpnt_property_datatype_idiademcomplexchannel.htm) | [IsReadOnly](../properties/diacmpnt_property_isreadonly_idiademcomplexchannel.htm) | [Maximum](../properties/diacmpnt_property_maximum_idiademcomplexchannel.htm) | [Minimum](../properties/diacmpnt_property_minimum_idiademcomplexchannel.htm) | [Name](../properties/diacmpnt_property_name_idiademcomplexchannel.htm) | [NoValues](../properties/diacmpnt_property_novalues_idiademcomplexchannel.htm) | [OperationalFlags](../properties/diacmpnt_property_operationalflags_idiademcomplexchannel.htm) | [Properties](../properties/diacmpnt_property_properties_idiademcomplexchannel.htm) | [ReservedSize](../properties/diacmpnt_property_reservedsize_idiademcomplexchannel.htm) | [UnitSymbol](../properties/diacmpnt_property_unitsymbol_idiademcomplexchannel.htm) | [Values](../properties/diacmpnt_property_values_idiademcomplexchannel.htm)

#### Methods

[GetReference](../methods/diacmpnt_method_getreference_idiademcomplexchannel.htm) | [GetValuesBlock](../methods/diacmpnt_method_getvaluesblock_idiademcomplexchannel.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademcomplexchannel.htm) | [RemoveValues](../methods/diacmpnt_method_removevalues_idiademcomplexchannel.htm) | [SetValues](../methods/diacmpnt_method_setvalues_idiademcomplexchannel.htm) | [SetValuesBlock](../methods/diacmpnt_method_setvaluesblock_idiademcomplexchannel.htm) | [XRelation](../methods/diacmpnt_method_xrelation_idiademcomplexchannel.htm)

#### Returned From

[Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddChannel](../methods/diacmpnt_method_addchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[Item](../methods/diacmpnt_method_item_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[GetChannel](../methods/diacmpnt_method_getchannel_inavidata.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademelementlist.htm language=enus -->
## TOPIC 01328: Collection: ElementList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademelementlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademelementlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/inavidata_collections_overview.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm)) > Collection: ElementList <Data>

Collection: ElementList <Data>

Collection of elements in the script interface for internal data. Use the ElementList collection to access channels, channel groups, or the root. You can add elements to the collection or remove elements from the collection. The data in the Data Portal remains unchanged. Every element of the collection ElementList is an [Element](../objects/diacmpnt_objects_idiademusielement.htm).

|  | Note The commands DataFileLoad, DataFileLoadRed, DataFileLoadSel, and StorageImport and the methods Navigator.LoadData and Navigator.LoadProperty return an ElementList object. |
| --- | --- |

The following example searches for all [1]/Speed and [1]/RPM channels, combines the two channel lists, and outputs the amount of channels found:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oChnList, oChn1, oChn2
 
Set oChn1 = Data.GetChannel("[1]/Speed")
Set oChn2 = Data.GetChannel("[1]/RPM")
Set oChnList = Data.CreateElementList
 
Call oChnList.Add(oChn1)
Call oChnList.Add(oChn2)
 
Call MsgBox(oChnList.Count)
```

[Copy script](javascript:void(0);)

```text
oChn1 = dd.Data.GetChannel("[1]/Speed") 
oChn2 = dd.Data.GetChannel("[1]/RPM") 
oChnList = dd.Data.CreateElementList() 
oChnList.Add(oChn1) 
oChnList.Add(oChn2) 
print(oChnList.Count) 
```

#### Properties

[Count](../properties/diacmpnt_property_count_idiademelementlist.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [AddElementList](../methods/diacmpnt_method_addelementlist_idiademelementlist.htm) | [Exists](../methods/diacmpnt_method_exists_idiademelementlist.htm) | [Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Remove](../methods/diacmpnt_method_remove_idiademelementlist.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_idiademelementlist.htm)

#### Returned From

[Data](../objects/diacmpnt_objects_inavidata.htm).[CreateElementList](../methods/diacmpnt_method_createelementlist_inavidata.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[GetChannelGroups](../methods/diacmpnt_method_getchannelgroups_inavidata.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[GetChannels](../methods/diacmpnt_method_getchannels_inavidata.htm) | [DropInformation](../objects/diacmpnt_objects_idropinformation.htm).[DiademElements](../properties/diacmpnt_property_diademelements_idropinformation.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademimplicitchannel.htm language=enus -->
## TOPIC 01329: Object: ImplicitChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Channels](../objects/diacmpnt_objects_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: ImplicitChannel <Data>

Object: ImplicitChannel <Data>

The ImplicitChannel object provides an implicit channel in the interface for internal data. An implicit channel contains linear generation specifications, which describes the data, instead of single values.

The following example generates an implicit channel and displays the name and the data type:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn
Set oMyChn = Data.Root.ChannelGroups(1).Channels.AddImplicitChannel("MyImplChn",1,5,100,DataTypeFloat64)
Call MsgBoxDisp ("Channel name: " & oMyChn.Name & VBCrLf & "Data type: " & oMyChn.DataType)
```

[Copy script](javascript:void(0);)

```text
oMyChn = dd.Data.Root.ChannelGroups(1).Channels.AddImplicitChannel("MyImplChn",1,5,100,dd.DataTypeFloat64) 
dd.MsgBoxDisp ("Channel name: " + oMyChn.Name + "\r\n" + "Data type: " + oMyChn.DataType) 
```

#### Properties

[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademimplicitchannel.htm) | [DataType](../properties/diacmpnt_property_datatype_idiademimplicitchannel.htm) | [Increment](../properties/diacmpnt_property_increment_idiademimplicitchannel.htm) | [IsReadOnly](../properties/diacmpnt_property_isreadonly_idiademimplicitchannel.htm) | [Maximum](../properties/diacmpnt_property_maximum_idiademimplicitchannel.htm) | [Minimum](../properties/diacmpnt_property_minimum_idiademimplicitchannel.htm) | [Name](../properties/diacmpnt_property_name_idiademimplicitchannel.htm) | [NoValues](../properties/diacmpnt_property_novalues_idiademimplicitchannel.htm) | [OperationalFlags](../properties/diacmpnt_property_operationalflags_idiademimplicitchannel.htm) | [Properties](../properties/diacmpnt_property_properties_idiademimplicitchannel.htm) | [Size](../properties/diacmpnt_property_size_idiademimplicitchannel.htm) | [StartValue](../properties/diacmpnt_property_startvalue_idiademimplicitchannel.htm) | [UnitSymbol](../properties/diacmpnt_property_unitsymbol_idiademimplicitchannel.htm) | [Values](../properties/diacmpnt_property_values_idiademimplicitchannel.htm)

#### Methods

[GetReference](../methods/diacmpnt_method_getreference_idiademimplicitchannel.htm) | [GetValuesBlock](../methods/diacmpnt_method_getvaluesblock_idiademimplicitchannel.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademimplicitchannel.htm) | [XRelation](../methods/diacmpnt_method_xrelation_idiademimplicitchannel.htm)

#### Returned From

[Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddChannel](../methods/diacmpnt_method_addchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddImplicitChannel](../methods/diacmpnt_method_addimplicitchannel_idiademchannels.htm) | [Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[Item](../methods/diacmpnt_method_item_idiademchannels.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[GetChannel](../methods/diacmpnt_method_getchannel_inavidata.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademproperties.htm language=enus -->
## TOPIC 01330: Collection: Properties <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AssignmentChannel](../objects/diacmpnt_objects_idiademassignmentchannel.htm) | [CalculationChannel](../objects/diacmpnt_objects_idiademcalculationchannel.htm) | [Channel](../objects/diacmpnt_objects_idiademchannel.htm) | [ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm) | [Collections](../objects/inavidata_collections_overview.htm) | [ComplexChannel](../objects/diacmpnt_objects_idiademcomplexchannel.htm) | [ImplicitChannel](../objects/diacmpnt_objects_idiademimplicitchannel.htm) | [Root](../objects/diacmpnt_objects_idiademroot.htm) | [VideoChannel](../objects/diacmpnt_objects_idiademvideochannel.htm)) > Collection: Properties <Data>

Collection: Properties <Data>

Collection of all the properties of a data element for the [Root](../objects/diacmpnt_objects_idiademroot.htm) object, the [ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm) object, or the [Channel](../objects/diacmpnt_objects_idiademchannel.htm) object, in the script interface for internal data. The properties include the base properties of the data model and custom properties. You use the Properties collection to access properties, and to delete or to add properties.

|  | Note Refer to Properties in DIAdem - Overview for information about properties of files, groups, and channels. |
| --- | --- |

The following example assigns new values to the properties Description and Author of the Root object:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Data.Root.Properties.Add("Description","test")
Call Data.Root.Properties.Add("Author","user")
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Properties.Add("Description","test") 
dd.Data.Root.Properties.Add("Author","user") 
```

#### Properties

[Count](../properties/diacmpnt_property_count_idiademproperties.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_idiademproperties.htm) | [AddProperties](../methods/diacmpnt_method_addproperties_idiademproperties.htm) | [Exists](../methods/diacmpnt_method_exists_idiademproperties.htm) | [Item](../methods/diacmpnt_method_item_idiademproperties.htm) | [Remove](../methods/diacmpnt_method_remove_idiademproperties.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_idiademproperties.htm)

#### Returned From

[AssignmentChannel <Data>](../objects/diacmpnt_objects_idiademassignmentchannel.htm).[Properties](../properties/diacmpnt_property_properties_idiademassignmentchannel.htm) | [CalculationChannel <Data>](../objects/diacmpnt_objects_idiademcalculationchannel.htm).[Properties](../properties/diacmpnt_property_properties_idiademcalculationchannel.htm) | [Channel <Data>](../objects/diacmpnt_objects_idiademchannel.htm).[Properties](../properties/diacmpnt_property_properties_idiademchannel.htm) | [ChannelGroup <Data>](../objects/diacmpnt_objects_idiademchannelgroup.htm).[Properties](../properties/diacmpnt_property_properties_idiademchannelgroup.htm) | [ImplicitChannel <Data>](../objects/diacmpnt_objects_idiademimplicitchannel.htm).[Properties](../properties/diacmpnt_property_properties_idiademimplicitchannel.htm) | [Root <Data>](../objects/diacmpnt_objects_idiademroot.htm).[Properties](../properties/diacmpnt_property_properties_idiademroot.htm) | [VideoChannel <Data>](../objects/diacmpnt_objects_idiademvideochannel.htm).[Properties](../properties/diacmpnt_property_properties_idiademvideochannel.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademproperty.htm language=enus -->
## TOPIC 01331: Object: Property <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AssignmentChannel](../objects/diacmpnt_objects_idiademassignmentchannel.htm) | [CalculationChannel](../objects/diacmpnt_objects_idiademcalculationchannel.htm) | [Channel](../objects/diacmpnt_objects_idiademchannel.htm) | [ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm) | [Collections](../objects/inavidata_collections_overview.htm) | [ComplexChannel](../objects/diacmpnt_objects_idiademcomplexchannel.htm) | [ImplicitChannel](../objects/diacmpnt_objects_idiademimplicitchannel.htm) | [Root](../objects/diacmpnt_objects_idiademroot.htm) | [VideoChannel](../objects/diacmpnt_objects_idiademvideochannel.htm)) > [Properties](../objects/diacmpnt_objects_idiademproperties.htm) > Object: Property <Data>

Object: Property <Data>

The Property object provides a property for the Root object, for the ChannelGroup object, or for the Channel object in the script interface for internal data. This property is either a DIAdem base property or a custom property. The Property object is an element of the [Properties](../objects/diacmpnt_objects_idiademproperties.htm) or [PropertyList](../objects/diacmpnt_objects_idiadempropertylist.htm) collection.

|  | Note Refer to Properties in DIAdem - Overview for information about properties of files, groups, and channels. |
| --- | --- |

The following example searches for the MyOffset channel property in all the channels of the first channel group and doubles the value of the property:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn, oMyProp
For Each oMyChn in Data.Root.ChannelGroups(1).Channels
  For Each oMyProp in oMyChn.Properties
    If oMyProp.Name = "MyOffset" Then
      oMyProp.Value = oMyProp.Value * 2
    End If
  Next
Next
```

[Copy script](javascript:void(0);)

```text
for oMyChn in dd.Data.Root.ChannelGroups(1).Channels: 
    for oMyProp in oMyChn.Properties: 
        if oMyProp.Name == "MyOffset" : 
            oMyProp.Value = oMyProp.Value * 2 
```

#### Properties

[Custom](../properties/diacmpnt_property_custom_idiademproperty.htm) | [DataType](../properties/diacmpnt_property_datatype_idiademproperty.htm) | [DisplayName](../properties/diacmpnt_property_displayname_idiademproperty.htm) | [Element](../properties/diacmpnt_property_element_idiademproperty.htm) | [Hidden](../properties/diacmpnt_property_hidden_idiademproperty.htm) | [Name](../properties/diacmpnt_property_name_idiademproperty.htm) | [ReadOnly](../properties/diacmpnt_property_readonly_idiademproperty.htm) | [Value](../properties/diacmpnt_property_value_idiademproperty.htm)

#### Returned From

[Properties <Data>](../objects/diacmpnt_objects_idiademproperties.htm).[Add](../methods/diacmpnt_method_add_idiademproperties.htm) | [Properties <Data>](../objects/diacmpnt_objects_idiademproperties.htm).[Item](../methods/diacmpnt_method_item_idiademproperties.htm) | [PropertyList <Data>](../objects/diacmpnt_objects_idiadempropertylist.htm).[Add](../methods/diacmpnt_method_add_idiadempropertylist.htm) | [PropertyList <Data>](../objects/diacmpnt_objects_idiadempropertylist.htm).[Item](../methods/diacmpnt_method_item_idiadempropertylist.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiadempropertylist.htm language=enus -->
## TOPIC 01332: Collection: PropertyList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiadempropertylist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiadempropertylist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Collections](../objects/inavidata_collections_overview.htm) > Collection: PropertyList <Data>

Collection: PropertyList <Data>

Collection of the [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm) objects which you dragged and dropped onto another object. Use the PropertyList <Data> collection to access an individual property of the Root, ChannelGroup, or Channel object. These properties might be DIAdem base properties or custom properties of the channels, the channel groups, or the root.

|  | Note To test the example script, you must first save the script and register the script as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The example executes the user command MyOnDropPageEvent when dragging groups, channels, or properties onto a worksheet. The user command displays the names of the elements that you dragged onto an object. After you have dragged the properties onto an object, the user command displays the names and the display names of the properties. The dummy commands for CodeCompletion depend on the type of elements and properties that you drag onto an object:

[Copy script](javascript:void(0);)

```text
Report.Events.OnDropPage = "MyOnDropPageEvent"

Sub MyOnDropPageEvent(Context, DropInformation)
  Dim sOutput, oMyDropElements, oMyDropElement, oMyDropProperties, oMyDropProperty 
  If DropInformation.IsKindOf(eDropDIAdemElement) Then
    If False Then Set oMyDropElements = Data.Root.ActiveChannelGroup.Channels(1) 'This is a dummy statement for autocompletion
    Set oMyDropElements = DropInformation.DiademElements
    sOutput = oMyDropElements.Count & " dropped elements:"
    For Each oMyDropElement in oMyDropElements
      sOutput = sOutput & VBCrLf & "Name: " & oMyDropElement.Name 
    Next
  ElseIf  DropInformation.IsKindOf(eDropDIAdemProperty) Then 
    If False Then Set oMyDropProperties = Data.Root.ChannelGroups(1).Channels(1).Properties  'This is a dummy statement for autocompletion
    Set oMyDropProperties = DropInformation.DiademProperties
    sOutput = oMyDropProperties.Count & " dropped properties:"
    For Each oMyDropProperty in oMyDropProperties
      sOutput = sOutput & VBCrLf & "Name: " & oMyDropProperty.Name & VBTab & "DisplayName: " & oMyDropProperty.DisplayName
    Next
  End If
  Call Msgbox(sOutput)
  Context.DoProceed = False
End Sub
```

#### Properties

[Count](../properties/diacmpnt_property_count_idiadempropertylist.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_idiadempropertylist.htm) | [AddPropertyList](../methods/diacmpnt_method_addpropertylist_idiadempropertylist.htm) | [Item](../methods/diacmpnt_method_item_idiadempropertylist.htm) | [Remove](../methods/diacmpnt_method_remove_idiadempropertylist.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_idiadempropertylist.htm)

#### Returned From

[DropInformation](../objects/diacmpnt_objects_idropinformation.htm).[DiademProperties](../properties/diacmpnt_property_diademproperties_idropinformation.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademroot.htm language=enus -->
## TOPIC 01333: Object: Root <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademroot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademroot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: Root <Data>

Object: Root <Data>

The Root object provides the collection of all the channel groups and all the [Properties](../../genshell/genshell/genshell_dd_properties.htm) of the data set in the script interface for internal data.

The following example deletes the internal data store and then generates the MyChannelGroup channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Data.Root.Clear()
Call Data.Root.ChannelGroups.Add("MyChannelGroup")
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.Data.Root.ChannelGroups.Add("MyChannelGroup") 
```

#### Properties

[ActiveChannelGroup](../properties/diacmpnt_property_activechannelgroup_idiademroot.htm) | [ChannelGroups](../properties/diacmpnt_property_channelgroups_idiademroot.htm) | [Name](../properties/diacmpnt_property_name_idiademroot.htm) | [Properties](../properties/diacmpnt_property_properties_idiademroot.htm)

#### Methods

[Clear](../methods/diacmpnt_method_clear_idiademroot.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademroot.htm)

#### Returned From

[ChannelGroup <Data>](../objects/diacmpnt_objects_idiademchannelgroup.htm).[Root](../properties/diacmpnt_property_root_idiademchannelgroup.htm) | [Data](../objects/diacmpnt_objects_inavidata.htm).[Root](../properties/diacmpnt_property_root_inavidata.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademusielement.htm language=enus -->
## TOPIC 01334: Object: Element <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademusielement.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademusielement.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: Element <Data>

Object: Element <Data>

The Element object provides a single element in the script interface for internal data. Depending on whether an element of the internal data is a data set ([Root](../objects/diacmpnt_objects_idiademroot.htm)), a group ([ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm)), or a channel ([Channel](../objects/diacmpnt_objects_idiademchannel.htm)), the Element object has additional properties. Use the [IsKindOf](../methods/diacmpnt_method_iskindof_idiademusielement.htm) method to determine the type of an element. Refer to [Working with the Elements Collection and the Element Object](../../genshell/genshell/genshell_working_with_elements.htm) for general information on working with the elements.

The Element object corresponds to one of the following objects:

| Root (IDiademRoot) | Data set |
| --- | --- |
| ChannelGroup (IDiademChannelGroup) | Channel group |
| Channel (IDiademChannel) | Channel |

The following example displays the name for each element that is selected in the Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMySelectedElement
For Each oMySelectedElement in Portal.Structure.Selection
  If oMySelectedElement.IsKindOf(eDataRoot) Then
    Call MsgBoxDisp ("Root: " & oMySelectedElement.Name)
  ElseIf oMySelectedElement.IsKindOf(eDataChannelGroup) Then
    Call MsgBoxDisp ("ChannelGroup: " & oMySelectedElement.Name)
  ElseIf oMySelectedElement.IsKindOf(eDataChannel) Then 
    Call MsgBoxDisp ("Channel: " & oMySelectedElement.Name)
  End If
Next
```

[Copy script](javascript:void(0);)

```text
for oMySelectedElement in dd.Portal.Structure.Select()ion: 
    if oMySelectedElement.IsKindOf(dd.eDataRoot) : 
        dd.MsgBoxDisp ("Root: " + oMySelectedElement.Name) 
    elif oMySelectedElement.IsKindOf(dd.eDataChannelGroup) : 
        dd.MsgBoxDisp ("ChannelGroup: " + oMySelectedElement.Name) 
    elif oMySelectedElement.IsKindOf(dd.eDataChannel) : 
        dd.MsgBoxDisp ("Channel: " + oMySelectedElement.Name) 
```

#### Properties

[Name](../properties/diacmpnt_property_name_idiademusielement.htm) | [Properties](../properties/diacmpnt_property_properties_idiademusielement.htm)

#### Methods

[IsKindOf](../methods/diacmpnt_method_iskindof_idiademusielement.htm)

#### Returned From

[ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_idiademvideochannel.htm language=enus -->
## TOPIC 01335: Object: VideoChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_idiademvideochannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_idiademvideochannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Channels](../objects/diacmpnt_objects_idiademchannels.htm) | [ElementList](../objects/diacmpnt_objects_idiademelementlist.htm) | [Property](../objects/diacmpnt_objects_idiademproperty.htm)) > Object: VideoChannel <Data>

Object: VideoChannel <Data>

The VideoChannel <Data> object provides a [video channel](../../genshell/genshell/genshell_channeltypes.htm).

The following example creates a video channel with a relative path to the data file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyVideoChn
Set oMyVideoChn= Data.Root.ChannelGroups(1).Channels.AddVideoChannel("Video", "Safetytest02.wmv", eFilePathRelative,NoValue, NoValue, 1)
```

[Copy script](javascript:void(0);)

```text
oMyVideoChn= dd.Data.Root.ChannelGroups(1).Channels.AddVideoChannel("Video", "Safetytest02.wmv", dd.eFilePathRelative,dd.NoValue, dd.NoValue, 1) 
```

#### Properties

[ChannelGroup](../properties/diacmpnt_property_channelgroup_idiademvideochannel.htm) | [IsReadOnly](../properties/diacmpnt_property_isreadonly_idiademvideochannel.htm) | [Name](../properties/diacmpnt_property_name_idiademvideochannel.htm) | [Properties](../properties/diacmpnt_property_properties_idiademvideochannel.htm)

#### Methods

[GetReference](../methods/diacmpnt_method_getreference_idiademvideochannel.htm) | [IsKindOf](../methods/diacmpnt_method_iskindof_idiademvideochannel.htm)

#### Returned From

[Channels <Data>](../objects/diacmpnt_objects_idiademchannels.htm).[AddVideoChannel](../methods/diacmpnt_method_addvideochannel_idiademchannels.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Add](../methods/diacmpnt_method_add_idiademelementlist.htm) | [ElementList <Data>](../objects/diacmpnt_objects_idiademelementlist.htm).[Item](../methods/diacmpnt_method_item_idiademelementlist.htm) | [Property <Data>](../objects/diacmpnt_objects_idiademproperty.htm).[Element](../properties/diacmpnt_property_element_idiademproperty.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_ifilelist.htm language=enus -->
## TOPIC 01336: Collection: FileList <DropInformation>

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_ifilelist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_ifilelist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Collections](../objects/inavidata_collections_overview.htm) > Collection: FileList <DropInformation>

Collection: FileList <DropInformation>

Specifies a file list you drag and drop to a different object.

The following example creates a tree you can drag files to. The tree displays the names of these files as new branches.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub Tree1_EventDropAllowed(ByRef This, DropInformation, ByRef DropEffect) 'Creataed Event Handler
  If (DropInformation.FileList.Count >0) Then
    DropEffect = eDropEffectCopy
  End If
End Sub

Sub Tree1_EventDrop(ByRef This, DropInformation, ByRef DropEffect, ByRef Node)
  Dim oMyFile
  If (DropInformation.FileList.Count >0) Then
    If (Not Node Is Nothing) Then
      For Each oMyFile In DropInformation.FileList
        Call Node.Nodes.Add(oMyFile)
      Next
      Node.Expanded = True        
      Call Node.Update(eUpdateModeNodeAndChilds)
    Else
      For Each oMyFile In DropInformation.FileList
        Call This.Nodes.Add(oMyFile)
      Next
      Call This.Refresh
    End If
  Else
    DropEffect = eDropEffectNone
  End If
End Sub
```

[Copy script](javascript:void(0);)

```text
def Tree1_EventDropAllowed(ByRef This, DropInformation, ByRef DropEffect): #Creataed Event Handler
    if (DropInformation.FileList.Count >0) : 
        DropEffect = eDropEffectCopy 
def Tree1_EventDrop(ByRef This, DropInformation, ByRef DropEffect, ByRef Node): 
    if (DropInformation.FileList.Count >0) : 
        if (not Node is None) : 
            for oMyFile in DropInformation.FileList: 
                Node.Nodes.Add(oMyFile) 
            Node.Expanded = True 
            Node.Update(dd.eUpdateModeNodeAndChilds) 
        else: 
            for oMyFile in DropInformation.FileList: 
                This.Nodes.Add(oMyFile) 
            This.Refresh() 
    else: 
        DropEffect = eDropEffectNone 
```

#### Properties

[Count](../properties/diacmpnt_property_count_ifilelist.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_ifilelist.htm) | [Item](../methods/diacmpnt_method_item_ifilelist.htm) | [Remove](../methods/diacmpnt_method_remove_ifilelist.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_ifilelist.htm)

#### Returned From

[DropInformation](../objects/diacmpnt_objects_idropinformation.htm).[FileList](../properties/diacmpnt_property_filelist_idropinformation.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_inavidata.htm language=enus -->
## TOPIC 01337: Object: Data

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_inavidata.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_inavidata.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Objects](../objects/inavidata_objects_overview.htm) > Object: Data

Object: Data

The Data object accesses the internal DIAdem data. You use the Data object to generate, to edit, and to delete channel groups and channels with the associated properties. The Data object is available as a global object in scripts and in dialog boxes.

Only read access.

|  | Note Use the commands DataFileLoad, DataFileLoadRed, and DataFileLoadSel, to load files into the internal DIAdem data store. Use the Navigator.LoadData method to load data elements from the search results or from the file browser in DIAdem NAVIGATOR, into DIAdem. |
| --- | --- |

|  | Note Use the Data.Root.Clear method to delete data from the internal data store. |
| --- | --- |

The following example displays the number of data set (root) properties:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp (Data.Root.Properties.Count)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp (dd.Data.Root.Properties.Count) 
```

#### Properties

[Root](../properties/diacmpnt_property_root_inavidata.htm) | [Settings](../properties/diacmpnt_property_settings_inavidata.htm)

#### Methods

[CreateElementList](../methods/diacmpnt_method_createelementlist_inavidata.htm) | [GetChannel](../methods/diacmpnt_method_getchannel_inavidata.htm) | [GetChannelGroups](../methods/diacmpnt_method_getchannelgroups_inavidata.htm) | [GetChannels](../methods/diacmpnt_method_getchannels_inavidata.htm) | [Move](../methods/diacmpnt_method_move_inavidata.htm) | [Remove](../methods/diacmpnt_method_remove_inavidata.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_itemplateproperties.htm language=enus -->
## TOPIC 01338: Collection: TemplateProperties

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_itemplateproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_itemplateproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/inavidata_collections_overview.htm) | [CustomPropertyTemplate](../objects/diacmpnt_objects_idatatemplate.htm)) > Collection: TemplateProperties

Collection: TemplateProperties

Collection of all the properties of a [custom properties template](../../dlgshell/dlgshell/dlg_custproptemplate_dialog.htm) for the [Root](../objects/diacmpnt_objects_idiademroot.htm) object, the [ChannelGroup](../objects/diacmpnt_objects_idiademchannelgroup.htm) object, or the [Channel](../objects/diacmpnt_objects_idiademchannel.htm) object in the script interface for internal data. You can use the TemplateProperties collection to access custom properties templates and to add and delete custom properties templates.

The following example generates a new custom property template for the data set (root):

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyPropTemplate
Set oMyPropTemplate = Data.Settings.CustomPropertyTemplate
Call oMyPropTemplate.RootProperties.Add("MyRootProp", 2)
```

[Copy script](javascript:void(0);)

```text
oMyPropTemplate = dd.Data.Settings.CustomPropertyTemplate 
oMyPropTemplate.RootProperties.Add("MyRootProp", 2) 
```

#### Properties

[Count](../properties/diacmpnt_property_count_itemplateproperties.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_itemplateproperties.htm) | [Exists](../methods/diacmpnt_method_exists_itemplateproperties.htm) | [Item](../methods/diacmpnt_method_item_itemplateproperties.htm) | [Remove](../methods/diacmpnt_method_remove_itemplateproperties.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_itemplateproperties.htm)

#### Returned From

[CustomPropertyTemplate](../objects/diacmpnt_objects_idatatemplate.htm).[ChannelGroupProperties](../properties/diacmpnt_property_channelgroupproperties_idatatemplate.htm) | [CustomPropertyTemplate](../objects/diacmpnt_objects_idatatemplate.htm).[ChannelProperties](../properties/diacmpnt_property_channelproperties_idatatemplate.htm) | [CustomPropertyTemplate](../objects/diacmpnt_objects_idatatemplate.htm).[RootProperties](../properties/diacmpnt_property_rootproperties_idatatemplate.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/objects/diacmpnt_objects_itemplateproperty.htm language=enus -->
## TOPIC 01339: Object: TemplateProperty

- bundle_id: `diadem`
- source_path: `inavidata/objects/diacmpnt_objects_itemplateproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/objects/diacmpnt_objects_itemplateproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/inavidata_collections_overview.htm) | [CustomPropertyTemplate](../objects/diacmpnt_objects_idatatemplate.htm)) > [TemplateProperties](../objects/diacmpnt_objects_itemplateproperties.htm) > Object: TemplateProperty

Object: TemplateProperty

The Property object provides a [custom properties template](../../dlgshell/dlgshell/dlg_custproptemplate_dialog.htm) of the data set ([Root](../objects/diacmpnt_objects_idiademroot.htm)), of a [Channel group](../objects/diacmpnt_objects_idiademchannelgroup.htm), or of a [Channel](../objects/diacmpnt_objects_idiademchannel.htm) in the script interface for internal data. The TemplateProperty object is an element of the [TemplateProperties](../objects/diacmpnt_objects_itemplateproperties.htm) collection.

The following example assigns the value 0 to the custom properties template MyRootProp:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyPropTemplate
Set oMyPropTemplate = Data.Settings.CustomPropertyTemplate
oMyPropTemplate.RootProperties("MyRootProp").Value = 0
```

[Copy script](javascript:void(0);)

```text
oMyPropTemplate = dd.Data.Settings.CustomPropertyTemplate 
oMyPropTemplate.RootProperties("MyRootProp").Value = 0 
```

#### Properties

[DataType](../properties/diacmpnt_property_datatype_itemplateproperty.htm) | [Name](../properties/diacmpnt_property_name_itemplateproperty.htm) | [Value](../properties/diacmpnt_property_value_itemplateproperty.htm)

#### Returned From

[TemplateProperties](../objects/diacmpnt_objects_itemplateproperties.htm).[Add](../methods/diacmpnt_method_add_itemplateproperties.htm) | [TemplateProperties](../objects/diacmpnt_objects_itemplateproperties.htm).[Item](../methods/diacmpnt_method_item_itemplateproperties.htm)

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_boundarylimitsleft_iassignmentlist.htm language=enus -->
## TOPIC 01340: Property: BoundaryLimitsLeft for AssignmentList <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_boundarylimitsleft_iassignmentlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_boundarylimitsleft_iassignmentlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: BoundaryLimitsLeft for AssignmentList <Data>

Property: BoundaryLimitsLeft for AssignmentList <Data>

Specifies the interval limit of the minimum value of an assignment in an assignment channel in the script interface for internal data.

```text
Object.BoundaryLimitsLeft
```

| Object | AssignmentList <Data>Object with this property |  |
| --- | --- | --- |
| Object.BoundaryLimitsLeft | Enumeration with read access and the following selection terms:1BoundsOpen Interval limit open. DIAdem only includes the values that are larger than the specified minimum value in the assignments.2BoundsClose Interval limit closed. DIAdem also includes the minimum value in the assignments. |  |
| 1 | BoundsOpen | Interval limit open. DIAdem only includes the values that are larger than the specified minimum value in the assignments. |
| 2 | BoundsClose | Interval limit closed. DIAdem also includes the minimum value in the assignments. |

|  | Note Specify the interval limits in a script before you generate individual assignments. |
| --- | --- |

|  | Note If you define assignments with single values, use the BoundsClose setting for the minimum and the maximum. |
| --- | --- |

The following example specifies the interval limits for the minimum and the maximum and displays these values:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", DataTypeChnFloat64, 1)
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.SetBoundaryLimits(BoundsOpen, BoundsClose) 
Call oMyAssgnList.Add("text1",1)
Call oMyAssgnList.Add("text2",2)
Call oMyAssgnList.Add("text3",3)
Call MsgBoxDisp("Left Limits: " & LimitsAsText(oMyAssgnList.BoundaryLimitsLeft) & vbCrLf & _
   "Right Limits: " & LimitsAsText(oMyAssgnList.BoundaryLimitsRight))

' Function to convert Boundary Limits from enum into text
Function LimitsAsText(eMyType)
 Select Case eMyType
  Case BoundsOpen
   LimitsAsText = "BoundsOpen"
  Case BoundsClose
   LimitsAsText = "BoundsClose"
 End Select
End Function
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value", dd.DataTypeChnFloat64, 1) 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.SetBoundaryLimits(dd.BoundsOpen, dd.BoundsClose) 
oMyAssgnList.Add("text1",1) 
oMyAssgnList.Add("text2",2) 
oMyAssgnList.Add("text3",3) 
dd.MsgBoxDisp("Left Limits: " + LimitsAsText(oMyAssgnList.BoundaryLimitsLeft) + "\r\n" + "Right Limits: " + LimitsAsText(oMyAssgnList.BoundaryLimitsRight)) 
# Function to convert Boundary Limits from enum into text
def LimitsAsText(eMyType): 
    select_variable_0 = eMyType 
    if (select_variable_0 == dd.BoundsOpen) : 
        LimitsAsText = "BoundsOpen" 
    elif (select_variable_0 == dd.BoundsClose) : 
        LimitsAsText = "BoundsClose" 
    return LimitsAsText
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_custompropertytemplate_idatasettings.htm language=enus -->
## TOPIC 01341: Property: CustomPropertyTemplate for Settings

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_custompropertytemplate_idatasettings.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_custompropertytemplate_idatasettings.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: CustomPropertyTemplate for Settings

Property: CustomPropertyTemplate for Settings

Specifies a [custom properties template](../../dlgshell/dlgshell/dlg_custproptemplate_dialog.htm) in the script interface for internal data.

```text
Set oCustomPropertyTemplate = Object.CustomPropertyTemplate
```

| Object | SettingsObject with this property |
| --- | --- |
| oCustomPropertyTemplate | CustomPropertyTemplateReturned object |

The following example generates a new template for custom properties of channels:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyPropTemplate
Set oMyPropTemplate = Data.Settings.CustomPropertyTemplate
Call oMyPropTemplate.ChannelProperties.Add("MyChnProp", 2)
```

[Copy script](javascript:void(0);)

```text
oMyPropTemplate = dd.Data.Settings.CustomPropertyTemplate 
oMyPropTemplate.ChannelProperties.Add("MyChnProp", 2) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_datastoreelements_idropinformation.htm language=enus -->
## TOPIC 01342: Property: DataStoreElements for DropInformation

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_datastoreelements_idropinformation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_datastoreelements_idropinformation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: DataStoreElements for DropInformation

Property: DataStoreElements for DropInformation

Specifies the data elements from a data store which you drag and drop onto an [XTable](../../sudref/objects/sud_objects_tovirtgridctrl.htm). For example, the data elements can be search results or selected elements.

```text
Set oFreeElementList = Object.DataStoreElements
```

| Object | DropInformationObject with this property |
| --- | --- |
| oFreeElementList | FreeElementList <DataStore>Returned object |

The following example executes the XTable1_EventDrop event when texts, for example from text processing, or elements from a data storage are dragged onto an XTable. The event outputs the text which you drag onto the XTable. If you drag elements from a data storage onto the XTable, the event displays the number of elements:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub XTable1_EventDrop(ByRef This, Row, Col, DropInformation)
  If DropInformation.IsKindOf(eDropText) Then
    Call Msgbox(DropInformation.Text)
  ElseIf DropInformation.IsKindOf(eDropDataStoreElement) Then
    Call Msgbox(DropInformation.DataStoreElements.Count)
  End If
End Sub

Sub XTable1_EventValGet(ByRef This, Row, Col, ByRef Cell, IsInputCell)
  Cell.Text = ""
End Sub

Sub XTable1_EventDropAllowed(ByRef This, Row, Col, DropInformation, ByRef DropEffect)
 DropEffect = eDropEffectCopy
End Sub
```

[Copy script](javascript:void(0);)

```text
def XTable1_EventDrop(ByRef This, Row, Col, DropInformation): 
    if DropInformation.IsKindOf(dd.eDropText) : 
        print(DropInformation.Text) 
    elif DropInformation.IsKindOf(dd.eDropDataStoreElement) : 
        print(DropInformation.DataStoreElements.Count) 
def XTable1_EventValGet(ByRef This, Row, Col, ByRef Cell, IsInputCell): 
    Cell.Text = "" 
def XTable1_EventDropAllowed(ByRef This, Row, Col, DropInformation, ByRef DropEffect): 
    DropEffect = eDropEffectCopy 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_datatype_idiademabstractchannel.htm language=enus -->
## TOPIC 01343: Property: DataType for BaseChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_datatype_idiademabstractchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_datatype_idiademabstractchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: DataType for BaseChannel <Data>

Property: DataType for BaseChannel <Data>

Returns the data type of a channel in the script interface for internal data.

```text
Object.DataType
```

| Object | BaseChannel <Data>Object with this property |  |
| --- | --- | --- |
| Object.DataType | Enumeration with read access and the following selection terms: 10DataTypeChnFloat64 Numerical values 23DataTypeChnString Text 30DataTypeChnDate Time value |  |
| 10 | DataTypeChnFloat64 | Numerical values |
| 23 | DataTypeChnString | Text |
| 30 | DataTypeChnDate | Time value |

The following example displays the data type of the first channel from the first channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn
Set oMyChn = Data.Root.ChannelGroups(1).Channels(1)
Call MsgBoxDisp ("Channel name: " & oMyChn.Name & VBCrLf & _
"Data type: " & ChannelDataTypeAsText(oMyChn.DataType) )

' Function to convert data type from integer into text ===
Function ChannelDataTypeAsText(eMyType)
 Select Case eMyType
  Case DataTypeFloat64
   ChannelDatatypeAsText = "Float64"
  Case DataTypeString
   ChannelDatatypeAsText = "String"
  Case DataTypeDate
   ChannelDatatypeAsText = "Date"
 End Select
End Function 'ChannelDataTypeAsText(eMyType)
```

[Copy script](javascript:void(0);)

```text
oMyChn = dd.Data.Root.ChannelGroups(1).Channels(1) 
dd.MsgBoxDisp ("Channel name: " + oMyChn.Name + "\r\n" + "Data type: " + ChannelDataTypeAsText(oMyChn.DataType) ) 
# Function to convert data type from integer into text ===
def ChannelDataTypeAsText(eMyType): 
    select_variable_0 = eMyType 
    if (select_variable_0 == dd.DataTypeFloat64) : 
        ChannelDatatypeAsText = "Float64" 
    elif (select_variable_0 == dd.DataTypeString) : 
        ChannelDatatypeAsText = "String" 
    elif (select_variable_0 == dd.DataTypeDate) : 
        ChannelDatatypeAsText = "Date" 
    return ChannelDataTypeAsText
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_datatype_idiademassignmentchannel.htm language=enus -->
## TOPIC 01344: Property: DataType for AssignmentChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_datatype_idiademassignmentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_datatype_idiademassignmentchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: DataType for AssignmentChannel <Data>

Property: DataType for AssignmentChannel <Data>

Specifies the data type of an assignment channel in the script interface for internal data.

```text
Object.DataType
```

| Object | AssignmentChannel <Data>Object with this property |  |
| --- | --- | --- |
| Object.DataType | Enumeration with read access and the following selection terms: 10 DataTypeFloat64 64-bit real values 23 DataTypeString Text 30 DataTypeDate Time values |  |
| 10 | DataTypeFloat64 | 64-bit real values |
| 23 | DataTypeString | Text |
| 30 | DataTypeDate | Time values |

The following example generates an assignment channel and displays the data type:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyChnList
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Call MsgBoxDisp(ChannelDataTypeAsText(oMyChn.DataType))

'Function to convert data type from integer into text
Function ChannelDataTypeAsText(eMyType)
 Select Case eMyType
  Case DataTypeFloat64
   ChannelDatatypeAsText = "Float64"
  Case DataTypeString
   ChannelDatatypeAsText = "String"
  Case DataTypeDate
   ChannelDatatypeAsText = "Date"
 End Select
End Function
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
dd.MsgBoxDisp(ChannelDataTypeAsText(oMyChn.DataType)) 
#Function to convert data type from integer into text
def ChannelDataTypeAsText(eMyType): 
    select_variable_0 = eMyType 
    if (select_variable_0 == dd.DataTypeFloat64) : 
        ChannelDatatypeAsText = "Float64" 
    elif (select_variable_0 == dd.DataTypeString) : 
        ChannelDatatypeAsText = "String" 
    elif (select_variable_0 == dd.DataTypeDate) : 
        ChannelDatatypeAsText = "Date" 
    return ChannelDataTypeAsText
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_datatype_idiademcalculationchannel.htm language=enus -->
## TOPIC 01345: Property: DataType for CalculationChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_datatype_idiademcalculationchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_datatype_idiademcalculationchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: DataType for CalculationChannel <Data>

Property: DataType for CalculationChannel <Data>

Specifies the file type of a calculation channel in the script interface for internal data.

```text
Object.DataType
```

| Object | CalculationChannel <Data>Object with this property |  |
| --- | --- | --- |
| Object.DataType | Enumeration with read access and the following selection terms: 10DataTypeChnFloat64 64-bit real values 23DataTypeChnString Text 30DataTypeChnDate Time values |  |
| 10 | DataTypeChnFloat64 | 64-bit real values |
| 23 | DataTypeChnString | Text |
| 30 | DataTypeChnDate | Time values |

The following example generates a calculation channel from a formula with the unit “m/s” and displays the data type:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalculationChn
Set oMyCalculationChn = Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1)
Call MsgBox(ChannelDataTypeAsText(oMyCalculationChn.DataType))

'Function to convert data type from integer into text
Function ChannelDataTypeAsText(eMyType)
 Select Case eMyType
  Case DataTypeFloat64
   ChannelDatatypeAsText = "Float64"
  Case DataTypeString
   ChannelDatatypeAsText = "String"
  Case DataTypeDate
   ChannelDatatypeAsText = "Date"
 End Select
End Function
```

[Copy script](javascript:void(0);)

```text
oMyCalculationChn = dd.Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1) 
print(ChannelDataTypeAsText(oMyCalculationChn.DataType)) 
#Function to convert data type from integer into text
def ChannelDataTypeAsText(eMyType): 
    select_variable_0 = eMyType 
    if (select_variable_0 == dd.DataTypeFloat64) : 
        ChannelDatatypeAsText = "Float64" 
    elif (select_variable_0 == dd.DataTypeString) : 
        ChannelDatatypeAsText = "String" 
    elif (select_variable_0 == dd.DataTypeDate) : 
        ChannelDatatypeAsText = "Date" 
    return ChannelDataTypeAsText
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_dvalues_idiademassignmentchannel.htm language=enus -->
## TOPIC 01346: Property: dValues for AssignmentChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_dvalues_idiademassignmentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_dvalues_idiademassignmentchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: dValues for AssignmentChannel <Data>

Property: dValues for AssignmentChannel <Data>

Specifies the single value of an assignment channel at a specific channel position as a Double vector type in the script interface for internal data.

```text
Object.dValues(Index)
```

| Object | AssignmentChannel <Data>Object with this property |
| --- | --- |
| Index | LongIntegerSpecifies the channel position. If you write values into a channel and the index is higher than the current channel length, DIAdem automatically adjusts the channel length. |
| Object.dValues | Variant with read and write access |

|  | Note Use the dvalues property to specify and output the numeric values of an assignment channel. Use the read-only property values to output a text assigned to an assignment channel. |
| --- | --- |

The following example generates an assignment channel with the values 1 to 20 and with three assignments, and displays the third and fourth text:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn, oMyGrp, oMyAssgnList, I
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",1)
Call oMyAssgnList.Add("text2",2)
Call oMyAssgnList.Add("text3",3)
For I = 1 to 20 
  oMyChn.dValues(I) = I
Next
Call MsgBoxDisp("Numeric value: " & oMyChn.dValues(1) & vbCrLf & "Assigned text: " & oMyChn.Values(1))
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",1) 
oMyAssgnList.Add("text2",2) 
oMyAssgnList.Add("text3",3) 
for I in range( 1, 20 + 1): 
    oMyChn.dValues[I] = I 
dd.MsgBoxDisp("Numeric value: " + oMyChn.dValues(1) + "\r\n" + "Assigned text: " + oMyChn.Values(1)) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_element_idiademproperty.htm language=enus -->
## TOPIC 01347: Property: Element for Property <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_element_idiademproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_element_idiademproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Element for Property <Data>

Property: Element for Property <Data>

Specifies in the script interface for internal data the element to which a property belongs. The element might be a [root](../objects/diacmpnt_objects_idiademroot.htm) type, a [channel group](../objects/diacmpnt_objects_idiademchannelgroup.htm) type, or a [channel](../objects/diacmpnt_objects_idiademchannel.htm) type.

```text
Set oElement = Object.Element
```

| Object | Property <Data>Object with this property |
| --- | --- |
| oElement | Element <Data>Returned object |

The following example displays the name of the element to which the first property of the first channel from the first channel group belongs:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannelProperty
Set oMyChannelProperty = Data.Root.ChannelGroups(1).Channels(1).Properties(2)
Call MsgBoxDisp(oMyChannelProperty.Element.Name)
```

[Copy script](javascript:void(0);)

```text
oMyChannelProperty = dd.Data.Root.ChannelGroups(1).Channels(1).Properties(2) 
dd.MsgBoxDisp(oMyChannelProperty.Element.Name) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_filelist_idropinformation.htm language=enus -->
## TOPIC 01348: Property: FileList for DropInformation

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_filelist_idropinformation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_filelist_idropinformation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: FileList for DropInformation

Property: FileList for DropInformation

Returns in user dialog boxes a collection of all files from a file list which you drag and drop to another object.

```text
Set oFileList = Object.FileList
```

| Object | DropInformationObject with this property |
| --- | --- |
| oFileList | FileList <DropInformation>Returned object |

The following example creates a tree you can drag files to. The tree displays the names of these files as new branches.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub Tree1_EventDropAllowed(ByRef This, DropInformation, ByRef DropEffect) 'Created Event Handler
  If (DropInformation.FileList.Count >0) Then
    DropEffect = eDropEffectCopy
  End If
End Sub

Sub Tree1_EventDrop(ByRef This, DropInformation, ByRef DropEffect, ByRef Node)
  Dim oMyFile, oMyFileList, iCount
  Set oMyFileList = DropInformation.FileList
  If (oMyFileList.Count > 0) Then
    If (Not Node Is Nothing) Then
      For iCount = 1 to oMyFileList.Count
        Call Node.Nodes.Add(oMyFileList(iCount))
      Next
      Node.Expanded = True        
      Call Node.Update(eUpdateModeNodeAndChilds)
    Else
      For iCount = 1 to oMyFileList.Count
        Call This.Nodes.Add(oMyFileList(iCount))
      Next
      Call This.Refresh
    End If
  Else
    DropEffect = eDropEffectNone
  End If
End Sub
```

[Copy script](javascript:void(0);)

```text
def Tree1_EventDropAllowed(ByRef This, DropInformation, ByRef DropEffect): #Created Event Handler
    if (DropInformation.FileList.Count >0) : 
        DropEffect = eDropEffectCopy 
def Tree1_EventDrop(ByRef This, DropInformation, ByRef DropEffect, ByRef Node): 
    oMyFileList = DropInformation.FileList 
    if (oMyFileList.Count > 0) : 
        if (not Node is None) : 
            for iCount in range( 1, oMyFileList.Count + 1): 
                Node.Nodes.Add(oMyFileList(iCount)) 
            Node.Expanded = True 
            Node.Update(dd.eUpdateModeNodeAndChilds) 
        else: 
            for iCount in range( 1, oMyFileList.Count + 1): 
                This.Nodes.Add(oMyFileList(iCount)) 
            This.Refresh() 
    else: 
        DropEffect = eDropEffectNone 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_formula_idiademcalculationchannel.htm language=enus -->
## TOPIC 01349: Property: Formula for CalculationChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_formula_idiademcalculationchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_formula_idiademcalculationchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Formula for CalculationChannel <Data>

Property: Formula for CalculationChannel <Data>

Specifies the formula of a calculation channel in the script interface for internal data.

```text
Object.Formula
```

| Object | CalculationChannel <Data>Object with this property |
| --- | --- |
| Object.Formula | String with read and write accessSpecifies the formula. If it is not a simple formula but a Calculation Manager calculation, the property returns an empty string.Within a formula, you can use channels of the target group, constants, numbers, and variables that reference values and channels. The channel names must not contain spaces, various special characters, or reserved DIAdem or VBS names, for example, Time, because otherwise DIAdem will use the reserved DIAdem or VBS name instead of the formula. Use CH to access these channels, for example, CH("Time"). If DIAdem cannot calculate the formula of an existing formula channel because, for example, an input channel is missing, DIAdem deletes all values and the unit of the formula channel when you update the values of this channel. If the functionality of the formula channel is not sufficient for your task, use the AddCalculationChannelRef method to use a calculation from the Calculation Manager. |

The following example displays the formula of a calculation channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalculationChn
Set oMyCalculationChn = Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1)
Call Msgbox("Formula: " & oMyCalculationChn.Formula)
```

[Copy script](javascript:void(0);)

```text
oMyCalculationChn = dd.Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1) 
print("Formula: " + oMyCalculationChn.Formula) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_hidden_idiademproperty.htm language=enus -->
## TOPIC 01350: Property: Hidden for Property <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_hidden_idiademproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_hidden_idiademproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Hidden for Property <Data>

Property: Hidden for Property <Data>

Specifies in the script interface for internal data, whether DIAdem displays the [property](../../genshell/genshell/genshell_dd_properties.htm) of a data element in the user interface. In DIAdem you can hide only the register properties. However, the properties are maintained in the associated collections.

```text
Object.Hidden
```

| Object | Property <Data>Object with this property |
| --- | --- |
| Object.Hidden | Boolean value with read access |

|  | Note DIAdem hides the register properties by default. |
| --- | --- |

The following example displays whether DIAdem hides the property RegisterInt1 of the first channel of the default channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp (Data.Root.ActiveChannelGroup.Channels(1).Properties("RegisterInt1").Hidden)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp (dd.Data.Root.ActiveChannelGroup.Channels(1).Properties("RegisterInt1").Hidden) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_increment_idiademimplicitchannel.htm language=enus -->
## TOPIC 01351: Property: Increment for ImplicitChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_increment_idiademimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_increment_idiademimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Increment for ImplicitChannel <Data>

Property: Increment for ImplicitChannel <Data>

Specifies the step width of the values of an implicit channel in the script interface for internal data.

```text
Object.Increment
```

| Object | ImplicitChannel <Data>Object with this property |
| --- | --- |
| Object.Increment | Variant with read and write access |

The following example displays the names and the step width of the values of an implicit channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn
Set oMyChn = Data.Root.ActiveChannelGroup.Channels(1)
If (oMyChn.IsKindOf(eDataImplicitChannel)) Then
  Call MsgBoxDisp("Channel name: " & oMyChn.Name & VBCrLf & "Increment: " & oMyChn.Increment)
Else 
  Call MsgBoxDisp("No implicit channel")
End If
```

[Copy script](javascript:void(0);)

```text
oMyChn = dd.Data.Root.ActiveChannelGroup.Channels(1) 
if (oMyChn.IsKindOf(dd.eDataImplicitChannel)) : 
    dd.MsgBoxDisp("Channel name: " + oMyChn.Name + "\r\n" + "Increment: " + oMyChn.Increment) 
else: 
    dd.MsgBoxDisp("No implicit channel") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_isactive_idiademchannelgroup.htm language=enus -->
## TOPIC 01352: Property: IsActive for ChannelGroup <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_isactive_idiademchannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_isactive_idiademchannelgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: IsActive for ChannelGroup <Data>

Property: IsActive for ChannelGroup <Data>

Specifies whether a channel group is the default group in the script interface for internal data.

```text
Object.IsActive
```

| Object | ChannelGroup <Data>Object with this property |
| --- | --- |
| Object.IsActive | Boolean value with read access |

The following example displays whether the first channel group In the Data Portal is the default channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBox(Data.Root.ChannelGroups(1).IsActive)
```

[Copy script](javascript:void(0);)

```text
print(dd.Data.Root.ChannelGroups(1).IsActive) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_isreadonly_idiademabstractchannel.htm language=enus -->
## TOPIC 01353: Property: IsReadOnly for BaseChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_isreadonly_idiademabstractchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_isreadonly_idiademabstractchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: IsReadOnly for BaseChannel <Data>

Property: IsReadOnly for BaseChannel <Data>

Specifies whether a channel is read-only.

```text
Object.IsReadOnly
```

| Object | BaseChannel <Data>Object with this property |
| --- | --- |
| Object.IsReadOnly | Boolean value with read accessThe value is TRUE if the channel is read-only. |

The following example displays whether the first channel of the default group is read-only:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel
Set oMyChannel = Data.Root.ActiveChannelGroup.Channels(1)
Call MsgBoxDisp(oMyChannel.IsReadOnly)
```

[Copy script](javascript:void(0);)

```text
oMyChannel = dd.Data.Root.ActiveChannelGroup.Channels(1) 
dd.MsgBoxDisp(oMyChannel.IsReadOnly) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_isreadonly_idiademassignmentchannel.htm language=enus -->
## TOPIC 01354: Property: IsReadOnly for AssignmentChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_isreadonly_idiademassignmentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_isreadonly_idiademassignmentchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: IsReadOnly for AssignmentChannel <Data>

Property: IsReadOnly for AssignmentChannel <Data>

Specifies whether an assignment channel is read-only.

```text
Object.IsReadOnly
```

| Object | AssignmentChannel <Data>Object with this property |
| --- | --- |
| Object.IsReadOnly | Boolean value with read access |

The following example displays whether the assignment channel is read-only:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn
Call Data.Root.Clear()
Call DataFileLoad(ProgramDrv & "Examples\Data\Report_expl.tdm")
Set oMyChn = Data.GetChannel("[6]/[4]")
Call MsgBoxDisp(oMyChn.IsReadOnly)
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.ProgramDrv + "Examples\\Data\\Report_expl.tdm") 
oMyChn = dd.Data.GetChannel("[6]/[4]") 
dd.MsgBoxDisp(oMyChn.IsReadOnly) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_isreadonly_idiademcalculationchannel.htm language=enus -->
## TOPIC 01355: Property: IsReadOnly for CalculationChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_isreadonly_idiademcalculationchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_isreadonly_idiademcalculationchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: IsReadOnly for CalculationChannel <Data>

Property: IsReadOnly for CalculationChannel <Data>

Specifies whether a calculation channel is read-only in the script interface for internal data.

```text
Object.IsReadOnly
```

| Object | CalculationChannel <Data>Object with this property |
| --- | --- |
| Object.IsReadOnly | Boolean value with read access |

The following example generates a calculation channel from a formula with the unit “m/s” and displays whether this calculation channel is read-only:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalculationChn
Set oMyCalculationChn = Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1)
Call MsgBox(oMyCalculationChn.IsReadOnly)
```

[Copy script](javascript:void(0);)

```text
oMyCalculationChn = dd.Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1) 
print(oMyCalculationChn.IsReadOnly) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_minimum_idiademabstractchannel.htm language=enus -->
## TOPIC 01356: Property: Minimum for BaseChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_minimum_idiademabstractchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_minimum_idiademabstractchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Minimum for BaseChannel <Data>

Property: Minimum for BaseChannel <Data>

Specifies the minimum value of a channel. The value of the Minimum property for Channel corresponds to the value of *Object*.Properties("minimum").value.

```text
Object.Minimum
```

| Object | BaseChannel <Data>Object with this property |
| --- | --- |
| Object.Minimum | Variant with read access |

The following example displays the minimum value of the first channel in the default group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel
Set oMyChannel = Data.Root.ActiveChannelGroup.Channels(1)
Call MsgBoxDisp(oMyChannel.Minimum)  ' is equivalent to oMyChannel.Properties("minimum").Value
```

[Copy script](javascript:void(0);)

```text
oMyChannel = dd.Data.Root.ActiveChannelGroup.Channels(1) 
dd.MsgBoxDisp(oMyChannel.Minimum) # is equivalent to oMyChannel.Properties("minimum").Value
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_minimum_idiademassignmentchannel.htm language=enus -->
## TOPIC 01357: Property: Minimum for AssignmentChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_minimum_idiademassignmentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_minimum_idiademassignmentchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Minimum for AssignmentChannel <Data>

Property: Minimum for AssignmentChannel <Data>

Specifies the minimum value of an assignment channel. The value of the Minimum property for AssignmentChannel corresponds to the value of *Object*.Properties("minimum").value.

```text
Object.Minimum
```

| Object | AssignmentChannel <Data>Object with this property |
| --- | --- |
| Object.Minimum | Variant with read access |

The following example displays the minimum value of an assignment channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn
Call Data.Root.Clear()
Call DataFileLoad(ProgramDrv & "Examples\Data\Report_expl.tdm")
Set oMyChn = Data.GetChannel("[6]/[4]")
Call MsgBoxDisp(oMyChn.Minimum) ' equivalent to oMyChannel.Properties("minimum").value
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.ProgramDrv + "Examples\\Data\\Report_expl.tdm") 
oMyChn = dd.Data.GetChannel("[6]/[4]") 
dd.MsgBoxDisp(oMyChn.Minimum) # equivalent to oMyChannel.Properties("minimum").value
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_minimum_idiademcalculationchannel.htm language=enus -->
## TOPIC 01358: Property: Minimum for CalculationChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_minimum_idiademcalculationchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_minimum_idiademcalculationchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Minimum for CalculationChannel <Data>

Property: Minimum for CalculationChannel <Data>

Specifies the maximum of a calculation channel in the script interface for internal data. The value of the Minimum property for CalculationChannel is the same as the value of [Value for Property <Data>](../properties/diacmpnt_property_value_idiademproperty.htm) with the property value minimum.

```text
Object.Minimum
```

| Object | CalculationChannel <Data>Object with this property |
| --- | --- |
| Object.Minimum | Variant with read access |

The following example generates a calculation channel from a formula with the unit “m/s” and displays the minimum of this calculation channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalculationChn
Set oMyCalculationChn = Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1)
Call MsgBox(oMyCalculationChn.Minimum)
```

[Copy script](javascript:void(0);)

```text
oMyCalculationChn = dd.Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1) 
print(oMyCalculationChn.Minimum) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_minimum_idiademchannel.htm language=enus -->
## TOPIC 01359: Property: Minimum for Channel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_minimum_idiademchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_minimum_idiademchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Minimum for Channel <Data>

Property: Minimum for Channel <Data>

Specifies the minimum value of a channel. The value of the Minimum property for Channel corresponds to the value of *Object*.Properties("minimum").value.

```text
Object.Minimum
```

| Object | Channel <Data>Object with this property |
| --- | --- |
| Object.Minimum | Variant with read access |

The following example displays the minimum value of the first channel in the default group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel
Set oMyChannel = Data.Root.ActiveChannelGroup.Channels(1)
Call MsgBoxDisp(oMyChannel.Minimum)  ' is equivalent to oMyChannel.Properties("minimum").Value
```

[Copy script](javascript:void(0);)

```text
oMyChannel = dd.Data.Root.ActiveChannelGroup.Channels(1) 
dd.MsgBoxDisp(oMyChannel.Minimum) # is equivalent to oMyChannel.Properties("minimum").Value
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_minimum_idiademcomplexchannel.htm language=enus -->
## TOPIC 01360: Property: Minimum for ComplexChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_minimum_idiademcomplexchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_minimum_idiademcomplexchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Minimum for ComplexChannel <Data>

Property: Minimum for ComplexChannel <Data>

Specifies the minimum value of a [complex channel](../../genshell/genshell/genshell_channeltypes.htm). The value of the Minimum property for ComplexChannel corresponds to the value of *Object*.Properties("minimum").value.

```text
Object.Minimum
```

| Object | ComplexChannel <Data>Object with this property |
| --- | --- |
| Object.Minimum | Variant with read access |

The following example displays the minimum value of the first channel in the default group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChannel
Set oMyChannel = Data.Root.ActiveChannelGroup.Channels(1)
Call MsgBoxDisp(oMyChannel.Minimum)  ' is equivalent to oMyChannel.Properties("minimum").Value
```

[Copy script](javascript:void(0);)

```text
oMyChannel = dd.Data.Root.ActiveChannelGroup.Channels(1) 
dd.MsgBoxDisp(oMyChannel.Minimum) # is equivalent to oMyChannel.Properties("minimum").Value
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_minimum_idiademimplicitchannel.htm language=enus -->
## TOPIC 01361: Property: Minimum for ImplicitChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_minimum_idiademimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_minimum_idiademimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Minimum for ImplicitChannel <Data>

Property: Minimum for ImplicitChannel <Data>

Specifies the minimum value of an implicit channel. The value of the Minimum property for ImplicitChannel corresponds to the value of *Object*.Properties("minimum").value.

```text
Object.Minimum
```

| Object | ImplicitChannel <Data>Object with this property |
| --- | --- |
| Object.Minimum | Variant with read access |

The following example generates an implicit channel and displays the minimum value:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyImplChannel
Set oMyImplChannel = Data.Root.ActiveChannelGroup.Channels.AddImplicitChannel("MyImplChn", 1, 1, 100,DataTypeFloat64)
Call MsgBoxDisp(oMyImplChannel.Minimum) ' equivalent to oMyImplChannel.Properties("minimum").Value
```

[Copy script](javascript:void(0);)

```text
oMyImplChannel = dd.Data.Root.ActiveChannelGroup.Channels.AddImplicitChannel("MyImplChn", 1, 1, 100,dd.DataTypeFloat64) 
dd.MsgBoxDisp(oMyImplChannel.Minimum) # equivalent to oMyImplChannel.Properties("minimum").Value
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_name_idiademabstractchannel.htm language=enus -->
## TOPIC 01362: Property: Name for BaseChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_name_idiademabstractchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_name_idiademabstractchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Name for BaseChannel <Data>

Property: Name for BaseChannel <Data>

Receives the name of a BaseChannel object in the script interface for internal data.

```text
Object.Name
```

| Object | BaseChannel <Data>Object with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example changes the name of the first channel of the first channel group in Temp:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Data.Root.ChannelGroups(1).Channels(1).Name = "Temp"
```

[Copy script](javascript:void(0);)

```text
Data.Root.ChannelGroups(1).Channels(1).Name = "Temp" 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_name_idiademassignmentchannel.htm language=enus -->
## TOPIC 01363: Property: Name for AssignmentChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_name_idiademassignmentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_name_idiademassignmentchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Name for AssignmentChannel <Data>

Property: Name for AssignmentChannel <Data>

Specifies the name of an assignment channel in the script interface for internal data.

```text
Object.Name
```

| Object | AssignmentChannel <Data>Object with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example generates an assignment channel and displays the name:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyChn, oMyGrp
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Call MsgBoxDisp(oMyChn.Name)
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
dd.MsgBoxDisp(oMyChn.Name) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_name_idiademcalculationchannel.htm language=enus -->
## TOPIC 01364: Property: Name for CalculationChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_name_idiademcalculationchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_name_idiademcalculationchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Name for CalculationChannel <Data>

Property: Name for CalculationChannel <Data>

Specifies the name of a calculation channel in the script interface for internal data. The value of the Name property for CalculationChannel is the same as the value of [Value for Property <Data>](../properties/diacmpnt_property_value_idiademproperty.htm) with the property value name.

```text
Object.Name
```

| Object | CalculationChannel <Data>Object with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example generates a calculation channel from a formula with the unit “m/s” and displays the name of this calculation channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalculationChn
Set oMyCalculationChn = Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1)
Call MsgBox(oMyCalculationChn.Name)
```

[Copy script](javascript:void(0);)

```text
oMyCalculationChn = dd.Data.Root.ChannelGroups(1).Channels.AddCalculationChannel("Result", "=Speed * 2", "m/s", 1) 
print(oMyCalculationChn.Name) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_name_idiademchannelgroup.htm language=enus -->
## TOPIC 01365: Property: Name for ChannelGroup <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_name_idiademchannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_name_idiademchannelgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Name for ChannelGroup <Data>

Property: Name for ChannelGroup <Data>

Receives the name of a ChannelGroup object in the script interface for internal data.

```text
Object.Name
```

| Object | ChannelGroup <Data>Object with this property |
| --- | --- |
| Object.Name | String with read and write accessReceives the name of the channel group. |

|  | Note The name must conform to the DIAdem conventions. If the name does not conform to the name conventions, DIAdem corrects the name. |
| --- | --- |

The following example changes the name of the first channel group in Temp:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Data.Root.ChannelGroups(1).Name = "Temp"
```

[Copy script](javascript:void(0);)

```text
Data.Root.ChannelGroups(1).Name = "Temp" 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_value_iassignment.htm language=enus -->
## TOPIC 01366: Property: Value for Assignment <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_value_iassignment.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_value_iassignment.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Value for Assignment <Data>

Property: Value for Assignment <Data>

Specifies the text value of an assignment in an assignment channel in the script interface for internal data. A text value (property Value) is assigned to a numeric value (property [Definition](../properties/diacmpnt_property_definitionrange_iassignment.htm)) or to a value range (property DefinitionRange) in order to define an assignment.

```text
Object.Value
```

| Object | Assignment <Data>Object with this property |
| --- | --- |
| Object.Value | String with read and write access |

The following example generates an assignment channel with three assignments and displays the values and the associated texts:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList, Assignment
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",1)
Call oMyAssgnList.Add("text2",2)
Call oMyAssgnList.Add("text3",3)
For Each Assignment in oMyAssgnList
  Call MsgBoxDisp("Definition Value: " & Assignment.Definition & vbCrLf & "Text: " & Assignment.Value)
Next
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",1) 
oMyAssgnList.Add("text2",2) 
oMyAssgnList.Add("text3",3) 
for Assignment in oMyAssgnList: 
    dd.MsgBoxDisp("Definition Value: " + Assignment.Definition + "\r\n" + "Text: " + Assignment.Value) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_value_idiademproperty.htm language=enus -->
## TOPIC 01367: Property: Value for Property <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_value_idiademproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_value_idiademproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Value for Property <Data>

Property: Value for Property <Data>

Specifies the value of a [property](../../genshell/genshell/genshell_dd_properties.htm) in the script interface for internal data.

```text
Object.Value
```

| Object | Property <Data>Object with this property |
| --- | --- |
| Object.Value | Variant with read and write accessVariant type String, Integer, Float, or Time with read and write access. |

|  | Note You can use the Navigator-API to assign time values to a DIAdem time property as a VariantDate object or as a UsiTimeDisp object. |
| --- | --- |

|  | Note When working with date values, pay attention to the following characteristics:The Value property returns a VBDate data type value. This data type has a valid range from 01/01/100 to 31/12/9999 23:59:59. On 30/12/1899 you can only use time information but no date information. If you convert VBDate type values that contain only time information into the USITimeDisp format, the program automatically adds the 01/01/0000 date information. The VBDate type Value property contains a maximum of 4 decimal places. If you convert VBDate type values into the DIAdem time format, the program adds the date information in relation to the variable ApplicationTimebaseHighResolution. Use the oValue property instead of the Valueproperty if you are working with time values that lie within the range between January 1 of year zero and 01/01/100, or concern December 30, 1899. The oValue property returns time values as USITimeDisp object in the USITimeDisp format. The USITimeDisp object is valid from 01/01 of the year zero to 12/31/9999 23:59:59. |
| --- | --- |

|  | Note You cannot assign NoValues to date/time type properties. You can only assign NoValues to channel values that are double types. |
| --- | --- |

The following example displays the name and the value for each property of the data set:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyProp
For Each oMyProp in Data.Root.Properties
  Call MsgBoxDisp (oMyProp.Name & ": " & oMyProp.Value)
Next
```

[Copy script](javascript:void(0);)

```text
for oMyProp in dd.Data.Root.Properties: 
    dd.MsgBoxDisp (oMyProp.Name +": " + oMyProp.Value) 
```

The following example determines the time values of the datetime root property of the TDM file indexed and focused in the file browser. Then the date/time value is assigned first as a VariantDate and then as a UsiTimeDisp object.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDateTime
Set oMyDateTime = Navigator.Display.CurrDataFinder.Browser.FocusedElement.Properties("DateTime").Value
Data.Root.Properties("DateTime").Value = oMyDateTime
Call MsgBox(Data.Root.Properties("DateTime").Value)
```

[Copy script](javascript:void(0);)

```text
oMyDateTime = dd.Navigator.Display.CurrDataFinder.Browser.FocusedElement.Properties("DateTime").Value 
Data.Root.Properties("DateTime").Value = oMyDateTime 
print(dd.Data.Root.Properties("DateTime").Value) 
```

The following example shows the difference between the use of time values of the VBDate type and the USITimeDisp type:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDateTime
Set oMyDateTime = createTime(2000, 05, 15, 12, 13, 14, 15, 16, 17)

Data.Root.Properties("DateTime").Value = oMyDateTime.VariantDate
Call MsgBox("DateTime (vbDate)= "&vbcrlf& _
     Data.Root.Properties("DateTime").Value)

Call Data.Root.Properties.Add("DateTime_Obj", oMyDateTime, DataTypeDate)
Dim oDate
Set oDate = Data.Root.Properties("DateTime_Obj").oValue
Call MsgBox("DateTime_Obj (UsiTimeDisp) = "&vbcrlf& _
     oDate.day &"."& oDate.Month &"."& oDate.Year &" "& oDate.Hour &":"& _
     oDate.Minute&":"& oDate.Second &"  "& oDate.Millisecond&" [ms]  " _
     & oDate.Microsecond &" [µs]  "& oDate.nanosecond &" [ns]")
```

[Copy script](javascript:void(0);)

```text
oMyDateTime = dd.createTime(2000, 05, 15, 12, 13, 14, 15, 16, 17) 
Data.Root.Properties("DateTime").Value = oMyDateTime.VariantDate 
print("DateTime (vbDate)= "+"\r\n"+ dd.Data.Root.Properties("DateTime").Value) 
dd.Data.Root.Properties.Add("DateTime_Obj", oMyDateTime, dd.DataTypeDate) 
oDate = dd.Data.Root.Properties("DateTime_Obj").oValue 
print("DateTime_Obj (UsiTimeDisp) = "+"\r\n"+ oDate.day +"."+ oDate.Month +"."+ oDate.Year +" "+ oDate.Hour +":"+ oDate.Minute+":"+ oDate.Second +"  "+ oDate.Millisecond+" [ms]  " + oDate.Microsecond +" [+micro;s]  "+ oDate.nanosecond +" [ns]") 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_value_itemplateproperty.htm language=enus -->
## TOPIC 01368: Property: Value for TemplateProperty

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_value_itemplateproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_value_itemplateproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Value for TemplateProperty

Property: Value for TemplateProperty

Specifies the initial value of a custom property from the [custom properties template](../../dlgshell/dlgshell/dlg_custproptemplate_dialog.htm), in the script interface for internal data.

```text
Object.Value
```

| Object | TemplatePropertyObject with this property |
| --- | --- |
| Object.Value | Variant with read and write accessThe variant can be a string type, an integer type, a float type, or a time type. |

The following example generates a new custom properties template for channels, creates a new channel, and displays the value of the custom properties template of the channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyProp
Set oMyProp = Data.Settings.CustomPropertyTemplate.ChannelProperties.Add("MyChnPropTemplate","",DataTypeString)
oMyProp.Value = "test"
Call Data.Root.ActiveChannelGroup.Channels.Add("MyChn",DataTypeString)
Call MsgBoxDisp (Data.Root.ActiveChannelGroup.Channels("MyChn").Properties("MyChnPropTemplate").Value)
```

[Copy script](javascript:void(0);)

```text
oMyProp = dd.Data.Settings.CustomPropertyTemplate.ChannelProperties.Add("MyChnPropTemplate","",dd.DataTypeString) 
oMyProp.Value = "test" 
dd.Data.Root.ActiveChannelGroup.Channels.Add("MyChn",dd.DataTypeString) 
dd.MsgBoxDisp (dd.Data.Root.ActiveChannelGroup.Channels("MyChn").Properties("MyChnPropTemplate").Value) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=inavidata/properties/diacmpnt_property_values_idiademassignmentchannel.htm language=enus -->
## TOPIC 01369: Property: Values for AssignmentChannel <Data>

- bundle_id: `diadem`
- source_path: `inavidata/properties/diacmpnt_property_values_idiademassignmentchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/inavidata/properties/diacmpnt_property_values_idiademassignmentchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Internal Data](../scriptdata_overview.htm) > [Properties](../properties/inavidata_property_overview.htm) > Property: Values for AssignmentChannel <Data>

Property: Values for AssignmentChannel <Data>

Specifies the single value of an assignment channel at a specific channel position in the script interface for internal data. You can only read the Values property.

```text
Object.Values(Index)
```

| Object | AssignmentChannel <Data>Object with this property |
| --- | --- |
| Index | LongIntegerSpecifies the position of the value in the channel. |
| Object.Values | Variant with read access |

|  | Note Use the dValues property to specify and output the numeric values of an assignment channel. The Values property returns the text value of an assignment. |
| --- | --- |

The following example generates an assignment channel with the values 1 to 20 and with three assignments, and displays the third and fourth text:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyGrp, oMyChn, oMyAssgnList, I
Set oMyGrp = Data.Root.ChannelGroups(1)
Set oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value")
Set oMyAssgnList = oMyChn.AssignmentList
Call oMyAssgnList.Add("text1",1)
Call oMyAssgnList.Add("text2",2)
Call oMyAssgnList.Add("text3",3)
For I = 1 to 20 
  oMyChn.dValues(I) = I
Next
Call MsgBoxDisp("Third channel value: " & oMyChn.Values(3) &vbCrLf & "Fourth channel value: " & oMyChn.Values(4))
```

[Copy script](javascript:void(0);)

```text
oMyGrp = dd.Data.Root.ChannelGroups(1) 
oMyChn = oMyGrp.Channels.AddAssignmentChannel("MyAssignmentChn","Default Value") 
oMyAssgnList = oMyChn.AssignmentList 
oMyAssgnList.Add("text1",1) 
oMyAssgnList.Add("text2",2) 
oMyAssgnList.Add("text3",3) 
for I in range( 1, 20 + 1): 
    oMyChn.dValues[I] = I 
dd.MsgBoxDisp("Third channel value: " + oMyChn.Values(3) +"\r\n" + "Fourth channel value: " + oMyChn.Values(4)) 
```

#### See Also

[Objects Overview](../objects/inavidata_objects_overview.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm) | [Sorting Channel Groups](../../exploff/examples/sortchannelgroups.htm) | [Sorting the Channels in the Default-Group](../../exploff/examples/sortchannels.htm)

<!--NI_TOPIC bundle=diadem path=jsonparser/methods/jsonparser_method_parsedatetime_ijsonparser.htm language=enus -->
## TOPIC 01370: Method: ParseDateTime for JsonParser

- bundle_id: `diadem`
- source_path: `jsonparser/methods/jsonparser_method_parsedatetime_ijsonparser.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/jsonparser/methods/jsonparser_method_parsedatetime_ijsonparser.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: ParseDateTime for JsonParser

Method: ParseDateTime for JsonParser

Converts a date according to ISO 8601 into a variable with the subtype Date.

```text
Set oDispatch = Object.ParseDateTime(String, LocalTime)
```

| Object | JsonParserObject with this method |
| --- | --- |
| String | StringReceives the date according to ISO 8601. |
| LocalTime | BooleanSpecifies whether the method returns the time as local time (TRUE) or as UTC (Coordinated Universal Time) (FALSE). |
| oDispatch | Returned object |

The following example creates a dictionary object from a JSON object, converts the "timestamp" item into a VBS date/time value, and displays the time values in the log area.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, sJsonDateTimeTag, oVbsObject, sVbsDictItem, VbsDate
Set oJsonParser = CreateJsonParser()
sJsonDateTimeTag = "{""timestamp"":""2018-11-27T12:33:27Z""}"
Call oJsonParser.Deserialize(sJsonDateTimeTag, oVbsObject)
sVbsDictItem = oVbsObject("timestamp")
VbsDate = oJsonParser.ParseDateTime(sVbsDictItem,True)
Call LogFileWrite("Local Time: " & CStr(VbsDate))
VbsDate = oJsonParser.ParseDateTime(sVbsDictItem,False)
Call LogFileWrite("UTC Time: " & CStr(VbsDate))
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
sJsonDateTimeTag = "{""timestamp"":""2018-11-27T12:33:27Z""}" 
oJsonParser.Deserialize(sJsonDateTimeTag, oVbsObject) 
sVbsDictItem = oVbsObject("timestamp") 
VbsDate = oJsonParser.ParseDateTime(sVbsDictItem,True) 
dd.LogFileWrite("Local Time: " + str(VbsDate)) 
VbsDate = oJsonParser.ParseDateTime(sVbsDictItem,False) 
dd.LogFileWrite("UTC Time: " + str(VbsDate)) 
```

#### See Also

[Objects Overview](../objects/ijsonparser_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=jsonparser/methods/jsonparser_method_readfile_ijsonparser.htm language=enus -->
## TOPIC 01371: Method: ReadFile for JsonParser

- bundle_id: `diadem`
- source_path: `jsonparser/methods/jsonparser_method_readfile_ijsonparser.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/jsonparser/methods/jsonparser_method_readfile_ijsonparser.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: ReadFile for JsonParser

Method: ReadFile for JsonParser

Reads in a string from a JSON file in UTF-8 format.

```text
sReadFile = Object.ReadFile(Filename)
```

| Object | JsonParserObject with this method |
| --- | --- |
| Filename | StringSpecifies the name and the path of the JSON file. |
| sReadFile | StringContains a JSON string. |

The following example reads a JSON file, converts the JSON string into a dictionary object or an array, and displays the size of the dictionary object or array and the JSON string in the log area:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, sFile, sJsonString, oVbsVariant
Set oJsonParser = CreateJsonParser()
sFile = DataWritePath & "JsonObject.json"
sJsonString = oJsonParser.ReadFile(sFile)
Call oJsonParser.Deserialize(sJsonString, oVbsVariant)
Select Case VarType(oVbsVariant) 
Case vbObject
  Call LogfileWrite("Dictionary size: "  & oVbsVariant.Count)
Case vbArray + vbVariant
  Call LogfileWrite("Array size: "  & UBound(oVbsVariant)+1)
Case Else
  Call MsgBox("Some other data type")
End Select
Call LogfileWrite(sJsonString)
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
sFile = dd.DataWritePath + "JsonObject.json" 
sJsonString = oJsonParser.ReadFile(sFile) 
oJsonParser.Deserialize(sJsonString, oVbsVariant) 
select_variable_0 = VarType(oVbsVariant) 
if (select_variable_0 == vbObject) : 
    dd.LogfileWrite("Dictionary size: "  + oVbsVariant.Count) 
elif (select_variable_0 == vbArray + vbVariant) : 
    dd.LogfileWrite("Array size: "  + len(oVbsVariant)+1) 
else: 
    print("Some other data type") 
dd.LogfileWrite(sJsonString) 
```

#### See Also

[Objects Overview](../objects/ijsonparser_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=jsonparser/methods/jsonparser_method_serialize_ijsonparser.htm language=enus -->
## TOPIC 01372: Method: Serialize for JsonParser

- bundle_id: `diadem`
- source_path: `jsonparser/methods/jsonparser_method_serialize_ijsonparser.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/jsonparser/methods/jsonparser_method_serialize_ijsonparser.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Serialize for JsonParser

Method: Serialize for JsonParser

Converts a [Dictionary Object](../../scripting/objects/scripting_objects_idictionary.htm) or a [VBS Array](../../vbs/methods/vbs_method_array_globalobj.htm) into a JSON object. The items of the dictionary object can contain dictionary objects, [VBS arrays](../../vbs/methods/vbs_method_array_globalobj.htm), and primitive data types, such as strings, integer, double, and boolean.

```text
sSerialize = Object.Serialize(Value, [PrettifyJson])
```

| Object | JsonParserObject with this method |
| --- | --- |
| Value | VariantSpecifies a dictionary object or a VBS array. |
| [PrettifyJson] | BooleanSpecifies whether DIAdem formats the JSON string with spaces and word wraps (TRUE) or not (FALSE). If you do not enter a value, DIAdem does not format the JSON string. |
| sSerialize | String |

The following example creates a JSON object from a dictionary object containing a dictionary object, an array, a time value, and primitive data types in the items, and displays the contents of the JSON object in the log area:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, oMySubobject, oMyMainObject, sJsonString
Set oJsonParser = CreateJsonParser()
Set oMySubobject = CreateObject("Scripting.Dictionary")
Set oMyMainObject = CreateObject("Scripting.Dictionary")

Call oMySubobject.Add("intVal", CInt(1))  
Call oMySubobject.Add("doubleVal", CDbl(1.2))
Call oMySubobject.Add("stringVal", "TextA")

Call oMyMainObject.Add("subobject", oMySubobject)
Call oMyMainObject.Add("array", Array("TextB", 5678, True))
Call oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True))

sJsonString  = oJsonParser.Serialize(oMyMainObject, True)
Call LogFileWrite(sJsonString)
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
oMySubobject = win32com.client.dis-patch("Scripting.Dictionary") 
oMyMainObject = win32com.client.dis-patch("Scripting.Dictionary") 
oMySubobject.Add("intVal", int(1)) 
oMySubobject.Add("doubleVal", float(1.2)) 
oMySubobject.Add("stringVal", "TextA") 
oMyMainObject.Add("subobject", oMySubobject) 
oMyMainObject.Add("array", Array("TextB", 5678, True)) 
oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True)) 
sJsonString  = oJsonParser.Serialize(oMyMainObject, True) 
dd.LogFileWrite(sJsonString) 
```

#### See Also

[Objects Overview](../objects/ijsonparser_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=jsonparser/methods/jsonparser_method_writefile_ijsonparser.htm language=enus -->
## TOPIC 01373: Method: WriteFile for JsonParser

- bundle_id: `diadem`
- source_path: `jsonparser/methods/jsonparser_method_writefile_ijsonparser.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/jsonparser/methods/jsonparser_method_writefile_ijsonparser.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: WriteFile for JsonParser

Method: WriteFile for JsonParser

Saves a text to an UTF-8 file.

```text
Object.WriteFile(String, Filename)
```

| Object | JsonParserObject with this method |
| --- | --- |
| String | StringSpecifies the text. |
| Filename | StringSpecifies the name and the path of the JSON file. |

The following example creates a JSON object from a dictionary object containing an array and a time value in the items. The example saves the JSON object in a UTF-8 file and displays the path in the log area:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, oMyMainObject, sJsonString
Set oJsonParser = CreateJsonParser()
Set oMyMainObject = CreateObject("Scripting.Dictionary")

Call oMyMainObject.Add("array", Array("TextB", 5678, True))
Call oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True))
sJsonString = oJsonParser.Serialize(oMyMainObject, True)
Call oJsonParser.WriteFile(sJsonString, DataWritePath & "JsonObject.json")
Call LogfileWrite(DataWritePath & "JsonObject.json")
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
oMyMainObject = win32com.client.dis-patch("Scripting.Dictionary") 
oMyMainObject.Add("array", Array("TextB", 5678, True)) 
oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True)) 
sJsonString = oJsonParser.Serialize(oMyMainObject, True) 
oJsonParser.WriteFile(sJsonString, dd.DataWritePath + "JsonObject.json") 
dd.LogfileWrite(dd.DataWritePath + "JsonObject.json") 
```

#### See Also

[Objects Overview](../objects/ijsonparser_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=jsonparser/objects/ijsonparser_objects_overview.htm language=enus -->
## TOPIC 01374: JsonParser Object

- bundle_id: `diadem`
- source_path: `jsonparser/objects/ijsonparser_objects_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/jsonparser/objects/ijsonparser_objects_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[JSON Parser](../objects/jsonparser_overview.htm) > JsonParser Object

JsonParser Object

The JsonParser object provides methods for reading and writing JSON files and for converting JSON strings into the respective VBS objects and vice versa. A VBS object might be a dictionary object, an array, a string value, a double value, an integer value, a boolean value, a date/time value, or the the value null. Use the [CreateJsonParser](../../comoff/createjsonparser.htm) command to create the JsonParser object.

<!--NI_TOPIC bundle=diadem path=jsonparser/objects/jsonparser_objects_ijsonparser.htm language=enus -->
## TOPIC 01375: Object: JsonParser

- bundle_id: `diadem`
- source_path: `jsonparser/objects/jsonparser_objects_ijsonparser.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/jsonparser/objects/jsonparser_objects_ijsonparser.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[JSON Parser](../objects/jsonparser_overview.htm) > [Objects](../objects/ijsonparser_objects_overview.htm) > Object: JsonParser

Object: JsonParser

The JsonParser object provides methods for reading and writing JSON files in UTF8 format and for converting a JSON object into a [Dictionary object](../../scripting/objects/scripting_objects_idictionary.htm) and vice versa. Use the [CreateJsonParser](../../comoff/createjsonparser.htm) command to create the [JsonParser](../objects/jsonparser_objects_ijsonparser.htm) object.

The following example creates a JSON object from a dictionary object containing a dictionary object, an array, a time value, and primitive data types in the items, and displays the contents of the JSON object in the log area:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, oMySubobject, oMyMainObject, sJsonString
Set oJsonParser = CreateJsonParser()
Set oMySubobject = CreateObject("Scripting.Dictionary")
Set oMyMainObject = CreateObject("Scripting.Dictionary")

Call oMySubobject.Add("intVal", CInt(1))  
Call oMySubobject.Add("doubleVal", CDbl(1.2))
Call oMySubobject.Add("stringVal", "TextA")

Call oMyMainObject.Add("subobject", oMySubobject)
Call oMyMainObject.Add("array", Array("TextB", 5678, True))
Call oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True))

sJsonString = oJsonParser.Serialize(oMyMainObject, True)
Call LogFileWrite(sJsonString)
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
oMySubobject = win32com.client.dis-patch("Scripting.Dictionary") 
oMyMainObject = win32com.client.dis-patch("Scripting.Dictionary") 
oMySubobject.Add("intVal", int(1)) 
oMySubobject.Add("doubleVal", float(1.2)) 
oMySubobject.Add("stringVal", "TextA") 
oMyMainObject.Add("subobject", oMySubobject) 
oMyMainObject.Add("array", Array("TextB", 5678, True)) 
oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True)) 
sJsonString = oJsonParser.Serialize(oMyMainObject, True) 
dd.LogFileWrite(sJsonString) 
```

The following example creates from a JSON object a dictionary object containing text, numbers, and another dictionary object. The example displays values of the dictionary object in the log area:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, oVbsObject, sJsonString, sPath, oAggregates, sAvg
Set oJsonParser = CreateJsonParser() 
sJsonString = "{""path"":""task.id.592d7b9e-7816-4517-973d-ef03cc814e35"",""current"":{""timestamp"":""2018-11-27T12:33:27Z""," & _
"""value"":{""type"":1,""value"":""47""}},""aggregates"":{""count"":1,""avg"":47.0,""min"":""47"",""max"":""47""}}"
Call oJsonParser.Deserialize(sJsonString, oVbsObject)
sPath = oVbsObject.Item("path")
Set oAggregates = oVbsObject.Item("aggregates")
sAvg = oAggregates.Item("avg")
sJsonString = oJsonParser.Serialize(oVbsObject, True) ' make pretty for viewing
Call LogFileWrite(sJsonString)
Call LogFileWrite("path: " &  sPath & vbCRLF & "avg: " & sAvg)
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
sJsonString = "{""path"":""task.id.592d7b9e-7816-4517-973d-ef03cc814e35"",""current"":{""timestamp"":""2018-11-27T12:33:27Z""," + """value"" 
{""type"":1,""value"":""47""}},""aggregates"":{""count"":1,""avg"":47.0,""min"":""47"",""max"":""47""}}" 
oJsonParser.Deserialize(sJsonString, oVbsObject) 
sPath = oVbsObject.Item("path") 
oAggregates = oVbsObject.Item("aggregates") 
sAvg = oAggregates.Item("avg") 
sJsonString = oJsonParser.Serialize(oVbsObject, True) # make pretty for viewing
dd.LogFileWrite(sJsonString) 
dd.LogFileWrite("path: " +  sPath + "\r\n" + "avg: " + sAvg) 
```

The following example creates a JSON object from a dictionary object containing an array and a time value in the items. The example saves the JSON object in a UTF-8 file and displays the path in the log area:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, oMyMainObject, sJsonString
Set oJsonParser = CreateJsonParser()
Set oMyMainObject = CreateObject("Scripting.Dictionary")

Call oMyMainObject.Add("array", Array("TextB", 5678, True))
Call oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True))
sJsonString = oJsonParser.Serialize(oMyMainObject, True)
Call oJsonParser.WriteFile(sJsonString, DataWritePath & "JsonObject.json")
Call LogfileWrite(DataWritePath & "JsonObject.json")
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
oMyMainObject = win32com.client.dis-patch("Scripting.Dictionary") 
oMyMainObject.Add("array", Array("TextB", 5678, True)) 
oMyMainObject.Add("timestamp", oJsonParser.CreateDateTime(Now, True)) 
sJsonString = oJsonParser.Serialize(oMyMainObject, True) 
oJsonParser.WriteFile(sJsonString, dd.DataWritePath + "JsonObject.json") 
dd.LogfileWrite(dd.DataWritePath + "JsonObject.json") 
```

The following example reads a JSON file, converts the JSON string into a dictionary object or an array, and displays the size of the dictionary object or array and the JSON string in the log area:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oJsonParser, sFile, sJsonString, oVbsVariant
Set oJsonParser = CreateJsonParser()
sFile = DataWritePath & "JsonObject.json"
sJsonString = oJsonParser.ReadFile(sFile)
Call oJsonParser.Deserialize(sJsonString, oVbsVariant)
Select Case VarType(oVbsVariant) 
Case vbObject
  Call LogfileWrite("Dictionary size: "  & oVbsVariant.Count)
Case vbArray + vbVariant
  Call LogfileWrite("Array size: "  & UBound(oVbsVariant)+1)
Case Else
  Call MsgBox("Some other data type")
End Select
Call LogfileWrite(sJsonString)
```

[Copy script](javascript:void(0);)

```text
oJsonParser = dd.CreateJsonParser() 
sFile = dd.DataWritePath + "JsonObject.json" 
sJsonString = oJsonParser.ReadFile(sFile) 
oJsonParser.Deserialize(sJsonString, oVbsVariant) 
select_variable_0 = VarType(oVbsVariant) 
if (select_variable_0 == vbObject) : 
    dd.LogfileWrite("Dictionary size: "  + oVbsVariant.Count) 
elif (select_variable_0 == vbArray + vbVariant) : 
    dd.LogfileWrite("Array size: "  + len(oVbsVariant)+1) 
else: 
    print("Some other data type") 
dd.LogfileWrite(sJsonString) 
```

#### Methods

[CreateDateTime](../methods/jsonparser_method_createdatetime_ijsonparser.htm) | [Deserialize](../methods/jsonparser_method_deserialize_ijsonparser.htm) | [ParseDateTime](../methods/jsonparser_method_parsedatetime_ijsonparser.htm) | [ReadFile](../methods/jsonparser_method_readfile_ijsonparser.htm) | [Serialize](../methods/jsonparser_method_serialize_ijsonparser.htm) | [WriteFile](../methods/jsonparser_method_writefile_ijsonparser.htm)

#### See Also

[Objects Overview](../objects/ijsonparser_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=jsonparser/objects/jsonparser_overview.htm language=enus -->
## TOPIC 01376: JSON Parser

- bundle_id: `diadem`
- source_path: `jsonparser/objects/jsonparser_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/jsonparser/objects/jsonparser_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

JSON Parser

JSON Parser

The subordinate topics in the contents tree in the help describe the object-oriented script interface for reading and writing JSON files and for converting JSON strings into the respective VBS objects and vice versa. They contain information on the methods, and examples on how to use the interface. Use the [CreateJsonParser](../../comoff/createjsonparser.htm) command to create the [JsonParser](../objects/jsonparser_objects_ijsonparser.htm) object.

<!--NI_TOPIC bundle=diadem path=lvhelper/methods/lvhelper_method_deinit_ilvruntime.htm language=enus -->
## TOPIC 01377: Method: DeInit for LVRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/methods/lvhelper_method_deinit_ilvruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/methods/lvhelper_method_deinit_ilvruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Methods](../methods/lvhelper_method_overview.htm) > Method: DeInit for LVRuntime

Method: DeInit for LVRuntime

Unloads the LabVIEW Run Time Library and disconnects LabVIEW.

```text
Object.DeInit
```

| Object | LVRuntimeObject with this method |
| --- | --- |

The following example connects LabVIEW and starts a VI. Then the example disconnects LabVIEW:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
' Initialize the LVRuntime
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT

' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test") 

' Call the VI
Call objVI.Run(true)
' Clean upSet VIT = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
# Initialize the LVRuntime
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test") 
# Call the VI
objVI.Run(True) 
# Clean upSet VIT = Nothing
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/methods/lvhelper_method_getcontrolvalue_iviruntime.htm language=enus -->
## TOPIC 01378: Method: GetControlValue for VIRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/methods/lvhelper_method_getcontrolvalue_iviruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/methods/lvhelper_method_getcontrolvalue_iviruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Methods](../methods/lvhelper_method_overview.htm) > Method: GetControlValue for VIRuntime

Method: GetControlValue for VIRuntime

Returns the output value while retaining the original data type. This means the type of the return value is the same as the value type in LabVIEW. You cannot always process the type-safe values in VBS functions, because the functions usually expect variant values. Use the [GetControlVariant](../methods/lvhelper_method_getcontrolvariant_iviruntime.htm) method to receive variant values. You can use the property [Value for Property](../../inavidata/properties/diacmpnt_property_value_idiademproperty.htm) or the function [ArrayToChannels](../../comoff/arraytochannels.htm) to edit, for example, the original data in DIAdem. You can use the [ChntoValue](../../comoff/chntovalue.htm) command to convert channels into variant arrays or you can use the [VariantToChn](../../comoff/varianttochn.htm) command to convert variant data arrays into channels.

```text
vGetControlValue = Object.GetControlValue(OutputName)
```

| Object | VIRuntimeObject with this method |
| --- | --- |
| OutputName | StringSpecifies the name of the output. You receive an error message if the name is not available or if it is an input.You can receive single values, vectors, and two-dimensional matrices. |
| vGetControlValue | VariantReceives the value of the output. You can request single values, vectors, and two-dimensional matrices.The following data types are supported: Boolean Boolean value I8 8-bit integer value I16 16-bit integer value I32 32-bit integer value U8 Unsigned 8-bit integer value U16 Unsigned 16-bit integer value U32 Unsigned 32-bit integer value DBL Double-precision floating point values String String |
| Boolean | Boolean value |
| I8 | 8-bit integer value |
| I16 | 16-bit integer value |
| I32 | 32-bit integer value |
| U8 | Unsigned 8-bit integer value |
| U16 | Unsigned 16-bit integer value |
| U32 | Unsigned 32-bit integer value |
| DBL | Double-precision floating point values |
| String | String |

|  | Note You only can read out LabVIEW waveforms and LabVIEW clusters with the GetControlVariant command. |
| --- | --- |

The following example returns the current value at the OutPut1 output:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi") 
Call objVI.Run(true)
Call MsgBoxDisp(objVI.GetControlValue("OutPut1"))
' Clean up
Set objVI = NothingLVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
objVI.Run(True) 
dd.MsgBoxDisp(objVI.GetControlValue("OutPut1")) 
# Clean up
objVI = NothingLVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/methods/lvhelper_method_getcontrolvariant_iviruntime.htm language=enus -->
## TOPIC 01379: Method: GetControlVariant for VIRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/methods/lvhelper_method_getcontrolvariant_iviruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/methods/lvhelper_method_getcontrolvariant_iviruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Methods](../methods/lvhelper_method_overview.htm) > Method: GetControlVariant for VIRuntime

Method: GetControlVariant for VIRuntime

Returns the value of an output. The return value type is a variant. VBS converts variant values automatically into the respective data format. Use the [GetControlValue](../methods/lvhelper_method_getcontrolvalue_iviruntime.htm) command to receive the data in the original data type.

```text
vGetControlVariant = Object.GetControlVariant(OutputName)
```

| Object | VIRuntimeObject with this method |
| --- | --- |
| OutputName | StringSpecifies the name of the output. You receive an error message if the name is not available or if it is an input. |
| vGetControlVariant | VariantReceives the value of the output. You can request single values, two-dimensional matrices, waveforms, and clusters. |

The following example returns the current value at the OutPut1 output:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test") 
Call objVI.run(true)
Call MsgBoxDisp(objVI.GetControlVariant("OutPut1"))
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test") 
objVI.run(True) 
dd.MsgBoxDisp(objVI.GetControlVariant("OutPut1")) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

The following example returns the current value of a matrix at the MyStringMatrix output:

[IMAGE alt='image' src='../image/example_matrix.gif']

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.loadvi(AutoActPath & "Test")
Call objVI.Run(true)
Dim MyMatrix(2,3)
MyMatrix = objVI.GetControlVariant("MyStringMatrix")
Dim I, J, strOutput
For I = 0 to UBound(MyMatrix,1)
  For J = 0 to UBound(MyMatrix,2)
    strOutput = strOutput + I & " Row " & j & " Column: " & MyMatrix(I, J) & VBCrLf
  Next
Next
Call MsgBoxDisp(strOutput)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.loadvi(dd.AutoActPath + "Test") 
objVI.Run(True) 
MyMatrix = objVI.GetControlVariant("MyStringMatrix") 
for I in range( 0, len(MyMatrix,1) + 1): 
    for J in range( 0, len(MyMatrix,2) + 1): 
        strOutput = strOutput + I + " Row " + j + " Column: " + MyMatrix(I, J) + "\r\n" 
dd.MsgBoxDisp(strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

You receive the cluster values as an array with a specific structure.

The following example returns the current values of a cluster at the MyCluster output:

[IMAGE alt='image' src='../image/example_cluster.gif']

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.loadvi(AutoActPath & "Test")

Call objVI.Run(true)
Dim MyMatrix
Dim aMyCluster
aMyCluster = objVI.GetControlVariant("MyCluster")
Dim strOutput
strOutput = aMyCluster(0) & VBCrLf 'Get the value MyI32Scalar
MyMatrix= aMyCluster(1) 'Get the matrix values MyStringMatrix
For I = 0 to UBound(MyMatrix,1)
  For J = 0 to UBound(MyMatrix,2)
    strOutput = strOutput & MyMatrix(I, J) & VBCrLf
  Next
Next
Call MsgBoxDisp(strOutput)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.loadvi(dd.AutoActPath + "Test") 
objVI.Run(True) 
aMyCluster = objVI.GetControlVariant("MyCluster") 
strOutput = aMyCluster(0) + "\r\n" #Get the value MyI32Scalar
MyMatrix= aMyCluster(1) #Get the matrix values MyStringMatrix
for I in range( 0, len(MyMatrix,1) + 1): 
    for J in range( 0, len(MyMatrix,2) + 1): 
        strOutput = strOutput + MyMatrix(I, J) + "\r\n" 
dd.MsgBoxDisp(strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

You receive the waveform values as an array with the following specific structure:

The following example returns the current values of a waveform at the MyWafevorm input:

[IMAGE alt='image' src='../image/example_wf.gif']

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.loadvi(AutoActPath & "Test")

Call objVI.Run(True)

Dim WaveFormT
WaveFormT = objVI.GetControlVariant("MyWaveformOut")

Dim strOutput
strOutput = ""
strOutput = strOutput & "T0: " & WaveFormT(0) & VBCrLf
strOutput = strOutput & "dT: " & WaveFormT(1) & VBCrLf

Dim AttributesT
AttributesT = WaveFormT(2)
Dim I
For I = 0 to UBound(AttributesT,1)
  strOutput = strOutput & "Attribute: " & AttributesT(I, 0) & " = " & AttributesT(I, 0) & VBCrLf
Next

Dim ValuesT
ValuesT = WaveFormT(3)
For I = 0 to UBound(ValuesT)
  strOutput = strOutput & "Values: " & ValuesT(I) & VBCrLf
Next
Call MsgBoxDisp (strOutput)

' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.loadvi(dd.AutoActPath + "Test") 
objVI.Run(True) 
WaveFormT = objVI.GetControlVariant("MyWaveformOut") 
strOutput = "" 
strOutput = strOutput + "T0: " + WaveFormT(0) + "\r\n" 
strOutput = strOutput + "dT: " + WaveFormT(1) + "\r\n" 
AttributesT = WaveFormT(2) 
for I in range( 0, len(AttributesT,1) + 1): 
    strOutput = strOutput + "Attribute: " + AttributesT(I, 0) + " = " + AttributesT(I, 0) + "\r\n" 
ValuesT = WaveFormT(3) 
for I in range( 0, len(ValuesT) + 1): 
    strOutput = strOutput + "Values: " + ValuesT(I) + "\r\n" 
dd.MsgBoxDisp (strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/methods/lvhelper_method_init_ilvruntime.htm language=enus -->
## TOPIC 01380: Method: Init for LVRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/methods/lvhelper_method_init_ilvruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/methods/lvhelper_method_init_ilvruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Methods](../methods/lvhelper_method_overview.htm) > Method: Init for LVRuntime

Method: Init for LVRuntime

Loads the LabVIEW Runtime Library and connects LabVIEW.

```text
bInit = Object.Init(Version)
```

| Object | LVRuntimeObject with this method |
| --- | --- |
| Version | StringVersion number, for example, 8.0. You must always specify the version number if you have installed just one runtime version of LabVIEW. If LabVIEW is installed and you do not specify a version number, DIAdem automatically specifies the version number from the registration file.You can use the LVRuntime.Version property to request the version. |
| bInit | BooleanReceives information as to whether a LabVIEW version with the correct version number has been connected (TRUE) or not (FALSE). |

The following example connects LabVIEW and starts a VI. Then the example disconnects LabVIEW:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
' Initialize the LVRuntime
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT

' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI("Test") 

' Call the VI
Call objVI.Run(true)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
# Initialize the LVRuntime
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI("Test") 
# Call the VI
objVI.Run(True) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/methods/lvhelper_method_item_iterminals.htm language=enus -->
## TOPIC 01381: Method: Item for Terminals

- bundle_id: `diadem`
- source_path: `lvhelper/methods/lvhelper_method_item_iterminals.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/methods/lvhelper_method_item_iterminals.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Methods](../methods/lvhelper_method_overview.htm) > Method: Item for Terminals

Method: Item for Terminals

Returns the Terminal object for a specific index of a VI. A terminal is an input terminal or an output terminal of a VI.

```text
Set oTerminal = Object.Item(NameOrIndex)
```

| Object | TerminalsObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the index of the selected terminal. |
| oTerminal | TerminalReturned object |

|  | Note You can omit the Item method because it is always the standard element of the collection. |
| --- | --- |

The following example displays the name of the terminal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVi(AutoActPath & "Test")

Dim oMyTerminals
Set oMyTerminals = objVI.Terminals 'Get Terminals
Dim strOutput
strOutput = "List of terminals:"
Dim I
For I = 0 to oMyTerminals.count-1
  strOutput = strOutput & VbCrLF & "Name: " & oMyterminals.Item(I).Name
Next
MsgBoxDisp (strOutput)

' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVi(dd.AutoActPath + "Test") 
oMyTerminals = objVI.Terminals #Get Terminals
strOutput = "List of terminals:" 
for I in range( 0, oMyTerminals.count-1 + 1): 
    strOutput = strOutput + "\r\n" + "Name: " + oMyterminals.Item(I).Name 
MsgBoxDisp (strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

If you omit Item, the script is easier to write:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
strOutput = strOutput & VbCrLF & "Name: " & oMyterminals(I).Name
```

[Copy script](javascript:void(0);)

```text
strOutput = strOutput + "\r\n" + "Name: " + oMyterminals(I).Name 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/methods/lvhelper_method_loadvi_ilvruntime.htm language=enus -->
## TOPIC 01382: Method: LoadVI for LVRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/methods/lvhelper_method_loadvi_ilvruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/methods/lvhelper_method_loadvi_ilvruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Methods](../methods/lvhelper_method_overview.htm) > Method: LoadVI for LVRuntime

Method: LoadVI for LVRuntime

Loads a VI.

```text
Set oVIRuntime = Object.LoadVI(VIPath)
```

| Object | LVRuntimeObject with this method |
| --- | --- |
| VIPath | StringSpecifies the complete name of the VI including the path. If you do not specify a filename extension, DIAdem uses the extension .vi. |
| oVIRuntime | VIRuntimeReturned object |

|  | Note If you create VIs with LabVIEW and you want these VIs to run only with the LabVIEW Runtime Engine, you must create a source distribution of the VIs. Refer to the LabVIEW help under the search term Source Distribution for further information.If LabVIEW cannot interpret relative path specifications in a normal installation, because, for example, you are using Express VIs, you must edit the DIAdem.ini file in the DIAdem program folder. If the file does not exist, you must create this file. Insert the following entry into the DIAdem.ini file: [LVRT] libdir="LabVIEW_ProgramPath" The LabVIEW_ProgramPath specifies the LabVIEW program path, such as C:\\Program Files\\National Instruments\\LabVIEW 8.2.After you make this modification, you must restart DIAdem. |
| --- | --- |

The following example connects LabVIEW and starts a VI. Then the example disconnects LabVIEW:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
' Initialize the LVRuntime
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT

' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test") 

' Call the VI
Call objVI.Run(true)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
# Initialize the LVRuntime
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test") 
# Call the VI
objVI.Run(True) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/methods/lvhelper_method_overview.htm language=enus -->
## TOPIC 01383: Methods

- bundle_id: `diadem`
- source_path: `lvhelper/methods/lvhelper_method_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/methods/lvhelper_method_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > Methods

Methods

Use methods to execute actions. For example, you can use a method to add a new element to a collection. Many methods return an object that contains the new element in the collection.

The subordinate topics contained in the tree on the contents tab of the Help describe all the methods of the LVRuntime script interface.

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_helppath_iviruntime.htm language=enus -->
## TOPIC 01384: Property: HelpPath for VIRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_helppath_iviruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_helppath_iviruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: HelpPath for VIRuntime

Property: HelpPath for VIRuntime

Returns the path for the HTML file (*.htm or *.html) or the help file (*.chm or *.hlp) for which the VI contains a link. If the path leads to a compiled help file, the [HelpTag](../properties/lvhelper_property_helptag_iviruntime.htm) property enables the selection of a topic in the help file. This property is similar to the **Help path** textbox from the **Documentation** page in the LabVIEW **VI properties** dialog field.

```text
Object.HelpPath
```

| Object | VIRuntimeObject with this property |
| --- | --- |
| Object.HelpPath | String with read and write access |

The following example returns the HelpPath of a VI:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi") 
Call MsgBoxDisp(objVI.HelpPath) 'Get HelpPath
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
dd.MsgBoxDisp(objVI.HelpPath) #Get HelpPath
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_helptag_iviruntime.htm language=enus -->
## TOPIC 01385: Property: HelpTag for VIRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_helptag_iviruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_helptag_iviruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: HelpTag for VIRuntime

Property: HelpTag for VIRuntime

Returns an index keyword or an HTML filename for a topic in the compiled help file to which the VI contains a link. For *.chm files this property can be an HTML filename or an index keyword. For *.hlp files this property can be an index keyword. This property is similar to the **Help tag** textbox from the **Documentation** page in the LabVIEW **VI properties** dialog field.

```text
Object.HelpTag
```

| Object | VIRuntimeObject with this property |
| --- | --- |
| Object.HelpTag | String with read and write access |

The following example returns the HelpTag of a VI:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi") 
Call MsgBoxDisp(objVI.HelpTag) 'Get HelpTag
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
dd.MsgBoxDisp(objVI.HelpTag) #Get HelpTag
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_isout_iterminal.htm language=enus -->
## TOPIC 01386: Property: IsOut for Terminal

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_isout_iterminal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_isout_iterminal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: IsOut for Terminal

Property: IsOut for Terminal

Specifies whether a terminal is an output.

```text
Object.IsOut
```

| Object | TerminalObject with this property |
| --- | --- |
| Object.IsOut | Boolean with read and write access |

The following example outputs the names, the dimensions, and the types for all terminals, and specifies whether the terminal is an output:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi")
Dim oMyTerminals
Set oMyTerminals = objVI.Terminals 'Get Terminals
Dim strOutPut
strOutput = "List of terminals:"
Dim oMyTerminal
For Each oMyTerminal in oMyTerminals
  strOutput = strOutput & VbCrLF & "Name: " & oMyterminal.Name()
  strOutput = strOutput & ": Is output: " & oMyterminal.IsOut()
Next
Call MsgBoxDisp (strOutput)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
oMyTerminals = objVI.Terminals #Get Terminals
strOutput = "List of terminals:" 
for oMyTerminal in oMyTerminals: 
    strOutput = strOutput + "\r\n" + "Name: " + oMyterminal.Name() 
    strOutput = strOutput + ": is output: " + oMyterminal.IsOut() 
dd.MsgBoxDisp (strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_name_iterminal.htm language=enus -->
## TOPIC 01387: Property: Name for Terminal

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_name_iterminal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_name_iterminal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: Name for Terminal

Property: Name for Terminal

Returns the name of an incoming and outgoing VI terminal.

```text
Object.Name
```

| Object | TerminalObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

|  | Note You can omit the Name property because the property is a standard element of the collection. |
| --- | --- |

The following example outputs the names of all terminals:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi")
Dim oMyTerminals
Set oMyTerminals = objVI.Terminals 'Get TerminalsDim strOutput
strOutput = "List of terminals:"
Dim oMyTerminal
For Each oMyTerminal in oMyTerminals
  strOutput = strOutput & VbCrLF & "Name: " & oMyterminal.Name
Next
MsgBoxDisp (strOutput)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
oMyTerminals = objVI.Terminals #Get TerminalsDim strOutput
strOutput = "List of terminals:" 
for oMyTerminal in oMyTerminals: 
    strOutput = strOutput + "\r\n" + "Name: " + oMyterminal.Name 
MsgBoxDisp (strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_name_iviruntime.htm language=enus -->
## TOPIC 01388: Property: Name for VIRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_name_iviruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_name_iviruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: Name for VIRuntime

Property: Name for VIRuntime

Returns the complete name and path of the VI.

```text
Object.Name
```

| Object | VIRuntimeObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

|  | Note You can omit the Name property because the property is a standard element of the collection. |
| --- | --- |

The following example returns the name of the VI:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi") 
Call MsgBoxDisp(objVI.Name) 'Get version
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
dd.MsgBoxDisp(objVI.Name) #Get version
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_overview.htm language=enus -->
## TOPIC 01389: Properties

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > Properties

Properties

Properties determine the behavior of objects or return objects. These objects can have their own properties and methods.

The subordinate topics contained in the tree on the contents tab of the Help describe all the properties of the LVRuntime script interface.

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_terminals_iviruntime.htm language=enus -->
## TOPIC 01390: Property: Terminals for VIRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_terminals_iviruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_terminals_iviruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: Terminals for VIRuntime

Property: Terminals for VIRuntime

Returns a list of output terminals and input terminals of a VI.

```text
Set oTerminals = Object.Terminals
```

| Object | VIRuntimeObject with this property |
| --- | --- |
| oTerminals | TerminalsReturned object |

The following example outputs the names, the dimensions, and the types for all terminals, and specifies whether the terminal is an output:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi")
Dim oMyTerminals
Set oMyTerminals = objVI.Terminals 'Get Terminals
Dim strOutput
strOutput = "List of terminals:"
For Each oMyTerminal in oMyTerminals
  strOutput = strOutput & VbCrLF & "Name: " & oMyterminal.Name()
  strOutput = strOutput & ": Dimension is: " & Str(oMyterminal.Dimensions())
  strOutput = strOutput & ": Type is: " & oMyterminal.Type()
  strOutput = strOutput & ": Is output: " & oMyterminal.IsOut()
Next
MsgBoxDisp (strOutput)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
oMyTerminals = objVI.Terminals #Get Terminals
strOutput = "List of terminals:" 
for oMyTerminal in oMyTerminals: 
    strOutput = strOutput + "\r\n" + "Name: " + oMyterminal.Name() 
    strOutput = strOutput + ": Dimension is: " + dd.Str(oMyterminal.Dimensions()) 
    strOutput = strOutput + ": Type is: " + oMyterminal.Type() 
    strOutput = strOutput + ": is output: " + oMyterminal.IsOut() 
MsgBoxDisp (strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_type_iterminal.htm language=enus -->
## TOPIC 01391: Property: Type for Terminal

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_type_iterminal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_type_iterminal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: Type for Terminal

Property: Type for Terminal

Returns the type of an incoming and outgoing VI terminal.

```text
Object.Type
```

| Object | TerminalObject with this property |
| --- | --- |
| Object.Type | Variant with read and write accessContents of the type for single values, vectors, or matrices: Boolean Boolean value I8 8-bit integer value I16 16-bit integer value I32 32-bit integer value U8 Unsigned 8-bit integer value U16 Unsigned 16-bit integer value U32 Unsigned 32-bit integer value DBL Double-precision floating point values SGL Single-precision floating point values String String Path LabVIEW path type If Type is a cluster or a waveform, the Type property returns an array that has the following structure. Assign a local VBS variable to such an array in order to be able to work with the array: Index Contents 0 Name of the cluster 1 Type, always "Cluster" 2 Dimension of the array, for cluster always 0 3 If the dimension is greater than 0, the element contains the number of elements of the first dimension.If the dimension is 0, the same structure starting at index 0 follows for the embedded elements. 4 If the dimension is greater than 1, the element contains the number of elements of the first dimension.If the dimension is smaller than 1, the same structure starting at index 0 follows for the embedded elements. ... The same structure as starting at index 0 follows for the embedded elements. If the type of a cluster element is again a cluster, DIAdem stores a reference to an array that contains this cluster. The dimension for a cluster is always 0. |
| Boolean Boolean value I8 8-bit integer value I16 16-bit integer value I32 32-bit integer value U8 Unsigned 8-bit integer value U16 Unsigned 16-bit integer value U32 Unsigned 32-bit integer value DBL Double-precision floating point values SGL Single-precision floating point values String String Path LabVIEW path type If Type is a cluster or a waveform, the Type property returns an array that has the following structure. Assign a local VBS variable to such an array in order to be able to work with the array: Index Contents 0 Name of the cluster 1 Type, always "Cluster" 2 Dimension of the array, for cluster always 0 3 If the dimension is greater than 0, the element contains the number of elements of the first dimension.If the dimension is 0, the same structure starting at index 0 follows for the embedded elements. 4 If the dimension is greater than 1, the element contains the number of elements of the first dimension.If the dimension is smaller than 1, the same structure starting at index 0 follows for the embedded elements. ... The same structure as starting at index 0 follows for the embedded elements. If the type of a cluster element is again a cluster, DIAdem stores a reference to an array that contains this cluster. The dimension for a cluster is always 0. |  |
| Boolean | Boolean value |
| I8 | 8-bit integer value |
| I16 | 16-bit integer value |
| I32 | 32-bit integer value |
| U8 | Unsigned 8-bit integer value |
| U16 | Unsigned 16-bit integer value |
| U32 | Unsigned 32-bit integer value |
| DBL | Double-precision floating point values |
| SGL | Single-precision floating point values |
| String | String |
| Path | LabVIEW path type |
| Index | Contents |
| 0 | Name of the cluster |
| 1 | Type, always "Cluster" |
| 2 | Dimension of the array, for cluster always 0 |
| 3 | If the dimension is greater than 0, the element contains the number of elements of the first dimension.If the dimension is 0, the same structure starting at index 0 follows for the embedded elements. |
| 4 | If the dimension is greater than 1, the element contains the number of elements of the first dimension.If the dimension is smaller than 1, the same structure starting at index 0 follows for the embedded elements. |
| ... | The same structure as starting at index 0 follows for the embedded elements. |

If the type is not a cluster, the following example outputs the type for all terminals:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi")
Dim oMyTerminals
Set oMyTerminals = objVI.Terminals 'Get Terminals
Dim strOutput
strOutput = "List of terminals:"
Dim oMyTerminal
For Each oMyTerminal in oMyTerminals
  strOutput = strOutput & VbCrLF & "Name: " & oMyterminal.Name()
  strOutput = strOutput & ": Type is: " & oMyterminal.Type()
Next
Call MsgBoxDisp (strOutput)
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
oMyTerminals = objVI.Terminals #Get Terminals
strOutput = "List of terminals:" 
for oMyTerminal in oMyTerminals: 
    strOutput = strOutput + "\r\n" + "Name: " + oMyterminal.Name() 
    strOutput = strOutput + ": Type is: " + oMyterminal.Type() 
dd.MsgBoxDisp (strOutput) 
# Clean up
objVI = None 
LVRuntime.DeInit 
```

If the type is a cluster, the following example outputs the cluster structure for all cluster type terminals:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
' Initialize the LVRuntime
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI, oMyTerminals
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test1.vi") 
Set oMyTerminals = objVI.Terminals 'Get Terminals
' Get more details about the terminals
Dim oMyTerminal 
Dim strOutput
strOutput  = ""
For Each oMyTerminal  in oMyTerminals
  strOutput  =  strOutput  _              
        & "--------------------------------------------------------------------------" & vbCrLf _
  Dim aClusterInfoT
  aClusterInfoT = oMyTerminal.Type
  If IsArray(aClusterInfoT) Then
    strOutput  =  strOutput  & vbCrLf & "Name: " & aClusterInfoT(0)
    strOutput  =  strOutput  & vbCrLf & "Type of Clusters: " & aClusterInfoT(1)
    strOutput  =  strOutput  & vbCrLf & "Dimension: " & aClusterInfoT(2)
    strOutput  =  strOutput  & vbCrLf & "Name of first Cluster element: " & aClusterInfoT(3)
    strOutput  =  strOutput  & vbCrLf & "Typ of first Cluster element: " & aClusterInfoT(4)
    strOutput  =  strOutput  & vbCrLf & "Dimension of first Cluster element: " & aClusterInfoT(5)
    strOutput  =  strOutput  & vbCrLf & "Name of second Cluster element: " & aClusterInfoT(6)
  Else
    strOutput  =  strOutput  & vbCrLf & "Name: " & oMyTerminal.Name
    strOutput  =  strOutput  & vbCrLf & "Not a Cluster: "
  End If

  strOutput  =  strOutput  & vbCrLf 

Next

Call MsgBoxDisp (strOutput)

' Clean upSet TerminalsT = Nothing
Set VIT = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
# Initialize the LVRuntime
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test1.vi") 
oMyTerminals = objVI.Terminals #Get Terminals
# Get more details about the terminals
strOutput  = "" 
for oMyTerminal  in oMyTerminals: 
    strOutput  =  strOutput  + "--------------------------------------------------------------------------" + "\r\n" 
    aClusterInfoT = oMyTerminal.Type 
    if IsArray(aClusterInfoT) : 
        strOutput  =  strOutput  + "\r\n" + "Name: " + aClusterInfoT(0) 
        strOutput  =  strOutput  + "\r\n" + "Type of Clusters: " + aClusterInfoT(1) 
        strOutput  =  strOutput  + "\r\n" + "Dimension: " + aClusterInfoT(2) 
        strOutput  =  strOutput  + "\r\n" + "Name of first Cluster element: " + aClusterInfoT(3) 
        strOutput  =  strOutput  + "\r\n" + "Typ of first Cluster element: " + aClusterInfoT(4) 
        strOutput  =  strOutput  + "\r\n" + "Dimension of first Cluster element: " + aClusterInfoT(5) 
        strOutput  =  strOutput  + "\r\n" + "Name of second Cluster element: " + aClusterInfoT(6) 
    else: 
        strOutput  =  strOutput  + "\r\n" + "Name: " + oMyTerminal.Name 
        strOutput  =  strOutput  + "\r\n" + "not a Cluster: " 
    strOutput  =  strOutput  + "\r\n" 
dd.MsgBoxDisp (strOutput) 
# Clean upSet TerminalsT = Nothing
dd.VIT = None 
LVRuntime.DeInit 
```

For example, you can have a cluster with a structure as shown in the following table.

[IMAGE alt='image' src='../image/example1.gif']

###### Structure:

| Index | Value | Explanation |
| --- | --- | --- |
| 0 | "MyCluster" | Name of the cluster |
| 1 | "Cluster" | Terminal type, always cluster |
| 2 | 0 | Always 0 |
| 3 | "MyI32Scalar" | Name of the first cluster element |
| 4 | "I32" | Type of the first cluster element, here 32 bit integer |
| 5 | 0 | Scalar |
| 6 | "MyStringArray" | Name of the second cluster element |
| 7 | "String" | Type of the second cluster element, here double |
| 8 | 2 | Matrix |
| 9 | 4 | Number of elements of the first dimension |
| 10 | 2 | Number of elements of the second dimension |
| 11 | Reference | Reference to the array of embedded cluster |
| ... 0 | "ClusterInCluster" | Name of the embedded cluster |
| ... 1 | "Cluster" | Terminal type, always cluster |
| ... 2 | 0 | Always 0 |
| ... 3 | ... | Further elements of the embedded cluster |
| 13 | ... | Further elements of the embedded cluster |

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_version_ilvruntime.htm language=enus -->
## TOPIC 01392: Property: Version for LVRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_version_ilvruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_version_ilvruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: Version for LVRuntime

Property: Version for LVRuntime

Returns the LabVIEW version that the LVRuntime uses.

```text
Object.Version
```

| Object | LVRuntimeObject with this property |
| --- | --- |
| Object.Version | String with read and write access |

|  | Note You can omit the Version property because the property is a standard element of the collection. |
| --- | --- |

The following example returns the LabVIEW version:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
Call MsgBoxDisp (LVRuntime.Version) 
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
dd.MsgBoxDisp (dd.LVRuntime.Version) 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/properties/lvhelper_property_version_iviruntime.htm language=enus -->
## TOPIC 01393: Property: Version for VIRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/properties/lvhelper_property_version_iviruntime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/properties/lvhelper_property_version_iviruntime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[LabVIEW](../scriptlvhelper_overview.htm) > [Properties](../properties/lvhelper_property_overview.htm) > Property: Version for VIRuntime

Property: Version for VIRuntime

Returns the LabVIEW version with which the VI was generated.

```text
Object.Version
```

| Object | VIRuntimeObject with this property |
| --- | --- |
| Object.Version | String with read and write access |

The following example returns the LabVIEW version:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim sgRunTimeVersionT : sgRunTimeVersionT = ""
LVRuntime.Init sgRunTimeVersionT
' Load "Test.VI"
Dim objVI
Set objVI = LVRuntime.LoadVI(AutoActPath & "Test.vi") 
Call MsgBoxDisp(objVI.Version) 'Get version
' Clean up
Set objVI = Nothing
LVRuntime.DeInit
```

[Copy script](javascript:void(0);)

```text
sgRunTimeVersionT = "" 
LVRuntime.Init sgRunTimeVersionT 
# Load "Test.VI"
objVI = dd.LVRuntime.LoadVI(dd.AutoActPath + "Test.vi") 
dd.MsgBoxDisp(objVI.Version) #Get version
# Clean up
objVI = None 
LVRuntime.DeInit 
```

#### See Also

[Object overview](../objects/ilvruntime_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=lvhelper/scriptlvhelper_overview.htm language=enus -->
## TOPIC 01394: LVRuntime

- bundle_id: `diadem`
- source_path: `lvhelper/scriptlvhelper_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/lvhelper/scriptlvhelper_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

LVRuntime

LVRuntime

The subordinate topics contained in the tree on the contents tab of the Help describe the object-oriented script interface LVRuntime, which you can use to access LabVIEW. The topics provide information about all objects, collections, methods, and properties, and examples that demonstrate how to use the interface.

<!--NI_TOPIC bundle=diadem path=mgc-help/erf_mgc_help.htm language=enus -->
## TOPIC 01395: Acquisition Device Definition for HBM MGC

- bundle_id: `diadem`
- source_path: `mgc-help/erf_mgc_help.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/mgc-help/erf_mgc_help.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM MGC](../mgc-help/mgc.htm) > Acquisition Device Definition for HBM MGC

Acquisition Device Definition for HBM MGC

The HBM MGC device driver operates the measurement amplifier MGC from Hottinger Baldwin Messtechnik (HBM).

#### Settings

| Name | Name of the device definition |
| --- | --- |
| Driver | Selected device driver HBM MGC |
|  | The selected device determines which signal types (for example, gross, S2 net) are available. |
| Device parameters | Hardware-specific settings for the HBM MGC device driver (for example, interface, MGC setup). Special help sections for the boards list the device parameters. |

The IEEE 488 bus or the V.24 interface connect the measurement amplification system to the computer. You must install the appropriate interface board to operate the measurement amplifier over the IEEE 488 bus.

When the measurement starts, DIAdem checks the parameters of the driver.

#### See Also

[General Help for Device Settings](../dlgdacsv/dac_dlg_general/geraetedefinition.htm)

[Acquisition Signal Parameters for HBM MGC](../mgc-help/erf_par_mgc_help.htm)

<!--NI_TOPIC bundle=diadem path=mgc-help/erf_par_mgc_help.htm language=enus -->
## TOPIC 01396: Acquisition Signal Parameters for HBM MGC

- bundle_id: `diadem`
- source_path: `mgc-help/erf_par_mgc_help.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/mgc-help/erf_par_mgc_help.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM MGC](../mgc-help/mgc.htm) > Acquisition Signal Parameters for HBM MGC

Acquisition Signal Parameters for HBM MGC

The HBM MGC device driver operates the measurement amplifier MGC from Hottinger Baldwin Messtechnik (HBM).

The MGC measurement amplification system returns up to four measured values and additional information for each amplifier unit or each plug-in board, through four limit switches. Therefore DIAdem DAC acquires up to eight different signals for each device.

The parameter settings that you need for the signal types are listed in the following.

#### Settings

| Signal type | Name of the signal type |
| --- | --- |
| Device | Name of the device definition |
| Signal type/parameters | Software-controlled parameters for the plug-in boards. Possible settings are listed in the following. |
| Device | Opens the dialog box where you set the device parameters. |

#### Signal Types for the Measurement Amplifiers or Plug-In Boards

| S1 gross | Measures the gross signal. |
| --- | --- |
| S2 net | Measures the gross signal converted by a tare value. |
| S3 peak 1 | Measures the peak values from the first peak-value storage saved in the amplifier |
| S4 peak 2 | Measures the peak values from the second peak-value storage saved in the amplifier |
| GW1 | Measures the status of the first limit switch |
| GW2 | Measures the status of the second limit switch. |
| GW3 | Measures the status of the third limit switch. |
| GW4 | Measures the status of the fourth limit switch. |

When the measurement starts, DIAdem checks the parameters of the driver.

#### See Also

[General Help for Device Settings](../dlgdacsv/dac_dlg_general/geraetedefinition.htm)

[Acquisition Device Definition for HBM MGC](../mgc-help/erf_mgc_help.htm)

<!--NI_TOPIC bundle=diadem path=mgc-help/mc01.htm language=enus -->
## TOPIC 01397: Supported Functions of the MC01 Board

- bundle_id: `diadem`
- source_path: `mgc-help/mc01.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/mgc-help/mc01.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM MGC](../mgc-help/mgc.htm) > Supported Functions of the MC01 Board

Supported Functions of the MC01 Board

The following section lists the device parameter settings and DIAdem-supported functions of the MC01 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for MGC

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. |
| --- | --- |
| IEEE address | If you want to exchange data using the IEEE 488 bus, enter the device address set on the MGC. Valid entries range from 701 to 730. |
| MGC setup | This parameter specifies the driver behavior during the measurement preparations. The following settings are possible |
|  | No file handling |
|  | Use the setup currently selected for the MGC. You must make the settings on the MGC before the measurement starts, because during the measurement the fields in the dialog box are disabled. |
|  | MGC -» File |
|  | Use the setup currently selected for the MGC. The entire MGC setup is also written to a file and saved. This can be reread and sent to the MGC. |
|  | File -» MGC |
|  | The MGC configurations saved as files can be read and sent to the individual amplifiers. The amplifier settings are then compared to the setup settings. If there are differences, you can change the amplifier settings. This applies only to the amplifiers activated when the check is made. |
| Filename | Name of the MGC setup file |
| Peak values | Peak values can be deleted at the beginning of the measurement. |

#### Features of the MC01 Plug-In Board

The MC01 plug-in board functions that DIAdem supports are listed in the following.

Sensor

| DC signals: | Yes |
| --- | --- |
| Thermocouples: | J, K, T, S |
| Measurement ranges |  |
| Voltage: | ±0.4 - 12V |
| Current: | ±2 - 60 mA |

#### See Also

[Device Parameters for HBM MGC](../mgc-help/trb_par_mgc_help.htm)

[Acquisition Device Definition for HBM MGC](../mgc-help/erf_mgc_help.htm)

[Acquisition Signal Parameters for HBM MGC](../mgc-help/erf_par_mgc_help.htm)

<!--NI_TOPIC bundle=diadem path=mgc-help/mc30.htm language=enus -->
## TOPIC 01398: Supported Functions of the MC30 Plug-In Board

- bundle_id: `diadem`
- source_path: `mgc-help/mc30.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/mgc-help/mc30.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM MGC](../mgc-help/mgc.htm) > Supported Functions of the MC30 Plug-In Board

Supported Functions of the MC30 Plug-In Board

The following section lists the device parameter settings and DIAdem-supported functions of the MC30 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for MGC

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. |
| --- | --- |
| IEEE address | If you want to exchange data using the IEEE 488 bus, enter the device address set on the MGC. Valid entries range from 701 to 730. |
| MGC setup | This parameter specifies the driver behavior during the measurement preparations. The following settings are possible |
|  | No file handling |
|  | Use the setup currently selected for the MGC. You must make the settings on the MGC before the measurement starts, because during the measurement the fields in the dialog box are disabled. |
|  | MGC -» File |
|  | Use the setup currently selected for the MGC. The entire MGC setup is also written to a file and saved. This can be reread and sent to the MGC. |
|  | File -» MGC |
|  | The MGC configurations saved as files can be read and sent to the individual amplifiers. The amplifier settings are then compared to the setup settings. If there are differences, you can change the amplifier settings. This applies only to the amplifiers activated when the check is made. |

| Filename | Name of the MGC setup file |
| --- | --- |
| Peak values | Peak values can be deleted at the beginning of the measurement. |

#### Features of the MC30 Plug-In Board

The functions of the MC30 plug-in board that DIAdem supports are listed in the following.

Sensor

| Strain gauge full bridge: | 30 Ohm- 5 kOhm |
| --- | --- |

Measurement ranges:

| Strain gauge bridges: | ±0.1 - 15mV/V |
| --- | --- |
| Carrier frequency for measurement bridges | 600 Hz |
| Bridge supply voltage | 1V, 2.5V, 5V |

#### See Also

[Device Parameters for HBM MGC](../mgc-help/trb_par_mgc_help.htm)

[Acquisition Device Definition for HBM MGC](../mgc-help/erf_mgc_help.htm)

[Acquisition Signal Parameters for HBM MGC](../mgc-help/erf_par_mgc_help.htm)

<!--NI_TOPIC bundle=diadem path=mgc-help/mc50.htm language=enus -->
## TOPIC 01399: Supported Functions of the MC50 Plug-In

- bundle_id: `diadem`
- source_path: `mgc-help/mc50.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/mgc-help/mc50.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM MGC](../mgc-help/mgc.htm) > Supported Functions of the MC50 Plug-In

Supported Functions of the MC50 Plug-In

The following section lists the device parameter settings and DIAdem-supported functions of the MC50 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for MGC

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. |
| --- | --- |
| IEEE address | If you want to exchange data using the IEEE 488 bus, enter the device address set on the MGC. Valid entries range from 701 to 730. |
| MGC setup | This parameter specifies the driver behavior during the measurement preparations. The following settings are possible |
|  | No file handling |
|  | Use the setup currently selected for the MGC. You must make the settings on the MGC before the measurement starts, because during the measurement the fields in the dialog box are disabled. |
|  | MGC -» File |
|  | Use the setup currently selected for the MGC. The entire MGC setup is also written to a file and saved. This can be reread and sent to the MGC. |
|  | File -» MGC |
|  | The MGC configurations saved as files can be read and sent to the individual amplifiers. The amplifier settings are then compared to the setup settings. If there are differences, you can change the amplifier settings. This applies only to the amplifiers activated when the check is made. |

| Filename | Name of the MGC setup file |
| --- | --- |
| Peak values | Peak values can be deleted at the beginning of the measurement. |

#### Features of the MC50 Plug-In Board

The MC50 plug-in board functions that DIAdem supports are listed in the following.

Sensor

| Ind. Half bridge | 2.5 – 20 mH |
| --- | --- |

Measurement ranges:

| ind. Half bridge | ±6 - 400 mV/V |
| --- | --- |
| Carrier frequency for measurement bridges | 4800 Hz |
| Bridge supply voltage | 1V, 2.5V |

#### See Also

[Device Parameters for HBM MGC](../mgc-help/trb_par_mgc_help.htm)

[Acquisition Device Definition for HBM MGC](../mgc-help/erf_mgc_help.htm)

[Acquisition Signal Parameters for HBM MGC](../mgc-help/erf_par_mgc_help.htm)

<!--NI_TOPIC bundle=diadem path=mgc-help/mc55.htm language=enus -->
## TOPIC 01400: Supported Functions of the MC55 Plug-In Board

- bundle_id: `diadem`
- source_path: `mgc-help/mc55.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/mgc-help/mc55.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[HBM MGC](../mgc-help/mgc.htm) > Supported Functions of the MC55 Plug-In Board

Supported Functions of the MC55 Plug-In Board

The following section lists the device parameter settings and DIAdem-supported functions of the MC55 plug-in board from Hottinger Baldwin Measurement Technologies (HBM). For further information, refer to the technical documentation provided by your hardware manufacturer.

#### Device Parameters for MGC

| Interface | Specifies the interface (COM1, COM2, IEEE 488 bus) for data exchange. |
| --- | --- |
| IEEE address | If you want to exchange data using the IEEE 488 bus, enter the device address set on the MGC. Valid entries range from 701 to 730. |
| MGC setup | This parameter specifies the driver behavior during the measurement preparations. The following settings are possible |
|  | No file handling |
|  | Use the setup currently selected for the MGC. You must make the settings on the MGC before the measurement starts, because during the measurement the fields in the dialog box are disabled. |
|  | MGC -» File |
|  | Use the setup currently selected for the MGC. The entire MGC setup is also written to a file and saved. This can be reread and sent to the MGC. |
|  | File -» MGC |
|  | The MGC configurations saved as files can be read and sent to the individual amplifiers. The amplifier settings are then compared to the setup settings. If there are differences, you can change the amplifier settings. This applies only to the amplifiers activated when the check is made. |
|  |  |
| Filename | Name of the MGC setup file |
| Peak values | Peak values can be deleted at the beginning of the measurement. |

#### Functions of the MC55 Plug-In Board

The MC55 plug-in board functions that DIAdem supports are listed in the following.

Sensor

| Strain gauge full bridge | 30 Ohm- 5 kOhm |
| --- | --- |
| Strain gauge half bridge | 30 Ohm- 5 kOhm |
| Ind. Full bridge | 2.5m H |
| Ind. Half bridge | 2.5m H |

Measurement ranges:

| Strain gauge bridges | ±0.1 - 15 mV/V |
| --- | --- |
| ind. Bridge | ±3 - 220 mV/V |
| Carrier frequency for measurement bridges | 4800 Hz |
| Bridge supply voltage | 1V, 2.5V, 5V |

#### See Also

[Device Parameters for HBM MGC](../mgc-help/trb_par_mgc_help.htm)

[Acquisition Device Definition for HBM MGC](../mgc-help/erf_mgc_help.htm)

[Acquisition Signal Parameters for HBM MGC](../mgc-help/erf_par_mgc_help.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_colname.htm language=enus -->
## TOPIC 01401: Variable: SQL_ColName

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_colname.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_colname.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_ColName

Variable: SQL_ColName

Receives a vector with the names of the columns requested in the ODBC data store.

| Definition | SQL_ColName(i), String variablei = 1 ... 100 |
| --- | --- |
|  | Maximum 80 characters |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColType](../odbcsql/sql_coltype.htm) | [Variable: SQL_CommitVal](../odbcsql/sql_commitval.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_Table](../odbcsql/sql_table.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_TransactVal](../odbcsql/sql_transactval.htm) | [Variable: SQL_Type](../odbcsql/sql_type.htm) | [Variable: SQL_User](../odbcsql/sql_user.htm) | [Variable: SQL_Values](../odbcsql/sql_values.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_ExecDirect](../odbcsql/sql_execdirect.htm) | [Command: SQL_Select](../odbcsql/sql_select.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_coltype.htm language=enus -->
## TOPIC 01402: Variable: SQL_ColType

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_coltype.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_coltype.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_ColType

Variable: SQL_ColType

Receives a vector with the data types of the columns requested in the ODBC data store.

| Definition | SQL_ColType(i), Longinteger variablei = 1 ... 100 |
| --- | --- |
|  |  |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColName](../odbcsql/sql_colname.htm) | [Variable: SQL_CommitVal](../odbcsql/sql_commitval.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_Table](../odbcsql/sql_table.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_TransactVal](../odbcsql/sql_transactval.htm) | [Variable: SQL_Type](../odbcsql/sql_type.htm) | [Variable: SQL_User](../odbcsql/sql_user.htm) | [Variable: SQL_Values](../odbcsql/sql_values.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_ExecDirect](../odbcsql/sql_execdirect.htm) | [Command: SQL_Select](../odbcsql/sql_select.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_commitval.htm language=enus -->
## TOPIC 01403: Variable: SQL_CommitVal

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_commitval.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_commitval.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_CommitVal

Variable: SQL_CommitVal

Specifies the Commit mode.

| Definition | SQL_CommitVal, Longinteger variable |
| --- | --- |
|  |  |

The SQL_CommitVal variable can contain the following values:

| Value | Meaning |
| --- | --- |
| 0 | DIAdem does not make database modifications automatically. |
| 1 | DIAdem makes database modifications automatically. |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColName](../odbcsql/sql_colname.htm) | [Variable: SQL_ColType](../odbcsql/sql_coltype.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_Table](../odbcsql/sql_table.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_TransactVal](../odbcsql/sql_transactval.htm) | [Variable: SQL_Type](../odbcsql/sql_type.htm) | [Variable: SQL_User](../odbcsql/sql_user.htm) | [Variable: SQL_Values](../odbcsql/sql_values.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_AutoCommit](../odbcsql/sql_autocommit.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_connect.htm language=enus -->
## TOPIC 01404: Command: SQL_Connect

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_connect.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_connect.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Commands > Command: SQL_Connect

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: SQL_Connect

Connects DIAdem to an ODBC interface through an ODBC/SQL data store.

```text
Call SQL_Connect(SQL_DSNNAME, SQL_USER, SQL_PASSWORD, SQL_CONRESERVE)
```

#### Input Parameters

| SQL_DSNNAME | Specifies the name of an ODBC data store. String variable Maximum 80 characters |
| --- | --- |
| String variable |  |
| Maximum 80 characters |  |
| SQL_USER | Specifies the name of the user of an ODBC data store. String variable Maximum 80 characters |
| String variable |  |
| Maximum 80 characters |  |
| SQL_PASSWORD | Specifies the password for the user of an ODBC data store. String variable Maximum 80 characters |
| String variable |  |
| Maximum 80 characters |  |
| SQL_CONRESERVE | Specifies other parameters that are required for an ODBC data store, as a character string. String variable Maximum 80 characters |
| String variable |  |
| Maximum 80 characters |  |

#### Return Parameters

| SQL_ConnectStat | Receives the status of the connection to the ODBC data store. Boolean variable The SQL_ConnectStat variable can contain the following values: Value Meaning 0 The ODBC data storage is not connected. 1 The ODBC data storage is connected. |
| --- | --- |
| Boolean variable |  |
| Value | Meaning |
| 0 | The ODBC data storage is not connected. |
| 1 | The ODBC data storage is connected. |
| SQL_Stat | Receives the status of an SQL command. Longinteger variable The SQL_Stat variable can contain the following values: Value Meaning >=0 The operation was successful. <0 An error occurred. |
| Longinteger variable |  |
| Value | Meaning |
| >=0 | The operation was successful. |
| <0 | An error occurred. |

|  | Note Refer to the page on The ODBC/SQL Interface for general information about the ODBC/SQL commands. The SQL Script Command Examples show how to use the ODBC/SQL commands. |
| --- | --- |

|  | Note Use the ADO interface to access databases in VBS. |
| --- | --- |

#### Example

The following example opens the Example.mdb data store and transfers the data from the Speed column to the new MySpeed data channel in the Data Portal.

|  | Note Before you can use the example, you must first register the Example.mdb data store as an ODBC data source in the DIAdem NAVIGATOR demo path. |
| --- | --- |

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Data.Root.Clear()Call SQL_Connect("Example", "","","")
If (SQL_ConnectStat = true) Then
  Call SQL_ExecDirect("Select * From Example")
  If (SQL_Stat > 0) Then
    Call SQL_BindChannel("MySpeed","Speed","n")
    Do While SQL_Next
      Call SQL_FetchNext()
    Loop
  End If
  Call SQL_DisConnect
End If
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear()Call SQL_Connect("Example", "","","") 
if (SQL_ConnectStat == True) : 
    SQL_ExecDirect("Select * From Example") 
    if (SQL_Stat > 0) : 
        SQL_BindChannel("MySpeed","Speed","n") 
        while Do : 
            SQL_FetchNext() 
    SQL_DisConnect 
```

#### Related Topics

[Command: SQL_BindChannel](../odbcsql/sql_bindchannel.htm) | [Command: SQL_BindTextChn](../odbcsql/sql_bindtextchn.htm) | [Command: SQL_BindVar](../odbcsql/sql_bindvar.htm) | [Command: SQL_Disconnect](../odbcsql/sql_disconnect.htm) | [Command: SQL_UnBindVar](../odbcsql/sql_unbindvar.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_table.htm language=enus -->
## TOPIC 01405: Variable: SQL_Table

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_table.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_table.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_Table

Variable: SQL_Table

Specifies the name of a table in the ODBC data store.

| Definition | SQL_Table, String variable |
| --- | --- |
|  | Maximum 80 characters |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColName](../odbcsql/sql_colname.htm) | [Variable: SQL_ColType](../odbcsql/sql_coltype.htm) | [Variable: SQL_CommitVal](../odbcsql/sql_commitval.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_TransactVal](../odbcsql/sql_transactval.htm) | [Variable: SQL_Type](../odbcsql/sql_type.htm) | [Variable: SQL_User](../odbcsql/sql_user.htm) | [Variable: SQL_Values](../odbcsql/sql_values.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_Delete](../odbcsql/sql_delete.htm) | [Command: SQL_Insert](../odbcsql/sql_insert.htm) | [Command: SQL_Select](../odbcsql/sql_select.htm) | [Command: SQL_Update](../odbcsql/sql_update.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_transactval.htm language=enus -->
## TOPIC 01406: Variable: SQL_TransactVal

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_transactval.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_transactval.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_TransactVal

Variable: SQL_TransactVal

Specifies whether DIAdem makes a specified change to an ODBC data store, or undoes a specified change.

| Definition | SQL_TransactVal, String variable |
| --- | --- |
|  | Maximum 80 characters |

The SQL_TransActVal variable can contain the following values:

| Value | Meaning |
| --- | --- |
| Commit | DIAdem makes a specified change. |
| Rollback | DIAdem undoes a specified change. |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColName](../odbcsql/sql_colname.htm) | [Variable: SQL_ColType](../odbcsql/sql_coltype.htm) | [Variable: SQL_CommitVal](../odbcsql/sql_commitval.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_Table](../odbcsql/sql_table.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_Type](../odbcsql/sql_type.htm) | [Variable: SQL_User](../odbcsql/sql_user.htm) | [Variable: SQL_Values](../odbcsql/sql_values.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_Transact](../odbcsql/sql_transact.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_type.htm language=enus -->
## TOPIC 01407: Variable: SQL_Type

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_type.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_type.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_Type

Variable: SQL_Type

Specifies the data type of a GPI variable.

| Definition | SQL_Type, String variable |
| --- | --- |
|  | Maximum 80 characters |

The SQL_Type variable can contain the following values:

| Value | Meaning |
| --- | --- |
| B | Specifies a Boolean variable. |
| F | Specifies a Text variable. |
| L | Specifies a Longinteger variable. |
| R | Specifies a floating-point number. |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColName](../odbcsql/sql_colname.htm) | [Variable: SQL_ColType](../odbcsql/sql_coltype.htm) | [Variable: SQL_CommitVal](../odbcsql/sql_commitval.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_Table](../odbcsql/sql_table.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_TransactVal](../odbcsql/sql_transactval.htm) | [Variable: SQL_User](../odbcsql/sql_user.htm) | [Variable: SQL_Values](../odbcsql/sql_values.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_BindVar](../odbcsql/sql_bindvar.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_unbindvar.htm language=enus -->
## TOPIC 01408: Command: SQL_UnBindVar

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_unbindvar.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_unbindvar.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Commands > Command: SQL_UnBindVar

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: SQL_UnBindVar

Releases a variable created with the [SQL_Bindvar](../odbcsql/sql_bindvar.htm) command.

```text
Call SQL_UnBindVar(SQL_VARNAM)
```

#### Input Parameters

| SQL_VARNAM | Specifies the name of a GPI variable. String variable Maximum 80 characters |
| --- | --- |
| String variable |  |
| Maximum 80 characters |  |

|  | Note Refer to the page on The ODBC/SQL Interface for general information about the ODBC/SQL commands. The SQL Script Command Examples show how to use the ODBC/SQL commands. |
| --- | --- |

|  | Note Use the ADO interface to access databases in VBS. |
| --- | --- |

#### Related Topics

[Command: SQL_BindChannel](../odbcsql/sql_bindchannel.htm) | [Command: SQL_BindTextChn](../odbcsql/sql_bindtextchn.htm) | [Command: SQL_BindVar](../odbcsql/sql_bindvar.htm) | [Command: SQL_Connect](../odbcsql/sql_connect.htm) | [Command: SQL_Disconnect](../odbcsql/sql_disconnect.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_update.htm language=enus -->
## TOPIC 01409: Command: SQL_Update

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_update.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_update.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Commands > Command: SQL_Update

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: SQL_Update

Modifies data in the table of an ODBC data store.

```text
Call SQL_Update(SQL_TABLE, SQL_COLLIST, SQL_VALUES, SQL_WHERE, SQL_WHEREEX)
```

#### Input Parameters

| SQL_TABLE | Specifies the name of a table in the ODBC data store. String variable Maximum 80 characters |
| --- | --- |
| String variable |  |
| Maximum 80 characters |  |
| SQL_COLLIST | Specifies the names of columns in an ODBC data store. String variable Maximum 80 characters |
| String variable |  |
| Maximum 80 characters |  |
| SQL_VALUES | Specifies values separated by commas. String variable Maximum 80 characters |
| String variable |  |
| Maximum 80 characters |  |
| SQL_WHERE | Specifies a condition. String variable Maximum 80 characters |
| String variable |  |
| Maximum 80 characters |  |
| SQL_WHEREEX | Specifies further SQL parameters. String variable Maximum 80 characters |
| String variable |  |
| Maximum 80 characters |  |

|  | Note The SQL_Update command creates an SQL string in the following form: UPDATE <Table> SET <Column>=<Value> WHERE <Condition> <Other parameters>. |
| --- | --- |

#### Return Parameters

| SQL_ResultRows | Receives the number of modified rows in the ODBC data store. Longinteger variable |
| --- | --- |
| Longinteger variable |  |
| SQL_Stat | Receives the status of an SQL command. Longinteger variable The SQL_Stat variable can contain the following values: Value Meaning >=0 The operation was successful. <0 An error occurred. |
| Longinteger variable |  |
| Value | Meaning |
| >=0 | The operation was successful. |
| <0 | An error occurred. |

|  | Note Refer to the page on The ODBC/SQL Interface for general information about the ODBC/SQL commands. The SQL Script Command Examples show how to use the ODBC/SQL commands. |
| --- | --- |
|  | Note Use the ADO interface to access databases in VBS. |

#### Example

The following example reads the channels Time, Pressure, and Acceleration from the DB1 data store and loads these channels to the Data Portal. The SQL_Update command modifies values in the Pressure column of the Measurement1 table. Refer to [SQL Script Command Examples](../odbcsql/sql_example.htm), Example 1, for more information.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call SQL_Connect("DB1","User1","","")
Call SQL_AutoCommit(0)
Call SQL_Select("Time,Pressure,Acceleration","Measurement1","Time>10 ORDER BY Time","")
T1 = SQL_Result(3,2)
T2 = SQL_ColName(1)
Call SQL_BindVar("Pressure","TestVariable","R","APPEND")
L1 = SQL_ResultRows
Call SQL_BindChannel("3","Acceleration","n")
Call SQL_BindChannel("Time1","Time","n")
Do While (SQL_Next)
  Call SQL_FetChNext()
Loop
Call SQL_Update("Measurement1","Pressure","0.7","Time=7","")
Call SQL_Transact("Rollback")
Call SQL_Update("Measurement1","Pressure","7.0","Time=7","")
Call SQL_Transact("Commit")
Call SQL_Insert("Measurement1","Time,Pressure","1200,0.12")
Call SQL_Transact("Commit")
Call SQL_Delete("Measurement","Time > 1000","")
Call SQL_Transact("Commit")
L1 = SQL_ResultRows
Call SQL_ExecDirect("DROP TABLE Measurement1","","","")
Call SQL_Disconnect
```

[Copy script](javascript:void(0);)

```text
SQL_Connect("DB1","User1","","") 
SQL_AutoCommit(0) 
SQL_Select("Time,Pressure,Acceleration","Measurement1","Time>10 ORDER BY Time","") 
T1 = SQL_Result(3,2) 
T2 = SQL_ColName(1) 
SQL_BindVar("Pressure","TestVariable","R","APPEND") 
L1 = SQL_ResultRows 
SQL_BindChannel("3","Acceleration","n") 
SQL_BindChannel("Time1","Time","n") 
while Do : 
    SQL_FetChNext() 
SQL_Update("Measurement1","Pressure","0.7","Time=7","") 
SQL_Transact("Rollback") 
SQL_Update("Measurement1","Pressure","7.0","Time=7","") 
SQL_Transact("Commit") 
SQL_Insert("Measurement1","Time,Pressure","1200,0.12") 
SQL_Transact("Commit") 
SQL_Delete("Measurement","Time > 1000","") 
SQL_Transact("Commit") 
L1 = SQL_ResultRows 
SQL_ExecDirect("DROP TABLE Measurement1","","","") 
SQL_Disconnect 
```

#### Related Topics

[Command: SQL_AutoCommit](../odbcsql/sql_autocommit.htm) | [Command: SQL_Delete](../odbcsql/sql_delete.htm) | [Command: SQL_ExecDirect](../odbcsql/sql_execdirect.htm) | [Command: SQL_FetchNext](../odbcsql/sql_fetchnext.htm) | [Command: SQL_Insert](../odbcsql/sql_insert.htm) | [Command: SQL_Select](../odbcsql/sql_select.htm) | [Command: SQL_Transact](../odbcsql/sql_transact.htm) | [Examples](../odbcsql/sql_example.htm) | [ODBC/SQL](../odbcsql/odbcsql.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_user.htm language=enus -->
## TOPIC 01410: Variable: SQL_User

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_user.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_user.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_User

Variable: SQL_User

Specifies the name of the user of an ODBC data store.

| Definition | SQL_User, String variable |
| --- | --- |
|  | Maximum 80 characters |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColName](../odbcsql/sql_colname.htm) | [Variable: SQL_ColType](../odbcsql/sql_coltype.htm) | [Variable: SQL_CommitVal](../odbcsql/sql_commitval.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_Table](../odbcsql/sql_table.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_TransactVal](../odbcsql/sql_transactval.htm) | [Variable: SQL_Type](../odbcsql/sql_type.htm) | [Variable: SQL_Values](../odbcsql/sql_values.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_Connect](../odbcsql/sql_connect.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=odbcsql/odbcsql/sql_values.htm language=enus -->
## TOPIC 01411: Variable: SQL_Values

- bundle_id: `diadem`
- source_path: `odbcsql/odbcsql/sql_values.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/odbcsql/odbcsql/sql_values.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Variables > Variable: SQL_Values

Variable: SQL_Values

Specifies values separated by commas.

| Definition | SQL_Values, String variable |
| --- | --- |
|  | Maximum 80 characters |

#### Related Topics

[Variable: SQL_BindMethodE](../odbcsql/sql_bindmethode.htm) | [Variable: SQL_BlockSize](../odbcsql/sql_blocksize.htm) | [Variable: SQL_ColList](../odbcsql/sql_collist.htm) | [Variable: SQL_ColName](../odbcsql/sql_colname.htm) | [Variable: SQL_ColType](../odbcsql/sql_coltype.htm) | [Variable: SQL_CommitVal](../odbcsql/sql_commitval.htm) | [Variable: SQL_ConnectStat](../odbcsql/sql_connectstat.htm) | [Variable: SQL_ConReserve](../odbcsql/sql_conreserve.htm) | [Variable: SQL_DSNName](../odbcsql/sql_dsnname.htm) | [Variable: SQL_IsSelected](../odbcsql/sql_isselected.htm) | [Variable: SQL_Next](../odbcsql/sql_next.htm) | [Variable: SQL_NumOrTime](../odbcsql/sql_numortime.htm) | [Variable: SQL_Password](../odbcsql/sql_password.htm) | [Variable: SQL_Result](../odbcsql/sql_result.htm) | [Variable: SQL_ResultCols](../odbcsql/sql_resultcols.htm) | [Variable: SQL_ResultRows](../odbcsql/sql_resultrows.htm) | [Variable: SQL_SQLString](../odbcsql/sql_sqlstring.htm) | [Variable: SQL_Stat](../odbcsql/sql_stat.htm) | [Variable: SQL_String1](../odbcsql/sql_string1.htm) | [Variable: SQL_String2](../odbcsql/sql_string2.htm) | [Variable: SQL_String3](../odbcsql/sql_string3.htm) | [Variable: SQL_String4](../odbcsql/sql_string4.htm) | [Variable: SQL_Table](../odbcsql/sql_table.htm) | [Variable: SQL_TimeFormat](../odbcsql/sql_timeformat.htm) | [Variable: SQL_TransactVal](../odbcsql/sql_transactval.htm) | [Variable: SQL_Type](../odbcsql/sql_type.htm) | [Variable: SQL_User](../odbcsql/sql_user.htm) | [Variable: SQL_VarNam](../odbcsql/sql_varnam.htm) | [Variable: SQL_Where](../odbcsql/sql_where.htm) | [Variable: SQL_WhereEx](../odbcsql/sql_whereex.htm)

#### Used by

[Command: SQL_Insert](../odbcsql/sql_insert.htm) | [Command: SQL_Update](../odbcsql/sql_update.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chncommentset_itodatasheet.htm language=enus -->
## TOPIC 01412: Method: ChnCommentSet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chncommentset_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chncommentset_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnCommentSet for TODataSheet

Method: ChnCommentSet for TODataSheet

Sets a channel comment.

```text
iChnCommentSet = Object.ChnCommentSet(vChnV, sgCommentV)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| sgCommentV | StringSpecifies the new channel comment. |
| iChnCommentSet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example sets the comment of the Time channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnCommentSet("Time","Comment")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnCommentSet("Time","Comment") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chndatatypeget_itodatasheet.htm language=enus -->
## TOPIC 01413: Method: ChnDataTypeGet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chndatatypeget_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chndatatypeget_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnDataTypeGet for TODataSheet

Method: ChnDataTypeGet for TODataSheet

Reads the channel data type.

```text
iChnDataTypeGet = Object.ChnDataTypeGet(vChnV, vDataTypeP)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| vDataTypeP | VariantReceives the data type of the channel. |
| iChnDataTypeGet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example reads the data type of the Time channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess, vChannel, vDataTypeP
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnDataTypeGet("Time", vDataTypeP)
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnDataTypeGet("Time", vDataTypeP) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chndatatypeset_itodatasheet.htm language=enus -->
## TOPIC 01414: Method: ChnDataTypeSet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chndatatypeset_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chndatatypeset_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnDataTypeSet for TODataSheet

Method: ChnDataTypeSet for TODataSheet

Sets the display format of a channel.

```text
iChnDataTypeSet = Object.ChnDataTypeSet(vChnV, DataTypeV)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| DataTypeV | StringSpecifies the display format of the channel.Possible data types are: "Time", "Numeric". |
| iChnDataTypeSet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example sets the data type of the Time channel to Numeric:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem. ChnDataTypeSet("Time", "Numeric")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem. ChnDataTypeSet("Time", "Numeric") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chndimget_itodatasheet.htm language=enus -->
## TOPIC 01415: Method: ChnDimGet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chndimget_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chndimget_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnDimGet for TODataSheet

Method: ChnDimGet for TODataSheet

Reads a channel unit.

```text
iChnDimGet = Object.ChnDimGet(vChnV, vDimensionP)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| vDimensionP | VariantReceives the unit. |
| iChnDimGet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example returns the unit of the Time channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess, vUnitP 
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnDimGet("Time",vUnitP)
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnDimGet("Time",vUnitP) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chndimset_itodatasheet.htm language=enus -->
## TOPIC 01416: Method: ChnDimSet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chndimset_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chndimset_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnDimSet for TODataSheet

Method: ChnDimSet for TODataSheet

Sets the unit in a channel.

```text
iChnDimSet = Object.ChnDimSet(vChnV, sgDimensionV)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| sgDimensionV | StringSpecifies the unit. |
| iChnDimSet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example sets the unit of the Time channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnDimSet("Time","s")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnDimSet("Time","s") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chnlengthget_itodatasheet.htm language=enus -->
## TOPIC 01417: Method: ChnLengthGet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chnlengthget_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chnlengthget_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnLengthGet for TODataSheet

Method: ChnLengthGet for TODataSheet

Reads the channel length.

```text
iChnLengthGet = Object.ChnLengthGet(vChnV, vLengthP)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| vLengthP | VariantReceives the channel length. |
| iChnLengthGet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example returns the maximum channel length of the Time channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess, vMaxLengthP
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.MaxChnLengthGet(1,vMaxLengthP)
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.MaxChnLengthGet(1,vMaxLengthP) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chnlengthset_itodatasheet.htm language=enus -->
## TOPIC 01418: Method: ChnLengthSet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chnlengthset_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chnlengthset_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnLengthSet for TODataSheet

Method: ChnLengthSet for TODataSheet

Sets the channel length.

```text
iChnLengthSet = Object.ChnLengthSet(vChnV, nLengthV)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| nLengthV | LongIntegerSpecifies the new channel length. The channel length must not exceed the maximum channel length. You can request the maximum channel length with MaxChnLengthGet. |
| iChnLengthSet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example sets the length of the Time channel to the value 10.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnLengthSet("Time",10)
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnLengthSet("Time",10) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chnnameget_itodatasheet.htm language=enus -->
## TOPIC 01419: Method: ChnNameGet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chnnameget_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chnnameget_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnNameGet for TODataSheet

Method: ChnNameGet for TODataSheet

Reads a channel name.

```text
iChnNameGet = Object.ChnNameGet(vChnV, vNameP)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| vNameP | VariantReceives the channel name. |
| iChnNameGet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example returns the name of channel 5:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess, vNameV
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnNameGet(5,vNameV)
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnNameGet(5,vNameV) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chnnameset_itodatasheet.htm language=enus -->
## TOPIC 01420: Method: ChnNameSet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chnnameset_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chnnameset_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnNameSet for TODataSheet

Method: ChnNameSet for TODataSheet

Sets a channel name.

```text
iChnNameSet = Object.ChnNameSet(vChnV, sgNameV)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vChnV | VariantSpecifies the channel number or the channel name. |
| sgNameV | StringSpecifies the new channel name. |
| iChnNameSet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example changes the name of the Time channel to NewTime:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnNameSet("Time","NewTime")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnNameSet("Time","NewTime") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chnparamsupdate_itodatasheet.htm language=enus -->
## TOPIC 01421: Method: ChnParamsUpdate for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chnparamsupdate_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chnparamsupdate_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnParamsUpdate for TODataSheet

Method: ChnParamsUpdate for TODataSheet

Refreshes the characteristic values of channels.

```text
iChnParamsUpdate = Object.ChnParamsUpdate(vStartChnV, vEndChnV)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| vStartChnV | VariantSpecifies the number or the name of the start channel. |
| vEndChnV | VariantSpecifies the number or the name of the end channel. |
| iChnParamsUpdate | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

The following example refreshes the characteristic values of channels 1 to 12 and of channels time to torque.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnParamsUpdate(1,12)
  'Using channel names:
  iSuccess = oDIAdem.ChnParamsUpdate("Time", "Torque")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnParamsUpdate(1,12) 
#Using channel names:
    iSuccess = oDIAdem.ChnParamsUpdate("Time", "Torque") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chnvalget_itodatasheet.htm language=enus -->
## TOPIC 01422: Method: ChnValGet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chnvalget_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chnvalget_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnValGet for TODataSheet

Method: ChnValGet for TODataSheet

Reads a single channel value.

```text
iChnValGet = Object.ChnValGet(nRowV, vChnV, vValueP)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| nRowV | LongIntegerSpecifies the line number. Possible values are between 1 and the maximum channel length |
| vChnV | VariantSpecifies the channel number or the channel name.If two channels with the same name exist, DIAdem selects the first channel. If no channel with this name exists, DIAdem returns an error message. |
| vValueP | VariantReceives the variable value. For a NoValue value, DIAdem returns the "NOVALUE" string. |
| iChnValGet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example reads the first 10 values of the Time channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess, vValueP, lCountT
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  For lCountT = 1 To 10
    iSuccess = oDIAdem.ChnValGet(lCountT,"Time", vValueP)
  Next
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    for lCountT in range( 1, 10 + 1): 
        iSuccess = oDIAdem.ChnValGet(lCountT,"Time", vValueP) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/methods/ole_method_chnvalset_itodatasheet.htm language=enus -->
## TOPIC 01423: Method: ChnValSet for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/methods/ole_method_chnvalset_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/methods/ole_method_chnvalset_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Methods](../methods/ole_method_overview.htm) > Method: ChnValSet for TODataSheet

Method: ChnValSet for TODataSheet

Sets a single channel value.

```text
iChnValSet = Object.ChnValSet(nRowV, vChnV, vValueV)
```

| Object | TODataSheetObject with this method |
| --- | --- |
| nRowV | LongIntegerSpecifies the line number. Possible values are between 1 and the maximum channel length |
| vChnV | VariantSpecifies the channel number or the channel name.If two channels with the same name exist, DIAdem selects the first channel. If no channel with this name exists, DIAdem returns an error message. |
| vValueV | VariantSpecifies the variable value. The possible value is the new value of the channel. To set the NOVALUE value, transfer the "NoValue" or "NV" string. |
| iChnValSet | LongIntegerDIAdem return value that indicates whether the command has executed successfully.The value is 1 if the command has executed successfully. The value is 0 if the command has not executed successfully. |

#### Example

The following example sets the first 10 values of the Timechannel to values from 10 to 100:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess, lCountT
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
If Not oDIAdem.bInterfaceLocked then
  For lCountT = 1 To 10
    iSuccess = oDIAdem.ChnValSet(lCountT,"Time", lCountT*10)
  Next
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
if not oDIAdem.bInterfaceLocked : 
    for lCountT in range( 1, 10 + 1): 
        iSuccess = oDIAdem.ChnValSet(lCountT,"Time", lCountT*10) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/objects/ole_set_date.htm language=enus -->
## TOPIC 01424: Setting a Date in DIAdem through the OLE Interface

- bundle_id: `diadem`
- source_path: `ole/objects/ole_set_date.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/objects/ole_set_date.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > Setting a Date in DIAdem through the OLE Interface

Setting a Date in DIAdem through the OLE Interface

You transfer a date value as the variant-date or as variant-double. If you transfer the date value as a variant-double, DIAdem interprets the value 0.0 in relation to the variable [ApplicationTimebaseHighResolution](../../varoff/applicationtimebasehighresolution.htm). The transferred double value is then automatically converted into the DIAdem date format.

As DIAdem may assume another reference point than the one used in your programming language, such as Visual Basic or C++, you may have to take this into account in your code, and correct it by adding or subtracting a constant.

Also note that in DIAdem a second corresponds to a 1, which is not necessarily the same in other programming languages.

A date value can only be set in channels that are defined as time channels.

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bdontcloseapplication_itocommand.htm language=enus -->
## TOPIC 01425: Property: bDontCloseApplication for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bdontcloseapplication_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bdontcloseapplication_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bDontCloseApplication for TOCommand

Property: bDontCloseApplication for TOCommand

Prevents DIAdem from closing automatically after DIAdem ends the OLE connection.

```text
Object.bDontCloseApplication
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bDontCloseApplication | Boolean with read and write accessIf the value is True, DIAdem does not close. If the value is False, DIAdem closes.The default setting is False. |

The following example opens DIAdem, displays a message, and makes DIAdem visible again.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bDontCloseApplication = True
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.CmdExecuteSync("MsgBoxDisp('Hello World')")
  iSuccess = oDIAdem.CmdExecuteSync("wndshow('shell','normal')")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bDontCloseApplication = True 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.CmdExecuteSync("MsgBoxDisp('Hello World')") 
    iSuccess = oDIAdem.CmdExecuteSync("wndshow('shell','normal')") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_binterfacelocked_itocommand.htm language=enus -->
## TOPIC 01426: Property: bInterfaceLocked for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_binterfacelocked_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_binterfacelocked_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bInterfaceLocked for TOCommand

Property: bInterfaceLocked for TOCommand

Requests the status of the OLE interfaces from DIAdem. Always request the status of the DIAdem OLE interfaces before you execute an OLE command. If you send an OLE command to DIAdem although the property has the value True, the behavior of DIAdem is unpredictable.

```text
Object.bInterfaceLocked
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bInterfaceLocked | Boolean with read and write accessIf the value is True, the OLE interface of DIAdem is locked because DIAdem is not completely initialized, for example, a dialog box is open, or because a script is active in DIAdem. If the value is False, the OLE interface to DIAdem is not locked. In DIAdem 10.2 and earlier versions, DIAdem systematically locked OLE methods. From version 11, DIAdem does not automatically lock these methods, instead you must use the bInterfaceLocked property to request the status. |

Refer to [Controlling DIAdem with OLE](../../exploff/examples/example_ole.htm) for an example. The following example initializes the ToCommand interface and waits until the OLE interface is free:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Option Explicit
Dim oDIAdem, iSuccess
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bNoActivityDisplay = True
If Not oDIAdem.bInterfaceLocked then
  'Initialize TOCommand Interface:
  Do 
  Loop Until Not oDIAdem.bInterfaceLocked
  iSuccess = oDIAdem.CmdExecuteSync("wndshow('shell','normal')")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bNoActivityDisplay = True 
if not oDIAdem.bInterfaceLocked : 
#Initialize TOCommand Interface:
    while True: 
    if not oDIAdem.bInterfaceLocked:
            break 
    iSuccess = oDIAdem.CmdExecuteSync("wndshow('shell','normal')") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_binterfacelocked_itodatasheet.htm language=enus -->
## TOPIC 01427: Property: bInterfaceLocked for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_binterfacelocked_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_binterfacelocked_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bInterfaceLocked for TODataSheet

Property: bInterfaceLocked for TODataSheet

Requests the status of the OLE interfaces from DIAdem. Always request the status of the DIAdem OLE interfaces before you execute an OLE command. If you send an OLE command to DIAdem although the property has the value True, the behavior of DIAdem is unpredictable.

```text
Object.bInterfaceLocked
```

| Object | TODataSheetObject with this property |
| --- | --- |
| Object.bInterfaceLocked | Boolean with read and write accessIf the value is True, the OLE interface of DIAdem is locked because DIAdem is not completely initialized, for example, a dialog box is open, or because a script is active in DIAdem. If the value is False, the OLE interface to DIAdem is not locked. In DIAdem 10.2 and earlier versions, DIAdem systematically locked OLE methods. From version 11, DIAdem does not automatically lock these methods, instead you must use the bInterfaceLocked property to request the status. |

Refer to [Controlling DIAdem with OLE](../../exploff/examples/example_ole.htm) for an example. To set a channel comment, the following example initializes the ToDataSheet interface and waits until the OLE interface is free:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem, iSuccess, vCommentP
oDIAdem = CreateObject("DIAdem.TODataSheet")
Do
Loop Until Not oDIAdem.bInterfaceLocked
iSuccess = oDIAdem.ChnCommentGet(5, vCommentP)
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
while True: 
if not oDIAdem.bInterfaceLocked:
        break 
iSuccess = oDIAdem.ChnCommentGet(5, vCommentP) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnoactivitydisplay_itocommand.htm language=enus -->
## TOPIC 01428: Property: bNoActivityDisplay for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnoactivitydisplay_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnoactivitydisplay_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoActivityDisplay for TOCommand

Property: bNoActivityDisplay for TOCommand

Suppresses the DIAdem Tray icon. This is useful if you want to operate DIAdem as a server and achieve the highest possible performance.

```text
Object.bNoActivityDisplay
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bNoActivityDisplay | Boolean with read and write accessIf the value is True, the DIAdem Tray icon is suppressed. If the value is False, the DIAdem Tray icon is displayed. The default setting is False.The Tray icon is a symbol that appears in the Windows task bar if you instance DIAdem via an OLE interface. The symbol indicates that the operating system is running a DIAdem in the background. |

The following example sets the DIAdem variable SmoothWidth to 4. The DIAdem Tray icon is not displayed:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bNoActivityDisplay = True
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.IntegerVarSet("SmoothWidth",4)
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bNoActivityDisplay = True 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.IntegerVarSet("SmoothWidth",4) 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnoactivitydisplay_itodatasheet.htm language=enus -->
## TOPIC 01429: Property: bNoActivityDisplay for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnoactivitydisplay_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnoactivitydisplay_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoActivityDisplay for TODataSheet

Property: bNoActivityDisplay for TODataSheet

Suppresses the DIAdem Tray icon. This is useful if you want to operate DIAdem as a server and achieve the highest possible performance.

```text
Object.bNoActivityDisplay
```

| Object | TODataSheetObject with this property |
| --- | --- |
| Object.bNoActivityDisplay | Boolean with read and write accessIf the value is True, the DIAdem Tray icon is suppressed. If the value is False, the DIAdem Tray icon is displayed. The default setting is False.The Tray icon is a symbol that appears in the Windows task bar if you instance DIAdem via an OLE interface. The symbol indicates that the operating system is running a DIAdem in the background. |

The following example sets the comment of the Time channel. The DIAdem Tray icon is not displayed:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
oDIAdem.bNoActivityDisplay = True
If Not oDIAdem.bInterfaceLocked then
  iSuccess = oDIAdem.ChnCommentSet("Time","Comment")
End If
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
oDIAdem.bNoActivityDisplay = True 
if not oDIAdem.bInterfaceLocked : 
    iSuccess = oDIAdem.ChnCommentSet("Time","Comment") 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnodialogdisplay_itocommand.htm language=enus -->
## TOPIC 01430: Property: bNoDialogDisplay for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnodialogdisplay_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnodialogdisplay_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoDialogDisplay for TOCommand

Property: bNoDialogDisplay for TOCommand

Suppresses all DIAdem messages.

```text
Object.bNoDialogDisplay
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bNoDialogDisplay | Boolean with read and write accessIf the value is True, all messages are suppressed. If the value is False, all messages are displayed.The default setting is False. |

The following example suppresses all messages:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bNoDialogDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bNoDialogDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnodialogdisplay_itodatasheet.htm language=enus -->
## TOPIC 01431: Property: bNoDialogDisplay for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnodialogdisplay_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnodialogdisplay_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoDialogDisplay for TODataSheet

Property: bNoDialogDisplay for TODataSheet

Suppresses all DIAdem messages.

```text
Object.bNoDialogDisplay
```

| Object | TODataSheetObject with this property |
| --- | --- |
| Object.bNoDialogDisplay | Boolean with read and write accessIf the value is True, all messages are suppressed. If the value is False, all messages are displayed.The default setting is False. |

The following example suppresses all messages:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
oDIAdem.bNoDialogDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
oDIAdem.bNoDialogDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnoerrordisplay_itocommand.htm language=enus -->
## TOPIC 01432: Property: bNoErrorDisplay for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnoerrordisplay_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnoerrordisplay_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoErrorDisplay for TOCommand

Property: bNoErrorDisplay for TOCommand

Suppresses all DIAdem error messages.

```text
Object.bNoErrorDisplay
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bNoErrorDisplay | Boolean with read and write accessIf the value is True, all error messages are suppressed. If the value is False, all messages are displayed.The default setting is False. |

The following example suppresses all error messages:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bNoErrorDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bNoErrorDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnoerrordisplay_itodatasheet.htm language=enus -->
## TOPIC 01433: Property: bNoErrorDisplay for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnoerrordisplay_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnoerrordisplay_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoErrorDisplay for TODataSheet

Property: bNoErrorDisplay for TODataSheet

Suppresses all DIAdem error messages.

```text
Object.bNoErrorDisplay
```

| Object | TODataSheetObject with this property |
| --- | --- |
| Object.bNoErrorDisplay | Boolean with read and write accessIf the value is True, all error messages are suppressed. If the value is False, all messages are displayed.The default setting is False. |

The following example suppresses all error messages:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
oDIAdem.bNoErrorDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
oDIAdem.bNoErrorDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnoinfodisplay_itocommand.htm language=enus -->
## TOPIC 01434: Property: bNoInfoDisplay for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnoinfodisplay_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnoinfodisplay_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoInfoDisplay for TOCommand

Property: bNoInfoDisplay for TOCommand

Suppresses all DIAdem information messages.

```text
Object.bNoInfoDisplay
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bNoInfoDisplay | Boolean with read and write accessIf the value is True, all information messages are suppressed. If the value is False, all information messages are displayed.The default setting is False. |

The following example suppresses all information messages:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bNoInfoDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bNoInfoDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnoinfodisplay_itodatasheet.htm language=enus -->
## TOPIC 01435: Property: bNoInfoDisplay for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnoinfodisplay_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnoinfodisplay_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoInfoDisplay for TODataSheet

Property: bNoInfoDisplay for TODataSheet

Suppresses all DIAdem information messages.

```text
Object.bNoInfoDisplay
```

| Object | TODataSheetObject with this property |
| --- | --- |
| Object.bNoInfoDisplay | Boolean with read and write accessIf the value is True, all information messages are suppressed. If the value is False, all information messages are displayed.The default setting is False. |

The following example suppresses all information messages:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
oDIAdem.bNoInfoDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
oDIAdem.bNoInfoDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnomsgdisplay_itocommand.htm language=enus -->
## TOPIC 01436: Property: bNoMsgDisplay for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnomsgdisplay_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnomsgdisplay_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoMsgDisplay for TOCommand

Property: bNoMsgDisplay for TOCommand

Suppresses all DIAdem messages and dialog boxes.

```text
Object.bNoMsgDisplay
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bNoMsgDisplay | Boolean with read and write accessIf the value is True, all messages and dialog boxes are suppressed. If the value is False, all messages and dialog boxes are displayed.The default setting is False. |

The following example suppresses all messages and dialog boxes:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bNoMsgDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bNoMsgDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnomsgdisplay_itodatasheet.htm language=enus -->
## TOPIC 01437: Property: bNoMsgDisplay for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnomsgdisplay_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnomsgdisplay_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoMsgDisplay for TODataSheet

Property: bNoMsgDisplay for TODataSheet

Suppresses all DIAdem message boxes and dialog boxes. This behavior is useful if you want to operate DIAdem as a server.

```text
Object.bNoMsgDisplay
```

| Object | TODataSheetObject with this property |
| --- | --- |
| Object.bNoMsgDisplay | Boolean with read and write accessIf the value is True, all messages and dialog boxes are suppressed. If the value is False, all messages and dialog boxes are displayed.The default setting is False. |

The following example suppresses all messages and dialog boxes:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
oDIAdem.bNoMsgDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
oDIAdem.bNoMsgDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnowarningdisplay_itocommand.htm language=enus -->
## TOPIC 01438: Property: bNoWarningDisplay for TOCommand

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnowarningdisplay_itocommand.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnowarningdisplay_itocommand.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoWarningDisplay for TOCommand

Property: bNoWarningDisplay for TOCommand

Suppresses all DIAdem warnings.

```text
Object.bNoWarningDisplay
```

| Object | TOCommandObject with this property |
| --- | --- |
| Object.bNoWarningDisplay | Boolean with read and write accessIf the value is True, all warnings are suppressed. If the value is False, all warnings are displayed.The default setting is False. |

The following example suppresses all warnings:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TOCommand")
oDIAdem.bNoWarningDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TOCommand") 
oDIAdem.bNoWarningDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_bnowarningdisplay_itodatasheet.htm language=enus -->
## TOPIC 01439: Property: bNoWarningDisplay for TODataSheet

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_bnowarningdisplay_itodatasheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_bnowarningdisplay_itodatasheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > [Properties](../properties/ole_property_overview.htm) > Property: bNoWarningDisplay for TODataSheet

Property: bNoWarningDisplay for TODataSheet

Suppresses all DIAdem warnings.

```text
Object.bNoWarningDisplay
```

| Object | TODataSheetObject with this property |
| --- | --- |
| Object.bNoWarningDisplay | Boolean with read and write accessIf the value is True, all warnings are suppressed. If the value is False, all warnings are displayed.The default setting is False. |

The following example suppresses all warnings:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDIAdem
Set oDIAdem = CreateObject("DIAdem.TODataSheet")
oDIAdem.bNoWarningDisplay = True
```

[Copy script](javascript:void(0);)

```text
oDIAdem = win32com.client.dis-patch("DIAdem.TODataSheet") 
oDIAdem.bNoWarningDisplay = True 
```

#### See Also

[Objects Overview](../objects/itocommand_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=ole/properties/ole_property_overview.htm language=enus -->
## TOPIC 01440: Properties

- bundle_id: `diadem`
- source_path: `ole/properties/ole_property_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/ole/properties/ole_property_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OLE](../objects/ole_overview.htm) > Properties

Properties

The subordinate topics contained in the tree on the contents tab of the Help describe the properties of the OLE script interface for applications.

<!--NI_TOPIC bundle=diadem path=parallelprocesscontrol/methods/parallelprocesscontrol_method_geterrorflag_iworker.htm language=enus -->
## TOPIC 01441: Method: GetErrorFlag for Worker

- bundle_id: `diadem`
- source_path: `parallelprocesscontrol/methods/parallelprocesscontrol_method_geterrorflag_iworker.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/parallelprocesscontrol/methods/parallelprocesscontrol_method_geterrorflag_iworker.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: GetErrorFlag for Worker

Method: GetErrorFlag for Worker

Specifies the error status of the Worker object. Always create a procedure in the master which is called by [OnWorkerStateChange for ParallelProcessControl](../properties/parallelprocesscontrol_property_onworkerstatechange_iparallelprocesscontrol.htm) and checks the error status of the Worker object.

```text
bGetErrorFlag = Object.GetErrorFlag
```

| Object | WorkerObject with this method |
| --- | --- |
| bGetErrorFlag | Boolean |

The following example starts five Worker objects. The Worker objects execute the WorkerScript.vbs on the current path. After a Worker object has executed the script, it executes the CallbackFct user command in the master.

The Worker objects receive an array as transfer parameter. The content of the first array element is an array, which contains the values of a channel. The second array element contains the ID of the Worker object and the third array element contains the interval width for an RMS calculation.

As soon as a Worker object changes its status, DIAdem executes the CheckState user command. In this user command, you can check, for example, whether an error has occurred. The user commands are defined in the registered Callback.vbs file.

If none of the Workers are executing a script, DIAdem deletes all Worker objects. As soon as a worker has completed the WorkerScript.vbs script, DIAdem executes the user command CallbackFct in the master.

[Copy script](javascript:void(0);)

```text
Dim i, oMyWorker, MyArgArray(2)
Call Data.Root.Clear()
Call DataFileLoad("Example.tdm","TDM","")
Call ScriptCmdAdd(CurrentScriptPath & "Callback.vbs")
ParallelProcessControl.OnWorkerStateChange = "CheckState"
For i= 1 to Data.Root.ChannelGroups(2).Channels.Count
  Set oMyWorker = ParallelProcessControl.Workers.Add(i,true,"")
  MyArgArray(0) = ChannelsToArray("[2]/[" & i & "]")
  MyArgArray(1) = i
  MyArgArray(2) = 50
  oMyWorker.SetArgument(MyArgArray)
  Call oMyWorker.Run(CurrentScriptPath & "WorkerScript.vbs","CallbackFct")
Next
Do
  Call Pause(0.1)
Loop Until ParallelProcessControl.Workers.RunningWorkersCount < 1
Call ParallelProcessControl.Workers.RemoveAll()
```

The following script displays the WorkerScript.vbs script mentioned above. The Worker script converts the contents of the first array element back into a channel. The script uses the third argument as the parameter for an RMS calculation. The LocalWorker object transfers the calculation result through the [SetArgument for LocalWorker](../methods/parallelprocesscontrol_method_setargument_ilocalworker.htm) method to the master and the CallbackFct user command evaluates the result. The algorithm is not optimized but is only used as an example for the calculation.

[Copy script](javascript:void(0);)

```text
Dim oTempChannel, i, aInputArg, aResults(1)
Call DBM ("Worker " & LocalWorker.ID)
Call Data.Root.Clear()
aInputArg = LocalWorker.GetArgument

Call ArrayToChannels(aInputArg(0), Array("tempChannel"))
set oTempChannel = Data.GetChannel("/tempChannel")

Call RMS(oTempChannel,aInputArg(2))  ' Do some analysis

aResults(0) = ChannelsToArray("/tempChannel")
aResults(1) = aInputArg(1)
Call LocalWorker.SetArgument(aResults)

Sub RMS(Channel, Width)
Dim i, Sum, j
  For i = 1 + Width to Channel.Size - Width
    Sum = 0
    For j = i - Width to i
      Sum = Sum + Channel(j) * Channel(j)
    Next
    Channel(i-Width) = Sqr(Sum/Width)
  Next
End Sub
```

The following script displays the Callback.vbs script mentioned above. The user command CallbackFct displays the ID of the requesting Worker object and evaluates the transfer parameter. In this example the user command replaces the input channels with the calculation results. If the master executes user command instructions, you must ensure that the DIAdem environment matches because, for example, data might have been deleted, layouts changed, or a different panel used after you called the Worker object.

The CheckState user command checks whether an error occurs in the Worker object. If an error occurs, the user command instruction [DBM](../../comoff/dbm.htm) outputs the error description as a debug message and resets the error status.

[Copy script](javascript:void(0);)

```text
Sub CallbackFct(oWorker)
Dim aResults
  aResults = oWorker.GetArgument
  Call DBM("Worker ID: " & oWorker.ID & " Result#: " & aResults(1))
  Call ArrayToChannels(aResults(0),array("[2]/[" & aResults(1) & "]"),true)
End Sub
 
Sub CheckState(oWorker,iState)
  ' The following statement is not executed. It is only used for autocompletion.
  If False Then Set oWorker = ParallelProcessControl.Workers.Add(i,true,"")

  If oWorker.GetErrorFlag Then
    Call DBM ("Error: " & oWorker.GetErrorText)
    oWorker.ResetError
  End If  
  Select Case iState 
  Case eWorkerCreated
    Call DBM ("Status "& oWorker.ID & " Created")
  Case eWorkerScriptStarting
    Call DBM ("Status "& oWorker.ID & " Starting")
  Case eWorkerScriptFinished
    Call DBM ("Status "& oWorker.ID & " Finished")
  Case eWorkerRemoving
    Call DBM ("Status "& oWorker.ID & " Removing")
  End Select
End Sub
```

#### See Also

[Objects Overview](../objects/iparallelprocesscontrol_objects_overview.htm)

#### Examples

[Parallel File Analysis](../../exploff/examples/expl_seriesanalysis.htm) | [Vibration Data Analysis with Parallel Processing](../../exploff/examples/expl_rotatingshaftanalysis.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcommapp.htm language=enus -->
## TOPIC 01442: Variable: PkCommApp

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcommapp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcommapp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCommApp

Variable: PkCommApp

Specifies in packet processing the text to be appended to a file comment.

| Definition | PkCommApp, String variable |
| --- | --- |
|  | Maximum 80 characters |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCommApp = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcommnew.htm language=enus -->
## TOPIC 01443: Variable: PkCommNew

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcommnew.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcommnew.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCommNew

Variable: PkCommNew

Specifies in packet processing the comment to be saved with the data.

| Definition | PkCommNew, String variable |
| --- | --- |
|  | Maximum 80 characters |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCommNew = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcompany.htm language=enus -->
## TOPIC 01444: Variable: PkCompany

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcompany.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcompany.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCompany

Variable: PkCompany

Specifies in packet processing the company logo that is to be saved with the written data.

| Definition | PkCompany, String variable |
| --- | --- |
|  | Maximum 80 characters |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCompany = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcontrol.htm language=enus -->
## TOPIC 01445: Variable: PkControl

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcontrol.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcontrol.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkControl

Variable: PkControl

Specifies in packet processing the data output number at the demultiplexer for data output.

| Definition | PkControl, Boolean variable |
| --- | --- |
|  | 0 or 1 |

The PkControl variable can contain the following values:

| Value | Meaning |
| --- | --- |
| 0 | The PkActiveOut variable specifies the data output number. |
| 1 | The data packets at the control input continuously return the data output numbers. DIAdem creates the control input S only if you select this setting. |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkControl = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcountblocks.htm language=enus -->
## TOPIC 01446: Variable: PkCountBlocks

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcountblocks.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcountblocks.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCountBlocks

Variable: PkCountBlocks

Specifies the period in which the packet processing counter outputs data packets.

| Definition | PkCountBlocks, Word variable |
| --- | --- |
|  | 0 <= PkCountBlocks <= 2147483646 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCountBlocks = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Counter](../../dlgdacpp/dac_packet_dlg_math/hb_zaehler.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcountmode.htm language=enus -->
## TOPIC 01447: Variable: PkCountMode

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcountmode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcountmode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCountMode

Variable: PkCountMode

Specifies in packet processing whether the counter counts measurement values, data packets, or time spans.

| Definition | PkCountMode, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Value Meaning 1 Forward every n-th block 2 Count blocks 3 Count data values 4 HIGH level period length counter 5 HIGH level value counter |
| Value | Meaning |
| 1 | Forward every n-th block |
| 2 | Count blocks |
| 3 | Count data values |
| 4 | HIGH level period length counter |
| 5 | HIGH level value counter |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCountMode = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Counter](../../dlgdacpp/dac_packet_dlg_math/hb_zaehler.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcrossspectr.htm language=enus -->
## TOPIC 01448: Variable: PkCrossSpectr

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcrossspectr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcrossspectr.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCrossSpectr

Variable: PkCrossSpectr

Specifies in packet processing whether the FFT of two signals calculates the cross spectrum or the transfer function.

| Definition | PkCrossSpectr, Boolean variable |
| --- | --- |
|  | 0 or 1 |

The PkCrossSpectr variable can contain the following values:

| Value | Meaning |
| --- | --- |
| 0 | DIAdem calculates the cross spectrum as a complex product of the two time signals. |
| 1 | DIAdem calculates the complex transfer frequency response of the Fourier transformed input signals. |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCrossSpectr = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Two Signal FFT](../../dlgdacpp/dac_packet_dlg_math/hb_fft_zwei.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcursleft.htm language=enus -->
## TOPIC 01449: Variable: PkCursLeft

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcursleft.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcursleft.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCursLeft

Variable: PkCursLeft

Receives in packet processing the point number of the left cursor in the measurement data window of the oscilloscope.

| Definition | PkCursLeft, LongInteger variable |
| --- | --- |
|  | 0 <= PkCursLeft <= x-range in the oscilloscope |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCursLeft = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Cursor Window](../../dlgdacpp/dac_packet_osci/pk_oscilloscope_cursordisplay.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkcutofffreq.htm language=enus -->
## TOPIC 01450: Variable: PkCutoffFreq

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkcutofffreq.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkcutofffreq.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkCutoffFreq

Variable: PkCutoffFreq

Specifies in packet processing the 3 dB-limit frequency for highpass and lowpass digital filters.

| Definition | PkCutoffFreq, Integer variable |
| --- | --- |
|  | 0 < PkCutoffFreq <= 2000000000 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkCutoffFreq = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Digital Filters](../../dlgdacpp/dac_packet_dlg_math/hb_digfilt_neu.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkdataonreset.htm language=enus -->
## TOPIC 01451: Variable: PkDataOnReset

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkdataonreset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkdataonreset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkDataOnReset

Variable: PkDataOnReset

Specifies in packet processing whether DIAdem outputs the mean values of a FFT of two signals only after a reset. Use this variable to control the data flow in order to transfer data packets after a reset.

| Definition | PkDataOnReset, Boolean variable |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkDataOnReset = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Two Signal FFT](../../dlgdacpp/dac_packet_dlg_math/hb_fft_zwei.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkdatapklength.htm language=enus -->
## TOPIC 01452: Variable: PKDataPkLength

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkdatapklength.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkdatapklength.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PKDataPkLength

Variable: PKDataPkLength

Specifies in packet processing the number of values in a data packet.

| Definition | PKDataPkLength, Longinteger variable |
| --- | --- |
|  | 1 <= PKDataPkLength <= 1000000000 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkDataPkLength = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkdffunction.htm language=enus -->
## TOPIC 01453: Variable: PkFunction

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkdffunction.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkdffunction.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkFunction

Variable: PkFunction

Specifies in packet processing the IIR filter type for digital filters.

| Definition | PkFunction, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Butterworth 2 Bessel 3 Chebyshev |
| Index | Meaning |
| 1 | Butterworth |
| 2 | Bessel |
| 3 | Chebyshev |

|  | Note Do not change the value of a measurement after the measurement starts. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkFunction = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkdispphmax.htm language=enus -->
## TOPIC 01454: Variable: PkDispPhMax

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkdispphmax.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkdispphmax.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkDispPhMax

Variable: PkDispPhMax

Specifies in packet processing whether DIAdem identifies the greatest measurement value in the voltmeter, with a marker.

| Definition | PkDispPhMax(i), Boolean variablei=1...Number of channels |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkDispPhMax(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Voltmeter Options](../../dlgdacpp/dac_packet_voltmeter/pk_voltmeter_options.htm) | [Voltmeter Peak Hold](../../dlgdacpp/dac_packet_voltmeter/pk_voltmeter_trend.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkdispphmin.htm language=enus -->
## TOPIC 01455: Variable: PkDispPhMin

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkdispphmin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkdispphmin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkDispPhMin

Variable: PkDispPhMin

Specifies in packet processing whether DIAdem identifies the smallest measurement value in the voltmeter, with a marker.

| Definition | PkDispPhMin(i), Boolean variablei=1...Number of channels |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkDispPhMin(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Voltmeter Options](../../dlgdacpp/dac_packet_voltmeter/pk_voltmeter_options.htm) | [Voltmeter Peak Hold](../../dlgdacpp/dac_packet_voltmeter/pk_voltmeter_trend.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkdisptrend.htm language=enus -->
## TOPIC 01456: Variable: PkDispTrend

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkdisptrend.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkdisptrend.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkDispTrend

Variable: PkDispTrend

Specifies in packet processing whether DIAdem displays the measurement data trend in the voltmeter.

| Definition | PkDispTrend(i), Boolean variablei=1...Number of channels |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkDispTrend(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Voltmeter Options](../../dlgdacpp/dac_packet_voltmeter/pk_voltmeter_options.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkemode.htm language=enus -->
## TOPIC 01457: Variable: PkMode

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkemode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkemode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkMode

Variable: PkMode

Specifies in packet processing the input instrument for manual input.

| Definition | PkMode(i), Enumeration variablei=1...Number of channels |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Slider control 2 Dial 3 Push button 4 Switch 5 Bit switch |
| Index | Meaning |
| 1 | Slider control |
| 2 | Dial |
| 3 | Push button |
| 4 | Switch |
| 5 | Bit switch |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkMode(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Input Mode of the Manual Input](../../dlgdacpp/dac_packet_manualinput/pk_manualinput_mode.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pklinthermotype.htm language=enus -->
## TOPIC 01458: Variable: PkLinThermoType

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pklinthermotype.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pklinthermotype.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkLinThermoType

Variable: PkLinThermoType

Specifies in packet processing the linearization function type of a thermo linearization. You can use DIN EN 60584-1 (IEC 584-1) type thermocouples and a thermolinearization for PT100 type resistance elements.

| Definition | PkLinThermoType, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 R 2 S 3 B 4 J 5 T 6 E 7 K 8 N 9 Pt100 |
| Index | Meaning |
| 1 | R |
| 2 | S |
| 3 | B |
| 4 | J |
| 5 | T |
| 6 | E |
| 7 | K |
| 8 | N |
| 9 | Pt100 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkLinThermoType = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Thermo Linearization](../../dlgdacpp/dac_packet_dlg_handling/hb_thermo_lin.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkmaavmw.htm language=enus -->
## TOPIC 01459: Variable: PkMAAVMW

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkmaavmw.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkmaavmw.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkMAAVMW

Variable: PkMAAVMW

Specifies in packet processing whether DIAdem calculates the average absolute deviation from the mean as a statistical characteristic value.

| Definition | PkMAAVMW, Integer variable |
| --- | --- |
|  | 0 or 1 |

|  | Note Do not change the value of the variable after you have started a measurement. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkMAAVMW = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkoffsetinmd.htm language=enus -->
## TOPIC 01460: Variable: PkOffsetInMd

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkoffsetinmd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkoffsetinmd.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkOffsetInMd

Variable: PkOffsetInMd

Specifies in packet processing the offset size in order to output large data packets in smaller overlapping sub-packets with the slider control.

| Definition | PkOffsetInMd, LongInteger variable |
| --- | --- |
|  | 101 or 102 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkOffsetInMd = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Offset Register](../../dlgdacpp/dac_packet_dlg_handling/hb_schieberegister.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkonebmp.htm language=enus -->
## TOPIC 01461: Variable: PkOneBmp

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkonebmp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkonebmp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkOneBmp

Variable: PkOneBmp

Specifies in packet processing whether DIAdem displays a bitmap on all switches of a bit switch. If you assign the value 0 to the variable, DIAdem distributes the loaded bitmap to the switches.

| Definition | PkOneBmp(i), Boolean variablei=1...Number of channels |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkOneBmp(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Input Mode of the Manual Input](../../dlgdacpp/dac_packet_manualinput/pk_manualinput_mode.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkorder.htm language=enus -->
## TOPIC 01462: Variable: PkOrder

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkorder.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkorder.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkOrder

Variable: PkOrder

Specifies in packet processing the filter order of digital filters. High filter orders provide a steeper filter with greater phase displacement

| Definition | PkOrder, Word variable |
| --- | --- |
|  | 0 <= PkOrder <= 10 (only even numbers) |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkOrder = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkout.htm language=enus -->
## TOPIC 01463: Variable: PkOut

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkout.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkout.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkOut

Variable: PkOut

Specifies in packet processing the output string to transfer data over a serial interface to an external device.

| Definition | PkOut, String variable |
| --- | --- |
|  | Maximum 80 characters |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkOut = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkoutmode.htm language=enus -->
## TOPIC 01464: Variable: PkOutMode

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkoutmode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkoutmode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkOutMode

Variable: PkOutMode

Specifies in packet processing whether the threshold value outputs a TTL signal or a data signal when the incoming data packets exceed or undershoot limit values.

| Definition | PkOutMode, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Logic high (low) 2 Data value (no value) |
| Index | Meaning |
| 1 | Logic high (low) |
| 2 | Data value (no value) |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkOutMode = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

| Selection term | Meaning |
| --- | --- |
| Logic high (low) | Specifies that the threshold value outputs the value 0 for TTL low or FALSE, and the value 5 for TTL high or TRUE. Use this setting to output event related control signals. |
| Data value (no value) | Specifies that the threshold value outputs the first value after the threshold is exceeded or undershot. The packet block does not return data if the input signal does not exceed or undershoot a threshold. |

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkparam.htm language=enus -->
## TOPIC 01465: Variable: PkParam

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkparam.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkparam.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkParam

Variable: PkParam

Specifies in packet processing the type of data amount to be created in sections.

| Definition | PkParam, LongInteger variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Number of values 2 Number of values per packet 3 No. of packets |
| Index | Meaning |
| 1 | Number of values |
| 2 | Number of values per packet |
| 3 | No. of packets |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkParam = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Ignore Block](../../dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkpckoffset.htm language=enus -->
## TOPIC 01466: Variable: PkPckOffset

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkpckoffset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkpckoffset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPckOffset

Variable: PkPckOffset

Specifies in packet processing the overlapping width with which the offset register outputs data packets.

| Definition | PkPckOffset, Integer variable |
| --- | --- |
|  | 0 < PkPckOffset < 100% |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPckOffset = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkpcksz.htm language=enus -->
## TOPIC 01467: Variable: PkPckSz

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkpcksz.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkpcksz.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPckSz

Variable: PkPckSz

Specifies in packet processing the number of values of a data packet.

| Definition | PkPckSz, LongInteger variable |
| --- | --- |
|  | 1 < PkPckSz |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPckSz = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[DATA Reader](../../dlgdacpp/dac_packet_dlg_disp_io/hb_read_matrix.htm) | [Offset Register](../../dlgdacpp/dac_packet_dlg_handling/hb_schieberegister.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkperiod.htm language=enus -->
## TOPIC 01468: Variable: PkPeriod

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkperiod.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkperiod.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPeriod

Variable: PkPeriod

Specifies in hours, minutes, and seconds how long the timer of the packet processing outputs a control signal. At the end of the run-time the control signal falls to TTL low.

| Definition | PkPeriod, String variable |
| --- | --- |
|  | Syntax: hh:mm:ss |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPeriod = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkpermxfrom.htm language=enus -->
## TOPIC 01469: Variable: PkPermXFrom

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkpermxfrom.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkpermxfrom.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPermXFrom

Variable: PkPermXFrom

Specifies in packet processing the start value of the x-axis in seconds in order to scale the x-axis of the oscilloscope.

| Definition | PkPermXFrom, Real variable |
| --- | --- |
|  | -1E35 <= PkPermXFrom <= 1E35 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPermXFrom = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Axis Ranges](../../dlgdacpp/dac_packet_osci/pk_oscilloscope_range.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkpermxon.htm language=enus -->
## TOPIC 01470: Variable: PkPermXOn

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkpermxon.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkpermxon.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPermXOn

Variable: PkPermXOn

Specifies in packet processing a fixed scaling for the x-axis of the oscilloscope. The permanent scaling of the x-axis is possible only for y/x-diagrams.

| Definition | PkPermXOn, Boolean variable |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPermXOn = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Axis Ranges](../../dlgdacpp/dac_packet_osci/pk_oscilloscope_range.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkpermyfrom.htm language=enus -->
## TOPIC 01471: Variable: PkPermYFrom

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkpermyfrom.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkpermyfrom.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPermYFrom

Variable: PkPermYFrom

Specifies in packet processing the start value of the y-axis in seconds in order to scale the y-axis of the oscilloscope.

| Definition | PkPermYFrom, Real variable |
| --- | --- |
|  | -1E35 <= PkPermYFrom <= 1E35 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPermYFrom = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Axis Ranges](../../dlgdacpp/dac_packet_osci/pk_oscilloscope_range.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkpermyto.htm language=enus -->
## TOPIC 01472: Variable: PkPermYTo

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkpermyto.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkpermyto.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPermYTo

Variable: PkPermYTo

Specifies in packet processing the end value of the y-axis in order to scale the y-axis of the oscilloscope.

| Definition | PkPermYTo, Real variable |
| --- | --- |
|  | -1E35 <= PkPermYTo <= 1E35 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPermYTo = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Axis Ranges](../../dlgdacpp/dac_packet_osci/pk_oscilloscope_range.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkphase.htm language=enus -->
## TOPIC 01473: Variable: PkPhase

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkphase.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkphase.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPhase

Variable: PkPhase

Specifies in packet processing the phase of a sine signal, a square signal, triangle signal, and an impulse signal generated by a function generator.

| Definition | PkPhase, Real variable |
| --- | --- |
|  | -1E35 <= PkPhase <= 1E35 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPhase = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Function Generator](../../dlgdacpp/dac_packet_dlg_disp_io/hb_generator.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkphasefft.htm language=enus -->
## TOPIC 01474: Variable: PkPhaseFFT

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkphasefft.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkphasefft.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPhaseFFT

Variable: PkPhaseFFT

Specifies in packet processing whether DIAdem calculates the phase spectrum for the FFT. For phase calculation, DIAdem calculates the angle measured counterclockwise between the positive real axis and the appropriate place vector (real part, imaginary part).

| Definition | PkPhaseFFT, Boolean variable |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPhaseFFT = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[FFT](../../dlgdacpp/dac_packet_dlg_math/hb_fft.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkportnr.htm language=enus -->
## TOPIC 01475: Variable: PkPortNr

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkportnr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkportnr.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPortNr

Variable: PkPortNr

Specifies in packet processing the serial interface to which an external device is connected.

| Definition | PkPortNr, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 COM1 2 COM2 3 COM3 4 COM4 |
| Index | Meaning |
| 1 | COM1 |
| 2 | COM2 |
| 3 | COM3 |
| 4 | COM4 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPortNr = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkpretrigrange.htm language=enus -->
## TOPIC 01476: Variable: PkPreTrigRange

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkpretrigrange.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkpretrigrange.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkPreTrigRange

Variable: PkPreTrigRange

Specifies in packet processing how many values DIAdem outputs before a trigger event. The pretrigger range must not exceed the block size.

| Definition | PkPreTrigRange, LongInteger variable |
| --- | --- |
|  | 0 < PkPreTrigRange |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkPreTrigRange = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger](../../dlgdacpp/dac_packet_dlg_handling/hb_trigger.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkqfactor.htm language=enus -->
## TOPIC 01477: Variable: PkQFactor

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkqfactor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkqfactor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkQFactor

Variable: PkQFactor

Specifies in packet processing the quality factor for bandpass and bandstop of digital filters.

| Definition | PkQFactor, Real variable |
| --- | --- |
|  | 0 <= PkQFactor <= 1E35 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkQFactor = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkqmean.htm language=enus -->
## TOPIC 01478: Variable: PkQMean

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkqmean.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkqmean.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkQMean

Variable: PkQMean

Specifies in packet processing whether DIAdem calculates the square mean or the root mean square as the statistical value.

| Definition | PkQMean, Integer variable |
| --- | --- |
|  | 0 or 1 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkQMean = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkqsum.htm language=enus -->
## TOPIC 01479: Variable: PkQSum

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkqsum.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkqsum.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkQSum

Variable: PkQSum

Specifies in packet processing whether DIAdem calculates the sum of the squared values of a data packet as a statistical characteristic value.

| Definition | PkQSum, Integer variable |
| --- | --- |
|  | 0 or 1 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkQSum = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkquanta.htm language=enus -->
## TOPIC 01480: Variable: PkQuantA

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkquanta.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkquanta.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkQuantA

Variable: PkQuantA

Specifies in packet processing the number of values or data packets of the first data amount A, to be created in sections.

| Definition | PkQuantA, Word variable |
| --- | --- |
|  | 0 <= PkQuantA <= 65535 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkQuantA = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Ignore Block](../../dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkquantb.htm language=enus -->
## TOPIC 01481: Variable: PkQuantB

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkquantb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkquantb.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkQuantB

Variable: PkQuantB

Specifies in packet processing the number of values or data packets of the second data amount B to be created in sections.

| Definition | PkQuantB, Word variable |
| --- | --- |
|  | 0 <= PkQuantA <= 65535 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkQuantB = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Ignore Block](../../dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkradio.htm language=enus -->
## TOPIC 01482: Variable: PkRadio

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkradio.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkradio.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRadio

Variable: PkRadio

Specifies in packet processing whether the switches of a multi-channel input instrument switch off each other.

| Definition | PkRadio(i), Boolean variablei=1...Number of channels |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRadio(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Input Mode of the Manual Input](../../dlgdacpp/dac_packet_manualinput/pk_manualinput_mode.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrange.htm language=enus -->
## TOPIC 01483: Variable: PkRange

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrange.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrange.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRange

Variable: PkRange

Specifies in packet processing the entire display area of a voltmeter.

| Definition | PkRange(i), Real variablei=1...Number of channels |
| --- | --- |
|  | -1E35 <= PkRange <= 1E35 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRange(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Voltmeter Options](../../dlgdacpp/dac_packet_voltmeter/pk_voltmeter_options.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrate.htm language=enus -->
## TOPIC 01484: Variable: PkRate

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrate.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrate.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRate

Variable: PkRate

Specifies in packet processing the sampling rate of the signal the function generator creates.

| Definition | PkRate, Real variable |
| --- | --- |
|  | -1E35 <= PkRate <= 1E35 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkClockRate = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Function Generator](../../dlgdacpp/dac_packet_dlg_disp_io/hb_generator.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrcontrol.htm language=enus -->
## TOPIC 01485: Variable: PkControl

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrcontrol.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrcontrol.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkControl

Variable: PkControl

Specifies in packet processing whether a control signal, a data signal, or the user controls the transmission and the distribution of data packets to the data outputs of a relay.

| Definition | PkControl, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Logic level at control input 2 Data packet at control input 3 Interactive answer of user |
| Index | Meaning |
| 1 | Logic level at control input |
| 2 | Data packet at control input |
| 3 | Interactive answer of user |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkControl = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Relay Switch](../../dlgdacpp/dac_packet_dlg_handling/hb_relais.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrealtime.htm language=enus -->
## TOPIC 01486: Variable: PkRealTime

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrealtime.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrealtime.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRealTime

Variable: PkRealTime

Specifies in packet processing whether the function generator generates data packets as fast as possible or with the specified clock rate and packet size.

| Definition | PkRealTime, Boolean variable |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRealTime = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Function Generator](../../dlgdacpp/dac_packet_dlg_disp_io/hb_generator.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkreclength.htm language=enus -->
## TOPIC 01487: Variable: PkRecLength

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkreclength.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkreclength.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRecLength

Variable: PkRecLength

Specifies in packet processing the number of values to be displayed simultaneously in the oscilloscope and thereby the display area of the recorder.

| Definition | PkRecLength, LongInteger variable |
| --- | --- |
|  | 0 < PkRecLength <= 2147483646 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRecLength = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Recorder Mode](../../dlgdacpp/dac_packet_osci/pk_oscilloscope_recorder.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkreduceval.htm language=enus -->
## TOPIC 01488: Variable: PkReduceVal

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkreduceval.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkreduceval.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkReduceVal

Variable: PkReduceVal

Specifies in packet processing the number of values in an interval, for which DIAdem calculates the mean value.

| Definition | PkReduceVal, Word variable |
| --- | --- |
|  | 0 <= PkReduceVal <= Packet size |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkReduceVal = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Mean](../../dlgdacpp/dac_packet_dlg_math/hb_mittelwert.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrefline.htm language=enus -->
## TOPIC 01489: Variable: PkRefLine

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrefline.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrefline.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRefLine

Variable: PkRefLine

Specifies in packet processing the zero line for the classification method, to separate oscillations into positive and negative sections.

| Definition | PkRefLine, LongInteger variable |
| --- | --- |
|  | 0 <= PkHyst |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRefLine = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Online Classification](../../dlgdacpp/dac_packet_dlg_math/hb_klassierung.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrepeatm.htm language=enus -->
## TOPIC 01490: Variable: PkRepeatM

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrepeatm.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrepeatm.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRepeatM

Variable: PkRepeatM

Specifies in packet processing which data DIAdem reads and how often DIAdem reads the data and outputs the data to the block diagram.

| Definition | PkRepeatM, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Repeat first packet 2 Repeat at end of channel 3 Stop at end of channel 4 Stop after first packet |
| Index | Meaning |
| 1 | Repeat first packet |
| 2 | Repeat at end of channel |
| 3 | Stop at end of channel |
| 4 | Stop after first packet |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRepeatM = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[DATA Reader](../../dlgdacpp/dac_packet_dlg_disp_io/hb_read_matrix.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrepeatmdupl.htm language=enus -->
## TOPIC 01491: Variable: PkRepeatM

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrepeatmdupl.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrepeatmdupl.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRepeatM

Variable: PkRepeatM

Specifies in packet processing how often the replicator repeatedly outputs a data packet to the block diagram.

| Definition | PkRepeatM, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Continuous 2 N times 3 Infinite copies of the current packet |
| Index | Meaning |
| 1 | Continuous |
| 2 | N times |
| 3 | Infinite copies of the current packet |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRepeatM = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Replicator](../../dlgdacpp/dac_packet_dlg_handling/hb_replicate.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrepeatmode.htm language=enus -->
## TOPIC 01492: Variable: PkRepeatMode

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrepeatmode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrepeatmode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRepeatMode

Variable: PkRepeatMode

Specifies in packet processing which data DIAdem reads repeatedly from a file.

| Definition | PkRepeatMode, enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Without repetition 2 Repeat entire file 3 Repeat first data packet 4 Repeat last data packet |
| Index | Meaning |
| 1 | Without repetition |
| 2 | Repeat entire file |
| 3 | Repeat first data packet |
| 4 | Repeat last data packet |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRepeatMode = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrepeatms.htm language=enus -->
## TOPIC 01493: Variable: PkRepeatM

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrepeatms.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrepeatms.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRepeatM

Variable: PkRepeatM

Specifies in packet processing that DIAdem writes a specified number of data packets into the Data Portal.

| Definition | PkRepeatM, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Continuous 2 Writes n packets 3 Writes n values 4 Writes only the last packet |
| Index | Meaning |
| 1 | Continuous |
| 2 | Writes n packets |
| 3 | Writes n values |
| 4 | Writes only the last packet |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRepeatM = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[DATA Writer](../../dlgdacpp/dac_packet_dlg_disp_io/hb_write_matrix.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkreset.htm language=enus -->
## TOPIC 01494: Variable: PkReset

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkreset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkreset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkReset

Variable: PkReset

Specifies in packet processing when DIAdem triggers the reset of an online classification to reject values and to begin a new count.

| Definition | PkReset, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 No 2 High level on control input 3 Repeat after N blocks of data |
| Index | Meaning |
| 1 | No |
| 2 | High level on control input |
| 3 | Repeat after N blocks of data |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkReset = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Online Classification](../../dlgdacpp/dac_packet_dlg_math/hb_klassierung.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkresetcount.htm language=enus -->
## TOPIC 01495: Variable: PkResetCount

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkresetcount.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkresetcount.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkResetCount

Variable: PkResetCount

Specifies in packet processing the number of data packets after which DIAdem rejects the current values of an FFT and restarts averaging.

| Definition | PkResetCount, LongInteger variable |
| --- | --- |
|  | 0 < PkResetCount |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkResetCount = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Two Signal FFT](../../dlgdacpp/dac_packet_dlg_math/hb_fft_zwei.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkresetmode.htm language=enus -->
## TOPIC 01496: Variable: PkResetMode

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkresetmode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkresetmode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkResetMode

Variable: PkResetMode

Specifies in packet processing whether DIAdem rejects the current values of an FFT of two time signals or of mean value calculation and restarts averaging.

| Definition | PkResetMode, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 2 High level on control input 3 Repeat after N blocks of data |
| Index | Meaning |
| 1 |  |
| 2 | High level on control input |
| 3 | Repeat after N blocks of data |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkResetMode = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Mean](../../dlgdacpp/dac_packet_dlg_math/hb_mittelwert.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Two Signal FFT](../../dlgdacpp/dac_packet_dlg_math/hb_fft_zwei.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkresnblocks.htm language=enus -->
## TOPIC 01497: Variable: PkResNBlocks

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkresnblocks.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkresnblocks.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkResNBlocks

Variable: PkResNBlocks

Specifies in packet processing the number of data packets after which DIAdem starts a new mean value calculation.

| Definition | PkResNBlocks, LongInteger variable |
| --- | --- |
|  | 0 < PkResNBlocks <= 2147483647 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkResNBlocks = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Mean](../../dlgdacpp/dac_packet_dlg_math/hb_mittelwert.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkretrigger.htm language=enus -->
## TOPIC 01498: Variable: PkRetrigger

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkretrigger.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkretrigger.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRetrigger

Variable: PkRetrigger

Specifies in packet processing whether DIAdem checks a trigger signal continuously for trigger events.

| Definition | PkRetrigger, Boolean variable |
| --- | --- |
|  | Selection term from the following list: Index Meaning 0 Condition 1 Automatic |
| Index | Meaning |
| 0 | Condition |
| 1 | Automatic |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRetrigger = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger Finder](../../dlgdacpp/dac_packet_dlg/hb_trigsuch.htm) | [Trigger](../../dlgdacpp/dac_packet_dlg_handling/hb_trigger.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkretrigtype.htm language=enus -->
## TOPIC 01499: Variable: PkRetrigType

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkretrigtype.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkretrigtype.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRetrigType

Variable: PkRetrigType

Specifies in packet processing which condition a retrigger activates for the trigger searcher.

| Definition | PkRetrigType, Boolean variable |
| --- | --- |
|  | Selection term from the following list: Index Meaning 0 Window 1 Slope |
| Index | Meaning |
| 0 | Window |
| 1 | Slope |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRetrigType = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger Finder](../../dlgdacpp/dac_packet_dlg/hb_trigsuch.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkripple.htm language=enus -->
## TOPIC 01500: Variable: PkRipple

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkripple.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkripple.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkRipple

Variable: PkRipple

Specifies in packet processing the ripples of digital filters in the pass-band of the Chebyshev and the elliptic filters.

| Definition | PkRipple, Integer variable |
| --- | --- |
|  | 0 < PkRipple < oo |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkRipple = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Digital Filters](../../dlgdacpp/dac_packet_dlg_math/hb_digfilt_neu.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)
