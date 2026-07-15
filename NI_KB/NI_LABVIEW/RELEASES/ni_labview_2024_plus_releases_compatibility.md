# NI_LABVIEW_2024_PLUS_RELEASE_COMPATIBILITY_FULL

<!--SYSTEM_CORPUS id=NI_LABVIEW_RELEASES format=markdown generated=2026-07-14T12:02:18+00:00 -->
- fidelity: full-section-records
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1

# SOURCE labview-runtime-compatibility

- title: LabVIEW and LabVIEW Run-Time Engine Compatibility
- category: compatibility
- url: https://www.ni.com/en/support/documentation/compatibility/17/labview-and-labview-run-time-engine-compatibility.html
- source_sha256: 9f761a6777cb33bd67be387ac5478d3e748310721cdd603e808faa7c8b2ff61d
- versions: ["2024 Q1", "2024 Q3", "2025 Q1", "2025 Q3", "2026 Q1"]

<!--KB_RECORD source=labview-runtime-compatibility locator=section:1 ordinal=1 -->
## Overview

This page shows supported versions of LabVIEW Run-Time Engine with LabVIEW development systems. Reference this information to ensure you install the correct toolkit version when upgrading or updating your system or software. Using incompatible versions may result in errors, or missing LabVIEW palettes or functions.

<!--END_KB_RECORD source=labview-runtime-compatibility locator=section:1 -->

<!--KB_RECORD source=labview-runtime-compatibility locator=section:2 ordinal=2 -->
## LabVIEW and LabVIEW Run-Time Engine Compatibility

The table below shows the compatibility between LabVIEW Development versions and LabVIEW Run-Time Engine (RTE) versions.

Note: LabVIEW Applications must be run on a LabVIEW Run-Time Engine of the same bitness that it was developed with. The table below can be used to determine compatibility between LabVIEW and its RTE for either bitness.

In the Downloads section at the bottom of this page, you can download a copy of this table, which may include older software versions.

If you are looking for an earlier version not listed in the table below or Compatibility Table download, you can find the LabVIEW Run-Time compatibility information in your version's readme.

LabVIEW Version
LabVIEW Run-Time Engine VersionRTE 2026 Q1RTE 2025 Q3RTE 2025 Q1RTE 2024 Q3RTE 2024 Q1RTE 2023 Q3RTE 2023 Q1RTE 2022 Q3RTE 2021 SP1RTE 20212026 Q1 2025 Q3 2025 Q1 2024 Q3 2024 Q1 2023 Q3 2023 Q1 2022 Q3 2021 SP1 2021 2020 SP1 2020 2019 SP1 2019

LabVIEW Version

Compatible

Compatible if application built to support later run-times*

*Starting from 2017, you can build compatibility with later LabVIEW Run-Time Engines into your applications. By default, LabVIEW builds applications to use the latest compatible run-time engine available on the system. While LabVIEW run-time engines maintain the same interfaces, they do not maintain the same behaviors as earlier compatible versions. Applications with the Allow future versions of the LabVIEW Runtime to run this application option selected may experience behavior changes when a newer run-time engine becomes available. If you would rather maintain the current behavior of your application than get bug fixes and performance improvements, deselect Allow future versions of the LabVIEW Runtime to run this application.

The LabVIEW Run-Time Engine must be installed on any system where you plan to run executables or shared libraries built with the LabVIEW Application Builder.

Note that EXEs built in LabVIEW 2016 or earlier can't be run in a newer version of the LabVIEW Run-Time Engine. Use the same version of LabVIEW Run-Time Engine to run the EXE as the LabVIEW version that you used to build it.

Multiple versions of the LabVIEW Run-Time Engine can be installed on the same computer as long as the major version number or the bitness is different. On a 64-bit system it is possible to install 32-bit and 64-bit versions of the LabVIEW Run-Time Engine with the same version number side-by-side. If you install an SP1 version of the LabVIEW Run-Time Engine on a system that already has the non-SP1 version installed, the SP1 version will replace the non-SP1 version.

LabVIEW Run-Time Engine Web Browser Plug-in

The LabVIEW Run-Time Engine Web Browser Plug-in (formerly known as the LabVIEW Minimum Run-Time Engine) is a smaller download intended for viewing VIs embedded in a web page (Remote Front Panels). It does not contain the full run-time engine and is not recommended for running executables. It is available in both 32-bit and 64-bit versions. The bitness of the Web Browser Plug-in must match the bitness of the web browser being used. The standard LabVIEW Run-Time Engine includes the Web Browser Plug-in.

<!--END_KB_RECORD source=labview-runtime-compatibility locator=section:2 -->

<!--KB_RECORD source=labview-runtime-compatibility locator=section:3 ordinal=3 -->
## Additional Resources

Install the LabVIEW Run-Time Engine

Which Versions of LabVIEW Run-Time Engine Do I Have Installed?

LabVIEW Runtime Download

<!--END_KB_RECORD source=labview-runtime-compatibility locator=section:3 -->

# SOURCE labview-2024-q1-known-issues

- title: LabVIEW 2024 Q1 Known Issues
- category: known-issues
- url: https://www.ni.com/en/support/documentation/bugs/24/labview-2024-q1-known-issues.html
- source_sha256: 8e34e9a879f0a4fb107ab03b7d9ccd8203f7fb6512f03fba434dab19f74d5dec
- versions: ["2024 Q1"]

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:1 ordinal=1 -->
## Overview

This document contains the LabVIEW known issues that were discovered before and since the release of LabVIEW 2024 Q1. Known issues are performance issues or technical bugs that NI has acknowledged exist within this version of the product.

Not every issue known to NI appears on this list; it is intended to show the most severe and common issues that you may encounter and provide workarounds when possible. Other technical issues that you may encounter could occur through normal product use or system compatibility issues. You may find more information on these issues in NI’s Product Documentation, Knowledgebase, or Community; see Additional Resources.

Bug Number

Legacy ID

Description

Details

2599334

WebDAV, HTTP, and SMTP Functions Fail to Use Certificates from Files
Configure SSL (WebDAV), Asynchronous Configure SSL (WebDAV), ConfigSSL (HTTP Client), and Config TLS (SMTP) functions fail to use certificate files but do not return errors.

Workaround:
Copy any needed certificates into the Windows certificate store.

Reported Version:
LabVIEW 2023 Q1
Resolved Version:
N/A
Added:
Jan 22, 2024

Offline Help for LabVIEW 2024 Q1 Chinese and Korean Versions Contains Content from LabVIEW 2023 Q3
In LabVIEW 2024 Q1 localized to Chinese or Korean, the offline help includes the same contents as the LabVIEW 2023 Q3 help.

Workaround:
Use the online help instead of the offline help.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
N/A
Added:
Jan 22, 2024

2625975

LabVIEW Crashes After Clicking the Help Button in Application Properties

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q1 Patch 1
Added:
Jan 22, 2024

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:1 -->

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:2 ordinal=2 -->
## WebDAV, HTTP, and SMTP Functions Fail to Use Certificates from Files

Configure SSL (WebDAV), Asynchronous Configure SSL (WebDAV), ConfigSSL (HTTP Client), and Config TLS (SMTP) functions fail to use certificate files but do not return errors.

Workaround:

Copy any needed certificates into the Windows certificate store.

Reported Version:

LabVIEW 2023 Q1

Resolved Version:

N/A

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:2 -->

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:3 ordinal=3 -->
## Offline Help for LabVIEW 2024 Q1 Chinese and Korean Versions Contains Content from LabVIEW 2023 Q3

In LabVIEW 2024 Q1 localized to Chinese or Korean, the offline help includes the same contents as the LabVIEW 2023 Q3 help.

Workaround:

Use the online help instead of the offline help.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

N/A

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:3 -->

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:4 ordinal=4 -->
## LabVIEW Crashes After Clicking the Help Button in Application Properties

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q1 Patch 1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:4 -->

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:5 ordinal=5 -->
## Final Time Issue Listed

Issues found in this section will not be listed in future known issues documents for this product.

Bug Number

Legacy ID

Description

Details

2052750

Same Version of LabVIEW Is Listed Twice in Software Section of NI MAX

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2022 Q3
Resolved Version:
N/A
Added:
Jan 22, 2024

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:5 -->

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:6 ordinal=6 -->
## Same Version of LabVIEW Is Listed Twice in Software Section of NI MAX

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2022 Q3

Resolved Version:

N/A

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:6 -->

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:7 ordinal=7 -->
## Additional Resources

Explore Support Content and Product Documentation

Search the NI KnowledgeBase for a solution

Learn how to get started and use the product

Ask the NI Community

Collaborate with other users in our discussion forums

Search the NI Community for a solution

Request Support from an Engineer

A valid service agreement may be required, and support options vary by country

Open a service request

Purchase or renew support services

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:7 -->

<!--KB_RECORD source=labview-2024-q1-known-issues locator=section:8 ordinal=8 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2024-q1-known-issues locator=section:8 -->

# SOURCE labview-2024-q1-bug-fixes

- title: LabVIEW 2024 Q1 Bug Fixes
- category: bug-fixes
- url: https://www.ni.com/en/support/documentation/bugs/24/labview-2024-q1-bug-fixes.html
- source_sha256: 6948879e2bb81c0422db587c9dc806f4d1b6f7862a380e93b5ed626f7a044ce2
- versions: ["2024 Q1"]

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:1 ordinal=1 -->
## Overview

The following items are notable issues fixed between the release of LabVIEW 2023 Q3 and LabVIEW 2024 Q1, including additional patches and service packs. If you have an issue ID, you can search this list to validate that the issue has been fixed. This is not an exhaustive list of issues fixed in the current version of LabVIEW.

Bug Number

Legacy ID

Description

Details

2058864

Function That Converts Variant to Flattened String Produces Incorrect String Type for Set Data

Workaround:
Not Applicable

Reported Version:
LabVIEW 2019 SP1
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2392126

List of Objects in Quick Change Dialog Is Not Localized

Workaround:
Not Applicable

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2440992

Using the Right-Click Menu Plugin to Lookup All Shortcut Menu Tags and Types Does Not Display Expected Results

Workaround:
Not Applicable

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2565540

Sort 2D Array.vim is Unexpectedly Slow When Operating on a Sorted Array

Workaround:
Not Applicable

Reported Version:
LabVIEW 2020 SP1
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2479826

Control Can Have Unexpected Default Value When Created Using Double Click During Wiring
When you create a control by double-clicking when wiring from a subVI terminal , the control can have a default value that is different from the displayed value.

Workaround:
Not Applicable

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2481419

Incorrect Value Returned When Reading Class Name Property of Some Event Structure Terminals
Using VI Scripting, reading the Class Name property of the Dynamic Terminal or Timeout Terminal of an Event Structure returns "Generic" instead of "Tunnel."

Workaround:
Not Applicable

Reported Version:
LabVIEW 2020 SP1
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2519019

Built Application Searches for NI_Matrix.lvlib:RealMatrix.ctl When Run
When you run an application built with the matrix datatype, the application searches for NI_Matrix.lvlib:RealMatrix.ctl.

Workaround:
Not Applicable

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2552750

Incorrect Wiring After Inserting Some Functions On Set and Map Wires with Quick Drop
After inserting a Remove From Set or Remove From Map function using Quick Drop, the output wire is not connected to the correct terminal.

Workaround:
Not Applicable

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2516141

64-bit Values Incorrectly Converted to 32-bit in Expression Node

Workaround:
Not Applicable

Reported Version:
LabVIEW 2021
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

2625975

LabVIEW Crashes After Clicking the Help Button in Application Properties

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q1
Added:
Jan 22, 2024

Fixed Security Issues Identified as CVE-2024-23608, CVE-2024-23609, CVE-2024-23610, CVE-2024-23611, & CVE-2024-23612

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

Sound File Read Returns Incorrect Offset When Using Relative Position Mode
The offset output should be the absolute offset from the beginning of the file, even in relative mode.

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2016
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

Sound File Read Does Not Reflect Position Offset in Waveform t0
The position offset is not reflected in the t0 of the waveform output of Sound File Read.

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2016
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

Incorrect Sound Data Is Sometimes Returned from Sound File Read in Absolute Position Mode

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2023 Q1
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

2619768

Duplicate Block Diagram Constant Differences in Compare VI Results
When comparing VIs, the same change to a block diagram constant can appear multiple times.

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

Missing LINX VIs in LabVIEW Community Edition Palettes

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

Unable to Connect to Raspberry Pi 5 Using Hobbyist Toolkit Target Configuration Dialog

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

2643576

Incorrect VI Reference Opened by Open VI Reference When Created from an Existing Strict VI Reference
When passing a strict VI reference to the VI path parameter of Open VI Reference, the VI reference output forms incorrectly. The wire's data type is a strict VI reference, but the reference is non-strict. Passing this reference to functions that require a strict VI reference, such as Start Asynchronous Call, will result in a run-time error.

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

719917

Sound File Open for Write Can Produce Unexpected Values
Sound File Write Open.vi can produce unexpected values since it rounds sample rates down rather than to the nearest.

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2016
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

Analog Waveform Data May Differ from WAV File Contents When Reading and Writing Sound Files

Workaround:
Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q1
Added:
Mar 8, 2024

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:1 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:2 ordinal=2 -->
## Function That Converts Variant to Flattened String Produces Incorrect String Type for Set Data

Workaround:

Not Applicable

Reported Version:

LabVIEW 2019 SP1

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:2 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:3 ordinal=3 -->
## List of Objects in Quick Change Dialog Is Not Localized

Workaround:

Not Applicable

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:3 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:4 ordinal=4 -->
## Using the Right-Click Menu Plugin to Lookup All Shortcut Menu Tags and Types Does Not Display Expected Results

Workaround:

Not Applicable

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:4 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:5 ordinal=5 -->
## Sort 2D Array.vim is Unexpectedly Slow When Operating on a Sorted Array

Workaround:

Not Applicable

Reported Version:

LabVIEW 2020 SP1

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:5 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:6 ordinal=6 -->
## Control Can Have Unexpected Default Value When Created Using Double Click During Wiring

When you create a control by double-clicking when wiring from a subVI terminal , the control can have a default value that is different from the displayed value.

Workaround:

Not Applicable

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:6 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:7 ordinal=7 -->
## Incorrect Value Returned When Reading Class Name Property of Some Event Structure Terminals

Using VI Scripting, reading the Class Name property of the Dynamic Terminal or Timeout Terminal of an Event Structure returns "Generic" instead of "Tunnel."

Workaround:

Not Applicable

Reported Version:

LabVIEW 2020 SP1

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:7 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:8 ordinal=8 -->
## Built Application Searches for NI_Matrix.lvlib:RealMatrix.ctl When Run

When you run an application built with the matrix datatype, the application searches for NI_Matrix.lvlib:RealMatrix.ctl.

Workaround:

Not Applicable

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:8 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:9 ordinal=9 -->
## Incorrect Wiring After Inserting Some Functions On Set and Map Wires with Quick Drop

After inserting a Remove From Set or Remove From Map function using Quick Drop, the output wire is not connected to the correct terminal.

Workaround:

Not Applicable

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:9 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:10 ordinal=10 -->
## 64-bit Values Incorrectly Converted to 32-bit in Expression Node

Workaround:

Not Applicable

Reported Version:

LabVIEW 2021

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:10 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:11 ordinal=11 -->
## LabVIEW Crashes After Clicking the Help Button in Application Properties

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q1

Added:

Jan 22, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:11 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:12 ordinal=12 -->
## Fixed Security Issues Identified as CVE-2024-23608, CVE-2024-23609, CVE-2024-23610, CVE-2024-23611, & CVE-2024-23612

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:12 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:13 ordinal=13 -->
## Sound File Read Returns Incorrect Offset When Using Relative Position Mode

The offset output should be the absolute offset from the beginning of the file, even in relative mode.

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2016

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:13 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:14 ordinal=14 -->
## Sound File Read Does Not Reflect Position Offset in Waveform t0

The position offset is not reflected in the t0 of the waveform output of Sound File Read.

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2016

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:14 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:15 ordinal=15 -->
## Incorrect Sound Data Is Sometimes Returned from Sound File Read in Absolute Position Mode

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2023 Q1

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:15 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:16 ordinal=16 -->
## Duplicate Block Diagram Constant Differences in Compare VI Results

When comparing VIs, the same change to a block diagram constant can appear multiple times.

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:16 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:17 ordinal=17 -->
## Missing LINX VIs in LabVIEW Community Edition Palettes

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:17 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:18 ordinal=18 -->
## Unable to Connect to Raspberry Pi 5 Using Hobbyist Toolkit Target Configuration Dialog

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:18 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:19 ordinal=19 -->
## Incorrect VI Reference Opened by Open VI Reference When Created from an Existing Strict VI Reference

When passing a strict VI reference to the VI path parameter of Open VI Reference, the VI reference output forms incorrectly. The wire's data type is a strict VI reference, but the reference is non-strict. Passing this reference to functions that require a strict VI reference, such as Start Asynchronous Call, will result in a run-time error.

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:19 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:20 ordinal=20 -->
## Sound File Open for Write Can Produce Unexpected Values

Sound File Write Open.vi can produce unexpected values since it rounds sample rates down rather than to the nearest.

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2016

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:20 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:21 ordinal=21 -->
## Analog Waveform Data May Differ from WAV File Contents When Reading and Writing Sound Files

Workaround:

Fixed in LabVIEW 2024 Q1 Patch 1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q1

Added:

Mar 8, 2024

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:21 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:22 ordinal=22 -->
## Additional Patch Information

Installing some patches may require certain additional steps or considerations. Please refer to the following table for more information about patches for this release.

These patches currently do not have any special instructions.

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:22 -->

<!--KB_RECORD source=labview-2024-q1-bug-fixes locator=section:23 ordinal=23 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2024-q1-bug-fixes locator=section:23 -->

# SOURCE labview-2024-q3-bug-fixes

- title: LabVIEW 2024 Q3 Bug Fixes
- category: bug-fixes
- url: https://www.ni.com/en/support/documentation/bugs/24/labview-2024-q3-bug-fixes.html
- source_sha256: d9aace1d20d1fefc57798730677888dc3a02d35a3024fb274b215736da4e1886
- versions: ["2024 Q3"]

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:1 ordinal=1 -->
## Overview

The following items are notable issues fixed between the release of LabVIEW 2024 Q1 and LabVIEW 2024 Q3, including additional patches and service packs. If you have an issue ID, you can search this list to validate that the issue has been fixed. This is not an exhaustive list of issues fixed in the current version of LabVIEW.

Bug Number

Legacy ID

Description

Details

2645388

Building a Packed Library May Fail Due to Incorrect Path to .NET DLL
In LabVIEW 2024 Q1, building a packed library can fail because LabVIEW incorrectly resolves a relative path to a .NET DLL.

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2714418

LabVIEW Sometimes Cannot Display File Dialog After Creating Override Methods in a Class

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2717959

LabVIEW Controls Do Not Receive Mouse Wheel Event with Ctrl Key Pressed

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2742395

LabVIEW Crashes When Comparing VIs with Different Passwords
When comparing VIs that are protected with different passwords, LabVIEW crashes after you enter the passwords.

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2748388

Compare VIs Does Not Report Difference When Label Changes Attached Object

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2752615

LabVIEW Editor Responds Slowly with Navigation Window Open and Block Diagram Zoomed

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2767151

Mass Compile Does Not Update Cache for Some VIs Installed in LVAddons
Mass compile doesn't update the compile cache for VIs installed in the shared LVAddons folder if the VIs are in read-only LLBs. Without an updated cache, TestStand cannot run the VIs using the LabVIEW Run-Time Engine.

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

221246
718006

LabVIEW Does Not Propagate Type Definition Changes to Containers, Causing Unexpected Run-Time Behavior
After you change a type definition's qualified name (for example, by removing it from a class), LabVIEW may fail to apply such change to event refnums or other container data types that include that type definition. VIs that references the affected container data type won’t show as broken, but may have unexpected run-time behavior.

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2016
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

812117
520215

Find Parallelizable Loops Does Not Analyze VIs Under Targets

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2009 SP1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2597746

LabVIEW Fails to Create Probe for Cluster that Contains IMAQ Image

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2663212

VI Block Diagram Wires Sometimes Draw Incorrectly on Ubuntu

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2675593

LabVIEW (64-bit) Sometimes Gives Incorrect Results When Converting Timestamps to Strings with Fractional Seconds Exceeding 19 Digits

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2023 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2682003

Resizing Loops Sometimes Moves Tunnels Unnecessarily

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2687156

Compare VIs Does Not Report Differences in Window Transparency Values

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2023 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2694996

Quick Drop Shortcuts Do Not Work When Placing VIs Shipped with LabVIEW

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2695155

LabVIEW Can Display the Wrong Portion of a VI Block Diagram During Debugging When Diagram is Zoomed In

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2707687

In Multi-Monitor Systems, LabVIEW Sometimes Fails to Display the Review and Update from Type Def. Dialog

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2713392

Compare VIs Does Not Report Adding a Custom Run-time Menu on a Control as a Difference

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2016
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2731705

On Property and Invoke Nodes, the Right-click Help Menu for the Selected Property or Method is Missing

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2599334

WebDAV, HTTP, and SMTP Functions Fail to Use Certificates from Files
Configure SSL (WebDAV), Asynchronous Configure SSL (WebDAV), ConfigSSL (HTTP Client), and Config TLS (SMTP) functions fail to use certificate files but do not return errors.

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2023 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

Offline Help for LabVIEW 2024 Q1 Chinese and Korean Versions Contains Content from LabVIEW 2023 Q3
In LabVIEW 2024 Q1 localized to Chinese or Korean, the offline help included the same contents as the LabVIEW 2023 Q3 help.

Workaround:
Fixed in LabVIEW 2024 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3
Added:
Jul 17, 2024

2786419

Palette Categories Are Visible Even When Empty
All the palette categories are visible by default.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 1
Added:
Jul 17, 2024

2811695

LabVIEW Class Becomes Corrupted After Editing Private Data Control and Saving from Unsaved Changes Dialog

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 1
Added:
Aug 7, 2024

2800868

LabVIEW Numeric Control Fails to Paste Values Copied from Microsoft Outlook or Word

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3 Patch 1
Added:
Aug 7, 2024

2798144

MATLAB Script Nodes Break VIs
VIs containing MATLAB Script Nodes are broken because the script support DLL is not found.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 1
Added:
Jul 17, 2024

2799931

Command Prompt Window Appears Briefly During Launch of LabVIEW on Windows

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Jul 17, 2024

2782815

LabVIEW Reports the Variable Configuration is Invalid After Deploying a Shared Variable
A shared variable with Bind to Source setting enabled and configured to bound to a network variable can be corrupted when a project loads. Deployment reports that the variable configuration is invalid.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Oct 14, 2024

2771439

Slow Editor Responsiveness When Editing VIs in LabVIEW for Linux

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Oct 14, 2024

2818129

LabVIEW Sometimes Erroneously Reports It Cannot Save to Previous Versions When Using Packed Libraries with LabVIEW Classes

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Oct 14, 2024

2826505

LabVIEW Crashes When Using Custom VI Menus and Actor Framework

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Oct 14, 2024

2840560

LabVIEW Sometimes Crashes When Building Build Specifications With VIs That Use Sets or Maps of Classes

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Oct 14, 2024

2849639

LabVIEW 2018 Crashes When Opening Some VIs Edited in LabVIEW 2024 Q3
When saving a VI for previous to LabVIEW 2018, the VI can become corrupted such that LabVIEW 2018 crashes when opening it. This happens when the VI contains an Error Constant wired to the selector of a Case Structure.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Oct 14, 2024

2781966

Unexpected Save Dialogs When Maintaining Projects in Older Save Version
LabVIEW may prompt you to save changes when editing VIs in a project maintained in an older version. For example, using DQMH for operations such as creating Private Events or validating a DQMH module will trigger a prompt to save VIs, indicating that the VI's source save version has changed.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 2
Added:
Jul 17, 2024

2945908

LabVIEW Sometimes Crashes With Internal Error 0xE59037CA
After opening some class member VIs, LabVIEW crashes with error 0xE59037CA at SliceSupport.cpp, line 58.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 3
Added:
Mar 21, 2025

2937381

VI Reentrancy Behavior Temporarily Incorrect When Project Save Version Set to Prior Version
When saving reentrant VIs in a project with the Project Save Version set to a prior version, VIs are executing as non-reentrant until they leave memory. After LabVIEW reloads the VIs, they behave normally.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 3
Added:
Mar 25, 2025

3013891

Vulnerabilities CVE-2025-2629, CVE-2025-2630, CVE-2025-2631 and CVE-2025-2632
Fixed
DLL Hijacking vulnerabilities due to uncontrolled search path identified as CVE-2025-2629 and CVE-2025-2630 Fixed out of bounds
write vulnerabilities due to improper bounds checking identified as CVE-2025-2631 and CVE-2025-2632

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 3
Added:
Mar 21, 2025

3022567

LabVIEW Built Application Crashes With Access Violation at EIP=0x5C81DFEC

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 3
Added:
Mar 21, 2025

3036893

Vulnerability CVE-2025-7361
Fixed Vulnerability CVE-2025-7361. LabVIEW no longer supports Code Interface Nodes unless the configuration file contains EnableCodeInterfaceNodes=True.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 4.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 4
Added:
Aug 1, 2025

3075204

Vulnerabilities CVE-2025-7848 and CVE-2025-7849
Fixed Memory Corruption Vulnerabilities CVE-2025-7848 and CVE-2025-7849.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 4.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 4
Added:
Aug 1, 2025

3429940

Vulnerabilities CVE-2025-64461, CVE-2025-64462, CVE-2025-64463, CVE-2025-64464, CVE-2025-64465, CVE-2025-64466, CVE-2025-64467, CVE-2025-64468, and CVE-2025-64469
Fixed memory corruption issues that crash LabVIEW when loading specifically corrupted VIs: CVE-2025-64461, CVE-2025-64462, CVE-2025-64463, CVE-2025-64464, CVE-2025-64465, CVE-2025-64466, CVE-2025-64467, CVE-2025-64468, CVE-2025-64469

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 5.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 5
Added:
Dec 15, 2025

3743979

Vulnerability CVE-2026-32861
Fixed out-of-bounds write vulnerability when opening a specifically corrupted .lvclass file: CVE-2026-32861.

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 6

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 6
Added:
Mar 16, 2026

3749030

Vulnerability CVE-2026-32860
Fixed out-of-bounds write vulnerability when opening a specifically corrupted .lvlib file: CVE-2026-32860

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 6

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 6
Added:
Mar 16, 2026

3749034

Vulnerabilities CVE-2026-32862, CVE-2026-32863, and CVE-2026-32864
Fixed memory corruption vulnerabilities when loading specifically corrupted VIs: CVE-2026-32862, CVE-2026-32863, CVE-2026-32864

Workaround:
Fixed in LabVIEW 2024 Q3 Patch 6

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2024 Q3 Patch 6
Added:
Mar 16, 2026

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:1 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:2 ordinal=2 -->
## Building a Packed Library May Fail Due to Incorrect Path to .NET DLL

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:2 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:3 ordinal=3 -->
## LabVIEW Sometimes Cannot Display File Dialog After Creating Override Methods in a Class

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:3 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:4 ordinal=4 -->
## LabVIEW Controls Do Not Receive Mouse Wheel Event with Ctrl Key Pressed

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:4 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:5 ordinal=5 -->
## LabVIEW Crashes When Comparing VIs with Different Passwords

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:5 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:6 ordinal=6 -->
## Compare VIs Does Not Report Difference When Label Changes Attached Object

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:6 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:7 ordinal=7 -->
## LabVIEW Editor Responds Slowly with Navigation Window Open and Block Diagram Zoomed

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:7 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:8 ordinal=8 -->
## Mass Compile Does Not Update Cache for Some VIs Installed in LVAddons

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:8 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:9 ordinal=9 -->
## LabVIEW Does Not Propagate Type Definition Changes to Containers, Causing Unexpected Run-Time Behavior

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2016

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:9 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:10 ordinal=10 -->
## Find Parallelizable Loops Does Not Analyze VIs Under Targets

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2009 SP1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:10 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:11 ordinal=11 -->
## LabVIEW Fails to Create Probe for Cluster that Contains IMAQ Image

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:11 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:12 ordinal=12 -->
## VI Block Diagram Wires Sometimes Draw Incorrectly on Ubuntu

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:12 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:13 ordinal=13 -->
## LabVIEW (64-bit) Sometimes Gives Incorrect Results When Converting Timestamps to Strings with Fractional Seconds Exceeding 19 Digits

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2023 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:13 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:14 ordinal=14 -->
## Resizing Loops Sometimes Moves Tunnels Unnecessarily

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:14 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:15 ordinal=15 -->
## Compare VIs Does Not Report Differences in Window Transparency Values

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2023 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:15 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:16 ordinal=16 -->
## Quick Drop Shortcuts Do Not Work When Placing VIs Shipped with LabVIEW

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:16 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:17 ordinal=17 -->
## LabVIEW Can Display the Wrong Portion of a VI Block Diagram During Debugging When Diagram is Zoomed In

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:17 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:18 ordinal=18 -->
## In Multi-Monitor Systems, LabVIEW Sometimes Fails to Display the Review and Update from Type Def. Dialog

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:18 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:19 ordinal=19 -->
## Compare VIs Does Not Report Adding a Custom Run-time Menu on a Control as a Difference

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2016

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:19 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:20 ordinal=20 -->
## On Property and Invoke Nodes, the Right-click Help Menu for the Selected Property or Method is Missing

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:20 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:21 ordinal=21 -->
## WebDAV, HTTP, and SMTP Functions Fail to Use Certificates from Files

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2023 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:21 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:22 ordinal=22 -->
## Offline Help for LabVIEW 2024 Q1 Chinese and Korean Versions Contains Content from LabVIEW 2023 Q3

Workaround:

Fixed in LabVIEW 2024 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:22 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:23 ordinal=23 -->
## Palette Categories Are Visible Even When Empty

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 1

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:23 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:24 ordinal=24 -->
## LabVIEW Class Becomes Corrupted After Editing Private Data Control and Saving from Unsaved Changes Dialog

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 1

Added:

Aug 7, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:24 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:25 ordinal=25 -->
## LabVIEW Numeric Control Fails to Paste Values Copied from Microsoft Outlook or Word

Workaround:

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3 Patch 1

Added:

Aug 7, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:25 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:26 ordinal=26 -->
## MATLAB Script Nodes Break VIs

Workaround:

Fixed in LabVIEW 2024 Q3 Patch 1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 1

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:26 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:27 ordinal=27 -->
## Command Prompt Window Appears Briefly During Launch of LabVIEW on Windows

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:27 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:28 ordinal=28 -->
## LabVIEW Reports the Variable Configuration is Invalid After Deploying a Shared Variable

Workaround:

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Oct 14, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:28 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:29 ordinal=29 -->
## Slow Editor Responsiveness When Editing VIs in LabVIEW for Linux

Workaround:

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Oct 14, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:29 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:30 ordinal=30 -->
## LabVIEW Sometimes Erroneously Reports It Cannot Save to Previous Versions When Using Packed Libraries with LabVIEW Classes

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Oct 14, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:30 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:31 ordinal=31 -->
## LabVIEW Crashes When Using Custom VI Menus and Actor Framework

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Oct 14, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:31 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:32 ordinal=32 -->
## LabVIEW Sometimes Crashes When Building Build Specifications With VIs That Use Sets or Maps of Classes

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Oct 14, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:32 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:33 ordinal=33 -->
## LabVIEW 2018 Crashes When Opening Some VIs Edited in LabVIEW 2024 Q3

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Oct 14, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:33 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:34 ordinal=34 -->
## Unexpected Save Dialogs When Maintaining Projects in Older Save Version

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 2

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:34 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:35 ordinal=35 -->
## LabVIEW Sometimes Crashes With Internal Error 0xE59037CA

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 3

Added:

Mar 21, 2025

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:35 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:36 ordinal=36 -->
## VI Reentrancy Behavior Temporarily Incorrect When Project Save Version Set to Prior Version

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 3

Added:

Mar 25, 2025

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:36 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:37 ordinal=37 -->
## Vulnerabilities CVE-2025-2629, CVE-2025-2630, CVE-2025-2631 and CVE-2025-2632

Fixed
DLL Hijacking vulnerabilities due to uncontrolled search path identified as CVE-2025-2629 and CVE-2025-2630

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 3

Added:

Mar 21, 2025

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:37 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:38 ordinal=38 -->
## LabVIEW Built Application Crashes With Access Violation at EIP=0x5C81DFEC

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 3

Added:

Mar 21, 2025

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:38 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:39 ordinal=39 -->
## Vulnerability CVE-2025-7361

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 4

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:39 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:40 ordinal=40 -->
## Vulnerabilities CVE-2025-7848 and CVE-2025-7849

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 4

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:40 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:41 ordinal=41 -->
## Vulnerabilities CVE-2025-64461, CVE-2025-64462, CVE-2025-64463, CVE-2025-64464, CVE-2025-64465, CVE-2025-64466, CVE-2025-64467, CVE-2025-64468, and CVE-2025-64469

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 5

Added:

Dec 15, 2025

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:41 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:42 ordinal=42 -->
## Vulnerability CVE-2026-32861

Workaround:

Fixed in LabVIEW 2024 Q3 Patch 6

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 6

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:42 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:43 ordinal=43 -->
## Vulnerability CVE-2026-32860

Workaround:

Fixed in LabVIEW 2024 Q3 Patch 6

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 6

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:43 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:44 ordinal=44 -->
## Vulnerabilities CVE-2026-32862, CVE-2026-32863, and CVE-2026-32864

Workaround:

Fixed in LabVIEW 2024 Q3 Patch 6

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2024 Q3 Patch 6

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:44 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:45 ordinal=45 -->
## Additional Patch Information

Installing some patches may require certain additional steps or considerations. Please refer to the following table for more information about patches for this release.

These patches currently do not have any special instructions.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:45 -->

<!--KB_RECORD source=labview-2024-q3-bug-fixes locator=section:46 ordinal=46 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2024-q3-bug-fixes locator=section:46 -->

# SOURCE labview-2025-q1-known-issues

- title: LabVIEW 2025 Q1 Known Issues
- category: known-issues
- url: https://www.ni.com/en/support/documentation/bugs/25/labview-2025-q1-known-issues.html
- source_sha256: e78395fee30a3056db1ac28d801f2736fcf780d97141b3606df7dbe0b4bb781a
- versions: ["2025 Q1"]

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:1 ordinal=1 -->
## Overview

This document contains the LabVIEW known issues that were discovered before and since the release of LabVIEW 2025 Q1. Known issues are performance issues or technical bugs that NI has acknowledged exist within this version of the product.

Not every issue known to NI appears on this list; it is intended to show the most severe and common issues that you may encounter and provide workarounds when possible. Other technical issues that you may encounter could occur through normal product use or system compatibility issues. You may find more information on these issues in NI’s Product Documentation, Knowledgebase, or Community; see Additional Resources.

Bug Number

Legacy ID

Description

Details

JKI Dragon 2024 Q3 Cannot Open LabVIEW 2025 Q1 Projects
The version of JKI Dragon that is included in the LabVIEW 2025 Q1 installer (version 2024 Q3) cannot open projects in LabVIEW 2025 Q1.

Workaround:
Open the JKI Dragon application and check for updates.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Jan 30, 2025

2954341

Invoke Node Calling .NET 8 Method Returns Error 1782 if Optional Parameter is Not Wired

Workaround:
Provide a value to the optional parameter.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Jan 30, 2025

2963459

Python Node Returns Error 1667 When Module Path Contains Unicode Characters

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2023 Q1 | LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Jan 27, 2025

2972983

Select .NET Core Constructor Dialog Incorrectly Reports No Public Constructors For Classes Not Part of Any Namespace
If you select a class that is not part of any namespace in the Select .NET Core Constructor dialog, the message This class contains no public constructors is displayed, even if the class does contain public constructors.

Workaround:
Declare your .NET classes as part of a namespace.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Jan 30, 2025

2930247

Mass Compile Slower Because LabVIEW Does Not Save VIs in LVAddons
When you mass compile VIs that reference VIs in the version-independent location on the computer (LVAddons), the VIs in LVAddons are compiled multiple times, which causes the mass compile to take longer to complete.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2024 Q1 | LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Jan 27, 2025

3019996

Bookmark Manager Does Not Display All Bookmarks in Projects Created from Templates
If you create a project from a template which contains VIs with bookmarks, the Bookmark Manager doesn't display those bookmarks until you modify them.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Feb 26, 2025

3011141

Tree Alternating Row Color is Incorrect on First Row if Column Headers Not Visible

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Mar 24, 2025

Offline Help Viewer Installation Fails on Ubuntu 24.04 LTS

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
N/A
Added:
Apr 16, 2025

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:1 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:2 ordinal=2 -->
## JKI Dragon 2024 Q3 Cannot Open LabVIEW 2025 Q1 Projects

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:2 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:3 ordinal=3 -->
## Invoke Node Calling .NET 8 Method Returns Error 1782 if Optional Parameter is Not Wired

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:3 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:4 ordinal=4 -->
## Python Node Returns Error 1667 When Module Path Contains Unicode Characters

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2023 Q1 | LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Jan 27, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:4 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:5 ordinal=5 -->
## Select .NET Core Constructor Dialog Incorrectly Reports No Public Constructors For Classes Not Part of Any Namespace

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:5 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:6 ordinal=6 -->
## Mass Compile Slower Because LabVIEW Does Not Save VIs in LVAddons

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2024 Q1 | LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Jan 27, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:6 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:7 ordinal=7 -->
## Bookmark Manager Does Not Display All Bookmarks in Projects Created from Templates

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Feb 26, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:7 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:8 ordinal=8 -->
## Tree Alternating Row Color is Incorrect on First Row if Column Headers Not Visible

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Mar 24, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:8 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:9 ordinal=9 -->
## Offline Help Viewer Installation Fails on Ubuntu 24.04 LTS

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

N/A

Added:

Apr 16, 2025

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:9 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:10 ordinal=10 -->
## Final Time Issue Listed

Issues found in this section will not be listed in future known issues documents for this product.

There are currently no issues to list.

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:10 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:11 ordinal=11 -->
## Additional Resources

Explore Support Content and Product Documentation

Search the NI KnowledgeBase for a solution

Learn how to get started and use the product

Ask the NI Community

Collaborate with other users in our discussion forums

Search the NI Community for a solution

Request Support from an Engineer

A valid service agreement may be required, and support options vary by country

Open a service request

Purchase or renew support services

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:11 -->

<!--KB_RECORD source=labview-2025-q1-known-issues locator=section:12 ordinal=12 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2025-q1-known-issues locator=section:12 -->

# SOURCE labview-2025-q1-bug-fixes

- title: LabVIEW 2025 Q1 Bug Fixes
- category: bug-fixes
- url: https://www.ni.com/en/support/documentation/bugs/25/labview-2025-q1-bug-fixes.html
- source_sha256: c9b28089726702eef04a617b3d3ec65b736a94530771bc083fdca31f53eebdfc
- versions: ["2025 Q1"]

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:1 ordinal=1 -->
## Overview

The following items are notable issues fixed between the release of LabVIEW 2024 Q3 and LabVIEW 2025 Q1, including additional patches and service packs. If you have an issue ID, you can search this list to validate that the issue has been fixed. This is not an exhaustive list of issues fixed in the current version of LabVIEW.

Bug Number

Legacy ID

Description

Details

2785983

LabVIEW Sometimes Prompts to Save Unedited VIs
LabVIEW may prompt to save VIs that reference shared libraries, including some VIs in the Electrical Power Toolkit. Not saving VIs can make deployment to Real-Time targets fail.

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jul 17, 2024

2750819

LabVIEW Crashes After Running VI With Timed Sequence Configured With -1 Priority on First Frame

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2782364

Ctrl+Shift+Scroll Wheel Does Not Change Frames of Block Diagram Structure When Mouse Is Positioned Over Nested Structure
When using Ctrl+Shift+scroll wheel to change the visible frame of a structure on a VI block diagram, if the cursor moves over a single-frame nested structure (such as a For Loop), the gesture stops changing the visible frame.

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2019
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2786118

LabVIEW SSH API Does Not Support Trust On First Use

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2819419

Application Using ADCS Library Is Broken Because of Missing subTimeDelay.vi

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2836079

LabVIEW May Report Erroneous Save Version Compatibility Issues When Debugging Built Applications

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2816478

LabVIEW Does Not Cache Compilation Results During Mass Compile of VIs Saving to Previous Versions

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2843028

LabVIEW Incorrectly Coerces Large Values Entered in Graph Axis Scale Labels
LabVIEW sometimes incorrectly coerces large values entered into the maximum scale value to -1.

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2843576

LabVIEW May Crash After Resizing Objects After Using Find Control on Subpanel
Using the Find Control right-click menu option on a subpanel reference may incorrectly select both the subpanel and the tab control that contains it. If you use the Resize Objects commands with both the subpanel and the tab control selected, LabVIEW crashes.

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2870271

Built Applications Include Unnecessary Help Files
When building an application from VIs that use CHM files for Help, the CHM files are erroneously included in the output of the build.

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2917738

Exported EMF Images Display Rotated Text as Black Boxes

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2921563

Setting Listbox Top Row Property to High Numbers Returns Error 1077
The Top Row property for the Listbox returns Error 1077 if set to a value higher than the maximum value of a 16-bit signed integer even though the data type of the property is 32-bit signed integer

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2927890

LabVIEW Can Crash When Writing 2D Array of Variant to File

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2946291

LabVIEW Sometimes Erroneously Searches for VIs When Using Project Save Version
If you create a project that uses Trim Whitespace and save it to an earlier version of LabVIEW using the Project Save Version, then when you open the project in an older version of LabVIEW, it can search for subVIs of Trim Whitespace that were not present in that earlier version.

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2830041

Compare Hierarchies Incorrectly Reports Difference When Identical VIs Call a .NET Framework Assembly

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2923306

LabVIEW Crashes When Executing Exported Function CallChain()

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2858647

NI Distributed System Manager Cannot Browse Network Items for Bind to Source
When configuring a variable in NI Distributed System Manager, if you select the Bind to Source option and click Browse, all the network items are grayed and disabled.

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2923230

LabVIEW Web Service Does Not Clear All Temporary Files

Workaround:
Fixed in LabVIEW 2025 Q1.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q1
Added:
Jan 30, 2025

2959404

Some Builds That Include Express VIs or Malleable VIs Produce Erroneous Missing Dependencies
Builds that do not utilize the latest Application Builder cache, such as all build specifications under RT Targets and any Source Distributions, may erroneously break callers of Express VIs and Malleable VIs. For executable (.exe) files, this often results in error 1003. Build artifacts from other build specification types can be loaded in the LabVIEW development environment to obtain more detailed error information where missing dependencies are reported.

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q1 Patch 1
Added:
Jan 30, 2025

2980565

LabVIEW for Linux Base and Full Versions Report Error 1003 When Creating Source Distributions

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q1 Patch 1
Added:
Jan 30, 2025

2997898

LabVIEW Sometimes Crashes with DAbort 0x0F1903CE
During some editing and scripting operations (including DQMH code generation), LabVIEW will crash and display the following message: "DAbort 0x0F1903CE: Should never have already existing class when patching the thing that is loading the class!"

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q1 Patch 1
Added:
Jan 30, 2025

3008437

Select .NET Core Constructor Does Not List Some Expected Constructors
When you use the Select .NET Core Constructor dialog with an assembly that is strongly named and has dependencies located in the same folder, LabVIEW does not present the expected constructors.

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 2.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q1 Patch 2
Added:
Feb 21, 2025

3022567

LabVIEW Built Application Crashes With Access Violation at EIP=0x5C81DFEC

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1 Patch 2
Added:
Mar 21, 2025

2945908

LabVIEW Sometimes Crashes With Internal Error 0xE59037CA
After opening some class member VIs, LabVIEW crashes with error 0xE59037CA at SliceSupport.cpp, line 58.

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1 Patch 2
Added:
Mar 21, 2025

3013891

Vulnerabilities CVE-2025-2629, CVE-2025-2630, CVE-2025-2631 and CVE-2025-2632
Fixed DLL Hijacking vulnerabilities due to uncontrolled search path identified as CVE-2025-2629 and CVE-2025-2630 Fixed out of bounds write vulnerabilities due to improper bounds checking identified as CVE-2025-2631 and CVE-2025-2632

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 2.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q1 Patch 2
Added:
Mar 21, 2025

3036893

Vulnerability CVE-2025-7361
Fixed Vulnerability CVE-2025-7361. LabVIEW no longer supports Code Interface Nodes unless the configuration file contains EnableCodeInterfaceNodes=True.

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q1 Patch 3
Added:
Aug 1, 2025

3064741

Command Window Appears When Running Installer Built by LabVIEW

Workaround:
Fixed in LabVIEW 2025 Q1 Patch 3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q1 Patch 3
Added:
Aug 1, 2025

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:1 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:2 ordinal=2 -->
## LabVIEW Sometimes Prompts to Save Unedited VIs

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jul 17, 2024

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:2 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:3 ordinal=3 -->
## LabVIEW Crashes After Running VI With Timed Sequence Configured With -1 Priority on First Frame

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:3 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:4 ordinal=4 -->
## Ctrl+Shift+Scroll Wheel Does Not Change Frames of Block Diagram Structure When Mouse Is Positioned Over Nested Structure

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2019

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:4 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:5 ordinal=5 -->
## LabVIEW SSH API Does Not Support Trust On First Use

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:5 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:6 ordinal=6 -->
## Application Using ADCS Library Is Broken Because of Missing subTimeDelay.vi

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:6 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:7 ordinal=7 -->
## LabVIEW May Report Erroneous Save Version Compatibility Issues When Debugging Built Applications

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:7 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:8 ordinal=8 -->
## LabVIEW Does Not Cache Compilation Results During Mass Compile of VIs Saving to Previous Versions

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:8 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:9 ordinal=9 -->
## LabVIEW Incorrectly Coerces Large Values Entered in Graph Axis Scale Labels

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:9 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:10 ordinal=10 -->
## LabVIEW May Crash After Resizing Objects After Using Find Control on Subpanel

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:10 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:11 ordinal=11 -->
## Built Applications Include Unnecessary Help Files

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:11 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:12 ordinal=12 -->
## Exported EMF Images Display Rotated Text as Black Boxes

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:12 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:13 ordinal=13 -->
## Setting Listbox Top Row Property to High Numbers Returns Error 1077

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:13 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:14 ordinal=14 -->
## LabVIEW Can Crash When Writing 2D Array of Variant to File

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:14 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:15 ordinal=15 -->
## LabVIEW Sometimes Erroneously Searches for VIs When Using Project Save Version

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:15 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:16 ordinal=16 -->
## Compare Hierarchies Incorrectly Reports Difference When Identical VIs Call a .NET Framework Assembly

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:16 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:17 ordinal=17 -->
## LabVIEW Crashes When Executing Exported Function CallChain()

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:17 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:18 ordinal=18 -->
## NI Distributed System Manager Cannot Browse Network Items for Bind to Source

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:18 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:19 ordinal=19 -->
## LabVIEW Web Service Does Not Clear All Temporary Files

Workaround:

Fixed in LabVIEW 2025 Q1.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:19 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:20 ordinal=20 -->
## Some Builds That Include Express VIs or Malleable VIs Produce Erroneous Missing Dependencies

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q1 Patch 1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:20 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:21 ordinal=21 -->
## LabVIEW for Linux Base and Full Versions Report Error 1003 When Creating Source Distributions

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q1 Patch 1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:21 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:22 ordinal=22 -->
## LabVIEW Sometimes Crashes with DAbort 0x0F1903CE

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q1 Patch 1

Added:

Jan 30, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:22 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:23 ordinal=23 -->
## Select .NET Core Constructor Does Not List Some Expected Constructors

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q1 Patch 2

Added:

Feb 21, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:23 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:24 ordinal=24 -->
## LabVIEW Built Application Crashes With Access Violation at EIP=0x5C81DFEC

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1 Patch 2

Added:

Mar 21, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:24 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:25 ordinal=25 -->
## LabVIEW Sometimes Crashes With Internal Error 0xE59037CA

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1 Patch 2

Added:

Mar 21, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:25 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:26 ordinal=26 -->
## Vulnerabilities CVE-2025-2629, CVE-2025-2630, CVE-2025-2631 and CVE-2025-2632

Fixed DLL Hijacking vulnerabilities due to uncontrolled search path identified as CVE-2025-2629 and CVE-2025-2630

Workaround:

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q1 Patch 2

Added:

Mar 21, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:26 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:27 ordinal=27 -->
## Vulnerability CVE-2025-7361

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q1 Patch 3

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:27 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:28 ordinal=28 -->
## Command Window Appears When Running Installer Built by LabVIEW

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q1 Patch 3

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:28 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:29 ordinal=29 -->
## Additional Patch Information

Installing some patches may require certain additional steps or considerations. Please refer to the following table for more information about patches for this release.

These patches currently do not have any special instructions.

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:29 -->

<!--KB_RECORD source=labview-2025-q1-bug-fixes locator=section:30 ordinal=30 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2025-q1-bug-fixes locator=section:30 -->

# SOURCE labview-2025-q3-known-issues

- title: LabVIEW 2025 Q3 Known Issues
- category: known-issues
- url: https://www.ni.com/en/support/documentation/bugs/25/labview-2025-q3-known-issues.html
- source_sha256: e10f4881e19e0547c9a542bf4f1668d66a0c1518c082c8656227ef08ee355f69
- versions: ["2025 Q3"]

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:1 ordinal=1 -->
## Overview

This document contains the LabVIEW known issues that were discovered before and since the release of LabVIEW 2025 Q3. Known issues are performance issues or technical bugs that NI has acknowledged exist within this version of the product.

Not every issue known to NI appears on this list; it is intended to show the most severe and common issues that you may encounter and provide workarounds when possible. Other technical issues that you may encounter could occur through normal product use or system compatibility issues. You may find more information on these issues in NI’s Product Documentation, Knowledgebase, or Community; see Additional Resources.

Bug Number

Legacy ID

Description

Details

3169574

Offline Help Viewer Not Available on Linux
On Linux systems, the Offline Help Viewer application either is not installed or fails to launch.

Workaround:
Use the online help or refer to NI Offline Help Viewer is Crashing on My Linux Installation for possible workarounds.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 1, 2025

3162143

Clipboard Listed in Debug Window
If you copy a portion of a diagram that includes a breakpoint, the Clipboard will be listed in the Debug Window.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 1, 2025

3077846

Constructor Node Does Not Allow Selection of Default Constructor for Non-Static Struct in .NET 8 Assembly

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 1, 2025

3129051

LabVIEW Prompts to Save Temporary VIs Used to Create VI Snippets
After creating a VI Snippet, LabVIEW asks to save an Untitled VI when closing your project. LabVIEW creates the temporary VI to build the VI snippet but fails to dispose of it properly.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 1, 2025

3152132

LabVIEW Erroneously Saves Breakpoint After You Remove Breakpoint in Dynamic Dispatch VI While Paused

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 8, 2025

3154235

Selecting Browse in Property and Invoke Nodes Configured for .NET Core Does Not Open Browse Dialog

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 8, 2025

3161664

LabVIEW Invoke Node Configured to .NET Core Method with Array In/Out Parameter Does Not Provide Output Terminal

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 8, 2025

3166968

LabVIEW Does Not Update the VI Name in the Debug Window After Renaming a VI in Project Configured to Use a Previous Save Version

Workaround:
Remove the probes and breakpoints listed under the VI in the Debug window. When you add your probes and breakpoints again, the Debug window will display the updated VI name.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 11, 2025

3173129

Scan from String Does Not Return Expected Error
If you set a format string that includes %I and %p (12-hour format PM/AM) in a "Scan From String" function and write an Input String that doesn't respect this format, the function does not return an error and the output will be: 12:00:00.000 PM 12/31/1903.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2021 | LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 8, 2025

3178201

LabVIEW Sometimes Crashes After Selecting Right-Click Help For Engine on a Variable Property Node

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 8, 2025

3192954

Search with Nigel Search Bar Does Not Find Add-On Content
When you search using the Search with Nigel search bar, it does not find palette items that were installed after the Nigel search cache was created.

Workaround:
In LabVIEW 2025 Q3 Patch 2 or later, restart LabVIEW. In LabVIEW 2025 Q3 (Patch 1), close LabVIEW and delete the %temp%\LabVIEW Nigel search cache folder.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 15, 2025

3019996

Bookmark Manager Does Not Display All Bookmarks in Projects Created from Templates
If you create a project from a template which contains VIs with bookmarks, the Bookmark Manager doesn't display those bookmarks until you modify them.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 16, 2025

3184572

Refnum Palette Contains Extraneous .NET Core Refnum
In the Controls palette, the .NET Core Refnum is functionally identical to the .NET Refnum.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 18, 2025

3192209

Export Data To Clipboard in Debug Window Doesn't Enable Pasting the Data Inside LabVIEW
When you probe a wire and right-click in the Debug Window to Export Data To Clipboard, you can paste the value in external applications. But if you paste in LabVIEW, you get whatever was previously on the clipboard.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Jul 18, 2025

3231187

LabVIEW 2025 Q3 Community Edition for Windows Incorrectly Includes Nigel AI Advisor
The installer for LabVIEW 2025 Q3 Community Edition includes the Nigel AI Advisor, but to use Nigel you must have an active subscription license, multi-seat license, or Software Service Program for LabVIEW Professional.

Workaround:
Deselect NI Nigel AI Advisor for LabVIEW 2025 when setting up your LabVIEW Community Edition installation.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
N/A
Added:
Aug 13, 2025

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:1 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:2 ordinal=2 -->
## Offline Help Viewer Not Available on Linux

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:2 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:3 ordinal=3 -->
## Clipboard Listed in Debug Window

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:3 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:4 ordinal=4 -->
## Constructor Node Does Not Allow Selection of Default Constructor for Non-Static Struct in .NET 8 Assembly

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:4 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:5 ordinal=5 -->
## LabVIEW Prompts to Save Temporary VIs Used to Create VI Snippets

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:5 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:6 ordinal=6 -->
## LabVIEW Erroneously Saves Breakpoint After You Remove Breakpoint in Dynamic Dispatch VI While Paused

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:6 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:7 ordinal=7 -->
## Selecting Browse in Property and Invoke Nodes Configured for .NET Core Does Not Open Browse Dialog

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:7 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:8 ordinal=8 -->
## LabVIEW Invoke Node Configured to .NET Core Method with Array In/Out Parameter Does Not Provide Output Terminal

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:8 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:9 ordinal=9 -->
## LabVIEW Does Not Update the VI Name in the Debug Window After Renaming a VI in Project Configured to Use a Previous Save Version

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 11, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:9 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:10 ordinal=10 -->
## Scan from String Does Not Return Expected Error

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2021 | LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:10 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:11 ordinal=11 -->
## LabVIEW Sometimes Crashes After Selecting Right-Click Help For Engine on a Variable Property Node

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:11 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:12 ordinal=12 -->
## Search with Nigel Search Bar Does Not Find Add-On Content

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 15, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:12 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:13 ordinal=13 -->
## Bookmark Manager Does Not Display All Bookmarks in Projects Created from Templates

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 16, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:13 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:14 ordinal=14 -->
## Refnum Palette Contains Extraneous .NET Core Refnum

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:14 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:15 ordinal=15 -->
## Export Data To Clipboard in Debug Window Doesn't Enable Pasting the Data Inside LabVIEW

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:15 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:16 ordinal=16 -->
## LabVIEW 2025 Q3 Community Edition for Windows Incorrectly Includes Nigel AI Advisor

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

N/A

Added:

Aug 13, 2025

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:16 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:17 ordinal=17 -->
## Final Time Issue Listed

Issues found in this section will not be listed in future known issues documents for this product.

There are currently no issues to list.

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:17 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:18 ordinal=18 -->
## Additional Resources

Explore Support Content and Product Documentation

Search the NI KnowledgeBase for a solution

Learn how to get started and use the product

Ask the NI Community

Collaborate with other users in our discussion forums

Search the NI Community for a solution

Request Support from an Engineer

A valid service agreement may be required, and support options vary by country

Open a service request

Purchase or renew support services

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:18 -->

<!--KB_RECORD source=labview-2025-q3-known-issues locator=section:19 ordinal=19 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2025-q3-known-issues locator=section:19 -->

# SOURCE labview-2025-q3-bug-fixes

- title: LabVIEW 2025 Q3 Bug Fixes
- category: bug-fixes
- url: https://www.ni.com/en/support/documentation/bugs/25/labview-2025-q3-bug-fixes.html
- source_sha256: a8f8d59aceb698ba5933cb8311bef0a56117390e01f36eb524d3126c60330823
- versions: ["2025 Q3"]

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:1 ordinal=1 -->
## Overview

The following items are notable issues fixed between the release of LabVIEW 2025 Q1 and LabVIEW 2025 Q3, including additional patches and service packs. If you have an issue ID, you can search this list to validate that the issue has been fixed. This is not an exhaustive list of issues fixed in the current version of LabVIEW.

Bug Number

Legacy ID

Description

Details

2855444

Python Node With Object Refnum Input Returns Error 1744 After Repeated Calls
When using a Python Node with a Python object refnum as an input, LabVIEW returns error 1744 after 1,048,576 calls.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

2972983

Select .NET Core Constructor Dialog Incorrectly Reports No Public Constructors For Classes Not Part of Any Namespace
If you select a class that is not part of any namespace in the Select .NET Core Constructor dialog, the message This class contains no public constructors is displayed, even if the class does contain public constructors.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3005689

LabVIEW Does Not Detect When LabVIEW Class Should Be Broken Because Its Private Data Includes Set or Map That Contains the Class

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2019
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3006536

.NET Refnum Control Is Missing Select .NET Core Class Right-Click Menu

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3008439

Constructor Node for .NET Core Does Not Include Exception Details with Error 1172

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3039297

Simple Numeric Constant Created Instead of Ring When Creating Constant from Ring Typed Terminal of LabVIEW Class Property Node

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3066513

Calls to .NET Core Methods With Multiple Return Values Do Not Return Values to Output Parameters
If you call a .NET Core method that uses the out keyword to have multiple return values, LabVIEW does not correctly return those values.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3066525

.NET Core Enumerations Are Treated As References
LabVIEW can pass numeric values to and from .NET Framework properties and method parameters, but when using .NET Core properties and methods, you must use references instead. This limitation requires you to write extra code to get and set values on the reference.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3073490

LabVIEW Crashes When Outputs on .NET Core Property or Invoke Nodes Are Unwired

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3077738

LabVIEW Sometimes Crashes With .NET Core Methods Using Arrays of Strings

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3144001, 3166958

Vulnerabilities CVE-2025-2633 and CVE-2025-2634
Fixed Vulnerabilities CVE-2025-2633 and CVE-2025-2634.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

2941475

Text Entry Renders Incorrectly in Table Cells with Centered Text

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

2963459

Python Node Returns Error 1667 When Module Path Contains Unicode Characters

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2023 Q1 | LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

2974910

Configuration Dialog Missing for Fixed Point Shared Variable

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3126088

Web Service URL Limited to 512 Characters

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

2918538

Compile Error When Using Not A Number/Path/Refnum Function with Dynamic Data

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

2922757

Cannot Edit Enum Array Element By Holding Ctrl Key and Clicking the Element

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2020 SP1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

2930247

Mass Compile Slower Because LabVIEW Does Not Save VIs in LVAddons
When you mass compile VIs that reference VIs in the version-independent location on the computer (LVAddons), the VIs in LVAddons are compiled multiple times, which causes the mass compile to take longer to complete.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2024 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3003728

LabVIEW Sometimes Crashes After Reordering Controls on Page of Tab Control

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2024 Q3
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3011141

Tree Alternating Row Color is Incorrect on First Row if Column Headers Not Visible

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3029109

VI Window Sometimes Positioned Incorrectly When VI Properties for Window Position and Panel Size Are Set
When a VI has both Window Position and Panel Size configured to non-default values in its Properties, the run-time position of the window can be incorrect.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3040552

LabVIEW Sometimes Crashes After Replacing Tab Control with Another Tab Control

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3042977

Probe Display of XML Reference Does Not Display Correct Value

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2023 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3044350

LabVIEW Does Not Report Save Compatibility Issue with Splitter Bars When Saving to Versions Earlier than 19.0

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3045969

LabVIEW Crashes When Executing Replace No Attributes Method on Tab Control

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3050230

Debug Write.vim Erroneously Displays Last Element of Non-string Array At Beginning of Debug String

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3058541

Some Mixed Signal Graph Plots Do Not Display Plot Area Foreground Image
When a Mixed Signal Graph has the "Plot Images:Front" property set, only the first plot displays the image.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3160785

No Value Change Event Fired After Deleting Array Element With Ctrl+Del Keyboard Shortcut

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3161234

Reentrant VIs Sometimes Lose Reentrancy Setting Unexpectedly in Project Configured With a Save Version Earlier Than the Editor Version

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3162353

Controls In Built Applications Do Not Receive Mouse Wheel Event If Ctrl Key Is Also Pressed

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3168519

LabVIEW Does Not Detect Save Incompatibility for Concatenate Strings in Save Versions Prior to 21.0

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

1554661

Error 1055 in VISL_findDependentVISvr.vi when Building Executable
Error 1055 sometimes occurs when building an EXE with the LabVIEW DSC Module installed.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2019 SP1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3036893

Vulnerability CVE-2025-7361
Fixed Vulnerability CVE-2025-7361. LabVIEW no longer supports Code Interface Nodes unless the configuration file contains EnableCodeInterfaceNodes=True.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2023 Q3
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3075204

Vulnerabilities CVE-2025-7848 and CVE-2025-7849
Fixed Memory Corruption Vulnerabilities CVE-2025-7848 and CVE-2025-7849.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3
Added:
Aug 1, 2025

3064741

Command Window Appears When Running Installer Built by LabVIEW

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Aug 1, 2025

3063044

VI Comparison Report Can Show Incorrect Text Value Change for Caption
In some cases, a caption text value change can have the "from" and "to" strings in the wrong order.

Workaround:
Fixed in LabVIEW 2025 Q3.

Reported Version:
LabVIEW 2025 Q1
Resolved Version:
LabVIEW 2025 Q3
Added:
Jul 1, 2025

3181565

Creating VI Comparison Report Can Delete Destination Folder
When creating a VI Comparison report in HTML, HTML single file, or XML format, if a folder with same name as the report exists in the specified destination, the folder and all its contents will be deleted.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Jul 8, 2025

3183388

Applications Using Code Interface Nodes Cannot Run With LabVIEW 2025 Q3 Run-Time Engine
If you build an application in LabVIEW 2025 Q3 that uses Code Interface Nodes (CINs), it will not execute. Also, if you install the 2025 Q3 LabVIEW Run-Time Engine on a system where an application uses both CINs and the setting to allow future versions of the LabVIEW Runtime to run this application, the application will no longer execute.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Jul 8, 2025

3179057

Internal warning 0x558A98DB: "undo.cpp", line 5422 When Removing Breakpoint from Reentrant Clones in Debug Window
After you remove a breakpoint from a reentrant clone in the Debug window, LabVIEW will display Internal warning 0x558A98DB: "undo.cpp", line 5422. The breakpoint will be removed from the reentrant original and all clones.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Jul 9, 2025

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:1 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:2 ordinal=2 -->
## Python Node With Object Refnum Input Returns Error 1744 After Repeated Calls

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:2 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:3 ordinal=3 -->
## Select .NET Core Constructor Dialog Incorrectly Reports No Public Constructors For Classes Not Part of Any Namespace

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:3 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:4 ordinal=4 -->
## LabVIEW Does Not Detect When LabVIEW Class Should Be Broken Because Its Private Data Includes Set or Map That Contains the Class

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2019

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:4 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:5 ordinal=5 -->
## .NET Refnum Control Is Missing Select .NET Core Class Right-Click Menu

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:5 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:6 ordinal=6 -->
## Constructor Node for .NET Core Does Not Include Exception Details with Error 1172

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:6 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:7 ordinal=7 -->
## Simple Numeric Constant Created Instead of Ring When Creating Constant from Ring Typed Terminal of LabVIEW Class Property Node

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:7 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:8 ordinal=8 -->
## Calls to .NET Core Methods With Multiple Return Values Do Not Return Values to Output Parameters

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:8 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:9 ordinal=9 -->
## .NET Core Enumerations Are Treated As References

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:9 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:10 ordinal=10 -->
## LabVIEW Crashes When Outputs on .NET Core Property or Invoke Nodes Are Unwired

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:10 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:11 ordinal=11 -->
## LabVIEW Sometimes Crashes With .NET Core Methods Using Arrays of Strings

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:11 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:12 ordinal=12 -->
## Vulnerabilities CVE-2025-2633 and CVE-2025-2634

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:12 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:13 ordinal=13 -->
## Text Entry Renders Incorrectly in Table Cells with Centered Text

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:13 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:14 ordinal=14 -->
## Python Node Returns Error 1667 When Module Path Contains Unicode Characters

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2023 Q1 | LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:14 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:15 ordinal=15 -->
## Configuration Dialog Missing for Fixed Point Shared Variable

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:15 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:16 ordinal=16 -->
## Web Service URL Limited to 512 Characters

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:16 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:17 ordinal=17 -->
## Compile Error When Using Not A Number/Path/Refnum Function with Dynamic Data

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:17 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:18 ordinal=18 -->
## Cannot Edit Enum Array Element By Holding Ctrl Key and Clicking the Element

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2020 SP1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:18 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:19 ordinal=19 -->
## Mass Compile Slower Because LabVIEW Does Not Save VIs in LVAddons

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2024 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:19 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:20 ordinal=20 -->
## LabVIEW Sometimes Crashes After Reordering Controls on Page of Tab Control

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2024 Q3

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:20 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:21 ordinal=21 -->
## Tree Alternating Row Color is Incorrect on First Row if Column Headers Not Visible

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:21 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:22 ordinal=22 -->
## VI Window Sometimes Positioned Incorrectly When VI Properties for Window Position and Panel Size Are Set

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:22 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:23 ordinal=23 -->
## LabVIEW Sometimes Crashes After Replacing Tab Control with Another Tab Control

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:23 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:24 ordinal=24 -->
## Probe Display of XML Reference Does Not Display Correct Value

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2023 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:24 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:25 ordinal=25 -->
## LabVIEW Does Not Report Save Compatibility Issue with Splitter Bars When Saving to Versions Earlier than 19.0

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:25 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:26 ordinal=26 -->
## LabVIEW Crashes When Executing Replace No Attributes Method on Tab Control

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:26 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:27 ordinal=27 -->
## Debug Write.vim Erroneously Displays Last Element of Non-string Array At Beginning of Debug String

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:27 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:28 ordinal=28 -->
## Some Mixed Signal Graph Plots Do Not Display Plot Area Foreground Image

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:28 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:29 ordinal=29 -->
## No Value Change Event Fired After Deleting Array Element With Ctrl+Del Keyboard Shortcut

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:29 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:30 ordinal=30 -->
## Reentrant VIs Sometimes Lose Reentrancy Setting Unexpectedly in Project Configured With a Save Version Earlier Than the Editor Version

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:30 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:31 ordinal=31 -->
## Controls In Built Applications Do Not Receive Mouse Wheel Event If Ctrl Key Is Also Pressed

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:31 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:32 ordinal=32 -->
## LabVIEW Does Not Detect Save Incompatibility for Concatenate Strings in Save Versions Prior to 21.0

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:32 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:33 ordinal=33 -->
## Error 1055 in VISL_findDependentVISvr.vi when Building Executable

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2019 SP1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:33 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:34 ordinal=34 -->
## Vulnerability CVE-2025-7361

Workaround:

Reported Version:

LabVIEW 2023 Q3

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:34 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:35 ordinal=35 -->
## Vulnerabilities CVE-2025-7848 and CVE-2025-7849

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:35 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:36 ordinal=36 -->
## Command Window Appears When Running Installer Built by LabVIEW

Workaround:

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:36 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:37 ordinal=37 -->
## VI Comparison Report Can Show Incorrect Text Value Change for Caption

Workaround:

Fixed in LabVIEW 2025 Q3.

Reported Version:

LabVIEW 2025 Q1

Resolved Version:

LabVIEW 2025 Q3

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:37 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:38 ordinal=38 -->
## Creating VI Comparison Report Can Delete Destination Folder

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:38 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:39 ordinal=39 -->
## Applications Using Code Interface Nodes Cannot Run With LabVIEW 2025 Q3 Run-Time Engine

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:39 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:40 ordinal=40 -->
## Internal warning 0x558A98DB: "undo.cpp", line 5422 When Removing Breakpoint from Reentrant Clones in Debug Window

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Jul 9, 2025

Bug Number

Legacy ID

Description

Details

3192961

LabVIEW Sometimes Displays Error Message When Searching With Nigel
If you use "Search with Nigel" in a VI toolbar before logging in to your NI User Account in the Nigel AI chat window, you will see a message that instructs you to log in. After logging in and using "Search with Nigel" again, you might see an error message that says: "Not enough memory to complete this operation."

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Aug 1, 2025

3195661

LabVIEW Options Dialog Erroneously Display Search Category
The Tools»Options dialog erroneously contains a Search category. Changing the settings in this category does not affect your LabVIEW settings.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Aug 1, 2025

3206439

LabVIEW Does Not List All Methods and Properties from .NET 8.0 Parent Interfaces
When you are configuring Invoke and Property nodes with .NET 8.0 assemblies, you might not see methods and properties from parent interfaces.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Aug 1, 2025

3188618

LabVIEW for Linux in Docker Container Exits After LabVIEWCLI Operation
When LabVIEW 2025 Q3 for Linux is running in a Docker Container, LabVIEW closes after running a LabVIEWCLI operation. This causes the following behaviors: Running multiple operations will be slower than expected. The CloseLabVIEW operation will return error -350000.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Jul 18, 2025

3192873

Password Authentication for OpenSSH SSH and SFTP VIs on Windows Fails with Error 42
When using OpenSSH with SSH and SFTP functions, using password authentication will fail and return error 42.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Jul 18, 2025

3192981

LabVIEW Crashes After Using Ctrl+Shift+Mouse Wheel Over a Flat Sequence Structure

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q1 | LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Jul 18, 2025

3193066

VIs Can Be Placed In Wrong Folders When Building Applications
Built VIs can be in unexpected destinations after building an application or library that includes an already-built Packed Library. This might include VIs being placed into a destination folder other than their caller.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Jul 18, 2025

3208367

VI Sometimes Erroneously Broken When Calling Property Node of a LabVIEW Class

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 2.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 2
Added:
Aug 4, 2025

3429940

Vulnerabilities CVE-2025-64461, CVE-2025-64462, CVE-2025-64463, CVE-2025-64464, CVE-2025-64465, CVE-2025-64466, CVE-2025-64467, CVE-2025-64468, and CVE-2025-64469
Fixed memory corruption issues that crash LabVIEW when loading specifically corrupted VIs: CVE-2025-64461, CVE-2025-64462, CVE-2025-64463, CVE-2025-64464, CVE-2025-64465, CVE-2025-64466, CVE-2025-64467, CVE-2025-64468, CVE-2025-64469

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 3.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 3
Added:
Dec 15, 2025

3240023

LabVIEW Community Edition Sometimes Fails to Activate
LabVIEW Community Edition for macOS and LabVIEW Community Edition for Linux experience intermittent failures when calling the ni.com service that checks a user account for an entitlement. These failures occur because the response from the service can take longer than the timeout.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 3.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 3
Added:
Dec 15, 2025

3238098

Additional Installer Settings in Installer Build Specification Display Garbled Characters in LabVIEW Korean and Japanese Versions

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 3.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 3
Added:
Dec 15, 2025

3229719

Delete Key Erroneously Removes Breakpoint or Probe When Renaming It in Debug Window

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 3.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 3
Added:
Dec 15, 2025

3228347

LabVIEW Crashes When Right-Clicking on Wires with Void Data Types

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 3.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 3
Added:
Dec 15, 2025

3280357

LabVIEW Crashes When Building Packed Library if Build Depends on a Packed Library that Depends on a Shared Library

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 3.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 3
Added:
Dec 15, 2025

3743979

Vulnerability CVE-2026-32861
Fixed out-of-bounds write vulnerability when opening a specifically corrupted .lvclass file: CVE-2026-32861.

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 4

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 4
Added:
Mar 16, 2026

3749030

Vulnerability CVE-2026-32860
Fixed out-of-bounds write vulnerability when opening a specifically corrupted .lvlib file: CVE-2026-32860

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 4

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 4
Added:
Mar 16, 2026

3749034

Vulnerabilities CVE-2026-32862, CVE-2026-32863, and CVE-2026-32864
Fixed memory corruption vulnerabilities when loading specifically corrupted VIs: CVE-2026-32862, CVE-2026-32863, CVE-2026-32864

Workaround:
Fixed in LabVIEW 2025 Q3 Patch 4

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2025 Q3 Patch 4
Added:
Mar 16, 2026

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:40 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:41 ordinal=41 -->
## LabVIEW Sometimes Displays Error Message When Searching With Nigel

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:41 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:42 ordinal=42 -->
## LabVIEW Options Dialog Erroneously Display Search Category

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:42 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:43 ordinal=43 -->
## LabVIEW Does Not List All Methods and Properties from .NET 8.0 Parent Interfaces

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Aug 1, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:43 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:44 ordinal=44 -->
## LabVIEW for Linux in Docker Container Exits After LabVIEWCLI Operation

Running multiple operations will be slower than expected.

The CloseLabVIEW operation will return error -350000.

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:44 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:45 ordinal=45 -->
## Password Authentication for OpenSSH SSH and SFTP VIs on Windows Fails with Error 42

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:45 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:46 ordinal=46 -->
## LabVIEW Crashes After Using Ctrl+Shift+Mouse Wheel Over a Flat Sequence Structure

Workaround:

Reported Version:

LabVIEW 2025 Q1 | LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:46 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:47 ordinal=47 -->
## VIs Can Be Placed In Wrong Folders When Building Applications

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:47 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:48 ordinal=48 -->
## VI Sometimes Erroneously Broken When Calling Property Node of a LabVIEW Class

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 2

Added:

Aug 4, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:48 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:49 ordinal=49 -->
## Vulnerabilities CVE-2025-64461, CVE-2025-64462, CVE-2025-64463, CVE-2025-64464, CVE-2025-64465, CVE-2025-64466, CVE-2025-64467, CVE-2025-64468, and CVE-2025-64469

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 3

Added:

Dec 15, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:49 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:50 ordinal=50 -->
## LabVIEW Community Edition Sometimes Fails to Activate

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 3

Added:

Dec 15, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:50 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:51 ordinal=51 -->
## Additional Installer Settings in Installer Build Specification Display Garbled Characters in LabVIEW Korean and Japanese Versions

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 3

Added:

Dec 15, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:51 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:52 ordinal=52 -->
## Delete Key Erroneously Removes Breakpoint or Probe When Renaming It in Debug Window

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 3

Added:

Dec 15, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:52 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:53 ordinal=53 -->
## LabVIEW Crashes When Right-Clicking on Wires with Void Data Types

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 3

Added:

Dec 15, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:53 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:54 ordinal=54 -->
## LabVIEW Crashes When Building Packed Library if Build Depends on a Packed Library that Depends on a Shared Library

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 3

Added:

Dec 15, 2025

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:54 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:55 ordinal=55 -->
## Vulnerability CVE-2026-32861

Workaround:

Fixed in LabVIEW 2025 Q3 Patch 4

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 4

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:55 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:56 ordinal=56 -->
## Vulnerability CVE-2026-32860

Workaround:

Fixed in LabVIEW 2025 Q3 Patch 4

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 4

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:56 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:57 ordinal=57 -->
## Vulnerabilities CVE-2026-32862, CVE-2026-32863, and CVE-2026-32864

Workaround:

Fixed in LabVIEW 2025 Q3 Patch 4

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2025 Q3 Patch 4

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:57 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:58 ordinal=58 -->
## Additional Patch Information

Installing some patches may require certain additional steps or considerations. Please refer to the following table for more information about patches for this release.

These patches currently do not have any special instructions.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

Mac and macOS are trademarks of Apple Inc., registered in the U.S. and other countries and regions.

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:58 -->

<!--KB_RECORD source=labview-2025-q3-bug-fixes locator=section:59 ordinal=59 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2025-q3-bug-fixes locator=section:59 -->

# SOURCE labview-2026-q1-known-issues

- title: LabVIEW 2026 Q1 Known Issues
- category: known-issues
- url: https://www.ni.com/en/support/documentation/bugs/26/labview-2026-q1-known-issues.html
- source_sha256: 20fff6f79613bacb65127a3ba4935d32064fc90982029ee409da8a3cf0776a19
- versions: ["2026 Q1"]

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:1 ordinal=1 -->
## Overview

This document contains the LabVIEW known issues that were discovered before and since the release of LabVIEW 2026 Q1. Known issues are performance issues or technical bugs that NI has acknowledged exist within this version of the product.

Not every issue known to NI appears on this list; it is intended to show the most severe and common issues that you may encounter and provide workarounds when possible. Other technical issues that you may encounter could occur through normal product use or system compatibility issues. You may find more information on these issues in NI’s Product Documentation, Knowledgebase, or Community; see Additional Resources.

Bug Number

Legacy ID

Description

Details

3599848

Localized Versions of LabVIEW Show English Names in Palettes
Space Constant and Command Line String To Path do not have localized names in the String palette.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3454278

LabVIEW May Report Error 1631 When Building a Packed Library

Workaround:
Add this line to the LabVIEW configuration file: NewAppBuilderCache.RemoveLibraryReferences=False

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3600663

JKI Dragon Does Not Always Install Declared Dependencies When Opening LabVIEW Projects
When you open a LabVIEW project that has missing declared dependencies, JKI Dragon may fail to initiate the dependency installation process.

Workaround:
Open the LabVIEW project in LabVIEW and open Project Dependencies from the toolbar to install the missing dependencies manually. Note that you can also open the JKI Dragon application and check for updates. Refer to the release notes for future versions of JKI Dragon for updates on this issue.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3686436

LabVIEW for Linux Reports Error When Installing ni-labview-offline-manual
When installing LabVIEW for Linux, an error message appears that says "Failed to connect to the bus: Did not receive a reply. Possible causes include: the remote application did not send a reply, the message bus security policy blocked the reply, the reply time expired, or the network connection was broken." However, both LabVIEW and the offline help install successfully and function correctly.

Workaround:
Consult How do I resolve errors when installing the offline user manual with the LabVIEW 2026 Q1 Linux ISO installer? for more information on this error.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3695783

LabVIEW Warns That Dependency Was Loaded From New Path When Opening .NET Core Example VI

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 3, 2026

3596234

LabVIEW on Ubuntu 22, RHEL 8, and RHEL 9 Crashes When Selecting Noto Color Emoji Font

Workaround:
Do not use the Noto Color Emoji font on distributions that use versions of libXft older than 2.3.5.

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3697602

VI Does Not Prompt to Save Changes After Removing Disabled Breakpoint
After removing a disabled breakpoint on a VI in LabVIEW 2025 Q3, or on a VI outside of a project in LabVIEW 2026 Q1, the VI is not marked with unsaved changes. Note that VIs in projects in LabVIEW 2026 Q1 store breakpoints in a separate file, so the lack of unsaved changes there is not a bug.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3702292

Initial Position Panel and Diagram for Main.vi in Simple State Machine Project Template Are Not at Top-Left of Monitor

Workaround:
Open [LabVIEW 2026]\ProjectTemplates\Source\Core\Simple State Machine\Main.vi, move its window to the desired initial window position, and save the VI.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3717800

Image Created by Get Conpane Image Method Includes Discuss with Nigel Link

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3231187

LabVIEW 2025 Q3 Community Edition for Windows Incorrectly Includes Nigel AI
The installer for LabVIEW 2026 Q1 Community Edition includes the Nigel AI, but to use Nigel you must have an active subscription license, multi-seat license, or Software Service Program for LabVIEW Professional.

Workaround:
Deselect NI Nigel AI for LabVIEW 2026 when setting up your LabVIEW Community Edition installation.

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Jan 29, 2026

LabVIEW Code Completion with Nigel AI May Suggest Code With Incorrectly Configured Nodes
LabVIEW Code Completion with Nigel AI may suggest code that includes Bundle, Unbundle, Property, and Invoke nodes that aren't configured to match the intended functionality.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3593533

LabVIEW Code Completion Always Prompts Login after Logging in to Nigel AI and Rebooting System
LabVIEW Code Completion always prompts you to log in to Nigel AI the first time you use it after rebooting the system. If you were previously logged in, the Nigel chat window opens and logs in automatically, but you need to repeat your code completion request.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 2, 2026

3700726

LabVIEW Loses Undo History Prior to Code Completion With Nigel AI
If you edit a VI before using Code Completion with Nigel AI, LabVIEW loses your undo history. You cannot use the Undo command to undo these earlier changes.

Workaround:
There is currently no known workaround for this issue.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Feb 3, 2026

3266479

VI Analyzer Toolkit Stops Working in Older Versions of LabVIEW When You Add a Newer Version
VI Analyzer Toolkit for LabVIEW 2024 Q3 and later installs into a shared location (LVAddons) instead of the LabVIEW folder. If you have LabVIEW 2024 Q3, 2025 Q1, or 2025 Q3 installed on your machine and install a newer version of LabVIEW (2025 Q1 or later) on the same machine, the older versions of LabVIEW lose access to VI Analyzer erroneously.

Workaround:
Refer to these documents for more information: VI Analyzer Tests Will Not Load After Installing Newer LabVIEW Version - NI, Missing Example and VI of LabVIEW Toolkit Version 2026 Q1 in LabVIEW 2025 Q3 - NI

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
N/A
Added:
Apr 7, 2026

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:1 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:2 ordinal=2 -->
## Localized Versions of LabVIEW Show English Names in Palettes

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:2 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:3 ordinal=3 -->
## LabVIEW May Report Error 1631 When Building a Packed Library

Workaround:

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:3 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:4 ordinal=4 -->
## JKI Dragon Does Not Always Install Declared Dependencies When Opening LabVIEW Projects

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:4 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:5 ordinal=5 -->
## LabVIEW for Linux Reports Error When Installing ni-labview-offline-manual

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:5 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:6 ordinal=6 -->
## LabVIEW Warns That Dependency Was Loaded From New Path When Opening .NET Core Example VI

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 3, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:6 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:7 ordinal=7 -->
## LabVIEW on Ubuntu 22, RHEL 8, and RHEL 9 Crashes When Selecting Noto Color Emoji Font

Workaround:

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:7 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:8 ordinal=8 -->
## VI Does Not Prompt to Save Changes After Removing Disabled Breakpoint

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:8 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:9 ordinal=9 -->
## Initial Position Panel and Diagram for Main.vi in Simple State Machine Project Template Are Not at Top-Left of Monitor

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:9 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:10 ordinal=10 -->
## Image Created by Get Conpane Image Method Includes Discuss with Nigel Link

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:10 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:11 ordinal=11 -->
## LabVIEW 2025 Q3 Community Edition for Windows Incorrectly Includes Nigel AI

Workaround:

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Jan 29, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:11 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:12 ordinal=12 -->
## LabVIEW Code Completion with Nigel AI May Suggest Code With Incorrectly Configured Nodes

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:12 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:13 ordinal=13 -->
## LabVIEW Code Completion Always Prompts Login after Logging in to Nigel AI and Rebooting System

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:13 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:14 ordinal=14 -->
## LabVIEW Loses Undo History Prior to Code Completion With Nigel AI

Workaround:

There is currently no known workaround for this issue.

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Feb 3, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:14 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:15 ordinal=15 -->
## VI Analyzer Toolkit Stops Working in Older Versions of LabVIEW When You Add a Newer Version

Workaround:

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

N/A

Added:

Apr 7, 2026

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:15 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:16 ordinal=16 -->
## Final Time Issue Listed

Issues found in this section will not be listed in future known issues documents for this product.

There are currently no issues to list.

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:16 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:17 ordinal=17 -->
## Additional Resources

Explore Support Content and Product Documentation

Search the NI KnowledgeBase for a solution

Learn how to get started and use the product

Ask the NI Community

Collaborate with other users in our discussion forums

Search the NI Community for a solution

Request Support from an Engineer

A valid service agreement may be required, and support options vary by country

Open a service request

Purchase or renew support services

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:17 -->

<!--KB_RECORD source=labview-2026-q1-known-issues locator=section:18 ordinal=18 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2026-q1-known-issues locator=section:18 -->

# SOURCE labview-2026-q1-bug-fixes

- title: LabVIEW 2026 Q1 Bug Fixes
- category: bug-fixes
- url: https://www.ni.com/en/support/documentation/bugs/26/labview-2026-q1-bug-fixes.html
- source_sha256: da195dc00142386ed3752569e369676a6e6cdceaaac3a077078753a1a4a05532
- versions: ["2026 Q1"]

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:1 ordinal=1 -->
## Overview

The following items are notable issues fixed between the release of LabVIEW 2025 Q3 and LabVIEW 2026 Q1, including additional patches and service packs. If you have an issue ID, you can search this list to validate that the issue has been fixed. This is not an exhaustive list of issues fixed in the current version of LabVIEW.

Bug Number

Legacy ID

Description

Details

3169574

Offline Help Viewer Not Available on Linux
On Linux systems, the Offline Help Viewer application either is not installed or fails to launch.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 1, 2025

3162143

Clipboard Listed in Debug Window
If you copy a portion of a diagram that includes a breakpoint, the Clipboard will be listed in the Debug Window.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 1, 2025

3077846

Constructor Node Does Not Allow Selection of Default Constructor for Non-Static Struct in .NET 8 Assembly

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 1, 2025

3129051

LabVIEW Prompts to Save Temporary VIs Used to Create VI Snippets
After creating a VI Snippet, LabVIEW asks to save an Untitled VI when closing your project. LabVIEW creates the temporary VI to build the VI snippet but fails to dispose of it properly.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 1, 2025

3152132

LabVIEW Erroneously Saves Breakpoint After You Remove Breakpoint in Dynamic Dispatch VI While Paused

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 8, 2025

3154235

Selecting Browse in Property and Invoke Nodes Configured for .NET Core Does Not Open Browse Dialog

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 8, 2025

3161664

LabVIEW Invoke Node Configured to .NET Core Method with Array In/Out Parameter Does Not Provide Output Terminal

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 8, 2025

3166968

LabVIEW Does Not Update the VI Name in the Debug Window After Renaming a VI in Project Configured to Use a Previous Save Version

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 11, 2025

3173129

Scan from String Does Not Return Expected Error
If you set a format string that includes %I and %p (12-hour format PM/AM) in a "Scan From String" function and write an Input String that doesn't respect this format, the function does not return an error and the output will be: 12:00:00.000 PM 12/31/1903.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2021 | LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 8, 2025

3178201

LabVIEW Sometimes Crashes After Selecting Right-Click Help For Engine on a Variable Property Node

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 8, 2025

3019996

Bookmark Manager Does Not Display All Bookmarks in Projects Created from Templates
If you create a project from a template which contains VIs with bookmarks, the Bookmark Manager doesn't display those bookmarks until you modify them.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 16, 2025

3184572

Refnum Palette Contains Extraneous .NET Core Refnum
In the Controls palette, the .NET Core Refnum is functionally identical to the .NET Refnum.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 18, 2025

3192209

Export Data To Clipboard in Debug Window Doesn't Enable Pasting the Data Inside LabVIEW
When you probe a wire and right-click in the Debug Window to Export Data To Clipboard, you can paste the value in external applications. But if you paste in LabVIEW, you get whatever was previously on the clipboard.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 18, 2025

3192954

Search with Nigel Search Bar Does Not Find Add-On Content
When you search using the Search with Nigel search bar, it does not find palette items that were installed after the Nigel search cache was created.

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1
Added:
Jul 15, 2025

3246143

LabVIEW Sometimes Crashes When Running VI After Placing Diagram Disable Structure

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1
Added:
Feb 3, 2026

3352943

Cannot Set Description and Tip in Constant Linked to a Type Definition

Workaround:
Fixed in LabVIEW 2026 Q1.

Reported Version:
LabVIEW 2020
Resolved Version:
LabVIEW 2026 Q1
Added:
Feb 3, 2026

3766237

LabVIEW Code Completion with Nigel AI in Localized Versions of LabVIEW Never Suggests Some Palette Functions

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

LabVIEW Code Completion with Nigel AI Never Suggests Code Containing Functions from Some NI Driver APIs
LabVIEW Code Completion with Nigel AI lacks support for NI-SCOPE, NI-FGEN, NI-DMM, NI-DCPower, NI-SWITCH, and NI-Digital driver APIs.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3462803, 3742258

Calling .NET (Core) 8.0 Code Leaks Memory

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3712082

LabVIEW Crashes When Displaying Context Help for Polymorphic VI with No Instance VIs

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3716259

Building "My Application" Build Specification in "Actor Framework Template" Project Fails

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3736642

Manage Trusted Files Dialog Takes a Long Time to Populate

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3739525

LabVIEW Sometimes Crashes When Using ExecuteJavaScript and FireUserEvent in Web Browser Control

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3741628

Externally Changed Files List Opens Erroneously When Running Some VI Tools

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3749227

To Lower Case Function Works Incorrectly in LabVIEW for macOS

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3743979

Vulnerability CVE-2026-32861
Fixed out-of-bounds write vulnerability when opening a specifically corrupted .lvclass file: CVE-2026-32861.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3749030

Vulnerability CVE-2026-32860
Fixed out-of-bounds write vulnerability when opening a specifically corrupted .lvlib file: CVE-2026-32860

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3749034

Vulnerabilities CVE-2026-32862, CVE-2026-32863, and CVE-2026-32864
Fixed memory corruption vulnerabilities when loading specifically corrupted VIs: CVE-2026-32862, CVE-2026-32863, CVE-2026-32864

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2025 Q3
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Mar 16, 2026

3716343

"Cannot Find libniDotNETCoreInterop.so" Message When Starting LabVIEW on Linux
On launch, LabVIEW on Linux outputs "Can't find libniDotNETCoreInterop.so." However, LabVIEW launches and functions correctly.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Feb 2, 2026

3662020

String Constants Suggested by LabVIEW Code Completion With Nigel AI Are Empty
When LabVIEW Code Completion by Nigel AI suggests code that contains a string constant, the string is set to empty instead of the value specified in the code suggestion.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Feb 3, 2026

3695843

Right-click Highlight Probe Command Draws Red Rectangle On Diagram When Debug Window is Not Open

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Feb 2, 2026

3445050

Externally Changed Files List May Appear Behind Other Windows
After closing the Externally Changed Files List and modifying an open project file on disk, LabVIEW displays the Externally Changed Files List again, but doesn't open the window in front of other windows.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 1.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 1
Added:
Feb 2, 2026

3782402

DAQ Assistant Fails to Generate Code
The DAQ Assistant fails to generate code when used with NI-DAQmx 2026 Q4 and later.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 2.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 2
Added:
Apr 22, 2026

3816758

DataFinder Toolkit Has Missing Dependencies

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 2.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 2
Added:
Apr 22, 2026

3817712

Manage Trusted Files Dialog Seems to Hang When Applying Changes
When using LabVIEW 2026 Q1 Patch 1, the Manage Trusted Files dialog can take an unreasonably long time to apply changes.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 2.

Reported Version:
LabVIEW 2026 Q1 Patch 1
Resolved Version:
LabVIEW 2026 Q1 Patch 2
Added:
Apr 22, 2026

3837188

Builds Using 'To .NET Object' Include Dependencies on Customer Experience Improvement Program VIs
LabVIEW includes VIs for the CEIP (Customer Experience Improvement Program) as dependencies when building applications or other binaries using "To .NET Object." CEIP VIs are only intended to be part of the LabVIEW development environment.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 2.

Reported Version:
LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 2
Added:
Apr 22, 2026

3742460, 3762025

Report Generation and Database Connectivity Toolkits Stop Working in Older Versions of LabVIEW When You Add a Newer Version
Report Generation and Database Connectivity Toolkits for LabVIEW 2024 Q3 and later install into a shared location (LVAddons) instead of the LabVIEW folder. If you have LabVIEW 2024 Q3, 2025 Q1, or 2025 Q3 installed on your machine and install a newer version of LabVIEW (2025 Q1 or later) on the same machine, the older versions of LabVIEW lose access to these toolkits erroneously.

Workaround:
Fixed in LabVIEW 2026 Q1 Patch 2.

Reported Version:
LabVIEW 2025 Q3 | LabVIEW 2026 Q1
Resolved Version:
LabVIEW 2026 Q1 Patch 2
Added:
Apr 7, 2026

Bug Number

Legacy ID

Description

Details

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:1 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:2 ordinal=2 -->
## Offline Help Viewer Not Available on Linux

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:2 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:3 ordinal=3 -->
## Clipboard Listed in Debug Window

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:3 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:4 ordinal=4 -->
## Constructor Node Does Not Allow Selection of Default Constructor for Non-Static Struct in .NET 8 Assembly

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:4 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:5 ordinal=5 -->
## LabVIEW Prompts to Save Temporary VIs Used to Create VI Snippets

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 1, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:5 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:6 ordinal=6 -->
## LabVIEW Erroneously Saves Breakpoint After You Remove Breakpoint in Dynamic Dispatch VI While Paused

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:6 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:7 ordinal=7 -->
## Selecting Browse in Property and Invoke Nodes Configured for .NET Core Does Not Open Browse Dialog

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:7 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:8 ordinal=8 -->
## LabVIEW Invoke Node Configured to .NET Core Method with Array In/Out Parameter Does Not Provide Output Terminal

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:8 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:9 ordinal=9 -->
## LabVIEW Does Not Update the VI Name in the Debug Window After Renaming a VI in Project Configured to Use a Previous Save Version

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 11, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:9 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:10 ordinal=10 -->
## Scan from String Does Not Return Expected Error

Workaround:

Reported Version:

LabVIEW 2021 | LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:10 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:11 ordinal=11 -->
## LabVIEW Sometimes Crashes After Selecting Right-Click Help For Engine on a Variable Property Node

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 8, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:11 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:12 ordinal=12 -->
## Bookmark Manager Does Not Display All Bookmarks in Projects Created from Templates

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 16, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:12 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:13 ordinal=13 -->
## Refnum Palette Contains Extraneous .NET Core Refnum

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:13 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:14 ordinal=14 -->
## Export Data To Clipboard in Debug Window Doesn't Enable Pasting the Data Inside LabVIEW

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 18, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:14 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:15 ordinal=15 -->
## Search with Nigel Search Bar Does Not Find Add-On Content

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1

Added:

Jul 15, 2025

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:15 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:16 ordinal=16 -->
## LabVIEW Sometimes Crashes When Running VI After Placing Diagram Disable Structure

Workaround:

Fixed in LabVIEW 2026 Q1.

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1

Added:

Feb 3, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:16 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:17 ordinal=17 -->
## Cannot Set Description and Tip in Constant Linked to a Type Definition

Workaround:

Reported Version:

LabVIEW 2020

Resolved Version:

LabVIEW 2026 Q1

Added:

Feb 3, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:17 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:18 ordinal=18 -->
## LabVIEW Code Completion with Nigel AI in Localized Versions of LabVIEW Never Suggests Some Palette Functions

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:18 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:19 ordinal=19 -->
## LabVIEW Code Completion with Nigel AI Never Suggests Code Containing Functions from Some NI Driver APIs

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:19 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:20 ordinal=20 -->
## Calling .NET (Core) 8.0 Code Leaks Memory

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:20 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:21 ordinal=21 -->
## LabVIEW Crashes When Displaying Context Help for Polymorphic VI with No Instance VIs

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:21 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:22 ordinal=22 -->
## Building "My Application" Build Specification in "Actor Framework Template" Project Fails

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:22 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:23 ordinal=23 -->
## Manage Trusted Files Dialog Takes a Long Time to Populate

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:23 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:24 ordinal=24 -->
## LabVIEW Sometimes Crashes When Using ExecuteJavaScript and FireUserEvent in Web Browser Control

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:24 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:25 ordinal=25 -->
## Externally Changed Files List Opens Erroneously When Running Some VI Tools

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:25 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:26 ordinal=26 -->
## To Lower Case Function Works Incorrectly in LabVIEW for macOS

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:26 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:27 ordinal=27 -->
## Vulnerability CVE-2026-32861

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:27 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:28 ordinal=28 -->
## Vulnerability CVE-2026-32860

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:28 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:29 ordinal=29 -->
## Vulnerabilities CVE-2026-32862, CVE-2026-32863, and CVE-2026-32864

Workaround:

Reported Version:

LabVIEW 2025 Q3

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Mar 16, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:29 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:30 ordinal=30 -->
## "Cannot Find libniDotNETCoreInterop.so" Message When Starting LabVIEW on Linux

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:30 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:31 ordinal=31 -->
## String Constants Suggested by LabVIEW Code Completion With Nigel AI Are Empty

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Feb 3, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:31 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:32 ordinal=32 -->
## Right-click Highlight Probe Command Draws Red Rectangle On Diagram When Debug Window is Not Open

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:32 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:33 ordinal=33 -->
## Externally Changed Files List May Appear Behind Other Windows

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 1

Added:

Feb 2, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:33 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:34 ordinal=34 -->
## DAQ Assistant Fails to Generate Code

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 2

Added:

Apr 22, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:34 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:35 ordinal=35 -->
## DataFinder Toolkit Has Missing Dependencies

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 2

Added:

Apr 22, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:35 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:36 ordinal=36 -->
## Manage Trusted Files Dialog Seems to Hang When Applying Changes

Workaround:

Reported Version:

LabVIEW 2026 Q1 Patch 1

Resolved Version:

LabVIEW 2026 Q1 Patch 2

Added:

Apr 22, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:36 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:37 ordinal=37 -->
## Builds Using 'To .NET Object' Include Dependencies on Customer Experience Improvement Program VIs

Workaround:

Reported Version:

LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 2

Added:

Apr 22, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:37 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:38 ordinal=38 -->
## Report Generation and Database Connectivity Toolkits Stop Working in Older Versions of LabVIEW When You Add a Newer Version

Workaround:

Reported Version:

LabVIEW 2025 Q3 | LabVIEW 2026 Q1

Resolved Version:

LabVIEW 2026 Q1 Patch 2

Added:

Apr 7, 2026

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:38 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:39 ordinal=39 -->
## Additional Patch Information

Installing some patches may require certain additional steps or considerations. Please refer to the following table for more information about patches for this release.

These patches currently do not have any special instructions.

Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

Mac and macOS are trademarks of Apple Inc., registered in the U.S. and other countries and regions.

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:39 -->

<!--KB_RECORD source=labview-2026-q1-bug-fixes locator=section:40 ordinal=40 -->
## Glossary of Terms

Bug ID - When an issue is reported to NI, you may be given this ID or find it on ni.com. You may also find IDs posted by NI on the discussion forums or in KnowledgeBase articles.

Legacy ID – An older issue ID that refers to the same issue. You may instead find this issue ID in older known issues documents.

Description - A few sentences which describe the problem. The brief description given does not necessarily describe the problem in full detail.

Workaround - Possible ways to work around the problem.

Reported Version - The earliest version in which the issue was reported.

Resolved Version - Version in which the issue was resolved or was no longer applicable. "N/A" indicates that the issue has not been resolved.

Date Added - The date the issue was added to the document (not the reported date).

<!--END_KB_RECORD source=labview-2026-q1-bug-fixes locator=section:40 -->

# SOURCE labview-2026-q1-features

- title: Announcing LabVIEW 2026 Q1
- category: version-changes
- url: https://forums.ni.com/t5/LabVIEW/Announcing-LabVIEW-2026-Q1/m-p/4468102
- source_sha256: 56830217e6ebf4f784e4357344ab3dcc743eec4d98739d3856e38aaeda51668c
- versions: ["2026 Q1"]

<!--KB_RECORD source=labview-2026-q1-features locator=section:1 ordinal=1 -->
## LabVIEW

Register

·

Login

·

Help

Subscribe to RSS Feed

Mark Topic as New

Mark Topic as Read

Float this Topic for Current User

Bookmark

Subscribe

Mute

Printer Friendly Page

All Forum Topics

Previous Topic

Next Topic

<!--END_KB_RECORD source=labview-2026-q1-features locator=section:1 -->

<!--KB_RECORD source=labview-2026-q1-features locator=section:2 ordinal=2 -->
## Announcing LabVIEW 2026 Q1!

‎02-03-2026

09:42 AM

- edited

‎02-04-2026

09:36 AM

Mark as New

Bookmark

Subscribe

Mute

Subscribe to RSS Feed

Permalink

Print

Report to a Moderator

NI Product Announcement

LabVIEW 2026 Q1 is now available for download!

LabVIEW 2026 Q1 delivers exciting new capabilities, such as, code completion with Nigel AI, improvements to the debugging workflow, added interoperability with .NET, and more!

Now, Nigel AI can make provide code suggestions giving you next steps as you develop, review LabVIEW Projects, and offer suggestions based on your hardware.

Additional updates include: a Web Browser front panel control, LabVIEW in Windows Docker containers, VI Comparison improvements, and more.

To see these features in action, join our webinar on March 5th.

NI Nigel™ AI Updates

LabVIEW 2026 Q1 adds the following updates to NI Nigel AI:

Nigel can suggest new code elements in your VI based on existing code and documentation.

Nigel can answer questions related to project structures. Nigel can provide information on targets, dependencies, build specifications, and configurations related to a project.

Nigel is aware of NI hardware connected to your test system and NI software installed on your test system. This lets Nigel answer questions related to your specific hardware and software.

Nigel can query, analyze, and retrieve test and measurement data stored after executing tests in TestStand. You can ask Nigel about these tests and their results to get information summaries and export data.

Nigel stores your chat history and allows you to load and pin previous discussions for easy access.

Enable or Disable VI Debugging Without File Modification

LabVIEW 2026 Q1 allows you to override the Allow Debugging VI property from the Project Environment Settings window on a per-target basis. This change lets you switch between development and debug workflows without modifying files, which can complicate source control.

LabVIEW 2026 Q1 also introduces .lvprojstate files to track user-specific project states. .lvprojstate files also facilitate executing debugging permission changes without file modification.

[Idea submitted by NI Discussion Forums member Darin.K]

Set Probes and Breakpoints Without Modifying Source VIs

LabVIEW 2026 Q1 allows you to set and save probes and breakpoints in source-only VIs in projects without altering the VI itself. LabVIEW saves these debugging settings in the .lvprojstate file for the project, which lets you exclude the settings from source control pipelines.

Enable or Disable Retain Wire Values Setting on Multiple VIs

LabVIEW 2026 Q1 improves debugging speed by adding the capability to enable or disable the Retain Wire Values setting for all VIs in a VI hierarchy. You can control this setting from your VI block diagram toolbar by selecting and holding the Retain Wire Values toolbar button.

[Idea submitted by NI Discussion Forums member asbo and Bob_Preis]

VI Comparison Improvements

LabVIEW 2026 Q1 introduces several enhancements to the Compare VIs function and VI Comparison reports:

You can include a report description in the report contents of VI Comparison reports.

VI Comparison reports include overview images of the VI front panels and block diagrams you're comparing.

The left and right images in the VI Comparison report show the same area of the panel or diagram when adding or removing objects.

VI comparison groups differences for attached labels with the attached object.

You can copy text from the Differences dialog lists to use elsewhere.

Differences with Bundle by Name and Unbundle by Names have details about the added and deleted elements.

Differences with window titles show the full titles.

Added Externally Changed Files List Dialog Box

LabVIEW 2026 Q1 introduces the Externally Changes Files List dialog box, which notifies you when open files change on disk. The dialog box also provides a quick way to reload your project and alerts you when you operate LabVIEW in a bad state caused by file change conflicts. These file change conflict alerts make it easier to execute branch changes when using Git for source code control.

The Externally Changed Files List opens automatically when LabVIEW detects that open files have changed on disk. You can also open the dialog from the View menu.

[Idea submitted by NI Discussion Forums member Taggart]

Support for LabVIEW Headless Environment

LabVIEW 2026 Q1 adds support for running LabVIEW headlessly through the command prompt or LabVIEWCLI (CLI) to perform continuous integration/continuous deployment (CI/CD) operations such as Masscompile without user interaction. Use the -headless tag to run LabVIEW headlessly. Headless operations don't require an active LabVIEW license.

Support for LabVIEW on Windows Docker Containers

NI provides a base Docker image with a ready-to-use LabVIEW 2026 Q1 installation on its account on Docker Hub. Use this image to set up Docker containers for CI/CD operations on Windows. You can also activate LabVIEW on a Windows Docker container using the NI License Manager (NILM) CLI without the need for a GUI on the container.

[Idea submitted by NI Discussion Forums member felipefoz]

Additional Security Features to Prevent Unknown External Code from Executing

LabVIEW 2026 Q1 adds a new security operation mode that is enabled by default. This security operation mode prevents unknown external code from automatically executing when called or loaded in LabVIEW. External code loaded in LabVIEW now loads in a broken, viewable state. You must add external files to the LabVIEW trusted files list using the Manage Trusted Files dialog.

Added Web Browser Front Panel Control

LabVIEW 2026 Q1 introduces a Web Browser front panel control. The Web Browser control lets you display a navigable webpage on a VI front panel, as well as programmatically navigate to a specified URL. This control is useful for displaying procedural documentation hosted online to operators.

[Idea submitted by NI Discussion Forums member amaury74]

.NET (Core) 8.0 Improvements

LabVIEW 2026 Q1 includes the following updates and improvements related to .NET (Core) 8.0:

Added new functionality which lets you create probes on .NET (Core) 8.0 reference wires. These probes function similarly to .NET Framework reference probes.

Added support for .NET Core APIs which get or set an array of class references.

Added support for the following functions:

.NET Object to Variant
Variant to .NET Object
To More Generic Class
To More Specific Class

.NET Object to Variant

Variant to .NET Object

To More Generic Class

To More Specific Class

Deprecation of Code Interface Nodes

As of LabVIEW 2026 Q1, LabVIEW no longer supports Code Interface Nodes (CINs). Update CINs in your VIs to Call Library Function Nodes (CLFNs).

Read the New Features and Changes Section in the LabVIEW Manual

All Forum Topics

Previous Topic

Next Topic

<!--END_KB_RECORD source=labview-2026-q1-features locator=section:2 -->

