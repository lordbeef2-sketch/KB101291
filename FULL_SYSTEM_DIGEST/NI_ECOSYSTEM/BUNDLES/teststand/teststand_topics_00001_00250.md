# NI DOCUMENT BUNDLE: teststand

<!--NI_BUNDLE_CHUNK bundle=teststand start=1 end=250 -->
<!--NI_TOPIC bundle=teststand path=64-bit-architecture-offers-more-memory.html language=enus -->
## TOPIC 00001: 64-bit Architecture Offers More Memory

- bundle_id: `teststand`
- source_path: `64-bit-architecture-offers-more-memory.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/64-bit-architecture-offers-more-memory.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: 64-bit architectures offer a larger address space than 32-bit architectures. 32-bit architectures use 32-bit pointers and can therefore use at most 4GB of memory but often less. By contrast, 64-bit applications can use up to 16TB (16,384GB) of memory. In most cases, the memory available for 32-bit T

### 64-bit Architecture Offers More Memory

64-bit architectures offer a larger address space than 32-bit architectures. 32-bit architectures use 32-bit pointers and can therefore use at most 4GB of memory but often less. By contrast, 64-bit applications can use up to 16TB (16,384GB) of memory.

In most cases, the memory available for 32-bit TestStand is more than adequate to meet the requirements of an application. Consider using 64-bit TestStand and the additional memory a 64-bit operating system offers for applications that generate large reports or handle image data.

Note

31

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=64-bit-teststand-and-migrating-from-32-bit-te.html language=enus -->
## TOPIC 00002: 64-bit TestStand and Migrating from 32-bit TestStand

- bundle_id: `teststand`
- source_path: `64-bit-teststand-and-migrating-from-32-bit-te.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/64-bit-teststand-and-migrating-from-32-bit-te.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand includes 32-bit TestStand and 64-bit TestStand. You can install and run 32-bit TestStand, 64-bit TestStand, or both on a computer running the 64-bit Windows operating system. 64-bit TestStand is similar to 32-bit TestStand, and, typically, you can edit and execute sequences in either versi

### 64-bit TestStand and Migrating from 32-bit TestStand

TestStand includes 32-bit TestStand and 64-bit TestStand. You can install and run 32-bit TestStand, 64-bit TestStand, or both on a computer running the 64-bit Windows operating system. 64-bit TestStand is similar to 32-bit TestStand, and, typically, you can edit and execute sequences in either version. However, the following significant differences exist between the two versions that you must consider when you migrate from 32-bit TestStand to 64-bit TestStand or write sequences to run on 32-bit TestStand and 64-bit TestStand.

- [Choosing between 32-bit TestStand and 64-bit TestStand](choosing-between-32-bit-teststand-and-64-bit.html)
- [Activating 32-bit TestStand and 64-bit TestStand](activating-32-bit-teststand-and-64-bit-testst.html)
- [Features 64-Bit TestStand does not Support](features-64-bit-teststand-does-not-support.html)
- [Driver Support for 64-bit TestStand](driver-support-for-64-bit-teststand.html)
- [64-bit Architecture Offers More Memory](64-bit-architecture-offers-more-memory.html)
- [Bitness-Conditional Code for 32-bit TestStand or 64-bit TestStand](bitness-conditional-code-for-32-bit-teststand.html)
- [Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand](representing-pointers-in-sequences-in-32-bit.html)
- [Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand](representing-pointer-sized-numbers-in-sequenc.html)
- [Locating the Correct Code Module in 32-bit TestStand and 64-bit TestStand](locating-the-correct-code-module-in-32-bit-te.html)
- [Adapter and Code Module Support for 64-bit TestStand](adapter-and-code-module-support-for-64-bit-te.html)
- [Call Executable Step Type Support for 64-bit TestStand](call-executable-step-type-support-for-64-bit.html)
- [CPU Affinity Step Type Support for 64-bit TestStand](cpu-affinity-step-type-support-for-64-bit-tes.html)
- [Synchronization Object Support for 64-bit TestStand](synchronization-object-support-for-64-bit-tes.html)
- [Session Manager Support for 64-bit TestStand](session-manager-support-for-64-bit-teststand.html)
- [Python Code Module Support for 64-bit TestStand](python-code-module-support-for-64-bit-teststa.html)
- [Deploying 32-bit TestStand and 64-bit TestStand Systems](deploying-32-bit-teststand-and-64-bit-teststa.html)
- [API Updates for 64-bit TestStand](api-updates-for-64-bit-teststand.html)

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=teststand path=accessing-arrays-using-api-htbasic.html language=enus -->
## TOPIC 00003: Accessing Arrays Using API - HTBasic

- bundle_id: `teststand`
- source_path: `accessing-arrays-using-api-htbasic.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-arrays-using-api-htbasic.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API from an HTBasic code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand. Example File Location <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\HTBasic\Accessing Arra

### Accessing Arrays Using API - HTBasic

#### Purpose

This example demonstrates how to use the TestStand API from an HTBasic code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Arrays Using
 API\HTBasic\Accessing Arrays Using API.seq

#### Highlighted Features

- HTBasic Adapter
- TestStand API

#### Major API

- PropertyObject.GetValNumberByOffset
- PropertyObject.SetValNumberByOffset
- PropertyObject.GetValStringByOffset
- PropertyObject.SetValStringByOffset

#### Prerequisites

When you use the demo version of HTBasic, you must configure the HTBasic Adapter to use the HTBasic demo server. Select the Use HTBasic Runtime Server option in the HTBasic Adapter Configuration dialog box and specify the path and filename for HTBwin.exe.

Note

#### How to Use This Example

Open the following ArraySubs.prg file, located in the <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\HTBasic directory, and review the following defined subroutines and the TestStand API calls used to get and set the TestStand local variables:

- Filllocalarray —Demonstrates how to use the TestStand API from HTBasic to populate an array stored in a TestStand local variable.
- Accessarray —Demonstrates how to use the TestStand API from HTBasic to read an array stored in a TestStand local variable and display a graph of the data.
- Fill2darray —Demonstrates how to use the TestStand API from HTBasic to populate a two-dimensional array stored in a TestStand local variable.
- Access2darray —Demonstrates how to use the TestStand API from HTBasic to read a two-dimensional array stored in a TestStand local variable.
- Fillstrarray —Demonstrates how to use the TestStand API from HTBasic to populate a string array stored in a TestStand local variable.
- Accessstrarray —Demonstrates how to use the TestStand API from HTBasic to read a string array stored in a TestStand local variable.

Complete the following steps to review how TestStand calls the subroutines in the HTBasic PRG file and review the created local variables.

1. Open the AccessingArrays.seq example sequence file. On the Variables pane, the NumericArray , TwoDimArray , and StrArray local variables have been created, but do not contain any data.
2. On the Steps pane, select an Action step.
3. On the Step Settings pane, review the settings for the Action step. The step does not pass local variables to or return local variables from the subroutine.
4. Select Execute»Single Pass to run the sequence. Use the TestStand debugging tools such as breakpoints, the Variables pane, and the Watch View pane to monitor the local variables and verify that the HTBasic subroutines populate the panes with data.

Parent topic:

Accessing Arrays Using API

Related concepts:

- TestStand Directory Structure
- Debugging Executions

<!--NI_TOPIC bundle=teststand path=accessing-arrays-using-api-labview.html language=enus -->
## TOPIC 00004: Accessing Arrays Using API - LabVIEW

- bundle_id: `teststand`
- source_path: `accessing-arrays-using-api-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-arrays-using-api-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API from a LabVIEW code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand. Example File Location <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\LabVIEW\Accessing Array

### Accessing Arrays Using API - LabVIEW

#### Purpose

This example demonstrates how to use the TestStand API from a LabVIEW code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Arrays Using
 API\LabVIEW\Accessing Arrays Using API.seq

#### Highlighted Features

- LabVIEW Adapter
- TestStand API

#### Major API

- PropertyObject.NewSubProperty
- PropertyObject.SetValVariant

#### Prerequisites

You must have the LabVIEW development system installed and you must configure the LabVIEW Adapter to use the LabVIEW development system.

#### How to Use This Example

Open the following example VIs, located in the <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\LabVIEW directory, and review the TestStand API calls used to get and set the TestStand local variables:

- FillLocalArray.vi —Demonstrates how to use the TestStand API from LabVIEW to populate an array stored in a TestStand local variable.
- AccessArray.vi —Demonstrates how to use the TestStand API from LabVIEW to read an array stored in a TestStand local variable and display a graph of the data.
- Create2DArray.vi —Demonstrates how to use the TestStand API from LabVIEW to dynamically create and populate a two-dimensional array stored in a TestStand local variable.
- Access2DArray.vi —Demonstrates how to use the TestStand API from LabVIEW to read a two-dimensional array stored in a TestStand local variable and display a graph of the data.
- SetStringArray.vi —Demonstrates how to use the TestStand API from LabVIEW to populate a string array stored in a TestStand local variable.
- GetStringArray.vi —Demonstrates how to use the TestStand API from LabVIEW to read a string array stored in a TestStand local variable and display the strings in the VI.

Complete the following steps to review how TestStand calls the VIs, review the created local variables, and review the parameters passed to and from the VIs.

1. Open the AccessingArrays.seq example sequence file. On the Variables pane, the NumericArray and StringArray local variables have been created, but do not contain any data.
2. On the Steps pane, select an Action step.
3. On the Step Settings pane, review the settings for the Action step. The step does not pass local variables to or return local variables from the VI.
4. Select Execute»Single Pass to run the sequence. The VIs populate the local variables with data, and LabVIEW accesses and displays the data.

Parent topic:

Accessing Arrays Using API

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=accessing-arrays-using-api-labwindows-cvi.html language=enus -->
## TOPIC 00005: Accessing Arrays Using API - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `accessing-arrays-using-api-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-arrays-using-api-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API from a LabWindows/CVI DLL code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand. Example File Location <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\CVI\Accessin

### Accessing Arrays Using API - LabWindows/CVI

#### Purpose

This example demonstrates how to use the TestStand API from a LabWindows/CVI DLL code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Arrays Using
 API\CVI\Accessing Arrays Using API.seq

#### Highlighted Features

- LabWindows/CVI Adapter
- TestStand API

#### Major API

- PropertyObject.NewSubProperty
- PropertyObject.GetValVariant
- PropertyObject.SetValVariant

#### Prerequisites

You must have the LabWindows/CVI Run-Time Engine installed and you must configure the LabWindows/CVI Adapter to execute steps in-process. If you want to use the Execute Steps in an External Instance of CVI option, you must have the LabWindows/CVI development environment installed.

#### How to Use This Example

Open the AccessArrays.c source file, located in the <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\CVI directory, and review the following defined functions and the TestStand API calls used to get and set the TestStand local variables:

- FillLocalArray —Demonstrates how to use the TestStand API from LabWindows/CVI to populate an array stored in a TestStand local variable.
- AccessLocalArray —Demonstrates how to use the TestStand API from LabWindows/CVI to read an array stored in a TestStand local variable and display a graph of the data.
- Create2DArray —Demonstrates how to use the TestStand API from LabWindows/CVI to dynamically create and populate a two-dimensional array stored in a TestStand local variable Note Normally, this function would use the InsertIfMissing property option to create the local variable, but this example does not use this property option to maintain compatibility with previous versions of TestStand.
- Access2DArray —Demonstrates how to use the TestStand API from LabWindows/CVI to read a two-dimensional array stored in a TestStand local variable and display a graph of the data.
- SetStringArray —Demonstrates how to use the TestStand API from LabWindows/CVI to populate a string array stored in a TestStand local variable.
- GetStringArray —Demonstrates how to use the TestStand API from LabWindows/CVI to read a string array stored in a TestStand local variable and display the strings in a message popup.

Complete the following steps to review how TestStand calls the functions in the DLL, review the created local variables, and review the parameters passed to and from the functions.

1. Open the AccessingArrays.seq example sequence file. On the Variables pane, the NumericArray and StringArray local variables have been created, but do not contain any data.
2. On the Steps pane, select an Action step.
3. On the Step Settings pane, review the settings for the Action step. The step does not pass local variables to or return local variables from the function.
4. Select Execute»Single Pass to run the sequence. The DLL calls populate the local variables with data, and LabWindows/CVI accesses and displays the data.

Parent topic:

Accessing Arrays Using API

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=accessing-arrays-using-api-mfc.html language=enus -->
## TOPIC 00006: Accessing Arrays Using API - MFC

- bundle_id: `teststand`
- source_path: `accessing-arrays-using-api-mfc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-arrays-using-api-mfc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API from a Microsoft Foundation Class (MFC) Library code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand. Example File Location <TestStand Public>\Examples\TestStand API\Accessing Arrays

### Accessing Arrays Using API - MFC

#### Purpose

This example demonstrates how to use the TestStand API from a Microsoft Foundation Class (MFC) Library code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Arrays Using
 API\MFC\Accessing Arrays Using API.seq

#### Highlighted Features

- C/C++ DLL Adapter
- TestStand API

#### Major API

- PropertyObject.NewSubProperty
- PropertyObject.GetValVariant
- PropertyObject.SetValVariant

#### Prerequisites

None

#### How to Use This Example

AppWizard creates AccessingArrays.dll, which demonstrates the basics of using the Microsoft Foundation Class (MFC) Library and serves as a starting point for writing a custom DLL.

The following files, located in the <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\MFC directory, make up AccessingArrays.dll:

- AccessingArrays.h —The main header file that declares the CAccessingArraysApp class for the DLL.
- AccessingArrays.cpp —The main DLL source file that contains the CAccessingArraysApp class.
- AccessingArrays.rc —A list of all the Microsoft Windows resources the program uses, including icons, bitmaps, and cursors stored in the res subdirectory. You can directly edit this file in Microsoft Developer Studio.
- res\AccessingArrays.rc2 —Contains resources Developer Studio does not edit. Place all resources the resource editor cannot edit in this file.
- AccessingArrays.def —Contains DLL information that must be provided to run with Windows. This file defines parameters such as the name and description of the DLL and exports functions from the DLL.
- AccessingArrays.clw —Contains information ClassWizard uses to edit existing classes, add new classes, and store information required to create and edit message maps and dialog data maps and to create prototype member functions.

Other standard files located in the <TestStand Public>\Examples\AccessingArraysUsingAPI\UsingMFC directory include the following:

- StdAfx.h and StdAfx.cpp —Used to build a precompiled header (PCH) file named AccessingArrays.pch and a precompiled types file named StdAfx.obj .
- Resource.h —The standard header file that defines new resource IDs. Developer Studio reads and updates this file.

Note

TODO:

Parent topic:

Accessing Arrays Using API

Related concepts:

- TestStand Directory Structure
- Organizing Test Program Files with LabVIEW-Built Shared Libraries

<!--NI_TOPIC bundle=teststand path=accessing-arrays-using-api-net.html language=enus -->
## TOPIC 00007: Accessing Arrays Using API - .NET

- bundle_id: `teststand`
- source_path: `accessing-arrays-using-api-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-arrays-using-api-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API from a .NET assembly code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand. Example File Location <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API\DotNet\Accessing

### Accessing Arrays Using API - .NET

#### Purpose

This example demonstrates how to use the TestStand API from a .NET assembly code module to access a one-dimensional array, two-dimensional array, and an array of strings in TestStand.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Arrays Using
 API\DotNet\Accessing Arrays Using API.seq

#### Highlighted Features

- .NET Adapter
- TestStand API

#### Major API

- PropertyObject.NewSubProperty
- PropertyObject.GetValVariant
- PropertyObject.SetValVariant

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review how TestStand calls the functions in the DLL, review the created local variables, and review the parameters passed to and from the functions.

1. Open the AccessingArraysDotNet.seq example sequence file. On the Variables pane, the NumericArray and StringArray local variables have been created, but do not contain any data.
2. On the Steps pane, select an Action step.
3. On the Step Settings pane, review the settings for the Action step. The step does not pass local variables to or return local variables from the function.
4. Select Execute»Single Pass to run the sequence. The DLL calls populate the local variables with data, and the .NET assemblies access and display the data.

Parent topic:

Accessing Arrays Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=accessing-arrays-using-api.html language=enus -->
## TOPIC 00008: Accessing Arrays Using API

- bundle_id: `teststand`
- source_path: `accessing-arrays-using-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-arrays-using-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\TestStand API\Accessing Arrays Using API directory contains the following examples.

### Accessing Arrays Using API

The <TestStand
 Public>\Examples\TestStand API\Accessing Arrays Using API
 directory contains the following examples.

- [Accessing Arrays Using API - HTBasic](accessing-arrays-using-api-htbasic.html)
- [Accessing Arrays Using API - LabWindows/CVI](accessing-arrays-using-api-labwindows-cvi.html)
- [Accessing Arrays Using API - LabVIEW](accessing-arrays-using-api-labview.html)
- [Accessing Arrays Using API - MFC](accessing-arrays-using-api-mfc.html)
- [Accessing Arrays Using API - .NET](accessing-arrays-using-api-net.html)

Parent topic:

Examples for the TestStand API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=accessing-built-in-properties-csharp.html language=enus -->
## TOPIC 00009: Accessing Built-in Properties in C#

- bundle_id: `teststand`
- source_path: `accessing-built-in-properties-csharp.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-built-in-properties-csharp.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In C#, you can access the built-in properties by using the native syntax for accessing properties of objects. The following code obtains the value of the Name property from a Sequence object: private void Example (Sequence sequenceObj) { String nameString = sequenceObj.Name; } The following code obt

### Accessing Built-in Properties in C#

In C#, you can access the built-in properties by using the native syntax for accessing properties of objects.

The following code obtains the value of the Name property from a Sequence object:

private void Example (Sequence sequenceObj)

{

String nameString = sequenceObj.Name;

}

The following code obtains a reference to a step of a sequence the Sequence object references:

private void Example (SequenceContext contextObj)

{

Sequence sequenceObj;

Step stepObj;

sequenceObj = contextObj.Sequence;

stepObj = sequenceObj.GetStep(2, StepGroups.StepGroup_Main);

}

Parent topic:

Programming with the TestStand API in C#

<!--NI_TOPIC bundle=teststand path=accessing-built-in-properties-in-labview.html language=enus -->
## TOPIC 00010: Accessing Built-in Properties in LabVIEW

- bundle_id: `teststand`
- source_path: `accessing-built-in-properties-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-built-in-properties-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand defines a number of built-in properties that are always present for objects, such as steps and sequences. Nearly every kind of TestStand object has built-in properties that are static with respect to the TestStand API, which you can use to access the properties in the programming language

### Accessing Built-in Properties in LabVIEW

TestStand defines a number of built-in properties that are always present for objects, such as steps and sequences. Nearly every kind of TestStand object has built-in properties that are static with respect to the TestStand API, which you can use to access the properties in the programming language you specify. Examples of built-in properties are the Sequence.Name property and the SequenceContext.Sequence property.

In LabVIEW, use the Property Node to access built-in properties. The block diagram in the following shows how to obtain the value of the Sequence.Name property.

[IMAGE alt='image' src='GUID-9F1FE057-61EC-4E28-8478-22029534C64B-a5.png']

The block diagram in the following figure shows how to obtain a reference to a step of a sequence that a Sequence object references.

[IMAGE alt='image' src='GUID-E5629178-6DC8-4DA2-9F3C-5888F6C6C8B1-a5.png']

Parent topic:

Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=accessing-built-in-properties-in-labwindows-c.html language=enus -->
## TOPIC 00011: Accessing Built-in Properties in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `accessing-built-in-properties-in-labwindows-c.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-built-in-properties-in-labwindows-c.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand defines a number of built-in properties that are always present for objects, such as steps and sequences. Nearly every kind of TestStand object has built-in properties that are static with respect to the TestStand API, which you can use to access the properties in the programming language

### Accessing Built-in Properties in LabWindows/CVI

TestStand defines a number of built-in properties that are always present for objects, such as steps and sequences. Nearly every kind of TestStand object has built-in properties that are static with respect to the TestStand API, which you can use to access the properties in the programming language you specify. The Sequence.Name and SequenceContext.Sequence properties are examples of built-in properties.

In LabWindows/CVI, you access built-in properties using a property function in the ActiveX driver. The following code obtains the value of the Sequence.Name property:

int GetSequenceName(CAObjHandle sequence)

{

int error = 0;

ErrMsg errMsg = "";

ERRORINFO errorInfo;

char *sequenceName = NULL;

tsErrChk(TS_SequenceGetName (sequence, &errorInfo, &sequenceName));

Error:

// Free Resources

if (sequenceName)

CA_FreeMemory(sequenceName);

return error;

}

The following function obtains a reference to a step named CVI Pass/Fail Test from a Sequence object:

int GetStepInSequence(CAObjHandle sequence)

{

int error = 0;

ErrMsg errMsg = "";

ERRORINFO errorInfo;

CAObjHandle step = 0;

tsErrChk(TS_SequenceGetStepByName (sequence, &errorInfo, "CVI Pass/Fail Test", StepGroup_Main, &step));

Error:

// Free Resources

if (step)

CA_DiscardObjHandle(step);

return error;

}

Parent topic:

Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=accessing-built-in-properties-msvb.html language=enus -->
## TOPIC 00012: Accessing Built-in Properties in Microsoft Visual Basic .NET

- bundle_id: `teststand`
- source_path: `accessing-built-in-properties-msvb.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-built-in-properties-msvb.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Microsoft Visual Basic .NET, you can access built-in properties by using the native syntax for accessing properties of objects. The following code obtains the value of the Name property from a Sequence object: Private Sub Example (SequenceObj As Sequence) Dim NameString As String NameString = Seq

### Accessing Built-in Properties in Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access built-in properties by using the native syntax for accessing properties of objects.

The following code obtains the value of the Name property from a Sequence object:

Private Sub Example (SequenceObj As Sequence)

Dim NameString As String

NameString = SequenceObj.Name

End Sub

The following code obtains a reference to a step of a sequence the Sequence object references:

Private Sub Example (ContextObj As SequenceContext)

Dim SequenceObj as Sequence

Dim StepObj as Step

Set SequenceObj = ContextObj.Sequence()

Set StepObj = SequenceObj.GetStep(2, StepGroups.StepGroup_Main)

End Sub

Parent topic:

Programming with the TestStand API in Microsoft Visual Basic .NET

<!--NI_TOPIC bundle=teststand path=accessing-built-in-properties-msvc.html language=enus -->
## TOPIC 00013: Accessing Built-in Properties in Microsoft Visual C++/#import

- bundle_id: `teststand`
- source_path: `accessing-built-in-properties-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-built-in-properties-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Microsoft Visual C++, the #import directive generates methods for accessing the values of the built-in properties for each TestStand class. The following C++ code obtains the value of the Name property from a Sequence object: void Example (LPDISPATCH sequenceDisp){ TS::SequencePtr sequence = sequ

### Accessing Built-in Properties in Microsoft Visual C++/#import

In Microsoft Visual C++, the #import directive generates methods for accessing the values of the built-in properties for each TestStand class. The following C++ code obtains the value of the Name property from a Sequence object:

void Example (LPDISPATCH sequenceDisp){

TS::SequencePtr sequence = sequenceDisp;

_bstr_t nameString = sequence->GetName();

}

The following code obtains a reference to a step in a sequence the Sequence object references:

void Example (LPDISPATCH sequenceContextDisp){

TS::SequenceContextPtr sequenceContext = sequenceContextDisp;

TS::SequencePtr sequence;

TS::StepPtr step;

sequence = sequenceContext->GetSequence();

step = sequence->GetStep(2, TS::StepGroup_Main);

}

Parent topic:

Programming with the TestStand API in Microsoft Visual C++

<!--NI_TOPIC bundle=teststand path=accessing-built-in-properties.html language=enus -->
## TOPIC 00014: Accessing Built-in Properties

- bundle_id: `teststand`
- source_path: `accessing-built-in-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-built-in-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand defines a number of built-in properties that always exist for objects, such as the Sequence.Name property or the SequenceContext.Sequence property. Almost every TestStand object defines built-in, static API properties you can access in the programming language you use to create code module

### Accessing Built-in Properties

TestStand defines a number of built-in properties that always exist for objects, such as the Sequence.Name property or the SequenceContext.Sequence property. Almost every TestStand object defines built-in, static API properties you can access in the programming language you use to create code modules.

Refer to the following examples for more information about accessing built-in properties in specific development environments:

- LabVIEW
- LabWindows/CVI
- Microsoft Visual Basic .NET
- C#
- Microsoft Visual C++/#import

Parent topic:

TestStand API Concepts

Related concepts:

- Accessing Built-in Properties in LabVIEW
- Accessing Built-in Properties in LabWindows/CVI
- Accessing Built-in Properties in Microsoft Visual Basic .NET
- Accessing Built-in Properties in C#
- Accessing Built-in Properties in Microsoft Visual C++/#import

<!--NI_TOPIC bundle=teststand path=accessing-dynamic-properties-csharp.html language=enus -->
## TOPIC 00015: Accessing Dynamic Properties in C#

- bundle_id: `teststand`
- source_path: `accessing-dynamic-properties-csharp.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-dynamic-properties-csharp.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In C#, you can access dynamic properties by obtaining a PropertyObject reference from the specific object reference using the AsPropertyObject method on the object. You can then use the PropertyObject interface to access custom properties of the object using a lookup string to specify the specific c

### Accessing Dynamic Properties in C#

In C#, you can access dynamic properties by obtaining a PropertyObject reference from the specific object reference using the AsPropertyObject method on the object. You can then use the PropertyObject interface to access custom properties of the object using a lookup string to specify the specific custom property.

The following code uses the PropertyObject.GetValString method to obtain the error message value for the current step:

private void Example (Step stepObj)

{

PropertyObject propertyObj;

String errorString;

propertyObj = stepObj.AsPropertyObject();

errorString = propertyObj.GetValString("Result.Error.Msg",0);

}

Parent topic:

Programming with the TestStand API in C#

<!--NI_TOPIC bundle=teststand path=accessing-dynamic-properties-in-labview.html language=enus -->
## TOPIC 00016: Accessing Dynamic Properties in LabVIEW

- bundle_id: `teststand`
- source_path: `accessing-dynamic-properties-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-dynamic-properties-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In TestStand, you can define custom step properties, sequence local variables, sequence file global variables, and station global variables. Because the TestStand API is independent of the variables and custom step properties you define, these variables and properties are dynamic with respect to the

### Accessing Dynamic Properties in LabVIEW

In TestStand, you can define custom step properties, sequence local variables, sequence file global variables, and station global variables. Because the TestStand API is independent of the variables and custom step properties you define, these variables and properties are dynamic with respect to the TestStand API. The TestStand API provides the PropertyObject class so you can access dynamic properties and variables from within code modules, where you use lookup strings to identify specific properties by name.

To access dynamic properties of an object, you must first use the AsPropertyObject method of the object to convert the specific object reference to a PropertyObject reference. Then, use the PropertyObject interface to access custom properties of the object. The PropertyObject interface uses a lookup string to specify the specific custom property.

The block diagram in the following figure shows how to use the GetValString method on the PropertyObject interface of a Step object to obtain the error message value for the current step.

[IMAGE alt='image' src='GUID-1C637F55-2B35-44BB-B5C2-665FC2EAF2EA-a5.png']

You can use the TestStand - Get Property Value VI or the TestStand - Set Property Value VI to access dynamic properties of a SequenceContext object. The block diagram in the following figure shows how to use the TestStand - Get Property Value VI to obtain the error message value for the current step.

[IMAGE alt='image' src='GUID-1A67849F-19DB-4430-AC3F-2BEDBE2EEBAE-a5.png']

Parent topic:

Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=accessing-dynamic-properties-in-labwindows-cv.html language=enus -->
## TOPIC 00017: Accessing Dynamic Properties in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `accessing-dynamic-properties-in-labwindows-cv.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-dynamic-properties-in-labwindows-cv.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In TestStand, you can define custom step properties, sequence local variables, sequence file global variables, and station global variables. Because the TestStand API is independent of the variables and custom step properties you define, these variables and properties are dynamic with respect to the

### Accessing Dynamic Properties in LabWindows/CVI

In TestStand, you can define custom step properties, sequence local variables, sequence file global variables, and station global variables. Because the TestStand API is independent of the variables and custom step properties you define, these variables and properties are dynamic with respect to the TestStand API. The TestStand API provides the PropertyObject class so you can access dynamic properties and variables from within code modules, where you use lookup strings to identify specific properties by name.

The following example shows how to call a method of the PropertyObject class on a handle to a SequenceContext object to set a local variable:

int SetLocalVariable(CAObjHandle seqContextCVI)

{

int error = 0;

ErrMsg errMsg = "";

ERRORINFO errorInfo;

VBOOL propertyExists;

// Set local variable NumericValue to a random number

tsErrChk(TS_PropertyExists(seqContextCVI, &errorInfo, "Locals.NumericValue", 0, &propertyExists));

if (propertyExists) tsErrChk(TS_PropertySetValNumber(seqContextCVI, &errorInfo, "Locals.NumericValue", 0, rand()));

Error:

return error;

}

Parent topic:

Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=accessing-dynamic-properties-in-msvc.html language=enus -->
## TOPIC 00018: Accessing Dynamic Properties in Microsoft Visual C++/#import

- bundle_id: `teststand`
- source_path: `accessing-dynamic-properties-in-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-dynamic-properties-in-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Microsoft Visual C++, you can use the classes the #import directive generates to access dynamic properties by obtaining a PropertyObject reference from the specific object reference using the AsPropertyObject method on the object. You can use the PropertyObject interface to access custom properti

### Accessing Dynamic Properties in Microsoft Visual C++/#import

In Microsoft Visual C++, you can use the classes the #import directive generates to access dynamic properties by obtaining a PropertyObject reference from the specific object reference using the AsPropertyObject method on the object. You can use the PropertyObject interface to access custom properties of the object using a lookup string to specify the custom property.

The following code uses the PropertyObject.GetValString method to obtain the error message value for the current step:

void Example (LPDISPATCH seqContextDisp){

TS::SequenceContextPtr sequenceContext = seqContextDisp;

TS::PropertyObjectPtr property;

_bstr_t errorString;

property = sequenceContext->GetStep()->AsPropertyObject();

errorString = property->GetValString("Result.Error.Msg",0);

}

Parent topic:

Programming with the TestStand API in Microsoft Visual C++

<!--NI_TOPIC bundle=teststand path=accessing-dynamic-properties-msvb.html language=enus -->
## TOPIC 00019: Accessing Dynamic Properties in Microsoft Visual Basic .NET

- bundle_id: `teststand`
- source_path: `accessing-dynamic-properties-msvb.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-dynamic-properties-msvb.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Microsoft Visual Basic .NET, you can access dynamic properties by obtaining a PropertyObject reference from the specific object reference using the AsPropertyObject method on the object. You can then use the PropertyObject interface to access custom properties of the object using a lookup string

### Accessing Dynamic Properties in Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access dynamic properties by obtaining a PropertyObject reference from the specific object reference using the AsPropertyObject method on the object. You can then use the PropertyObject interface to access custom properties of the object using a lookup string to specify the specific custom property.

The following code uses the PropertyObject.GetValString method to obtain the error message value for the current step:

Private sub Example (StepObj as Step)

Dim PropertyObj as PropertyObject

Dim ErrorString as String

Set PropertyObj = StepObj.AsPropertyObject()

ErrorString = PropertyObj.GetValString("Result.Error.Msg",0)

End Sub

Parent topic:

Programming with the TestStand API in Microsoft Visual Basic .NET

<!--NI_TOPIC bundle=teststand path=accessing-dynamic-properties.html language=enus -->
## TOPIC 00020: Accessing Dynamic Properties

- bundle_id: `teststand`
- source_path: `accessing-dynamic-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-dynamic-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define custom step properties, sequence local variables, sequence file global variables, and station global variables that are dynamic with respect to the TestStand API. The TestStand API provides the PropertyObject class so you can access dynamic properties and variables in the programming

### Accessing Dynamic Properties

You can define custom step properties, sequence local variables, sequence file global variables, and station global variables that are dynamic with respect to the TestStand API. The TestStand API provides the PropertyObject class so you can access dynamic properties and variables in the programming language you use to create code modules. Instead of using defined constants, use lookup strings to identify specific properties by name.

Refer to the following examples for more information about accessing dynamic properties in specific development environments:

- LabVIEW
- LabWindows/CVI
- Microsoft Visual Basic .NET
- C#
- Microsoft Visual C++/#import

Parent topic:

TestStand API Concepts

Related concepts:

- Lookup Strings
- Accessing Dynamic Properties in LabVIEW
- Accessing Dynamic Properties in LabWindows/CVI
- Accessing Dynamic Properties in Microsoft Visual Basic .NET
- Accessing Dynamic Properties in C#
- Accessing Dynamic Properties in Microsoft Visual C++/#import

<!--NI_TOPIC bundle=teststand path=accessing-privilege-settings-for-any-user.html language=enus -->
## TOPIC 00021: Accessing Privilege Settings for Any User

- bundle_id: `teststand`
- source_path: `accessing-privilege-settings-for-any-user.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-privilege-settings-for-any-user.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand API includes methods to access the privileges of any user or group. Use the Engine.GetUser and Engine.GetUserGroup methods to return a User object, then call the User.HasPrivilege method, which returns True when the user or any group to which the user belongs has the privilege you spec

### Accessing Privilege Settings for Any User

The TestStand API includes methods to access the privileges of any user or group. Use the Engine.GetUser and Engine.GetUserGroup methods to return a User object, then call the User.HasPrivilege method, which returns True when the user or any group to which the user belongs has the privilege you specify by name. When you call the User.HasPrivilege method on a User object the Engine.GetUser method returns, the User.HasPrivilege method behaves identically to the CurrentUserHasPrivilege method or expression function.

Parent topic:

Privileges

<!--NI_TOPIC bundle=teststand path=accessing-privilege-settings-for-the-current.html language=enus -->
## TOPIC 00022: Accessing Privilege Settings for the Current User

- bundle_id: `teststand`
- source_path: `accessing-privilege-settings-for-the-current.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-privilege-settings-for-the-current.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Call the CurrentUserHasPrivilege expression function to verify in an expression that the current user has a specific privilege. Use the Engine.CurrentUserHasPrivilege method in the TestStand API to verify the privilege in a code module. The Engine.CurrentUserHasPrivilege method behaves identically t

### Accessing Privilege Settings for the Current User

Call the CurrentUserHasPrivilege expression function to verify in an expression that the current user has a specific privilege. Use the Engine.CurrentUserHasPrivilege method in the TestStand API to verify the privilege in a code module. The Engine.CurrentUserHasPrivilege method behaves identically to the CurrentUserHasPrivilege expression function.

When you call the CurrentUserHasPrivilege method or expression function, you must specify the property name of the privilege as a string argument. You can pass any subset of the property name tree structure to CurrentUserHasPrivilege. For example, you can call CurrentUserHasPrivilege with the following expressions to determine whether the current user has the privilege to terminate an execution:

- CurrentUserHasPrivilege("Terminate")
- CurrentUserHasPrivilege("Operate.Terminate")

You can pass "*" as the string argument to CurrentUserHasPrivilege to determine whether a user is currently logged in.

Parent topic:

Privileges

Related concepts:

- Expressions

<!--NI_TOPIC bundle=teststand path=accessing-properties-using-api-labview.html language=enus -->
## TOPIC 00023: Accessing Properties Using API - LabVIEW

- bundle_id: `teststand`
- source_path: `accessing-properties-using-api-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-properties-using-api-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class. Example

### Accessing Properties Using API - LabVIEW

#### Purpose

This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Properties Using
 API\LabVIEW\Accessing Properties Using API.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetValNumber
- PropertyObject.GetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the example executes, read the message popups for information about built-in and dynamic properties and how they are accessed.

Complete the following steps to review the sequences and steps in this example.

1. Open the Accessing Built-In Properties sequence from the Sequences pane. Select the Access Built-in properties step, then click Edit VI in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand API to access built-in properties and methods.
2. Open the Accessing Dynamic Properties sequence from the Sequences pane. Select the Get Step Results step, then click Edit VI in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to get the values of dynamic step properties.
3. Select the Set Step Results step, then click Edit VI in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to set the values of dynamic step properties.
4. Select the Set Variables step, then click Edit VI in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to set the value of a local variable, and create a new local variable that exists only at run-time.

Parent topic:

Accessing Properties Using API

Related concepts:

- Accessing Built-in Properties
- Accessing Dynamic Properties
- TestStand Directory Structure
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=accessing-properties-using-api-labwindows-cvi.html language=enus -->
## TOPIC 00024: Accessing Properties Using API - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `accessing-properties-using-api-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-properties-using-api-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class. Example

### Accessing Properties Using API - LabWindows/CVI

#### Purpose

This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Properties Using
 API\CVI\Accessing Properties Using API.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetValNumber
- PropertyObject.GetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the example executes, read the message popups for information about built-in and dynamic properties and how they are accessed.

Complete the following steps to review the sequences and steps in this example.

1. Open the Accessing Built-In Properties sequence from the Sequences pane. Select the Access Built-in properties step, then click Edit Code in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand API to access built-in properties and methods.
2. Open the Accessing Dynamic Properties sequence from the Sequences pane. Select the Get Step Results step, then click Edit Code in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to get the values of dynamic step properties.
3. Select the Set Step Results step, then click Edit Code in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to set the values of dynamic step properties.
4. Select the Set Variables step, then click Edit Code in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to set the value of a local variable, and create a new local variable that exists only at run-time.

Parent topic:

Accessing Properties Using API

Related concepts:

- Accessing Built-in Properties
- Accessing Dynamic Properties
- TestStand Directory Structure
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=accessing-properties-using-api-mfc.html language=enus -->
## TOPIC 00025: Accessing Properties Using API - MFC

- bundle_id: `teststand`
- source_path: `accessing-properties-using-api-mfc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-properties-using-api-mfc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: None Purpose This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class. Exa

### Accessing Properties Using API - MFC

None

#### Purpose

This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class.

#### Example File
 Location

<TestStand Public>\Examples\TestStand
 API\Accessing Properties Using API\MFC\Accessing Properties Using
 API.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetValNumber
- PropertyObject.GetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant

#### Prerequisites

None

#### How to Use This Example

AppWizard creates AccessingPropertiesAndVariables.dll, which demonstrates the basics of using the Microsoft Foundation Class (MFC) Library and serves as a starting point for writing a custom DLL.

The following files, located in the <TestStand Public>\Examples\TestStand API\Accessing Properties Using API\MFC directory, make up AccessingPropertiesAndVariables.dll:

- AccessingPropertiesAndVariables.h —The main header file that declares the CAccessingPropertiesAndVariablesApp class for the DLL.
- AccessingPropertiesAndVariables.cpp —The main DLL source file that contains the CAccessingPropertiesAndVariablesApp class.
- AccessingPropertiesAndVariables.rc —A list of all the Microsoft Windows resources the program uses, including icons, bitmaps, and cursors stored in the res subdirectory. You can directly edit this file in Microsoft Developer Studio.
- res\AccessingPropertiesAndVariables.rc2 —Contains resources Developer Studio does not edit. Place all resources the resource editor cannot edit in this file.
- AccessingPropertiesAndVariables.def —Contains DLL information that must be provided to run with Windows. This file defines parameters such as the name and description of the DLL and exports functions from the DLL.
- AccessingPropertiesAndVariables.clw —Contains information ClassWizard uses to edit existing classes, add new classes, and store information required to create and edit message maps and dialog data maps and to create prototype member functions.

Other standard files located in the <TestStand Public>\Examples\Accessing Properties Using API\MFC directory include the following:

- StdAfx.h and StdAfx.cpp —Used to build a precompiled header (PCH) file named AccessingPropertiesAndVariables.pch and a precompiled types file named StdAfx.obj .
- Resource.h —The standard header file that defines new resource IDs. Developer Studio reads and updates this file.

Note

TODO:

Parent topic:

Accessing Properties Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=accessing-properties-using-api-net.html language=enus -->
## TOPIC 00026: Accessing Properties Using API - .NET

- bundle_id: `teststand`
- source_path: `accessing-properties-using-api-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-properties-using-api-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class. Example

### Accessing Properties Using API - .NET

#### Purpose

This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Properties Using
 API\DotNet\Accessing Properties Using API.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetValNumber
- PropertyObject.GetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the example executes, read the message popups for information about built-in and dynamic properties and how they are accessed.

Complete the following steps to review the sequences and steps in this example.

1. Open the Accessing Built-In Properties sequence from the Sequences pane. Select the Access Built-in properties step, then click Edit In Visual Studio in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand API to access built-in properties and methods.
2. Open the Accessing Dynamic Properties sequence from the Sequences pane. Select the Get Step Results step, then click Edit In Visual Studio in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to get the values of dynamic step properties.
3. Select the Set Step Results step, then click Edit In Visual Studio in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to set the values of dynamic step properties.
4. Select the Set Variables step, then click Edit In Visual Studio in the Module tab of the Step Settings pane to open the code module. This code module uses the TestStand PropertyObject methods to set the value of a local variable, and create a new local variable that exists only at run-time.

Parent topic:

Accessing Properties Using API

Related concepts:

- Accessing Built-in Properties
- Accessing Dynamic Properties
- TestStand Directory Structure
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=accessing-properties-using-api-teststand-expr.html language=enus -->
## TOPIC 00027: Accessing Properties Using API - TestStand Expressions

- bundle_id: `teststand`
- source_path: `accessing-properties-using-api-teststand-expr.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-properties-using-api-teststand-expr.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class. Example

### Accessing Properties Using API - TestStand Expressions

#### Purpose

This example shows how to access built-in and dynamic TestStand properties. Built-in TestStand properties are defined by the TestStand API, and are available for any object of a given class. Dynamic properties, also known as SubProperties, can vary between objects of the same class.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Accessing Properties Using
 API\TestStand Expressions\Accessing Properties Using
 API.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetValNumber
- PropertyObject.GetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the example executes, read the message popups for information about built-in and dynamic properties and how they are accessed.

Complete the following steps to review the sequences and steps in this example.

1. Open the Accessing Built-In Properties sequence from the Sequences pane. Review the statement steps in this sequence. These steps access built-in properties and methods using the TestStand API.
2. Open the Accessing Dynamic Properties sequence from the Sequences pane. Review the first set of statement steps under the Get Step Properties label. These steps use the TestStand PropertyObject methods to get the values of dynamic step properties.
3. Review the set of statement steps under the Set Step Properties label. These steps use the TestStand PropertyObject methods to set the values of dynamic step properties.
4. Review the set of statement steps under the Get Step Properties label. These steps use the TestStand ProprtyObject methods to set the value of a local variable, and dynamically create a local variable that exists only at run-time.

Parent topic:

Accessing Properties Using API

Related concepts:

- Accessing Built-in Properties
- Accessing Dynamic Properties
- TestStand Directory Structure
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=accessing-properties-using-api.html language=enus -->
## TOPIC 00028: Accessing Properties Using API

- bundle_id: `teststand`
- source_path: `accessing-properties-using-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-properties-using-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\TestStand API\Accessing Properties Using API directory contains the following examples.

### Accessing Properties Using API

The <TestStand
 Public>\Examples\TestStand API\Accessing Properties Using
 API directory contains the following examples.

- [Accessing Properties Using API - LabWindows/CVI](accessing-properties-using-api-labwindows-cvi.html)
- [Accessing Properties Using API - LabVIEW](accessing-properties-using-api-labview.html)
- [Accessing Properties Using API - MFC](accessing-properties-using-api-mfc.html)
- [Accessing Properties Using API - .NET](accessing-properties-using-api-net.html)
- [Accessing Properties Using API - TestStand Expressions](accessing-properties-using-api-teststand-expr.html)

Parent topic:

Examples for the TestStand API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=accessing-rule-configuration-data.html language=enus -->
## TOPIC 00029: Accessing Rule Configuration Data in Rule Configuration Modules and Analysis Modules

- bundle_id: `teststand`
- source_path: `accessing-rule-configuration-data.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-rule-configuration-data.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Sequence Analyzer passes a RuleConfigurationContext object to the rule configuration module. After calling a VI, the sequence analyzer checks the Error Out cluster output and reports an error if the status indicates that an error occurred. After calling a function, the sequence analyze

### Accessing Rule Configuration Data in Rule Configuration Modules and Analysis
 Modules

The TestStand Sequence Analyzer passes a
 RuleConfigurationContext
 object to the rule configuration module. After calling a VI, the sequence analyzer
 checks the Error Out cluster output and reports an error if the
 status indicates that an error occurred. After calling a function, the sequence analyzer
 checks the return value and reports an error if the bool value is
 False or if the int value is not
 0.

To save custom rule settings, the rule configuration module first uses the
 RuleConfigurationContext.RuleConfiguration
 property to retrieve the rule configuration. The rule configuration module adds setting
 values to the
 RuleConfiguration.ConfigurationData
 PropertyObject,
 which is initially an empty container. When the user configures the rule, the rule
 configuration module adds subproperties to the PropertyObject that
 corresponds to the custom rule settings.

To use custom rule settings during analysis, the analysis module first uses the
 AnalysisContext.GetRuleConfiguration
 method to retrieve the rule configuration and then accesses the
 RuleConfiguration.ConfigurationData
 PropertyObject, which is an empty container if the user did not
 configure the rule. The analysis module uses the default setting values in this case.
 Otherwise, the analysis module retrieves the setting values from the subproperties of
 the PropertyObject. Set the
 RuleConfiguration.Description
 property in a rule configuration module to include a description of the setting values.
 This enables users to view the rule settings through the rule descriptions in the Rules
 pane or tab and populates generated reports with a description of the setting values.

Parent topic:

TestStand Sequence Analyzer

Related information:

- RuleConfigurationContext
- RuleConfiguration
- AnalysisContext
- PropertyObject

<!--NI_TOPIC bundle=teststand path=accessing-rule-settings-in-analysis-modules.html language=enus -->
## TOPIC 00030: Accessing Rule Settings in Analysis Modules

- bundle_id: `teststand`
- source_path: `accessing-rule-settings-in-analysis-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-rule-settings-in-analysis-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you select Use Rule Settings from the Configuration Option ring control on the Advanced tab of the Edit Rules dialog box to use rule settings during analysis, the analysis module uses the AnalysisContext.GetRuleConfiguration method to retrieve the rule configuration and then uses the RuleConfig

### Accessing Rule Settings in Analysis Modules

When you select Use Rule Settings from the Configuration Option ring control on the
 Advanced tab of the Edit Rules dialog box to use rule settings during analysis, the
 analysis module uses the
 AnalysisContext.GetRuleConfiguration
 method to retrieve the rule configuration and then uses the
 RuleConfiguration.RuleSettingValues
 property to access the setting values. Use the
 RuleSettingValues.GetBooleanValue,
 RuleSettingValues.GetStringValue
 and
 RuleSettingValues.GetNumberValue
 methods to obtain individual setting values.

The following examples show how to access a number rule setting value in LabVIEW,
 LabWindows/CVI, Microsoft Visual C#, and Microsoft Visual C++.

#### LabVIEW

[IMAGE alt='image' src='GUID-C4762DAC-CEAC-4D94-B99E-24E58DB764CE-a5.gif']

#### LabWindows/CVI

TSAnalyzerObj_RuleConfiguration ruleConfiguration = 0;
 TSAnalyzerObj_RuleSettingValues ruleSettingValues = 0;
 double mySettingValue = 0.0;
 tsErrChk(TSAnalyzer_AnalysisContextGetRuleConfiguration (analysisContext,
 &errorInfo, "MyCompany_RuleId", &ruleConfiguration));
 tsErrChk(TSAnalyzer_RuleConfigurationGetRuleSettingValues(ruleConfiguration,
 &errorInfo, &ruleSettingValues));
 tsErrChk(TSAnalyzer_RuleSettingValuesGetNumberValue(ruleSettingValues,
 &errorInfo, "MySetting", &mySettingValue));

Error:

CLEAR(ruleConfiguration, CA_DiscardObjHandle);
 CLEAR(ruleSettingValues, CA_DiscardObjHandle);

#### Microsoft Visual C#

RuleConfiguration ruleConfiguration =
 analysisContext.GetRuleConfiguration("MyCompany_RuleId");
 double mySettingValue =
 ruleConfiguration.RuleSettingValues.GetNumberValue("MySetting");

#### Microsoft Visual C++

TSAnalyzer::RuleConfigurationPtr ruleConfiguration =
 analysisContext->GetRuleConfiguration("MyCompany_RuleId");
 double mySettingValue =
 ruleConfiguration->RuleSettingValues->GetNumberValue("MySetting");

Parent topic:

TestStand Sequence Analyzer

Related information:

- AnalysisContext
- RuleConfiguration
- RuleSettingValues
- Edit Rule Dialog Box

<!--NI_TOPIC bundle=teststand path=accessing-the-sequence-context.html language=enus -->
## TOPIC 00031: Accessing the Sequence Context

- bundle_id: `teststand`
- source_path: `accessing-the-sequence-context.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/accessing-the-sequence-context.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In expressions, you can access the value of a variable or property by specifying a path from the sequence context to the particular variable or property. For example, you can specify the status of a step using the following expression:Step.Result.Status = "Passed" During an execution, you can view a

### Accessing the Sequence Context

In expressions, you can access the value of a variable or property by specifying a path from the sequence context to the particular variable or property. For example, you can specify the status of a step using the following expression:Step.Result.Status = "Passed"

During an execution, you can view and modify the values of the properties in the sequence context from the Variables pane in the Execution window. The Variables pane displays the sequence context for the sequence invocation currently selected on the Call Stack pane. You can also monitor individual variables or properties from the Watch View pane.

You can pass a reference to a SequenceContext object to a code module. In code modules, you access the value of a variable or property by using PropertyObject methods in the TestStand API with the sequence context. As with expressions, you must specify a path from the sequence context to the particular property or variable.

Select View»Sequence File»Variables or View»Execution»Variables in the TestStand Sequence Editor to display the Variables pane, which contains the names of variables, properties, and sequence parameters you can access from expressions and code modules.

Note

Parent topic:

Sequence Context

Related concepts:

- Sequence Context

<!--NI_TOPIC bundle=teststand path=acquiring-a-derived-class-csharp.html language=enus -->
## TOPIC 00032: Acquiring a Derived Class from the PropertyObject Class in C#

- bundle_id: `teststand`
- source_path: `acquiring-a-derived-class-csharp.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/acquiring-a-derived-class-csharp.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In C#, you can acquire a derived class from a dynamic property the PropertyObject class returns by using the as keyword or by casting. The following code uses a lookup string to obtain a reference to a Step object from the sequence context: private void Example (SequenceContext contextObj) { Propert

### Acquiring a Derived Class from the PropertyObject Class in C#

In C#, you can acquire a derived class from a dynamic property the PropertyObject class returns by using the as keyword or by casting.

The following code uses a lookup string to obtain a reference to a Step object from the sequence context:

private void Example (SequenceContext contextObj)

{

PropertyObject propertyObj;

Step stepObj;

propertyObj = contextObj.AsPropertyObject();

// stepObj would be null if GetPropertyObject did not return a step

stepObj = propertyObj.GetPropertyObject("RunState.Sequence.Main[2]",0) as Step;

// C# would raise an exception if GetPropertyObject did not return a step

stepObj = (Step)propertyObj.GetPropertyObject("RunState.Sequence.Main[2]",0);

}

Parent topic:

Programming with the TestStand API in C#

<!--NI_TOPIC bundle=teststand path=acquiring-a-derived-class-in-labview.html language=enus -->
## TOPIC 00033: Acquiring a Derived Class from the PropertyObject Class in LabVIEW

- bundle_id: `teststand`
- source_path: `acquiring-a-derived-class-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/acquiring-a-derived-class-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In some cases, you might need to use the PropertyObject class methods to obtain a reference to a TestStand object. You might then want to access one of the static properties of the TestStand object, such as the run mode for the third step in the Main step group of the currently executing sequence. F

### Acquiring a Derived Class from the PropertyObject Class in LabVIEW

In some cases, you might need to use the PropertyObject class methods to obtain a reference to a TestStand object. You might then want to access one of the static properties of the TestStand object, such as the run mode for the third step in the Main step group of the currently executing sequence.

For methods in the PropertyObject class that can return objects derived from PropertyObject, you must acquire the derived interface for the object to access the built-in properties and methods of the derived class.

The block diagram in the following figure shows how to use a lookup string to obtain a reference to a Step object from a SequenceContext object.

Note

Step

[IMAGE alt='image' src='GUID-C8D76036-D837-40CB-A78F-7AF96BC41713-a5.png']

Parent topic:

Programming with the TestStand API in LabVIEW

Related concepts:

- Obtaining a Different Interface for TestStand Objects in LabVIEW

<!--NI_TOPIC bundle=teststand path=acquiring-a-derived-class-msvb.html language=enus -->
## TOPIC 00034: Acquiring a Derived Class from the PropertyObject Class in Microsoft Visual Basic .NET

- bundle_id: `teststand`
- source_path: `acquiring-a-derived-class-msvb.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/acquiring-a-derived-class-msvb.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Microsoft Visual Basic .NET, you can acquire a derived class from a dynamic property the PropertyObject class returns. The following code uses a lookup string to obtain a reference to a Step object from the sequence context: Private Sub Example (ContextObj As SequenceContext) Dim PropertyObj as P

### Acquiring a Derived Class from the PropertyObject Class in Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can acquire a derived class from a dynamic property the PropertyObject class returns.

The following code uses a lookup string to obtain a reference to a Step object from the sequence context:

Private Sub Example (ContextObj As SequenceContext)

Dim PropertyObj as PropertyObject

Dim StepObj as Step

Set PropertyObj = ContextObj.AsPropertyObject()

StepObj = PropertyObj.GetPropertyObject("RunState.Sequence.Main[2]", 0)

End Sub

Parent topic:

Programming with the TestStand API in Microsoft Visual Basic .NET

<!--NI_TOPIC bundle=teststand path=acquiring-a-derived-class-msvc.html language=enus -->
## TOPIC 00035: Acquiring a Derived Class from the PropertyObject Class in Microsoft Visual C++/#import

- bundle_id: `teststand`
- source_path: `acquiring-a-derived-class-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/acquiring-a-derived-class-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Microsoft Visual C++, you can use a class the #import directive generates to acquire a derived class from a dynamic property the PropertyObject class returns. The following code uses a lookup string to obtain a reference to a Step object from the sequence context: void Example (LPDISPATCH seqCont

### Acquiring a Derived Class from the PropertyObject Class in Microsoft Visual C++/#import

In Microsoft Visual C++, you can use a class the #import directive generates to acquire a derived class from a dynamic property the PropertyObject class returns.

The following code uses a lookup string to obtain a reference to a Step object from the sequence context:

void Example (LPDISPATCH seqContextDisp){

TS::SequenceContextPtr sequenceContext = seqContextDisp;

TS::PropertyObjectPtr property;

TS::StepPtr step;

property = sequenceContext->AsPropertyObject();

step = property->GetPropertyObject("RunState.Sequence.Main[2]",0);

}

Parent topic:

Programming with the TestStand API in Microsoft Visual C++

<!--NI_TOPIC bundle=teststand path=acquiring-a-derived-class.html language=enus -->
## TOPIC 00036: Acquiring a Derived Class from the PropertyObject Class

- bundle_id: `teststand`
- source_path: `acquiring-a-derived-class.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/acquiring-a-derived-class.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In some cases, you can obtain a reference to a TestStand object using the PropertyObject class methods and then access one of the static properties of the object. For example, you might want to obtain the run mode for the third step of the Main step group of the currently executing sequence. For met

### Acquiring a Derived Class from the PropertyObject Class

In some cases, you can obtain a reference to a TestStand object using the PropertyObject class methods and then access one of the static properties of the object. For example, you might want to obtain the run mode for the third step of the Main step group of the currently executing sequence. For methods on the PropertyObject class that can return objects derived from the PropertyObject class, you must acquire the derived interface for the object to access the built-in properties and methods of the derived class.

Refer to the following examples for more information about acquiring a derived class from the PropertyObject class in specific development environments:

- LabVIEW
- Microsoft Visual Basic .NET
- C#
- Microsoft Visual C++/#import

Parent topic:

TestStand API Concepts

Related concepts:

- Acquiring a Derived Class from the PropertyObject Class in LabVIEW
- Acquiring a Derived Class from the PropertyObject Class in Microsoft Visual Basic .NET
- Acquiring a Derived Class from the PropertyObject Class in C#
- Acquiring a Derived Class from the PropertyObject Class in Microsoft Visual C++/#import

<!--NI_TOPIC bundle=teststand path=activating-32-bit-teststand-and-64-bit-testst.html language=enus -->
## TOPIC 00037: Activating 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `activating-32-bit-teststand-and-64-bit-testst.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/activating-32-bit-teststand-and-64-bit-testst.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Version Selector does not treat 32-bit TestStand and 64-bit TestStand as separate product versions. However, 32-bit TestStand and 64-bit TestStand use separate <Program Files>, <TestStand Public>, and <TestStand Application Data> directories and therefore use independent settings, such

### Activating 32-bit TestStand and 64-bit TestStand

The TestStand Version Selector does not treat 32-bit TestStand and 64-bit TestStand as separate product versions. However, 32-bit TestStand and 64-bit TestStand use separate <Program Files>, <TestStand Public>, and <TestStand Application Data> directories and therefore use independent settings, such as station options.

Use the TestStand Version Selector to select the active TestStand version and click the Launch 32-bit button to launch the 32-bit TestStand Sequence Editor or click the Launch 64-bit button to launch the 64-bit TestStand Sequence Editor. Microsoft Windows Explorer uses the same bitness version of the sequence editor you last launched to open sequence files and other TestStand files. The TestStand File Diff and Merge utility also matches the bitness of the sequence editor you last launched.

When you make a previous TestStand version active, the TestStand Version Selector
 deactivates the current 32-bit TestStand and 64-bit TestStand. The Launch
 64-bit button is dimmed when a previous version of TestStand is active.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=activex-automation-server-concepts.html language=enus -->
## TOPIC 00038: ActiveX Automation Server Concepts

- bundle_id: `teststand`
- source_path: `activex-automation-server-concepts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/activex-automation-server-concepts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An ActiveX Automation server is any executable code that other applications can access. ActiveX uses a client/server relationship in which the client requests objects from the server and sends commands to the server to perform actions on the objects. Clients and servers can run on a single computer

### ActiveX Automation Server Concepts

An ActiveX Automation server is any executable code that other applications can access. ActiveX
 uses a client/server relationship in which the client requests objects from the
 server and sends commands to the server to perform actions on the objects.

Clients and servers can run on a single computer or on separate computers connected by a network. An ActiveX server is local when it runs on the same computer as its client and remote when it runs on a different computer.

On a single computer, an ActiveX server runs in-process or out-of-process with respect to the client. An in-process ActiveX server is a DLL that runs in the same process space as the client. An out-of-process ActiveX server is an executable and therefore does not run in the same process space as the client.

Note

Parent topic:

TestStand ActiveX API Overview

Related concepts:

- Objects, Classes, Methods, Properties, and Controls
- Object References
- Adding and Releasing References

<!--NI_TOPIC bundle=teststand path=activex-com-adapter.html language=enus -->
## TOPIC 00039: ActiveX/COM Adapter

- bundle_id: `teststand`
- source_path: `activex-com-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/activex-com-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the ActiveX/COM Adapter to create ActiveX/COM objects, call methods, and access properties of those objects. When you create an object, you can assign the object reference to a variable or property for later use in other ActiveX/COM Adapter steps. When you call methods and access properties, you

### ActiveX/COM Adapter

Use the ActiveX/COM Adapter to create ActiveX/COM objects, call methods, and access properties of those objects. When you create an object, you can assign the object reference to a variable or property for later use in other ActiveX/COM Adapter steps. When you call methods and access properties, you can specify an expression for each input and output parameter. Use the ActiveX/COM Adapter Configuration dialog box to configure the ActiveX/COM Adapter.

When you specify a module for a step, the TestStand Sequence Editor displays the ActiveX/COM Module tab, and the TestStand User Interfaces launch the Edit ActiveX/COM Call dialog box.

Parent topic:

Module Adapters

Related concepts:

- Adapter and Code Module Support for 64-bit TestStand
- ActiveX/COM Code Module Support for 64-bit TestStand
- Driver Support for 64-bit TestStand
- Module Adapter Parameter Mapping Guidelines

<!--NI_TOPIC bundle=teststand path=activex-com-code-module-support-for-64-bit-te.html language=enus -->
## TOPIC 00040: ActiveX/COM Code Module Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `activex-com-code-module-support-for-64-bit-te.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/activex-com-code-module-support-for-64-bit-te.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you migrate ActiveX/COM code modules from 32-bit TestStand to 64-bit TestStand or need to simultaneously support 32-bit TestStand and 64-bit TestStand, you must consider how you use in-process and out-of-process COM servers.

### ActiveX/COM Code Module Support for 64-bit TestStand

When you migrate ActiveX/COM code modules from 32-bit TestStand to 64-bit TestStand or need to simultaneously support 32-bit TestStand and 64-bit TestStand, you must consider how you use in-process and out-of-process COM servers.

Parent topic:

Adapter and Code Module Support for 64-bit TestStand

Related concepts:

- In-Process COM Servers Support in 32-bit TestStand and 64-bit TestStand
- Out-of-Process COM Servers in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=adapter-and-code-module-support-for-64-bit-te.html language=enus -->
## TOPIC 00041: Adapter and Code Module Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `adapter-and-code-module-support-for-64-bit-te.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adapter-and-code-module-support-for-64-bit-te.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Code modules that run in-process must match the bitness of TestStand or be bitness independent, such as an AnyCPU .NET assembly. The following table provides suggested strategies for migrating from 32-bit TestStand to 64-bit TestStand or simultaneously supporting 32-bit TestStand and 64-bit TestStan

### Adapter and Code Module Support for 64-bit TestStand

Code modules that run in-process must match the bitness of TestStand or be bitness independent, such as an AnyCPU .NET assembly. The following table provides suggested strategies for migrating from 32-bit TestStand to 64-bit TestStand or simultaneously supporting 32-bit TestStand and 64-bit TestStand.

| Adapter | Code Module Type | Notes |
| --- | --- | --- |
| C/C++ DLL Adapter | C/C++ DLL | DLL must match bitness of TestStand. Use the $(Platform) path macro, a custom search directory that differs based on architecture, or the <TestStand Public> directory to locate the correct DLL. |
| LabWindows/CVI Adapter | C DLL | DLL must match bitness of TestStand. Use the $(Platform) path macro, a custom search directory that differs based on architecture, or the <TestStand Public> directory to locate the correct DLL. |
| .NET Adapter | .NET assembly | Use AnyCPU assemblies when possible. Assemblies that target a particular architecture must match the bitness of TestStand. If you use platform-specific assemblies, use the $(Platform) path macro, a custom search directory that differs based on architecture, or the <TestStand Public> directory to locate the correct assembly. Note In TestStand 2023 Q4 and earlier, you can also use the GAC to locate the correct assembly. |
| ActiveX/COM Adapter | In-process COM server | Server must match the bitness of TestStand. TestStand automatically locates the server that matches its bitness using Microsoft Windows registry redirection. |
| ActiveX/COM Adapter | Out-of-process COM server | Server does not have to match the bitness of TestStand, but TestStand uses the version that matches its bitness if that version exists. |
| LabVIEW Adapter | VI | Use source-only VIs for all LabVIEW code modules to make the VIs bitness independent in most sequence files. Bitness of VIs you run in-process with the LabVIEW Run-Time Engine must match the bitness of TestStand. Bitness of VIs you run out-of-process does not need to match the bitness of TestStand. Packed project libraries must match the bitness of the LabVIEW server you are using. |
| Sequence Call Adapter | TestStand sequence files | NI recommends using bitness-independent sequences. |
| None Adapter | N/A | Works the same in 32-bit TestStand and in 64-bit TestStand. |
| HTBasic Adapter | HTBasic .prg file | 64-bit TestStand does not support HTBasic steps. |
| LabVIEW NXG Adapter | N/A | LabVIEW NXG modules can only be used with 64-bit TestStand. |
| Python Adapter | Python code module | Python version specified for use in execution must match bitness of TestStand. |

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand
- TestStand Directory Structure
- .NET Code Module Support for 64-bit TestStand
- In-Process COM Servers Support in 32-bit TestStand and 64-bit TestStand
- Out-of-Process COM Servers in 32-bit TestStand and 64-bit TestStand
- LabVIEW Code Module Support for 64-bit TestStand
- Sequence Call Adapter Support for 64-bit TestStand
- Python Code Module Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=add-release-references-msc-import.html language=enus -->
## TOPIC 00042: Adding and Releasing References in Microsoft Visual C++/#import

- bundle_id: `teststand`
- source_path: `add-release-references-msc-import.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/add-release-references-msc-import.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The pointer classes the #import directive generates automatically add object references when you construct a pointer, as shown in the following code: TS::PropertyObjectPtr newObjectPtr(objectPtr); The assignment operator of the pointer classes first releases the reference to the object it currently

### Adding and Releasing References in Microsoft Visual C++/#import

The pointer classes the #import directive generates automatically add object references when you construct a pointer, as shown in the following code:

TS::PropertyObjectPtr newObjectPtr(objectPtr);

The assignment operator of the pointer classes first releases the reference to the object it currently holds and then adds a reference to the object being assigned to it. For example, the following assignment statement first releases the reference to the object to which newObjectPtr refers and then adds a reference to the object to which objectPtr refers:

newObjectPtr = objectPtr;

The destructor for the pointer class releases the object reference. Assigning the value NULL to a pointer variable also releases the object reference, as shown in the following example:

objectPtr = NULL; // releases the reference

Parent topic:

Adding and Releasing References

<!--NI_TOPIC bundle=teststand path=add-release-references-msvb.html language=enus -->
## TOPIC 00043: Adding and Releasing References in Microsoft Visual Basic .NET

- bundle_id: `teststand`
- source_path: `add-release-references-msvb.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/add-release-references-msvb.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Microsoft Visual Basic .NET automatically adds object references when you assign the object to another variable, as shown in the following code: Set ReferenceObj = OtherReferenceObj Visual Basic .NET also automatically releases object references when a variable or list that contains a reference to a

### Adding and Releasing References in Microsoft Visual Basic .NET

Microsoft Visual Basic .NET automatically adds object references when you assign the object to another variable, as shown in the following code:

Set ReferenceObj = OtherReferenceObj

Visual Basic .NET also automatically releases object references when a variable or list that contains a reference to an object goes out of scope. Local variable scope ends when the function returns. You can initiate the release of a reference to an object by setting the variable to the value Nothing, as shown in the following code:

Set ReferenceObj = Nothing

Parent topic:

Adding and Releasing References

<!--NI_TOPIC bundle=teststand path=adding-and-releasing-references-csharp.html language=enus -->
## TOPIC 00044: Adding and Releasing References in C#

- bundle_id: `teststand`
- source_path: `adding-and-releasing-references-csharp.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-and-releasing-references-csharp.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: C# automatically adds object references when you assign the object to another variable, as shown in the following code: referenceObj = otherReferenceObj; C# also automatically releases object references when a variable or list that contains a reference to an object goes out of scope. Local variable

### Adding and Releasing References in C#

C# automatically adds object references when you assign the object to another variable, as shown in the following code:

referenceObj = otherReferenceObj;

C# also automatically releases object references when a variable or list that contains a reference to an object goes out of scope. Local variable scope ends when the function returns. You can initiate the release of a reference to an object by setting the variable to the value null, as shown in the following code:

referenceObj = null;

Parent topic:

Adding and Releasing References

<!--NI_TOPIC bundle=teststand path=adding-and-releasing-references-in-cvi.html language=enus -->
## TOPIC 00045: Adding and Releasing References in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `adding-and-releasing-references-in-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-and-releasing-references-in-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabWindows/CVI automatically maintains an object reference for each handle you obtain for an object. When you assign the handle to another variable, LabWindows/CVI does not add a reference to the object. Use the CA_DuplicateObjHandle function in the LabWindows/CVI ActiveX Automation Library to obtai

### Adding and Releasing References in LabWindows/CVI

LabWindows/CVI automatically maintains an object reference for each handle you obtain for an object. When you assign the handle to another variable, LabWindows/CVI does not add a reference to the object. Use the CA_DuplicateObjHandle function in the LabWindows/CVI ActiveX Automation Library to obtain a new handle to an existing object, which adds a reference to the object.

LabWindows/CVI automatically releases the object reference for each handle you obtain when you call the CA_DiscardObjHandle function from the LabWindows/CVI ActiveX Automation Library.

The following example shows how to obtain a handle to the TestStand Engine from the SequenceContext object, how to call a method on the engine to acquire a version string, and how to release the handle to the engine and the string.

int GetEngineVersion(CAObjHandle seqContextCVI)

{

int error = 0;

ErrMsg errMsg = "";

ERRORINFO errorInfo;

CAObjHandle engine = 0;

char *versionString = NULL;

tsErrChk(TS_SeqContextGetEngine(seqContextCVI, &errorInfo, &engine));

tsErrChk(TS_EngineGetVersionString (engine, &errorInfo, &versionString));

Error:

// Free Resources

if (engine)

CA_DiscardObjHandle(engine);

if (versionString)

CA_FreeMemory(versionString);

return error;

}

Note

While many of the functions specified in the tsapicvi.fp library are simple wrappers to API methods that require no storage of information, there are several functions, especially those containing Get or New, where TestStand is actively allocating new memory to hold the information. In any instance where you are using a function of this type, you must release the allocated memory at the end of the code using calls to CA_FreeMemory, CA_DiscardObjHandle, or similar functions.

When you are concerned about a function returning a piece of data that must be manually released, refer to the LabWindows/CVI Help or to the NI TestStand Help for that function. Both of these resources explicitly state if the function is allocating memory and often contain additional code fragments explaining how to use the function.

The following are examples of functions that allocate memory:

- TS_PropertyGetValString()
- TS_PropertyGetValIDispatch()
- TS_PropertyGetPropertyObject()
- TS_NewEngine()
- TS_SeqFileNewEditContext()
- TS_EngineNewSequence()

The following example uses one of the previous functions and then releases the memory:

char *stringVal = NULL;

TS_PropertyGetValString (propObj, &errorInfo, "Step.Limits.String", 0, &stringVal);

...

CA_FreeMemory (stringVal);

Parent topic:

Adding and Releasing References

<!--NI_TOPIC bundle=teststand path=adding-and-releasing-references-in-cvi_2.html language=enus -->
## TOPIC 00046: Adding and Releasing References in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `adding-and-releasing-references-in-cvi_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-and-releasing-references-in-cvi_2.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabWindows/CVI automatically maintains an object reference for each handle you obtain for an object. When you assign the handle to another variable, LabWindows/CVI does not add a reference to the object. Use the CA_DuplicateObjHandle function in the LabWindows/CVI ActiveX Automation Library to obtai

### Adding and Releasing References in LabWindows/CVI

LabWindows/CVI automatically maintains an object reference for each handle you obtain for an object. When you assign the handle to another variable, LabWindows/CVI does not add a reference to the object. Use the CA_DuplicateObjHandle function in the LabWindows/CVI ActiveX Automation Library to obtain a new handle to an existing object, which adds a reference to the object.

LabWindows/CVI automatically releases the object reference for each handle you obtain when you call the CA_DiscardObjHandle function from the LabWindows/CVI ActiveX Automation Library.

The following example shows how to obtain a handle to the TestStand Engine from the SequenceContext object, how to call a method on the engine to acquire a version string, and how to release the handle to the engine and the string.

int GetEngineVersion(CAObjHandle seqContextCVI)

{

int error = 0;

ErrMsg errMsg = "";

ERRORINFO errorInfo;

CAObjHandle engine = 0;

char *versionString = NULL;

tsErrChk(TS_SeqContextGetEngine(seqContextCVI, &errorInfo, &engine));

tsErrChk(TS_EngineGetVersionString (engine, &errorInfo, &versionString));

Error:

// Free Resources

if (engine)

CA_DiscardObjHandle(engine);

if (versionString)

CA_FreeMemory(versionString);

return error;

}

Note

While many of the functions specified in the tsapicvi.fp library are simple wrappers to API methods that require no storage of information, there are several functions, especially those containing Get or New, where TestStand is actively allocating new memory to hold the information. In any instance where you are using a function of this type, you must release the allocated memory at the end of the code using calls to CA_FreeMemory, CA_DiscardObjHandle, or similar functions.

When you are concerned about a function returning a piece of data that must be manually released, refer to the LabWindows/CVI Help or to the NI TestStand Help for that function. Both of these resources explicitly state if the function is allocating memory and often contain additional code fragments explaining how to use the function.

The following are examples of functions that allocate memory:

- TS_PropertyGetValString()
- TS_PropertyGetValIDispatch()
- TS_PropertyGetPropertyObject()
- TS_NewEngine()
- TS_SeqFileNewEditContext()
- TS_EngineNewSequence()

The following example uses one of the previous functions and then releases the memory:

char *stringVal = NULL;

TS_PropertyGetValString (propObj, &errorInfo, "Step.Limits.String", 0, &stringVal);

...

CA_FreeMemory (stringVal);

Parent topic:

Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=adding-and-releasing-references.html language=enus -->
## TOPIC 00047: Adding and Releasing References

- bundle_id: `teststand`
- source_path: `adding-and-releasing-references.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-and-releasing-references.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Whenever you create an ActiveX object directly or receive an ActiveX object as a return value from a method or property, you have a reference to the object. You must release this reference when you no longer require the object. Normally, when you receive an object as a parameter to a function or Lab

### Adding and Releasing References

Whenever you create an ActiveX object directly or receive an ActiveX object as a return value from a method or property, you have a reference to the object. You must release this reference when you no longer require the object.

Normally, when you receive an object as a parameter to a function or LabVIEW VI, you do not need to add or release a reference to the object because the caller of the function already holds a reference to the object. If, however, the function or VI stores the object for later use after the function or VI returns, you must add a reference to the object in the function or VI.

In general, maintaining a reference to an object guarantees that the object exists for at least at long as you hold the reference. The object frees its resources only when you release the final reference to the object.

Refer to the following examples for more information about adding and releasing references in specific development environments:

- LabVIEW
- LabWindows/CVI
- Microsoft Visual Basic .NET
- C#
- Microsoft Visual C++/#import

Parent topic:

Object References

Related concepts:

- Releasing ActiveX References in LabVIEW
- Adding and Releasing References in LabWindows/CVI
- Adding and Releasing References in Microsoft Visual Basic .NET
- Adding and Releasing References in C#
- Adding and Releasing References in Microsoft Visual C++/#import

<!--NI_TOPIC bundle=teststand path=adding-assembly-references-in-microsoft-visua.html language=enus -->
## TOPIC 00048: Adding Assembly References in Microsoft Visual Studio

- bundle_id: `teststand`
- source_path: `adding-assembly-references-in-microsoft-visua.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-assembly-references-in-microsoft-visua.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add an assembly reference in Microsoft Visual Studio. Select the project in the Solution Explorer. Select Project»Add Reference to launch the Add Reference dialog box. (Visual Studio 2010 and earlier) Click the .NET tab and select TestStand <Version> Utilities from th

### Adding Assembly References in Microsoft Visual Studio

Complete the following steps to add an assembly reference in Microsoft Visual Studio.

1. Select the project in the Solution Explorer.
2. Select Project»Add Reference to launch the Add Reference dialog box.
3. (Visual Studio 2010 and earlier) Click the .NET tab and select TestStand <Version> Utilities from the list of components.(Visual Studio 2012 and later) Click the Assemblies item and select Extensions . Select TestStand <Version> Utilities from the list of components.
4. Click OK to close the Add Reference dialog box.

Note

- TestStand <Version> Utilities is the name for the NationalInstruments.TestStand.Utility assembly.
- In Visual Studio 2012 and later, the Add Reference dialog box is named the Reference Manager dialog box.

When you add an assembly reference, you must also complete the following steps to change the value of the Embed Interop Types property of the referenced assembly to False.

1. In the Solution Explorer, select the referenced assembly in the References section of the project.
2. In the Properties window, change the value of the Embed Interop Types property to False .

Parent topic:

TestStand Utility Functions Library

<!--NI_TOPIC bundle=teststand path=adding-columns-and-rows-to-an-atml-test-resul.html language=enus -->
## TOPIC 00049: Adding Columns and Rows to an ATML Test Results 6.01 or 5.0 Report

- bundle_id: `teststand`
- source_path: `adding-columns-and-rows-to-an-atml-test-resul.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-columns-and-rows-to-an-atml-test-resul.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you add extra information to a report, confirm that other XSL templates do not already add to the report the result information you want to include. TR6_Horizontal.xsl or TR5_Horizontal.xsl To add custom columns to reports using the TR6_Horizontal.xsl or TR5_Horizontal.xsl file, you must modi

### Adding Columns and Rows to an ATML Test Results 6.01 or 5.0 Report

Before you add extra information to a report, confirm that other XSL templates do not already add to the report the result information you want to include.

#### TR6_Horizontal.xsl or TR5_Horizontal.xsl

To add custom columns to reports using the TR6_Horizontal.xsl or TR5_Horizontal.xsl file, you must modify the XSL templates to add a column and then add data to the new column. Complete the following steps to add an extra StepID column to the right side of the report table using the TR6_Horizontal.xsl or TR5_Horizontal.xsl file. You can also copy and add the following code for each new column you want to add.

1. Open the .xsl file you want to change.
2. Search for the <!-- Customization variables--> comment.
3. Search for the gNumExtraColumnsToAdd variable and increment the value of the gNumExtraColumnsToAdd variable by the number of columns you want to add. The initial value is 0 . For example, to add one extra column, replace the 0 value with 1 , which results in the following line of code: <xsl:variable name="gNumExtraColumnsToAdd" select="1"/>
4. Search for the CREATE_EXTRA_COLUMNS comment and uncomment the following
 code: <td rowspan="2" valign="bottom" style="text-align:center;" width="10%">
 <b>StepID</b>
</td>
5. Search for each of three instances of the ADD_COLUMN_DATA_1 comment and
 uncomment the following code for each instance:
 <td><xsl:value-of
 select="@testReferenceID"/></td> The expression
 "@testReferenceID" specifies the XPath expression to obtain the
 testReferenceID from the XML file. You must customize this XPath expression
 to match the data you want to add to the additional columns. Refer to the
 W3Schools website for more information on XPath. Refer to ATML Test Results
 6.01 and 5.0 Report Structure for the XML object structure.

The following figure shows a modified report with a StepID column added for Sequence Call steps using the TR6_Horizontal.xsl or TR5_Horizontal.xsl file.

[IMAGE alt='image' src='GUID-4BACA18E-EF75-477A-9230-E3BDCAD83C25-a5.png']

#### TR6_report.xsl, TR5_report.xsl, TR6_Expand.xsl, or TR5_Expand.xsl

Complete the following steps to add an extra row with StepID information under each step in the report table using the TR6_report.xsl, TR5_report.xsl, TR6_Expand.xsl, or TR5_Expand.xsl file.

1. Open the .xsl file you want to change.
2. Search for each of three instances of the ADD_EXTRA_ROWS comment and uncomment
 the following code for each
 instance: <tr>
 <td>StepID</td>
 <td><xsl:value-of select="@testReferenceID"/></td>
</tr>

The following figure shows a modified report with a StepID row added for Sequence Call steps using the TR6_report.xsl or TR5_report.xsl file.

[IMAGE alt='image' src='GUID-556EFC7C-2A0E-4D96-887F-9918D3D50285-a5.png']

The following figure shows a modified report with a StepID row added for Sequence Call steps using the TR6_Expand.xsl or TR5_Expand.xsl file.

[IMAGE alt='image' src='GUID-68061586-45A8-4F7C-AA49-9A2632AAE0CA-a5.png']

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

Related concepts:

- ATML Test Results 6.01 and 5.0 Report Structure

Related information:

- W3Schools

<!--NI_TOPIC bundle=teststand path=adding-columns-and-rows-to-an-xml-report.html language=enus -->
## TOPIC 00050: Adding Columns and Rows to an XML Report

- bundle_id: `teststand`
- source_path: `adding-columns-and-rows-to-an-xml-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-columns-and-rows-to-an-xml-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you add extra information to a report, confirm that other XSL templates do not already add to the report the result information you want to include. horizontal.xsl To add custom columns to reports using the horizontal.xsl file, you must modify the XSL templates and JavaScript code to add a co

### Adding Columns and Rows to an XML
 Report

Before you add extra information
 to a report, confirm that other XSL templates do not already add to the report the
 result information you want to include.

#### horizontal.xsl

To add
 custom columns to reports using the horizontal.xsl file, you must
 modify the XSL templates and JavaScript code to add a column and then add data to
 the new column. Complete the following steps to add an extra StepID column to the
 right side of the report table using the horizontal.xsl
 file.

1. Open the horizontal.xsl file.
2. Search for the CREATE_EXTRA_COLUMNS comment in the
 BeginTable function of the JavaScript section.
3. Uncomment the following code to add a new StepID column: "<td
 rowspan='2' valign='bottom' align='center' style='width:30%'><span
 style='font-size:0.6em'><b>StepID</b></span></td>\n"
 +
4. Search for the INITIALIZE_COLUMN_SPAN_VARIABLES comment and
 increment all the variables by the number of extra columns you are adding to set
 the column span for result data you add as rows to the report. Using column span
 information ensures that each row in the report includes the same number of
 columns and uses the correct formatting. Because you are adding only the StepID
 column in this example, replace the following
 code: <xsl:variable name="gSecondColumnSpan5" select="5"/> 
<xsl:variable name="gSecondColumnSpan6" select="6"/> 
<xsl:variable name="gSecondColumnSpan7" select="7"/> 
<xsl:variable name="gSecondColumnSpan8" select="8"/> with
 the following
 code: <xsl:variable name="gSecondColumnSpan5" select="6"/> 
<xsl:variable name="gSecondColumnSpan6" select="7"/> 
<xsl:variable name="gSecondColumnSpan7" select="8"/> 
<xsl:variable name="gSecondColumnSpan8" select="9"/>
5. Search for each of three instances of the ADD_COLUMN_DATA_1 
 comment and uncomment the following code for each instance:
 <td><xsl:value-of
 select="@testReferenceID"/></td> The expression
 "@testReferenceID" specifies the XPath expression to obtain the
 testReferenceID from the XML file. You must customize this XPath expression
 to match the data you want to add to the additional columns. Refer to the
 W3Schools website for more information on XPath. Refer to ATML Test Results
 6.01 and 5.0 Report Structure for the XML object structure.
6. Repeat steps 2 through 5 to add additional columns.

The following figure shows a modified report with a StepID column for Sequence
 Call steps using horizontal.xsl:

[IMAGE alt='image' src='GUID-F94B0206-1E2C-45CE-88E1-F0D8B7502682-a5.png']

#### report.xsl and
 expand.xsl

Complete the following steps to add an extra row with StepID
 information under each step in the report table using the
 report.xsl file and the expand.xsl
 file.

1. Open the report.xsl or expand.xsl file.
2. Search for the ADD_EXTRA_ROWS comment.
3. Uncomment the following code after the ADD_EXTRA_ROWS comment:
 <tr>
 <td>
 <xsl:attribute name="style">border-color:<xsl:value-of select="$reportOptions/Prop[2Name='Colors']/Prop
 [@Name='TableBorder']/Value"/></xsl:attribute>
 <span style='font-size:82%;'>StepID</span>
 </td>
 <td>
 <xsl:attribute name="style">border-color:<xsl:value-of select="$reportOptions/Prop[2Name='Colors']/Prop
 [@Name='TableBorder']/Value"/></xsl:attribute>
 <span style='font-size:82%;'><xsl:value-of select='./Prop[@Name='TS']/Prop[@Name='StepId']/Value"/></span>
 </td>
</tr>

The following figure shows a modified report with a StepID row using
 report.xsl:

[IMAGE alt='image' src='GUID-8B7A650D-70F8-4BB4-AC63-B62A1B619E9E-a5.png']

The
 following figure shows a modified report with a StepID row using
 expand.xsl:

[IMAGE alt='image' src='GUID-C37F188C-42E8-4E60-96CD-DE712FEEC90B-a5.png']

Parent topic:

Customizing XML Report Style Sheets

Related concepts:

- ATML Test Results 6.01 and 5.0 Report Structure

Related information:

- W3Schools

<!--NI_TOPIC bundle=teststand path=adding-columns-to-an-atml-test-results-2.html language=enus -->
## TOPIC 00051: Adding Columns to an ATML Test Results 2.02 Report

- bundle_id: `teststand`
- source_path: `adding-columns-to-an-atml-test-results-2.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-columns-to-an-atml-test-results-2.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to modify the TR_horizontal.xsl style sheet to modify the XSL templates and JavaScript code to add a new StepID column to the right side of the report table. You can also copy and add the following code for each new column you want to add. Open the TR_horizontal.xsl file

### Adding Columns to an ATML Test Results 2.02 Report

Complete the following steps to modify the TR_horizontal.xsl style sheet to modify the XSL templates and JavaScript code to add a new StepID column to the right side of the report table. You can also copy and add the following code for each new column you want to add.

1. Open the TR_horizontal.xsl file.
2. Search for the CREATE_EXTRA_COLUMNS comment in the StartTable 
 JavaScript function. Copy the following comment, paste the copy below the
 original, and uncomment the copy to add a new StepID column: "<td
 rowspan='2' valign='bottom' align='center' width='20%'><font
 size='1'><b>StepID</b></font></td>"
 + The StepID value is the heading of the
 new column. Modify this value to customize the column heading.
3. Search for the INITIALIZE_NUMBER_OF_CUSTOM_COLUMNS comment and increment the value of the gNoOfCustomColumns variable by the number of columns you want to add. Because you are adding only the StepID column in this example, replace the 0 value with 1 , which results in the following line of code: <xsl:variable name="gNoOfCustomColumns" select="1"/>
4. Search for each instance of the ADD_COLUMN_DATA comment and the uncomment the
 following
 code: <td align="right">
 <xsl:value-of select="n1:Extension/ts:TSStepProperties/ts:StepId"/>
</td> The
 expression "n1:Extension/ts:TSStepProperties/ts:StepId" 
 specifies the XPath expression to obtain the step ID from the XML file. You must
 customize the XPath expression to match the data you want to add to the
 additional columns. Refer to the World Wide Web Consortium (W3C) website,
 located at www.w3.org , for more information about XPath.
5. Repeat steps 2 through 4 to add additional columns.

Parent topic:

Customizing the ATML Test Results 2.02 Report Style Sheet

<!--NI_TOPIC bundle=teststand path=adding-custom-application-settings.html language=enus -->
## TOPIC 00052: Adding Custom Application Settings

- bundle_id: `teststand`
- source_path: `adding-custom-application-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-custom-application-settings.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: After the application calls the ApplicationMgr.Start method, complete the following steps to add your own setting to persist in the configuration file. Access the ApplicationMgr.ConfigFile property to obtain the PropertyObjectFile that holds the contents of the configuration file. Access the Propert

### Adding Custom Application Settings

After the application calls the ApplicationMgr.Start method, complete the following steps to add your own setting to persist in the configuration file.

1. Access the ApplicationMgr.ConfigFile property to obtain the PropertyObjectFile that holds the contents of the configuration file.
2. Access the PropertyObjectFile.Data property to obtain the PropertyObject that holds the application settings.
3. Ensure the custom setting exists in the PropertyObject by setting a default value of the setting by calling a method, such as the PropertyObject.SetValBoolean method, with a lookup string, such as "CustomSettings.MyExampleBooleanSetting" , and an options parameter of the PropOption_SetOnlyIfDoesNotExist constant.
4. Call a method, such as the PropertyObject.GetValBoolean method, to obtain the current value of the custom option.
5. Call a method, such as the PropertyObject.SetValBoolean method, with an options parameter of the PropOption_NoOptions constant to set the custom option in response to user input.

When you call the ApplicationMgr.Shutdown method or change any Application Manager control setting, the Application Manager control persists the application settings to the configuration file. You can also call the PropertyObjectFile.WriteFile method at any time to persist the settings.

Parent topic:

Persisting Application Settings

Related concepts:

- Application Manager

<!--NI_TOPIC bundle=teststand path=adding-custom-data-to-a-report.html language=enus -->
## TOPIC 00053: Adding Custom Data to a Report

- bundle_id: `teststand`
- source_path: `adding-custom-data-to-a-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-custom-data-to-a-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose You must complete the following tasks to add additional data to a report: Configure the desired property to be logged as a result. Results are stored in the Locals.ResultList array. Configure the result to be added to the report. This is typically accomplished by enabling the \IncludeInRepor

### Adding Custom Data to a Report

#### Purpose

You must complete the following tasks to add additional data to a report:

- Configure the desired property to be logged as a result. Results are stored in the Locals.ResultList array.
- Configure the result to be added to the report. This is typically accomplished by enabling the \IncludeInReport\ flag.

This example demonstrates the following approaches for adding custom data to a report:

- Using the UUT.AddtionalData container to add data to the report header
- Using the API method Execution.AddExtraResult
- Creating a custom property and setting the IncludeInReport flag
- Creating a custom step type with custom properties in the Step.Result container
- Using the Additional Results step type or property setting

#### Example File
 Location

<TestStand
 Public>\Examples\Customizing Result Processing\Adding Custom Data
 To a Report\Adding Custom Data To a Report.seq

#### Highlighted Features

- TestStand API
- PreUUT Callback
- Custom step types

#### Major API

- Execution.AddExtraResult
- PropertyObject.SetValString
- PropertyObject.SetFlags

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Single Pass to execute the sequence.
2. As the example executes, read the message popups for information about each method demonstrated.

Complete the following steps to review the sequences and steps in this example.

1. Select the PreUUT Callback in the sequences pane. Note that the statement steps create new properties in the Parameters.UUT.AdditionalData container, which will appear in the report header. The PropertyObject.SetFlags method is used to configure the property to display in the report.
2. Select the AddExtraResult sequence. This sequence calls the Execution.AddExtraResult method to add the Step.MessageExpr property to the Result list. For the property to appear in the report, the IncludeInReport flag must be enabled for this property.
3. Select the CustomProperty sequence. This sequence uses the PropertyObject.SetValString method to create a new property in a Numeric Limit Test step. The sequence then calls PropertyObject.SetFlags to enable the IncludeInReport flag for the new property so that it is displayed in the report.
4. Select the CustomStepType sequence. This sequence calls a step type which has an additional property in the results container. The IncludeInReport flag for this property is enabled in the step type definition, so you do not need to enable it for each instance of the type.
5. Select the AdditionalResults sequence. This sequence uses the Additional Results step to log additional data to the report. It also uses the Log option for parameters in the Calculate Area of Circle code module to log the parameter values

Parent topic:

Examples for Customizing Result Processing

Related concepts:

- Storing Additional Information for UUTs and Test Stations in Process Models
- TestStand Directory Structure
- Custom Step Types

<!--NI_TOPIC bundle=teststand path=adding-custom-images-to-a-report.html language=enus -->
## TOPIC 00054: Adding Custom Images to a Report

- bundle_id: `teststand`
- source_path: `adding-custom-images-to-a-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-custom-images-to-a-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example is identical to the computer.seq example included in the <TestStand Public>\Examples\Demo directory except that it demonstrates how to modify the report of any failed diagnostic test steps to include HTML hyperlinks. When you are using an HTML-compatible report viewer, scroll do

### Adding Custom Images to a Report

#### Purpose

This example is identical to the computer.seq example included in the <TestStand Public>\Examples\Demo directory except that it demonstrates how to modify the report of any failed diagnostic test steps to include HTML hyperlinks. When you are using an HTML-compatible report viewer, scroll down in the report to view any failed tests.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Customizing Result Processing\Adding Custom
 Images To a Report\Adding Custom Images To a Report.seq

#### Highlighted Features

Generating a test report

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Note

Toggle Analyze File Before Executing

Continue Execution

Complete the following steps to use this example.

1. Select Execute»Single Pass to run the sequence. TestStand launches the Test Simulator dialog box, in which you select a computer motherboard test that you want to fail.
2. Select at least one test to fail and click Done . After execution completes, TestStand displays the report on the Report pane.
3. Review the report. The Failure Section of the report lists the steps that failed and, for each failed step, includes an HTML hyperlink that links to the section of the report with more information about the step.
4. Close the Report pane.
5. In the Sequence File window, select the second If step. The If Condition edit tab specifies an expression that determines whether any test in the sequence failed. If a test failed, the sequence checks the status of each test and calls computer.dll , located in the <TestStand Public>\Examples\Customizing Result Processing\Adding Custom Images To a Report\HTMLDiagnosticLinks directory, to determine what information to add to the report. TestStand passes value by reference so the DLL can update the report.

This example uses a DLL to maintain modular and reusable code, but you can also configure each step that fails to add HTML content directly to the report.

Parent topic:

Examples for Customizing Result Processing

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=adding-dynamically-called-files-to-a-workspac.html language=enus -->
## TOPIC 00055: Adding Dynamically Called Files to a Workspace

- bundle_id: `teststand`
- source_path: `adding-dynamically-called-files-to-a-workspac.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-dynamically-called-files-to-a-workspac.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add dynamically called files to a workspace. Select Tools»Deploy TestStand System in the TestStand Sequence Editor to launch the TestStand Deployment Utility. On the System Source tab, enable the Deploy Files»From TestStand Workspace File option. To deploy a dynamical

### Adding Dynamically Called Files to a Workspace

Complete the following steps to add dynamically called files to a workspace.

1. Select Tools»Deploy TestStand System in the TestStand Sequence Editor to launch the TestStand Deployment Utility.
2. On the System Source tab, enable the Deploy Files»From TestStand Workspace File option. To deploy a dynamically called file, you must add the file to a workspace that you deploy.
3. Click the File Browse button located to the right of the From TestStand Workspace File control.
4. Browse to the <TestStand Public>\Examples\Fundamentals\Deployment directory and select the Dynamically_called_sequence.tsw workspace file.
5. Click Open .
6. Click the Distributed Files tab.
7. Click Yes in the dialog box that launches to allow the deployment utility to analyze the workspace file and dependent files.
8. Click the Build Status tab and review the Status Log, which reports a warning that an expression calls a sequence file you might need to add to the workspace.
9. Click the Distributed Files tab and notice that Dynamic.seq is missing in the Distributed Files list.
10. In the sequence editor, open the <TestStand Public>\Examples\Fundamentals\Deployment\Dynamically_called_sequence.tsw workspace file.
11. Add <TestStand Public>\Examples\Fundamentals\Deployment\Dynamic.seq to the workspace file and save the changes.
12. On the Distributed Files tab of the deployment utility, click the Analyze Source Files button to analyze the modified workspace file. Notice that the Distributed File list now includes Dynamic.seq .
13. Click the Build Status tab and review the Status Log, which reports a warning about an expression calling a sequence file. You can ignore the warning because you just added the correct sequence to the workspace.

#### Configuring the Installer

Complete the following steps to configure the installer.

1. On the Installer Options tab, use the Installer Directory control to specify the directory to which the deployment utility copies the installer for the test system and enable the Install TestStand Runtime option.
2. Click the Drivers and Components button to launch the Drivers and Components dialog box, in which you can select additional components to include in the installer.
3. Disable the Only display runtime installers option to display the
 TestStand product.
4. Select the TestStand product to include the sequence editor in the TestStand Runtime installation.
5. Click OK to apply the new settings and close the dialog box.
6. Click Save to save the build as Dynamic.tsd .
7. Click the Build button to build the installer.

#### Package-based distribution

Complete the following steps to configure the package distribution:

1. On the Mode tab, select the Package-based Distribution output type, then select the Package Installer option.
2. On the Package Distribution Options tab, use the Output Directory control to specify the directory to which the deployment utility copies the installer for the test system.
3. On the Package Distribution Options tab, enable the Install TestStand Runtime option.
4. Click the Dependencies button to launch the Drivers and Components dialog box, in which you can select additional components to include in the distribution.
5. Select the TestStand Sequence Editor product to include the sequence editor in the TestStand Runtime installation.
6. Click OK to apply the new settings and close the dialog box.
7. Click Save to save the build as EnginePackageInstaller.tsd.
8. Click Build to build the package installer.

#### Installing the Test System

Complete the following steps to install the test system.

1. To use the installer, copy all the files from the installer directory you specified on the Installer Options tab to the distribution media you want to use or to a shared directory on a network.
2. On the test station computer, insert the distribution media or connect to the network and run the installer executable to start the installer.
3. When the installation completes, complete the following steps to verify that the TestStand Runtime installed correctly.
  - Launch NI Package Manager
  - Select the Installed tab, and enter teststand in the search field.
  - Verify that the TestStand products you included are present in the list of packages.
4. Activate a license when the sequence editor prompts you.
5. Verify the installation by loading and running <TestStand Public>\Examples\Fundamentals\Deployment\Call_sequence_dynamically.seq .
6. On the Mode tab, select the MSI-based installer output type.

Parent topic:

Common Deployment Scenarios

Related concepts:

- TestStand Directory Structure
- Activating and Licensing TestStand
- Distributing a User Interface
- Distributing Tests from a Workspace

<!--NI_TOPIC bundle=teststand path=adding-images-and-text-to-an-atml-test-result.html language=enus -->
## TOPIC 00056: Adding Images and Text to an ATML Test Results 6.01 or 5.0 Report Header or Footer

- bundle_id: `teststand`
- source_path: `adding-images-and-text-to-an-atml-test-result.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-images-and-text-to-an-atml-test-result.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can modify the XSL code that generates report headers and footers. Complete the following steps to add images and text to report headers and footers. Open the .xsl file you want to change. Search for the ADD_HEADER_INFO comment and uncomment the following lines of code to add a company logo and

### Adding Images and Text to an ATML Test Results 6.01 or 5.0 Report Header or Footer

You can modify the XSL code that generates report headers and footers. Complete the following steps to add images and text to report headers and footers.

1. Open the .xsl file you want to change.
2. Search for the ADD_HEADER_INFO comment and uncomment the following lines of
 code to add a company logo and Computer Motherboard Test text
 to the header of the report:
 <img src = 'C:/Images/CompanyLogo.jpg'/>
<span style="font-size:1.13em;color:#003366;">Computer Motherboard Test</span> The
 HTML <img> tag provides additional functionality, such as
 aligning the image to the left, right, or center. Refer to the W3Schools
 website, located at www.w3schools.com , for more information
 about the <img> tag.
3. Search for the ADD_FOOTER_INFO comment and uncomment the following lines of
 code before the closing </body> tag to add the text
 TestStand Generated Report to the footer of the report:
 <span style="font-size:1.13em;color:#003366;">TestStand Generated Report</span>
4. Add CompanyLogo.jpg to the C:\Images directory.

#### TR6_Horizontal.xsl or TR5_Horizontal.xsl

The following figure shows a modified report header using the TR6_Horizontal.xsl or TR5_Horizontal.xsl file.

[IMAGE alt='image' src='GUID-18C42AD4-BB5A-4349-8C5F-67342F1B2FA4-a5.png']

The following figure shows a modified report footer using the TR6_Horizontal.xsl or TR5_Horizontal.xsl file.

[IMAGE alt='image' src='GUID-E33090D6-FF58-45F6-9C78-A70A5EE21069-a5.png']

#### TR6_report.xsl or TR5_report.xsl

The following figure shows a modified report header using the TR6_report.xsl or TR5_report.xsl file.

[IMAGE alt='image' src='GUID-87F6A280-8F36-4D56-AAE5-D01FECD64BCA-a5.png']

The following figure shows a modified report footer using the TR6_report.xsl or TR5_report.xsl file.

[IMAGE alt='image' src='GUID-26F0923E-9020-4482-9829-5690B5596220-a5.png']

#### TR6_Expand.xsl or TR5_Expand.xsl

The following figure shows a modified report header using the TR6_Expand.xsl or TR5_Expand.xsl file.

[IMAGE alt='image' src='GUID-D055DACF-EED7-46C1-884E-7639FFA86E81-a5.png']

The following figure shows a modified report footer using the TR6_Expand.xsl or TR5_Expand.xsl file.

[IMAGE alt='image' src='GUID-7EE6F2AC-3070-437C-A697-DFD9A6F44110-a5.png']

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

<!--NI_TOPIC bundle=teststand path=adding-images-and-text-to-an-xml-report-heade.html language=enus -->
## TOPIC 00057: Adding Images and Text to an XML Report Header or Footer

- bundle_id: `teststand`
- source_path: `adding-images-and-text-to-an-xml-report-heade.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-images-and-text-to-an-xml-report-heade.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can modify the XSL code that generates report headers and footers. Complete the following steps to add images and text to report headers and footers using the horizontal.xsl file, report.xsl file, or expand.xsl file. Open the .xsl file you want to change. Remove the comment tags from around the

### Adding Images and Text to an XML Report Header or Footer

You can modify the XSL code that generates report headers and footers. Complete the following steps to add images and text to report headers and footers using the horizontal.xsl file, report.xsl file, or expand.xsl file.

1. Open the .xsl file you want to change.
2. Remove the comment tags from around the following lines of code after the ADD_HEADER_INFO comment to add a company logo to the header and add a Computer Motherboard Test header to the report: <img src = 'c:\Images\CompanyLogo.jpg'/> <span style="font-size:1.13em;color:#003366;">Computer Motherboard Test</span><br/> The HTML <img> tag provides additional functionality, such as aligning the image to the left, right, or center. Refer to the W3Schools website, located at www.w3schools.com , for more information about the <img> tag.
3. Search for the ADD_FOOTER_INFO comment and remove the comment tags from around the following line of code before the closing </body> tag to add the text TestStand Generated Report to the footer of the report: <span style = "font-family:arial;color:#003366;">TestStand Generated Report</span>
4. Add CompanyLogo.jpg to the C:\Images directory.

#### horizontal.xsl

The following figure shows a modified report header using horizontal.xsl:

[IMAGE alt='image' src='GUID-611BE40A-9C3C-4174-AF1B-4375BAFC5B66-a5.png']

The following figure shows a modified report footer using horizontal.xsl:

[IMAGE alt='image' src='GUID-A48E8D2C-7859-403A-BF2B-A0101E674F3C-a5.png']

#### report.xsl

The following figure shows a modified report header using report.xsl:

[IMAGE alt='image' src='GUID-00A7135A-491C-4BF1-8BEA-CEF2FF2AF875-a5.png']

The following figure shows a modified report footer using report.xsl:

[IMAGE alt='image' src='GUID-F81A18EC-5A25-49CA-B1D6-A1FF3E5F4EB6-a5.png']

#### expand.xsl

The following figure shows a modified report header using expand.xsl:

[IMAGE alt='image' src='GUID-D81ECE4D-9CBF-4CB1-9A77-184F4A181118-a5.png']

The following figure shows a modified report footer using expand.xsl:

[IMAGE alt='image' src='GUID-8FDE074D-7781-4209-8C64-391B4C8BA92C-a5.png']

Parent topic:

Customizing XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=adding-new-files-to-a-patch-deployment.html language=enus -->
## TOPIC 00058: Adding New Files to a Patch Deployment

- bundle_id: `teststand`
- source_path: `adding-new-files-to-a-patch-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-new-files-to-a-patch-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modify the existing code of a test system to add new projects to a workspace, add new sequence files and any other additional new files to existing TestStand projects, or add new steps to a sequence. When you create a patch deployment, the TestStand Deployment Utility automatically detects the chang

### Adding New Files to a Patch Deployment

Modify the existing code of a test system to add new projects to a workspace, add new sequence files and any other additional new files to existing TestStand projects, or add new steps to a sequence. When you create a patch deployment, the TestStand Deployment Utility automatically detects the changes and adds new files to the list of top-level files. Use the Distributed Files tab of the deployment utility to change the destination or file properties of the new files.

Note

Parent topic:

Including and Excluding Files in MSI-based Installer Patches

<!--NI_TOPIC bundle=teststand path=adding-rule-settings-custom-tsa.html language=enus -->
## TOPIC 00059: Adding Rule Settings for Custom Rules in the TestStand Sequence Analyzer

- bundle_id: `teststand`
- source_path: `adding-rule-settings-custom-tsa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-rule-settings-custom-tsa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to add rule settings for users to configure custom rules. On the Advanced tab of the Edit Rule dialog box, select Use Rule Settings from the Configuration Option ring control. Click the Add button to add a new setting. Use the Rule Settings table to edit the name, type,

### Adding Rule Settings for Custom Rules in the
 TestStand Sequence Analyzer

Complete the following steps to add rule
 settings for users to configure custom rules.

1. On the Advanced tab of the Edit Rule
 dialog box, select Use Rule Settings from the
 Configuration Option ring control.
2. Click the Add button to add a new setting.
3. Use the Rule Settings table to edit the name, type, and default value for the
 new setting. Rule settings can have number, string, Boolean, or enumeration
 types. Click the Enums button to launch the
 Edit Rule Settings Enumerations dialog box, in which
 you create new rule settings enumeration types to use for rule settings. 
 Note When you add
 rule settings to a custom rule, the Rules pane or tab
 displays a Settings button next to the rule in the
 Edit Rule dialog box. Click the
 Settings button to launch the Rule
 Settings dialog box.

- Advanced tab 
 Accessing Rule Settings in Analysis Modules 
 Edit Rule Settings Enumerations dialog box 
 Edit Rule dialog box 
 Rules pane 
 Rule Settings dialog box 
 Rules tab

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand path=adding-sequence-call-step-results-to-an-atml.html language=enus -->
## TOPIC 00060: Adding Sequence Call Step Results to an ATML Test Results 6.01 or 5.0 Report without Indentation

- bundle_id: `teststand`
- source_path: `adding-sequence-call-step-results-to-an-atml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-sequence-call-step-results-to-an-atml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to ensure that a report does not indent Sequence Call step results using the TR6_report.xsl, TR5_report.xsl, TR6_Expand.xsl, or TR5_Expand.xsl file. Open the .xsl file you want to change. Search for the <!-- Customization variables--> comment. Search for the gIndentSeque

### Adding Sequence Call Step Results to an ATML Test Results 6.01 or 5.0 Report without Indentation

Complete the following steps to ensure that a report does not indent Sequence Call step results using the TR6_report.xsl, TR5_report.xsl, TR6_Expand.xsl, or TR5_Expand.xsl file.

1. Open the .xsl file you want to change.
2. Search for the <!-- Customization variables--> comment.
3. Search for the gIndentSequenceCalls variable and change the value of the select attribute from true to false , which results in the following line of code: <xsl:variable name="gIndentSequenceCalls" select="false()"/>

Note

#### TR6_report.xsl or TR5_report.xsl

The following figure shows a modified report that includes Sequence Call steps without indentation using the TR6_report.xsl or TR5_report.xsl file.

[IMAGE alt='image' src='GUID-9B30B846-0205-4DC8-890B-C9039E384694-a5.png']

#### TR6_Expand.xsl or TR5_Expand.xsl

The following figure shows a modified report that includes Sequence Call steps without indentation using the TR6_Expand.xsl or TR5_Expand.xsl file.

[IMAGE alt='image' src='GUID-F5E48394-CB32-4CFF-9B05-8B2F1DD8D54A-a5.png']

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

<!--NI_TOPIC bundle=teststand path=adding-sequence-call-step-results-to-an-xml-r.html language=enus -->
## TOPIC 00061: Adding Sequence Call Step Results to an XML Report without Indentation

- bundle_id: `teststand`
- source_path: `adding-sequence-call-step-results-to-an-xml-r.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-sequence-call-step-results-to-an-xml-r.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: None horizontal.xsl Change the value of the global JavaScript variable gIndentTables from True to False in the horizontal.xsl file to disable indentation of the Sequence Call step result tables in the report. Flow Control steps continue to indent even with this customization. The following figure sh

### Adding Sequence Call Step Results to an XML Report without Indentation

None

#### horizontal.xsl

Change the value of the global JavaScript variable gIndentTables from True to False in the horizontal.xsl file to disable indentation of the Sequence Call step result tables in the report.

Note

The following figure shows a modified report that includes Sequence Call steps without indentation using horizontal.xsl:

[IMAGE alt='image' src='GUID-48EB31C4-BCBA-43CA-AD6B-958DBEA2FBCC-a5.png']

#### report.xsl

Complete the following steps in the report.xsl file to disable indentation of the Sequence Call step result tables in the report.

1. Open the report.xsl file.
2. Search for all instances of the REMOVE_INDENTATION comment.
3. Comment out <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() + 1)"/> and <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() - 1)"/> by replacing the code with <!-- <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() + 1)"/> --> and <!-- <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() - 1)"/> --> , respectively.

Note

The following figure shows a modified report that includes Sequence Call steps without indentation using report.xsl:

[IMAGE alt='image' src='GUID-5DB7D7AD-B82F-463E-9BFB-19B5713A4AA6-a5.png']

#### expand.xsl

Complete the following steps in the expand.xsl file to disable indentation of the Sequence Call step result tables in the report.

1. Open the expand.xsl file.
2. Search for all instances of the REMOVE_INDENTATION comment.
3. Comment out <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() + 1)"/> and <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() - 1)"/> by replacing the code with <!-- <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() + 1)"/> --> and <!-- <xsl:value-of select="user:SetIndentationLevel(user:GetIndentationLevel() - 1)"/> --> , respectively.

Note

The following figure shows a modified report that includes Sequence Call steps without indentation using expand.xsl:

[IMAGE alt='image' src='GUID-6398AA55-71C6-459C-90BA-8AD69CCD71AA-a5.png']

Parent topic:

Customizing XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=adding-step-results-to-an-atml-test-results-6.html language=enus -->
## TOPIC 00062: Adding Step Results to an ATML Test Results 6.01 or 5.0 Report without Indentation

- bundle_id: `teststand`
- source_path: `adding-step-results-to-an-atml-test-results-6.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-step-results-to-an-atml-test-results-6.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to ensure a report does not indent any step results using the TR6_Horizontal.xsl, TR5_Horizontal.xsl, TR6_report.xsl, TR5_report.xsl, TR6_Expand.xsl, or TR5_Expand.xsl files. Open the .xsl file you want to change. Search for the Customization variables comment. Search fo

### Adding Step Results to an ATML Test
 Results 6.01 or 5.0 Report without Indentation

Complete the following steps to
 ensure a report does not indent any step results using the
 TR6_Horizontal.xsl, TR5_Horizontal.xsl,
 TR6_report.xsl, TR5_report.xsl,
 TR6_Expand.xsl, or TR5_Expand.xsl
 files.

1. Open the .xsl file you want to change.
2. Search for the Customization variables comment.
3. Search for the gRemoveIndentationFunctionality variable and
 change the value of the select attribute from "false" to "true", which results
 in the following line of code: <xsl:variable name="gRemoveIndentationFunctionality"select="true()"/>

The following figure shows a modified report without indentation using the
 TR6_Horizontal.xsl or TR5_Horizontal.xsl
 file.

[IMAGE alt='image' src='GUID-18407883-DC34-41C0-B8D2-31830C91E99E-a5.png']

The following figure shows a modified report without indentation using the
 TR6_report.xsl or TR5_report.xsl
 file.

[IMAGE alt='image' src='GUID-24C89215-EDB5-4153-BFD3-DB93A30D729E-a5.png']

The following figure shows a modified report without
 indentation using the TR6_Expand.xsl or
 TR5_Expand.xsl file.

[IMAGE alt='image' src='GUID-E3ABDF2A-DB68-4828-9744-76A08B43B57A-a5.png']

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

<!--NI_TOPIC bundle=teststand path=adding-step-types-to-surround-selection-with.html language=enus -->
## TOPIC 00063: Adding Step Types to Surround Selection With Context Menu

- bundle_id: `teststand`
- source_path: `adding-step-types-to-surround-selection-with.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-step-types-to-surround-selection-with.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a custom step type to the Surround Selection With context menu of the Steps pane and to add an end step after the last step in the contiguous block of steps you selected. Complete the following steps to add the custom step type to the Surround Selection With conte

### Adding Step Types to Surround Selection With Context Menu

Complete the following steps to add a custom step type to the Surround Selection With context menu of the Steps pane and to add an end step after the last step in the contiguous block of steps you selected.

1. Complete the following steps to add the custom step type to the Surround Selection With context menu.
  1. Right-click the custom step type and select Properties to launch the Step Type Properties dialog box.
  2. Click the Advanced button and select Block Structure from the drop-down menu to launch the Block Structure dialog box.
  3. Enable the Can Surround a Selection of Steps option to include the custom step type in the Surround Selection With context menu.
2. Create an OnNewStep substep to execute when you insert an instance of the custom step type.
3. Create a code module for the OnNewStep substep to check the value of the Boolean SequenceContext.RunState.ShouldEncapsulate property to determine where to add a corresponding end step.When you use the Insert Step menu or the Insertion Palette to insert a new step, the SequenceContext.RunState.ShouldEncapsulate property does not exist, and the SequenceContext.SelectedSteps property contains the newly inserted step.When you use the Surround Selection With menu to surround a set of selected steps with corresponding begin and end steps, the SequenceContext.RunState.ShouldEncapsulate property is True , and the SequenceContext.SelectedSteps property contains the set of selected steps.In the code module for the OnNewStep substep, verify that the SequenceContext.RunState.ShouldEncapsulate Boolean property exists and is True . When the SequenceContext.RunState.ShouldEncapsulate property is True , you must add the corresponding end step after the last step of the selected steps. When the SequenceContext.RunState.ShouldEncapsulate property is False or does not exist, you can add the end step after the newly inserted step or in another location you specify.

Parent topic:

Custom Step Types

Related concepts:

- Using Substeps

<!--NI_TOPIC bundle=teststand path=adding-support-for-other-database-management.html language=enus -->
## TOPIC 00064: Adding Support for Other Database Management Systems

- bundle_id: `teststand`
- source_path: `adding-support-for-other-database-management.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-support-for-other-database-management.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add support for database management systems (DBMSs) other than SQL Server, Oracle, Microsoft Access, Sybase, and MySQL by adding a new schema in the Database Options dialog box or by using SQL scripts. Click the Duplicate button on the Schemas tab of the Database Options dialog box to copy a

### Adding Support for Other Database Management Systems

You can add support for database management systems (DBMSs) other than SQL Server, Oracle, Microsoft Access, Sybase, and MySQL by adding a new schema in the Database Options dialog box or by using SQL scripts.

Click the Duplicate button on the Schemas tab of the Database Options dialog box to copy an existing schema and then customize the statement, column, and parameter settings to work with the new DBMS. The TestStand schemas for each DBMS conform to the default database tables.

Alternatively, you can create result tables for the default table schema for a similar DBMS by using the SQL script files located in the <TestStand>\Components\Models\TestStandModels\Database directory and modifying the schema for the new DBMS.

You can also complete the following steps to create new script files for a DBMS.

1. Create new script files in the <TestStand
 Public>\Components\Models\TestStandModels\Database directory. NI recommends
 including the name of the DBMS in the filename.
2. In the new script files, enter the SQL commands for creating and deleting DBMS tables. Refer to
 the SQL database script files TestStand provides for guidelines. For example,
 the SQL database syntax file for Oracle result tables might contain the
 following commands for creating a UUT_Result table:
 CREATE TABLE UUT_RESULT 
(
 ID NUMBER PRIMARY KEY,
 UUT_SERIAL_NUMBER CHAR (255),
 USER_LOGIN_NAME CHAR (255),
 START_DATE_TIME DATE,
 EXECUTION_TIME NUMBER,
 UUT_STATUS CHAR (255),
 UUT_ERROR_CODE NUMBER,
 UUT_ERROR_MESSAGE CHAR (255) 
) 
/ 
CREATE SEQUENCE SEQ_UUT_RESULT START WITH 1 
/ 
CREATE FUNCTION UUT_RESULT_NEXT_ID RETURN NUMBER IS
 X NUMBER; 
BEGIN
 SELECT SEQ_UUT_RESULT.NextVal INTO X FROM DUAL;
 RETURN X; 
END; 
/ Note 
 Notice that the script uses three separate commands, each separated by the
 "/" character, to create the UUT_RESULT table in
 Oracle. Use a similar syntax for deleting tables. For example, the SQL
 script file for Oracle might contain the following commands for deleting a
 UUT_RESULT table:
 DROP TABLE UUT_RESULT 
/
DROP SEQUENCE SEQ_UUT_RESULT
/ 
DROP FUNCTION UUT_RESULT_NEXT_ID 
/

Parent topic:

TestStand Database Result Tables

Related concepts:

- TestStand Directory Structure
- UUT_RESULT Table Schema

<!--NI_TOPIC bundle=teststand path=adding-type-libraries-to-labwindows-cvi-dlls.html language=enus -->
## TOPIC 00065: Adding Type Libraries to LabWindows/CVI DLLs

- bundle_id: `teststand`
- source_path: `adding-type-libraries-to-labwindows-cvi-dlls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-type-libraries-to-labwindows-cvi-dlls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a DLL contains export information or when a LabWindows/CVI DLL file contains a type library, the LabWindows/CVI Adapter automatically populates the Function control on the LabWindows/CVI Module tab with all the function names the DLL exports. In addition, when you select a function in the DLL,

### Adding Type Libraries to LabWindows/CVI DLLs

When a DLL contains export information or when a LabWindows/CVI DLL file contains a type library, the LabWindows/CVI Adapter automatically populates the Function control on the LabWindows/CVI Module tab with all the function names the DLL exports.

In addition, when you select a function in the DLL, the adapter queries the export information or the type library for the parameter list information and adds it in the Parameters Table control on the LabWindows/CVI Module tab.

You must enter the parameter information manually in the Parameters Table control for DLLs created with LabWindows/CVI 6.0 or earlier and for DLLs that do not have type library information.

Parent topic:

Calling DLLs from TestStand

Related concepts:

- Programming with the TestStand API in LabWindows/CVI
- Generating Type Library Information to Include in a DLL
- Specifying String Buffer Size in a Type Library

<!--NI_TOPIC bundle=teststand path=adding-users-and-setting-privileges.html language=enus -->
## TOPIC 00066: Adding Users and Setting Privileges

- bundle_id: `teststand`
- source_path: `adding-users-and-setting-privileges.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/adding-users-and-setting-privileges.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand User Manager to maintain the list of users, user names, user passwords, user privileges, groups, group privileges, and members of groups. TestStand can limit the functionality of the TestStand Sequence Editor and User Interfaces depending on the privilege settings you specify in th

### Adding Users and Setting Privileges

Use the TestStand User Manager to maintain the list of users, user names, user passwords, user privileges, groups, group privileges, and members of groups. TestStand can limit the functionality of the TestStand Sequence Editor and User Interfaces depending on the privilege settings you specify in the user manager for the current user and the groups to which the user belongs.

The user manager helps you implement policies and procedures that concern the use of test stations. The user manager is not a security system, and it does not inhibit or control the operating system or third-party applications. Use the system-level security features the operating system provides to secure test station computers against unauthorized use.

Note

<TestStand Public>\Tutorial\Solution

#### Adding a New User

Note

administrator

File»Login

administrator

OK

Complete the following steps to add a new user.

1. Click the User Manager button on the toolbar to open the User Manager window, which shows all the users and groups configured on the test station.
2. Right-click the Users item, select Insert User from the context menu, and enter a name to create a new user.
3. Right-click the new user you just added, select Properties from the context menu to launch the <User> Properties dialog box, and complete the following steps.
  1. Confirm that the User Name control displays the new name you entered.
  2. Enter the full name in the Full Name control.
  3. Enter a password in the Password and Confirm Password controls.
  4. Select Operator in the Group Privileges control.
  5. Click OK to close the User Properties dialog box.
4. Save the changes to the user manager.
5. Select File»Login to launch the Login dialog box. The User Name ring control now includes the new user you just added.
6. Select the user you just created, enter the appropriate password, and click OK .
7. Open <TestStand Public>\Tutorial\Computer.seq .
8. Select the Execute menu and notice that the Single Pass and Run MainSequence options of the Execute menu are disabled because the user you just created does not have the privileges to execute them.
9. Right-click the Steps pane to insert a new step. The Insert Step menu command is also disabled because the user privileges have changed.
10. Select File»Login and select administrator from the User Name ring control. Leave the Password field empty and click OK .

#### Creating a New Group

You can use the user manager to modify the default groups and to create new groups that define a combination of appropriate privileges.

The default Operator, Technician, Developer, and Administrator groups define a set of privilege settings for the new user to inherit. By default, the Operator group grants a user the privilege to execute, terminate, and abort sequences but does not grant the privilege to create or debug sequences.

Complete the following steps to create a new group.

1. Open the User Manager window.
2. Expand the Groups item to show the four default groups.
3. Right-click the Operator group and select Copy from the context menu.
4. Right-click the Groups item and select Paste from the context menu.
5. Rename the new group Senior Operator . The new group is identical to the Operator group except for the name.

#### Modifying Privileges

The TestStand
 User Manager stores user and group privileges as Boolean properties and organizes the
 privileges in the following categories:

- Operate —Privileges for executing sequences and terminating and
 aborting executions.
- Debug —Privileges for controlling execution flow, executing manual
 and interactive executions, and editing station global variables and run-time
 variables.
- Develop —Privileges for editing and saving sequence files, editing
 and saving workspace files, and using source code control.
- Configure —Privileges for editing process model files and
 configuring station options, users, adapters, application settings, and report, database
 logging, and model options.
- Custom —Custom privileges you define. Customize the
 NI_UserCustomPrivileges data type to add new privileges.

You can grant all privileges in a specific category for each user or group in the user
 manager, and you can grant specific privileges for each user or group. In addition, when you
 add a user as a member of a group, TestStand grants the user all the privileges of the
 group. TestStand grants a privilege to a user or group when the property value for the
 privilege is True or when the value of the GrantAll
 property in any enclosing parent privilege category is True. For example, a
 user has the privilege to terminate an execution when one of the following properties is
 True:

- <User>.Privileges.Operate.Terminate
- <User>.Privileges.Operate.GrantAll
- <User>.Privileges.GrantAll
- <Group>.Privileges.Operate.Terminate
- <Group>.Privileges.Operate.GrantAll
- <Group>.Privileges.GrantAll

Note

Privileges

Privileges

GrantAll

Privileges.GrantAll

GrantAll

True

GrantAll

False

Complete the following steps to modify the default privileges for the
 group you created in the previous section of this tutorial.

1. Expand the Senior Operator item and expand the
 Privileges property.
2. Expand the Debug item, which is a property that contains Boolean
 subproperties. Use the Value column ring control to change the
 SinglePass property under Debug to True .
3. Complete the following steps to add the user you created in the Adding a New User
 section of this tutorial to the Senior Operator group.
  1. Right-click the user you previously created under Users and select
 Properties from the context menu to launch the
 <User> Properties dialog box.
  2. Disable Operator in the Group Privileges control and enable
 Senior Operator instead.
  3. Click OK to close the User Properties dialog box.
4. Save the changes to the user manager.
5. Select File»Login to launch the Login dialog box. Select the user
 you previously created, enter the appropriate password, and click
 OK .
6. Select the Computer.seq window.
7. Select the Execute menu. Notice that the Single Pass option is
 now available, but the Run MainSequence option is disabled because the user you created
 does not have the privilege to execute sequences without a Model entry point.
8. Close all the windows in the sequence editor.
9. Select File»Login and select administrator 
 from the User Name ring control. Leave the Password field empty and click
 OK .

Refer to the Creating & Deleting Users Using API.seq example
 located in the <TestStand Public>\Examples\TestStand API\Creating &
 Deleting Users Using APIs directory for information about how to use the
 TestStand API to add and remove users programmatically.

Parent topic:

Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=ade-specific-issues-for-msi-based-installer-p.html language=enus -->
## TOPIC 00067: ADE-specific Issues for MSI-based Installer Patches

- bundle_id: `teststand`
- source_path: `ade-specific-issues-for-msi-based-installer-p.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/ade-specific-issues-for-msi-based-installer-p.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`

### ADE-specific Issues for MSI-based Installer
 Patches

- [Patching LabVIEW VIs](patching-labview-vis.html)
- [Patching LabWindows/CVI DLLs and Executables](patching-labwindows-cvi-dlls-and-executables.html)
- [Patching Microsoft .NET Assemblies](patching-microsoft.html)

Parent topic:

Patching Deployments

<!--NI_TOPIC bundle=teststand path=advanced-user-interface-development.html language=enus -->
## TOPIC 00068: Advanced User Interface Development

- bundle_id: `teststand`
- source_path: `advanced-user-interface-development.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/advanced-user-interface-development.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to develop advanced user interfaces.

### Advanced User Interface Development

Learn how to develop advanced user interfaces.

- [TestStand Utility Functions Library](teststand-utility-functions-library.html)
- [Managing Menus and Menu Items](managing-menus-and-menu-items.html)
- [Implementing Command-Line Arguments for a User Interface](implementing-command-line-arguments-for-a-use.html)
- [Authenticode Signatures for Microsoft Windows](authenticode-signatures-for-microsoft-windows.html)
- [Application Manifests](application-manifests.html)
- [Making Dialog Boxes Modal to TestStand](making-dialog-boxes-modal-to-teststand.html)

Parent topic:

Creating Custom User Interfaces

<!--NI_TOPIC bundle=teststand path=agilent-vee-step-types.html language=enus -->
## TOPIC 00069: Agilent VEE Step Types

- bundle_id: `teststand`
- source_path: `agilent-vee-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/agilent-vee-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example uses ActiveX to call Agilent VEE code from TestStand using custom step types, which you can use to execute the user functions of VEE user libraries. Example File Location <TestStand Public>\Examples\Custom Step Types\Agilent VEE Step Types\Agilent VEE Computer Motherboard Test.s

### Agilent VEE Step Types

#### Purpose

This example uses ActiveX to call Agilent VEE code from TestStand using custom step types, which you can use to execute the user functions of VEE user libraries.

#### Example File
 Location

<TestStand
 Public>\Examples\Custom Step Types\Agilent VEE Step Types\Agilent
 VEE Computer Motherboard Test.seq

#### Highlighted Features

Custom step types

#### Major API

N/A

#### Prerequisites

VEE Evaluation, Development, or Run-Time Environment version 6.0 or later.

Note

#### How to Use This Example

The example sequence file, Agilent VEE Computer Motherboard Test.seq, contains a SequenceFileLoad callback that TestStand automatically executes when you open the sequence file and that performs the following necessary actions:

- Copies the TestStand example file VEE_StepType.dll , which implements the step type functionality, from the <TestStand Public>\Examples\Custom Step Types\Agilent VEE Step Types directory to the <TestStand Public>\Components\StepTypes\Agilent VEE directory and registers the DLL. Note VEE_StepType.dll was created using Microsoft Visual Basic. The example directory includes the VEE_StepType.vbp Visual Basic project file, which you can use to recompile VEE_StepType.dll.
- Copies the <TestStand Public>\Examples\Custom Step Types\Agilent VEE Step Types\compMotherBoard.bmp file to the default Bitmaps subdirectory of the VEE installation directory. The SimulationDialog VEE user function displays the bitmap on its view panel. When using a bitmap on a VEE view panel, you can reference the bitmap using an absolute path or you can place the bitmap in the Bitmaps subdirectory of the VEE installation directory.

When you open <TestStand Public>\Examples\Custom Step Types\Agilent VEE Step Types\Agilent VEE Computer Motherboard Test.seq in the TestStand Sequence Editor, the VEE step types appear in the VEE group on the Insertion Palette. You can make the VEE step types available for any sequence file by copying the VEE step types from Computer.seq in the Types window to a type palette, such as MyTypes.ini.

When you insert a VEE step type into a sequence, you must configure the step by clicking the Specify VEE Module button on the Step Settings pane to launch the Edit VEE Module dialog box. For the VEE Library to Load control, specify a valid VEE library. The step automatically populates the VEE Function ring control with user functions the VEE user library exports. When you select an exported function, the step automatically populates the input and output arguments of the function. The VEE step types currently support the following data types and data shapes for arguments of VEE user functions:

- Scalar:
  - Signed 32-bit integer
  - 64-bit real number (double)
  - String
- 1D-Array:
  - Signed 32-bit integer
  - 64-bit real number (double)
  - String

You can select each input and output argument from the Argument control of the Input section and the Output section, respectively, and set a corresponding TestStand property path. The step uses the value of the property as input for input arguments or receives the output value for output arguments.

The VEE step types also support debugging. You can step into a VEE user function and use the VEE debug functionality to debug the user function.

This example includes VB_VEE_Action, VB_VEE_NumericLimitTest, VB_VEE_PassFailTest, and VB_VEE_StringValueTest step types. The VB_VEE_NumericLimitTest, VB_VEE_PassFailTest, and VB_VEE_StringValueTest step types combine the functionality of the VB_VEE_Action step with the built-in Numeric Limit Test, Pass Fail Test, and String Value Test step types, respectively, to call VEE functions in addition to the functionality of the built-in steps. For example, the VB_VEE_NumericLimitTest step returns a number from a VEE user function and compares the number to numeric limits.

Parent topic:

Examples for Custom Step Types

Related concepts:

- TestStand Directory Structure
- Custom Step Types

<!--NI_TOPIC bundle=teststand path=all-development-environments.html language=enus -->
## TOPIC 00070: All Development Environments

- bundle_id: `teststand`
- source_path: `all-development-environments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/all-development-environments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any component that requires direct access to Session Manager can obtain a reference to Session Manager by creating a session manager object. Because Session Manager is a single instance, in-process ActiveX server, each component in the process receives a reference to the same session manager object.

### All Development Environments

Any component that requires direct access to Session Manager can obtain a reference to Session Manager by creating a session manager object. Because Session Manager is a single instance, in-process ActiveX server, each component in the process receives a reference to the same session manager object. After you use Session Manager to obtain a session or perform a query, you can release the session and then recreate it later when you need it again.

The base name of the Session Manager server is SessionMgr. For ActiveX environments in which you cannot browse for a registered server, you can import the type information you need to access the Session Manager server from NISessionServer.dll.

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=analyze-in-tse.html language=enus -->
## TOPIC 00071: Analyzing a Sequence File or Workspace File in the TestStand Sequence Editor

- bundle_id: `teststand`
- source_path: `analyze-in-tse.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/analyze-in-tse.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use the TestStand Sequence Analyzer to analyze a sequence file or workspace file. In the TestStand Sequence Editor, click the Current Sequence Analyzer Project button on the Sequence Analyzer toolbar or select Debug»Sequence Analyzer»Current Sequence Analyzer Project

### Analyzing a Sequence File or Workspace File in
 the TestStand Sequence Editor

Complete the following steps to use the
 TestStand Sequence Analyzer to analyze a sequence file or workspace file.

1. In the TestStand Sequence Editor, click the Current Sequence
 Analyzer Project button on the Sequence Analyzer toolbar or
 select Debug»Sequence Analyzer»Current Sequence Analyzer
 Project to open the Current Sequence Analyzer Project window and
 the most recently opened analyzer project file. 
 Note The first time you launch Current Sequence Analyzer Project window, the
 sequence editor creates a default project, named
 MyAnalyzerProject.tsaproj, which specifies the rules
 and related settings to use during the analysis. You can create, modify, and
 save project files to customize the set of rules, rule configuration
 settings, and set of files to use during analysis.
2. On the Rules pane, enable and configure the rules you want to use to analyze
 the file. 
 Note The sequence
 analyzer enables most of the built-in rules by default. You cannot disable
 or delete the built-in rules in the Analysis Errors category.
3. Open and activate the sequence file or workspace file you want to analyze.
 Click the Analyze <Sequence
 Filename> button on the Sequence Analyzer toolbar
 to analyze a sequence file. Right-click the workspace file and select
 Analyze Workspace from the context menu to analyze a
 workspace file. 
 Note By default, the sequence analyzer enables the Analyze File Before
 Executing option in the Sequence Analyzer Options dialog box. In the
 sequence editor, click the Toggle Analyze File Before
 Executing button on the Sequence Analyzer toolbar or select
 Debug»Sequence Analyzer»Toggle Analyze File Before
 Executing to enable or disable this option. When you enable
 this option, the sequence analyzer uses the rules and settings in the
 current sequence analyzer project to analyze the active sequence file when
 you initiate an execution. Enabling this option can help you find errors
 early during development.
4. The status bar at the bottom of the Analysis Results pane indicates the
 progress of the analysis. You can click the Stop Analysis
 button on the Sequence Analyzer toolbar or select Debug»Sequence
 Analyzer»Stop Analysis at any time during analysis. The sequence
 analyzer finishes analyzing the current object before stopping the analysis and
 shows the current list of messages on the Analysis Results pane.
5. (Optional) When you complete an analysis, you can save an XML report file to
 use in an external viewer for comparison. In the sequence editor, click
 Generate Analysis Results on the Analysis Results
 pane to save the messages for the most recent analysis in an XML report file to
 use in an external viewer. The XML file uses the AnalyzerReportViewer.xsl style
 sheet, located in the
 <TestStand>\Components\Stylesheets\Analyzer
 directory. When you generate a report file, the sequence analyzer provides a
 snapshot of the most recent analysis, including a list of the analyzed files, a
 list of the rules and settings used during the analysis, and a list of all the
 generated messages. 
 Note Use the XML
 Packaging Utility to package the files necessary to view the XML report on a
 computer that does not have TestStand installed.
6. Use the Show and Group By
 drop-down lists to control how to view the generated messages on the Analysis
 Results pane. Right-click each message and select an option from the Analyzer
 Messages tab context menu to resolve the message. 
 For each active message, you can perform the following actions:Go to the location of the object in the TestStand file that caused the
 message and resolve the issue.
 Ignore the issue for subsequent analysis and remove it from the Active
 Messages view. Select this option only when you are certain the issue
 will not cause a run-time error.
 Mark the message as fixed and remove it from the Active Messages
 view.
 Disable or configure the corresponding rule on the Rules pane of the
 sequence analyzer.Note You can save the project file at any time when you are resolving
 messages.

You can repeat these steps to cycle through
 the analysis, report generation, and message resolution stages until you attain
 acceptable results.

Parent topic:

Analyzing Files

Related concepts:

- Search Directories
- TestStand Sequence Analyzer Rules Descriptions
- XML Packaging Utility

Related tasks:

- Creating Custom Rules in the TestStand Sequence Analyzer

Related information:

- Analysis Results Pane

<!--NI_TOPIC bundle=teststand path=analyze-mult-files-tsa.html language=enus -->
## TOPIC 00072: Analyzing Multiple TestStand Files Using the TestStand Sequence Analyzer

- bundle_id: `teststand`
- source_path: `analyze-mult-files-tsa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/analyze-mult-files-tsa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use the TestStand Sequence Analyzer to analyze multiple TestStand files. In the TestStand Sequence Editor, click the Current Sequence Analyzer Project button on the Sequence Analyzer toolbar or select Debug»Sequence Analyzer»Current Sequence Analyzer Project to open t

### Analyzing Multiple TestStand Files Using the
 TestStand Sequence Analyzer

Complete the following steps to use the
 TestStand Sequence Analyzer to analyze multiple TestStand files.

1. In the TestStand Sequence Editor, click the Current Sequence
 Analyzer Project button on the Sequence Analyzer toolbar or
 select Debug»Sequence Analyzer»Current Sequence Analyzer
 Project to open the Current Sequence Analyzer Project window and
 the most recently opened analyzer project file. 
 Note The first time you launch the Current Sequence Analyzer Project window,
 the sequence editor creates a default project, named
 MyAnalyzerProject.tsaproj, which specifies the rules
 and related settings to use during the analysis. You can create, modify, and
 save project files to customize the set of rules, rule configuration
 settings, and set of files to use during analysis.
 Note If you want to use the stand-alone sequence analyzer application, select
 Start»National Instruments»TestStand»Tools»TestStand Sequence
 Analyzer to launch the application. Click the New
 Sequence Analyzer Project button on the Sequence Analyzer
 toolbar or select File»New Sequence Analyzer Project
 to create a new project.
2. On the Files pane or tab, select the files or directories you want to analyze.
 When you select a workspace file, the sequence analyzer automatically analyzes
 all the sequence files in that workspace file.
3. On the Rules pane or tab, enable and configure the rules you want to use in the
 current project. 
 Note You cannot
 disable or delete built-in rules in the Analysis Errors category.
4. On the Options pane or tab, enable or disable the analyzer project options you
 need.
5. Click the Analyze <project
 filename> button on the Sequence Analyzer toolbar
 or select Debug»Sequence Analyzer»Analyze <project
 filename>. You can also select
 Project»Analyze in the sequence analyzer
 application. 
 Note Use the status bar at the bottom of the Analysis Results pane in the
 sequence editor and at the bottom of the Messages tab in the sequence
 analyzer application to view the progress of the analysis.
 Note At any time during analysis, you can click the Stop
 Analysis button on the Sequence Analyzer toolbar or select
 Debug»Sequence Analyzer»Stop Analysis in the
 sequence editor or select Project»Stop Analysis in
 the sequence analyzer application. The sequence analyzer finishes analyzing
 the current object before stopping the analysis and shows the current list
 of messages on the Analysis Results pane in the sequence editor and on the
 Messages tab in the sequence analyzer application.
6. (Optional) When you complete an analysis, you can save an XML report file to
 use in an external viewer for comparison. In the sequence editor, click
 Generate Analysis Results on the Analysis Results
 pane or select Project»Generate Analysis Report in the
 sequence analyzer to save the messages for the most recent analysis in an XML
 report file to use in an external viewer. The XML file uses the
 AnalyzerReportViewer.xsl style sheet, located in the
 <TestStand>\Components\Stylesheets\Analyzer
 directory. When you generate a report file, the sequence analyzer provides a
 snapshot of the most recent analysis, including a list of the analyzed files, a
 list of the rules and settings used during the analysis, and a list of all the
 generated messages. 
 Note Use the XML
 Packaging Utility to package the files necessary to view the XML report on a
 computer that does not have TestStand installed.
7. Use the Show and Group By drop-down lists to filter the generated messages on
 the Analysis Results pane in the sequence editor and on the Messages tab in the
 sequence analyzer application. Right-click each message and select an option
 from the Analyzer Messages tab context menu in the sequence editor or the
 Messages tab context menu in the sequence analyzer application to resolve the
 message. 
 For each active message, you can perform the following actions: Go to the location of the object in the TestStand file that caused the
 message and resolve the issue.
 Ignore the issue for subsequent analysis and remove it from the Active
 Messages view. Select this option only when you are certain the issue
 will not cause a run-time error.
 Mark the message as fixed and remove it from the Active Messages
 view.
 Disable or configure the corresponding rule on the Rules pane of the
 sequence analyzer.Note You can save the project file at any time when you are resolving
 messages.

You can repeat these steps to cycle through
 the analysis, report generation, and message resolution stages until you attain
 acceptable results.

Parent topic:

Analyzing Files

Related concepts:

- Search Directories
- TestStand Sequence Analyzer Rules Descriptions
- TestStand Sequence Analyzer Application

Related tasks:

- Creating Custom Rules in the TestStand Sequence Analyzer

Related information:

- Analysis Results Pane
- Current Sequence Analyzer Project Window

<!--NI_TOPIC bundle=teststand path=analyzing-files-tsa.html language=enus -->
## TOPIC 00073: Analyzing Files

- bundle_id: `teststand`
- source_path: `analyzing-files-tsa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/analyzing-files-tsa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Sequence Analyzer completes the tasks described in the following figure to analyze workspace files, sequence files, directories, type palette files, station globals files, template files, and users files. The analyzer engine begins analyzing the workspace file, sequence file, directory

### Analyzing Files

The TestStand Sequence Analyzer completes the tasks described in the following figure to
 analyze workspace files, sequence files, directories, type palette files, station
 globals files, template files, and users files.

[IMAGE alt='image' src='GUID-EFA917F4-E584-4F5C-B9B6-E6B32DF5534D-a5.png']

1. The analyzer engine begins analyzing the workspace file, sequence file, directory,
 type palette file, station globals file, template file, or users file.
2. The analyzer engine checks for analysis modules that apply to the analyzed file. For
 example, if an analysis module applies to a variable, the analyzer invokes the code
 module
 the analysis module specifies for each variable in the analyzed file. An analysis
 module can apply to more than one element of a file, or you can apply more than one
 module to one element of a file.
3. Each code module an analysis module calls reports any broken rules to the analyzer
 engine.
4. The analyzer engine filters the list of reported rules through the sequence analyzer
 project, which specifies whether some rules are disabled, the severity of each
 enabled rule, and the description to display for each enabled rule.
5. The analyzer engine outputs the severity, description, and location for each
 triggered, enabled rule to the Analysis Results pane in the sequence editor or the
 Messages tab in the stand-alone sequence analyzer application.

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Code Modules
- Creating Analysis Modules for Custom Rules
- TestStand Sequence Analyzer Rules Descriptions

Related tasks:

- Creating Custom Rules in the TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand path=analyzing-the-test-system.html language=enus -->
## TOPIC 00074: Analyzing the Test System

- bundle_id: `teststand`
- source_path: `analyzing-the-test-system.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/analyzing-the-test-system.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the System Source tab of the TestStand Deployment Utility to specify a workspace or directory that includes the components you want to deploy. The deployment utility analyzes the workspace file or directory by opening all the source files and searching for dependencies to generate a complete lis

### Analyzing the Test System

Use the System Source tab of the TestStand Deployment Utility to specify a workspace or directory that includes the components you want to deploy. The deployment utility analyzes the workspace file or directory by opening all the source files and searching for dependencies to generate a complete list of source files and dependencies to include in the deployment. For example, the deployment utility opens a workspace file and adds all the TestStand project files to the deployment, then opens each project and adds all the files in the projects to the deployment. The deployment utility continues this process until it identifies and adds all the dependencies of the test system.

#### Troubleshooting Deployment Analysis
 Errors

The deployment utility uses a log to report errors that might
 prevent test systems from functioning correctly, such as missing code modules.
 Resolve the errors and warnings on the development computer before you create or
 install a deployment because locating and resolving errors and warnings on the test
 station computer might require significant time and effort.

You can prevent
 many deployment issues by ensuring the test system is up-to-date and error-free by
 preparing the test system for deployment and by using the TestStand Sequence
 Analyzer to identify common problems with test sequences, such as steps that are
 missing code modules or code modules that TestStand cannot load.

If the
 deployment utility reports missing files, search the development computer to confirm
 the files exist in the correct directories. If the files exist on the computer but
 TestStand cannot find the files, use the Edit Search Directories dialog box to
 update the search directories, then exit and relaunch the deployment utility. NI
 recommends using paths relative to the workspace for TestStand projects and sequence
 files and paths relative to the calling sequence for all code modules to reduce the
 possibility of loading incorrect code modules.

If the deployment utility
 reports missing dependencies for code modules, you might not have installed the
 driver software the test system requires. Launch Measurement & Automation
 Explorer and expand My System»Software to review the NI
 software installed on the computer. Use the standard Microsoft Windows Control Panel
 facility for adding and removing programs to review the third-party drivers or other
 software installed on the computer.

In the following situations, the
 deployment utility reports that a sequence uses a file but the deployable image
 folder might not contain the file:

- The sequence file dynamically references the file—You must manually add
 dynamically referenced files to the deployment.
- The deployment utility filters files to prevent deployments from including
 operating system files—You can change the filtering settings using the
 Filter.ini file located in the <TestStand
 Application Data>\Cfg directory.

Parent topic:

Creating Deployments

Related concepts:

- Using a TestStand Workspace File to Create a Deployment
- Using a Directory to Create a Deployment
- Identifying Components to Deploy
- Preparing Source Components for Deployment
- Search Directories
- Manually Adding or Removing Files to or from Deployments
- Filtering and Excluding Files
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=anycpu-assemblies-in-32-bit-teststand-and-64.html language=enus -->
## TOPIC 00075: AnyCPU Assemblies in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `anycpu-assemblies-in-32-bit-teststand-and-64.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/anycpu-assemblies-in-32-bit-teststand-and-64.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: AnyCPU .NET assemblies are bitness independent. You can load the same version of the assembly in 32-bit TestStand and in 64-bit TestStand. When you migrate from 32-bit TestStand to 64-bit TestStand, you do not need to modify a sequence file that relies only on AnyCPU .NET assemblies that reside in l

### AnyCPU Assemblies in 32-bit TestStand and 64-bit TestStand

AnyCPU .NET assemblies are bitness independent. You can load the same version of the assembly in 32-bit TestStand and in 64-bit TestStand. When you migrate from 32-bit TestStand to 64-bit TestStand, you do not need to modify a sequence file that relies only on AnyCPU .NET assemblies that reside in locations 32-bit TestStand and 64-bit TestStand share.

You can migrate AnyCPU assemblies located in the <TestStand Public> directory or other non-shared search directory using one of the following techniques:

- Copy the assembly to a shared location and reference the assembly from the new location before you migrate from 32-bit TestStand to 64-bit TestStand.
- Copy the assemblies to the equivalent 64-bit location to use in 64-bit TestStand.

NI recommends placing AnyCPU assemblies in a location 32-bit TestStand and 64-bit TestStand share
 so that 32-bit TestStand and 64-bit TestStand can share a single copy of each
 assembly. NI also recommends replacing existing 32-bit (x86) .NET assemblies with
 AnyCPU versions in-place before migrating from 32-bit TestStand to 64-bit
 TestStand.

Parent topic:

.NET Code Module Support for 64-bit TestStand

Related concepts:

- TestStand Directory Structure
- Using TestStand Search Directories to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=api-containment.html language=enus -->
## TOPIC 00076: API Containment

- bundle_id: `teststand`
- source_path: `api-containment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/api-containment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the TestStand API, many objects contain other types of objects. For example, a SequenceFile object contains Sequence objects, and Sequence objects contain Step objects. The following figure shows the containment relationship between objects in the TestStand API.

### API Containment

In the TestStand API, many objects contain other types of objects. For example, a SequenceFile object contains Sequence objects, and Sequence objects contain Step objects. The following figure shows the containment relationship between objects in the TestStand API.

[IMAGE alt='image' src='GUID-E8ED25B8-72CB-47DC-A5EC-3F58AC43B7CB-a5.png']

Parent topic:

Object Relationships

<!--NI_TOPIC bundle=teststand path=api-inheritance.html language=enus -->
## TOPIC 00077: API Inheritance

- bundle_id: `teststand`
- source_path: `api-inheritance.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/api-inheritance.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Almost all TestStand API classes inherit from the PropertyObject class, which means you can use PropertyObject methods and properties on objects of other classes. For example, you can use the PropertyObject.Name property to obtain the name of a SequenceFile object, Sequence object, or Step object. Y

### API Inheritance

Almost all TestStand API classes inherit from the PropertyObject class, which means you can
 use PropertyObject methods and properties on objects of other classes. For
 example, you can use the PropertyObject.Name property to obtain the name of a SequenceFile
 object, Sequence object, or Step object. You can also create subproperties using the
 PropertyObject methods. You can programmatically create a new subproperty
 of a step using the PropertyObject methods PropertyObject.SetValNumber,
 PropertyObject.SetValBoolean, or PropertyObject.SetValString with the
 PropOption_InsertIfMissing option.

Note

AsPropertyObject

PropertyObject

PropertyObject

PropertyObject

AsPropertyObject

Parent topic:

Object Relationships

<!--NI_TOPIC bundle=teststand path=api-overview.html language=enus -->
## TOPIC 00078: TestStand API Overview

- bundle_id: `teststand`
- source_path: `api-overview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/api-overview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn basic information about the TestStand ActiveX Automation server, API concepts, and writing applications with TestStand. Using TestStand API Objects In the TestStand API, many objects reference other types of objects. You can obtain an object of one class from an object of another class by call

### TestStand API Overview

Learn basic information about the TestStand ActiveX Automation server, API concepts, and writing
 applications with TestStand.

#### Using TestStand API Objects

In the TestStand API, many objects reference other types of objects. You can obtain an object of one class from an object of another class by calling a method or accessing a property. For example, you can obtain the Engine, Thread, Execution, and Report objects from the SequenceContext object. In another example, a UIMessage object references an Execution object, and an Execution object references a SequenceFile object.

Related concepts:

- Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=api-updates-for-64-bit-teststand.html language=enus -->
## TOPIC 00079: API Updates for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `api-updates-for-64-bit-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/api-updates-for-64-bit-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some TestStand 2013 or earlier API methods and properties represents pointers or pointer-sized values as 32-bit integral data types, usually long, which does not work for 64-bit applications. The following table lists obsolete properties and methods and the corresponding TestStand properties and met

### API Updates for 64-bit TestStand

Some TestStand 2013 or earlier API methods and properties represents pointers or pointer-sized values as 32-bit integral data types, usually long, which does not work for 64-bit applications. The following table lists obsolete properties and methods and the corresponding TestStand properties and methods that support 32-bit applications and 64-bit applications.

| Class | Obsolete (32-bit only) Property or Method | 32-bit TestStand and 64-bit TestStand Property or Method |
| --- | --- | --- |
| Engine | LargeImageList | LargeImageListEx |
| Engine | RegisterUIMessageCallback | RegisterUIMessageCallbackEx |
| Engine | SmallImageList | SmallImageListEx |
| Station Options | DefaultCPUAffinityForThreads | DefaultCPUAffinityForThreadsEx |
| InstrSession | CloseFunction | CloseFunctionEx |
| InstrSession | GetHandle | GetHandleEx |

| Class | Obsolete (32-bit only) Property or Method | 32-bit TestStand and 64-bit TestStand Property or Method |
| --- | --- | --- |
| Engine | LargeImageList | LargeImageListEx |
| Engine | RegisterUIMessageCallback | RegisterUIMessageCallbackEx |
| Engine | SmallImageList | SmallImageListEx |
| Station Options | DefaultCPUAffinityForThreads | DefaultCPUAffinityForThreadsEx |
| InstrSession | CloseFunction | CloseFunctionEx |
| InstrSession | GetHandle | GetHandleEx |

32-bit TestStand supports the obsolete properties and methods for compatibility, but NI
 recommends using the obsolete API only when you migrate existing 32-bit TestStand
 systems to 32-bit TestStand. For TestStand 2014 or later applications and for
 updates to existing systems, use the TestStand API regardless of current
 requirements for 64-bit support. The obsolete properties and methods return errors
 when invoked in 64-bit TestStand.

In addition, the following new methods support attaching user-defined pointer-sized values to sessions and function similarly to the existing InstrSession.AttachLong and InstrSession.GetLong methods:

- InstrSession.AttachLongPtr
- InstrSession.GetLongPtr

Continue to use the InstrSession.AttachLong and InstrSession.GetLong methods with values that are 32-bits regardless of architecture.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=application-manager.html language=enus -->
## TOPIC 00080: Application Manager

- bundle_id: `teststand`
- source_path: `application-manager.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/application-manager.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Application Manager control performs the following basic operations, which are necessary to use the TestStand Engine in an application: Processes command-line arguments. Maintains an application configuration file. Initializes and shuts down the TestStand Engine. Loads type palette files at init

### Application Manager

The Application Manager control performs the following basic operations, which are necessary to use the TestStand Engine in an application:

- Processes command-line arguments.
- Maintains an application configuration file.
- Initializes and shuts down the TestStand Engine.
- Loads type palette files at initialization.
- Logs users in and out.
- Loads and unloads sequence files.
- Launches executions.
- Tracks existing sequence files and executions.

An application must have a single Application Manager control that exists for the duration of the application.

Parent topic:

Manager Controls

<!--NI_TOPIC bundle=teststand path=application-manifests.html language=enus -->
## TOPIC 00081: Application Manifests

- bundle_id: `teststand`
- source_path: `application-manifests.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/application-manifests.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When an application launches on Microsoft Windows 10/8.1/7, the User Account Control (UAC) security component determines whether to grant the application administrative privileges. A user that logs into Windows as a standard user can write only to specific locations on disk and in the registry. Stan

### Application Manifests

When an application launches on Microsoft Windows 10/8.1/7, the User Account Control (UAC) security component determines whether to grant the application administrative privileges. A user that logs into Windows as a standard user can write only to specific locations on disk and in the registry. Standard user is the default login.

Microsoft recommends that applications run without requiring administrator privileges. If you design applications that do not attempt to access protected areas of the operating system, all users can run the application as intended without requiring administrator privileges. You can also include manifests to specify the execution level the application requires.

When an application does not specify an execution level in a manifest, the UAC launches the application with the standard or administrator privileges of the user. With standard privileges, the system uses virtualization to redirect any read and write operations for system files and registry keys to a per-user location instead of the actual system copy of the file or registry key. Do not create applications that rely on virtualization to perform these types of administrative operations.

The default TestStand User Interface application binary files include manifests that instruct the UAC to execute the application without virtualization and without requiring administrative privileges. With LabVIEW, you can specify a custom manifest for built applications. With LabWindows/CVI, you can specify a manifest for built applications. When you build the application, refer to the documentation for the application development environment you used for more information about how to include a manifest.

Parent topic:

Advanced User Interface Development

<!--NI_TOPIC bundle=teststand path=assigning-values-to-object-references.html language=enus -->
## TOPIC 00082: Assigning Values to Object References

- bundle_id: `teststand`
- source_path: `assigning-values-to-object-references.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/assigning-values-to-object-references.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Object reference properties can contain references to LabVIEW, .NET, ActiveX/COM, and other objects. When a property is an object reference, you can use the Release Object button, which displays only when the value of the property is non-zero, in the Value column on the Variables pane to release the

### Assigning Values to Object References

Object reference properties can contain references to LabVIEW, .NET, ActiveX/COM, and other objects. When a property is an object reference, you can use the Release Object button, which displays only when the value of the property is non-zero, in the Value column on the Variables pane to release the reference.

You can set the reference value by using an expression, using the TestStand API, or configuring a call to a code module with a parameter or return value that returns such an object.

When you have two object reference properties and use the equality operator in an expression, TestStand performs an equality comparison on the IUnknown pointers for ActiveX objects and the pointer values for .NET objects.

#### Releasing References to
 Objects

When you assign an object reference value to an object reference
 property, TestStand maintains a reference to the object for as long as the property
 exists, or until the value changes. TestStand automatically releases the reference
 to the object when the property loses scope. For example, when a sequence local
 variable contains a reference to an object, TestStand releases the reference when
 the call to the sequence completes.

You can also release the reference to the
 object by assigning the property a new value or the constant
 Nothing. Assign the constant Nothing, rather
 than the value 0, to clear the reference. When you assign
 0 to an object reference variable, TestStand creates a numeric
 variable with a value of 0 and assigns a reference to that numeric
 variable to the object reference variable.

When you release all references to
 an object, the availability of the object after release changes depending on the
 type of object, as shown in the following table.

| Type of Object | Object Availability |
| --- | --- |
| .NET | The object is available for .NET garbage collection. |
| ActiveX/COM | The object is destroyed. |

#### Sharing .NET Objects Between LabVIEW and
 TestStand

Note

Parent topic:

Modifying Type Instances, Values, and Type Definitions

<!--NI_TOPIC bundle=teststand path=atlas-step-type.html language=enus -->
## TOPIC 00083: ATLAS Step Type

- bundle_id: `teststand`
- source_path: `atlas-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/atlas-step-type.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates a custom step type for calling an Abbreviated Test Language for All Systems (ATLAS) test program set (TPS), which is created in the PAWS Developer Studio. The ATLAS custom step type integrates with the PAWS Run-Time System (RTS) to execute TPS files (.PAWS). These e

### ATLAS Step Type

#### Purpose

This example demonstrates a custom step type for calling an Abbreviated Test Language for All Systems (ATLAS) test program set (TPS), which is created in the PAWS Developer Studio. The ATLAS custom step type integrates with the PAWS Run-Time System (RTS) to execute TPS files (.PAWS). These examples require the TYX PAWS RTS Server to run the provided test program sets.

The ATLAS custom step type example includes the following example sequence files:

- A parameter passing example that demonstrates passing parameters between TestStand and a TPS.
- A manual intervention example that demonstrates support for handling a request for manual intervention by the PAWS RTS Server.

#### Example File
 Location

<TestStand
 Public>\Examples\Custom Step Types\ATLAS Step Types\Parameter
 Passing Example.seq

<TestStand
 Public>\Examples\Custom Step Types\ATLAS Step Types\Manual
 Intervention Example.seq

#### Highlighted Features

Custom step types

#### Major API

N/A

#### Prerequisites

TYX PAWS RTS 1.22 or later

#### How to Use This Example

The example sequence files contain a SequenceFileLoad callback that TestStand automatically executes when you open either sequence file. The SequenceFileLoad callback copies the ATLAS_StepType.dll file from the <TestStand Public>\Examples\Custom Step Types\ATLAS Step Types directory to the <TestStand Public>\Components\StepTypes\ATLAS directory and registers the DLL. The ATLAS custom step type calls functions within ATLAS_StepType.dll to configure and handle interactions between TestStand and PAWS.

You must install the PAWS RTS with the TPS Server before you can build the accompanying project. You must contact TYX Corporation for more information about obtaining the PAWS RTS.

The project assumes you have installed the PAWS RTS in the default location of C:\usr. If you installed the PAWS RTS in a different location, modify the path in the following lines of code, located in <TestStand Public>\Examples\Custom Step Types\ATLAS Step Types\ATLAS\StdAfx.h, to reflect the new location:

- Change the line #import "C:\usr\tyx\com\rtsax.dll" raw_interfaces_only to #import "<New Location>\tyx\com\rtsax.dll" raw_interfaces_only
- Change the line #import "C:\usr\tyx\com\ComUtil.dll" raw_interfaces_only to #import "<New Location>\tyx\com\ComUtil.dll" raw_interfaces_only

When you set the paths correctly, you can build the ATLAS custom step type project with Microsoft Visual C++ 6.0.

The ATLAS custom step type creates the PAWS RTS and executes a TPS through the PAWS TPS COM Server, and communicates with the TPS server by calling methods within the NI ATLAS Step Type ActiveX server located in ATLAS_StepType.dll. The server contains the IExecuteTPS class, which includes the following methods:

- Edit Step —Sets up a TPS to call and the parameter to pass to the TPS.
- Execute TPS —Creates the PAWS RTS and executes a TPS.

The ATLAS custom step type supports the use of the TestStand numeric, Boolean, and string types. You can use parameters of these types to pass data between TestStand and the TPS server. Data is exchanged through COM boundaries between the ATLAS custom step type in TestStand, the NI ATLAS Step Type server, and the TPS server, which monitors the PAWS RTS server, as shown in the following figure.

[IMAGE alt='image' src='GUID-5423039B-9AF2-4288-BD0C-7B6381A66DBF-a5.svg']

#### Parameter Passing Example

When you open the ParameterPassingExample.seq example sequence file, the SequenceFileLoad callback copies the required files to the appropriate directories. When TestStand executes the Main step group of the MainSequence, TestStand launches a dialog box that requests a numeric value to pass to the sample TPS. TestStand passes the numeric value, along with various other parameters, the TPS server. The sample TPS modifies the numeric value and parameters and shows the modified values when execution returns to TestStand.

#### Manual Intervention Example

When you open the ManualInterventionExample.seq example sequence file, the SequenceFileLoad callback copies the required files to the appropriate directories. When TestStand executes the Main step group of the MainSequence, the ATLAS step calls a TPS that simulates and tests several devices. When the TPS simulates the DMM, TestStand launches a dialog box that prompts for the simulated voltage. If you enter a voltage that is within the acceptable range of 21 to 23 V, the test passes. Otherwise, the test fails.

During execution, the TPS server also simulates a manual intervention request, in which you can pause the execution while the TPS server resolves the condition that caused the request. The simulated manual intervention launches a dialog box on the same computer on which TestStand is running to inform you that manual intervention has been requested. Click Continue in the dialog box to resume TPS execution from TestStand.

#### Using the ATLAS Step in New Sequence Files

You can call an ATLAS TPS using step instances of the ATLAS custom step type. The example sequence files contain ATLAS steps preconfigured to call a sample TPS. You can execute these sequences without making changes. You can also use the ATLAS custom step type in your own sequence files to call an ATLAS TPS. You can insert an ATLAS step into a sequence in one of the following ways:

- Copy an ATLAS step from one of the example sequence files to the new sequence.
- Copy the ATLAS custom step type from one of the example sequence files to the new sequence.
- Add the ATLAS custom step type to a type palette file and use the Insert Step submenu in the Steps Pane context menu to create an instance of an ATLAS step.

Before you can execute a sequence that contains an ATLAS step, you must configure the step to call the appropriate TPS and pass any desired parameters. Click the Edit ATLAS Step button on the Step Settings pane to launch the Edit ATLAS Call dialog box, in which you can specify the TPS the step executes and the parameters passed between TestStand and the TPS.

You can then execute the sequence that contains the steps. The ATLAS custom step type fails on an ATLAS step if any faults are reported when the TPS executes. The ATLAS custom step type also propagates and reports any errors the TPS server encounters to TestStand. If the TPS server encounters no errors or faults, the step passes.

When TestStand first executes an ATLAS step, the ATLAS custom step type loads an instance of the RTS, or attaches to an existing RTS if one already exists. TestStand stores a reference to this instance as a temporary global variable in the TestStand Engine. Future executions of the ATLAS custom step type use the same reference for TPS executions. The engine releases the reference when it shuts down.

Note

#### Limitations

The following are known limitations of the ATLAS custom step type:

- The step type does not support passing TestStand arrays, containers, or object references as parameters.
- You can execute only one ATLAS step at a time for each local or remote computer. The ATLAS steps are locked globally with respect to the name of the local or remote computer. A sequence might contain multiple ATLAS steps that pertain to the same local or remote computer, but the step executions are sequential. You can execute ATLAS steps that pertain to different computers simultaneously.
- The TestStand Deployment Utility does not automatically copy and register ActiveX servers. You must add ATLAS_StepType.dll to the list of deployment files to deploy the ATLAS custom step type. When you deploy the step type, you must register the NI ATLAS Step Type ActiveX server. Refer to the SequenceFileLoad callback sequence in either ATLAS example sequence file for an example of registering an ActiveX server.

#### Error Codes and Descriptions

You might receive some error codes when using this example.

Parent topic:

Examples for Custom Step Types

Related concepts:

- TestStand Directory Structure
- Custom Step Types
- Type Palette Files
- Edit ATLAS Call Dialog Box
- Deploying TestStand Systems
- Error Codes and Descriptions

<!--NI_TOPIC bundle=teststand path=atml-report-style-sheets.html language=enus -->
## TOPIC 00084: ATML Report Style Sheets

- bundle_id: `teststand`
- source_path: `atml-report-style-sheets.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/atml-report-style-sheets.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Apply a style sheet to an ATML report to specify how a web browser or external viewer application displays the ATML content. Use the Style Sheet control on the Contents tab of the Report Options dialog box to select the style sheet to apply to an ATML report. You can select a different style sheet d

### ATML Report Style Sheets

Apply a style sheet to an ATML report to specify how a web browser or external viewer application displays the ATML content. Use the Style Sheet control on the Contents tab of the Report Options dialog box to select the style sheet to apply to an ATML report. You can select a different style sheet depending on the version of the ATML Test Results and Session Information schema against which the report validates.

#### ATML Test Results 6.01 Reports Style Sheets

TestStand provides the following style sheets, located in the <TestStand>\Components\Models\TestStandModels\ATML\StyleSheets directory, for generating an ATML Test Results 6.01 report. You can customize the style sheets directly.

- TR6_Expand.xsl —Displays reports similar to TR6_report.xsl , with expandable and collapsible sections for each step or for the entire report.
- TR6_Horizontal.xsl —Displays reports in a horizontal, tabular, indented format with data for each step in one or more rows.
- TR6_report.xsl —Displays reports in a vertical, tabular, indented format with data for each step in multiple rows. Customizable, color-coded rows visually separate relevant information, such as step group, status, and so on.

#### ATML Test Results 5.0 Reports Style Sheets

TestStand provides the following style sheets, located in the <TestStand>\Components\Models\TestStandModels\ATML\StyleSheets directory, for generating an ATML Test Results 5.0 report. You can customize the style sheets directly.

- TR5_Expand.xsl —Displays reports similar to TR5_report.xsl , with expandable and collapsible sections for each step or for the entire report.
- TR5_Horizontal.xsl —Displays reports in a horizontal, tabular, indented format with data for each step in one or more rows.
- TR5_report.xsl —Displays reports in a vertical, tabular, indented format with data for each step in multiple rows. Customizable, color-coded rows visually separate relevant information, such as step group, status, and so on.

#### ATML Test Results 2.02 Reports Style Sheets

TestStand provides the following style sheet, located in the <TestStand>\Components\Models\TestStandModels\ATML\StyleSheets directory, for generating an ATML Test Results 2.02 report. You can customize the style sheet directly.

- TR_horizontal.xsl —Displays reports in a concise tabular format with expand and collapse sections. The TR_horizontal.xsl style sheet merges the functionality of the horizontal.xsl and expand.xsl XML report style sheets and displays TestStand PropertyObject attributes for parameters and additional results in the report.

Parent topic:

ATML Test Results Reports

Related concepts:

- ATML Test Results Reports
- TestStand Directory Structure
- Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets
- Customizing the ATML Test Results 2.02 Report Style Sheet
- XML Report Style Sheets
- PropertyObject Attributes

<!--NI_TOPIC bundle=teststand path=atml-test-results-2.html language=enus -->
## TOPIC 00085: ATML Test Results 2.02 Report Structure

- bundle_id: `teststand`
- source_path: `atml-test-results-2.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/atml-test-results-2.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand process models use the ATML Test Results (TR) report generator, ATMLSupport.dll, located in the <TestStand>\Components\Models\TestStandModels directory, to generate a valid ATML TR report format from TestStand variables. The process models call the following functions the report genera

### ATML Test Results 2.02 Report Structure

The TestStand process models use the ATML Test Results (TR) report generator, ATMLSupport.dll, located in the <TestStand>\Components\Models\TestStandModels directory, to generate a valid ATML TR report format from TestStand variables. The process models call the following functions the report generator implements and exports:

- Get_Atml_Report —Generates a valid XML report in TR format.
- GenerateUUID —Generates a universally unique identifier (UUID) for the TR report document, which the uuid attribute of the <TestResults> TR element references.

The TR report generator generates the following XML structure for an ATML TR 2.02 report:

[IMAGE alt='image' src='GUID-5511F976-E681-4C70-A589-598C9484AED6-a5.png']

Note

Parent topic:

ATML Test Results Reports

<!--NI_TOPIC bundle=teststand path=atml-test-results-6-01-and-5.html language=enus -->
## TOPIC 00086: ATML Test Results 6.01 and 5.0 Report Structure

- bundle_id: `teststand`
- source_path: `atml-test-results-6-01-and-5.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/atml-test-results-6-01-and-5.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand process models use the ATML Test Results (TR) report generator, ATMLSupport.dll, located in the <TestStand>\Components\Models\TestStandModels directory, to generate a valid ATML TR report format from TestStand variables. The process models call the following functions the report genera

### ATML Test Results 6.01 and 5.0 Report Structure

The TestStand process models use the ATML Test Results (TR) report generator, ATMLSupport.dll, located in the <TestStand>\Components\Models\TestStandModels directory, to generate a valid ATML TR report format from TestStand variables. The process models call the following functions the report generator implements and exports:

- Get_Atml_Report —Generates a valid XML report in TR format.
- GenerateUUID —Generates a universally unique identifier (UUID) for the TR report document, which the uuid attribute of the <TestResults> TR element references.

The TR report generator generates the following XML structure for an ATML TR 6.01 and 5.0 report:

[IMAGE alt='image' src='GUID-3CE748B3-915F-49AD-B878-EA103CD0C325-a5.png']

Note

Parent topic:

ATML Test Results Reports

<!--NI_TOPIC bundle=teststand path=atml-test-results-reports.html language=enus -->
## TOPIC 00087: ATML Test Results Reports

- bundle_id: `teststand`
- source_path: `atml-test-results-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/atml-test-results-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML Test Results and Session Information schema provides the definition for the data collected when you execute a test or tests of a UUT using test procedures in an automated test environment, including the measured values, pass/fail results, and accompanying data, such as test operator, statio

### ATML Test Results Reports

The ATML Test Results and Session Information schema provides the definition for the data collected when you execute a test or tests of a UUT using test procedures in an automated test environment, including the measured values, pass/fail results, and accompanying data, such as test operator, station information, environmental conditions, and so on. ATML Test Results is a component standard of IEEE 1636 Software Interface for Maintenance Information Collection Analysis (SIMICA).

TestStand generates XML reports that validate against the following versions of the Test Results and Session Information schema the ATML standard defines:

- Approved version 6.01
- Unapproved version 5.0
- Approved version 2.02

Use the Report Format ring control on the Contents tab of the Report Options dialog box to select the version you want to use.

The <TestStand>\Components\Models\TestStandModels\ATML\Schemas directory contains copies of versions 6.01, 5.0, and 2.02 of the schema.

Note

You can customize an ATML report TestStand creates by implementing a DLL that calls one or more exported extension functions.

#### Known Issues with ATML Report Generators

- When a step containing limits has a run mode set to force failure, TestStand does not evaluate the comparator for the limits. This results in an empty comparator attribute value in the generated report XML, which may cause schema validation errors.
- ATML 2 does not support using an EqualityComparisonOperator attribute that is case sensitive. Therefore, ATML 2 reports always display IgnoreCase regardless of which comparison type you select in a String Value Test step.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- ATML
- Comparing Report Format Features
- TestStand Directory Structure
- Customizing the ATML Test Results Report Generator
- Choosing the Appropriate Report Generation Strategy

<!--NI_TOPIC bundle=teststand path=atml.html language=enus -->
## TOPIC 00088: ATML

- bundle_id: `teststand`
- source_path: `atml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/atml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Automatic Test Markup Language (ATML) is an emerging standard in military and aerospace industries for sharing data among different components of a test system. ATML supports test program, test asset, and unit under test (UUT) interoperability within an automatic test environment. ATML accomplishes

### ATML

Automatic Test Markup Language (ATML) is an emerging standard in military and aerospace industries for sharing data among different components of a test system. ATML supports test program, test asset, and unit under test (UUT) interoperability within an automatic test environment. ATML accomplishes this through a standard XML schema for exchanging UUT test and diagnostic information among components of the test system.

ATML specifies standards for test environments that encompass the total product life cycle and defines an integrated set of test-related information that supports the information needs of test environments for testing applications.

ATML standards focus on the following areas:

- Diagnostics
- Instrument Description
- Test Adapter
- Test Configuration
- Test Description
- Test Results and Session Information
- Test Station
- UUT Description

#### Purpose

ATML is intended to accomplish the following objectives:

- Facilitate the communication, sharing, and reuse of product design and test information for the purpose of testing the product.
- Facilitate test program set (TPS) portability and interoperability.
- Facilitate instrument interchangeability.
- Facilitate the development, integration, and use of test software and test software development tools.
- Support the application of integrated diagnostics.
- Support modular software architectures based on a framework that supports reusable software products.

Refer to the ATML website for more information about ATML.

Parent topic:

ATML Test Results Reports

Related concepts:

- ATML Test Results Reports

<!--NI_TOPIC bundle=teststand path=attaching-a-csv-output-stream-to-the-current.html language=enus -->
## TOPIC 00089: Attaching a CSV Output Stream to the Current Execution

- bundle_id: `teststand`
- source_path: `attaching-a-csv-output-stream-to-the-current.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/attaching-a-csv-output-stream-to-the-current.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a CSV file with the New CSV Output Stream step type, you can attach it the current execution if you name the stream. The name must be unique within the scope of the execution. Providing this name (or the optional ExecutionOutputRecordStream object reference) to a Write Record step al

### Attaching a CSV Output Stream to the Current Execution

When you create a CSV file with the New CSV Output Stream step type, you can attach it the current execution if you name the stream. The name must be unique within the scope of the execution. Providing this name (or the optional ExecutionOutputRecordStream object reference) to a Write Record step allows you to display the data being written to the CSV file in the Report view in real time.

Records to Display

Note

Although you can view data written to an output CSV file in the Report view, the CSV file is not a TestStand report as it is not otherwise connected to TestStand reporting features. TestStand reports are driven by process models with their data coming from step results. Using Data Streams, sequences can create and store data to CSV files without running in a TestStand process model. If they do run in a process model, they can still generate ATML, XML, ASCII, HTML, or custom reports. Reports generated using the process model do not interfere with the CSV output file, and the CSV output file does not interfere with reports generated by the model. There is no implicit connection between step results and data written to CSV files. Only data specifically written using Data Streams step types or the TestStand API is stored to the CSV file.

For a demonstration of TestStand Data Streams, see the <TestStand Public>\Examples\Fundamentals\Using Data Streams examples.

Parent topic:

Using the Data Streams Step Type

Related concepts:

- Using Data Streams

<!--NI_TOPIC bundle=teststand path=attaching-additional-data-to-a-session.html language=enus -->
## TOPIC 00090: Attaching Additional Data to a Session

- bundle_id: `teststand`
- source_path: `attaching-additional-data-to-a-session.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/attaching-additional-data-to-a-session.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following methods to attach an object or data structure to a session object. You can also attach additional objects to an instrument session to implement a component that represents the instrument connection at a higher level of abstraction. InstrSession.AttachLong InstrSession.AttachLongPtr

### Attaching Additional Data to a Session

Use the following methods to attach an object or data structure to a session object. You can also attach additional objects to an instrument session to implement a component that represents the instrument connection at a higher level of abstraction.

- InstrSession.AttachLong
- InstrSession.AttachLongPtr
- InstrSession.AttachObject
- InstrSession.AttachString
- InstrSession.DetachData
- InstrSession.GenerateUniqueID
- InstrSession.GetLong
- InstrSession.GetLongPtr
- InstrSession.GetObject
- InstrSession.GetString

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=authenticode-signatures-for-microsoft-windows.html language=enus -->
## TOPIC 00091: Authenticode Signatures for Microsoft Windows

- bundle_id: `teststand`
- source_path: `authenticode-signatures-for-microsoft-windows.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/authenticode-signatures-for-microsoft-windows.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Authenticode signatures can help identify the publisher of a binary file and can help ensure that a binary file has not been modified since publication. In addition, when an application launches on Microsoft Windows 10/8.1/7, User Account Control (UAC) determines whether to grant the application adm

### Authenticode Signatures for Microsoft Windows

Authenticode signatures can help identify the publisher of a binary file and can help ensure that a binary file has not been modified since publication. In addition, when an application launches on Microsoft Windows 10/8.1/7, User Account Control (UAC) determines whether to grant the application administrator privileges and displays your company as the publisher when confirming elevation. Refer to Microsoft documentation for more information about Authenticode signatures.

Add an Authenticode signature to a TestStand user interface you create when you plan to allow users to download the user interface from a non-trusted public site and you want the operating system to identify your company as the publisher of the user interface. Also add an Authenticode signature to a user interface you create when the user interface requires administrator privileges to run on Windows and you want the UAC elevation prompt to identify your company as the publisher of the user interface.

To verify an Authenticode signature, the requesting computer must connect to the Internet to obtain a current Certificate Revocation List (CRL). For .NET applications, the .NET Common Language Runtime (CLR) verifies Authenticode signatures for assemblies. If the computer that loads the assembly is not connected to the Internet, the CLR waits 15 seconds before timing out.

Complete the following steps to disable CRL validation in Microsoft Internet Explorer to avoid the timeout period on the computer, even when the default browser on the computer is not Internet Explorer. Using the Internet Explorer Internet Options to disable CRL validation does not expose the computer to any additional security threats.

1. Navigate to the standard Windows Control Panel facility for Internet options and click the Advanced tab.
2. In the Security section, disable the Check for publisher's certificate revocation option.

Alternatively, you can disable CRL validation by setting the registry key value of HKCU\Software\Microsoft\Windows\CurrentVersion\WinTrust\Trust Providers\Software Publishing\State to 0x00023e00. To enable CRL validation, set the registry key value to 0x00023c00.

When you disable CRL validation to avoid the timeout period, the CLR does not validate Authenticode-signed assemblies and does not grant the assemblies publisher evidence or publisher identity permissions, which is the same result when a timeout occurs. If the assemblies need these permissions, the computer must connect to the Internet or you must download a current CRL every 10–15 days.

As an alternative to disabling CRL validation for the entire computer, you can work around CRL validation if an application that uses the .NET Framework 2.0 and that has an Authenticode signature experiences the 15-second load time delay. Microsoft provides a fix you can download so you can correct this delay for .NET Framework 2.0 applications. The .NET Framework 2.0 Service Pack 1 also includes this fix. Refer to the Microsoft support article at support.microsoft.com/kb/936707 for more information about correcting delays in .NET Framework 2.0 applications that use Authenticode signatures.

The TestStand Sequence Editor and user interface examples do not include Authenticode signatures
 because NI distributes TestStand through trusted channels and because the sequence
 editor and user interface examples do not require administrator privileges to run on
 Windows. Additionally, NI finds the 15-second load time delay on isolated networks
 unacceptable and believes that you should use discretion when disabling CRL
 validation. Therefore, when you run the sequence editor or example user interfaces
 as administrator on Windows, the UAC elevation prompt does not identify the sequence
 editor or example user interface as a NI product.

Parent topic:

Advanced User Interface Development

<!--NI_TOPIC bundle=teststand path=auto-scheduling-and-thread-synchronization-op.html language=enus -->
## TOPIC 00092: Auto Scheduling and Thread Synchronization Operations

- bundle_id: `teststand`
- source_path: `auto-scheduling-and-thread-synchronization-op.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/auto-scheduling-and-thread-synchronization-op.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Auto Scheduling and Thread Synchronization Operations When you use an Auto Schedule step, you also create sub-blocks of steps by using the Use Auto Scheduled Resource steps. Each Use Auto Scheduled Resource step specifies the resources, or locks, it must acquire to run the steps within the sub-block

### Auto Scheduling and Thread Synchronization Operations

#### Auto Scheduling and Thread Synchronization Operations

When you use an 
Auto Schedule step, you also create sub-blocks of steps by using the Use Auto Scheduled Resource steps. Each Use Auto Scheduled Resource step specifies the resources, or locks, it must acquire to run the steps within the sub-block of the step. Before a thread can acquire the resources a Use Auto Scheduled Resource step specifies, the thread must first acquire exclusive access to the step itself.

The Execution Profiler shows an item that represents the Use Auto Scheduled Resource step so you can view the time that threads spend waiting to acces the step. Select View»Show Synchronization»Show Auto Schedulingin the Execution Profiler window to remove the checkmark that appears to the left of the menu item to hide items that represent Use Auto Scheduled Resource steps.

You can also select View»Show Synchronization»Show<Synchronization Type>in the profiler window to selectively show or hide the following other types of TestStand thread synchronization operations:

- Locks
- Rendezvous
- Queue
- Notification
- Batch Synchronization
- Semaphore
- Wait Operations

The profiler shows thread synchronization operations for only the current operating system process. In a typical system, most or all TestStand locks and synchronization operations are local to the current process. You can create cross-process synchronization operations by prefixing the resource name with an asterisk character. You can also create cross-machine operations by prefixing the resource name with a computer name. However, these non-local operations do not appear in the profiler.

Parent topic:

Execution Profiler

Related information:

- Auto Schedule Step
- Execution Profiler Window
- Use Auto Scheduled Resource Step

<!--NI_TOPIC bundle=teststand path=automatic-result-collection.html language=enus -->
## TOPIC 00093: Automatic Result Collection

- bundle_id: `teststand`
- source_path: `automatic-result-collection.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/automatic-result-collection.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand can automatically collect the results of each step. You can enable or disable result collection for a step, a sequence, an execution, or for the entire test station. You can generate a report and log results to a database to process the collected test results. Each sequence includes a loca

### Automatic Result Collection

TestStand can automatically collect the results of each step. You can enable or disable result collection for a step, a sequence, an execution, or for the entire test station. You can generate a report and log results to a database to process the collected test results.

Each sequence includes a local array that stores the results of each step. The contents of the results for each step vary depending on the step type. TestStand stores the results for a step in the array and adds information, such as the name of the step and its position in the sequence. For a step that calls a sequence, TestStand also adds the result array from the subsequence.

Parent topic:

TestStand Building Blocks

Related concepts:

- Result Collection
- Database Logging

<!--NI_TOPIC bundle=teststand path=automatically-adding-or-removing-a-plug-in-fi.html language=enus -->
## TOPIC 00094: Automatically Adding or Removing a Plug-in File to or from Configurations

- bundle_id: `teststand`
- source_path: `automatically-adding-or-removing-a-plug-in-fi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/automatically-adding-or-removing-a-plug-in-fi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you plan to deploy a new model plug-in to an existing TestStand installation and you want TestStand to automatically add an instance of the new plug-in to existing configurations, you must set in the process model plug-in sequence file the Boolean FileGlobals.ModelPluginComponentDescription.Defau

### Automatically Adding or Removing a Plug-in File to or from Configurations

If you plan to deploy a new model plug-in to an existing TestStand installation and you want TestStand to automatically add an instance of the new plug-in to existing configurations, you must set in the process model plug-in sequence file the Boolean FileGlobals.ModelPluginComponentDescription.Default.Base.AutoAddToConfigurations to True.

A setting of True causes the plug-in to be removed from all configurations when the plug-in is removed from the TestStand installation.

Alternatively, you can set the above Boolean to False to disable automatically updating the configurations.

Parent topic:

Configuring Process Model Plug-ins

Related concepts:

- Configuring Process Model Plug-ins
- Programmatically Updating a Configuration File
- Model Plug-in Categories

<!--NI_TOPIC bundle=teststand path=automating-deployment-with-teststand-deployme.html language=enus -->
## TOPIC 00095: Automating Deployment with TestStand Deployment Utility

- bundle_id: `teststand`
- source_path: `automating-deployment-with-teststand-deployme.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/automating-deployment-with-teststand-deployme.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the BuildTSD.exe executable to automate builds of TestStand Deployment Utility files and to make modifications to deployment utility files before the build occurs. BuildTSD.exe accepts a .tsd deployment configuration file and supports optional parameters for configuring properties of the build.

### Automating Deployment with TestStand Deployment Utility

Use the BuildTSD.exe executable to automate builds of TestStand Deployment Utility files and to make modifications to deployment utility files before the build occurs. BuildTSD.exe accepts a .tsd deployment configuration file and supports optional parameters for configuring properties of the build. It will also return a numeric code to provide information about whether the build completed successfully or failed due to an error.

#### Supported Command Line Arguments

BuildTSD.exe supports the <Optional Changes> with the following command line arguments:

- Mode Tab
- System Source Tab
- Installer Options Tab
- Advanced Options Dialog
- Drivers and Components Dialog
- Process Options
- Patching Specific Options

#### Mode Tab

| Option | Type | Notes |
| --- | --- | --- |
| /outputMode | Enumeration | Possible values: ImageMSIInstallerPackageDistribution |
| /packageDistMode | Enumeration | Possible values: SinglePackageRepositoryPackageInstaller |

#### System Source Tab

| Option | Type | Notes |
| --- | --- | --- |
| /deployTSWorkspace | Boolean |  |
| /workspacePath | Absolute Path | You must set the /deployTSWorkspace flag to include the specified workspace in the deployment. |
| /deployDirectory | Boolean |  |
| /directoryToDeploy | Absolute Path |  |
| /includeSubdirectories | Boolean |  |
| /deployTSPublicDirectories | Boolean |  |
| /deployTSCfgDirectory | Boolean |  |
| /deployableImage | Boolean |  |
| /ActiveEnvironmentFile | Absolute Path |  |
| /DeployEnvironmentFile | Boolean |  |

#### Installer Options Tab

| Option | Type | Notes |
| --- | --- | --- |
| /createInstaller | Boolean | This flag is included for backwards compatibility. For new applications, use the /outputMode flag with the value MSIInstaller instead of this flag. |
| /installationName | String |  |
| /installerDirectory | String |  |
| /startMenuItemGroup | String |  |
| /defaultInstallationBaseDir | Enumeration | Possible values: WindowsVolumeTeststandWindowsSystemSystem32ProgramFilesStartMenuStartupDesktopPersonalTempNationalInstrumentsTSPublicTSAppDataAbsolutePath |
| /doNotAskUserForInstallationDirectory | Boolean |  |
| /defaultInstallationSubdirectory | String |  |
| /installerLanguage | Enumeration | Possible values: EnglishFrenchGermanJapaneseKorean |
| /installTSEngine | Boolean |  |
| /hideLicenseDialog | Boolean |  |

#### Advanced Options Dialog

| Option | Type | Notes |
| --- | --- | --- |
| /manufacturer | String |  |
| /versionString | String | Use format #.#.# |
| /autoIncrementVersion | Boolean |  |
| /upgradeCode | String | Use a GUID of the form {21EC2020-3AEA-1069-A2DD-08002B30309D} |
| /readmeFile | Path |  |
| /licenseAgreement | Path |  |
| /mediaSizeMB | Integer |  |
| /includeNetworkLicenseServerSettings | Boolean |  |
| /specifyConfigurationDirectory | Boolean |  |
| /configDestination | Enumeration | Possible values:InstallationTeststandWindowsSystemSystem32ProgramFilesStartMenuStartupDesktopPersonalTempNationalInstrumentsTSPublicTSAppData |
| /configSubDirectory | Relative Path |  |
| /alternateAssociationSeqFiles | Absolute Path |  |
| /processModel | Enumeration | Possible values:NoChangeForceDefaultModelsForceLegacyModels |
| /installerExecutableName | String | If no value is specified, Deployment Utility uses the default value of install.exe. |

#### Drivers and Components Dialog

| Option | Type | Notes |
| --- | --- | --- |
| /includeHardwareConfiguration | Boolean |  |
| /hardwareConfigurationFile | Absolute Path |  |
| /displayDialogDuringImport | Boolean |  |
| /MAXImportOptions | Enumeration | Possible values:MergeReplacePreserve |

#### Process Options

| Option | Type | Notes |
| --- | --- | --- |
| /copyLogFiles <FilePath> | Absolute Path | Copies the log files from the build to the <FilePath> location. The path must be a directory. |
| /LoadTSDOnly | - | This option will just launch the TSDU and perform the operations specified without automatically performing the build and shutting down.This is useful for checking your command line parameters manually. |
| /SaveTSDFile <FilePath> | Absolute Path | Saves the .tsd file after the build to the <FilePath> location. |

Note

/LoadTSDOnly

#### Patching Specific Options

| Option | Type | Notes |
| --- | --- | --- |
| /SetDistribution | Enumeration | Possible values:FullPatch |
| /UserFilesToInclude | Enumeration | Possible values:IncludeChangedFilesDoNotIncludeFilesManual |
| /UpgradesandPatchesToInclude | Enumeration | Possible values:TSEngineandDriversTSEngineDriversNone |
| /DependOn | Enumeration | Possible values:FullDeploymentBaselinePatchDeployment |

Note

TRUE

FALSE

#### BuildTSD.exe Exit Codes

The Deployment Utility returns one of the following return values after building a TSD:

#### Exit Codes

| Number | Result | Definition |
| --- | --- | --- |
| 0 | Success | The build succeeded without errors or warnings. |
| 1 | Load failed | The TSD file failed to load. |
| 2 | Aborted | The TSDU was aborted while building, the installer was not built. |
| 3 | Fatal error | The TSDU encountered a fatal error while building. |
| 4 | Built with errors | The TSDU created an installer but there were some errors while building. |
| 5 | Built with warnings | The TSDU created an installer but there were some warnings while building. |
| 6 | Could not start the TSDU | The TSDU could not be found. |
| 7 | TSDU did not return a value | This can happen if the TSDU crashes before being able to communicate the result to the caller process. |
| 8 | No build performed | TSDU exited without performing a build. |

Parent topic:

Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=avoid-batch-synchronization-sections-in-proce.html language=enus -->
## TOPIC 00096: Avoid Batch Synchronization Sections in Process Model Plug-in Entry Points

- bundle_id: `teststand`
- source_path: `avoid-batch-synchronization-sections-in-proce.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/avoid-batch-synchronization-sections-in-proce.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Do not use Serial, Parallel, or One Thread Only batch synchronization sections in model plug-in entry point sequence files.

### Avoid Batch Synchronization Sections in Process Model Plug-in Entry Points

Do not use Serial, Parallel, or One Thread Only batch synchronization sections in model plug-in entry point sequence files.

Parent topic:

Structure of Plug-in Sequence Files

Related concepts:

- Model Plug-in Entry Points

<!--NI_TOPIC bundle=teststand path=avoiding-unwanted-type-version-propagation.html language=enus -->
## TOPIC 00097: Avoiding Unwanted Type Version Propagation

- bundle_id: `teststand`
- source_path: `avoiding-unwanted-type-version-propagation.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/avoiding-unwanted-type-version-propagation.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a type conflict occurs, selecting to use the later version number of a type can propagate unwanted type versions to all instances of the type. For example, unwanted propagation might occur in the following situations: You create a new version of a step type that is not compatible with previous

### Avoiding Unwanted Type Version Propagation

When a type conflict occurs, selecting to use the later version number of a type can propagate unwanted type versions to all instances of the type. For example, unwanted propagation might occur in the following situations:

- You create a new version of a step type that is not compatible with previous versions of TestStand. A sequence file that contains the new type loads in a previous version of TestStand that contains an older version of the type in a type palette. In versions of TestStand earlier than version 4.1, the new version of the type automatically propagates to the type palette in the previous version of TestStand and to all files loaded in memory from then on. Because the type is not compatible with previous versions of TestStand, you might experience undesired behavior when you run sequences that use the new type. In TestStand 4.1 or later, by default types no longer automatically propagate to type palette files.
- Two types with completely different functionality share the same name. When the TestStand Engine loads the two types, the engine assumes that the types are different versions of the same type and loads the type with the later version number, which can affect the functionality of the sequence files that contain instances of the second type.
- Two different developers independently customize the same type with different changes.

#### Avoiding Unwanted Type Version Propagation to Previous Versions of TestStand

Because you can save sequence files to previous versions of TestStand but some types might not run correctly on previous versions of TestStand, you can specify the earliest version of TestStand that can run a type. Enable the Set Earliest TestStand Version that can Use this Type option on the Version tab of the Step Type Properties dialog box or on the Version tab of the Type Properties dialog box and set the earliest version to the current version of TestStand to prevent the current version of a type from being used in or accidentally propagated to an earlier TestStand version.

You can also create different versions of the type to run in different versions of TestStand. When you save a sequence for a previous version of TestStand, TestStand searches a set of compatibility directories to find the type version that is compatible with the previous version for which you want to save the sequence file. TestStand saves the types from the type palette files in the <TestStand>\Components\Compatibility\<version number> and <TestStand Public>\Components\Compatibility\<version number> directories with the sequence file. You can place type palette files from earlier versions of TestStand in the <TestStand Public>\Components\Compatibility\<version number> directory to ensure that TestStand saves the correct version of the types with the sequence file.

Parent topic:

Managing Type Revisions

Related concepts:

- Managing Type Revisions
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=batch-controller-and-socket-arch.html language=enus -->
## TOPIC 00098: Batch Controller and Test Socket Synchronization Architecture

- bundle_id: `teststand`
- source_path: `batch-controller-and-socket-arch.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/batch-controller-and-socket-arch.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Batch process model creates a controller execution and an execution for each test socket. When performing certain operations, the batch model synchronizes the controller and test socket executions at various synchronization points to ensure exclusive access to shared resources and data. If you c

### Batch Controller and Test Socket Synchronization Architecture

The Batch process model creates a controller execution and an execution for each test socket. When performing certain operations, the batch model synchronizes the controller and test socket executions at various synchronization points to ensure exclusive access to shared resources and data.

If you create a model plug-in that performs operations in the Batch Start and Batch Done controller entry points that must synchronize with operations in the UUT Start and UUT Done test socket entry points, you can call methods of the ControllerAndSocketSynchronizationManager class of ManagedModelSupport.dll, located in the <TestStand>\Components\Models\TestStandModels\ManagedModelSupport directory, from the controller thread or the test socket thread, as described in the following table.

| Method | Called From |
| --- | --- |
| WaitForTestSockets | Controller thread |
| SyncWithController | Test socket thread |
| AllowTestSocketsToContinue | Controller thread |

You can use the class to implement controller and test socket synchronization in which the sockets either to release them or to release them.

#### Test Sockets Wait for the Controller to Release the Sockets

The controller thread calls the WaitForTestSockets method, which waits until all test sockets reach a corresponding call to the SyncWithController method, which then waits until the controller executes a corresponding call to the AllowTestSocketsToContinue method, as shown in the following figure.

[IMAGE alt='image' src='GUID-F9A2A4F5-C8A7-4EDA-8FCD-320B01B21988-a5.svg']

This synchronization implementation requires the following functionality:

- The controller passes True to the socketsWaitForController parameter of the WaitForTestSockets method.
- The test sockets pass True to the waitForController parameter of the SyncWithController method.
- The controller executes a corresponding call to the AllowTestSocketsToContinue method.

#### Test Sockets Do Not Wait for the Controller to Release the Sockets

The controller thread calls the WaitForTestSockets method, which waits until all test sockets reach a corresponding call to the SyncWithController method. The test sockets immediately continue execution after calling the SyncWithController method. The controller does not execute a corresponding call to the AllowTestSocketsToContinue method, as shown in the following figure.

[IMAGE alt='image' src='GUID-AEC9C468-7815-4BAA-9581-491B79BE8689-a5.gif']

This synchronization implementation requires the following functionality:

- The controller passes False to the socketsWaitForController parameter of the WaitForTestSockets method.
- The test sockets pass False to the waitForController parameter of the SyncWithController method.
- The controller must not execute a corresponding call to the AllowTestSocketsToContinue method.

Parent topic:

Batch Process Model

Related concepts:

- Batch Process Model
- Process Model Plug-In Architecture
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=batch-controller-and-socket-restrictions.html language=enus -->
## TOPIC 00099: Batch Controller and Test Socket Synchronization Restrictions

- bundle_id: `teststand`
- source_path: `batch-controller-and-socket-restrictions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/batch-controller-and-socket-restrictions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ControllerAndSocketSynchronizationManager class of ManagedModelSupport.dll, located in the <TestStand>\Components\Models\TestStandModels\ManagedModelSupport directory, requires a corresponding call to the WaitForTestSockets method for each call to the SyncWithController method, regardless of the

### Batch Controller and Test Socket Synchronization Restrictions

The ControllerAndSocketSynchronizationManager class of ManagedModelSupport.dll, located in the <TestStand>\Components\Models\TestStandModels\ManagedModelSupport directory, requires a corresponding call to the WaitForTestSockets method for each call to the SyncWithController method, regardless of the controller and test socket synchronization implementation.

In addition, when you implement controller and test socket synchronization in which the sockets wait for the controller to release them, the ControllerAndSocketSynchronizationManager class requires a corresponding call to the AllowTestSocketsToContinue method for each specific call to the WaitForTestSockets method.

Parent topic:

Batch Controller and Test Socket Synchronization Architecture

Related concepts:

- Batch Controller and Test Socket Synchronization Architecture
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=batch-process-model.html language=enus -->
## TOPIC 00100: Batch Process Model

- bundle_id: `teststand`
- source_path: `batch-process-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/batch-process-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Batch process model, <TestStand>\Components\Models\TestStandModels\BatchModel.seq, includes sequences for the following components: Main Execution entry pointsTest UTsSingle Pass Hidden Execution entry pointsTest UUTs - Test Socket Entry PointSingle Pass - Test Socket Entry Point Configuration e

### Batch Process Model

The Batch process model, <TestStand>\Components\Models\TestStandModels\BatchModel.seq, includes sequences for the following components:

- Main Execution entry points
  - Test UTs
  - Single Pass
- Hidden Execution entry points
  - Test UUTs - Test Socket Entry Point
  - Single Pass - Test Socket Entry Point
- Configuration entry points
- Model callbacks
- Plug-in utility sequences
- Engine callbacks

Use the Batch model to control a set of test sockets that test multiple UUTs as a group. For example, if you have a set of circuit boards attached to a common carrier, use the Batch model to ensure that you start and finish testing all boards at the same time.

Note

With the synchronization features of the Batch model, you can direct a step that applies to the batch as a whole to run only once per batch instead of once for each UUT. You can also specify whether certain steps or groups of steps cannot run on more than one UUT at a time or whether certain steps must run on all UUTs at the same time. The Batch model generates batch reports that summarize the test results for the UUTs in the batch.

When you select the Single Pass Execution entry point, the Batch model launches a separate execution for each test socket without prompting for UUT serial numbers.

Parent topic:

Process Model Architecture

Related concepts:

- TestStand Directory Structure
- Main Execution Entry Points in the Batch Process Model
- Test UUTs Execution Entry Point in the Batch Process Model
- Single Pass Execution Entry Point in the Batch Process Model
- Hidden Execution Entry Points in the Batch Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model
- Single Pass - Test Socket Entry Point in the Batch Process Model
- Configuration Entry Points
- Model Callbacks in the Batch Process Model
- Plug-in Utility Sequences
- Engine Callback
- Testing UUTs in Parallel - Batch Model
- Overriding PreBatch and PostBatch Model Callbacks
- Overriding PreUUT and PostUUT Batch Model Callbacks

<!--NI_TOPIC bundle=teststand path=batch-reports.html language=enus -->
## TOPIC 00101: Batch Reports

- bundle_id: `teststand`
- source_path: `batch-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/batch-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use the Batch process model, the model generates a batch report in addition to a report for each UUT. The batch report summarizes the results for all the UUTs in the batch. ATML 6.01, ATML 5.0, XML, and HTML reports link to each UUT report. The ATML 2.02 standard does not support batch repo

### Batch Reports

When you use the Batch process model, the model generates a batch report in addition to a report for each UUT. The batch report summarizes the results for all the UUTs in the batch. ATML 6.01, ATML 5.0, XML, and HTML reports link to each UUT report.

The ATML 2.02 standard does not support batch reports. The Batch process model generates only UUT reports when you select ATML 2.02 as a report format.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- Batch Process Model

<!--NI_TOPIC bundle=teststand path=before-you-begin.html language=enus -->
## TOPIC 00102: Before You Begin

- bundle_id: `teststand`
- source_path: `before-you-begin.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/before-you-begin.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you start developing a test system, you must understand the concepts in this section so you can make appropriate design decisions that affect deployment as you complete development tasks. TestStand systems typically run on test station computers used exclusively for testing devices during the

### Before You Begin

Before you start developing a test system, you must understand the concepts in this section so
 you can make appropriate design decisions that affect deployment as you complete
 development tasks.

TestStand systems typically run on test station computers used exclusively for testing devices during the design validation or manufacturing process. Test system developers use separate development computers to create and modify code modules, test sequences, user interfaces, and process models without affecting tests that run on test station computers. In most cases, development computers contain the complete test system, including NI drivers and components and any required third-party components and installers.

Typically, developers manually configure test systems on development computers by running multiple installers, copying files, and changing settings as required. However, using a manual technique might not be efficient or reliable when you must move a test system from a development computer to multiple test station computers.

#### Deployment

Deployment is the process of moving software components a TestStand-based test system requires for successful execution from a development computer to one or more test station computers. Using a well-designed and robust deployment process, you can more easily accomplish the following tasks:

- Increase the number of test station computers, such as adding test station computers to a production line
- Update deployed test systems to correct issues or add support to test new products or product lines
- Develop new test systems that reuse existing components

NI provides two applications you can use to deploy TestStand systems:

- TestStand Deployment Utility – Allows you to create MSI-based distributions and patches, create simple package-based distributions and patch installers, and create deployable images shared via network drive or source code control system.
- NI Package Builder – Allows you to create multiple top-level packages from a single TestStand project and build multiple distributions. Note You may need to update NI Package Builder to support building packages for the version of TestStand you use. Refer to the TestStand Readme and the NI Package Builder Readme for information about supported versions.NI Package Builder is missing some features that the TestStand Deployment Utility supports. NI plans to continuously develop new features in Package Builder so that it can eventually replace the TestStand Deployment Utility. New releases of Package Builder will be made available through NI Package Manager.If your deployment applications require any missing features of NI Package Builder, you can
 continue to use the TestStand Deployment Utility until the features
 are added to Package Builder. Refer to the *NI Package Builder
 Manual* on ni.com/docs for a
 comparison of features in TestStand Deployment Utility versus
 Package Builder.

Use the appropriate application to complete the following common tasks:

- Specify source files directory or a TestStand workspace file that references required files and dependencies, including sequence files, code modules, and other supporting files
- Analyze test sequences and create a full or patch deployable image of the test system
- Use the deployment utility or third-party installer development tools to build a customized full or patch deployment distribution to transfer the test system from the development computer to the test station computer
- Use the deployable image as the source for deploying test systems using a network drive or a source code control system

#### Using MSI-Based Installers to Deploy Test Systems

For MSI-based deployments, you must use the TestStand Deployment Utility. You can use the deployment utility to accomplish the following installer-related tasks:

- Build a single, custom installer to redistribute only the NI drivers and software components that the test system requires and that you have installed on the development computer. Note You must install the TestStand Runtime for TestStand-based test systems to function correctly. You must also install the LabVIEW Run-Time Engine on the test station computer to execute VIs and any required NI hardware devices drivers, such as NI-DAQmx.
- Build multiple installers for the test system to reduce the time required to create the deployment, to reduce the size of the installer, and to more easily perform frequent updates for the test system you deploy.
- Install multiple test systems on a single test station computer.
- Build patch deployment installers that contain only the files and software components that differ from the previous deployment.

Note

<National Instruments>\_Legal Information

#### Using Package-Based Distributions to
 Deploy Test Systems

You can use a package based distribution to distribute
 as a package visible from NI Package Management tools, including NI Package Manager.
 You can use the package distribution capability of the TestStand Deployment Utility
 or NI Package Builder to accomplish the following tasks:

- Build a single package file, which you can distribute by copying directly to a
 test station computer, or using NI package sharing tools. Note You must install
 the TestStand Runtime for TestStand-based test systems to function
 correctly. You must also install the LabVIEW Run-Time Engine on the test
 station computer to execute VIs and any required NI hardware devices
 drivers, such as NI-DAQmx.
- Create a repository or package installer, which includes required run-time and
 driver dependencies in the distribution in addition to the single package
 file.
- Build a patch deployment which includes only updated packages for drivers and
 run-time software that were not present in the previous deployment.

Note

Building a Distribution with
 NI Package Builder

NI Package Builder Manual

ni.com/docs

Parent topic:

Deploying TestStand Systems

Related concepts:

- Deployment Process Overview
- Preparing Source Components for Deployment
- Using a Directory to Create a Deployment
- Using a TestStand Workspace File to Create a Deployment
- Identifying Components to Deploy
- Analyzing the Test System
- Creating Deployments
- Building an Installer with the TestStand Deployment Utility
- Building an Installer with Third-Party Tools
- Building a Customized MSI-based Installer
- Transferring Files
- Using a Network Drive to Deploy Test Systems
- Using a Source Code Control System to Deploy Test Systems
- Redistributing MSI-based Installer Products in a Deployment
- Choosing Single or Multiple Deployments
- Deploying Multiple Test Systems to the Same Test Station
- Patching Deployments
- Building a Package Distribution with NI Package Builder
- Deploying 32-bit TestStand and 64-bit TestStand Systems
- Installer Issues for 32-bit TestStand and 64-bit TestStand

Related information:

- NI Package Builder Manual

<!--NI_TOPIC bundle=teststand path=benchmarks.html language=enus -->
## TOPIC 00103: Benchmarks

- bundle_id: `teststand`
- source_path: `benchmarks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/benchmarks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example performs a benchmark on each of the TestStand adapters. Example File Location <TestStand Public>\Examples\TestStand Debugging Features\Benchmarks\Benchmarks.seq Highlighted Features Module adapters Performance Major API None Prerequisites You must log into TestStand as a user wi

### Benchmarks

#### Purpose

This example performs a benchmark on each of the TestStand adapters.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand Debugging
 Features\Benchmarks\Benchmarks.seq

#### Highlighted Features

- Module adapters
- Performance

#### Major API

None

#### Prerequisites

You must log into TestStand as a user with administrator privileges. To use the LabVIEW benchmark portion of the example, you must have the LabVIEW development system or LabVIEW Run-Time Engine (RTE) installed and you must configure the LabVIEW Adapter to use the LabVIEW development system or LabVIEW RTE.

#### How to Use This Example

This example runs multiple sets of steps. Each set uses a different adapter and configuration. As the sequence executes, it records the total time required to execute each set of steps. The sequence generates a custom report to display the average execution time for a single step in each set of steps.

You can adjust the following options to improve performance:

- Disable the Enable Tracing option on the Execution tab of the Station Options dialog box.
- Enable the Disable Result Recording for All Sequences option on the Execution tab of the Station Options dialog box.
- To improve the performance of the ActiveX/COM Adapter, disable the Use Late Binding option in the ActiveX/COM Adapter Configuration dialog box.
- To improve the performance of the LabVIEW Adapter, enable the Reserve Loaded VIs for Execution option in the LabVIEW Adapter Configuration dialog box.

Complete the following steps to use this example.

1. Select Execute»Single Pass to run the sequence.
2. Select Continue . If you do not have the LabVIEW development system or LabVIEW RTE installed, select the Continue - skip LabVIEW option.
3. When execution completes, review the report on the Report pane.

Parent topic:

Examples for TestStand Debugging Features

Related concepts:

- Module Adapters
- TestStand Directory Structure
- Privileges
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=binding-a-teststand-custom-user-interface-to.html language=enus -->
## TOPIC 00104: Binding a TestStand Custom User Interface to a Side-by-Side Version of the LabWindows/CVI RTE

- bundle_id: `teststand`
- source_path: `binding-a-teststand-custom-user-interface-to.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/binding-a-teststand-custom-user-interface-to.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following options in LabWindows/CVI 2012 or later to bind a user interface executable to a specific, side-by-side version of the LabWindows/CVI RTE: <version> side-by-side for executable only—Use this option to use the side-by-side version of the LabWindows/CVI RTE only for the user

### Binding a TestStand Custom User Interface to a Side-by-Side Version of the LabWindows/CVI RTE

You can use the following options in LabWindows/CVI 2012 or later to bind a user interface executable to a specific, side-by-side version of the LabWindows/CVI RTE:

- <version> side-by-side for executable only —Use this option to use the side-by-side version of the LabWindows/CVI RTE only for the user interface executable. This option does not affect which version of the LabWindows/CVI RTE used by DLL modules that the LabWindows/CVI Adapter or the C/C++ DLL Adapter call. Those DLL modules use the version of the LabWindows/CVI RTE to which they were bound.
- <version> side-by-side for entire application —Use this option to use the side-by-side version of the LabWindows/CVI RTE for the user interface executable and for DLL modules bound to the default LabWindows/CVI RTE the LabWindows/CVI Adapter and C/C++ DLL Adapter call.

Parent topic:

Using TestStand UI Controls in LabWindows/CVI

Related concepts:

- Choosing Between the Shared or Side-by-Side Version of the LabWindows/CVI Run-Time Engine
- Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand

<!--NI_TOPIC bundle=teststand path=bitness-conditional-code-for-32-bit-teststand.html language=enus -->
## TOPIC 00105: Bitness-Conditional Code for 32-bit TestStand or 64-bit TestStand

- bundle_id: `teststand`
- source_path: `bitness-conditional-code-for-32-bit-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/bitness-conditional-code-for-32-bit-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you cannot write bitness-independent sequence files, use the Engine.Is64Bit property to specify that certain steps or portions of expressions execute only in 32-bit TestStand or in 64-bit TestStand. Typically, you must dynamically load steps that execute conditionally based on bitness. If you p

### Bitness-Conditional Code for 32-bit TestStand or 64-bit TestStand

When you cannot write bitness-independent sequence files, use the Engine.Is64Bit property to specify that certain steps or portions of expressions execute only in 32-bit TestStand or in 64-bit TestStand.

Typically, you must dynamically load steps that execute conditionally based on bitness. If you preload steps that depend on bitness-specific code modules, the version of the step that does not match the bitness of TestStand fails to load and returns an error even though the bitness-conditional code prevents the step from executing.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=bitness-conditional-code-for-dlls-with-differ.html language=enus -->
## TOPIC 00106: Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces

- bundle_id: `teststand`
- source_path: `bitness-conditional-code-for-dlls-with-differ.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/bitness-conditional-code-for-dlls-with-differ.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Function names and parameters can differ between the 32-bit version of an interface and the 64-bit version of an interface for a code module. Parameter type differences might not be obvious because preprocessor macros can generate types. The C/C++ size_t type is a common example of a type that chang

### Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces

Function names and parameters can differ between the 32-bit version of an interface and the 64-bit version of an interface for a code module.

Parameter type differences might not be obvious because preprocessor macros can generate types. The C/C++ size_t type is a common example of a type that changes between the 32-bit version and the 64-bit version of a code module. size_t is a 32-bit unsigned integer in 32-bit DLLs and a 64-bit unsigned integer in 64-bit DLLs. TestStand treats 32-bit versions and 64-bit versions of prototypes that contain size_t parameters as distinct and cannot execute both instances from a single adapter step.

Create a 32-bit version of a step and a 64-bit version of a step and use the Engine.Is64Bit property to write conditional code to call code modules with dissimilar 32-bit versions and 64-bit versions from the same sequence. Use the !RunState.Engine.Is64Bit precondition in the 32-bit version of the step and use the RunState.Engine.Is64Bit precondition in the 64-bit version of the step to execute the version of the step that matches the bitness of TestStand. Alternatively, you can use the RunState.Engine.Is64Bit property in an If step to achieve similar results. Set both steps to load dynamically. If you preload the steps, the version of the step that does not match the bitness of TestStand fails to load and returns an error.

Parent topic:

C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand

Related concepts:

- Bitness-Conditional Code for 32-bit TestStand or 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=build-source-files-and-execute.html language=enus -->
## TOPIC 00107: Build Source Files and Execute

- bundle_id: `teststand`
- source_path: `build-source-files-and-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/build-source-files-and-execute.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Build Source Files and Execute feature supports executing source-only VIs in TestStand using the LabVIEW adapter when it is configured to use the LabVIEW runtime engine.The following options and software are required to use the Build Source Files and Execute feature: LabVIEW Development System v

### Build Source Files and Execute

The Build Source Files and Execute feature supports executing
 source-only VIs in TestStand using the LabVIEW adapter when it is configured to use the LabVIEW
 runtime engine.

The following options and software are required to use the Build Source Files and Execute feature:

- LabVIEW Development System version 2023 Q3 or higher of the same bitness as TestStand must be
 installed on the machine and must be the active LabVIEW version. Keep the following in mind to
 ensure that a compatible version of LabVIEW is set as and stays the active LabVIEW version when
 using the Build Source Files and Execute feature: Note When using the
 Build Source Files and Execute feature with LabVIEW 2024 Q3 or later,
 follow these steps before executing the sequence file:Disable the Maintain the Save Version of Loaded Projects by Default
 feature in LabVIEW. This option can be found in the Tools tab in LabVIEW
 under Tools»Options»Environment.
 If you mass-compiled your LabVIEW files before disabling Maintain the Save
 Version of Loaded Projects by Default, set the save version of your LabVIEW
 projects to Editor Version in the project properties.
  - The active LabVIEW version on a machine is the latest version of LabVIEW that was launched
 on that machine. If a version of LabVIEW Development System is already running, launching a
 different version does not make the second version the active version. You can make a version
 of LabVIEW supported by the Build Source Files and Execute option active by closing any open
 LabVIEW instances and launching the supported version of LabVIEW with the same bitness as
 TestStand.
  - If a supported version of LabVIEW Development System is not installed or active when
 TestStand is launched, the Build Source Files and Execute option is disabled. You must make a
 supported version of LabVIEW Development System active and restart TestStand to enable the
 feature.
  - Sequence files throw errors on execution if the active LabVIEW version changes to an
 unsupported version while the Build Source Files and Execute option is enabled. To resolve
 these errors, make a supported version of LabVIEW Development System active and restart your
 sequence file execution.
- The TestStand Tools package must be installed on the machine. Note 

 This package is installed by default when installing TestStand but is an optional component of the installation.
- The Enable Version Independent Runtime Engine option must be enabled in the LabVIEW Adapter Configuration. Note 

 Enabling the Build Source Files and Execute option in the LabVIEW Adapter Configuration dialog box will also enable the Enable Version Independent Runtime option. The Enable Version Independent Runtime option cannot be disabled while the Build Source Files and Execute option is enabled.

Note

The LabVIEW runtime engine can only load VIs if compiled code created in a LabVIEW version matching the version of the runtime engine is available. Source-only VIs cannot normally be loaded using the LabVIEW runtime engine, as compiled code for these VIs is only present in LabVIEW's compiled object cache if the VI:

- is opened in the LabVIEW Development Environment and compiled or run, or
- is modified and saved.

Note

- LabVIEW steps which call Express VIs are excluded from the PPL builds.
- LabVIEW modules present in step type sub-steps are not included in PPLs built using the Build Source Files and Execute feature. Custom step type authors should ensure that the LabVIEW modules called from sub-steps of a custom step type have compiled code present to allow execution in the LabVIEW runtime engine.

When using the Build Source Files and Execute feature the LabVIEW modules will load and execute the VIs present in the constructed PPLs during execution instead of the VIs specified in the LabVIEW steps. Since VIs present in PPLs are compiled, they can execute in the LabVIEW runtime engine without issues. Executing the VIs in the built PPLs lets you use the functionality of source-only VIs without requiring compiled code for the VIs to be available.

The Build Source Files and Execute feature builds the LabVIEW source files into PPLs when either:

- You execute the sequence files calling the LabVIEW files for the first time, or
- You make changes to the LabVIEW files being called or the LabVIEW steps calling the files.

TestStand only rebuilds the generated PPLs if at least one LabVIEW module from the sequence file gets loaded before execution. If all the LabVIEW modules from the file are already loaded, any changes made to the source files after that will not be present in the PPLs when running your TestStand sequence.

Note

#### Optimizing PPL Build Times

You can improve PPL build times for source-only VIs by making your LabVIEW files source-only when possible. The compiled code for source-only VIs is stored in LabVIEW's cache and can be used to optimize PPL build times.

To set a VI to source-only, press Ctrl+I to open VI Properties and enable Separate Compiled Code from Source File.

#### Build Source Files and Execute Constraints

The following features and options are not supported when using the Build Source Files and Execute feature:

- The Switching Between VIs and Packed Project Libraries feature is disabled when the Build Source Files and Execute feature is enabled. If your sequence file is already configured to switch between VIs and PPLs, you can use the Switching Between VIs and Packed Project Libraries feature to use PPL build specifications from your LabVIEW projects instead of a default build specification generated by TestStand.
- The Preload on File Open load option does not apply to LabVIEW and Sequence Call steps when using the Build Source Files and Execute feature. Steps with this option enabled behave like the load option is set to Preload Before Execution .
- The Load Dynamically load option does not function for Sequence Call steps when using the Build Source Files and Execute feature. Steps with this option selected preloads their modules before execution begins.

#### Forcing PPL Rebuilds

If you encounter build errors when building LabVIEW source file PPLs in TestStand or want to force a rebuild of existing PPLs, you can clear the Builder cache by selecting Execute → Clear LabVIEW Builder Cache from the main TestStand window.

Clearing the Builder cache for a sequence file clears the data stored for built PPLs related to that sequence file, forcing the next execution of the sequence file to rebuild PPLs for any LabVIEW VIs called from that file. You can clear the Builder cache for the active sequence file or for all files using previously built PPLs.

Note

Clear LabVIEW Builder Cache

#### Support for Debugging

To debug PPLs built using the Build Source Files and Execute
 option:

1. Enable the Enable Debugging and Tracing option to make PPLs built
 using the Build Source Files and Execute feagure debuggable. Note Changes made to this option
 do not take effect until you restart the TestStand application.
2. Open the source VI you would like to debug, place breakpoints where necessary and save
 the changes. When the PPL containing the modified VI is built, the corresponding VI in the
 PPL will also have breakpoints.
3. Execute the sequence you want to debug once to build the PPLs and load VIs into memory
 in the LabVIEW runtime Engine.
4. Set LabVIEW to use the TestStand executable to debug.
  1. Open the Debug Application or Shared Library window in LabVIEW by navigating to
 Operate → Debug Application or Shared Library.
  2. Attach LabVIEW to TestStand by selecting the following in the Application or Shared
 Library drop-down menu:

- SeqEdit.exe - ‹ProjectName›.lvproj - My Computer to debug VIs called in project
 context.
- SeqEdit.exe to debug VIs called in the default Application context.

- Execute your sequence in TestStand. If there are breakpoints present in a called VI,
 they will be hit and will break execution to allow for debugging. If there are breakpoints
 present in called LabVIEW steps, they will also break execution and allow you to step into
 called VIs to debug using the LabVIEW Development System.

Note

Parent topic:

LabVIEW Adapter

Related information:

- LabVIEW Adapter Configuration Dialog Box

<!--NI_TOPIC bundle=teststand path=building-a-customized-msi-based-installer.html language=enus -->
## TOPIC 00108: Building a Customized MSI-based Installer

- bundle_id: `teststand`
- source_path: `building-a-customized-msi-based-installer.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-customized-msi-based-installer.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand Deployment Utility to build an MSI-based installer for the deployable image or patch deployable image. You must save the MSI-based installer for the full deployment to build an MSI-based installer for the patch deployment. Use the MSI-based Installer Options tab of the deployment u

### Building a Customized MSI-based Installer

Use the TestStand Deployment Utility to build an MSI-based installer for the deployable image or patch deployable image.

Note

Use the MSI-based Installer Options tab of the deployment utility to customize the MSI-based
 installer as a whole, and use the Distributed Files tab of the deployment utility to
 customize the installation of individual files. You can include the TestStand
 Runtime and MSI-based installers for NI hardware drivers and other software
 components. An MSI-based installer you build with the deployment utility
 automatically requests a reboot when any of the NI drivers or software components
 you redistribute require a reboot, such as the TestStand Runtime.

Note

<National Instruments>\_Legal Information

#### Upgrading Previous
 Installations

Use the following table to determine which technique to use
 to upgrade a previous installation.

| Situation | Action |
| --- | --- |
| New MSI-based installer updates previous MSI-based installer | Create a full deployment that can update an existing installation or that can install to test station computers that do not have the previous installation.To upgrade using a full deployment, use the Advanced MSI-based Installer Options dialog box to increment the installer version but do not modify the upgrade code. Generate a new upgrade code to install a full deployment side-by-side with a previous version of the deployment. Create a patch deployment that can only update a previous installation. Using this technique can significantly reduce the size of the MSI-based installer.To upgrade using a patch deployment, use the Mode tab of the deployment utility to create a patch deployment, which automatically updates the version and upgrade code to install the patch deployment. When you create a cumulative patch deployment, the deployment utility generates a new upgrade code so you can install patch deployments on the test station computer. If you create a patch deployment from a baseline patch deployment, the deployment utility uses the upgrade code of the baseline patch deployment. |
| Files already exist on test station computer | Review the scenarios in which an MSI-based installer overwrites an existing file. |
| You want to override the default MSI-based installer behavior | Enable the Force File to Install option on the Distributed Files tab. Notice When you enable the Force File to Install option, an MSI-based installer can replace a newer version of a file with an older version of a file, which can be problematic for DLLs because components on the computer might rely on functionality available only in the newer version of the DLL and might not execute correctly when the MSI-based installer downgrades the DLL. |

#### Troubleshooting MSI-based Installers You Build with the TestStand Deployment Utility

Use the following techniques to troubleshoot building MSI-based installers with the TestStand Deployment Utility:

- Ensure the hard drive has sufficient disk space for building the MSI-based installer. For example, including the TestStand Runtime requires about 450 MB of disk space.
- Clear the product cache if you are including a NI component or driver in the MSI-based installer
 to remove out-of-date or corrupt files.
- Review the Status Log on the Build Status tab of the deployment utility for more information
 about MSI-based installer build errors. Right-click the Status Log and select
 Group By»Severity or use the column headers to filter
 and display only errors and warnings to help you locate possible problems with
 the MSI-based installer. Click the Save Log drop down
 button and select Save Technical Support Report to save a
 copy of the log that NI can use the log files the deployment utility generates
 to help you diagnose MSI-based installer-related issues.

#### Installing TestStand
 Silently

You can install TestStand without viewing any installation dialog
 boxes. Refer to the NI support article 4CJDP38M, Automating the Installation of a
 Single Installer, on the NI website for information about installing NI software
 silently.

Parent topic:

Creating Deployments

Related concepts:

- Patching Deployments
- Redistributing MSI-based Installer Products in a Deployment
- Clearing the Product Cache
- Deploying 32-bit TestStand and 64-bit TestStand Systems
- Installer Issues for 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=building-a-customized-package-distribution.html language=enus -->
## TOPIC 00109: Building a Customized Package Distribution

- bundle_id: `teststand`
- source_path: `building-a-customized-package-distribution.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-customized-package-distribution.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand Deployment Utility or NI Package Builder to build a package distribution for the deployable image or patch deployable image. You can customize the package attributes, the dependency relationships, and the inclusion of individual files in the package distribution. If you choose the

### Building a Customized Package Distribution

Use the TestStand Deployment Utility or NI Package Builder to build a package distribution for the deployable image or patch deployable image.

You can customize the package attributes, the dependency relationships, and the inclusion of
 individual files in the package distribution. If you choose the Repository or
 Package Installer build outputs, you can include the TestStand Runtime and
 installers for NI hardware drivers and other software components. If you choose the
 single package build output, the generated package will require these components to
 be present on the test station computer, but will not include them in the
 distribution.

A package installer you build automatically requests a reboot when any of the NI drivers or
 software components you redistribute require a reboot, such as the TestStand
 Runtime.

Note

Building a Distribution with NI Package
 Builder

NI Package Builder Manual

#### Upgrading Previous Package
 Distributions

NI packages are uniquely identified by the package name that
 you specify. If you create a new package with the same name as another package, NI
 Package Manager will replace the previous package with the newer package. If the
 version number of the newer package is less than the existing package, NI Package
 Manager will indicate that the package is a downgrade.

When you create a patch
 for a package distribution, the package name must remain the same to ensure that the
 previous package version is replaced with the updated package.

#### Troubleshooting Installers You Build with the TestStand Deployment Utility

Use the following techniques to troubleshoot building installers with the TestStand Deployment Utility:

- Review the Status Log on the Build Status tab of the deployment utility for more information
 about installer build errors. Right-click the Status Log and select
 Group By»Severity or use the column headers to filter
 and display only errors and warnings to help you locate possible problems with
 the installer. Click the Save Log drop down button and
 select Save Technical Support Report to save a copy of
 the log that NI can use the log files the deployment utility generates to help
 you diagnose installer-related issues.
- Ensure the hard drive has sufficient disk space for building the installer. For example, including the TestStand Runtime requires about 450 MB of disk space.

#### Troubleshooting Installers You Build with the NI Package Builder

NI package builder provides build output and error log panes to help troubleshoot issues with deployment. Refer to NI Package Builder Help for more information on how the application displays error logging and output messages.

#### Installing Package Distributions Silently

You can install a package distribution without viewing any installation dialog boxes. For single packages, refer to the NI Package Manager Manual for information on silent installation through the command line.

Parent topic:

Creating Deployments

Related concepts:

- Building a Package Distribution with NI Package Builder

Related information:

- NI Package Builder Manual
- NI Package Manager Manual

<!--NI_TOPIC bundle=teststand path=building-a-package-distribution-with-ni-packa.html language=enus -->
## TOPIC 00110: Building a Package Distribution with NI Package Builder

- bundle_id: `teststand`
- source_path: `building-a-package-distribution-with-ni-packa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-package-distribution-with-ni-packa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use NI Package Builder to build a package-based distribution that contains the files the test system requires to execute successfully on a test station computer, such as sequence files, support files, user interface files, the TestStand Runtime, NI run-time engines (RTEs), and NI drivers and

### Building a Package Distribution with NI Package Builder

You can use NI Package Builder to build a package-based distribution that contains the files the
 test system requires to execute successfully on a test station computer, such as
 sequence files, support files, user interface files, the TestStand Runtime, NI
 run-time engines (RTEs), and NI drivers and components. Additionally, the package
 distribution you build with the deployment utility can perform additional
 post-installation tasks using custom execute commands.

Note

Package Builder can create the following types of package distributions:

- Single Package — The test system files are packaged into a single .nipkg file. Dependencies you select are referenced by the package, and must be installed on the deployment target in order to install the package.
- Repository — In addition to the main package, all dependent packages are
 also included in the deployment. A feed is generated which references all
 included packages. A feed is used to identify packages in NI Package Management
 tools, such as NI Package Manager. To install the deployment, register the feed
 in NI Package Manager on the target machine.
- Package Installer — In addition to the main package, all dependent packages are also included in the deployment. Package Builder also generates a standalone installer which installs all the packages on a machine. The installer will also install NI Package Manager if it is not present on the machine.

Note

NI Package
 Builder Manual

Parent topic:

Choosing a Deployment Mechanism

Related information:

- NI Package Builder Manual

<!--NI_TOPIC bundle=teststand path=building-a-package-distribution-with-the-test.html language=enus -->
## TOPIC 00111: Building a Package Distribution with the TestStand Deployment Utility

- bundle_id: `teststand`
- source_path: `building-a-package-distribution-with-the-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-package-distribution-with-the-test.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand Deployment Utility to build a package-based distribution that contains the files the test system requires to execute successfully on a test station computer, such as sequence files, support files, user interface files, the TestStand Runtime, NI run-time engines (RTEs), and

### Building a Package Distribution with the TestStand Deployment Utility

You can use the TestStand Deployment Utility to build a package-based distribution that contains
 the files the test system requires to execute successfully on a test station
 computer, such as sequence files, support files, user interface files, the TestStand
 Runtime, NI run-time engines (RTEs), and NI drivers and components. Additionally,
 the package distribution you build with the deployment utility can perform the
 following tasks:

- Import hardware configuration information from Measurement & Automation Explorer (MAX)
- Create program items, such as shortcuts
- Launch a custom license agreement at install time

TestStand Deployment Utility can create the following types of package distributions:

- Single Package — The test system files are packaged into a single .nipkg file. Dependencies you select are referenced by the package, and must be installed on the deployment target in order to install the package.
- Repository — In addition to the main package, all dependent packages are
 also included in the deployment. A feed is generated which references all
 included packages. A feed is used to identify packages in NI Package Management
 tools, such as NI Package Manager. To install the deployment, register the feed
 in NI Package Manager on the target machine.
- Package Installer — In addition to the main package, all dependent packages are also included in the deployment. TestStand Deployment Utility also generates a standalone installer which installs all the packages on a machine. The installer will also install NI Package Manager if it is not present on the machine.

Note

Building
 a Distribution with NI Package Builder

NI Package Builder
 Manual

The Repository and Package installer modes also generate a Virtual Package (a package with no file contents) which depends on the main package, and all package dependencies. This package is generated for future support of creating supplemental packages to add to an existing package deployment.

Parent topic:

Choosing a Deployment Mechanism

Related concepts:

- Building a Package Distribution with NI Package Builder

Related information:

- NI Package Builder Manual

<!--NI_TOPIC bundle=teststand path=building-a-sequence-using-api-labview.html language=enus -->
## TOPIC 00112: Building a Sequence Using API - LabVIEW

- bundle_id: `teststand`
- source_path: `building-a-sequence-using-api-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-sequence-using-api-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to programmatically create and execute new test sequences. This example uses an XML file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file. Example File Location <TestStand Public>\Examples\TestSta

### Building a Sequence Using API - LabVIEW

#### Purpose

This example demonstrates how to programmatically create and execute new test sequences. This example uses an XML file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Building a Sequence Using
 API\LabVIEW\Building a Sequence Using API - XML.seq

#### Highlighted Features

- TestStand API
- Flow Control steps

#### Major API

- Engine.NewSequenceFile
- Engine.NewStep
- Sequence.InsertStep
- Engine.GetSequenceFileEx
- Engine.NewExecution
- Execution.WaitForEndEx
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to start the example.
2. When prompted, select the example XML file. The data in this file will be used to create a new sequence file.
3. Notice that a new execution is created. This execution is running the dynamically created sequence file.
4. Open the sample XML file located in <TestStand Public>\TestStand API\Building a Sequence Using API\Common in a text editor. You can modify this file to change the steps in the generated sequence file.

Parent topic:

Building a Sequence Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=building-a-sequence-using-api-net.html language=enus -->
## TOPIC 00113: Building a Sequence Using API - .NET

- bundle_id: `teststand`
- source_path: `building-a-sequence-using-api-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-sequence-using-api-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to programmatically create and execute new test sequences. This example uses an XML file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file. Example File Location <TestStand Public>\Examples\TestSta

### Building a Sequence Using API - .NET

#### Purpose

This example demonstrates how to programmatically create and execute new test sequences. This example uses an XML file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Building a Sequence Using
 API\DotNet\Building a Sequence Using API - XML.seq

#### Highlighted Features

- TestStand API
- Flow Control steps

#### Major API

- Engine.NewSequenceFile
- Engine.NewStep
- Sequence.InsertStep
- Engine.GetSequenceFileEx
- Engine.NewExecution
- Execution.WaitForEndEx
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to start the example.
2. When prompted, select the example XML file. The data in this file will be used to create a new sequence file.
3. Notice that a new execution is created. This execution is running the dynamically created sequence file.
4. Open the sample XML file located in <TestStand Public>\TestStand API\Building a Sequence Using API\Common in a text editor. You can modify this file to change the steps in the generated sequence file.

Parent topic:

Building a Sequence Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=building-a-sequence-using-api-teststand-ini.html language=enus -->
## TOPIC 00114: Building a Sequence Using API - TestStand Expressions (INI)

- bundle_id: `teststand`
- source_path: `building-a-sequence-using-api-teststand-ini.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-sequence-using-api-teststand-ini.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to programmatically create and execute new test sequences. This example uses an INI file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file. Example File Location <TestStand Public>\Examples\TestSta

### Building a Sequence Using API - TestStand Expressions (INI)

#### Purpose

This example demonstrates how to programmatically create and execute new test sequences. This example uses an INI file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Building a Sequence Using
 API\TestStand Expressions\Building a Sequence Using API -
 INI.seq

#### Highlighted Features

- TestStand API
- Flow Control steps

#### Major API

- Engine.NewSequenceFile
- Engine.NewStep
- Sequence.InsertStep
- Engine.GetSequenceFileEx
- Engine.NewExecution
- Execution.WaitForEndEx
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to start the example.
2. When prompted, select the example INI file. The data in this file will be used to create a new sequence file.
3. Notice that a new execution is created. This execution is running the dynamically created sequence file.
4. Open the sample INI file located in <TestStand Public>\TestStand API\Building a Sequence Using API\Common in a text editor. You can modify this file to change the steps in the generated sequence file.

Parent topic:

Building a Sequence Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=building-a-sequence-using-api-teststand-xml.html language=enus -->
## TOPIC 00115: Building a Sequence Using API - TestStand Expressions (XML)

- bundle_id: `teststand`
- source_path: `building-a-sequence-using-api-teststand-xml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-sequence-using-api-teststand-xml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to programmatically create and execute new test sequences. This example uses an XML file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file. Example File Location <TestStand Public>\Examples\TestSta

### Building a Sequence Using API - TestStand Expressions (XML)

#### Purpose

This example demonstrates how to programmatically create and execute new test sequences. This example uses an XML file to create new steps and insert them into a new sequence. The example then saves and executes the new sequence file.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Building a Sequence Using
 API\TestStand Expressions\Building a Sequence Using API -
 XML.seq

#### Highlighted Features

- TestStand API
- Flow Control steps

#### Major API

- Engine.NewSequenceFile
- Engine.NewStep
- Sequence.InsertStep
- Engine.GetSequenceFileEx
- Engine.NewExecution
- Execution.WaitForEndEx
- Engine.ReleaseSequenceFileEx

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to start the example.
2. When prompted, select the example XML file. The data in this file will be used to create a new sequence file.
3. Notice that a new execution is created. This execution is running the dynamically created sequence file.
4. Open the sample XML file located in <TestStand Public>\TestStand API\Building a Sequence Using API\Common in a text editor. You can modify this file to change the steps in the generated sequence file.

Parent topic:

Building a Sequence Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=building-a-sequence-using-api.html language=enus -->
## TOPIC 00116: Building a Sequence Using API

- bundle_id: `teststand`
- source_path: `building-a-sequence-using-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-sequence-using-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\TestStand API\Building a Sequence Using API directory contains the following examples.

### Building a Sequence Using API

The <TestStand
 Public>\Examples\TestStand API\Building a Sequence Using
 API directory contains the following examples.

- [Building a Sequence Using API - LabVIEW](building-a-sequence-using-api-labview.html)
- [Building a Sequence Using API - .NET](building-a-sequence-using-api-net.html)
- [Building a Sequence Using API - TestStand Expressions (INI)](building-a-sequence-using-api-teststand-ini.html)
- [Building a Sequence Using API - TestStand Expressions (XML)](building-a-sequence-using-api-teststand-xml.html)

Parent topic:

Examples for the TestStand API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=building-a-teststand-deployment-with-labview.html language=enus -->
## TOPIC 00117: Building a TestStand Deployment with LabVIEW

- bundle_id: `teststand`
- source_path: `building-a-teststand-deployment-with-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-teststand-deployment-with-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the Deploying TestStand Systems help for the following information: Preparing source components for deployment Processing LabVIEW code modules for deployment Troubleshooting LabVIEW code module issues Using multiple LabVIEW versions in a test system

### Building a TestStand Deployment with LabVIEW

Refer to the Deploying TestStand Systems help for the following information:

- Preparing source components for deployment
- Processing LabVIEW code modules for deployment
- Troubleshooting LabVIEW code module issues
- Using multiple LabVIEW versions in a test system

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Deploying TestStand Systems
- Processing LabVIEW Code Modules for Deployment
- Troubleshooting LabVIEW Code Module Issues
- Using Multiple LabVIEW Versions in a Test System
- Calling VIs That Use XControls
- Creating Custom Step Types that Call VIs for Substeps
- Deploying Stand-alone VIs
- Deploying VIs in LabVIEW Packed Project Libraries
- Deploying VIs in LabVIEW Projects

<!--NI_TOPIC bundle=teststand path=building-a-teststand-ui-cvi.html language=enus -->
## TOPIC 00118: Building a TestStand UI with Native Controls - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `building-a-teststand-ui-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-teststand-ui-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to create a TestStand user interface using only LabWindows/CVI controls. The UI uses the TestStand UI manager controls to manage the application. Example File Location <TestStand Public>\Examples\Modifying User Interfaces\Building a TestStand UI with Native Controls\CV

### Building a TestStand UI with Native Controls - LabWindows/CVI

#### Purpose

This example shows how to create a TestStand user interface using only LabWindows/CVI controls. The UI uses the TestStand UI manager controls to manage the application.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Building a TestStand UI
 with Native Controls\CVI\TestStand UI with Native
 Controls.prj

#### Highlighted Features

TestStand User Interface API

#### Major API

- ApplicationManager.GetCommand
- Command.Execute

#### Prerequisites

You must have LabWindows/CVI installed to execute this example.

#### How to Use This Example

Complete the following steps to review the code in this example:

1. In TestStand UI with Native Controls.prj , open TestExec.c .
2. Select the Initialize case. In this case, references to the manager controls and the LabVIEW controls are stored in the UI data cluster, and this application is set as the main TestStand window.
3. Find the SetupActiveXControls function. This case specifies callback functions that will execute when a TestStand event occurs. Refer to the in-line comments for more information. Note The user interface used control callbacks to implement functionality for controls, in the same way as a typical CVI UI application. These callbacks use the TSUI_ApplicationMgrGetCommand and TSUI_CommandExecute functions to implement TestStand-specific functionality.

Complete the following steps to run the example:

1. (64-bit TestStand) Navigate to Build»Configuration and select Debug64 as the configuration.
2. Click Debug Project to start the user interface.
3. Select Open Sequence File to open a sequence file, then select Execute to run the file using the first entry point in the current process model.
4. Once the execution completes, the report file path is added to the table control. This functionality is implemented in the ApplicationMgr_OnEndExecution event callback.

Parent topic:

Building a TestStand UI with Native Controls

Related concepts:

- TestStand Directory Structure
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=building-a-teststand-ui-labview.html language=enus -->
## TOPIC 00119: Building a TestStand UI with Native Controls - LabVIEW

- bundle_id: `teststand`
- source_path: `building-a-teststand-ui-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-teststand-ui-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to create a TestStand user interface using only LabVIEW controls. The UI uses the TestStand UI manager controls to manage the application. Example File Location <TestStand Public>\Examples\Modifying User Interfaces\Building a TestStand UI with Native Controls\LabVIEW\T

### Building a TestStand UI with Native Controls - LabVIEW

#### Purpose

This example shows how to create a TestStand user interface using only LabVIEW controls. The UI uses the TestStand UI manager controls to manage the application.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Building a TestStand UI
 with Native Controls\LabVIEW\TestStand UI with Native
 Controls.lvproj

#### Highlighted Features

TestStand User Interface API

#### Major API

- ApplicationManager.GetCommand
- Command.Execute

#### Prerequisites

You must have the LabVIEW Development System installed to execute this example.

#### How to Use This
 Example

Complete the following steps to review the code in this
 example:

1. In TestStand UI with Native Controls.lvproj , open
 BasicUIwithNativeControls.vi .
2. Select the Initialize case. In this case, references to
 the manager controls and the LabVIEW controls are stored in the UI data cluster,
 and this application is set as the main TestStand window.
3. Select the Register Event Callbacks case. This case
 specifies callback VIs that will execute when a TestStand event occurs. Refer to
 the in-line comments for more information.
4. Select the Handle Events case. This case handles user
 interaction. Within the event cases, the GetCommand and
 Command.Execute methods are called to implement
 TestStand-specific functionality.
5. Select the Shutdown case. This case closes all references
 and closes the panel.

Complete the following steps to run the example:

1. Click Run to start the user interface.
2. Select Open Sequence File to open a sequence file, then
 select Execute to run it using the first entry point in
 the current process model.
3. Once the execution completes, the report file path is added to the table
 control. This functionality is implemented in the EndExecution event
 callback.

Parent topic:

Building a TestStand UI with Native Controls

Related concepts:

- TestStand Directory Structure
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=building-a-teststand-ui-net.html language=enus -->
## TOPIC 00120: Building a TestStand UI with Native Controls - .NET

- bundle_id: `teststand`
- source_path: `building-a-teststand-ui-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-teststand-ui-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to create a TestStand user interface using only .NET controls. The UI uses the TestStand UI manager controls to manage the application. Example File Location <TestStand Public>\Examples\Modifying User Interfaces\Building a TestStand UI with Native Controls\dotNET\TestS

### Building a TestStand UI with Native Controls
 - .NET

#### Purpose

This example shows how to create a TestStand user interface using only .NET controls. The UI uses the TestStand UI manager controls to manage the application.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Building a TestStand UI
 with Native Controls\dotNET\TestStand UI with Native
 Controls.sln

#### Highlighted Features

TestStand User Interface API

#### Major API

- ApplicationManager.GetCommand
- Command.Execute

#### Prerequisites

You must have Visual Studio installed to execute this example.

#### How to Use This
 Example

Complete the following steps to review the code in this
 example:

1. In TestStand UI with Native Controls.sln , right-click
 MainForm.cs .
2. Select the ApplicationManager control, then click
 Events in the properties pane. Notice that callbacks
 have been specified for certain TestStand events. Double-click a callback to
 view the code. Note 
 The user interface used control callbacks to implement functionality for
 controls, in the same way as a typical .NET UI application. These callbacks
 use the axApplicationMgr.GetCommand and
 Command.Execute methods to implement TestStand-specific
 functionality.

Complete the following steps to run the example:

1. Click Start Debugging to start the user interface.
2. Select Open Sequence File to open a sequence file, then
 select Execute to run the file using the first entry
 point in the current process model.
3. Once the execution completes, the report file path is added to the table
 control. This functionality is implemented in the axApplicationMgr_EndExecution
 event callback.

Parent topic:

Building a TestStand UI with Native Controls

Related concepts:

- TestStand Directory Structure
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=building-a-teststand-ui-with-native-controls.html language=enus -->
## TOPIC 00121: Building a TestStand UI with Native Controls

- bundle_id: `teststand`
- source_path: `building-a-teststand-ui-with-native-controls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-a-teststand-ui-with-native-controls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Modifying User Interfaces\Building a TestStand UI with Native Controls directory contains the following examples.

### Building a TestStand UI with Native Controls

The <TestStand
 Public>\Examples\Modifying User Interfaces\Building a TestStand UI
 with Native Controls directory contains the following examples.

- [Building a TestStand UI with Native Controls - LabWindows/CVI](building-a-teststand-ui-cvi.html)
- [Building a TestStand UI with Native Controls - LabVIEW](building-a-teststand-ui-labview.html)
- [Building a TestStand UI with Native Controls - .NET](building-a-teststand-ui-net.html)

Parent topic:

Examples for Modifying User Interfaces

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=building-an-installer-with-the-teststand-depl.html language=enus -->
## TOPIC 00122: Building an Installer with the TestStand Deployment Utility

- bundle_id: `teststand`
- source_path: `building-an-installer-with-the-teststand-depl.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-an-installer-with-the-teststand-depl.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand Deployment Utility to build an installer that contains the files the test system requires to execute successfully on a test station computer, such as sequence files, support files, user interface files, the TestStand Runtime, NI run-time engines (RTEs), and NI drivers and c

### Building an Installer with the TestStand Deployment Utility

You can use the TestStand Deployment Utility to build an installer that contains the files the
 test system requires to execute successfully on a test station computer, such as
 sequence files, support files, user interface files, the TestStand Runtime, NI
 run-time engines (RTEs), and NI drivers and components. Additionally, the installer
 you build with the deployment utility can perform the following tasks:

- Import hardware configuration information from Measurement & Automation Explorer (MAX)
- Register ActiveX Automation servers
- Create program items, such as shortcuts
- Launch a Readme file and license agreement at install time
- Associate sequence files ( .seq ) with a user interface by using the Alternate Association for .seq Files option in the Advanced Installer Options dialog box
- Run other installers

The deployment utility uses options and configuration settings to build an installer based on Microsoft Windows Installer technology but does not require you to have specific knowledge of Windows Installer technology.

Note

<National Instruments>\_Legal Information

#### Advantages

Using an installer you build with the deployment utility offers the following advantages:

- Using the deployment utility to build the installer does not require additional development tasks to build or customize an installer. You configure installer options in the deployment utility to build an installer using Windows Installer technology.
- You can customize the installer to include the TestStand Runtime, RTEs, and NI drivers and
 components. Because you select the TestStand Runtime optional features to
 include at build time, you can ensure that you deploy the same set of TestStand
 Runtime optional features to all test station computers.
- The installer can launch third-party installers.
- You can include MAX hardware configuration information from the development computer to import into MAX on the test station computer.
- You can place the installer on removable distribution media to physically move to test station computers, which do not require a network infrastructure.
- You can install files in TestStand-specific directories, such as the <TestStand> or <TestStand Public> directories, even if you do not install TestStand to the default location.
- The installer can uninstall files it installed on the test station computer.
- You can build a patch installer that installs only an updated subset of files from a previous installer.

#### Disadvantages

Using an installer you build with the deployment utility presents the following disadvantages:

- You must run the installer on each test system computer, which might not scale well if you use a large number of test station computers.
- The installer does not support repair.
- Users cannot select specific features to install.
- The installer requires a fixed overhead size of about 6.5 MB, which is inefficient for creating deployments that are smaller than that size.

Parent topic:

Choosing a Deployment Mechanism

Related concepts:

- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Building a Customized MSI-based Installer
- Using Custom Commands to Execute Third-Party Installers
- Network-Based Deployment Mechanisms
- TestStand Directory Structure
- Uninstalling a TestStand Deployment

<!--NI_TOPIC bundle=teststand path=building-an-installer-with-third-party-tools.html language=enus -->
## TOPIC 00123: Building an Installer with Third-Party Tools

- bundle_id: `teststand`
- source_path: `building-an-installer-with-third-party-tools.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/building-an-installer-with-third-party-tools.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Deployment Utility does not expose the full set of Microsoft Windows Installer technology features. You must use third-party tools to build a more customized installer that incorporates these features. Building an installer using third-party tools requires specific knowledge of Windows

### Building an Installer with Third-Party Tools

The TestStand Deployment Utility does not expose the full set of Microsoft Windows Installer technology features. You must use third-party tools to build a more customized installer that incorporates these features.

Building an installer using third-party tools requires specific knowledge of Windows Installer technology and typically requires a longer development process than using the deployment utility installer, which does not require specific knowledge of Windows Installer technology.

#### Advantages

Using an installer you build with third-party tools offers the following advantages:

- The installer can repair a damaged installation.
- You can build a patch installer that installs only an updated subset of the files from a previous deployment.
- The installer has a small overhead size.
- You can customize the appearance and functionality of the installer user interface to include more advanced features so users can choose which components to include at install time.
- You can add logic to decide which features to install based on what software already exists on a particular computer
- The installer can remove files it installed on the computer.
- The installer does not require test station computers to rely on a network infrastructure.

#### Disadvantages

Using an installer you build with third-party tools presents the following disadvantages:

- You must have specific knowledge of Windows Installer technology.
- The development process to design, build, and test the installer usually requires more time.
- You must use the deployment utility to build an installer to redistribute NI components or you
 must separately run the installer from the appropriate NI distribution media to
 install the TestStand Runtime and NI run-time engines, drivers, and
 components.
- You must run the installer on each test system computer, which might not scale well if you use a large number of test station computers.

Parent topic:

Choosing a Deployment Mechanism

Related concepts:

- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Building an Installer with the TestStand Deployment Utility
- Redistributing MSI-based Installer Products in a Deployment

<!--NI_TOPIC bundle=teststand path=built-in-and-custom-properties.html language=enus -->
## TOPIC 00124: Built-In and Custom Properties

- bundle_id: `teststand`
- source_path: `built-in-and-custom-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/built-in-and-custom-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand defines a set of built-in properties for some objects, such as steps and sequences. The TestStand Sequence Editor hides these built-in properties by default, but you can modify the property values through panes and dialog boxes. You can also access the built-in properties through the TestS

### Built-In and Custom Properties

TestStand defines a set of built-in properties for some objects, such as steps and sequences. The TestStand Sequence Editor hides these built-in properties by default, but you can modify the property values through panes and dialog boxes. You can also access the built-in properties through the TestStand API.

You can define custom properties, such as high- and low-limit properties in a step or local variables in a sequence.

Parent topic:

Properties

Related concepts:

- Built-In Step Properties
- TestStand ActiveX API Overview
- Custom Step Properties

<!--NI_TOPIC bundle=teststand path=built-in-step-properties.html language=enus -->
## TOPIC 00125: Built-In Step Properties

- bundle_id: `teststand`
- source_path: `built-in-step-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/built-in-step-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand steps include built-in properties you can specify using the following panels on the Properties tab of the Step Settings pane: General Panel Run Options Panel Looping Panel Post Actions Panel Switching Panel Synchronization Panel Expressions Panel Preconditions Panel Requirements Panel Addi

### Built-In Step Properties

TestStand steps include built-in properties you can specify using the following panels on the Properties tab of the Step Settings pane:

- General Panel
- Run Options Panel
- Looping Panel
- Post Actions Panel
- Switching Panel
- Synchronization Panel
- Expressions Panel
- Preconditions Panel
- Requirements Panel
- Additional Results Panel
- Property Browser Panel

Parent topic:

Steps

Related concepts:

- Accessing Properties Using API
- Custom Step Properties

<!--NI_TOPIC bundle=teststand path=built-in-step-types.html language=enus -->
## TOPIC 00126: Built-In Step Types

- bundle_id: `teststand`
- source_path: `built-in-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/built-in-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand groups the core set of built-in step types into the following categories: Step types you can use with any module adapter. Step types such as the Numeric Limit Test and the String Value Test call any code module you specify. They also might perform additional actions, such as comparing a va

### Built-In Step Types

TestStand groups the core set of built-in step types into the following categories:

- Step types you can use with any module adapter. Step types such as the Numeric Limit Test and the String Value Test call any code module you specify. They also might perform additional actions, such as comparing a value the code module returns with limits you specify.
- Step types that always use a specific module adapter to call code modules. Sequence Call is the only step type in this category.
- Step types that perform a specific action and do not require you to specify a code module. Step types such as Message Popup, Statement, and Flow Control perform actions you configure on an edit tab or in an edit dialog box specific to the step type.

Note

Parent topic:

Fundamentals

Related concepts:

- Step Types You Can Use with Any Module Adapter
- Step Types That Work with Specific Module Adapters
- Step Types That Do Not Use Module Adapters
- Instrument Control Step Types

<!--NI_TOPIC bundle=teststand path=c-c-dll-adapter.html language=enus -->
## TOPIC 00127: C/C++ DLL Adapter

- bundle_id: `teststand`
- source_path: `c-c-dll-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/c-c-dll-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the C/C++ DLL Adapter to call C/C++ functions and static C++ class methods in a DLL with a variety of parameter types. You can call global static methods or static class methods in C++ DLLs. You can create the DLL code module with LabWindows/CVI, Microsoft Visual Studio, or any other environment

### C/C++ DLL Adapter

Use the C/C++ DLL Adapter to call C/C++ functions and static C++ class methods in a DLL with a variety of parameter types. You can call global static methods or static class methods in C++ DLLs. You can create the DLL code module with LabWindows/CVI, Microsoft Visual Studio, or any other environment that can create a C/C++ DLL, including LabVIEW-built shared libraries. Use the C/C++ DLL Adapter Configuration dialog box to configure the C/C++DLL Adapter.

When you specify a module for a step the TestStand Sequence Editor displays the C/C++ DLL Module tab on the Step Settings pane to specify a C/C++ DLL Adapter module call, to specify the source code associated with the module call, and to create and edit C/C++ code modules directly from TestStand. TestStand User Interfaces launch the Edit C/C++ DLL Call dialog box.

For DLLs built with LabWindows/CVI, you must use the LabWindows/CVI Adapter to create and edit code modules directly from TestStand. The LabWindows/CVI Adapter provides full integration with the LabWindows/CVI ADE for debugging. You can also use a text editor to create and edit code directly from TestStand.

Note

Parent topic:

Module Adapters

Related concepts:

- Code Modules
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Debugging DLLs
- Features 64-Bit TestStand does not Support
- Adapter and Code Module Support for 64-bit TestStand
- C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand
- Loading Subordinate DLLs
- Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand
- Module Adapter Parameter Mapping Guidelines
- Programming with the TestStand API in Microsoft Visual C++

<!--NI_TOPIC bundle=teststand path=c-c-dll-and-labwindows-cvi-dll-support-for-64.html language=enus -->
## TOPIC 00128: C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `c-c-dll-and-labwindows-cvi-dll-support-for-64.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/c-c-dll-and-labwindows-cvi-dll-support-for-64.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you migrate C/C++ DLL and LabWindows/CVI DLLs from 32-bit TestStand to 64-bit TestStand or want to simultaneously support 32-bit TestStand and 64-bit TestStand, you must ensure that TestStand locates the correct DLL, account for DLLs with different 32-bit interfaces and 64-bit interfaces, and u

### C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand

When you migrate C/C++ DLL and LabWindows/CVI DLLs from 32-bit TestStand to 64-bit TestStand or want to simultaneously support 32-bit TestStand and 64-bit TestStand, you must ensure that TestStand locates the correct DLL, account for DLLs with different 32-bit interfaces and 64-bit interfaces, and use the appropriate pointers and handles.

For the C/C++ DLL and LabWindows/CVI Adapters, the performance for calling 32-bit and 64-bit DLL code modules is similar. However, the performance for loading DLLs into memory is slightly slower for 64-bit DLLs than for 32-bit DLLs.

Parent topic:

Adapter and Code Module Support for 64-bit TestStand

Related concepts:

- Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand
- Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces
- Pointers and Handles in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=call-executable-step-type-support-for-64-bit.html language=enus -->
## TOPIC 00129: Call Executable Step Type Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `call-executable-step-type-support-for-64-bit.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/call-executable-step-type-support-for-64-bit.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you migrate from 32-bit TestStand to 64-bit TestStand or when you need to simultaneously support the 32-bit architecture and the 64-bit architecture, you must consider how to set the Process Handle Location option on the Wait Options tab of the Call Executable edit tab in the TestStand Sequence

### Call Executable Step Type Support for 64-bit TestStand

When you migrate from 32-bit TestStand to 64-bit TestStand or when you need to simultaneously support the 32-bit architecture and the 64-bit architecture, you must consider how to set the Process Handle Location option on the Wait Options tab of the Call Executable edit tab in the TestStand Sequence Editor or on the Wait Options tab of the Configure Call Executable dialog box in a TestStand User Interface. The Process Handle Location option stores a process handle as a pointer-sized value. 32-bit TestStand expects this expression to be of type Object Reference or Number with the default representation (double). 64-bit TestStand expects this expression to be of type Object Reference.

Use the Step.ProcessHandle Call Executable step type property, which is a Number with the default (double) representation, only for backward compatibility. For new code and code that needs to be 64-bit compatible, use the Step.ProcessHandlePtr property instead. The Step.ProcessHandlePtr Call Executable step type property is an Object Reference variable that can store a pointer-sized integer regardless of the bitness of TestStand. When you pass this value into a code module, you can use the pointer/handle type for C/C++, the IntPtr type for the .NET Adapter, or use the expression functions UInt64 or Float64 to convert the value to a 64-bit number for 64-bit TestStand or to a 32-bit number for 32-bit TestStand as needed.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=call-rule-config-custom-rules.html language=enus -->
## TOPIC 00130: Calling Rule Configuration Modules for Custom Rules

- bundle_id: `teststand`
- source_path: `call-rule-config-custom-rules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/call-rule-config-custom-rules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to call a rule configuration module to launch a dialog box you create to configure a custom rule. On the Advanced tab of the Edit Rule dialog box, select Use Configuration Module from the Configuration Option ring control. Click the Browse button to navigate to the VI, .

### Calling Rule Configuration Modules for Custom
 Rules

Complete the following steps to call a rule
 configuration module to launch a dialog box you create to configure a custom
 rule.

1. On the Advanced tab of the Edit Rule
 dialog box, select Use Configuration Module from the
 Configuration Option ring control.
2. Click the Browse button to navigate to the VI, .NET
 assembly, or DLL rule configuration module you want to use.
3. If you selected a DLL, use the Function ring control to
 specify the function in the DLL to call.
4. If you selected a .NET assembly, use the Class and
 Method ring controls to specify the method in the
 .NET assembly to call. 
 Note When you add
 rule settings to a custom rule, the Rules pane or tab displays a Settings
 button next to the rule in the Edit Rule dialog box. Click the Settings
 button to launch the Rule Settings dialog box.

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Creating Rule Configuration Modules in the TestStand Sequence Analyzer

Related information:

- Edit Rule Dialog Box
- RuleConfigurationContext
- Rules Pane - Current Sequence Analyzer Project Window

<!--NI_TOPIC bundle=teststand path=callback-sequences.html language=enus -->
## TOPIC 00131: Callback Sequences

- bundle_id: `teststand`
- source_path: `callback-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/callback-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Callbacks are sequences TestStand calls under specific circumstances. You can create new callbacks or you can override existing callbacks to customize the operation of the test station. Use the Sequence File Callbacks dialog box to add a callback to a sequence file. TestStand defines Model callbacks

### Callback Sequences

Callbacks are sequences TestStand calls under specific circumstances. You can create new callbacks or you can override existing callbacks to customize the operation of the test station. Use the Sequence File Callbacks dialog box to add a callback to a sequence file.

TestStand defines Model callbacks, Engine callbacks, and Front-End callbacks based on the entity that invokes the callback and the location in which you define the callback, as shown in the following table.

| Callback Type | Where You Define the Callback | What Calls the Callback | Description |
| --- | --- | --- | --- |
| Model Callbacks | The process model file defines Model callbacks, and the client sequence file or StationCallbacks.seq can override the callback | Sequences in the process model file | Customizes the behavior of a process model for each Main sequence that uses it. |
| Engine Callbacks | StationCallbacks.seq for Station Engine callbacks, the process model file for Process Model Engine callbacks, or a regular sequence file for Sequence File Engine callbacks. | The TestStand Engine defines and invokes Engine callbacks at specific points during execution. | Engine |
| Front-End Callbacks | FrontEndCallbacks.seq | User interface application | User interface programs call Front-End callbacks so multiple user interfaces share the same behavior for a specific operation. |

Parent topic:

TestStand Building Blocks

Related concepts:

- List of Engine Callbacks
- Customizing Process Models and Callbacks

<!--NI_TOPIC bundle=teststand path=calling-dlls-from-teststand.html language=enus -->
## TOPIC 00132: Calling DLLs from TestStand

- bundle_id: `teststand`
- source_path: `calling-dlls-from-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-dlls-from-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can call LabVIEW, Microsoft Foundation Class (MFC), and subordinate DLLs from TestStand. If a DLL contains export information, TestStand displays parameter information on the Module tab on the Step Settings pane. Calling LabVIEW DLLs that Use ActiveX Controls LabVIEW shared libraries (DLLs) that

### Calling DLLs from TestStand

You can call LabVIEW, Microsoft Foundation Class (MFC), and subordinate DLLs from TestStand. If a DLL contains export information, TestStand displays parameter information on the Module tab on the Step Settings pane.

#### Calling LabVIEW DLLs that Use ActiveX Controls

LabVIEW shared libraries (DLLs) that use ActiveX controls must load in a thread initialized as single-threaded apartment (STA) for the controls to function correctly. When the TestStand step that calls the DLL preloads the DLL, TestStand ensures that the DLL loads in an STA thread. However, when you dynamically load a step that calls the DLL, you must ensure that the loading sequence executes in an STA thread.

Use the Run Sequence in a New Thread option or the Run Sequence in a New Execution option located in the Multithreading and Remote Execution section in the Edit Sequence Call dialog box to select an STA thread. Click the Settings button in the Edit Sequence Call dialog box to launch the Thread Settings dialog box, which contains the STA thread options.

#### Calling DLLs that Use MFC Functions

The MFC Library places several requirements on DLLs that use the DLL version of the MFC run-time library. When you call a DLL that includes MFC functions, verify that the DLL meets these requirements. Also, when the DLL uses resources such as dialog boxes, verify that the AFX_MANAGE_STATE macro appears at the beginning of the function body of each function you call. Refer to the MFC documentation for more information about calling DLLs.

Parent topic:

Module Adapters

Related concepts:

- Loading Subordinate DLLs
- Launching an MFC Dialog with ActiveX Controls

<!--NI_TOPIC bundle=teststand path=calling-dynamic-dispatch-vis.html language=enus -->
## TOPIC 00133: Calling Dynamic Dispatch VIs

- bundle_id: `teststand`
- source_path: `calling-dynamic-dispatch-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-dynamic-dispatch-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how you can use dynamic dispatch with LabVIEW classes directly from a TestStand sequence to implement a hardware abstraction layer (HAL). In this approach, TestStand calls the implementation of each Class VI corresponding to the class you select in the initial dialo

### Calling Dynamic Dispatch VIs

#### Purpose

This example demonstrates how you can use dynamic dispatch with LabVIEW classes directly from a TestStand sequence to implement a hardware abstraction layer (HAL). In this approach, TestStand calls the implementation of each Class VI corresponding to the class you select in the initial dialog.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Calling Dynamic Dispatch VIs\Calling
 Dynamic Dispatch VIs.seq

#### Highlighted Features

- LabVIEW Adapter - Class Member Call
- Dynamic Dispatch

#### Major API

None

#### Prerequisites

The LabVIEW 2012 Run-Time engine or LabVIEW 2012 or higher development system is required to execute this example. Dynamic dispatch support in TestStand requires LabVIEW 2012 or higher.

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Single Pass to execute the sequence.
2. When prompted, select the DMM base class and click OK .
3. When the sequence completes, view the report. Notice that the report text indicates the class used.
4. Select Execute»Single Pass to execute the sequence again.
5. When prompted, select one of the child classes and click OK .
6. When the sequence completes, view the report. Notice that the report text has now changed because the steps called the specific VIs in the class you selected.

Complete the following steps to review the sequences and steps in this example:

1. In MainSequence, select the Select Class VI . This VI returns a reference to a different LabVIEW class based on the user selection. The VI can return the parent DMM Base class, or one of two child classes—PCI-4070 or Simulated DMM. Note The Initialize, Read, and Close steps are configured using the Class member call call type in order to call members of the Generic DMM class. Based on the class selected previously, TestStand dynamically selects the implementation of the class VI which matches the class reference. This action allows the sequence to behave differently based on the type of LabVIEW class reference selected.
2. To view the implementation of the LabVIEW classes, open classes.prj, located in <TestStand Public>\Examples\Fundamentals\Calling Dynamic Dispatch VIs.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure
- Calling LabVIEW Class Member VIs from TestStand
- Passing an Instance of a LabVIEW Class Object

<!--NI_TOPIC bundle=teststand path=calling-labview-class-member-vis-from-teststa.html language=enus -->
## TOPIC 00134: Calling LabVIEW Class Member VIs from TestStand

- bundle_id: `teststand`
- source_path: `calling-labview-class-member-vis-from-teststa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-labview-class-member-vis-from-teststa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select the Class Member Call option from the Call Type ring control on the LabVIEW Module tab in the TestStand Sequence Editor or on the Module tab of the Edit LabVIEW VI Call dialog box in a TestStand User Interface to call a member VI defined in a LabVIEW class, as shown in the following table. La

### Calling LabVIEW Class Member VIs from TestStand

Select the Class Member Call option from the Call Type ring control on the LabVIEW Module tab in the TestStand Sequence Editor or on the Module tab of the Edit LabVIEW VI Call dialog box in a TestStand User Interface to call a member VI defined in a LabVIEW class, as shown in the following table.

| LabVIEW Version | TestStand Behavior |
| --- | --- |
| LabVIEW 2012 or later | TestStand supports dynamically dispatching a member VI from a LabVIEW class. |
| LabVIEW 2009 SP1 or later | TestStand supports calling static member VIs defined in a LabVIEW class. TestStand statically calls member VIs for which dynamic dispatching is enabled. |

You can call only public members, methods, and properties from LabVIEW classes, but cannot execute a member call remotely.

TestStand supports passing an instance of a LabVIEW Class data type, also called a LabVIEW class object, wired to and from the connector pane of a member VI. You can store LabVIEW class objects in TestStand object reference variables.

Note

- TestStand does not support dynamic dispatching when you select the VI Call option from the Call Type ring control.
- You must have LabVIEW 2012 or later to use LabVIEW dynamic dispatching when calling LabVIEW classes in TestStand.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Passing an Instance of a LabVIEW Class Object
- Calling LabVIEW VIs
- Getting Started with TestStand
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=calling-labview-property-nodes-from-teststand.html language=enus -->
## TOPIC 00135: Calling LabVIEW Property Nodes from TestStand

- bundle_id: `teststand`
- source_path: `calling-labview-property-nodes-from-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-labview-property-nodes-from-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure a TestStand step to call a LabVIEW Property Node, which you can use to configure several properties for LabVIEW I/O references. Complete the following steps to insert a LabVIEW step that configures a LabVIEW Property Node call. Insert an Action step in the Main step group. Select P

### Calling LabVIEW Property Nodes from TestStand

You can configure a TestStand step to call a LabVIEW Property Node, which you can use to configure several properties for LabVIEW I/O references. Complete the following steps to insert a LabVIEW step that configures a LabVIEW Property Node call.

1. Insert an Action step in the Main step group.
2. Select Property Node Call from the Call Type ring control LabVIEW Module tab in the TestStand Sequence Editor or on the Module tab of the Edit LabVIEW VI Call dialog box in a TestStand User Interface. The LabVIEW Module tab updates to display the Property Node Type control.
3. Click the Configure Settings for Property Node button located to the right of the Property Node Type control to launch the Configure Property Node dialog box.
4. Select a library type from the Property Node Type control, which displays the different types available in LabVIEW, depending on the hardware configuration.
5. Select the appropriate LabVIEW I/O reference type from the Property Node Class control, which specifies the I/O Reference class for the type you selected in the Property Node Type control. The Available Properties List control lists the properties available for the currently selected LabVIEW I/O reference type or LabVIEW class.
6. Select a property from the Available Properties List control and click the Add to Selected Properties button. The selected property appears in the Selected Properties control, and the Description for control updates to display the LabVIEW description associated with the property. You can also click the LabVIEW VI Help button to launch the associated LabVIEW Help topic. Depending on the property, you can change the direction of the property to in or out, or you can use the default (reset) value.
7. Click OK to create a VI configured with a Property Node using the specified I/O reference and properties.
8. Close the Configure Property Node dialog box.
9. Save the sequence file.

Note

- You must have LabVIEW 2013 or later to configure and call LabVIEW Property Nodes in TestStand.
- Depending on the hardware configuration on the computer, the Configure Property Node dialog box might list several different Property Node types.
- In LabVIEW, you must configure properties for LabVIEW classes to appear in Property Nodes so that you can select the properties in the Configure Property Node dialog box.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Calling LabVIEW VIs
- Getting Started with TestStand
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=calling-labview-vis.html language=enus -->
## TOPIC 00136: Calling LabVIEW VIs

- bundle_id: `teststand`
- source_path: `calling-labview-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-labview-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the LabVIEW Adapter to call VIs from TestStand, to create new LabVIEW projects and VIs to call from TestStand, to edit and debug existing VIs, and to use LabVIEW data types in TestStand. Completed solution files are located in the <TestStand Public>\Tutorial\Solution directory. Required LabVIEW

### Calling LabVIEW VIs

Use the LabVIEW Adapter to call VIs from TestStand, to create new LabVIEW projects and VIs to call from TestStand, to edit and debug existing VIs, and to use LabVIEW data types in TestStand.

Note

<TestStand Public>\Tutorial\Solution

#### Required LabVIEW Settings

All of the tutorials on this page require you to have the LabVIEW development system and TestStand installed on the same computer. In addition, you must configure the LabVIEW Adapter to run VIs using the LabVIEW development system.

Confirm the following settings in LabVIEW:

- To edit or run a VI from TestStand, you must include the VI in the VI Server: Exported VIs list in LabVIEW. By default, LabVIEW allows access to all VIs. Select Tools»Options to launch the Options dialog box. Select the VI Server category and browse to the Exported VIs section.
- Confirm that "*" is included in the VI Server: Exported VIs list and that the Allow Access option is enabled.

#### Creating and Configuring Steps with the LabVIEW Adapter

You can create steps that call stand-alone VIs, call VIs in the context of a LabVIEW project, and call LabVIEW class member VIs.

#### Calling a Stand-alone VI

Complete the following steps to insert a new LabVIEW step and configure the step to call a stand-alone VI.

1. Select File»New»Sequence File to open a new sequence file.
2. Save the sequence file as Call LabVIEW VI.seq in the <TestStand Public>\Tutorial directory.
3. Select the LabVIEW adapter from the Adapter ring control above the Step Types list.
4. Insert a Pass/Fail Test step in the Main step group and rename the new step LabVIEW Pass/Fail Test .
5. On the LabVIEW Module tab of the Step Settings pane, click the Browse for VI button located to the right of the VI Path control, navigate to <TestStand Public>\Tutorial\LabVIEW Pass-Fail Test.vi , and click Open . TestStand reads the description and connector pane information from the VI and updates the LabVIEW Module tab so you can configure the data to pass to and from the VI.
6. In the VI Parameter Table, enter the values shown in Table 11-1. Parameter NameValuePASS/FAIL FlagStep.Result.PassFailReport TextStep.Result.ReportText When TestStand calls the VI, it places the value the VI returns in the
 PASS/FAIL Flag and Report Text indicators into the
 Result.PassFail and Result.ReportText 
 properties of the step, respectively. Notice that TestStand automatically fills
 in the Value column of the error out output parameter
 with the Step.Result.Error property. By default, when a VI uses
 the standard LabVIEW error out cluster as an output
 parameter, TestStand automatically passes that value into the
 Step.Result.Error property for the step. You can also
 update the value manually. If an error occurs during execution of the VI and the
 error out cluster is passed to
 Step.Result.Error , TestStand launches the Run-Time Error
 dialog box by default.
7. Save the changes. Leave the sequence file open for the next tutorial.

#### Calling a VI in the Context of a LabVIEW Project

Complete the following steps to insert a new LabVIEW step and configure the step to call a VI in the context of a LabVIEW project.

1. Insert another Pass/Fail Test step in the Main step group and rename the new step LabVIEW Project Pass/Fail Test .
2. On the LabVIEW Module tab, click the Browse for LabVIEW Project button located to the right of the Project Path control, navigate to <TestStand Public>\Tutorial\Test Project.lvproj , and click Open . Notice that some of the TestStand button icons and tool tips change to indicate support for LabVIEW projects.
3. Click the Browse for VI in LabVIEW Project button, located to the right of the VI Path control, to launch the Select VI from LabVIEW Project dialog box.
4. Select LabVIEW ProjectPass-Fail Test.vi and click OK . Notice that the path defined in the project is selected as the VI path.
5. In the VI Parameter Table, enter the values shown in Table 11-2. Parameter NameValuePASS/FAIL FlagStep.Result.PassFailReport TextStep.Result.ReportText
6. Save the changes. Leave the sequence file open for the next tutorial.

#### Calling LabVIEW Class Member VIs

Complete the following steps to insert two new LabVIEW steps, configure the first step to call a static member VI from a LabVIEW class to create a LabVIEW class object, and configure the second step to call a dynamically dispatched member method VI on the created object.

Note

#### Calling a Static Member VI from a LabVIEW Class

Complete the following steps to insert a new LabVIEW step and configure the step to call a static member VI from a LabVIEW class in order to create a LabVIEW class object.

1. Insert an Action step in the Main step group and rename the new step Create LabVIEW Class Object .
2. On the LabVIEW Module tab, select Class Member Call from the Call Type ring control. Notice that some of the TestStand button icons and tool tips change to indicate support for LabVIEW class member calls.
3. Click the Browse for LabVIEW Project button, navigate to <TestStand Public>\Tutorial\Test Project.lvproj , and click Open .
4. Click the Browse for LabVIEW Class in LabVIEW Project button, located to the right of the Class Path control, to launch the Select a Class from LabVIEW Project dialog box.
5. Select LabVIEW Child Class.lvclass and click OK .
6. Select LabVIEW Child Static Factory Member.vi from the Member Name ring control.
7. In the VI Parameter Table, enter Locals.myChildObject in the Value column of the LabVIEW Child Class out output parameter. The myChildObject local variable name appears in red text because it does not exist yet. You create this variable in the next step.
8. Right-click the Locals.myChildObject value and select Create Locals.myChildObject»Object Reference from the context menu to create Locals.myChildObject as an object reference local variable, which appears on the Variables pane.
9. Save the changes. Leave the sequence file open for the next tutorial.

#### Calling a Dynamically Dispatched Member Method VI

Complete the following steps to insert a new LabVIEW step and configure the step to call a dynamically dispatched member method VI on the LabVIEW class object that the Create LabVIEW Class Object step creates.

1. Insert another Pass/Fail Test step in the Main step group and rename the new step LabVIEW Class Member Pass/Fail Test .
2. On the LabVIEW Module tab, select Class Member Call from the Call Type ring control.
3. Click the Browse for LabVIEW Project button, navigate to <TestStand Public>\Tutorial\Test Project.lvproj , and click Open .
4. Click the Browse for LabVIEW Class in LabVIEW Project button to launch the Select a Class from LabVIEW Project dialog box.
5. Select LabVIEW Parent Class.lvclass and click OK.
6. Select LabVIEW Dynamic Pass-Fail Test Member.vi from the Member Name ring control.
7. In the VI Parameter table, enter the values shown in Table 11-3. Parameter NameValueLabVIEW Parent Class inLocals.myChildObjectLabVIEW Parent Class outLocals.myChildObjectPASS/FAIL FlagStep.Result.PassFailReport TextStep.Result.ReportText
8. Save the changes. Leave the sequence file open for the next tutorial.

#### Executing the Sequence

Complete the following steps to execute the sequence of steps.

1. Select Execute»Single Pass . When the execution completes, the report indicates the steps passed.
2. Close the Execution window. Leave the sequence file open for the next tutorial.

Note

#### Creating and Editing VIs

You can use the LabVIEW Adapter to create a new VI from TestStand, create a new LabVIEW project and add a new VI to the project from TestStand, and edit an existing VI from TestStand.

#### Creating a New VI from TestStand

Complete the following steps to create a new VI from TestStand.

1. Select File»Save <filename> As and save the sequence file as Call LabVIEW VI 2.seq in the <TestStand Public>\Tutorial directory.
2. Insert a Numeric Limit Test step after the LabVIEW Class Member Pass/Fail Test step and rename the new step LabVIEW Numeric Limit Test .
3. On the LabVIEW Module tab, complete the following steps to configure the LabVIEW Numeric Limit Test step.
  1. Click the Create VI button, located to the right of the VI Path control, to create a new VI.
  2. In the File dialog box, browse to the <TestStand Public>\Tutorial directory, enter LabVIEW Numeric Limit Test.vi in the File Name control, and click OK . TestStand creates a new VI based on the available code templates for the TestStand Numeric Limit Test and opens the VI in LabVIEW. Note The TestStand Numeric Limit Test step type requires code modules to store a measurement value in the Step.Result.Numeric property, and the step type performs a comparison operation to determine whether the step passes or fails. Code modules can pass step properties as parameters to and from the code module or use the TestStand API in the code module to update step properties. When you use a default code template from NI to create a code module, TestStand creates the parameters needed to access the step properties for you.
  3. In LabVIEW, select Window»Show Block Diagram to open the block diagram.
  4. Right-click the Numeric Measurement indicator terminal, select Create»Constant from the context menu, and enter 10.0 .
  5. Save and close the VI.
4. In TestStand, click the LabVIEW Module tab. Notice that TestStand automatically updates the output parameters for the VI based on the information stored in the code template for the Numeric Limit Test step type.
5. Save the changes and select Execute»Single Pass . When the execution completes, the report indicates the step passed with a numeric measurement of 10 .
6. Close the Execution window. Leave the sequence file open for the next tutorial.

#### Creating a New LabVIEW Project and Adding a New VI to the Project from TestStand

Complete the following steps to create a new LabVIEW project and add a new VI to that project from TestStand.

1. Insert another Numeric Limit Test step after the LabVIEW Numeric Limit Test step and rename the new step LabVIEW Project Numeric Limit Test .
2. On the LabVIEW Module tab, complete the following steps to configure the LabVIEW Project Numeric Limit Test step.
  1. Click the Create LabVIEW Project button, located to the right of the Project Path control, to create a new LabVIEW Project.
  2. In the File dialog box, browse to the <TestStand Public>\Tutorial directory, enter LabVIEW Project Test.lvproj in the File Name control, and click OK . TestStand creates a new LabVIEW Project and opens the project in LabVIEW.
  3. In TestStand, click the Add or Remove VIs from LabVIEW Project button, located to the right of the VI Path control, to launch the Add or Remove Items from LabVIEW Project dialog box.
  4. Right-click the My Computer item in the LabVIEW Project control and select New VI from the context menu to launch the Select the LabVIEW VI to Create dialog box.
  5. In the Select LabVIEW VI to Create dialog box, browse to the <TestStand Public>\Tutorial directory, enter LabVIEW Project Numeric Limit Test.vi in the File Name control, and click OK . TestStand creates a new VI based on the available code templates for the TestStand Numeric Limit Test step type and adds the VI to the LabVIEW project.
  6. Right-click the new VI under the My Computer item and select Edit VI from the context menu. TestStand opens the VI in LabVIEW within the project context, which LabVIEW displays in the bottom left corner of the front panel.
  7. In LabVIEW, open the block diagram for the VI.
  8. Right-click the Numeric Measurement indicator terminal, select Create»Constant from the context menu, and enter 10.0 .
  9. Save and close the VI.
3. In TestStand, select LabVIEW Project Numeric Limit Test.vi in the Add or Remove Items from the LabVIEW Project dialog box, and click Select to close the Add or Remove Items from LabVIEW Project dialog box. On the LabVIEW Module tab, notice that TestStand automatically updates the output parameters for the VI based on the information stored in the code template for the Numeric Limit step type.
4. Save the changes and select Execute»Single Pass . When the execution completes, the report indicates the steps passed with a numeric measurement of 10.0 .
5. Close the Execution window. Leave the sequence file open for the next tutorial.

#### Editing Existing VIs from TestStand

Complete the following steps to edit existing VIs from TestStand.

1. Select the LabVIEW Pass/Fail Test step and use the LabVIEW Module tab to complete the following steps.
  1. Click the Edit VI button, located to the right of the VI Path control. LabVIEW becomes the active application in which the LabVIEW Pass-Fail Test VI is open.
  2. Open the block diagram for the VI and change the PASS/FAIL Flag Boolean constant to False .
  3. Save and close the VI.
2. In TestStand, select the LabVIEW Project Pass/Fail Test step and use the LabVIEW Module tab to complete the following steps.
  1. Click the Edit VI button. LabVIEW becomes the active application and the LabVIEW Project Pass-Fail Test VI is open within the LabVIEW project context.
  2. Open the block diagram for the VI and change the PASS/FAIL Flag Boolean constant to False .
  3. Save and close the VI.
3. In TestStand, save the changes and select Execute»Single Pass . When the execution completes, the report indicates the LabVIEW Pass/Fail Test and LabVIEW Project Pass/Fail Test steps failed.
4. Close the Execution window. Leave the sequence file open for the next tutorial.

#### Debugging VIs

Complete the following steps to debug VIs you call from TestStand using the LabVIEW Adapter.

1. Place a breakpoint at the LabVIEW Pass/Fail Test step.
2. Select Execute»Run MainSequence . The execution pauses at the LabVIEW Pass/Fail Test step.
3. Complete the following steps to debug the LabVIEW Pass-Fail Test VI the LabVIEW Pass/Fail Test step calls.
  1. Click the Step Into button at the top of the Execution window. LabVIEW becomes the active application, in which the LabVIEW Pass-Fail Test VI is open and in a suspended state.
  2. Open the block diagram of the suspended VI.
  3. Click the Step Into or Step Over button on the LabVIEW toolbar to begin stepping through the VI. You can click the Finish VI button at any time to finish stepping through the VI.
  4. When you finish stepping through the VI, click the Return to Caller button on the LabVIEW toolbar to return to TestStand. The execution pauses at the next step in the sequence.
4. Click the Resume button on the Debug toolbar in TestStand to complete the execution.
5. Close the Execution window.
6. Remove the breakpoint from the LabVIEW Pass/Fail Test step. Leave the sequence file open for the next tutorial.

#### Creating TestStand Data Types from
 LabVIEW Clusters

TestStand provides number, string, Boolean, and object
 reference built-in data types. TestStand also provides several standard named data
 types, including Path, Error, LabVIEWAnalogWaveform, and others. You can create
 container data types to hold any number of other data types. TestStand container
 data types are analogous to LabVIEW clusters.

Complete the following steps to
 create a TestStand data type that matches a LabVIEW cluster.

1. Select File»Save <filename> As 
 and save the sequence file as Call LabVIEW VI 3.seq in the
 <TestStand Public>\Tutorial directory.
2. Insert a Pass/Fail Test step in the Main step group after the LabVIEW Project
 Numeric Limit Test step and rename the new step Pass Container to
 VI .
3. On the LabVIEW Module tab, click the Browse for VI 
 button, navigate to <TestStand Public>\Tutorial\VI with Cluster
 Input.vi , and click Open .
4. Click the Create/Update Custom Data Type button, located
 in the Type column of the Input Cluster parameter in the
 VI Parameter Table, to launch the Create/Update Custom Data Type From Cluster
 dialog box. TestStand maps the cluster elements to subproperties in a container
 called Input_Cluster, which is a new TestStand custom data type. You can rename
 the data type and subproperties as necessary and specify where TestStand stores
 the new data type.
5. In the Create/Update Custom Data Type From Cluster dialog box, change the type
 name to InputData and click the Create 
 button to accept the automatically assigned values and to create the data type
 in the current sequence file.
6. On the LabVIEW Module tab, remove the checkmark from the Default column for the
 Input Cluster input parameter, click the
 Expression Browse button in the Value column to
 launch the Expression Browser dialog box, and complete the following steps.
  1. On the Variables/Properties tab, right-click the
 Locals item and select Insert
 Types»InputData to create a local variable of the
 InputData data type. Rename the local variable
 ContainerData .
  2. Right-click the Number subproperty of
 ContainerData and select
 Properties from the context menu to launch
 the Number Properties dialog box.
  3. Enter 23 in the Value control and click
 OK .
  4. Right-click the String subproperty of
 ContainerData and select
 Properties from the context menu to launch
 the String Properties dialog box.
  5. Enter My String Data in the Value control and click
 OK .
  6. Enter Locals.ContainerData in the
 Expression control on the
 Variables/Properties tab and click OK . The Value
 column for the Input Cluster parameter now
 contains Locals.ContainerData .
7. Enter Step.Result.ReportText in the
 Value column for the Report
 Text output parameter. When TestStand calls the VI, it passes
 the values in the ContainerData local variable to the
 Input Cluster control on the VI and returns the
 Number and String elements of
 the Input Cluster parameter to the ReportText property of
 the step.
8. Save the changes and select Execute»Single Pass . When the
 execution completes, the report shows the text the VI with Cluster Input VI
 returns.
9. Close all the windows in the sequence editor.

Parent topic:

Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=calling-labwindows-cvi-code-modules.html language=enus -->
## TOPIC 00137: Calling LabWindows/CVI Code Modules

- bundle_id: `teststand`
- source_path: `calling-labwindows-cvi-code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-labwindows-cvi-code-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the LabWindows/CVI Adapter to call LabWindows/CVI code modules from TestStand, to create new code modules to call from TestStand, to edit and debug existing code modules, and to use LabWindows/CVI data types in TestStand. Completed solution files are located in the <TestStand Public>\Tutorial\So

### Calling LabWindows/CVI Code Modules

Use the LabWindows/CVI Adapter to call LabWindows/CVI code modules from TestStand, to create new code modules to call from TestStand, to edit and debug existing code modules, and to use LabWindows/CVI data types in TestStand.

Note

<TestStand Public>\Tutorial\Solution

#### Required LabWindows/CVI Settings

All of the tutorials on this page require you to have the LabWindows/CVI development system and TestStand installed on the same computer.

In addition, complete the following steps to configure the LabWindows/CVI Adapter to execute steps in an external instance of the LabWindows/CVI development system and to allow only new code templates.

1. Select Configure»Adapters to launch the Adapter Configuration dialog box.
2. Select LabWindows/CVI in the Adapter column and click the Configure button to launch the LabWindows/CVI Adapter Configuration dialog box.
3. In the Step Execution section, select the Execute Steps in an External Instance of CVI option.
4. In the Code Template Policy section, select the Allow Only New Templates option.
5. Click OK to close the LabWindows/CVI Adapter Configuration dialog box, click OK again when the adapter displays a warning that confirms TestStand will unload all modules, and click Done in the Adapter Configuration dialog box.

#### Creating and Configuring Steps with the LabWindows/CVI Adapter

Complete the following steps to insert a new step that uses the LabWindows/CVI Adapter and configure the step to call a code module.

1. Select File»New»Sequence File to open a new sequence file.
2. Save the sequence file as CallCVICodeModule.seq in the <TestStand Public>\Tutorial directory.
3. Select the LabWindows/CVI adapter from the Adapter ring control above the Step Types list.
4. Insert a Pass/Fail Test step in the Main step group and rename the new step CVI Pass/Fail Test .
5. On the LabWindows/CVI Module tab of the Step Settings pane, click the File Browse button located to the right of the Module control, navigate to <TestStand Public>\Tutorial\CallCVICodeModule.dll , and click Open .
6. Select PassFailTest from the Function ring control. Note When you select a function, the LabWindows/CVI Adapter attempts to read the export information LabWindows/CVI includes in the DLL or the function parameter information from the type library in the code module, if one exists. When the function parameter information is not defined, you can select a code template from the Code Template ring control to specify the function prototype or add parameters to the Parameters Table control to specify the function prototype.
7. Select PassFail template for LabWindows/CVI from the Code Template ring control. The Parameters Table control contains the default value expressions the code template specifies. When TestStand calls the code module, the LabWindows/CVI Adapter stores the returned values for the result and the error details in the specified properties of the step.
8. Save the changes and select Execute»Single Pass . Because the LabWindows/CVI Adapter is configured to use an external instance of LabWindows/CVI to execute code modules, TestStand launches the LabWindows/CVI development environment to execute the function the step calls. When the execution completes, the report indicates the step passed.
9. Select File»Unload All Modules to unload the DLL the step calls so you can rebuild the DLL in a subsequent tutorial.
10. Close the Execution window. Leave the sequence file open for the next tutorial.

#### Creating a New Code Module from TestStand

Note

Complete the following steps to create a new code module from TestStand.

1. Select File»Save <filename> As and save the sequence file as CallCVICodeModule2.seq in the <TestStand Public>\Tutorial directory.
2. Insert a Numeric Limit Test step after the CVI Pass/Fail Test step and rename the new step CVI Numeric Limit Test .
3. On the LabWindows/CVI Module tab, complete the following steps to configure the CVI Numeric Limit Test step.
  1. Click the File Browse button, navigate to <TestStand Public>\Tutorial\CallCVICodeModule.dll , and click Open .
  2. Enter NumericLimitTest in the Function ring control.
  3. Select NumericLimit template for LabWindows/CVI from the Code Template ring control. Notice that TestStand automatically updates the function prototype and parameter values based on the information stored in the code template for the Numeric Limit Test step type.
4. Click the Source Code Files button, located to the right of the Parameter Details Table control, to launch the CVI Source Code Files window and complete the following steps.
  1. Enter CVINumericLimitTest.c in the Source File Containing Function control.
  2. For the CVI Project File to Open control, click the File Browse button, navigate to <TestStand Public>\Tutorial\CallCVICodeModule.prj , and click Open .
  3. Click Close .
5. Click the Create Code button, located just below the Source Code Files button, to create a code module. When you click the Create Code button, TestStand launches the Select a Source File dialog box, in which you can specify the source code to use for the code module.
6. Navigate to the <TestStand Public>\Tutorial directory and click OK . TestStand creates a new code module source file named CVINumericLimitTest.c based on the available code templates for the TestStand Numeric Limit Test step type and opens the code module in LabWindows/CVI. Note The TestStand Numeric Limit Test step type requires code modules to store a measurement value in the Step.Result.Numeric property, and the step type performs a comparison operation to determine whether the step passes or fails. Code modules can pass step properties as parameters to and from the code module or use the TestStand API in the code module to update step properties. When you use a default code template from NI to create a code module, TestStand creates the parameters needed to access the step properties for you.
7. In LabWindows/CVI, uncomment the following code in the source file: double testMeasurement = 10.0; double lowLimit; *measurement = testMeasurement;
8. Save and close the source file. Leave LabWindows/CVI open.
9. In the LabWindows/CVI project window, select Build»Create Debuggable Dynamic Link Library to rebuild the DLL. Click OK when LabWindows/CVI prompts you that the files are created.
10. In TestStand, save the changes and select Execute»Single Pass . When the execution completes, the report indicates the step passed with a numeric measurement of 10 .
11. Select File»Unload All Modules to unload the DLL.
12. Close the Execution window. Leave the sequence file and LabWindows/CVI open for the next tutorial.

#### Editing an Existing Code Module from TestStand

Complete the following steps to edit an existing code module from TestStand.

1. Select the CVI Numeric Limit Test step and use the LabWindows/CVI Module tab to complete the following steps.
  1. Click the Edit Code button, located just below the Create Code button. LabWindows/CVI becomes the active application in which the CVINumericLimitTest.c source file is open.
  2. Change the initial value in the declaration for the testMeasurement variable to 5.0 .
  3. Save and close the source file. Leave LabWindows/CVI open.
2. Rebuild the DLL. Click OK when LabWindows/CVI prompts you that the files are created.
3. In TestStand, select Execute»Single Pass . When the execution completes, the report indicates the step failed with a numeric measurement of 5 .
4. Close the Execution window. Leave the sequence file and LabWindows/CVI open for the next tutorial.

#### Debugging a Code Module

Complete the following steps to debug a code module you call from TestStand using the LabWindows/CVI Adapter.

1. Place a breakpoint at the CVI Pass/Fail Test step.
2. Select Execute»Run MainSequence . The execution pauses at the CVI Pass/Fail Test step.
3. Complete the following steps to debug the code module the CVI Pass/Fail Test step calls.
  1. Click the Step Into button on the Debug toolbar in TestStand. LabWindows/CVI becomes the active application, in which the LabWindows/CVI Pass-Fail Test code module is open and in a suspended state.
  2. Click the Step Into button or the Step Over button on the LabWindows/CVI toolbar to begin stepping through the code module.
  3. When you finish stepping through the code module, click the Finish Function button on the LabWindows/CVI toolbar to return to TestStand. The execution pauses at the next step in the sequence.
4. Click the Resume button on the Debug toolbar in TestStand to complete the execution.
5. Close the Execution window.
6. Select File»Unload All Modules to unload the DLL.
7. Remove the breakpoint from the CVI Pass/Fail Test step. Leave the sequence file and LabWindows/CVI open for the next tutorial.

#### Creating TestStand Data Types from LabWindows/CVI Structs

TestStand provides number, string, Boolean, and object reference built-in data types. TestStand also provides several standard named data types, including Path and Error. You can create container data types to hold any number of other data types. TestStand container data types are analogous to C structures in LabWindows/CVI.

Complete the following steps to create a TestStand data type that matches a LabWindows/CVI struct and call a function in a DLL that has the struct as a parameter.

#### Creating a New Custom Data Type

Complete the following steps to create a new container data type that contains numeric and string subproperties.

1. Click the Types button on the sequence editor toolbar to open the Types window.
2. Select the CallCVICodeModule2.seq sequence file on the View Types For pane.
3. Right-click the Custom Data Types item and select Insert Custom Data Type»Container from the context menu to insert a new data type. Rename the new container data type CVITutorialStruct .
4. Expand the CVITutorialStruct item.
5. Right-click the CVITutorialStruct item and select Insert Field»Number from the context menu to insert a new field in the data type. Rename the new field Measurement .
6. Right-click the CVITutorialStruct item and select Insert Field»String from the context menu to insert another new field in the CVITutorialStruct container data type. Rename the new field Buffer .
7. Save the changes. If TestStand warns you that the sequence file contains modified types, review the information in the warning dialog box, select the Increment Type Versions option, and click OK . Leave the sequence file open for the next tutorial.

#### Specifying Structure Passing Settings

Complete the following steps to specify the structure passing properties for the CVITutorialStruct container data type.

1. Right-click the CVITutorialStruct item in the Types window and select Properties from the context menu to launch the Type Properties dialog box. The name of the Type Properties dialog box is specific to the name of the property you select.
2. Click the C Struct Passing tab of the Type Properties dialog box.
3. Enable the Allow Objects of This Type to be Passed as Structs option. The Property ring control lists the two fields in the CVITutorialStruct container data type. Notice that the Numeric Type control for the Measurement property defaults to 64-bit Real Number (double).
4. Select the Buffer property from the Property ring control.
5. For the String Type control, select the C String Buffer option to allow the C function to alter the value of the structure field.
6. Click the Version tab of the Type Properties dialog box and disable the Modified option.
7. Select OK to close the Type Properties dialog box.
8. Save the changes. Close the Types window. Leave the sequence file open for the next tutorial.

#### Calling a Function with a Struct
 Parameter

Complete the following steps to use the
 CVITutorialStruct container data type as a parameter to a
 function a step calls.

1. Select File»Save <filename> As 
 and save the sequence file as CallCVIModule3.seq in the
 <TestStand Public>\Tutorial directory.
2. Click the Variables pane.
3. Right-click the Locals item, select Insert
 Local»Type»CVITutorialStruct from the context menu to insert an
 instance of the container data type, and rename the new variable
 CVIStruct .
4. Insert an Action step into the Main step group after the CVI Numeric Limit Test
 step and rename the new step Pass Struct Test .
5. On the LabWindows/CVI Module tab, click the File Browse 
 button, navigate to <TestStand
 Public>\Tutorial\CallCVICodeModule.dll , and click
 Open .
6. Enter PassStructTest in the Function control.
7. Click the Add Parameter button, located to the right of
 the Parameters Table control, to insert a new parameter in the Parameters Table
 control.
8. Enter the following information in the Parameter Details Table control:
  1. In the Name field, rename the parameter
 cviStruct .
  2. In the Category field, select C
 Struct .
  3. In the Type field, select
 CVITutorialStruct .
9. Enter Locals.CVIStruct in the Value Expression column for the
 parameter in the Parameters Table control.
10. Click the Source Code Files button to launch the CVI
 Source Code Files window. Complete the following steps to select the source file
 and project file to use when inserting the function.
  1. Enter CVIStructPassingTest.c in the Source File
 Containing Function control.
  2. For the CVI Project File to Open control, click the File
 Browse button, navigate to <TestStand
 Public>\Tutorial\CallCVICodeModule.prj , and click
 Open .
  3. Click Close .
11. Click the Create Code button to create a code module.
 TestStand launches the Select a Source File dialog box.
12. Browse to the <TestStand Public>\Tutorial directory and
 click OK . TestStand creates a new source file named
 CVIStructPassingTest.c with an empty function.
13. In LabWindows/CVI, complete the following steps.
  1. Add the following type definition before the
 PassStructTest function:
 struct CVITutorialStruct { double measurement; char buffer[256]; };
  2. Add the following code to the PassStructTest function:
 if (cviStruct) { cviStruct->measurement = 10.0; strcpy(cviStruct->buffer, "Average Voltage"); }
  3. Add the following statement to the top of the source file to include
 the declaration of the strcpy function:
 #include <ansi_c.h>
14. Save and close the source file.
15. In the LabWindows/CVI project window, select Build»Create Debuggable
 Dynamic Link Library to rebuild the DLL. Click
 OK when LabWindows/CVI notifies you that the files
 are created.
16. In TestStand, place a breakpoint at the new Pass Struct Test step.
17. Save the changes and select Execute»Run MainSequence .
18. Step through the sequence and review the values in the
 Locals.CVIStructvariable on the Variables pane of the
 Execution window before and after executing the Pass Struct Test step.
19. Select File»Unload All Modules to unload the DLL.
20. Remove the breakpoint from the CVI Pass/Fail Test step. Close all the windows in
 the sequence editor.

Parent topic:

Getting Started with TestStand

Related concepts:

- Calling LabVIEW VIs

<!--NI_TOPIC bundle=teststand path=calling-legacy-labview-code-modules.html language=enus -->
## TOPIC 00138: Legacy Configurations for LabVIEW Code Modules in TestStand

- bundle_id: `teststand`
- source_path: `calling-legacy-labview-code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-legacy-labview-code-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In versions of TestStand earlier than 3.0, you could call VIs only with a specific set of controls and indicators. Using TestStand 3.0 or later, you can call VIs with a variety of connector panes, including VIs with legacy configurations. All legacy-style VIs must include the Test Data cluster and e

### Legacy Configurations for LabVIEW Code Modules
 in TestStand

In versions of TestStand earlier than 3.0, you could call VIs only with a specific set of controls and indicators. Using TestStand 3.0 or later, you can call VIs with a variety of connector panes, including VIs with legacy configurations.

All legacy-style VIs must include the Test Data cluster and error out cluster indicators. The Input Buffer, Invocation Info, and Sequence Context controls are optional inputs to legacy VIs, which can contain any combination of these controls.

You must assign each control and indicator of the test VI to a terminal on the connector pane of the test VI. If these assignments do not exist, TestStand returns an error when it attempts to call the test VI. TestStand does not require that you use a particular connector pane pattern, and it does not require that you assign the controls and indicators to specific terminals.

Although you usually create new VIs using the LabVIEW Module tab for steps that use the LabVIEW Adapter, you can configure the LabVIEW Adapter to create legacy-style VIs.

You can use the following methods to pass data between the code module and TestStand:

- Use the Test Data cluster
- Use the sequence context ActiveX reference to call the TestStand ActiveX API functions to set the variables used to store the results of the test, such as Step.Result.PassFail

Note

Test Data

Test Data

Test Data

Step.Result.PassFail

Test Data

Step.Result.ReportText

Parent topic:

LabVIEW Adapter

Related concepts:

- TestStand ActiveX API Overview

Related information:

- LabVIEW Adapter Configuration Dialog Box
- Legacy VI Settings Dialog Box

<!--NI_TOPIC bundle=teststand path=calling-legacy-labwindows-cvi-code-modules.html language=enus -->
## TOPIC 00139: Calling Legacy LabWindows/CVI Code Modules

- bundle_id: `teststand`
- source_path: `calling-legacy-labwindows-cvi-code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-legacy-labwindows-cvi-code-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Versions of TestStand earlier than 3.0 required the DLL Flexible Prototype Adapter to call functions in LabWindows/CVI DLLs that did not use a specific prototype. Using TestStand 3.0 or later, you can call functions with a variety of parameter data types, including code modules with legacy function

### Calling Legacy LabWindows/CVI Code Modules

Versions of TestStand earlier than 3.0 required the DLL Flexible Prototype Adapter to call functions in LabWindows/CVI DLLs that did not use a specific prototype. Using TestStand 3.0 or later, you can call functions with a variety of parameter data types, including code modules with legacy function prototypes.

#### Prototypes of Legacy LabWindows/CVI Code Modules

TestStand supports the following legacy prototypes:

- Standard legacy prototype:
 void TX_TEST StandardFunc(tTestData *data, tTestError *error)
- Extended legacy prototype:
 int TX_TEST ExtendedFunc(const char *params, tTestData *data, tTestError *error)

In earlier versions of TestStand, National Instruments recommended using the standard prototype. The extended prototype provides compatibility with the LabWindows/CVI Test Executive Toolkit version 2.0 or earlier and offers an additional string parameter.

Although you usually create new code modules using the LabWindows/CVI Module tab for steps that use the LabWindows/CVI Adapter, TestStand can also create legacy-style code modules.

The legacy prototypes contain the tTestData and tTestError structure parameters, which the LabWindows/CVI Adapter uses to pass values into and out of the code module.

- [Updating Step Properties](updating-step-properties.html)
- [Example Legacy LabWindows/CVI Code Module](example-legacy-labwindows-cvi-code-module.html)

Parent topic:

LabWindows/CVI Adapter

<!--NI_TOPIC bundle=teststand path=calling-sequences-dynamically.html language=enus -->
## TOPIC 00140: Calling Sequences Dynamically

- bundle_id: `teststand`
- source_path: `calling-sequences-dynamically.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-sequences-dynamically.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add to a sequence a step that dynamically runs one of two sequences, and you can pass parameters to the sequence you call. Completed solution files are located in the <TestStand Public>\Tutorial\Solution directory. Dynamically Specifying a Sequence to Run Complete the following steps to open

### Calling Sequences Dynamically

You can add to a sequence a step that dynamically runs one of two sequences, and you can pass parameters to the sequence you call.

Note

<TestStand Public>\Tutorial\Solution

#### Dynamically Specifying a Sequence to Run

Complete the following steps to open an existing sequence, add steps to prompt the operator for a CPU type and the number of CPUs to test, and add a step to call one of two different sequences depending on the type of CPU the user specifies.

1. Open <TestStand Public>\Tutorial\Computer.seq .
2. Select File»Save <filename> As and save the sequence as Computer6.seq in the <TestStand Public>\Tutorial directory.
3. Click the Variables pane in the Sequence File window, right-click the Locals item, select Insert Local»String from the context menu, and name the local variable CPUType .
4. Click the Steps pane in the Sequence File window to show the steps in the MainSequence .
5. Insert a Message Popup step below the Power On step, rename the new step Select CPU Type , and complete the following steps to configure the Select CPU Type step.
  1. On the Text and Buttons tab of the Step Settings pane, enter the following values in the corresponding controls:
    - Message Expression — "Please select the CPU type for the UUT."
    - Button 1 — "INTEL CPU"
    - Button 2 — "AMD CPU"
    - Cancel Button — None
  2. On the Layout tab of the Step Settings pane, enable the Make Modal option in the Dialog Options section. Enabling this option prevents the sequence editor from hiding the Select CPU dialog box and prevents you from interacting with the sequence editor until you close the Select CPU dialog box.
  3. On the Properties tab of the Step Settings pane, click Expressions to show the Expressions panel.
  4. In the Post-Expression control, enter the following expression to assign the string value "AMD" or "INTEL" to the local variable depending on the button users click: Locals.CPUType = ((Step.Result.ButtonHit == 2) ? "AMD" : "INTEL") Click the Check Expression for Errors button to verify that the expression contains valid syntax.
6. On the Steps pane, insert a Message Popup step below the Select CPU Type step, rename the new step Specify Number of CPUs , and complete the following steps to configure the Specify Number of CPUs step.
  1. On the Text and Buttons tab of the Step Settings pane, enter the following values in the corresponding controls:
    - Message Expression — "Please select the number of CPUs installed for the UUT."
    - Button 1 — "1"
    - Button 2 — "2"
    - Button 3 — "3"
    - Button 4 — "4"
    - Cancel Button — None
  2. On the Layout tab of the Step Settings pane, enable the Make Modal option in the Dialog Options section.
7. Insert a Sequence Call step below the Specify Number of CPUs step, rename the step CPU Test , and complete the following steps to configure the CPU Test step.
  1. On the Module tab of the Step Settings pane, enable the Specify By Expression option.
  2. Enter Locals.CPUType + "Processor.seq" in the File Path or Reference control and "MainSequence" in the Sequence control.
  3. Click the Load Prototype button to launch the Load Sequence Prototype dialog box, in which you can select the prototype for the Sequence Call step.
  4. Click the Browse button in the Load Sequence Prototype dialog box and select <TestStand Public>\Tutorial\AMDProcessor.seq .
  5. Click OK to close the Load Sequence Prototype dialog box. TestStand populates the Parameters Table on the Module tab with the parameter list for the sequence.
  6. Click in the Value column of the CPUsInstalled parameter and enter the following expression: RunState.Sequence.Main["Specify Number of CPUs"].Result.ButtonHit Click the Check Expression for Errors button to verify that the expression contains valid syntax.
8. Save the changes. Leave the sequence file open for the next tutorial.

#### Running a Sequence
 Dynamically

Complete the following steps to run a sequence
 dynamically.

1. Place a breakpoint at the CPU Test step.
2. Select Execute»Single Pass .
3. Click Done in the Test Simulator dialog box.
4. Click the INTEL CPU button in the Select CPU Type dialog
 box and click the 2 button in the Specify Number of CPUs
 dialog box.
5. When execution suspends at the breakpoint on the CPU Test step, click the
 Step Into button on the Execution window toolbar to
 step into the MainSequence sequence in
 INTELProcessor.seq .
6. Click the Call Stack pane. The call stack list shows
 INTELProcessor.seq at the top of the sequence call
 stack.
7. Click the tab for the Variables pane of the Execution window and expand the
 Parameters item. The value of the CPUsInstalled
 parameter equals the value on the button you clicked in the Specify Number of
 CPUs dialog box. The MainSequence sequence in the
 INTELProcessor.seq sequence file also requires a ModelName
 parameter. The Sequence Call step you created did not specify the ModelName
 parameter, so the TestStand Engine initializes the parameter to the default
 name.
8. Click the tab for the Steps pane of the Execution window and click the
 Resume button on the Execution window toolbar. When
 the execution completes, review the report but do not close the Execution
 window.
9. Click the Restart button on the Execution window toolbar
 to restart the execution and click Done in the Test
 Simulator dialog box. The Execution window must be the active window to restart
 the execution.
10. Click the AMD CPU button in the Select CPU Type dialog
 box and click the 3 button in the Specify Number of CPUs
 dialog box.
11. When the execution suspends at the breakpoint on the CPU Test step, step into
 the MainSequence sequence in AMDProcessor.seq .
 The Call Stack pane lists AMDProcessor.seq at the top of the
 call stack.
12. Resume and complete the execution and review the report.
13. Close all the windows in the sequence editor.

Parent topic:

Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=calling-vis-on-remote-computers.html language=enus -->
## TOPIC 00141: Calling VIs on Remote Computers

- bundle_id: `teststand`
- source_path: `calling-vis-on-remote-computers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-vis-on-remote-computers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can directly call VIs on remote computers, including computers that run the LabVIEW development system or a LabVIEW executable and PXI controllers that run the LabVIEW Real-Time Module. TestStand does not support automatically downloading VIs to systems that run the Real-Time Module. To use the

### Calling VIs on Remote Computers

You can directly call VIs on remote computers, including computers that run the LabVIEW development system or a LabVIEW executable and PXI controllers that run the LabVIEW Real-Time Module.

Note

Because TestStand uses the LabVIEW VI Server to run VIs remotely, the remote computers can use any operating system LabVIEW supports, including Linux and OS X.

Complete the following steps to call a VI remotely:

1. Configure the TestStand step to specify that the call occurs on a remote computer.
2. Configure the remote computer to allow TestStand to call VIs located on the computer.
3. Configure the computer running TestStand to have network access to the remote computer running the LabVIEW VI Server.

#### Using LabVIEW Class Data Type Parameters in Remote VI Calls

TestStand supports remote VI calls that use LabVIEW class data type parameters only when you preload the LabVIEW class definition in the same version of the LabVIEW Run-Time Engine as the LabVIEW version of the VI on the local computer. Otherwise, LabVIEW fails to interpret the returned LabVIEW class data because it is not loaded into LabVIEW.

Complete the following steps for every step you configure to make a remote VI call that uses LabVIEW class data type parameters to work around this issue.

1. Create another sequence in the same sequence file.
2. Copy all the steps and required variables into the new sequence.
3. For each step in the new sequence, click the Advanced Settings button on the LabVIEW Module tab of the Step Settings pane to launch the LabVIEW Advanced Settings window.
4. Disable the Run VI on a Remote Computer option and enable the Always Run VI in LabVIEW Run-Time Engine option.

Note

#### Calling Class Member VIs on Remote Machines

TestStand does not support remote Class Member calls.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Configuring a LabVIEW Step to Run Remotely
- Configuring the LabVIEW VI Server to Run VIs Remotely

<!--NI_TOPIC bundle=teststand path=calling-vis-that-create-activex-references.html language=enus -->
## TOPIC 00142: Calling VIs That Create ActiveX References

- bundle_id: `teststand`
- source_path: `calling-vis-that-create-activex-references.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-vis-that-create-activex-references.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW might seem to hang with 100% processor use when all of the following conditions are true: You call a LabVIEW VI that creates ActiveX references, such as calling the ApplicationMgr.GetEngine method directly. You configure the VI to use the same as caller execution system. You call the VI from

### Calling VIs That Create ActiveX References

LabVIEW might seem to hang with 100% processor use when all of the following conditions are true:

- You call a LabVIEW VI that creates ActiveX references, such as calling the ApplicationMgr.GetEngine method directly.
- You configure the VI to use the same as caller execution system.
- You call the VI from a sequence running in a single-threaded apartment thread.

Change the Preferred Execution System option in LabVIEW to a value different from same as caller to work around this issue.

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Evaluating Conditional Disable Structures and Symbols
- Calling VIs That Use XControls

<!--NI_TOPIC bundle=teststand path=calling-vis-that-use-xcontrols.html language=enus -->
## TOPIC 00143: Calling VIs That Use XControls

- bundle_id: `teststand`
- source_path: `calling-vis-that-use-xcontrols.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/calling-vis-that-use-xcontrols.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand supports calling VIs that use XControls on Microsoft Windows systems.

### Calling VIs That Use XControls

TestStand supports calling VIs that use XControls on Microsoft Windows systems.

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Calling VIs That Create ActiveX References
- Building a TestStand Deployment with LabVIEW

<!--NI_TOPIC bundle=teststand path=caption-connections.html language=enus -->
## TOPIC 00144: Caption Connections

- bundle_id: `teststand`
- source_path: `caption-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/caption-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Caption connections display text that describes the status of the application. For example, you can use the Application Manager control to connect a caption to a Label control so that the Label control displays the name of the currently logged-in user. The CaptionSources enumeration defines the set

### Caption Connections

Caption connections display text that describes the status of the application. For example, you can use the Application Manager control to connect a caption to a Label control so that the Label control displays the name of the currently logged-in user.

The CaptionSources enumeration defines the set of captions to which you can connect. Some captions apply to the selected item in the manager control with which you connect them. For example, the UUTSerialNumber caption displays the serial number of the current UUT for the execution an ExecutionView Manager control selects. Other captions, such as UserName, function the same regardless of which manager control you use to connect them.

Call the following methods to connect a caption to a Label control, an ExpressionEdit control, or a StatusBar pane:

- ApplicationMgr.ConnectCaption
- SequenceFileViewMgr.ConnectCaption
- ExecutionViewMgr.ConnectCaption

Call the following methods to obtain the text of a caption without connecting the caption to a control:

- ApplicationMgr.GetCaptionText
- SequenceFileViewMgr.GetCaptionText
- ExecutionViewMgr.GetCaptionText

Parent topic:

Information Source Connections

Related concepts:

- Application Manager
- Manager Controls
- ExecutionView Manager

<!--NI_TOPIC bundle=teststand path=caveats-for-configuring-the-labview-adapter-t.html language=enus -->
## TOPIC 00145: Caveats for Configuring the LabVIEW Adapter to Use a LabVIEW Run-Time Engine or Other Executable Server

- bundle_id: `teststand`
- source_path: `caveats-for-configuring-the-labview-adapter-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/caveats-for-configuring-the-labview-adapter-t.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you select LabVIEW Run-Time Engine or Other Executable as a server in the LabVIEW Adapter Configuration dialog box, you must ensure that the server can locate the complete hierarchy of VIs, including any subVIs, that TestStand executes. The version of the VIs that TestStand executes must match

### Caveats for Configuring the LabVIEW Adapter to Use a LabVIEW Run-Time Engine or Other Executable Server

Note

Auto detect using VI version

Adapters.cfg

When you use the TestStand Version Selector to activate a different version of TestStand, TestStand copies new versions of the VIs to the <LabVIEW>\vi.lib\addons\TestStand directory. If you select LabVIEW Run-Time Engine as the server on a development system, TestStand might report that it cannot load some VIs in the LabVIEW RTE, even though the VIs run successfully using the LabVIEW development system as the server, because TestStand cannot load a subVI that was saved in a different version of LabVIEW than the LabVIEW RTE specified in the LabVIEW Adapter Configuration dialog box. This discrepancy occurs most often when a top-level VI uses a subVI or controls located in the <LabVIEW>\vi.lib\addons\TestStand directory and that subVI was saved in a different version of LabVIEW than the LabVIEW RTE. Mass compiling the <LabVIEW>\vi.lib\addons\TestStand directory usually resolves the discrepancy. You can also mass compile top-level VIs, which in turn compiles any subVIs. Mass compile the VIs located in this directory after you activate the new version of TestStand.

This behavior can also occur in the following situations:

- When you try to run a VI you save in the <TestStand>\API directory and the <TestStand Public>\Examples directory
- When the directories contain VIs with the same names as the subVIs the VI uses
- When the VIs were saved with a different version of LabVIEW

Save VIs in a working directory instead of using the TestStand directories to work around this issue.

Normally, the LabVIEW RTE can execute top-level VIs only when you save the VI with the entire VI hierarchy or when the LabVIEW RTE can locate the subVIs using the LabVIEW search directories. By default, the LabVIEW RTE does not search for required subVIs within the LabVIEW development system, such as files in vi.lib. However, when TestStand loads a LabVIEW RTE on a computer where you also installed the LabVIEW development system, TestStand automatically adds directories from the development system to the search paths for the LabVIEW RTE, but only for directories where the version of the development system matches the version of the LabVIEW RTE. Therefore, when TestStand executes a top-level VI saved without a hierarchy, the LabVIEW RTE searches the directory of the top-level VI and then searches the directories TestStand added to find subVIs. When the LabVIEW RTE finds a subVI saved in a different version of LabVIEW first, the LabVIEW RTE cannot load the subVI and does not load the top-level VI.

Parent topic:

LabVIEW Adapter

Related concepts:

- Search Directories

Related information:

- LabVIEW Adapter Configuration Dialog Box

<!--NI_TOPIC bundle=teststand path=caveats-for-using-engine-callbacks.html language=enus -->
## TOPIC 00146: Caveats for Using Engine Callbacks

- bundle_id: `teststand`
- source_path: `caveats-for-using-engine-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/caveats-for-using-engine-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following issues when you define Engine callbacks: Typically, you do not define SequenceFile<xxx> callbacks in a process model file because these types of callbacks apply only to the steps in the process model file. Do not define a SequenceFileLoad or SequenceFileUnload callback in the

### Caveats for Using Engine Callbacks

Consider the following issues when you define Engine callbacks:

- Typically, you do not define SequenceFile< xxx > callbacks in a process model file because these types of callbacks apply only to the steps in the process model file.
- Do not define a SequenceFileLoad or SequenceFileUnload callback in the StationCallbacks.seq because TestStand does not call these callbacks.
- When a callback sequence is empty, TestStand does not invoke the Engine callback.
- Process models use the Execution.EnableCallback method to disable the ProcessModelPostResults callback when the model does not need to process results on-the-fly for report generation, database logging, offline result file generation, or for any other result processing plug-in.
- TestStand calls other Engine callbacks only when executing the SequenceFileLoad or SequenceFileUnload Engine callbacks. TestStand does not call Engine callbacks when executing the other Engine callbacks.
- When TestStand reloads a sequence file after the file is modified on disk, TestStand can call the SequenceFileLoad callback in the new file without calling the SequenceFileUnload callback in the original file.
- TestStand passes the ProcessModelPostResults, SequenceFilePostResults, and StationPostResults callbacks an extra result for each Sequence Call step. The extra result, called a provisional result, accumulates in the executing thread before the thread calls the sequence the step specifies. Provisional results do not appear in the result list and TestStand does not pass provisional results to the PostResultListEntry callbacks. A provisional result includes a TS.Provisional Boolean property that is set to True . If the ProcessModelPostResults, SequenceFilePostResults, or StationPostResults callback does not need provisional results, it can use the TS.Provisional field to identify and ignore them.

Parent topic:

Modifying Engine Callbacks

Related concepts:

- List of Engine Callbacks
- Step Results

<!--NI_TOPIC bundle=teststand path=caveats-for-using-the-labview-example-user-in.html language=enus -->
## TOPIC 00147: Caveats for Using the LabVIEW Example User Interfaces

- bundle_id: `teststand`
- source_path: `caveats-for-using-the-labview-example-user-in.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/caveats-for-using-the-labview-example-user-in.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following issues when using the example LabVIEW user interfaces: The Load Top-Level VI.vi, located in the <TestStand Public>\UserInterfaces\Full-Featured\LabVIEW\Source Code directory, launches the LabVIEW user interface in the context of a LabVIEW project. If you use the files located

### Caveats for Using the LabVIEW Example User Interfaces

Consider the following issues when using the example LabVIEW user interfaces:

- The Load Top-Level VI.vi , located in the <TestStand Public>\UserInterfaces\Full-Featured\LabVIEW\Source Code directory, launches the LabVIEW user interface in the context of a LabVIEW project.
- If you use the files located in the <TestStand
 Public>\UserInterfaces\Full-Featured\LabVIEW\Source Code or
 <TestStand Public>\UserInterfaces\Simple\LabVIEW\Source
 Code directories as a starting point for creating a user interface,
 NI recommends that you always run the user interface in the context of its
 LabVIEW project to avoid name collisions. If you expect the user interface to
 run outside the context of the LabVIEW project, you must modify the names of the
 VIs in the user interface to ensure the names will not collide with the names of
 code module VIs or its subVIs.
- A LabVIEW project library provides a namespace for the LabVIEW simple and full-featured user interface examples. If you load any VI from the user interface by name, you must update the code that loads the VI to include the namespace.
- When you run the TestExec.exe build specification to generate an executable, LabVIEW prefixes VIs listed under the Dependencies node in the LabVIEW project with Simple UI - or Full UI - for the simple and full-featured user interfaces, respectively, to avoid name collisions. If you load any VI from the user interface by name, you must update the code that loads the VI to include VI prefixes. Complete one of the following options for all dynamic calls listed under the Dependencies node, including VIs that you call from top-level files but that you have not explicitly added to the My Computer target in the LabVIEW project, to resolve this issue:
  - Add the Simple UI - or Full UI - prefix to the path you pass to the Open VI Reference function when the caller VI runs in the LabVIEW RTE. You can use the Application:Kind property in LabVIEW to determine whether the VI is running in the development system or the LabVIEW RTE.
  - Add the VIs listed under the Dependencies node to the My Computer target to prevent the name
 change when you build the executable. LabVIEW prefixes only the files
 listed under the Dependencies node. NI recommends that you prefix these
 VIs manually to avoid potential name collisions that might prevent the
 user interface from running VIs that have conflicting names.

Note

user
 interface

standard

other 2

Parent topic:

Example User Interfaces

Related concepts:

- Example User Interfaces
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=changing-environments.html language=enus -->
## TOPIC 00148: Changing Environments

- bundle_id: `teststand`
- source_path: `changing-environments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/changing-environments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Changing environments requires exiting the existing application instance and launching a new one. You can do this manually by exiting the application and launching a new application instance, specifying the new environment on the command line. For convenience, the TestStand Sequence Editor and full

### Changing Environments

Changing environments requires exiting the existing application instance and
 launching a new one. You can do this manually by exiting the application and
 launching a new application instance, specifying the new environment on the command
 line.

For convenience, the TestStand Sequence Editor and full featured User Interfaces
 support changing environments directly from the Configure Environment dialog.

Select Configure»Environment to launch the Configure
 Environment dialog box. From there, load the desired .tsenv file,
 and choose Set Engine Environment. When prompted to end all
 executions, close all sequence files, and restart the engine, click
 OK. The current application instance shuts down. A new
 instance launches in the specified environment.

Parent topic:

TestStand Environments

<!--NI_TOPIC bundle=teststand path=changing-ex-time-display-format-atml.html language=enus -->
## TOPIC 00149: Changing the Display Format of Execution Time in an ATML Test Results 6.01 or 5.0 Report

- bundle_id: `teststand`
- source_path: `changing-ex-time-display-format-atml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/changing-ex-time-display-format-atml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: XSL and JavaScript code generate the HTML code for the execution time information, for which the default display is in seconds. Complete the following steps to display the execution time information in Hour:Minutes:Seconds format. Open the .xsl file you want to change. Search for the CHANGE_TOTAL_TI

### Changing the Display Format of Execution
 Time in an ATML Test Results 6.01 or 5.0 Report

XSL and JavaScript code generate
 the HTML code for the execution time information, for which the default display is
 in seconds. Complete the following steps to display the execution time information
 in Hour:Minutes:Seconds format.

1. Open the .xsl file you want to change.
2. Search for the CHANGE_TOTAL_TIME_FORMAT comment.
3. Delete the following line of code: <xsl:value-of
 select="tr:ResultSet/tr:Extension/ts:TSStepProperties/ts:TotalTime/@value"/>
 seconds
4. Uncomment the following lines of
 code: <xsl:call-template name="GetTotalTimeInHHMMSSFormat">
 <xsl:with-param name="timeInSeconds" select="tr:ResultSet/tr:Extension/ts:TSStepProperties/ts:TotalTime/@value"/>
</xsl:call-template>

#### TR6_Horizontal.xsl or
 TR5_Horizontal.xsl

The following figure shows the modified execution time
 in a report using the TR6_Horizontal.xsl or
 TR5_Horizontal.xsl file.

[IMAGE alt='image' src='GUID-ED271A0F-5D87-4E67-9F00-8C519A864768-a5.png']

#### TR6_report.xsl or
 TR5_report.xsl

The following figure shows the modified execution time in a
 report using the TR6_report.xsl or TR5_report.xsl
 file.

[IMAGE alt='image' src='GUID-73D7E3D5-49F5-4E4A-ACA5-6AA81B13973F-a5.png']

#### TR6_Expand.xsl or
 TR5_Expand.xsl

The following figure shows the modified execution time in a
 report using the TR6_Expand.xsl or TR5_Expand.xsl
 file.

[IMAGE alt='image' src='GUID-FF254AA0-B153-463A-A480-CDDD9EDD76CA-a5.png']

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

<!--NI_TOPIC bundle=teststand path=changing-ex-time-display-format-xml.html language=enus -->
## TOPIC 00150: Changing the Display Format of Execution Time in an XML Report

- bundle_id: `teststand`
- source_path: `changing-ex-time-display-format-xml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/changing-ex-time-display-format-xml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: XSL and JavaScript code generate the HTML code for the execution time information, for which the default display is in seconds. Complete the following steps to display the execution time information in Hour:Minutes:Seconds format. Open the .xsl file you want to change. Search for the CHANGE_TOTAL_TI

### Changing the Display Format of Execution Time in an XML Report

XSL and JavaScript code generate the HTML code for the execution time information, for which the default display is in seconds. Complete the following steps to display the execution time information in Hour:Minutes:Seconds format.

1. Open the .xsl file you want to change.
2. Search for the CHANGE_TOTAL_TIME_FORMAT comment.
3. Modify the TotalTime XSL template to use a different display format for execution time.
  1. Remove the comment tags from around the following XSL template and add comment tags around the
 existing TotalTime template in the
 horizontal.xsl file and in the
 report.xsl 
 file: <xsl:template match="Prop[@Name='TotalTime']">
 <xsl:param name="reportOptions"/>
 <xsl:value-of disable-output-escaping="yes" select="user:GetTotalTimeInHHMMSSFormat (Value)"/>
</xsl:template>
  2. Remove comment tags from around the following XSL template and add comment tags around the
 existing TotalTime template in the
 expand.xsl 
 file: <xsl:template match="Prop[@Name='TotalTime']">
 <xsl:param name="includeStepResults"/>
 <xsl:param name="includeTimes"/>
 <xsl:param name="useLocalizedDecimalPoint"/>
 <xsl:value-of disable-output-escaping="yes" select="user:GetTotalTimeInHHMMSSFormat (Value)"/>
</xsl:template>

#### horizontal.xsl

The following figure shows the modified execution time in a report using horizontal.xsl:

[IMAGE alt='image' src='GUID-916C7412-E705-4F4F-A840-AD79B82F254C-a5.png']

#### report.xsl

The following figure shows the modified execution time in a report using report.xsl:

[IMAGE alt='image' src='GUID-19BC07EC-6EDA-4AAE-99A3-10C029ED26CF-a5.png']

#### expand.xsl

The following figure shows the modified execution time in a report using expand.xsl:

[IMAGE alt='image' src='GUID-F7718CEF-E508-4446-B22E-D00B5AFA92BE-a5.png']

Parent topic:

Customizing XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=characterization-of-a-transistor.html language=enus -->
## TOPIC 00151: Characterization of a Transistor

- bundle_id: `teststand`
- source_path: `characterization-of-a-transistor.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/characterization-of-a-transistor.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how you can use the Sweep Loop step to characterize a transistor. Example File Location <TestStand Public>\Examples\Interfacing with Hardware\TransistorCharacterizationUsingSweepLoop\TransistorCharacterization.seq Highlighted Features Sweep Loop Step Type Major API

### Characterization of a Transistor

#### Purpose

This example demonstrates how you can use the Sweep Loop step to characterize a transistor.

#### Example File Location

<TestStand Public>\Examples\Interfacing with
 Hardware\TransistorCharacterizationUsingSweepLoop\TransistorCharacterization.seq

#### Highlighted Features

- Sweep Loop Step Type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence sequence, review the steps in the Setup step group.
  - The Get Sequence File Directory step gets the directory of the example sequence file.
  - The Identify CSV Output file step creates the output stream in the sequence file directory.
  - The Write Headers to CSV Output file step adds the row that contains "Temperature (C)", "Voltage (CE)", "Current (Ic)", and "Current gain" denoting the headers for the subsequent records.
2. On the Steps pane, review the steps in the Main step group.
  - The Sweep Transistor - Temperature step sweeps on the junction temperature of the transistor.
  - The While loop containing the Measure Junction temperature step executes until the measured temperature is equal to the desired junction temperature ±0.1 as set in the Sweep loop step above.
  - The Sweep Transistor - Voltage and Current step sweeps on various Voltage and Current parameters.
  - The Calculate Vce step calculates the Collector-Emitter voltage as the difference of voltage between Vcc and Ve.
  - The Measure Ic step simulates the measuring of Collector current.
  - The Measure Ie step simulates the measuring of Emitter current.
  - The Calculate DC Current Gain (hFE) step calculates the gain in current as the ratio of output current (Ic) to input current (Ie).
  - The Write Record to CSV Output file step writes the values of Temperature, Vce, measured Ic and Current gain to the output CSV file for each iteration of the Sweep Loop step.
3. On the Steps pane, review the steps in the Cleanup step group.
  - The Close CSV Output file Stream reference step closes the reference to the CSV Output File Stream.
4. Select Execute»Single Pass to execute the sequence.
5. The Temperature, Vce, Ic and Current gain values are logged to <TestStand
 Public>\Examples\Interfacing with
 Hardware\TransistorCharacterizationUsingSweepLoop\output.csv .

Parent topic:

Examples for Interfacing with Hardware

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=checking-for-suspended-or-stopped-execution-w.html language=enus -->
## TOPIC 00152: Checking for Suspended or Stopped Execution within Code Modules

- bundle_id: `teststand`
- source_path: `checking-for-suspended-or-stopped-execution-w.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/checking-for-suspended-or-stopped-execution-w.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Code modules that TestStand calls can launch dialog boxes or perform other time-consuming operations. In these cases, you might want code modules to periodically check whether TestStand terminated or aborted the parent execution of the code module so the code module can stop gracefully and allow the

### Checking for Suspended or Stopped Execution within Code Modules

Code modules that TestStand calls can launch dialog boxes or perform other time-consuming operations. In these cases, you might want code modules to periodically check whether TestStand terminated or aborted the parent execution of the code module so the code module can stop gracefully and allow the parent execution to terminate or abort. For example, you might want a code module to dismiss a dialog box or cancel a long acquisition and immediately return to TestStand when execution of the code module terminates.

In addition, you might want code modules to permit TestStand to suspend the parent execution thread at a breakpoint without requiring the code module to first return to TestStand. For example, you might want TestStand to be able to suspend an execution at a breakpoint while a code module launches a dialog box that waits for user input.

Use the Execution.InitTerminationMonitor and Execution.GetTerminationMonitorStatus methods to determine whether the execution receives a request to terminate or abort the execution. The termination monitor only recognizes requests to terminate or abort while monitoring, so a code module that executes in a Cleanup step group of an already terminating execution monitors for a subsequent request to terminate the step or abort the execution.

Because the Allow Break While in Code Modules option on the Execution tab of the Station Options dialog box is enabled by default, TestStand suspends the execution thread at a breakpoint even if other threads are executing code modules. Therefore, you do not need to use the Thread.ExternallySuspended property unless you disable the Allow Break While in Code Modules option.

Use the Execution.GetStates method to determine whether the execution is suspended.

#### LabVIEW

As an alternative to the Execution API, you can use the following VIs to enable VIs that TestStand calls to determine whether the execution receives a request to terminate or abort the execution:

- TestStand - Initialize Termination Monitor
- TestStand - Get Termination Monitor Status
- TestStand - Close Termination Monitor

The Termination Monitor only recognizes requests to terminate or abort while monitoring, so a code module that executes in a cleanup step group of an already terminating execution monitors for a subsequent request to terminate the step or abort the execution.

Refer to the VIs in the following directory for examples of how to use these VIs:

- <TestStand Public>\Examples\Demos\Computer Motherboard Test\LabVIEW

Because the Allow Break While in Code Modules option on the Execution tab of the Station Options dialog box is enabled by default, TestStand suspends the execution thread at a breakpoint even if other threads are executing code modules. Therefore, you do not need to use the TestStand – Set Thread Externally Suspended VI unless you disable the Allow Break While in Code Modules option.

#### LabWindows/CVI

As an alternative to the Execution API, you can use the TS_CancelDialogIfExecutionStops function the TestStand Utility Functions driver provides to enable code modules that launch dialog boxes to verify whether the execution that called the function has stopped. Refer to the dialog box code in the following example source file for examples of how to use this function:

- <TestStand Public>\Examples\Demos\Computer Motherboard Test\CVI\Computer Motherboard Test Sequence.c

Parent topic:

Executing Sequences

Related concepts:

- TestStand Directory Structure
- TestStand Utility Functions Library

<!--NI_TOPIC bundle=teststand path=choosing-a-deployment-mechanism.html language=enus -->
## TOPIC 00153: Choosing a Deployment Mechanism

- bundle_id: `teststand`
- source_path: `choosing-a-deployment-mechanism.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/choosing-a-deployment-mechanism.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following installer-based or network-based mechanisms to transfer a test system to one or more test station computers: Distribution you build with the TestStand Deployment Utility Distribution you build with NI Package Builder Installer you build with third-party tools Network drives

### Choosing a Deployment Mechanism

[IMAGE alt='image' src='GUID-6A6FEAAE-4F5A-4C89-AF0B-3EE75BECC2D2-a5.svg']

You can use the
 following installer-based or network-based mechanisms to transfer a test system to
 one or more test station computers:

- Distribution you build with the TestStand Deployment Utility
- Distribution you build with NI Package Builder
- Installer you build with third-party tools
- Network drives
- Source code control (SCC) system/revision control system (RCS)

Consider the following issues as you determine the to use:

- Network access of test station computers —If no network
 infrastructure exists, you cannot use a network drive or SCC system to deploy
 test systems and must instead use an installer on distribution media. Using the
 deployment utility instead of a third-party tool to build a distribution
 requires less specialized knowledge and development time and offers flexible
 customization options, such as using custom commands to run other installers.
 You must use a third-party tool to build installers that support repairing an
 installation or allowing users to select the features to install.
- Test system functionality during network outage—If test station computers must
 maintain production-level operation during network outages, the test station
 computers must include local copies of all the files the test system requires,
 such as user interfaces, configuration files, sequence files, code modules,
 files shared among test station computers, and so on. Test station computers
 must also locally store reporting and database logging results if you must
 maintain test system functionality during a network outage. You can deploy the
 test system using a network drive or an SCC system, but you must store local
 copies of the files on the test station computer.
- Initial development investment and updating
 requirements —Use the deployment utility to build a distribution to
 deploy a test system to test station computers you do not plan to update
 frequently. You can use the deployment utility to build patch distributions to
 update these types of test stations. Use a network-based deployment mechanism to
 deploy a test system to a large number of test station computers you plan to
 update frequently. Setting up a network-based solution for a large deployment
 can make updating the test system more efficient. You can also use a combination
 of mechanisms to deploy a test system. For example, you can use the deployment
 utility to build distributions and transfer those distributions to test stations
 using a network drive or SCC system.
- Design the test system to account for the deployment
 mechanism —You can automate the install and update process by
 writing an application that downloads and uses all the necessary distributions
 to set up the test system instead of running several deployments manually for
 each test station. You can also run a batch program that synchronizes to a set
 of directories from an SCC server or copies a set of directories from a network
 drive and then runs the downloaded distributions. If the test system requires a
 manual initial set-up process, you can automate updating the test code. For
 example, you can modify a process model to read the UUT serial number and
 synchronize sequence files or code modules from an SCC server or copy the files
 from a network drive before testing the UUT.Consider the following issues if you
 use the Microsoft Windows startup folder or Task Scheduler to launch an update
 application you create to complete updates before or after testing occurs.
  - If you implement an automatic update solution, design the application to
 fail without changing the test system or revert the changes to account
 for situations in which network connections fail. Network outages during
 an update can result in a partially updated test system, which might
 return incorrect results or not work properly.
  - Copy all the updated installers to the test station before running the
 installers to prevent partial updates. If any copy of an installer
 fails, do not run any of the installers.
  - Revert changes by backing up directories before syncing the directories
 to the SCC server. If any synchronization fails, restore the directories
 from the backup copies.
  - If the test system requires a manual update process, you can use the
 user interface to prompt users to perform an update after a certain
 amount of time passes.
- Creating patch deployments —Use the same deployment
 mechanism for patch deployments as you used for the full deployment you want to
 update.

If you choose to create a distribution with the TestStand Deployment Utility,
 you must consider the following build output options:

- Deployable Image Only—A directory which contains the files and statically
 referenced dependencies you specify on the System Source tab.
- MSI-based Installer —A custom installer to redistribute
 the deployable image and any NI drivers and software components required by the
 deployment.
- Package-based distribution —A custom NI package to
 redistribute the deployable image. Package based distributions can reference or
 include required driver and run-time packages depending on the distribution
 type.

Note

Building a Distribution with
 NI Package Builder

NI Package Builder Manual

If you do not use the deployment utility to build a
 distribution, you can use the deployment utility to create a deployable image, which
 you can deploy to test station computers by using a different deployment
 mechanism.

Regardless of the deployment mechanism you use, NI recommends that
 you document the required process and procedures to effectively create a
 deployment.

The following table lists the important features each deployment
 mechanism supports.

| Feature of Deployment Mechanism | Distribution You Build with Deployment Utility or NI Package Builder | Installer You Build with Third-Party Tools | Network Drive | SCC System |
| --- | --- | --- | --- | --- |
| Provides a simple way to create a deployment that requires only configuration, not additional development tasks. | ✓ | — | — | — |
| Can deploy the TestStand Runtime, which is required to execute TestStand-based test systems. Mechanisms that cannot automatically deploy the TestStand Runtime must install TestStand by running the installer NI provides. | ✓ | — | — | — |
| Can deploy NI drivers and components, such as NI-DAQmx. Mechanisms that cannot automatically deploy NI drivers must install the drivers by running the installers NI provides, such as the NI Driver DVD. | ✓ | — | — | — |
| Can import hardware configuration information into Measurement & Automation Explorer. You must manually import hardware configuration information if the mechanism does not support automatically importing the information. Using an installer you build with third-party tools requires additional development to import the configuration. | ✓ | ✓ | — | — |
| Can run multiple third-party installers. You must manually run third-party installers if the mechanism does not support automatically running the installers. | ✓ | ✓ | — | — |
| Can install files in TestStand directories, such as the <TestStand Application Data>\\Cfg directory, the <TestStand Public> directory, and the <TestStand> directory. | ✓ | — | — | ✓ |
| Can create a deployment without having specific knowledge of Microsoft Windows Installer technology. | ✓ | — | ✓ | ✓ |
| Does not require test station computers to rely on a network infrastructure. | ✓ | ✓ | — | — |
| Test station computers use local copies of files to ensure test system operation during network outages. | ✓ | ✓ | — | ✓ |
| Submitting modified files does not affect executing test systems because test station computers receive changes only when requested. | ✓ | ✓ | — | ✓ |
| Supports uninstalling files you installed for the test system. | ✓ | ✓ | — | — |
| Supports repairing the deployment to replace deleted or modified files. | — | ✓ | — | — |
| Provides a way for users to decide which features to install on a test station computer. | — | ✓ | — | — |
| Provides an efficient way to perform small updates to the deployment. The size of the files changed determines the size of the update, which does not require a large, fixed, overhead size. | ✓ | ✓ | ✓ | ✓ |
| Automatically identify the set of modified files to include in a patch deployment. | ✓* | — | — | ✓ |
| Easily scales to a large number of test system computers by updating files in a central repository. | — | — | ✓ | ✓ |
| Can revert to a previous version of the test system. | — | — | — | ✓ |

Features marked with an asterisk (*) are available in MSI-based installer
 deployments created by TestStand Deployment Utility, but are not available in
 package-based deployments.

Parent topic:

Deployment Process Overview

Related concepts:

- Network-Based Deployment Mechanisms
- Building an Installer with the TestStand Deployment Utility
- Building a Package Distribution with NI Package Builder
- Building an Installer with Third-Party Tools
- Using a Network Drive to Deploy Test Systems
- Using a Source Code Control System to Deploy Test Systems
- Building a Customized MSI-based Installer
- Using Custom Commands to Execute Third-Party Installers
- Creating a Deployable Image
- TestStand Directory Structure
- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Uninstalling a TestStand Deployment

Related information:

- NI Package Builder Manual

<!--NI_TOPIC bundle=teststand path=choosing-a-teststand-deployment-utility-deplo.html language=enus -->
## TOPIC 00154: Choosing a TestStand Deployment Utility Deployment Build Output

- bundle_id: `teststand`
- source_path: `choosing-a-teststand-deployment-utility-deplo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/choosing-a-teststand-deployment-utility-deplo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Familiarize yourself with the different output types before using this help topic: Creating a deployable image Building an Installer with the TestStand Deployment Utility Building a package distribution with the TestStand deployment utility Feature Comparison for TestStand Deployment Utility build o

### Choosing a TestStand Deployment Utility Deployment Build Output

Familiarize yourself with the different output types before using this help topic:

- Creating a deployable image
- Building an Installer with the TestStand Deployment Utility
- Building a package distribution with the TestStand deployment utility

#### Feature Comparison for TestStand
 Deployment Utility build output types

| Feature | Deployable Image Only | MSI Based Installer | Package Based Distribution - Single Package | Package Based Distribution - Repository | Package Based Distribution - Package Installer |
| --- | --- | --- | --- | --- | --- |
| Consolidates all files in the deployment into a single file | - | - | Yes | Yes | Yes |
| Can be installed by running a single application | - | Yes | Yes | No | Yes |
| Deploy files to multiple destinations on a test station computer | - | Yes | Yes* | Yes* | Yes* |
| Allow the user to specify a custom target directory for files while installing the deployment on a test station computer | Yes | Yes | - | - | - |
| Allows registration of executables or DLL as activeX servers on the test station computer | - | Yes | - | - | - |
| Allows creation of program items in the start menu for files in the deployment | - | Yes | - | - | - |
| Allows creation of shortcuts to files in the deployment | - | Yes | Yes, with restrictions¹ | Yes, with restrictions¹ | Yes, with restrictions¹ |
| Automatically import hardware settings using a MAX configuration | - | Yes | - | Yes, with restrictions² | Yes, with restrictions² |
| Include custom commands to run 3rd party tools or executables | - | Yes | - | - | - |
| Create a file association for TestStand sequence files to a specific User Interface application | - | Yes | - | - | - |
| Available in 32-bit and 64-bit TestStand | Yes | Yes | Yes | Yes | Yes |
| Supports installation with no user interaction (silent installation) | - | Yes | Yes | Yes | Yes |
| Can be installed on a clean machine without NI software | Yes | Yes | No, NI Package Management software and required drivers must be present | No, NI Package Management software must be present | Yes |
| Includes required drivers and run-times in the distribution | - | Yes | No, dependencies are referenced only | Yes | Yes |
| Require a specific version or version range for required drivers and components | - | No, but included drivers will be installed if an older version is present on the deployment target | Yes | Yes | Yes |
| Include references to recommended or optional drivers or components | - | - | Yes | Yes | Yes |
| Create patch distributions which contain only new or updated files | - | Yes | - | - | - |
| Create patch distributions which contain only new or updated drivers and components | - | Yes | Yes | Yes | Yes |
| Include MSI-based additional components | - | Yes | - | - | - |
| Include package-based additional components | - | Yes, but only automatically detected dependencies | Yes | Yes | Yes |
| Distribute deployment with NI package distribution tools | - | - | Yes | Yes | Yes |

¹Shortcuts in package deployments do not support the command line
 arguments and start in options

²MAX
 configuration imports from package based distributions do not support silent
 installation

#### Choosing the Best Build Output for Your Deployment Scenario

If multiple deployment output types are viable based on the table above, consider the below recommendations to choose the best option for your requirements.

1. The deployment requires specific software versions of drivers and components to meet validation requirements. Recommendation: Create a package based deployment and configure the package dependencies to require a specific version of all drivers. Create a package installer or repository to include the required versions of the dependencies in the software.
2. The deployment will be installed on many test station computers with network access, and each must have the same version of driver and components. Recommendation: Use the repository build output to generate a feed which references all required drivers. Host the feed and packages in a network location where it is accessible by the test station computers. Use package management software to register the feed on the test station computer to access the packages.
3. The deployment will be installed on many test station computers without network access, and each must have the same version of driver and components. Recommendation: Create an MSI-based installer with all required software, and ensure that test station computers do not have any NI software present before installing the deployment.

Parent topic:

Choosing a Deployment Mechanism

<!--NI_TOPIC bundle=teststand path=choosing-an-environment.html language=enus -->
## TOPIC 00155: Choosing an Environment

- bundle_id: `teststand`
- source_path: `choosing-an-environment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/choosing-an-environment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To launch the TestStand Sequence Editor or a TestStand User Interface in an environment,specify the /env command line switch followed by the path of the .tsenv file. For example: SeqEdit.exe /env "MyEnvironment.tsenv" If no environment is specified, the application runs without an environment, and t

### Choosing an Environment

To launch the TestStand Sequence Editor or a TestStand User Interface in an
 environment,specify the /env command line switch followed by the
 path of the .tsenv file. For example:

SeqEdit.exe /env "MyEnvironment.tsenv"

If no environment is specified, the application runs without an environment, and the
 TestStand Engine uses the default locations for the various directories. Running
 without an environment is referred to as running in the “global” environment, though
 there is no global environment file.

For convenience, you can specify the global environment by explicitly passing an
 empty string for the environment file path on the command line. For example,
 both

SeqEdit.exe

and

SeqEdit.exe /env ""

launch the Sequence Editor in the global environment.

The following TestStand executables all support the /env command line switch to
 specify an environment:

- TestStand Sequence Editor
- TestStand
 User Interfaces
- TestStand Offline Results Processing Utility
- TestStand Sequence Analyzer Stand-Alone Application
- TestStand File Diff and Merge Utility
- Database Viewer Application

TestStand executables that launch other TestStand executables that use the TestStand Engine
 need to pass the current environment at launch, assuming they want the newly launched
 executable to use the same environment. For example, when you select the
 Tools»DatabaseViewer option in the Sequence Editor, the Sequence
 Editor uses Engine.GetEnvironmentPath with the /env switch to pass the
 current environment toDatabaseView.exe. To see this behavior, select
 Tools»Customize and examine the definition of Database Viewer
 command.

Note

Parent topic:

TestStand Environments

Related concepts:

- Creating Custom User Interfaces

<!--NI_TOPIC bundle=teststand path=choosing-between-32-bit-teststand-and-64-bit.html language=enus -->
## TOPIC 00156: Choosing between 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `choosing-between-32-bit-teststand-and-64-bit.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/choosing-between-32-bit-teststand-and-64-bit.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following issues when making the decision to use 32-bit TestStand or 64-bit TestStand: Requirements of the test system TestStand system requirements and supported application development environments Supported TestStand features Driver support Memory requirements Integration with existi

### Choosing between 32-bit TestStand and 64-bit TestStand

Consider the following issues when making the decision to use 32-bit TestStand or 64-bit TestStand:

- Requirements of the test system
- TestStand system requirements and supported application development environments
- Supported TestStand features
- Driver support
- Memory requirements
- Integration with existing 32-bit sequence files
- Migration issues

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- Features 64-Bit TestStand does not Support
- Driver Support for 64-bit TestStand
- 64-bit Architecture Offers More Memory
- Bitness-Conditional Code for 32-bit TestStand or 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=choosing-between-the-shared-or-side-by-side-v.html language=enus -->
## TOPIC 00157: Choosing Between the Shared or Side-by-Side Version of the LabWindows/CVI Run-Time Engine

- bundle_id: `teststand`
- source_path: `choosing-between-the-shared-or-side-by-side-v.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/choosing-between-the-shared-or-side-by-side-v.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The shared and side-by-side versions of the LabWindows/CVI Run-Time Engine (RTE) differ in the following ways when you install a new version of the RTE. Shared RTE—Installing a new version of the default shared RTE upgrades the previous version of the RTE. The default RTE is backward compatible and

### Choosing Between the Shared or Side-by-Side Version of the LabWindows/CVI Run-Time Engine

The shared and side-by-side versions of the LabWindows/CVI Run-Time Engine (RTE) differ in the following ways when you install a new version of the RTE.

- Shared RTE —Installing a new version of the default shared RTE upgrades the previous version of the RTE. The default RTE is backward compatible and can execute LabWindows/CVI executables or DLLs built with previous versions of LabWindows/CVI. However, the executables or DLLs might not behave exactly the same way as a result of changes in the RTE code. For example, optimizations in the RTE might result in functions executing faster than in previous versions of the RTE.
- Side-by-Side RTE —Because the side-by-side version of the RTE is version-specific, installing a new version of the side-by-side RTE prevents any behavior changes to applications built with older versions of LabWindows/CVI. Previously built LabWindows/CVI applications behave identically because they continue to call the same version of the side-by-side RTE they originally called.

For most applications, NI recommends that you use the default shared RTE. However, if the test
 system requires validation, use the side-by-side version of the RTE to minimize the
 amount of validation required. For example, if you start using a new LabWindows/CVI
 feature in a code module, you must install a new version of the LabWindows/CVI RTE
 on test stations that use the test system. If you use the shared RTE, you would
 validate the entire test system after you installed a new LabWindows/CVI RTE because
 the behavior of DLLs could change using the new version of the RTE. If you use the
 side-by-side RTE, you would validate only the new code because the old code
 continues to call the same RTE version it did before.

Parent topic:

Calling DLLs from TestStand

Related concepts:

- Binding a TestStand Custom User Interface to a Side-by-Side Version of the LabWindows/CVI RTE
- Identifying Components to Deploy

<!--NI_TOPIC bundle=teststand path=choosing-single-or-multiple-deployments.html language=enus -->
## TOPIC 00158: Choosing Single or Multiple Deployments

- bundle_id: `teststand`
- source_path: `choosing-single-or-multiple-deployments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/choosing-single-or-multiple-deployments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Typically, you can expect to update a deployed test system to fix bugs or to add more tests over the lifetime of the test system. The initial configuration of the test system determines the size of the installer and the effort involved to build the installer to update the test system. You can create

### Choosing Single or Multiple Deployments

Typically, you can expect to update a deployed test system to fix bugs or to add more tests over the lifetime of the test system. The initial configuration of the test system determines the size of the installer and the effort involved to build the installer to update the test system.

You can create a or for a test system. Each TestStand deployment specification file (.tsd) contains the information to create a single deployment. To create multiple deployments with different contents, define one .tsd file for each deployment.

#### Single Deployment

If you use a single deployment that contains all the required components for the test system, when you build a patch installer, the deployment utility must analyze and create a deployable image of the entire test system to determine the changed files to include in the patch deployment. Using this technique can increase the time required to build the patch installer to update a test system.

#### Multiple Deployments

You can use multiple deployments to divide the parts of the test system into groups that you most likely will upgrade at the same time. For example, you can create a deployment that contains the TestStand Runtime and another deployment that contains the rest of the test system because the TestStand Runtime is a large component that does not usually change when you update a test system. One common strategy is to use one deployment for the TestStand Runtime, another deployment for TestStand framework files, such as user interfaces and process models, and a third deployment for the rest of the test system, including test sequences and code modules. You can also create product-specific deployments that include only the test sequences and code modules required to test that product, but using this technique can become complex.

#### Include Shared Code in a Separate
 Deployment

Use separate deployments for shared code to ensure that code
 modules execute without errors after installation and to ensure that deployments
 execute correctly when you uninstall shared files.

Note

#### Ensuring Shared Code Executes without
 Errors after Installation

Updating a shared file that multiple deployments use can affect code modules in the other
 deployments that depend on the shared file, especially when you use LabVIEW code modules.
 For example, changes to the inplaceness of a subVI require that you recompile all VIs that
 call the subVI. Determining which deployed VIs require recompilation can be difficult
 because you cannot easily detect inplaceness changes or find all the callers of a VI.
 Additionally, removing VIs from a shared project library can affect the VIs in other
 deployments.

For example, consider that you deployed Caller VI and Called VI. After deployment, you make
 a change in the Called VI that changes memory allocation, such as changing the data wired to
 an indicator to a copy of the data of another indicator, and then save the Called VI. When
 you attempt to run the Caller VI from the test system using the LabVIEW Run-Time Engine, the
 VI appears broken but loads correctly in the LabVIEW development system despite including a
 coercion dot.

For LabVIEW code modules, build packed project libraries and enable the Callers
 adapt at run time to Exported VI connector pane state option on the Connector
 Pane State page of the Packed Library Properties dialog box in LabVIEW. If you do not use
 this technique and you want to change VIs in a deployed test system, you must redeploy all
 the VIs in the test system to prevent run-time errors when LabVIEW recompiles VIs to account
 for inplaceness changes.

#### Uninstalling One Deployment Can Affect Remaining Deployments that Use Shared Files

When multiple deployments use installers you built using the deployment utility to install the same set of shared files and you use one of the uninstallers to remove a deployment, the deployment utility uninstaller removes the shared files from the test station computer, which might affect the remaining deployments that require the shared files. You must uninstall the broken deployment and reinstall it to work around this issue.

You can use LabVIEW packed project libraries to deploy shared files because the deployment utility installer marks the packed project library as a shared file, which the operating system reference counts correctly and does not uninstall the file until you uninstall all installers that require the shared file.

Parent topic:

Creating Deployments

Related concepts:

- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Organizing Test Program Files with LabVIEW Project Libraries
- Upgrade Codes That Affect MSI-based Installer Behavior

<!--NI_TOPIC bundle=teststand path=choosing-the-appropriate-report-generation-st.html language=enus -->
## TOPIC 00159: Choosing the Appropriate Report Generation Strategy

- bundle_id: `teststand`
- source_path: `choosing-the-appropriate-report-generation-st.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/choosing-the-appropriate-report-generation-st.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most automated test systems need to generate a report that logs information about each test run against the unit under test (UUT), including the test status, measurement results, test parameters, and diagnostic information collected during the test. Test systems also have system-level requirements a

### Choosing the Appropriate Report Generation Strategy

Most automated test systems need to generate a report that logs information about each test run against the unit under test (UUT), including the test status, measurement results, test parameters, and diagnostic information collected during the test. Test systems also have system-level requirements and constraints—such as hardware platform, test throughput, tester up-time, and linkage to Manufacturing Execution Systems (MES) or other enterprise management systems—that can influence the report generation strategy the test system uses.

In most cases, the report generation strategy defined for one test system might not meet the requirements of another test system, even within the same organization. Test system architects must typically consider many or all of the following requirements when defining the appropriate report generation strategy for a particular test system:

- Maximize test system throughput
- Minimize report file size
- Include all necessary report content
- Interoperate with other processes and systems
- Support post-failure information recovery
- Generate reports immediately for the current UUT before testing the next UUT
- Generate multiple reports for each UUT
- Generate and view the report during test sequence execution

The topics in this section examine each of these requirements, recommend TestStand report
 generation settings and configurations that best meet each
 requirement in typical scenarios, and identify other requirements
 you might have to sacrifice to optimize a test system for the
 requirement. NI recommends that you use the information in this
 section as a starting point for designing a report generation
 strategy for a test system and iteratively measure and modify the
 test system to achieve the optimal balance among the
 requirements.

Consider the different scenarios in which you run a test system and which requirements are most important for each scenario. For example, when you first develop and debug a test system, throughput might not matter, but support for post-failure information recovery might be critical. When you move to production, throughput might be the most important requirement.

Note

- In some cases, a test system might specify a unique set of requirements that the built-in report
 generators cannot satisfy. NI recommends that you choose a report format
 that most closely satisfies the set of requirements and modify it to fit the
 requirements. You can create custom result processing model plug-ins to
 generate such a report. For example, a test system might require the
 performance throughput of an ASCII report format, the interoperability of an
 XML report format, and the ability to log a small amount of data to the
 report. You can create a custom result processing model plug-in that
 generates an XML report that contains only the information you require.
- You can use multiple results processing configurations to switch easily between settings based on test system execution scenarios.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- Maximizing Test System Throughput
- Minimizing Report File Size
- Including All Necessary Report Content
- Interoperating with Other Processes and Systems
- Supporting Post-Failure Information Recovery
- Generating the Report for the Current UUT before Testing the Next UUT
- Generating Multiple Reports for Each UUT
- Generating and Viewing the Report during Test Sequence Execution
- Process Model Plug-In Architecture

<!--NI_TOPIC bundle=teststand path=clearing-the-product-cache.html language=enus -->
## TOPIC 00160: Clearing the Product Cache

- bundle_id: `teststand`
- source_path: `clearing-the-product-cache.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/clearing-the-product-cache.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The product cache, located at <Program Files>\National Instruments\Shared\ProductCache and at <ProgramData>\National Instruments\MDF\ProductCache on Microsoft Windows 10/8.1/7, contains copies of NI installers you can include in the installer you build with the TestStand Deployment Utility. If the d

### Clearing the Product Cache

The product cache, located at <Program Files>\National
 Instruments\Shared\ProductCache and at
 <ProgramData>\National Instruments\MDF\ProductCache on
 Microsoft Windows 10/8.1/7, contains copies of NI installers you can include in the
 installer you build with the TestStand Deployment Utility.

If the deployment utility cannot locate the required installers in the product cache, the utility
 prompts you to copy the installers from the appropriate NI distribution media before
 you create the deployment. Enable the Copy The Selected Installers And
 All Future Installers to This Computer option in the Drivers and
 Components dialog box for the deployment utility to copy the installers to the
 product cache when the deployment utility builds an installer that contains drivers
 and to make all NI products copy the installers to the product cache when you run
 the installers.

If the deployment utility returns errors when you try to build an installer that includes NI
 drivers or components, deleting the files in the product cache might resolve the
 error if the product cache includes out-of-date or corrupt files.

If you do not plan to include NI drivers or components in the installer you build with the
 deployment utility, you can safely delete the files in the product cache.

Note

Parent topic:

Building a Customized MSI-based Installer

<!--NI_TOPIC bundle=teststand path=code-modules.html language=enus -->
## TOPIC 00161: Code Modules

- bundle_id: `teststand`
- source_path: `code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/code-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A code module is a program module from an application development environment (ADE) or programming language and can contain one or more functions that perform a specific test or other action. Module adapters load and call code modules, pass parameters to code modules, and return values and status fr

### Code Modules

A code module is a program module from an application development environment (ADE) or programming language and can contain one or more functions that perform a specific test or other action. Module adapters load and call code modules, pass parameters to code modules, and return values and status from code modules.

Configure a step to use a module adapter to a step to specify what type of code module the step calls. For example, use the LabVIEW Adapter to call a LabVIEW VI (.vi) or use the LabWindows/CVI Adapter to call a Microsoft Windows dynamic link library (.dll).

Module adapters load and call code modules, pass parameters to code modules, and return values and status from code modules.

Note

- Use relative paths to specify code modules because you typically organize code module files in a folder relative to the TestStand sequence file and TestStand steps. Absolute paths can cause errors in deployment and multiple-developer scenarios because directory structures frequently vary among systems. Absolute paths also increase the maintenance burden if you want to move files within the TestStand system.
- Not all steps call code modules. Some steps perform standard actions you configure using panes and dialog boxes. In this case, the panes and dialog boxes use the custom step properties to store the configuration settings you specify.

Parent topic:

TestStand Building Blocks

Related concepts:

- Module Adapters
- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- Deploying TestStand Systems
- Custom Step Properties
- Communicating with Hardware Drivers
- Executing Code Modules in Parallel

<!--NI_TOPIC bundle=teststand path=command-connections.html language=enus -->
## TOPIC 00162: Command Connections

- bundle_id: `teststand`
- source_path: `command-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/command-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand applications typically use menus, buttons, or other controls to provide commands to users. The OpenSequenceFile, ExecuteEntryPoint, RunSelectedSteps, Break, Resume, Terminate, and Exit commands are common to most TestStand applications. The CommandKinds enumeration in the TestStand User In

### Command Connections

TestStand applications typically use menus, buttons, or other controls to provide commands to users. The OpenSequenceFile, ExecuteEntryPoint, RunSelectedSteps, Break, Resume, Terminate, and Exit commands are common to most TestStand applications.

The CommandKinds enumeration in the TestStand User Interface (UI) Controls API defines a set of common commands you can add to an application. You can connect these commands to TestStand buttons or application menu items, which automatically execute the command. You do not need an event handler to implement the command.

The commands also determine the menu item or button text to display according to the current language and automatically dim or enable buttons or menu items according to the state of the application. Because the TestStand UI Controls API implements many common application commands, connecting commands to buttons and menu items significantly reduces the amount of source code an application requires.

Some commands apply to the selected item in the manager control to which you connect. For example, the Break command suspends the current execution an ExecutionView Manager control selects. Other commands, such as Exit, function the same regardless of the manager control you use to connect them.

Call the following methods to connect a command to a Button or CheckBox control:

- ApplicationMgr.ConnectCommand
- SequenceFileViewMgr.ConnectCommand
- ExecutionViewMgr.ConnectCommand

To invoke a command without connecting it to a control, call one of the following methods to obtain a Command object:

- ApplicationMgr.GetCommand
- ApplicationMgr.NewCommands
- SequenceFileViewMgr.GetCommand
- ExecutionViewMgr.GetCommand

After you obtain a Command object, call the Command.Execute method to invoke the command.

Parent topic:

Connecting Manager Controls to Visible Controls

Related concepts:

- Manager Controls
- ExecutionView Manager
- Managing Menus and Menu Items

<!--NI_TOPIC bundle=teststand path=common-deployment-scenarios.html language=enus -->
## TOPIC 00163: Common Deployment Scenarios

- bundle_id: `teststand`
- source_path: `common-deployment-scenarios.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/common-deployment-scenarios.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To complete the following examples that describe how to use the TestStand Deployment Utility in common deployment scenarios, you need one development computer that contains a complete installation of TestStand and one test station computer. Deploying the TestStand Runtime Distributing Tests from a W

### Common Deployment Scenarios

To complete the following examples that describe how to use the TestStand Deployment Utility in common deployment scenarios, you need one development computer that contains a complete installation of TestStand and one test station computer.

- Deploying the TestStand Runtime
- Distributing Tests from a Workspace
- Adding Dynamically Called Files to a Workspace
- Distributing a User Interface

To run the TestStand Sequence Editor or User Interface application on the test station computer, you must activate an appropriate license or run the application in Evaluation Mode.

Parent topic:

Deploying TestStand Systems

Related concepts:

- Deploying the TestStand Runtime
- Distributing Tests from a Workspace
- Adding Dynamically Called Files to a Workspace
- Distributing a User Interface
- Activating and Licensing TestStand

<!--NI_TOPIC bundle=teststand path=communicating-with-hardware-drivers.html language=enus -->
## TOPIC 00164: Communicating with Hardware Drivers

- bundle_id: `teststand`
- source_path: `communicating-with-hardware-drivers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/communicating-with-hardware-drivers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI does not recommend calling functions in hardware driver DLLs directly from TestStand. Instead, NI recommends that you create a code module from a supported application development environment (ADE) to interface with the driver and acquire data. You can then call this code module from a step in a

### Communicating with Hardware Drivers

NI does not recommend calling functions in hardware driver DLLs directly from TestStand. Instead,
 NI recommends that you create a code module from a supported application development
 environment (ADE) to interface with the driver and acquire data. You can then call
 this code module from a step in a TestStand sequence.

NI recommends this approach for the following reasons:

- Writing a code module in a supported ADE provides access to driver wrapper code, such as the LabVIEW NI-DAQmx Library, which is fully documented and supported.
- Using a code module can help modularize components of the test system and reduce unnecessary complexity in a TestStand sequence. For example, instead of creating multiple TestStand steps that interact directly with a hardware driver, you can create a single code module that configures the hardware, acquires measurement data, and returns a numeric result to TestStand for evaluation.

Parent topic:

Code Modules

<!--NI_TOPIC bundle=teststand path=comparing-report-format-features.html language=enus -->
## TOPIC 00165: Comparing Report Format Features

- bundle_id: `teststand`
- source_path: `comparing-report-format-features.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/comparing-report-format-features.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table illustrates the supported features among the TestStand report formats. 24 Data Types Feature ATML 6.01 or 5.0 ATML 2.02 XML HTML Text Array ✓ ✓ ✓ ✓ ✓ Container* ✓ ✓ ✓ ✓ ✓ Number ✓ ✓ ✓ ✓ ✓ String ✓ ✓ ✓ ✓ ✓ Boolean ✓ ✓ ✓ ✓ ✓ Object reference — — ✓ — — * HTML/Text/XML/ATML reports d

### Comparing Report Format Features

The following table illustrates
 the supported features among the TestStand report formats.

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Array | ✓ | ✓ | ✓ | ✓ | ✓ |
| Container* | ✓ | ✓ | ✓ | ✓ | ✓ |
| Number | ✓ | ✓ | ✓ | ✓ | ✓ |
| String | ✓ | ✓ | ✓ | ✓ | ✓ |
| Boolean | ✓ | ✓ | ✓ | ✓ | ✓ |
| Object reference | — | — | ✓ | — | — |

Note

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Real | ✓ | ✓ | ✓ | ✓ | ✓ |
| Integer | ✓ | ✓ | ✓ | ✓ | ✓ |
| Unsigned integer | ✓ | ✓ | ✓ | ✓ | ✓ |
| Hexadecimal | ✓ | ✓ | ✓ | ✓ | ✓ |
| Octal | ✓ | ✓ | ✓ | ✓ | ✓ |
| Binary | ✓ | ✓ | ✓ | ✓ | ✓ |
| Custom numeric formats with units (such as %#B123x) | ✓ | ✓ | ✓ | ✓ | ✓ |

Note

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Attributes of attributes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Array of attributes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Container with attributes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Attributes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Attributes in NI_TDMSReference type | ✓ | ✓ | ✓ | ✓ | ✓ |
| Attributes for subproperties of the UUT.AdditionalData container | ✓ | — | ✓ | ✓ | ✓ |

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Arrays with negative indexes | ✓ | — | ✓ | ✓ | ✓ |
| Display empty graph for empty numeric array when you select Insert Graph from the Include Arrays ring control | — | N/A | — | ✓ | N/A |
| Empty arrays | ✓ | ✓ | ✓ | ✓ | ✓ |
| Display array index labels | ✓ | ✓ (Only name, not lower or upper bounds) | ✓ | ✓ | ✓ |
| Display array index labels for empty 2D arrays | Displays[0..Empty] | N/A (Only name, not lower or upper bounds) | Displays[0..Empty] | Displays[0..Empty][0..Empty] | Displays[0..Empty][0..Empty] |
| Arrays of different data types | ✓ | ✓ | ✓ | ✓ | ✓ |
| Display graph for array of numbers with a numeric format other than Real, Integer, or Unsigned Integer | — | N/A | — | ✓ | N/A |

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Displays Hidden property in container | — | — | ✓ | — | — |
| Displays property hierarchy when no parent properties have the "Include In Report" flag enabled | ✓ | — | ✓ | — | — |
| Empty structured containers | ✓ | ✓ | ✓ | ✓ | ✓ |
| Empty unstructured containers | ✓ | ✓ | ✓ | ✓ | ✓ |
| Arrays of containers | ✓ | ✓ | ✓ | ✓ | ✓ |

Note

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Comments associated with properties | — | — | — | ✓ | ✓ |

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Append report to target file if target file already exists | ✓ | — | ✓ | ✓ | ✓ |
| Array representation in graph | ✓ | — | ✓ | ✓ | — |
| Array representation in table | ✓ | ✓ | ✓ | ✓ | ✓ |
| Result filtering expression | ✓ | ✓ | — | ✓ | ✓ |
| On-the-fly | ✓ | ✓ | ✓ | ✓ | ✓ |
| Conserve memory | ✓ | ✓ | ✓ | ✓ | ✓ |
| Test limits | ✓ | ✓ | ✓ | ✓ | ✓ |
| Measurements | ✓ | ✓ | ✓ | ✓ | ✓ |
| Include execution time | ✓ | — | ✓ | ✓ | ✓ |
| Include step results | ✓ | —ATML 2.0 does not display the report when you disable the Include Step Reports option. | ✓ | ✓ | ✓ |
| Report colors | ✓ | — | ✓ | ✓ | — |
| Include attributes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Batch reports | ✓ | — | ✓ | ✓ | ✓ |
| TestStand-specific properties (such as generating smaller reports) | ✓ | ✓ | N/A | N/A | N/A |

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Expand/collapse Sequence Call step results | ✓ | ✓ | — | N/A | N/A |
| Log parameters | ✓ | ✓ | ✓ | N/A | N/A |
| Report color | ✓ | — | ✓ | N/A | N/A |
| Module time | — | — | — | N/A | N/A |

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Features supported in XML style sheet | ✓ | N/A | ✓ | N/A | N/A |

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Features supported in XML style sheet | ✓ | N/A | ✓ | N/A | N/A |

| Feature | ATML 6.01 or 5.0 | ATML 2.02 | XML | HTML | Text |
| --- | --- | --- | --- | --- | --- |
| Parameters and results | ✓ | ✓ | ✓ | ✓ | ✓ |
| Failure chain | ✓ | — | ✓ | ✓ | ✓ |
| Background color for status of the measurement elements in Multiple Numeric Test steps | — | N/A | — | ✓ | N/A |
| Escaping strings | ✓ | ✓ | ✓ | — | N/A |
| TD attributes | Step Description inserted using <tr:Description> element. Step ID assigned to the ID attribute of the step. Description appears as attribute in generated report. HTML report does not display Step Description or Step ID. | Step Description and Description inserted using <tr:Description> element. Step ID assigned to the ID attribute of the step. HTML report does not display Step ID. | Step Description, Step ID, and Description appear as attributes in generated report. HTML report does not display Step Description or Step ID. | Description appears as attribute in generated report. Report does not display Step Description or Step ID. | Description appears as attribute in generated report. Report does not display Step Description or Step ID. |
| Variable with white space | Report collapses multiple white spaces to single white space. | Report collapses multiple white spaces to single white space. | Report collapses multiple white spaces to single white space. | Report collapses multiple white spaces to single white space. | Report displays multiple white spaces. |
| Execution time with a numeric format other than Decimal | Always displays in decimal format | N/A | Displays in specified numeric format | Displays in specified numeric format | Displays in specified numeric format |
| Empty sequence file | Header and "No Sequence Results Found" | Header and "No Results Found" | Header and "No Sequence Results Found" | Header only | Header only |

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- NI_TDMSReference
- Choosing the Appropriate Report Generation Strategy

<!--NI_TOPIC bundle=teststand path=comparing-resource-usage-strategies.html language=enus -->
## TOPIC 00166: Comparing Resource Usage Strategies

- bundle_id: `teststand`
- source_path: `comparing-resource-usage-strategies.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/comparing-resource-usage-strategies.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Description This example demonstrates how to use the Execution Profiler to measure and understand how different multithreaded resource usage strategies affect the performance of a simultaneous test of four UUTs when each UUT requires a DMM measurement and a scope measurement. Example File Location <

### Comparing Resource Usage Strategies

#### Description

This example demonstrates how to use the Execution Profiler to measure and understand how different multithreaded resource usage strategies affect the performance of a simultaneous test of four UUTs when each UUT requires a DMM measurement and a scope measurement.

#### Example File
 Location

<TestStand
 Public>\Examples\Parallel Testing\Comparing Resource Usage
 Strategies\Comparing Resource Usage Strategies.seq

#### Highlighted Features

- Execution Profiler
- Synchronization step types

#### Major API

N/A

#### Prerequisites

None

#### How to Use This Example

When you open the Comparing Resource Usage Strategies.seq example sequence file, TestStand also launches the Execution Profiler window.

Complete the following steps to walk through the example:

1. In the TestStand Sequence Editor, select the MainSequence and select Run MainSequence from the Execute menu. In the Execution Profiler window, view the instrument usage in the Item Usage per Thread graph as the example executes five sequences with five different strategies for using the DMM and scope resources. Make the profiler window wider if your screen has room. The first row of the graph shows per step locks on the top level sequence call steps. The example has these locks to better highlight the duration of each strategy in the profiler. Below the square for each lock, you can see the usage of the DMM and scope resources for that strategy.
2. For Sequential, note that each UUT uses the DMM in turn, and then each UUT uses the scope in turn.
3. For Parallel, note that each UUT uses the DMM as soon as it is available and then uses the scope as soon as it is available.
4. For Auto-scheduled, note that each UUT first uses an instrument of either kind, as soon as one is available, and then uses the other kind of instrument as soon as it is available.
5. For Parallel With Additional DMM, note that each UUT first uses either one of two DMMs as soon as one is available and then uses the scope as soon as it is available.
6. For Auto Scheduled With Additional DMM, note that each UUT first uses any instrument, as soon as one is available. It then uses the remaining type of instrument as soon as one is available.
7. Note that each strategy completes in a shorter time than the previous strategy.
8. Open the View menu in the profiler. To focus on the instrument usage only, the example unchecked the following menu items when it launched the profiler in its SequenceFileLoad sequence: Toggle each menu item on and off to observe the additional data the profiler displays when each item is on.
  - Show Blocked Threads
  - Show Code Modules»Step
  - Show Code Modules»Step Type
  - Show Code Modules»Load
  - Show Code Modules»Unload
  - Show Synchronization»Show Auto Scheduling
  - Show Synchronization»Show Batch Synchronization
  - Show Synchronization»Show Wait Operations
  - Show Steps
  - Show UUTs, Batches, and Lots

Complete the following steps to walk through the example:

1. Checkmark the following items in the View menu:
  - Show Blocked Threads
  - Show Synchronization»Show Auto Scheduling
  - Show Synchronization»Show Batch Synchronization
  - Show Synchronization»Show Wait Operations
  - Show UUTs, Batches, and Lots
2. Click Clear and complete the following steps:
  1. In the TestStand Sequence Editor, right-click the Sequential step in the Main step group of the MainSequence and select Run Selected Steps from the context menu.
  2. In the Execution Profiler window, checkmark Auto Fit below the Item Usage Per Thread graph. The Sequential strategy example sequentially runs the DMM test and then the scope test on each UUT. For each test socket thread, the Item Usage per Thread graph shows the use of the DMM resource and the scope resource. The red rectangles in the graph whose tool tips contain Batch Synchronization indicate threads waiting to enter and exit Batch Serial Sections, which is the mechanism this example uses to enforce sequential use of the DMM and scope resources. You can hide the Batch Synchronization operations by unchecking View»Show Batch Synchronized Sections . The Sequential strategy example uses Wait steps to simulate instrument usage. In addition, the Sequential step in the MainSequence is configured to wait for the execution it launches to complete. You can hide the Wait operations by unchecking View»Show Wait Operations . The graph also shows that none of the resources are used in parallel. The time displayed when you hover over the square labeled <No Serial Number> (Batch) is 30 seconds, which is the time it took to test the batch of UUTs. The proceeding steps attempt to lower the total time span value.
  3. Click the Clear button to remove the graph information.
  4. In the sequence editor, right-click the Parallel step in the Main step group of the MainSequence and select Run Selected Steps from the context menu. In the Execution Profiler window, notice that all threads attempt to use the DMM, but only one thread acquires the DMM while the other threads block. As each thread completes the DMM test, another thread can acquire the DMM. You can hide the time that threads block while waiting to acquire resources from the graph in the profiler window display by unchecking View»Show Blocked Threads . Because the DMM and scope resources are used in parallel much of the time, the length of the Batch reduces to 21 seconds. However, because each thread first uses the DMM and then uses the scope, no parallelism exists until the first thread releases the DMM.
  5. Click the Clear button to remove the graph information and select View»Show Blocked Threads to show the time that threads block while waiting to acquire resources.
  6. In the sequence editor, right-click the Auto Schedule step in the Main step group of the
 MainSequence and select Run Selected Steps from the context
 menu. In the profiler, notice that the graph now includes rectangles labeled
 Auto Schedule ("Resource name") , which correspond to Use Auto
 Scheduled Resource steps that define resource usage sections in the sequence. The
 graph shows that the Use Auto Scheduled Resource steps block the execution of their
 threads until the steps can lock the resources that their section of the sequence
 requires. You can hide the operations of the Auto Schedule and Use Auto Scheduled
 Resource steps by unchecking View»Show Auto Scheduling . Notice
 that for some threads, the Auto Schedule example reorders the use of the DMM and scope
 resources to reduce the batch time to approximately 18 seconds, because each DMM test
 takes a minimum of 4.5 seconds. In this example, the test time is now resource
 limited, and any further improvements will require additional resources.
  7. Click the Items tab to display the Items table.
  8. Uncheck View»Show UUTs, Batches, and Lots .
  9. Click the % Actual Time in Use column heading twice to sort the percent values in descending order, as indicated by an inverted triangle icon. The Auto Scheduled item has the highest % Actual Time in Use value. However, this is only the name of the lock the example holds to force the profiler to display the name of the strategy being used. Ignoring that item, the DMM item now has the highest Percent Time in Use value, which indicates that system performance might improve if you add additional DMM resources.
  10. Click the Clear button to remove the graph information and uncheck View»Display Blocked Threads . Checkmark View»Show UUTs, Batches, and Lots .
  11. In the sequence editor, right-click the Parallel with Additional DMM step in the Main step group of the MainSequence and select Run Selected Steps from the context menu. In the profiler, notice that the additional DMM reduces the value of the batch time to approximately 17 seconds. Because the DMM test always precedes the scope test, the scope test cannot execute in parallel until a thread completes its DMM test.
  12. Click the Clear button to remove the graph information.
  13. In the sequence editor, right-click the Auto Scheduled with Additional DMM step in the Main step group of the MainSequence and select Run Select Steps from the context menu. In the profiler, notice that the batch time reduces to approximately 12 seconds, which is a substantial improvement over the initial value of 30 seconds for the Sequential strategy example, in which no parallel resource usage existed.
  14. In the sequence editor, open and examine the Sequential, Parallel, Auto Scheduled, Parallel with Additional DMM, and Auto Scheduled with Additional DMM sequences to view how each sequence synchronizes access to the DMM and scope resources. Notice that the DMM and scope are represented by Wait steps. The example models tests that are resource-bound instead of CPU-bound, and is an accurate model for tests that must wait on instrument and I/O operations and for multi-core systems in which the number of cores equals or exceeds the number of UUTs. You can change the values of the DMMSimulatedTestDuration and ScopeSimulatedTestDuration file global variables to determine the effect of different resource speeds on total throughput. The example contains a ModelOptions callback sequence that sets the number of UUTs to four. You can edit the callback sequence, or you can delete the sequence and select Configure»Model Options to launch the Model Options dialog box and modify the value of the Number of Test Sockets option to experiment with the effect of changing the number of UUTs.

Parent topic:

Examples for Parallel Testing

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=components-directory.html language=enus -->
## TOPIC 00167: Components Directory

- bundle_id: `teststand`
- source_path: `components-directory.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/components-directory.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand installs the default sequences, executables, project files, and source files for components in the following subdirectories of the <TestStand>\Components directory. Directory Name Contents Analyzer Contains TestStand Sequence Analyzer built-in rules file, built-in analysis modules, and ana

### Components Directory

TestStand installs the default sequences, executables, project files, and source files for components in the following subdirectories of the <TestStand>\Components directory.

| Directory Name | Contents |
| --- | --- |
| Analyzer | Contains TestStand Sequence Analyzer built-in rules file, built-in analysis modules, and analysis module templates. You can customize sequence analyzer rules. |
| Callbacks | Contains the sequence files in which TestStand stores Station Engine callbacks and Front-End callbacks. |
| Compatibility | Contains type palette files TestStand uses to save sequence files compatible with earlier versions of TestStand. |
| Icons | Contains icon files for module adapters and step types. |
| Language | Contains string resource files in language-specific subdirectories. |
| Models | Contains the default process model sequence files that you can customize, process model plug-ins, and supporting code modules. |
| Obsolete | Contains components TestStand no longer uses but installs to maintain compatibility. |
| Schemas | Contains the schema for XML-formatted TestStand sequence files. |
| StepTypes | Contains support files for built-in step types. TestStand installs support files for the built-in step types in the <TestStand>\\Components\\StepTypes directory. You can also customize step types. |
| Stylesheets | Contains the style sheet and supporting files to view sequence analyzer reports and TestStand File Diff and Merge utility reports. |
| Tools | Contains sequences and supporting files for the Tools menu commands. |
| Translators | Contains sequence file translator DLLs. TestStand does not create this directory by default. |
| TypePalettes | Contains the default type palette files. |

The TestStand Engine searches for sequences and code modules using the TestStand search directory
 path. The default search precedence places the <TestStand
 Public>\Components directory before the
 <TestStand>\Components directory to ensure that
 TestStand loads the sequences and code modules you customize instead of loading the
 default TestStand versions of the files. Select Configure»Search
 Directories from the sequence editor menu bar to modify the
 precedence of the search directory paths.

When you use the TestStand Deployment Utility to deploy a run-time version of the TestStand Engine, you can bundle customized components in the <TestStand Public> directory with the TestStand run-time deployment.

Parent topic:

TestStand Directory

Related concepts:

- Modifying Engine Callbacks
- Modifying Front-End Callbacks
- Module Adapters
- Creating String Resource Files
- Process Model Support Files
- Modifying Process Model Sequence Files
- Process Model Plug-In Architecture
- Built-In Step Types
- TestStand Directory
- Custom Step Types
- Customizing the Tools Menu
- Sequence File Translators
- Type Concepts
- Search Directories
- TestStand Public Directory
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=computer-motherboard-test-sequence-htbasic.html language=enus -->
## TOPIC 00168: Computer Motherboard Test Sequence - HTBasic

- bundle_id: `teststand`
- source_path: `computer-motherboard-test-sequence-htbasic.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/computer-motherboard-test-sequence-htbasic.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example simulates the testing of a computer motherboard using test steps that use the HTBasic Adapter. The example calls subsequences in the CPU Diagnostic Sequence.seq and CPU Test Sequence.seq sequence files. Example File Location <TestStand Public>\Examples\Demos\Computer Motherboard

### Computer Motherboard Test Sequence - HTBasic

#### Purpose

This example simulates the testing of a computer motherboard using test steps that use the HTBasic Adapter. The example calls subsequences in the CPU Diagnostic Sequence.seq and CPU Test Sequence.seq sequence files.

#### Example File
 Location

<TestStand
 Public>\Examples\Demos\Computer Motherboard Test\HTBasic\Computer
 Motherboard Test Sequence.seq

#### Highlighted Features

- Preconditions
- Sequence Call steps
- Test step types

#### Major API

None

#### Prerequisites

The example contains sequence files designed to work with HTBasic 8.0.

When you use the demo version of HTBasic, you must configure the HTBasic Adapter to use the HTBasic demo server. Select the Use HTBasic Runtime Server option in the HTBasic Adapter Configuration dialog box and specify the path and filename for HTBwin.exe.

Note

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence , review the steps in the Main step group.
  - The Powerup Test step, which is a Pass/Fail Test step, simulates a power-up test. Each of the five test steps that follow the Powerup Test specifies a precondition expression that executes the step only when the Powerup Test step passes.
  - The CPU Test step, which is a Sequence Call step, calls the MainSequence in the CPU Test Sequence.seq sequence file to simulate CPU tests.
  - The ROM Test, RAM Test, Video Test, and Keyboard Test steps simulate tests. Each of the diagnostic steps
  - The Powerup Diagnostics step, which is a Numeric Limit Test step, simulates a power-up diagnostics test. Each of the five diagnostic steps that follow the Powerup Diagnostics step specifies a precondition expression that executes the step only when the corresponding test step fails.
  - The CPU Diagnostics step, which is a Sequence Call step, calls the MainSequence in the CPU Diagnostic Sequence.seq sequence file to simulate CPU diagnostics.
2. Select Execute»Single Pass to run the sequence.
3. When execution completes, review the report on the Report pane to see how TestStand reports the passed and failed steps.

Parent topic:

Computer Motherboard Test

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=computer-motherboard-test-sequence-labview.html language=enus -->
## TOPIC 00169: Computer Motherboard Test Sequence - LabVIEW

- bundle_id: `teststand`
- source_path: `computer-motherboard-test-sequence-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/computer-motherboard-test-sequence-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example simulates the testing of a computer motherboard using test steps that use the LabVIEW Adapter. Example File Location <TestStand Public>\Examples\Demos\Computer Motherboard Test\LabVIEW\Computer Motherboard Test Sequence.seq Highlighted Features Flow Control step types Preconditi

### Computer Motherboard Test Sequence - LabVIEW

#### Purpose

This example simulates the testing of a computer motherboard using test steps that use the LabVIEW Adapter.

#### Example File
 Location

<TestStand
 Public>\Examples\Demos\Computer Motherboard Test\LabVIEW\Computer
 Motherboard Test Sequence.seq

#### Highlighted Features

- Flow Control step types
- Preconditions
- Sequence Call steps
- Test step types

#### Major API

None

#### Prerequisites

None

Note

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence , review the steps in the Setup step group.
  - The Simulation Dialog step calls a VI that launches a dialog box to prompt you to select a test or tests you want to simulate to fail.
  - The Turn Vacuum Table On step, which is an Action step, simulates the activation of a vacuum table. In the Cleanup step group, the Turn Vacuum Table Off step deactivates the vacuum table.
2. On the Steps pane, review the steps in the Main step group.
  - The Powerup Test step, which is a Pass/Fail Test step, simulates a power-up test, and the results of the step determine whether the following If/Else structure continues testing or executes the Powerup Diagnostics step.
  - The CPU Test step, which is a Sequence Call step, calls the CPU Test subsequence to simulate CPU tests.
  - The ROM Test, RAM Test, Video Test, and Keyboard Test steps simulate tests, and if any test fails, the following If structure executes.
  - Each step in the If structure specifies a precondition expression that executes the step only when the corresponding test step fails.
3. Select Execute»Single Pass to run the sequence.
4. In the Test Simulator dialog box, select the Power On test to fail.
5. When execution completes, review the report on the Report pane. The report indicates that the test steps after the Powerup Test step did not execute, but the Powerup Diagnostics step did execute.
6. Select Execute»Restart to run the sequence again.
7. In the Test Simulator dialog box, select any test other than the Power On test to fail.
8. When execution completes, review the report. The report indicates that the Powerup Test step passes and TestStand ran the remaining tests, and that TestStand ran diagnostic steps for any failed test steps but skipped diagnostic steps for any passed test steps.

Parent topic:

Computer Motherboard Test

Related concepts:

- Programming with the TestStand API in LabVIEW
- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=computer-motherboard-test-sequence-labwindows.html language=enus -->
## TOPIC 00170: Computer Motherboard Test Sequence - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `computer-motherboard-test-sequence-labwindows.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/computer-motherboard-test-sequence-labwindows.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example simulates the testing of a computer motherboard using test steps that use the LabWindows/CVI Adapter. Example File Location <TestStand Public>\Examples\Demos\Computer Motherboard Test\CVI\Computer Motherboard Test Sequence.seq Highlighted Features Flow Control step types Precond

### Computer Motherboard Test Sequence - LabWindows/CVI

#### Purpose

This example simulates the testing of a computer motherboard using test steps that use the LabWindows/CVI Adapter.

#### Example File
 Location

<TestStand
 Public>\Examples\Demos\Computer Motherboard Test\CVI\Computer
 Motherboard Test Sequence.seq

#### Highlighted Features

- Flow Control step types
- Preconditions
- Sequence Call steps
- Test step types

#### Major API

None

#### Prerequisites

You must have the LabWindows/CVI Run-Time Engine installed and you must configure the LabWindows/CVI Adapter to execute steps in-process. If you want to use the Execute Steps in an External Instance of CVI option, you must have the LabWindows/CVI development environment installed.

Note

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence , review the steps in the Setup step group.
  - The Simulation Dialog step calls a DLL that launches a dialog box to prompt you to select a test or tests you want to simulate to fail.
  - The Turn Vacuum Table On step, which is an Action step, simulates the activation of a vacuum table. In the Cleanup step group, the Turn Vacuum Table Off step deactivates the vacuum table.
2. On the Steps pane, review the steps in the Main step group.
  - The Powerup Test step, which is a Pass/Fail Test step, simulates a power-up test, and the results of the step determine whether the following If/Else structure continues testing or executes the Powerup Diagnostics step.
  - The CPU Test step, which is a Sequence Call step, calls the CPU Test subsequence to simulate CPU tests.
  - The ROM Test, RAM Test, Video Test, and Keyboard Test steps simulate tests, and if any test fails, the following If structure executes.
  - Each step in the If structure specifies a precondition expression that executes the step only when the corresponding test step fails.
3. Select Execute»Single Pass to run the sequence.
4. In the Test Simulator dialog box, select the Power On test to fail.
5. When execution completes, review the report on the Report pane. The report indicates that the test steps after the Powerup Test step did not execute, but the Powerup Diagnostics step did execute.
6. Select Execute»Restart to run the sequence again.
7. In the Test Simulator dialog box, select any test other than the Power On test to fail.
8. When execution completes, review the report. The report indicates that the Powerup Test step passes and TestStand ran the remaining tests, and that TestStand ran diagnostic steps for any failed test steps but skipped diagnostic steps for any passed test steps.

Parent topic:

Computer Motherboard Test

Related concepts:

- Programming with the TestStand API in LabWindows/CVI
- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=computer-motherboard-test-sequence-python.html language=enus -->
## TOPIC 00171: Computer Motherboard Test Sequence - Python

- bundle_id: `teststand`
- source_path: `computer-motherboard-test-sequence-python.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/computer-motherboard-test-sequence-python.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example simulates the testing of a computer motherboard using test steps that use the Python Adapter. Example File Location <TestStand Public>\Examples\Demos\Computer Motherboard Test\Python\Computer Motherboard Test Sequence.seq Highlighted Features Flow Control step types Precondition

### Computer Motherboard Test Sequence - Python

#### Purpose

This example simulates the testing of a computer motherboard using test steps that use the Python Adapter.

#### Example File
 Location

<TestStand
 Public>\Examples\Demos\Computer Motherboard Test\Python\Computer
 Motherboard Test Sequence.seq

#### Highlighted Features

- Flow Control step types
- Preconditions
- Post Actions
- Sequence Call steps
- Test step types

#### Major API

None

#### Prerequisites

You must have the required version of CPython interpreter installed and added to your PATH variable. You must update the Python version to use in the Python Adapter Configuration dialog box before using the example.

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence sequence, review the steps in the Setup step group.
  - The Simulation Dialog step calls a CVI DLL that launches a dialog box to prompt you to select a test or tests you want to simulate to fail.
  - The Initialize Computer Test step, which is an Action step, creates an instance of a Python class that stores the settings the user specifies in the simulation dialog. TestStand uses the instance of the class to call class functions which do the testing.
  - The Turn Vacuum Table On step, which is an Action step, simulates the activation of a vacuum table. In the Cleanup step group, the Turn Vacuum Table Off step deactivates the vacuum table.
2. On the Steps pane, review the steps in the Main step group.
  - The Powerup Test step, which is a Pass/Fail Test step, simulates a power-up test, and the results of the step determine whether the following If/Else structure continues testing or executes the Powerup Diagnostics step.
  - The CPU Test step, which is a Sequence Call step, calls the CPU Test subsequence to simulate CPU tests.
  - The ROM Test, RAM Test, Video Test, and Keyboard Test steps simulate tests, and if any test fails, the following If structure executes.
  - Each step in the If structure specifies a precondition expression that executes the step only when the corresponding test step fails.
3. Select Execute»Single Pass to run the sequence.
4. In the Test Simulator dialog box, select the Power On test to fail.
5. When execution completes, review the report on the Report pane. The report indicates that the test steps after the Powerup Test step did not execute, but the Powerup Diagnostics step did execute.
6. Select Execute»Restart to run the sequence again.
7. In the Test Simulator dialog box, select any test other than the Power On test to fail.
8. When execution completes, review the report. The report indicates that the Powerup Test step passes and TestStand ran the remaining tests, and that TestStand ran diagnostic steps for any failed test steps but skipped diagnostic steps for any passed test steps.

Parent topic:

Computer Motherboard Test

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=computer-motherboard-test-sequence.html language=enus -->
## TOPIC 00172: Computer Motherboard Test Sequence - .NET

- bundle_id: `teststand`
- source_path: `computer-motherboard-test-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/computer-motherboard-test-sequence.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example simulates the testing of a computer motherboard using test steps that use the .NET Adapter. Example File Location <TestStand Public>\Examples\Demos\Computer Motherboard Test\DotNET\Computer Motherboard Test Sequence.seq Highlighted Features Flow Control step types Preconditions

### Computer Motherboard Test Sequence - .NET

#### Purpose

This example simulates the testing of a computer motherboard using test steps that use the .NET Adapter.

#### Example File
 Location

<TestStand
 Public>\Examples\Demos\Computer Motherboard Test\DotNET\Computer
 Motherboard Test Sequence.seq

#### Highlighted Features

- Flow Control step types
- Preconditions
- Sequence Call steps
- Test step types

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence , review the steps in the Setup step group.
  - The Simulation Dialog step calls a .NET assembly that launches a dialog box to prompt you to select a test or tests you want to simulate to fail.
  - The Turn Vacuum Table On step, which is an Action step, simulates the activation of a vacuum table. In the Cleanup step group, the Turn Vacuum Table Off step deactivates the vacuum table.
2. On the Steps pane, review the steps in the Main step group.
  - The Powerup Test step, which is a Pass/Fail Test step, simulates a power-up test, and the results of the step determine whether the following If/Else structure continues testing or executes the Powerup Diagnostics step.
  - The CPU Test step, which is a Sequence Call step, calls the CPU Test subsequence to simulate CPU tests.
  - The ROM Test, RAM Test, Video Test, and Keyboard Test steps simulate tests, and if any test fails, the following If structure executes.
  - Each step in the If structure specifies a precondition expression that executes the step only when the corresponding test step fails.
3. Select Execute»Single Pass to run the sequence.
4. In the Test Simulator dialog box, select the Power On test to fail.
5. When execution completes, review the report on the Report pane. The report indicates that the test steps after the Powerup Test step did not execute, but the Powerup Diagnostics step did execute.
6. Select Execute»Restart to run the sequence again.
7. In the Test Simulator dialog box, select any test other than the Power On test to fail.
8. When execution completes, review the report. The report indicates that the Powerup Test step passes and TestStand ran the remaining tests, and that TestStand ran diagnostic steps for any failed test steps but skipped diagnostic steps for any passed test steps.

Parent topic:

Computer Motherboard Test

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=computer-motherboard-test.html language=enus -->
## TOPIC 00173: Computer Motherboard Test

- bundle_id: `teststand`
- source_path: `computer-motherboard-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/computer-motherboard-test.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Demos\Computer Motherboard Test directory contains the following examples.

### Computer Motherboard Test

The <TestStand
 Public>\Examples\Demos\Computer Motherboard Test
 directory contains the following examples.

- [Computer Motherboard Test Sequence - HTBasic](computer-motherboard-test-sequence-htbasic.html)
- [Computer Motherboard Test Sequence - LabWindows/CVI](computer-motherboard-test-sequence-labwindows.html)
- [Computer Motherboard Test Sequence - LabVIEW](computer-motherboard-test-sequence-labview.html)
- [Computer Motherboard Test Sequence - .NET](computer-motherboard-test-sequence.html)
- [Computer Motherboard Test Sequence - Python](computer-motherboard-test-sequence-python.html)

Parent topic:

Examples for Demos

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=configuration-entry-points.html language=enus -->
## TOPIC 00174: Configuration Entry Points

- bundle_id: `teststand`
- source_path: `configuration-entry-points.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuration-entry-points.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Sequential, Parallel, and Batch process models include the following Configuration entry point sequences: Configure Result Processing—Launches the Result Processing dialog box, in which you can enable or disable instances of the built-in and custom result processing model plug-ins and configure

### Configuration Entry Points

The Sequential, Parallel, and Batch process models include the following Configuration entry point sequences:

- Configure Result Processing —Launches the Result Processing dialog box, in which you can enable or disable instances of the built-in and custom result processing model plug-ins and configure how the model plug-ins process test results.
- Configure Model Options —Launches the Model Options dialog box, in which
 you configure the number of test sockets and other process model-related
 options.

The Configuration entry points save the station report, database, and model options to the <TestStand Application Data>\Cfg directory. The report, database, and model settings apply to the test station as a whole.

Parent topic:

Features Common to All TestStand Process Models

Related concepts:

- Sequential Process Model
- Parallel Process Model
- Batch Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=configuration-files.html language=enus -->
## TOPIC 00175: Configuration Files

- bundle_id: `teststand`
- source_path: `configuration-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuration-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand stores configuration settings in .ini files in the <TestStand Application Data>\Cfg and <TestStand Application Data>\Cfg\ModelPlugins directories. You can add modified configuration files to a workspace to include the files in a deployment to alter the behavior of TestStand on the test sta

### Configuration Files

TestStand stores configuration settings in .ini files in the <TestStand Application Data>\Cfg and <TestStand Application Data>\Cfg\ModelPlugins directories. You can add modified configuration files to a workspace to include the files in a deployment to alter the behavior of TestStand on the test station computer. If you do not include configuration files in the deployment, TestStand creates a version of the configuration files with default settings.

If you deploy a new test system that uses the TestStand 2012 or later process models to an existing system that uses the equivalent legacy TestStand 2010 process models, you must use the Legacy Model Switcher tool to migrate the report or database options to the TestStand 2012 or later process models. To build an installer that contains the default process models, enable the Install TestStand Runtime option on the Installer Options tab of the TestStand Deployment Utility.

The following table lists commonly modified configuration files, specifies the information TestStand stores in those files, and specifies whether to include those configuration files in a deployment.

| File | Contents | Used in Execution | Used in Editing | Include in Deployment? |
| --- | --- | --- | --- | --- |
| Analyzer.ini | Settings for the TestStand Sequence Analyzer | — | ✓ | If you customize the default sequence analyzer settings |
| CustomRules.tsarules | Information about custom sequence analyzer rules | — | ✓ | If you create custom sequence analyzer rules |
| ConnectionSource.ini | Datalink list the Database and Legacy Property Loader steptypes use for configuration. | ✓ | ✓ | If the test system loads properties from databases using the Legacy Property Loader steps or uses Database step types |
| ModelPlugins\\ResultProcessing.cfg | Configuration information for all result processing model plug-in instances | ✓ | — | If you use the TestStand process models and customized the default reporting, result logging, or database options |
| PLPropertyLoader.ini | Configuration options for the Legacy Property Loader Import/Export Properties toolNote: Legacy Property Loader steps do not use this file. | — | ✓ | If the deployed test system uses the Import/Export Properties tool |
| ImportExportTool.ini | Configuration options for the Import/Export Properties toolNote: Property Loader steps do not use this file. | — | ✓ | If the deployed test system uses the Import/Export Properties tool |
| StationGlobals.ini | Definitions and values of station global variables | ✓ | ✓ | If the test system uses station global variables |
| Templates.ini | Templates configuration for the Insertion Palette pane inthe TestStand Sequence Editor | — | ✓ | If you defined any templates to use in the test system |
| GeneralEngine.cfg | Configuration Options for stations, the Insertion Palette pane, the file path history, and the type palette list | ✓ | ✓ | If you defined custom configurations for the test system |
| Adapters.cfg | Configuration for adapters | ✓ | ✓ | If you defined custom adapter configurations for the test system |
| SearchDirectories.cfg | Configuration for search directories | ✓ | ✓ | If you defined custom search directories for the test system |
| TypePalettes.cfg | Specifies locations of type palette files | ✓ | ✓ | If you defined custom type palette files used in the deployment |
| StartupCfg.ini | Settings needed prior to engine construction | ✓ | ✓ | If you defined custom engine settings for the test system |
| TestStandDatabaseSchemas.ini | Database schemas for result logging | ✓ | — | If you use a custom or modified database schema to log data to a database |
| TestStandModelModelOptions.ini | Model options for built-in process models | ✓ | — | If you use the TestStand process models and customized the default model options |
| ToolMenu.ini | List of Tools menu items | ✓ | ✓ | If you customize the Tools menu on the test station computer. Refer to Export Tools Menu Dialog Box for more information about how to create an export of a Tools menu and how to merge the export onto an existing TestStand deployed system. |
| Users.ini | List of TestStand users | ✓ | ✓ | If you want to configure the set of users on the test station computer |
| FileDiffer.ini | Configuration for the TestStand File Diff and Merge Utility | — | ✓ | If you want to include customized file differ settings in the test system |
| DatabaseViewerOptions.ini | Configuration for the TestStand Database Viewer Application | — | ✓ | If you want to include customized database viewer settings in the test system |
| ModelPlugins\\Addons.cfg | Configuration for the process model plug-in add-ons | ✓ | ✓ | If you want to include process model add-ons in the test system |

The following table lists commonly modified configuration files for the equivalent legacy TestStand 2010 process models, the information TestStand stores in those files, and whether to include those configuration files in a deployment.

| File | Contents | Used in Execution | Used in Editing | Include in Deployment? |
| --- | --- | --- | --- | --- |
| TestStandModelReportOptions.ini | Report options for built-in process models | ✓ | — | If you use the TestStand process models and customized the default report options |
| TestStandDatabaseOptions.ini | Database options for built-in process models | ✓ | — | If you use the TestStand process models and customized the default database options |

You typically do not modify the following files for use in a deployment:

- Deployment Utility Protected Folders.ini —List of directories that cannot be modified by the TestStand Deployment Utility.
- Deployment Utility RecentFiles.ini —Most recently used file list for the TestStand Deployment Utility.
- DeploymentUtilityOptions.ini —Configuration options for the deployment utility.
- DocGen.ini —Configuration options for the Sequence File Documentation tool.
- EngineParts.ini —The deployment utility uses this file when you include the TestStand Runtime in an installer. Do not edit or deploy this file.
- ExpressMenu —Cache of the Express VI menu for the specified LabVIEW version installed on the computer. Do not deploy this file because the cache on the development computer might be different from the cache on the test station computer.
- Filter.ini —List of files to exclude from deployment.
- TestStandPersistedOptions.opt —Persisted breakpoints and watch expressions to use when no workspace is loaded.

#### User-Specific Application Data

TestStand stores the following sequence editor layout and user interface configuration files in the <TestStand Local Application Data> directory. You typically do not include these files in a deployment because users customize these files during normal TestStand use.

- layout_current.bin —Layout of the sequence editor the last time it was closed, including window position, size, docked state, and other settings for the panes, menus, and toolbars.
- SeqEdit.xml —Configuration options for the sequence editor, such as panel size and font settings used on the Insertion Palette pane and the Variables pane.
- UserInterface.xml —Configuration options for the user interfaces, such as window and panel sizes, font settings, and sequences to load. You can customize the data stored in this file.

Parent topic:

Customizing Components You Deploy

Related concepts:

- TestStand Directory Structure
- Using a TestStand Workspace File to Create a Deployment
- Station Global Variables
- Configuring Process Model Plug-ins
- Filtering and Excluding Files

<!--NI_TOPIC bundle=teststand path=configure-keyboard-shortcut-seqedit.html language=enus -->
## TOPIC 00176: Configuring Keyboard Shortcuts in the TestStand Sequence Editor

- bundle_id: `teststand`
- source_path: `configure-keyboard-shortcut-seqedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configure-keyboard-shortcut-seqedit.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure keyboard shortcuts or keyboard mappings in the TestStand sequence editor: View»Customize Toolbars/Menus to launch the Customize dialog box. Click Keyboard to launch the Customize Keyboard dialog box, in which you can customize the shortcut keys for all comma

### Configuring Keyboard Shortcuts in the
 TestStand Sequence Editor

Complete the following steps to configure
 keyboard shortcuts or keyboard mappings in the TestStand sequence editor:

1. View»Customize Toolbars/Menus to launch the Customize
 dialog box.
2. Click Keyboard to launch the Customize Keyboard dialog
 box, in which you can customize the shortcut keys for all commands. 
 Note The
 Customize Keyboard dialog box does not allow you to assign a single key to
 multiple commands. However the default configurations assign the <F5>
 and <Ctrl–F5> keys to multiple commands, such as Run Test UUTs,
 Restart, and Continue. If you attempt to reassign these keys to another
 command, the Customize Keyboard dialog box unassigns only one of the default
 assignments.

Parent topic:

Customizing TestStand Sequence Editor Toolbars and Menus

<!--NI_TOPIC bundle=teststand path=configuring-a-labview-step-to-run-remotely.html language=enus -->
## TOPIC 00177: Configuring a LabVIEW Step to Run Remotely

- bundle_id: `teststand`
- source_path: `configuring-a-labview-step-to-run-remotely.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-a-labview-step-to-run-remotely.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure a LabVIEW step to run remotely. The VI must be present on the local computer so TestStand can configure and run the VI. Click the Advanced Settings button on the LabVIEW Module tab to launch the LabVIEW Advanced Settings window, in which you can specify the

### Configuring a LabVIEW Step to Run Remotely

Complete the following steps to configure a LabVIEW step to run remotely. The VI must be present on the local computer so TestStand can configure and run the VI.

1. Click the Advanced Settings button on the LabVIEW Module tab to launch the LabVIEW Advanced Settings window, in which you can specify the name or an expression that evaluates to the name of the remote computer on which you want to run the VI.
2. Specify the path to the remote VI using the following guidelines: ScenarioControl to Use in LabVIEW Advanced Settings WindowThe remote computer is running the LabVIEW development system or a LabVIEW executable, and you are calling a VI that is not a part of a LabVIEW project.Use the Remove VI Path control to specify the path to the VI on the remote computer.You are calling a VI that is part of a LabVIEW project.Use the Remote Project Path control to specify the path to the LabVIEW project on the remote computer, and use the Remote VI Path control to specify the path within the LabVIEW project to the VI you want to call.

#### Downloading VIs to a PXI Controller

You can use the LabVIEW development system to download VIs to a PXI controller that runs the LabVIEW Real-Time Module. You can also use the TestStand FTP Files step type to download files from and upload files to a remote computer.

Complete the following steps to use FTP to download VIs to the PXI controller.

1. Use the LabVIEW development system to create a Source Distribution with all the VIs to ensure that you include all the dependencies of the VIs to transfer to the hard drive of the LabVIEW Real-Time (RT) target.
2. In the distribution, disable the options to exclude VIs from the <LabVIEW>\vi.lib , <LabVIEW>\instr.lib , and <LabVIEW>\user.lib directories.
3. Use FTP to transfer the source distribution output to the hard drive of the LabVIEW RT target.

After you download the VIs to the PXI controller running the LabVIEW RT module, you can use the Remote VI Path option in the LabVIEW Advanced Settings window to call the VIs.

Note

- TestStand does not support remotely calling VIs that use projects on PXI controllers that run the LabVIEW Real-Time Module because LabVIEW RT does not support LabVIEW projects.
- Refer to the Getting Started with the LabVIEW Real-Time Module manual ( RT_Getting_Started.pdf ) in the <LabVIEW>\manuals directory for more information about downloading VIs to a PXI controller.

Parent topic:

Calling VIs on Remote Computers

Related concepts:

- Calling VIs on Remote Computers
- Organizing Test Program Files with LabVIEW Projects

<!--NI_TOPIC bundle=teststand path=configuring-connection-strings.html language=enus -->
## TOPIC 00178: Configuring Connection Strings

- bundle_id: `teststand`
- source_path: `configuring-connection-strings.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-connection-strings.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A connection string is a string version of the data link connection information that is required to open a database session. You can use the Data Link Properties dialog box to create a connection string that uses OLE DB providers. You can manually create connection strings that use ODBC Drivers and

### Configuring Connection Strings

A connection string is a string version of the data link connection information that is required to open a database session.

You can use the Data Link Properties dialog box to create a connection string that uses OLE DB providers. You can manually create connection strings that use ODBC Drivers and save them as a .udl file. Use these files to specify database connections from TestStand (Database Options, Database Step Types, and Property Loader Step) and from the Database Viewer application.

In the Database Viewer, enter the connection strings in the New Data Link dialog box using the formats given below to establish a connection to the corresponding DBMS servers. Use the Save Data Link option to save the connection information as a .udl file.

This topic lists the connection string formats for the following DBMS servers and their supported providers:

- Access
- MySQL
- Oracle
- SQL Server
- Sybase

#### Access

(32-bit TestStand)

OLE DB:
 Provider=Microsoft.Jet.OLEDB.4.0;Data Source=path to mdb/accdb file;Persist
 Security Info=False;

- Example: Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\Program
 Files\National Instruments\TestStand
 2014\Components\Models\TestStandModels\Database\TestStand
 Results.mdb;Persist Security Info=False;

ODBC:
 Driver={Microsoft Access Driver (*.mdb)};DBQ=path to mdb/accdb
 file

- Example: Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\Program
 Files\National Instruments\TestStand
 2014\Components\Models\TestStandModels\Database\TestStand
 Results.mdb

OLE DB:
 Provider=Microsoft.ACE.OLEDB.12.0;Data Source= path to mdb/accdb
 file;Persist Security Info=False;

- Example: Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\Program
 Files\National Instruments\TestStand
 2014\Components\Models\TestStandModels\Database\TestStand
 Results.mdb;Persist Security Info=False;

ODBC:
 Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path to mdb/accdb
 file

- Example: Driver={Microsoft Access Driver (*.mdb,
 *.accdb)};DBQ=C:\Program Files\National Instruments\TestStand
 2014\Components\Models\TestStandModels\Database\TestStand
 Results.mdb

#### MySQL

ODBC: Driver={MySQL ODBC 5.2 ANSI Driver};Server=<database server name>;Database=<schema name>;User=<user name>;Password=<user password>;Option=<options>;

- Example: Driver={MySQL ODBC 5.2 ANSI Driver};Server=xfiles2010;Database=TSInsert;User=tester;Password=teststand;Option=259;

Note

- You must install the MySQL ODBC Connector to use MySQL.
- You should specify a default database for the connection. Failure to do so generally results in errors.

#### Oracle

OLE DB: Provider=OraOLEDB.Oracle.1;Password=<user password>;Persist Security Info=True;User ID=<user name>;Data Source=<data source name as configured in the Oracle client>;Database=<schema name>;

- Example: Provider=OraOLEDB.Oracle.1;Password=teststand;Persist Security Info=True;User ID=tester;Data Source=ORCL;Database=tester;

ODBC: Driver={Oracle in OraClient11g_home1};Dbq=<data source name as configured in the Oracle client>;Uid=<user name>;Pwd=<user password>;

- Example: Driver={Oracle in OraClient11g_home1};Dbq=ORCL;Uid=tester;Pwd=teststand;

Note

#### SQL Server

OLE DB:

- Using SQL Server Native Client: Provider=SQLNCLI10.1;Password=<user password>;Persist Security Info=True;User ID=<user name>;Initial Catalog=<catalog name>;Data Source=<database server name>;
  - Example: Provider=SQLNCLI10.1;Password=user;Persist Security Info=True;User ID=user;Initial Catalog=user;Data Source=XFILES2010;
- Using Microsoft OLE DB Provider for SQL Server: Provider=SQLOLEDB.1;Persist Security Info=True;User ID=<user name>;Password=<user password>;Data Source=<database server name>;Initial Catalog==<catalog name>;
  - Example: Provider=SQLOLEDB.1;Persist Security Info=True;User ID=abc;Password=testing;Data Source= XFILES2010\TESTSTANDDB;Initial Catalog=test;
- Using Integrated Security: Provider=SQLOLEDB.1; Integrated Security=SSPI;Data Source=<database server name>;Initial Catalog==<catalog name>; 
 Note 

 This option is available in both the SQL Server Native Client provider and the Microsoft OLE DB Provider for SQL Server. Use this option to create connection strings that do not reveal user authentication information.

ODBC:

Driver={SQL Server Native Client 10.0};Uid=<user name>;Pwd=<user password>;Server=<database server name>;Database=<database name>;

- Example: Driver={SQL Server Native Client 10.0};Uid=user;Pwd=user;Server= XFILES2010\TESTSTANDDB;Database=test;

#### Sybase

OLE DB: Provider=SAOLEDB.10;ENG=<database engine name>;DBN=<database name>;User Id=<user name>;Password=<user password>;

- Example: Provider=SAOLEDB.10;ENG=Diff_Db;DBN=Diff_Db;User Id=diff_tester;Password=sql;

ODBC: Driver={SQL Anywhere 10};UID=<user name>;DatabaseName=<database name>;EngineName=<database engine name>;AutoStop=YES;Integrated=NO;EncryptedPassword=3ff6c3114e;Debug=NO;DisableMultiRowFetch=NO;CommLinks='TCPIP{HOST=<database server name>;PORT=<port number for remote connections>}';Compress=NO

- Example: Driver={SQL Anywhere 10};UID=user;DatabaseName=teststand;EngineName=teststand;AutoStop=YES;Integrated=NO;EncryptedPassword=3ff6c3114e;Debug=NO;DisableMultiRowFetch=NO;CommLinks='TCPIP{HOST=xfiles2000;PORT=4436}';Compress=NO

Parent topic:

Database Viewer Application

Related concepts:

- Microsoft ADO, OLE DB, and ODBC Database Technologies

<!--NI_TOPIC bundle=teststand path=configuring-isolated-execution-environments-for-net-modules.html language=enus -->
## TOPIC 00179: Configuring Isolated Execution Environments for .NET Modules

- bundle_id: `teststand`
- source_path: `configuring-isolated-execution-environments-for-net-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-isolated-execution-environments-for-net-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to configure isolated execution environments for specific step types in .NET modules to ensure sensitive or complex operations run independently. Introduced in TestStand 2026 Q1. Launch TestStand. Select View Types . Right-click a type and select Properties. You can select any step type th

### Configuring Isolated Execution
 Environments for .NET Modules

Learn how to configure isolated execution environments for specific step types in
 .NET modules to ensure sensitive or complex operations run independently.

Introduced in TestStand 2026 Q1.

1. Launch TestStand.
2. Select View»Types.
3. Right-click a type and select Properties. 
 You can select any step type that supports .NET modules.
4. Click Advanced»Attributes.
5. Under Type Attributes, right-click to add an
 attribute.
6. Select Insert Attribute»Boolean.
7. Enter UseSeparateAlc for the attribute name.
8. Set Value to True.
9. If you want to use the same assembly load context across multiple step types,
 configure the first step type as detailed above.
  1. For each additional step type, follow steps [2](configuring-isolated-execution-environments-for-net-modules.html#GUID-F045EDEF-A7A5-40C0-955F-C31F7CCB4A73__OEJFLDBXGNLVC)
 through [5](configuring-isolated-execution-environments-for-net-modules.html#GUID-F045EDEF-A7A5-40C0-955F-C31F7CCB4A73__ASDFGHJK).
  2. Select Insert Attribute»String
  3. Enter UseAlcFromStepType for the attribute
 name.
  4. Set Value to the name of the first step type.
 For example, if you have StepType1 and StepType2 the value of the
 UseAlcFromStepType attribute for StepType2
 would be StepType1.
10. Click OK twice to return to the main TestStand window.

By opting into isolated execution
 environments, you can reduce interference from other .NET-based step types. This
 feature is particularly useful for workflows involving complex or critical
 operations.

Note

Parent topic:

.NET Adapter

<!--NI_TOPIC bundle=teststand path=configuring-logging-to-custom-database.html language=enus -->
## TOPIC 00180: Configuring Logging to Custom Database

- bundle_id: `teststand`
- source_path: `configuring-logging-to-custom-database.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-logging-to-custom-database.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps before you use the default process model to log results to a database. Ensure that you thoroughly understand fundamental database concepts. Decide which database management system (DBMS) you want to use. By default, TestStand supports SQL Server, Oracle, Microsoft Access

### Configuring Logging to Custom Database

Complete the following steps before you use the default process model to log results to a database.

1. Ensure that you thoroughly understand fundamental database concepts.
2. Decide which database management system (DBMS) you want to use. By default, TestStand supports SQL Server, Oracle, Microsoft Access, Sybase, and MySQL. You can add support for other database management systems.
3. Ensure you installed the appropriate client DBMS software required to communicate with the DBMS. You must decide to use an Open Database Connectivity (ODBC) driver or a specific Object Linking and Embedding Database (OLE DB) provider for the DBMS. Use the OLE DB providers for SQL Server and Access. Most Oracle ODBC drivers and OLE DB providers require that you install Oracle Client. Refer to the Recommended Database Client Software section of the NI TestStand Readme for more information about suggested providers, versions of ODBC drivers, client DBMS software, and any known issues.
4. Create the default database tables in the DBMS. The
 <TestStand>\Components\Models\TestStandModels\Database 
 directory contains SQL script files to create and delete the default database
 tables the default TestStand schemas require. For example, the Access
 Create Generic Recordset Result Tables.sql file contains SQL
 commands to create the default tables for Access. The Access Drop
 Result Tables.sql file contains SQL commands to delete the
 default tables. TestStand includes an example Access database,
 TestStand Results.mdb , in the
 <TestStand>\Components\Models\TestStandModels\Database 
 directory. You can also create the default database tables using an SQL script
 file.
5. Use the Database Options dialog box to enable database logging and to define a data link and schema for the default process model to use.

Parent topic:

Data Links

Related concepts:

- TestStand Database Fundamentals
- Adding Support for Other Database Management Systems
- TestStand Directory Structure
- Default TestStand Table Schemas
- Database Viewer—Creating Result Tables
- Data Links
- Database Known Issues

<!--NI_TOPIC bundle=teststand path=configuring-process-model-plug-ins.html language=enus -->
## TOPIC 00181: Configuring Process Model Plug-ins

- bundle_id: `teststand`
- source_path: `configuring-process-model-plug-ins.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-process-model-plug-ins.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A process model invokes plug-in instances at defined points during execution. A plug-in instance specifies the plug-in sequence file to invoke and the set of options with which to invoke the sequence file. At run time, the process model reads the set of plug-in instances to invoke from the plug-in c

### Configuring Process Model Plug-ins

A process model invokes plug-in instances at defined points during execution. A plug-in instance specifies the plug-in sequence file to invoke and the set of options with which to invoke the sequence file. At run time, the process model reads the set of plug-in instances to invoke from the plug-in configuration (.cfg) files located in the <TestStand Application Data>\Cfg\ModelPlugins directory. By default, TestStand creates the ResultProcessing.cfg and Addons.cfg configuration files in the <TestStand Application Data>\Cfg\ModelPlugins directory if the files do not already exist.

#### ResultProcessing.cfg

The ResultProcessing.cfg file stores the information for plug-in instances you configure in the Result Processing dialog box.

#### Model Plug-in Add-ons and Addons.cfg

A model plug-in add-on is a model plug-in the process model invokes without requiring end users to create and configure a plug-in instance. For example, you can use an add-on to override the dialog boxes the Test UUTs and Single Pass Execution entry points launch and create a custom serial number entry solution instead.

Place a model plug-in sequence file in the <TestStand Public>\Components\Models\ModelPlugins\Addons directory to create a model plug-in add-on. The process model updates the Addons.cfg file when the model detects a new, removed, or updated plug-in in the Addons directory. The process model automatically uses the default set of options the add-on sequence file defines to create one plug-in instance for each add-on in the Addons.cfg file.

#### Creating Additional Model Plug-in Configuration Files

You can create additional model plug-in configuration files in the following ways:

- Call the DisplayModelPluginDialogEx function in ModelSupport2.dll as defined in ResultProcessing.h , located in the <Teststand>\Components\Models\TestStandModels directory, to launch a dialog box that creates and edits a configuration file.
- Copy an existing configuration file to a new filename, open the new file in a text editor, and replace any occurrence of the previous filename with the new filename.
- Create a configuration file programmatically using an instance of the PropertyObjectFile class with a file type of FileType_PropertyObjectFile. The type of the PropertyObjectFile.Data property of the file must be NI_ModelPluginConfigurationSet .

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- TestStand Directory Structure
- Programmatically Updating a Configuration File
- Model Plug-in Categories

<!--NI_TOPIC bundle=teststand path=configuring-remote-executions.html language=enus -->
## TOPIC 00182: Configuring Remote Executions

- bundle_id: `teststand`
- source_path: `configuring-remote-executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-remote-executions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must properly configure a remote computer and the TestStand server application on the remote computer when you want to invoke a sequence on the remote computer from TestStand on a client computer. You must enable the TestStand server on the remote computer to accept remote execution requests. Yo

### Configuring Remote Executions

You must properly configure a remote computer and the TestStand server application on the remote computer when you want to invoke a sequence on the remote computer from TestStand on a client computer. You must enable the TestStand server on the remote computer to accept remote execution requests. You must also configure Windows system security to allow users to access and launch the TestStand server remotely. When you use the TestStand API on the server computer to access objects on the client computer, you must also configure Windows system security on the local client.

Note

Parent topic:

Executing Sequences Remotely

Related concepts:

- Configuring TestStand as a Server for Remote Executions
- TestStand ActiveX API Overview
- Executing Sequences Remotely

<!--NI_TOPIC bundle=teststand path=configuring-search-directories-for-deployment.html language=enus -->
## TOPIC 00183: Configuring Search Directories for Deployment

- bundle_id: `teststand`
- source_path: `configuring-search-directories-for-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-search-directories-for-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you want to configure search directories for deploying a TestStand system, you can manually add additional search paths to the list of default search paths on the target computer. The TestStand Deployment Utility does not copy additional search paths because the new directories might not exist

### Configuring Search Directories for Deployment

When you want to configure search directories for deploying a TestStand system, you can manually add additional search paths to the list of default search paths on the target computer. The TestStand Deployment Utility does not copy additional search paths because the new directories might not exist on the target computer.

NI recommends installing the <TestStand Application
 Data>\Cfg\SearchDirectories.cfg file with the deployment for that
 system because TestStand stores the search directories in
 SearchDirectories.cfg. Use the Force File to
 Install option on the Distributed Files tab of the TestStand
 Deployment Utility to overwrite existing files.

Parent topic:

Search Directories

Related concepts:

- Preparing Source Components for Deployment
- TestStand Directory Structure
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=configuring-sequence-editor-and-user-interfac.html language=enus -->
## TOPIC 00184: Configuring Sequence Editor and User Interface Startup Options

- bundle_id: `teststand`
- source_path: `configuring-sequence-editor-and-user-interfac.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-sequence-editor-and-user-interfac.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Sequence Editor and all user interface applications support command-line options for opening and running sequences. You can append the startup options in the following table to the sequence editor and user interface command line. The "/" and "-" characters are valid command prefixes. U

### Configuring Sequence Editor and User Interface Startup Options

The TestStand Sequence Editor and all user interface applications support command-line options for opening and running sequences. You can append the startup options in the following table to the sequence editor and user interface command line. The "/" and "-" characters are valid command prefixes. Use spaces to separate command parameters. You must use quotation marks for arguments that contain spaces, such as "Test UUTs" and "C:\My Documents\MySeq.seq".

| Option | Purpose |
| --- | --- |
| sequencefile {sequencefile2}... | Instructs the application to automatically load the sequence files at startup, as shown in the following example: SeqEdit.exe "c:\\My Seqs\\seq1.seq" "c:\\My Seqs\\seq2.seq" |
| /run sequencesequencefile | Instructs the application to automatically load and run the sequence in the sequence file at startup, as shown in the following example: SeqEdit.exe /run MainSequence "c:\\My Seqs\\test.seq" |
| /runEntryPoint entrypointnamesequencefile | Instructs the application to automatically load and run the sequence file at startup using the Execution entry point you specify, as shown in the following example: SeqEdit.exe /runEntryPoint "Test UUTs" "c:\\My Seqs\\test.seq" You must use the entry point name to specify the entry point to use, not the sequence name. The entry point name is displayed in the Execute menu in the sequence editor. To change the entry point name, edit the Entry Point Name Expression field, located in the Model tab of the Sequence options. |
| /editor | Instructs the application to open in Editor Mode when the application supports editing, as shown in the following example: testexec.exe /editor |
| /goto location | Instructs the application to display the item the location property object path specifies, as shown in the following example: testexec.exe c:\\example.seq /goto "Seq[1].Main[4].TS.LoadOpt" |
| /operatorInterface | Instructs the application to open in Operator Mode, as shown in the following example: testexec.exe /operatorInterface |
| /quit | Instructs the application to exit after running the executions you specify, as shown in the following example: SeqEdit.exe /run MainSequence "c:\\My Seqs\\test.seq" /quitTestStand ignores the /quit option if the execution fails to launch. |
| /useExisting | Instructs the application to use the existing running instance of the application instead of opening a new instance, as shown in the following example: SeqEdit.exe /useExistingTestStand ignores the /useExisting option when you specify the /quit option. |
| /setCurrentDir | Instructs the application to set the current directory to the first directory in the File dialog box directory history list, as shown in the following example: SeqEdit.exe /setCurrentDirThe current directory is the directory the File dialog box initially displays when you open or save a file. Use this option to instruct the File dialog box to display the directory the File dialog box displayed the last time you ran the application. TestStand sets the current directory after processing the other command-line options. |
| /? | Instructs the application to launch a help dialog box that contains a list of valid command-line arguments and then close immediately, as shown in the following example: SeqEdit.exe /?TestStand ignores all other options when you specify the "/?" option. |
| /outputToStdIO | Instructs the application to write the status of completed executions as standard output, as shown in the following example: SeqEdit.exe /outputToStdIOWhen you run a user interface from the command line, the console window displays the standard output from the application. |
| /env <environment path> | Launches the application in the environment defined in the .tsenv file located at <environment path>. |
| workspacefile | Instructs the application to automatically load the workspace file at startup, as shown in the following example: SeqEdit.exe "c:\\My Workspaces\\ws1.tsw"This option applies only to the Sequence Editor. |
| sequenceanalyzerprojectfile | Instructs the application to automatically load the sequence analyzer project file at startup, as shown in the following example: SeqEdit.exe "c:\\My spaces\\myAnalyzerFile.tsaproj"This option applies only to the Sequence Editor. |

Refer to the ApplicationMgr.ProcessUserCommandLineArguments event for more information about processing user-defined command-line arguments in a user interface. When an error exists in the command-line argument, the Application Manager control generates an ApplicationMgr.ReportError event.

Parent topic:

Extending TestStand

Related concepts:

- Creating Editor Applications
- Editor Versus Operator Interface Applications
- Application Manager

<!--NI_TOPIC bundle=teststand path=configuring-teststand-as-a-server-for-remote.html language=enus -->
## TOPIC 00185: Configuring TestStand as a Server for Remote Executions

- bundle_id: `teststand`
- source_path: `configuring-teststand-as-a-server-for-remote.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-teststand-as-a-server-for-remote.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable the Allow Sequence Calls from Remote Computers to Run on this Computer option on the Remote Execution tab of the Station Options dialog box to allow the TestStand server to accept remote execution requests from a client computer. TestStand does not support remotely executing a sequence across

### Configuring TestStand as a Server for Remote Executions

Enable the Allow Sequence Calls from Remote Computers to Run on this Computer option on the Remote Execution tab of the Station Options dialog box to allow the TestStand server to accept remote execution requests from a client computer.

Note

A TestStand server is active while the TestStand application <TestStand>\Bin\REngine.exe runs on a remote computer. Each TestStand client communicates with a dedicated version of the TestStand server, which launches automatically when a TestStand client uses the server.

Enable the Show the System Tray Icon While the TestStand Remote System is Active on this Machine option on the Remote Execution tab of the Station Options dialog box on the remote computer to make the TestStand icon visible in the remote computer system tray for each instance of the remote engine application. The tooltip for the icon indicates which computer is connected to the remote engine. Right-click the TestStand icon to display when the engine was created or to force the remote engine application to close.

Note

TestStand automatically registers the server during installation. To manually register or unregister the server, invoke the executable with the /RegServer or /UnregServer command-line arguments.

Parent topic:

Configuring Remote Executions

<!--NI_TOPIC bundle=teststand path=configuring-teststand-ui-controls-cvi.html language=enus -->
## TOPIC 00186: Configuring the TestStand UI Controls for a LabWindows/CVI User Interface

- bundle_id: `teststand`
- source_path: `configuring-teststand-ui-controls-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-teststand-ui-controls-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the functions in the example user interface files that demonstrate configuring connections, commands, and other settings for the TestStand User Interface (UI) Controls. Source Files Functions <TestStand Public>\UserInterfaces\Simple\CVI\Source Code\TestExec.c SetupActiveXCo

### Configuring the TestStand UI Controls for a LabWindows/CVI User Interface

The following table lists the functions in the example user interface files that demonstrate configuring connections, commands, and other settings for the TestStand User Interface (UI) Controls.

| Source Files | Functions |
| --- | --- |
| <TestStand Public>\\UserInterfaces\\Simple\\CVI\\Source Code\\TestExec.c | SetupActiveXControls |
| <TestStand Public>\\UserInterfaces\\Full-Featured\\CVI\\Source Code\\TestExec.c | GetActiveXControlHandlesRegisterActiveXEventCallbacksConnectTestStandControlsConnectStatusBarPanesRebuildMenuBar |

Parent topic:

Using TestStand UI Controls in LabWindows/CVI

Related concepts:

- Example User Interfaces
- TestStand UI Controls
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=configuring-teststand-ui-controls-labview.html language=enus -->
## TOPIC 00187: Configuring the TestStand UI Controls for a LabVIEW User Interface

- bundle_id: `teststand`
- source_path: `configuring-teststand-ui-controls-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-teststand-ui-controls-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following example user interface VIs for examples of configuring connections, commands, and other settings for the TestStand User Interface (UI) Controls: Simple OI - Configure Application Manager Simple OI - Configure SequenceFileView Manager Simple OI - Configure ExecutionView Manager

### Configuring the TestStand UI Controls for a LabVIEW User Interface

Refer to the following example user interface VIs for examples of configuring connections, commands, and other settings for the TestStand User Interface (UI) Controls:

- Simple OI - Configure Application Manager
- Simple OI - Configure SequenceFileView Manager
- Simple OI - Configure ExecutionView Manager
- Full UI - Configure StatusBar
- Full UI - Configure SequenceFileView Manager
- Full UI - Configure ListBar
- Full UI - Configure ExecutionView Manager

Parent topic:

Using TestStand UI Controls in LabVIEW

Related concepts:

- Example User Interfaces
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=configuring-the-adapter-icon-color-for-a-cust.html language=enus -->
## TOPIC 00188: Configuring the Adapter Icon Color for a Custom Step Type

- bundle_id: `teststand`
- source_path: `configuring-the-adapter-icon-color-for-a-cust.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-the-adapter-icon-color-for-a-cust.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the adapter icon color for a custom step type to enable users to distinguish between step types in the Step Types list and in a sequence. On the Types pane of the Types window, locate and expand the step type. Right-click and select Insert Field from the context menu, select String, and na

### Configuring the Adapter Icon Color for a Custom Step Type

Configure the adapter icon color for a custom step type to enable users to distinguish between step types in the Step Types list and in a sequence.

1. On the Types pane of the Types window, locate and expand the step type.
2. Right-click and select Insert Field from the context menu, select String , and name it Category .
3. Click the Values column and enter one of the following values:
  - Action —sets the icon color to green.
  - Test —sets the icon color to magenta.
4. Hide the property on step instances. Step instances do not require the property.
  1. Double-click Category to open the Type Properties dialog box.
  2. Click Advanced , then select Flags .
  3. Select PropFlags_ExcludeFromCopy .
  4. (Optional) Select PropFlags_Hidden and PropFlags_HiddenInTypes to hide the property in the Types pane.

Parent topic:

Custom Step Types

Related concepts:

- Creating Custom Step Types
- Custom Properties of Step Types

<!--NI_TOPIC bundle=teststand path=configuring-the-cpu-affinity-for-labview-exec.html language=enus -->
## TOPIC 00189: Configuring the CPU Affinity for LabVIEW Execution Threads

- bundle_id: `teststand`
- source_path: `configuring-the-cpu-affinity-for-labview-exec.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-the-cpu-affinity-for-labview-exec.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When TestStand executes a VI using the LabVIEW development system, the CPU affinity for all LabVIEW execution threads is set to allow all CPUs. When TestStand executes a VI using the LabVIEW RTE, the CPU affinity for LabVIEW execution threads depends on the following factors: The CPU affinity of the

### Configuring the CPU Affinity for LabVIEW Execution Threads

When TestStand executes a VI using the LabVIEW development system, the CPU affinity for all LabVIEW execution threads is set to allow all CPUs.

When TestStand executes a VI using the LabVIEW RTE, the CPU affinity for LabVIEW execution threads depends on the following factors:

- The CPU affinity of the TestStand execution thread
- Whether you enable the Execute ‘Same as caller’ VIs Using Multiple Threads option in the LabVIEW Adapter Configuration dialog box
- Whether you enable the Additional Threads Inherit Calling Thread’s CPU Affinity option in the LabVIEW Adapter Configuration dialog box
- The setting of the Preferred Execution System option on the Execution page of the VI Properties dialog box in LabVIEW
- The version of LabVIEW that executes the VI

#### LabVIEW 2009 or Later

The
 following table shows how these factors apply when TestStand executes VIs using the
 LabVIEW 2009 or later RTE and the preferred execution system of the VI is
 same as caller.

| TestStand Option:Execute 'Same as caller' VIs Using Multiple Threads | TestStand Option:Additional Threads Inherit Calling Thread's CPU Affinity | CPU Affinity Behavior |
| --- | --- | --- |
| Disabled | — | The VI executes using the TestStand execution thread and its CPU affinity. |
| Enabled | Disabled | The CPU affinity for all execution threads, including the TestStand execution thread, is set to allow all CPUs. The CPU affinity of the TestStand execution thread is restored to its original affinity when the VI execution completes and the TestStand execution thread returns to TestStand. |
| Enabled | Enabled | The CPU affinity for all additional LabVIEW execution threads is set to match the CPU affinity of the TestStand thread. |

When TestStand executes VIs using the LabVIEW 2009 or later RTE and the
 preferred execution system of the VIs is set to something to other than
 same as caller, the CPU affinity for all LabVIEW
 execution threads is set to allow all CPUs.

#### LabVIEW 8.6.1 or
 Earlier

The following table describes the CPU affinity for LabVIEW
 execution threads when TestStand executes VIs using the LabVIEW 8.6.1 or earlier
 RTE.

| LabVIEW Setting:Preferred Execution System | CPU Affinity Behavior |
| --- | --- |
| same as caller | The VI executes using the TestStand execution thread and its CPU affinity. |
| Not same as caller | The CPU affinity for all LabVIEW execution threads is set to allow all CPUs |

Parent topic:

Symmetric Multiprocessing in VIs Executed from TestStand

<!--NI_TOPIC bundle=teststand path=configuring-the-labview-vi-server-to-run-vis.html language=enus -->
## TOPIC 00190: Configuring the LabVIEW VI Server to Run VIs Remotely

- bundle_id: `teststand`
- source_path: `configuring-the-labview-vi-server-to-run-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-the-labview-vi-server-to-run-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW development system or LabVIEW executable from which you call a VI must be running on the remote computer, and you must configure the development system or built executable to allow VI calls through the TCP/IP protocol of the VI Server. You can configure the VI Server settings for the fol

### Configuring the LabVIEW VI Server to Run VIs Remotely

The LabVIEW development system or LabVIEW executable from which you call a VI must be running on the remote computer, and you must configure the development system or built executable to allow VI calls through the TCP/IP protocol of the VI Server.

You can configure the VI Server settings for the following test system configurations:

- A main application instance —Select Tools»Options in LabVIEW to launch the Options dialog box and select the VI Server category.
- A project application instance —Right-click My Computer in the LabVIEW Project Explorer window, select Properties from the context menu to launch the My Computer Properties dialog box, and select the VI Server category.
- A target, such as a LabVIEW Real-Time Server —Right-click the appropriate target in the LabVIEW Project Explorer window, select Properties from the context menu to launch the Target Properties dialog box, and select the VI Server category.
- A LabVIEW-built executable —Add VI Server-specific settings to the LabVIEW configuration INI file associated with the executable, or use the Server properties of the Application class to programmatically enable and configure the VI Server for a running application.

#### Configuring Additional VI Server Options

Use the following sections in the Options dialog box in LabVIEW to further configure a VI Server:

- VI Server category —Enable the TCP/IP protocol and the VI call options. You can also specify the TCP/IP port the server uses. The port you specify in LabVIEW must be the same port you specify in TestStand in the LabVIEW Advanced Settings window.
- Machine Access section of the VI Server category —Allow specific computers access to the VI Server. You can also specify certain computers or entire domains that can call VIs on the server computer.
- Exported VIs section of the VI Server category —Configure the VIs you want to call through the VI Server. You must export all VIs you want to call remotely from TestStand. The default setting in LabVIEW is to export all VIs. The asterisk (*) in the Exported VIs list control indicates this setting.

#### Configuring VI Server Security

TestStand does not support user-based VI security for executing VIs on remote computers. You must use the Machine access list in the Machine Access section of the VI Server category in the Options dialog box in LabVIEW to protect a VI server on a remote computer.

Parent topic:

Calling VIs on Remote Computers

Related concepts:

- Calling VIs on Remote Computers

<!--NI_TOPIC bundle=teststand path=configuring-the-number-of-execution-threads-a.html language=enus -->
## TOPIC 00191: Configuring the Number of Execution Threads Assigned to a LabVIEW Execution System

- bundle_id: `teststand`
- source_path: `configuring-the-number-of-execution-threads-a.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-the-number-of-execution-threads-a.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add tokens to a .ini file to configure the number of threads assigned to a LabVIEW execution system. The full name and location of the .ini file depends on which of the following servers you configure in the LabVIEW Adapter Configuration dialog box to use to execute VIs: LabVIEW Run-Time Eng

### Configuring the Number of Execution Threads Assigned to a LabVIEW Execution System

You can add tokens to a .ini file to configure the number of threads assigned to a LabVIEW execution system. The full name and location of the .ini file depends on which of the following servers you configure in the LabVIEW Adapter Configuration dialog box to use to execute VIs:

- LabVIEW Run-Time Engine —LabVIEW looks for a .ini file with the same name and location as the TestStand application, such as SeqEdit.ini for the TestStand Sequence Editor or TestExec.ini for a TestStand User Interface.
- Development System —LabVIEW looks for a .ini file named LabVIEW.ini , located in the same directory as the LabVIEW.exe development system executable.

For the LabVIEW development system, add the following tokens below the [LabVIEW] tag in the .ini file. For the LabVIEW Run-Time Engine, add the following tokens below the [LVRT] tag in the .ini file.

ESys.StdNParallel = -1

ESys<Built-in Execution System>.Normal = n

where

- n is the number of threads to assign to the execution system. Specify -1 to use the default number of threads in LabVIEW, which is the greater of four or the number of CPUs in the system.
- <Built-in Execution System> is the execution system for which you want to set the number of threads. The following lists the valid values for specifying the execution system.

| Execution System Name | Value |
| --- | --- |
| Standard | <EmptyString> |
| Instrument | .Instrument |
| DAQ | .DAQ |
| Other1 | .other1 |
| Other2 | .other2 |

Note

- You must restart LabVIEW for the new settings to take effect.
- The settings you specify apply to all versions of the LabVIEW RTE that TestStand loads.

Parent topic:

Symmetric Multiprocessing in VIs Executed from TestStand

Related concepts:

- Symmetric Multiprocessing in VIs Executed from TestStand

<!--NI_TOPIC bundle=teststand path=configuring-the-number-of-labview-rte-executi.html language=enus -->
## TOPIC 00192: Configuring the Number of LabVIEW RTE Execution Threads

- bundle_id: `teststand`
- source_path: `configuring-the-number-of-labview-rte-executi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-the-number-of-labview-rte-executi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using the LabVIEW Adapter, you can configure the number of execution threads the LabVIEW Run-Time Engine (RTE) uses to execute VIs. You can adjust these settings to optimize performance for a particular system. If the Preferred Execution System option on the Execution page of the VI Properties dialo

### Configuring the Number of LabVIEW RTE Execution Threads

Using the LabVIEW Adapter, you can configure the number of execution threads the LabVIEW Run-Time Engine (RTE) uses to execute VIs. You can adjust these settings to optimize performance for a particular system.

If the Preferred Execution System option on the Execution page of the VI Properties dialog box in LabVIEW of the VI is same as caller, the LabVIEW RTE uses the TestStand execution thread to execute the VI. If you enable the Execute ‘Same as caller’ VIs Using Multiple Threads option in the LabVIEW Adapter Configuration dialog box, the LabVIEW Adapter configures the LabVIEW RTE to use additional LabVIEW threads, in addition to the TestStand execution thread, to execute the VI.

If the preferred execution system of the VI is set to something other than same as caller, LabVIEW uses only LabVIEW threads to execute the VI. The TestStand execution thread processes window messages while waiting for the VI execution to complete.

Parent topic:

Symmetric Multiprocessing in VIs Executed from TestStand

Related concepts:

- Programming with the TestStand API in LabVIEW
- Symmetric Multiprocessing in VIs Executed from TestStand

<!--NI_TOPIC bundle=teststand path=configuring-the-package-settings.html language=enus -->
## TOPIC 00193: Configuring the Package Settings

- bundle_id: `teststand`
- source_path: `configuring-the-package-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/configuring-the-package-settings.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Package distribution settings are configured on the package distribution options tab. On this tab, you can choose the package name and the destination where TestStand Deployment Utility will generate the distribution. To configure additional settings for the package, click the Package Attributes but

### Configuring the Package Settings

Package distribution settings are configured on the package distribution options tab. On this tab, you can choose the package name and the destination where TestStand Deployment Utility will generate the distribution.

To configure additional settings for the package, click the Package Attributes button.

Note

Include Required Certificate Packages

To Include package-based dependencies, click the Dependencies button. For each dependency you select, you can configure the dependency level:

- Required (default) — The package cannot be installed unless the dependency is on the system or can be found by NI Package Manager through a registered feed. These packages will be included in the deployment in the repository or package distribution mode.
- Recommended — The package can be installed without these dependencies.They are not included in the repository or package distribution mode. If the dependency package is referenced in a feed on the test station computer, the dependency will be displayed as an optional package when the deployment package is installed, and will be selected by default.
- Optional — The same as a recommended package, except that optional packages are not selected by default when installing the deployment package.

You can also specify a required version range for each dependency:

- Any Version — Do not require a specific version.
- Specific Version — Require the exact version number specified in the Version control.
- Greater Than (default) — The required package version must be greater than the version specified in the Version control. The version field is set by default to the currently installed version of the package.
- Less Than — The required package version must be greater than the version specified in the Version control.
- In Range — The required package version must be in a specified version range. When you enable this option, a second version control is available to enter the maximum version.

The following features are currently not supported in package mode:

- Creating program items in the start menu
- Registering deployed files as an activeX server
- Executing Custom Commands
- Including readme files or license agreements
- Media spanning

Parent topic:

Building a Package Distribution with the TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand path=connecting-manager-controls-to-visible-contro.html language=enus -->
## TOPIC 00194: Connecting Manager Controls to Visible Controls

- bundle_id: `teststand`
- source_path: `connecting-manager-controls-to-visible-contro.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/connecting-manager-controls-to-visible-contro.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect a manager control to a visible control to display sequences or reports, present a list of items to users, invoke an application command, or display information about the current state of the application. When you connect controls, you do not need to write the majority of the source code you

### Connecting Manager Controls to Visible Controls

Connect a manager control to a visible control to display sequences or reports, present a list of items to users, invoke an application command, or display information about the current state of the application. When you connect controls, you do not need to write the majority of the source code you usually write for the application to update the user interface and respond to user input.

You can make view connections, list connections, command connections, and information source connections, depending on the type of manager control and visible control you connect.

Refer to the NI TestStand User Interface Controls Reference Poster for an illustration of control connections in a sample user interface.

Parent topic:

Getting Started with User Interface Development

Related concepts:

- Manager Controls
- Visible Controls

<!--NI_TOPIC bundle=teststand path=connecting-to-a-database-with-the-odbc-admini.html language=enus -->
## TOPIC 00195: Connecting to a Database with the ODBC Administrator

- bundle_id: `teststand`
- source_path: `connecting-to-a-database-with-the-odbc-admini.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/connecting-to-a-database-with-the-odbc-admini.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To access databases through the Open Database Connectivity (ODBC) standard, you must have an ODBC driver for each database system you use. Each ODBC driver must register itself with the operating system when you install it. You must also define and name data sources in the ODBC Administrator on the

### Connecting to a Database with the ODBC Administrator

To access databases through the Open Database Connectivity (ODBC) standard, you must have an ODBC driver for each database system you use. Each ODBC driver must register itself with the operating system when you install it. You must also define and name data sources in the ODBC Administrator on the Windows Control Panel, which typically requires information such as a server, database, and additional database-specific options. You can define one or more data sources for each ODBC driver. Navigate to the standard Windows Control Panel facility for administrative tools and select Data Sources (ODBC) to launch the ODBC Data Source Administrator dialog box.

(Windows 10/8.1/7) If you use the ODBC Administrator and you receive any warnings, follow the prompts. You might need administrator access to create a new Database Source Name (DSN).

Note

Parent topic:

Data Links

Related concepts:

- Microsoft ADO, OLE DB, and ODBC Database Technologies
- ODBC Data Source Administrator Dialog Box

<!--NI_TOPIC bundle=teststand path=connecting-ui-controls-demo.html language=enus -->
## TOPIC 00196: Connecting UI Controls Demo

- bundle_id: `teststand`
- source_path: `connecting-ui-controls-demo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/connecting-ui-controls-demo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose The Connecting Controls User Interface demonstrates the available TestStand User Interface controls and allows you to customize their functionality. The TestStand User Interface controls get their functionality through a connection to a manager control. The manager controls provide methods t

### Connecting UI Controls Demo

#### Purpose

The Connecting Controls User Interface demonstrates the available TestStand User Interface controls and allows you to customize their functionality. The TestStand User Interface controls get their functionality through a connection to a manager control. The manager controls provide methods to implement the various types of connections.

This example allows you to explore the available connections and see their behavior in real time.

#### Example File Location

<TestStand Public>\Examples\Modifying User Interfaces\Connecting UI Controls\DotNet\bin\Release\TestExec.exe

#### Highlighted Features

TestStand User Interface Controls

#### Major API

UI Connection methods

#### Prerequisites

None

#### How to Use This Example

To launch the User Interface, Open the TestExec.exe executable. The UI automatically opens a sequence file and runs a sequence, then pauses the sequence at a breakpoint.

Navigate the tabs of the interface to view the different UI controls available with TestStand and the types of connections to manager controls that they support. Each tab provides more information about each of the following UI Control connection types:

- View Connections —Activates a SequenceView, VariablesView, or ReportView control. The manager controls provide a separate method for each connection type, so no cmdKind parameter is needed.
- List Connections —Configures a TestStand ComboBox, ListBarPage, or ListBox to display a TestStand List, such as the sequences in the current file. The manager controls provide a separate method for each connection type, so no cmdKind parameter is needed.
- Command Connections —Configures a TestStand Button or Checkbox control to execute a specified command when clicked. Change the enumerations to see the behavior of the available command kinds.
- Information Source Connections —Displays caption, image, and numeric information on Label controls, ExpressionEdit controls, and StatusBar panes. Changing the source Input will change what information is displayed in the connected control.

Click the Additional Information button in the example UI to view more information about these connection types.

Parent topic:

Examples for Modifying User Interfaces

Related concepts:

- TestStand Directory Structure
- TestStand API Overview
- Connecting Manager Controls to Visible Controls

<!--NI_TOPIC bundle=teststand path=console-for-interpreter-sessions-in-python.html language=enus -->
## TOPIC 00197: Console for Interpreter Sessions in Python

- bundle_id: `teststand`
- source_path: `console-for-interpreter-sessions-in-python.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/console-for-interpreter-sessions-in-python.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use Advanced Settings Dialog to specify if you want to display console for each Python interpreter session created for executing Python code modules. The console will be automatically closed based on the lifetime of Python interpreter session which is configured in Python Interpreter to Use.

### Console for Interpreter Sessions in Python

You can use Advanced Settings Dialog to specify if you want to display console for each Python interpreter session created for executing Python code modules.

The console will be automatically closed based on the lifetime of Python interpreter session which is configured in Python Interpreter to Use. The console window for the Global interpreter option will stay open between executions. Call 'Unload All Modules' to properly unload the Global interpreter and close the window.

Note

Parent topic:

Python Adapter

<!--NI_TOPIC bundle=teststand path=convert-lv-modules-to-dlls.html language=enus -->
## TOPIC 00198: Converting LabVIEW Analysis Modules and Rule Configuration Modules to DLLs

- bundle_id: `teststand`
- source_path: `convert-lv-modules-to-dlls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/convert-lv-modules-to-dlls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you deploy LabVIEW analysis modules, consider building a DLL using a LabVIEW project. By deploying a LabVIEW-built DLL, you can avoid having to deploy multiple VIs that comprise the full hierarchy of the analysis modules and rule configuration modules. Refer to the LabVIEW Help for more infor

### Converting LabVIEW Analysis Modules and Rule
 Configuration Modules to DLLs

LabVIEW Help

LabVIEW Define VI Prototype

1. For the return value, change the VI Output to
 code, which is the code element of
 the Error Out cluster.
2. Delete the code parameter.
3. Delete the status parameter.

Function Prototype

```text
int32_t VIName(IDispatch *AnalysisContext, char source[], int32_t len)
```

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand path=copying-read-only-files-to-modify.html language=enus -->
## TOPIC 00199: Copying Read-Only Files to Modify

- bundle_id: `teststand`
- source_path: `copying-read-only-files-to-modify.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/copying-read-only-files-to-modify.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, TestStand installs source files in the protected and non-writeable <TestStand>\CodeTemplates, <TestStand>\Components, and <TestStand>\UserInterfaces directories. To modify the installed code templates or components or to create new code templates or components, copy the files from the <T

### Copying Read-Only Files to Modify

By default, TestStand installs source files in the protected and non-writeable
 <TestStand>\CodeTemplates,
 <TestStand>\Components, and
 <TestStand>\UserInterfaces directories.

To modify the installed code templates or components or to create new code templates or
 components, copy the files from the <TestStand>
 directories to the <TestStand Public>directories and
 make changes to the copies of the files.

To modify the installed user interfaces or to create new user interfaces, modify the files TestStand installs in the <TestStand Public>\UserInterfaces directory.

#### Guidelines for Modifying Copied Files

Use the following guidelines when you copy installed files to modify:

- You must rename the files after you modify them if you want to create a separate custom component. You must register any new or renamed ActiveX components.
- You do not have to rename the files after you modify them if you only want to modify the behavior of an existing component.
- If you do not rename the files and you use the files in a future version of TestStand, changes
 NI makes to the component might not be compatible with the modified version of
 the component.
- Storing new and customized files in the <TestStand Public> directory ensures that new installations of the same version of TestStand do not overwrite the customizations and ensures that uninstalling TestStand does not remove the files you customize.

Note

<TestStand>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand>\Components\Models\TestStandModels

<TestStand>\Components\Models\ModelPlugins

<TestStand Public>\Components\Models\ModelPlugins

Parent topic:

TestStand Public Directory

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=cpu-affinity-mask-support-for-64-bit-teststan.html language=enus -->
## TOPIC 00200: CPU Affinity Mask Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `cpu-affinity-mask-support-for-64-bit-teststan.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/cpu-affinity-mask-support-for-64-bit-teststan.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Setting the CPU affinity is optional. When you select Use Custom CPU Affinity as the CPU Affinity option for threads or executions with Sequence Call Adapter steps, you can specify the CPU affinity mask for a new thread or new execution. Because 32-bit Microsoft Windows uses a 32-bit CPU affinity ma

### CPU Affinity Mask Support for 64-bit TestStand

Setting the CPU affinity is optional. When you select Use Custom CPU Affinity as the CPU Affinity option for threads or executions with Sequence Call Adapter steps, you can specify the CPU affinity mask for a new thread or new execution. Because 32-bit Microsoft Windows uses a 32-bit CPU affinity mask, and 64-bit Windows uses a 64-bit mask, the mask behaves as a pointer-sized integer. 32-bit TestStand expects the affinity mask to be a TestStand Number data type with the default (double) representation. 64-bit TestStand expects the affinity mask to be a Number data type with the 64-bit unsigned integer representation.

If a sequence needs to support only one architecture, use the representation that matches the required architecture. If the sequence must support the 32-bit architecture and the 64-bit architecture, use bitness-conditional code in the mask expression. For example, to enable all CPUs, use the following expression:

RunState.Engine.Is64Bit? -1ui64 : -1

where -1 indicates to set all bits and therefore use all CPUs.

Only the Use Custom CPU Affinity option requires specifying the mask. The Use Station Option for CPU Affinity, Use CPU Affinity of Caller, and Use All CPUs options do not require or allow specification of the affinity mask and therefore do not require bitness-conditional code.

In TestStand 2014 or later, the Default CPU Affinity for Threads option on the Preferences tab of the Station Options dialog box is a 64-bit unsigned integer for 32-bit TestStand and 64-bit TestStand. However, because of the 32-bit limitation on affinity masks in 32-bit Windows, 32-bit TestStand cannot specify affinity for processors beyond the first 32 processors if more than 32 processors are present.

When you use the TestStand Engine API to set the default CPU affinity mask, use the StationOptions.DefaultCPUAffinityForThreadsEx property for 32-bit applications and for 64-bit applications instead of the now obsolete StationOptions.DefaultCPUAffinityForThreads property.

Parent topic:

Sequence Call Adapter Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=cpu-affinity-step-type-support-for-64-bit-tes.html language=enus -->
## TOPIC 00201: CPU Affinity Step Type Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `cpu-affinity-step-type-support-for-64-bit-tes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/cpu-affinity-step-type-support-for-64-bit-tes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the CPU Affinity step type to specify the CPU affinity mask of a process or thread. Because 32-bit Microsoft Windows uses a 32-bit CPU affinity mask, and 64-bit Windows uses a 64-bit mask, the mask behaves as a pointer-sized integer. 32-bit TestStand expects the affinity mask to be a Tes

### CPU Affinity Step Type Support for 64-bit TestStand

You can use the CPU Affinity step type to specify the CPU affinity mask of a process or thread. Because 32-bit Microsoft Windows uses a 32-bit CPU affinity mask, and 64-bit Windows uses a 64-bit mask, the mask behaves as a pointer-sized integer. 32-bit TestStand expects the affinity mask to be a TestStand Number data type with the default (double) representation. 64-bit TestStand expects the affinity mask to be a Number data type with the 64-bit unsigned integer representation.

If a sequence needs to support only one architecture, use the representation that matches the required architecture. If the sequence must support the 32-bit architecture and the 64-bit architecture, use bitness-conditional code in the mask expression. For example, to enable all CPUs, use the following expression:

RunState.Engine.Is64Bit? -1ui64 : -1

where -1 indicates to set all bits and therefore use all CPUs.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=crash-recovery-for-teststand-applications.html language=enus -->
## TOPIC 00202: Crash Recovery for TestStand Applications

- bundle_id: `teststand`
- source_path: `crash-recovery-for-teststand-applications.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/crash-recovery-for-teststand-applications.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand has the option to generate a log containing execution information and use the NI Error Reporting Service, NIER, to automatically generate a crash dump file. You can use a crash dump file to diagnose the root cause of a crash. In cases where the crash is in an NI product, you can send the c

### Crash Recovery for TestStand Applications

TestStand has the option to generate a log containing execution information and use the NI
 Error Reporting Service, NIER, to automatically generate a crash dump file. You can use a
 crash dump file to diagnose the root cause of a crash. In cases where the crash is in an NI
 product, you can send the crash dump file to NI support engineers for diagnosis. TestStand
 also offers a way to register a custom sequence to execute in an external process in
 response to a crash.

TestStand Crash Log—When a crash occurs TestStand generates a log file in the directory <TestStand_LocalAppData>\CrashLogs.Only the last 100 crash logs are saved, after which the earliest log file will be deleted and a new log file is created.

NIER Crash Dump—Using the same error reporting service as LabVIEW, TestStand generates a NIER crash dump in <TestStand_LocalAppData>\NIERdump.

The following figure shows the sequence that occurs when a crash occurs in a TestStand application.

[IMAGE alt='image' src='GUID-A8A1A763-C335-40F4-8DF9-686095548E0F-a5.svg']

Parent topic:

Extending TestStand

<!--NI_TOPIC bundle=teststand path=create-custom-rules-tsa.html language=enus -->
## TOPIC 00203: Creating Custom Rules in the TestStand Sequence Analyzer

- bundle_id: `teststand`
- source_path: `create-custom-rules-tsa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/create-custom-rules-tsa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can customize the TestStand Sequence Analyzer by creating custom rules and analysis modules. A rule defines a single task to perform during analysis, such as ensuring that the prototype of each code module is up to date or ensuring that each expression specified evaluates to the correct type and

### Creating Custom Rules in the TestStand
 Sequence Analyzer

You can customize the TestStand Sequence Analyzer by creating custom rules and analysis
 modules.

A rule defines a single task to perform during analysis, such as ensuring that the
 prototype of each code
 module
 is up to date or ensuring that each expression specified evaluates to the correct
 type and does not include any syntax errors. An analysis module is a VI, a class
 method in a .NET assembly, or a function in a DLL the sequence analyzer invokes to
 implement analyzer rules. Analysis modules perform the checks the rules specify and
 generate messages which the sequence analyzer stores in the analyzer project.

Analysis module specifications specify the analysis modules to call. Analysis module
 specifications also specify when the sequence analyzer calls the analysis module,
 the types of objects to which the analysis modules apply, and whether to call the
 analysis module when transitioning from one type of object to another. The sequence
 analyzer stores custom rules and analysis module specifications in
 <TestStand Application
 Data>\Cfg\CustomRules.tsarules.
 Refer to the Analyzer Examples for more information about custom rules and analysis
 modules.

Complete the following steps to create a custom analyzer rule and a corresponding
 analysis module.

1. If you are using the sequence analyzer in the TestStand Sequence Editor, click
 the Sequence Analyzer Options button on the Sequence
 Analyzer toolbar or select Debug»Sequence Analyzer»Sequence Analyzer
 Options to launch the Sequence Analyzer Options dialog box. 
 Note The sequence
 editor requires an enabled ConfigApp user
 privilege
 to launch the Configure Available Rules dialog box. The built-in TestStand
 Developer and Administrator user groups grant this privilege by default.
2. If you are using the stand-alone sequence analyzer application, click the
 Available Rules button in the Sequence Analyzer
 Options dialog box or select Edit»Available Rules to
 launch the Configure Sequence Analyzer Available Rules dialog box.
3. Complete the following steps to create or edit a custom rule in the Configure
 Sequence Analyzer Available Rules dialog box. 
 Note The set of
 rules available on a computer is the same for all analyzer projects you open
 on that computer. When you use the Configure Sequence Analyzer Available
 Rules dialog box to add a new rule to the computer and then open an older
 project, the sequence analyzer automatically adds the new rule to the
 project. Similarly, the sequence analyzer removes from projects any rules
 that you removed using the Configure Sequence Analyzer Available Rules
 dialog box.
  1. Select the Rules tab and expand the
 CustomRules.tsarules section.
  2. Click New Rule button to the right of the
 <Insert New Rule> Rule ID to launch the Edit Rule dialog
 box.
  3. On the General tab of the Edit Rule dialog box, enter or select values
 for the Rule ID, Category, Severity, Name, and Description controls. You
 can also use the Rules tab of the Configure Sequence Analyzer Available
 Rules dialog box to edit the general settings of custom rules. 
 Note Select
 a Rule ID that is unique to the rules on your computer and the rules
 on any other computers to which you might deploy the rule. National
 Instruments recommends that you add your company name as a prefix to
 the Rule ID to prevent potential conflicts with other custom Rule
 IDs.
  4. (Optional) On the Advanced tab of the Edit Rule dialog box, enter or
 select values for the Resource String Category and Configuration Option
 controls to specify options for localization and configuration. You can
 add custom rule settings by using the Edit Rule dialog box to launch a
 standard sequence analyzer dialog box in which users configure custom
 rules or by creating a custom rule configuration module to launch a
 dialog box you create in which users configure custom rules.
  5. Click OK to save the changes and close the Edit
 Rule dialog box.
4. Use LabVIEW, LabWindows/CVI, Microsoft Visual C#, or Microsoft Visual C++ to
 create an analysis module that implements one or more rules.
5. Complete the following steps to add a custom analysis module to the
 CustomRules.tsarules section on the Analysis Modules
 tab of the Configure Sequence Analyzer Available Rules dialog box.
  1. Select the Analysis Modules tab and expand the
 CustomRules.tsarules section.
  2. Click the New Analysis Module button to the
 right of the <Insert New Analysis Module> analysis module to
 launch the Edit Analysis Module dialog box.
  3. In the Edit Analysis Module dialog box, enter the path to the module, a
 VI, .NET assembly, or DLL and select the kinds of objects, object types,
 and transition settings for the custom analysis module.
  4. If you specify a VI as the analysis module and you want to debug the
 VI, disable the Run VI in LabVIEW Run-Time Engine
 option. You must also enable the Development
 System option in the Select or Type Which LabVIEW Server
 to Use section of the LabVIEW Adapter Configuration dialog box.
  5. Click OK to save the changes and close the Edit
 Analysis Module dialog box.

You can deploy custom rules and analysis
 modules for use in analysis projects or to analyze individual files on other computers
 on which TestStand is installed.

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Code Modules
- Search Directories
- Adding Users and Setting Privileges
- Creating Analysis Modules for Custom Rules
- Creating Rule Configuration Modules in the TestStand Sequence Analyzer
- Debugging Analysis Modules and Rule Configuration Modules
- TestStand Sequence Analyzer Application

Related tasks:

- Adding Rule Settings for Custom Rules in the TestStand Sequence Analyzer
- Deploying Custom Rules and Analysis Modules

Related information:

- Configure Sequence Analyzer Available Rules Dialog Box
- Edit Analysis Module Dialog Box
- Edit Rule Dialog Box
- LabVIEW Adapter Configuration Dialog Box
- Sequence Analyzer Options Dialog Box

<!--NI_TOPIC bundle=teststand path=creating-a-basic-user-interface-labview.html language=enus -->
## TOPIC 00204: Creating a Basic User Interface - LabVIEW

- bundle_id: `teststand`
- source_path: `creating-a-basic-user-interface-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-basic-user-interface-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example provides a simplified user interface to demonstrate the architecture of a TestStand user interface. The interface code demonstrates the following actions in a TestStand interface: Initialize the TestStand engine Provide functionality to TestStand controls by connecting them to m

### Creating a Basic User Interface - LabVIEW

#### Purpose

This example provides a simplified user interface to demonstrate the architecture of a TestStand user interface. The interface code demonstrates the following actions in a TestStand interface:

- Initialize the TestStand engine
- Provide functionality to TestStand controls by connecting them to manager controls
- Register callbacks to execute when TestStand events occur
- Shut down TestStand

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Creating a Basic User
 Interface\LabVIEW\Basic User Interface.lvproj

#### Highlighted Features

- TestStand User Interface Controls
- TestStand User Interface API

#### Major API

TestStand User Interface API

#### Prerequisites

You must have the LabVIEW Development System involved to execute this example.

#### How to Use This Example

Complete the following steps to run the example:

1. Click Run to start the user interface.
2. Notice that the control functionality matches the specified connections in the Configure Connections case.
3. Use the interface to open a sequence file and execute it. The execution displays in the executionView control if tracing is enabled.

Complete the following steps to review the sequences and steps in this example:

1. In Basic User Interface.lvproj, open TestStand Basic User interface.vi .
2. Select the Initialize case. In this case, references to the UI controls are stored in the UI data cluster, and this application is set as the main TestStand window.
3. Select the Configure Connections case. In this case, the TestStand UI controls are connected to manager controls to give them functionality. Refer to the in-line comments for more information.
4. Select the Register Event Callbacks case. This case specifies callback VIs that will execute when a TestStand event occurs. Refer to the in-line comments for more information.
5. Select the Handle Events case. This case handles LabVIEW specific events, such as closing the panel. Refer to the in-line comments for more information.
6. Select the Shutdown case. This case closes all references and closes the panel.

Parent topic:

Creating a Basic User Interface

Related concepts:

- TestStand Directory Structure
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=creating-a-basic-user-interface-labwindows-cv.html language=enus -->
## TOPIC 00205: Creating a Basic User Interface - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `creating-a-basic-user-interface-labwindows-cv.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-basic-user-interface-labwindows-cv.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example provides a simplified user interface to demonstrate the architecture of a TestStand user interface. The interface code demonstrates the following actions in a TestStand interface: Provide functionality to TestStand controls by connecting them to manager controls Register callbac

### Creating a Basic User Interface - LabWindows/CVI

#### Purpose

This example provides a simplified user interface to demonstrate the architecture of a TestStand user interface. The interface code demonstrates the following actions in a TestStand interface:

- Provide functionality to TestStand controls by connecting them to manager controls
- Register callbacks to execute when TestStand events occur

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Creating a Basic User
 Interface\CVI\Basic User Interface.prj

#### Highlighted Features

- TestStand User Interface Controls
- TestStand User Interface API

#### Major API

TestStand User Interface API

#### Prerequisites

You must have LabWindows/CVI installed to execute this example.

#### How to Use This Example

Complete the following steps to run the example:

1. (64-bit TestStand) Navigate to Build»Configuration and select Debug64 as the configuration.
2. Click Debug Project to start the user interface.
3. Notice that the control functionality matches the specified connections in the SetupActiveXControls function.
4. Use the interface to open a sequence file and execute it. The execution displays in the executionView control if tracing is enabled.

Complete the following steps to review the sequences and steps in this example:

1. In Basic User Interface.prj, open TestExec.c .
2. Find the SetupActiveXControls function. This function registers callback functions that will execute when a TestStand event occurs. Also, the TestStand UI controls are connected to manager controls to give them functionality. Refer to the in-line comments for more information.

Parent topic:

Creating a Basic User Interface

Related concepts:

- TestStand Directory Structure
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=creating-a-basic-user-interface-net.html language=enus -->
## TOPIC 00206: Creating a Basic User Interface - .NET

- bundle_id: `teststand`
- source_path: `creating-a-basic-user-interface-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-basic-user-interface-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example provides a simplified user interface to demonstrate the architecture of a TestStand user interface. The interface code demonstrates the following actions in a TestStand interface: Provide functionality to TestStand controls by connecting them to manager controls Register callbac

### Creating a Basic User Interface -
 .NET

#### Purpose

This example provides a simplified user interface to demonstrate the architecture of a TestStand user interface. The interface code demonstrates the following actions in a TestStand interface:

- Provide functionality to TestStand controls by connecting them to manager controls
- Register callbacks to execute when TestStand events occur

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Creating a Basic User
 Interface\DotNet\Basic User Interface.sln

#### Highlighted Features

- TestStand User Interface Controls
- TestStand User Interface API

#### Major API

TestStand User Interface API

#### Prerequisites

You must have Visual Studio installed to execute this example.

#### How to Use This Example

Complete the following steps to run the example:

1. Click Run to start the user interface.
2. Notice that the control functionality matches the specified connections in the MainForm_Load method.
3. Use the interface to open a sequence file and execute it. The execution displays in the executionView control if tracing is enabled.

Complete the following steps to review the sequences and steps in this example.

1. Open Basic User Interface.sln in Visual Studio, then right click MainForm.cs and select View Code.
2. Find the MainForm_Load method. Within this method, the TestStand UI controls are connected to manager controls to give them functionality. Refer to the in-line comments for more information.
3. Double click MainForm.cs to view the designer. Select the ApplicationManager control, then click Events in the properties pane. Notice that callback functions have been specified for certain TestStand events. Double click the event callback to view the callback code.

Parent topic:

Creating a Basic User Interface

Related concepts:

- TestStand Directory Structure
- TestStand API Overview

<!--NI_TOPIC bundle=teststand path=creating-a-basic-user-interface.html language=enus -->
## TOPIC 00207: Creating a Basic User Interface

- bundle_id: `teststand`
- source_path: `creating-a-basic-user-interface.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-basic-user-interface.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Modifying User Interfaces\Creating a Basic User Interface directory contains the following examples.

### Creating a Basic User Interface

The <TestStand
 Public>\Examples\Modifying User Interfaces\Creating a Basic User
 Interface directory contains the following examples.

- [Creating a Basic User Interface - LabWindows/CVI](creating-a-basic-user-interface-labwindows-cv.html)
- [Creating a Basic User Interface - LabVIEW](creating-a-basic-user-interface-labview.html)
- [Creating a Basic User Interface - .NET](creating-a-basic-user-interface-net.html)

Parent topic:

Examples for Modifying User Interfaces

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-a-deployable-image.html language=enus -->
## TOPIC 00208: Creating a Deployable Image

- bundle_id: `teststand`
- source_path: `creating-a-deployable-image.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-deployable-image.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Deployment Utility collects all the files the deployment requires into one directory called the deployable image, which contains the files and statically referenced dependencies you specify on the System Source tab. Creating a deployable image with the deployment utility helps you veri

### Creating a Deployable Image

The TestStand Deployment Utility collects all the files the deployment requires into one directory called the deployable image, which contains the files and statically referenced dependencies you specify on the System Source tab. Creating a deployable image with the deployment utility helps you verify that you include the required files and process the files before you build an installer or use a network drive or source code control system to deploy the files.

When you create a patch deployment, the deployment utility removes files from the patch deployable image that have not changed since the previous full or baseline patch deployment image.

#### Troubleshooting the Deployable Image

Use the deployment utility status log to diagnose any potential problems with the deployment. If the log has any errors or warnings, the help page displays information about the steps required to fix the issue.

Note

#### Directory Structure Differences between Source Distributions and Packed Project Library Distributions

You can include in the deployable image the source files necessary to rebuild packed project libraries, but doing so places the packed project library source files in a different directory structure from the default source distribution directory structure, as shown in the following figure.

[IMAGE alt='image' src='GUID-550E5E40-BC12-4C62-AA6A-32F038DD682D-a5.svg']

When you create a source distribution that contains packed project libraries, the deployment utility includes dependencies of the Packed Libraries, including other packed project libraries and shared libraries (DLLs), in the SubVI Location directory you specify in the LabVIEW VI Options dialog box.

When you create a packed project library distribution, the deployment utility automatically includes dependencies in the same top-level directory as the packed project library.

If you previously deployed a source distribution and then switch to using a packed project library distribution, the directory structure of the new deployment changes but the functionality remains the same. Typically, you do not need to make changes to the new deployment unless you are using a source code control system for distribution and rely on consistent locations of files for revision history information.

#### Default Image Directory of a Source Distribution

The default image directory of a source distribution includes the following directories and files:

Note

- The deployment utility can create additional directories depending on the destination subdirectory of the top-level files in the source distribution. Use the Distributed Files tab to change the destination subdirectory of top-level files.
- Patch deployments use the same image directory structure, and the deployment utility automatically removes any files the patch deployment does not require.

- Selected Installation Destination —Contains top-level files, such as VIs, sequences, LabVIEW projects, TestStand workspaces, and TestStand projects. Select a file on the Distributed Files tab of the deployment utility and use the Installation Destination option to specify this directory. Use the Installation Destination Subdirectory control to specify a subdirectory.
  - SubVI Location directory —Contains direct dependencies of the top-level VIs, including subVIs, DLLs, and libraries of the subVIs. You specify this directory in the SubVI Location option in the LabVIEW VI Options dialog box. Note If a direct dependency of a top-level VI is also a top-level file, such as when you call a DLL from a VI and also call the DLL from a step in a sequence, the deployment utility places the file in the path you specify in the Installation Destination Subdirectory control. The deployment utility also correctly links the VIs and sequences that call the file.
    - Data directory —Contains indirect dependencies of the top-level VIs, including libraries of top-level files and classes.
  - VIs for Project_Name directory —Contains top-level files for the project. If you consolidate projects, the deployment utility creates only one VIs for Projects directory in which to store all the top-level files for all projects.
    - SubVI Location directory —Uses the same name and structure as the top-level SubVI Location directory.
      - Data directory —Uses the same name and structure as the top-level Data directory.

#### Image Directory of a Packed Project Library Distribution

The image directory of a packed project library distribution includes the following directories and files:

Note

- Selected Installation Destination —Contains top-level files, such as packed project libraries, sequences, LabVIEW projects, TestStand workspaces, and TestStand projects. This directory also contains packed project library dependencies, such as DLLs called from VIs in the packed project library. Select a file on the Distributed Files tab of the deployment utility and use the Installation Destination option to specify this directory. Use the Installation Destination Subdirectory control to specify a subdirectory.
  - VIs for Project_Name directory —Contains top-level files for the project. If you consolidate projects, the deployment utility creates only one VIs for Projects directory in which to store all the top-level files for all projects.
  - Packed Project Library Source directory —Contains one LabVIEW project for each packed project library in the deployment and one readme file for each project. (LabVIEW 2012 SP1 or earlier) After the projects have been built in the Packed Project Library Source directory, this directory contains the packed project libraries generated by the projects with the same directory structure as the selected installation destination.
    - Source Files directory —Contains directories for each project.
      - VIs for Project_Name directory —Contains all the files added to the top-level library in the project, including top-level files, libraries of the top-level files, and other VIs in the libraries of the top-level files.
        - NI Top Level Library.lvlib , which is the top-level library for the deployment.
        - Support VIs directory —Contains dependencies of the top-level VIs in the project, including subVIs, DLLs, and libraries of the subVIs.
    - Builds directory —(LabVIEW 2013 or later) After the projects have been built in the Packed Project Library Source directory, this directory contains the packed project libraries generated by the projects with the same directory structure as the selected installation destination.

Parent topic:

Creating Deployments

Related concepts:

- Identifying Components to Deploy
- Preparing Source Components for Deployment
- Choosing a Deployment Mechanism
- Patching Deployments
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Deploying 32-bit TestStand and 64-bit TestStand Systems
- Deploying VIs in LabVIEW Packed Project Libraries
- Installer Issues for 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=creating-a-sequence-file-translator-dll.html language=enus -->
## TOPIC 00209: Creating a Sequence File Translator DLL

- bundle_id: `teststand`
- source_path: `creating-a-sequence-file-translator-dll.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-sequence-file-translator-dll.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand can load custom sequence files if an existing translator can read and convert the file into a TestStand SequenceFile object. Translators are Microsoft Windows DLLs you can create that export required C callback functions TestStand uses to translate files. You can create custom sequence fil

### Creating a Sequence File Translator DLL

TestStand can load custom sequence files if an existing translator can read and convert the file into a TestStand SequenceFile object. Translators are Microsoft Windows DLLs you can create that export required C callback functions TestStand uses to translate files.

You can create custom sequence file translators in any development environment that can create a
 Windows DLL with the required C callback functions. NI recommends using the
 translator examples written in LabVIEW, LabWindows/CVI, and Microsoft Visual C++ as
 a guide. Each example in the <TestStand
 Public>\Examples\Fundamentals\Sequence File Translators - Examples
 directory includes a template project, which contains source code with empty
 callback functions you must export from the translator DLL. You must add the
 necessary code to the required callbacks to ensure that the translator properly
 integrates with TestStand.

When an application loads the TestStand Engine, TestStand loads the DLLs that export the required callback functions from the <TestStand>\Components\Translators directory and the <TestStand Public>\Components\Translators directory. When you run a TestStand sequence file translator example, located in the <TestStand Public>\Components\Translators directory, the example copies the example translator DLL to the <TestStand Public>\Examples\Fundamentals\Sequence File Translators - Examples directory, and you must restart the application before you can use the translator.

\To create new translator DLLs, add the project for the translator in the <TestStand Public>\Components\Translators directory and ensure that the project saves the DLL to the <TestStand Public>\Components\Translators directory. Storing new and customized files in the <TestStand Public> directory ensures that newer installations of the same version of TestStand do not overwrite the customizations and ensures that uninstalling TestStand does not remove the files you customize.

A translator DLL can contain one or more translators. When TestStand loads a translator DLL, TestStand uses the callback functions of the DLL to obtain information about the translators the DLL contains. TestStand calls the CanTranslate callback function to determine whether the DLL contains a translator that recognizes a file. The callback returns the index of the translator that recognizes the file after examining the extension of the file and the contents of the file, typically the file header. Most of the callback functions the translator DLL implements contain an index parameter, which references a specific translator in the DLL that must operate on a file.

Parent topic:

Sequence File Translators

Related concepts:

- Example Sequence File Translators
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-a-subsequence-from-selected-steps.html language=enus -->
## TOPIC 00210: Creating a Subsequence from Selected Steps - Sequence File Window

- bundle_id: `teststand`
- source_path: `creating-a-subsequence-from-selected-steps.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-subsequence-from-selected-steps.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creating a Subsequence from Selected Steps You can create a new subsequence from selected steps in a sequence file. TestStand will replace the steps you select in the parent sequence with a Sequence Call step to call the new subsequence. TestStand will also create variables and update expressions fo

### Creating a Subsequence from Selected Steps - Sequence File Window

#### Creating a Subsequence from Selected Steps

You can create a new subsequence from selected steps in a sequence file. TestStand will
replace the steps you select in the parent sequence with a Sequence Call step to call the new subsequence.
TestStand will also create variables and update expressions for the new subsequence and will
delete Local variables that are no longer referenced by the remaining steps in the parent
sequence.

Note

Note

In the Steps Pane context menu, select New Subsequence from Steps. You can choose to
perform the operation With Preview or Without Preview. If you choose to preview the
operation, TestStand will launch the Preview dialog box, which contains the following options:

- Sequence Options —The Preview dialog box contains the following sequence options:
  - Subsequence Name —Specifies the name of the subsequence. A default name is
loaded when the dialog box launches.
  - Use Current Sequence File —This option is selected by default. When you select this
option, a new subsequence will be created in the current sequence file. You can
select a different sequence file in which to create the subsequence by unselecting this
option.
  - Sequence File Path —The pathname of the sequence file in which to create the new
subsequence.
  - Delete Locals No Longer Used In Parent Sequence —Deletes Local variables that are
no longer referenced by the remaining steps in the parent sequence. This option is
selected by default.
- Subsequence Options —The Preview dialog box contains the following subsequence options:
 
 Expanding a potential parameter displays auto-resolved references and/or possible
references:
  - Potential Parameters —Lists the potential parameters that will be created in the new
 sequence. A variable is listed as a potential parameter if that variable is referenced
 by the remaining steps in the parent sequence or if that variable belongs to the Parameters variable group in the parent sequence. Unchecking Use Current
 Sequence File and selecting a different sequence file path processes the variables in
 the File Globals variable group in the parent sequence and adds them as parameters
 if a variable is used by the selected steps.
  - Original Location —Displays the location of the selected parameter in the parent sequence.
 
 Note 

 Unchecking a variable in the potential parameter list moves the
variable to the original variable group (original location). If a variable’s
original variable group is Parameters, then unchecking is not allowed for
that variable.
  - Auto-Resolved References —Lists the references that can be resolved to the selected
variable at Edit time. The expressions in the referenced locations are updated to refer
to the selected variable.
  - Possible References —Lists the references that cannot be resolved to the selected
variable at Edit time and can only be resolved during runtime. Expressions in the
Possible References are editable.
  - Selected Reference Expression —Displays the expression in the selected location of
Auto-Resolved or Possible References.

Right-click on an auto-resolved reference or a possible reference to access the context menu. The context menu contains the following options, which are disabled by default:

- Revert —When you edit an expression that is listed as a possible reference, this option is enabled for that reference and any other related reference. Selecting this option reverts the expression to its original state (the state immediately following the creation of the subsequence), regardless of the number of edits you have made.
- Redo —This option is enabled if you choose to revert an edited expression. Selecting this option undoes the revert operation and restores the changes you made to the expression before you reverted to the original.

When you click OK, TestStand will create a sequence file for the new subsequence and move the steps you selected in the parent sequence into the subsequence. TestStand will also create any necessary variables and update expressions for the new subsequence. A Sequence Call step will be inserted in the parent sequence to call the new subsequence and pass appropriate parameters. If you selected the Delete Locals No Longer Used In Parent Sequence option, TestStand will delete Local variables in the parent sequence that are no longer referenced by the remaining steps.

Parent topic:

TestStand Sequence Editor

<!--NI_TOPIC bundle=teststand path=creating-a-user-interface-message-handler.html language=enus -->
## TOPIC 00211: Creating a User Interface Message Handler

- bundle_id: `teststand`
- source_path: `creating-a-user-interface-message-handler.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-a-user-interface-message-handler.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you create the TestStand Engine as an ActiveX control, the easiest way to handle user interface messages is to implement the UIMessageEvent callback sequence for the ActiveX control. Whenever the engine sends a user interface message for an application, the engine calls the callback with a UIMess

### Creating a User Interface Message Handler

If you create the TestStand Engine as an ActiveX control, the easiest way to handle user interface messages is to implement the UIMessageEvent callback sequence for the ActiveX control. Whenever the engine sends a user interface message for an application, the engine calls the callback with a UIMessage object as a parameter.

Note

UIMessage.Acknowledge

If you do not create the engine as an ActiveX control and are not using the TestStand User Interface (UI) Controls, you can handle user interface messages in the following two ways:

- When you can write a C-callable function in the application development environment (ADE), you can instruct the engine to call such a function by passing its address to the Engine.RegisterUIMessageCallbackEx method. The application thread that calls this method must regularly process Microsoft Windows messages to use this option.
- When the ADE cannot create C-callable functions, you must complete the following steps to create a polling loop for user interface messages. Tip One way to implement a polling loop in an application is to create a Timer callback that polls each time it executes.
  1. Inform the engine that you are polling by setting the Engine.UIMessagePollingEnabled property to True .
  2. Implement a polling loop by periodically checking the Engine.IsUIMessageQueueEmpty property.
  3. If the queue is not empty, call the Engine.GetUIMessage method to obtain the next user interface message from the engine. Do not check the queue again until you complete whatever action the user interface message requires and release all references to the UIMessage object.

Parent topic:

User Interface Messages (UIMessages)

<!--NI_TOPIC bundle=teststand path=creating-an-enumeration-data-type-and-definin.html language=enus -->
## TOPIC 00212: Creating an Enumeration Data Type and Defining the Enumerators

- bundle_id: `teststand`
- source_path: `creating-an-enumeration-data-type-and-definin.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-an-enumeration-data-type-and-definin.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a TestStand enumeration, go to the Types View in the TestStand Sequence Editor. In a sequence file of your choosing, go to Custom Data Types and right click to insert a type. From the context menu, select Insert Custom Data Type and choose Enumeration. Name the newly created data type Colo

### Creating an Enumeration Data Type and Defining the Enumerators

To create a TestStand enumeration, go to the Types View in the TestStand Sequence Editor. In a sequence file of your choosing, go to Custom Data Types and right click to insert a type. From the context menu, select Insert Custom Data Type and choose Enumeration. Name the newly created data type Color, for example. Note that the current state of the type Color is {Invalid} [] (0). The Color type currently has no enumerators, so its default value is invalid. This is one example of how a TestStand enumeration can end up in an invalid state.

Click the Edit Enumerators button next to Color to launch the Edit Enumerators dialog box.In the table control, define the following three enumerators:

| Red | 255 |
| --- | --- |
| Blue | 65280 |
| Green | 16711680 |

Note

0xff

0xff00

0xff0000

Click OK to commit these changes and close the dialog box. Notice that Color is no longer invalid and has a default value of Red. The underlying numeric value of 255 is displayed in parentheses for convenience.

Since hexadecimal is more convenient for this example, change the numeric format. Right click on the type definition. In the context menu, choose Numeric Format to launch the Numeric Format dialog box. Change the type to Hexadecimal and click OK. Note that the number in parentheses is now displayed in hexadecimal format.

Parent topic:

Getting Started Creating a TestStand Enumeration

<!--NI_TOPIC bundle=teststand path=creating-an-enumeration-instance.html language=enus -->
## TOPIC 00213: Creating an Enumeration Instance

- bundle_id: `teststand`
- source_path: `creating-an-enumeration-instance.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-an-enumeration-instance.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Variables View for a sequence, under Locals, right click to launch the context menu. Choose Insert Local»Type»Color to create an instance of the Color enumeration. The instance has the same default value and numeric format as the type definition. You can edit the value of this instance just l

### Creating an Enumeration Instance

In the Variables View for a sequence, under Locals, right click to launch the context menu. Choose InsertLocal»Type»Color to create an instance of the Color enumeration. The instance has the same default value and numeric format as the type definition. You can edit the value of this instance just like the type definition by selecting one of the enumerators from the value drop-down or by launching the Edit Enumeration Value dialog box.

Note

Insert Local»Enumeration

Parent topic:

Getting Started Creating a TestStand Enumeration

<!--NI_TOPIC bundle=teststand path=creating-analysis-modules-for-custom-rules.html language=enus -->
## TOPIC 00214: Creating Analysis Modules for Custom Rules

- bundle_id: `teststand`
- source_path: `creating-analysis-modules-for-custom-rules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-analysis-modules-for-custom-rules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends that you copy an analysis module template from the <TestStand>\Components\Analyzer\Templates\<Environment> directory to the <TestStand Public>\Components\Analyzer\<YourRuleName> directory, where <Environment> is LabVIEW, CVI, CSharp, or VC, or LabVIEW NXG and <YourRuleName> is the desc

### Creating Analysis Modules for Custom Rules

NI recommends that you copy an analysis module template from the
 <TestStand>\Components\Analyzer\Templates\<Environment>
 directory to the <TestStand
 Public>\Components\Analyzer\<YourRuleName>
 directory, where <Environment> is LabVIEW,
 CVI, CSharp, or VC, or
 LabVIEW NXG and <YourRuleName> is the
 descriptive name or the unique ID of the custom rule. NI recommends also using your
 company name as part of the directory name to avoid potential conflicts with other
 custom analysis modules. After you copy the template files, search for the text
 Template in each source file and follow the instructions in the
 file.

- [Prototypes for Analysis Modules](prototypes-for-analysis-modules.html)
- [Implementing Analysis Modules](implementing-analysis-modules.html)

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Search Directories
- Accessing Rule Configuration Data in Rule Configuration Modules and Analysis Modules
- Accessing Rule Settings in Analysis Modules
- Debugging Analysis Modules and Rule Configuration Modules

Related tasks:

- Creating Custom Rules in the TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand path=creating-and-customizing-code-template-files.html language=enus -->
## TOPIC 00215: Creating and Customizing Code Template Files

- bundle_id: `teststand`
- source_path: `creating-and-customizing-code-template-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-and-customizing-code-template-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click the Create button on the Code Templates tab of the Step Type Properties dialog box to launch the Create Code Templates dialog box. TestStand copies the files for the existing code template you select into a new subdirectory in the <TestStand Public>\CodeTemplates directory based on the code te

### Creating and Customizing Code Template Files

Click the Create button on the Code Templates tab of the Step Type Properties dialog box to launch the Create Code Templates dialog box.

TestStand copies the files for the existing code template you select into a new subdirectory in the <TestStand Public>\CodeTemplates directory based on the code template name you specified in the Create Code Templates dialog box. You can then customize the code template files in the new <TestStand Public>\CodeTemplates directory.

For example, you can include example code that shows users how to access the custom properties of the step. For most environments, you can add a value parameter to pass the information from TestStand. You can also show how to obtain the high- and low-limit properties in a LabVIEW or LabWindows/CVI code template for a Numeric Limit Test step by customizing the prototype for the code module to specify the high and low limits as value parameters. As another example, you might want to show how to return a measurement value from a code module. For the LabVIEW, LabWindows/CVI, and C/C++ DLL Adapters, you can customize the prototype in the code template by specifying the measurement as a reference parameter.

Parent topic:

Custom Step Types

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- Organizing Test Program Files with LabVIEW-Built Shared Libraries

<!--NI_TOPIC bundle=teststand path=creating-and-deleting-users-using-api.html language=enus -->
## TOPIC 00216: Creating and Deleting Users Using API

- bundle_id: `teststand`
- source_path: `creating-and-deleting-users-using-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-and-deleting-users-using-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to programmatically create and delete users. Example File Location <TestStand Public>\Examples\TestStand API\Creating & Deleting Users Using API\Creating & Deleting Users Using API.seq Highlighted Features User management Major API Engine.GetUserGroup Engine.New

### Creating and Deleting Users Using API

#### Purpose

This example demonstrates how to programmatically create and delete users.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Creating & Deleting Users Using
 API\Creating & Deleting Users Using API.seq

#### Highlighted Features

- User management

#### Major API

- Engine.GetUserGroup
- Engine.NewUser
- Engine.UserNameExists
- Engine.UsersFile
- PropertyObject.SetPropertyObjectByOffset
- PropertyObject.SetValStringByOffset
- UsersFile.UserList

#### Prerequisites

You must be logged into TestStand as a user with administrator privileges.

#### How to Use This Example

Complete the following steps to review the sequences and steps in this example.

1. On the Steps pane of the MainSequence , select the Create or Delete a User step.
2. On the Step Settings pane, click the Text and Buttons tab. When you run the sequence, you select whether you want to create a user or delete a user. The If and Else steps call the Create User sequence or Delete User sequence, depending on which option you select.
3. On the Sequences pane, select the Create User sequence, which specifies the following functionality:
  1. The Get New User Name step prompts for a new user name.
  2. The If step uses the Engine.UserNameExists method to determine whether the user name already exists. If the user name does not exist, the user is created.
  3. The Select User Group step in the If structure prompts you to select a group for the user.
  4. A series of Statement steps perform API calls to create the new user and increment the change count of the user file.
4. On the Steps pane, select each Statement step one at a time and click the Expression edit tab on the Step Settings pane to review the expression each step uses. The steps use the Engine.NewUser method to create the new user, the UsersFile.UserList property and PropertyObject.SetPropertyObjectByOffset method to insert the new user in the user list, and the Engine.GetUserGroup method and PropertyObject.SetValStringByOffset method to add the user to a group.
5. On the Sequences pane, select the Delete User sequence, which specifies the following functionality:
  1. The Get User Names step, which is a Sequence Call step, calls a subsequence to generate an array of all user names in the user list.
  2. In the If structure, the Delete User sequence verifies that more than one user exists so that you cannot delete the only user and become locked out of TestStand.
  3. The Delete User sequence stores the user name to delete in a local variable before the user is actually deleted and removed from any groups.
  4. A Statement step increments the change count of the user file.
6. On the Steps pane of the MainSequence , select the Save Users File step.
7. On the Step Settings pane, click the Text and Buttons tab. When you run the sequence and have selected whether to create a new user or delete a user, the precondition evaluates whether the Users file has been modified. If the file has been modified, the step prompts you to save the changes. If you select No , TestStand reflects the changes in the User Manager but does not save the changes.

Complete the following steps to run the example.

1. On the Sequences pane, select the MainSequence .
2. Select Execute»Run MainSequence to run the sequence.
3. In the Create or Delete a User dialog box, click Create User .
4. In the New User Name dialog box, enter a name for the new user and click OK .
5. In the User Group dialog box, select any group for the new user.
6. In the Save the Modified Users File dialog box, select whether you want to save the changes made to the User file.
7. Select Execute»Restart to run the sequence again.
8. In the Create or Delete a User dialog box, click Delete User .
9. In the Select User dialog box, select the new user you created in step 4.
10. In the Save the Modified Users File dialog box, select whether you want to save the changes made to the User file.

Parent topic:

Examples for the TestStand API

Related concepts:

- TestStand Directory Structure
- Managing Users
- Privileges

<!--NI_TOPIC bundle=teststand path=creating-custom-data-types.html language=enus -->
## TOPIC 00217: Creating Custom Data Types

- bundle_id: `teststand`
- source_path: `creating-custom-data-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-custom-data-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create a custom data type. On the Types pane of the Types window, expand the Custom Data Types section. Right-click and select Insert Custom Data Type from the context menu. You can also use the Copy and Paste context menu items to copy and rename an existing data typ

### Creating Custom Data Types

Complete the following steps to create a custom data type.

1. On the Types pane of the Types window, expand the Custom Data Types section.
2. Right-click and select Insert Custom Data Type from the context menu. You can also use the Copy and Paste context menu items to copy and rename an existing data type.
3. Select the data type you want from the submenu. When you select the Container type from the submenu, TestStand creates the data type without any fields in which you can insert additional data types.
4. Right-click the new data type and select Properties from the context menu to launch the Type Properties dialog box, in which you can specify the version number of the type and how to pass the data type to LabVIEW, LabWindows/CVI, and .NET code modules.

When you create new data types, use unique names to avoid conflicts with the default names TestStand uses and names other companies and users create. For example, begin new custom data type names with a unique ID, such as a company prefix.

Parent topic:

Data Types

Related concepts:

- Creating Instances of Data Types
- Type Palette Files

Related information:

- Types Window

<!--NI_TOPIC bundle=teststand path=creating-custom-step-types-that-call-vis-for.html language=enus -->
## TOPIC 00218: Creating Custom Step Types that Call VIs for Substeps

- bundle_id: `teststand`
- source_path: `creating-custom-step-types-that-call-vis-for.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-custom-step-types-that-call-vis-for.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a custom step type that defines a Pre-Step, Post-Step, or Edit substep that calls a VI, you must create a source distribution to ensure that TestStand can resolve the file paths to all the dependencies of the VI when TestStand executes the custom step type. If you created the VI usin

### Creating Custom Step Types that Call VIs for Substeps

When you create a custom step type that defines a Pre-Step, Post-Step, or Edit substep that calls a VI, you must create a source distribution to ensure that TestStand can resolve the file paths to all the dependencies of the VI when TestStand executes the custom step type. If you created the VI using LabVIEW 2010 or later, you can create a LabVIEW packed project library to consolidate all dependencies into a single file that the step type calls.

When you create a source distribution or packed project library, NI recommends that you enable
 the Always Run VI in LabVIEW Run-Time option in the LabVIEW
 Advanced Settings window in the TestStand Sequence Editor or on the Advanced
 Settings tab of the Edit LabVIEW VI Call dialog box in a TestStand User Interface to
 ensure that the VIs execute in the correct version of the LabVIEW Run-Time
 Engine.

If you do not create a source distribution or packed project library, LabVIEW browses its search directories to resolve the file paths to all the dependencies of the VI, which might break the VI.

Note

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Creating Custom Step Types
- Using Substeps
- Search Directories
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Building a TestStand Deployment with LabVIEW

<!--NI_TOPIC bundle=teststand path=creating-custom-step-types.html language=enus -->
## TOPIC 00219: Creating Custom Step Types

- bundle_id: `teststand`
- source_path: `creating-custom-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-custom-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create a custom step type. On the Types pane of the Types window, expand the Step Types section. Right-click and select Insert Step Type from the context menu. You can also use the Copy and Paste context menu items to copy and rename an existing step. When you create

### Creating Custom Step Types

Complete the following steps to create a custom step type.

1. On the Types pane of the Types window, expand the Step Types section.
2. Right-click and select Insert Step Type from the context menu. You can also use the Copy and Paste context menu items to copy and rename an existing step. When you create new step types, use unique names to avoid conflicts with the default names TestStand uses. For example, begin new custom step type names with a unique ID, such as a company prefix.
3. Right-click the new step and select Properties from the context menu to launch the Step Type Properties dialog box.
4. Click the Menu tab and specify the menu item name for the new step.
5. Click the General tab and specify the default name for new steps you create from the new type and specify the description expression for those steps.
6. Click the Substeps tab and select an adapter.
7. Click Add and select the type of step to create substeps. Use the Substep Info section on the Substeps tab to specify the menu item name of Edit steps.

Note

Parent topic:

Custom Step Types

<!--NI_TOPIC bundle=teststand path=creating-custom-user-interfaces.html language=enus -->
## TOPIC 00220: Creating Custom User Interfaces

- bundle_id: `teststand`
- source_path: `creating-custom-user-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-custom-user-interfaces.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create or customize a user interface application, including custom sequence editors and applications that can only run sequences. Refer to the following topics before you create a custom user interface application: Example User Interfaces Writing an Application with the TestStand UI Controls

### Creating Custom User Interfaces

You can create or customize a user interface application, including custom sequence editors and applications that can only run sequences.

Refer to the following topics before you create a custom user interface application:

- Example User Interfaces
- Writing an Application with the TestStand UI Controls
- TestStand ActiveX API Overview
- Core UI Classes, Properties, Methods, and Events
- Core API Classes, Properties, and Methods
- Using TestStand UI Controls in LabVIEW
- Using TestStand UI Controls in LabWindows/CVI

Refer to the following TestStand documents for more information about creating and using custom user interfaces with LabVIEW or LabWindows/CVI.

- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- The NI TestStand User Interface Controls Reference Poster

Refer to the following sources for general instructions for creating a user interface application with an environment other than LabVIEW or LabWindows/CVI.

- Programming with the TestStand API in Different Languages

Parent topic:

Extending TestStand

Related concepts:

- Example User Interfaces
- Writing an Application with the TestStand User Interface Controls
- TestStand ActiveX API Overview
- Using TestStand UI Controls in LabVIEW
- Using TestStand UI Controls in LabWindows/CVI
- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- Programming with the TestStand API in Different Languages

<!--NI_TOPIC bundle=teststand path=creating-deployments.html language=enus -->
## TOPIC 00221: Creating Deployments

- bundle_id: `teststand`
- source_path: `creating-deployments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-deployments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a full or patch deployment, the TestStand Deployment Utility completes the following tasks: Analyzes the test system to generate a list of source files and dependencies. Creates a deployable image by copying the list of files generated during analysis to a directory hierarchy under a

### Creating Deployments

[IMAGE alt='image' src='GUID-04ECCD86-7732-4745-836A-1A666FE0FEEE-a5.svg']

When you create
 a full or patch deployment, the TestStand Deployment Utility completes the
 following tasks:

- Analyzes
 the test system to generate a list of source files and
 dependencies.
- Creates a
 deployable image by copying the list of files generated during
 analysis to a directory hierarchy under a single root directory.
- (Optional) Builds an installer or package distribution that contains all the files from the
 deployable image and NI drivers and other third-party components.

You can create a patch deployment at any
 point after the full deployment creation process. When you change to patch
 deployment mode, options in the deployment utility might change as well.

Note

.tsd

Parent topic:

Deployment Process Overview

Related concepts:

- Patching Deployments
- Analyzing the Test System
- Creating a Deployable Image
- Building a Customized MSI-based Installer

<!--NI_TOPIC bundle=teststand path=creating-editor-applications.html language=enus -->
## TOPIC 00222: Creating Editor Applications

- bundle_id: `teststand`
- source_path: `creating-editor-applications.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-editor-applications.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must enable the Editor Mode for the TestStand User Interface (UI) Controls to create an Editor application. Set the ApplicationMgr.IsEditor property at edit time to specify whether Editor Mode is on or off by default. Alternatively, you can set the ApplicationMgr.IsEditor property in the applica

### Creating Editor Applications

You must enable the Editor Mode for the TestStand User Interface (UI) Controls to create an Editor application.

Set the ApplicationMgr.IsEditor property at edit time to specify whether Editor Mode is on or off by default. Alternatively, you can set the ApplicationMgr.IsEditor property in the application source code before you call the ApplicationMgr.Start method.

You can pass a command-line argument to override the default editing mode for the application. Pass /editor to set the ApplicationMgr.IsEditor property and pass /operatorInterface to clear the ApplicationMgr.IsEditor property. Set the ApplicationMgr.CommandLineCanChangeEditMode property to False to prevent users from changing the ApplicationMgr.IsEditor property from the command line.

The full-featured user interface examples allow users with sequence file editing permissions to
 toggle the editing mode by pressing <Ctrl-Alt-Shift-Insert>. To change or
 disable this keystroke in an application based on a full-featured example, set the
 ApplicationMgr.EditModeShortcutKey and
 ApplicationMgr.EditModeShortcutModifier properties in the
 designer or in the user interface source code.

Parent topic:

Editor Versus Operator Interface Applications

Related concepts:

- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=creating-independent-patch-deployments.html language=enus -->
## TOPIC 00223: Creating Independent Patch Deployments

- bundle_id: `teststand`
- source_path: `creating-independent-patch-deployments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-independent-patch-deployments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Deployment Utility does not support creating independent patch deployments that install side-by-side, as shown in the following figure. NI does not support independent patch deployments for the following reasons: Independent patch deployments contain only the items you define and do no

### Creating Independent Patch Deployments

The TestStand Deployment Utility does not
 support creating independent patch deployments that install side-by-side, as shown
 in the following figure.

[IMAGE alt='image' src='GUID-B1ADDC2E-8F42-4202-944C-5533CBAFCAE8-a5.svg']

NI does not support independent patch deployments for the
 following reasons:

- Independent patch deployments contain only the items you define and do not
 automatically contain all the updates from previous deployments.
- Installers for independent patch deployments do not include dependencies on
 other installers for patch deployments, which means that users can determine
 which independent patch deployments to install and the order in which to install
 them.
- It can be difficult to maintain test system functionality when independent patch
 deployments share files with previous patch deployments because for each shared
 file, the independent patch deployment must include all the changes made in
 previous patch deployments to ensure that the test station continues to operate
 correctly.
- Using independent patch deployments can create significant testing burdens
 because for each independent patch deployment, you must test each permutation of
 installation order.

NI recommends creating dependency patch deployments to enforce installation
 order, which can also reduce testing requirements.

Parent topic:

Patching Deployments

Related concepts:

- Patching Deployments

<!--NI_TOPIC bundle=teststand path=creating-instances-of-data-types.html language=enus -->
## TOPIC 00224: Creating Instances of Data Types

- bundle_id: `teststand`
- source_path: `creating-instances-of-data-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-instances-of-data-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The context menu of each window or pane in which you can insert a variable, parameter, or property includes an Insert item, as listed in the following table. Context Menu Item Local of Context Menu Item Inserted Insert File Global File Globals section of the Variables pane in the Sequence File windo

### Creating Instances of Data Types

The context menu of each window or pane in which you can insert a variable, parameter, or property includes an Insert item, as listed in the following table.

| Context Menu Item | Local of Context Menu | Item Inserted |
| --- | --- | --- |
| Insert File Global | File Globals section of the Variables pane in the Sequence File window | Sequence file global variable |
| Insert Parameter | Parameters section of the Variables pane in the Sequence File window | Sequence parameter |
| Insert Local | Locals section of the Variables pane in the Sequence File window | Sequence local variable |
| Insert Station Global | Station Globals window | Station global variable |
| Insert UserInsert Group | User Manager window | New object with the User data type |
| Insert Field | Types window | New element in an existing data type |

With the exception of the Insert User and Insert Group items, all the context menu items in the preceding table provide a submenu from which you can select the following categories of data types:

- Basic types, such as number, string, Boolean, and object reference.
- The Container type, in which you can insert subproperties of any type. Note You can use an empty container as a parameter when you want to pass an object of any type to the sequence, in which case you also must turn off type checking for the parameter.
- Named data types, including all the custom named data types in type palette files or in the file you are currently editing. The submenu also includes standard TestStand named data types, such as Error, CommonResults, Path, Expression, and NI_TDMSReference.
- An array of elements of one of the types described above.

You can also create a new, custom data type in the Types window and then select the new data type from the Type submenu of the Insert context menu.

Parent topic:

Data Types

Related concepts:

- Using Standard Named Data Types
- NI_TDMSReference
- Creating and Deleting Users Using API

<!--NI_TOPIC bundle=teststand path=creating-new-properties-using-api-labview.html language=enus -->
## TOPIC 00225: Creating New Properties Using API - LabVIEW

- bundle_id: `teststand`
- source_path: `creating-new-properties-using-api-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-new-properties-using-api-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with man

### Creating New Properties Using API - LabVIEW

#### Purpose

This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with many objects in TestStand, including step properties and variables.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Creating New Properties Using
 API\LabVIEW\Creating New Properties Using API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.NewPropertyObject
- PropertyObject.NewSubProperty
- PropertyObject.InsertSubProperty
- PropertyObject.SetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant
- PropertyObject.SetFlags

#### Prerequisites

Report generation should be enabled in order to see the result of adding a PropertyObject to the Result container of a step.

#### How to Use This
 Example

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. TestStand will display Message Popups to explain each section of the example.
 After each section completes, the execution will automatically break to allow
 you to observe the results of each approach.
3. When you are ready to continue execution, simply click the green
 Resume button on the debug toolbar.
4. After execution completes, examine the report to observe the results of the
 final section, where a PropertyObject named SpecialResults was added to a step’s
 Result container.

Complete the following steps to review the sequences and steps in this
 example:

1. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps corresponding to the different
 approaches demonstrated in this example.
2. On the Sequences pane, select the Create New
 PropertyObject sequence. This sequence uses the
 Engine.NewPropertyObject and PropertyObject.InsertSubProperty API calls to
 create a new PropertyObject and insert it into the Locals container as a new
 Local variable. Although this method of creating PropertyObjects is less common
 than other approaches, it is included for completeness.
3. On the Sequences pane, select the SetVal Methods 
 sequence. This sequence uses the PropertyObject.SetValString,
 PropertyObject.SetValNumber, and
 PropertyObject.SetValBoolean methods to create
 PropertyObjects and insert them as Local variables. This approach allows you to
 create and assign a value to a PropertyObject with a single API call.
4. On the Sequences pane, select the Create New Container 
 sequence. This sequence demonstrates a method of creating complex container
 structures with the SetVal methods. The PropertyObject.NewSubProperty
 method is used to create a container field for error data, which is
 a defined type in the TestStand Types pane. Additionally, this sequence uses a
 PropertyObject.NewSubProperty method call to create an
 array and assigns a value to that array using the
 PropertyObject.SetValVariant method.
5. On the Sequences pane, select the Insert PropertyObject Into Step
 Results sequence. This sequence creates a new PropertyObject and
 inserts it into the step’s Result container. The PropertyObject.SetFlags
 TestStand API method is used to mark this PropertyObject to be included in the
 report generated after execution. This demonstrates a common use case for
 creating new PropertyObjects in a test sequence.

Parent topic:

Creating New Properties Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-new-properties-using-api-labwindows.html language=enus -->
## TOPIC 00226: Creating New Properties Using API - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `creating-new-properties-using-api-labwindows.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-new-properties-using-api-labwindows.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with man

### Creating New Properties Using API - LabWindows/CVI

#### Purpose

This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with many objects in TestStand, including step properties and variables.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Creating New Properties Using
 API\CVI\Creating New Properties Using API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.NewPropertyObject
- PropertyObject.NewSubProperty
- PropertyObject.InsertSubProperty
- PropertyObject.SetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant
- PropertyObject.SetFlags

#### Prerequisites

Report generation should be enabled in order to see the result of adding a PropertyObject to the Result container of a step.

#### How to Use This
 Example

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. TestStand will display Message Popups to explain each section of the example.
 After each section completes, the execution will automatically break to allow
 you to observe the results of each approach.
3. When you are ready to continue execution, simply click the green
 Resume button on the debug toolbar.
4. After execution completes, examine the report to observe the results of the
 final section, where a PropertyObject named SpecialResults was added to a step’s
 Result container.

Complete the following steps to review the sequences and steps in this
 example:

1. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps corresponding to the different
 approaches demonstrated in this example.
2. On the Sequences pane, select the Create New
 PropertyObject sequence. This sequence uses the
 Engine.NewPropertyObject and PropertyObject.InsertSubProperty API calls to
 create a new PropertyObject and insert it into the Locals container as a new
 Local variable. Although this method of creating PropertyObjects is less common
 than other approaches, it is included for completeness.
3. On the Sequences pane, select the SetVal Methods 
 sequence. This sequence uses the PropertyObject.SetValString,
 PropertyObject.SetValNumber, and
 PropertyObject.SetValBoolean methods to create
 PropertyObjects and insert them as Local variables. This approach allows you to
 create and assign a value to a PropertyObject with a single API call.
4. On the Sequences pane, select the Create New Container 
 sequence. This sequence demonstrates a method of creating complex container
 structures with the SetVal methods. The
 PropertyObject.NewSubProperty method is used to create a
 container field for error data, which is a defined type in the TestStand Types
 pane. Additionally, this sequence uses a
 PropertyObject.NewSubProperty method call to create an
 array and assigns a value to that array using the
 PropertyObject.SetValVariant method.
5. On the Sequences pane, select the Insert PropertyObject Into Step
 Results sequence. This sequence creates a new PropertyObject and
 inserts it into the step’s Result container. The PropertyObject.SetFlags
 TestStand API method is used to mark this PropertyObject to be included in the
 report generated after execution. This demonstrates a common use case for
 creating new PropertyObjects in a test sequence.

Parent topic:

Creating New Properties Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-new-properties-using-api-net.html language=enus -->
## TOPIC 00227: Creating New Properties Using API - .NET

- bundle_id: `teststand`
- source_path: `creating-new-properties-using-api-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-new-properties-using-api-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with man

### Creating New Properties Using API - .NET

#### Purpose

This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with many objects in TestStand, including step properties and variables.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Creating New Properties Using
 API\DotNet\Creating New Properties Using API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.NewPropertyObject
- PropertyObject.NewSubProperty
- PropertyObject.InsertSubProperty
- PropertyObject.SetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant
- PropertyObject.SetFlags

#### Prerequisites

Report generation should be enabled in order to see the result of adding a PropertyObject to the Result container of a step.

#### How to Use This
 Example

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. TestStand will display Message Popups to explain each section of the example.
 After each section completes, the execution will automatically break to allow
 you to observe the results of each approach.
3. When you are ready to continue execution, simply click the green
 Resume button on the debug toolbar.
4. After execution completes, examine the report to observe the results of the
 final section, where a PropertyObject named SpecialResults was added to a step’s
 Result container.

Complete the following steps to review the sequences and steps in this
 example:

1. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps corresponding to the different
 approaches demonstrated in this example.
2. On the Sequences pane, select the Create New
 PropertyObject sequence. This sequence uses the
 Engine.NewPropertyObject and PropertyObject.InsertSubProperty API calls to
 create a new PropertyObject and insert it into the Locals container as a new
 Local variable. Although this method of creating PropertyObjects is less common
 than other approaches, it is included for completeness.
3. On the Sequences pane, select the SetVal Methods 
 sequence. This sequence uses the PropertyObject.SetValString,
 PropertyObject.SetValNumber, and
 PropertyObject.SetValBoolean methods to create
 PropertyObjects and insert them as Local variables. This approach allows you to
 create and assign a value to a PropertyObject with a single API call.
4. On the Sequences pane, select the Create New Container 
 sequence. This sequence demonstrates a method of creating complex container
 structures with the SetVal methods. The
 PropertyObject.NewSubProperty method is used to create a
 container field for error data, which is a defined type in the TestStand Types
 pane. Additionally, this sequence uses a
 PropertyObject.NewSubProperty method call to create an
 array and assigns a value to that array using the
 >PropertyObject.SetValVariant method.
5. On the Sequences pane, select the Insert PropertyObject Into Step
 Results sequence. This sequence creates a new PropertyObject and
 inserts it into the step’s Result container. The PropertyObject.SetFlags
 TestStand API method is used to mark this PropertyObject to be included in the
 report generated after execution. This demonstrates a common use case for
 creating new PropertyObjects in a test sequence.

Parent topic:

Creating New Properties Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-new-properties-using-api-teststand-e.html language=enus -->
## TOPIC 00228: Creating New Properties Using API - TestStand Expressions

- bundle_id: `teststand`
- source_path: `creating-new-properties-using-api-teststand-e.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-new-properties-using-api-teststand-e.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with man

### Creating New Properties Using API - TestStand Expressions

#### Purpose

This example demonstrates how to use the TestStand API to create and assign values to PropertyObjects. With the exception of the TestStand Engine, any object in TestStand can be accessed as a PropertyObject. This arrangement allows the methods demonstrated in this example to be used with many objects in TestStand, including step properties and variables.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Creating New Properties Using
 API\TestStand Expressions\Creating New Properties Using
 API.seq

#### Highlighted Features

- TestStand API

#### Major API

- Engine.NewPropertyObject
- PropertyObject.NewSubProperty
- PropertyObject.InsertSubProperty
- PropertyObject.SetValString
- PropertyObject.SetValNumber
- PropertyObject.SetValBoolean
- PropertyObject.SetValVariant
- PropertyObject.SetFlags

#### Prerequisites

Report generation should be enabled in order to see the result of adding a PropertyObject to the Result container of a step.

#### How to Use This
 Example

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. TestStand will display Message Popups to explain each section of the example.
 After each section completes, the execution will automatically break to allow
 you to observe the results of each approach.
3. When you are ready to continue execution, simply click the green
 Resume button on the debug toolbar.
4. After execution completes, examine the report to observe the results of the
 final section, where a PropertyObject named SpecialResults was added to a step’s
 Result container.

Complete the following steps to review the sequences and steps in this
 example:

1. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps corresponding to the different
 approaches demonstrated in this example.
2. On the Sequences pane, select the Create New
 PropertyObject sequence. This sequence uses the
 Engine.NewPropertyObject and PropertyObject.InsertSubProperty API calls to
 create a new PropertyObject and insert it into the Locals container as a new
 Local variable. Although this method of creating PropertyObjects is less common
 than other approaches, it is included for completeness.
3. On the Sequences pane, select the SetVal Methods 
 sequence. This sequence uses the PropertyObject.SetValString,
 PropertyObject.SetValNumber, and
 PropertyObject.SetValBoolean methods to create
 PropertyObjects and insert them as Local variables. This approach allows you to
 create and assign a value to a PropertyObject with a single API call.
4. On the Sequences pane, select the Create New Container 
 sequence. This sequence demonstrates a method of creating complex container
 structures with the SetVal methods. The
 PropertyObject.NewSubProperty method is used to create a
 container field for error data, which is a defined type in the TestStand Types
 pane. Additionally, this sequence uses a
 PropertyObject.NewSubProperty method call to create an
 array and assigns a value to that array using the
 PropertyObject.SetValVariant method.
5. On the Sequences pane, select the Insert PropertyObject Into Step
 Results sequence. This sequence creates a new PropertyObject and
 inserts it into the step’s Result container. The PropertyObject.SetFlags
 TestStand API method is used to mark this PropertyObject to be included in the
 report generated after execution. This demonstrates a common use case for
 creating new PropertyObjects in a test sequence.

Parent topic:

Creating New Properties Using API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-new-properties-using-api.html language=enus -->
## TOPIC 00229: Creating New Properties Using API

- bundle_id: `teststand`
- source_path: `creating-new-properties-using-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-new-properties-using-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\TestStand API\Creating New Properties Using API directory contains the following examples.

### Creating New Properties Using API

The <TestStand
 Public>\Examples\TestStand API\Creating New Properties Using
 API directory contains the following examples.

Parent topic:

Examples for the TestStand API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-process-model-plug-ins.html language=enus -->
## TOPIC 00230: Creating Process Model Plug-ins

- bundle_id: `teststand`
- source_path: `creating-process-model-plug-ins.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-process-model-plug-ins.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Process model plug-in sequence files must meet the following conditions: You must save the model plug-in sequence files in one of the following directories:<TestStand>\Components\Models\ModelPlugins (built-in plug-ins)<TestStand Public>\Components\Models\ModelPlugins (custom plug-ins)<TestStand>\Com

### Creating Process Model Plug-ins

Process model plug-in sequence files must meet the following conditions:

- You must save the model plug-in sequence files in one of the following directories:
  - <TestStand>\Components\Models\ModelPlugins (built-in plug-ins)
  - <TestStand Public>\Components\Models\ModelPlugins (custom plug-ins)
  - <TestStand>\Components\Models\ModelPlugins\Addons (built-in add-ons)
  - <TestStand Public>\Components\Models\ModelPlugins\Addons (custom add-ons)
- You must include a file global variable named ModelPluginComponentDescription of type NI_ModelPluginComponentDescription
- You must select Model from the Type ring control on the Advanced tab of the Sequence File Properties dialog box for the model plug-in sequence file
- You must include one or more plug-in entry point sequences in the model plug-in sequence file

TestStand uses the location of the sequence file and the existence of the ModelPluginComponentDescription file global variable to identify plug-ins. Because TestStand loads and inspects all the sequence files within the top level of the ModelPlugins directories and of the ModelPlugins\Addons directories, you must place any supporting sequence files that a model plug-in calls in a different directory.

NI recommends that you use a unique prefix that includes your company name, such as
 Acme_ReportGenerator.seq, for custom plug-ins you create.
 TestStand uses the root filename as a <plug-in name> prefix
 for plug-in data types it creates, such as
 Acme_ReportGeneratorOptions. NI also recommends that you store
 any support files the plug-in requires in a subdirectory with the same name as the
 plug-in file, such as
 ModelPlugins\Acme_ReportGenerator\Acme_ReportGenerator_Support.seq.

Complete the following steps to generate a new plug-in that you can modify.

1. Select Configure»Result Processing to launch the Result Processing dialog box.
2. Enable the Show More Options option and click the Advanced button to launch the Advanced Result Processing Settings dialog box.
3. Click the Create New Process Model Plug-in button.
4. Use a unique filename that includes your company name as a prefix for the plug-in, such as Acme_ReportGenerator.seq .
5. Click Save to create and load the new plug-in sequence file. TestStand creates and adds the following new data types to the file. The data types are empty containers in which you can add plug-in-specific properties.
  - <plug-in name> Options
  - <plug-in name> AdditionalOptions
  - <plug-in name> RuntimeVariables
  - <plug-in name> PerSocketRuntimeVariables
6. Close the open dialog boxes to view and edit the plug-in you just created.
7. Use an expression in the FileGlobals.ModelPluginComponentDescription.Default.Base.DisplayNameExpression subproperty to display a string that describes the plug-in or its output in the Output column of the Result Processing dialog box. Use an expression in the FileGlobals.ModelPluginComponentDescription.DisplayNameExpression subproperty to display a string that identifies the plug-in in the plug-in insertion menu of the Result Processing dialog box.
8. If you do not want plug-in end users to configure any plug-in-specific options, delete the Configure Standard Options and the Configure Additional Options sequences from the plug-in sequence file.
9. Complete the following steps if you want plug-in end users to configure plug-in-specific options.
  - Add each option you want plug-in end users to configure as a subproperty of the <plug-in name> Options data type.
  - Create a modal dialog box, in which plug-in end users can view and edit the plug-in options. Refer to the <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog directory for examples of creating modal dialog boxes.
    - Export a function, method, or VI to launch the dialog box and call the function, method, or VI in the Configure Standard Options sequence.
    - You can pass each <plug-in name> Options subproperty into and out of the dialog box entry point. You can also pass the plug-in or the <plug-in name> Options subproperty as a property object and use the TestStand PropertyObject class methods to access the <plug-in name> Options subproperties within the dialog box code.
    - Pass the value of the RunState.Engine property to the dialog box code so you can call the Engine.NotifyStartOfModalDialogEx and Engine.NotifyEndOfModalDialog methods to enforce the modality of the dialog box.
    - If you are using the LabWindows/CVI Adapter or the LabVIEW Adapter to create the dialog box, ensure that you configure the step that launches the dialog box to always run in the run-time engine to avoid creating out-of-process modal windows, which can result in hangs. Note When you call a LabVIEW VI that creates ActiveX references, such as calling the ApplicationMgr.GetEngine method directly, you configure the VI to use the same as caller execution system, and you call the VI from a sequence running in a single-threaded apartment thread, LabVIEW might seem to hang with 100% processor use. Change the Preferred Execution System option in LabVIEW to a value other than same as caller to work around this issue.
  - Optionally, you can use an expression in the FileGlobals.ModelPluginComponentDescription.Default.Base.OptionsDescriptionExpression subproperty to display information in the Options column of the Result Processing dialog box. For example, the NI_ReportGenerator plug-in uses this expression to display the report format in the Options column of the Result Processing dialog box.
10. Consider whether you want the plug-in to always process information in a new thread other than the model execution thread, never process information in a new thread, or allow end users to specify whether to process information in a new thread. Typically, you allow processing in a new thread if the plug-in requires a significant amount of processing time and the plug-in can process the information while processing information from other instances of the plug-in and testing subsequent UUTs. According to your decision, set the following subproperties of FileGlobals.ModelPluginComponentDescription.Default :
  - Base.NewThread
  - Base.CompleteBeforeNextUUT
  - Base.UseDefaultNewThreadImplementation
11. Save and close the plug-in when you have completed the customizations.
12. Complete the following steps to add an instance of the new plug-in to a result processing configuration. TestStand stores the configuration in <TestStand Application Data>\Cfg\ModelPlugins\ResultProcessing.cfg . The process model loads this configuration file at run time to determine the plug-ins to invoke.
  1. Select Configure»Result Processing to launch the Result Processing dialog box.
  2. Click the Add button and select the plug-in name from the drop-down list.
13. When you have completed customizing and testing the plug-in, you can delete the entry point sequences the plug-in does not require. If you later determine that you need an entry point sequence you deleted, complete the following steps to add the entry point to the plug-in:
  1. Unload the plug-in.
  2. Restart the user interface or other TestStand-based application.
  3. Generate a new plug-in with the same filename to a different location.
  4. Copy the entry point sequences you need from the new plug-in to the original plug-in.
  5. Delete the new plug-in.Alternatively, instead of deleting unused entry points, you can rename them so the model does not call them. For example, you can add a [Reserved] prefix the name of each unused entry point.

When you insert a plug-in instance, the modal dialog box inserts a copy of the FileGlobals.ModelPluginComponentDescription.Default property values to use for that instance of the plug-in. Any changes you make to these values in the plug-in sequence file apply only to subsequent instances of the plug-in you create.

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- TestStand Directory Structure
- Model Plug-in Entry Points
- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- Dynamically Set the Client Sequence File

<!--NI_TOPIC bundle=teststand path=creating-rule-configuration-modules.html language=enus -->
## TOPIC 00231: Creating Rule Configuration Modules in the TestStand Sequence Analyzer

- bundle_id: `teststand`
- source_path: `creating-rule-configuration-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-rule-configuration-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Use Configuration Module from the Configuration Option ring control on the Advanced tab of the Edit Rule dialog box to use a rule configuration module. The TestStand Sequence Analyzer calls the configuration module when the user clicks the Settings button next to the rule on the Rules pane or

### Creating Rule Configuration Modules in the
 TestStand Sequence Analyzer

Select Use Configuration Module from the Configuration Option ring
 control on the Advanced tab of the Edit Rule dialog box to use a rule configuration
 module. The TestStand Sequence Analyzer calls the configuration module when the user
 clicks the Settings button next to the rule on the Rules pane or tab.

National Instruments recommends that you copy a rule configuration module template from
 the
 <TestStand>\Components\Analyzer\Templates\<Environment>
 directory to the
 <TestStand Public>\Components\Analyzer\<YourRuleName>
 directory, where Environment is LabVIEW,
 CVI, CSharp, or VC and
 YourRuleName is the descriptive name or the unique ID of the custom
 rule. National Instruments recommends also using your company name as part of the
 directory name to avoid potential conflicts with other custom analysis modules.

(LabVIEW)  After you copy the template files, rename the VIs using the rule ID to avoid
 potential conflicts with other analysis module VIs, and enable the VIs to perform rule
 checking.

(LabWindows/CVI, Microsoft Visual C#, Microsoft Visual C++)  After you copy the template
 file, search for the text Template in each source file and follow the
 instructions in the file.

The TestStand Sequence Analyzer requires that rule configuration modules use the
 following specific prototypes.

#### LabVIEW

The VI connector pane must use an ActiveX Refnum input with
 the ActiveX class set to
 TSAnalyzer.RuleConfigurationContext
 and can optionally include an Error Out cluster output or a
 Boolean, an I32 numeric, and a string output, which represent the unbundled elements
 of an Error Out cluster. You can use the Unbundle by Name
 function in LabVIEW to obtain the individual elements of the Error
 Out cluster.

#### LabWindows/CVI

The function prototype must be one of the following:

void Function(CAObjHandle ruleConfigurationContext);
 bool Function(CAObjHandle ruleConfigurationContext, char
 errorMessage[]);
 int Function(CAObjHandle ruleConfigurationContext, char
 errorMessage[]);

where ruleConfigurationContext is an input that contains an instance
 of the
 TSAnalyzer.RuleConfigurationContext
 ActiveX class, and errorMessage is a string buffer of 1024
 characters in which the function returns error messages for the rule configuration
 module code.

#### Microsoft Visual C#

The method prototype must be one of the following:

void
 Method(NationalInstruments.TestStand.Interop.SequenceAnalyzer.RuleConfigurationContext
 ruleConfigurationContext);
 bool
 Method(NationalInstruments.TestStand.Interop.SequenceAnalyzer.RuleConfigurationContext
 ruleConfigurationContext, out string errorMessage);

where ruleConfigurationContext is an input that contains an instance
 of the RuleConfigurationContext COM interop class and
 errorMessage is an output string in which the method returns
 error messages for the rule configuration module code.

#### Microsoft Visual C++

The function prototype must be one of the following:

void Function(TSAnalyzer::RuleConfigurationContext
 *ruleConfigurationContext);
 bool Function(TSAnalyzer::RuleConfigurationContext
 *ruleConfigurationContext, char errorMessage[]);
 int Function(TSAnalyzer::RuleConfigurationContext *ruleConfigurationContext,
 char errorMessage[]);

where ruleConfigurationContext is an input that contains an instance
 of the TSAnalyzer.RuleConfigurationContext ActiveX class, and
 errorMessage is a string buffer of 1024 characters in which the
 function returns error messages for the rule configuration module code.

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Search Directories
- Accessing Rule Configuration Data in Rule Configuration Modules and Analysis Modules

Related information:

- Edit Rule Dialog Box
- RuleConfigurationContext

<!--NI_TOPIC bundle=teststand path=creating-steps-from-step-types.html language=enus -->
## TOPIC 00232: Creating Steps from Step Types

- bundle_id: `teststand`
- source_path: `creating-steps-from-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-steps-from-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use step types when you insert steps in the Setup, Main, and Cleanup groups of the Steps pane in the Sequence File window. You can insert a step using the Step Types list in the Insertion Palette or the Insert Step submenu in the Steps pane context menu. The Insertion Palette and the Insert Step sub

### Creating Steps from Step Types

Use step types when you insert steps in the Setup, Main, and Cleanup groups of the Steps pane in the Sequence File window. You can insert a step using the Step Types list in the Insertion Palette or the Insert Step submenu in the Steps pane context menu. The Insertion Palette and the Insert Step submenu list all the available step types.

When you insert a step type from the Insertion Palette or the Insert Step submenu, TestStand creates a step using the step type and the module adapter selected in the Insertion Palette or toolbar. After you insert the step, select Specify Module from the context menu to specify the code module or sequence, if any, the step calls. The Specify Module option displays a Module tab on the Step Settings pane that is different for each adapter.

For each step type, other options appear in the context menu above the Specify Module item. For example, the Edit Limits option appears in the context menu for Numeric Limit Test steps, and the Edit Data Source option appears in the context menu for Pass/Fail Test steps. Select the menu option to display a step-type-specific pane or launch a step-type-specific dialog box in which you can modify step properties specific to the step type.

To modify step properties common to all step types, click the Properties tab of the Step Settings pane.

The Insertion Palette also contains a Templates list you can use to hold copies of sequences, steps, and variables you reuse.

Parent topic:

Built-In Step Types

Related concepts:

- Built-In Step Properties

<!--NI_TOPIC bundle=teststand path=creating-string-resource-files.html language=enus -->
## TOPIC 00233: Creating String Resource Files

- bundle_id: `teststand`
- source_path: `creating-string-resource-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-string-resource-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand uses the Engine.GetResourceString method to obtain the string messages to display in TestStand Sequence Editor and TestStand User Interface windows and dialog boxes. The Engine.GetResourceString method uses a string category and a tag name as arguments and searches for the string resource

### Creating String Resource Files

TestStand uses the Engine.GetResourceString method to obtain the string messages to display in TestStand Sequence Editor and TestStand User Interface windows and dialog boxes. The Engine.GetResourceString method uses a string category and a tag name as arguments and searches for the string resource in all string resource files in the following predefined order of directories:

1. <TestStand Public>\Components\Language\< current language >
2. <TestStand Public>\Components\Language\English
3. <TestStand Public>\Components\Language
4. <TestStand>\Components\Language\< current language >
5. <TestStand>\Components\Language\English
6. <TestStand>\Components\Language

Select Configure»Station Options to launch the Station Options dialog box and click the Localization tab to change the current language setting.

To customize a string resource file for a supported language or to create a resource file for a new language, copy an existing language file from the <TestStand>\Components\Language\<current language> directory, place the file in the <TestStand Public>\Components\Language\<current language> directory, and modify the file. To create a resource string file that applies to all languages, place the resource file in the base <TestStand Public>\Components\Language directory.

Note

Parent topic:

Extending TestStand

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=creating-the-teststand-engine.html language=enus -->
## TOPIC 00234: Creating the TestStand Engine

- bundle_id: `teststand`
- source_path: `creating-the-teststand-engine.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/creating-the-teststand-engine.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you write an application using the TestStand API, you must create a TestStand Engine object. Because you can create the TestStand Engine as an ActiveX control or as an ActiveX Automation server, you can access the engine from any application development environment that supports ActiveX. If you

### Creating the TestStand Engine

When you write an application using the TestStand API, you must create a TestStand Engine object. Because you can create the TestStand Engine as an ActiveX control or as an ActiveX Automation server, you can access the engine from any application development environment that supports ActiveX. If you use a development environment that supports ActiveX controls with events, such as Microsoft Visual Basic or Microsoft Visual C/C++, create the Engine object by adding the TestStand Engine control to the main form of the application. If the development environment does not support ActiveX controls, you can create the Engine object as an in-process automation server.

Note

Parent topic:

Writing an Application with the TestStand Engine API

<!--NI_TOPIC bundle=teststand path=cross-bitness-support-using-the-labview-devel.html language=enus -->
## TOPIC 00235: Cross-Bitness Support using the LabVIEW Development System

- bundle_id: `teststand`
- source_path: `cross-bitness-support-using-the-labview-devel.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/cross-bitness-support-using-the-labview-devel.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use the LabVIEW development system to call VIs, you can call 32-bit VIs from 64-bit TestStand and 64-bit VIs from 32-bit TestStand. Select one of the following options in the LabVIEW Adapter Configuration dialog box to specify which LabVIEW development system version to launch: Use Active L

### Cross-Bitness Support using the LabVIEW Development System

When you use the LabVIEW development system to call VIs, you can call 32-bit VIs from 64-bit TestStand and 64-bit VIs from 32-bit TestStand. Select one of the following options in the LabVIEW Adapter Configuration dialog box to specify which LabVIEW development system version to launch:

- Use Active LabVIEW Version —Launches the current active 32-bit or 64-bit LabVIEW development system, with a preference to match the bitness of TestStand.
- Use Active 32-bit Version —Launches the current active 32-bit LabVIEW development system.
- Use Active 64-bit Version —Launches the current active 64-bit LabVIEW development system.

TestStand does not support cross-bitness LabVIEW calls when you configure the LabVIEW Adapter to use the LabVIEW Run-Time Engine.

Parent topic:

LabVIEW Code Module Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=custom-analyzer-rules.html language=enus -->
## TOPIC 00236: Custom Analyzer Rules

- bundle_id: `teststand`
- source_path: `custom-analyzer-rules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/custom-analyzer-rules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to implement custom TestStand Sequence Analyzer rules and analysis modules in LabVIEW, LabWindows/CVI, Microsoft Visual C#, and Microsoft Visual C++. The example directory contains the following example custom rules: CheckNumberOfLocals—This rule verifies that t

### Custom Analyzer Rules

#### Purpose

This example demonstrates how to implement custom TestStand Sequence Analyzer rules and analysis modules in LabVIEW, LabWindows/CVI, Microsoft Visual C#, and Microsoft Visual C++. The example directory contains the following example custom rules:

- CheckNumberOfLocals —This rule verifies that the number of locals in each analyzed sequence does not exceed a maximum number. The maximum is a configurable rule setting that users edit with a standard built-in dialog box. This example demonstrates how to use rule settings to configure rules and how to use analysis transitions to perform bookkeeping tasks.
- CheckStepNameLength —This rule verifies that the analyzed step names do not exceed a maximum length. The maximum length is a configurable rule setting that users edit using a custom dialog box. This example demonstrates how to use a rule configuration module to configure rules using a custom dialog box and how to store and retrieve rule configuration data.

Each example rule contains source code for analysis modules and rule configuration modules written in LabVIEW, LabWindows/CVI, Microsoft Visual C#, and Microsoft Visual C++.

#### Example File Location

This example does not use a separate sequence file. Create a new sequence file and follow the steps in to import the files located in the <TestStand Public>\Examples\TestStand Debugging Features directory.

#### Highlighted Features

- Analysis module
- Analysis transitions
- Rule configuration module
- Rule settings

#### Major API

- AnalysisContext
- RuleConfiguration
- RuleConfigurationContext

#### Prerequisites

You do not need any additional software to run the examples. You must have a supported version of LabVIEW, LabWindows/CVI, or Microsoft Visual Studio installed to modify and rebuild the modules.

#### How to Use This Example

This example implements several rules and analysis modules using LabVIEW, LabWindows/CVI, Visual C#, and Visual C++. You must import the corresponding rules files in the Configure Sequence Analyzer Available Rules dialog box to add the example rules to the sequence analyzer.

After you add the rule to the sequence analyzer, the analyzer adds the rule to all opened analyzer projects. The sequence analyzer uses the analysis module the next time you analyze a project.

Parent topic:

Examples for TestStand Debugging Features

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=custom-properties-of-step-types.html language=enus -->
## TOPIC 00237: Custom Properties of Step Types

- bundle_id: `teststand`
- source_path: `custom-properties-of-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/custom-properties-of-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add any number of custom properties in a step type you create. Each step you create using the step type includes the custom properties you create. On the Types pane of the Types window, expand the step type, right-click, select Insert Field from the context menu, and select a data type to ad

### Custom Properties of Step Types

You can add any number of custom properties in a step type you create. Each step you create using the step type includes the custom properties you create.

1. On the Types pane of the Types window, expand the step type, right-click, select Insert Field from the context menu, and select a data type to add fields to a step type.
2. Right-click the field and use the context menu to cut, copy, paste, delete, and rename fields.

Parent topic:

Custom Step Types

<!--NI_TOPIC bundle=teststand path=custom-result-properties.html language=enus -->
## TOPIC 00238: Custom Result Properties

- bundle_id: `teststand`
- source_path: `custom-result-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/custom-result-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each step type defines a set of custom result properties. All steps that use the step type have the same set of custom properties. All built-in step types contain the following custom properties: Step.Result.Error.Code—Code that describes the error that occurred. TestStand supports only 32-bit signe

### Custom Result Properties

Each step type defines a set of custom result properties. All steps that use the step type have the same set of custom properties.

All built-in step types contain the following custom properties:

- Step.Result.Error.Code —Code that describes the error that occurred. Note TestStand supports only 32-bit signed integer values for the run-time error code property. Although you can assign a larger or fractional value to the property, TestStand will truncate the value to 32-bit when handling and propagating a run-time error.
- Step.Result.Error.Msg —Message string that describes the error that occurred.
- Step.Result.Error.Occurred —Boolean flag that indicates a run-time error occurred in the step. TestStand documentation refers to this property as the error occurred flag.The error occurred flag can become True when a run-time error condition occurs and the code module or module adapter sets the value to True or when an unhandled exception occurs in the code module or at any other time during step execution. When a step finishes execution and the error occurred flag is True , the TestStand Engine responds in the following ways:
  - Does not evaluate the status and post-expressions for a step and sets the step status to Error .
  - Evaluates the Ignore Run-Time Errors step property.
    - When this property is False , TestStand reports the run-time error to the sequence.
    - When this property is True , TestStand continues execution normally after the step.
- Step.Result.Status —The status of the last execution of the step, such as Done , Passed , Failed , Skipped , or Error . TestStand documentation refers to this property as the step status.Before TestStand executes a step, it sets the step status to Running or Looping . When a step finishes execution and the error occurred flag is False , TestStand changes the step status to Done . The step status becomes Passed or Failed only when a code module, module adapter, or step type explicitly sets the step status to Passed or Failed .
- Step.Result.ReportText —Message string TestStand includes in the report.
- Step.Result.Common —Placeholder container you can customize by modifying the CommonResults standard data type.

Note

The Common property uses the CommonResults custom data type and is a subproperty of the Result
 property for every step type. Consequently, you can add a subproperty to the result
 of every step type by adding a subproperty to the definition of the CommonResults
 custom data type. When you modify the CommonResults data type, you must ensure that
 the new type definition does not conflict with earlier versions of the type in other
 files. NI recommends modifying the CommonResults data type only when you want to
 perform an architectural change to all step types that you use.

Note

Parent topic:

Result Collection

Related concepts:

- Error and CommonResults
- Built-In Step Types
- Type Versioning
- Modifying Types
- Result Collection
- Exceptions to Custom Result Properties
- Standard Result Properties

<!--NI_TOPIC bundle=teststand path=custom-step-properties.html language=enus -->
## TOPIC 00239: Custom Step Properties

- bundle_id: `teststand`
- source_path: `custom-step-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/custom-step-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can usually modify the values of custom step properties using the tabs on the Step Settings pane. If the step type does not include a tab for the custom properties, select the Property Browser panel to view the custom properties for the step. Although code modules usually do not modify the value

### Custom Step Properties

You can usually modify the values of custom step properties using the tabs on the Step Settings pane. If the step type does not include a tab for the custom properties, select the Property Browser panel to view the custom properties for the step.

Although code modules usually do not modify the values of the built-in step properties at run time, they often modify and read the values of the custom step properties when determining the pass/fail status of the step.

Note

Parent topic:

Steps

Related concepts:

- Code Modules
- Built-In Step Properties
- Accessing Properties Using API

<!--NI_TOPIC bundle=teststand path=custom-step-types.html language=enus -->
## TOPIC 00240: Custom Step Types

- bundle_id: `teststand`
- source_path: `custom-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/custom-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create custom step types to meet the needs of an application. Custom step types differ from the step templates you store in the Templates list on the Insertion Palette, as the following table describes: Item Description Effect of Change Made Custom step types Define standard functionality fo

### Custom Step Types

You can create custom step types to meet the needs of an application. Custom step types differ from the step templates you store in the Templates list on the Insertion Palette, as the following table describes:

| Item | Description | Effect of Change Made |
| --- | --- | --- |
| Custom step types | Define standard functionality for a class of steps. | Changes can affect step instances previously inserted into sequences. |
| Step templates | Preconfigured instances of step types you typically use, such as calls to frequently used code modules. | Changes do not affect steps previously inserted into sequences. |

Parent topic:

Extending TestStand

<!--NI_TOPIC bundle=teststand path=customizing-atml-test-results-6-01-or-5.html language=enus -->
## TOPIC 00241: Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

- bundle_id: `teststand`
- source_path: `customizing-atml-test-results-6-01-or-5.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-atml-test-results-6-01-or-5.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a text editor to customize a style sheet you can use for a report that validates against version 6.01 or 5.0 of the ATML Test Results and Session Information schema in the following ways: Add columns and rows to reports Add images and text to headers and footers Add step results to repor

### Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

You can use a text editor to customize a style sheet you can use for a report that validates against version 6.01 or 5.0 of the ATML Test Results and Session Information schema in the following ways:

- Add columns and rows to reports
- Add images and text to headers and footers
- Add step results to reports without indentation
- Add Sequence Call step results to reports without indentation
- Change the display format of execution time
- Customize the UUT Report header
- Modify table cell background color based on step status
- Render HTML elements and new line characters in reports

Note

<TestStand>\Components\Models\TestStandModels\ATML\StyleSheets

<TestStand Public>\Components\Models\TestStandModels\ATML\StyleSheets

Parent topic:

ATML Report Style Sheets

Related concepts:

- ATML Report Style Sheets
- ATML Test Results Reports
- Adding Columns and Rows to an ATML Test Results 6.01 or 5.0 Report
- Adding Images and Text to an ATML Test Results 6.01 or 5.0 Report Header or Footer
- Adding Step Results to an ATML Test Results 6.01 or 5.0 Report without Indentation
- Adding Sequence Call Step Results to an ATML Test Results 6.01 or 5.0 Report without Indentation
- Changing the Display Format of Execution Time in an ATML Test Results 6.01 or 5.0 Report
- Customizing the UUT Report Header for an ATML Test Results 6.01 or 5.0 Report
- Modifying Cell Background Color Based on Step Status in an ATML Test Results 6.01 or 5.0 Report
- Rendering HTML Elements and New Line Characters in an ATML Test Results 6.01 or 5.0 Report
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=customizing-components-you-deploy.html language=enus -->
## TOPIC 00242: Customizing Components You Deploy

- bundle_id: `teststand`
- source_path: `customizing-components-you-deploy.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-components-you-deploy.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the System Source tab and the Distributed Files tab of the TestStand Deployment Utility to specify and customize the files or directories you select to include in the deployment. Specifying Source Files When you specify the source files for a test system on the System Source tab of the deploymen

### Customizing Components You Deploy

[IMAGE alt='image' src='GUID-2D0C88EC-0084-47BC-B4A4-A1071E05AF55-a5.svg']

Use the System Source tab and the Distributed Files tab of the TestStand Deployment Utility to specify and customize the files or directories you select to include in the deployment.

#### Specifying Source Files

When you specify the source files for a test system on the System Source tab of the deployment utility, the deployment utility prompts you to analyze the source files before displaying the files in the Distributed Files list on the Distributed Files tab of the deployment utility. You must manually add certain types of files to the deployment. If you modify files after adding them to the deployment, click the Analyze Source Files button to re-analyze the files.

When you specify a TestStand workspace file on the System Source tab, the Distributed Files list on the Distributed Files tab includes the workspace file, its contents, and the dependencies, which include all the TestStand projects in the workspace, all the sequence files in each of the projects, any code modules sequence files call statically, and any other files in the project. By default, the Distributed Files list does not include code module dependencies. However, when you use the System Source tab to specify a directory from which to deploy files, the Distributed Files list on the Distributed Files tab includes all the files from that directory and the dependencies. If you use the Distributed Files tab to change the file properties of a code module dependency, add the code module dependency to a TestStand project because the Distributed Files list includes all files in a TestStand project.

#### Excluding Source Files

If the Distributed Files list includes files you do not want to include in the deployment, use the View Source or View Build Preview views to remove the checkmark next to the file or directory you want to exclude from the deployable image when you create a full deployment.

#### Customizing File Properties

Select a file or directory in the Distributed Files list and use the options in the File Properties section on the Distributed Files tab to customize how to include each file or directory in the deployable image and how the installer you build with the deployment utility for the deployable image operates on the files.

Enable the Include Without Processing Item or Dependencies option in the File Properties section on the Distributed Files tab in the following situations:

- When you want to include the source files for a user interface without modification but process code module VIs normally
- When you want to deploy VIs in a different version of LabVIEW from the code modules
- When you use checksums for strict control of which files to deploy and do not want the deployment utility to make any changes to the files
- When you want to deploy files that have already been processed, such as third-party step types that use LabVIEW VIs or a LabVIEW User Interface

Enable the Include All Files in LabVIEW Project option in the File Properties section on the Distributed Files tab to add all the files in the selected LabVIEW project to the deployment so you can more easily modify the test system you deploy. LabVIEW packed project libraries the deployment utility creates always include all the files in LabVIEW projects.

#### Installer Properties

The options in the Installer Properties section on the Distributed Files tab apply only when you use the deployment utility to build an MSI-based installer. These options do not affect the files in the deployable image directory.

#### LabVIEW Options

Use the LabVIEW VI Options dialog box to customize how the deployment utility saves VIs in the deployable image.

#### Using Packed Project Libraries

Enable the Output VIs to Packed Project Library option to output packed project libraries instead of VIs in a deployment, which offers the following advantages:

- Reduces the number of files in the deployment because the packed project library contains all the VIs you select.
- Occupies less disk space than VIs because packed project libraries are compressed.
- Simplifies tracking file versions, updating, and installer behavior because packed project libraries use a version resource number, you specify.
- Ensures that you do not need to recompile calling VIs when VIs inside a packed project library change their inplaceness, or ability to reuse memory. The deployment utility enables by default the Callers adapt at run time to Exported VI connector pane state option on the Connector Pane State page of the Packed Library Properties dialog box in LabVIEW for all packed project libraries it creates so you can update subsets of VIs on a test station computer without mass compiling all the VIs on the test station computer.
- Simplifies upgrading test systems and preventing code duplication in test systems because packed project libraries are versioned files, which offer the following benefits:
  - Installers can correctly update the files if multiple installers that use the packed project library reside on the same computer.
  - Multiple installers can include the same packed project library, and the installer correctly installs only one copy of the file, which all code within the test system can share.

Use the Packed Project Library Options dialog box to configure options for how the deployment utility builds LabVIEW packed project libraries. You can also use LabVIEW to build packed project libraries.

#### Excluding VIs

The LabVIEW Development System installs vi.lib. Instrument drivers install VIs in instr.lib. Toolkits and third-party software install VIs in user.lib. Exclude dependencies from vi.lib, instr.lib, or user.lib from deployments when you deploy VIs that you expect others to edit, such as when you deploy VIs to another development computer or to a test station computer that includes the LabVIEW Development System, the TestStand Runtime, a custom user interface, and a TestStand Custom Sequence Editor License so other developers can modify and redeploy test sequences.

Including VIs from vi.lib, instr.lib, or user.lib in a deployment you install on a computer that includes the LabVIEW Development System can cause the following issues:

- The VIs in the deployment have the same qualified names as the source VIs in vi.lib , instr.lib , or user.lib , which introduces the possibility of cross-linking.
- The deployment does not reflect changes later versions of LabVIEW make to vi.lib , which can result in broken VIs or VIs that do not run correctly if the VIs do not include the changes that later versions of LabVIEW require.
- Partial project libraries can cause broken VIs.

#### LabVIEW Optimizations

Use
 the Optimizations section of the LabVIEW VI Options dialog box to removed unused VI
 components and consolidate files projects share if you call VIs in the context of
 multiple LabVIEW projects.

Parent topic:

Deployment Process Overview

Related concepts:

- Manually Adding or Removing Files to or from Deployments
- Using a TestStand Workspace File to Create a Deployment
- Using a Directory to Create a Deployment
- Filtering and Excluding Files
- Using Multiple LabVIEW Versions in a Test System
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Managing Versioned and Non-Versioned Files
- Choosing Single or Multiple Deployments
- Partial Project Libraries
- Deploying VIs in LabVIEW Packed Project Libraries
- Organizing LabVIEW-Based TestStand Systems

<!--NI_TOPIC bundle=teststand path=customizing-database-logging-expressions.html language=enus -->
## TOPIC 00243: Customizing Database Logging Expressions

- bundle_id: `teststand`
- source_path: `customizing-database-logging-expressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-database-logging-expressions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When TestStand starts logging data to a database, it creates a temporary Logging property in the sequence context to evaluate expressions. The Logging property contains subproperties that provide information about database settings, process model data structures, and the results TestStand processes.

### Customizing Database Logging Expressions

When TestStand starts logging data to a database, it creates a temporary Logging property in the sequence context to evaluate expressions.

The Logging property contains subproperties that provide information about database settings, process model data structures, and the results TestStand processes. As the Logging property processes the result list, TestStand updates the subproperties of the Logging property to refer to the UUT result, step result, and the property result TestStand is processing. You can reference the Logging subproperties in the precondition and value expressions you specify for schema statements and columns.

The Logging property contains the following subproperties:

- UUTResult —The UUT result TestStand is processing. When TestStand is processing a step or a subproperty, this property contains the UUT result that contains the step result or subproperty.
- StepResult —The step result TestStand is processing. When TestStand is processing a subproperty, this property holds the step result that contains the subproperty. When TestStand is processing a UUT result, this property contains the result of the sequence call in the process model that calls the Main sequence in the client file.
- PropertyResult —The subproperty of the step result TestStand is processing. When TestStand is not processing a subproperty, this property does not exist.
- PropertyResultDetails —Information about the subproperty of the step result TestStand is processing. When TestStand is not processing a subproperty, this container does not exist.
- ExecutionOrder —A numeric value TestStand increments after it processes each step result.
- StartDate —The date on which the UUT test began. This property is an instance of the DateDetails custom data type.
- StartTime —The time at which the UUT test began. This property is an instance of the TimeDetails custom data type.
- UUT —Specifies the serial number, test socket index, and other information about the UUT. This property is an instance of the UUT custom data type.
- DatabaseOptions —The process model database settings you configure in the Database Options dialog box. This property is an instance of the DatabaseOptions custom data type.
- StationInfo —The station ID and the user name. This property is an instance of the StationInfo custom data type.

The TestStand process model files define the structure of the DateDetails, TimeDetails, UUT, DatabaseOptions, and StationInfo custom data types.

Parent topic:

TestStand Database Result Tables

Related concepts:

- Sequence Context

<!--NI_TOPIC bundle=teststand path=customizing-process-models-and-callbacks.html language=enus -->
## TOPIC 00244: Customizing Process Models and Callbacks

- bundle_id: `teststand`
- source_path: `customizing-process-models-and-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-process-models-and-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can customize the default process models and callback sequences. Customize callbacks to implement custom functionality specific to unit under test (UUT) models. Customize process models to implement functionality that is standard throughout an organization and applies to all or most UUTs. Use ca

### Customizing Process Models and Callbacks

You can customize the default process models and callback sequences. Customize callbacks to implement custom functionality specific to unit under test (UUT) models. Customize process models to implement functionality that is standard throughout an organization and applies to all or most UUTs. Use callbacks to implement functionality you might change. Use process models to implement functionality you are unlikely to change. You can extend the functionality of existing process models by creating or customizing process model plug-ins.

Note

<TestStand>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand>\Components\Models\TestStandModels

<TestStand>\Components\Models\ModelPlugins

<TestStand Public>\Components\Models\ModelPlugins

Parent topic:

Extending TestStand

Related concepts:

- Process Model Architecture
- Callback Sequences
- Process Model Plug-In Architecture
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=customizing-reports-with-expressions.html language=enus -->
## TOPIC 00245: Customizing Reports with Expressions

- bundle_id: `teststand`
- source_path: `customizing-reports-with-expressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-reports-with-expressions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to using options to determine the names and locations of report files, you can specify a custom expression with predefined macros TestStand evaluates at run time for each UUT to fully customize the filename of reports and the directory in which TestStand stores reports. For example, you

### Customizing Reports with Expressions

In addition to using options to determine the names and locations of report files, you
 can specify a custom expression with predefined macros TestStand evaluates at run time
 for each UUT to fully customize the filename of reports and the directory in which
 TestStand stores reports. For example, you can use expressions to save reports in a
 directory that uses the sequence filename, save reports in different directories based
 on execution status, and generate report filenames that include the serial number, user
 name, or execution status.

You can use expressions to replicate all existing report filename options. Use the Report
 File Pathname tab of the Report Options dialog box to specify an expression for a
 report.

The following table lists common report options and the equivalent expression for the
 Sequential process model using the client sequence file directory as the base
 directory.

| Current Report Option | Equivalent Expression |
| --- | --- |
| New UUT Report File for Each UUT | $(ClientFileDir)\\\\Report_$(UUT).$(FileExtension) |
| Prefix Sequence File Name to Report File Name | $(ClientFileDir)\\\\$(ClientFileName)_Report.$(FileExtension) |
| Add Date and Time to File Name | $(ClientFileDir)\\\\Report_$(FileDate)$(FileTime).$(FileExtension) |
| Force File Name to Be Unique | $(ClientFileDir)\\\\Report_$(Unique).$(FileExtension) |
| Prefix Sequence File Name to Report File Name + New UUT Report File for Each UUT + Add Date and Time to File Name | $(ClientFileDir)\\\\$(ClientFileName)_Report_$(UUT)_$(FileDate)$(FileTime).$(FileExtension) |

The following table lists example expressions for common tasks using the Sequential
 process model.

| Task | Equivalent Expression |
| --- | --- |
| Save reports in a directory that uses the sequence filename | C:\\\\$(ClientFileName)\\\\Report.$(FileExtension) Note TestStand overwrites existing files unless you use the $(Unique) macro or enable the Append if File Already Exists option on the Contents tab of the Report Options dialog box. |
| Save reports in different directories based on execution status | C:\\\\$(ClientFileName)\\\\$(UUTStatus)\\\\Report.$(FileExtension) Note TestStand overwrites existing files unless you use the $(Unique) macro or enable the Append if File Already Exists option. |
| Generate report filenames that include the UUT serial number | C:\\\\$(ClientFileName)\\\\Report_$(UUT).$(FileExtension) |
| Generate report filenames that include the user name | C:\\\\$(ClientFileName)\\\\Report_$(UserName).$(FileExtension) |
| Generate report filenames that include the execution status | C:\\\\$(ClientFileName)\\\\Report_$(UUTStatus).$(FileExtension) |

Note

Parent topic:

Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=customizing-reports.html language=enus -->
## TOPIC 00246: Customizing Reports

- bundle_id: `teststand`
- source_path: `customizing-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can customize report generation within TestStand in a variety of ways. You can also create a custom results format by creating a custom result processing plug-in. Completed solution files are located in the <TestStand Public>\Tutorial\Solution directory. Configuring Test Report Options Complete

### Customizing Reports

You can customize report generation within TestStand in a variety of ways. You can also create a custom results format by creating a custom result processing plug-in.

Note

<TestStand Public>\Tutorial\Solution

#### Configuring Test Report Options

Complete the following steps to configure the test report options.

1. Open <TestStand Public>\Tutorial\Computer.seq .
2. Select Configure»Result Processing to launch the Result Processing dialog box.
3. Click the icon in the Options column for the built-in Report model plug-in to launch the Report Options dialog box and complete the following steps.
  1. On the Contents tab, select ATML 6.01 Standards Report Document from the Report Format ring control.
  2. Enable the Include Step Results option and confirm the following step result settings:
    - Enable the Include Test Limits option.
    - Enable the Include Measurements option.
    - Select Insert Graph from the Include Arrays ring control.
  3. Click the Edit Format button located to the right of the Default Numeric Format control to launch the Numeric Format dialog box, in which you specify the format TestStand uses to display the value of a numeric variable or property. By default, TestStand configures the numeric format to report numbers with 13 digits of precision.
  4. Change Maximum Number of Significant Digits to 2 and click OK to close the Numeric Format dialog box.
4. Click the Report File Pathname tab, which you use to specify the report file pathname. You can specify a fixed pathname to use for all report files or you can specify options the report generator uses to generate report file pathnames. Use the default values for the options on this tab and click OK to close the Report Options dialog box.
5. Click OK to close the Result Processing dialog box.
6. Select Execute»Test UUTs . Run through several iterations of the sequence, selecting components other than the Video and CPU tests to fail.
7. Click Stop in the UUT Information dialog box to stop sequence execution. The test report contains failure chain information for UUTs that fail. The failure chain shows the step failure that caused the UUT to fail and shows the Sequence Call steps through which the execution reached the failing step. Each step name in the failure chain links to the section of the report that shows the result for the step.
8. Close the Execution window.
9. Select Configure»Result Processing to launch the Result Processing dialog box.
10. Click the icon in the Options column for the built-in Report model plug-in to launch the Report Options dialog box and complete the following steps.
  1. Click the Contents tab and select ASCII Text File from the Report Format ring control.
  2. Select Exclude Passed/Done/Skipped from the Result Filtering Expression ring control for TestStand to apply a filtering expression to determine what steps appear in the report. In this example, you configure TestStand to record only the results of the steps that do not pass or steps that complete without any status. TestStand also changes the value of the Include Arrays ring control to Insert Table because ASCII reports do not support graphs.
11. Click OK to close the Report Options dialog box, and click OK to close the Result Processing dialog box.
12. Repeat steps 6 through 8 and examine the text version of the test report. Close the Execution window when you finish reviewing the report.

#### Using External Report Viewers

You can view the test report in external applications more suited for showing and editing text, such as Microsoft Word or Microsoft Excel.

Complete the following steps to use an external report viewer to view the test report.

1. Select Configure»External Viewers to launch the Configure External Viewers dialog box.
2. Click the Add button.
3. Click the Browse button located to the right of the Viewer control and navigate to the application you want to use to view the report, such as Word, and click OK . Note When you select the application you want to use and click OK, TestStand might launch the File Not Found dialog box because TestStand cannot locate the file within the default TestStand search directories, which TestStand uses to resolve relative paths to code modules and other files or directories. Select the Use an absolute path for the file you selected option to ensure that TestStand can access the application you want to use to view the report, and click OK to close the File Not Found dialog box.
4. Select txt from the Format pull-down menu.
5. Enable the Automatically Launch Viewer option.
6. Click OK to close the Configure External Viewers dialog box.
7. Select Execute»Test UUTs . Run through several iterations of the sequence, selecting components other than the Video and CPU tests to fail.
8. Click Stop in the UUT Information dialog box to stop sequence execution. TestStand generates the text report and launches the external viewer application you configured in step 3 to show the test report.
9. Examine the test report and close the external report viewing application.
10. Close the Execution window.
11. Complete the following steps to change the report settings back to the default settings.
  1. Select Configure»Result Processing to launch the Result Processing dialog box.
  2. Enable the Show More Options option.
  3. Click the Reset to Defaults button.
  4. Click OK in the Reset Configuration prompt.
  5. Click OK to close the Result Processing dialog box.
12. Complete the following steps to change the external viewer settings back to the default settings.
  1. Launch the Configure External Viewers dialog box.
  2. Select the external viewer application you configured in step 3 and click the Delete button.
  3. Click OK to close the Configure External Viewers dialog box.
13. Close all the windows in the sequence editor.

#### Adding Additional Results to Reports

Use the Additional Results panel to add and configure additional results, which are values TestStand adds to the result list of a step when the step executes. An additional result can be a module parameter or a custom additional result in which you specify the name and value of the result. You can configure TestStand to automatically include additional results when generating a report or when logging results to a database. The default TestStand report generator style sheets do not display additional results for skipped steps.

Complete the following steps to create a step that calls a DLL code module to return a numeric array and add the numeric array and other values to the report.

1. Select File»New»Sequence File to open a new sequence file.
2. Save the sequence file as CustomReport.seq in the <TestStand Public>\Tutorial directory.
3. Complete the following steps to create a local variable.
  1. Click the Variables pane in the Sequence File window, right-click the Locals item and select Insert Local»Array of»Number from the context menu to launch the Array Bounds dialog box, in which you can modify the array bounds.
  2. Enter 49 in the Upper Bounds control and click OK .
  3. Rename the local variable NumArray .
4. Click the C/C++ DLL adapter icon, as shown in the following figure and located at the top of the Insertion Palette.
5. Insert an Action step in the Main step group and complete the following steps to configure the Action step.
  1. On the Module tab of the Step Settings pane, click the Browse button located to the right of the Module control, navigate to <TestStand Public>\Tutorial\NumericArray.dll , and click Open .
  2. Select GetNumericArray from the Function ring control.
  3. In the Value Expression column of the measurements parameter in the Parameters Table, enter Locals.NumArray to copy the value from the numeric array output parameter to the Locals.NumArray variable when TestStand returns from calling the GetNumericArray function.
  4. In the Value column of the Dim 1 Size property in the Parameter Details Table located to the right of the Parameters Table, enter -1 to specify that TestStand passes all elements of the Locals.NumArray property to the code module.
6. On the Properties tab of the Step Settings pane, complete the following steps to add the numeric array and other values to the report.
  1. Click Additional Results to show the Additional Results panel.
  2. Place a checkmark in the measurements [Out] parameter checkbox to log the output value of the parameter.
  3. Click the Add Custom Result button to add a new empty row to the list of the results.
  4. Enter "Time" , including the quotation marks, in the Name column and enter Time() in the Value to Log column. The Time TestStand expression function returns the current time.
  5. Click the Add Custom Result button again.
  6. Enter "Date", including the quotation marks, in the Name column and enter Date() in the Value to Log column. The Date TestStand expression function returns the current date.
7. Save the changes you made and select Execute»Single Pass . Review the report that includes the array data, the time, and the date.
8. Close all the windows in the sequence editor.

#### Adding to Reports Using
 Callbacks

Complete the following steps to add a logo to the header of the
 HTML report using a Report callback in the process model.

1. Open <TestStand Public>\Tutorial\Computer.seq .
2. Select File»Save <filename> As 
 and save the sequence file as Computer7.seq in the
 <TestStand Public>\Tutorial directory.
3. Select Configure»Result Processing to launch the Result
 Processing dialog box.
4. Click the icon in the Options column for the built-in Report model plug-in to
 launch the Report Options dialog box and complete the following steps.
  1. On the Contents tab, select HTML Document from
 the Report Format ring control.
  2. Click OK to close the Report Options dialog box,
 and click OK to close the Result Processing
 dialog box.
5. Select Edit»Sequence File Callbacks to launch the
 Sequence File Callbacks dialog box, select the
 ModifyReportHeader callback, and click
 Add to add the callback to the sequence file.
6. Click Edit to close the Sequence File Callbacks dialog
 box and edit the new ModifyReportHeader callback sequence in the Sequence File
 window, which TestStand automatically opens.
7. Click the Variables pane, right-click the
 Locals item, select Insert
 Local»String from the context menu, and name the local variable
 AddToHeader . Click in the Value column of the AddToHeader
 variable and enter the following text:
 <img alt='Logo Goes Here' src='Logo.jpg'><br><br> <a href='http://www.ni.com'>Visit Our Website</a><br><br>
8. Insert a Statement step in the Main step group and rename the step Add
 Custom Logo .
9. On the Expression tab of the Step Settings pane, enter the following expression
 in the Expression control:
 Parameters.ReportHeader = Locals.AddToHeader + Parameters.ReportHeader 
 Click the Check Expression for Errors button to verify
 that the expression contains valid syntax.
10. Save the changes and select Execute»Single Pass .
11. Click Done in the Test Simulator dialog box. Review the
 report after the execution completes and notice the new logo image at the top of
 the UUT report.
12. Complete the following steps to change the report settings back to the default
 settings.
  1. Select Configure»Result Processing to launch the
 Result Processing dialog box.
  2. Enable the Show More Options option.
  3. Click the Reset to Defaults button.
  4. Click OK in the Reset Configuration prompt.
  5. Click OK to close the Result Processing dialog
 box.
13. Close all the windows in the sequence editor.

Parent topic:

Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=customizing-the-atml-test-results-2.html language=enus -->
## TOPIC 00247: Customizing the ATML Test Results 2.02 Report Style Sheet

- bundle_id: `teststand`
- source_path: `customizing-the-atml-test-results-2.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-atml-test-results-2.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a text editor to customize the TR_horizontal.xsl report style sheet you can use for a report that validates against version 2.02 of the ATML Test Results and Session Information schema in the following ways: Add columns to the report Enable or disable table indentation Display or hide Te

### Customizing the ATML Test Results 2.02 Report Style Sheet

You can use a text editor to customize the TR_horizontal.xsl report style sheet you can use for a report that validates against version 2.02 of the ATML Test Results and Session Information schema in the following ways:

- Add columns to the report
- Enable or disable table indentation
- Display or hide TestStand-specific information
- Display the fully expanded state of the report in a plain HTML format
- Customize the UUT report header

Note

<TestStand>\Components\Models\TestStandModels\ATML\StyleSheets

<TestStand Public>\Components\Models\TestStandModels\ATML\StyleSheets

Parent topic:

ATML Report Style Sheets

Related concepts:

- ATML Report Style Sheets
- ATML Test Results Reports
- Adding Columns to an ATML Test Results 2.02 Report
- Enabling or Disabling Table Indentation in an ATML Test Results 2.02 Report
- Displaying or Hiding TestStand-Specific Information in an ATML Test Results 2.02 Report
- Displaying the Fully Expanded ATML Test Results 2.02 Report in Plain HTML
- Customizing the UUT Report Header for an ATML Test Results 2.02 Report
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=customizing-the-atml-test-results-report-gene.html language=enus -->
## TOPIC 00248: Customizing the ATML Test Results Report Generator

- bundle_id: `teststand`
- source_path: `customizing-the-atml-test-results-report-gene.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-atml-test-results-report-gene.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can customize an ATML Test Results (TR) report TestStand creates by implementing a DLL that exports one or more exported extension functions. TestStand calls the functions while creating the report. Complete the following steps to customize an ATML TR report. Create an extension DLL to implement

### Customizing the ATML Test Results Report Generator

You can customize an ATML Test Results (TR) report TestStand creates by implementing a DLL that exports one or more exported extension functions. TestStand calls the functions while creating the report.

Complete the following steps to customize an ATML TR report.

1. Create an extension DLL to implement one or more of the supported exported functions.
2. In the TestStand Sequence Editor, open or create a sequence file for which you want to generate a customized report.
3. Select Edit»Sequence File Callbacks to launch the Sequence File Callbacks dialog box.
4. Select the ReportOptions callback sequence and click Add to override the ReportOptions callback in the sequence file. Click OK to close the Sequence File Callbacks dialog box.
5. On the Sequences pane, double-click ReportOptions to open the ReportOptions callback sequence.
6. Insert a Statement step in the ReportOptions callback sequence.
7. With the Statement step selected, click the Expression edit tab of the Step Settings pane.
8. Enter the following expression in the Expression control: Parameters.ReportOptions.Atml_Rpt_Options.ExtensionDLLAbsolutePath = <absolute path to extension DLL> TestStand resolves the value of the Parameters.ReportOptions.Atml_Rpt_Options.ExtensionDLLAbsolutePath variable at run time, so you can implement run-time logic in the ReportOptions callback to assign different values to this variable. For example, the value of the Parameters.ReportOptions.Atml_Rpt_Options.ExtensionDLLAbsolutePath variable might be different depending on whether the Parameters.ReportOptions.ReportStyle variable is ATML or ATML5 .

Parent topic:

ATML Test Results Reports

Related concepts:

- ATML Test Results Reports
- Using Callback Sequences to Modify Process Models

<!--NI_TOPIC bundle=teststand path=customizing-the-database-viewer-user-interfac.html language=enus -->
## TOPIC 00249: Customizing the Database Viewer User Interface

- bundle_id: `teststand`
- source_path: `customizing-the-database-viewer-user-interfac.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-database-viewer-user-interfac.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can preview, switch between, dock/undock, float, and group certain tabs and panes in the Database Viewer application. Document Selector Press <Ctrl+Tab> to launch the document selector when the Database Viewer window is active to display a list of open panes and tabs and a preview of the selecte

### Customizing the Database Viewer User Interface

You can preview, switch between, dock/undock, float, and group certain tabs and panes in the Database Viewer application.

#### Document Selector

Press <Ctrl+Tab> to launch the document selector when the Database Viewer window is active to display a list of open panes and tabs and a preview of the selected pane or tab. Hold down the <Ctrl>key and use the arrow keys or the mouse to navigate through the list. The document that is selected when you release the <Ctrl> key becomes the active document when you close the document selector.

#### Dock/Undock

Tabs in the Database Viewer can be docked/undocked and floated as required. To undock a tab, double-click on the tab or drag it out of the main window or right-click on the tab header and choose the Float option.

To dock a floating tab, drag it over the main application window and choose a docking location.

Note

- You can undock and float the Database Explorer pane like a tab. However, this pane cannot be closed.
- Operations selected from the main application menu do not apply to floating tabs. The shortcuts for these operations can be used for the active floating tab to accomplish the same action.

#### Tab Groups

You can organize tabs into horizontal or vertical groups by dragging the tabs to the location you want or by using the context menu in the tab headers.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand path=customizing-the-graph-control-in-reports.html language=enus -->
## TOPIC 00250: Customizing the Graph Control in Reports

- bundle_id: `teststand`
- source_path: `customizing-the-graph-control-in-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/customizing-the-graph-control-in-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can customize the graph control for your reports by editing the stylesheet for the report. Removing Grid Lines Complete the following steps to remove grid lines from the graph: Open one of the following files in a text editor: For HTML reports, open <TestStand_Components>\Models\TestStandModels\

### Customizing the Graph Control in Reports

You can customize the graph control for your reports by editing the stylesheet for the report.

#### Removing Grid Lines

Complete the following steps to remove grid lines from the graph:

1. Open one of the following files in a text editor:
  - For HTML reports, open <TestStand_Components>\Models\TestStandModels\modelsupport2\c_report.c .
  - For XML and ATML reports, open the stylesheet listed in the Style Sheet field of the Report Options dialog box.
2. Search for the GRID_LINES comment.
3. Set the value of the variable gridLines to "grid-lines" to enable grids lines, or to "" to disable grid lines.
4. For HTML reports, open <TestStand_Components>\Models\TestStandModels\modelsupport2\modelsupport2.prj in LabWindows/CVI and build modelsupport2.dll for the corresponding bitness of TestStand you are using.

The following image shows how the graph looks without grid lines.[IMAGE alt='image' src='GUID-8D0ABEBE-B30D-4677-AF51-4CDC76FA9C5F-a5.png']

#### Enabling the Display of Coordinates when Hovering Over a Point

Complete the following steps to enable displaying coordinates when you hover a mouse over a point on the graph:

1. Open one of the following files in a text editor:
  - For HTML reports, open <TestStand_Components>\Models\TestStandModels\modelsupport2\c_report.c .
  - For XML and ATML reports, open the stylesheet listed in the Style Sheet field of the Report Options dialog box.
2. Search for the ENABLE_HOVER comment.
3. Set the value of the variable enableHover to "enable-hover" to enable hovering, or to "" to disable hovering.
4. For HTML reports, open <TestStand_Components>\Models\TestStandModels\modelsupport2\modelsupport2.prj in LabWindows/CVI and build modelsupport2.dll for the corresponding bitness of TestStand you are using.

The following image shows how the graph looks when hover is enabled.[IMAGE alt='image' src='GUID-8F72F9E2-7236-46BC-A7F9-35D48EA3B7E6-a5.png']

#### Changing the Background Color of the Graph (Excluding the Plot)

Complete the following steps to change the background color of the area outside the plot of the graph:

1. Open one of the following files in a text editor:
  - For HTML reports, open <TestStand_Components>\Models\TestStandModels\modelsupport2\c_report.c .
  - For XML and ATML reports, open the stylesheet listed in the Style Sheet field of the Report Options dialog box.
2. Search for the CHANGE_BACKGROUND_COLOR comment.
3. Change the value of background-color in the <ni-cartesian-graph> tag to the required color name or hex color code. Refer to HTML Color Codes for more information.
4. For HTML reports, open <TestStand_Components>\Models\TestStandModels\modelsupport2\modelsupport2.prj in LabWindows/CVI and build modelsupport2.dll for the corresponding bitness of TestStand you are using.

The following image shows how the graph looks when value is set to #dddddd.[IMAGE alt='image' src='GUID-A828EC3C-D882-4786-A814-6A039004A40F-a5.png']

#### Changing the Background Color of the Plot

Complete the following steps to change the background color of the plot area of the graph:

1. Open <TestStand_Components>\Models\TestStandModels\GraphControl\TSGraphStyle.css in a text editor.
2. Search for the CHANGE_BACKGROUND_COLOR comment.
3. Change the value of background-color to the required color name or hex color code. Refer to HTML Color Codes for more information.

The following image shows how the graph looks when the value is set to #000000 (black).[IMAGE alt='image' src='GUID-E28D120F-96FA-4FEE-9834-0528A09C6DCB-a5.png']

Parent topic:

Generating and Customizing TestStand Reports

Related information:

- HTML Color Codes
