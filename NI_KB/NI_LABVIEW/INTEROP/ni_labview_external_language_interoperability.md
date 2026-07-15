# NI_LABVIEW_EXTERNAL_LANGUAGE_INTEROPERABILITY

<!--SYSTEM_CORPUS id=NI_LABVIEW_LANGUAGE_INTEROP generated=2026-07-14T12:02:18+00:00 -->
- source: https://www.ni.com/en/shop/labview/using-python-matlab-and-c-with-labview.html
- source_sha256: 81b086409af051f064bddde8f4d54d249db48f24ccaa7e2bda5fcaf200394ec6
- surfaces: Python|MATLAB|C|C++|DLL|shared-library|.NET|C#|ActiveX|COM|CLI|external-process

## Using Python, MathWorks® MATLAB® Software, and C/C++ with LabVIEW

## Overview

LabVIEW’s connectivity to other programming languages is an attractive feature for engineers building test systems. Integrating languages, such as Python, MathWorks MATLAB software, C/C++, and .NET into LabVIEW’s graphical data flow combines the best of each language to create a flexible test system built in less time.

In this white paper, learn how to integrate code from four popular programming technologies with LabVIEW. This flexibility means that you’re always able to select the right tool for the job and succeed faster.

## Contents

- Call Python Scripts from LabVIEW

- Integrate LabVIEW and MathWorks MATLAB Software

- Call C/C++ DLLs in LabVIEW

- Call .NET Assemblies in LabVIEW

- Conclusion

- Next Steps

Over the years, Python has grown in popularity and expanded to offer hundreds of thousands of libraries for a wide spectrum of applications. Incorporating Python into LabVIEW merges the flexible scripting capabilities of Python with the system design tools in LabVIEW.

With the Python Node, LabVIEW provides a native ability to call a Python script from a LabVIEW Block Diagram. This feature allows for interoperability between the languages with low latency.

Figure 1: Integrate Python scripts in LabVIEW by calling them with Python Node.

In the Python Node, you can specify which version to use and the path to Python when calling functions, which allows access to Python installed in custom directories. This capability means that you can use multiple Python Nodes to open multiple sessions of different versions or executables stored in custom directories.

LabVIEW 2022 Q3 added support for passing Python class objects as parameters. The refnum output on the Python Node represents a Python class object, which you can then pass as an input to another Python Node to act on the class object.

.

Figure 2: LabVIEW 2022 supports passing of Python class objects as parameters.

LabVIEW 2023 Q1 adds a new function for calling Python virtual environments with Anaconda and Venv.

NI is continuously investing in improving the Python-LabVIEW interoperability, with updates planned through 2023 and beyond. You can learn more about what’s new in LabVIEW and our future plans on our LabVIEW overview page.

Common programming approaches for numeric analysis, signal processing, and advanced mathematics can be used to call .m files developed in MATLAB. By combining these files in a VI with G using the MATLAB Node, MATLAB analysis capabilities can integrate your test and measurement system.

Figure 3: Integrate .m files into LabVIEW by calling them with Call MATLAB Function from the MATLAB Node.

Additionally, LabVIEW now allows users to select specific MATLAB versions for execution.

Figure 4: With MATLAB Node, select a specific MATLAB version for execution.

New debugging capabilities are available starting with LabVIEW 2022 Q3. You can add breakpoints in your MATLAB editor, debug your code by single-stepping from LabVIEW into your .m file, and launch your MATLAB IDE from LabVIEW to edit your .m file on the go.

Figure 5: Use LabVIEW’s debugging tools to step into your .m file and debug from LabVIEW.

With LabVIEW, you can reuse existing code by calling dynamic link libraries (DLLs) or shared libraries.

For instance, if you need to reuse an existing C/C++ shared library in LabVIEW, you can call it using the Call Library Function Node. To make importing external libraries simple, LabVIEW also includes the Import Shared Library Wizard. This wizard automatically creates or updates a LabVIEW wrapper VI project library that you can incorporate into your LabVIEW block diagram.

Figure 6: Use the Call Library Function Node to reuse existing C or C++ shared libraries in-line with G programming.

Another way to reuse existing code with LabVIEW is by calling .NET assemblies.

To access a .NET assembly, use the Constructor Node. When it is placed on the block diagram, a dialog window appears, allowing the user to select the appropriate .NET assembly. LabVIEW automatically recognizes all methods and properties and exposes these through the Method and Property Nodes.

Figure 7: Create a reference to the .NET assembly using the .NET Constructor Node function. Then, pass the reference to Property or Invoke Node functions, so the functions know which assembly they are operating on.

LabVIEW can load .NET assemblies that target the .NET CLR 4.0 or earlier. However, LabVIEW loads all assemblies in the .NET CLR 4.0.

We have covered four ways to connect to popular languages with LabVIEW, highlighting its flexibility and interoperability. This connectivity helps you seamlessly combine the best of each tool to create flexible test systems, faster.

- Explore your LabVIEW purchase options

- Learn more about using Python with LabVIEW

- Learn more about calling DLLs from LabVIEW

- Learn more about using .NET with LabVIEW

MathWorks® and MATLAB® are registered trademarks of The MathWorks, Inc.
