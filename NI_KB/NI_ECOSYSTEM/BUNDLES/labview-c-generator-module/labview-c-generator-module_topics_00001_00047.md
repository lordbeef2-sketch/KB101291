# NI DOCUMENT BUNDLE: labview-c-generator-module

<!--NI_BUNDLE_CHUNK bundle=labview-c-generator-module start=1 end=47 -->
<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_arrays_function_prototype.html language=enus -->
## TOPIC 00001: Using Arrays in the Function Prototype (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_arrays_function_prototype.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_arrays_function_prototype.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Using Arrays in the Function Prototype (C Generator)

The LabVIEW C Generator supports arrays as parameters of the [exported VI prototype](cgen_config_function_prototype.html). You can use array pointers or LabVIEW arrays to pass data in an exported VI function. A length parameter for both inputs and outputs follows the 1D array parameter. For an array, the length is the total number of elements in the array.

#### Array Pointers

When you use array pointers to pass 1D arrays, the prototype includes pointers to data elements and the length. For example, a 1D array of doubles is represented as a float64 * and an int32 length parameter.

When you use array pointers to pass multi-dimensional arrays, the C Generator creates the following struct, which contains pointers to the data elements and the dimension size.

typedef struct {

int32 dimSizes[2],

float64 *elemArr;   //In this case, a 2D array of doubles.

} TD1;

In the [Define VI Prototype](../lvcgenref/define_vi_prototype_cgen_db.html) dialog box, select the array in the **Parameters** list and set the **Pass By** option to **Array Data Pointer** to use array pointers. When you use array pointers to pass data, LabVIEW creates an internal copy of the array.

#### LabVIEW Arrays

Use LabVIEW arrays to avoid creating an extra copy of the array in the exported VI function. When you use LabVIEW arrays to pass data, the C Generator creates the following struct. This struct is defined in the VINameLib.h file, where VIName is the name of the exported VI.

typedef struct {

uInt32 res1;

int16 res2;

uInt8 res3;

uInt8 res4;

uInt32 numDims;

ArrDimSize dimSizes[2];   //In this case, a 2D array of doubles

float64 elemArr[1];

} LvArr1, *LVArr1Hdl;

In the **Define VI Prototype** dialog box, select the array in the **Parameters** list and set the **Pass By** option to **LV Array** to use LabVIEW arrays.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_appcontrol.html language=enus -->
## TOPIC 00002: Limitations with Application Control VIs and Functions (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_appcontrol.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_appcontrol.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Application Control VIs and Functions (C Generator)

The [Close Reference](/csh?topicname=glang/close_lv_object_reference.html) function is supported, but the following refnums are unsupported:

- .NET
- ActiveX

The [Call By Reference Node](/csh?topicname=glang/call_by_reference_node.html) is supported only for local references. To use a Call By Reference Node with a local reference, create a VI reference, include the VI you are referencing in the **Always Included** listbox in the [Source Files](../lvcgenref/source_files_page_ccode_gen_db.html) page of the [C Code Generation Properties](../lvcgenref/c_code_gen_properties_db.html) dialog box, and then use the Call By Reference Node to call the VI by reference using the VI name.

The [Call Chain](/csh?topicname=glang/call_chain.html) function always returns an empty array.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_express.html language=enus -->
## TOPIC 00003: Limitations with Express VIs (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_express.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_express.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Express VIs (C Generator)

The following Express VIs and palettes are unsupported:

- Comparison
- Elapsed Time
- Input Express VIs
- Output Express VIs except the Build Text Express VI
- Scaling and Mapping
- Signal Analysis Express VIs
- Signal Manipulation Express VIs
- Time Delay
- Time Domain Math

The dynamic data type is unsupported.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_libs_exes.html language=enus -->
## TOPIC 00004: Limitations with Libraries and Executables (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_libs_exes.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_libs_exes.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Libraries and Executables (C Generator)

You can use a [Call Library Function Node](/csh?topicname=glang/call_library_function.html) to access external C libraries. Include the libraries as additional files in the **Source Files** page of the **Build Specification Properties** dialog box. LabVIEW links these files when you build the VI into an application.

If you want to call external libraries from the [exported VI](cgen_dev_vis_cgen.html), you must create a .dll file that contains the exported function names. Add the .dll file to the **Library Name or Path** path control in the [Call Library Function](/csh?topicname=lvdialog/call_lib_function_db.html) dialog box.

National Instruments recommends that you do not wire large arrays to or from a Call Library Function Node because large arrays might cause execution delays. To avoid execution delays, split large arrays into smaller arrays and pass them one at a time to or from the Call Library Function Node.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_memcontrol.html language=enus -->
## TOPIC 00005: Limitations with Memory Control Functions (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_memcontrol.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_memcontrol.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Memory Control Functions (C Generator)

The LabVIEW C Generator supports the following [Memory Control](/csh?topicname=glang/copy_mitigation.html) functions:

- Data Value Reference Read / Write Element
- New Data Value Reference
- Delete Data Value Reference

The C Generator supports data value references with the following limitations:

- You cannot create a data value reference to a LabVIEW class object.
- You cannot use the Type Cast or Unflatten From String function to obtain a valid data value reference. You must use the New Data Value Reference function instead.
- To avoid deadlock, do not place an In Place Element structure with a data value reference inside another In Place Element structure with the same data value reference.
- When you use a Data Value Reference Read / Write Element border node, the border node does not return all error codes and messages.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_numeric.html language=enus -->
## TOPIC 00006: Limitations with Numeric Functions (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_numeric.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_numeric.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Numeric Functions (C Generator)

The [Round To Nearest](/csh?topicname=glang/round_to_nearest.html) and [Round Toward –Infinity](/csh?topicname=glang/round_to_neginfinity.html) functions return the same output on timestamps because when a timestamp is rounded to the nearest integer, the timestamp value always is rounded down to the next lowest integer.

You cannot use the [Type Cast](/csh?topicname=glang/type_cast.html) or [Unflatten From String](/csh?topicname=glang/unflatten_from_string.html) function to obtain a valid data value reference. You must use the [New Data Value Reference](/csh?topicname=glang/new_data_value_reference.html) function instead.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_signalprocess.html language=enus -->
## TOPIC 00007: Limitations with Signal Processing VIs (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_signalprocess.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_signalprocess.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Signal Processing VIs (C Generator)

The [Unit Vector](/csh?topicname=lvanls/unit_vector.html) VI does not support setting the **norm type** input to 5, which is the User Defined type of norm.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_strings.html language=enus -->
## TOPIC 00008: Limitations with String Functions (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_strings.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_strings.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with String Functions (C Generator)

The [Format Into String](/csh?topicname=glang/format_into_string.html) and [Scan From String](/csh?topicname=glang/scan_from_string.html) functions do not support the %x or %z [format specifier](/csh?topicname=lvconcepts/format_specifier_syntax.html). The Scan From String function does not support wildcard matches.

The [Scan String For Tokens](/csh?topicname=glang/scan_string_for_tokens.html) function does not support caching of delimiter or operator data.

The [Search and Replace String](/csh?topicname=glang/search_and_replace_string.html) function does not support regular expression mode. Right-clicking the function and selecting **Regular Expression** has no effect on the function. The following Search and Replace String inputs are unsupported because they apply to regular expression mode:

- multiline?
- ignore case?

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_structures.html language=enus -->
## TOPIC 00009: Limitations with Structures (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_structures.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_structures.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Structures (C Generator)

#### Formula Nodes

[Formula Nodes](/csh?topicname=glang/formula_node.html) have the following restrictions:

- You must use strict C code or LabVIEW cannot build the VI into an application. LabVIEW does not check for strict C code at edit time.
- Arrays and clusters are unsupported in the Formula Node.
- You cannot define variables inside of a Formula Node. For example, int x; and double y; result in an error when you build the VI into an application. The only way to create variables in a Formula Node is to create the variables as inputs and outputs.
- The ** power function is unsupported. To perform a power operation in a Formula Node, you must use the pow() function. For example, replace Y=X**4; with Y=pow(X,4); .
- You cannot declare data types for the inputs or outputs. If you declare outputs inside of a Formula Node, the Formula Node causes syntax errors in the generated code. Create an input with the same name and type as the output to avoid declaring the output inside of a Formula Node.
- All Formula Node outputs are floating-point values.

#### Feedback Nodes

[Feedback Nodes](/csh?topicname=glang/feedback_node.html) have the following restrictions:

- Setting Delay on the Configuration page of the Properties dialog box has no effect. The value of Delay defaults to 1 .
- The Feedback Node always initializes on first call of the VI. Right-clicking the initializer terminal and selecting a value for Globally Initialize from the shortcut menu has no effect.

#### Conditional Disable Structure

Use the [Conditional Disable](/csh?topicname=glang/conditional_disable_structure.html) structure to execute a subdiagram based on the target operating system.

When you [add a subdiagram](/csh?topicname=lvhowto/adding_subdiagrams.html) to the Conditional Disable structure, you must set the **Value** of the TARGET_TYPE symbol to Embedded in the [Configure Condition](/csh?topicname=lvdialog/configure_condition_db.html) dialog box. When the LabVIEW C Generator [generates C code](cgen_gen_code_from_vis.html) for a VI that contains a Conditional Disable structure, the C Generator generates C code only for the subdiagram with the **Value** of the TARGET_TYPE symbol set to Embedded. To generate C code for the Conditional Disable structure, the structure also must include a subdiagram with the **Value** of the TARGET_TYPE symbol set to Windows. While the C Generator does not generate C code for the subdiagram that executes in the Windows target, the subdiagram for the Windows target cannot contain broken code or unsupported functionality.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_bd_timediaerror.html language=enus -->
## TOPIC 00010: Limitations with Timing VIs and Functions (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_bd_timediaerror.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_bd_timediaerror.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Timing VIs and Functions (C Generator)

The [Format Date/Time String](/csh?topicname=glang/format_date_time_string.html) function does not support the following formats:

- %j
- %U
- %w
- %W
- %z

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_build_analysis_lib.html language=enus -->
## TOPIC 00011: Building the Analysis Libraries (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_build_analysis_lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_build_analysis_lib.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Building the Analysis Libraries (C Generator)

When you use the LabVIEW C Generator to [generate C code](cgen_gen_code_from_vis.html) for an exported VI that uses the [Mathematics](/csh?topicname=gmath/mathematics.html) or [Signal Processing](/csh?topicname=lvanls/signal_processing_vis.html) VIs, you must build the analysis library and link to it from the project. You can build the analysis library as a static library and link to it from multiple C code generation projects.

Refer to labview\CCodeGen\analysis\Makefile for an example analysis [makefile](cgen_build_gen_c_code_spec_targ.html) that builds the analysis library into a 32-bit Windows platform (Win32) statically linked library.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_build_gen_c_code_spec_targ.html language=enus -->
## TOPIC 00012: Building Generated C Code for a Specific Target (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_build_gen_c_code_spec_targ.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_build_gen_c_code_spec_targ.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Building Generated C Code for a Specific Target (C Generator)

When you [build the C Code Generation build specification](cgen_gen_code_from_vis.html), the LabVIEW C Generator generates C code files and makefiles. Makefiles describe how to create an external application based on target requirements and dependencies. You [use the GNU Make utility](cgen_run_makefiles.html) to build applications and libraries automatically from the generated C code. The C Generator generates the following makefiles:

- Makefile is an example makefile. When you use the make command, the GNU Make utility reads this file. After the C Generator generates Makefile , the C Generator does not overwrite this file if you regenerate the C code. If you want to generate a new example Makefile , you must delete the file before regenerating the C code.
- dependencies.mk is the secondary makefile. The C Generator includes all LabVIEW settings, such the build specification name and C code generation option values, that are required to generate C code. The C Generator updates this file if the hierarchy of the exported VI changes. LabVIEW also automatically overwrites this file during the build process.

Before you can [run](cgen_run_makefiles.html) the Makefile, you must complete the following steps to setup the required toolchain.

1. Install GNU Make for Windows. Makefile is formatted to run only on the GNU Make utility. Refer to the Make for Windows Web site at http://gnuwin32.sourceforge.net/packages/make.htm to install the GNU Make utility.
2. Setup the PATH environment variable in Windows to include make.exe .
3. Install a compiler for the target on which you want the external application to run. By default, Makefile uses the Microsoft Visual Studio compiler. The VSPATH variable in Makefile specifies the location of the Microsoft Visual Studio compiler.
4. Setup the environment for the compiler. Refer to the compiler documentation for more information about setting up the environment.

You must [edit](cgen_edit_makefiles.html) the Makefile to customize compiler and linker options, dependencies, and build rules.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_cgen_fixedpoint.html language=enus -->
## TOPIC 00013: Limitations with Fixed-Point Support (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_cgen_fixedpoint.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_cgen_fixedpoint.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Limitations with Fixed-Point Support (C Generator)

The [fixed-point data type](/csh?topicname=lvconcepts/numeric_data.html) has limited support. The C Generator accepts a maximum word length of 32 bits for fixed-point data.

|  | Note Overflow mode is supported, but overflow status is not supported. |
| --- | --- |

#### Comparison Functions

The following [Comparison](/csh?topicname=glang/comparison_functions.html) functions support the fixed-point data type:

- Equal?
- Equal To 0?
- Greater Or Equal?
- Greater Or Equal To 0?
- Greater?
- Greater Than 0?
- In Range and Coerce
- Less Or Equal?
- Less Or Equal To 0?
- Less?
- Less Than 0?
- Not Equal?
- Not Equal To 0?

#### Conversion Functions

The following [Conversion](/csh?topicname=glang/conversion_functions.html) functions support the fixed-point data type:

- Boolean Array To Number
- Number To Boolean Array
- To Byte Integer
- To Double Precision Float
- To Extended Precision Float
- To Fixed-Point
- To Long Integer
- To Quad Integer
- To Single Precision Float
- To Unsigned Byte Integer
- To Unsigned Long Integer
- To Unsigned Quad Integer
- To Unsigned Word Integer
- To Word Integer

#### Data Manipulation Functions

The following [Data Manipulation](/csh?topicname=glang/data_manipulation_funct.html) functions support the fixed-point data type:

- Flatten To String
- Logical Shift
- Rotate Left With Carry
- Rotate Right With Carry
- Type Cast
- Unflatten From String

#### Fixed-Point Functions

The following [Fixed-Point](/csh?topicname=glang/fxp_fxns.html) functions are supported:

- Fixed-Point to Integer Cast
- Integer to Fixed-Point Cast

#### LabVIEW Schema Functions

The following [LabVIEW Schema](/csh?topicname=glang/xml_vis.html) functions support the fixed-point data type:

- Flatten To XML
- Unflatten From XML

#### Numeric Functions

The following [Numeric](/csh?topicname=glang/numeric_functions.html) functions support the fixed-point data type:

- Absolute Value
- Add
- Decrement
- Divide
- Increment
- Multiply
- Negate
- Reciprocal
- Round To Nearest
- Round Toward +Infinity
- Round Toward –Infinity
- Scale By Power Of 2 Function
- Sign
- Subtract
- Square
- Square Root

#### String/Number Conversion Functions

The following [String/Number Conversion](/csh?topicname=glang/string_numb_conver_func.html) functions support the fixed-point data type:

- Decimal String To Number
- Fract/Exp String To Number
- Hexadecimal String To Number
- Number To Decimal String
- Number To Engineering String
- Number To Exponential String
- Number To Fractional String
- Number To Hexadecimal String
- Number To Octal String
- Octal String To Number

#### Structures

The [Inline C Node](/csh?topicname=inlinecnode/inline_c_node.html) supports the fixed-point data type.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_clusters_function_prototype.html language=enus -->
## TOPIC 00014: Using Clusters in the Function Prototype (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_clusters_function_prototype.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_clusters_function_prototype.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Using Clusters in the Function Prototype (C Generator)

The LabVIEW C Generator represents clusters as structs, which are defined in the VINameLib.h file, where VIName is the name of the exported VI. The C Generator only supports flat clusters, which are clusters that contain only scalar values.

|  | Note The Parameters list of the Define VI Prototype dialog box does not display clusters that are not flat clusters. |
| --- | --- |

The following example shows a cluster control that contains a Boolean control and a numeric control:

[IMAGE alt='image' src='clustercgen.gif']

When the C Generator generates C code for the VI that contains the cluster shown in the previous example, the C Generator creates the following struct to represent the cluster:

typedef struct {

Boolean myBool;

float64 myDouble;

} TD1;

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_config_function_prototype.html language=enus -->
## TOPIC 00015: Configuring the Function Prototype (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_config_function_prototype.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_config_function_prototype.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Configuring the Function Prototype (C Generator)

Use the [Define VI Prototype](../lvcgenref/define_vi_prototype_cgen_db.html) dialog box to define the parameters for the [exported VI](cgen_dev_vis_cgen.html) for which you want to generate a C function interface. The LabVIEW C Generator generates a C function interface for the VI you specify in the C Code Generation build specification. The generated function converts the C-type parameters into C Generator data types. The generated function calls an internal function that implements the functionality of the exported VI. The generated function name is the same as the VI name unless the VI name contains a disallowed character, such as a space, in the file name. Underscores replace disallowed characters. The exported VI uses default data if any input or output terminal has an [unsupported data type](cgen_datatype_support.html).

The C Generator creates a header file that contains the function prototype for the exported VI. You can include this header file where the exported function is called. The header file has the same name as the exported VI appended with Lib.h.

The exported VI is more restrictive in terms of data type support than the rest of the VI hierarchy because the C Generator maps exported VI terminals to standard C data types. The C Generator supports the following data types for exported VIs:

- Strings
- Scalars, including Boolean, numeric, and fixed-point data types
- Arrays that contain only scalar values. For example, you cannot use an array of strings or an array of clusters.
- Flat clusters , which are clusters that contain only scalar values. For example, you cannot use a cluster that contains a string or an array.

The [execution behavior of the C code](cgen_execution_behavior.html) that the C Generator creates differs from the typical execution behavior of LabVIEW VIs running on Windows.

|  | Note Input strings to the function prototype must be null-terminated C strings. |
| --- | --- |

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_custom_platform_def.html language=enus -->
## TOPIC 00016: Customizing the Platform Definition File (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_custom_platform_def.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_custom_platform_def.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Customizing the Platform Definition File (C Generator)

LVDefs_plat.h contains basic constants and macros that the LabVIEW C Generator needs to generate C code. This file provides the mapping between generic C function calls that the C Generator generates and platform-specific, run-time functions. LVDefs_plat.h also contains platform definitions of data types for the compiler.

The C Generator includes an example LVDefs_plat.h file for several platforms. If you are using one of the example platforms, you can use the installed LVDefs_plat.h file for that platform instead of creating a new file. The LVDefs_plat.h files are located in platform-specific folders in the labview\CCodeGen\include\platform directory.

The example LVDefs_plat.h files include comments that explain what you must define for the platform. To properly define data types, you must know the compiler definitions of those data types. Refer to the documentation for the compiler to determine those values. To define the generic function calls, you must know how the target SDK implements these function calls. Refer to the SDK documentation for the target to define these function calls.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_datatype_support.html language=enus -->
## TOPIC 00017: Data Type Support (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_datatype_support.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_datatype_support.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Data Type Support (C Generator)

The following data types are supported in VIs you develop for C code generation, but not necessarily supported in the [exported function prototype](cgen_config_function_prototype.html):

- Arrays
- Booleans
- Complex single-precision, floating-point numerics (CSG)
- Complex double-precision, floating-point numerics (CDB)
- Complex extended-precision, floating-point numerics (CXT)
- Clusters
- Single-precision, floating point numerics
- Double-precision, floating-point numerics
- Enumerated types
- Fixed-point numerics
- Strings
- 8-bit, 16-bit, and 32-bit signed integers
- 64-bit signed and unsigned integers
- Timestamps
- 8-bit, 16-bit, and 32-bit unsigned integers
- Variants
- VI references
- Waveforms

The following data types are unsupported in VIs you develop for C code generation:

- Digital
- Dynamic
- Extended-precision floating-point numerics (EXT)
- LabVIEW classes
- Paths
- References except for VI references

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_debug_overridden_subvi.html language=enus -->
## TOPIC 00018: Debugging and Troubleshooting Overridden SubVIs (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_debug_overridden_subvi.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_debug_overridden_subvi.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Debugging and Troubleshooting Overridden SubVIs (C Generator)

If you [create a Funclist entry](cgen_override_subvi_calls_gen_code.html) and the generated C code is still generating the subVI call instead of the C function call, restart LabVIEW to reload the Funclist files. After you restart LabVIEW, verify the subVI name enclosed in the <VI Name> tags of the Funclist entry.

If compiler errors occur when you generate C code, verify the format of the C function call and the order of the parameters enclosed in the <Function> tags of the Funclist entry.

If compiler errors occur in LVFuncsUsed.h, verify that the <Feature> tags in the Funclist entry contain a valid C identifier.

|  | Note Funclist files contain minimal error reporting. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_define_cgen_options.html language=enus -->
## TOPIC 00019: Defining C Code Generation Options (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_define_cgen_options.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_define_cgen_options.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Defining C Code Generation Options (C Generator)

From a LabVIEW block diagram, the C Generator creates ANSI C code that you can compile on many targets. When you generate C code from an [exported VI](cgen_dev_vis_cgen.html), LabVIEW traverses the block diagram and generates simple C primitives if possible. For example, the C Generator converts While Loops to while() statements and converts the Add function to a simple C operation. However, a straight mapping is not possible for more complex functions so the C Generator uses the LabVIEW C Code Run-Time Library, which is analogous to the LabVIEW Run-Time Engine. The LabVIEW C Code Run-Time Library contains such things as data manipulation and math functions. The C Generator includes the source code for the LabVIEW C Code Run-Time Library.

You can use the [C Code Generation Settings](../lvcgenref/ccode_gen_settings_page.html) page of the [C Code Generation Properties](../lvcgenref/c_code_gen_properties_db.html) dialog box to specify C code generation settings and optimizations for all VIs in the hierarchy of the exported VI. You also can use the [Source File Settings](../lvcgenref/source_file_settings_ccode_gen_db.html) page of the **C Code Generation Properties** dialog box to specify individual C code generation options for each VI in the hierarchy of the exported VI.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_determine_endian_align.html language=enus -->
## TOPIC 00020: Determining Endianness and Alignment (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_determine_endian_align.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_determine_endian_align.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Determining Endianness and Alignment (C Generator)

Use the [C Code Generation Properties](../lvcgenref/c_code_gen_properties_db.html) dialog box to specify Endianness and alignment for the C code generated by the LabVIEW C Generator.

Endianness describes how the CPU stores or loads a multiple-byte number in memory. CPUs can use big-endian or little-endian form. Some CPUs can switch between being big-endian or little-endian form. Refer to the CPU documentation to determine endianness for the CPU.

|  | Tip You can use the htonl function, which converts any value to big-endian form, in a C application to determine endianness. The following example demonstrates the htonl function. |
| --- | --- |

if ( htonl(2010) == 2010 ) printf("Big Endian\n");

else printf("Little Endian\n");

Alignment describes restrictions on where CPUs can store or load numbers in memory. The C Generator requires the most restrictive alignment among all the data types that LabVIEW uses. [LVDefs_plat.h](cgen_custom_platform_def.html) defines these data types. Alignment differs based on the compiler you are using and the compiler options you specify to compile the C code. Refer to the compiler and CPU documentation to determine the correct alignment value. Most compilers provide an __alignof macro to determine the alignment of a data type.

|  | Tip You can create a union of all data types you reference in LVDefs_plat.h to determine the most restrictive alignment. The following example demonstrates the union you might create. |
| --- | --- |

union max_align_t {

char t0;

short t1;

int t2;

long t3;

long long t4;

void* t5;

float t6;

double t7;

}

printf("Alignment = %ul\n", __alignof(union max_align_t));

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_dev_vis_cgen.html language=enus -->
## TOPIC 00021: Developing VIs for C Code Generation (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_dev_vis_cgen.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_dev_vis_cgen.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Developing VIs for C Code Generation (C Generator)

Complete the following steps to develop a VI for C code generation.

1. Create a new LabVIEW project in the Project Explorer window.
2. Create the VI you want to export for C code generation under the My Computer target in the project. The exported VI must be under the My Computer target in order to generate C code for the VI.
 [IMAGE alt='image' src='note.gif']
**Note** You can export only one VI per [build specification](../lvcgenref/c_code_gen_properties_db.html) for C code generation.
3. As you develop the VI, account for differences in VIs developed to run as LabVIEW applications and VIs you develop for C code generation. Exported VIs and all VIs in their hierarchies support the following block diagram objects differently from VIs running as LabVIEW applications:
 
 [IMAGE alt='image' src='note.gif']
**Note** You cannot debug an exported VI in LabVIEW. Debug the generated C code in an external IDE.
  - Application Control VIs and functions
  - Express VIs
  - Data type support
  - Fixed-point data types
  - Libraries and executables
  - Memory Control functions
  - Numeric functions
  - Signal Processing VIs
  - String functions
  - Structures
  - Timing VIs and functions
  - Unsupported VIs and functions
  - Support for MathScript RT Module functions
4. On the Source Files page of the C Code Generation Properties dialog box, specify the VI you developed in the Exported VI listbox.

After you develop the VI for C code generation, you must [customize the platform definition file](cgen_custom_platform_def.html), [define C code generation options](cgen_define_cgen_options.html), and [configure the exported function prototype](cgen_config_function_prototype.html).

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_edit_makefiles.html language=enus -->
## TOPIC 00022: Editing Makefiles (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_edit_makefiles.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_edit_makefiles.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Editing Makefiles (C Generator)

To build the generated C code for a [specific target](cgen_build_gen_c_code_spec_targ.html), you must edit Makefile to customize compiler and linker options, dependencies, and build rules. By default, the C Generator creates a makefile for building a 32-bit Windows platform (Win32) DLL. To generate an application or library for a specific target, refer to the code comments in Makefile for instructions on customizing Makefile.

|  | Tip To open the directory containing the generated C files, including Makefile, right-click the C Code Generation build specification in the Project Explorer window and select Explore from the shortcut menu. |
| --- | --- |

Do not edit dependencies.mk because this file is overwritten automatically each time you generate C code.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_execution_behavior.html language=enus -->
## TOPIC 00023: Execution Behavior in Generated C Code (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_execution_behavior.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_execution_behavior.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Execution Behavior in Generated C Code (C Generator)

The execution behavior of the C code that the LabVIEW C Generator creates differs from the typical execution behavior of LabVIEW VIs running on Windows. LabVIEW VIs running on Windows use parallel execution behavior, while generated C code does not. For example in generated C code, parallel [While Loops](/csh?topicname=glang/while_loop.html) execute in sequence with one While Loop executing only after the other While Loop completely finishes. To avoid potential deadlock in the generated C code, ensure that the exported VI does not include parallel execution.

The C Generator generates C code for all VIs in the VI hierarchy as if all VIs are [subroutine priority VIs](/csh?topicname=lvconcepts/prioritizing_parallel_tasks.html). The main difference between the subroutine priority setting in the **VI Properties** dialog box and how the C Generator generates C code is that subroutine VIs running on Windows do not allow asynchronous functions. The C Generator converts asynchronous functions into synchronous functions and does not return to the caller until complete.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold.html language=enus -->
## TOPIC 00024: Expression Folding Patterns (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Patterns (C Generator)

LabVIEW uses expression folding patterns when you select the **Expression folding** build specification option.

The C Generator recognizes the following patterns when you [generate C code](cgen_gen_code_from_vis.html) from a VI:

- pattern 1
- pattern 2
- pattern 3
- pattern 4
- pattern 5
- pattern 6
- pattern 7
- pattern 8

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat1.html language=enus -->
## TOPIC 00025: Expression Folding Pattern 1 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat1.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat1.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 1 (C Generator)

Takes the pattern reference count-array index-primitive-array-replace and replaces it with a single array expression.

[IMAGE alt='image' src='expfold_pattern1.gif']

You must wire a value to all **index** inputs for the [Index Array](/csh?topicname=glang/index_array.html) function. You can only wire arrays that contain double-precision, floating-point numeric values or integer values to the **n-dimension array** input for the Index Array function.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat2.html language=enus -->
## TOPIC 00026: Expression Folding Pattern 2 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat2.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat2.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 2 (C Generator)

Takes the pattern left shift register-reference count-array index-right shift register and eliminates the reference count.

[IMAGE alt='image' src='expfold_pattern2.gif']

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat3.html language=enus -->
## TOPIC 00027: Expression Folding Pattern 3 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat3.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat3.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 3 (C Generator)

Takes the pattern global-reference count-array index-primitive-array replace-global and replaces it with an array expression directly on the global variable.

[IMAGE alt='image' src='expfold_pattern3.gif']

You must wire a value to all **index** inputs for the [Index Array](/csh?topicname=glang/index_array.html) function. You can only wire arrays that contain double-precision, floating-point numeric values or integer values to the **n-dimension array** input for the Index Array function.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat4.html language=enus -->
## TOPIC 00028: Expression Folding Pattern 4 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat4.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat4.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 4 (C Generator)

Takes the pattern global-reference count-array index-global and replaces it with an array index directly on the global variable.

[IMAGE alt='image' src='expfold_pattern4.gif']

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat5.html language=enus -->
## TOPIC 00029: Expression Folding Pattern 5 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat5.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat5.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 5 (C Generator)

Takes the pattern global-reference count-array replace-global and replaces it with an array replace directly on the global variable.

[IMAGE alt='image' src='expfold_pattern5.gif']

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat6.html language=enus -->
## TOPIC 00030: Expression Folding Pattern 6 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat6.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat6.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 6 (C Generator)

Folds function expressions for unary and binary operations into a single line of code and eliminates heap or stack variables. LabVIEW treats the [Quotient & Remainder](/csh?topicname=glang/quotient_and_remainder.html) function with integer inputs and only one output wired as a binary operation for this pattern. If the output wire of a function branches, LabVIEW cannot include the function in the folded expression because the intermediate value is needed.

You must turn off the guard code generation option for this pattern to work.

[IMAGE alt='image' src='expfold_pattern6.gif']

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat7.html language=enus -->
## TOPIC 00031: Expression Folding Pattern 7 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat7.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat7.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 7 (C Generator)

Folds expressions into a select statement and eliminates heap or stack variables.

[IMAGE alt='image' src='expfold_pattern7.gif']

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_expressfold_pat8.html language=enus -->
## TOPIC 00032: Expression Folding Pattern 8 (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_expressfold_pat8.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_expressfold_pat8.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Expression Folding Pattern 8 (C Generator)

Takes the pattern reference count-unbundle-bundle and eliminates reference counts and copies. This pattern works only if the elements unbundled and bundled are exactly the same.

[IMAGE alt='image' src='expfold_pattern8.gif']

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_gen_ccode_command_line.html language=enus -->
## TOPIC 00033: Generating C Code from the Command Line (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_gen_ccode_command_line.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_gen_ccode_command_line.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Generating C Code from the Command Line (C Generator)

You can use lvcg.exe from the command line to [generate C code](cgen_gen_code_from_vis.html). The lvcg utility is useful if you want to create a [makefile](cgen_build_gen_c_code_spec_targ.html) that regenerates C code when you modify the project. The output of the lvcg utility is the same as using a [C Code Generation build specification](../lvcgenref/c_code_gen_properties_db.html) to generate C code.

From the command line, enter the following commands to run the lvcg utility.

lvcg [-options] project pathbuild specification name

project path is the destination directory to save the generated C code. build specification name is the name of an existing C Code Generation build specification. You can use the -override-destination option to generate the C files in the current working directory instead of the destination directory specified in the build specification.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_gen_code_from_vis.html language=enus -->
## TOPIC 00034: Generating C Code from VIs (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_gen_code_from_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_gen_code_from_vis.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Generating C Code from VIs (C Generator)

After you [develop the VI for C code generation](cgen_dev_vis_cgen.html), [customize the platform definition file](cgen_custom_platform_def.html), [define C code generation options](cgen_define_cgen_options.html), and [configure the exported function prototype](cgen_config_function_prototype.html), you can generate C code from the exported VI. In the C Code Generation build specification, click the **Build** button to generate C code. You also can right-click the C Code Generation build specification in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window and select **Build** from the shortcut menu to generate C code.

The LabVIEW C Generator uses the options you specify in the [C Code Generation Properties](../lvcgenref/c_code_gen_properties_db.html) dialog box to generate C code from the block diagram. The C Generator generates each VI in the VI hierarchy into a separate C file using a C function name, which is more restrictive than a VI name. Any non-alphanumeric characters become underscores. If the VI name begins with a non-alphanumeric character, the C Generator prepends A_ to the beginning of the C function name.

Use the **Destination directory** option on the [Information](../lvcgenref/info_page_ccode_gen_db.html) page of the [C Code Generation Properties](../lvcgenref/c_code_gen_properties_db.html) dialog box to specify where to save the generated C files.

The C Generator generates the following files:

- *exportedVIname*.c , where exportedVIname , is the name of the VI you want to export as a C function. This file contains the exported function. You must include this file in the linker input list.
- *exportedVIname*Lib.h , where exportedVIname , is the name of the VI you want to export as a C function. This file contains the library interface that specifies the generated function you defined in the Define VI Prototype dialog box. You must include this file in the external application.
- *VIname*.c , where VIname is the name of a subVI in the hierarchy of the exported VI. You must include this file in the linker input list.
- LVForms.h contains declarations for the entry point functions for each VI. This file is required for compiling the generated C files.
- LVFuncsUsed.h contains usage information to support source-level dead-code stripping. This file is required for compiling the generated C files.
- LVGlobs.h contains declarations for global initialization functions and data type information used in an external application. This file is required for compiling the generated C files.
- Makefile is an example makefile . When you use the make command, the GNU Make utility reads this file. After the C Generator generates Makefile , the C Generator does not overwrite this file if you regenerate the C code. If you want to generate a new example Makefile , you must delete the file before regenerating the C code. 
 [IMAGE alt='image' src='note.gif']
**Note** LabVIEW code depends on the LabVIEW run-time library, which includes support for all basic functions. You must link to the LabVIEW run-time library with all exported VIs. The LabVIEW run-time library source is located in the labview\CCodeGen\libsrc directory. You also must link to the LabVIEW analysis library if the exported VI uses math or signal processing VIs. The LabVIEW analysis library source is located in the labview\CCodeGen\analysis directory. You also must link to the LabVIEW simulation library if the exported VI uses the Simulation VIs and functions. The LabVIEW simulation library source is located in the labview\CCodeGen\simulation.
- dependencies.mk is the secondary makefile. The C Generator includes all LabVIEW settings, such the build specification name and C code generation option values, that are required to generate C code. The C Generator updates this file if the hierarchy of the exported VI changes. LabVIEW also automatically overwrites this file during the build process.

DllMain.c, which is not created when the C Generator generates C code, is an example entry point for a DLL. This file is required for building DLLs that run on Windows. This file is located in the labview\CCodeGen\libsrc\platform\win directory.

|  | Tip To open the directory containing the generated C files, right-click the C Code Generation build specification in the Project Explorer window and select Explore from the shortcut menu. |
| --- | --- |

#### Removing Generated C Code

To delete all generated *.c and *.h files in the destination directory for an exported VI, right-click the C Code Generation build specification in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window and select **Clean** from the shortcut menu. The **Clean** option does not delete makefiles or built libraries.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_gsg.html language=enus -->
## TOPIC 00035: Getting Started with the LabVIEW C Generator

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_gsg.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_gsg.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Getting Started with the LabVIEW C Generator

The Getting Started with the NI LabVIEW C Generator manual contains a tutorial that guides you through creating a VI to export for C code generation, configuring C code generation settings, defining the function prototype for the exported VI, generating C code, and using the generated C code in an application. The tutorial also describes how to create and configure the generated C code so you can use it in different types of targets.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_include_gen_code_ext_apps.html language=enus -->
## TOPIC 00036: Including Generated C Code in External Applications (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_include_gen_code_ext_apps.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_include_gen_code_ext_apps.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Including Generated C Code in External Applications (C Generator)

If you have an existing [makefile](cgen_build_gen_c_code_spec_targ.html) or project you created in another IDE in which you want to include the [generated C code](cgen_gen_code_from_vis.html), you can use that makefile or project instead of the makefiles generated by the LabVIEW C Generator. You can include the generated C code in an external project in one of the following ways:

- Add the necessary files directly into the external project.
- Build the generated C code files into a static library, or archive file, and link the static library into the external project.
- Build the generated C code files into a DLL and load the DLL from the external project at run time.

Regardless of which method you choose to include the generated C code in the external project, you must compile the following files:

- All generated C files .
- Run-time library files from the labview\CCodeGen\libsrc\blockdiagram directory, which include the following files:
  - CCGArrSupport.c
  - CCGArrSupport2.c
  - CCGArrSupport3.c
  - CCGClusterSupport.c
  - CCGCmplxSupport.c
  - CCGDVRSupport.c
  - CCGEnumSupport.c
  - CCGFltSupport.c
  - CCGFXPSupport.c
  - CCGIntSupport.c
  - CCGStrSupport.c
  - CCGTimeSupport.c
  - CCGTokString.c
  - CCGUDClassSupport.c
  - CCGVariant.c
  - CCGXMLSupport.c
  - ExecStack.c
  - LVBlockDiagram.c
  - LVCGenRTInit.c
  - LVContext.c
  - LVHeap.c
  - LVTdp.c
  - MemCheck.c
  - nbemptybin.c
  - nbfifo.c
  - nbfifo_inst.c
  - nbitemtable.c
  - NumText.c
  - rtmath.c
  - ViLib.c
- The following files from the labview\CCodeGen\libsrc\comms :
  - CCGVIRefSupport.c
  - crc.c
- The following files from the labview\CCodeGen\libsrc\frontpanel :
  - LVArrayControl.c
  - LVBoolean.c
  - LVClusterControl.c
  - LVEnumCtl.c
  - LVFrontPanel.c
  - LVListbox.c
  - LVNumeric.c
  - LVRadioClustCtl.c
  - LVRing.c
  - LVScrollbar.c
  - LVString.c
  - LVTab.c
  - LVTable.c
  - LVTimestamp.c
  - LVTree.c
  - Pict.c
- Headless.c from the labview\CCodeGen\libsrc\os\common directory
- arrresize.c from the labview\CCodeGen\libsrc\analysis directory

You also must set the compiler options to include the following build specification output path directories in the header search paths:

- The directory in which you saved the generated C files. You specify this directory in the Destination directory option on the Information page of the C Code Generation Properties dialog box.
- labview\CCodeGen\include\blockdiagram
- labview\CCodeGen\include\comms
- labview\CCodeGen\include\frontpanel
- labview\CCodeGen\include\platform\*subdirectory* , where *subdirectory* is the platform you are using
- labview\CCodeGen\analysis\development\include
- labview\CCodeGen\analysis\LV\source\include

You also must build and link to the [analysis library](cgen_build_analysis_lib.html) if you use the [Mathematics](/csh?topicname=gmath/mathematics.html) or [Signal Processing](/csh?topicname=lvanls/signal_processing_vis.html) VIs in the exported VI.

|  | Tip You also can generate C code from the command line. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_include_os_specific_libs.html language=enus -->
## TOPIC 00037: Including Platform-Specific Libraries (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_include_os_specific_libs.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_include_os_specific_libs.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Including Platform-Specific Libraries (C Generator)

LVSysIncludes.h is a list of header files for a target platform. Depending on the target platform, LVSysIncludes.h contains platform-specific header files, toolchain-specific header files, and standard C header files. Most files in the labview\CCodeGen directory include LVSysIncludes.h.

You must choose which .h files from the target to include in LVSysIncludes.h. The C Generator includes an example LVSysIncludes.h file for several platforms. If you are using one of the example platforms, you can use the installed LVSysIncludes.h file for that platform instead of creating a new file. The LVSysIncludes.h files are located in platform-specific folders in the labview\CCodeGen\include\platform directory.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_lvcgenhelpdocinfo.html language=enus -->
## TOPIC 00038: C Generator

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_lvcgenhelpdocinfo.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_lvcgenhelpdocinfo.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### C Generator

June 2013, 373144C-01

Use the LabVIEW C Generator to generate generic C code from VIs. The generated C code can run on most platforms. The C code generation process includes the following steps.

1. Create a new LabVIEW project .
2. Develop the VI you want to export for C code generation under the My Computer target.
3. Test the exported VI in LabVIEW.
4. Customize the platform definition file for the target.
5. Create a C Code Generation build specification in the project and specify the VI to export.
 [IMAGE alt='image' src='note.gif']
**Note** The C Generator does not support [packed project libraries](/csh?topicname=lvconcepts/packed_libraries.html).
6. Configure the function prototype for the exported VI.
7. Specify C code generation options .
8. Build the C Code Generation project, which generates makefiles (.mk), .c files, and .h files .
9. Test the generated C code .
10. Directly include the C files in an external application or build the generated C files into a binary file that will run on the target.

© 2010–2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_mathscript_support.html language=enus -->
## TOPIC 00039: Support for MathScript RT Module Functions in VIs Developed for C Code Generation (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_mathscript_support.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_mathscript_support.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Support for MathScript RT Module Functions in VIs Developed for C Code Generation (C Generator)

**Requires:** C Generator *and* MathScript RT Module

You can use [MathScript Nodes](/csh?topicname=gmath/mathscript_node.html) with built-in [MathScript functions](/csh?topicname=lvtextmath/msfunc_classes.html) in exported VIs you [develop for C code generation](cgen_dev_vis_cgen.html). However, the C Generator does not support certain functions in exported VIs or supports some functions only under certain conditions.

|  | Note (Control Design and Simulation Module) If you use the Control Design and Simulation Module with the C Generator, additional Control Design MathScript RT Module functions are not supported. |
| --- | --- |

The C Generator does not support the following MathScript functions.

| Function | Class |
| --- | --- |
| addpath | support |
| ar_cov | modeling and prediction |
| ar_mcov | modeling and prediction |
| area | plots |
| axes | plots |
| axis | plots |
| balance | linalgebra |
| bar | plots |
| bar3d | plots |
| bar3dhoriz | plots |
| barhoriz | plots |
| beep | audio |
| break | programming |
| cd | support |
| clear | commands |
| clfig | plots |
| clgraph | plots |
| colormap | plots |
| colormapplot | plots |
| continue | programming |
| contour | plots |
| contour3d | plots |
| contouris | plots |
| date_to_num | time |
| date_to_str | time |
| date_to_vector | time |
| datescale | plots |
| delete | support |
| dir | support |
| dos | support |
| errorbar | plots |
| eval | basic |
| evalscript | basic |
| exist | membership |
| feather | plots |
| figure | plots |
| fileinfo | support |
| fill | plots |
| filternorm | linear systems |
| fir_lsq (differentiator mode not supported) | filter design |
| fwrite_xls | support |
| global | support |
| grid | plots |
| gsvd | linalgebra |
| help | support |
| iir_butter | filter design |
| image | plots |
| imagescaled | plots |
| int64 | support |
| is_dir | membership |
| is_global | membership |
| is_member | membership |
| lattice_to_tf | linear systems |
| legend | plots |
| line | plots |
| linearsolve | linalgebra |
| loaddialog | support |
| loglog | plots |
| lookfor | support |
| menu | support |
| mesh | plots |
| meshcontour | plots |
| mx_to_str | string |
| now | time |
| num_to_str | string |
| ode_adams | ode |
| ode_bdf15 | ode |
| ode_bdf23 | ode |
| ode_radau5 | ode |
| ode_rk23 | ode |
| ode_rk45 | ode |
| ode_rosen | ode |
| pareto | plots |
| path | support |
| pathdefault | support |
| pathremove | support |
| pause | commands |
| pie | plots |
| plot | plots |
| plot3d | plots |
| plotcoord | plots |
| plotf | plots |
| plotf_3d | plots |
| plotf_contour | plots |
| plotf_contouris | plots |
| plotf_mesh | plots |
| plotf_meshcontour | plots |
| plotf_polar | plots |
| plotf_surf | plots |
| plotf_surfcontour | plots |
| plotmatrix | plots |
| plottext | plots |
| plotyy | plots |
| polar | plots |
| polyeign | polynomials |
| quiver | plots |
| qz | linalgebra |
| ref_plotarea | plots |
| ref_plotwin | plots |
| regex | string |
| regex_i | string |
| regex_replace | string |
| regex_convert | string |
| return | programming |
| run | support |
| save | support |
| scatter | plots |
| scatter3d | plots |
| schur | linalgebra |
| selectdata | plots |
| semilog_x | plots |
| semilog_y | plots |
| showplot | plots |
| sound | audio |
| soundscaled | audio |
| sprintf | string |
| sscanf | string |
| stairs | plots |
| stem | plots |
| stem3d | plots |
| str_to_path | support |
| stripplot | plots |
| strread | string |
| subplot | plots |
| surface | plots |
| surfacecontour | plots |
| surfacenorm | plots |
| system | support |
| tempdir | support |
| tempname | support |
| text | plots |
| tf_to_lattice | linear systems |
| title | plots |
| titles | plots |
| treeplot | plots |
| uint64 | support |
| userpath | support |
| view | plots |
| voronoi | geometry |
| waitforbuttonpress | commands |
| waterfall | plots |
| wavplay | audio |
| wavread | audio |
| wavrecord | audio |
| wavwrite | audio |
| weekday | time |
| who | support |
| who_all | support |
| xlabel | plots |
| xlabels | plots |
| xlimit | plots |
| ylabel | plots |
| ylabels | plots |
| ylimit | plots |
| zlabel | plots |
| zlimit | plots |
| zoom | plots |
| zplane | filter design |

You can use the following MathScript functions in exported VIs only when you assign the output of the function to a variable. For example, the C Generator supports a = coherence(x, y) in exported VIs. However, the C Generator does not support coherence(x, y) because when you call the function without assigning the output to a variable, LabVIEW generates an output plot that the C Generator does not support. You can use these functions in exported VIs only if you assign the output of the function to a MathScript variable.

| Function | Class |
| --- | --- |
| coherence | spectral analysis |
| coherence_ms | spectral analysis |
| crosspsd | spectral analysis |
| crosssd | spectral analysis |
| cylinder | geometry |
| dimpulse | modeling and prediction |
| dlsim | modeling and prediction |
| dstep | modeling and prediction |
| ellipsoid | geometry |
| freqsd | filter design |
| freqzd | filter design |
| grpdelay | filter design |
| histogram | statistics |
| impzd | filter design |
| peakfcn2d | matrix |
| phasedelay | filter design |
| phasezd | filter design |
| psd | spectral analysis |
| psd_burg | spectral analysis |
| psd_covar | spectral analysis |
| psd_mcovar | spectral analysis |
| psd_periodogram | spectral analysis |
| psd_welch | spectral analysis |
| psd_yule | spectral analysis |
| pspec_eign | spectral analysis |
| pspec_music | spectral analysis |
| spectrogram | spectral analysis |
| sphere | geometry |
| stepzd | filter design |
| tf_estimate | spectral analysis |
| tf_estimateplot | spectral analysis |
| zerophase | filter design |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_override_subvi_calls_gen_code.html language=enus -->
## TOPIC 00040: Understanding Overridden SubVI Calls in Generated C Code (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_override_subvi_calls_gen_code.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_override_subvi_calls_gen_code.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Understanding Overridden SubVI Calls in Generated C Code (C Generator)

Funclist files are XML files that contain entries that enable you to override subVI calls with a fragment of C code. For example in C code generated by the LabVIEW C Generator, the [CCG Mem Peek 8](/csh?topicname=embsharedvi/ccg_peek_8.html) VI has an alternate implementation that makes direct calls to a C function. You can modify Funclist entries to provide an alternative implementation for VIs that ship with LabVIEW or VIs you create. Funclist files are useful when you wrap high-performance, target-specific C function calls into subVIs. Creating subVI wrappers provide a better experience in LabVIEW so you can have the ease of use of LabVIEW and the performance of an optimized C function call.

|  | Caution Funclist entries have specific formatting requirements and contain little error checking. If the formatting is incorrect, compiler errors occur, and LabVIEW might crash when you generate C code. |
| --- | --- |

Funclist files contain lines, or Funclist entries, that describe how to replace a subVI call in the generated
C code with a fragment of C code. These code fragments can be anything, but they are usually C function calls. The C Generator includes Funclist files for some VIs that ship with LabVIEW in the labview\CCodeGen\Funclist directory. For example, Memory Access.xml contains Funclist entries for the [Memory Access](/csh?topicname=embsharedvi/emb_memaccess_pal.html) VIs. If you create a Funclist file for VIs you create, you must include that Funclist file in the labview\CCodeGen\Funclist directory.

Each Funclist entry must contain the <VI Name>, <Function>, and <Features> tags. The following example shows the Funclist entry for the CCG Mem Peek 8 VI:

<VI Override>

<VI Name>CCG_Mem_Peek_8<‌/VI Name>

<Function>@CCG_Mem_Peek_8( @i2, @i1(0), @o3, @o2, @o1 );<‌/Function>

<Feature>CGenMemPeek<‌/Feature>

<VI Override>

#### <VI Name>

The <VI Name> tags contain the name of the VI you are overriding. In the Funclist entry, you must change the VI name in the following ways:

- Convert spaces to underscores.
- If the VI begins with an underscore, prepend A__ to the VI name.

#### <Function>

The <Function> tags contain the line of C code that replaces the subVI call. If you call a C function, the <Function> tags contain the function parameters.

You must pass the function parameters directly. When you pass parameters, you must do the following things in the Funclist entry:

- Place an @ character at the beginning of the line of C code.
- Use a format code in the form @ xn to access the subVI inputs and outputs. x represents a character that determines if the parameter is an input or output and the way the C Generator passes the parameter. 
For x , use the following characters to indicate how the C Generator passes the parameter:
 
 n is the number of the input or output on the connector pane. The numbering on the connector pane is not intuitive. You might have to use trial and error to find the correct number.
  - I is an input passed by reference.
  - i is an input passed by value.
  - o is an output passed by reference.
  - it is the type of input.
- Place a value in parentheses after a format code to specify a default, or unwired, value for the input.
For example, if you want to pass input 3 by reference with Null as the default value, the syntax is
 @I3(Null) .

#### <Feature>

The <Features> tags contain a string that describes the feature you are overriding. You can use any string in the <Feature> tags as long as the string is a valid C identifier and the string is unique to the other <Feature> strings in the Funclist file.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_related_docs.html language=enus -->
## TOPIC 00041: Related Documentation (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_related_docs.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_related_docs.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Related Documentation (C Generator)

The following documents contain information that you might find helpful as you use the LabVIEW C Generator:

- Getting Started with the NI LabVIEW C Generator—This manual contains a tutorial that guides you through creating a VI to export for C code generation, configuring C code generation settings, defining the function prototype for the exported VI, generating C code, and using the generated C code in an application. The tutorial also describes how to create and configure the generated C code so you can use it in different types of targets.
- LabVIEW C Generator Readme —Use this file to learn important last-minute information about the C Generator, including known issues. Open the readme file by selecting Start»All Programs»National Instruments»LabVIEW»Readme and opening readme_CGenerator.html .
- C Generator Examples—Use the C Generator examples as a starting point for developing VIs to export for C code generation. You can modify an example, or you can copy and paste from one or more examples into a VI that you create. Use the NI Example Finder, available by selecting Help»Find Examples , to browse or search the example VIs. You also can browse the examples by navigating to the labview\examples\CGenerator directory.
- Additional LabVIEW documentation .

Refer to the National Instruments Product Manuals Library for updated documentation resources.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_run_makefiles.html language=enus -->
## TOPIC 00042: Running Makefiles (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_run_makefiles.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_run_makefiles.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Running Makefiles (C Generator)

After you [edit](cgen_edit_makefiles.html) the Makefile for a [specific target](cgen_build_gen_c_code_spec_targ.html) and [setup the toolchain](cgen_build_gen_c_code_spec_targ.html), you can run the GNU Make for Windows utility. Call the make command from the command line to run the GNU Make utility on Makefile.

Refer to the Make for Windows Web site at http://gnuwin32.sourceforge.net/packages/make.htm for more information about running the GNU Make utility.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_signal_naming_conventions.html language=enus -->
## TOPIC 00043: Signal Naming Convention (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_signal_naming_conventions.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_signal_naming_conventions.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Signal Naming Convention (C Generator)

The LabVIEW C Generator generates C-style source code comments and variable names from the labels on the block diagram. Underscores ( _ ) replace special characters and spaces.

Use VarNames.vi, located in the labview\CCodeGen directory, to set the maximum size of variable names, data type prefix strings, and tunnel name abbreviation strings.

|  | Tip Keep prefix names and tunnel abbreviation strings short to make comments more readable and to avoid truncated variable names or comments. |
| --- | --- |

The following table shows the LabVIEW signal source and corresponding generated C variable name and comment.

| LabVIEW Signal Source | Attributes Used | Block Diagram Example | Generated C Variable Name | Generated C Comment |
| --- | --- | --- | --- | --- |
| Front panel control | Label |  | Motor_On | /* Motor On */ |
| Constant | Label |  | Trigger_Level | /* Trigger Level */ |
| Function | Label, terminal name |  | Over_Voltage_x_y__ | /* Over Voltage: x > y?*/ |
| Loop tunnel | Source name, “LT” |  | Trigger_Level_LT | /* Trigger Level: Loop Tunnel */ |
| Case selector | Source name, “CS” |  | Relay_CS | /* Relay: Case Selector */ |
| Case tunnel | Structure label, “CT” |  | My_Structure_CT | /* My Structure: CT */ |
| Shift register (initialized) | Source name, “SR” |  | Init_SR, Init_SR_1 | /* Init: SR */, /* Init: SR 1 */ |
| Shift register (uninitialized) | Source name, “SR” |  | Foo_Loop_SR, Foo_Loop_SR_1, Foo_Loop_SR_2 | /* Foo Loop: SR */, /* Foo Loop: SR 1 */, /* Foo Loop: SR 2 */ |
| Sequence Local | Source name, “SL” |  | Init_SL | /* Init: Sequence local */ |
| Sequence tunnel | Source name, “ST” |  | Level_Y_ST | /* Level Y: ST */ |
| Structure terminal | Label, terminal name |  | Wave_Loop_i | /* Wave Loop: i */ |
| Local variable | Label, local variable name |  | Motor_Control | /* Motor Control */ |
| Global variable | Label, global variable name |  | sensors_Temp_1 | /* sensors: Temp 1 */ |
| User VI | Label, terminal name |  | Filter_Analog | /* Filter: Analog */ |

|  | Note Generated variables must be unique. If multiple variables have identical names, the C Generator appends a sequential number to the end of the variable name to make the name unique. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_testing_gen_c_code.html language=enus -->
## TOPIC 00044: Testing and Troubleshooting Generated C Code (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_testing_gen_c_code.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_testing_gen_c_code.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Testing and Troubleshooting Generated C Code (C Generator)

National Instruments recommends you test the [exported VI](cgen_dev_vis_cgen.html) before [generating C code](cgen_gen_code_from_vis.html) and test generated C code before you use it externally. You can test the exported VI in LabVIEW to simulate the behavior of the generated C code.

|  | Note You cannot debug an exported VI in LabVIEW. Debug the generated C code in an external IDE. |
| --- | --- |

You might encounter the following issues when generating C code:

- The C Generator supports some block diagram objects differently in exported VIs and all VIs in their hierarchy.
- The exported VI cannot contain parallel code .
- The C Generator cannot generate C code for a VI that is not under the My Computer target in the project.
- The C Generator cannot generate C code if the exported VI hierarchy contains unsupported data types , VIs, functions, or structures .

The C Generator includes syntax checking of the exported VI. When you create a [C Code Generation build specification](../lvcgenref/c_code_gen_properties_db.html), the C Generator enables syntax checking for the exported VI. When LabVIEW checks the syntax of the VI for which you want to generate C code, LabVIEW is checking that the C Generator can create generic C code based on the design of the exported VI. LabVIEW always checks the syntax of the exported VI before it builds the VI.

If the exported VI contains a syntax error, the LabVIEW toolbar displays the **Warning** button, which is shown as follows.

[IMAGE alt='image' src='noloc_env_warnbtn.gif']

|  | Note If you remove the checkmark from the Show Warnings checkbox in the Error list window, LabVIEW no longer displays syntax warnings for C code generation. If you disable warnings, you can check the syntax of the exported VI by right-clicking the C Code Generation build specification in the Project Explorer window and selecting Check Syntax from the shortcut menu. |
| --- | --- |

LabVIEW displays the **Warning** button during syntax checking if the exported VI hierarchy contains unsupported data types, VIs, functions, or structures. While syntax warnings do not prevent you from running the exported VI in LabVIEW, you cannot generate C code for the VI until you correct all syntax warnings. To locate a specific error on the block diagram, double-click the error description in the [Error list](/csh?topicname=lvdialog/error_list_dialog_box.html) window to highlight the error on the block diagram.

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_unsupported_vis.html language=enus -->
## TOPIC 00045: Unsupported VIs and Functions (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_unsupported_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_unsupported_vis.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Unsupported VIs and Functions (C Generator)

The following VIs and functions are unsupported:

- Cast Unit Bases function
- Connectivity VIs and functions except for the Call Library Function Node
- Convert Unit function
- CPU Information functions
- Data Communication VIs and functions except for the First Call? function, global variables , and local variables
- Dialog & User Interface VIs and functions except for Clear Errors , Error Cluster From Error Code , Find First Error, and Merge Errors
- File I/O VIs and functions
- Get Drag Drop Data function
- Get Waveform Attribute function
- Graphics & Sound VIs
- Instrument I/O VIs and functions
- Invoke Node
- LabVIEW classes
- Measurement I/O VIs and functions
- Notifier Operations functions
- Occurrences functions
- Open Application Reference function
- Palette Editing VIs
- Property Node
- Queue Operations functions
- Quit LabVIEW function
- Report Generation VIs
- Set Waveform Attribute function
- Stop function
- Timed Structures and VIs
- Timing VIs and functions except the To Time Stamp and Format Date/Time String functions
- VI Scripting VI and functions

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenhelp/cgen_using_gen_c_code.html language=enus -->
## TOPIC 00046: Using Generated C Code (C Generator)

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenhelp/cgen_using_gen_c_code.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenhelp/cgen_using_gen_c_code.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### Using Generated C Code (C Generator)

After you [generate C code](cgen_gen_code_from_vis.html) from an exported VI, you can use the C files in the following ways:

- Directly include the C files in an external application
- Build the generated C files into a binary file that runs on the target

|  | Note National Instruments recommends you test the generated C code before you use it externally. |
| --- | --- |

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-c-generator-module path=lvcgenref/cgen_pal.html language=enus -->
## TOPIC 00047: C Generator VIs

- bundle_id: `labview-c-generator-module`
- source_path: `lvcgenref/cgen_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-c-generator-module/raw/resource/enus/lvcgenref/cgen_pal.html
- document_id: `labview-c-generator-module`
- page_type: `leaf`
- content_type: ``

### C Generator VIs

**Requires:** C Generator. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the C Generator VIs to [generate generic C code](../lvcgenhelp/cgen_lvcgenhelpdocinfo.html) from VIs.

| Palette Object | Description |
| --- | --- |
| Inline C Node | Adds C code or assembly code to the block diagram. |

| Subpalette | Description |
| --- | --- |
| Memory Access VIs | Use the Memory Access VIs to read and write values to specific memory address locations. |
| Real-Time FIFO VIs | Use the Real-Time FIFO VIs to transfer data between VIs in an application. An RT FIFO acts like a fixed queue, where the first value you write to the FIFO is the first value that you can read from the FIFO. |

©2010–2013 National Instruments. All rights reserved.
