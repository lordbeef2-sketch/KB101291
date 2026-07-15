# NI DOCUMENT BUNDLE: labview-nxg-fpga-module-designing-application

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-fpga-module-designing-application start=1 end=2 -->
<!--NI_TOPIC bundle=labview-nxg-fpga-module-designing-application path=Chunk42600358.html language=enus -->
## TOPIC 00001: Map

- bundle_id: `labview-nxg-fpga-module-designing-application`
- source_path: `Chunk42600358.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-designing-application/raw/resource/enus/Chunk42600358.html
- document_id: `labview-nxg-fpga-module-designing-application`
- page_type: `leaf`
- content_type: `topic`
- source_description: FPGA Design Flow Create an application, integrate the application into your system for use with hardware, and deploy the application to an FPGA all within a single development environment. The FPGA design flow consists of the following phases: Creating and Testing FPGA Code—Create, test, and impleme

Map

#### FPGA Design Flow

Create an application, integrate the application into your system for use with hardware, and deploy the application to an FPGA all within a single development environment.

The FPGA design flow consists of the following phases:

1. Creating and Testing FPGA Code —Create, test, and implement the components you need to complete your system before you deploy.
2. Deploying and Debugging Applications —Compile, debug, and deploy your application to hardware.

##### Deploying and Debugging Applications

When your application is complete and functions as you expect when you test it, you are ready to compile and deploy the application to an FPGA. 
 Compilation involves configuring and building a bitfile for your top-level FPGA VI. Deployment involves downloading the bitfile to an FPGA and running the bitfile.

If an error occurs during compilation or your application doesn't run properly after you deploy it to the FPGA, you must debug the application to resolve the issues.

The following resources provide information to help you deploy and debug your application.

- Execution of FPGA Code — You can run FPGA code on the FPGA directly or you can run the code on the host computer to simulate running it on the FPGA. Simulating FPGA code on the host computer helps you identify and resolve errors in your application before you run FPGA code on the FPGA directly.
- Compiling FPGA Code — To run code on an FPGA, you must compile the FPGA code into a bitfile that you then deploy to the FPGA. The bitfile contains binary data that describes how to configure the FPGA circuit so that it performs the same function as the code in the FPGA VI.
- Downloading and Running an FPGA VI —After you successfully compile a bitfile without errors, download the bitfile to the FPGA and run the application. Use the FPGA Host Interface nodes to download, run, and communicate with code on the FPGA.
- Debugging a Deployed Application—If your application doesn't run properly after you deploy it to the FPGA, debug your undeployed application and compile a new bitfile. Make sure your application runs within the constraints of your hardware. Search for your hardware device within this manual to locate specifications and data sheets for your device. The capabilities of your hardware determine how best to develop and implement your application.

Related concepts:

- FPGA Design Flow

<!--NI_TOPIC bundle=labview-nxg-fpga-module-designing-application path=system-integration.html language=enus -->
## TOPIC 00002: Creating and Testing FPGA Code

- bundle_id: `labview-nxg-fpga-module-designing-application`
- source_path: `system-integration.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-fpga-module-designing-application/raw/resource/enus/system-integration.html
- document_id: `labview-nxg-fpga-module-designing-application`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create your FPGA code, move the design to the FPGA in SystemDesigner, call it from your FPGA application, test the system components and the overall system, and make any necessary adjustments to meet the specifications of your hardware device. Creating and Integrating FPGA Code FPGA VIs serve as the

Creating and Testing FPGA Code

Create your FPGA code, move the design to the FPGA in SystemDesigner, call it from your FPGA application, test the system components and the overall system, and make any necessary adjustments to meet the specifications of your hardware device.

#### Creating and Integrating FPGA Code

FPGA VIs serve as the container for all code that runs on an FPGA, so when you integrate the FPGA code, you integrate it into an FPGA VI or into a Clock-Driven Logic document called from an FPGA VI. 
 
 Designate a top-level FPGA VI within an Application document (.gcomp) that represents a bitfile. The top-level FPGA VI serves as the container for your overall FPGA application. Place all of the code that makes up your FPGA application either directly on the diagram of the FPGA VI, or within subdocuments located on the diagram of the FPGA VI. This code can include Clock-Driven Logic. If you are using a project template, the FPGA VI that you add your design to may be one of the VIs in the project template.

The following resources provide information to help you integrate the pieces of your system.

- Use a Project Template— Project templates provide common application architectures using well-established industry design patterns that you can modify to quickly build a working system. When you are ready to integrate your design into an FPGA application, consider adding your design to a project template.
- Language Integration in LabVIEW— You can use multiple programming languages to develop your application. How you integrate pieces of code written in different languages into your overall application depends on the language and the target you are integrating the code into.
- Clock-Driven Logic —Clock-Driven Logic is the primary language on the FPGA. Clock-Driven Logic allows you to integrate the pieces of your application and communicate with system resources.
- Using Handshaking to Ensure Valid Data in a Clock-Driven Loop —When you integrate code into Clock-Driven Logic, use a handshaking protocol to ensure valid data transfers to and from code that requires more than one clock cycle to return valid data.

#### System and Component Testing

Testing and adjusting your system components before integrating into your system saves you time and effort when you test your entire system.

Component testing allows you to ensure that each component, or complex portion of code that relies on the timing of the system, works as you expect and reduces the amount of troubleshooting your application requires at the system level. System testing helps you identify any necessary adjustments you need to make to ensure your system runs properly.

The following resources provide information to help you test your system and its components.

- Strategies for Testing FPGA Applications —Use these strategies to identify and test your system and its components.
- Testing a Clock-Driven Logic Document on the Host —To test that a
 Clock-Driven Logic (CDL) document processes data as you expect, use the
 Run GCDL Simulation node in a testbench to simulate running
 the CDL document on an FPGA.
- Testing Communication between the Host VI and an FPGA VI —To ensure your system application will run as you expect it to on an FPGA, use the FPGA Host Interface nodes in a testbench to simulate how your code will run on an FPGA.

Related concepts:

- FPGA Design Flow
