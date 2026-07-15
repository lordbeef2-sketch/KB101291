# NI DOCUMENT BUNDLE: pulsed-rf-meas-library-api-ref

<!--NI_BUNDLE_CHUNK bundle=pulsed-rf-meas-library-api-ref start=1 end=106 -->
<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-api-overview.html language=enus -->
## TOPIC 00001: Pulsed RF Measurement Library API Reference

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-api-overview.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-api-overview.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### [IMAGE alt='image' src='guid-ce18412b-7ee5-4b71-ad96-b279407c212e-a5.gif'] 
Pulsed RF Measurement
 Library API Reference

2022-06-28

This document provides reference information about the
 Pulsed RF Measurement (PRFMsc) VIs. Use the PRFMsc VIs to configure and execute pulsed RF
 measurements, such as S-parameter, PAE, pulse profile, and pulse stability
 measurements.

#### Accessing the Pulsed RF Measurement
 Library and Examples

Pulsed RF Measurement Library VIs are available from the Functions»Addons»NI PRFMsubpalette and the labview\vi.lib\addons\PRFMsc directory.
 Programming examples for the Pulsed RF Measurement Library LabVIEW VIs are located in the
 labview\examples\PRFMsc directory. You can modify an example VI to
 fit an application, or you can copy and paste from one or more examples into a VI you
 create.

© 2021–2022 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-calibrate-s-parameters.html language=enus -->
## TOPIC 00002: PRFMsc Calibrate S-Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-calibrate-s-parameters.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-calibrate-s-parameters.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Calibrate S-Parameters

PRFMsc Get Calibration Actions

[IMAGE alt='image' src='guid-9ba0363f-7fea-48e3-a8a9-09fbd399b4e2-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png']
 Calibration Action

Specifies the calibration action to perform. Obtain this string using the Get
 Calibration Actions VI. The default value is an empty string.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-close-measurement-pae.html language=enus -->
## TOPIC 00003: PRFMsc Close Measurement

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-close-measurement-pae.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-close-measurement-pae.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Close Measurement

Closes the PAE measurement session.

[IMAGE alt='image' src='guid-a1f427a1-5964-49e4-8a26-d69b91439989-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-close-measurement-pulse.html language=enus -->
## TOPIC 00004: PRFMsc Close Measurement

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-close-measurement-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-close-measurement-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Close Measurement

Closes the pulse reference session.

[IMAGE alt='image' src='guid-c39ed106-ca4f-4361-b07d-63c69400a49f-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-close.html language=enus -->
## TOPIC 00005: PRFMsc Close

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-close.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-close.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Close

Closes the S-parameter measurement session.

[IMAGE alt='image' src='guid-c7ebe1f3-091d-4cbd-839c-9eb531c4da62-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-commit-pae.html language=enus -->
## TOPIC 00006: PRFMsc Commit

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-commit-pae.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-commit-pae.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Commit

Commits parameters to the instruments and the PAE measurement.

- PRFMsc Commit (All)
- PRFMsc Commit Measurement
- PRFMsc Commit NIDCPower
- PRFMsc Commit NIRFmx
- PRFMsc Commit NIRFSG

#### PRFMsc Commit (All)

Commits all of the parameters to the NI-DCPower, NI-RFSG, and NI-RFmx instruments and
 commits the parameters for the PAE measurement.

[IMAGE alt='image' src='guid-fffb8c94-d522-4af4-ae71-b994f30ccf12-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Commit Measurement

Commits the parameters related to the measurement as Power Sweep and Frequency Sweep.
 Call this VI when you change any of the paramters for the PAE or PxdB
 measurement.

[IMAGE alt='image' src='guid-f79798b2-57c6-420d-b224-c4bd4347b767-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Commit NIDCPower

Commits the parameters to the NI-DCPower hardware. Call the Set NIDCPower
 Session VI with an initialized instrument before calling this VI.

[IMAGE alt='image' src='guid-1acee5c2-85f5-467a-9007-2d49709e0fc1-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Commit NIRFmx

Commits the parameters to the NI-RFmx hardware. Call the Set NIRFmx
 Session VI with an initialized instrument before calling this VI.

[IMAGE alt='image' src='guid-2995f1fe-f002-4e50-a71c-8ad52e363282-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Commit NIRFSG

Commits the parameters to the NI-RFSG hardware. Call the Set NIRFSG
 Session VI with an initialized instrument before calling this VI.

[IMAGE alt='image' src='guid-757d1100-acae-4ca6-92c4-e1b94b894f42-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-commit-pulse.html language=enus -->
## TOPIC 00007: PRFMsc Commit

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-commit-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-commit-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Commit

Commits parameters to the instruments and the pulse measurement.

- PRFMsc Commit (All)
- PRFMsc Commit (Pulse Configuration)
- PRFMsc Commit (NIRFSG Configurations)
- PRFMsc Commit (NIRFmx Configurations)

#### PRFMsc Commit (All)

Commits all of the parameters to the NI-RFSG and NI-RFmx instruments and commits the
 parameters for the pulse measurement. Call the Set NIRFSG Session and
 Set NIRFmx Session VIs with initialized instruments before calling
 this VI.

[IMAGE alt='image' src='guid-4ff7443f-e153-47c3-9a62-47e5e120d168-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Commit (Pulse Configuration)

Commits the parameters related to the measurement only.

[IMAGE alt='image' src='guid-0c21ad72-1a7b-4bb6-8519-99ffb3217699-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Commit (NIRFSG Configurations)

Commits the parameters to the NI-RFSG instrument. Call the PRFMsc Set NIRFSG
 Session VI before calling this VI.

[IMAGE alt='image' src='guid-2c4274da-7062-4062-ad99-7b382a1cc8b9-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Commit (NIRFmx Configurations)

Commits the parameters to the NI-RFmx instrument. Call the PRFMsc Set NIRFmx
 Session VI before calling this VI.

[IMAGE alt='image' src='guid-6e32af4e-757d-4608-89a0-413f28fd3491-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-commit.html language=enus -->
## TOPIC 00008: PRFMsc Commit

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-commit.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-commit.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Commit

PRFMsc Load Calibration

[IMAGE alt='image' src='guid-0738f7a9-a8e0-4376-9ca6-c849eb5af08b-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-compression-point.html language=enus -->
## TOPIC 00009: PRFMsc Configure Compression Point

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-compression-point.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-compression-point.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Compression Point

Defines the compression point used for the PxdB measurement. If you are not using PxdB
 measurement, you do not need to use this VI.

[IMAGE alt='image' src='guid-ca6eccd9-ca13-4eaf-9fcb-7129b5e84b48-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Compression Point
 (dB)

Specifies which compression point the PxdB algorithm will
 calculate. This is the difference, in dB, between the gain measured at the
 compression point and the gain measured within the linear range of the DUT. The
 default value is 1 dB for P1dB.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Maximum Linear Range
 (dBm)

Specifies the maximum DUT input power level that is in the
 linear range of the DUT. This value must be higher than the initial power and
 lower than stop power from the PRFMsc Configure RF Power
 Sweep VI. The default value is –5
 dBm.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-dcpower-levels.html language=enus -->
## TOPIC 00010: PRFMsc Configure DCPower Levels

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-dcpower-levels.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-dcpower-levels.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure DCPower Levels

Defines the voltage level and the current limit used by the NI-DCPower instrument to
 excite the external device. In pulse DC mode this specifies the voltage during the on phase
 of the pulse.

[IMAGE alt='image' src='guid-cdf54949-ed9f-4eea-9255-b4cc6df3bab9-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Voltage Level (V)

Specifies the voltage
 level, in volts, for the DC Power. The default value is 5
 V.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Current Limit
 (A)

Specifies the current limit for the DC Power. The default value is
 100 mA.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-dcpower-stimulus.html language=enus -->
## TOPIC 00011: PRFMsc Configure DCPower Stimulus

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-dcpower-stimulus.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-dcpower-stimulus.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure DCPower Stimulus

Configures the type of stimulus that the DCPower instrument will provide.

- PRFMsc Configure DCPower Stimulus (Constant)
- PRFMsc Configure DCPower Stimulus (Pulsed)

#### PRFMsc Configure DCPower Stimulus
 (Constant)

Configures DC Power to provide a constant voltage.

[IMAGE alt='image' src='guid-0170bd5b-e1fa-4d16-8e63-e243096a55d2-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png']
 PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure DCPower Stimulus
 (Pulsed)

Configures DCPower to generate voltage pulses.

[IMAGE alt='image' src='guid-996fb831-1ad4-46ad-91b9-901ed1246e94-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Pulse Width (s)

Specifies the pulse width, in us, of the voltage pulse The default value is
 200.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Bias Voltage Level (V)

Specifies the voltage level, in volts, during the low portion of the pulse for the DC
 Power. The default value is 0.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Bias Current Limit (A)

Specifies the current limit, in mA, during the low portion of the pulse, for the DC
 Power. The default value is 100.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-dcpower-to-rfsg-trigger.html language=enus -->
## TOPIC 00012: PRFMsc Configure DCPower to RFSG Trigger

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-dcpower-to-rfsg-trigger.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-dcpower-to-rfsg-trigger.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure DCPower to RFSG
 Trigger

Configures the trigger that synchronizes the RF pulse to the DC pulse.

- PRFMsc Configure DCPower to RFSG Trigger (Automatic Routing)
- PRFMsc Configure DCPower to RFSG Trigger (Manual Routing)

#### PRFMsc Configure DCPower to RFSG Trigger
 (Automatic Routing)

When the DCPower mode is pulsed, this method uses dynamic routing to set the DCPower
 Source Complete event as the input to the RFSG Pulse Trigger using an available PXI backplane
 trigger line. When the DCPower mode is constant, this method does not export the DC Power Source
 Complete event or configure the RF Pulse trigger input. The Source Complete event is generated
 after both the configured delay and sourcing operation are complete. In CW mode the setting of
 the RFSG pulse trigger is ignored.

[IMAGE alt='image' src='guid-d815cc33-90f8-4b72-84a2-d0e8e5749f61-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] DCPower Source Delay (s)

Specifies the time, in seconds, between the start of the DC pulse and the generation of
 the Source Complete event. The default value is 0.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFSG Pulse
 Trigger Delay (s)

Specifies the time, in seconds, between when RFSG receives the pulse trigger and when it
 starts generating the pulse. The default value is 0.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure DCPower to RFSG Trigger
 (Manual Routing)

Configures the trigger that synchronizes the RF pulse to the DC pulse. The terminals on
 this VI are used for the DC Source Complete Event Out Terminal and the RFSG Pulse Trigger In
 Terminal. The Source Complete event is generated after both the configured delay and sourcing
 operation are complete. In CW mode the setting of the RFSG pulse trigger is ignored.

[IMAGE alt='image' src='guid-b43e2b32-c290-44d8-9ee6-5dfa194a5565-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFSG Pulse
 Trigger In Terminal

Specifies where to export the signal. The default value is an empty string. An empty
 string means that an RFSG Pulse trigger is not used.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] DCPower Source
 Delay (s)

Specifies the time, in seconds, between the start of the DC pulse and the generation of
 the Source Complete event. The default value is 0.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFSG Pulse
 Trigger Delay (s)

Specifies the time, in seconds, between when RFSG receives the pulse trigger and when it
 starts generating the pulse. The default value is 0.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] DCPower Source Complete Event Out
 Terminal

Specifies where to export the signal. The default value is an empty string. An empty
 string indicates this event is not exported.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-pulse-profile-droop-meas-window.html language=enus -->
## TOPIC 00013: PRFMsc Configure Pulse Profile Droop Measurement Window

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-pulse-profile-droop-meas-window.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-pulse-profile-droop-meas-window.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Profile Droop
 Measurement Window

Configure the window size you can use for the droop measurement.

[IMAGE alt='image' src='guid-22907415-6f20-48d4-8e20-9bfe888fc455-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Droop
 Window Size (%)

Specifies the portion of pulse top to use for the
 computation of droop in percentage. The default value is
 50.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfmx-freq-range-sweep.html language=enus -->
## TOPIC 00014: PRFMsc Configure RFmx Frequency Range Sweep

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfmx-freq-range-sweep.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfmx-freq-range-sweep.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Frequency Range
 Sweep

Defines the frequency range used to measure the device under test. Internally it
 specifies the start and end frequency for the NI RFmx instrument, and uses the same number
 of steps as the Configure RFSG Frequency Range Sweep VI.

[IMAGE alt='image' src='guid-658e78a1-98e7-485c-b570-1b76d466c829-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RFmx Start Frequency (Hz)

Specifies the
 start frequency, in Hz, of the frequency sweep. The default value is 5
 GHz.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RFmx Stop Frequency
 (Hz)

Specifies the stop frequency, in Hz, of the frequency sweep. The
 default value is 6 GHz.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfmx-meas-interval.html language=enus -->
## TOPIC 00015: PRFMsc Configure RFmx Measurement Interval

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfmx-meas-interval.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfmx-meas-interval.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Measurement
 Interval

Specifies the acquisition time, in seconds, for the RF power measurement.

[IMAGE alt='image' src='guid-984019aa-4be4-496d-92e5-88d2c4436154-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RF Measurement Interval (s)

Specifies the
 acquisition time, in seconds, for the measurement. The default value is
 1 ms.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfmx-rbw-parameters.html language=enus -->
## TOPIC 00016: PRFMsc Configure RFmx RBW Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfmx-rbw-parameters.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfmx-rbw-parameters.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx RBW Parameters

Defines the Resolution Bandwidth (RBW) filter to measure the RF power of the signal as
 seen through this filter. Note: the RRC Alpha input is only
 applicable when RBW Filter Type is
 RRC.

[IMAGE alt='image' src='guid-4cc8d5c5-532f-4ab1-8b24-b7fff49d7973-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RBW (Hz)

Specifies the bandwidth, in Hz,
 of the resolution bandwidth (RBW) filter used to measure the signal. The default
 value is 5 MHz.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 RBW Filter Type

Flat

| None (1) | The measurement does not use any RBW filtering. |
| --- | --- |
| Gaussian (2) | The RBW filter has a Gaussian response. |
| Flat (3) | The RBW filter has a flat response. |
| RRC (4) | The RRC filter with the roll-off specified by RRC Alpha parameter is used as the RBW filter. |

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RRC Alpha

Specifies the roll-off factor
 for the root-raised-cosine (RRC) filter. The default value is
 0.1.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfmx-to-dcpower-trigger.html language=enus -->
## TOPIC 00017: PRFMsc Configure RFmx to DCPower Trigger

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfmx-to-dcpower-trigger.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfmx-to-dcpower-trigger.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx to DCPower
 Trigger

Configures the trigger that synchronizes the DCPower measurement to the RFmx
 measurement.

- PRFMsc Configure RFmx to DCPower Trigger (Automatic Routing)
- PRFMsc Configure RFmx to DCPower Trigger (Manual Routing)

#### PRFMsc Configure RFmx to DCPower Trigger
 (Automatic Routing)

When the RF mode is Pulsed CW, this method uses dynamic routing to set the RFmx
 reference trigger as the input to the DCPower measure trigger using an available PXI backplane
 trigger line. When the RF mode is CW, this method does not export the RFmx reference trigger or
 configure a DCPower measure trigger. RFmx exports the reference trigger when it takes a
 measurement. DCPower waits for the measure trigger before taking each measurement.

[IMAGE alt='image' src='guid-5bd0866d-e20b-4f59-9682-fda5290a7dff-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] PAE Reference
 Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFmx to DCPower Trigger
 (Manual Routing)

Configures the trigger to synchronize the DCPower measurement to the RFmx measurement.
 The terminals on this VI are used for the RFmx Reference Trigger Output Terminal and the DCPower
 Measure Trigger Input Terminal terminals. RFmx exports the reference trigger when it takes a
 measurement. DCPower waits for the measure trigger before taking each measurement.

[IMAGE alt='image' src='guid-fe64678f-19db-48dc-b08e-1e4ac909be01-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] DCPower Measure Trigger Input
 Terminal

Specifies the input terminal for the digital edge measure trigger. The default value is
 an empty string. An empty string indicates that no measurement trigger is used.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] PAE Reference
 Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] RFmx Reference Trigger Output
 Terminal

Specifies where to export the selected signal. The default value is Do not
 export signal.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfsg-attenuation.html language=enus -->
## TOPIC 00018: PRFMsc Configure RFSG Attenuation

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfsg-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfsg-attenuation.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Attenuation

Configures the RFSG attenuation type so that the power level at the DUT port is
 corrected to match the same power level set by the PRFMsc Configure RFSG Power
 Level VI.

- PRFMsc Configure RFSG
 Attenuation (Constant).vi
- PRFMsc Configure RFSG
 Attenuation (XML File).vi

#### PRFMsc Configure RFSG Attenuation
 (Constant)

Specifies a single value to compensate for the attenuation on the signal path from VST
 RF out to the ports connected to the DUT.

[IMAGE alt='image' src='guid-bcdf7086-f0b6-48e5-b49a-7f5cb83c2c69-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png'] Path
 Selection

Specifies the path to apply the attenuation setting.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Tx Constant
 Attenuation (dB)

Specifies the constant attenuation value applied to the RFSG session. For example, if the
 attenuation is set to 1 dB and the PRFMsc Configure RFSG Power Level VI
 Power Level (dBm) input is set to 0 dBm, the
 actual power level at the VST RFout port is 1 dBm to compensate for the
 attenuation on the signal path.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Attenuation (XML
 File)

Specifies the attenuation to the RFSG session for the path from VST RF out to the ports
 connected to the DUT. The path is based on the RFSG system calibration XML file created using
 the RF System Calibration Assistant. Use the RF System Calibration Assistant to save multiple
 generator path calibrations in a single XML file. Specify the path to use with the
 RFSG Attenuation Path Name input. Although the RF System Calibration
 Assistant allows you to calibrate one path at multiple power levels for the same frequency, this
 API only supports calibrations done at one power level for each frequency. This function returns
 an error if you do not wire the RFSG XML File Path input or specify an
 empty or relative path.

[IMAGE alt='image' src='guid-4043ae6b-a29a-4f08-b542-34b97c1f145c-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png'] Path
 Selection

Specifies the path to apply the attenuation setting.

##### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png'] RFSG XML File
 Path

Specifies the absolute path to the XML file generated by the RF System Calibration
 Assistant. The default value is empty.

##### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] RFSG
 Attenuation Path Name

Specifies the name of the generator path to use. This path is specified by the XML file
 created with the RF System Calibration Assistant.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfsg-export-trigger.html language=enus -->
## TOPIC 00019: PRFMsc Configure RFSG Export Trigger

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfsg-export-trigger.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfsg-export-trigger.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Export Trigger

Configures the type and source of the trigger to export for each pulse. This
 configuration supports the 2 couplers per port 1 VST with solid state switch setup. If the
 trigger is not configured, or configured for an unsupported setup, no trigger is exported.

- PRFMsc Configure RFSG Export Trigger (None)
- PRFMsc Configure RFSG Export Trigger (Gate)
- PRFMsc Configure RFSG Export Trigger (Pulse)

#### PRFMsc Configure RFSG Export Trigger
 (None)

Configures RFSG to not export a trigger.

[IMAGE alt='image' src='guid-ee7110bb-fb4f-40d2-86e9-1083b30e62c4-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Export Trigger
 (Gate)

Configures RFSG to export a gated trigger, and configures the parameters for the
 trigger.

[IMAGE alt='image' src='guid-53529784-ee3a-4d2d-b489-8bbac412ffcf-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] Trigger Output

Specifies the terminal on which to export a trigger. Enter a valid terminal (PFI0,1,2,3,
 PXI_Trig0-7, PXI_STAR, PXIe_DStarC, or TrigIN) or leave empty. The default value is
 Do not export signal (not set).

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Pre-trigger
 Time (s)

Specifies the time, in seconds, to wait before the rising edge of the pulse to toggle the
 gated trigger as high.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Post-trigger
 Time (s)

Specifies the time, in seconds, to wait after the falling edge of the pulse to toggle the
 gated trigger as low.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Export Trigger
 (Pulse)

Configures RFSG to export a pulse trigger and specifies the terminal on which RFSG
 exports the trigger.

[IMAGE alt='image' src='guid-09a4111f-79d1-4a64-9df7-3d86e6a7bd27-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] Trigger Output

Specifies the terminal on which to export a trigger. Enter a valid terminal (PFI0,1,2,3,
 PXI_Trig0-7, PXI_STAR, PXIe_DStarC, or TrigIN) or leave empty. The default value is
 Do not export signal (not set).

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfsg-freq-range-sweep.html language=enus -->
## TOPIC 00020: PRFMsc Configure RFSG Frequency Range Sweep

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfsg-freq-range-sweep.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfsg-freq-range-sweep.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Frequency Range
 Sweep

Defines the frequency range used to excite the device under test. It is specified by the
 start and stop frequencies and the number of points between the range, linearly spaced.
 Internally it is used to define the NI RFSG frequencies for PAE and PxdB
 measurements.

[IMAGE alt='image' src='guid-c4767466-3283-4fdf-97dc-4b088a8ad00c-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RFSG Start Frequency (Hz)

Specifies the
 start frequency, in Hz, of the frequency sweep. The default value is 5
 GHz.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RFSG Stop Frequency (Hz)

Specifies the
 stop frequency, in Hz, of the frequency sweep. The default value is 6
 GHz.

#### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Number of Frequency
 Steps

Specifies the number of frequency steps to use in the frequency
 sweep. The default values is 5.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfsg-stimulus.html language=enus -->
## TOPIC 00021: PRFMsc Configure RFSG Stimulus

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfsg-stimulus.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfsg-stimulus.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Stimulus

Configures the type of stimulus generated by RFSG.

- PRFMsc Configure RFSG Stimulus (CW)
- PRFMsc Configure RFSG Stimulus (Pulsed CW)

#### PRFMsc Configure RFSG Stimulus (CW)

Configures RFSG to generate a CW signal, and RFmx to measure a CW signal.

[IMAGE alt='image' src='guid-8e80c3f1-55be-4d46-8e62-0b6d091d2684-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] PAE Reference
 Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Stimulus (Pulsed
 CW)

Configures RFSG to generate pulses, and RFmx to measure pulses.

[IMAGE alt='image' src='guid-629b6635-15f8-4fa4-9d59-29ce860961da-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Pulse Width
 (s)

Specifies the pulse width of the baseband signal to generate and measure. The default
 value is 200 us.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] PRI
 (s)

Specifies the pulse repetition interval (PRI) of the baseband signal to generate and
 measure. The default value is 900 us.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] PAE Reference
 Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-rfsg-to-rfmx-trigger.html language=enus -->
## TOPIC 00022: PRFMsc Configure RFSG to RFmx Trigger

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-rfsg-to-rfmx-trigger.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-rfsg-to-rfmx-trigger.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG to RFmx
 Trigger

Configures the trigger that synchronizes the RF measurement with the RF pulse
 generation.

- PRFMsc Configure RFSG to RFmx Trigger (Automatic Routing) (Pulse)
- PRFMsc Configure RFSG to RFmx Trigger (Manual Routing) (Gate)
- PRFMsc Configure RFSG to RFmx Trigger (Manual Routing) (Pulse)

#### PRFMsc Configure RFSG to RFmx Trigger
 (Automatic Routing) (Pulse)

Configures the pulse trigger used for the synchronization. When the RF mode is Pulsed
 CW, this method uses dynamic routing to set the RFSG Pulse Trigger Output as the input to the
 RFmx Trigger using an available PXI backplane trigger line. When the RF mode is CW, this method
 does not export the RFSG Pulse Trigger or configure a RFmx Trigger. In Pulsed CW mode, RFSG
 exports the pulse trigger at the start of each pulse. In CW RF mode, no trigger is exported and
 this setting is ignored. RFmx waits for the measure trigger before taking each measurement.

[IMAGE alt='image' src='guid-25241398-8fba-46cd-bbb3-039db794544e-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFmx Trigger
 Delay (s)

Specifies the time, in seconds, RFmx waits after receiving a reference trigger before
 taking a measurement. The default value is 0.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG to RFmx Trigger
 (Manual Routing) (Gate)

Configures the trigger that synchronizes the RF measurement with the RF pulse
 generation. RFSG exports a gate trigger around the RF pulse. The gate starts the RFSG
 pre-trigger time before the RF pulse, and the gate ends the RFSG post-trigger time after the
 pulse. RFmx only responds to a pulse trigger, so the RFmx reference trigger corresponds to the
 rising edge of the gate.

[IMAGE alt='image' src='guid-78962ec7-1b27-454b-9336-b973402fb980-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] RFmx Reference
 Trigger Input Terminal

Specifies the input terminal for the digital edge trigger. The default value is an empty
 string. An empty strings indicates no trigger is used.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFmx Trigger
 Delay (s)

Specifies the time, in seconds, RFmx waits after receiving a reference trigger before
 taking a measurement. The default value is 0.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFSG
 Pre-trigger Time (s)

Specifies the amount of time, in seconds, that the gate trigger is high before the RF
 pulse starts.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFSG
 Post-trigger Time (s)

The amount of time, in seconds, that the gate trigger remains high after the RF pulse
 stops.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] PAE Reference
 Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] RFSG Pulse Trigger Output Terminal

Specifies where to export the selected signal. The default value is Do not
 export signal.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG to RFmx Trigger
 (Manual Routing) (Pulse)

Configures the trigger that synchronizes the RF measurement with the RF pulse
 generation. A pulse trigger is used for the synchronization. In pulsed CW RF mode RFSG exports
 the pulse trigger at the start of each pulse. In CW RF mode, no pulse trigger is exported and
 this setting is ignored.

[IMAGE alt='image' src='guid-8c115488-843c-4265-86c1-06e6408ab88f-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] RFmx Reference
 Trigger Input Terminal

Specifies the input terminal for the digital edge trigger. The default value is an empty
 string. An empty strings indicates no trigger is used.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] RFmx Trigger Delay (s)

Specifies the time, in seconds, RFmx waits after receiving a reference trigger before
 taking a measurement. The default value is 0.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] RFSG Pulse Trigger Output Terminal

Specifies where to export the selected signal. The default value is Do not
 export signal.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-config-topology.html language=enus -->
## TOPIC 00023: PRFMsc Configure Topology

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-config-topology.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-config-topology.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Topology

Configures the type of NI and third party hardware configuration used to calculate
 S-parameters.

- PRFMsc Configure Topology (1CperPort2VST)
- PRFMsc Configure Topology (2CperPort1VST)
- PRFMsc Configure Topology (1CperPort1VST)
- PRFMsc Configure Topology (1CperPort1VSTS21)
- PRFMsc Configure Topology (S11_1Coupler)
- PRFMsc Configure Topology (S11_2Couplers)
- PRFMsc Configure Topology (2CperPort1VST Solid State Switch)

Refer to the [Electronically Scanned Array Characterization Reference Architecture User
 Manual](https://www.ni.com/r/mmic-user-manual) for details about each topology.

#### PRFMsc Configure Topology
 (1CperPort2VST)

Configures the S-parameter measurement to use two VSTs with one coupler per
 port.

[IMAGE alt='image' src='guid-d416b615-a56f-45e7-96e5-b4c4d4ae61cb-a5.png']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFmx Session Instr 2

Specifies the NI-RFmx session name associated with the VST connected to Port 2 of the DUT. The default value is empty.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFSG Session Instr 2

Specifies the NI-RFSG session name associated with the VST connected to Port 2 of the DUT. The default value is empty.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI RFSG Session Instr 1

Specifies the NI-RFSG session name associated with the VST connected to Port 1 of
 the DUT. The default value is empty.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFmx Session Instr 1

Specifies the NI-RFmx session name associated with the VST connected to Port 1 of the DUT. The default value is empty.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Topology
 (2CperPort1VST)

Configures the S-parameter measurement to use one VST with two couplers per
 port.

[IMAGE alt='image' src='guid-1e18ca7d-b118-470c-a518-a9542350255c-a5.png']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFSG Session

Specifies the name of the NI-RFSG session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFmx Session

Specifies the name of the NI-RFmx session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Switch
 Reference

Specifies the class instance of the switch. Refer to [S-Parameter
 Switching Configuration Class](s-parameter-switching-configuration-class.html) for more information. The default value
 is empty.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Topology
 (1CperPort1VST)

Configures the S-parameter measurement to use one VST with one coupler per
 port.

[IMAGE alt='image' src='guid-844c9e1f-0eb2-4790-8da8-e26f3cf9ea4a-a5.png']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFSG Session

Specifies the name of the NI-RFSG session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFmx Session

Specifies the name of the NI-RFmx session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Switch
 Reference

Specifies the class instance of the switch. Refer to [S-Parameter
 Switching Configuration Class](s-parameter-switching-configuration-class.html) for more information. The default value
 is empty.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Topology
 (1CperPort1VSTS21)

Configures the S21 measurement to use one VST.

[IMAGE alt='image' src='guid-d8fefbda-7bf6-4088-abef-557757c722f7-a5.png']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFSG Session

Specifies the name of the NI-RFSG session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI
 RFmx Session

Specifies the name of the NI-RFmx session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Topology
 (S11_1Coupler)

Configures the S-parameter measurement to use S11 with one coupler.

[IMAGE alt='image' src='guid-99d0b072-25c4-4f54-ac5b-323a14028215-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI RFSG
 Session

Specifies the name of the NI-RFSG session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI RFmx
 Session

Specifies the name of the NI-RFmx session being used. The default value is empty.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Topology
 (S11_2Couplers)

Configures the S-parameter measurement to use S11 with two couplers.

[IMAGE alt='image' src='guid-71c33fc6-8329-47ac-80e7-e2edf1e81288-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI RFSG
 Session

Specifies the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI RFmx
 Session

Specifies the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] Switch
 Reference

Specifies the class instance of the switch. Refer to the [S-Parameter Switching Configuration Class](s-parameter-switching-configuration-class.html) for more information.
 The default value is empty.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Topology (2CperPort1VST
 Solid State Switch)

Configures the S-parameter measurement to use one 1 VST solid state switch with two
 couplers per port.

[IMAGE alt='image' src='guid-ede1d8b2-2646-4603-8c53-cf633f8c4854-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI RFSG
 Session

Specifies the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] NI RFmx
 Session

Specifies the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] Switch
 Reference

Specifies the class instance of the switch. Refer to [S-Parameter Switching
 Configuration Class](s-parameter-switching-configuration-class.html) for more information. The default value is empty.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-averaging.html language=enus -->
## TOPIC 00024: PRFMsc Configure Averaging

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-averaging.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-averaging.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Averaging

Configures the averaging technique used to calculate the S-parameter for the
 instrument.

[IMAGE alt='image' src='guid-2c306730-d366-4c36-aaab-6188768c4dd1-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png']
 Averaging Enabled

Specifies whether averaging is enabled or disabled. The default value is
 FALSE.

| TRUE | Averaging is enabled. |
| --- | --- |
| FALSE | Averaging is disabled. |

#### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png']
 Averaging Count

Specifies the averaging count. When you set the Averaging
 Type parameter to Per Sweep, this value
 defines the number of sweeps. When you set the Averaging
 Type parameter to Per Point, this value
 defines the number of records collected at each frequency step.

#### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png']
 Averaging Type

Specifies the type of averaging to perform. The default value is Per Sweep.

| Per Sweep | Performs the entire sweep as defined by the stimulus parameters for forward direction first, repeats the sweep several times, and then proceeds to do the same for the reverse direction. Data correction is applied and the corrected data for the different sweeps is averaged together. |
| --- | --- |
| Per Point | Collects multiple records for each frequency step defined for the stimulus. Averaging is then applied on the corrected data. |

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-burst-parameters.html language=enus -->
## TOPIC 00025: PRFMsc Configure Burst Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-burst-parameters.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-burst-parameters.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Burst Parameters

Configures the number of pulses to be analyzed in a burst. A burst is defined as a
 collection of pulses. Currently only bursts of uniform pulses with no gaps between bursts
 are supported.

[IMAGE alt='image' src='guid-4ee17d64-bb64-4056-884a-105e70d1258b-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Number
 of Pulses per Burst

Specifies the number of pulses that constitute a burst. The
 default value is 20.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-calibration-method.html language=enus -->
## TOPIC 00026: PRFMsc Configure Calibration Method

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-calibration-method.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-calibration-method.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Calibration Method

Sets the calibration method to use for the S-parameter measurement.

[IMAGE alt='image' src='guid-7b49b9d0-cc46-4ee4-81c2-165f19b41782-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] Calibration
 Method

Specifies the supported calibration method based on the measurement
 topology. The default value is None.

| SOL | Specifies that SOL calibration is performed. This calibration is appropriate for the S11, 1 Coupler measurement topology and the S11, 2 Couplers measurement topology. |
| --- | --- |
| SOLT | Specifies that SOLT calibration is performed. This calibration is appropriate for the 1 Coupler per Port, 1 VST measurement topology or the 1 Coupler Per Port, 2 VSTs measurement topology. |
| SOLR | Specifies that SOLR calibration is performed. This calibration is appropriate for the 2 Couplersper Port, 1 VST measurement topology. |
| QSOLT | Specifies that QSOLT calibration is performed. This calibration is appropriate for the 2 Couplers per Port, 1 VST measurement topology. |
| Through | Specifies that through calibration is performed. This calibration is appropriate for S21 only S-parameter measurements. |
| TRL | Specifies that TRL calibration is performed. This calibration is appropriate for 2 Couplers per Port,1 VST with Solid State Switch measurement topology. |
| None | Specifies not to perform calibration. This method is valid for all measurements. When you specify this method, results are calculated based on raw measurements. |

#### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif'] error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif'] error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-calibration-standards-file-path.html language=enus -->
## TOPIC 00027: PRFMsc Configure Calibration Standards File Paths

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-calibration-standards-file-path.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-calibration-standards-file-path.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Calibration Standards File
 Paths

Configures the locations of the short, open, and load standard characterization files
 that are used in the system-wide calibration.

[IMAGE alt='image' src='guid-73c0aa6f-2a3a-47bf-9f66-42cb72856341-a5.png']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png'] Short
 s1p File Path

Specifies the location of the short s1p file used for calibration. The default value is empty.

#### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png'] Open
 s1p File Path

Specifies the location of the open s1p file used for calibration. The default value is empty.

#### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png'] Load
 s1p File Path

Specifies the location of the load s1p file used for calibration. The default value is empty.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-calibration-through-file.html language=enus -->
## TOPIC 00028: PRFMsc Configure Calibration Through File Path

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-calibration-through-file.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-calibration-through-file.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Calibration Through File
 Path

Configures the location of the through adapter calibration file that is used in the
 system-wide calibration.

[IMAGE alt='image' src='guid-74fb96fd-b519-4719-8165-87a646f15ee4-a5.png']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png']
 Through s2p File Path

Specifies the location of the through s2p file used for calibration. The default value is empty.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-dcpower-measurement-interval.html language=enus -->
## TOPIC 00029: PRFMsc Configure DCPower Measurement Interval

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-dcpower-measurement-interval.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-dcpower-measurement-interval.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure DCPower Measurement
 Interval

Specifies the duration of the voltage and current measurement.

[IMAGE alt='image' src='guid-bf977773-e25a-4b90-ab52-6e963349a23a-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] DCPower Measurement Interval
 (s)

Specifies the duration, in seconds, to measure voltage and
 current. The default value is .02 s. This value is limited by
 the capability of the instrument used. For example, for the PXIe-4130 the
 minimum is 0.00033 s (1 sample to average) and maximum is 0.170333 s (511
 samples to average). For the PXIe-4139, refer to the [PXI Source Measure
 Unit Manual](https://www.ni.com/r/pxie4139) for more details.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-dcpower-pulse-trigger-input.html language=enus -->
## TOPIC 00030: PRFMsc Configure DCPower Pulse Trigger Input

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-dcpower-pulse-trigger-input.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-dcpower-pulse-trigger-input.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure DCPower Pulse Trigger
 Input

Defines the trigger that the DCPower instrument will wait for before generating each
 pulse.

[IMAGE alt='image' src='guid-ebd89682-31eb-495d-89f9-594b0630c96f-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-724cb036-669e-474a-afd6-2043afdda667-a5.gif'] DCPower Pulse
 Trigger Input Terminal

Specifies the input terminal for the digital edge pulse
 trigger. The default value is an empty string. An empty strings indicates no pulse trigger
 is used.

#### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-expected-dut-gain.html language=enus -->
## TOPIC 00031: PRFMsc Configure Expected DUT Gain

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-expected-dut-gain.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-expected-dut-gain.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Expected DUT Gain

Configures the expected gain of the device under test. This information will be used to
 calculate the appropriate level for the acquisition of the transmission power.

[IMAGE alt='image' src='guid-63bbdcc3-4257-40cf-bbf4-081931c16580-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Expected Gain (dB)

Specifies the expected gain, in dB, of the DUT.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-external-gain.html language=enus -->
## TOPIC 00032: PRFMsc Configure External Gain

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-external-gain.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-external-gain.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure External Gain

Configures the maximum gain of all the paths from VST RFout to RFin so you can set the
 appropriate reference level for the measurements.

[IMAGE alt='image' src='guid-17f8f02b-0f08-470f-8211-7d263a043740-a5.png']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif']
 External Gain (dB)

Specifies the expected gain between the generation and analysis ports of the VST(s). This
 value should include attenuation in cabling, couplers, and other signal
 conditioning between the transmission and analysis ports of the VST. The default
 value is -30 dB.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-frequency-range.html language=enus -->
## TOPIC 00033: PRFMsc Configure Frequency Range

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-frequency-range.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-frequency-range.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Frequency Range

Configures the frequency range used for S-parameter measurements.

[IMAGE alt='image' src='guid-caad0b1e-b0e4-4371-89e0-53ad7133ab55-a5.png']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Start
 Frequency (Hz)

Specifies the beginning frequency of the stimulus to be applied to the DUT. The
 default value is 5 GHz.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif']
 Frequency Step (Hz)

Specifies the frequency step size of the stimulus to be applied to the DUT. The
 default value is 50 MHz.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Stop
 Frequency (Hz)

Specifies the ending frequency of the stimulus to be applied to the DUT. The
 default value is 5.5 GHz.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-if-bandwidth.html language=enus -->
## TOPIC 00034: PRFMsc Configure IF Bandwidth

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-if-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-if-bandwidth.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure IF Bandwidth

Configures the IF bandwidth of the measurement.

[IMAGE alt='image' src='guid-375b9656-a8ab-41db-8ae6-f958c44b6dc7-a5.png']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] IF
 Bandwidth (Hz)

Specifies the IF bandwidth of the measurement. When the IF bandwidth is reduced,
 noise taken into the measurement decreases and the measurement time increases.
 The default value is 1 kHz.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-intrapulse-stability-test-points.html language=enus -->
## TOPIC 00035: PRFMsc Configure Intrapulse Stability Test Points (Sampling Window)

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-intrapulse-stability-test-points.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-intrapulse-stability-test-points.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Intrapulse Stability Test
 Points (Sampling Window)

Configures the sampling window used to calculate the reference value for the intrapulse
 stability measurement.

[IMAGE alt='image' src='guid-349ff752-0fbc-4d57-b553-ed888f83e827-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Start Position (%)

Specifies the starting point of the measurement in terms of percent of pulse width. The
 default value is 40.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Window Size (%)

Specifies the duration over which samples are selected to perform the measurement in terms of
 percent of pulse width. The default value is 20.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-parameters.html language=enus -->
## TOPIC 00036: PRFMsc Configure Pulse Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-parameters.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-parameters.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Parameters

Configure the pulse width and pulse repetition interval of the baseband signal. These
 parameters are used for both the pulse generation and the measurement
 configuration.

[IMAGE alt='image' src='guid-888be0df-52f3-4d44-83ae-4843269667b5-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Pulse
 Width (s)

Specifies the pulse width of
 the baseband signal to generate and measure. The default value is 200
 us.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] PRI (s)

Specifies the pulse repetition
 interval (PRI) of the baseband signal to generate and measure. The default value
 is 900 us..

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-profile-disable-period-and-duty-cycle.html language=enus -->
## TOPIC 00037: PRFMsc Configure Pulse Profile Disable Period and Duty Cycle

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-profile-disable-period-and-duty-cycle.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-profile-disable-period-and-duty-cycle.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Profile Disable Period
 and Duty Cycle

Configures whether to measure period and duty cycle. When the period and duty cycle
 measurements are not performed, the off time of the pulse is not stored.

[IMAGE alt='image' src='guid-4881ea6d-dedd-4f21-8242-6d8a0de88543-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Period and Duty Cycle Disabled

Specifies whether to measure the period and duty cycle, where TRUE means LabVIEW
 does not measure period and duty cycle. The default value is 0
 (FALSE).

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-profile-level-settings.html language=enus -->
## TOPIC 00038: PRFMsc Configure Pulse Profile Level Settings

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-profile-level-settings.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-profile-level-settings.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Profile Level
 Settings

Configures how to determine the high and low state levels.

|  | Note: LabVIEW applies the settings specified by this VI only if you choose Percentage as the reference level units on the PRFMsc Configure Pulse Profile Reference Level VI. |
| --- | --- |

[IMAGE alt='image' src='guid-409c9951-d801-4bdb-baba-90082abfd335-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png']
 Method

Specifies how to compute the high and low state levels. The default value is
 Histogram.

| Histogram | Returns the levels of the histogram bins with the maximum number of hits in the upper and lower regions of the waveform. The upper and lower regions of the waveform include the upper and lower 40%, respectively, of the peak-to-peak range of the waveform. |
| --- | --- |
| Peak | Searches the entire waveform for its maximum and minimum levels. |
| Auto-select | Determines whether the histogram bins that correspond to the high and low state levels each have over 5% of the total hits. If so, LabVIEW returns those results. Otherwise, LabVIEW uses the Peak method. This ensures a reasonable answer for either a square wave (ignoring the overshoot and undershoot) or a triangle wave (where a histogram fails). |

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Histogram Size

Specifies the number of bins in the histogram LabVIEW uses to determine the high
 and low state levels of the waveform.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-profile-reference-level.html language=enus -->
## TOPIC 00039: PRFMsc Configure Pulse Profile Reference Level

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-profile-reference-level.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-profile-reference-level.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Profile Reference
 Level

Configures the high, middle, and low reference levels of a pulse waveform. Pulse profile
 reference levels are used to define the measurement interval of one complete cycle. The
 distance between High Reference Level and Mid Reference
 Level must equal the distance between Mid Reference
 Level and Low Reference Level. If the two
 distances are not equal, this VI adjusts either High Reference
 Level or Low Reference Level to match the smaller
 of the two distances. For example, if you set High Reference Level
 to 90%, Mid Reference Level to 50%, and Low Reference
 Level to 20%, this VI adjusts High Reference Level
 to 80%.

[IMAGE alt='image' src='guid-316eb193-1d77-454c-bfc4-63ca95fb4d98-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 High Reference Level

Specifies the high reference level of the waveform in units as specified by
 Reference Level Units. After the signal crosses the
 mid reference level in the rising direction, it must cross the high reference
 level before the next falling mid reference level crossing can be counted. The
 default value is 90.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Mid Reference Level

Specifies the middle reference level in units as specified by
 Reference Level Units. The interval between
 consecutive rising mid reference level crossings defines one cycle, or period,
 of the waveform. At least one high or low reference level crossing must separate
 each mid reference level crossing. The default value is
 50.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Low Reference Level

Specifies the low reference level of the waveform in units as specified by
 Reference Level Units. After the signal crosses the
 mid reference level in the falling direction, it must cross the low reference
 level before the next rising mid reference level crossing can be counted. The
 default value is 10.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png']
 Reference Level Units

Specifies whether the VI interprets the reference level inputs as percentages of
 the full range of the waveform or as absolute units. The absolute unit supported
 by this API is voltage. The default value is Percentage.

| Percentage | The VI interprets the reference level inputs as percentages of the full range of the waveform. |
| --- | --- |
| Absolute | The VI interprets the reference level inputs as voltage. You must wire data to the reference level inputs if you select this option. |

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-stability-averaging.html language=enus -->
## TOPIC 00040: PRFMsc Configure Pulse Stability Averaging

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-stability-averaging.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-stability-averaging.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Stability
 Averaging

Configures the averaging used for pulse stability measurements. If
 Multiburst Averaging Enabled is TRUE, LabVIEW acquires a number
 of bursts equal to the value of Number of Bursts to Average.
 LabVIEW calculates the stability values within each burst and averages the results across
 bursts.

[IMAGE alt='image' src='guid-494cddc1-03b2-4cb9-92ef-a571c4972c35-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Multiburst Averaging Enabled

Specifies whether or not to use multiple bursts to average the pulse stability
 measurements. The default value is 0 (FALSE).

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Number of Burst to Average

Specifies the number of bursts to use when averaging the pulse stability
 measurements. The default value is 10.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-stability-filtering.html language=enus -->
## TOPIC 00041: PRFMsc Configure Pulse Stability Filtering

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-stability-filtering.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-stability-filtering.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Stability
 Filtering

Configures whether to apply a low-pass FIR filter to the pulse stability
 measurement.

|  | Note: LabVIEW applies filters enabled by this VI only to pulse stability measurements. The values you configure with this VI have no effect on pulse profile measurements. |
| --- | --- |

[IMAGE alt='image' src='guid-236ef528-5712-4dd6-ba6e-ae0d58eeaa17-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Filtering Enabled

Specifies whether to pass the acquired data through a low-pass FIR filter before
 performing pulse and intrapulse stability measurements. The default value is
 0 (FALSE).

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Number of Taps

Specifies the number of taps of the filter. The default value is
 60.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-stability-measurement-offset.html language=enus -->
## TOPIC 00042: PRFMsc Configure Pulse Stability Measurement Offset

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-stability-measurement-offset.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-stability-measurement-offset.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Stability Measurement
 Offset

Configures the pulse offset from which to perform the pulse stability measurement.
 For example, if the offset is set to 1, LabVIEW starts the measurement with pulse number 1
 instead of pulse number 0.

[IMAGE alt='image' src='guid-41e7c138-332e-4e98-828c-128de5ce72cc-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Measurement Offset

Specifies the pulse offset from which to start the stability measurement. An
 offset of 0 means the pulse stability measurement uses all pulses. The default
 value is 0.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-pulse-stability-test-points.html language=enus -->
## TOPIC 00043: PRFMsc Configure Pulse Stability Test Points

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-pulse-stability-test-points.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-pulse-stability-test-points.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Pulse Stability Test
 Points

Configure the points at which to measure pulse stability.

- PRFMsc Configure Pulse Stability Test Points (Sampling Window)
- PRFMsc Configure Pulse Stability Test Points (Custom)

#### PRFMsc Configure Pulse Stability Test Points
 (Sampling Window)

Configures a sampling window within which all samples are used to calculate pulse
 stability.

[IMAGE alt='image' src='guid-ac2f473d-81cd-4637-871c-80e6c212d27e-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Start Position (%)

Specifies the starting point of the measurement in terms of percent of pulse width. The
 default value is 40.

##### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Window Size (%)

Specifies the duration over which samples are selected to perform the measurement in terms of
 percent of pulse width. The default value is 20.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Pulse Stability Test Points
 (Custom)

Configures specific points to use to calculate pulse stability.

[IMAGE alt='image' src='guid-713fb9be-a87c-4cae-8db4-2dd59d5a0971-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-322430dd-34cd-42d6-b2d5-4f3c348ab5f5-a5.gif']
 Test Points (%)

Specifies the points, in terms of the percent of the pulse width, on which to
 calculate pulse stability. The default value is an empty array.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rf-power-sweep.html language=enus -->
## TOPIC 00044: PRFMsc Configure RF Power Sweep

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rf-power-sweep.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rf-power-sweep.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RF Power Sweep

Configures the power range and power step size for the RF power sweep applied to the
 device under test.

[IMAGE alt='image' src='guid-edf8c46f-e4a6-48f5-ab71-e07d6ea05aa9-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif']
 Initial Power (dBm)

Specifies the initial power of the RF signal, in
 dBm, to be applied to the DUT. The default is –10
 dBm.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Power Step Size (dB)

Specifies the interval
 between two adjacent samples, in dB, of the RF signal. The default is 1
 dB.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Final
 Power (dBm)

Specifies the final power of the RF signal, in dBm, to be
 applied to the DUT. The default is 0 dBm.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfmx-attenuation-poly.html language=enus -->
## TOPIC 00045: PRFMsc Configure RFmx Attenuation

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfmx-attenuation-poly.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfmx-attenuation-poly.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Attenuation

Defines the path losses between the RF IN connector of the signal analyzer and the
 device under test.

- PRFMsc Configure RFmx Constant Attenuation
- PRFMsc Configure RFmx
 Attenuation (XML File)

#### PRFMsc Configure RFmx Constant
 Attenuation

Specifies a constant loss between the RF IN connector of the signal analyzer and the
 device under test.

[IMAGE alt='image' src='guid-a5146afc-4ed7-4e9d-b032-c7bc2bdeb56f-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFmx Attenuation
 Enabled

Specifies whether RFmx is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RFmx External Attenuation (dB)

Specifies
 the attenuation, in dB, of a switch (or cable) connected to the RF In connector
 of the signal transceiver. For more information about attenuation, refer to the
 "Attenuation and Signal Levels" topic for your device in the NI RF Vector
 Signal Analyzers Help. The default value is
 0.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFmx Attenuation (XML
 File)

Specifies the absolute path to the RF system calibration XML file created using the RF
 System Calibration Assistant. Use the RF System Calibration Assistant to save multiple
 analyzer path calibrations in a single xml file. Specify the path to use with the
 RFmx Attenuation Path Name input. Although the RF System
 Calibration Assistant allows you to calibrate one path at multiple reference levels for the
 same frequency, this API supports calibrations done at only one reference level for each
 frequency. This function returns an error if you do not wire the RFmx XML File
 Path input or specify an empty or relative path.

[IMAGE alt='image' src='guid-29b89f2d-eff4-4282-b470-4e725c2e4624-a5.png']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFmx Attenuation
 Enabled

Specifies whether RFmx is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png']
 RFmx XML File Path

Specifies the absolute path to the XML file
 generated by the RF System Calibration Utility. The default value is
 empty.

##### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] RFmx Attenuation Path
 Name

Specifies the name of the analyzer path to use. This path is
 specified by the XML file created with the RF System Calibration
 Assistant.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfmx-attenuation-pulse.html language=enus -->
## TOPIC 00046: PRFMsc Configure RFmx Attenuation

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfmx-attenuation-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfmx-attenuation-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Attenuation

Defines the path losses between the RF IN connector of the signal analyzer and the
 device under test.

- PRFMsc Configure RFmx
 Constant Attenuation
- PRFMsc Configure RFmx
 Attenuation (XML File)

#### PRFMsc Configure RFmx Attenuation
 (Constant)

Specifies a single value to compensate for external attenuation at all frequencies and
 reference levels.

[IMAGE alt='image' src='guid-b0e7a279-7ba8-482c-ac5f-4fc1dcffc46f-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFmx Attenuation
 Enabled

Specifies whether RFmx is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RFmx Constant Attenuation (dB)

Specifies the
 constant attenuation value to apply when RFmx Attenuation
 Enabled is TRUE. The default value is
 0.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFmx Attenuation (XML
 File)

Specifies the absolute path to the RF system calibration XML file created using the RF
 System Calibration Assistant. Use the RF System Calibration Assistant to save multiple
 analyzer path calibrations in a single xml file. Specify the path to use with the
 RFmx Attenuation Path Name input. Although the RF System
 Calibration Assistant allows you to calibrate one path at multiple reference levels for the
 same frequency, this API supports calibrations done at only one reference level for each
 frequency. This function returns an error if you do not wire the RFmx XML File
 Path input or specify an empty or relative path.

[IMAGE alt='image' src='guid-c6d3f124-bd55-4f37-bca1-9d52c8606f6a-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFmx Attenuation
 Enabled

Specifies whether RFmx is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png']
 RFmx XML File Path

Specifies the absolute path to the XML file
 generated by the RF System Calibration Utility. The default value is
 empty.

##### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] RFmx Attenuation Path
 Name

Specifies the name of the analyzer path to use. This path is
 specified by the XML file created with the RF System Calibration
 Assistant.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfmx-center-frequency.html language=enus -->
## TOPIC 00047: PRFMsc Configure RFmx Center Frequency

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfmx-center-frequency.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfmx-center-frequency.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Center
 Frequency

Configures the center frequency of the receiver.

[IMAGE alt='image' src='guid-116ef7fc-01f3-49e5-a66b-ef91ef0582b3-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Center Frequency (Hz)

Specifies the
 center frequency of the RF signal to be acquired. The default value is
 5.5 GHz.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfmx-measurement-bandwidth.html language=enus -->
## TOPIC 00048: PRFMsc Configure RFmx Measurement Bandwidth

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfmx-measurement-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfmx-measurement-bandwidth.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Measurement
 Bandwidth

Configures the measurement bandwidth of the receiver. This VI sets the sampling rate
 as 1.25 times the value of Measurement Bandwidth (Hz). Sample rate should
 be an integer multiple of pulse repetition frequency (reciprocal of pulse repetition
 interval), so that the sampling locations of pulses are the same.

|  | Note: NI recommends setting the Measurement Bandwidth input to at least 10 divided by the pulse width. |
| --- | --- |

[IMAGE alt='image' src='guid-763a9004-f425-4bd4-9639-0879ec68315f-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Measurement Bandwidth (Hz)

Specifies the expected measurement bandwidth of the received signal. The measurement
 bandwidth is used to set the IQ rate of the acquisition instrument. The default value is
 2 MHz. The minimum setting should be 10 times the pulse width.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfmx-reference-level.html language=enus -->
## TOPIC 00049: PRFMsc Configure RFmx Reference Level

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfmx-reference-level.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfmx-reference-level.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Reference Level

Configures the mximum expected power, in dBm, of an input RF signal.

[IMAGE alt='image' src='guid-244a0524-96cd-4003-928e-3cb406c1524e-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Reference Level (dBm)

Configures the maximum
 expected power of an input RF signal. The default value is 0
 dBm.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfmx-trigger.html language=enus -->
## TOPIC 00050: PRFMsc Configure RFmx Trigger

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfmx-trigger.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfmx-trigger.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFmx Trigger

PRFMsc Configure RFSG Export
 Trigger Mode

[IMAGE alt='image' src='guid-36f3358f-1114-4b30-a7b9-84b926eabad8-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png']
 Acquisition Trigger Source

Specifies the terminal on which the RFmx instrument looks for a trigger. The
 default value is PXI_Trig0.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Pretrigger Time (s)

Specifies how long before the trigger to start capturing samples. Use this input
 to acquire the full first transition of the first pulse. The default value is
 0.

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png']
 Trigger Delay (s)

Specifies how long the RFmx device waits after, or before in the case of a
 negative value, receiving the trigger before acknowledging it. Use this input to
 align the trigger to the start of the top of the pulse. The default value is
 0.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-attenuation-poly-pulse.html language=enus -->
## TOPIC 00051: PRFMsc Configure RFSG Attenuation

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-attenuation-poly-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-attenuation-poly-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Attenuation

Defines the path losses between the RF OUT connector of the signal generator and the
 input of the device under test.

- PRFMsc Configure RFSG
 Constant Attenuation
- PRFMsc Configure RFSG
 Attenuation (XML File)

#### PRFMsc Configure RFSG Attenuation
 (Constant)

Specifies a single value to compensate for external attenuation at all frequencies and
 power levels.

[IMAGE alt='image' src='guid-c2085441-e122-4adb-b370-08eb3ee4dac6-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFSG Attenuation
 Enabled

Specifies whether RFSG is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif']
 RFSG Constant Attenuation (dB)

Specifies the constant attenuation value to apply when RFSG Attenuation
 Enabled is TRUE. The default value is 0.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Attenuation (XML
 File)

Specifies the absolute path to the RFSG system calibration XML file created using the
 RF System Calibration Assistant. Use the RF System Calibration Assistant to save multiple
 generator path calibrations in a single xml file. Specify the path to use with the
 RFSG Attenuation Path Name input. Although the RF System
 Calibration Assistant allows you to calibrate one path at multiple power levels for the same
 frequency, this API only supports calibrations done at one power level for each frequency.
 This function returns an error if you do not wire the RFSG XML File
 Path input or specify an empty or relative path.

[IMAGE alt='image' src='guid-c6dd5a83-618e-4371-a97f-09e2fc6d012b-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFSG Attenuation
 Enabled

Specifies whether RFSG is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png']
 RFSG XML File Path

Specifies the absolute path to the XML file
 generated by the RF System Calibration Utility. The default value is
 empty.

##### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] RFSG Attenuation Path
 Name

Specifies the name of the generator path to use. This path is
 specified by the XML file created with the RF System Calibration
 Assistant.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-attenuation-poly.html language=enus -->
## TOPIC 00052: PRFMsc Configure RFSG Attenuation

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-attenuation-poly.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-attenuation-poly.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Attenuation

Defines the path losses between the RF OUT connector of the signal generator and the
 input of the device under test.

- PRFMsc Configure RFSG
 Constant Attenuation
- PRFMsc Configure RFSG
 Attenuation (XML File)

#### PRFMsc Configure RFSG Constant
 Attenuation

Specifies a single value to compensate for external attenuation at all frequencies and
 power levels.

[IMAGE alt='image' src='guid-2abdddc9-3bc1-4905-8e5a-94529e427e3d-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFSG Attenuation
 Enabled

Specifies whether RFSG is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] RFSG External Attenuation
 (dB)

Specifies the attenuation, in dB, of a switch (or cable)
 connected to the RF Out connector of the signal transceiver. For more
 information about attenuation, refer to the "Attenuation and Signal Levels"
 topic for your device in the NI RF Vector Signal Analyzers Help.
 The default value is 0.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Attenuation (XML
 File)

Specifies the absolute path to the RFSG system calibration XML file created using the RF
 System Calibration Assistant. Use the RF System Calibration Assistant to save multiple
 generator path calibrations in a single xml file. Specify the path to use with the
 RFSG Attenuation Path Name input. Although the RF System
 Calibration Assistant allows you to calibrate one path at multiple power levels for the same
 frequency, this API only supports calibrations done at one power level for each frequency.
 This function returns an error if you do not wire the RFSG XML File
 Path input or specify an empty or relative path.

[IMAGE alt='image' src='guid-c6dd5a83-618e-4371-a97f-09e2fc6d012b-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] RFSG Attenuation
 Enabled

Specifies whether RFSG is configured to compensate for
 external attenuation. The default value is
 False.

##### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png']
 RFSG XML File Path

Specifies the absolute path to the XML file
 generated by the RF System Calibration Utility. The default value is
 empty.

##### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] RFSG Attenuation Path
 Name

Specifies the name of the generator path to use. This path is
 specified by the XML file created with the RF System Calibration
 Assistant.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-center-frequency-pulse.html language=enus -->
## TOPIC 00053: PRFMsc Configure RFSG Center Frequency

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-center-frequency-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-center-frequency-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Center
 Frequency

Configures the center frequency of the RF signal.

[IMAGE alt='image' src='guid-116ef7fc-01f3-49e5-a66b-ef91ef0582b3-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Center Frequency
 (Hz)

Specifies the center frequency of the RF signal to generate. The
 default value is 5.5 GHz.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-export-trigger-mode.html language=enus -->
## TOPIC 00054: PRFMsc Configure RFSG Export Trigger Mode

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-export-trigger-mode.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-export-trigger-mode.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Export Trigger
 Mode

Configures how often the signal generator sends a trigger and how often the signal
 analyzer waits for a trigger. The trigger can be sent with every pulse or every burst (a
 collection of pulses).

[IMAGE alt='image' src='guid-269cd8e8-fa86-472f-bd42-932b748a6706-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png'] Trigger
 Mode

Trigger Per Pulse

| Trigger per Pulse | The trigger is generated in the form of a marker at the beginning of every pulse in the burst. |
| --- | --- |
| Trigger per Burst | The trigger is generated in the form of a marker at the beginning of the starting pulse of a burst. |

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-export-trigger-poly.html language=enus -->
## TOPIC 00055: PRFMsc Configure RFSG Export Trigger

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-export-trigger-poly.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-export-trigger-poly.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Export Trigger

Configures the type and source of the trigger to export.

- PRFMsc Configure RFSG
 Export Trigger (None)
- PRFMsc
 Configure RFSG Export Trigger (Pulse)
- PRFMsc
 Configure RFSG Export Trigger (Gate)

#### PRFMsc Configure RFSG Export Trigger
 (None)

Configures RFSG to not export a trigger.

[IMAGE alt='image' src='guid-40f048e8-fc8a-4da6-ad36-65da4bc752ae-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Export Trigger
 (Pulse)

Configures RFSG to export a pulse trigger and specifies the terminal on which RFSG
 exports the trigger.

[IMAGE alt='image' src='guid-92db5392-9e73-4ec0-a831-c7a70d69cc62-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] External Trigger
 Destination

Specifies the terminal on which to export a trigger. Enter a valid terminal (PFI0,1,2,3,
 PXI_Trig0-7, PXI_STAR, PXIe_DStarC, or TrigIN) or leave empty. The default value
 is Do not export signal (not set).

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure RFSG Export Trigger
 (Gate)

Configures RFSG to export a gate trigger and configures the parameters for the trigger.

[IMAGE alt='image' src='guid-7607f478-4716-45d8-a3fe-f0e9e6d5dec2-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] External Trigger
 Destination

Specifies the terminal on which to export a trigger. Enter a valid terminal (PFI0,1,2,3,
 PXI_Trig0-7, PXI_STAR, PXIe_DStarC, or TrigIN) or leave empty. The default value
 is Do not export signal (not set).

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Export Pre-trigger Time (s)

Specifies the
 time, in seconds, to wait before the start of the pulse or burst signal to start
 the gate trigger. The default value is 0.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Export
 Post-trigger Time (s)

Specifies the time, in seconds, to wait after
 the end of the pulse or burst signal to end the gate trigger. The default value
 is 0.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-import-trigger.html language=enus -->
## TOPIC 00056: PRFMsc Configure RFSG Import Trigger

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-import-trigger.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-import-trigger.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Import Trigger

Configures the signal generator to wait for a trigger from an external DUT setup before
 generating each pulse or burst, depending on the value set with the PRFMsc
 Configure RFSG Export Trigger Mode VI Trigger Mode
 input. This VI also configures the trigger source and trigger delay for the Reference
 Digital Edge Trigger if a trigger is used.

[IMAGE alt='image' src='guid-a546dcff-426d-426d-9504-8618c44945fa-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png'] Import
 Trigger

Specifies whether RFSG waits for an external trigger before
 generating a pulse or burst signal. The default value is
 None.

| None | RFSG generates a signal without waiting for an external trigger to occur. |
| --- | --- |
| External | RFSG waits for an external trigger before generating a signal. |

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] External Trigger
 Source

Specifies the terminal on which the RFSG looks for a trigger
 when the Import Trigger input is set to
 External. Enter a valid terminal (PFI0,1,2,3,
 PXI_Trig0-6, PXI_STAR, PXIe_DStarB, or TrigOut) or leave empty. The default
 value is empty (not set).

#### [IMAGE alt='image' src='guid-cfaaa37d-7713-4be6-abbe-68a61b52f8f4-a5.png'] Trigger Delay
 (s)

Specifies the duration, in seconds, to wait after receiving a
 trigger before generating a signal. The default value is
 0.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-power-level-pulse.html language=enus -->
## TOPIC 00057: PRFMsc Configure RFSG Power Level

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-power-level-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-power-level-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Power Level

Configures the power level of the pulse to generate.

[IMAGE alt='image' src='guid-7888d81d-d9af-4be6-b4d9-f59a632e0883-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Power
 Level (dBm)

Specifies the power level of the RF signal to generate. The default value is
 0 dBm.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-power-level.html language=enus -->
## TOPIC 00058: PRFMsc Configure RFSG Power Level

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-power-level.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-power-level.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Power Level

Configures the power level used to calculate the S-parameter measurement.

[IMAGE alt='image' src='guid-00e920f3-58c2-4311-8c28-7fcee54e11bd-a5.png']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Power
 Level (dBm)

Specifies the power level of the RF signal to generate. The default value is
 0 dBm.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-rfsg-sample-rate.html language=enus -->
## TOPIC 00059: PRFMsc Configure RFSG Sample Rate

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-rfsg-sample-rate.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-rfsg-sample-rate.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure RFSG Sample Rate

Configures the IQ rate of the baseband waveform to be generated. When an external
 trigger is sent to the NI-RFSG, there is a delay between the time the trigger is received and
 the time the signal is generated. This delay increases with lower IQ rates. Sample rate should
 be an integer multiple of pulse repetition frequency (reciprocal of pulse repetition
 interval), so that the sampling locations of pulses are the same.

|  | Note: NI recommends setting the Sample Rate input to the maximum value supported by the device. |
| --- | --- |

[IMAGE alt='image' src='guid-6d6bddac-4355-49b0-b3ca-596af7637f82-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Sample Rate (S/s)

Specifies the IQ Rate of the RF signal to generate. The default value is 1.25
 GS/s.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

|  | Note: When an external trigger is sent to the NI-RFSG, there is a delay between the time the trigger is received and the time the signal is generated. This delay increases with lower IQ rates. NI recommends setting the RFSG Sample Rate to the maximum value supported by the device |
| --- | --- |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-stimulus-poly.html language=enus -->
## TOPIC 00060: PRFMsc Configure Stimulus

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-stimulus-poly.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-stimulus-poly.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Stimulus

Defines the type of RF signal used to stimulate the DUT.

- PRFMsc
 Configure Stimulus (CW)
- PRFMsc
 Configure Stimulus (Pulsed CW)

#### PRFMsc Configure Stimulus (CW)

Defines the stimulus as a continuous wave.

[IMAGE alt='image' src='guid-3320aa49-8f19-4531-9d04-25e3113f7cfd-a5.png']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Configure Stimulus (Pulsed CW)

Defines the stimulus as a pulsed continuous wave and configures the wave.

[IMAGE alt='image' src='guid-f80fac9f-2ce9-40f9-9c3b-38e6fe19c985-a5.png']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] Pulse
 Width (s)

Specifies the pulse width. The default value is 10 us.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] PRI
 (s)

Specifies the pulse repetition interval (PRI). The default value is 1
 ms.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-configure-trl-calibration.html language=enus -->
## TOPIC 00061: PRFMsc Configure TRL Calibration

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-configure-trl-calibration.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-configure-trl-calibration.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure TRL Calibration

Configures options for TRL calibration.

[IMAGE alt='image' src='guid-cbecee4f-f2c7-42fe-90fc-6f747e0c90db-a5.gif']

|  | S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. |
| --- | --- |
|  | TRL Calibration Configuration Specifies configuration options for TRL calibration. Reflection Type Specifies the type of reflection to use for the reflection step. Short: Performs the reflection step with a short standard. Open: Performs the reflection step with an open standard. Line Delays Specifies the delay of the lines used for the calibration, in ps. Up to two delay lines are supported. If more than two delays are specified, the calibration errors out. |
|  | Reflection Type Specifies the type of reflection to use for the reflection step. Short: Performs the reflection step with a short standard. Open: Performs the reflection step with an open standard. |
|  | Short: Performs the reflection step with a short standard. |
|  | Open: Performs the reflection step with an open standard. |
|  | Line Delays Specifies the delay of the lines used for the calibration, in ps. Up to two delay lines are supported. If more than two delays are specified, the calibration errors out. |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | S-Par Reference Out Returns the session reference handle of the S-parameter measurement session. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-averaged-power.html language=enus -->
## TOPIC 00062: PRFMsc Fetch Averaged Power

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-averaged-power.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-averaged-power.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Averaged Power

Fetches the averaged RF power and the averaged DC power of the measurement.

[IMAGE alt='image' src='guid-0f8f1814-0d01-41ad-8714-c0799abec540-a5.gif']

|  | PAE Reference In Specifies the reference name of the PAE measurement session. |
| --- | --- |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PAE Reference Out Returns the reference name of the PAE measurement session. |
|  | Averaged RF Power Returns a 1D array of plots of RF power at DUT output port against RF power at DUT input port. Each plot in the array corresponds to one frequency in the frequency sweep. Input Power Returns the RF Input power applied at the DUT input port. Average RF Power Returns the averaged RF power measured at the DUT output port. |
|  | Input Power Returns the RF Input power applied at the DUT input port. |
|  | Average RF Power Returns the averaged RF power measured at the DUT output port. |
|  | Averaged DC Power Returns a 1D array of plots of DC power against the RF power at the DUT input port. Each plot in the array corresponds to one frequency in the frequency sweep. Input Power Returns the RF Input power applied at the DUT input port. Average DC Power Returns the averaged DC power provided to the DUT. |
|  | Input Power Returns the RF Input power applied at the DUT input port. |
|  | Average DC Power Returns the averaged DC power provided to the DUT. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-data.html language=enus -->
## TOPIC 00063: PRFMsc Fetch Data

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-data.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-data.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Data

Fetches the stored data in the reference in different formats.

- PRFMsc Fetch Data (Pulse IQ)
- PRFMsc Fetch Data (Pulse Magnitude Phase)
- PRFMsc Fetch Data (Burst IQ)
- PRFMsc Fetch Data (All)
- PRFMsc Fetch Data (Array of Pulses)
- PRFMsc Fetch Data (Array of Bursts)

#### PRFMsc Fetch Data (Pulse IQ)

Fetches complex-valued IQ data for the Pulse Number you specify
 within the Burst Number.

[IMAGE alt='image' src='guid-8c2be3ff-680e-4068-a048-107b8f811f31-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Burst Number

Specifies the burst to fetch. The value can be between 0 and the value you specify in the
 Number of Burst to Average parameter in the
 PRFMsc Configure Pulse Stability Averaging VI. The
 default value is 0.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Pulse Number

Specifies the pulse to be fetched in the burst you specify. The default value is 0.

##### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] Type of Data

Unfiltered

| Unfiltered | The type of data fetched is unfiltered. |
| --- | --- |
| Filtered | The type of data fetched is filtered. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-806ed314-26c3-46cb-95a3-39184b081642-a5.gif'] Pulse IQ Data

Returns the complex valued IQ data of the pulse.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Data (Pulse Magnitude
 Phase)

Fetches the magnitude and phase data for the pulse you specify in Burst
 Number and Pulse Number.

[IMAGE alt='image' src='guid-4cc5fe75-47ae-44e4-9af2-41986eddd0c0-a5.png']

##### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] Type of Data

Unfiltered

| Unfiltered | The type of data fetched is unfiltered. |
| --- | --- |
| Filtered | The type of data fetched is filtered. |

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Burst Number

Specifies the burst to fetch. The value can be between 0 and the value you specify in the
 Number of Burst to Average parameter in the
 PRFMsc Configure Pulse Stability Averaging VI. The
 default value is 0.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Pulse Number

Specifies the pulse to be fetched in the burst you specify. The default value is 0.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Unit

Specifies which unit to be used for the burst amplitude. The default value is Power (dBm).

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-806ed314-26c3-46cb-95a3-39184b081642-a5.gif'] Pulse
 Magnitude

Returns the amplitude waveform of the pulse.

##### [IMAGE alt='image' src='guid-806ed314-26c3-46cb-95a3-39184b081642-a5.gif'] Pulse Phase

Returns the phase waveform of the pulse.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Data (Burst IQ)

Fetches complex-valued IQ data for the burst number you specify in Burst
 Number.

[IMAGE alt='image' src='guid-5ce09085-2e7b-4169-ad5f-8ee74c2c8dde-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Burst Number

Specifies the burst to fetch. The value can be between 0 and the value you specify in the
 Number of Burst to Average parameter in the
 PRFMsc Configure Pulse Stability Averaging VI. The
 default value is 0.

##### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] Type of Data

Unfiltered

| Unfiltered | The type of data fetched is unfiltered. |
| --- | --- |
| Filtered | The type of data fetched is filtered. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-806ed314-26c3-46cb-95a3-39184b081642-a5.gif'] Burst IQ Data

Returns the complex valued IQ data of the burst.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Data (Burst Magnitude
 Phase)

Fetches the magnitude and phase data of the IQ data for the burst number you specify in
 Burst Number.

[IMAGE alt='image' src='guid-52c3882a-6630-4520-9f7a-5078368be4da-a5.png']

##### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] Type of Data

Unfiltered

| Unfiltered | The type of data fetched is unfiltered. |
| --- | --- |
| Filtered | The type of data fetched is filtered. |

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Burst Number

Specifies the burst to fetch. The value can be between 0 and the value you specify in the
 Number of Burst to Average parameter in the
 PRFMsc Configure Pulse Stability Averaging VI. The
 default value is 0.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Unit

Specifies which unit to be used for the burst amplitude. The default value is Power (dBm).

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-806ed314-26c3-46cb-95a3-39184b081642-a5.gif'] Burst
 Magnitude

Returns the amplitude waveform of the burst.

##### [IMAGE alt='image' src='guid-806ed314-26c3-46cb-95a3-39184b081642-a5.gif'] Burst Phase

Returns the phase waveform of the burst.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Data (All)

Averaging Count

[IMAGE alt='image' src='guid-f04366cc-028f-4460-af8a-ad22eab43975-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] Type of Data

Unfiltered

| Unfiltered | The type of data fetched is unfiltered. |
| --- | --- |
| Filtered | The type of data fetched is filtered. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-806ed314-26c3-46cb-95a3-39184b081642-a5.gif'] All IQ Data

Returns a complex valued IQ data waveform of all bursts.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Data (Array of Pulses)

Fetches complex-valued IQ data for all the bursts as specified by the
 Averaging Count parameter in the Configure Pulse Stability
 Averaging VI. The output waveform is a 2D array of waveform datatype, where element at index
 (0,0) corresponds to Burst_0, Pulse_0, element at index (0,n-1) corresponds to Burst_0,
 Pulse_(n-1) element at index (1,0) corresponds to Burst_1, Pulse 0 Index ((m-1),(n-1)) of
 the array corresponds to Burst_(m-1), Pulse_(n-1).

[IMAGE alt='image' src='guid-7ff28b27-0500-46be-8c1c-114ac7c7c2af-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] Type of Data

Unfiltered

| Unfiltered | The type of data fetched is unfiltered. |
| --- | --- |
| Filtered | The type of data fetched is filtered. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-e415f110-a59b-4853-b5be-f08d612737b2-a5.gif'] Array of Pulse IQ Data

Returns a 2D array of pulse IQ data waveforms.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Data (Array of Bursts)

Fetches complex-valued IQ data for all the bursts as specified by the
 Averaging Count parameter in the Configure Pulse Stability
 Averaging VI. The output waveform is an array of waveform datatype, where each element in
 the array corresponds to the data for a particular burst. Index 0 of the array corresponds
 to all pulses in Burst_0 and Index (m-1) of the array corresponds to all pulses in the
 burst.

[IMAGE alt='image' src='guid-5d593c55-a73e-4d8e-b7a7-b17a198cf5c1-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] Type of Data

Unfiltered

| Unfiltered | The type of data fetched is unfiltered. |
| --- | --- |
| Filtered | The type of data fetched is filtered. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-4c84ad5d-c23c-4d41-aa02-b95605d63cde-a5.png'] Array of Burst IQ Data

Returns an array of burst IQ data waveforms.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-gains.html language=enus -->
## TOPIC 00064: PRFMsc Fetch Gains

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-gains.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-gains.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Gains

Fetches the gain of the DUT as function of the frequency and input power.

[IMAGE alt='image' src='guid-8cec1bc4-4930-4707-9ada-778ca2d93043-a5.gif']

|  | PAE Reference In Specifies the reference name of the PAE measurement session. |
| --- | --- |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PAE Reference Out Returns the reference name of the PAE measurement session. |
|  | Gain (Linear Range) Per Frequency Returns the gain versus frequency plot. The gain is calculated using measurements where the RF power at the DUT input port is less than Maximum Linear Range (dBm). Frequency Levels (Hz) Returns the frequency of the measurement. Gain (Linear Range) Returns the gain of the DUT averaged over all measurements within the DUTs linear range. |
|  | Frequency Levels (Hz) Returns the frequency of the measurement. |
|  | Gain (Linear Range) Returns the gain of the DUT averaged over all measurements within the DUTs linear range. |
|  | Gain Returns a 1D array of plots of gain versus RF power at the DUT input port. Each plot corresponds to one frequency in the frequency sweep. Input Power Returns the RF Input power applied at the DUT input port. Gain Returns the gain of the DUT. |
|  | Input Power Returns the RF Input power applied at the DUT input port. |
|  | Gain Returns the gain of the DUT. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-intrapulse-stability.html language=enus -->
## TOPIC 00065: PRFMsc Fetch Intrapulse Stability

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-intrapulse-stability.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-intrapulse-stability.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Intrapulse Stability

Fetches the intrapulse stability results.

You can select from the following instances of this VI:

- PRFMsc Fetch Intrapulse Stability (Index)
- PRFMsc Fetch Intrapulse Stability (All)
- PRFMsc Fetch Intrapulse Stability (Trace)

#### PRFMsc Fetch Intrapulse Stability
 (Index)

Fetches the intrapulse stability results for a specific pulse.

[IMAGE alt='image' src='guid-b0517624-54c2-4790-9238-f3169dc6adaf-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Pulse
 Number

Specifies the pulse number in a burst for which the intrapulse measurement is
 retrieved. The default value is 0.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Intrapulse Amplitude Stability (dB)

Returns the intrapulse amplitude stability per sample point for the specified pulse averaged over all bursts.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Intrapulse Phase Stability (dB)

Returns the intrapulse phase stability per sample point for the specified pulse averaged over all bursts.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Intrapulse Total Stability (dB)

Returns the intrapulse total stability per sample point for the specified pulse averaged over all bursts.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Sample Points

Returns the time from the start of the top of the pulse to where the sample point was measured. This value is expressed in seconds.

#### PRFMsc Fetch Intrapulse Stability
 (All)

Fetches the intrapulse stability results for all pulses.

[IMAGE alt='image' src='guid-2f89ba67-5883-42c3-a825-43dc228a44d8-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-65c6c5cf-c434-4fa8-9bbe-ba71f2aaa2f0-a5.gif']
 Intrapulse Amplitude Stability (dB)

Returns the intrapulse amplitude stability per sample point for the specified pulse averaged over all bursts. The row corresponds to the pulse number and the column corresponds to the sample point.

##### [IMAGE alt='image' src='guid-65c6c5cf-c434-4fa8-9bbe-ba71f2aaa2f0-a5.gif']
 Intrapulse Phase Stability (dB)

Returns the intrapulse phase stability per sample point for the specified pulse averaged over all bursts. The row corresponds to the pulse number and the column corresponds to the sample point.

##### [IMAGE alt='image' src='guid-65c6c5cf-c434-4fa8-9bbe-ba71f2aaa2f0-a5.gif']
 Intrapulse Total Stability (dB)

Returns the intrapulse total stability per sample point for the specified pulse averaged over all bursts. The row corresponds to the pulse number and the column corresponds to the sample point.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Sample Points

Returns the time from the start of the top of the pulse to where the sample point was measured. This value is expressed in seconds.

#### PRFMsc Fetch Intrapulse Stability
 (Trace)

Fetches the intrapulse stability results for a particular pulse.

[IMAGE alt='image' src='guid-cb20d9ac-5fb7-428a-afaa-2d644fd8aded-a5.gif']

|  | Pulse Reference In Specifies the reference name of the Pulse measurement session. |
| --- | --- |
|  | Pulse Number Specifies the pulse number in a burst for which the intrapulse measurement is retrieved. The default value is 0. |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Pulse Reference Out Returns the reference name of the Pulse measurement session. |
|  | Intrapulse Amplitude Stability Returns a cluster of test point and amplitude stability arrays. Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. Amplitude Stability (dB) Returns an array containing intrapulse amplitude stability for a single pulse per test point averaged over all bursts. |
|  | Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. |
|  | Amplitude Stability (dB) Returns an array containing intrapulse amplitude stability for a single pulse per test point averaged over all bursts. |
|  | Intrapulse Phase Stability Returns a cluster of test point and phase stability arrays. Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. Phase Stability (dB) Returns an array containing intrapulse phase stability for a single pulse per test point averaged over all bursts. |
|  | Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. |
|  | Phase Stability (dB) Returns an array containing intrapulse phase stability for a single pulse per test point averaged over all bursts. |
|  | Intrapulse Total Stability Returns a cluster of test point and total stability arrays. Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. Total Stability (dB) Returns an array containing intrapulse total stability for a single pulse per test point averaged over all bursts. |
|  | Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. |
|  | Total Stability (dB) Returns an array containing intrapulse total stability for a single pulse per test point averaged over all bursts. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-pae.html language=enus -->
## TOPIC 00066: PRFMsc Fetch PAE

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-pae.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-pae.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch PAE

Fetches the PAE results.

- PRFMsc Fetch PAE
 (All)
- PRFMsc Fetch PAE (Trace)

#### PRFMsc Fetch PAE (All)

Fetches the PAE in a tabulated format.

[IMAGE alt='image' src='guid-9462d035-21bb-4bad-b4cd-8b45abb6830d-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error
 in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-65c6c5cf-c434-4fa8-9bbe-ba71f2aaa2f0-a5.gif'] Power Added Efficiency (%)

Returns the result of the PAE measurement for all power and frequencies. This parameter
 returns a 2D array where the row index defines the applied frequency and the column index
 defines the input power.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png'] Frequencies

Returns the list of frequencies used to excite the DUT.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png'] Input Power

Returns the list of input powers (RFSG Power) used to excite the DUT.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch PAE (Trace)

Fetches the PAE in a trace format.

[IMAGE alt='image' src='guid-0576ee55-4fb8-4052-9019-f8bb333587b4-a5.gif']

|  | PAE Reference In Specifies the reference name of the PAE measurement session. |
| --- | --- |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PAE Reference Out Returns the reference name of the PAE measurement session. |
|  | Power Added-Efficiency Returns the result of the PAE measurements for all power and frequencies. This parameter returns a 1D array of XY graphs with the PAE value against the input powers. The index of the 1D array defines the applied frequency. Input Power Returns the RF Input power applied at the DUT input port. PAE Returns the PAE at the corresponding input power level. |
|  | Input Power Returns the RF Input power applied at the DUT input port. |
|  | PAE Returns the PAE at the corresponding input power level. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-pulse-profile-amplitude.html language=enus -->
## TOPIC 00067: PRFMsc Fetch Pulse Profile Amplitude

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-pulse-profile-amplitude.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-pulse-profile-amplitude.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Pulse Profile Amplitude

Fetches the pulse amplitude, state levels, droop, and ripple results. The results are
 returned as 1D arrays where the array index corresponds to the pulse number.

[IMAGE alt='image' src='guid-efae2c48-ffa5-4ea2-b1d4-b18e72ba7a38-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif']
 Level Unit

Specifies the units you can use for returning the amplitude results. The default value is Power (dBm).

#### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif']
 Ripple and Droop Unit

Specifies the units you can use for returning the ripple and droop results. The default value is Percentage (%).

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Amplitude

Returns the difference between High State Level and Low State Level.

#### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 High State Level

Returns the level at which a pulse or transition waveform is defined to be in its highest state.

#### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Low State Level

Returns the level at which a pulse or transition waveform is defined to be in its lowest state.

#### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Droop

Returns the difference in height between the point at the start of the pulse top to the end of the pulse top on a straight line fit to the top of the pulse.

#### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Ripple

Returns the difference between the point furthest above and furthest below a straight line fit to the top of the pulse.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-pulse-profile-transition.html language=enus -->
## TOPIC 00068: PRFMsc Fetch Pulse Profile Transition

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-pulse-profile-transition.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-pulse-profile-transition.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Pulse Profile Transition

Fetches the transition measurement results.

- PRFMsc Fetch Pulse Profile Transition (Rising Edge)
- PRFMsc Fetch Pulse Profile Transition (Falling Edge)

#### PRFMsc Fetch Pulse Profile Transition (Rising
 Edge)

Retrieves the transition measurement results for the rising edge of the
 pulse.

[IMAGE alt='image' src='guid-26373266-2b69-4f57-a27c-62dc6d8ad4d5-a5.gif']

|  | Pulse Reference In Specifies the reference name of the Pulse measurement session. |
| --- | --- |
|  | Overshoot and Undershoot Unit Specifies the unit you can use to represent the overshoot and undershoot measurements. The default value is Percentage (%). |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Pulse Reference Out Returns the reference name of the Pulse measurement session. |
|  | Pre-transition Undershoot Returns the height of the local minimum preceding a transition. |
|  | Post-transition Undershoot Returns the height of the local minimum following a transition. |
|  | Transition Duration (s) Returns the duration from when the waveform crosses the low ref level to when it crosses the high ref level. This value is expressed in seconds. |
|  | Pre-transition Overshoot Returns the height of the local maximum preceding a transition. |
|  | Post-transition Overshoot Returns the height of the local maximum following a transition. |
|  | measurement info Returns the transition interval end points and the absolute reference levels used to define the transition. Start Time Returns time of the rising low ref level crossing that defines the start of the transition. Stop Time Returns time of the rising high ref level crossing that defines the end of the transition. ref levels Returns the user-defined reference levels of the waveform in absolute units. high ref level Returns the high reference level. mid ref level Returns the middle reference level. low ref level Returns the low reference level. ref units is always absolute in measurement info. Slope Returns a measure of the rate of change of the signal in a transition region between high ref level and low ref level. |
|  | Start Time Returns time of the rising low ref level crossing that defines the start of the transition. |
|  | Stop Time Returns time of the rising high ref level crossing that defines the end of the transition. |
|  | ref levels Returns the user-defined reference levels of the waveform in absolute units. high ref level Returns the high reference level. mid ref level Returns the middle reference level. low ref level Returns the low reference level. ref units is always absolute in measurement info. |
|  | high ref level Returns the high reference level. |
|  | mid ref level Returns the middle reference level. |
|  | low ref level Returns the low reference level. |
|  | ref units is always absolute in measurement info. |
|  | Slope Returns a measure of the rate of change of the signal in a transition region between high ref level and low ref level. |
|  | error out Error information. This output provides standard error out functionality. |

#### PRFMsc Fetch Pulse Profile Transition
 (Falling Edge)

Retrieves the transition measurement results for the falling edge of the
 pulse.

[IMAGE alt='image' src='guid-22355df2-1b03-4036-b44a-6120c3f580f5-a5.gif']

|  | Pulse Reference In Specifies the reference name of the Pulse measurement session. |
| --- | --- |
|  | Overshoot and Undershoot Unit Specifies the unit you can use to represent the overshoot and undershoot measurements. The default value is Percentage (%). |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Pulse Reference Out Returns the reference name of the Pulse measurement session. |
|  | Pre-transition Undershoot Returns the height of the local minimum preceding a transition. |
|  | Post-transition Undershoot Returns the height of the local minimum following a transition. |
|  | Transition Duration (s) Returns the duration from when the waveform crosses the high ref level to when it crosses the low ref level. This value is expressed in seconds. |
|  | Pre-transition Overshoot Returns the height of the local maximum preceding a transition. |
|  | Post-transition Overshoot Returns the height of the local maximum following a transition. |
|  | measurement info Returns the transition interval end points and the absolute reference levels used to define the transition. Start Time Returns time of the falling high ref level crossing that defines the start of the transition. Stop Time Returns time of the falling low ref level crossing that defines the end of the transition. ref levels Returns the user-defined reference levels of the waveform in absolute units. high ref level Returns the high reference level. mid ref level Returns the middle reference level. low ref level Returns the low reference level. ref units is always absolute in measurement info. Slope Returns a measure of the rate of change of the signal in a transition region between high ref level and low ref level. |
|  | Start Time Returns time of the falling high ref level crossing that defines the start of the transition. |
|  | Stop Time Returns time of the falling low ref level crossing that defines the end of the transition. |
|  | ref levels Returns the user-defined reference levels of the waveform in absolute units. high ref level Returns the high reference level. mid ref level Returns the middle reference level. low ref level Returns the low reference level. ref units is always absolute in measurement info. |
|  | high ref level Returns the high reference level. |
|  | mid ref level Returns the middle reference level. |
|  | low ref level Returns the low reference level. |
|  | ref units is always absolute in measurement info. |
|  | Slope Returns a measure of the rate of change of the signal in a transition region between high ref level and low ref level. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-pulse-profile-width.html language=enus -->
## TOPIC 00069: PRFMsc Fetch Pulse Profile Width

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-pulse-profile-width.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-pulse-profile-width.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Pulse Profile Width

Retrieves the period, duration, duty cycle, and other results related to the pulse
 width. The results are returned as 1D arrays where the array index corresponds to the
 pulse number.

[IMAGE alt='image' src='guid-d779e3e4-8804-4ea4-b2fb-e45c895b4db2-a5.gif']

|  | Pulse Reference In Specifies the reference name of the Pulse measurement session. |
| --- | --- |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Pulse Reference Out Returns the reference name of the Pulse measurement session. |
|  | Period (s) Returns the duration between adjacent mid ref level crossings in the same direction. This value is expressed in seconds. The reciprocal of this value is the pulse frequency. |
|  | Pulse Duration (s) Returns the difference in time between the first two mid ref level crossings of the pulse. This value is expressed in seconds. Pulse duration is also defined as pulse width. |
|  | Duty Cycle (%) Returns a fraction of the period specified by the quotient of Pulse Duration parameter divided by Period multiplied by 100. Duty cycle is also defined as duty factor. |
|  | measurement info Returns the pulse center time of the selected pulse and the absolute reference levels used to define the measurement cycle. pulse center Returns the time instant of the midpoint of the pulse. ref levels Returns the user-defined reference levels of the waveform in absolute units. high ref level Returns the high reference level. mid ref level Returns the middle reference level. low ref level Returns the low reference level. ref units is always absolute in measurement info. |
|  | pulse center Returns the time instant of the midpoint of the pulse. |
|  | ref levels Returns the user-defined reference levels of the waveform in absolute units. high ref level Returns the high reference level. mid ref level Returns the middle reference level. low ref level Returns the low reference level. ref units is always absolute in measurement info. |
|  | high ref level Returns the high reference level. |
|  | mid ref level Returns the middle reference level. |
|  | low ref level Returns the low reference level. |
|  | ref units is always absolute in measurement info. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-pulse-stability.html language=enus -->
## TOPIC 00070: PRFMsc Fetch Pulse Stability

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-pulse-stability.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-pulse-stability.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch Pulse Stability

Fetches the pulse stability results.

You can select from the following instances of this VI:

- PRFMsc Fetch Pulse Stability (All)
- PRFMsc Fetch Pulse Stability (Average)
- PRFMsc Fetch Pulse Stability (Trace)

#### PRFMsc Fetch Pulse Stability (All)

Fetches the pulse stability results per Test Point averaged
 over all pulses and bursts.

[IMAGE alt='image' src='guid-98b46e73-76eb-4fc6-8af8-43e27291a1cb-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Pulse Amplitude Stability (dB)

Returns the amplitude stability per Test Point averaged over all
 pulses/bursts.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Pulse Phase Stability (dB)

Returns the phase stability per Test Point averaged over all
 pulses/bursts.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Pulse Total Stability (dB)

Returns the total stability per Test Point averaged over all
 pulses/bursts.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Test Points

Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Pulse Stability
 (Average)

Fetches the pulse stability results averaged over all pulses, bursts, and test
 points.

[IMAGE alt='image' src='guid-1df63d88-cab5-46e3-b082-7e5971828af2-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Average Amplitude Stability (dB)

Returns the amplitude stability per test point averaged over all test points, pulses, and
 bursts.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Average Phase Stability (dB)

Returns the phase stability per test point averaged over all test points, pulses, and
 bursts.

##### [IMAGE alt='image' src='guid-389b1e48-8bde-43a5-ada1-ba89172e053a-a5.png']
 Average Total Stability (dB)

Returns the total stability per test point averaged over all test points, pulses, and
 bursts.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch Pulse Stability (Trace)

Test Point

[IMAGE alt='image' src='guid-616295e2-a692-4a85-94ed-0bfae9fae436-a5.gif']

|  | Pulse Reference In Specifies the reference name of the Pulse measurement session. |
| --- | --- |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Pulse Reference Out Returns the reference name of the Pulse measurement session. |
|  | Pulse Amplitude Stability Returns a cluster of test point and amplitude stability arrays. Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. Amplitude Stability Returns an array containing amplitude stability per Test Point averaged over all pulses/bursts. |
|  | Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. |
|  | Amplitude Stability Returns an array containing amplitude stability per Test Point averaged over all pulses/bursts. |
|  | Pulse Phase Stability Returns a cluster of test point and phase stability arrays. Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. Phase Stability Returns an array containing phase stability per Test Point averaged over all pulses/bursts. |
|  | Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. |
|  | Phase Stability Returns an array containing phase stability per Test Point averaged over all pulses/bursts. |
|  | Pulse Total Stability Returns a cluster of test point and total stability arrays. Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. Total Stability Returns an array containing total stability per Test Point averaged over all pulses/bursts. |
|  | Test Points Returns the time from the start of the top of the pulse to when the test point was measured. This value is expressed in seconds. |
|  | Total Stability Returns an array containing total stability per Test Point averaged over all pulses/bursts. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-pxdb.html language=enus -->
## TOPIC 00071: PRFMsc Fetch PxdB

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-pxdb.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-pxdb.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch PxdB

Fetches the PxdB results.

- PRFMsc Fetch PxdB (All)
- PRFMsc Fetch PxdB
 (Trace)

#### PRFMsc Fetch PxdB (Trace)

Fetches the compression power at x dB (PxdB) in a trace format.

[IMAGE alt='image' src='guid-e5f7fbf9-d1df-40f1-ace2-234cff4b1e50-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif'] PxdB Not Found
 Value

Specifies the value to be returned when the PxdB value is not found. The default value is
 0.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] PAE Reference
 Out

Returns the session reference handle of the PAE measurement session.

##### [IMAGE alt='image' src='guid-2153ef9a-0403-4388-a342-11c3eef58623-a5.png'] Power Output at
 PxdB

Returns the output power when the DUT is in compression of PxdB over a frequency
 range.

##### [IMAGE alt='image' src='guid-2153ef9a-0403-4388-a342-11c3eef58623-a5.png'] Power Input at
 PxdB

Returns the input power when the DUT is in compression of PxdB over a frequency
 range.

##### [IMAGE alt='image' src='guid-2153ef9a-0403-4388-a342-11c3eef58623-a5.png'] PxdB Not
 Found

Returns the value you specify in the PxdB Not Found Value parameter,
 indicating that this VI could not find the PxdB over a frequency range.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch PxdB (All)

Fetches the compression power at x dB (PxdB) in a tabulated format.

[IMAGE alt='image' src='guid-a9179113-96c1-458a-a008-5253672af097-a5.gif']

|  | PAE Reference In Specifies the reference name of the PAE measurement session. |
| --- | --- |
|  | error in Error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PAE Reference Out Returns the reference name of the PAE measurement session. |
|  | Output Power Returns the RF power measured for the DUT on the last measured frequency. |
|  | Input Power Returns the RF Input power applied at the DUT input port for the last measured frequency. |
|  | PxdB Results Returns the measured PxdB results. This parameter returns a 1D array that contains Pin@PxdB, Pout@PxdB, PxdB Found, Gain (linear range), and Frequency level (Hz). Pin@PxdB Returns the input power at the PxdB. This value is expressed in dBm. Pout@PxdB Returns the output power at the PxdB. This value is expressed in dBm. PxdB Found Indicates whether the algorithm encountered the PxdB. TRUE The algorithm encountered the PxdB. FALSE The algorithm did not encounter the PxdB. Gain (linear range) Returns the calculated gain for linear range. Frequency Level (Hz) Returns the obtained frequency. |
|  | Pin@PxdB Returns the input power at the PxdB. This value is expressed in dBm. |
|  | Pout@PxdB Returns the output power at the PxdB. This value is expressed in dBm. |
|  | PxdB Found Indicates whether the algorithm encountered the PxdB. TRUE The algorithm encountered the PxdB. FALSE The algorithm did not encounter the PxdB. |
| TRUE | The algorithm encountered the PxdB. |
| FALSE | The algorithm did not encounter the PxdB. |
|  | Gain (linear range) Returns the calculated gain for linear range. |
|  | Frequency Level (Hz) Returns the obtained frequency. |
|  | error out Error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-fetch-s-parameters-poly.html language=enus -->
## TOPIC 00072: PRFMsc Fetch S-Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-fetch-s-parameters-poly.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-fetch-s-parameters-poly.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Fetch S-Parameters

Fetches the calculated S-parameter measurement.

You can select from the following instances of this VI:

- PRFMsc Fetch S-Parameters (Mag-Phase)
- PRFMsc Fetch
 S-Parameters (Complex)
- PRFMsc Fetch
 S-Parameters (All Complex)

#### PRFMsc Fetch S-Parameters (Mag-Phase)

Fetches the frequency, magnitude, and phase of a single S-parameter
 measurement.

[IMAGE alt='image' src='guid-e23adacc-6074-437e-b6c1-c34ac73b82f5-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png'] S-Parameter Selection

Specifies which S-parameter measurement the VI fetches. The default value is
 S11.

| S11 | Specifies the S11 S-parameter measurement. |
| --- | --- |
| S21 | Specifies the S21 S-parameter measurement. |
| S12 | Specifies the S12 S-parameter measurement. |
| S22 | Specifies the S22 S-parameter measurement. |

##### [IMAGE alt='image' src='guid-d1915a5d-aa77-474c-ac0e-99bcb14aee37-a5.png'] Magnitude
 Format

Specifies the format of the magnitude for the given S-parameter
 measurement. The default value is Log Magnitude
 (dB).

| Log Magnitude | Specifies that the Magnitude output returns the magnitude of the given S-parameter measurement in log magnitude, in units of dB. |
| --- | --- |
| Lin Magnitude | Specifies that the Magnitude output returns the magnitude of the given S-parameter measurement in linear magnitude. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] Magnitude

Returns the magnitude of the specified S-parameter. This value is expressed in
 units as defined by the Magnitude Format input.

##### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] Phase

Returns the phase of the specified S-parameter. This value is expressed in
 degrees.

##### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] Frequency (Hz)

Returns the frequency of the specified S-parameter. This value is expressed in
 Hz.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch S-Parameters (Complex)

Fetches the frequency and the complex number of a single S-parameter
 measurement.

[IMAGE alt='image' src='guid-0d03a3e7-1eec-47de-99b0-d5a320db5b33-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png'] S-Parameter Selection

Specifies which S-parameter measurement the VI fetches. The default value is
 S11.

| S11 | Specifies the S11 S-parameter measurement. |
| --- | --- |
| S21 | Specifies the S21 S-parameter measurement. |
| S12 | Specifies the S12 S-parameter measurement. |
| S22 | Specifies the S22 S-parameter measurement. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-592d4b8c-d3ea-4be2-8428-944248b68100-a5.gif'] S-Parameters

Returns a single S-parameter measurement. This value is expressed as a complex
 number.

##### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] Frequency (Hz)

Returns the frequency of the specified S-parameter. This value is expressed in
 Hz.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Fetch S-Parameters (All
 Complex)

Fetches all S-parameters in a measurement.

[IMAGE alt='image' src='guid-1435b7cd-e9bb-46a0-9c1a-abb424a5fb2e-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-985b77c5-012e-4ce8-93ac-0f507657725e-a5.gif'] S-Parameters

Returns all four S-parameter measurements, expressed as a 2D array of complex
 numbers. Each row of the 2D array is the S-parameter at a frequency point,
 corresponding to the element at the same array index of the
 Frequency (Hz) output. The columns of the 2D array
 are ordered as S11, S21, S12 and S22.

##### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] Frequency (Hz)

Returns the frequency of the specified S-parameter. This value is expressed in
 Hz.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-calibration-actions.html language=enus -->
## TOPIC 00073: PRFMsc Get Calibration Actions

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-calibration-actions.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-calibration-actions.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Calibration Actions

PRFMsc Calibrate S-Parameters

[IMAGE alt='image' src='guid-c57e511a-48f8-4b7a-a39e-19b539f9298c-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-4f5a3976-3bf6-4697-b33e-171d54dc47ff-a5.png'] Calibration
 Actions

Returns the calibration actions, expressed as an array of
 strings to perform. Wire this output to the PRFMsc Calibrate
 S-Parameters VI.

SOLR or SOLT Calibration (1 Coupler per
 port, 2 VST and 1 Coupler per Port, 1 VST):

| String | Description |
| --- | --- |
| Port 1: Short | Performs and stores the Short measurements for Port 1. |
| Port 1: Open | Performs and stores the Open measurements for Port 1. |
| Port 1: Load | Performs and stores the Load measurements for Port 1. |
| Port 2: Short | Performs and stores the Short measurements for Port 2. |
| Port 2: Open | Performs and stores the Open measurements for Port 2. |
| Port 2: Load | Performs and stores the Load measurements for Port 2. |
| Through | Performs and stores the Through measurements. |
| Calculate | Calculates the error coefficients based on the measurements done by the previous actions. |

QSOLT Calibration (2 Couplers per Port, 1 VST):

| String | Description |
| --- | --- |
| Port 1: Short | Performs and stores the Short measurements for Port 1. |
| Port 1: Open | Performs and stores the Open measurements for Port 1. |
| Port 1: Load | Performs and stores the Load measurements for Port 1. |
| Through | Performs and stores the Through measurements. |
| Calculate | Calculates the error coefficients based on the measurements done by the previous actions. |

Through Calibration (S21 Only, 1 VST):

| String | Description |
| --- | --- |
| Through | Performs and stores the Through measurements. |
| Calculate | Calculates the error coefficients based on the measurements done by the previous actions. |

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-calibration-meas.html language=enus -->
## TOPIC 00074: PRFMsc Get Calibration Measurement

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-calibration-meas.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-calibration-meas.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Calibration Measurement

SOLT Measurements

TRL Measurements

[IMAGE alt='image' src='guid-1cfa4e99-cd91-4d06-a752-ee838a2a43f9-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-2153ef9a-0403-4388-a342-11c3eef58623-a5.png'] SOLT Measurements

Returns raw calibration measurements for SOLT, SOLR and QSOLT
 calibration.

| String | Description |
| --- | --- |
| Port 1 SOL | Returns the Short, Open, Load measurements for port 1. For 1 coupler per port there are three test coupler measurements, and for 2 couplers per port there is 1 test coupler measurement and 1 reference coupler measurement for each standard. |
| Port 2 SOL | Returns the Short, Open, Load measurements for port 2. For 1 coupler per port there are three test coupler measurements, and for 2 couplers per port there is 1 test coupler measurement and 1 reference coupler measurement for each standard. |
| Through | Returns the Through measurements for SOLT, SOLR and QSOLT calibration methods. For 1 coupler per port there are 2 test coupler measurements for each direction (forward and reverse), and for 2 couplers per port there is 1 test coupler measurement and 1 reference coupler measurement for each direction (forward and reverse). |

#### [IMAGE alt='image' src='guid-2153ef9a-0403-4388-a342-11c3eef58623-a5.png'] TRL Measurements

Returns raw calibration measurements for TRL calibration.

| String | Description |
| --- | --- |
| Port 1 Reflection | Returns Reflection measurements for port 1. There is 1 test coupler measurement and 1 reference coupler measurement. |
| Port 2 Reflection | Returns Reflection measurements for port 2. There is 1 test coupler measurement and 1 reference coupler measurement. |
| Through | Returns Through measurements for TRL calibration methods. There is 1 test coupler measurement and 1 reference coupler measurement for each direction (forward and reverse). |
| Lines | Returns a measurement array for 2 ports with multiple delay lines. There is 1 test coupler measurement and 1 reference coupler measurement for each direction (forward and reverse) for each element in the array. |

#### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-calibration-status.html language=enus -->
## TOPIC 00075: PRFMsc Get Calibration Status

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-calibration-status.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-calibration-status.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Calibration Status

Fetches the calibration status of S-Parameter measurements, including whether
 calibration was performed on the measurement, and the timestamp when calibration was
 performed.

[IMAGE alt='image' src='guid-00dbf1b7-df25-4c4a-a582-ca4c9bb9ee7c-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-6c052875-af23-479b-922b-ca1c3c4d5ab3-a5.png']
 Calibrated

Returns whether calibration was performed on the measurement.

#### [IMAGE alt='image' src='guid-54b09eec-f3cd-4463-b10f-05229f66f2cc-a5.gif'] Calibration
 Timestamp

Returns the timestamp of the last calibration date.

#### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-frequency-iteration.html language=enus -->
## TOPIC 00076: PRFMsc Get Frequency for Iteration

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-frequency-iteration.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-frequency-iteration.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Frequency for Iteration

Gets the specific frequency that you apply in the iteration based on the index value.
 The index value is specified based on the calculations of the power and frequency
 sweep.

[IMAGE alt='image' src='guid-e02adc2e-c105-422b-8a8a-5e3aa06a2b83-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] Loop Iteration Index

Specifies the index used to calculate the power/frequency that is applied to RFSG and
 RFmx. This value is, in general, specified by the iteration terminal (i) of the
 For Loop.

#### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] NI RFSG Frequency (Hz)

Returns the frequency that you should apply to NI RFSG for the specific iteration.

#### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] NI RFmx Frequency (Hz)

Returns the frequency that you should apply to NI RFmx for the specific iteration.

#### [IMAGE alt='image' src='guid-7c113a24-bb55-42d9-9194-618975c5ea4c-a5.png'] Frequency Iteration Index

Returns the index used to obtain the frequency value from the list of frequencies to be
 applied.

#### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] Frequency Iteration Fraction

Returns the equivalent of the index value expressed as a decimal scaled between 0 and
 1.

#### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-nidcpower-session.html language=enus -->
## TOPIC 00077: PRFMsc Get NIDCPower Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-nidcpower-session.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-nidcpower-session.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get NIDCPower Session

Returns the NI-DCPower instrument session used by the PAE measurement
 session.

[IMAGE alt='image' src='guid-ddf0e352-c323-4681-9383-e4ab9d421009-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-7991e30a-0772-4e6b-9a80-7fe8b20b90b4-a5.png'] NI DCPower Instrument Handle

Returns a reference to the NI-DCPower instrument session used for the
 measurement.

#### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] NI DCPower Channel Name

Returns the name of the NI-DCPower channel(s) used for the measurement.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-nirfmx-session-pulse.html language=enus -->
## TOPIC 00078: PRFMsc Get NIRFmx Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-nirfmx-session-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-nirfmx-session-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get NIRFmx Session

Returns the NI-RFmx instrument session used by the pulse measurement
 session.

[IMAGE alt='image' src='guid-8d06d94a-3b1b-4fa5-ad34-efb3b4c7ac55-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-7991e30a-0772-4e6b-9a80-7fe8b20b90b4-a5.png'] NI RFmx Instrument Handle

Returns a reference to the NI-RFmx instrument session used for the
 measurement.

#### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] NI RFmx Port

Returns the name of the NI-RFmx port used for the measurement.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-nirfmx-session.html language=enus -->
## TOPIC 00079: PRFMsc Get NIRFmx Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-nirfmx-session.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-nirfmx-session.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get NIRFmx Session

Returns the NI-RFmx instrument session used by the PAE measurement session.

[IMAGE alt='image' src='guid-87808549-8c65-4b0d-ba19-bc2caf7657b7-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-7991e30a-0772-4e6b-9a80-7fe8b20b90b4-a5.png'] NI RFmx Instrument Handle

Returns a reference to the NI-RFmx instrument session used for the
 measurement.

#### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] NI RFmx Port

Returns the name of the NI-RFmx port used for the measurement.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-nirfsg-session-pulse.html language=enus -->
## TOPIC 00080: PRFMsc Get NIRFSG Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-nirfsg-session-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-nirfsg-session-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get NIRFSG Session

Returns the NI-RFSG instrument session used by the pulse measurement
 session.

[IMAGE alt='image' src='guid-1afb420e-4db7-4ca5-a740-caf4040d3e3c-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-7991e30a-0772-4e6b-9a80-7fe8b20b90b4-a5.png'] NI RFSG Instrument Handle

Returns a reference to the NI-RFSG instrument session used for the
 measurement.

#### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] NI RFSG Port

Returns the name of the NI-RFSG port used for the measurement.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-nirfsg-session.html language=enus -->
## TOPIC 00081: PRFMsc Get NIRFSG Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-nirfsg-session.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-nirfsg-session.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get NIRFSG Session

Returns the NI-RFSG instrument session used by the PAE measurement session.

[IMAGE alt='image' src='guid-62b6662d-8665-41db-9ebc-8a17cc34de42-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-7991e30a-0772-4e6b-9a80-7fe8b20b90b4-a5.png'] NI RFSG Instrument Handle

Returns a reference to the NI-RFSG instrument session used for the
 measurement.

#### [IMAGE alt='image' src='guid-c38e40b9-0a37-472c-8bd9-94fc19b54727-a5.png'] NI RFSG Port

Returns the name of the NI-RFSG port used for the measurement.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-number-of-iteration.html language=enus -->
## TOPIC 00082: PRFMsc Get Number of Iterations

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-number-of-iteration.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-number-of-iteration.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Number of Iterations

Gets the number of iterations necessary to calculate the PAE and PxdB calculations
 through the sweep by power and sweep by frequency.

[IMAGE alt='image' src='guid-04c21aef-3220-4e99-96be-7421562166db-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-7c113a24-bb55-42d9-9194-618975c5ea4c-a5.png']
 Total Number of Iterations

Returns the number of iterations required to sweep all power and frequencies. This value is specified as the number of iterations for power multiplied by the number of iterations for frequency.

#### [IMAGE alt='image' src='guid-7c113a24-bb55-42d9-9194-618975c5ea4c-a5.png']
 Number of Iterations for Power

Returns the number of iterations necessary to sweep all power values.

#### [IMAGE alt='image' src='guid-7c113a24-bb55-42d9-9194-618975c5ea4c-a5.png']
 Number of Iterations for Frequency

Returns the number of iterations necessary to sweep all frequency values.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-number-of-iterations-pulse.html language=enus -->
## TOPIC 00083: PRFMsc Get Number of Iterations

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-number-of-iterations-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-number-of-iterations-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Number of Iterations

Returns the number of measurements and the number of records per measurement. Use the
 outputs of this VI to determine how many times to call the PRFMsc
 Measure VI.

[IMAGE alt='image' src='guid-4380bf05-8822-4a5b-97bb-0fbfbac2bceb-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-7c113a24-bb55-42d9-9194-618975c5ea4c-a5.png'] Number of Measurements

Returns the number of separate measurements in the measurement session. Start the
 measurements by calling an RFmx Initiate VI for each.

#### [IMAGE alt='image' src='guid-7c113a24-bb55-42d9-9194-618975c5ea4c-a5.png'] Number of Records per Measurement

Returns the number of records in each measurement.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### Example

Refer to the PRFMsc Pulse Measurements VI at
 labview\examples\PRFMsc\PRFMsc Pulse Measurements.vi for an
 example of using the PRFMsc Get Number of Iterations VI.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-get-power-for-iteration.html language=enus -->
## TOPIC 00084: PRFMsc Get Power for Iteration

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-get-power-for-iteration.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-get-power-for-iteration.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Power for Iteration

Gets the specific power that you apply in the iteration based on the index value. The
 index value is specified based on the calculations of the power and frequency
 sweep.

[IMAGE alt='image' src='guid-5687c333-c371-4954-b7c2-cf5e3ea246d1-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE Reference
 In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] Loop Iteration Index

Specifies the index used to calculate the power/frequency that is applied to RFSG and
 RFmx. This value is, in general, specified by the iteration terminal (i) of the
 For Loop.

#### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] NI RFSG Power (dBm)

Returns the power that you should apply to NI RFSG for the specific iteration.

#### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] NI RFmx Power (dBm)

Returns the power that you should apply to NI RFmx for the specific iteration.

#### [IMAGE alt='image' src='guid-7c113a24-bb55-42d9-9194-618975c5ea4c-a5.png'] Power Iteration Index

Returns the index used to obtain the power value from the list of powers to be
 applied.

#### [IMAGE alt='image' src='guid-73666ac7-0c1e-415a-8c0f-caecb2fe820f-a5.png'] Power Iteration Fraction

Returns the equivalent of the index value expressed as a decimal scaled between 0 and
 1.

#### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-initialize-measurement-pae.html language=enus -->
## TOPIC 00085: PRFMsc Initialize Measurement

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-initialize-measurement-pae.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-initialize-measurement-pae.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Initialize Measurement

Initializes a PRFMsc PAE session for the session name that you specify in the
 Session Name parameter and returns a session reference handle
 that identifies the session in all subsequent PRFMsc VIs.

[IMAGE alt='image' src='guid-03c0630b-a4bd-4261-8dac-b6c189920b7b-a5.gif']

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] Session Name

Specifies a unique measurement name. For multiple measurements within the same process, the
 name must be unique.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session created by this VI.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-initialize-measurement-pulse.html language=enus -->
## TOPIC 00086: PRFMsc Initialize Measurement

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-initialize-measurement-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-initialize-measurement-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Initialize Measurement

Creates a PRFMsc Pulse session for the session name that you specify in the
 Session Name parameter and returns a session reference handle
 that identifies the session in all subsequent PRFMsc VIs.

[IMAGE alt='image' src='guid-c30032f0-a85b-46a1-9cbf-30bb3015bbc3-a5.gif']

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] Session Name

Specifies a unique measurement name. For multiple measurements within the same process, the
 name must be unique.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session created by this VI.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-initialize-measurement.html language=enus -->
## TOPIC 00087: PRFMsc Initialize Measurement

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-initialize-measurement.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-initialize-measurement.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Initialize Measurement

Initializes a PRFMsc S-parameter session for the session name that you specify in the Session Name parameter and returns a session reference handle that identifies the session in all subsequent PRFMsc VIs.

[IMAGE alt='image' src='guid-a44f4853-8dec-4c23-b4b8-34f40a6af14a-a5.png']

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] Session Name

Specifies a unique measurement name. For multiple measurements within the same process, the
 name must be unique.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session created by this VI.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-load-cal-parameters.html language=enus -->
## TOPIC 00088: PRFMsc Load Calibration Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-load-cal-parameters.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-load-cal-parameters.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Load Calibration Parameters

PRFMsc Save Calibration Parameters

[IMAGE alt='image' src='guid-a416f83e-609f-4962-992f-7cfc4bc4579a-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png'] Calibration Parameters File Path

Specifies
 the location of the calibration parameters file. The default value is
 empty.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-measure-pae.html language=enus -->
## TOPIC 00089: PRFMsc Measure

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-measure-pae.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-measure-pae.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Measure

PAE reference

[IMAGE alt='image' src='guid-e8b969dc-2913-4e59-9259-d4234c857190-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif']
 Loop Iteration Index

Specifies the index used to calculate the power/frequency that is applied to RFSG and RFmx. This
 value is, in general, specified by the iteration terminal (i) of the
 For Loop.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif']
 Measured RF Power

Specifies the RF power that was measured with the RFmx TXP measurement. This value is expressed in dBm.

#### [IMAGE alt='image' src='guid-96b98364-aa14-483a-b456-99448ec4bdab-a5.gif']
 Measured DC Power

Specifies the measured DC Power defined by the current and voltage measured by the SMU (or by any
 other technique). This value is expressed in units determined by the
 DC Power Unit parameter.

#### [IMAGE alt='image' src='guid-f398bab3-cb69-48f5-871b-a37628ad0db3-a5.gif'] DC
 Power Unit

Specifies the unit used to calculate the DC Power. This
 value can either be expressed in dBm or watt. The default value is
 watt.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-measure.html language=enus -->
## TOPIC 00090: PRFMsc Measure

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-measure.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-measure.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Measure

Performs enabled measurements on the data you specify and stores the results in the
 pulse measurement session. To complete the full measurement, you must call this VI once for
 each record in each measurement. Get the number of measurements and number of records per
 measurement from the PRFMsc Get Number of Iterations VI.

[IMAGE alt='image' src='guid-114f52fd-a9fd-4547-9e30-760b740b3019-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-35214749-111d-4924-9786-da040963e55e-a5.png'] Data

Specifies the I/Q data cluster corresponding to the measurement and record index.
 The default value is an empty cluster.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] Measurement Index

Specifies the current measurement. The default value is 0.

#### [IMAGE alt='image' src='guid-642c8b9e-2e03-4aa0-92ed-65992bca5fa3-a5.gif'] Record Index

Specifies the current record within the current measurement. The default value is
 0.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### Example

Refer to the PRFMsc Pulse Measurements VI at
 labview\examples\PRFMsc\PRFMsc Pulse Measurements.vi for an
 example of using the PRFMsc Measure VI.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-save-cal-param.html language=enus -->
## TOPIC 00091: PRFMsc Save Calibration Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-save-cal-param.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-save-cal-param.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Save Calibration Parameters

Saves the calibration parameters in a .tdms file.

[IMAGE alt='image' src='guid-96c7b054-85be-4fe1-9a7d-7b7006c6d001-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png'] Calibration Parameters File Path

Specifies
 the location of the calibration parameters file. The default value is
 empty.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-save-s-param.html language=enus -->
## TOPIC 00092: PRFMsc Save S-Parameters

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-save-s-param.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-save-s-param.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Save S-Parameters

Saves measurement results in an .s2p file.

[IMAGE alt='image' src='guid-e461b072-d635-4745-9119-d7c306920f98-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-7b3a224a-c8c8-487d-a44e-f4ea0c2d85e5-a5.png'] S-Parameters File Path

Specifies the location of the S-parameters
 measurement data.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-select-measurements.html language=enus -->
## TOPIC 00093: PRFMsc Select Measurements

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-select-measurements.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-select-measurements.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Select Measurements

Enables the measurement(s) specified in the Pulse Measurement
 parameter and disables all others.

- PRFMsc Select Measurements (Single)
- PRFMsc Select
 Measurements (Multiple)

#### PRFMsc Select Measurements (Single)

Enables the measurement type specified by the Pulse Measurement
 input.

[IMAGE alt='image' src='guid-2234a4d2-aca7-49e1-b5bd-3f253c61cd5f-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png'] Pulse
 Measurement

Specifies the pulse measurement to enable. The default value is Pulse to Pulse
 Stability.

| Pulse to Pulse Stability | Specifies a Pulse to Pulse Stability measurement. Pulse-to-pulse stability measurements calculate the amplitude and phase stability of one or more selected measurement points in a pulse. |
| --- | --- |
| Intrapulse Stability | Specifies an Intrapulse Stability measurement. Intrapulse stability measurements calculate the amplitude and phase stability of selected measurement points in each pulse of a single burst. |
| Pulse Profile | Specifies a Pulse Profile measurement. Pulse profile measurements calculate the different characteristics of a pulse, such as the pulse amplitude, width, period, and transition. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Select Measurements (Multiple)

Enables the measurement types specified by the Pulse
 Measurements input.

[IMAGE alt='image' src='guid-b1175cd9-f635-49be-bf1f-81e8e771828a-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-c510a0c1-548b-456c-9b56-e5d4093f72a7-a5.gif'] Pulse
 Measurements

Specifies the pulse measurement types to enable. The
 default value is an empty array.

| Pulse to Pulse Stability | Specifies a Pulse to Pulse Stability measurement. Pulse-to-pulse stability measurements calculate the amplitude and phase stability of one or more selected measurement points in a pulse. |
| --- | --- |
| Intrapulse Stability | Specifies a Intrapulse Stability measurement. Intrapulse stability measurements calculate the amplitude and phase stability of selected measurement points in each pulse of a single burst. |
| Pulse Profile | Specifies a Pulse Profile measurement. Pulse profile measurements calculate the different characteristics of a pulse, such as the pulse amplitude, width, period, and transition. |

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-set-nidcpower-session.html language=enus -->
## TOPIC 00094: PRFMsc Set NIDCPower Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-set-nidcpower-session.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-set-nidcpower-session.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Set NIDCPower Session

Adds the NI-DCPower instrument session to the PAE measurement session. Use PRFMsc Commit
 VIs to commit parameters to the NI-DCPower session you specify.

[IMAGE alt='image' src='guid-af80a37f-3070-44bc-a7a3-44e6207a2fbd-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-665975b8-626f-4338-9a2b-dd603cdf6bc5-a5.png'] NI DCPower Instrument Handle

Specifies the NI-DCPower instrument session to add to the PAE measurement
 session. Obtain the NI-DCPower instrument session from the niDCPower
 Initialize With Independent Channels VI.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] NI DCPower Channel Name

Specifies the channel(s) to use for the measurement. Specify the channel(s) using
 the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
 PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are
 instrument resource names and 0, 2, and 3 are channels. If you do not wire this
 parameter, LabVIEW uses all channels in the instrument session for the
 measurement.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-set-nirfmx-session-pulse.html language=enus -->
## TOPIC 00095: PRFMsc Set NIRFmx Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-set-nirfmx-session-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-set-nirfmx-session-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Set NIRFmx Session

Adds the NI-RFmx instrument session to the pulse measurement session. Use PRFMsc Commit
 VIs to commit parameters to the NI-RFmx instrument session you specify.

[IMAGE alt='image' src='guid-e234f8e1-734d-4edf-8fed-fe602a874fb1-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-665975b8-626f-4338-9a2b-dd603cdf6bc5-a5.png'] NI RFmx Instrument Handle

Specifies the NI-RFmx instrument session to add to the PAE measurement session.
 Obtain the NI-RFmx instrument session from the RFmxInstr Initialize
 NIRFSA VI.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] NI RFmx Port

Specifies the instrument port to use for the measurement. The default value is an
 empty string. Obtain valid port names from the RFmxInstr Get Available
 Ports VI.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-set-nirfmx-session.html language=enus -->
## TOPIC 00096: PRFMsc Set NIRFmx Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-set-nirfmx-session.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-set-nirfmx-session.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Set NIRFmx Session

Adds the NI-RFmx instrument session to the PAE measurement session. Use PRFMsc Commit
 VIs to commit parameters to the NI-RFmx session you specify.

[IMAGE alt='image' src='guid-3a6d76ba-90bb-4921-b2c1-85b014adc853-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-665975b8-626f-4338-9a2b-dd603cdf6bc5-a5.png'] NI RFmx Instrument Handle

Specifies the NI-RFmx instrument session to add to the PAE measurement session.
 Obtain the NI-RFmx instrument session from the RFmxInstr Initialize
 NIRFSA VI.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] NI RFmx Port

Specifies the instrument port to use for the measurement. The default value is an
 empty string. Obtain valid port names from the RFmxInstr Get Available
 Ports VI.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-set-nirfsg-session-pulse.html language=enus -->
## TOPIC 00097: PRFMsc Set NIRFSG Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-set-nirfsg-session-pulse.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-set-nirfsg-session-pulse.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Set NIRFSG Session

Adds the NI-RFSG instrument session to the pulse measurement session. Use PRFMsc Commit
 VIs to commit parameters to the NI-RFSG instrument session you specify.

[IMAGE alt='image' src='guid-0c33884a-6fd6-437f-9860-f65aa3b0c00e-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] Pulse Reference In

Specifies the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-665975b8-626f-4338-9a2b-dd603cdf6bc5-a5.png'] NI RFSG Instrument Handle

Specifies the NI-RFSG instrument session to add to the PAE measurement session.
 Obtain the NI-RFSG instrument session from either the niRFSG
 Initialize VI or the niRFSG Initialize With
 Options VI.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] NI RFSG Port

Specifies the instrument port to use for the measurement. The default value is an
 empty string. The following table lists valid values for each device this VI
 supports:

| PXIe-5831 | if0 if1 |
| --- | --- |
| PXIe-5841 | "" (empty string) |

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] Pulse Reference
 Out

Returns the session reference handle of the Pulse measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-set-nirfsg-session.html language=enus -->
## TOPIC 00098: PRFMsc Set NIRFSG Session

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-set-nirfsg-session.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-set-nirfsg-session.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Set NIRFSG Session

Adds the NI-RFSG instrument session to the PAE measurement session. Use PRFMsc Commit
 VIs to commit parameters to the NI-RFSG session you specify.

[IMAGE alt='image' src='guid-bd0783b3-df8b-4d9c-8222-a9670636594b-a5.gif']

#### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] PAE
 Reference In

Specifies the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-665975b8-626f-4338-9a2b-dd603cdf6bc5-a5.png'] NI RFSG Instrument Handle

Specifies the NI-RFSG instrument session to add to the PAE measurement session.
 Obtain the NI-RFSG instrument session from either the niRFSG
 Initialize VI or the niRFSG Initialize With
 Options VI.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] NI RFSG Port

Specifies the instrument port to use for the measurement. The default value is an
 empty string. The following table lists valid values for each device this VI
 supports:

| PXIe-5831 | if0 if1 |
| --- | --- |
| PXIe-5841 | "" (empty string) |

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] PAE Reference Out

Returns the session reference handle of the PAE measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-spar-1c1vst-switching-class.html language=enus -->
## TOPIC 00099: PRFMsc S-Par 1 Coupler Per Port 1 VST Switching Class

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-spar-1c1vst-switching-class.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-spar-1c1vst-switching-class.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc S-Par 1 Coupler Per Port 1 VST
 Switching Class

This class is the base class for 1 coupler per port 1 VST setup. To implement your own
 switching class, inherit from this class and override the following two
 functions.

#### Connect.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='guid-f2feca01-d551-4993-b4fd-0c14320109f0-a5.gif']

[IMAGE alt='image' src='guid-c644037e-574f-48ea-a17b-e0c11b315e58-a5.png']
 Port 1 incident

Specifies the direction of the stimulus.

| TRUE | The stimulus comes from Port 1. |
| --- | --- |
| FALSE | The stimulus comes from Port 2. |

[IMAGE alt='image' src='guid-c644037e-574f-48ea-a17b-e0c11b315e58-a5.png']
 Reflection

| TRUE | Reflection measurement. |
| --- | --- |
| FALSE | Transmission measurement. |

#### Close
 Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='guid-f5aa0d4a-aee0-47b8-8ea4-252cfa8289c5-a5.gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='guid-5b527d40-2db4-48d3-b60e-800123017afb-a5.gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-spar-2c1vst-switching-class.html language=enus -->
## TOPIC 00100: PRFMsc S-Par 2 Couplers Per Port 1 VST Switching Class

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-spar-2c1vst-switching-class.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-spar-2c1vst-switching-class.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc S-Par 2 Couplers Per Port 1 VST
 Switching Class

This class is the base class for 2 couplers per port 1 VST setup. To implement your own
 switching class, inherit from this class and override the following two
 functions.

#### Connect.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='guid-66f22943-908e-4b05-8a85-4c6664f1bb1e-a5.gif']

[IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png']
 Incident Selection

[IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png']
 Coupler Selection

Specifies the coupler to measure.

#### Close
 Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='guid-7efd7a0e-7058-486d-b596-21426a9fe81b-a5.gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='guid-1ae747a4-3181-432d-a28e-75364ad7065d-a5.gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-spar-2c1vst-switching-scan-mode-class.html language=enus -->
## TOPIC 00101: PRFMsc S-Par 2 Couplers Per Port 1 VST Switching (Scan Mode) Class

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-spar-2c1vst-switching-scan-mode-class.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-spar-2c1vst-switching-scan-mode-class.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc S-Par 2 Couplers Per Port 1 VST
 Switching (Scan Mode) Class

This class is the base class for 2 couplers per port 1 VST, solid state switch setup.
 To implement your own switching class, inherit from this class and override the
 following two functions. This switching configuration should enable scanning of the
 switches automatically with a trigger input so that the switching path can be updated as
 needed.

#### Update
 Scan Status.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='guid-6b9fb237-3936-4007-80e7-691a09401256-a5.gif']

[IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png']
 Scanning Status

Specifies the status to set on the switches. Select from the following
 options.

| Idle | Specifies that no switching is needed. The internal status should be initialized as Idle. |
| --- | --- |
| Port 1 SOL | Scans the two couplers on Port 1, mainly for SOL calibration of Port 1. |
| Port 2 SOL | Scans the two couplers on Port 2, mainly for SOL calibration of Port 2. |
| Through/DUT | Scans the 2 port measurements for through calibration or DUT measurements. |

[IMAGE alt='image' src='guid-6c052875-af23-479b-922b-ca1c3c4d5ab3-a5.png']
 Status Changed

Returns TRUE when a change in the scanning status occurs after this VI is
 called. Returns FALSE when the scanning status is unchanged
 after this VI is called.

#### Close
 Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='guid-7efd7a0e-7058-486d-b596-21426a9fe81b-a5.gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='guid-f04a9eca-02d6-40ec-9e71-dd742c8a758e-a5.gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-spar-s112c-switching-class.html language=enus -->
## TOPIC 00102: PRFMsc S-Par S11 2 Couplers Switching Class

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-spar-s112c-switching-class.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-spar-s112c-switching-class.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc S-Par S11 2 Couplers Switching
 Class

This class is the base class for the S11 2 couplers setup. To implement your own
 switching class, inherit from this class and override the following two
 functions.

#### Connect.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='guid-e237082e-24a6-4776-8c05-adc96ce991ce-a5.gif']

[IMAGE alt='image' src='guid-3ea01054-9c40-4557-9a66-3f764e6298f9-a5.png']
 Coupler Selection

Specifies the coupler to measure.

#### Close
 Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='guid-7efd7a0e-7058-486d-b596-21426a9fe81b-a5.gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='guid-b3167dd4-eda7-4763-854a-99766b56367c-a5.gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-sparam-initiate.html language=enus -->
## TOPIC 00103: PRFMsc Initiate

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-sparam-initiate.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-sparam-initiate.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Initiate

Begins the S-parameter measurement.

[IMAGE alt='image' src='guid-5920f330-8a0c-45e9-804b-f36e179f4849-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-start-trig-input.html language=enus -->
## TOPIC 00104: PRFMsc Configure Start Trigger Input

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-start-trig-input.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-start-trig-input.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Configure Start Trigger Input

Configures the trigger to start the S-parameter measurement. The measurement is
 complete when there is a rising edge on the assigned trigger. This configuration only
 supports the 2 couplers per port 1 VST with solid state switch setup. If the trigger is
 not configured or configured for an unsupported setup the measurement is performed
 immediately after initiated.

[IMAGE alt='image' src='guid-74cc02fc-b8f7-4a9d-b93e-72d0591de790-a5.gif']

#### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-58e56919-5b2d-4e6c-aa69-669e6e2655a8-a5.png'] Start Trigger
 Input

Specifies the terminal on which the S-parameter session looks for a start
 trigger. The default value is None.

#### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

#### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

#### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/prfmsc-topology-references.html language=enus -->
## TOPIC 00105: PRFMsc Get Topology References

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/prfmsc-topology-references.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/prfmsc-topology-references.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### PRFMsc Get Topology References

Fetches the RFmx and RFSG references of the current S-parameter measurement session.

- PRFMsc
 Get Topology References (1CperPort2VST)
- PRFMsc
 Get Topology References (2CperPort1VST)
- PRFMsc
 Get Topology References (1CperPort1VST)
- PRFMsc
 Get Topology References (1CperPort1VSTS21)
- PRFMsc Get Topology References (S11_1Coupler)
- PRFMsc Get Topology References (S11_2Couplers)
- PRFMsc Get Topology References (2CperPort1VST Solid State Switch)

Refer to the [Electronically Scanned Array Characterization Reference Architecture User
 Manual](https://www.ni.com/r/mmic-user-manual) for details about each topology.

#### PRFMsc Get Topology References
 (1CperPort2VST)

Fetches the references of a 1 Coupler per Port, 2 VST measurement session.

[IMAGE alt='image' src='guid-8f546b55-243e-4945-afcb-ed2f0479a8e3-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFSG Session Instr 2

Returns the NI-RFSG session name associated with the VST connected to Port 2 of the DUT.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx Session Instr 2

Returns the NI-RFmx session name associated with the VST connected to Port 2 of the DUT.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI
 RFSG Session Instr 1

Returns the NI-RFSG session name associated with the VST connected to Port 1 of the DUT.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx Session Instr 1

Returns the NI-RFmx session name associated with the VST connected to Port 1 of the DUT.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Get Topology References
 (2CperPort1VST)

Fetches the references of a 2 Coupler per Port, 1 VST measurement session.

[IMAGE alt='image' src='guid-9b30c0c3-4be7-4775-9957-ed92679b8a95-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI
 RFSG Session

Returns the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx Session

Returns the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] Switch Reference

Returns the class instance of the switch. Refer to [S-Parameter
 Switching Configuration Class](s-parameter-switching-configuration-class.html) for more information.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Get Topology References
 (1CperPort1VST)

Fetches the references of a 1 Coupler per Port, 1 VST measurement session.

[IMAGE alt='image' src='guid-07c12ccc-afe5-4449-ac63-d4b3e84fdf9f-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI
 RFSG Session

Returns the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx Session

Returns the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] Switch Reference

Returns the class instance of the switch. Refer to [S-Parameter
 Switching Configuration Class](s-parameter-switching-configuration-class.html) for more information.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Get Topology References
 (1CperPort1VSTS21)

Fetches the references of a 1 VST measurement session that was used for an S21
 measurement only.

[IMAGE alt='image' src='guid-00fe358a-692e-4164-b326-c1deedf58a69-a5.gif']

##### [IMAGE alt='image' src='guid-a0ede53e-ddcb-4367-b3e8-660a3c747583-a5.png'] S-Par Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-aae4dcb1-df3e-4d2a-90da-0c1637dffa27-a5.gif'] error in

Error
 conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-b3f04d9e-70a3-4f92-b9ee-e5825bb52dcf-a5.png'] S-Par Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI
 RFSG Session

Returns the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx Session

Returns the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-029e8ba4-3033-45af-b52f-84a533ec7cea-a5.gif'] error out

Error
 information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Get Topology References
 (S11_1Coupler)

Fetches the references of an S11, 1 Coupler measurement session.

[IMAGE alt='image' src='guid-0e131a87-8b7f-4b20-8af8-bbf7bee4aafe-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFSG
 Session

Returns the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx
 Session

Returns the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Get Topology References
 (S11_2Couplers)

Fetches the references of an S11, 2 Couplers measurement session.

[IMAGE alt='image' src='guid-55804449-3580-45b5-8b77-cf79cfde58c1-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFSG
 Session

Returns the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx
 Session

Returns the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] Switch
 Reference

Returns the name of the NI-Switch session that was used.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

#### PRFMsc Get Topology References
 (2CperPort1VST Solid State Switch)

Fetches the references of a 2 Coupler per Port, 1 VST solid state switch measurement
 session.

[IMAGE alt='image' src='guid-c20a5229-7f38-4d73-a148-ddf10168af8f-a5.gif']

##### [IMAGE alt='image' src='guid-164e13c6-00f2-4a27-8505-ee772752b719-a5.png'] S-Par
 Reference In

Specifies the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-6648b999-cd2a-41d8-bbf1-995739a656fc-a5.gif']
 error in

Error conditions that occur before this node runs. This input provides [standard error in](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_in/) functionality.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] S-Par
 Reference Out

Returns the session reference handle of the S-parameter measurement session.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFSG
 Session

Returns the name of the NI-RFSG session that was used.

##### [IMAGE alt='image' src='guid-5bd8da4b-4856-4563-9fc1-b2af12d250b4-a5.gif'] NI RFmx
 Session

Returns the name of the NI-RFmx session that was used.

##### [IMAGE alt='image' src='guid-d907d9e8-fca5-4b3c-9d6b-e9b52fc4c2d6-a5.png'] Switch
 Reference

Returns the name of the NI-Switch session that was used.

##### [IMAGE alt='image' src='guid-def717f3-ca9f-4bc3-bd7d-4ac1644220b9-a5.gif']
 error out

Error information. This output provides [standard error out](http://zone.ni.com/reference/en-xx/help/371361r-01/lvconcepts/using_standard_error_out/) functionality.

<!--NI_TOPIC bundle=pulsed-rf-meas-library-api-ref path=prfmscapi/s-parameter-switching-configuration-class.html language=enus -->
## TOPIC 00106: S-Parameter Switching Configuration Class

- bundle_id: `pulsed-rf-meas-library-api-ref`
- source_path: `prfmscapi/s-parameter-switching-configuration-class.html`
- source_url: https://docs-be.ni.com/bundle/pulsed-rf-meas-library-api-ref/raw/resource/enus/prfmscapi/s-parameter-switching-configuration-class.html
- document_id: `pulsed-rf-meas-library-api-ref`
- page_type: `leaf`
- content_type: ``

### S-Parameter Switching Configuration
 Class

labview\vi.lib\addons\PRFMsc\S-parameters\Switching

PRFMsc S-Par Switching.lvlib includes base classes for
 one-coupler-per-port, single VST setups, two-couplers-per-port, single VST setups, S11
 two couplers setups, and two-couplers-per-port, single VST (solid state switch)
 setups.

By inheriting the corresponding base class, you can create a switching configuration class
 that uses your own switches for S-parameter measurements. Refer to the
 labview\examples\PRFMsc\SubVIs\Switching for S-Parameters
 directory for example VIs that demonstrate how to implement the switching configuration
 classes.
