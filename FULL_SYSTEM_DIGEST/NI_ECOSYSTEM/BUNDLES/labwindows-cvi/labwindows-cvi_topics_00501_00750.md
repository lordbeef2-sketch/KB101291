# NI DOCUMENT BUNDLE: labwindows-cvi

<!--NI_BUNDLE_CHUNK bundle=labwindows-cvi start=501 end=750 -->
<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvitdms_getchannelgroupstringpropertylength.htm language=enus -->
## TOPIC 00501: TDMS_GetChannelGroupStringPropertyLength

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvitdms_getchannelgroupstringpropertylength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvitdms_getchannelgroupstringpropertylength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TDMS_GetChannelGroupStringPropertyLength

int TDMS_GetChannelGroupStringPropertyLength (TDMSChannelGroupHandle channelGroup, const char *property, unsigned int *length);

#### Purpose

Gets the length of the current value of a string property. The length does not include the terminating NUL byte.

You can call this function to determine the necessary buffer size before getting the value of a string property.

#### Parameters

| Input |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Description |  |
| channelGroup | TDMSChannelGroupHandle | The channel group handle. |  |
| property | const char * | The name of the channel group property. You can specify a built-in property, virtual property, or a property created by TDMS_SetChannelGroupProperty. Virtual properties are special properties that are not saved in the .tdms file, but they can be used to perform certain actions. The following built-in properties are available: Property Constant Data Type Name TDMS_CHANNELGROUP_NAME String (char *) Description TDMS_CHANNELGROUP_DESCRIPTION String (char *) The following virtual properties are available: Property Constant Data Type Description NI_MinimumBufferSize TDMS_NI_MINIMUM_BUFFER_SIZE unsigned int Use this property to reduce the size of a .tdms file by controlling the number of times the data is written to disk. |  |
| Property | Constant | Data Type |  |
| Name | TDMS_CHANNELGROUP_NAME | String (char *) |  |
| Description | TDMS_CHANNELGROUP_DESCRIPTION | String (char *) |  |
| Property | Constant | Data Type | Description |
| NI_MinimumBufferSize | TDMS_NI_MINIMUM_BUFFER_SIZE | unsigned int | Use this property to reduce the size of a .tdms file by controlling the number of times the data is written to disk. |
| Output |  |  |  |
| Name | Type | Description |  |
| length | unsigned int | The length of the current value of the string property. The length does not include the terminating NUL byte. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero represents successful execution and a negative number represents the error code. Error codes are defined in cvi\\include\\cvitdms.h. |

#### Additional Information

**Library:** [TDM Streaming Library](../../cvi/libref/cvitdmslibraryfunctiontree.htm)

**Include file:** cvitdms.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

© 2016 National Instruments. All rights reserved.

#### Example

Refer to TDM Streaming\tdmsReader.cws for an example of using the TDMS_GetChannelGroupStringPropertyLength function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvivariants_and_safe_arrays.htm language=enus -->
## TOPIC 00502: Interacting with Variant and Safe Array Data Types

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvivariants_and_safe_arrays.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvivariants_and_safe_arrays.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Interacting with Variant and Safe Array Data Types

The VARIANT data type is a structure that can hold a value of any valid ActiveX
data type. Refer to the [Fundamental Data Types for Variants, Safe Arrays, and Properties](cvidata_types_for_variants_safe_arr.htm#b5105a57) table and to the [Data Type Modifiers for Variants, Safe Arrays, and Properties](cvidata_types_for_variants_safe_arr.htm#b5105a58) table for valid ActiveX data types. ActiveX server functions
declare a parameter as a VARIANT when the parameter can take a value of more than one data type. This help
uses the term *variant* to refer to parameters or variables declared with the VARIANT data type. The ActiveX Library provides functions to help you pass
values as variant input parameters and retrieve values from variant output
parameters.

The SAFEARRAY data type is a structure that holds an array of data, the number of
dimensions in the array, and the size of each dimension. ActiveX server
functions use the SAFEARRAY data type to pass arrays. This document uses the term *safe array* to refer to parameters or variables declared with the SAFEARRAY data type. The ActiveX Library provides functions to convert
between C-style arrays and safe arrays stored inside variants, functions to obtain the number of dimensions
in a safe array, and functions to obtain the size of each dimension.

You can declare a variant structure as a local or global variable, but safe
arrays are always dynamically allocated. Consequently, you must always reference
safe arrays using pointers. Use the LPSAFEARRAY typedef to declare a pointer to a safe array. Microsoft adds LP at the beginning of data type names to indicate a pointer to a data type.
Thus, LPSAFEARRAY signifies a pointer to a SAFEARRAY.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvivariants_that_store_values_in_dy.htm language=enus -->
## TOPIC 00503: Variants That Store Values in Dynamic Memory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvivariants_that_store_values_in_dy.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvivariants_that_store_values_in_dy.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Variants That Store Values in Dynamic Memory

Variants of the following data types store their values in dynamically
allocated memory.

CAVT_CSTRING

CAVT_OBJHANDLE

<any type> | CAVT_ARRAY

The functions that retrieve values from such variants free the memory. If you
do not retrieve the value stored in the variant, you can free the contents of the
variant using CA_VariantClear.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cvivprintf.htm language=enus -->
## TOPIC 00504: vprintf

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cvivprintf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cvivprintf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### vprintf

int vprintf (const char formatString[], va_list argumentList);

#### Purpose

Writes output to standard output according to format specifiers in **formatString**. This function is similar to
[printf](../../cvi/libref/cviprintf.htm) except that vprintf
takes as a parameter an argument list initialized by the va_start macro.

|  | Note You cannot execute this function panel because of the nature of how variable argument lists are created. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| formatString | const char [] | Contains the format string that specifies how subsequent arguments are converted for output. Use standard ANSI C format specifiers. If insufficient arguments exist for the format, the behavior is undefined. If the format is exhausted while arguments remain, the excess arguments are evaluated but are otherwise ignored. Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |
|  | Note For more information about the standard ANSI C format specifiers, refer to an external ANSI C reference. |  |
| argumentList | va_list | Contains a variable argument list initialized by the va_start macro and possibly subsequent va_arg calls. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| CharactersWritten | int | Contains the number of characters transmitted or a negative value if an output error occurred. If an error occurs, vprintf sets errno to a nonzero value. |

#### Additional Information

**Library:** [ANSI C Library](../../cvi/libref/cviansi_c_libfunctiontree.html)

**Include file:** ansi_c.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/libref/cviwind_hpf.htm language=enus -->
## TOPIC 00505: Wind_HPF

- bundle_id: `labwindows-cvi`
- source_path: `cvi/libref/cviwind_hpf.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/libref/cviwind_hpf.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Wind_HPF

*Advanced Analysis Library Only*

AnalysisLibErrType Wind_HPF (double samplingFrequency, double cutoffFrequency, int numberOfCoef, double coefficientArray[], int windowType);

#### Purpose

|  | Note This function has been superseded by WindFIR_Filter. |
| --- | --- |

Designs a digital highpass FIR linear phase filter using a windowing technique. Five windows are available. Wind_HPF generates only the filter coefficients; it does not actually perform data filtering.

The attenuation value determines the approximate peak value of the sidelobes. Transition bandwidth determines a frequency range over which the filter response changes from the pass band to the stop band or from the stop band to the pass band. For more information, refer to *Discrete-Time Signal Processing* by Oppenheim and Schafer, cited in the [Bibliography](../../cvi/libref/cvibibliography_for_advanced_analys.htm).

##### Example Code

/* Design a 55-point highpass FIR linear phase filter that can achieve at least a 44 dB attenuation and filter the incoming signal with the designed filter. */ 
 
double x[256], coef[55], y[310], fs, fc; 
 
n, m, windType; 
 
fs = 1000.0; /* sampling frequency */ 
 
fc = 200.0; /* desired cutoff frequency */ 
 
n = 55; /* filter length */ 
 
windType = 3; /* using Hanning window */ 
 
m = 256; 
 Wind_HPF (fs, fc, n, coef, windType); 
 
Convolve (coef, n, x, m, y); /* Convolve the filter with the signal. */

#### Parameters

| Input |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Description |  |
| samplingFrequency | double | Sampling frequency in Hertz. |  |
| cutoffFrequency | double | Cutoff frequency of the filter in Hertz. |  |
| numberOfCoef | int | Length of the window FIR filter. numberOfCoef must be odd for this filter. |  |
| windowType | int | Window type. windowType selects one of the five windows as shown in the following table. windowType Window Attenuation (dB) Transition Bandwidth (fs/n) 1 Rectangular 21 0.9 2 Triangular 25 1.18 3 Hanning 44 2.5 4 Hamming (Default) 53 3.13 5 Blackman 74 4.6 |  |
| windowType | Window | Attenuation (dB) | Transition Bandwidth (fs/n) |
| 1 | Rectangular | 21 | 0.9 |
| 2 | Triangular | 25 | 1.18 |
| 3 | Hanning | 44 | 2.5 |
| 4 | Hamming (Default) | 53 | 3.13 |
| 5 | Blackman | 74 | 4.6 |
| Output |  |  |  |
| Name | Type | Description |  |
| coefficientArray | double [] | Calculated output window FIR filter coefficients. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | AnalysisLibErrType | A value that specifies the type of error that occurred. Refer to analysis.h for definitions of these constants. |

#### Additional Information

**Library:** [Advanced Analysis Library](../../cvi/libref/cviadvanced_analysis_library_overvi.htm)

**Include file:** analysis.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/recsforcreatingdll.htm language=enus -->
## TOPIC 00506: Recommendations for Creating a DLL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/recsforcreatingdll.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/recsforcreatingdll.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Recommendations for Creating a DLL

To make creating a DLL as simple as possible, adhere to the following recommendations:

- Use the DLLSTDCALL macro in the declaration and definition of all functions you want to export. Do not export functions with a variable number of arguments.
- Identify the symbols you want to export using the include file method. Do not use export qualifiers. If you use an external compiler , use the .def file method.
- Do not export variables from the DLL. For each variable you want to export, create functions to get and set the variable value or a function to return a pointer to the variable. Do not use import qualifiers in the include file.

If you follow these recommendations, you gain the following benefits:

- You can distribute with your DLL the same include file that you include in the source files you use to make the DLL. This is especially useful when you create DLLs from instrument drivers.
- You can use the same source code to create the DLL in LabWindows/CVI and the external compiler .
- You can use your DLL in Microsoft Visual Basic or other non-C environments.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/rules_for_using_dll_files.htm language=enus -->
## TOPIC 00507: Rules for Using DLL Files

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/rules_for_using_dll_files.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/rules_for_using_dll_files.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Rules for Using DLL Files

Your executable or DLL can link to a DLL only through an import library. This section refers to a DLL that an executable or another DLL uses as a *subsidiary* DLL. You can link an import library into your program in any of the following ways:

- List the DLL import library in your project
- Associate the DLL import library with the .fp file for an instrument driver or user library
- Dynamically load the DLL import library by calling the Windows SDK function LoadLibrary

If you list a DLL import library in the project or associate it with an instrument driver or user library, LabWindows/CVI statically links the import library into your executable or DLL. However, if you load the import library through a call to LoadLibrary, you must distribute it separately from your executable.

Regardless of the method you use to link the import library, you must distribute the subsidiary DLL separately. The import library always contains the name of the subsidiary DLL. When your executable or DLL is loaded, the operating system finds the subsidiary DLL using the standard DLL search algorithm. For information about the DLL search algorithm, refer to the help for LoadLibrary on www.msdn.com. The search precedence is as follows:

1. The directory from which the user loads the application
2. The current working directory
3. The Windows system directory
4. The Windows directory
5. The directories listed in the PATH environment variable

When you create a [new distribution](../usermanual/newdistdb.htm), LabWindows/CVI automatically adds the DLLs to which your project refers to the **Installation Files & Directories** browser in the Edit Installer dialog box [Files](../usermanual/editinstallerfiles.htm) tab. You must build your project for LabWindows/CVI to automatically add these dependent files to the installer. You must use the **Files** tab to add to the installer any DLLs that you load by calling the Windows SDK function LoadLibrary.

Do not use the Edit Installer dialog box **Files** tab to include DLLs for National Instruments hardware in your installer. Instead, select the necessary hardware components in the Edit Installer dialog box [Drivers & Components](../usermanual/editinstallerdc.htm) tab.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/rulesforaccessinguirimagepanelstatefiles.htm language=enus -->
## TOPIC 00508: Rules for Accessing .uir, Image, and Panel State Files

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/rulesforaccessinguirimagepanelstatefiles.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/rulesforaccessinguirimagepanelstatefiles.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Rules for Accessing .uir, Image, and Panel State Files

To access .uir, image, and panel state files in your executable program, place the files in the same directory as the executable and pass simple filenames with no drive letters or directory names to LoadPanel, LoadPanelEx, DisplayImageFile, SavePanelState, and RecallPanelState.

If you do not want to store these files in the same directory as your executable, you must pass pathnames to LoadPanel, LoadPanelEx, DisplayImageFile, SavePanelState, and RecallPanelState. These functions interpret relative pathnames as being relative to the directory that contains the executable.

|  | Note You do not need to include .uir files if you have enabled the Embed project .UIRs option in the Target Settings dialog box. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/runningcodeinsecondarythreads.htm language=enus -->
## TOPIC 00509: Running Code in Secondary Threads

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/runningcodeinsecondarythreads.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/runningcodeinsecondarythreads.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Running Code in Secondary Threads

The thread in a single-threaded program is referred to as the *main thread*. The OS creates the main thread when the user tells the OS to begin executing a particular program. In a multithreaded program, the program itself tells the OS to create threads in addition to the main thread. These threads are referred to as *secondary threads*. A major difference between the main thread and secondary threads is where each type of thread begins execution. The OS begins execution of the main thread in the main or WinMain function. You specify the function in which each secondary thread begins executing.

In a typical LabWindows/CVI multithreaded program, you use the main thread to create, display, and run the [user interface](../uiref/cvidifferent_approaches_to_multithr.htm). You then use secondary threads to perform other time-critical operations such as data acquisition. LabWindows/CVI provides two high-level mechanisms for running code in secondary threads: thread pools and asynchronous timers. A [thread pool](usingthreadpool.htm) is appropriate for tasks that you need to perform a discrete number of times or tasks that you need to perform in a loop. An [asynchronous timer](../../toolslib/toolslibasychronous_timers_control.htm) is appropriate for tasks that you need to perform at regular intervals.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/settingprocessor.htm language=enus -->
## TOPIC 00510: Setting the Preferred Processor for a Thread

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/settingprocessor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/settingprocessor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Setting the Preferred Processor for a Thread

You can use the following Windows SDK functions if you want to set a processor for threads in your program.

- Call SetThreadIdealProcessor if you need to specify the processor on which to run a particular thread.
- Call SetProcessAffinityMask to specify the processors on which the threads in your program are allowed to run.
- Call SetThreadAffinityMask to specify processors on which a particular thread in your program is allowed to run.

|  | Note The SetThreadIdealProcessor and SetThreadAffinityMask functions take a thread handle as their first parameter. You can call the LabWindows/CVI Utility Library CmtGetThreadPoolFunctionAttribute function with the ATTR_TP_FUNCTION_THREAD_HANDLE attribute to obtain the handle of a thread pool thread. The second parameter to SetThreadIdealProcessor is the zero-based index of the processor. You can call the LabWindows/CVI Utility Library CmtGetNumProcessors function to programmatically determine the number of processors in the machine that is running your program. The mask you pass to SetThreadAffinityMask must be a subset of the mask you pass to SetProcessAffinityMask. These functions have an effect only when your program runs on a multiprocessor machine. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/specifyinglibdependencies.htm language=enus -->
## TOPIC 00511: Specifying Library Dependencies

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/specifyinglibdependencies.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/specifyinglibdependencies.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Specifying Library Dependencies

When one library you distribute depends on another library you distribute, you can specify this dependency in the function panel file for the dependent library. When LabWindows/CVI loads the dependent library, it attempts to load the libraries upon which it depends. Use the [Edit».FP Auto-Load List](../usermanual/fteeditfpautoloadlist.htm) command in the Function Tree Editor of the dependent library to list the .fp files of the libraries upon which it depends.

LabWindows/CVI can find the required libraries most easily when they are all in the same directory as the dependent library. When you cannot put them in the same directory, you must add the directories in which the required libraries reside to the user's Instrument Directories list. The user can manually enter this information using the [Instrument»Search Directories](../usermanual/prjinstrumentdirectories.htm) command in the Workspace window. Also, you can add to the Instrument Directories list by editing the Registry.

The modreg program is in the LabWindows/CVI bin subdirectory for this purpose. A documentation file called modreg.txt is in the same directory.

Assume that you install two .fp files in the following locations:

c:\newlib\liba.fp 

 c:\genlib\libb.fp

If liba depends on libb, you must add the following path to the user's Instrument Directories list:

c:\genlib

For LabWindows/CVI to be able to find the dependent file, use the following modreg command file:

setkey [HKEY_LOCAL_MACHINE\Software\National Instruments] 

 appendkey CVI\*major.minor* 
 
 add InstrumentDirectories InstrDir "c:\genlib"

*major.minor* refers to the LabWindows/CVI version, for example 9.1. Refer to the [LabWindows/CVI Year-Based and Major.Minor.Tiny Version Equivalents](../cviversioning.htm) for the current *major.minor* version equivalent.

After the user installs the library files, the modreg program must be run on the user's disk using the command file.

|  | Note Make sure that LabWindows/CVI is not running when you use the modreg program to modify the Registry. If LabWindows/CVI is running while you use this program, you will lose your changes. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/stacksize.htm language=enus -->
## TOPIC 00512: Stack Size

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/stacksize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/stacksize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Stack Size

Your program uses the stack to pass function parameters and store automatic local variables. You can set the maximum stack size by selecting [Options»Build Options](../usermanual/prjbuildopt.htm) in the Workspace window. LabWindows/CVI supports the following stack size range:

- Minimum = 100 KB
- Default = 250 KB
- Maximum = 2 GB

If you enable the **Detect uninitialized local variables at run time** option in the Build Options dialog box, LabWindows/CVI might use extra stack space. You can adjust your maximum stack size to avoid a stack overflow.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/statusreportindataacq.htm language=enus -->
## TOPIC 00513: Status Reporting by the Traditional NI-DAQ Library

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/statusreportindataacq.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/statusreportindataacq.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Status Reporting by the Traditional NI-DAQ Library

The Traditional NI-DAQ Library functions return negative values when they detect errors. They return positive values as warnings when they are able to complete their tasks but not in the way you might expect. This library uses a common set of error codes. The positive warning codes are the same absolute values as the negative error codes.

You can use GetNIDAQErrorString to get the error message associated with each Traditional NI-DAQ Library error or warning code.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/statusreportinnidaqmx.htm language=enus -->
## TOPIC 00514: Status Reporting by the NI-DAQmx Library

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/statusreportinnidaqmx.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/statusreportinnidaqmx.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Status Reporting by the NI-DAQmx Library

The NI-DAQmx Library functions return negative values when they detect errors. They return positive values as warnings when they are able to complete their tasks but not in the way you might expect.

You can use DAQmxGetErrorString to get the error message associated with each NI-DAQmx Library error or warning code. Use DAQmxGetExtendedErrorInfo to get additional information about the last error reported. For example, if an error occurs in an attribute function and you call DAQmxGetExtendedErrorInfo, LabWindows/CVI provides information such as the attribute name, what you set the attribute to, and what values are valid for that attribute in addition to the error message.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/threadsafevariable.htm language=enus -->
## TOPIC 00515: Using Thread Safe Variables to Protect Data

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/threadsafevariable.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/threadsafevariable.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Using Thread Safe Variables to Protect Data

Thread safe variables combine your variable and an OS thread-locking object into a single entity. This approach offers the following advantages over using a thread lock to protect a piece of data:

- Using thread safe variables can help you avoid one of the most common errors in multithreaded programs: forgetting to get a lock before accessing a variable. 
With thread safe variables, you must call a Utility Library function to get access to the data. Because the API function acquires the OS thread-locking object, you will not accidentally access the data without acquiring the OS thread-locking object.
- This approach also makes it easier to pass protected data between functions because you have to pass only the thread safe variable handle rather than passing a thread-lock handle and the variable that it protects.

The LabWindows/CVI Utility Library contains [functions for creating and accessing thread safe variables](../libref/thread_safe_variable_class_utility.html). With these functions, you can create thread safe variables of any type. Typically, you do not call the LabWindows/CVI Utility Library thread safe variable functions directly. Instead, you can [use macros](../libref/macrosandtsvariables.htm) that provide type-safe wrapper functions around the Utility Library functions. In addition to providing type safety, these macros also help you avoid forgetting to release the lock after accessing the data and attempting to release the lock without previously acquiring the lock.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/translatingmessagefile.htm language=enus -->
## TOPIC 00516: Translating the Message File

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/translatingmessagefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/translatingmessagefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Translating the Message File

The message file, msgrte.txt, is a text file that contains the error messages that the LabWindows/CVI Runtime displays. You can find msgrte.txt in the bin folder of the [LabWindows/CVI Runtime installation directory](cvirtengine.htm). To translate the message file into other languages, complete the following steps:

|  | Note This procedure suggests a naming convention for translated message files; in this example, creating a German message file. You can use your own naming convention. |
| --- | --- |

1. Make a copy of the original msgrte.txt file named msgrte-draft-de.txt .
2. Use a text editor to translate msgrte-draft-de.txt . Modify only the text that is inside quotation marks. Do not add or delete any message numbers.
3. Run countmsg.exe on the file to encode msgrte-draft-de.txt for use with the Runtime, as shown in the following example: 

 countmsg <*Location of file*>\msgrte-draft-de.txt <*Location to save file*>\msgrte-de.txt 
 [IMAGE alt='Note' src='note.gif']
**Note** countmsg.exe is located in the LabWindows/CVI bin folder.

msgrte-de.txt is the translated and encoded file. Because encoding the message file includes setting a count marker in the file, make edits to msgrte-draft-de.txt and run countmsg.exe again.

You can include the translated, encoded message file in a LabWindows/CVI [Windows installer](../usermanual/editinstalleradvanced.htm#msgfile) or [package](../usermanual/editpackageadvanced.htm#msgfile) distribution. If you have an existing, translated message file and want to support a different version of LabWindows/CVI than the version with which you translated and encoded the message file, complete the following steps:

1. Compare the existing, translated message file and the message file that ships with the other version of LabWindows/CVI.
2. Replicate the changes from the other version of LabWindows/CVI into your existing translated file.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/programmerref/typesofdatatoprotect.htm language=enus -->
## TOPIC 00517: Types of Data to Protect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/programmerref/typesofdatatoprotect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/programmerref/typesofdatatoprotect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Types of Data to Protect

Global variables, static local variables, and dynamically allocated memory are located in common memory areas that are accessible to all threads in a program. Make sure that you [protect data](protectingdatamulti.htm) stored in these types of memory locations against concurrent access from multiple threads to ensure that values are not corrupted. Function parameters and nonstatic local variables are located on the stack. The OS allocates a separate stack for each thread. Therefore, each thread gets its own copy of parameters and nonstatic local variables, so parameters and nonstatic local variables do not have to be protected against concurrent access. The following code shows which types of data must be protected against concurrent access by multiple threads.

int globalArray[1000];// Must be protected 

static staticGlobalArray[500];// Must be protected 

void foo (int i)// i does NOT need to be protected 

int globalInt;// Must be protected

{

int localInt;// Does NOT need to be protected 

int localArray[1000];// Does NOT need to be protected 

int *dynamicallyAllocdArray;// Must be protected 

static int staticLocalArray[1000];// Must be protected 

dynamicallyAllocdArray = malloc (1000 * sizeof (int));

}

For example, consider a multithreaded program that increments an integer global counter variable from multiple threads as follows:

count = count + 1;

This code is executed as the following sequence of CPU instructions:

1. Move the value in count into a processor register
2. Increment the value in the processor register
3. Write the value in the processor register back into count

Because the OS might interrupt a thread at arbitrary points in its execution, two threads executing this sequence of instructions could execute them in the following order (assume that count starts with the value 5):

Thread 1: Move the value in count into a processor register. (count = 5, register = 5) 

Switch to Thread 2. (count = 5, register = ?) 

Thread 2: Move the value in count into a processor register. (count = 5, register = 5) 

Thread 2: Increment the value in the processor register. (count = 5, register = 6) 

Thread 2: Write the value in the processor register back into count. (count = 6, register = 6) 

Switch to Thread 1. (count = 6, register = 5) 

Thread 1: Increment the value in the processor register. (count = 6, register = 6) 

Thread 1: Write the value in the processor register back into count. (count = 6, register = 6)

Because thread 1 was interrupted before it could increment the value and write it back, the value of count is set to 6 instead of 7. The OS keeps a separate copy of the processor registers for each thread in the system. Even if you write the code as count++, you continue to have the same problem because the processor continues to execute the code as multiple instructions. Notice the particular timing condition that causes this failure. This means that your program might run correctly 1000 times for each time it fails. Empirical evidence has shown that multithreaded programs with incorrect data protection typically run correctly during testing but fail immediately when your customer installs and runs them.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviaddpaneltosplitter.htm language=enus -->
## TOPIC 00518: AddPanelToSplitter

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviaddpaneltosplitter.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviaddpaneltosplitter.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### AddPanelToSplitter

int AddPanelToSplitter (int panelHandle, int controlID, int anchor, int panelToAttach, int snapOnAttach, int attachmentMode);

#### Purpose

Attaches a new panel to the splitter control. Once attached, this panel is automatically sized or moved whenever you operate the splitter.

The panel to be attached must already be a child panel belonging to the same panel as the splitter.

#### Supported Controls

You can use AddPanelToSplitter with [splitter controls](../../cvi/uiref/cviprogramming_with_splitter_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| anchor | int | This parameter determines to which edge of the splitter control you are attaching the panel. For horizontal splitters, valid choices are VAL_TOP_ANCHOR and VAL_BOTTOM_ANCHOR. For vertical splitters, valid choices are VAL_LEFT_ANCHOR and VAL_RIGHT_ANCHOR. Constant Name Constant Value VAL_RIGHT_ANCHOR -2147483633 VAL_LEFT_ANCHOR -2147483634 VAL_BOTTOM_ANCHOR -2147483635 VAL_TOP_ANCHOR -2147483636 Which edge of the splitter you attach a panel determines how the panel is sized. For example, if you attach a panel to the left edge of the splitter, then the right edge of the panel follows the splitter, thus sizing the panel. |
| Constant Name | Constant Value |  |
| VAL_RIGHT_ANCHOR | -2147483633 |  |
| VAL_LEFT_ANCHOR | -2147483634 |  |
| VAL_BOTTOM_ANCHOR | -2147483635 |  |
| VAL_TOP_ANCHOR | -2147483636 |  |
| panelToAttach | int | Pass the specifier for the particular panel that you want to attach. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| snapOnAttach | int | Specify a nonzero value or select Yes in the function panel if you want the panel that is being attached to automatically move to the corresponding edge of the splitter control. For example, if you pass VAL_BOTTOM_ANCHOR as the anchor parameter, LabWindows/CVI places the panel immediately below the splitter. In this case, the horizontal position of the panel would not be affected. Specify 0 or select No in the function panel otherwise. |
| attachmentMode | int | Specify a nonzero value or select Move control in the function panel to move the panel that is being attached when you operate the splitter control. Specify 0 or select Size control in the function panel to size the panel that is being attached when you operate the splitter control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the AddPanelToSplitter function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattractualxdivisions.htm language=enus -->
## TOPIC 00519: ATTR_ACTUAL_XDIVISIONS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattractualxdivisions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattractualxdivisions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ACTUAL_XDIVISIONS

| Type: | Control attribute |
| --- | --- |
| Description: | Returns the actual number of X-divisions for the graph if ATTR_XDIVISIONS is set to VAL_AUTO. Returns the value set in ATTR_XDIVISIONS if ATTR_XDIVISIONS is not set to VAL_AUTO. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| Valid Range: | 1 to 100 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationcaption.htm language=enus -->
## TOPIC 00520: ATTR_ANNOTATION_CAPTION

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationcaption.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationcaption.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_CAPTION

| Type: | Annotation attribute |
| --- | --- |
| Description: | The string displayed in the caption of the annotation. To determine the size of the buffer to pass when you are obtaining the caption, call GetAnnotationAttribute and specify the ATTR_ANNOTATION_CAPTION_LENGTH attribute. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationcaptionangle.htm language=enus -->
## TOPIC 00521: ATTR_ANNOTATION_CAPTION_ANGLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationcaptionangle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationcaptionangle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_CAPTION_ANGLE

| Type: | Annotation attribute |
| --- | --- |
| Description: | Specifies the angle of rotation, in tenths of degrees, of the annotation text. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationlocked.htm language=enus -->
## TOPIC 00522: ATTR_ANNOTATION_LOCKED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationlocked.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationlocked.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_LOCKED

| Type: | Annotation attribute |
| --- | --- |
| Description: | Specifies whether the user can move the annotation caption when ATTR_CTRL_MODE is not set to VAL_INDICATOR. 0 = Not locked 1 = Locked |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationoffsetmode.htm language=enus -->
## TOPIC 00523: ATTR_ANNOTATION_OFFSET_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationoffsetmode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationoffsetmode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_OFFSET_MODE

| Type: | Annotation attribute |
| --- | --- |
| Description: | Specifies the caption offset mode of the annotation. If the value is set to VAL_GLYPH_OFFSET, then the offset is calculated relative to the point being annotated. If the value is set to VAL_TOP_LEFT_OFFSET, then the offset is calculated relative to the top-left corner of the plot area. |
| Data Type: | integer |
| Default Value: | VAL_GLYPH_OFFSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_GLYPH_OFFSET | The caption offset is calculated relative to the point being annotated. |
| --- | --- |
| VAL_TOP_LEFT_OFFSET | The caption offset is calculated relative to the top-left corner of the plot area. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationvisible.htm language=enus -->
## TOPIC 00524: ATTR_ANNOTATION_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_VISIBLE

| Type: | Annotation attribute |
| --- | --- |
| Description: | Specifies whether the annotation is visible. 0 = Hidden 1 = Visible |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationxaxis.htm language=enus -->
## TOPIC 00525: ATTR_ANNOTATION_XAXIS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationxaxis.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationxaxis.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_XAXIS

| Type: | Annotation attribute |
| --- | --- |
| Description: | Changes the x-axis with which the graph annotation is associated. When a graph annotation is created, the x-axis with which it is associated is determined by the value of ATTR_ACTIVE_XAXIS. Afterwards, you can use ATTR_ANNOTATION_XAXIS to change the association. The associated x-axis serves as the reference for the annotation position coordinates for ATTR_ANNOTATION_XVALUE. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_BOTTOM_XAXIS | The x-axis on the bottom of the graph. |
| --- | --- |
| VAL_TOP_XAXIS | The x-axis on the top of the graph. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationxoffset.htm language=enus -->
## TOPIC 00526: ATTR_ANNOTATION_XOFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationxoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationxoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_XOFFSET

| Type: | Annotation attribute |
| --- | --- |
| Description: | The x-offset of the caption, in pixels, from the top-left corner of the caption to the point being annotated or the top-left corner of the graph, depending on the value of ATTR_ANNOTATION_OFFSET_MODE. If the offset mode is VAL_TOP_LEFT_OFFSET, specifying a negative value for the x-offset will result in some or all of the caption being placed outside the plot area, if ATTR_ANNOTATION_CAPTION_ALWAYS_IN_VIEW is disabled. |
| Data Type: | integer |
| Default Value: | 50 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrannotationxvalue.htm language=enus -->
## TOPIC 00527: ATTR_ANNOTATION_XVALUE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrannotationxvalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrannotationxvalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ANNOTATION_XVALUE

| Type: | Annotation attribute |
| --- | --- |
| Description: | The x-value of the annotated point. The annotation glyph is displayed at this point, and the arrowhead and line attached to the caption always point toward it. |
| Data Type: | double |
| Default Value: | 50.00 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrautosizing.htm language=enus -->
## TOPIC 00528: ATTR_AUTO_SIZING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrautosizing.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrautosizing.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_AUTO_SIZING

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the button is automatically resized when you programmatically change its text. |
| Control Types: | Command buttons, text buttons. |
| Data Type: | integer |
| Default Value: | VAL_GROW_ONLY |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.0 and later |

##### Values

| VAL_ALWAYS_AUTO_SIZE | Command button is always resized to fit its text. |
| --- | --- |
| VAL_GROW_ONLY | Command button is resized when the text does not fit in the button. |
| VAL_SHRINK_ONLY | Command button is resized when the text is smaller than the button. |
| VAL_NEVER_AUTO_SIZE | Command button is never resized. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrbackcolor_panel.htm language=enus -->
## TOPIC 00529: ATTR_BACKCOLOR (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrbackcolor_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrbackcolor_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_BACKCOLOR (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The RGB color value of the panel background. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrbackcolor_tab page.htm language=enus -->
## TOPIC 00530: ATTR_BACKCOLOR (Tab Page)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrbackcolor_tab page.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrbackcolor_tab%20page.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_BACKCOLOR (Tab Page)

| Type: | Tab Page attribute |
| --- | --- |
| Description: | The RGB color value of the tab page background. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrbinaryswitchcolor.htm language=enus -->
## TOPIC 00531: ATTR_BINARY_SWITCH_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrbinaryswitchcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrbinaryswitchcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_BINARY_SWITCH_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the binary switch. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Binary switches. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrbold_control menu.htm language=enus -->
## TOPIC 00532: ATTR_BOLD (Control Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrbold_control menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrbold_control%20menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_BOLD (Control Menu)

| Type: | Control Menu attribute |
| --- | --- |
| Description: | Specifies whether a menu item is bold. 0 = Not bold 1 = Bold |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrbold_menu.htm language=enus -->
## TOPIC 00533: ATTR_BOLD (Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrbold_menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrbold_menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_BOLD (Menu)

| Type: | Menu attribute |
| --- | --- |
| Description: | Specifies whether a menu item is bold. 0 = Not bold 1 = Bold |
| Menu Objects: | Menu Items. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcasesensitivecompare_row.htm language=enus -->
## TOPIC 00534: ATTR_CASE_SENSITIVE_COMPARE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcasesensitivecompare_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcasesensitivecompare_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CASE_SENSITIVE_COMPARE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies whether case sensitive comparisons are made when looking for a specific string in the item list of a cell. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcellframecolor_column.htm language=enus -->
## TOPIC 00535: ATTR_CELL_FRAME_COLOR (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcellframecolor_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcellframecolor_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CELL_FRAME_COLOR (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The RGB color value of the pull-down area of a ring or a combo box cell. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcellframecolor_control.htm language=enus -->
## TOPIC 00536: ATTR_CELL_FRAME_COLOR (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcellframecolor_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcellframecolor_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CELL_FRAME_COLOR (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The default RGB color value of the pull-down area of new ring or combo box table cells when ATTR_TABLE_MODE is set to VAL_GRID. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Tables. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcellmode_row.htm language=enus -->
## TOPIC 00537: ATTR_CELL_MODE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcellmode_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcellmode_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CELL_MODE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies the mode of the table cell. |
| Data Type: | integer |
| Default Value: | VAL_HOT |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_INDICATOR | The cell can be changed programmatically, but operator action cannot generate commit or value changed events. |
| --- | --- |
| VAL_HOT | The cell can be operated by the user or changed programmatically. User action can generate commit or value changed events. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcelltype_cell.htm language=enus -->
## TOPIC 00538: ATTR_CELL_TYPE (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcelltype_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcelltype_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CELL_TYPE (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | Specifies the type of the table cell. |
| Data Type: | integer |
| Default Value: | VAL_CELL_STRING |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_CELL_BUTTON | The cell consists of a labelled button that can be depressed. |
| --- | --- |
| VAL_CELL_RING | The cell holds a list of items from which the cell value can be selected. |
| VAL_CELL_COMBO_BOX | The cell holds text data and a list of items. The cell's value can be selected from this list, or it can be set independently. |
| VAL_CELL_NUMERIC | The cell holds numeric data. |
| VAL_CELL_STRING | The cell holds text data. |
| VAL_CELL_PICTURE | The cell holds images. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcharthscrolloffset.htm language=enus -->
## TOPIC 00539: ATTR_CHART_HSCROLL_OFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcharthscrolloffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcharthscrolloffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CHART_HSCROLL_OFFSET

| Type: | Control attribute |
| --- | --- |
| Description: | The amount (in points) by which the scroll bar of a paused strip chart is scrolled to the left. A value of 0 means that the most recently plotted points are visible. This value cannot exceed the chart's history buffer size minus the points per screen or the number of points plotted to the chart minus the points per screen. |
| Control Types: | Strip charts. |
| Data Type: | integer |
| Valid Range: | 0-1000000 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2010 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcheckrange_control.htm language=enus -->
## TOPIC 00540: ATTR_CHECK_RANGE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcheckrange_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcheckrange_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CHECK_RANGE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The type of range checking for the control. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. |
| Control Types: | Numerics, numeric slides, tables. |
| Data Type: | integer |
| Default Value: | VAL_NOTIFY |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_COERCE | The value is coerced to the upper or lower range boundary, whichever is closer. When a value is coerced, an EVENT_VAL_COERCED event occurs. |
| --- | --- |
| VAL_IGNORE | The value remains unchanged. |
| VAL_NOTIFY | Whenever the control is active, the operator is notified with an Out of Range box. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcheckrange_row.htm language=enus -->
## TOPIC 00541: ATTR_CHECK_RANGE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcheckrange_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcheckrange_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CHECK_RANGE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The type of range checking for the table cell. |
| Data Type: | integer |
| Default Value: | VAL_NOTIFY |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_COERCE | The value is coerced to the upper or lower range boundary, whichever is closer. When a value is coerced, an EVENT_VAL_COERCED event occurs. |
| --- | --- |
| VAL_IGNORE | The value remains unchanged. |
| VAL_NOTIFY | Whenever the control is active, the operator is notified with an Out of Range box. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcmdbuttoncolor_row.htm language=enus -->
## TOPIC 00542: ATTR_CMD_BUTTON_COLOR (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcmdbuttoncolor_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcmdbuttoncolor_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CMD_BUTTON_COLOR (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The RGB color value of a button cell. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcollapsed.htm language=enus -->
## TOPIC 00543: ATTR_COLLAPSED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcollapsed.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcollapsed.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLLAPSED

| Type: | Tree Item attribute |
| --- | --- |
| Description: | Specifies whether a tree item has children that are not exposed. 0 = Tree item has no children or has exposed children 1 = Tree item has unexposed children |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcollapsedimageindex_control.htm language=enus -->
## TOPIC 00544: ATTR_COLLAPSED_IMAGE_INDEX (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcollapsedimageindex_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcollapsedimageindex_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLLAPSED_IMAGE_INDEX (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The index into the tree image list that specifies which image to use to indicate a collapsed item. A collapsed item is one that has children that aren't exposed. If the attribute is set to -1, then the tree will use the default image (a box containing a plus sign). |
| Control Types: | Trees. |
| Data Type: | integer |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcollapsedimageindex_tree item.htm language=enus -->
## TOPIC 00545: ATTR_COLLAPSED_IMAGE_INDEX (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcollapsedimageindex_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcollapsedimageindex_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLLAPSED_IMAGE_INDEX (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The index into the tree image list that specifies which image to display with a collapsed item. This image will be used when the tree item has unexposed children. If the attribute is set to -1, then no image is displayed with the item. |
| Data Type: | integer |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcolordepth.htm language=enus -->
## TOPIC 00546: ATTR_COLOR_DEPTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcolordepth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcolordepth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLOR_DEPTH

| Type: | Monitor attribute |
| --- | --- |
| Description: | The number of bits in the number of possible colors. For example, if the monitor has 256 possible colors the color depth would be 8. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcolormode.htm language=enus -->
## TOPIC 00547: ATTR_COLOR_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcolormode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcolormode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLOR_MODE

| Type: | Print attribute |
| --- | --- |
| Description: | This attribute determines the color mode of the hardcopy image. The behavior of this attribute varies based on whether you are using a color printer. The following describes the various behaviors. With color printer: VAL_COLOR prints in color VAL_GRAYSCALE prints in grayscale VAL_BW undefined With non-color printer: VAL_COLOR prints in grayscale VAL_GRAYSCALE prints in grayscale VAL_BW prints in black and white |
| Types of Printing: | Graphics. |
| Data Type: | integer |
| Default Value: | VAL_COLOR |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_BW | Set output to print in black & white. |
| --- | --- |
| VAL_GRAYSCALE | Set output to print in grayscale. |
| VAL_COLOR | Set output to print in color. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcolumnlabelscolor.htm language=enus -->
## TOPIC 00548: ATTR_COLUMN_LABELS_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcolumnlabelscolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcolumnlabelscolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLUMN_LABELS_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the row of column labels. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Tables, trees. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcolumnlabelsheight.htm language=enus -->
## TOPIC 00549: ATTR_COLUMN_LABELS_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcolumnlabelsheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcolumnlabelsheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLUMN_LABELS_HEIGHT

| Type: | Control attribute |
| --- | --- |
| Description: | The height in pixels of the row of column labels. |
| Control Types: | Tables, trees. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 25 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcolumnlabelsvisible.htm language=enus -->
## TOPIC 00550: ATTR_COLUMN_LABELS_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcolumnlabelsvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcolumnlabelsvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLUMN_LABELS_VISIBLE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the row of column labels. 0 = Hide column labels 1 = Show column labels |
| Control Types: | Tables, trees. |
| Data Type: | integer |
| Default Value: | 1 (tables), 0 (trees) |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcolumnoffset.htm language=enus -->
## TOPIC 00551: ATTR_COLUMN_OFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcolumnoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcolumnoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLUMN_OFFSET

| Type: | Control attribute |
| --- | --- |
| Description: | A constant offset to add to the column indices. |
| Control Types: | Tables. |
| Data Type: | integer |
| Valid Range: | -2147483648 to 1000000000 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcolumnvisible_tree column.htm language=enus -->
## TOPIC 00552: ATTR_COLUMN_VISIBLE (Tree Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcolumnvisible_tree column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcolumnvisible_tree%20column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_COLUMN_VISIBLE (Tree Column)

| Type: | Tree Column attribute |
| --- | --- |
| Description: | Determines whether the tree column is visible. You cannot make column zero invisible. 0 = Not visible 1 = Visible |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrconstantname_menu.htm language=enus -->
## TOPIC 00553: ATTR_CONSTANT_NAME (Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrconstantname_menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrconstantname_menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CONSTANT_NAME (Menu)

| Type: | Menu attribute |
| --- | --- |
| Description: | The constant name assigned to the menu bar, menu, or menu item in the User Interface Editor. To determine the size of the buffer to pass when you are obtaining the constant name, call GetMenuBarAttribute and specify the ATTR_CONSTANT_NAME_LENGTH attribute. |
| Menu Objects: | Menu Bars, menus, submenus, menu Items. |
| Restrictions: | Not settable. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrconstantnamelength_control.htm language=enus -->
## TOPIC 00554: ATTR_CONSTANT_NAME_LENGTH (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrconstantnamelength_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrconstantnamelength_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CONSTANT_NAME_LENGTH (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the constant name of the control. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_CONSTANT_NAME attribute. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strings, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrctrlindex.htm language=enus -->
## TOPIC 00555: ATTR_CTRL_INDEX

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrctrlindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrctrlindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CTRL_INDEX

| Type: | Control attribute |
| --- | --- |
| Description: | The index of the currently selected label/value pair or tab page in the control. The index is a zero-based value that represents the position of the label/value pair or tab page in the control. If the control is a tab control, this attribute sets the currently selected tab page without giving the keyboard focus to the tab page. SetActiveTabPage sets the selected tab page and gives it the keyboard focus. |
| Control Types: | Binary switches, list boxes, picture rings, rings, ring slides, tab controls, trees. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrctrlmode.htm language=enus -->
## TOPIC 00556: ATTR_CTRL_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrctrlmode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrctrlmode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CTRL_MODE

| Type: | Control attribute |
| --- | --- |
| Description: | The mode of the control. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, radio buttons, rings, numeric slides, ring slides, splitters, strings, tab controls, tables, text boxes, text buttons, toggle buttons, trees. |
| Restrictions: | Not settable for digital graphs controls or controls of type CTRL_ACTIVEX. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_INDICATOR | The control can be changed programmatically, but operator action cannot generate commit or value changed events. Some controls are always indicators. |
| --- | --- |
| VAL_HOT | The control can be operated by the user or changed programmatically. User action can generate commit or value changed events. For example, if the user moves a binary switch from off to on, a value changed event and a commit event are generated. |
| VAL_NORMAL | The control can be operated by the user or changed programmatically. User action can generate value changed events but not commit events. |
| VAL_VALIDATE | Similar to a VAL_HOT, except that before a commit event is generated, LabWindows/CVI validates all numeric controls on the panel that have the range-checking attribute set to Notify. Invalid conditions cause a notification box to appear. No commit event is generated until the user enters valid values. Note: This value is not valid for graph controls. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrctrlval_cell.htm language=enus -->
## TOPIC 00557: ATTR_CTRL_VAL (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrctrlval_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrctrlval_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CTRL_VAL (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The current value of a cell. Using this in GetTableCellAttribute is equivalent to calling the GetTableCellVal function. Using this in SetTableCellAttribute or SetTableCellRangeAttribute is equivalent to calling the SetTableCellVal or SetTableCellRangeVals functions, except that the cell does not display the value until LabWindows/CVI processes draw events. Note: If the table control in which you are setting a cell value is the active control in the panel, the cell nevertheless displays the value immediately. |
| Data Type: | variable |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrctrlval_control.htm language=enus -->
## TOPIC 00558: ATTR_CTRL_VAL (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrctrlval_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrctrlval_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CTRL_VAL (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The current value of a control. Using this in GetCtrlAttribute is equivalent to calling the GetCtrlVal function. Using this in SetCtrlAttribute is equivalent to calling the SetCtrlVal function, except that the control does not display the value until LabWindows/CVI processes draw events. Note: If the control in which you are setting the value is the active control in the panel, the control nevertheless displays the value immediately. For a list box, ring, or tree, using this in SetCtrlAttribute sets the current item to the first item with the value. (To set the current list item via zero-based index, use the SetCtrlIndex function instead.) For a text box, setting the value appends the value to the contents of the text box. |
| Control Types: | Binary switches, color numerics, command buttons, LEDs, list boxes, numerics, picture buttons, picture rings, radio buttons, rings, numeric slides, ring slides, strings, text boxes, text buttons, text messages, toggle buttons, trees. |
| Data Type: | variable |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcursorcolor.htm language=enus -->
## TOPIC 00559: ATTR_CURSOR_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcursorcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcursorcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CURSOR_COLOR

| Type: | Cursor attribute |
| --- | --- |
| Description: | The RGB color value of the graph cursor. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrcursormode.htm language=enus -->
## TOPIC 00560: ATTR_CURSOR_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrcursormode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrcursormode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_CURSOR_MODE

| Type: | Cursor attribute |
| --- | --- |
| Description: | Specifies the behavior of a graph cursor. Free-form cursors move to any location inside the plot area. Snap-to-point cursors snap to the nearest point when released. |
| Data Type: | integer |
| Default Value: | VAL_FREE_FORM |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_FREE_FORM | Graph cursors can be placed anywhere inside the plot area. |
| --- | --- |
| VAL_SNAP_TO_POINT | Graph cursors snap to the nearest plotted point when released. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdatasocketmode.htm language=enus -->
## TOPIC 00561: ATTR_DATASOCKET_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdatasocketmode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdatasocketmode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DATASOCKET_MODE

| Type: | Control attribute |
| --- | --- |
| Description: | The control's current bound mode, either VAL_DS_READ or VAL_DS_WRITE. Linux: DataSocket is not supported. |
| Control Types: | Graphs, numerics, numeric slides, strings, strip charts, tables, text boxes. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdatasocketsource.htm language=enus -->
## TOPIC 00562: ATTR_DATASOCKET_SOURCE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdatasocketsource.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdatasocketsource.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DATASOCKET_SOURCE

| Type: | Control attribute |
| --- | --- |
| Description: | The URL that the control is currently bound to. Linux: DataSocket is not supported. To determine the size of the buffer to pass when you are obtaining the DataSocket source, call GetCtrlAttribute and specify the ATTR_DATASOCKET_SOURCE_LENGTH attribute. |
| Control Types: | Graphs, numerics, numeric slides, strings, strip charts, tables, text boxes. |
| Restrictions: | Not settable. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdigdisptop.htm language=enus -->
## TOPIC 00563: ATTR_DIG_DISP_TOP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdigdisptop.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdigdisptop.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DIG_DISP_TOP

| Type: | Control attribute |
| --- | --- |
| Description: | The vertical offset in pixels of the digital display relative to the origin of the panel. The panel origin (0,0) is the upper-left corner of the panel below the title bar and to the right of the panel frame. |
| Control Types: | Numeric slides. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767, or VAL_AUTO_CENTER |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_AUTO_CENTER | Center the digital display with respect to the control. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdigdispwidth.htm language=enus -->
## TOPIC 00564: ATTR_DIG_DISP_WIDTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdigdispwidth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdigdispwidth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DIG_DISP_WIDTH

| Type: | Control attribute |
| --- | --- |
| Description: | Width of the digital display in pixels. |
| Control Types: | Numeric slides. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 75 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdigwaveformautosize.htm language=enus -->
## TOPIC 00565: ATTR_DIGWAVEFORM_AUTOSIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdigwaveformautosize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdigwaveformautosize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DIGWAVEFORM_AUTOSIZE

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether LabWindows/CVI autosizes digital waveform plots based on the height of the graph's plot area. Digital graph plots must be the minimum plot size or larger. The height of the state label font determines the minimum plot size. If the plot area is not large enough to show all the digital lines, LabWindows/CVI does not display lines that would be below the plot area. |
| Control Types: | Digital graphs. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdigwaveformbuslabellength.htm language=enus -->
## TOPIC 00566: ATTR_DIGWAVEFORM_BUS_LABEL_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdigwaveformbuslabellength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdigwaveformbuslabellength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DIGWAVEFORM_BUS_LABEL_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the bus label string for digital graph plots. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_DIGWAVEFORM_BUS_LABEL attribute. |
| Control Types: | Digital graphs. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdigwaveformexpandbuses.htm language=enus -->
## TOPIC 00567: ATTR_DIGWAVEFORM_EXPAND_BUSES

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdigwaveformexpandbuses.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdigwaveformexpandbuses.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DIGWAVEFORM_EXPAND_BUSES

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether digital buses are divided into individual line plots (expanded) or combined into one plot per bus (collapsed). If the buses are collapsed, the state labels display the hexadecimal value of the bus instead of the individual high or low values for each line. |
| Control Types: | Digital graphs. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdigwaveformfont.htm language=enus -->
## TOPIC 00568: ATTR_DIGWAVEFORM_FONT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdigwaveformfont.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdigwaveformfont.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DIGWAVEFORM_FONT

| Type: | Control attribute |
| --- | --- |
| Description: | The name of the metafont used in digital graph state labels. To determine the size of the buffer to pass when you are obtaining the font name, call GetCtrlAttribute and specify the ATTR_DIGWAVEFORM_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. If you set ATTR_DIGWAVEFORM_AUTOSIZE to TRUE, then the height of the metafont determines the height of the plots. |
| Control Types: | Digital graphs. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

##### Values

| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| --- | --- |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdimmed_control menu.htm language=enus -->
## TOPIC 00569: ATTR_DIMMED (Control Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdimmed_control menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdimmed_control%20menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DIMMED (Control Menu)

| Type: | Control Menu attribute |
| --- | --- |
| Description: | Specifies whether the menu item is dimmed. 0 = Not dimmed 1 = Dimmed |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdisablepaneltheme.htm language=enus -->
## TOPIC 00570: ATTR_DISABLE_PANEL_THEME

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdisablepaneltheme.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdisablepaneltheme.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DISABLE_PANEL_THEME

| Type: | Control attribute |
| --- | --- |
| Description: | Overrides theme drawing for an individual control if you have specified that controls draw based on the Theme setting on Windows or if you have enabled the ATTR_CONFORM_TO_SYSTEM_THEME panel or systems popup attribute. 0 = Do not disable theme drawing 1 = Disable theme drawing |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strings, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.1 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdisableprogpanelsizeevents.htm language=enus -->
## TOPIC 00571: ATTR_DISABLE_PROG_PANEL_SIZE_EVENTS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdisableprogpanelsizeevents.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdisableprogpanelsizeevents.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DISABLE_PROG_PANEL_SIZE_EVENTS

| Type: | System attribute |
| --- | --- |
| Description: | Specifies whether a change in panel size or position that occurs as a result of a call to a User Interface Library function should generate an EVENT_PANEL_SIZE or EVENT_PANEL_MOVE. 0 = Enable programmatic panel size events. 1 = Disable programmatic panel size events. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrdrawlightbevel.htm language=enus -->
## TOPIC 00572: ATTR_DRAW_LIGHT_BEVEL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrdrawlightbevel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrdrawlightbevel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DRAW_LIGHT_BEVEL

| Type: | Menu attribute |
| --- | --- |
| Description: | Indicates whether the menubar draws with a light bevel or a dark bevel at the bottom. 0 = Draw dark bevel 1 = Draw light bevel |
| Menu Objects: | Menu Bars. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrduplex.htm language=enus -->
## TOPIC 00573: ATTR_DUPLEX

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrduplex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrduplex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_DUPLEX

| Type: | Print attribute |
| --- | --- |
| Description: | This attribute specifies whether the output is single or double-sided. If you specify VAL_USE_PRINTER_SETTING, the next call to a User Interface Library printing function uses the system's current setting for the selected printer. After the printing function returns, the value of the attribute is no longer VAL_USE_PRINTER_SETTING. Instead, the library stores the system's setting as the attribute value. If you want to update the attribute value based on the current system setting each time you print, set the attribute to VAL_USE_PRINTER_SETTING before each call to a printing function. |
| Types of Printing: | Text and graphics. |
| Data Type: | integer |
| Default Value: | VAL_SIMPLEX |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_SIMPLEX | Set output to print in simplex (single sided). |
| --- | --- |
| VAL_VERTDUPLEX | Set output to print in vertical duplex (double sided with the top side of each page on the opposite edges). |
| VAL_HORIZDUPLEX | Set output to print in horizontal duplex (double sided with the top side of each page on the same edge). |
| VAL_USE_PRINTER_SETTING | Windows platforms only). Use the system's current setting for the selected printer. The next printing operation uses the current system setting and stores it as the attribute value. If you want to update the attribute from the current system setting each time you print, set the attribute to VAL_USE_PRINTER_SETTING before each call to a printing function. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattredgestyle.htm language=enus -->
## TOPIC 00574: ATTR_EDGE_STYLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattredgestyle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattredgestyle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_EDGE_STYLE

| Type: | Control attribute |
| --- | --- |
| Description: | The graph border style. VAL_RECESSED_EDGE is not valid for Lab Style graphs, strip charts, or digital graphs. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | VAL_RAISED_EDGE |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RAISED_EDGE | Highlight control to give a raised appearance. |
| --- | --- |
| VAL_FLAT_EDGE | Do not highlight control, thereby giving a flat or flush appearance. |
| VAL_RECESSED_EDGE | Highlight control to give a recessed appearance. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrejectafter.htm language=enus -->
## TOPIC 00575: ATTR_EJECT_AFTER

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrejectafter.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrejectafter.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_EJECT_AFTER

| Type: | Print attribute |
| --- | --- |
| Description: | Specifies whether to eject the paper from the printer after the next call to a printing function. If ATTR_EJECT_AFTER is set to zero, outputs are printed on the same page until ATTR_EJECT_AFTER is set to one. 0 = Do not eject after 1 = Eject after |
| Types of Printing: | Text and graphics. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenableantialiasing.htm language=enus -->
## TOPIC 00576: ATTR_ENABLE_ANTI_ALIASING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenableantialiasing.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenableantialiasing.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENABLE_ANTI_ALIASING

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether the control uses anti-aliasing. Anti-aliased drawings look smoother, but the drawing speed is significantly slower. Note: If you enable anti-aliasing for a canvas control, thick lines are not rounded. This caveat, along with the slower drawing speed, might affect the manner in which you draw complex shapes. LabWindows/CVI ignores this attribute for text you add using the PlotText, CanvasDrawText, and CanvasDrawTextAtPoint functions. To enable anti-aliasing for transparent canvas controls, you must set the ATTR_DRAW_POLICY attribute to VAL_DIRECT_TO_SCREEN. National Instruments recommends that you use anti-aliasing only for post-processed data. |
| Control Types: | Canvases, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2012 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenabledragdrop.htm language=enus -->
## TOPIC 00577: ATTR_ENABLE_DRAG_DROP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenabledragdrop.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenabledragdrop.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENABLE_DRAG_DROP

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether you can interactively drag and drop tree items or tab pages to change their position in the tree or tab control. 0 = Disable drag and drop 1 = Enable drag and drop |
| Control Types: | Tab controls, trees. |
| Data Type: | integer |
| Default Value: | 1 (tree), 0 (tab) |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenabledrop.htm language=enus -->
## TOPIC 00578: ATTR_ENABLE_DROP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenabledrop.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenabledrop.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENABLE_DROP

| Type: | Tree Item attribute |
| --- | --- |
| Description: | Determines whether you can interactively drop an item from a different part of the tree as a child of the item. 0 = Prevent dropping into item 1 = Allow dropping into item |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenableeditableaxes.htm language=enus -->
## TOPIC 00579: ATTR_ENABLE_EDITABLE_AXES

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenableeditableaxes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenableeditableaxes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENABLE_EDITABLE_AXES

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether graph axes can be interactively edited when the user clicks either the axis minimum or maximum. For axes to be editable, the control mode for the graph must be VAL_HOT or VAL_NORMAL and the axis mode must be VAL_MANUAL or VAL_LOCK. If you enable the ATTR_XUSE_LABEL_STRINGS or ATTR_YUSE_LABEL_STRINGS attribute, you cannot use editable axis labels. If you set ATTR_XFORMAT or ATTR_YFORMAT to VAL_RELATIVE_TIME_FORMAT or VAL_ABSOLUTE_TIME_FORMAT, you also cannot use editable axis labels. If the user modifies a label value so that the minimum value becomes greater than or equal to the maximum value (or so that the maximum value becomes less than or equal to the minimum value), LabWindows/CVI pans the axis range. For example, if a graph has an x-axis range with 0 as the minimum and 10 as the maximum, and the user changes the minimum to 20, LabWindows/CVI displays the graph so that its x-axis ranges from 20 to 30. If the user enters an invalid number or string, LabWindows/CVI ignores the input and reverts the label to its original value. If the user modifies a label value so that the new minimum value becomes greater than the existing maximum value or the new maximum value becomes less than the existing minimum value, LabWindows/CVI pans the log scales by the difference in power between the original minimum and maximum values. For example, if the graph has an x-axis range with 1 as the minimum and 100 as the maximum, and the user changes the minimum to 1,000, the new maximum is the new value (1,000) times the original difference in power (100) for a result of 100,000. 0 = Prevent editing of graph axes 1 = Allow editing of graph axes |
| Control Types: | Graphs. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.1 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenablepopupmenu.htm language=enus -->
## TOPIC 00580: ATTR_ENABLE_POPUP_MENU

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenablepopupmenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenablepopupmenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENABLE_POPUP_MENU

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether right-clicking on the table displays the popup menu associated with the control. 0 = Popup menu disabled 1 = Popup menu enabled |
| Control Types: | Tables, trees. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenablerowsizing.htm language=enus -->
## TOPIC 00581: ATTR_ENABLE_ROW_SIZING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenablerowsizing.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenablerowsizing.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENABLE_ROW_SIZING

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether interactive sizing of rows is enabled for a table. If you enable row sizing, and ATTR_SIZE_MODE is set to VAL_USE_EXPLICIT_SIZE for a particular row, the user can resize that row interactively. 0 = Row sizing disabled 1 = Row sizing enabled |
| Control Types: | Tables. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenablezoomandpan.htm language=enus -->
## TOPIC 00582: ATTR_ENABLE_ZOOM_AND_PAN

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenablezoomandpan.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenablezoomandpan.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENABLE_ZOOM_AND_PAN

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether the end-user can interactively zoom and pan the graph viewport. This attribute has no effect on axes that use the log scale mapping mode. 0 = Disabled 1 = Enabled |
| Control Types: | Graphs. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenterisnewline_cell.htm language=enus -->
## TOPIC 00583: ATTR_ENTER_IS_NEWLINE (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenterisnewline_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenterisnewline_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENTER_IS_NEWLINE (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | Specifies whether the <Enter> key causes a newline. If not, the operator of the table cell must use <Ctrl-Enter> to create a new line. 0 = <Ctrl-Enter> causes newline 1 = <Enter> or <Ctrl-Enter> causes newline |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenterisnewline_control.htm language=enus -->
## TOPIC 00584: ATTR_ENTER_IS_NEWLINE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenterisnewline_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenterisnewline_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENTER_IS_NEWLINE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the <Enter> key causes a newline. If not, the operator of the control must use <Ctrl-Enter> to create a new line. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. 0 = <Ctrl-Enter> causes newline 1 = <Enter> or <Ctrl-Enter> causes newline |
| Control Types: | Tables, text boxes. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrenterisnewline_row.htm language=enus -->
## TOPIC 00585: ATTR_ENTER_IS_NEWLINE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrenterisnewline_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrenterisnewline_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ENTER_IS_NEWLINE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies whether the <Enter> key causes a newline. If not, the operator of the table cell must use <Ctrl-Enter> to create a new line. 0 = <Ctrl-Enter> causes newline 1 = <Enter> or <Ctrl-Enter> causes newline |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrextralines.htm language=enus -->
## TOPIC 00586: ATTR_EXTRA_LINES

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrextralines.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrextralines.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_EXTRA_LINES

| Type: | Control attribute |
| --- | --- |
| Description: | The maximum number of text box lines that can be retained off-screen. Use -1 to specify an unlimited number of lines. |
| Control Types: | Text boxes. |
| Data Type: | integer |
| Valid Range: | -1 or greater |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfastdrawbutton.htm language=enus -->
## TOPIC 00587: ATTR_FAST_DRAW_BUTTON

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfastdrawbutton.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfastdrawbutton.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FAST_DRAW_BUTTON

| Type: | Control attribute |
| --- | --- |
| Description: | Note This attribute is obsolete. This attribute allowed picture toggle buttons and picture command buttons to draw their images faster in return for certain limitations. It has been made obsolete, since all buttons are now drawn in this mode, and all limitations have been eliminated. 0 = Disable fast draw 1 = Enable fast draw |
|  | Note This attribute is obsolete. |
| Control Types: | Picture buttons. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfillcolor.htm language=enus -->
## TOPIC 00588: ATTR_FILL_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfillcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfillcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FILL_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value used to fill a control. For slide rings, the side that uses the fill color is specified by ATTR_FILL_OPTION. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Numeric slides, ring slides. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfirstchild.htm language=enus -->
## TOPIC 00589: ATTR_FIRST_CHILD

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfirstchild.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfirstchild.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIRST_CHILD

| Type: | Panel attribute |
| --- | --- |
| Description: | The panel handle of the first child panel in the panel you specify. Call GetPanelAttribute with ATTR_NEXT_PANEL on this first child panel handle to obtain the handle of the next sibling panel. On the last child panel, ATTR_NEXT_PANEL returns zero. Use the panel attribute ATTR_NUM_CHILDREN to get the total number of child panels in a panel. Note: If you pass zero for the parent panel, the first top-level panel is returned. You can then use ATTR_NEXT_PANEL to get the next sibling panel. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfirstitemid.htm language=enus -->
## TOPIC 00590: ATTR_FIRST_ITEM_ID

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfirstitemid.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfirstitemid.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIRST_ITEM_ID

| Type: | Menu attribute |
| --- | --- |
| Description: | The ID of the first menu item in the menu. The menu attribute ATTR_FIRST_ITEM_ID returns the ID of the first menu item in the menu. When you call GetMenuBarAttribute on the first menu item ID, ATTR_NEXT_ITEM_ID returns the ID of the next menu item in the menu. On the last menu item, ATTR_NEXT_ITEM_ID returns zero. Use the menu attribute ATTR_NUM_MENU_ITEMS to get the total number of menu items in a menu. |
| Menu Objects: | Menus, submenus. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfirstmenuid.htm language=enus -->
## TOPIC 00591: ATTR_FIRST_MENU_ID

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfirstmenuid.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfirstmenuid.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIRST_MENU_ID

| Type: | Menu attribute |
| --- | --- |
| Description: | The ID of the first menu in the menu bar. The menu bar attribute ATTR_FIRST_MENU_ID returns the ID of the first menu in the menu bar. When you call GetMenuBarAttribute on the first menu ID, ATTR_NEXT_MENU_ID returns the ID of the next menu in the menu bar. On the last menu, ATTR_NEXT_MENU_ID returns zero. Use the menu bar attribute ATTR_NUM_MENUS to get the total number of menus in a menu bar. |
| Menu Objects: | Menu Bars. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfirstmonitor.htm language=enus -->
## TOPIC 00592: ATTR_FIRST_MONITOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfirstmonitor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfirstmonitor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIRST_MONITOR

| Type: | System attribute |
| --- | --- |
| Description: | The ID of the first monitor to be used when iterating through all the monitors. Use the monitor attribute ATTR_NEXT_MONITOR to iterate through the monitors. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfirstplot.htm language=enus -->
## TOPIC 00593: ATTR_FIRST_PLOT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfirstplot.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfirstplot.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIRST_PLOT

| Type: | Control attribute |
| --- | --- |
| Description: | The ID of the first plot in the graph. This control attribute returns the ID of the first plot that exists in the graph. When you call GetPlotAttribute and pass it the first plot ID, ATTR_NEXT_PLOT returns the ID of the next plot on the graph. On the last plot, ATTR_NEXT_PLOT returns zero. Use the control attribute ATTR_NUM_PLOTS to get the total number of plots in a graph. |
| Control Types: | Graphs. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfirstvisiblecolumn.htm language=enus -->
## TOPIC 00594: ATTR_FIRST_VISIBLE_COLUMN

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfirstvisiblecolumn.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfirstvisiblecolumn.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIRST_VISIBLE_COLUMN

| Type: | Control attribute |
| --- | --- |
| Description: | The index of the first visible column. The index is one-based for a table, and zero-based for a tree. |
| Control Types: | Tables, trees. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfitmode_column.htm language=enus -->
## TOPIC 00595: ATTR_FIT_MODE (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfitmode_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfitmode_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIT_MODE (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies the placement and sizing of an image within a table cell. |
| Data Type: | integer |
| Default Value: | VAL_SIZE_TO_PICTURE |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_SIZE_TO_PICTURE | Make the picture conform to the size of the cell. |
| --- | --- |
| VAL_PICT_CORNER | Place the picture image at the top-left corner of the cell. |
| VAL_PICT_CENTER | Center the picture image in the cell. |
| VAL_PICT_TILE | Tile or repeat the image so that it fills up the cell. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfitmode_row.htm language=enus -->
## TOPIC 00596: ATTR_FIT_MODE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfitmode_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfitmode_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FIT_MODE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies the placement and sizing of an image within a table cell. |
| Data Type: | integer |
| Default Value: | VAL_SIZE_TO_PICTURE |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_SIZE_TO_PICTURE | Make the picture conform to the size of the cell. |
| --- | --- |
| VAL_PICT_CORNER | Place the picture image at the top-left corner of the cell. |
| VAL_PICT_CENTER | Center the picture image in the cell. |
| VAL_PICT_TILE | Tile or repeat the image so that it fills up the cell. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfloating.htm language=enus -->
## TOPIC 00597: ATTR_FLOATING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfloating.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfloating.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FLOATING

| Type: | Panel attribute |
| --- | --- |
| Description: | Specifies whether the panel's window floats above all non-floating windows. This attribute is not supported for child panels. Linux: This attribute is not supported. |
| Data Type: | integer |
| Default Value: | VAL_FLOAT_NEVER |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| VAL_FLOAT_NEVER | Panel's window never floats relative to other top level windows. |
| --- | --- |
| VAL_FLOAT_APP_ACTIVE | Panel's window only floats when the application is active. |
| VAL_FLOAT_ALWAYS | Panel's window always floats relative to other top level windows. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrforcesmoothdragging.htm language=enus -->
## TOPIC 00598: ATTR_FORCE_SMOOTH_DRAGGING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrforcesmoothdragging.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrforcesmoothdragging.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FORCE_SMOOTH_DRAGGING

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether the control jumps from the maximum value to the minimum value and the converse, and whether the user only can drag the control in a circular motion. 0 = Jumps from max to min values and does not enforce circular motion only 1 = Cannot jump from max to min values and control drags in circular motion only |
| Control Types: | Numeric slides. |
| Restrictions: | Valid only for controls of type CTRL_NUMERIC_KNOB, CTRL_NUMERIC_KNOB_LS, CTRL_NUMERIC_DIAL, CTRL_NUMERIC_DIAL_LS, CTRL_NUMERIC_GAUGE, CTRL_NUMERIC_GAUGE_LS, CTRL_NUMERIC_METER, CTRL_NUMERIC_METER_LS. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrformat_cell.htm language=enus -->
## TOPIC 00599: ATTR_FORMAT (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrformat_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrformat_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FORMAT (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The display format of the table cell. |
| Data Type: | integer |
| Default Value: | VAL_FLOATING_PT_FORMAT |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_FLOATING_PT_FORMAT | Example: 123.000 |
| --- | --- |
| VAL_SCIENTIFIC_FORMAT | Example: 1.23E+2 |
| VAL_ENGINEERING_FORMAT | Example: 123.00E+0 |
| VAL_DECIMAL_FORMAT | Example: 123 |
| VAL_HEX_FORMAT | Example: 7B |
| VAL_OCTAL_FORMAT | Example: 173 |
| VAL_BINARY_FORMAT | Example: 1111011 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrformat_column.htm language=enus -->
## TOPIC 00600: ATTR_FORMAT (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrformat_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrformat_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FORMAT (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The display format of the table cell. |
| Data Type: | integer |
| Default Value: | VAL_FLOATING_PT_FORMAT |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_FLOATING_PT_FORMAT | Example: 123.000 |
| --- | --- |
| VAL_SCIENTIFIC_FORMAT | Example: 1.23E+2 |
| VAL_ENGINEERING_FORMAT | Example: 123.00E+0 |
| VAL_DECIMAL_FORMAT | Example: 123 |
| VAL_HEX_FORMAT | Example: 7B |
| VAL_OCTAL_FORMAT | Example: 173 |
| VAL_BINARY_FORMAT | Example: 1111011 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrformat_control.htm language=enus -->
## TOPIC 00601: ATTR_FORMAT (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrformat_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrformat_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FORMAT (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The display format of the numeric control. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. |
| Control Types: | Numerics, numeric slides, tables. |
| Data Type: | integer |
| Default Value: | VAL_FLOATING_PT_FORMAT |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_FLOATING_PT_FORMAT | Example: 123.000 |
| --- | --- |
| VAL_SCIENTIFIC_FORMAT | Example: 1.23E+2 |
| VAL_ENGINEERING_FORMAT | Example: 123.00E+0 |
| VAL_DECIMAL_FORMAT | Example: 123 |
| VAL_HEX_FORMAT | Example: 7B |
| VAL_OCTAL_FORMAT | Example: 173 |
| VAL_BINARY_FORMAT | Example: 1111011 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrformat_row.htm language=enus -->
## TOPIC 00602: ATTR_FORMAT (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrformat_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrformat_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FORMAT (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The display format of the table cell. |
| Data Type: | integer |
| Default Value: | VAL_FLOATING_PT_FORMAT |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_FLOATING_PT_FORMAT | Example: 123.000 |
| --- | --- |
| VAL_SCIENTIFIC_FORMAT | Example: 1.23E+2 |
| VAL_ENGINEERING_FORMAT | Example: 123.00E+0 |
| VAL_DECIMAL_FORMAT | Example: 123 |
| VAL_HEX_FORMAT | Example: 7B |
| VAL_OCTAL_FORMAT | Example: 173 |
| VAL_BINARY_FORMAT | Example: 1111011 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframeactualheight.htm language=enus -->
## TOPIC 00603: ATTR_FRAME_ACTUAL_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframeactualheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframeactualheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_ACTUAL_HEIGHT

| Type: | Panel attribute |
| --- | --- |
| Description: | Returns the actual height of the panel frame, regardless of whether the panel is a child panel or top level panel. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframeactualwidth.htm language=enus -->
## TOPIC 00604: ATTR_FRAME_ACTUAL_WIDTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframeactualwidth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframeactualwidth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_ACTUAL_WIDTH

| Type: | Panel attribute |
| --- | --- |
| Description: | Returns the actual width of the panel frame, regardless of whether the panel is a child panel or top level panel. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframecolor_control.htm language=enus -->
## TOPIC 00605: ATTR_FRAME_COLOR (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframecolor_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframecolor_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_COLOR (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value for a control frame. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | ActiveX controls, color numerics, decorations, list boxes, numerics, picture rings, pictures, rings, numeric slides, ring slides, splitters, strings, tables, text boxes, trees. |
| Restrictions: | Not valid for controls of type CTRL_RING_KNOB, CTRL_RING_KNOB_LS, CTRL_RING_DIAL, CTRL_RING_DIAL_LS, CTRL_RING_POINTER_VSLIDE, CTRL_RING_POINTER_VSLIDE_LS, CTRL_RING_TANK, CTRL_RING_TANK_LS, CTRL_RING_THERMOMETER, CTRL_RING_THERMOMETER_LS, CTRL_RING_POINTER_HSLIDE, CTRL_RING_POINTER_HSLIDE_LS, CTRL_RING_LEVEL_VSLIDE, CTRL_RING_LEVEL_VSLIDE_LS, CTRL_RING_LEVEL_HSLIDE, CTRL_RING_LEVEL_HSLIDE_LS, CTRL_RING_VSLIDE, CTRL_RING_HSLIDE, CTRL_RING_FLAT_VSLIDE, or CTRL_RING_FLAT_HSLIDE. Setting the frame color on controls with a transparent frame (CTRL_STRING_LS, CTRL_TEXT_BOX_LS, CTRL_TABLE_LS, CTRL_TREE_LS, CTRL_LIST_LS, CTRL_RING_GAUGE_LS, CTRL_COLOR_NUMERIC_LS) will have no visible effect. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframecolor_panel.htm language=enus -->
## TOPIC 00606: ATTR_FRAME_COLOR (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframecolor_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframecolor_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_COLOR (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The RGB color value of the panel frame. This is for child panels only. Top-level panel frame colors are controlled by the operating system. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframestyle.htm language=enus -->
## TOPIC 00607: ATTR_FRAME_STYLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframestyle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframestyle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_STYLE

| Type: | Panel attribute |
| --- | --- |
| Description: | The style of frame for the panel. |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| Default Value: | VAL_RAISED_OUTLINED_FRAME |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_OUTLINED_FRAME | Single black line for panel frame. |
| --- | --- |
| VAL_BEVELLED_FRAME | Slanted or angled look for panel frame. |
| VAL_RAISED_FRAME | Raised look for the panel frame. |
| VAL_HIDDEN_FRAME | No frame for the panel. |
| VAL_STEP_FRAME | Single colorable line of variable width around panel frame. |
| VAL_RAISED_OUTLINED_FRAME | Raised colorable line of variable width around panel frame. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframethickness_control.htm language=enus -->
## TOPIC 00608: ATTR_FRAME_THICKNESS (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframethickness_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframethickness_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_THICKNESS (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The frame thickness for the control. |
| Control Types: | Color numerics, list boxes, numerics, pictures, rings, splitters, strings, text boxes, trees. |
| Restrictions: | This attribute is gettable and settable for splitter controls. It is gettable, but not settable, for controls of type CTRL_NUMERIC, CTRL_STRING, CTRL_TEXTBOX, CTRL_RING, CTRL_RECESSED_MENU_RING, CTRL_LISTBOX, CTRL_TREE, CTRL_PICTURE, and their equivalent Lab Style controls. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframethickness_panel.htm language=enus -->
## TOPIC 00609: ATTR_FRAME_THICKNESS (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframethickness_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframethickness_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_THICKNESS (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The frame thickness for the panel. Always set ATTR_FRAME_STYLE before setting the thickness. |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| Valid Range: | 1 to 10 |
| Default Value: | 5 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrframevisible.htm language=enus -->
## TOPIC 00610: ATTR_FRAME_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrframevisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrframevisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FRAME_VISIBLE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide a control frame. 0 = Hide frame 1 = Show frame |
| Control Types: | ActiveX controls, picture rings, pictures, tab controls, tables, trees. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrfullrowselect.htm language=enus -->
## TOPIC 00611: ATTR_FULL_ROW_SELECT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrfullrowselect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrfullrowselect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_FULL_ROW_SELECT

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether the entire row of a selected item is highlighted. 0 = Disable full row select 1 = Enable full row select |
| Control Types: | Trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrgraphbgcolor.htm language=enus -->
## TOPIC 00612: ATTR_GRAPH_BGCOLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrgraphbgcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrgraphbgcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_GRAPH_BGCOLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the graph or chart background. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrgridareaheight.htm language=enus -->
## TOPIC 00613: ATTR_GRID_AREA_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrgridareaheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrgridareaheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_GRID_AREA_HEIGHT

| Type: | Control attribute |
| --- | --- |
| Description: | The height of the cell grid area in pixels |
| Control Types: | Tables. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrgridarealeft.htm language=enus -->
## TOPIC 00614: ATTR_GRID_AREA_LEFT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrgridarealeft.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrgridarealeft.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_GRID_AREA_LEFT

| Type: | Control attribute |
| --- | --- |
| Description: | The offset in pixels of the left edge of the cell grid area from the left edge of the control. |
| Control Types: | Tables. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrgridareatop.htm language=enus -->
## TOPIC 00615: ATTR_GRID_AREA_TOP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrgridareatop.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrgridareatop.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_GRID_AREA_TOP

| Type: | Control attribute |
| --- | --- |
| Description: | The offset in pixels of the top of the cell grid area from the top of the control. |
| Control Types: | Tables. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrgridareawidth.htm language=enus -->
## TOPIC 00616: ATTR_GRID_AREA_WIDTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrgridareawidth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrgridareawidth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_GRID_AREA_WIDTH

| Type: | Control attribute |
| --- | --- |
| Description: | The width of the cell grid area in pixels. |
| Control Types: | Tables. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrgridcolor.htm language=enus -->
## TOPIC 00617: ATTR_GRID_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrgridcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrgridcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_GRID_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the graph or strip chart grid. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | VAL_BLACK (CTRL_GRAPH), VAL_LT_GRAY (CTRL_GRAPH_LS) |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrgridstyle.htm language=enus -->
## TOPIC 00618: ATTR_GRID_STYLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrgridstyle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrgridstyle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_GRID_STYLE

| Type: | Control attribute |
| --- | --- |
| Description: | The line style of the graph or strip chart grid. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | VAL_SOLID |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

##### Values

| VAL_DASH_DOT | A line with alternating dashes and dots. |
| --- | --- |
| VAL_SOLID | A solid line. |
| VAL_DASH | A dashed line. |
| VAL_DOT | A dotted line. |
| VAL_DASH_DOT_DOT | A line alternating between one dash and two dots. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhastaskbarbutton.htm language=enus -->
## TOPIC 00619: ATTR_HAS_TASKBAR_BUTTON

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhastaskbarbutton.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhastaskbarbutton.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HAS_TASKBAR_BUTTON

| Type: | Panel attribute |
| --- | --- |
| Description: | This attribute specifies whether the panel has its own button on the taskbar. The button text is always the panel title. This attribute is not supported for child panels. Note: Changing this attribute recreates the window and causes the ATTR_SYSTEM_WINDOW_HANDLE to be invalid. Linux: This attribute is not supported. 0 = No separate taskbar button for panel. 1 = Panel has its own taskbar button. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrheight_control.htm language=enus -->
## TOPIC 00620: ATTR_HEIGHT (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrheight_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrheight_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HEIGHT (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The height of the control body in pixels. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Restrictions: | Not valid for controls of type CTRL_RING, CTRL_RECESSED_MENU_RING, CTRL_MENU_RING, CTRL_HORIZONTAL_SPLITTER, and their equivalent Lab Style controls. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrheight_monitor.htm language=enus -->
## TOPIC 00621: ATTR_HEIGHT (Monitor)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrheight_monitor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrheight_monitor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HEIGHT (Monitor)

| Type: | Monitor attribute |
| --- | --- |
| Description: | The height of the work area of the monitor (in pixels). The work area is the portion of the screen not obscured by the taskbar. For DPI unaware applications the work area is influenced by the DPI scalling factor. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrheight_panel.htm language=enus -->
## TOPIC 00622: ATTR_HEIGHT (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrheight_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrheight_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HEIGHT (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The height of the panel in pixels. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhideactiveitem.htm language=enus -->
## TOPIC 00623: ATTR_HIDE_ACTIVE_ITEM

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhideactiveitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhideactiveitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HIDE_ACTIVE_ITEM

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether a dotted outline around the active item is drawn when the tree does not have the focus. 0 = Disable hiding active item 1 = Enable hiding active item |
| Control Types: | Trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhideactiveitemalways.htm language=enus -->
## TOPIC 00624: ATTR_HIDE_ACTIVE_ITEM_ALWAYS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhideactiveitemalways.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhideactiveitemalways.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HIDE_ACTIVE_ITEM_ALWAYS

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether a dotted outline around the active item is drawn. 0 = Disable hiding active item 1 = Enable hiding active item |
| Control Types: | Trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.1 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhidehilite.htm language=enus -->
## TOPIC 00625: ATTR_HIDE_HILITE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhidehilite.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhidehilite.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HIDE_HILITE

| Type: | Control attribute |
| --- | --- |
| Description: | When enabled, prevents the control from highlighting its active or selected items. When disabled, the active or selected items are highlighted. |
| Control Types: | Tables, trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.1 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhilitecurrentitem.htm language=enus -->
## TOPIC 00626: ATTR_HILITE_CURRENT_ITEM

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhilitecurrentitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhilitecurrentitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HILITE_CURRENT_ITEM

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to highlight the currently selected item in a list box. The highlight is shown in reversed colors when the list box is active and as a dashed box when the list box is inactive. 0 = Do not highlight any item 1 = Highlight the current item |
| Control Types: | List boxes. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhiliteonlywhenpanelactive.htm language=enus -->
## TOPIC 00627: ATTR_HILITE_ONLY_WHEN_PANEL_ACTIVE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhiliteonlywhenpanelactive.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhiliteonlywhenpanelactive.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HILITE_ONLY_WHEN_PANEL_ACTIVE

| Type: | Control attribute |
| --- | --- |
| Description: | When enabled, prevents the control from highlighting its active or selected items when the panel itself is not active. When disabled, the active or selected items are highlighted as long as the control is active. |
| Control Types: | List boxes, tables, trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhistorybuffersize.htm language=enus -->
## TOPIC 00628: ATTR_HISTORY_BUFFER_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhistorybuffersize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhistorybuffersize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HISTORY_BUFFER_SIZE

| Type: | Control attribute |
| --- | --- |
| Description: | The size of the history buffer for the strip chart. This value determines how much previously plotted data is available when you enable ATTR_STRIP_CHART_PAUSED. Pass a value that is at least as large as ATTR_POINTS_PER_SCREEN. |
| Control Types: | Strip charts. |
| Data Type: | integer |
| Valid Range: | Points per screen to 1,000,000 |
| Default Value: | 1024 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalbarcolor.htm language=enus -->
## TOPIC 00629: ATTR_HORIZONTAL_BAR_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalbarcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalbarcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_BAR_COLOR

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | Specifies the color of the horizontal bar. |
| Data Type: | integer |
| Default Value: | VAL_BLUE |
| LabWindows/CVICompatibility: | LabWindows/CVI 2010 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalbarvalue.htm language=enus -->
## TOPIC 00630: ATTR_HORIZONTAL_BAR_VALUE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalbarvalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalbarvalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_BAR_VALUE

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | Specifies the value that the horizontal bar represents. The range is from 0.0 to 100.0. |
| Data Type: | double |
| Default Value: | 0.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2009 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridcolor_cell.htm language=enus -->
## TOPIC 00631: ATTR_HORIZONTAL_GRID_COLOR (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridcolor_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridcolor_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_COLOR (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The RGB color value of the horizontal grid line of the table cell. This attribute refers to the grid line immediately below the cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridcolor_column.htm language=enus -->
## TOPIC 00632: ATTR_HORIZONTAL_GRID_COLOR (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridcolor_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridcolor_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_COLOR (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The RGB color value of the horizontal grid line of the table cell. This attribute refers to the grid line immediately below the cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridcolor_control.htm language=enus -->
## TOPIC 00633: ATTR_HORIZONTAL_GRID_COLOR (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridcolor_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridcolor_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_COLOR (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The default RGB color value of the horizontal grid line of new table cells when ATTR_TABLE_MODE is set to VAL_GRID. This attribute refers to the grid line immediately below the cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Tables. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridcolor_row.htm language=enus -->
## TOPIC 00634: ATTR_HORIZONTAL_GRID_COLOR (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridcolor_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridcolor_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_COLOR (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The RGB color value of the horizontal grid line of the table cell. This attribute refers to the grid line immediately below the cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridcolor_tree item.htm language=enus -->
## TOPIC 00635: ATTR_HORIZONTAL_GRID_COLOR (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridcolor_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridcolor_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_COLOR (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The RGB color value of the horizontal grid line of the tree item. This attribute refers to the grid line at the bottom of the item. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| Default Value: | VAL_OFFWHITE |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridvisible_cell.htm language=enus -->
## TOPIC 00636: ATTR_HORIZONTAL_GRID_VISIBLE (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridvisible_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridvisible_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_VISIBLE (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the horizontal grid line of the table cell. This attribute refers to the grid line immediately below the cell. 0 = Hide grid 1 = Show grid |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridvisible_column.htm language=enus -->
## TOPIC 00637: ATTR_HORIZONTAL_GRID_VISIBLE (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridvisible_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridvisible_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_VISIBLE (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the horizontal grid line of the table cell. This attribute refers to the grid line immediately below the cell. 0 = Hide grid 1 = Show grid |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridvisible_control.htm language=enus -->
## TOPIC 00638: ATTR_HORIZONTAL_GRID_VISIBLE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridvisible_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridvisible_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_VISIBLE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the horizontal grid line of new table cells when ATTR_TABLE_MODE is set to VAL_GRID. This attribute refers to the grid line immediately below the cell. 0 = Hide grid 1 = Show grid |
| Control Types: | Tables. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridvisible_row.htm language=enus -->
## TOPIC 00639: ATTR_HORIZONTAL_GRID_VISIBLE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridvisible_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridvisible_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_VISIBLE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the horizontal grid line of the table cell. This attribute refers to the grid line immediately below the cell. 0 = Hide grid 1 = Show grid |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhorizontalgridvisible_tree item.htm language=enus -->
## TOPIC 00640: ATTR_HORIZONTAL_GRID_VISIBLE (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhorizontalgridvisible_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhorizontalgridvisible_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HORIZONTAL_GRID_VISIBLE (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the horizontal grid line of the tree item. This attribute refers to the grid line at the bottom of the item. 0 = Hide grid 1 = Show grid |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhscrolloffset_control.htm language=enus -->
## TOPIC 00641: ATTR_HSCROLL_OFFSET (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhscrolloffset_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhscrolloffset_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HSCROLL_OFFSET (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The amount (in pixels) by which the control is scrolled to the right. |
| Control Types: | Strings, tables, text boxes, trees. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhscrolloffset_panel.htm language=enus -->
## TOPIC 00642: ATTR_HSCROLL_OFFSET (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhscrolloffset_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhscrolloffset_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HSCROLL_OFFSET (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The amount (in pixels) by which the panel is scrolled to the right. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhscrolloffsetmax_control.htm language=enus -->
## TOPIC 00643: ATTR_HSCROLL_OFFSET_MAX (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhscrolloffsetmax_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhscrolloffsetmax_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HSCROLL_OFFSET_MAX (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The maximum amount (in pixels) by which the control can be scrolled to the right. This depends on the current contents of the control. |
| Control Types: | Strings, tables, text boxes, trees. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrhscrolloffsetmax_panel.htm language=enus -->
## TOPIC 00644: ATTR_HSCROLL_OFFSET_MAX (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrhscrolloffsetmax_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrhscrolloffsetmax_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_HSCROLL_OFFSET_MAX (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The maximum amount (in pixels) by which the panel can be scrolled to the right. This depends on the current contents of the panel. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrimagefile.htm language=enus -->
## TOPIC 00645: ATTR_IMAGE_FILE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrimagefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrimagefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_IMAGE_FILE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies the image file to load into the picture button. The following image types are supported: TIF, PCX, BMP, DIB, RLE, ICO, JPG, PNG, WMF, and EMF. A NULL or empty string reverts the control to its default state, without an image. To determine the size of the buffer to pass when you are obtaining the image, call GetCtrlAttribute and specify the ATTR_IMAGE_FILE_LENGTH attribute. |
| Control Types: | Picture buttons. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrimagefilelength.htm language=enus -->
## TOPIC 00646: ATTR_IMAGE_FILE_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrimagefilelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrimagefilelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_IMAGE_FILE_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the image file name for the picture button. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_IMAGE_FILE attribute. |
| Control Types: | Picture buttons. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrimageindex.htm language=enus -->
## TOPIC 00647: ATTR_IMAGE_INDEX

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrimageindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrimageindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_IMAGE_INDEX

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The index into the tree image list that specifies which image to display with an item. This image will be used when the tree item has no children or when the item is expanded (has exposed children). If the attribute is set to -1, then no image is displayed with the item. |
| Data Type: | integer |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecarrowcolor_cell.htm language=enus -->
## TOPIC 00648: ATTR_INCDEC_ARROW_COLOR (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecarrowcolor_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecarrowcolor_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_ARROW_COLOR (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The RGB color value of the inc/dec arrows of a numeric cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. The arrows are only visible whenever that cell is being edited. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecarrowcolor_column.htm language=enus -->
## TOPIC 00649: ATTR_INCDEC_ARROW_COLOR (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecarrowcolor_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecarrowcolor_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_ARROW_COLOR (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The RGB color value of the inc/dec arrows of a numeric cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. The arrows are only visible whenever that cell is being edited. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecarrowcolor_control.htm language=enus -->
## TOPIC 00650: ATTR_INCDEC_ARROW_COLOR (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecarrowcolor_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecarrowcolor_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_ARROW_COLOR (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The default RGB color value of the inc/dec arrows of a new numeric cells when ATTR_TABLE_MODE is set to VAL_GRID. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Tables. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecarrowcolor_row.htm language=enus -->
## TOPIC 00651: ATTR_INCDEC_ARROW_COLOR (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecarrowcolor_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecarrowcolor_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_ARROW_COLOR (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The RGB color value of the inc/dec arrows of a numeric cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. The arrows are only visible whenever that cell is being edited. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecwidth_cell.htm language=enus -->
## TOPIC 00652: ATTR_INCDEC_WIDTH (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecwidth_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecwidth_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_WIDTH (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | Specifies the width of the inc/dec arrows of a numeric cell. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 9 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecwidth_column.htm language=enus -->
## TOPIC 00653: ATTR_INCDEC_WIDTH (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecwidth_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecwidth_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_WIDTH (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies the width of the inc/dec arrows of a numeric cell. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 9 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecwidth_control.htm language=enus -->
## TOPIC 00654: ATTR_INCDEC_WIDTH (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecwidth_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecwidth_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_WIDTH (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies the width of the inc/dec arrows. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. |
| Control Types: | Numerics, picture rings, rings, numeric slides, tables. |
| Restrictions: | Not valid for controls of type CTRL_RECESSED_MENU_RING, CTRL_MENU_RING, CTRL_POPUP_MENU_RING, and their equivalent Lab Style controls. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 9 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincdecwidth_row.htm language=enus -->
## TOPIC 00655: ATTR_INCDEC_WIDTH (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincdecwidth_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincdecwidth_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCDEC_WIDTH (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies the width of the inc/dec arrows of a numeric cell. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 9 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincrvalue_cell.htm language=enus -->
## TOPIC 00656: ATTR_INCR_VALUE (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincrvalue_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincrvalue_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCR_VALUE (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The incremental value for the Inc/Dec arrows. The data type of the attribute value depends on the data type of the table cell. |
| Data Type: | variable |
| Default Value: | 1.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincrvalue_column.htm language=enus -->
## TOPIC 00657: ATTR_INCR_VALUE (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincrvalue_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincrvalue_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCR_VALUE (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The incremental value for the Inc/Dec arrows. The data type of the attribute value depends on the data type of the table cell. |
| Data Type: | variable |
| Default Value: | 1.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincrvalue_control.htm language=enus -->
## TOPIC 00658: ATTR_INCR_VALUE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincrvalue_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincrvalue_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCR_VALUE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The incremental value for the Inc/Dec arrows. The data type of the attribute value depends on the data type of the control. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. |
| Control Types: | Numerics, numeric slides, tables. |
| Data Type: | variable |
| Default Value: | 1.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrincrvalue_row.htm language=enus -->
## TOPIC 00659: ATTR_INCR_VALUE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrincrvalue_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrincrvalue_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INCR_VALUE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The incremental value for the Inc/Dec arrows. The data type of the attribute value depends on the data type of the table cell. |
| Data Type: | variable |
| Default Value: | 1.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrindentoffset.htm language=enus -->
## TOPIC 00660: ATTR_INDENT_OFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrindentoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrindentoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INDENT_OFFSET

| Type: | Control attribute |
| --- | --- |
| Description: | The horizontal offset in pixels of a child item relative to the parent item. |
| Control Types: | Trees. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 15 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrinnermarkersvisible.htm language=enus -->
## TOPIC 00661: ATTR_INNER_MARKERS_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrinnermarkersvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrinnermarkersvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INNER_MARKERS_VISIBLE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether labels and tick marks are shown next to the minor grid lines of graph axes. 0 = Not visible 1 = Visible |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrinterpolatepixels.htm language=enus -->
## TOPIC 00662: ATTR_INTERPOLATE_PIXELS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrinterpolatepixels.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrinterpolatepixels.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INTERPOLATE_PIXELS

| Type: | Plot attribute |
| --- | --- |
| Description: | Enables the use of linear interpolation in calculating the color of each unplotted pixel in the plot area. With interpolation, the color of each unplotted pixel is calculated using the color of the 4 plotted points surrounding it. Without interpolation, each pixel color is set equal to the color of the nearest plotted point. 0 = Interpolate pixels 1 = No interpolation |
| Plot Types: | Intensity, scaled intensity. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrinterval.htm language=enus -->
## TOPIC 00663: ATTR_INTERVAL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrinterval.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrinterval.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_INTERVAL

| Type: | Control attribute |
| --- | --- |
| Description: | The interval (in seconds) at which the timer control callback function is called. An interval of zero results in timer events occurring as fast as possible. An interval less than the resolution of the system clock results in timer events with an interval equal to the clock resolution. If the timer has already started, setting ATTR_INTERVAL resets the timer. |
| Control Types: | Timers. |
| Data Type: | double |
| Default Value: | 1.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrisseparator_control menu.htm language=enus -->
## TOPIC 00664: ATTR_IS_SEPARATOR (Control Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrisseparator_control menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrisseparator_control%20menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_IS_SEPARATOR (Control Menu)

| Type: | Control Menu attribute |
| --- | --- |
| Description: | Indicates whether the menu item is a separator. 0 = Not a separator 1 = A separator |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrisseparator_menu.htm language=enus -->
## TOPIC 00665: ATTR_IS_SEPARATOR (Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrisseparator_menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrisseparator_menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_IS_SEPARATOR (Menu)

| Type: | Menu attribute |
| --- | --- |
| Description: | Indicates whether the menu item is a separator. 0 = Not a separator 1 = A separator |
| Menu Objects: | Menu Items. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritemactualheight.htm language=enus -->
## TOPIC 00666: ATTR_ITEM_ACTUAL_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritemactualheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritemactualheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_ACTUAL_HEIGHT

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The actual height of the item in pixels, resulting from the calculations performed as a consequence of the value of ATTR_SIZE_MODE. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritembitmap_control menu.htm language=enus -->
## TOPIC 00667: ATTR_ITEM_BITMAP (Control Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritembitmap_control menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritembitmap_control%20menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_BITMAP (Control Menu)

| Type: | Control Menu attribute |
| --- | --- |
| Description: | Bitmap ID of the image to place on the menu item or submenu. The menu must have ATTR_SHOW_IMAGES enabled to see the image. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritembitmap_menu.htm language=enus -->
## TOPIC 00668: ATTR_ITEM_BITMAP (Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritembitmap_menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritembitmap_menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_BITMAP (Menu)

| Type: | Menu attribute |
| --- | --- |
| Description: | Bitmap ID of the image to place on the menu item or submenu. The menu must have ATTR_SHOW_IMAGES enabled to see the image. |
| Menu Objects: | Submenus, menu Items. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritemheight.htm language=enus -->
## TOPIC 00669: ATTR_ITEM_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritemheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritemheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_HEIGHT

| Type: | Tree Item attribute |
| --- | --- |
| Description: | Specifies the height in pixels of the tree item when the value of the item attribute ATTR_SIZE_MODE is VAL_USE_EXPLICIT_SIZE. Use ATTR_ITEM_ACTUAL_HEIGHT to obtain the resulting height of the item. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritemname_control menu.htm language=enus -->
## TOPIC 00670: ATTR_ITEM_NAME (Control Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritemname_control menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritemname_control%20menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_NAME (Control Menu)

| Type: | Control Menu attribute |
| --- | --- |
| Description: | The text name for the menu item. To determine the size of the buffer to pass when you are obtaining the menu item name, call GetCtrlMenuAttribute and specify the ATTR_ITEM_NAME_LENGTH attribute. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritemname_menu.htm language=enus -->
## TOPIC 00671: ATTR_ITEM_NAME (Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritemname_menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritemname_menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_NAME (Menu)

| Type: | Menu attribute |
| --- | --- |
| Description: | The text name for the menu item. To determine the size of the buffer to pass when you are obtaining the menu item name, call GetMenuBarAttribute and specify the ATTR_ITEM_NAME_LENGTH attribute. |
| Menu Objects: | Menu Items. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritemnamelength_control menu.htm language=enus -->
## TOPIC 00672: ATTR_ITEM_NAME_LENGTH (Control Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritemnamelength_control menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritemnamelength_control%20menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_NAME_LENGTH (Control Menu)

| Type: | Control Menu attribute |
| --- | --- |
| Description: | The number of bytes in the menu item text name. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlMenuAttribute and specify the ATTR_ITEM_NAME attribute. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattritemnamelength_menu.htm language=enus -->
## TOPIC 00673: ATTR_ITEM_NAME_LENGTH (Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattritemnamelength_menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattritemnamelength_menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ITEM_NAME_LENGTH (Menu)

| Type: | Menu attribute |
| --- | --- |
| Description: | The number of bytes in the menu item text name. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetMenuBarAttribute and specify the ATTR_ITEM_NAME attribute. |
| Menu Objects: | Menu Items. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelangle_column.htm language=enus -->
## TOPIC 00674: ATTR_LABEL_ANGLE (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelangle_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelangle_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_ANGLE (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies the angle of rotation, in tenths of degrees, of the column label text. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelangle_control.htm language=enus -->
## TOPIC 00675: ATTR_LABEL_ANGLE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelangle_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelangle_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_ANGLE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies the angle of rotation, in tenths of degrees, of the label text. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, strings, strip charts, tables, text boxes, text buttons, timers, toggle buttons, trees. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelangle_row.htm language=enus -->
## TOPIC 00676: ATTR_LABEL_ANGLE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelangle_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelangle_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_ANGLE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies the angle of rotation, in tenths of degrees, of the row label text. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelangle_tree column.htm language=enus -->
## TOPIC 00677: ATTR_LABEL_ANGLE (Tree Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelangle_tree column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelangle_tree%20column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_ANGLE (Tree Column)

| Type: | Tree Column attribute |
| --- | --- |
| Description: | Specifies the angle of rotation, in tenths of degrees, of the column label text. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelbgcolor_control.htm language=enus -->
## TOPIC 00678: ATTR_LABEL_BGCOLOR (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelbgcolor_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelbgcolor_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_BGCOLOR (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the background behind the label text. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, strings, strip charts, tables, text boxes, text buttons, timers, toggle buttons, trees. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelbgcolor_tree item.htm language=enus -->
## TOPIC 00679: ATTR_LABEL_BGCOLOR (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelbgcolor_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelbgcolor_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_BGCOLOR (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The RGB color value of the background behind the label text. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. Using this in SetTreeItemAttribute or GetTreeItemAttribute is equivalent to using it in SetTreeCellAttribute or GetTreeCellAttribute if you pass zero for the column index. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelbold_column.htm language=enus -->
## TOPIC 00680: ATTR_LABEL_BOLD (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelbold_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelbold_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_BOLD (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies whether the column label is bold. 0 = Not bold 1 = Bold |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelbold_tree cell.htm language=enus -->
## TOPIC 00681: ATTR_LABEL_BOLD (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelbold_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelbold_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_BOLD (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | Specifies whether the tree cell label is bold. 0 = Not bold 1 = Bold |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelbold_tree item.htm language=enus -->
## TOPIC 00682: ATTR_LABEL_BOLD (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelbold_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelbold_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_BOLD (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | Specifies whether the tree item label is bold. Using this in SetTreeItemAttribute or GetTreeItemAttribute is equivalent to using it in SetTreeCellAttribute or GetTreeCellAttribute if you pass zero for the column index. 0 = Not bold 1 = Bold |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcharacterset_column.htm language=enus -->
## TOPIC 00683: ATTR_LABEL_CHARACTER_SET (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcharacterset_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcharacterset_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_CHARACTER_SET (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The character set for the column label. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcharacterset_control.htm language=enus -->
## TOPIC 00684: ATTR_LABEL_CHARACTER_SET (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcharacterset_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcharacterset_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_CHARACTER_SET (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The character set for the control label. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, strings, strip charts, tables, text boxes, text buttons, timers, toggle buttons, trees. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcharacterset_row.htm language=enus -->
## TOPIC 00685: ATTR_LABEL_CHARACTER_SET (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcharacterset_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcharacterset_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_CHARACTER_SET (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The character set for the row label. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcharacterset_tab page.htm language=enus -->
## TOPIC 00686: ATTR_LABEL_CHARACTER_SET (Tab Page)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcharacterset_tab page.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcharacterset_tab%20page.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_CHARACTER_SET (Tab Page)

| Type: | Tab Page attribute |
| --- | --- |
| Description: | The character set for the tab page label. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcharacterset_tree cell.htm language=enus -->
## TOPIC 00687: ATTR_LABEL_CHARACTER_SET (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcharacterset_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcharacterset_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_CHARACTER_SET (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | The character set for the tree cell label. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcharacterset_tree column.htm language=enus -->
## TOPIC 00688: ATTR_LABEL_CHARACTER_SET (Tree Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcharacterset_tree column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcharacterset_tree%20column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_CHARACTER_SET (Tree Column)

| Type: | Tree Column attribute |
| --- | --- |
| Description: | The character set for the tree column label. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcolor_tree cell.htm language=enus -->
## TOPIC 00689: ATTR_LABEL_COLOR (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcolor_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcolor_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_COLOR (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | The RGB color value of the label text. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelcolor_tree item.htm language=enus -->
## TOPIC 00690: ATTR_LABEL_COLOR (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelcolor_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelcolor_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_COLOR (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The RGB color value of the label text. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. Using this in SetTreeItemAttribute or GetTreeItemAttribute is equivalent to using it in SetTreeCellAttribute or GetTreeCellAttribute if you pass zero for the column index. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelfontnamelength_tree item.htm language=enus -->
## TOPIC 00691: ATTR_LABEL_FONT_NAME_LENGTH (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelfontnamelength_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelfontnamelength_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_FONT_NAME_LENGTH (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The number of bytes in the name of the font for the tree item label. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetTreeItemAttribute and specify the ATTR_LABEL_FONT attribute. Using this in GetTreeItemAttribute or SetTreeItemAttribute is equivalent to using it in GetTreeCellAttribute or SetTreeCellAttribute if you pass zero for the column index. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelitalic_control.htm language=enus -->
## TOPIC 00692: ATTR_LABEL_ITALIC (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelitalic_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelitalic_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_ITALIC (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the control label is in italics. 0 = Not italics 1 = Italics |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, strings, strip charts, tables, text boxes, text buttons, timers, toggle buttons, trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelitalic_row.htm language=enus -->
## TOPIC 00693: ATTR_LABEL_ITALIC (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelitalic_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelitalic_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_ITALIC (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies whether the row label is in italics. 0 = Not italics 1 = Italics |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelitalic_tree column.htm language=enus -->
## TOPIC 00694: ATTR_LABEL_ITALIC (Tree Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelitalic_tree column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelitalic_tree%20column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_ITALIC (Tree Column)

| Type: | Tree Column attribute |
| --- | --- |
| Description: | Specifies whether the tree column label is in italics. 0 = Not italics 1 = Italics |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabeljustify_tree column.htm language=enus -->
## TOPIC 00695: ATTR_LABEL_JUSTIFY (Tree Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabeljustify_tree column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabeljustify_tree%20column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_JUSTIFY (Tree Column)

| Type: | Tree Column attribute |
| --- | --- |
| Description: | The label justification of tree column. |
| Data Type: | integer |
| Default Value: | VAL_CENTER_CENTER_JUSTIFIED |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_TOP_LEFT_JUSTIFIED | Justify text to the top left. |
| --- | --- |
| VAL_TOP_RIGHT_JUSTIFIED | Justify text to the top right. |
| VAL_TOP_CENTER_JUSTIFIED | Justify text to the top center. |
| VAL_BOTTOM_LEFT_JUSTIFIED | Justify text to the bottom left. |
| VAL_BOTTOM_RIGHT_JUSTIFIED | Justify text to the bottom right. |
| VAL_BOTTOM_CENTER_JUSTIFIED | Justify text to the bottom center. |
| VAL_CENTER_LEFT_JUSTIFIED | Justify text to the center left. |
| VAL_CENTER_RIGHT_JUSTIFIED | Justify text to the center right. |
| VAL_CENTER_CENTER_JUSTIFIED | Justify text to the center. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelpointsize_tree item.htm language=enus -->
## TOPIC 00696: ATTR_LABEL_POINT_SIZE (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelpointsize_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelpointsize_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_POINT_SIZE (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The font point size for the tree item label. Using this in SetTreeItemAttribute or GetTreeItemAttribute is equivalent to using it in SetTreeCellAttribute or GetTreeCellAttribute if you pass zero for the column index. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelsizetotext.htm language=enus -->
## TOPIC 00697: ATTR_LABEL_SIZE_TO_TEXT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelsizetotext.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelsizetotext.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_SIZE_TO_TEXT

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the size of the control label box is dynamically adjusted to the size of the label text. 0 = Label not sized to text 1 = Label sized to text |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, strings, strip charts, tables, text boxes, text buttons, timers, toggle buttons, trees. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelstrikeout_tree column.htm language=enus -->
## TOPIC 00698: ATTR_LABEL_STRIKEOUT (Tree Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelstrikeout_tree column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelstrikeout_tree%20column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_STRIKEOUT (Tree Column)

| Type: | Tree Column attribute |
| --- | --- |
| Description: | Specifies whether the tree column label has strikeout. 0 = No strikeout 1 = Strikeout |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabeltext_column.htm language=enus -->
## TOPIC 00699: ATTR_LABEL_TEXT (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabeltext_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabeltext_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_TEXT (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The text label for the column. This string is used only if ATTR_USE_LABEL_TEXT is set to TRUE. To determine the size of the buffer to pass when you are obtaining the label, call GetTableColumnAttribute and specify the ATTR_LABEL_TEXT_LENGTH attribute. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabeltextlength_row.htm language=enus -->
## TOPIC 00700: ATTR_LABEL_TEXT_LENGTH (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabeltextlength_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabeltextlength_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_TEXT_LENGTH (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The number of bytes in the row label. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetTableRowAttribute and specify the ATTR_LABEL_TEXT attribute. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabeltop.htm language=enus -->
## TOPIC 00701: ATTR_LABEL_TOP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabeltop.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabeltop.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_TOP

| Type: | Control attribute |
| --- | --- |
| Description: | The vertical offset in pixels of the label relative to the origin of the panel. The panel origin (0,0) is the upper-left corner of the panel below the title bar and to the right of the panel frame. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, strings, strip charts, tables, text boxes, text buttons, timers, toggle buttons, trees. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767, or VAL_AUTO_CENTER |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_AUTO_CENTER | Center the label with respect to the control. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelunderline_column.htm language=enus -->
## TOPIC 00702: ATTR_LABEL_UNDERLINE (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelunderline_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelunderline_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_UNDERLINE (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies whether the column label is underlined. 0 = Not underlined 1 = Underlined |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelunderline_row.htm language=enus -->
## TOPIC 00703: ATTR_LABEL_UNDERLINE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelunderline_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelunderline_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_UNDERLINE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies whether the row label is underlined. 0 = Not underlined 1 = Underlined |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelunderline_tree cell.htm language=enus -->
## TOPIC 00704: ATTR_LABEL_UNDERLINE (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelunderline_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelunderline_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_UNDERLINE (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | Specifies whether the tree cell label is underlined. 0 = Not underlined 1 = Underlined |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelunderline_tree column.htm language=enus -->
## TOPIC 00705: ATTR_LABEL_UNDERLINE (Tree Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelunderline_tree column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelunderline_tree%20column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_UNDERLINE (Tree Column)

| Type: | Tree Column attribute |
| --- | --- |
| Description: | Specifies whether the tree column label is underlined. 0 = Not underlined 1 = Underlined |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelvisible_column.htm language=enus -->
## TOPIC 00706: ATTR_LABEL_VISIBLE (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelvisible_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelvisible_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_VISIBLE (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies whether the column label is visible. 0 = Hidden 1 = Visible |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrlabelwidth.htm language=enus -->
## TOPIC 00707: ATTR_LABEL_WIDTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrlabelwidth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrlabelwidth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_LABEL_WIDTH

| Type: | Control attribute |
| --- | --- |
| Description: | The width of the label body in pixels. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, strings, strip charts, tables, text boxes, text buttons, timers, toggle buttons, trees. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmaxentrychars_row.htm language=enus -->
## TOPIC 00708: ATTR_MAX_ENTRY_CHARS (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmaxentrychars_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmaxentrychars_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MAX_ENTRY_CHARS (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The maximum number of characters that can be entered into a table cell. In this context, a dual-byte character counts as 1. If you want to restrict the table cell to a specific number of bytes, use ATTR_MAX_ENTRY_LENGTH. If you use both attributes, LabWindows/CVI applies the more restrictive of the two values. A (-1) value means no limit. |
| Data Type: | integer |
| Valid Range: | -1 or greater |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 6.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmaxentrychars_tree cell.htm language=enus -->
## TOPIC 00709: ATTR_MAX_ENTRY_CHARS (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmaxentrychars_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmaxentrychars_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MAX_ENTRY_CHARS (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | The maximum number of characters that can be entered into a tree cell. In this context, a dual-byte character counts as 1. If you want to restrict the tree cell to a specific number of bytes, use ATTR_MAX_ENTRY_LENGTH. If you use both attributes, LabWindows/CVI applies the more restrictive of the two values. A (-1) value means no limit. |
| Data Type: | integer |
| Valid Range: | -1 or greater |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2010SP1 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmaxentrylength_column.htm language=enus -->
## TOPIC 00710: ATTR_MAX_ENTRY_LENGTH (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmaxentrylength_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmaxentrylength_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MAX_ENTRY_LENGTH (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The maximum length of the value, in bytes, that can be entered into a table cell. If you want to restrict the table cell to a specific number of characters, use ATTR_MAX_ENTRY_CHARS. If you use both attributes, LabWindows/CVI applies the more restrictive of the two values. A (-1) value means no limit. |
| Data Type: | integer |
| Valid Range: | -1 or greater |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmaxentrylength_control.htm language=enus -->
## TOPIC 00711: ATTR_MAX_ENTRY_LENGTH (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmaxentrylength_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmaxentrylength_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MAX_ENTRY_LENGTH (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The maximum length of the value, in bytes, that can be entered into a string or text box control. If you want to restrict the string or text box control to a specific number of characters, use ATTR_MAX_ENTRY_CHARS. If you use both attributes, LabWindows/CVI applies the more restrictive of the two values. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. A (-1) value means no limit. |
| Control Types: | Strings, tables, text boxes. |
| Data Type: | integer |
| Valid Range: | -1 or greater |
| Default Value: | -1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmaxvalue_cell.htm language=enus -->
## TOPIC 00712: ATTR_MAX_VALUE (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmaxvalue_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmaxvalue_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MAX_VALUE (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The maximum value of a table cell. The user is not allowed to enter a value or use the increment arrows to alter the value above the maximum. The data type of this attribute value depends on the data type of the table cell. |
| Data Type: | variable |
| Default Value: | +Inf |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenubarimagesize.htm language=enus -->
## TOPIC 00713: ATTR_MENU_BAR_IMAGE_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenubarimagesize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenubarimagesize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_BAR_IMAGE_SIZE

| Type: | Menu attribute |
| --- | --- |
| Description: | Indicates the size allocated for images placed in a menu. This space is always square and is influenced by the menu bar font settings. |
| Menu Objects: | Menu Bars. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenubaritalic.htm language=enus -->
## TOPIC 00714: ATTR_MENU_BAR_ITALIC

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenubaritalic.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenubaritalic.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_BAR_ITALIC

| Type: | Menu attribute |
| --- | --- |
| Description: | Specifies whether the font associated with the specified menu bar is italic. |
| Menu Objects: | Menu Bars. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenubarpointsize.htm language=enus -->
## TOPIC 00715: ATTR_MENU_BAR_POINT_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenubarpointsize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenubarpointsize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_BAR_POINT_SIZE

| Type: | Menu attribute |
| --- | --- |
| Description: | Specifies the point size of the font associated with the specified menu bar. |
| Menu Objects: | Menu Bars. |
| Data Type: | integer |
| Valid Range: | 1-255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenubarstrikeout.htm language=enus -->
## TOPIC 00716: ATTR_MENU_BAR_STRIKEOUT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenubarstrikeout.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenubarstrikeout.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_BAR_STRIKEOUT

| Type: | Menu attribute |
| --- | --- |
| Description: | Specifies whether the font associated with the specified menu bar is struck out. |
| Menu Objects: | Menu Bars. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenuheight.htm language=enus -->
## TOPIC 00717: ATTR_MENU_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenuheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenuheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_HEIGHT

| Type: | Panel attribute |
| --- | --- |
| Description: | Height of the menu in pixels. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 21 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenuimagebackgroundcolor_menu.htm language=enus -->
## TOPIC 00718: ATTR_MENU_IMAGE_BACKGROUND_COLOR (Menu)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenuimagebackgroundcolor_menu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenuimagebackgroundcolor_menu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_IMAGE_BACKGROUND_COLOR (Menu)

| Type: | Menu attribute |
| --- | --- |
| Description: | Specifies the background color of the image column on menus. ATTR_SHOW_IMAGES must be enabled for this attribute to have any effect. |
| Menu Objects: | Menus, submenus. |
| Data Type: | integer |
| Default Value: | VAL_TRANSPARENT |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenuname.htm language=enus -->
## TOPIC 00719: ATTR_MENU_NAME

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenuname.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenuname.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_NAME

| Type: | Menu attribute |
| --- | --- |
| Description: | The text name for the menu. To determine the size of the buffer to pass when you are obtaining the menu name, call GetMenuBarAttribute and specify the ATTR_MENU_NAME_LENGTH attribute. |
| Menu Objects: | Menus. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrmenunamelength.htm language=enus -->
## TOPIC 00720: ATTR_MENU_NAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrmenunamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrmenunamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MENU_NAME_LENGTH

| Type: | Menu attribute |
| --- | --- |
| Description: | The number of bytes in the menu text name. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetMenuBarAttribute and specify the ATTR_MENU_NAME attribute. |
| Menu Objects: | Menus, submenus. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrminnumlinesvisible_row.htm language=enus -->
## TOPIC 00721: ATTR_MIN_NUM_LINES_VISIBLE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrminnumlinesvisible_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrminnumlinesvisible_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MIN_NUM_LINES_VISIBLE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The number of lines of text to take into account when performing the calculations associated with the VAL_SIZE_TO_CELL_FONT value of ATTR_SIZE_MODE. |
| Data Type: | integer |
| Valid Range: | 1 or greater |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrminvalue_row.htm language=enus -->
## TOPIC 00722: ATTR_MIN_VALUE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrminvalue_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrminvalue_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MIN_VALUE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The minimum value of a table cell. The user is not allowed to enter a value or use the decrement arrows to alter the value below the minimum. The data type of this attribute value depends on the data type of the table cell. |
| Data Type: | variable |
| Default Value: | -Inf |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrminwidthforscaling.htm language=enus -->
## TOPIC 00723: ATTR_MIN_WIDTH_FOR_SCALING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrminwidthforscaling.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrminwidthforscaling.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_MIN_WIDTH_FOR_SCALING

| Type: | Panel attribute |
| --- | --- |
| Description: | Specifies the smallest panel width for which scaling is allowed. If you enable the ATTR_SCALE_CONTENTS_ON_RESIZE attribute and the user resizes your panel so that it is very small, scaling might cause the controls in the panel to overlap. This attribute allows you to specify the smallest panel width for which scaling is allowed. If the user resizes the panel so that it is narrower than the specified width, the content area is clipped. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnextctrl.htm language=enus -->
## TOPIC 00724: ATTR_NEXT_CTRL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnextctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnextctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NEXT_CTRL

| Type: | Control attribute |
| --- | --- |
| Description: | The ID of the next control on the panel. The panel attribute ATTR_PANEL_FIRST_CTRL returns the lowest control ID that exists in the panel. When you call GetCtrlAttribute on the first control ID, ATTR_NEXT_CTRL returns the next higher control ID in the panel. On the last control, ATTR_NEXT_CTRL returns zero. Use the panel attribute ATTR_NUM_CTRLS to get the total number of controls in a panel. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strings, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnextitemid.htm language=enus -->
## TOPIC 00725: ATTR_NEXT_ITEM_ID

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnextitemid.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnextitemid.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NEXT_ITEM_ID

| Type: | Menu attribute |
| --- | --- |
| Description: | The ID of the next menu item in the menu. The menu attribute ATTR_FIRST_ITEM_ID returns the ID of the first menu item in the menu. When you call GetMenuBarAttribute on the first menu item ID, ATTR_NEXT_ITEM_ID returns the ID of the next menu item in the menu. On the last menu item, ATTR_NEXT_ITEM_ID returns zero. Use the menu attribute ATTR_NUM_MENU_ITEMS to get the total number of menu items in a menu. |
| Menu Objects: | Menu Items. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnoeditlabel.htm language=enus -->
## TOPIC 00726: ATTR_NO_EDIT_LABEL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnoeditlabel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnoeditlabel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NO_EDIT_LABEL

| Type: | Tree Item attribute |
| --- | --- |
| Description: | Determines whether the tree item label can be interactively edited. 0 = Tree item label can be interactively edited 1 = Tree item label cannot be interactively edited |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnoedittext_cell.htm language=enus -->
## TOPIC 00727: ATTR_NO_EDIT_TEXT (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnoedittext_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnoedittext_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NO_EDIT_TEXT (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | Specifies whether to disable the ability to edit the text in a cell. 0 = Enable editing 1 = Disable editing |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnoedittext_control.htm language=enus -->
## TOPIC 00728: ATTR_NO_EDIT_TEXT (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnoedittext_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnoedittext_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NO_EDIT_TEXT (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to disable the ability to edit the text in a control. 0 = Enable editing 1 = Disable editing |
| Control Types: | Numerics, strings, tables, text boxes. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnoedittext_row.htm language=enus -->
## TOPIC 00729: ATTR_NO_EDIT_TEXT (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnoedittext_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnoedittext_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NO_EDIT_TEXT (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Specifies whether to disable the ability to edit the text in a cell. 0 = Enable editing 1 = Disable editing |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnumcelldfltvalue_control.htm language=enus -->
## TOPIC 00730: ATTR_NUM_CELL_DFLT_VALUE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnumcelldfltvalue_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnumcelldfltvalue_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NUM_CELL_DFLT_VALUE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies the default numeric value for the new table cells when ATTR_TABLE_MODE is set to VAL_GRID. The default value is the value to which the cell is set when the panel is loaded or when you call DefaultCtrl or DefaultPanel. The data type of the attribute value depends on the data type of the cell. |
| Control Types: | Tables. |
| Data Type: | variable |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnumcolorrampvalues.htm language=enus -->
## TOPIC 00731: ATTR_NUM_COLOR_RAMP_VALUES

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnumcolorrampvalues.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnumcolorrampvalues.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NUM_COLOR_RAMP_VALUES

| Type: | Control attribute |
| --- | --- |
| Description: | The number of ColorMapEntry structures in the color ramp of the specified control. |
| Control Types: | Numeric slides. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnumctrls.htm language=enus -->
## TOPIC 00732: ATTR_NUM_CTRLS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnumctrls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnumctrls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NUM_CTRLS

| Type: | Panel attribute |
| --- | --- |
| Description: | The number of controls in the panel you specify. The panel attribute ATTR_PANEL_FIRST_CTRL returns the lowest control ID that exists in the panel. When you call GetCtrlAttribute on this first control ID, ATTR_NEXT_CTRL returns the next higher control ID in the panel. On the last control, ATTR_NEXT_CTRL returns zero. Use the panel attribute ATTR_NUM_CTRLS to get the total number of controls in a panel. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnumcursors.htm language=enus -->
## TOPIC 00733: ATTR_NUM_CURSORS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnumcursors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnumcursors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NUM_CURSORS

| Type: | Control attribute |
| --- | --- |
| Description: | The number of cursors in a graph control. |
| Control Types: | Graphs. |
| Data Type: | integer |
| Valid Range: | 0 or greater |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnumdivisions.htm language=enus -->
## TOPIC 00734: ATTR_NUM_DIVISIONS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnumdivisions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnumdivisions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NUM_DIVISIONS

| Type: | Control attribute |
| --- | --- |
| Description: | The number of divisions in a numeric slide control. |
| Control Types: | Numeric slides. |
| Data Type: | integer |
| Valid Range: | 1 to 100, or VAL_AUTO |
| Default Value: | VAL_AUTO |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_AUTO |
| --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrnummonitors.htm language=enus -->
## TOPIC 00735: ATTR_NUM_MONITORS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrnummonitors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrnummonitors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_NUM_MONITORS

| Type: | System attribute |
| --- | --- |
| Description: | The number of monitors included in the desktop. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrofftext.htm language=enus -->
## TOPIC 00736: ATTR_OFF_TEXT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrofftext.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrofftext.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_OFF_TEXT

| Type: | Control attribute |
| --- | --- |
| Description: | The text displayed on the control in the OFF state. To determine the size of the buffer to pass when you are obtaining the text, call GetCtrlAttribute and specify the ATTR_OFF_TEXT_LENGTH attribute. |
| Control Types: | Binary switches, text buttons. |
| Data Type: | string |
| Default Value: | "Off" |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattroffvaluelength.htm language=enus -->
## TOPIC 00737: ATTR_OFF_VALUE_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattroffvaluelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattroffvaluelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_OFF_VALUE_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the OFF value text for a binary switch of data type VAL_STRING. The length does not include the ASCII NUL byte. For controls of data type VAL_STRING, use this attribute to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_OFF_VALUE attribute. |
| Control Types: | Binary switches. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattroncolor.htm language=enus -->
## TOPIC 00738: ATTR_ON_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattroncolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattroncolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ON_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the control's ON state. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | LEDs, picture buttons, radio buttons, text buttons, toggle buttons. |
| Restrictions: | Not valid for controls of type CTRL_PICTURE_COMMAND_BUTTON. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattronvalue.htm language=enus -->
## TOPIC 00739: ATTR_ON_VALUE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattronvalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattronvalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ON_VALUE

| Type: | Control attribute |
| --- | --- |
| Description: | The value of the binary switch in the ON position. The data type of this attribute value depends on the data type of the control. For controls of data type VAL_STRING, call GetCtrlAttribute and specify the ATTR_ON_VALUE_LENGTH attribute to determine the size of the buffer to pass when you are obtaining the on value. |
| Control Types: | Binary switches. |
| Data Type: | variable |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattroperableasindicator.htm language=enus -->
## TOPIC 00740: ATTR_OPERABLE_AS_INDICATOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattroperableasindicator.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattroperableasindicator.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_OPERABLE_AS_INDICATOR

| Type: | Control attribute |
| --- | --- |
| Description: | Use this attribute in order to have splitter controls that have ATTR_CTRL_MODE set to VAL_INDICATOR still be operable. This attribute is useful if you want to have an operable splitter but do not want it to retain the keyboard focus. 0 = Disabled 1 = Enabled |
| Control Types: | Splitters. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattroverlapped.htm language=enus -->
## TOPIC 00741: ATTR_OVERLAPPED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattroverlapped.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattroverlapped.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_OVERLAPPED

| Type: | Control attribute |
| --- | --- |
| Description: | Indicates whether the canvas is overlapped by another control. 0 = Not overlapped 1 = Overlapped |
| Control Types: | Canvases. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpadding_cell.htm language=enus -->
## TOPIC 00742: ATTR_PADDING (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpadding_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpadding_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PADDING (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The minimum number of characters to display in the table cell. This pads the number with zeros to ensure that it is at least the minimum length. If the length of the number is greater than the minimum, the cell will display the complete number even if it exceeds the minimum number of characters. |
| Data Type: | integer |
| Valid Range: | 0 to 64 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpadding_control.htm language=enus -->
## TOPIC 00743: ATTR_PADDING (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpadding_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpadding_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PADDING (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The minimum number of characters to display in the numeric control. This pads the number with zeros to ensure that it is at least the minimum length. If the length of the number is greater than the minimum, the numeric will display the complete number even if it exceeds the minimum number of characters. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. |
| Control Types: | Numerics, numeric slides, tables. |
| Data Type: | integer |
| Valid Range: | 0 to 64 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpanelfirstctrl.htm language=enus -->
## TOPIC 00744: ATTR_PANEL_FIRST_CTRL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpanelfirstctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpanelfirstctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PANEL_FIRST_CTRL

| Type: | Panel attribute |
| --- | --- |
| Description: | The ID of the first control on the panel. The panel attribute ATTR_PANEL_FIRST_CTRL returns the lowest control ID that exists in the panel. When you call GetCtrlAttribute on this first control ID, ATTR_NEXT_CTRL returns the next higher control ID in the panel. On the last control, ATTR_NEXT_CTRL returns zero. Use the panel attribute ATTR_NUM_CTRLS to get the total number of controls in a panel. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpaperwidth.htm language=enus -->
## TOPIC 00745: ATTR_PAPER_WIDTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpaperwidth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpaperwidth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PAPER_WIDTH

| Type: | Print attribute |
| --- | --- |
| Description: | Note This attribute has been superseded by ATTR_PRINT_AREA_WIDTH. Specifies the width of the output in millimeters/10. VAL_USE_PRINTER_DEFAULT (now called VAL_USE_ENTIRE_PAPER) specifies that the output should use as much of the paper width as possible. VAL_INTEGRAL_SCALE forces the hardcopy output to be scaled to an integral multiple of its screen size, thereby preventing aliasing and distortion. |
|  | Note This attribute has been superseded by ATTR_PRINT_AREA_WIDTH. |
| Types of Printing: | Graphics. |
| Data Type: | integer |
| Valid Range: | 1 to 7620, VAL_USE_PRINTER_DEFAULT or VAL_INTEGRAL_SCALE |
| Default Value: | VAL_USE_PRINTER_DEFAULT |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_INTEGRAL_SCALE | When applied to either the height or the width, VAL_INTEGRAL_SCALE ensures that the ratio between the object's height and width in dots on the hardcopy is the same as the ratio between its height and width in pixels on the screen. This prevents distortion. Using VAL_INTEGRAL_SCALE also ensures that, for both the height and width, the number of dots on the hardcopy is an integral multiple of the number of pixels on the screen. This prevents aliasing, in which screen lines are lost or duplicated in an uneven manner. If you use VAL_INTEGRAL_SCALE for both the height and width, the number of dots on the hardcopy will be identical to the number of pixels on the screen. If you use VAL_INTEGRAL_SCALE on just one dimension, then LabWindows/CVI may round down the other dimension to maintain the integral scaling. |
| --- | --- |
| VAL_USE_PRINTER_DEFAULT | Use as much of the paper as possible. (The defined constant for this value has been changed to VAL_USE_ENTIRE_PAPER). |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpencolor.htm language=enus -->
## TOPIC 00746: ATTR_PEN_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpencolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpencolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PEN_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value used to draw points, lines, frames, and text on the canvas. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Canvases. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpenwidth.htm language=enus -->
## TOPIC 00747: ATTR_PEN_WIDTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpenwidth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpenwidth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PEN_WIDTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of pixels in the width of a pen stroke. This applies to lines, frames, and points. |
| Control Types: | Canvases. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpictbgcolor.htm language=enus -->
## TOPIC 00748: ATTR_PICT_BGCOLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpictbgcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpictbgcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PICT_BGCOLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value in the portions of the control not covered by an image or a drawn shape. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. PNG images with alpha-channel transparency lose their transparency when displayed on transparent classic-style picture controls. |
| Control Types: | Canvases, picture rings, pictures. |
| Data Type: | integer |
| Default Value: | VAL_WHITE |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotfontnamelength.htm language=enus -->
## TOPIC 00749: ATTR_PLOT_FONT_NAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotfontnamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotfontnamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_FONT_NAME_LENGTH

| Type: | Plot attribute |
| --- | --- |
| Description: | The number of bytes in the name of the font for the text plot. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetPlotAttribute and specify the ATTR_PLOT_FONT attribute. |
| Plot Types: | Text. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotlgfont.htm language=enus -->
## TOPIC 00750: ATTR_PLOT_LG_FONT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotlgfont.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotlgfont.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_LG_FONT

| Type: | Plot attribute |
| --- | --- |
| Description: | The name of the font for the text string that describes the plot in the graph legend. To determine the size of the buffer to pass when you are obtaining the font name, call GetPlotAttribute and specify the ATTR_PLOT_LG_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Always set the font before setting the size or style. |
| Plot Types: | Arc, bitmap, intensity, line, oval, point, polygon, rectangle, scaled intensity, text, waveform, X, XY, Y. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
