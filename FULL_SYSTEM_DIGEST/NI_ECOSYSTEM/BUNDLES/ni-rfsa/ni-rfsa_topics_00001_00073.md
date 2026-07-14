# NI DOCUMENT BUNDLE: ni-rfsa

<!--NI_BUNDLE_CHUNK bundle=ni-rfsa start=1 end=73 -->
<!--NI_TOPIC bundle=ni-rfsa path=a-device-does-not-appear-in-max.html language=enus -->
## TOPIC 00001: A Device Does Not Appear in MAX

- bundle_id: `ni-rfsa`
- source_path: `a-device-does-not-appear-in-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/a-device-does-not-appear-in-max.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your NI-RFSA device does not appear in MAX, complete the following steps: In the MAX configuration tree, expand the Chassis tree. Press <F5> to refresh the list of installed devices. If the NI-RFSA device is still not listed, power off the system, ensure that the NI-RFSA device is correctly insta

### A Device Does Not Appear in MAX

If your NI-RFSA device does not appear in MAX, complete the following steps:

1. In the MAX configuration tree, expand the Chassis tree.
2. Press <F5> to refresh the list of installed devices.
3. If the NI-RFSA device is still not listed, power off the system, ensure that the
 NI-RFSA device is correctly installed, and restart the system.
4. Navigate to the Device Manager.
  - (Windows 10/8.1) Right-click the Start button, and
 select Device Manager .
  - (Windows 7) Select
 Start » Control
 Panel » Device Manager .
5. If you are using a PXI controller, verify that a National
 Instruments entry appears in the system device list. Reinstall the
 driver software and the hardware devices if error conditions are present in the
 list. If you are using a MXI-3 controller, right-click PCI-to-PCI
 Bridge and select Configure from the shortcut
 menu to verify that the bridge is enabled.
6. If the NI-RFSA device still fails to appear in MAX, contact NI technical support or
 visit
 ni.com/support.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=acquiring-data-net.html language=enus -->
## TOPIC 00002: Acquire Data With the NI-RFSA .NET Class Library

- bundle_id: `ni-rfsa`
- source_path: `acquiring-data-net.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/acquiring-data-net.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can acquire data with the NI-RFSA .NET class library with a fetch method or a read method. You can configure NI-RFSA to acquire data in one of the following modes: IQ Spectrum Spectrum mode supports only read methods. IQ Mode The following code snippet shows how to configure NIRfsa to acquire da

### Acquire Data With the NI-RFSA .NET Class Library

You can acquire data with the NI-RFSA .NET class library
 with a fetch method or a read method.

You can configure NI-RFSA to acquire data in one of the following modes:

- IQ
- Spectrum

Note

#### IQ Mode

The following code snippet shows how to configure NIRfsa to
 acquire data in IQ mode.

Note

NIRfsa

```text
VB.NET

session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ
```

```text
Visual C#

session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ;
```

#### Spectrum Mode

You can only use spectrum mode with single record read methods. You can't use
 spectrum mode with fetch methods. Spectrum mode supports both regular and
 memory-optimized read methods. Spectrum mode supports only the double data type.

The following code snippet shows how to configure NIRfsa to
 acquire data in Spectrum mode.

Note

NIRfsa

```text
VB.NET

session.Configuration.AcquisitionType = RfsaAcquisitionType.Spectrum
```

```text
Visual C#

session.Configuration.AcquisitionType = RfsaAcquisitionType.Spectrum;
```

#### Using the Fetch Method to Acquire Data

Follow these steps to acquire data with a Fetch method:

1. Initialize NIRfsa .
2. Configure NIRfsa .
3. Use Initiate to initiate acquisition.
4. Use Fetch to transfer the acquired samples from the NI-RFSA device memory to the system memory.

You can fetch the acquired data either as a single record or as a set of multiple
 records. Both single and multi-record fetch methods support a regular fetch
 acquisition or a memory-optimized acquisition. You can fetch data as one of the
 following data types:

- ComplexDouble
- ComplexInt16
- ComplexWaveform<ComplexDouble> (for single record acquisition) or
 ComplexWaveformCollection<ComplexDouble> (for multi record acquisition)
- ComplexWaveform<ComplexInt16> (for single record acquisition) or
 ComplexWaveformCollection<ComplexInt16> (for multi record acquisition)

Some examples of NI-RFSA fetch methods include:

- FetchIQSingleRecordComplex<T>
- MemoryOptimizedFetchIQSingleRecordComplexWaveform<T>
- FetchIQMultiRecordComplexWaveforms<T>

Refer to the *NI-RFSA C# .NET API Reference Manual* for a complete list of
 fetch methods.

The following code snippet shows a single-record memory-optimized fetch method:

```text
VB.NET

Using session As New NIRfsa("Rfsa", True, True)
    session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ
    session.Configuration.Vertical.ReferenceLevel = -10.0
    session.Configuration.IQ.CarrierFrequency = 10000000.0
    session.Configuration.IQ.NumberOfSamples = 1000
    Dim data As New ComplexWaveform(Of ComplexDouble)(1000)
    session.Acquisition.IQ.Initiate()
    session.Acquisition.IQ.MemoryOptimizedFetchIQSingleRecordComplexWaveform(Of ComplexDouble)(0, 1000, New PrecisionTimeSpan(5), data)
End Using
```

```text
Visual C#

using (NIRfsa session = new NIRfsa("Rfsa", true, true))
{
session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ;
session.Configuration.Vertical.ReferenceLevel = -10.0;
session.Configuration.IQ.CarrierFrequency = 10E+6;
session.Configuration.IQ.NumberOfSamples = 1000;
ComplexWaveform<ComplexDouble> data = new ComplexWaveform<ComplexDouble>(1000);
session.Acquisition.IQ.Initiate();
session.Acquisition.IQ.MemoryOptimizedFetchIQSingleRecordComplexWaveform<ComplexDouble>(0, 1000, new PrecisionTimeSpan(5),ref data);
}
```

#### Using the Read Method to Acquire Data

Follow these steps to acquire data with a read method:

1. Initialize NIRfsa .
2. Configure NIRfsa .
3. Use a read method to initiate the acquisition.
4. Wait for the acquisition to finish and retrieve the data.

Unlike fetch methods, read methods support only common use cases. Multi-record read
 methods don't exist.

You can read data as one of the following data types:

- ComplexDouble
- ComplexWaveform<ComplexDouble>

Some examples of NIRfsa read methods include:

- ReadIQSingleRecordComplex
- ReadIQSingleRecordComplexWaveform
- MemoryOptimizedReadIQSingleRecordComplexWaveform

Refer to the *NI-RFSA C# .NET API Reference Manual* for a complete list of
 read methods.

Parent topic:

Using the NI-RFSA .NET Class Library

Related information:

- NI-RFSA C# .NET API Reference Manual

<!--NI_TOPIC bundle=ni-rfsa path=additional-ni-rfsa-sfp-features.html language=enus -->
## TOPIC 00003: Additional NI-RFSA SFP Features

- bundle_id: `ni-rfsa`
- source_path: `additional-ni-rfsa-sfp-features.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/additional-ni-rfsa-sfp-features.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Video Bandwidth and Detectors The NI-RFSA SFP supports video bandwidth (VBW) and detectors. Refer to Emulating Video Bandwidth and Detectors in an FFT-based Vector Signal Analyzer on ni.com for more information about using VBW and detectors in the SFP. Additional Measurements The SFP supports additi

### Additional NI-RFSA SFP Features

#### Video Bandwidth and Detectors

The NI-RFSA SFP supports video bandwidth (VBW) and detectors. Refer to Emulating
 Video Bandwidth and Detectors in an FFT-based Vector Signal
 Analyzer
 on ni.com for more information about using VBW and detectors in the SFP.

#### Additional Measurements

The SFP supports additional measurements, such as channel power, occupied bandwidth,
 third-order intercept (TOI), complementary cumulative distribution functions (CCDF),
 spectral emission mask, and transmit power. Refer to Performing Measurements in the
 NI-RFSA SFP for more information about performing measurements.

#### Debugging

You can use SFP session access to allow the SFP to access a device with an existing
 open session. Accessing the device session using the SFP can help you debug your
 code. Refer to Debugging Your Application Using SFP Session Access for more
 information about SFP session access.

Parent topic:

NI-RFSA Soft Front Panel

Related concepts:

- Performing Measurements in the NI-RFSA SFP
- Debugging Your Application Using SFP Session Access

<!--NI_TOPIC bundle=ni-rfsa path=associating-modules.html language=enus -->
## TOPIC 00004: Associating Hardware Modules in SystemDesigner

- bundle_id: `ni-rfsa`
- source_path: `associating-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/associating-modules.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you can program your vector signal analyzer, you must create an association between the individual hardware modules to control them as a single RF device. After launching LabVIEW NXG, complete the following steps to associate your hardware modules. When you associate modules in SystemDesigner

### Associating Hardware Modules in SystemDesigner

Before you can program your vector signal analyzer, you must create an association between the individual hardware modules to control them as a single RF device.

Note

1. Open the Live view in SystemDesigner.
2. On the diagram, select the RF signal downconverter for your vector signal analyzer.
3. On the 
 Item tab in the Configuration pane, expand 
 Configure vector signal analyzer.
4. Select the appropriate hardware module from each system component drop-down listbox. 
 Note Select 
 Not Specified if you do not want to associate a specific module with the downconverter. Select 
 External if you want to use an external module, such as a third-party LO or digitizer, with your downconverter. 
 Once you associate all the modules, your vector signal analyzer model displays underneath the label of the downconverter on the Live view.

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsa path=associating-ni-rfsa-modules.html language=enus -->
## TOPIC 00005: Associating NI-RFSA Modules

- bundle_id: `ni-rfsa`
- source_path: `associating-ni-rfsa-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/associating-ni-rfsa-modules.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: To control multiple hardware modules as a single RF device, you must first associate the modules. MAX treats the hardware modules as separate devices. You must associate the devices for transparent operation of all hardware modules as a single device using NI-RFSA. The association requirement is app

### Associating NI-RFSA Modules

To control multiple hardware modules as a single RF device, you must first associate
 the modules.

- PXI-5661
- PXIe-5663/5663E/5665/5667/5668/5668 with PXIe-5698
- PXIe-5830/5831/5831 with PXIe-5653/5832/5841 with PXIe-5655

Complete the following steps to associate modules in MAX:

1. In the configuration tree, select the module associated with your hardware system,
 as identified in the following table.
2. In the Associated Devices section for the selected module, select the appropriate
 module from each system component drop-down list. Refer to the following table for a
 complete list of device associations.
3. Click Save in the MAX toolbar.

| Hardware System | Associations |
| --- | --- |
| PXI-5661 | Select the PXI-5600 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXI-5142 from the Digitizer list. |
| PXIe-5663/5663E | Select the PXI-5601 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5622 from the Digitizer list and the PXI/PXIe-5652 from the LO list. |
| PXIe-5665 | Select the PXIe-5603/5605 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5622 from the Digitizer list and the PXIe-5653 from the LO list. |
| PXIe-5667 | Select the PXIe-5603/5605 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the following devices: The PXIe-5622 from the Digitizer list The PXIe-5653 from the LO list The PXIe-5693 from the RF Conditioner list The PXIe-5694 from the IF Conditioner list |
| PXIe-5668 | Select the PXIe-5606 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the PXIe-5624 from the Digitizer list and the PXIe-5653 from the LO list. |
| PXIe-5668 with PXIe-5698 | Select the PXIe-5606 RF Signal Downconverter in the configuration tree. In the Associated Devices section, select the following devices: The PXIe-5624 from the Digitizer list The PXIe-5653 from the LO list The PXIe-5698 from the RF Conditioner list |
| PXIe-5830 | Select the PXIe-3621 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list. |
| PXIe-5831 | Select the PXIe-3622 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list. |
| PXIe-5831 with PXIe-5653 | Select the PXIe-3622 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list and the PXIe-5653 from the LO1 (mmWave LO) list. The mmRH-5582 mmWave Radio Head automatically appears as connected in MAX when you expand the PXIe-3622 configuration tree item. |
| PXIe-5832 | Select the PXIe-3623 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list. |
| PXIe-5832 with PXIe-5653 | Select the PXIe-3623 Vector Signal Up/Down Converter in the configuration tree. In the Associated Devices section, select the PXIe-5820 from the Baseband list and the PXIe-5653 from the LO1 (mmWave LO) list. The mmRH-5582 mmWave Radio Head automatically appears as connected in MAX when you expand the PXIe-3623 configuration tree item. |
| PXIe-5841 with PXIe-5655 | Select the PXIe-5841 Vector Signal Transceiver in the configuration tree. In the Associated Devices section, select the PXIe-5655 from the RF In LO and RF Out LO lists. You must select the same PXIe-5655 from both lists. |

Note

Not Specified

External

Note

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=configuring-sfp-session-access-using-labview.html language=enus -->
## TOPIC 00006: Configuring SFP Session Access Using LabVIEW

- bundle_id: `ni-rfsa`
- source_path: `configuring-sfp-session-access-using-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/configuring-sfp-session-access-using-labview.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, LabVIEW enables SFP session access when you launch the SFP from a probe. You can also explicitly enable or disable SFP session access using one of two VIs. NI-RFSA does not support NI-TClk when driver session debugging is enabled. Using the niRFSA Initialize With Options VI To enable S

### Configuring SFP Session Access Using LabVIEW

Note

#### Using the niRFSA Initialize With Options VI

To enable SFP session access using the niRFSA Initialize with
 Options
 VI, create a new device session for your device by wiring the following string into
 the option string input:

DriverSetup=SFPSessionAccess:1

The following figure shows the proper string wired into the niRFSA Initialize with
 Options VI.

[IMAGE alt='image' src='GUID-46CA9A68-5174-4A74-9C41-5621C51A69AD-a5.gif']

Disabling SFP session access prevents users from altering the execution of critical
 test code. To disable SFP session access, wire the following string into the
 option string input:

DriverSetup=SFPSessionAccess:0

Refer to Driver Setup
 Options
 for more information about using the option string
 parameter.

Note

#### Using the niRFSA Enable Session Access VI

To enable SFP session access using the niRFSA Enable Session
 Access
 VI, specify your instrument using the instrument handle input
 and wire TRUE into the session access enabled input.

To disable SFP session access, specify your instrument using the
 instrument handle input and wire FALSE into the
 session access enabled input.

Note

Parent topic:

Configuring SFP Session Access

Related concepts:

- Launching the NI-RFSA SFP from LabVIEW

<!--NI_TOPIC bundle=ni-rfsa path=configuring-sfp-session-access-using-labwindo.html language=enus -->
## TOPIC 00007: Configuring SFP Session Access Using LabWindows/CVI or C

- bundle_id: `ni-rfsa`
- source_path: `configuring-sfp-session-access-using-labwindo.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/configuring-sfp-session-access-using-labwindo.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can enable or disable NI-RFSA Soft Front Panel (SFP) session access with one of two functions. Breakpoints in LabWindows/CVI or C code pause all threads in the attached process, including the session for which SFP session access is enabled. If your code includes breakpoints, configure SFP Sess

### Configuring SFP Session Access Using LabWindows/CVI or C

Note

Note

#### Using the niRFSA_InitWithOptions Function

To enable SFP session access using the
 niRFSA_InitWithOptions
 function, create a new device session for your device and pass the following string
 into the optionString parameter:

DriverSetup=SFPSessionAccess:1

Disabling SFP session access prevents users from altering the execution of critical
 test code. To disable SFP session access, pass the following string into the
 optionString parameter:

DriverSetup=SFPSessionAccess:0

Refer to Driver Setup
 Options
 for more information about using the option string
 parameter.

#### Using the niRFSA_EnableSessionAccess Function

To enable SFP session access using the
 niRFSA_EnableSessionAccess
 function, specify a resourceNameand pass
 VI_TRUE to the enabled parameter.

To disable SFP session access, specify a resourceNameand pass
 VI_FALSE to the enabled parameter.

Note

niRFSA_EnableSessionAccess

niRFSA_InitWithOptions

Parent topic:

Configuring SFP Session Access

Related concepts:

- Configuring SFP Session Access Using the NI-RFSA Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsa path=configuring-sfp-session-access-using-the-ni-r.html language=enus -->
## TOPIC 00008: Configuring SFP Session Access Using the NI-RFSA Soft Front Panel

- bundle_id: `ni-rfsa`
- source_path: `configuring-sfp-session-access-using-the-ni-r.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/configuring-sfp-session-access-using-the-ni-r.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to enable or disable SFP session access using the NI-RFSA Soft Front Panel (SFP). Select Device»Configure Debug. The Configure Debug Session window appears. Select the device or devices you want to debug from the list. Use the Disabled or Enabled button to disable or ena

### Configuring SFP Session Access Using the NI-RFSA Soft Front Panel

Complete the following steps to enable or disable SFP session access using the NI-RFSA
 Soft Front Panel (SFP).

1. Select Device»Configure Debug . The Configure Debug
 Session window appears.
2. Select the device or devices you want to debug from the list.
3. Use the Disabled or Enabled button to
 disable or enable SFP session access.
4. If applicable, select the checkbox next to Using breakpoints in
 C/C++/.NET application? 
 Note Breakpoints in LabWindows/CVI or C code pause all threads in
 the attached process, including the session for which SFP session access is
 enabled. You must select this option to prevent the SFP from pausing with the
 rest of your code.
5. Click OK.
6. Restart your application. Note Your configuration settings are not
 applied until you reopen the device session. Restarting your application ensures
 that the session is reopened.

[IMAGE alt='image' src='GUID-5271ED07-EFA3-4B16-A473-A48C307CC91D-a5.gif']

Note

niRFSA_InitWithOptions

enable

Configure Debug
 Session

Note

Parent topic:

Configuring SFP Session Access

<!--NI_TOPIC bundle=ni-rfsa path=configuring-sfp-session-access.html language=enus -->
## TOPIC 00009: Configuring SFP Session Access

- bundle_id: `ni-rfsa`
- source_path: `configuring-sfp-session-access.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/configuring-sfp-session-access.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, NI-RFSA enables SFP session access when you launch the SFP from a probe in LabVIEW. You can configure SFP session access using the NI-RFSA Soft Front Panel (SFP), using LabVIEW, or using LabWindows/CVI or C.

### Configuring SFP Session Access

By default, NI-RFSA enables SFP session access when you launch the SFP from a probe in
 LabVIEW. You can configure SFP session access using the NI-RFSA Soft Front Panel (SFP),
 using LabVIEW, or using LabWindows/CVI or C.

- [Configuring SFP Session Access Using the NI-RFSA Soft Front Panel](configuring-sfp-session-access-using-the-ni-r.html)
- [Configuring SFP Session Access Using LabVIEW](configuring-sfp-session-access-using-labview.html)
- [Configuring SFP Session Access Using LabWindows/CVI or C](configuring-sfp-session-access-using-labwindo.html)

Parent topic:

Debugging Your Application Using SFP Session Access

<!--NI_TOPIC bundle=ni-rfsa path=creating-an-application.html language=enus -->
## TOPIC 00010: Creating an Application with NI-RFSA

- bundle_id: `ni-rfsa`
- source_path: `creating-an-application.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/creating-an-application.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSA controls the configuration and operation of NI-RFSA devices using LabVIEW software and LabWindows/CVI, as well as conventional programming languages such as Microsoft Visual C/C++/C# or VB .NET.

### Creating an Application with NI-RFSA

NI-RFSA controls the configuration and operation of NI-RFSA devices using LabVIEW software and LabWindows/CVI, as well as conventional programming languages such as Microsoft Visual C/C++/C# or VB .NET.

- [Using NI-RFSA in LabVIEW](using-labview.html)
- [Using NI-RFSA in LabWindows/CVI](using-labwindows-cvi.html) Complete the following steps to develop an NI-RFSA application in LabWindows/CVI:
- [Using NI-RFSA with Microsoft Visual C/C++](using-microsoft-visual.html) You can develop an NI-RFSA application using Microsoft Visual C/C++ with Microsoft Visual C++ 6.0 or Microsoft Visual Studio 2010. Follow these general steps to create a C/C++ application.
- [Using the NI-RFSA .NET Class Library with Microsoft Visual Studio](using-net.html) You can use the NI-RFSA .NET Class Library with Microsoft Visual C# .NET or Microsoft Visual Basic .NET in any Visual Studio version that can target .NET Framework 4.0 or .NET Framework 4.5.

Parent topic:

Getting Started with NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=creating-dynamic-and-static-signal-routes-for.html language=enus -->
## TOPIC 00011: Creating Dynamic and Static Signal Routes for an NI-RFSA Device

- bundle_id: `ni-rfsa`
- source_path: `creating-dynamic-and-static-signal-routes-for.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/creating-dynamic-and-static-signal-routes-for.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: To establish a dynamic route across segments, you must specify a fully qualified terminal name for the source and the destination signal. In the configuration tree, double-click Device and Interfaces to see a list of installed devices. Installed devices appear under the name of their associated chas

### Creating Dynamic and Static Signal Routes for an NI-RFSA Device

To establish a dynamic route across segments, you must specify a fully qualified
 terminal name for
 the source and the destination signal.

1. In the configuration tree, double-click Device and Interfaces 
 to see a list of installed devices. Installed devices appear under the name of their
 associated chassis. Note 
 If you are using your NI-RFSA device with the LabVIEW Real-Time Module, expand
 Remote Systems. Find your target IP address or name,
 expand it, and then expand Devices and
 Interfaces.
2. Select your chassis in the configuration tree. The attributes of your chassis are
 displayed on the right of the MAX window.
3. Click the Trigger tab below the attributes view. A table in
 the Triggers view shows the PXI trigger bus segments of your
 chassis.
4. Configure the static route that you want to make.
5. Save the changes.

Note

- Your application already contains too many static routes between the PXI
 trigger buses of your chassis.
- Your hardware route segmentation does not support dynamic signal
 routing.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=creating-static-and-dynamic-routes.html language=enus -->
## TOPIC 00012: Creating Static and Dynamic Signal Routes

- bundle_id: `ni-rfsa`
- source_path: `creating-static-and-dynamic-routes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/creating-static-and-dynamic-routes.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: To establish a dynamic route across segments, you must specify a fully qualified terminal name for the source and destination signal. Launch NI Measurement & Automation Explorer (MAX). Expand Devices and Interfaces, then expand the Chassis tree. If you are using a remote RT target, expand Remote Sys

### Creating Static and Dynamic Signal Routes

To establish a dynamic route across segments, you must specify a fully qualified terminal name for the source and destination signal.

1. Launch NI Measurement & Automation Explorer (MAX).
2. Expand 
 Devices and Interfaces, then expand the 
 Chassis tree. 
 Note If you are using a remote RT target, expand 
 Remote Systems, find and expand your remote RT target, and then expand 
 Devices and Interfaces.
3. Select your chassis. 
 The attributes of your chassis are displayed on the right of the MAX window.
4. Click the 
 Trigger tab below the attributes view. 
 A table in the 
 Triggers view shows the PXI trigger bus segments of your chassis.
5. Configure the static route that you want to make and save the changes. 
 Note You may not be able to establish a dynamic route across segments if your application already contains too many static routes between PXI trigger buses of your chassis or if your hardware route segmentation does not support dynamic signal routing. Refer to your chassis documentation to determine the number of allowed static routes between the PXI trigger buses of your chassis and whether your chassis supports dynamic signal routing.

Parent topic:

Signal Routing

<!--NI_TOPIC bundle=ni-rfsa path=debugging-your-application-using-sfp-session.html language=enus -->
## TOPIC 00013: Debugging Your Application Using SFP Session Access

- bundle_id: `ni-rfsa`
- source_path: `debugging-your-application-using-sfp-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/debugging-your-application-using-sfp-session.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use NI-RFSA Soft Front Panel (SFP) session access to allow the SFP to access a device with an existing open session. Examining the open device session with the SFP can help you debug your code. NI-RFSA does not support NI-TClk when driver session debugging is enabled.

### Debugging Your Application Using SFP Session Access

Note

- [Configuring SFP Session Access](configuring-sfp-session-access.html)
- [Launching the NI-RFSA SFP from LabVIEW](launching-the-ni-rfsa-sfp-from-labview.html)
- [Transitioning to and from SFP Control (Local)](transitioning-to-and-from-sfp-control-local.html)
- [Reproducing SFP Configurations Using the NI-RFSA Driver](reproducing-sfp-configurations-using-the-ni-r.html)

Parent topic:

NI-RFSA Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsa path=digital-edge-trigger.html language=enus -->
## TOPIC 00014: Digital Edge Trigger

- bundle_id: `ni-rfsa`
- source_path: `digital-edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/digital-edge-trigger.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: A digital edge trigger acts on the rising or falling edge of a digital signal. A digital signal has two discrete levels: a high level and a low level. When the signal transitions from high to low or from low to high, a digital edge is created. There are two types of edges: Rising Occurs when the sig

### Digital Edge Trigger

A *digital edge trigger* acts on the rising or falling edge of a digital
 signal.

A digital signal has two discrete levels: a high level and a low level. When the signal
 transitions from high to low or from low to high, a *digital edge* is created.

Rising

Falling

Triggers configured to act on a rising or a falling edge of a digital signal are called
 *edge triggers*. Digital triggering is possible on the RTSI lines, PFI lines, and
 the PXI Star Trigger line.

As the following figure shows, an edge trigger could be configured to occur either at the
 Falling Edge of Signal or Rising Edge of Signal.

Figure 7.

[IMAGE alt='image' src='GUID-924FFFCA-65EE-492E-B8CA-229D4A012FB7-a5.svg']

Parent topic:

NI-RFSA Named Trigger Types

<!--NI_TOPIC bundle=ni-rfsa path=driver-setup-options.html language=enus -->
## TOPIC 00015: Driver Setup Options

- bundle_id: `ni-rfsa`
- source_path: `driver-setup-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/driver-setup-options.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Driver Setup string is used with Initialize With Options to set the initial values for properties that are specific to NI-RFSA. You can use the DriverSetup keyword in the option string input to complete the following tasks: Specify your hardware device or external (non-NI) device Simulate hardwa

### Driver Setup Options

The Driver Setup string is used with Initialize With Options to set the initial values for properties that are specific to NI-RFSA.

You can use the 
 DriverSetup keyword in the option string input to complete the following tasks:

- Specify your hardware device or external (non-NI)
 device
- Simulate hardware that is not present
- Specify an NI-RFSA instrument driver FPGA extensions bitfile
- Enable soft front panel (SFP) session access

#### Driver Setup String Format

The Driver Setup string uses the following format: 
 DriverSetup=Tag:Value.

To set multiple properties, separate tag and value pairs with a semicolon, as shown in the following string: 
 DriverSetup=Tag1:Value1;Tag2:Value2;Tag3:Value3

Parent topic:

Programming Considerations

Related tasks:

- Specifying or Simulating a Device with NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=dynamic-range.html language=enus -->
## TOPIC 00016: Dynamic Range

- bundle_id: `ni-rfsa`
- source_path: `dynamic-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/dynamic-range.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Dynamic range (DR) is the range between the minimum detectable signal, in this case the noise floor, and the -1 dB compression point. This relationship is shown in the following figure. Dynamic range is expressed with the following equation: DR (dB) - P[1 dB](dBm) - Noise Floor (dBm/Hz) Another term

### Dynamic Range

*Dynamic range* (DR) is the range between the minimum detectable signal, in
 this case the *noise floor*, and the -1 dB
 compression point.

This relationship is shown in the following figure.

[IMAGE alt='image' src='GUID-2B76A84D-52B3-4CF5-9EA3-7108CFCC6F76-a5.svg']

Dynamic range is expressed with the following equation:

DR (dB) - P<sub>1 dB</sub>(dBm) - 
 *Noise Floor* (dBm/Hz)

Another term often used to describe the dynamic range is the *spurious free dynamic
 range* (SFDR). In the traditional sense of an amplifier or transmitter, SFDR
 is the level where the power of the *intermodulation distortion* (IMD)
 products are equal to the noise floor. Therefore, the input signals are adjusted such
 that the difference between the desired signals and the noise floor is equal to the
 difference between the desired signals and the spurs. The following figure is a
 graphical representation of the SFDR.

[IMAGE alt='image' src='GUID-4D0E78AB-D150-43D0-B2FE-720FFE1FD42E-a5.svg']

The SFDR can be calculated from the third order intercept (TOI) point and the second order intercept (SOI) point using the following equations:

SFDR<sub>TOI</sub> = 2/3(OIP<sub>3</sub> - 
 *Noise Floor*)

SFDR<sub>SOI</sub> =
 .5(OIP<sub>2</sub> -
 *Noise Floor*)

Using the PXI-5610 RF Signal Upconverter module as a stand-alone unit, maximize the SFDR
 using the same procedure used to maximize the TOI. This procedure minimizes RF
 attenuation.

When using the PXI-5610 in conjunction with an AWG module as a calibrated RF signal
 generator, the SFDR for a two-tone signal is the difference between the desired tones
 and the intermodulation levels. This value can be calculated from the TOI and SOI using
 the following equations:

IMD<sub>TOI</sub> =
 2(OIP<sub>3</sub> -
 P<sub>out</sub>)

IMD<sub>SOI</sub> =
 OIP<sub>2</sub> -
 P<sub>out</sub>

| Output Power (dBm) | Noise Floor (dBm/Hz) | TOI Products (dBc) |
| --- | --- | --- |
| -20 | -140 | -86 |
| -6 | -126 | -86 |
| 5 | -115 | -54 |

Parent topic:

NI-RFSA Noise Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=events.html language=enus -->
## TOPIC 00017: Events

- bundle_id: `ni-rfsa`
- source_path: `events.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/events.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Triggers and clocks are generally considered input signals. Exportable triggers and clocks, such as the Sample Clock, can also be considered output signals. Output signals that do not have a trigger or clock counterpart are called events. Events are generated to signify a device state change, the ar

### Events

Triggers and clocks are generally considered input signals. Exportable triggers and clocks, such as the Sample Clock, can also be considered output signals. Output signals that do not have a trigger or clock counterpart are called 
 *events*. 
 Events are generated to signify a device state change, the arrival of a certain kind of sample, the production of a certain amount of samples, or the passage of time.

#### NI-RFSA Event
 Types

NI-RFSA includes specific events you can use in tandem
 with triggers to coordinate actions across instruments.

Ready for Start

Ready for Advance

Ready for Ref

End of Record Event

Done

<!--NI_TOPIC bundle=ni-rfsa path=examples.html language=enus -->
## TOPIC 00018: NI-RFSA Examples

- bundle_id: `ni-rfsa`
- source_path: `examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/examples.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examples demonstrate the functionality of your device and serve as programming models and building blocks for your own applications. LabVIEW and LabWindows/CVI Examples You can use the NI Example Finder to locate examples within LabVIEW and LabWindows/CVI. In LabVIEW or LabWindows/CVI, select HelpFi

### NI-RFSA Examples

Examples demonstrate the functionality of your device and serve as programming models and building blocks for your own applications.

#### LabVIEW and LabWindows/CVI Examples

You can use the NI Example Finder to locate examples within LabVIEW and LabWindows/CVI. In LabVIEW or LabWindows/CVI, select 
 Help»Find Examples, and navigate to 
 Hardware Input and Output»Modular Instruments.

You can also find the installed examples in the following locations:

- The LabVIEW examples are located in the 
 <LabVIEW>\examples\instr\niRFSA directory, where 
 <LabVIEW> is the LabVIEW directory for the specific LabVIEW version you installed on your system.
- The LabWindows/CVI examples are located in the 
 Program Files\IVI Foundation\IVI\Drivers\niRFSA\Examples\CVI directory.

#### Microsoft .NET Examples

The Microsoft .NET examples are located in the 
 <Public Documents>\National Instruments\\Examples\VS201x directory.

#### C Examples

The C examples are located in the 
 <Public Documents>\National Instruments\\Examples\c directory.

#### Common Examples

RFSA Getting Started IQ

RFSA Getting Started Spectrum

RFSA Power vs Time (Zero-Span)

NI-RFSA

RFSA Pulse Trigger Acquisition

NI-RFSA

RFSA Synchronization (TClk, Shared LO and Reference Clock)

NI-RFSA

NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=exporting-ni-rfsa-sfp-data.html language=enus -->
## TOPIC 00019: Exporting NI-RFSA SFP Data

- bundle_id: `ni-rfsa`
- source_path: `exporting-ni-rfsa-sfp-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/exporting-ni-rfsa-sfp-data.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click the Export button to export trace data from the NI-RFSA SFP. Select whether to export the trace data as a tab-delimited (.txt) or comma-delimited (.csv) file in the Export dialog box.

### Exporting NI-RFSA SFP Data

Click the Export button to export trace data from the NI-RFSA SFP.
 Select whether to export the trace data as a tab-delimited (.txt) or
 comma-delimited (.csv) file in the Export dialog
 box.

Parent topic:

NI-RFSA Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsa path=fund-carrierwave.html language=enus -->
## TOPIC 00020: Carrier Wave

- bundle_id: `ni-rfsa`
- source_path: `fund-carrierwave.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/fund-carrierwave.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The carrier wave is a sinusoidal wave that is modulated by a message signal, m(t), prior to transmission. The message signal modifies the carrier wave amplitude, frequency, or phase. The modulation process may vary these characteristics individually or in combination. The modified carrier signal, al

### Carrier Wave

The 
 *carrier wave* is a sinusoidal wave that is modulated by a 
 *message signal*, m(t), prior to transmission.

The message signal modifies the carrier wave amplitude, frequency, or phase. The modulation process may vary these characteristics individually or in combination. The modified carrier signal, also referred to as the 
 *modulated wave*, is transmitted to a receiver.

The process of 
 *demodulation* recovers a replica of the original message signal from the carrier wave. In advanced communication systems, the carrier may be a moving signal, also known as a 
 *spread spectrum signal*. When the characteristics of the carrier signal are deterministic and known by the receiver, virtually any type of carrier signal can be used.

The nominal frequency of the carrier wave is the 
 *carrier frequency*. The carrier frequency is the center frequency of the spread spectrum signal.

Parent topic:

NI-RFSA RF Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=fund-messagesignal.html language=enus -->
## TOPIC 00021: Message Signal

- bundle_id: `ni-rfsa`
- source_path: `fund-messagesignal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/fund-messagesignal.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The message signal contains the data for transmission. The message signal is used to modulate the carrier wave to create the modulated wave for transmission. The message signal data is recovered from the modulated wave by the process of demodulation. The message signal is often referred to as the ba

### Message Signal

The 
 *message signal* contains the data for transmission.

The message signal is used to modulate the carrier wave to create the modulated wave for transmission. The message signal data is recovered from the modulated wave by the process of demodulation.

The message signal is often referred to as the 
 *baseband signal*.

Parent topic:

NI-RFSA RF Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=gain-compression-point.html language=enus -->
## TOPIC 00022: 1 dB Gain Compression Point

- bundle_id: `ni-rfsa`
- source_path: `gain-compression-point.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/gain-compression-point.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 1 dB gain compression point describes amplifier saturation. An amplifier maintains a constant gain for low-level input signals. However, at higher input levels, the amplifier saturates and its gain decreases. The 1 dB gain compression point (P[1 dB]) indicates the power level that causes the gai

### 1 dB Gain Compression Point

The 1 dB gain compression point describes amplifier saturation.

An amplifier maintains a constant gain for low-level input signals. However, at higher input levels, the amplifier saturates and its gain decreases. The 1 dB gain compression point (P<sub>1 dB</sub>) indicates the power level that causes the gain to drop by 1 dB from its small signal value.

The 1 dB gain compression point is derived from the gain relationship between output power and input power. Output power is plotted against input power in the following figure.

Figure 6.

1 dB

[IMAGE alt='image' src='GUID-D97AFBB3-74C9-4E0C-87BD-8DCD2934DDD5-a5.svg']

The straight line on this graph is an extrapolation of the small signal gain of the unit under test (UUT). The input 1 dB compression point is the input power that causes the UUT gain to drop by 1 dB from this small signal value. In this figure, the gain drop occurs at approximately -12 dBm.

Parent topic:

NI-RFSA Noise Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=getting-started.html language=enus -->
## TOPIC 00023: Getting Started with NI-RFSA

- bundle_id: `ni-rfsa`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/getting-started.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: To get started using your device with NI-RFSA, refer to the documentation for your device, available at ni.com/docs. Refer to your device documentation to complete the following tasks: Install the software and hardware Interconnect multiple modules Configure and associate the hardware in MAX Program

### Getting Started with NI-RFSA

To get started using your device with NI-RFSA, refer to
 the documentation for your device, available at [ni.com/docs](https://www.ni.com/docs).

Refer to your device documentation to complete the following tasks:

- Install the software and hardware
- Interconnect multiple modules
- Configure and associate the hardware in MAX
- Program the hardware
- Generate a signal
- Troubleshoot

Tip

<!--NI_TOPIC bundle=ni-rfsa path=harmonic-distortion.html language=enus -->
## TOPIC 00024: Harmonic Distortion

- bundle_id: `ni-rfsa`
- source_path: `harmonic-distortion.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/harmonic-distortion.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Harmonic distortion is a measure of the amount of power contained in the harmonics of a fundamental signal compared to the power of the fundamental signal. Harmonic distortion is inherent to devices and systems that possess nonlinear characteristics. The more nonlinear the device, the greater its ha

### Harmonic Distortion

*Harmonic distortion* is a measure of the amount of power contained in the harmonics of a fundamental signal compared to the power of the fundamental signal.

Harmonic distortion is inherent to devices and systems that possess nonlinear characteristics. The more nonlinear the device, the greater its harmonic distortion.

Harmonic distortion can be expressed as a power ratio or as a percentage. Use the following formula to express it as a power ratio:

P
 <sub>HD</sub> = P<sub>fund</sub>–P<sub>harm</sub>(dBc)

where

- P 
 HD is the power of the harmonic distortion in dBc
- P 
 fund is the fundamental signal power in dB or dBm
- P 
 harm is the power of the harmonic of interest in dB or dBm

Convert power to voltage and use the following equation to express harmonic distortion as a percentage ratio:

Percentage of Distortion

=

V

h

a

r

m

V

f

u

n

d

×

100

%

Percentage of Distortion

=

V

h

a

r

m

V

f

u

n

d

×

100

%

Parent topic:

NI-RFSA Noise Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=imd3.html language=enus -->
## TOPIC 00025: Two-Tone Third-Order Intermodulation Distortion

- bundle_id: `ni-rfsa`
- source_path: `imd3.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/imd3.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Two-tone third-order intermodulation distortion (IMD[3]) is the measure of third-order distortion products that a nonlinear device produces when it receives two tones that are close in frequency. This distortion product is usually so close to the carrier that it is almost impossible to filter out. S

### Two-Tone Third-Order Intermodulation Distortion

*Two-tone third-order intermodulation distortion*
 (IMD<sub>3</sub>) is the measure of third-order distortion products that
 a nonlinear device produces when it receives two tones that are close in
 frequency.

This distortion product is usually so close to the carrier that it is almost impossible to
 filter out. Such distortion can cause interference in multichannel communications
 equipment.

If F<sub>1</sub> and F<sub>2</sub> are the
 frequencies of the two tones, the third-order distortion products occur on both sides of
 these tones at 2F<sub>2</sub> – F<sub>1</sub> and
 2F<sub>1</sub> – F<sub>2</sub> . Assuming equal
 power levels of the two tones, IMD<sub>3</sub> is the difference between
 the power of the fundamental signals and the third-order products, as defined in the
 following equation:

IMD
 <sub>3</sub> = P<sub>o</sub> – P<sub>o3</sub>

where

- P o3 is the power level of one of the
 output third-order products
- P o is the power level of one of the
 fundamental tones

The math becomes more involved if the powers of the two tones are different.

After you calculate the IMD<sub>3</sub> using the preceding formula, you can calculate the unit under test (UUT) output third-order intercept point (OIP<sub>3</sub>) using the following equation:

O

I

P

3

=

I

M

D

3

2

+

P

o

=

1

2

(

3

P

o

−

P

o

3

)

(

d

B

)

The input third-order intercept point (IIP<sub>3</sub>) is defined as:

IIP
 <sub>3</sub> = (OIP<sub>3</sub> – G)

Where G is the gain of the device. The IIP<sub>3</sub> number quantifies the third-order linearity input referred of a device.

The following figure shows the relationship between the second- and third-order distortions and the linear output of a device.

[IMAGE alt='image' src='GUID-7C79B7A8-2595-4433-9A19-D2D983D39ED9-a5.svg']

The two tones injected into the UUT must be free from any third-order products. These two
 tones are combined, or summed, at or before the UUT input. If the two tones are not well
 isolated, the tones intermodulate with each other and cause distortion. To minimize
 distortion of the input tones, use a signal combiner with good input-to-input isolation.

Parent topic:

NI-RFSA Noise Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=improving-your-measurements.html language=enus -->
## TOPIC 00026: Improving Your Measurements

- bundle_id: `ni-rfsa`
- source_path: `improving-your-measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/improving-your-measurements.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when configuring your measurements to achieve the best results. All Measurement Types Lock your source and analyzer to a common reference. Match your reference accuracy to the most sensitive instrument. When using an external reference, ensure that the accuracy of the re

### Improving Your Measurements

Use the following guidelines when configuring your measurements to achieve the best
 results.

#### All Measurement Types

- Lock your source and analyzer to a common reference.
- Match your reference accuracy to the most sensitive instrument. When using an
 external reference, ensure that the accuracy of the reference is suitable for
 your most sensitive or demanding instrument. Failure to do so can lead to lost
 or incorrect results.
- Set the reference level just above the maximum power level expected in your
 measurement, but not higher. Setting the reference level too low causes
 inaccurate results due to distortion products in the instrument signal chain.
 Setting the reference level too high decreases instrument sensitivity and
 dynamic range.
- Manually adjust the attenuation to an appropriate amount for your measurement.
 An improper attenuation setting can cause measurement errors. Low power signals
 might fall below the automatic attenuation setting, decreasing dynamic
 range.
- Use an appropriate resolution bandwidth (RBW). Using a narrower RBW setting can
 help resolve lower power signals and distinguish signal shapes. However, a
 narrower RBW setting increases measurement times.
- Use averaging when appropriate. Applying averaging to your measurement increases
 measurement repeatability and helps identify signals close to the noise floor.
 However, averaging increases measurement times.

#### Channel Power Measurements

- Set the RBW small enough to precisely define the channel bandwidth, but not
 smaller. Setting the RBW too large relative to the channel bandwidth causes
 power to be improperly applied across channels.
- Use noise correction. The inherent noise of the device can obscure signals that
 are measured near the noise floor. Enable SFP Noise Correction to improve your
 measurement.
- Use the internal preamplifier to increase dynamic range for low power signals.
 To enable the internal preamplifier in the SFP, complete the following steps:
  1. Press the Amptd key.
  2. Navigate to the second page of the softkey menu, and press the
 Internal Preamp softkey.

#### Third-Order Intercept (TOI)
 Measurements

- Calculate the maximum power using the sum of the two signals. In a two-tone
 test, the maximum expected power is cumulative.
- Adjust the attenuation to an appropriate amount. The internal distortion of the
 analyzer can cause measurement inaccuracies if the attenuation is
 insufficient.

Parent topic:

NI-RFSA Soft Front Panel

Related concepts:

- Noise Correction

<!--NI_TOPIC bundle=ni-rfsa path=iq-modulation.html language=enus -->
## TOPIC 00027: I/Q Modulation

- bundle_id: `ni-rfsa`
- source_path: `iq-modulation.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/iq-modulation.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: I/Q is a common way to represent message signals in modern communication systems. There are two fundamental ways (degrees of freedom) to produce a modulated wave from a carrier wave: you can perturb either its amplitude or its phase. I/Q signaling allows you to simultaneously change both amplitude a

### I/Q Modulation

I/Q is a common way to represent message signals in modern communication
 systems.

There are two fundamental ways (degrees of freedom) to produce a modulated wave from a
 carrier wave: you can perturb either its amplitude or its phase. I/Q signaling allows you to
 simultaneously change both amplitude and phase. Using both degrees of freedom when modulating
 a carrier allows greater spectral efficiency with regard to bits per hertz of channel
 bandwidth (for a given bits per second transmission rate) compared to using only one degree of
 freedom.

To simultaneously perturb both the amplitude and phase of a carrier, two canonical forms of
 frequency-translating transmitters use the two degrees of freedom in modulation
 simultaneously. These canonical forms are referred to as *canonical polar
 modulation* and *canonical rectangular modulation*.

Parent topic:

NI-RFSA RF Fundamentals

#### Canonical Polar Modulation

Figure 2.

[IMAGE alt='image' src='GUID-8A3EEB61-4ACA-4AC2-8FF3-C84BE1E116A8-a5.svg']

In polar modulation, the message signal is split into two components.

- R(t) controls the carrier wave amplitude changes
- φ(t) drives the carrier wave phase changes

#### Canonical Rectangular Modulation

Figure 3.

[IMAGE alt='image' src='GUID-3D31EE80-0C9E-478C-88F6-34F61552F53D-a5.svg']

In rectangular modulation, the message signal is split into two components.

- I(t) controls the in-phase carrier wave changes
- Q(t) controls the quadrature-phase carrier wave changes

#### Mathematical Relationship between Canonical Modulation Forms

The modulated outputs of the two canonical forms are mathematically and physically
 equivalent. To show their equality, you can compare and translate between the polar and
 rectangular representations.

Begin with the following equation:

R(t)cos(ω<sub>c</sub>(t)
 + φ(t))

Plug in the following trigonometric identity:

cos(α + β) = cos α cos β - sin α sin β

to yield the following equation:

R(t)[cosω<sub>c</sub>(t)cosφ(t)
 -
 sinω<sub>c</sub>(t)sinφ(t)]

Simplify the preceding equation to arrive at the following relationship:

I(t)cos(ω<sub>c</sub>(t))
 -
 Q(t)sin(ω<sub>c</sub>(t))

where

- I ( t ) =
 R ( t )cos( φ ( t ))
- Q ( t ) =
 R ( t )sin( φ ( t ))
- ω 
 c = 2 π f c
- f 
 c is the carrier frequency in Hz

The rectangular form of modulation, often called *I/Q modulation*, has become
 popular for certain technical reasons.

In the rectangular modulation figure, the real baseband signals of
 I(t) and Q(t)
 are created (in some way) to contain all the information of message input
 m(t).<sup>[[1]](#note-d2268e431)</sup>[<sup>1</sup>](#fnsrc_1-d2268e431) The polar
 R(t) and φ(t)
 also contain the information of m(t). Because the
 carriers cos(ω<sub>c</sub>(t)) and
 sin(ω<sub>c</sub>(t)) are
 orthogonal functions, we use the terminology of *quadrature modulation*, where the
 signal applied to the cosine mixer is called the In-phase component (I),
 and the signal applied to the sine mixer is call the Quadrature-phase component
 (Q). The I and Q designations are
 useful because the I(t) baseband signal is applied to
 the cosine mixer, and the Q(t) baseband signal is
 applied to the sine mixer.

The analytical relationship between the polar form
 (R(t) and φ(t)) of
 the baseband signal and Cartesian form (I(t) and
 Q(t)) of the baseband signal is shown in the following
 figure.

Figure 4.

[IMAGE alt='image' src='GUID-A9F9B68F-8DD5-4AEE-AA5F-1EA04E1EB8B2-a5.svg']

The diagram is a "snapshot in time" of the complex
 (analytical) baseband envelope g(t). The diagram is for
 an arbitrary instant in time, therefore the independent time variable t is
 dropped. The amplitude of Qprojects onto the imaginary
 (j) axis. The amplitude of Iprojects onto the real
 axis.

#### I/Q Receiver

An I/Q receiver recovers a signal containing both amplitude and phase modulation.

For the incoming signal, p(t), the normalized outputs of the cosine and sine mixers are respectively:

I(t) + I(t)cos(2ω<sub>c</sub>t) + Q(t)sin(2ω<sub>c</sub>t)

Q(t) + Q(t)sin(2ω<sub>c</sub>t) + I(t)cos(2ω<sub>c</sub>t)

After the mixers, the lowpass filters remove all the high-frequency 2ω<sub>c</sub>t terms, leaving the recovered I(t) and Q(t) signals.

The diagrams and discussion in this topic are ideal. They imply that the original message signal m(t) is recovered along the transmitter-path-receiver chain. This implication is useful when focusing purely upon the signaling method. In reality, however, the receiver returns a version of m(t) corrupted by noise and distortion impairments.

The vector signal analyzer measures the unit under test (UUT) noise and distortion impairments and determines if the performance of the UUT is sufficient for the desired transmission scheme. Because the I/Q signal representation is relatively straightforward (and also has practical and physical application in communication systems), it is conceptually used to evaluate the noise and distortion performance of these communication systems.

[<sup>1</sup>](#note_ref-d2268e431) The polar
 R(t) and φ(t)
 also contain the information of m(t).

<!--NI_TOPIC bundle=ni-rfsa path=iq-power-edge-trigger.html language=enus -->
## TOPIC 00028: I/Q Power Edge Trigger

- bundle_id: `ni-rfsa`
- source_path: `iq-power-edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/iq-power-edge-trigger.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `reference`
- source_description: After data has been downconverted and decimated, NI-RFSA calculates the instantaneous power of the I/Q data (I^2 + Q^2) in the digital downconverter and uses this value as a source for the Reference Trigger for the IF digitizer. As shown in the figure, an I/Q power edge trigger can be configured to

### I/Q Power Edge Trigger

After data has been downconverted and decimated, NI-RFSA calculates the instantaneous power of the I/Q data (I<sup>2</sup> + Q<sup>2</sup>) in the digital
 downconverter and uses this value as a source for the Reference Trigger for the IF
 digitizer.

As shown in the figure, an I/Q power edge trigger can be configured to occur either at the
 positive slope or the negative slope.

Figure 8.

[IMAGE alt='image' src='GUID-1AFDCE1D-7ABD-4FF9-B751-0177CD01CEA7-a5.svg']

Only Reference triggers may be configured to trigger based on the I/Q
 power edge.

Parent topic:

NI-RFSA Named Trigger Types

<!--NI_TOPIC bundle=ni-rfsa path=launching-the-ni-rfsa-sfp-from-labview.html language=enus -->
## TOPIC 00029: Launching the NI-RFSA SFP from LabVIEW

- bundle_id: `ni-rfsa`
- source_path: `launching-the-ni-rfsa-sfp-from-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/launching-the-ni-rfsa-sfp-from-labview.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using NI-RFSA Soft Front Panel (SFP) session access, you can automatically launch the SFP from a LabVIEW probe. Using the SFP can help you verify proper configuration of your hardware. Additionally, you can modify your hardware configuration from the SFP. When you launch the SFP from a probe, SFP se

### Launching the NI-RFSA SFP from LabVIEW

Using NI-RFSA Soft Front Panel (SFP) session access, you can automatically launch the SFP
 from a LabVIEW probe. Using the SFP can help you verify proper configuration of your
 hardware. Additionally, you can modify your hardware configuration from the SFP. When
 you launch the SFP from a probe, SFP session access is automatically enabled.

1. In your block diagram, probe the device instrument handle by right-clicking a valid
 NI-RFSA session reference wire and selecting Probe .
2. In the Probe Watch Window , place a checkmark in the
 Launch Soft Front Panel (Pause VI Execution) 
 checkbox.

The following figure shows the Probe Watch Window.

[IMAGE alt='image' src='GUID-EFA2A628-642E-4814-A14F-A2CF04415723-a5.gif']

When your program data reaches the probe, code execution pauses and the SFP launches.

#### Related Information

Transitioning to and from SFP Control (Local)

Parent topic:

Debugging Your Application Using SFP Session Access

Related concepts:

- Transitioning to and from SFP Control (Local)

<!--NI_TOPIC bundle=ni-rfsa path=locating-an-ni-rfsa-device.html language=enus -->
## TOPIC 00030: Locating an NI-RFSA Device

- bundle_id: `ni-rfsa`
- source_path: `locating-an-ni-rfsa-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/locating-an-ni-rfsa-device.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: To locate your NI-RFSA device in MAX, complete the following steps: In the configuration tree, double-click Device and Interfaces to see a list of installed devices. Installed devices appear under the name of their associated chassis. If you are using your NI-RFSA device with the LabVIEW Real-Time M

### Locating an NI-RFSA Device

To locate your NI-RFSA device in MAX, complete the following steps:

1. In the configuration tree, double-click Device and Interfaces 
 to see a list of installed devices. Installed devices appear under the name of their
 associated chassis. Note 
 If you are using your NI-RFSA device with the LabVIEW Real-Time Module, expand
 Remote Systems. Find your target IP address or name,
 expand it, and then expand Devices and
 Interfaces.
2. Expand your chassis tree item. MAX lists all devices installed in the chassis. Your
 default device names may vary.
3. Record the device identifier MAX assigns to the hardware. Use this identifier when
 programming your NI-RFSA device. For hardware systems, record the device identifier
 for the downconverter module. Tip Instead of using the default naming convention, you may find it
 convenient to rename your devices in MAX.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=manage-errors-warnings-net.html language=enus -->
## TOPIC 00031: Errors and Warnings in the NI-RFSA .NET Class Library

- bundle_id: `ni-rfsa`
- source_path: `manage-errors-warnings-net.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/manage-errors-warnings-net.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-RFSA .NET Class Library manages errors and warnings by converting error codes into exceptions and warning codes into events. Subscribe to the Warning event to handle warnings effectively, ensuring you capture all potential warnings. The NI-RFSA driver reports errors or warnings through the me

### Errors and Warnings in the NI-RFSA .NET Class Library

The NI-RFSA .NET Class Library manages errors and
 warnings by converting error codes into exceptions and warning codes into events. Subscribe
 to the Warning event to handle warnings effectively, ensuring you capture all potential
 warnings.

The NI-RFSA driver reports errors or warnings through the
 method return values. Negative return values indicate errors and positive values
 indicate warnings.

The NI-RFSA .NET class library converts the error codes into
 exceptions. All exceptions are either .NET defined or IVI defined; none of them are
 custom exceptions. The exception message for driver errors includes the driver error
 code at the end.

#### Subscribe to Warning Events

The NI-RFSA .NET class library converts the warning
 codes into events. To receive warnings, you must subscribe to the Warning event as
 follows:

```text
VB.NET

session.DriverOperation.Warning += New EventHandler(Of RfsaWarningEventArgs)(DriverOperation_Warning)

Private Sub DriverOperation_Warning(ByVal sender As Object, ByVal e As RfsaWarningEventArgs)
'User code goes here
End Sub
```

```text
Visual C#

session.DriverOperation.Warning += new EventHandler<RfsaWarningEventArgs>(DriverOperation_Warning);

void DriverOperation_Warning(object sender, RfsaWarningEventArgs e)
{
//User code goes here
}
```

Note

NIRfsa

The RfsaWarningEventArgs class contains a read-only property to
 get the RfsaWarning object out. For ease-of-use, it also gives
 direct access to the warning’s Code and
 Message.

RfsaWarning is an immutable class and hence its
 Equals method and the == operator are
 overloaded to compare values and not references.

The driver dynamically generates the warning message for a particular warning code,
 so it's possible for a warning with same code to have different messages. The
 default behavior of the Equals method checks the value equality
 of both the Code and the Message. However,
 there is an overload of the Equals method that lets you ignore
 the Message when comparing two warnings.

Parent topic:

Using the NI-RFSA .NET Class Library

<!--NI_TOPIC bundle=ni-rfsa path=max-help-for-ni-rfsa-devices.html language=enus -->
## TOPIC 00032: Using Measurement & Automation Explorer for NI-RFSA

- bundle_id: `ni-rfsa`
- source_path: `max-help-for-ni-rfsa-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/max-help-for-ni-rfsa-devices.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to complete the most common NI-RFSA tasks in Measurement & Automation Explorer (MAX).

### Using Measurement & Automation
 Explorer for NI-RFSA

Learn how to complete the most common NI-RFSA tasks in Measurement & Automation
 Explorer (MAX).

- [Locating an NI-RFSA Device](locating-an-ni-rfsa-device.html)
- [Simulating an NI-RFSA Device in MAX](simulating-an-ni-rfsa-device.html) Simulate an NI-RFSA device using Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware.
- [Removing a Simulated NI-RFSA Device](removing-a-simulated-ni-rfsa-device.html)
- [Associating NI-RFSA Modules](associating-ni-rfsa-modules.html) To control multiple hardware modules as a single RF device, you must first associate the modules.
- [Renaming an NI-RFSA Device](renaming-an-ni-rfsa-device.html)
- [Running a Self-Test on an NI-RFSA Device](running-a-self-test-on-an-ni-rfsa-device.html)
- [Using the NI-RFSA Soft Front Panel](using-the-ni-rfsa-soft-front-panel.html)
- [Creating Dynamic and Static Signal Routes for an NI-RFSA Device](creating-dynamic-and-static-signal-routes-for.html) To establish a dynamic route across segments, you must specify a fully qualified terminal name for the source and the destination signal.
- [Synchronizing NI-RFSA Devices](synchronizing-ni-rfsa-devices.html)
- [A Device Does Not Appear in MAX](a-device-does-not-appear-in-max.html)

<!--NI_TOPIC bundle=ni-rfsa path=modulation.html language=enus -->
## TOPIC 00033: Modulation

- bundle_id: `ni-rfsa`
- source_path: `modulation.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/modulation.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modulation is a process that alters the characteristics of a carrier wave according to information in the message signal, m(t), to generate and transmit a modulated wave. There are several types of modulation. The unmodulated carrier is represented by the following equation: v(t) = A[c]cos(2πf[c]t +

### Modulation

Modulation is a process that alters the characteristics of a carrier wave according to information in the message signal, m(t), to generate and transmit a modulated wave.

There are several types of modulation.

The unmodulated carrier is represented by the following equation: v(t) = A<sub>c</sub>cos(2πf<sub>c</sub>t + φ)

The amplitude-modulated carrier signal is represented by the following equation: v(t) = (m(t) + A<sub>c</sub>)cos(2πf<sub>c</sub>t + φ)

The frequency-modulated carrier signal is represented by the following equation: v(t) = A<sub>c</sub>cos(2πf<sub>c</sub>t + φ + ∫ m(t)dt)

The phase-modulated carrier signal is represented by the following equation: v(t) = A<sub>c</sub>cos(2πf<sub>c</sub>t + φ + m(t))

where

- m ( t ) is the time varying message signal
- A 
 c is the amplitude of the carrier wave
- f 
 c is the frequency of the carrier wave

Parent topic:

NI-RFSA RF Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=net-values-for-properties.html language=enus -->
## TOPIC 00034: Using Predefined or Custom Values for Source or Output Terminal Properties

- bundle_id: `ni-rfsa`
- source_path: `net-values-for-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/net-values-for-properties.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to use predefined values or custom values for source properties or output terminal properties in the NI-RFSA .NET API. How Do I Pass a Predefined Value to an NI-RFSA Property? There are certain properties, such as trigger sources, clock sources, and output terminals, that work with a set o

### Using Predefined or Custom Values for Source
 or Output Terminal Properties

Learn how to use predefined values or custom values for source properties or output
 terminal properties in the NI-RFSA .NET API.

#### How Do I Pass a Predefined Value to an NI-RFSA
 Property?

There are certain properties, such as trigger sources, clock sources, and output
 terminals, that work with a set of predefined string values, but might also accept
 custom values. For this you can use the utility classes that are part of NI-RFSA .NET API. For example, the
 Source property in
 RfsaDigitalEdgeStartTrigger specifies an
 RfsaDigitalEdgeStartTriggerSource object. You can configure
 Source using one of the predefined values, such as:

```text
VB.NET

session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = RfsaDigitalEdgeReferenceTriggerSource.Pfi0
```

```text
Visual C#

session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = RfsaDigitalEdgeReferenceTriggerSource.Pfi0;
```

You can also create a custom value with the static FromString
 method:

```text
VB.NET

session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = RfsaDigitalEdgeReferenceTriggerSource.FromString("CustomSource")
```

```text
Visual C#

session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = RfsaDigitalEdgeReferenceTriggerSource.FromString("CustomSource");
```

You can also directly set the source as a string instead of using the
 FromString method:

```text
VB.NET

session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = "CustomSource"
```

```text
Visual C#

session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = "CustomSource";
```

#### How Do I Get the Underlying String from Source or Output Terminal Value?

You can use the ToString method to retrieve the underlying source
 values. The following code shows how to retrieve the source name:

```text
VB.NET

Dim triggerSource As String = RfsaDigitalEdgeReferenceTriggerSource.Pfi0.ToString()
```

```text
Visual C#

string triggerSource = RfsaDigitalEdgeReferenceTriggerSource.Pfi0.ToString();
```

You can use the underlying string value if you want to assign a source or output
 terminal to some other source or output terminal.

```text
VB.NET

session.Configuration.Events.ReadyForReferenceEvent.OutputTerminal = RfsaReadyForReferenceEventExportedOutputTerminal.Pfi0
session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = session.Configuration.Events.ReadyForReferenceEvent.OutputTerminal.ToString()
```

```text
Visual C#

session.Configuration.Events.ReadyForReferenceEvent.OutputTerminal = RfsaReadyForReferenceEventExportedOutputTerminal.Pfi0;
session.Configuration.Triggers.ReferenceTrigger.DigitalEdge.Source = session.Configuration.Events.ReadyForReferenceEvent.OutputTerminal.ToString();
```

Parent topic:

Using the NI-RFSA .NET Class Library

<!--NI_TOPIC bundle=ni-rfsa path=new-features-and-changes.html language=enus -->
## TOPIC 00035: NI-RFSA New Features and Changes

- bundle_id: `ni-rfsa`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/new-features-and-changes.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of NI-RFSA. Discover what is new in the latest releases of NI-RFSA.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include

### NI-RFSA
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of NI-RFSA.

NI-RFSA

Note

Release Notes

Related information:

- Software and Driver Downloads

#### NI-RFSA
 2026 Q2 Changes

Learn about new features, behavior changes, and other updates in NI-RFSA 2026 Q2.

This version of NI-RFSA provides support for the
 following features:

- Support for NI RMM-5544
- Support for saving and loading configurations from a file
- Support for 1-channel variant of PXIe-5860

#### NI-RFSA
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in NI-RFSA 2026 Q1.

This version of NI-RFSA provides support for the
 following features:

- Support for List Mode for PXIe-5860 VST with PXIe-5633 VNA.

#### NI-RFSA
 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in NI-RFSA 2025 Q4.

This version of NI-RFSA provides support for the
 following features:

- Support for PXIe-5842 VST with 54 GHz Frequency Extension (RMM-5586).
- Improved trigger/event to data alignment for PXIe-5860.

#### NI-RFSA
 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in NI-RFSA 2025 Q3.

This version of NI-RFSA provides support for the
 following features:

- Support for SystemLink Asset Utilization.
- Support for PXIe-5842 VST with 54 GHz Frequency Extension (RMM-5585).
- Support for PXIe-5563 RF Port Switch.

#### NI-RFSA
 2025 Q2 Changes

Learn about new features, behavior changes, and other updates in NI-RFSA 2025 Q2.

This version of NI-RFSA provides support for the
 following features:

- Support for PXIe-5860 VST with PXIe-5633 VNA.

#### NI-RFSA
 2025 Q1 Changes

Learn about new features, behavior changes, and other updates in NI-RFSA 2025 Q1.

This version of NI-RFSA provides support for the
 following features:

- Support for 4 GHz Bandwidth variant of PXIe-5842 VST.

#### NI-RFSA 2024 Q4 New Features and
 Changes

##### Behavior Changes

- Uninstalling the RFSA software also removes any previous versions of RFSA .NET runtimes that were leaked in .NET Global Assembly
 Cache directory.

#### NI-RFSA 2024 Q3 New Features and
 Changes

- Support for PXIe-5860 VST

#### NI-RFSA 2024 Q1 New Features and
 Changes

- Support for Subspan Overlap in PXIe-5842
- Support for an enhanced functionality which now allows the utilization of
 DIO or PFIN as triggers and events for
 PXIe-5841 and PXIe-5842

#### NI-RFSA 2023 Q4 New Features and
 Changes

- Support for PXIe-5842 VST with PXIe-5633 VNA

<!--NI_TOPIC bundle=ni-rfsa path=ni-frsa-rd-fundamentals.html language=enus -->
## TOPIC 00036: NI-RFSA RF Fundamentals

- bundle_id: `ni-rfsa`
- source_path: `ni-frsa-rd-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/ni-frsa-rd-fundamentals.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Radio Frequency (RF) communication enables the transmission and reception of information over the air.

### NI-RFSA RF
 Fundamentals

Radio Frequency (RF) communication enables the transmission and reception of information
 over the air.

- [Carrier Wave](fund-carrierwave.html) The carrier wave is a sinusoidal wave that is modulated by a message signal , m(t) , prior to transmission.
- [Message Signal](fund-messagesignal.html) The message signal contains the data for transmission.
- [Modulation](modulation.html) Modulation is a process that alters the characteristics of a carrier wave according to information in the message signal, m ( t ), to generate and transmit a modulated wave.
- [I/Q Modulation](iq-modulation.html#GUID-08787418-57B3-471F-9B22-E8C8033F7378) I/Q is a common way to represent message signals in modern communication systems.

<!--NI_TOPIC bundle=ni-rfsa path=ni-rfsa-noise-fundamentals.html language=enus -->
## TOPIC 00037: NI-RFSA Noise Fundamentals

- bundle_id: `ni-rfsa`
- source_path: `ni-rfsa-noise-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/ni-rfsa-noise-fundamentals.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise is an unavoidable in RF communication that affects signal integrity and system performance. Understanding the different types and sources of noise is essential for designing and evaluating communication systems.

### NI-RFSA Noise
 Fundamentals

Noise is an unavoidable in RF communication that affects signal integrity and system
 performance. Understanding the different types and sources of noise is essential for
 designing and evaluating communication systems.

- [Noise Figure](noise-figure.html) The noise figure of a UUT is the ratio, in dB, of its noise power to the noise power that a matched resistive load would deliver at room temperature.
- [Noise Floor](noise-floor.html) Noise floor is the measure of the noise density, in dBm/Hz, or the noise power in a 1 Hz bandwidth.
- [Harmonic Distortion](harmonic-distortion.html) Harmonic distortion is a measure of the amount of power contained in the harmonics of a fundamental signal compared to the power of the fundamental signal.
- [Total Harmonic Distortion](total-harmonic-distortion.html) Total harmonic distortion (THD) is a representation of the effect that multiple harmonic spurs throughout a spectrum band have on the fundamental tone.
- [Two-Tone Third-Order Intermodulation Distortion](imd3.html) Two-tone third-order intermodulation distortion ( IMD 3 ) is the measure of third-order distortion products that a nonlinear device produces when it receives two tones that are close in frequency.
- [1 dB Gain Compression Point](gain-compression-point.html) The 1 dB gain compression point describes amplifier saturation.
- [Dynamic Range](dynamic-range.html) Dynamic range (DR) is the range between the minimum detectable signal, in this case the noise floor , and the -1 dB compression point.

<!--NI_TOPIC bundle=ni-rfsa path=ni-rfsa-sfp-environment.html language=enus -->
## TOPIC 00038: NI-RFSA SFP Environment

- bundle_id: `ni-rfsa`
- source_path: `ni-rfsa-sfp-environment.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/ni-rfsa-sfp-environment.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-RFSA Soft Front Panel (SFP) is a PC-based interface for RF signal analysis, offering enhanced processing, storage, and display. Similar to stand-alone RF signal analyzers, the NI-RFSA SFP controls the RF device, and analyzes and presents data. However, because the SFP operates on the PC, it p

### NI-RFSA SFP Environment

The NI-RFSA Soft Front Panel (SFP) is a PC-based interface for RF signal analysis,
 offering enhanced processing, storage, and display.

Similar to stand-alone RF signal analyzers, the NI-RFSA SFP controls the RF device, and
 analyzes and presents data. However, because the SFP operates on the PC, it provides
 additional processing, storage, and display capabilities. You can open multiple
 instances of the SFP to interact with more than one device. Each instance of the SFP
 opens as a separate application window.

You can access the NI-RFSA SFP at Start»All Programs»National
 Instruments»NI-RFSA»NI-RFSA Soft Front Panel. The SFP launches at the
 minimum application window size. To resize the application window, click the Maximize
 button in the upper right corner of the window or click and drag a corner of the window.

The following figure illustrates the elements of the NI-RFSA SFP environment.

Figure 1.

[IMAGE alt='image' src='GUID-5EF3583E-5BB7-461D-8188-C513C04D469D-a5.gif']

1. Use the NI-RFSA SFP Menu s to perform the following actions:
  - Use the File menu for the following
    - Open new instances of the NI-RFSA SFP.
    - Print the Display Window .
    - Save and recall configuration files.
    - Export trace data.
    - Exit the NI-RFSA SFP.
  - Use the Edit menu to set acquisition and display
 options.
  - Use the Device menu to open and close a device
 session.
  - Use the Help menu to access information about the
 SFP, help for the SFP, and device-specific help.
2. The Display Window provides a graphical representation of the
 current acquisition and information about the current SFP configuration. The data
 entry field appears when you click instrument control buttons for which you can
 specify instrument settings. Note The current device might coerce some parameter values to a value
 that the current device supports. The Device Configuration and Measurements
 Display Area displays actual (coerced) values. While the data entry field and
 softkey continue to display the desired value.
3. Use the Instrument Control Buttons to select softkey menus.
 In the softkey menus, you can configure measurements and specify device, system, and
 display options. You can also use instrument control buttons to print the current
 Display Window, export trace data, and save and recall measurement configurations.
 Use the instrument control buttons as you would the buttons on stand-alone RF signal
 analyzers.
4. Use the Softkey Menu to configure measurements and specify
 device, system, and display settings. The softkey menu is dynamic and changes
 according to the selected instrument control button. The
 >> symbol on a softkey indicates additional options
 are available by clicking that softkey. Click the Return 
 softkey to return to the previous softkey menu. Use the < 
 and the > softkeys below the Return 
 softkey to view additional softkeys related to the current softkey menu.
5. Use the Keypad and Knob to enter values for device settings
 as you would on stand-alone RF signal analyzers. You can use your computer keyboard
 to enter values for device settings. You can use the mouse scroll wheel to move the
 knob.
6. The pane below the Display Window is the Device Configuration and
 Measurements Display Area . The Device Configuration and
 Measurements Display Area shows the following:
  - Configuration settings of the current device session
  - Parameters of the current measurement
  - Measurement results and marker results
7. The Status Bar displays status, warning, and error
 information about the current device session. Click the Clear 
 button to clear warnings from the status bar. The SFP automatically clears resolved
 errors from the status bar.

Parent topic:

NI-RFSA Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsa path=ni-rfsa-soft-front-panel-help.html language=enus -->
## TOPIC 00039: NI-RFSA Soft Front Panel

- bundle_id: `ni-rfsa`
- source_path: `ni-rfsa-soft-front-panel-help.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/ni-rfsa-soft-front-panel-help.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI-RFSA Soft Front Panel (SFP) to interactively control your NI RF vector signal analyzer. The NI-RFSA SFP uses the NI-RFSA driver software for LabVIEW to perform standard, built-in RF signal analyzer operations. This help file includes information about the SFP environment and details about

### NI-RFSA Soft Front Panel

Use the NI-RFSA Soft Front Panel (SFP) to interactively control your NI RF vector
 signal analyzer.

Tip

To learn about using the NI-RFSA SFP, launch the SFP and select Help»Show
 Context Help or press <Ctrl-H>. In the context
 help window, move the cursor over an item to display additional help.

Related concepts:

- NI-RFSA SFP Environment
- Performing Measurements in the NI-RFSA SFP
- Programming Considerations

<!--NI_TOPIC bundle=ni-rfsa path=ni-rfsa-triggers-vst.html language=enus -->
## TOPIC 00040: NI-RFSA Named Trigger Types

- bundle_id: `ni-rfsa`
- source_path: `ni-rfsa-triggers-vst.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/ni-rfsa-triggers-vst.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Named trigger types in NI-RFSA define the action you want an instrument to take upon detecting a specific signal condition. Start Transitions an instrument into a state where the instrument can respond to Sample Clocks. This trigger transitions the instrument from a nonsampling state into a sampling

### NI-RFSA Named
 Trigger Types

Named trigger types in NI-RFSA define the action you
 want an instrument to take upon detecting a specific signal condition.

Start

Supported
 signal conditions: None, Digital Edge, Software

Reference

Supported signal
 conditions: None, Digital Edge, IQ Power Edge, Software

Advance

Supported signal conditions: None, Digital Edge, Software

- [None](no-trigger.html) Signal acquisition starts immediately upon execution of the NI-RFSA Initiate function; no Start or Script trigger is necessary. This configuration is the default for instruments programmed with NI-RFSA .
- [Digital Edge Trigger](digital-edge-trigger.html) A digital edge trigger acts on the rising or falling edge of a digital signal.
- [I/Q Power Edge Trigger](iq-power-edge-trigger.html) After data has been downconverted and decimated, NI-RFSA calculates the instantaneous power of the I/Q data ( I<sup>2</sup> + Q<sup>2</sup> ) in the digital downconverter and uses this value as a source for the Reference Trigger for the IF digitizer.
- [Software Trigger](software-edge-trigger.html) A software trigger is generated internally by a programmatic call to the NI-RFSA Send Software Edge Trigger function and can occur at any time, based upon the conditions specified in the program.

<!--NI_TOPIC bundle=ni-rfsa path=nirfsa-simulated-devices.html language=enus -->
## TOPIC 00041: NI-RFSA Simulated Devices

- bundle_id: `ni-rfsa`
- source_path: `nirfsa-simulated-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/nirfsa-simulated-devices.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can simulate NI-RFSA device using NI-RFSA or Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage. Additionally, you can use a simulated NI-RFSA device to ev

### NI-RFSA Simulated Devices

You can simulate NI-RFSA device using NI-RFSA or Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware.

Using a simulated device to test an application eliminates the risk of hardware damage. Additionally, you can use a simulated NI-RFSA device to evaluate an NI product for which you do not have hardware.

Note

PXIe-5624

NI-RFSA

PXIe-5668

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsa path=no-trigger.html language=enus -->
## TOPIC 00042: None

- bundle_id: `ni-rfsa`
- source_path: `no-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/no-trigger.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `reference`
- source_description: Signal acquisition starts immediately upon execution of the NI-RFSA Initiate function; no Start or Script trigger is necessary. This configuration is the default for instruments programmed with NI-RFSA.

### None

Signal acquisition starts immediately upon execution of the NI-RFSA
 Initiate function; no Start or Script trigger is necessary. This
 configuration is the default for instruments programmed with NI-RFSA.

Parent topic:

NI-RFSA Named Trigger Types

<!--NI_TOPIC bundle=ni-rfsa path=noise-correction.html language=enus -->
## TOPIC 00043: Noise Correction

- bundle_id: `ni-rfsa`
- source_path: `noise-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/noise-correction.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The inherent noise of the RF signal analyzers affects signals measured near the noise floor. To reduce the noise components, enable noise correction in the SFP to calculate and subtract the average noise from a measured signal. When you enable noise correction, the SFP performs the following steps t

### Noise Correction

The inherent noise of the RF signal analyzers affects signals measured near the noise
 floor. To reduce the noise components, enable noise correction in the SFP to calculate
 and subtract the average noise from a measured signal. When you enable noise correction,
 the SFP performs the following steps to reduce the noise.

1. Enables input isolation to disconnect the input signal.
2. Measures the noise floor by averaging the spectrum data acquired with the input
 disconnected.
3. Disables input isolation to the reconnected input signal.
4. Performs the ACP measurement, subtracting the stored noise floor measurement.
5. Returns the final compensated measurement results.

Once enabled, the SFP calculates the noise and stores it internally. On subsequent runs,
 it uses the same value for noise unless the configuration changes. For example, if noise
 correction is enabled and a device setting, such as RBW, changes, the SFP automatically
 recalculates the noise.

Parent topic:

NI-RFSA Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsa path=noise-figure.html language=enus -->
## TOPIC 00044: Noise Figure

- bundle_id: `ni-rfsa`
- source_path: `noise-figure.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/noise-figure.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: All devices have inherent noise. When a noise is quantified, it is usually referred to the device input. In other words, all the noise power a unit under test (UUT) inherits is assumed to come from its input. The noise figure of a UUT is the ratio, in dB, of its noise power to the noise power that a

### Noise Figure

All devices have inherent noise. When a noise is quantified, it is usually referred to the device input. In other words, all the noise power a unit under test (UUT) inherits is assumed to come from its input. 
 The noise figure of a UUT is the ratio, in dB, of its noise power to the noise power that a matched resistive load would deliver at room temperature.

If you terminate a UUT input with a matched resistive load (typically 50 Ω) and measure the noise power density, in watts/Hz, at its output (N<sub>0</sub>), the noise figure (NF) is given by the following equation:

N

F

=

10

log

⁡

(

N

0

/

G

k

T

)

N

F

=

10

log

⁡

(

N

0

/

G

k

T

)

where

- G is the power gain (in linear units) of the UUT
- k is Boltzmann's constant (≈ 1.38 ×10 -23 J/K)
- T is the ambient temperature (≈ 290° K )

If you use the vector signal analyzer to measure the output noise of a UUT, the resulting
 measurement contains both UUT noise and noise intrinsic to the vector signal analyzer. If
 the UUT gain (G<sub>UUT</sub> in dB) is known, compute
 the noise figure of the UUT with the following equation:

N

F

=

10

log

[

N

m

−

N

r

f

s

a

k

T

+

1

]

−

G

U

U

T

N

F

=

10

log

[

N

m

−

N

r

f

s

a

k

T

+

1

]

−

G

U

U

T

where

- N 
 rfsa is the noise, in watts/Hz, measured by the vector signal analyzer when its input is
 terminated with a matched resistive load
- N 
 m is the measured noise, in watts/Hz, with the UUT attached
- G is the linear power gain
- NF is expressed in dB

Parent topic:

NI-RFSA Noise Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=noise-floor.html language=enus -->
## TOPIC 00045: Noise Floor

- bundle_id: `ni-rfsa`
- source_path: `noise-floor.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/noise-floor.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Noise floor is the measure of the noise density, in dBm/Hz, or the noise power in a 1 Hz bandwidth. Noise can be classified into several types, including the following: Shot noise Thermal noise Flicker noise Burst noise Quantization noise Avalanche noise The noise due to a matched resistive load (N[

### Noise Floor

*Noise floor* is the measure of the noise density, in dBm/Hz, or the noise power in a 1 Hz bandwidth.

Noise can be classified into several types, including the following:

- Shot noise
- Thermal noise
- Flicker noise
- Burst noise
- Quantization noise
- Avalanche noise

The noise due to a matched resistive load (N<sub>i</sub>) can be expressed as the following relation:

(N<sub>i</sub>) = kTB watts

where

- k is Boltzmann's Constant ( k = 1.38 x 10 -23 J / K
- T is the resistor temperature in Kelvin
- B is the bandwidth in Hz

If B is set to 1 Hz, then
 N<sub>i</sub> is equal to the output noise density in watts/Hz. For the
 system shown in the following figure, the output noise floor
 (N<sub>O</sub>) is the combination of the input noise multiplied by the
 gain or loss of the system plus the internal noise of the system
 (N<sub>n</sub>).

[IMAGE alt='image' src='GUID-B1E1CF4A-E259-4680-8274-3C6B48C31463-a5.svg']

The internal noise of a system is therefore represented by the following equation:

N
 <sub>n</sub> = N<sub>i</sub>G – N<sub>O</sub>

Parent topic:

NI-RFSA Noise Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=overview.html language=enus -->
## TOPIC 00046: NI-RFSA Overview

- bundle_id: `ni-rfsa`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/overview.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSA is a driver software you use to control and configure your NI PXI vector signal analyzer (VSA) and NI PXI vector signal transceiver (VST) devices. NI-RFSA provides the standard IVI-based functionality needed for most VSA and VST applications. You can use the NI-RFSA operations and properties

### NI-RFSA
 Overview

NI-RFSA is a driver software you use to control and
 configure your NI PXI vector signal analyzer (VSA) and NI PXI vector signal transceiver
 (VST) devices. NI-RFSA provides the standard IVI-based
 functionality needed for most VSA and VST applications. You can use the NI-RFSA operations and properties to create custom
 measurements or applications that require I/Q data.

<!--NI_TOPIC bundle=ni-rfsa path=performing-measurements-in-the-ni-rfsa-sfp.html language=enus -->
## TOPIC 00047: Performing Measurements in the NI-RFSA SFP

- bundle_id: `ni-rfsa`
- source_path: `performing-measurements-in-the-ni-rfsa-sfp.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/performing-measurements-in-the-ni-rfsa-sfp.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Common Measurements You can use the NI-RFSA Soft Front Panel (SFP) to perform the following common measurements: Adjacent channel power (ACP) Channel Power Complementary cumulative distribution functions (CCDF) Occupied bandwidth (OBW) Spectral emission mask Third-order intercept (TOI) Transmit powe

### Performing Measurements in the NI-RFSA SFP

#### Common Measurements

You can use the NI-RFSA Soft Front Panel (SFP) to perform the following common
 measurements:

- Adjacent channel power (ACP)
- Channel Power
- Complementary cumulative distribution functions (CCDF)
- Occupied bandwidth (OBW)
- Spectral emission mask
- Third-order intercept (TOI)
- Transmit power

#### Performing Measurements

For each measurement type, complete the following steps to perform the measurement in
 the NI-RFSA SFP.

Note

1. Open the NI-RFSA SFP by selecting Start»All Program Files»National
 Instruments»NI-RFSA»NI-RFSA Soft Front Panel .
2. If you have more than one device configured in MAX, select the device you want
 from the Select Device dialog box. If you have only one
 device configured, the SFP automatically opens a session for that device. Tip You can run multiple instances of the SFP if you have multiple
 devices installed in your chassis. Select
 File»New Window to open
 another instance of the SFP.
3. Click the Meas button to display the
 Measure softkey menu.
4. Click the softkey corresponding to the measurement you want to perform. The
 softkey menu displays options specific to the measurement you selected.
5. Adjust the parameters of the measurement using the softkeys. For specific
 information about the parameters controlled by each softkey, press
 Ctrl + H to display the SFP context help.

Refer to Improving Your Measurements for a list of guidelines for achieving the best
 measurement results.

Parent topic:

NI-RFSA Soft Front Panel

Related concepts:

- Improving Your Measurements

<!--NI_TOPIC bundle=ni-rfsa path=printing-the-ni-rfsa-sfp-display-window.html language=enus -->
## TOPIC 00048: Printing the NI-RFSA SFP Display Window

- bundle_id: `ni-rfsa`
- source_path: `printing-the-ni-rfsa-sfp-display-window.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/printing-the-ni-rfsa-sfp-display-window.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click the Print button to send the current view of the NI-RFSA SFP Display Window and the Device Configuration and Measurements Display Area to a printer or clipboard. Select from one of the following print or copy options. Select File»Page Setup to specify page and printer settings prior to printin

### Printing the NI-RFSA SFP Display Window

Click the Print button to send the current view of the NI-RFSA SFP
 Display Window and the Device Configuration and Measurements Display Area to a printer
 or clipboard. Select from one of the following print or copy options. Select
 File»Page Setup to specify page and
 printer settings prior to printing.

- Print (White Background) —Sends the current view of the
 Display Window and the Device Configuration and Measurements Display Area to the
 printer. This selection inverts the colors of the display to print the current view
 on a white background.
- Print (Black Background) —Sends the current view of the
 Display Window and the Device Configuration and Measurements Display Area to the
 printer.
- Copy to Clipboard (White Background) —Sends the current view
 of the Display Window and the Device Configuration and Measurements Display Area to
 the clipboard. You can paste the contents of the clipboard into reports or charts.
 This selection inverts the colors of the display to generate the current view on a
 white background.
- Copy to Clipboard (Black Background) —Sends the current view
 of the Display Window and the Device Configuration and Measurements Display Area to
 the clipboard. You can paste the contents of the clipboard into reports or
 charts.

Parent topic:

NI-RFSA Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsa path=programming-considerations.html language=enus -->
## TOPIC 00049: Programming Considerations

- bundle_id: `ni-rfsa`
- source_path: `programming-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/programming-considerations.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Understand the RF programming tools and modes.

### Programming Considerations

Understand the RF programming tools and modes.

- [RF List Mode](rf-list-mode.html) RF list mode is an operating mode in which the hardware deterministically sequences through a predetermined set of RF configurations.
- [Driver Setup Options](driver-setup-options.html) The Driver Setup string is used with Initialize With Options to set the initial values for properties that are specific to NI-RFSA .
- [Specifying or Simulating a Device with NI-RFSA](simulating-a-device-using-nirfsa.html) You can simulate NI-RFSA device using NI-RFSA to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage.
- [NI-RFSA Simulated Devices](nirfsa-simulated-devices.html) You can simulate NI-RFSA device using NI-RFSA or Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware.
- [Associating Hardware Modules in SystemDesigner](associating-modules.html) Before you can program your vector signal analyzer, you must create an association between the individual hardware modules to control them as a single RF device.
- [Using the NI-RFSA .NET Class Library](using-net-class-library.html) You can use the NI-RFSA .NET class library to initialize, configure, initiate, run, and close a session on your NI-RFSA device. The NI-RFSA .NET API is an IVI-compliant instrument driver that features a set of methods and properties that exercise the functionality of the NI-RFSA hardware.

<!--NI_TOPIC bundle=ni-rfsa path=removing-a-simulated-ni-rfsa-device.html language=enus -->
## TOPIC 00050: Removing a Simulated NI-RFSA Device

- bundle_id: `ni-rfsa`
- source_path: `removing-a-simulated-ni-rfsa-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/removing-a-simulated-ni-rfsa-device.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: To remove a simulated NI-RFSA device in MAX, complete the following steps: Right-click the device name in the configuration tree. Select Delete.

### Removing a Simulated NI-RFSA Device

To remove a simulated NI-RFSA device in MAX, complete the following steps:

1. Right-click the device name in the configuration tree.
2. Select Delete .

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=renaming-an-ni-rfsa-device.html language=enus -->
## TOPIC 00051: Renaming an NI-RFSA Device

- bundle_id: `ni-rfsa`
- source_path: `renaming-an-ni-rfsa-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/renaming-an-ni-rfsa-device.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: MAX allows you to rename each of your NI-RFSA devices. The MAX name is used in NI-RFSA to operate the hardware resources. You are not required to change the device names from the default, but doing so can make programming easier. To rename your NI-RFSA device in MAX, complete the following steps: Se

### Renaming an NI-RFSA Device

MAX allows you to rename each of your NI-RFSA devices. The MAX name is used in NI-RFSA to
 operate the hardware resources. You are not required to change the device names from the
 default, but doing so can make programming easier. To rename your NI-RFSA device in MAX,
 complete the following steps:

1. Select the device name in the configuration tree.
2. Within the Settings section, enter a new name for your NI-RFSA device in the Name
 textbox.
3. Click Save in the MAX toolbar.
4. Verify that the new names for all of your devices are displayed before associating
 your devices.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=reproducing-sfp-configurations-using-the-ni-r.html language=enus -->
## TOPIC 00052: Reproducing SFP Configurations Using the NI-RFSA Driver

- bundle_id: `ni-rfsa`
- source_path: `reproducing-sfp-configurations-using-the-ni-r.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/reproducing-sfp-configurations-using-the-ni-r.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-RFSA Soft Front Panel (SFP) automatically performs the configurations necessary for certain measurement settings. If you perform the same measurements using SFP session access, you may need to manually make certain configuration changes to achieve the same results when you resume your applica

### Reproducing SFP Configurations Using the NI-RFSA Driver

The NI-RFSA Soft Front Panel (SFP) automatically performs the configurations
 necessary for certain measurement settings. If you perform the same
 measurements using SFP session access, you may need to manually make
 certain configuration changes to achieve the same results when you
 resume your application without the SFP.

The following example illustrates a situation in which you use NI-RFSA in
 your application to duplicate behavior that is automatically performed
 by the SFP:

1. You use the SFP to connect to a device session.
2. Using the SFP, you configure your measurement to display the sum
 of two traces. The SFP automatically performs the math
 operations and displays the result. You want to log the data
 to a file.
3. You exit SFP control (local) to return to your application. The
 math operations are no longer performed for you, and you no
 longer receive trace sum data.
4. You manually update your application to return the sum of the two
 traces using math functions and log the data to a file.

The following table displays the special configurations performed by the SFP.
 Refer to the National Instruments website at
 ni.com/info
 and enter the Info Code
 exmdfm
 for examples of how to duplicate SFP configuration using NI-RFSA.

| SFP Control Button Label | Configuration Performed by SFP | Result of Exiting SFP Local Mode or SFP Application |
| --- | --- | --- |
| Trigger»IQ Power Edge Trigger»External Digital Trigger»Software | The SFP sets the Acquisition Type to I/Q, acquires I/Q samples, and uses the I/Q samples to calculate the power spectrum. | NI-RFSA Acquisition Type remains IQ. |
| Trigger»External Digital»Delay Trigger»IQ Power Edge»Delay | When the trigger delay is positive, the SFP configures pre trigger samples as 0 and reference trigger delay as the delay value. When the trigger delay is negative, the SFP configures pre trigger samples using delay and IQ rate, and configures reference trigger delay to 0. | The calculated values do not change from the last configured settings. |
| BW»RBW»Automatic | The SFP automatically calculates and configures the RBW value using dependent controls. | RBW calculation mode reverts to Manual using the last automatically calculated value. |
| BW»VBW | For explanations of how the SFP performs video bandwidth (VBW) filtering, refer to the National Instruments website at ni.com/info and enter one of the following Info Codes: Enter code exsqb5 for a conceptual overview of video bandwidth and detector emulation. Enter code exmdfm for an example of how the SFP performs VBW filtering. | No VBW filter is applied to the acquired spectrum. The VBW value reverts to bypass. |
| BW»Coupling Ratios | The SFP provides an option to define how span, RBW, and VBW values are coupled with each other in RBW automatic mode and VBW automatic mode. | Parameters are decoupled. |
| Amptd»PSD | The SFP analyzes the acquired spectrum and displays the power level per unit bandwidth and displays the data in unit/Hz. | The acquired power spectrum is returned in the configured unit, not as PSD. |
| Trace/Detector»Average | The SFP retains the average of the point-by-point values of the previous trace data and the newly acquired data. | If Average Control is configured to SFP, NI-RFSA configures Averaging mode to no averaging. |
| Trace/Detector»Max Hold | The SFP retains the maximum point-by-point values of the previous trace data and the newly acquired data. | If Average Control is configured to SFP, NI-RFSA configures Averaging mode to no averaging. |
| Trace/Detector»Min Hold | The SFP retains the minimum point-by-point values of the previous trace data and the newly acquired data. | If Average Control is configured to SFP, NI-RFSA configures Averaging mode to no averaging. |
| Trace/Detector»Detector»Average | The SFP displays the average of signals within a bin. For explanations of how the SFP applies detectors, refer to the National Instruments website at ni.com/info and enter one of the following Info Codes: Enter code exsqb5 for a conceptual overview of video bandwidth and detector emulation. Enter code exmdfm for an example of how the SFP performs VBW filtering and detector emulation. | The trace detector mode reverts to sample. |
| Trace/Detector»Detector»Positive Peak | The SFP displays the highest amplitude within a bin. For explanations of how the SFP applies detectors, refer to the National Instruments website at ni.com/info and enter one of the following Info Codes: Enter code exsqb5 for a conceptual overview of video bandwidth and detector emulation. Enter code exmdfm for an example of how the SFP performs VBW filtering and detector emulation. | The trace detector mode reverts to sample. |
| Trace/Detector»Detector»Negative Peak | The SFP displays the lowest amplitude within a bin. For explanations of how the SFP applies detectors, refer to the National Instruments website at ni.com/info and enter one of the following Info Codes: Enter code exsqb5 for a conceptual overview of video bandwidth and detector emulation. Enter code exmdfm for an example of how the SFP performs VBW filtering and detector emulation. | The trace detector mode reverts to sample. |
| Trace/Detector»Math Trace/Detector»Trace Math | The SFP supports displaying the acquired spectrum in four different traces. You can apply predefined mathematical operations to display the sum of traces, the difference between traces, or trace offsets. | No math operations are applied to the acquired spectrum. |
| Trace/Detector»AverageControl | When Averaging Control is configured to Driver, the driver averaging mode is set to the value configured in the SFP. When Averaging Control is configured to SFP, the driver averaging mode is set to None and averaging is performed by the SFP. | If Average Control is configured to SFP, Averaging mode is configured to no averaging. |

Parent topic:

Debugging Your Application Using SFP Session Access

<!--NI_TOPIC bundle=ni-rfsa path=resolution-bandwidth.html language=enus -->
## TOPIC 00053: Resolution Bandwidth

- bundle_id: `ni-rfsa`
- source_path: `resolution-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/resolution-bandwidth.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: For NI VSAs and VSTs, the resolution bandwidth (RBW) determines the fast-Fourier transform (FFT) bin size, or the smallest frequency that can be resolved. The following graphs represent the same signal with varying RBW. The smaller RBW, on the right, has much finer resolution which allows the sideba

### Resolution Bandwidth

For NI VSAs and VSTs, the *resolution bandwidth* (*RBW*)
 determines the fast-Fourier transform (FFT) bin size, or the smallest frequency that can be
 resolved.

The following graphs represent the same signal with varying RBW.

[IMAGE alt='image' src='GUID-175B075B-C5CA-46DC-AEA0-540E12EAEAB0-a5.svg']

The smaller RBW, on the right, has much finer resolution which allows the sidebands to be
 visible. Finer resolution requires a longer acquisition time. When acquisition time is a
 factor and the display needs to be updated rapidly or when the modulation bandwidth is wide,
 you can use a larger RBW. RBW and acquisition time are inversely proportional.

The following table shows the advantages and disadvantages of both larger and smaller
 RBWs:

| Characteristic | Larger RBW | Smaller RBW |
| --- | --- | --- |
| FFT size | Smaller | Larger |
| Number of samples | Fewer | More |
| Measurement speed | Faster | Slower |
| Ability to resolve tones | Often unable to resolve two closely spaced tones in a spectrum | Tones are easily resolved |

In FFT-based (digital) spectrum analyzers and vector signal analyzers, RBW is inversely
 proportional to the number of samples acquired. By taking more samples in the time domain, or
 making the acquisition time longer while keeping the sampling rate the same, the RBW is
 lowered. The result is more bins in the same span and improved frequency resolution.

The FFT process is equivalent to passing a time-domain signal through a bank of bandpass
 filters with center frequencies corresponding to the frequencies of the FFT bins. For wide
 sweeps, a wide RBW is required to shorten acquisition times. For narrow sweeps, a narrow
 filter improves frequency resolution.

Carefully consider which FFT window type to use. As an example, a Flat Top window minimizes
 amplitude measurement error and is recommended for amplitude measurements even though it has
 non-optimal selectivity.

<!--NI_TOPIC bundle=ni-rfsa path=rf-list-mode.html language=enus -->
## TOPIC 00054: RF List Mode

- bundle_id: `ni-rfsa`
- source_path: `rf-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/rf-list-mode.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: RF list mode is an operating mode in which the hardware deterministically sequences through a predetermined set of RF configurations. A given set of RF configurations, as specified by an RF configuration list, is enacted by the RF modules without any interaction with the host system and NI-RFSA. Bec

### RF List Mode

RF list mode is an operating mode in which the hardware deterministically sequences
 through a predetermined set of RF configurations. A given set of RF
 configurations, as specified by an RF configuration list, is enacted by the RF modules without
 any interaction with the host system and NI-RFSA. Because the
 host system is not involved in executing the RF configuration list changes, the changes from one
 step in the list to the next are deterministic.

Note

RF List Mode Supported Hardware: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5840/5841/5842

Parent topic:

Programming Considerations

<!--NI_TOPIC bundle=ni-rfsa path=running-a-self-test-on-an-ni-rfsa-device.html language=enus -->
## TOPIC 00055: Running a Self-Test on an NI-RFSA Device

- bundle_id: `ni-rfsa`
- source_path: `running-a-self-test-on-an-ni-rfsa-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/running-a-self-test-on-an-ni-rfsa-device.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The MAX self-test performs a basic verification of hardware resources. To run a self-test on your NI-RFSA device in MAX, complete the following steps: You can only perform a self-test on the individual associated modules within a hardware system. Select the device name in the configuration tree. C

### Running a Self-Test on an NI-RFSA Device

Note

1. Select the device name in the configuration tree.
2. Click Self-Test in the MAX toolbar. Note For
 the PXIe-3621/3622/3623, you can perform a basic or intermediate self-test. Use
 a basic self-test to verify communication with the device. Use an intermediate
 self-test to verify analog cable connections and locate failures on the device
 and associated devices.
3. A message appears indicating the self-test result. Close the dialog box to
 continue.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=saving-a-configuration.html language=enus -->
## TOPIC 00056: Saving a Configuration

- bundle_id: `ni-rfsa`
- source_path: `saving-a-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/saving-a-configuration.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-RFSA SFP allows you to save all the current settings and to later recall them to restore the Soft Front Panel to a predefined state. The NI-RFSA SFP utilizes the TDMS file type for this purpose. Although the configuration is stored in binary format, you can open and read TDMS files using the

### Saving a Configuration

The NI-RFSA SFP allows you to save all the current settings and to later recall them to
 restore the Soft Front Panel to a predefined state. The NI-RFSA SFP utilizes the TDMS
 file type for this purpose. Although the configuration is stored in binary format, you
 can open and read TDMS files using the NI LabVIEW TDMS viewer, shown in the following
 figure, or the TDM Excel Add-In for Microsoft Excel.

[IMAGE alt='image' src='GUID-A3B4A523-F30E-4B98-8CFF-7570C102082B-a5.png']

Click the Save button to save measurement and acquisition
 configurations in the TDMS file format. Click the Save to File
 softkey to save to a TDMS file, or click one of the Quick Save
 softkeys to allow for one click save/recall. Click the Recall
 button to recall a previously saved configuration.

To save your current Soft Front Panel settings, complete the following steps:

1. Click the Save button or select File»Save
 Configuration .
2. If you click the Save button, click the Save to
 File softkey, otherwise, skip to step 3.
3. Specify a path and file name in the dialog box.
4. Click OK .

To apply a Soft Front Panel configuration that was previously saved, complete the
 following steps:

1. Click the Recall button or select File»Recall
 Configuration .
2. If you clicked the Recall button, click the Recall
 from File softkey, otherwise, skip to step 3.
3. In the file dialog box, navigate to the configuration that you want to recall.
4. Click OK .

Parent topic:

NI-RFSA Soft Front Panel

<!--NI_TOPIC bundle=ni-rfsa path=signal-routing.html language=enus -->
## TOPIC 00057: Signal Routing

- bundle_id: `ni-rfsa`
- source_path: `signal-routing.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/signal-routing.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: A can send and receive signals through the front panel connectors and the trigger bus. The front panel connectors provide connectivity for the input and output signals and for the control lines that send and receive clocks, triggers, and events. You can use the trigger bus to send and receive events

### Signal Routing

A can send and receive signals through the front panel connectors and the trigger bus. 
 The front panel connectors provide connectivity for the input and output signals and for the control lines that send and receive clocks, triggers, and events. You can use the trigger bus to send and receive events, triggers, and Sample and Reference Clocks.

Signals can be routed to and from the supported front panel connectors of your device. All signal routing operations can be characterized by a source and a destination. The possible signal routes for your device depend on the device, the chassis, and the occupied chassis slot. Refer to your chassis documentation to determine the configuration of trigger bus segments of your chassis.

Note

#### Static and Dynamic Routes

When a signal is exported to a trigger line from a device, only devices in the same chassis segment recognize the signal from that trigger line. To route the signal to devices in a different chassis segment, you must establish a static or dynamic route.

A 
 *dynamic route* is a type of signal route that is specified by only the route endpoints. The actual route is determined automatically in software and is reserved and unreserved based on the NI-RFSA session using that route. To release a dynamic route, close the NI-RFSA session(s) using that route.

A 
 *static route* is a type of signal route that you must create manually. To create and configure static routes, you must use the NI-DAQmx API.

<!--NI_TOPIC bundle=ni-rfsa path=simulating-a-device-using-nirfsa.html language=enus -->
## TOPIC 00058: Specifying or Simulating a Device with NI-RFSA

- bundle_id: `ni-rfsa`
- source_path: `simulating-a-device-using-nirfsa.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/simulating-a-device-using-nirfsa.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: You can simulate NI-RFSA device using NI-RFSA to develop, modify, and/or test an application without hardware. Using a simulated device to test an application eliminates the risk of hardware damage. You can also simulate a device in Measurement & Automation Explorer (MAX). Refer to Simulating an NI-

### Specifying or Simulating a Device with NI-RFSA

You can simulate NI-RFSA device using NI-RFSA to develop, modify, and/or test an application without
 hardware. Using a simulated device to test an application eliminates the risk of hardware
 damage.

You can also simulate a device in Measurement & Automation Explorer (MAX). Refer to
 *Simulating an NI-RFSA Device in MAX* for more information.

Note

PXIe-5624

NI-RFSA

PXIe-5668

Complete the following steps to specify or simulate the device that you want to use.

1. Call Initialize With Options.
2. Set the option string input. 
 The option string input is composed of the
 Simulate and the DriverSetup keywords,
 as shown in the following table.
 Note In the following tables, the portion
 of the string that follows the colon is the device name you see in NI Measurement &
 Automation Explorer (MAX). For the PXIe-5624/5668 and PXIe-5644/5645/5646, the string must include
 R after the model number.Table 2.Specifying or Simulating a Device
 Using PXIe-5663E/5665/5667/5668Use
 Example Driver Setup StringSimulate a digitizer
 Simulate=1,DriverSetup=Digitizer:5622To simulate a
 device using the PXIe-562225 MHz digitizer:Set the Digitizer field to
 5622_25MHz_DDC.
 Set the Simulate field to
 1.You can set the Digitizer field to
 5622_25MHz_DDC only when using the PXIe-5665.
 Specify a digitizer
 DriverSetup=Digitizer:my5622
 Specify an external digitizer
 DriverSetup=Digitizer:<external>
 Simulate an LO source
 Simulate=1,DriverSetup=LO:5652To
 specify a simulated device, use a string similar to:
 Simulate=1,DriverSetup=LOBoardType:PXIe.
 Specify an LO source
 DriverSetup=LO:my5652
 Specify an external LO source
 DriverSetup=LO:<external>
 Simulate multiple devices
 Simulate=1,DriverSetup=Model:5601;LO:5652;Digitizer:5622;LOBoardType:PXIeWhen
 specifying or simulating multiple associated devices, separate devices with a
 semicolon, as shown in the preceding string.
 Simulate a vector signal analyzer
 Simulate=1,DriverSetup=Model:5668R or
 Simulate=1, DriverSetup=Model:5606; Digitizer:5624R;
 LO:5653
 Specify the resource name of the RF conditioning
 sourceOnly for PXIe-5667/5668.
 DriverSetup=RFConditioning:PXISlot2
 where PXISlot2 is an applicable RF
 conditioning device.
 Specify the resource name of the IF conditioning
 sourceOnly for PXIe-5667.
 DriverSetup=IFConditioning:PXISlot3
 where PXISlot3 is an applicable IF
 conditioning device.Table 3.Specifying or Simulating a Device
 Using PXIe-5830/5831/5840/5841/5842Use
 Example Driver Setup StringSimulate a digitizer(Only for PXIe-5830/5831.)
 Simulate=1,DriverSetup=Digitizer:5622
 To simulate a device using the PXIe-562225 MHz digitizer:Set the Digitizer field to
 5622_25MHz_DDC.
 Set the Simulate field to
 1.You can set the Digitizer field to
 5622_25MHz_DDC only when using the PXIe-5665.
 Specify a digitizer(Only for PXIe-5830/5831.)
 DriverSetup=Digitizer:my5622
 Specify an external digitizer(Only for PXIe-5830/5831.)
 DriverSetup=Digitizer:<external>
 Simulate an LO source(Only for PXIe-5830/5831.)
 Simulate=1,DriverSetup=LO:5652To
 specify a simulated device, use a string similar to:
 Simulate=1,DriverSetup=LOBoardType:PXIe.
 Specify an LO source
 DriverSetup=LO:my5652
 Specify an external LO source
 DriverSetup=LO:<external>
 Simulate multiple devices
 Simulate=1,DriverSetup=Model:5601;LO:5652;Digitizer:5622;LOBoardType:PXIe
 When specifying or simulating multiple associated devices, separate the
 devices with a semicolon, as shown in the preceding string.
 Simulate a vector signal transceiver
 Simulate=1,DriverSetup=Model:5644RTable 4.Specifying or Simulating a Device
 Using PXIe-5820/5860Use
 Example Driver Setup StringSimulate a vector signal transceiver
 Simulate=1,DriverSetup=Model:5644RTable 5.Specifying or Simulating a Device
 Using PXIe-5644/5645/5646Use
 Example Driver Setup StringSpecify an external LO source
 DriverSetup=LO:<external>
 Simulate multiple devices
 Simulate=1,DriverSetup=Model:5601;LO:5652;Digitizer:5622;LOBoardType:PXIe
 When specifying or simulating multiple associated devices, separate The
 devices with a semicolon, as shown in the preceding string.
 Simulate a vector signal transceiver
 Simulate=1,DriverSetup=Model:5644R

Parent topic:

Programming Considerations

Related concepts:

- Driver Setup Options

Related tasks:

- Simulating an NI-RFSA Device in MAX

<!--NI_TOPIC bundle=ni-rfsa path=simulating-an-ni-rfsa-device.html language=enus -->
## TOPIC 00059: Simulating an NI-RFSA Device in MAX

- bundle_id: `ni-rfsa`
- source_path: `simulating-an-ni-rfsa-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/simulating-an-ni-rfsa-device.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: Simulate an NI-RFSA device using Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware. You can also simulate your device using NI-RFSA. Refer to Specifying or Simulating a Device with NI-RFSA for more information. Using a simulated device to test an

### Simulating an NI-RFSA Device in
 MAX

Simulate an NI-RFSA device using Measurement & Automation Explorer (MAX) to
 develop, modify, and/or test an application without hardware.

You can also simulate your device using NI-RFSA. Refer to *Specifying or Simulating
 a Device with NI-RFSA* for more information.

Using a simulated device to test an application eliminates the risk of hardware
 damage. Additionally, you can use a simulated NI-RFSA device to evaluate an NI
 product for which you don't have hardware.

Note

Complete the following steps to create and configure a simulated NI-RFSA device in
 MAX.

1. Launch MAX.
2. Select Devices and Interfaces in the MAX configuration
 tree, and click Create New in the MAX toolbar. The Create
 New dialog box opens.
3. Select Simulated NI-DAQmx Device or Modular Instrument,
 and click Finish.
4. In the Create Simulated NI-DAQmx Device window, expand
 RF Devices, and select the NI-RFSA device to
 simulate. 
 Note There is no
 option to simulate a vector signal analyzer. If you want to simulate a
 vector signal analyzer, you must simulate the individual devices that
 comprise the vector signal analyzer.
5. Click OK. 
 The NI-RFSA device appears in the MAX configuration tree with a yellow
 icon to indicate that it's a simulated device.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

Related tasks:

- Specifying or Simulating a Device with NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=software-edge-trigger.html language=enus -->
## TOPIC 00060: Software Trigger

- bundle_id: `ni-rfsa`
- source_path: `software-edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/software-edge-trigger.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `reference`
- source_description: A software trigger is generated internally by a programmatic call to the NI-RFSA Send Software Edge Trigger function and can occur at any time, based upon the conditions specified in the program. You can configure each named trigger in NI-RFSA to operate based on a software edge.

### Software Trigger

A software trigger is generated internally by a programmatic call to the NI-RFSA
 Send Software Edge Trigger function and can occur at any time, based upon
 the conditions specified in the program.

You can configure each named trigger in NI-RFSA to operate based on a software edge.

Parent topic:

NI-RFSA Named Trigger Types

<!--NI_TOPIC bundle=ni-rfsa path=synchronizing-ni-rfsa-devices.html language=enus -->
## TOPIC 00061: Synchronizing NI-RFSA Devices

- bundle_id: `ni-rfsa`
- source_path: `synchronizing-ni-rfsa-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/synchronizing-ni-rfsa-devices.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you plan to share triggers or clocks to synchronize devices, your chassis and controller must be properly detected and identified in MAX. PXI Express devices controlled using MXI-Express: In the MAX configuration tree under Devices and Interfaces, right-click PXI System. Select Identify As, and s

### Synchronizing NI-RFSA Devices

If you plan to share triggers or clocks to synchronize devices, your chassis and
 controller must be properly detected and identified in MAX.

#### PXI Express devices controlled using MXI-Express:

1. In the MAX configuration tree under Devices and Interfaces, right-click
 PXI System .
2. Select Identify As , and select External
 PC . Your chassis is automatically identified.

#### PXI Express controllers:

A PXI Express controller installed in a PXI Express chassis is automatically
 identified in MAX.

For more information on synchronizing NI-RFSA devices, refer to the NI-TClk
 Synchronization Help.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=system-requirements.html language=enus -->
## TOPIC 00062: System Requirements

- bundle_id: `ni-rfsa`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/system-requirements.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-RFSA has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAMDepending on the data you acquire or process, your system might need more memory. A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs No OS supports guest acc

### System Requirements

NI-RFSA has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM [[1]](#note-d2524e29) [<sup>1</sup>](#fnsrc_1-d2524e29) Depending on the data you acquire or process, your system might need more
 memory.
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

Note

[<sup>1</sup>](#note_ref-d2524e29) Depending on the data you acquire or process, your system might need more
 memory.

<!--NI_TOPIC bundle=ni-rfsa path=terminal-name-syntax.html language=enus -->
## TOPIC 00063: Terminal Names and Terminal Name Syntax

- bundle_id: `ni-rfsa`
- source_path: `terminal-name-syntax.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/terminal-name-syntax.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: A terminal name is a unique identifier that refers to a physical terminal in your system. A terminal name is fully qualified if it is an unambiguous reference to a specific terminal. Terminal names use the following format: /instrument name/terminal name where instrument name is the name of the inst

### Terminal Names and Terminal Name
 Syntax

A *terminal name* is a unique identifier that
 refers to a physical terminal in your system. A terminal name is *fully qualified* if
 it is an unambiguous reference to a specific terminal.

Terminal names use the following format:

/instrument name/terminal name

where

- instrument name is the name of the instrument as configured in MAX or
 Hardware Configuration Utility, such as PXI1Slot2
- terminal name is the name of the specific terminal, such as
 PFI1

This format guarantees the uniqueness of a terminal name across multiple
 instruments.

For example, the fully qualified terminal name for PFI1
 on PXI1Slot2 is /PXI1Slot2/PFI1.

Parent topic:

Signal Routing

<!--NI_TOPIC bundle=ni-rfsa path=total-harmonic-distortion.html language=enus -->
## TOPIC 00064: Total Harmonic Distortion

- bundle_id: `ni-rfsa`
- source_path: `total-harmonic-distortion.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/total-harmonic-distortion.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: Total harmonic distortion (THD) is a representation of the effect that multiple harmonic spurs throughout a spectrum band have on the fundamental tone. You can calculate THD by summing the power in each of the harmonics and dividing by the total power of the fundamental. As a general principle, a si

### Total Harmonic Distortion

*Total harmonic distortion* (THD) is a representation of the effect that multiple harmonic spurs throughout a spectrum band have on the fundamental tone.

You can calculate THD by summing the power in each of the harmonics and dividing by the total power of the fundamental. As a general principle, a signal becomes visibly distorted when the THD approaches -30 dB.

The equation for THD is:

T

H

D

=

V

h

2

2

+

V

h

3

2

+

V

h

4

2

+

…

+

V

h

N

2

V

f

u

n

d

×

100

%

T

H

D

=

V

h

2

2

+

V

h

3

2

+

V

h

4

2

+

…

+

V

h

N

2

V

f

u

n

d

×

100

%

As this equation suggests, the THD specification evaluates the power in harmonic spurs from the second through the n<sup>th</sup> harmonic. In practice, typical signal generators feature THD specifications for harmonics two through six. The following figure shows an example plot of a generated signal and illustrates the concept of THD specification in signal generators.

Figure 5.

[IMAGE alt='image' src='GUID-91B04663-A872-40E2-B0CD-9DDDE129956B-a5.svg']

The previous figure shows an example plot of a 20 kHz sinusoid generated with an arbitrary waveform generator. Notice the power levels of the harmonic spurs, indicated with circles. This generator features -77 dBc or better of THD for the second through sixth harmonics.

THD generally deteriorates as the generated signal increases in frequency. When working with a signal generator, consider the THD throughout the bandwidth of the generator.

Parent topic:

NI-RFSA Noise Fundamentals

<!--NI_TOPIC bundle=ni-rfsa path=transitioning-to-and-from-sfp-control-local.html language=enus -->
## TOPIC 00065: Transitioning to and from SFP Control (Local)

- bundle_id: `ni-rfsa`
- source_path: `transitioning-to-and-from-sfp-control-local.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/transitioning-to-and-from-sfp-control-local.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: When NI-RFSA Soft Front Panel (SFP) session access is enabled, SFP control (local) allows you to take control of the device and change device or measurement settings from the SFP. For example, you might determine that you want to change your device configuration based on unexpected results from your

### Transitioning to and from SFP Control (Local)

When NI-RFSA Soft Front Panel (SFP) session access is enabled, SFP control (local) allows
 you to take control of the device and change device or measurement settings from the
 SFP.

For example, you might determine that you want to change your device configuration based
 on unexpected results from your application. Using SFP control (local), you can
 immediately make your changes in the SFP and execute the rest of your code with the new
 settings. Changing device settings from the SFP can help you troubleshoot problems.

To use SFP control (local), complete the following steps:

1. Ensure that SFP session access is enabled for your device in your application.
2. At the appropriate point, pause your code execution and launch the SFP. You can
 launch the SFP from the Start menu or from a probe in LabVIEW. Note 
 Your application must remain paused while you are using SFP control (local).
3. Click the SFP Control (Local) softkey in the SFP.
4. Make changes to the device settings using the SFP controls.
5. Exit the SFP, close the session, or switch devices. The Revert
 changes? dialog box appears. Note Resuming your code
 without exiting the SFP causes the SFP to lose control of the device and
 prevents you from reverting any changes.
6. Click Show Changes to see a list of changes made to the
 application by the SFP.
7. Click Apply Changes to apply your changes to the device and
 return to your application. Click Revert Changes to return
 the device to the state it was in prior to opening the SFP.

Caution

Preset

Note

Parent topic:

Debugging Your Application Using SFP Session Access

Related concepts:

- Configuring SFP Session Access Using LabVIEW
- Launching the NI-RFSA SFP from LabVIEW

<!--NI_TOPIC bundle=ni-rfsa path=user-manual-welcome.html language=enus -->
## TOPIC 00066: NI-RFSA User Manual

- bundle_id: `ni-rfsa`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-RFSA User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-RFSA
 User Manual

The NI-RFSA User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-RFSA
- NI-RFSA Release Notes
- Interactive Activation Guide
- RFSA C API Reference Manual
- NI-RFSA C# .NET API Reference Manual
- NI-RFSA LabVIEW VI Reference
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-rfsa path=using-labview.html language=enus -->
## TOPIC 00067: Using NI-RFSA in LabVIEW

- bundle_id: `ni-rfsa`
- source_path: `using-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/using-labview.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to develop an NI-RFSA application in LabVIEW: Open an existing or new VI. From the Functions palette, locate the NI-RFSA VIs at Instrument I/OInstrument Driver. Select the VIs that you want to use and place them on the block diagram to build your application.

### Using NI-RFSA in LabVIEW

Complete the following steps to develop an NI-RFSA
 application in LabVIEW:

1. Open an existing or new VI.
2. From the 
 Functions palette, locate the NI-RFSA VIs at 
 Instrument I/O»Instrument Driver.
3. Select the VIs that you want to use and place them on the block diagram to build your application.

Parent topic:

Creating an Application with NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=using-labwindows-cvi.html language=enus -->
## TOPIC 00068: Using NI-RFSA in LabWindows/CVI

- bundle_id: `ni-rfsa`
- source_path: `using-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/using-labwindows-cvi.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to develop an NI-RFSA application in LabWindows/CVI: Open an existing or new project file in LabWindows/CVI. Select InstrumentLoad and select the NI-RFSA function panel (.fp). Use the function panel to navigate the function hierarchy and generate function calls with the

### Using NI-RFSA in LabWindows/CVI

Complete the following steps to develop an NI-RFSA application in LabWindows/CVI:

1. Open an existing or new project file in LabWindows/CVI.
2. Select 
 Instrument»Load and select the NI-RFSA function panel (.fp).
3. Use the function panel to navigate the function hierarchy and generate function calls with the proper syntax and variable values.

Parent topic:

Creating an Application with NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=using-microsoft-visual.html language=enus -->
## TOPIC 00069: Using NI-RFSA with Microsoft Visual C/C++

- bundle_id: `ni-rfsa`
- source_path: `using-microsoft-visual.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/using-microsoft-visual.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: You can develop an NI-RFSA application using Microsoft Visual C/C++ with Microsoft Visual C++ 6.0 or Microsoft Visual Studio 2010. Follow these general steps to create a C/C++ application. Open an existing or new Visual C/C++ project to manage your application code. Create source code files of type

### Using NI-RFSA with Microsoft Visual C/C++

You can develop an NI-RFSA application using Microsoft Visual C/C++ with Microsoft Visual C++ 6.0 or Microsoft Visual Studio 2010. Follow these general steps to create a C/C++ application.

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type 
 .c (C) or 
 .cpp (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: 
 #include ".h"
5. Add the NI-RFSA include and library files to the project.
  1. Navigate to the following location for your ADE and add the 
 and 
 visa.h files, separated by a semicolon. 
 In Microsoft Visual C++, select 
 Project»Settings»C/C++»Preprocessor»Additional include directories.
 In Microsoft Visual Studio, select 
 Project»Properties»Configuration Properties»C/C++»General»Additional Include Directories. 
 Note The 
 and 
 visa.h files are located in the 
 <IVIROOTDIR32>\Include and 
 <VXIPNPPATH>\WinNT\Visa\include directories, respectively.
  2. Select 
 Project»Link»General»Object/Library Modules and add 
 .
  3. Select 
 Project»Link»Input»Additional library path and add the path to the 
 file. 
 Note The 
 file is located in the the 
 <IVIROOTDIR32>\Lib x64\msc directory.
6. Build your application using the appropriate programming flow steps.

Parent topic:

Creating an Application with NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=using-net-class-library.html language=enus -->
## TOPIC 00070: Using the NI-RFSA .NET Class Library

- bundle_id: `ni-rfsa`
- source_path: `using-net-class-library.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/using-net-class-library.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NI-RFSA .NET class library to initialize, configure, initiate, run, and close a session on your NI-RFSA device. The NI-RFSA .NET API is an IVI-compliant instrument driver that features a set of methods and properties that exercise the functionality of the NI-RFSA hardware. 1. Initial

### Using the NI-RFSA .NET Class Library

You can use the NI-RFSA .NET class library to initialize,
 configure, initiate, run, and close a session on your NI-RFSA device. The NI-RFSA .NET API is an IVI-compliant
 instrument driver that features a set of methods and properties that exercise the
 functionality of the NI-RFSA hardware.

#### 1. Initialization

Use a constructor to create a new instance of the NIRfsa class.

Important

NI-RFSA

```text
VB.NET

Dim session As New NIRfsa("Rfsa", True, True) ' Initialize
```

```text
Visual C#

NIRfsa session = new NIRfsa("Rfsa", true, true); // Initialize
```

#### 2. Configuration

The NIRfsa object that you created gives you direct access to
 various sub-objects, which allow you to configure NI-RFSA, directly or indirectly. You can perform
 most of the configuration through the configuration sub-object.

```text
VB.NET

Dim session As New NIRfsa("Rfsa", True, True) ' Initialize
session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ
session.Configuration.Vertical.ReferenceLevel = -10.0
session.Configuration.IQ.CarrierFrequency = 10000000.0
session.Configuration.IQ.NumberOfSamples = 1000
```

```text
Visual C#

NIRfsa session = new NIRfsa("Rfsa", true, true); // Initialize
session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ;
session.Configuration.Vertical.ReferenceLevel = -10.0;
session.Configuration.IQ.CarrierFrequency = 10E+6;
session.Configuration.IQ.NumberOfSamples = 1000;
```

#### 3. Initiate

The NI-RFSA device starts acquiring the configured
 waveform signal as soon as you initiate the signal acquisition, unless the NI-RFSA driver is waiting for a trigger.

```text
VB.NET

session.Acquisition.IQ.Initiate()
```

```text
Visual C#

session.Acquisition.IQ.Initiate();
```

#### 4. Fetch

Transfers the acquired data from NI-RFSA memory to the system memory.

The different types of fetch are:

- Single record fetch
- Single record memory optimized fetch
- Multi-record fetch
- Multi-record memory optimized fetch

```text
VB.NET

session.Acquisition.IQ.Initiate()
session.Acquisition.IQ.FetchIQSingleRecordComplex(Of ComplexDouble)(0, 1000, New PrecisionTimeSpan(5))
```

```text
Visual C#

session.Acquisition.IQ.Initiate();
session.Acquisition.IQ.FetchIQSingleRecordComplex<ComplexDouble>(0, 1000, new PrecisionTimeSpan(5));
```

#### 5. Read

Initiates acquisition, waits for the acquisition to complete and then retrieves the
 data.

There are two types of read :

- Single record read
- Single record memory optimized read

```text
VB.NET

session.Acquisition.IQ.ReadIQSingleRecordComplex(New PrecisionTimeSpan(5))
```

```text
Visual C#

session.Acquisition.IQ.ReadIQSingleRecordComplex(new PrecisionTimeSpan(5));
```

#### 6. Close

Close the session to the device and free unmanaged resources that the session holds.
 You can close the session with Close or
 Dispose.

```text
VB.NET

session.Close()
```

```text
Visual C#

session.Close();
```

or

```text
VB.NET

session.Dispose()
```

```text
Visual C#

session.Dispose();
```

or

```text
VB.NET

Using session As New NIRfsa("Rfsa", True, True)
'User code goes here
End Using
```

```text
Visual C#

using (NIRfsa session = new NIRfsa("Rfsa", true, true))
{
// User code goes here
}
```

#### Example: Acquiring a
 Waveform

The following code snippet acquires a waveform.

```text
VB.NET

Using session As New NIRfsa("Rfsa", True, True)
    session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ
    session.Configuration.Vertical.ReferenceLevel = -10.0
    session.Configuration.IQ.CarrierFrequency = 10000000.0
    session.Configuration.IQ.NumberOfSamples = 1000
    session.Acquisition.IQ.Initiate()
    Dim data As ComplexWaveform(Of ComplexDouble) = session.Acquisition.IQ.FetchIQSingleRecordComplexWaveform(Of ComplexDouble)(0, 1000, New PrecisionTimeSpan(5))
End Using
```

```text
Visual C#

using (NIRfsa session = new NIRfsa("Rfsa", true, true))
 {
    session.Configuration.AcquisitionType = RfsaAcquisitionType.IQ;
    session.Configuration.Vertical.ReferenceLevel = -10.0;
    session.Configuration.IQ.CarrierFrequency = 10E+6;
    session.Configuration.IQ.NumberOfSamples = 1000;
    session.Acquisition.IQ.Initiate();
    ComplexWaveform<ComplexDouble> data = session.Acquisition.IQ.FetchIQSingleRecordComplexWaveform<ComplexDouble>(0, 1000, new PrecisionTimeSpan(5));
 }
```

Parent topic:

Programming Considerations

Related information:

- NI-RFSA C# .NET API Reference Manual

<!--NI_TOPIC bundle=ni-rfsa path=using-net.html language=enus -->
## TOPIC 00071: Using the NI-RFSA .NET Class Library with Microsoft Visual Studio

- bundle_id: `ni-rfsa`
- source_path: `using-net.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/using-net.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the NI-RFSA .NET Class Library with Microsoft Visual C# .NET or Microsoft Visual Basic .NET in any Visual Studio version that can target .NET Framework 4.0 or .NET Framework 4.5. To develop an NI-RFSA application in Visual C# or Visual Basic .NET, follow these general steps. Open an exis

### Using the NI-RFSA .NET Class Library with Microsoft Visual Studio

You can use the NI-RFSA .NET Class Library with Microsoft Visual C# .NET or Microsoft Visual Basic .NET in any Visual Studio version that can target .NET Framework 4.0 or .NET Framework 4.5.

To develop an NI-RFSA application in Visual C# or Visual Basic .NET, follow these general steps.

1. Open an existing or new project file.
2. Load the NI-RFSA .NET class library (NationalInstruments.ModularInstruments..Fx40.dll or 
 NationalInstruments.ModularInstruments..Fx45.dll).
3. Use the hierarchy tree to navigate the sub-objects of . The object represents a session with your NI-RFSA device. All NI-RFSA functionality exists in or one of its sub-objects.

Parent topic:

Creating an Application with NI-RFSA

<!--NI_TOPIC bundle=ni-rfsa path=using-rf-list-mode.html language=enus -->
## TOPIC 00072: Using RF List Mode

- bundle_id: `ni-rfsa`
- source_path: `using-rf-list-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/using-rf-list-mode.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `task`
- source_description: An RF configuration list is composed of configuration list steps. Each step specifies the state of the instrument by specifying values for attributes/properties. Out of all available properties, select only those that you want to set from step-to-step and add them to the list. To use the RF list mod

### Using RF List Mode

An 
 *RF configuration list* is composed of 
 *configuration list steps*. Each step specifies the state of the instrument by specifying values for attributes/properties. Out of all available properties, select only those that you want to set from step-to-step and add them to the list.

To use the RF list mode, complete the following steps:

1. Create the RF configuration list.
  1. Call the Create Configuration List VI or function.
  2. Pass the array of properties or attribute IDs that you intend to change between configuration list steps. 
 When the set as active list input is set to True, the newly created list is set as the active configuration list.
2. If in the previous step you did not specify the active configuration list, do so now using the Active Configuration List property or attribute. 
 The active configuration list also specifies whether NI-RFSA operates using the RF list mode.
3. When the list is first created, the list has no steps. Populate the steps that make up the list, by calling the Create Configuration List Step VI or function. 
 When the set as active step input is set to True, the newly created step becomes the active configuration list step.
4. If in the previous step you did not specify the active configuration list step, do so now using the Active Configuration List Step property or attribute. 
 Initially, the active configuration list step contains the driver default values for each configuration list property that you specified in Create Configuration List. You can use the NI-RFSA property node or one of the set attribute functions to change the default values of those properties and attributes. 
 Note Configuration list steps are zero-based and numbered in the order in which you created them for the active list. List execution always starts with step zero.
5. To start RF list mode operation, call the Initiate VI or function. 
 After Initiate, the device starts executing the list as indicated by the Active Configuration List property or attribute.
 Note If you set the active list to 
 "", the NI-RFSA device operates without using RF list mode.

The RF configuration list advances at the end of each record, and the Ready for Advance Event waits for the device to settle in the new configuration; therefore, each record has a corresponding list step. If there are more records than list steps, the list steps advance from the last step to step zero. For example, if you have 10 records and five steps, records five through nine are acquired with list steps zero through four. This also applies to infinite records.

Note

PXIe-5663E/5665/5667

PXIe-5830/5831/5841/5842 with PXIe-5655

Parent topic:

RF List Mode

<!--NI_TOPIC bundle=ni-rfsa path=using-the-ni-rfsa-soft-front-panel.html language=enus -->
## TOPIC 00073: Using the NI-RFSA Soft Front Panel

- bundle_id: `ni-rfsa`
- source_path: `using-the-ni-rfsa-soft-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa/raw/resource/enus/using-the-ni-rfsa-soft-front-panel.html
- document_id: `ni-rfsa`
- page_type: `leaf`
- content_type: `concept`
- source_description: To verify your device configuration, use the NI-RFSA Soft Front Panel (SFP) to analyze a simple signal using your hardware. Select the device name in the MAX configuration tree. Click Soft Front Panel in the MAX toolbar. The NI-RFSA SFP launches. In the NI-RFSA SFP, specify a center frequency, span,

### Using the NI-RFSA Soft Front Panel

To verify your device configuration, use the NI-RFSA Soft Front Panel (SFP) to analyze a
 simple signal using your hardware.

1. Select the device name in the MAX configuration tree.
2. Click Soft Front Panel in the MAX toolbar. The NI-RFSA SFP
 launches.
3. In the NI-RFSA SFP, specify a center frequency, span, reference level, and
 resolution bandwidth for signal analysis.
4. Close the SFP when you have finished signal analysis.

Parent topic:

Using Measurement & Automation Explorer for NI-RFSA
