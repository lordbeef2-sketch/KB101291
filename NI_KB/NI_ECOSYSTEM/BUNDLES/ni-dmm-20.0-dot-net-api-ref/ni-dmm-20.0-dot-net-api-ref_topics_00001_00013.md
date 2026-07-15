# NI DOCUMENT BUNDLE: ni-dmm-20.0-dot-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-20.0-dot-net-api-ref start=1 end=13 -->
<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/copyright.html language=enus -->
## TOPIC 00001: Copyright

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/copyright.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/copyright.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Copyright

#### End-User License Agreements and Third-Party Legal Notices

Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including
 photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior
 written consent of National Instruments Corporation.

National Instruments respects the intellectual property of others, and we ask our users to do the same. NI software is protected
 by copyright and other intellectual property laws. Where NI software may be used to reproduce software or other materials
 belonging to others, you may use NI software only to reproduce materials that you may reproduce in accordance with the terms
 of any applicable license or other legal restriction.

You can find end-user license agreements (EULAs) and third-party legal notices in the following locations:

- Notices are located in the 
 <National Instruments>\_Legal Information and 
 <National Instruments> directories.
- EULAs are located in the 
 <National Instruments>\Shared\MDF\Legal\license directory.
- Review 
 <National Instruments>\_Legal Information.txt for information on including legal information in installers built with NI products.

If you are an agency, department, or other entity of the United States Government ("Government"), the use, duplication, reproduction,
 release, modification, disclosure or transfer of the technical data included in this manual is governed by the Restricted
 Rights provisions under Federal Acquisition Regulation 52.227-14 for civilian agencies and Defense Federal Acquisition Regulation
 Supplement Section 252.227-7014 and 252.227-7015 for military agencies.

Content from the IVI specifications reproduced with permission from the IVI Foundation.

The IVI Foundation and its member companies make no warranty of any kind with regard to this material, including, but not
 limited to, the implied warranties of merchantability and fitness for a particular purpose. The IVI Foundation and its member
 companies shall not be liable for errors contained herein or for incidental or consequential damages in connection with the
 furnishing, performance, or use of this material.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/export-compliance.html language=enus -->
## TOPIC 00002: Export Compliance Information

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/export-compliance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/export-compliance.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Export Compliance Information

Refer to the 
 Export Compliance Information at 
 ni.com/legal/export-compliance for the National Instruments global trade compliance policy and how to obtain relevant HTS codes, ECCNs, and other import/export
 data.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/fetch-read-dmm-dotnet.html language=enus -->
## TOPIC 00003: Using Memory-Optimized and Async Methods to Fetch and Read

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/fetch-read-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/fetch-read-dmm-dotnet.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Using Memory-Optimized and Async Methods to Fetch and Read

The **Fetch** and **Read** methods are in the **DmmMeasurement**and **DmmWaveformAcquisition** classes. A session must be open and configured correctly for reading. In case of fetch, the session must be open, configured
 correctly, and initiated before the actual fetch. Reading is equivalent to initiating the acquisition and fetching the results.
 Calling **Read()** combines **Initiate()** and **Fetch()** into one call. **Read()** is suitable for simple acquisitions. **Initiate()** and **Fetch()** are better suited for complex applications.

The **Read** and **Fetch** methods can be categorized into:

- Normal methods
- Memory-optimized methods
- Async methods
- Async memory-optimized methods

Normal overloads have the option of specifying the number of points to fetch and maximum time allowed for the operation to
 complete. Each of the overloads has a corresponding memory-optimized overload and async overload.

#### Memory-Optimized Methods

Memory-optimized methods perform the fetch operation on pre-allocated memory.

If you fetch or read large amounts of data, and your application processes data between each call, and the acquired data is
 not necessary after processing, you can use the memory-optimized method overloads of the reader classes to improve the performance
 of your application.

Memory-optimized methods take an object that stores the acquired data. These overloads do not allocate memory if the buffer
 object passed is large enough to hold the amount of data being fetched or read, which prevents the overhead of .NET memory
 allocation and garbage collection. As a result, performance will improve for applications that fetch or read large amount
 of data.

```text
VB.NET

Dim reading As Double() = New Double(999) {}
Dim dmmSession As New NIDmm("DMM-4072", False, False)
dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, 0.0001)
dmmSession.Trigger.MultiPoint.SampleCount = 2000
dmmSession.Measurement.Initiate()

Dim actualNumberOfPoints As Integer 

'Passing the reading for the first time.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, actualNumberOfPoints, reading)

'Process the reading using the 'reading' variable, then fetch next few samples into the 
'same variable, which reuses rather than reallocates memory. 
'Ensure that the data in the 'reading' variable is no longer needed.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, actualNumberOfPoints, reading)
```

```text
C#

double[] reading = new double[1000];
NIDmm dmmSession = new NIDmm("DMM-4072", false, false);
dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, .0001);
dmmSession.Trigger.MultiPoint.SampleCount = 2000;
dmmSession.Measurement.Initiate();

int actualNumberOfPoints;
//Passing the reading for the first time.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, out actualNumberOfPoints, ref reading);

//Process the reading using the 'reading' variable, then fetch next few samples into the 
//same variable, which reuses rather than reallocates memory. 
//Ensure that the data in the 'reading' variable is no longer needed.
dmmSession.Measurement.MemoryOptimizedFetchMultiPoint(1000, out actualNumberOfPoints, ref reading);
```

#### Async Methods

For every non-asynchronous fetch and read method, there is a method which does the same operation asynchronously. We follow
 the event-based asynchronous pattern. These asynchronous methods perform the fetch or read operation in a separate worker
 thread and return the data through **OperationCompleted** events. Each of these asynchronous methods has a corresponding **OperationCompleted** event. After an async method completes execution, its corresponding event occurs. You must handle this event to get the result
 of the asynchronous operation. The event handler to this event should take two parameters, one of type **Object** and another of type **DmmMeasurementEventArgs<T>**.

The following code shows how to read a sample number of points asynchronously.

```text
VB.NET

Dim dmmSession As NIDmm
Dim result As Double()
Public Sub FetchAsync()
    dmmSession = New NIDmm("DMM-4072", False, False)
    AddHandler dmmSession.Measurement.ReadMultiPointCompleted, AddressOf Measurement_ReadMultipointCompleted
    dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, 0.0001)
    dmmSession.Trigger.MultiPoint.SampleCount = 10
    dmmSession.Measurement.ReadMultiPointAsync(10, Nothing)
End Sub 

Sub Measurement_ReadMultipointCompleted(ByVal sender As Object, ByVal e As DmmMeasurementEventArgs(Of Double()))
    If e.[Error] IsNot Nothing Then
        result = e.Reading
    End If
    dmmSession.Close()
End Sub
```

```text
C#

NIDmm dmmSession;
double[] result;
public void Fetch()
{
    dmmSession = new NIDmm("DMM-4072", false, false);
    dmmSession.Measurement.ReadMultiPointCompleted += new EventHandler<DmmMeasurementEventArgs<double[]>>(Measurement_ReadMultiPointCompleted);
    dmmSession.Configure(DmmMeasurementFunction.DCVolts, 10, .0001);
    dmmSession.Trigger.MultiPoint.SampleCount = 10;
    dmmSession.Measurement.ReadMultiPointAsync(10, null);
}
void Measurement_ReadMultiPointCompleted(object sender, DmmMeasurementEventArgs<double[]> e)
{
    if (e.Error == null)
    {
        result = e.Reading;
    }
    dmmSession.Close();
}
```

#### Async Memory-Optimized Methods

There are asynchronous versions of memory-optimized methods. You use these asynchronous methods similarly to the way you use
 non-memory-optimized asynchronous methods. The only difference between memory-optimized asynchronous methods and non-memory-optimized
 asynchronous methods is that the asynchronous memory-optimized read or fetch methods take an additional buffer object that
 stores the data.

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/guid-d0ea49a0-fffa-4df3-90ad-80b2df2a7b11.html language=enus -->
## TOPIC 00004: Trademarks

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/guid-d0ea49a0-fffa-4df3-90ad-80b2df2a7b11.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/guid-d0ea49a0-fffa-4df3-90ad-80b2df2a7b11.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Trademarks

Refer to the 
 NI Trademarks and Logo Guidelines at 
 [ni.com/trademarks](http://www.ni.com/trademarks) for more information on NI trademarks.

ARM, Keil, and µVision are trademarks or registered of ARM Ltd or its subsidiaries.

LEGO, the LEGO logo, WEDO, and MINDSTORMS are trademarks of the LEGO Group.

TETRIX by Pitsco is a trademark of Pitsco, Inc.

FIELDBUS FOUNDATION™ and FOUNDATION™ are trademarks of the Fieldbus Foundation.

EtherCAT® is a registered trademark of and licensed by Beckhoff Automation GmbH.

CANopen® is a registered Community Trademark of CAN in Automation e.V.

DeviceNet™ and EtherNet/IP™ are trademarks of ODVA.

Go!, SensorDAQ, and Vernier are registered trademarks of Vernier Software & Technology. Vernier Software & Technology and
 vernier.com are trademarks or trade dress.

Xilinx is the registered trademark of Xilinx, Inc.

Taptite and Trilobular are registered trademarks of Research Engineering & Manufacturing Inc.

FireWire® is the registered trademark of Apple Inc.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

Handle Graphics®, MATLAB®, Simulink®, Stateflow®, and xPC TargetBox® are registered trademarks, and Simulink Coder™, TargetBox™,
 and Target Language Compiler™ are trademarks of The MathWorks, Inc.

Tektronix®, Tek, and Tektronix, Enabling Technology are registered trademarks of Tektronix, Inc.

The Bluetooth® word mark is a registered trademark owned by the Bluetooth SIG, Inc.

The ExpressCard™ word mark and logos are owned by PCMCIA and any use of such marks by National Instruments is under license.

The mark LabWindows is used under a license from Microsoft Corporation. Windows is a registered trademark of Microsoft Corporation
 in the United States and other countries.

Other product and company names mentioned herein are trademarks or trade names of their respective companies.

Members of the National Instruments Alliance Partner Program are business entities independent from NI and have no agency,
 partnership, or joint-venture relationship with NI.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/interchangeability-ivi-dmm-dotnet.html language=enus -->
## TOPIC 00005: Using the NI-DMM .NET Class Library in IVI.NET Applications

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/interchangeability-ivi-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/interchangeability-ivi-dmm-dotnet.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Using the NI-DMM .NET Class Library in IVI.NET Applications

NI Digital Multimeters Help

|  | Note Integrated help for IVI Foundation interfaces is not provided. You must use the IntelliSense help. |
| --- | --- |

The .NET API for NI-DMM has two parts: the IVI.NET class-compliant API and the specific driver API. The following code snippet
 demonstrates how you can use an NI-DMM .NET specific driver API from a session obtained from an IVI.NET class-compliant API.

|  | Note The default value of OperationMode is IviDmmMode. When configuring the session by directly setting properties for waveform acquisition, OperationMode should be set to WaveformMode. |
| --- | --- |

|  | Note The session object must be closed once, either through an IIviDmm reference or through an NIDmm reference. |
| --- | --- |

1. Create an IVI.NET class-compliant session object and acquire data, then create and use a specific driver **NIDmm** object to access device-specific functionality. 
 
 VB.NET

'Create an IVI DMM session. 
Dim iviDmmSession As IIviDmm = Ivi.Driver.IviDriver.Create(Of IIviDmm)("DMM-4072", True, True)
Dim currentRange As Double = 0.2 
Dim currentResolutionDigits As Double = 6.5
iviDmmSession.Configure(Ivi.Dmm.MeasurementFunction.DCCurrent, currentRange, currentResolutionDigits)

'Take a reading. 
Dim reading As Double = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2))

'Get an NIDmm session from the IVI DMM session and get a reading using the NIDmm session. 
Dim sampleDmmSession As NIDmm = TryCast(iviDmmSession.GetService(GetType(NIDmm)), NIDmm)
If sampleDmmSession IsNot Nothing Then 
 Dim waveformVoltageRange As Double = 10 
 Dim waveformPointsToRead As Integer = 100 
 Dim rate As Double = 100
 sampleDmmSession.ConfigureWaveformAcquisition(DmmMeasurementFunction.WaveformVoltage, waveformVoltageRange, rate, waveformPointsToRead)
 Dim readingArray As AnalogWaveform(Of Double) = sampleDmmSession.WaveformAcquisition.ReadWaveform(waveformPointsToRead, NationalInstruments.PrecisionTimeSpan.FromMilliseconds(10000))
Else 
 Dim voltageRange As Double = 10, voltageResolution As Double = 0.0001 
 Dim numberOfSamples As Integer = 100
 iviDmmSession.Configure(MeasurementFunction.DCVolts, voltageRange, voltageResolution)
 iviDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples
 iviDmmSession.Trigger.Source = "Immediate" 
 Dim readingArray As Double() = iviDmmSession.Measurement.ReadMultiPoint(Ivi.Driver.PrecisionTimeSpan.FromMilliseconds(20000))
End If
iviDmmSession.Close() 
 C# 

// Create an IVI DMM session.
IIviDmm iviDmmSession = Ivi.Driver.IviDriver.Create<IIviDmm>("DMM-4072", true, true);
double currentRange = 0.2;
double currentResolutionDigits = 6.5;
iviDmmSession.Configure(Ivi.Dmm.MeasurementFunction.DCCurrent, currentRange, currentResolutionDigits);

//Take a reading. 
double reading = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2));

//Get an NIDmm session from the IVI DMM session and get a reading using the NIDmm session.
NIDmm sampleDmmSession = iviDmmSession.GetService(typeof(NIDmm)) as NIDmm;
if (sampleDmmSession != null)
{
 double waveformVoltageRange = 10;
 int waveformPointsToRead = 100;
 double rate = 100;
 sampleDmmSession.ConfigureWaveformAcquisition(DmmMeasurementFunction.WaveformVoltage, waveformVoltageRange, rate, waveformPointsToRead);
 AnalogWaveform<double> readingArray = sampleDmmSession.WaveformAcquisition.ReadWaveform(waveformPointsToRead, NationalInstruments.PrecisionTimeSpan.FromMilliseconds(10000));
}
else
{
 double voltageRange = 10, voltageResolution = 0.0001;
 int numberOfSamples = 100;
 iviDmmSession.Configure(MeasurementFunction.DCVolts, voltageRange, voltageResolution);
 iviDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples;
 iviDmmSession.Trigger.Source = "Immediate";
 double[] readingArray = iviDmmSession.Measurement.ReadMultiPoint(Ivi.Driver.PrecisionTimeSpan.FromMilliseconds(20000));
}
iviDmmSession.Close();
2. Switch from an NI-DMM .NET-specific driver session to an IVI.NET DMM session in the application. 
 
 
 [IMAGE alt='Note' src='note.gif']
 Note Before obtaining an **IIviDmm** reference from an existing **NIDmm** that is configured for waveform acquisition, set the **OperationMode** to **IviDmmMode**. 
 VB.NET

Dim sampleDmmSession As New NIDmm("DMM-4072", True, True)
Dim range As Double = 100 
Dim resolution As Double = 6.5 
' Use the NIDmm session as an IVI DMM session.
sampleDmmSession.OperationMode = DmmOperationMode.IviDmmMode
Dim serviceProvider As IServiceProvider = TryCast(sampleDmmSession, IServiceProvider)
Dim iviDmmSession As IIviDmm = TryCast(serviceProvider.GetService(GetType(IIviDmm)), IIviDmm)
If iviDmmSession IsNot Nothing Then
 iviDmmSession.Configure(MeasurementFunction.DCVolts, range, resolution)
 Dim reading As Double = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2))
End If
sampleDmmSession.Close() 
 C#

NIDmm sampleDmmSession = new NIDmm("DMM-4072", true, true);
double range = 100;
double resolution = 6.5;
// Use the NIDmm session as an IVI DMM session.
sampleDmmSession.OperationMode = DmmOperationMode.IviDmmMode;
IServiceProvider serviceProvider = sampleDmmSession as IServiceProvider;
IIviDmm iviDmmSession = serviceProvider.GetService(typeof(IIviDmm)) as IIviDmm;
if (iviDmmSession != null)
{
 iviDmmSession.Configure(MeasurementFunction.DCVolts, range, resolution);
 double reading = iviDmmSession.Measurement.Read(Ivi.Driver.PrecisionTimeSpan.FromSeconds(2));
}
sampleDmmSession.Close();

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/legal-info.html language=enus -->
## TOPIC 00006: Legal Information

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/legal-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/legal-info.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Legal Information

[Limited Warranty](limited-warranty.html)

[Copyright](copyright.html)

[Trademarks](guid-d0ea49a0-fffa-4df3-90ad-80b2df2a7b11.html)

[Patents](patents.html)

[Export Compliance Information](export-compliance.html)

[Warning Regarding Use of NI Products](warning.html)

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/limited-warranty.html language=enus -->
## TOPIC 00007: Limited Warranty

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/limited-warranty.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/limited-warranty.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Limited Warranty

This document is provided "as is" and is subject to being changed, without notice, in future editions. For the latest version,
 refer to 
 ni.com/manuals. NI reviews this document carefully for technical accuracy; however, NI MAKES NO EXPRESS OR IMPLIED WARRANTIES AS TO THE
 ACCURACY OF THE INFORMATION CONTAINED HEREIN AND SHALL NOT BE LIABLE FOR ANY ERRORS.

NI warrants that its hardware products will be free of defects in materials and workmanship that cause the product to fail
 to substantially conform to the applicable NI published specifications for one (1) year from the date of invoice.

For a period of ninety (90) days from the date of invoice, NI warrants that (i) its software products will perform substantially
 in accordance with the applicable documentation provided with the software and (ii) the software media will be free from defects
 in materials and workmanship.

If NI receives notice of a defect or non-conformance during the applicable warranty period, NI will, in its discretion: (i)
 repair or replace the affected product, or (ii) refund the fees paid for the affected product. Repaired or replaced hardware
 will be warranted for the remainder of the original warranty period or ninety (90) days, whichever is longer. If NI elects
 to repair or replace the product, NI may use new or refurbished parts or products that are equivalent to new in performance
 and reliability and are at least functionally equivalent to the original part or product.

You must obtain an RMA number from NI before returning any product to NI. NI reserves the right to charge a fee for examining
 and testing hardware not covered by the Limited Warranty.

This Limited Warranty does not apply if the defect of the product resulted from improper or inadequate maintenance, installation,
 repair, or calibration (performed by a party other than NI); unauthorized modification; improper environment; use of an improper
 hardware or software key; improper use or operation outside of the specification for the product; improper voltages; accident,
 abuse, or neglect; or a hazard such as lightning, flood, or other act of nature.

THE REMEDIES SET FORTH ABOVE ARE EXCLUSIVE AND THE CUSTOMER’S SOLE REMEDIES, AND SHALL APPLY EVEN IF SUCH REMEDIES FAIL OF
 THEIR ESSENTIAL PURPOSE.

EXCEPT AS EXPRESSLY SET FORTH HEREIN, PRODUCTS ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND AND NI DISCLAIMS ALL WARRANTIES,
 EXPRESSED OR IMPLIED, WITH RESPECT TO THE PRODUCTS, INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
 PURPOSE, TITLE OR NON-INFRINGEMENT, AND ANY WARRANTIES THAT MAY ARISE FROM USAGE OF TRADE OR COURSE OF DEALING. NI DOES NOT
 WARRANT, GUARANTEE, OR MAKE ANY REPRESENTATIONS REGARDING THE USE OF OR THE RESULTS OF THE USE OF THE PRODUCTS IN TERMS OF
 CORRECTNESS, ACCURACY, RELIABILITY, OR OTHERWISE. NI DOES NOT WARRANT THAT THE OPERATION OF THE PRODUCTS WILL BE UNINTERRUPTED
 OR ERROR FREE.

In the event that you and NI have a separate signed written agreement with warranty terms covering the products, then the
 warranty terms in the separate agreement shall control.

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/mapping-c-api-dmm-dotnet.html language=enus -->
## TOPIC 00008: Mapping the NI-DMM .NET API to the NI-DMM C API

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/mapping-c-api-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/mapping-c-api-dmm-dotnet.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Mapping the NI-DMM .NET API to the NI-DMM C API

The following table maps the NI-DMM .NET API members to the corresponding NI-DMM C API and IVI .NET API members. All .NET
 members are in the **NationalInstruments.ModularInstruments.NIDmm** namespace.

| IVI .NET API Member | .NET API Member | C API Member |
| --- | --- | --- |
|  | DmmCalibration Class |  |
|  | UserDefinedInfoMaximumSize | niDMM_GetCalUserDefinedInfoMaxSize |
|  | ExternalCalibrationRecommendedInterval | niDMM_GetExtCalRecommendedInterval |
|  | GetCalibrationCount | niDMM_GetCalCount |
|  | GetCalibrationDateAndTime | niDMM_GetCalDateAndTime |
|  | GetDeviceTemperature | niDMM_GetDevTemp |
|  | GetLastCalibrationTemperature | niDMM_GetLastCalTemp |
|  | SelfCalibrate | niDMM_SelfCal |
|  | RestoreLastExternalCalibrationConstants | niDMM_RestoreLastExtCalConstants |
|  | SetCalibrationPassword | niDMM_SetCalPassword |
|  | IsSelfCalibrationSupported | niDMM_GetSelfCalSupported |
|  | UserDefinedInfo | niDMM_GetCalUserDefinedInfo / niDMM_SetCalUserDefinedInfo |
|  | NIDmm Class |  |
| Ivi.Driver.IIviDriver.Close | Close | niDMM_close |
| Ivi.Dmm.IIviDmm.Configure | Configure | niDMM_ConfigureMeasurementAbsolute |
|  | ConfigureMeasurementDigits | niDMM_ConfigureMeasurementDigits |
|  | ConfigureWaveformAcquisition | niDMM_ConfigureWaveformAcquisition |
| Ivi.Dmm.IIviDmm.AutoRange | AutoRange | NIDMM_ATTR_RANGE |
|  | MeasurementPeriod | niDMM_GetMeasurementPeriod |
|  | InputResistance | NIDMM_ATTR_INPUT_RESISTANCE |
|  | CurrentSource | NIDMM_ATTR_CURRENT_SOURCE |
| Ivi.Dmm.IIviDmm.Resolution | Resolution | NIDMM_ATTR_RESOLUTION_ABSOLUTE |
|  | DigitsResolution | NIDMM_ATTR_RESOLUTION_DIGITS |
| Ivi.Dmm.IIviDmm.Range | Range | NIDMM_ATTR_RANGE |
| Ivi.Dmm.IIviDmm.MeasurementFunction | MeasurementFunction | NIDMM_ATTR_FUNCTION |
|  | OperationMode | NIDMM_ATTR_OPERATION_MODE |
|  | DmmAC Class |  |
| Ivi.Dmm.IIviDmmAC.ConfigureBandwidth | ConfigureBandwidth | niDMM_ConfigureACBandwidth |
| Ivi.Dmm.IIviDmmAC.FrequencyMin | FrequencyMin | NIDMM_ATTR_AC_MIN_FREQ |
| Ivi.Dmm.IIviDmmAC.FrequencyMax | FrequencyMax | NIDMM_ATTR_AC_MAX_FREQ |
|  | DmmMeasurement Class |  |
| Ivi.Dmm.IIviDmmMeasurement.Abort | Abort | niDMM_Abort |
| Ivi.Dmm.IIviDmmMeasurement.Fetch | Fetch | niDMM_Fetch |
| Ivi.Dmm.IIviDmmMeasurement.FetchMultiPoint | FetchMultiPoint | niDMM_FetchMultiPoint |
|  | MemoryOptimizedFetchMultiPoint | niDMM_FetchMultiPoint |
|  | FetchMultiPointAsync | niDMM_FetchMultiPoint |
|  | MemoryOptimizedFetchMultiPointAsync | niDMM_FetchMultiPoint |
| Ivi.Dmm.IIviDmmMeasurement.Initiate | Initiate | niDMM_Initiate |
|  | IsOverRange | niDMM_IsOverRange |
| Ivi.Dmm.IIviDmmMeasurement.ReadMultiPoint | ReadMultiPoint | niDMM_ReadMultiPoint |
|  | MemoryOptimizedReadMultiPoint | niDMM_ReadMultiPoint |
|  | ReadMultiPointAsync | niDMM_ReadMultiPoint |
|  | MemoryOptimizedReadMultiPointAsync | niDMM_ReadMultiPoint |
| Ivi.Dmm.IIviDmmMeasurement.SendSoftwareTrigger | SendSoftwareTrigger | niDMM_SendSoftwareTrigger |
|  | IsUnderRange | niDMM_IsUnderRange |
|  | Control | niDMM_Control |
|  | ReadAsync | niDMM_Read |
| Ivi.Dmm.IIviDmmMeasurement.Read | Read | niDMM_Read |
|  | ReadStatus | niDMM_ReadStatus |
|  | DmmTrigger Class |  |
| Ivi.Dmm.IIviDmmTrigger.DelayAuto | DelayAuto | NIDMM_ATTR_TRIGGER_DELAY |
| Ivi.Dmm.IIviDmmTrigger.MeasurementCompleteDestination | MeasurementCompleteDestination | NIDMM_ATTR_MEAS_COMPLETE_DEST |
|  | MeasurementCompleteDestinationSlope | NIDMM_ATTR_MEAS_DEST_SLOPE |
| Ivi.Dmm.IIviDmmTrigger.Configure | Configure | niDMM_ConfigureTrigger |
| Ivi.Dmm.IIviDmmTrigger.Source | Source | NIDMM_ATTR_TRIGGER_SOURCE |
| Ivi.Dmm.IIviDmmTrigger.Slope | Slope | NIDMM_ATTR_TRIGGER_SLOPE |
| Ivi.Dmm.IIviDmmTrigger.Delay | Delay | NIDMM_ATTR_TRIGGER_DELAY |
|  | DmmDriverIdentity Class |  |
| Ivi.Driver.IIviDriverIdentity.GetSupportedInstrumentModels | GetSupportedInstrumentModels | NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS |
| Ivi.Driver.IIviDriverIdentity.GetGroupCapabilities | GetGroupCapabilities | NIDMM_ATTR_GROUP_CAPABILITIES |
| Ivi.Driver.IIviComponentIdentity.Vendor | Vendor | NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR |
| Ivi.Driver.IIviComponentIdentity.Revision | Revision | NIDMM_ATTR_SPECIFIC_DRIVER_REVISION |
| Ivi.Driver.IIviComponentIdentity.Description | Description | NIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION |
| Ivi.Driver.IIviDriverIdentity.Identifier | Identifier | NIDMM_ATTR_INSTR_SERIAL_NUMBER |
| Ivi.Driver.IIviDriverIdentity.InstrumentModel | InstrumentModel | NIDMM_ATTR_INSTRUMENT_MODEL |
| Ivi.Driver.IIviDriverIdentity.InstrumentManufacturer | InstrumentManufacturer | NIDMM_ATTR_INSTRUMENT_MANUFACTURER |
| Ivi.Driver.IIviDriverIdentity.InstrumentFirmwareRevision | InstrumentFirmwareRevision | NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION |
|  | SpecificDriverPrefix | NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX |
|  | SpecificDriverMinorVersion | NIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION |
|  | SpecificDriverMajorVersion | NIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION |
|  | DmmDriverUtility Class |  |
| Ivi.Driver.IIviDriverUtility.SelfTest | SelfTest | niDMM_self_test |
| Ivi.Driver.IIviDriverUtility.ErrorQuery | ErrorQuery | niDMM_error_query |
|  | RevisionQuery | NIDMM_ATTR_SPECIFIC_DRIVER_REVISION |
| Ivi.Driver.IIviDriverUtility.Disable | Disable | niDMM_Disable |
| Ivi.Driver.IIviDriverUtility.ResetWithDefaults | ResetWithDefaults | niDMM_ResetWithDefaults |
| Ivi.Driver.IIviDriverUtility.Lock | Lock |  |
| Ivi.Driver.IIviDriverUtility.Reset | Reset | niDMM_reset |
|  | DmmDriverOperation Class |  |
| Ivi.Driver.IIviDriverOperation.ResetInterchangeCheck | ResetInterchangeCheck | niDMM_ResetInterchangeCheck |
| Ivi.Driver.IIviDriverOperation.InvalidateAllAttributes | InvalidateAllAttributes | niDMM_Control |
| Ivi.Driver.IIviDriverOperation.IOResourceDescriptor | IOResourceDescriptor | NIDMM_ATTR_RESOURCE_DESCRIPTOR |
| Ivi.Driver.IIviDriverOperation.LogicalName | LogicalName | NIDMM_ATTR_LOGICAL_NAME |
| Ivi.Driver.IIviDriverOperation.Simulate | Simulate | NIDMM_ATTR_SIMULATE |
|  | RecordValueCoercions | NIDMM_ATTR_RECORD_COERCIONS |
| Ivi.Driver.IIviDriverOperation.RangeCheck | RangeCheck | NIDMM_ATTR_RANGE_CHECK |
| Ivi.Driver.IIviDriverOperation.QueryInstrumentStatus | QueryInstrumentStatus | NIDMM_ATTR_QUERY_INSTR_STATUS |
|  | InterchangeCheck | NIDMM_ATTR_INTERCHANGE_CHECK |
| Ivi.Driver.IIviDriverOperation.DriverSetup | DriverSetup | NIDMM_ATTR_DRIVER_SETUP |
| Ivi.Driver.IIviDriverOperation.Cache | Cache | NIDMM_ATTR_CACHE |
|  | DmmWaveformAcquisition Class |  |
|  | ReadWaveform | niDMM_ReadWaveform |
|  | MemoryOptimizedReadWaveform | niDMM_ReadWaveform |
|  | ReadWaveformAsync | niDMM_ReadWaveform |
|  | MemoryOptimizedReadWaveformAsync | niDMM_ReadWaveform |
|  | FetchWaveform | niDMM_FetchWaveform |
|  | MemoryOptimizedFetchWaveform | niDMM_FetchWaveform |
|  | FetchWaveformAsync | niDMM_FetchWaveform |
|  | MemoryOptimizedFetchWaveformAsync | niDMM_FetchWaveform |
|  | Rate | NIDMM_ATTR_WAVEFORM_RATE |
|  | NumberOfPoints | NIDMM_ATTR_WAVEFORM_POINTS |
|  | Coupling | NIDMM_ATTR_WAVEFORM_COUPLING |
|  | DmmMultiPoint Class |  |
| Ivi.Dmm.IIviDmmMultiPoint.Configure | Configure | niDMM_ConfigureMultiPoint |
| Ivi.Dmm.IIviDmmMultiPoint.TriggerCount | TriggerCount | NIDMM_ATTR_TRIGGER_COUNT |
|  | SampleTriggerSlope | NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE |
| Ivi.Dmm.IIviDmmMultiPoint.SampleTrigger | SampleTrigger | NIDMM_ATTR_SAMPLE_TRIGGER |
| Ivi.Dmm.IIviDmmMultiPoint.SampleInterval | SampleInterval | NIDMM_ATTR_SAMPLE_INTERVAL |
|  | SampleDelayMode | NIDMM_ATTR_SAMPLE_DELAY_MODE |
| Ivi.Dmm.IIviDmmMultiPoint.SampleCount | SampleCount | NIDMM_ATTR_SAMPLE_COUNT |
|  | Latency | NIDMM_ATTR_LATENCY |
|  | BufferSize | NIDMM_ATTR_BUFFER_SIZE |
|  | DmmAdvancedCapacitanceAndInductance Class |  |
|  | NumberOfLCMeasurementsToAverage | NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE |
|  | DCBias | NIDMM_ATTR_DC_BIAS |
|  | LCCalculationModel | NIDMM_ATTR_LC_CALCULATION_MODEL |
|  | DmmFrequency Class |  |
| Ivi.Dmm.IIviDmmFrequency.VoltageAutoRange | VoltageAutoRange | NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE |
| Ivi.Dmm.IIviDmmFrequency.VoltageRange | VoltageRange | NIDMM_ATTR_FREQ_VOLTAGE_RANGE |
|  | DmmTemperature Class |  |
|  | ConfigureThermistorCustom | niDMM_ConfigureThermistorCustom |
|  | ThermistorType | niDMM_ConfigureThermistorType |
| Ivi.Dmm.IIviDmmTemperature.TransducerType | TransducerType | niDMM_ConfigureTransducerType |
|  | ThermistorA | NIDMM_ATTR_TEMP_THERMISTOR_A |
|  | ThermistorB | NIDMM_ATTR_TEMP_THERMISTOR_B |
|  | ThermistorC | NIDMM_ATTR_TEMP_THERMISTOR_C |
|  | DmmThermocouple Class |  |
| Ivi.Dmm.IIviDmmThermocouple.ReferenceJunctionType | ReferenceJunctionType | NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE |
| Ivi.Dmm.IIviDmmThermocouple.FixedReferenceJunction | FixedReferenceJunction | NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC |
| Ivi.Dmm.IIviDmmThermocouple.Type | Type | NIDMM_ATTR_TEMP_TC_TYPE |
| Ivi.Dmm.IIviDmmThermocouple.Configure | Configure | niDMM_ConfigureThermocouple |
|  | DmmRtd Class |  |
|  | A | NIDMM_ATTR_TEMP_RTD_A |
|  | B | NIDMM_ATTR_TEMP_RTD_B |
|  | C | NIDMM_ATTR_TEMP_RTD_C |
| Ivi.Dmm.IIviDmmRtd.Resistance | Resistance | NIDMM_ATTR_TEMP_RTD_RES |
| Ivi.Dmm.IIviDmmRtd.Type | Type | NIDMM_ATTR_TEMP_RTD_TYPE |
|  | ConfigureCustom | niDMM_ConfigureRTDCustom |

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/mapping-enums-dmm-dotnet.html language=enus -->
## TOPIC 00009: Mapping the NI-DMM .NET API Enums and Enum Values to the NI-DMM C API Attributes and Values

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/mapping-enums-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/mapping-enums-dmm-dotnet.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Mapping the NI-DMM .NET API Enums and Enum Values to the NI-DMM C API Attributes and Values

The following table maps the NI-DMM .NET API enums and enum values to the corresponding NI-DMM C API attributes and values.
 All .NET members are in the **NationalInstruments.ModularInstruments.NIDmm** namespace.

| .NET API Enums and Enum Values | C API Attributes and Values |
| --- | --- |
| DmmMeasurementFunction | NIDMM_ATTR_FUNCTION |
| DCVolts | NIDMM_VAL_DC_VOLTS |
| ACVolts | NIDMM_VAL_AC_VOLTS |
| DCCurrent | NIDMM_VAL_DC_CURRENT |
| ACCurrent | NIDMM_VAL_AC_CURRENT |
| TwoWireResistance | NIDMM_VAL_2_WIRE_RES |
| FourWireResistance | NIDMM_VAL_4_WIRE_RES |
| Frequency | NIDMM_VAL_FREQ |
| Period | NIDMM_VAL_PERIOD |
| ACVoltsDCCoupled | NIDMM_VAL_AC_VOLTS_DC_COUPLED |
| Diode | NIDMM_VAL_DIODE |
| Capacitance | NIDMM_VAL_CAPACITANCE |
| Inductance | NIDMM_VAL_INDUCTANCE |
| WaveformVoltage | NIDMM_VAL_WAVEFORM_VOLTAGE |
| WaveformCurrent | NIDMM_VAL_WAVEFORM_CURRENT |
| DmmAdcCalibration | NIDMM_ATTR_ADC_CALIBRATION |
| Auto | NIDMM_VAL_ADC_CALIBRATION_AUTO |
| Off | NIDMM_VAL_ADC_CALIBRATION_OFF |
| On | NIDMM_VAL_ADC_CALIBRATION_ON |
| DmmAuto | NIDMM_ATTR_AUTO_ZERO |
| Auto | NIDMM_VAL_AUTO_ZERO_AUTO |
| Off | NIDMM_VAL_AUTO_ZERO_OFF |
| On | NIDMM_VAL_AUTO_ZERO_ON |
| Once | NIDMM_VAL_AUTO_ZERO_ONCE |
| DmmDCNoiseRejection | NIDMM_ATTR_DC_NOISE_REJECTION |
| Auto | NIDMM_VAL_DCNR_AUTO |
| Normal | NIDMM_VAL_DCNR_NORMAL |
| SecondOrder | NIDMM_VAL_DCNR_SECOND_ORDER |
| HighOrder | NIDMM_VAL_DCNR_HIGH_ORDER |
| DmmOffsetCompensatedOhm | NIDMM_ATTR_OFFSET_COMP_OHMS |
| Off | NIDMM_VAL_OFFSET_COMP_OHMS_OFF |
| On | NIDMM_VAL_OFFSET_COMP_OHMS_ON |
| DmmCableCompensationType | NIDMM_ATTR_CABLE_COMP_TYPE |
| None | NIDMM_VAL_CABLE_COMP_NONE |
| Open | NIDMM_VAL_CABLE_COMP_OPEN |
| Short | NIDMM_VAL_CABLE_COMP_SHORT |
| OpenAndShort | NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT |
| DmmLCCalculationModel | NIDMM_ATTR_LC_CALCULATION_MODEL |
| Auto | NIDMM_VAL_CALC_MODEL_AUTO |
| Series | NIDMM_VAL_CALC_MODEL_SERIES |
| Parallel | NIDMM_VAL_CALC_MODEL_PARALLEL |
| DmmDcBias | NIDMM_ATTR_DC_BIAS |
| Off | NIDMM_VAL_DC_BIAS_OFF |
| On | NIDMM_VAL_DC_BIAS_ON |
| DmmSlope | NIDMM_ATTR_MEAS_DEST_SLOPE |
| Positive | NIDMM_VAL_POSITIVE |
| Negative | NIDMM_VAL_NEGATIVE |
| DmmApertureTimeUnits | NIDMM_ATTR_APERTURE_TIME_UNITS |
| Seconds | NIDMM_VAL_SECONDS |
| PowerLineCycles | NIDMM_VAL_POWER_LINE_CYCLES |
| DmmOperationMode | NIDMM_ATTR_OPERATION_MODE |
| IvidmmMode | NIDMM_VAL_IVIDMM_MODE |
| WaveformMode | NIDMM_VAL_WAVEFORM_MODE |
| DmmWaveformCoupling | NIDMM_ATTR_WAVEFORM_COUPLING |
| AC | NIDMM_VAL_WAVEFORM_COUPLING_AC |
| DC | NIDMM_VAL_WAVEFORM_COUPLING_DC |
| DmmTransducerType | niDMM_ConfigureTransducerType |
| TwoWireRtd | NIDMM_VAL_2_WIRE_RTD |
| FourWireRtd | NIDMM_VAL_4_WIRE_RTD |
| Thermistor | NIDMM_VAL_THERMISTOR |
| Thermocouple | NIDMM_VAL_THERMOCOUPLE |
| DmmThermocoupleType | NIDMM_ATTR_TEMP_TC_TYPE |
| B | NIDMM_VAL_TEMP_TC_B |
| E | NIDMM_VAL_TEMP_TC_E |
| J | NIDMM_VAL_TEMP_TC_J |
| K | NIDMM_VAL_TEMP_TC_K |
| N | NIDMM_VAL_TEMP_TC_N |
| R | NIDMM_VAL_TEMP_TC_R |
| S | NIDMM_VAL_TEMP_TC_S |
| T | NIDMM_VAL_TEMP_TC_T |
| DmmThermistorType | NIDMM_ATTR_TEMP_THERMISTOR_TYPE |
| Custom | NIDMM_VAL_TEMP_THERMISTOR_CUSTOM |
| Thermistor44004 | NIDMM_VAL_TEMP_THERMISTOR_44004 |
| Thermistor44006 | NIDMM_VAL_TEMP_THERMISTOR_44006 |
| Thermistor44007 | NIDMM_VAL_TEMP_THERMISTOR_44007 |
| DmmRtdType | NIDMM_ATTR_TEMP_RTD_TYPE |
| Custom | NIDMM_VAL_TEMP_RTD_CUSTOM |
| PT3851 | NIDMM_VAL_TEMP_RTD_PT3851 |
| PT3750 | NIDMM_VAL_TEMP_RTD_PT3750 |
| PT3916 | NIDMM_VAL_TEMP_RTD_PT3916 |
| PT3920 | NIDMM_VAL_TEMP_RTD_PT3920 |
| PT3911 | NIDMM_VAL_TEMP_RTD_PT3911 |
| PT3928 | NIDMM_VAL_TEMP_RTD_PT3928 |
| DmmReferenceJunctionType | NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE |
| Fixed | NIDMM_VAL_TEMP_REF_JUNC_FIXED |
| DmmDelayMode | NIDMM_ATTR_SAMPLE_DELAY_MODE |
| IntervalSampleTrigger | NIDMM_ATTR_SAMPLE_INTERVAL |
| AnySampleTrigger | NIDMM_ATTR_SAMPLE_ANY |
| DmmControlAction | niDMM_Control |
| Commit | NIDMM_VAL_CONTROL_COMMIT |
| DmmCalibrationType | niDMM_GetCalCount |
| SelfCalibration | NIDMM_VAL_INTERNAL_AREA |
| External | NIDMM_VAL_EXTERNAL_AREA |
| DmmMeasurementCompleteDestination | NIDMM_ATTR_MEAS_COMPLETE_DEST |
| None | NIDMM_VAL_NONE |
| External | NIDMM_VAL_EXTERNAL |
| Ttl0 | NIDMM_VAL_TTL0 |
| Ttl1 | NIDMM_VAL_TTL1 |
| Ttl2 | NIDMM_VAL_TTL2 |
| Ttl3 | NIDMM_VAL_TTL3 |
| Ttl4 | NIDMM_VAL_TTL4 |
| Ttl5 | NIDMM_VAL_TTL5 |
| Ttl6 | NIDMM_VAL_TTL6 |
| Ttl7 | NIDMM_VAL_TTL7 |
| LbrTrig0 | NIDMM_VAL_LBR_TRIG_0 |
| DmmSampleTrigger | NIDMM_ATTR_SAMPLE_TRIGGER |
| Immediate | NIDMM_VAL_IMMEDIATE |
| External | NIDMM_VAL_EXTERNAL |
| SoftwareTrigger | NIDMM_VAL_SOFTWARE_TRIG |
| Ttl0 | NIDMM_VAL_TTL0 |
| Ttl1 | NIDMM_VAL_TTL1 |
| Ttl2 | NIDMM_VAL_TTL2 |
| Ttl3 | NIDMM_VAL_TTL3 |
| Ttl4 | NIDMM_VAL_TTL4 |
| Ttl5 | NIDMM_VAL_TTL5 |
| Ttl6 | NIDMM_VAL_TTL6 |
| Ttl7 | NIDMM_VAL_TTL7 |
| PxiStar | NIDMM_VAL_PXI_STAR |
| LbrTrig1 | NIDMM_VAL_LBR_TRIG_1 |
| AuxTrig1 | NIDMM_VAL_AUX_TRIG_1 |
| Interval | NIDMM_VAL_INTERVAL |
| DmmTriggerSource | NIDMM_ATTR_TRIGGER_SOURCE |
| Immediate | NIDMM_VAL_IMMEDIATE |
| External | NIDMM_VAL_EXTERNAL |
| SoftwareTrigger | NIDMM_VAL_SOFTWARE_TRIG |
| Ttl0 | NIDMM_VAL_TTL0 |
| Ttl1 | NIDMM_VAL_TTL1 |
| Ttl2 | NIDMM_VAL_TTL2 |
| Ttl3 | NIDMM_VAL_TTL3 |
| Ttl4 | NIDMM_VAL_TTL4 |
| Ttl5 | NIDMM_VAL_TTL5 |
| Ttl6 | NIDMM_VAL_TTL6 |
| Ttl7 | NIDMM_VAL_TTL7 |
| PxiStar | NIDMM_VAL_PXI_STAR |
| LbrTrig1 | NIDMM_VAL_LBR_TRIG_1 |
| AuxTrig1 | NIDMM_VAL_AUX_TRIG_1 |

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/overview-dmm-dotnet.html language=enus -->
## TOPIC 00010: NI-DMM .NET Class Library Help

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/overview-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/overview-dmm-dotnet.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-DMM .NET Class Library Help

You can use the NI-DMM .NET Class Library to initialize, configure, and read from your NI-DMM instrument.

For additional information on developing applications using NI drivers and the .NET Framework, refer to 
 [ni.com/mstudio](http://www.ni.com/mstudio/) or visit 
 [ni.com/info](http://www.ni.com/info/) and enter the Info Code 
 NIdotNET.

You can find example applications by selecting 
 **National Instruments»****NI-DMM»****NI-DMM Examples** in the Start menu.

|  | Note Integrated help for IVI Foundation interfaces is not provided. You must use the IntelliSense help. |
| --- | --- |

© 2016-2017 National Instruments. All rights reserved.

Related concepts

Using Memory-Optimized and Async Methods to Fetch and Read

NI-DMM .NET Programming Flow

Related tasks

Using the NI-DMM .NET Class Library in IVI.NET Applications

Related reference

Mapping the NI-DMM .NET API Enums and Enum Values to the NI-DMM C API Attributes and Values

Mapping the NI-DMM .NET API to the NI-DMM C API

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/patents.html language=enus -->
## TOPIC 00011: Patents

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/patents.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/patents.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### Patents

Help»Patents

patents.txt

National Instruments Patent Notice

ni.com/patents

Parent topic:

Legal Information

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/program-flow-dmm-dotnet.html language=enus -->
## TOPIC 00012: NI-DMM .NET Programming Flow

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/program-flow-dmm-dotnet.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/program-flow-dmm-dotnet.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-DMM .NET Programming Flow

You can use the NIDmm .NET class library to initialize, configure, and read from your NI-DMM device. NI-DMM .NET, an Interchangeable
 Virtual Instrument (IVI)-compliant instrument driver, features a set of methods and properties that exercise the functionality
 of the NI-DMM hardware.

|  | Tip For more information, refer to the Programming with NI-DMM topic in the NI Digital Multimeters Help. |
| --- | --- |

The following diagram shows the basic programming flow of applications using NI-DMM.

[IMAGE alt='NI-DMM Programming Workflow Diagram' src='guid-93266187-2881-4b64-8bd2-136881eb93ae-5.5x8.5_-_a5.png']

#### Initializing a New NIDmm Session Object

For any application you write, you need to create a new **NIDmm** session object to establish communication with your NI-DMM device. In addition to establishing a session with the NI-DMM
 device in .NET, creating a new session object also sends initialization commands to set the instrument to the state necessary
 for the operation of the instrument driver.

#### Configuring the Hardware

You can configure NI-DMM .NET to acquire single point measurements, multipoint measurements, and waveform acquisitions. If
 you are configuring NI-DMM .NET directly by setting properties, you need to also set **OperationMode**. If you are configuring NI-DMM .NET using a configuration method, then you can determine the configuration method depending
 on the type of acquisition you use in your application. For example, **DmmTrigger** contains methods and properties for configuring triggers, and **DmmAdvanced** contains methods and properties for advanced configurations such as **PowerlineFrequency** and **OperationMode**. Set this property to **WaveformMode** for waveform acquisition and to **IviDmmMode** to work in IVI applications.

#### Acquiring Data

After you have configured your NI-DMM device, you can acquire data by calling **Read** or **Initiate** and **Fetch**. For multipoint acquisitions, you can use **ReadMultiPoint** or **Initiate** and **FetchMultiPoint**, and for waveform acquisitions you can use **ReadWaveform** or**Initiate** and **FetchWaveform**.

#### Closing the Session

When your acquisition is complete, close the instrument I/O session with **Close** or **Dispose**. **Close** destroys the session and all of its attributes and deallocates any memory resources used by the **NIDmm**. **Dispose** calls **Close**, then disposes the .NET object.

|  | Note If the NIDmm session in use was created using an IntPtr, then calling Close or Dispose on the session does not destroy the underlying instrument handle. |
| --- | --- |

#### Configuring the NIDmm for Reading

The code snippet below creates and configures an **NIDmm** object to read DC voltage with a specific range and resolution and then closes the session.

```text
VB.NET

Dim sampleDmmSession As New NIDmm("DMM-4072", True, True)
Dim range As Double = 100 
Dim resolution As Double = 6.5
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution)
Dim reading As Double = sampleDmmSession.Measurement.Read()
sampleDmmSession.Close()
```

```text
C#

NIDmm sampleDmmSession = new NIDmm("DMM-4072", true, true);
double range = 100;
double resolution = 6.5;
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution);
double reading = sampleDmmSession.Measurement.Read();
sampleDmmSession.Close();
```

#### Configuring NI-DMM .NET for Multipoint Operations

The code snippet below demonstrates how to:

1. Create and configure an NIDmm object to read DC voltage with a specific range and resolution;
2. Acquire a multipoint measurement of 10 samples;
3. Use ReadStatus to determine the number of samples acquired;
4. Call FetchMultiPoint when a sufficient number of samples is acquired; and
5. Call Close to end the session and deallocate any memory resources used by this NIDmm .

```text
VB.NET

Dim sampleDmmSession As New NIDmm("DMM-4072", True, True)
Dim range As Double = 100 
Dim resolution As Double = 6.5 
Dim numberOfSamples As Integer = 10 
Dim acquisitionBacklog As Integer = 0
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution)
sampleDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples
sampleDmmSession.Trigger.Source = DmmTriggerSource.Immediate
sampleDmmSession.Measurement.Initiate()
While acquisitionBacklog < numberOfSamples 
    sampleDmmSession.Measurement.ReadStatus(acquisitionBacklog)
End While 
Dim readingArray As Double() = sampleDmmSession.Measurement.FetchMultiPoint(PrecisionTimeSpan.FromMilliseconds(2000), acquisitionBacklog)
sampleDmmSession.Close()
```

```text
C#

NIDmm sampleDmmSession = new NIDmm("DMM-4072", true, true);
double range = 100;
double resolution = 6.5;
int numberOfSamples = 10;
int acquisitionBacklog=0;
sampleDmmSession.ConfigureMeasurementDigits(DmmMeasurementFunction.DCVolts, range, resolution);
sampleDmmSession.Trigger.MultiPoint.SampleCount = numberOfSamples;
sampleDmmSession.Trigger.Source = DmmTriggerSource.Immediate;
sampleDmmSession.Measurement.Initiate();
while (acquisitionBacklog < numberOfSamples) 
    sampleDmmSession.Measurement.ReadStatus(out acquisitionBacklog);
double[] readingArray = sampleDmmSession.Measurement.FetchMultiPoint(PrecisionTimeSpan.FromMilliseconds(2000), acquisitionBacklog);
sampleDmmSession.Close();
```

Parent topic:

NI-DMM .NET Class Library Help

<!--NI_TOPIC bundle=ni-dmm-20.0-dot-net-api-ref path=ninetdmmfx40/warning.html language=enus -->
## TOPIC 00013: WARNING REGARDING USE OF NATIONAL INSTRUMENTS PRODUCTS

- bundle_id: `ni-dmm-20.0-dot-net-api-ref`
- source_path: `ninetdmmfx40/warning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-20.0-dot-net-api-ref/raw/resource/enus/ninetdmmfx40/warning.html
- document_id: `ni-dmm-20.0-dot-net-api-ref`
- page_type: `leaf`
- content_type: ``

### WARNING REGARDING USE OF NATIONAL INSTRUMENTS PRODUCTS

YOU ARE ULTIMATELY RESPONSIBLE FOR VERIFYING AND VALIDATING THE SUITABILITY AND RELIABILITY OF THE PRODUCTS WHENEVER THE
 PRODUCTS ARE INCORPORATED IN YOUR SYSTEM OR APPLICATION, INCLUDING THE APPROPRIATE DESIGN, PROCESS, AND SAFETY LEVEL OF SUCH
 SYSTEM OR APPLICATION.

PRODUCTS ARE NOT DESIGNED, MANUFACTURED, OR TESTED FOR USE IN LIFE OR SAFETY CRITICAL SYSTEMS, HAZARDOUS ENVIRONMENTS OR ANY
 OTHER ENVIRONMENTS REQUIRING FAIL-SAFE PERFORMANCE, INCLUDING IN THE OPERATION OF NUCLEAR FACILITIES; AIRCRAFT NAVIGATION;
 AIR TRAFFIC CONTROL SYSTEMS; LIFE SAVING OR LIFE SUSTAINING SYSTEMS OR SUCH OTHER MEDICAL DEVICES; OR ANY OTHER APPLICATION
 IN WHICH THE FAILURE OF THE PRODUCT OR SERVICE COULD LEAD TO DEATH, PERSONAL INJURY, SEVERE PROPERTY DAMAGE OR ENVIRONMENTAL
 HARM (COLLECTIVELY, "HIGH-RISK USES"). FURTHER, PRUDENT STEPS MUST BE TAKEN TO PROTECT AGAINST FAILURES, INCLUDING PROVIDING
 BACK-UP AND SHUT-DOWN MECHANISMS. NI EXPRESSLY DISCLAIMS ANY EXPRESS OR IMPLIED WARRANTY OF FITNESS OF THE PRODUCTS OR SERVICES
 FOR HIGH-RISK USES.

Parent topic:

Legal Information
